const ip = 'http://159.69.85.34:8001';
const axios = require('axios');

export async function uploadFile (audioFile) {
    let data = new FormData();
    data.append('mp3', audioFile);
    // return await axios.get(ip + '/get_image_stft', {
    //       responseType: 'blob',
    //     })
    return await axios.post(ip + '/image_stft', data, {
        headers: {
          'Content-Type': 'multipart/form-data'
        },
        responseType: 'blob',
      })
        .then(response => {
            const url = window.URL.createObjectURL(new Blob([response.data], {
              type: response.headers['content-type'],
            }))
            return url

        })
        .catch(error => {
            console.log(error);
            return error;
        });
}

let api = {
    uploadFile
};

export default api;

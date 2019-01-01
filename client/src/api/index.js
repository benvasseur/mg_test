
import axios from 'axios';

const BASE_URL = 'http://127.0.0.1:8000'

const api = {
    login(credentials) {
        return axios.post(`${BASE_URL}/api/auth/login`, credentials);
    },
    register(data) {
        return axios.post(`${BASE_URL}/api/auth/register`, data);
    },
    update(id, data) {
        return axios.put(`${BASE_URL}/api/users/${id}`, data);
    },
    updateProfilePic(id, data) {
        return axios.put(`${BASE_URL}/api/users/picture/${id}`, data, {
            headers: {
            //   'Content-Type': 'multipart/form-data'
              'Content-Type': 'application/x-www-form-urlencoded'
            }
        });
    }
}

export default api
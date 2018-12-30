
import axios from 'axios';

const BASE_URL = 'http://127.0.0.1:8001'

const api = {
    login(credentials) {
        return axios.post(`${BASE_URL}/api/auth/login`, credentials);
    },
    register(data) {
        return axios.post(`${BASE_URL}/api/auth/register`, data);
    },
    update(id, data) {
        return axios.put(`${BASE_URL}/api/users/${id}`, data);
    }
}

export default api
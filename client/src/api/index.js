
import axios from 'axios';

const api = {
    login(credentials) {
        return axios.post('http://127.0.0.1:8000/api/rest-auth/login/', credentials);
    }
}

export default api
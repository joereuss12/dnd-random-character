// src/apiService.js
import axios from 'axios';

export const generateCharacter = async (specifications) => {
    try {
        const resp = await axios.post('http://localhost:5000/generate', specifications);
        return resp.data;
    } catch (error) {
        console.error('Error generating character:', error);
        throw error;
    }
};
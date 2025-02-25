import axios from "axios";

const API_URL = "http://127.0.0.1:8000/api/auth/";

export const registerUser = async (userData) => {
  return axios.post(`${API_URL}register/`, userData);
};

export const loginUser = async (credentials) => {
  return axios.post(`${API_URL}login/`, credentials);
};

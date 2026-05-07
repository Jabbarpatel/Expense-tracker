import axios from "axios";

const IS_DEV: boolean = true;
const BACKEND_PORT: number = 80;

const API_URL: string = IS_DEV
  ? `${window.location.origin.replace(/:\d+?$/, "")}:${BACKEND_PORT}/api`
  : `${window.location.origin}/api`;

export const customApi = axios.create({
  baseURL: API_URL,
  headers: { "Content-Type": "application/json" },
});

customApi.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");

  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  } else {
    config.headers.Authorization = "";
  }
  return config;
});

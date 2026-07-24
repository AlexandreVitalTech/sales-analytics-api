// URL base da API FastAPI. Se o backend rodar em outra porta/host, ajuste aqui.
export const API_BASE_URL = "http://127.0.0.1:8000";

async function get(endpoint) {
  const res = await fetch(`${API_BASE_URL}${endpoint}`);
  if (!res.ok) {
    throw new Error(`Falha ao buscar ${endpoint}: ${res.status}`);
  }
  return res.json();
}

export function fetchTotal() {
  return get("/total");
}

export function fetchTicket() {
  return get("/ticket");
}

export function fetchCategoria() {
  return get("/categoria");
}

export function fetchCidade() {
  return get("/cidade");
}

export function fetchExtMax() {
  return get("/ext_max");
}

export function fetchExtMin() {
  return get("/ext_min");
}

export function fetchCanal() {
  return get("/canal");
}

export function fetchPagamento() {
  return get("/pagamento");
}

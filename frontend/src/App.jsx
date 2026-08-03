import { useEffect, useState } from "react";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  Cell,
  PieChart,
  Pie,
  Legend,
} from "recharts";
import {
  fetchTotal,
  fetchTicket,
  fetchCategoria,
  fetchCidade,
  fetchExtMax,
  fetchExtMin,
  fetchCanal,
  fetchPagamento,
} from "./api";
import "./App.css";

const CATEGORIA_COLORS = ["#3b4b8c", "#1f8a70", "#c98a2c", "#8c5a3b", "#a8412f"];
const CIDADE_COLOR = "#3b4b8c";
const CANAL_COLORS = { Loja: "#23261f", Online: "#8c5a3b" };
const PAGAMENTO_COLORS = { Cartão: "#3b4b8c", Pix: "#1f8a70", Boleto: "#c98a2c" };

function toChartArray(obj = {}) {
  return Object.entries(obj).map(([name, value]) => ({ name, value }));
}

function formatBRL(valor) {
  return valor?.toLocaleString("pt-BR", { style: "currency", currency: "BRL" });
}

function nomesProduto(obj = {}) {
  const nomes = Object.keys(obj);
  if (nomes.length === 0) return "—";
  if (nomes.length === 1) return nomes[0];
  return `${nomes[0]} +${nomes.length - 1}`;
}

function ChartCard({ title, note, children }) {
  return (
    <div className="chart-card">
      <h2>{title}</h2>
      {note && <p className="chart-note">{note}</p>}
      <ResponsiveContainer width="100%" height={260}>
        {children}
      </ResponsiveContainer>
    </div>
  );
}

export default function App() {
  const [dados, setDados] = useState(null);
  const [erro, setErro] = useState(null);

  useEffect(() => {
    async function carregarTudo() {
      try {
        const [total, ticket, categoria, cidade, extMax, extMin, canal, pagamento] =
          await Promise.all([
            fetchTotal(),
            fetchTicket(),
            fetchCategoria(),
            fetchCidade(),
            fetchExtMax(),
            fetchExtMin(),
            fetchCanal(),
            fetchPagamento(),
          ]);
        setDados({ total, ticket, categoria, cidade, extMax, extMin, canal, pagamento });
      } catch (e) {
        setErro(e.message);
      }
    }
    carregarTudo();
  }, []);

  if (erro) {
    return (
      <div className="dashboard">
        <p className="state-msg error">
          Não foi possível conectar à API ({erro}). Confirme que o backend está
          rodando em http://127.0.0.1:8000.
        </p>
      </div>
    );
  }

  if (!dados) {
    return (
      <div className="dashboard">
        <p className="state-msg">Carregando dados de vendas…</p>
      </div>
    );
  }

  const categoriaData = toChartArray(dados.categoria);
  const cidadeData = toChartArray(dados.cidade).sort((a, b) => b.value - a.value);
  const canalData = toChartArray(dados.canal);
  const pagamentoData = toChartArray(dados.pagamento);

  return (
    <div className="dashboard">
      <div className="dashboard-header">
        <h1>Painel de Vendas</h1>
      </div>

      <div className="receipt">
        <div className="receipt-title">Resumo geral</div>
        <div className="receipt-grid">
          <div className="receipt-item">
            <div className="label">Total de vendas</div>
            <div className="value">{formatBRL(dados.total.total_vendas)}</div>
          </div>
          <div className="receipt-item">
            <div className="label">Ticket médio</div>
            <div className="value">{formatBRL(dados.ticket.ticket_medio)}</div>
          </div>
          <div className="receipt-item">
            <div className="label">Mais vendido</div>
            <div className="value small">{nomesProduto(dados.extMax)}</div>
          </div>
          <div className="receipt-item">
            <div className="label">Menos vendido</div>
            <div className="value small">{nomesProduto(dados.extMin)}</div>
          </div>
        </div>
      </div>

      <div className="charts-grid">
        <ChartCard title="Vendas por categoria" note="Quantidade de itens vendidos">
          <BarChart data={categoriaData}>
            <CartesianGrid strokeDasharray="3 3" stroke="var(--line)" vertical={false} />
            <XAxis dataKey="name" tick={{ fontSize: 12 }} />
            <YAxis tick={{ fontSize: 12 }} allowDecimals={false} />
            <Tooltip />
            <Bar dataKey="value" radius={[3, 3, 0, 0]}>
              {categoriaData.map((_, i) => (
                <Cell key={i} fill={CATEGORIA_COLORS[i % CATEGORIA_COLORS.length]} />
              ))}
            </Bar>
          </BarChart>
        </ChartCard>

        <ChartCard title="Vendas por cidade" note="Quantidade de itens vendidos">
          <BarChart data={cidadeData} layout="vertical" margin={{ left: 16 }}>
            <CartesianGrid strokeDasharray="3 3" stroke="var(--line)" horizontal={false} />
            <XAxis type="number" tick={{ fontSize: 12 }} allowDecimals={false} />
            <YAxis type="category" dataKey="name" tick={{ fontSize: 12 }} width={110} />
            <Tooltip />
            <Bar dataKey="value" radius={[0, 3, 3, 0]} fill={CIDADE_COLOR} />
          </BarChart>
        </ChartCard>

        <ChartCard title="Canal de venda" note="Loja física x Online">
          <PieChart>
            <Pie
              data={canalData}
              dataKey="value"
              nameKey="name"
              innerRadius={55}
              outerRadius={90}
              paddingAngle={2}
            >
              {canalData.map((entry, i) => (
                <Cell key={i} fill={CANAL_COLORS[entry.name] || "#999"} />
              ))}
            </Pie>
            <Tooltip />
            <Legend />
          </PieChart>
        </ChartCard>

        <ChartCard title="Forma de pagamento" note="Número de vendas por método">
          <BarChart data={pagamentoData}>
            <CartesianGrid strokeDasharray="3 3" stroke="var(--line)" vertical={false} />
            <XAxis dataKey="name" tick={{ fontSize: 12 }} />
            <YAxis tick={{ fontSize: 12 }} allowDecimals={false} />
            <Tooltip />
            <Bar dataKey="value" radius={[3, 3, 0, 0]}>
              {pagamentoData.map((entry, i) => (
                <Cell key={i} fill={PAGAMENTO_COLORS[entry.name] || "#999"} />
              ))}
            </Bar>
          </BarChart>
        </ChartCard>
      </div>
    </div>
  );
}

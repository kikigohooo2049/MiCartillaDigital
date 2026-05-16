import { Link } from "react-router-dom";

export default function Dashboard() {
  return (
    <div>
      <h1>Bienvenido al sistema de cartilla digital</h1>
      <div style={{ marginTop: 20 }}>
        <Link to="/pacientes">
          <button>Ver Pacientes</button>
        </Link>
      </div>
    </div>
  );
}
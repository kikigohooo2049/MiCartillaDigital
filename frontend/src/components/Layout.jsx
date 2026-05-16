import { Link, useNavigate } from "react-router-dom";
import { useContext } from "react";
import { AuthContext } from "../auth/AuthContext";

export default function Layout({ children }) {
  const { logout } = useContext(AuthContext);
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate("/login");
  };

  return (
    <div>
      <header style={{ padding: "10px", borderBottom: "1px solid #ccc" }}>
        <strong>Cartilla Digital</strong>{" "}
        <Link to="/" style={{ marginLeft: 10 }}>Dashboard</Link>{" "}
        <Link to="/pacientes" style={{ marginLeft: 10 }}>Pacientes</Link>
        <button onClick={handleLogout} style={{ marginLeft: 20 }}>Salir</button>
      </header>

      <main style={{ padding: "20px" }}>{children}</main>
    </div>
  );
}
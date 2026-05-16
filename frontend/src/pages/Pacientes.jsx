import { useEffect, useState } from "react";
import api from "../api/axios";

export default function Pacientes() {
  const [pacientes, setPacientes] = useState([]);
  const [nombre, setNombre] = useState("");
  const [apellido, setApellido] = useState("");
  const [edad, setEdad] = useState("");

  const cargarPacientes = async () => {
    const res = await api.get("pacientes/");
    setPacientes(res.data);
  };

  useEffect(() => {
    cargarPacientes();
  }, []);

  const crearPaciente = async (e) => {
    e.preventDefault();
    await api.post("pacientes/", {
      nombre,
      apellido,
      edad: edad ? parseInt(edad) : null,
    });
    setNombre("");
    setApellido("");
    setEdad("");
    cargarPacientes();
  };

  return (
    <div>
      <h2>Pacientes</h2>

      <form onSubmit={crearPaciente} style={{ marginBottom: 20 }}>
        <input
          placeholder="Nombre"
          value={nombre}
          onChange={(e) => setNombre(e.target.value)}
        />
        <input
          placeholder="Apellido"
          value={apellido}
          onChange={(e) => setApellido(e.target.value)}
        />
        <input
          placeholder="Edad"
          type="number"
          value={edad}
          onChange={(e) => setEdad(e.target.value)}
        />
        <button type="submit">Crear</button>
      </form>

      <ul>
        {pacientes.map((p) => (
          <li key={p.id}>
            {p.nombre} {p.apellido} ({p.edad})
          </li>
        ))}
      </ul>
    </div>
  );
}
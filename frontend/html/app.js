const tablaBody = document.getElementById("team-tabla-body");
const estadoIndicador = document.getElementById("backend-estado");

async function fetchTeamData() {

	try {
		//conexion con el backend
		const respuesta = await fetch("http://localhost:5000/api/team"); 
		
		if (!respuesta.ok) throw new Error("Error en la respuesta del servidor");

		const data = await respuesta.json();

		//si la conexion es exitosa se cambia el indicador de estado a verde
		estadoIndicador.innerText = "Conectado"
		estadoIndicador.className = "estado-on"

		data.forEach(integrante => {
			const columnas = ` 
				<tr>
					<td>${integrante.nombre}</td>
					<td>${integrante.legajo}</td>
					<td>${integrante.feature}</td>
					<td>${integrante.servicio}</td>
					<td>${integrante.estado}</td>
				</tr>`;
			tablaBody.innerHTML += columnas;
		});

	} catch (error) {
		console.error("Error al obtener los datos:", error);
		//el estado se mantiene en desconectado si falla el back o todavia no esta corriendo
		estadoIndicador.innerText = "Desconectado";
		estadoIndicador.className = "estado-off";
	}
}

fetchTeamData();

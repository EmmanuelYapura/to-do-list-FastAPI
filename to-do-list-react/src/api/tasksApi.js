const API_URL = "http://localhost:8000/api/tasks";

export async function getTasks() {
  try {
    const response = await fetch(API_URL);
    if (!response.ok) throw new Error("Error al obtener tareas");
    return await response.json();
  } catch (error) {
    console.error(error);
    return [];
  }
}

export async function createTask(task) {
  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-type": "application/json" },
      body: JSON.stringify(task),
    });
    if (!response.ok)
      throw new Error("Error al crear tarea: ", response.status);
    return await response.json();
  } catch (error) {
    console.error("CreateTask error: ", error);
    throw error;
  }
}

export async function updateTask(id, updateData) {
  try {
    await fetch(`${API_URL}/${id}`, {
      method: "PUT",
      headers: { "Content-type": "application/json" },
      body: JSON.stringify(updateData),
    });
  } catch (error) {
    console.error("Error al actualizar tarea importante: ", error);
  }
}

export async function deleteTask(id) {
    try{
        await fetch(`${API_URL}/${id}`, {
            method: "DELETE"
        });
    }catch(error){
        console.log("Error al eliminar tarae: ", error);
    }
}
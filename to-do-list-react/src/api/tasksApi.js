const API_URL = 'http://localhost:8000/api/tasks';

export async function getTasks() {
    try{
        const response = await fetch(API_URL);
        if (!response.ok) throw new Error("Error al obtener tareas");
        return await response.json();
    }catch(error){
        console.error(error)
        return [];
    }
}
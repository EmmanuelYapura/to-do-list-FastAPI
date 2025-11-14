import { useState } from "react"

export function TaskForm({addTask}){
    const [nombre, setNombre] = useState("")
    const [completa, setCompleta] = useState(false)
    const [importante, setImportante] = useState(false)

    const handleSubmit = async (e) => {
        e.preventDefault()
        const newTask = {nombre, completa, importante}
        
        try{
            const response = await fetch("http://127.0.0.1:8000/api/tasks", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(newTask),
        });
        
        if(!response.ok){
            throw new Error("Error al crear la tarea")       
        }
        const data = await response.json()
        addTask(data)
        /* limpia nuestro form */
        setNombre("")
        setCompleta(false)
        setImportante(false)
    }catch (error){
        console.error(error)
    }

    }

    return(
        <section>
            <h2>Ingresa una tarea: </h2>
            <form onSubmit={handleSubmit}>
                <input onChange={(e) => setNombre(e.target.value)} value={nombre} type="text" name="nombre" placeholder="Ingrese su tarea..." />
                <label htmlFor="checkbox-label">
                    <input checked={completa} onChange={(e) => setCompleta(e.target.checked)} type="checkbox" name="completa"/>
                    Completada
                </label>
                <label htmlFor="checkbox-label">
                    <input checked={importante} onChange={e => setImportante(e.target.checked)} type="checkbox" name="importante"/>
                    Importante
                </label>
                <button type="submit">Agregar</button>
            </form>
        </section>
    )
}
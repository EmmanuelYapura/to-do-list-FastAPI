import { useState } from "react"
import { createTask } from "../api/tasksApi"

export function TaskForm({addTask}){
    const [nombre, setNombre] = useState("")
    const [completa, setCompleta] = useState(false)
    const [importante, setImportante] = useState(false)

    const handleSubmit = async (e) => {
        e.preventDefault()

        const newTask = {nombre, completa, importante}
        const data = await createTask(newTask)
        addTask(data)

        setNombre("")
        setCompleta(false)
        setImportante(false)
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
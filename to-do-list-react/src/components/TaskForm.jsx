import { useState } from "react"
import { createTask } from "../api/tasksApi"
import '../styles/tasks.css'


export function TaskForm({addTask}){
    const [errorMessage, setErrorMessage] = useState(false);
    const [nombre, setNombre] = useState("")
    const [importante, setImportante] = useState(false)
    let completa = false

    const handleSubmit = async (e) => {
        e.preventDefault()

        if(nombre.trim()){
            const newTask = {nombre, completa, importante}
            const data = await createTask(newTask)
            addTask(data)
    
            setNombre("")
            setImportante(false)
            setErrorMessage(false)
            return
        }

        setErrorMessage(true)
    }

    return(
        <section>
            <form onSubmit={handleSubmit}>
                <input onChange={(e) => setNombre(e.target.value)} value={nombre} type="text" name="nombre" placeholder="Ingrese una nueva tarea..." />
                <div className="form-options">
                <label>
                    <input checked={importante} onChange={e => setImportante(e.target.checked)} type="checkbox" name="importante"/>
                    Importante
                </label>
                <button type="submit">Agregar</button>
                </div>
            </form>
            <div className={`div-error ${errorMessage? "text-error" : "hidden"}`}>
                <p>No puede agregarse una cadena vacia</p>
            </div>
        </section>
    )
}
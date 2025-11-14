import '../styles/tasks.css'

export function TaskItem({task, onDelete, onToggleComplete, onToggleImportant}){
    return(
        <div className="task-item">
            <h4>{task.nombre}</h4>
            <p className={task.completa? "done" : "pending"}
            onClick={() => onToggleComplete(task.id, !task.completa)}
            style={{cursor: "pointer"}}
            >completada: {task.completa? "SI" : "NO"}</p>
            <p className={task.importante? "important" : "normal"}
            onClick={() => onToggleImportant(task.id, !task.importante)}
            style={{cursor: "pointer"}}
            >importante: {task.importante? "SI" : "NO"}</p>
            <button
                className="btn-delete"
                onClick={() => onDelete(task.id)}
            >
                Eliminar
            </button>
        </div>
    )
}
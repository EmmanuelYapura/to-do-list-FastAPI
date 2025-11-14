import { useState, useEffect } from "react";
import { getTasks } from "../api/tasksApi";
import { TaskItem } from "./TaskItem";
import { TaskForm } from "./TaskForm";

export function TaskList() {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchTasks() {
      const data = await getTasks();
      setTasks(data);
      setLoading(false);
    }
    fetchTasks();
  }, []);

  const addTask = (newTask) => {
    setTasks([...tasks, newTask]);
  };

  const deleteTask = async (id) => {
    try {
      await fetch(`http://localhost:8000/api/tasks/${id}`, {
        method: "DELETE",
      });
      setTasks(tasks.filter((task) => task.id !== id));
    } catch (error) {
      console.error("Error al eliminar tarea: ", error);
    }
  };

  const updateTask = async (id, completa) => {
    try {
      await fetch(`http://localhost:8000/api/tasks/${id}`, {
        method: "PUT",
        headers: { "Content-type": "application/json" },
        body: JSON.stringify({ completa: completa }),
      });
      setTasks(
        tasks.map((task) =>
          task.id === id ? { ...task, completa: completa } : task
        )
      );
    } catch (error) {
      console.error("Error al marcar completa: ", error);
    }
  };
  
  const updateImporantTask = async (id, importante) => {
    try {
      await fetch(`http://localhost:8000/api/tasks/${id}`, {
        method: "PUT",
        headers: { "Content-type": "application/json" },
        body: JSON.stringify({ importante: importante }),
      });
      setTasks(
        tasks.map((task) =>
          task.id === id ? { ...task, importante: importante } : task
        )
      );
    } catch (error) {
      console.error("Error al actualizar tarea importante: ", error);
    }
  };

  if (loading) return <h1>Cargando...</h1>;

  return (
    <div className="tasks-container">
      <h1>To-Do List</h1>
      <TaskForm addTask={addTask} />
      <h2>Lista de tareas</h2>
      {tasks.length === 0 ? (
        <p>No hay tareas aun.</p>
      ) : (
        tasks.map((task) => (
          <TaskItem
            key={task.id}
            task={task}
            onDelete={deleteTask}
            onToggleComplete={updateTask}
            onToggleImportant={updateImporantTask}
          />
        ))
      )}
    </div>
  );
}

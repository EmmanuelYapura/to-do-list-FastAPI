import { useState, useEffect } from "react";
import { deleteTask, getTasks, updateTask } from "../api/tasksApi";
import { TaskItem } from "./TaskItem";
import { TaskForm } from "./TaskForm";
import '../styles/tasks.css'

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

  const removeTask = async (id) => {
      await deleteTask(id)
      setTasks(tasks.filter((task) => task.id !== id));
  };

  const toggleAttribute = async (id, updateData) => {
      await updateTask(id, updateData)
      let key = Object.keys(updateData)[0]
      let value = Object.values(updateData)[0]
      setTasks(
        tasks.map((task) =>
          task.id === id ? { ...task, [key] : value } : task
        )
      );

  };

  if (loading) return <h1>Cargando...</h1>;

  return (
    <div className="tasks-container">
      <h1>To-Do List</h1>
      <p className="subtitle">Una forma moderna de gestionar tus tareas</p>
      <TaskForm addTask={addTask} />
      {tasks.length === 0 ? (
        <p>No hay tareas aun.</p>
      ) : (
        tasks.map((task) => (
          <TaskItem
            key={task.id}
            task={task}
            onDelete={removeTask}
            onToggleAttribute={toggleAttribute}
          />
        ))
      )}
    </div>
  );
}

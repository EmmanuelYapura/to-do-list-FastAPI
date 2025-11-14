import { TaskList } from "../components/TaskList";

function Home (){
    return(
        <main className="home">
            <h1>To-Do List con React y FastAPI</h1>
            <TaskList />
        </main>
    )
}

export default Home
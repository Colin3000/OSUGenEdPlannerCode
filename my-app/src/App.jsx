import './App.css'
import CourseTable from './CourseTable.jsx'
import Save from './Save.jsx'
import Load from './Load.jsx'

function Planner(){
  return (
    <div>
      <div>
        <Save />
        <Load />
      </div>
      <div>
        <CourseTable />
        <CourseTable />
      </div>
      <CourseTable />
      <CourseTable />
    </div>
  );
}

export default function App() {
  return <Planner />;
}

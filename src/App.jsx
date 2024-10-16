import './App.css'
import CourseTable from './CourseTable.jsx'
import BookendCourse from './BookendCourse.jsx'
import Save from './Save.jsx'
import Load from './Load.jsx'

function Planner(){
  const foundationsList = [
    "Race, Ethnicity and Gender Diversity",
    "Social and Behavioral Sciences",
    "Historical or Cultural Studies",
    "Writing and Information Literacy",
    "Literary, Visual, and Performing Arts",
    "Natural Sciences",
    "Mathematical and Quantitative Reasoning"
    ];
  const themesList = [
    "Citizenship for a Diverse and Just World"
  ];
  return (
    <div>
      <h1 id='Title'>The Ohio State University General Education Planner</h1>
      <div className='SaveAndLoad'>
        <Save />
        <Load />
      </div>
      <div className='BookendParent'>
        <BookendCourse CourseName="Launch Seminar"/>
        <BookendCourse CourseName="Reflection Seminar"/>
      </div>
      <table>
        <CourseTable CategoryName="Foundations" CourseType={foundationsList} />
        <CourseTable CategoryName="Themes" CourseType={themesList} />
      </table>
    </div>
  );
}

export default function App() {
  return <Planner />;
}

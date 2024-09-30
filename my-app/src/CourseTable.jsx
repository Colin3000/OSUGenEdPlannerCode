import Popup from 'reactjs-popup';
import SearchBar from './SearchBar.jsx';

function CourseSelection({ CourseType }) {
    const CourseLookupPage = () => (
        <Popup trigger={<button className="button"> 🔎 </button>} modal nested>
          <span> Modal content </span>
        </Popup>
      );
    return (
        <tr className='CourseRow'>
            <td><p>{CourseType}</p></td>
            <td className="SearchBar"><SearchBar /></td> 
            <td>{CourseLookupPage()}</td>
        </tr>
    );
}

export default function CourseTable({ CategoryName, CourseType }) {
    const courseRows = [];
    CourseType.forEach(element => {
        courseRows.push(<CourseSelection CourseType={element} />)
    });
    return (
        <tbody>
            <tr><th>{CategoryName}</th></tr>
            {courseRows}
        </tbody>
    );
}
import CourseLookupPage from './CourseLookupPage.jsx';
import { useState } from 'react';
import { createPortal } from 'react-dom';

fetch('https://github.com/Colin3000/OSUGenEdPlanner/blob/main/GECourseData.json')
    .then((response) => response.json())
    .then((data) => console.log(data));

function CourseSelection({ CourseType }) {
    const [showModal, setShowModal] = useState(false);
    return (
        <tr className='CourseRow'>
            <td><p>{CourseType}</p></td>
            <td className="SearchBar"><input type="text" /></td> 
            <td><button onClick={() => setShowModal(true)}>🔎</button></td>
            {showModal && createPortal(
                <CourseLookupPage onClose={() => setShowModal(false)} CourseType={CourseType}/>,
                document.body
            )}
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
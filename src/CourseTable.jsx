import CourseLookupPage from './CourseLookupPage.jsx';
import { useState } from 'react';
import { createPortal } from 'react-dom';

// const URL = 'https://wauwao.github.io/OSUGenEdPlanner/GECourseData.json';
// const response = await fetch(URL);
// const courseData = await response.json();

function getCourseAttributeKey (CourseType) {
    switch (CourseType) {
    }
} 

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

function SpecialCourseSelection({ CourseType }) {
    const [showModal, setShowModal] = useState(false);
    const options = [];
    CourseType.forEach((element, index) => {
        if (index >= 1)
            options.push(<option value={element}>{element}</option>)
    })
    return (
        <tr className="CourseRow">
            <td className="SpecialRow">
                <select>
                    {options}
                </select>
            </td> 
            <td className="SearchBar SpecialRow"><input type="text" /></td> 
            <td className="SpecialRow"><button onClick={() => setShowModal(true)}>🔎</button></td>
            {showModal && createPortal(
                <CourseLookupPage onClose={() => setShowModal(false)} CourseType={CourseType}/>,
                document.body
            )}
        </tr>
    )
}

export default function CourseTable({ CategoryName, CourseType }) {
    if (CategoryName === "Foundations") {
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
    } else {
        return (
            <tbody>
                <tr><th>{CategoryName}</th></tr>
                <CourseSelection CourseType={CourseType[0]} />
                <tr id="SpecialRowHeader">Choose a Theme</tr>
                <SpecialCourseSelection CourseType={CourseType} />
            </tbody>
        );
    }
}
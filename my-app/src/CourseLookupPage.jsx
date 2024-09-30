export default function CourseLookupPage({ onClose, CourseType }) {
    return (
        <div className="modal-overlay" onClick={() => {onClose()}}>
            <div className="modal" onClick={(e) => e.stopPropagation()}>
                <h3>{CourseType}</h3>
                <CourseSearchBar />
                <Course />
                <button id="closeButton" onClick={onClose}>&#10005;</button>
            </div>
        </div>
    );
}

function CourseSearchBar() {
    return (
        <input type="text" />
    );
}

function Course() {
    return (
        <div>
            <p>Course</p>
        </div>
    );
}


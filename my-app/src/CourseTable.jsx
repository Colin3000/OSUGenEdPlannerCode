function CourseCategory() {
    return <h1>Foundations</h1>;
}

function CourseSelection() {
    return (
        <div>
            <p>CourseSelection</p>
            <CourseLookup />
        </div>
    );
}

function CourseLookup() {
    return <button>?</button>
}
export default function CourseTable() {
    return (
        <div>
            <CourseCategory />
            <CourseSelection />
        </div>
    );
}
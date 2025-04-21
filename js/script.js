// // Get the student details from localStorage
// const name = localStorage.getItem('studentName');
// const roll_no = localStorage.getItem('studentRollNum');
// const email = localStorage.getItem('studentEmail');
const mess = localStorage.getItem('adminMess') || "No data available";
const registeredCount = localStorage.getItem('studentCount') || "No data available"; 
// Populate the profile information dynamically
// const profileName = document.getElementById('profileName');
// const profileRoll = document.getElementById('profileRoll');
// const profileEmail = document.getElementById('profileEmail');

// If the information is available, populate it; otherwise, show a message
// if (name && roll_no && email) {
//     profileName.textContent = mess;
//     profileRoll.textContent = roll_no;
//     profileEmail.textContent = email;
// } else {
//     profileName.textContent = "No data available";
//     profileRoll.textContent = "No data available";
//     profileEmail.textContent = "No data available";
// }

const mess_name = document.getElementById('mess_name');
const student_num = document.getElementById('student_num');

if ( mess) {
    mess_name.textContent = mess;
}

if (registeredCount) {
    student_num.textContent = registeredCount;
}




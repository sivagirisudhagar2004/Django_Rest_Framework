// main.js

// CREATE - POST
function CreateData() {
    const data = {
        tamil: 87,
        english: 76,
        maths: 56,
        science: 65,
        social_science: 80
    };
    
    fetch('http://localhost:8000/student/mark/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
        },
        credentials: 'include',
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Created:', data);
        alert('Record created! ID: ' + data.id);
    })
    .catch(error => console.error('Error:', error));
}


// READ - GET
function GetData() {
    fetch('http://localhost:8000/student/mark', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
        credentials: 'include',
    })
    .then(response => response.json())
    .then(data => {
        console.log('All Records:', data);
        displayTable(data.data);  // Display in table
    })
    .catch(error => console.error('Error:', error));
}


// UPDATE - PUT
function UpdateData(studentId) {
    const updatedData = {
        tamil: 90,          // Updated value
        maths: 85,          // Updated value
        english: 92         // Updated value
        // Other fields optional - only send what you want to change
    };
    
    fetch(`http://localhost:8000/student/mark/${studentId}/`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
        },
        credentials: 'include',
        body: JSON.stringify(updatedData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Updated:', data);
        alert('Record updated successfully!');
        GetData();  // Refresh data
    })
    .catch(error => console.error('Error:', error));
}


// DELETE - DELETE
function DeleteData(studentId) {
    if (confirm('Are you sure you want to delete this record?')) {
        fetch(`http://localhost:8000/student/mark/${studentId}/`, {
            method: 'DELETE',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
            },
            credentials: 'include',
        })
        .then(response => {
            if (response.status === 204) {
                console.log('Deleted successfully');
                alert('Record deleted!');
                GetData();  // Refresh data
            } else {
                return response.json();
            }
        })
        .catch(error => console.error('Error:', error));
    }
}


// Helper function
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


// Display data in a table
function displayTable(students) {
    let html = '<table border="1"><tr><th>ID</th><th>Tamil</th><th>English</th><th>Maths</th><th>Science</th><th>Social</th><th>Actions</th></tr>';
    students.forEach(student => {
        html += `<tr>
            <td>${student.id}</td>
            <td>${student.tamil}</td>
            <td>${student.english}</td>
            <td>${student.maths}</td>
            <td>${student.science}</td>
            <td>${student.social_science}</td>
            <td>
                <button onclick="UpdateData(${student.id})">Edit</button>
                <button onclick="DeleteData(${student.id})">Delete</button>
            </td>
        </tr>`;
    });
    html += '</table>';
    document.getElementById('dataTable').innerHTML = html;
}
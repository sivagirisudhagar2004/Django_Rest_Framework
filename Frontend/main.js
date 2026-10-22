function GetData(){
    fetch("http://localhost:8000/student/mark")
    .then( response => response.json())
    .then( data => console.log(data))
    .catch( error => console.log(error))
}

function CreateData(){
    fetch("http://localhost:8000/student/mark/",{
        method : "POST",
        headers :{
            "content-type" : "Application/json",
            "Authorization":""
        },
        body: JSON.stringify({
            "tamil":80,
            "english":75,
            "maths":85,
            "science":80,
            "social_science":83
        })
    })
    .then( response => response.json())
    .then(data => console.log(data))
    .catch(error => console.log(error))
}
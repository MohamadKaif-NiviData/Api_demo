function onDelete(userid) {
    var id = userid
    console.log(id);
    
       fetch(`http://127.0.0.1:8000/delete/${id}/`, {
       method: "DELETE",
       headers: {"Content-Type":"application/json"}
    });
}


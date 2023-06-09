var form = document.getElementById('form')


form.addEventListener('submit',function(e){
    e.preventDefault()
   var pk = document.getElementById('uid').value 
   var name = document.getElementById('name').value
   var body = document.getElementById('body').value
   var city = document.getElementById('city').value

    console.log(name,body);
    console.log(pk);
  //https://jsonplaceholder.typicode.com/posts

    fetch(`http://127.0.0.1:8000/update/${pk}/`, {
        method: 'PUT',
        body: JSON.stringify({
          name: name,
          no: body,
          city:city
        }),
        headers: {
          'Content-type': 'application/json; charset=UTF-8',
        },
      })
        .then((response) => response.json())
        .then((json) => {
            var res = document.getElementById('res')
            res.innerHTML=`${json.name} ${json.no} ${json.city}`
        }
       );
})
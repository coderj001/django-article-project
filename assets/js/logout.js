document.querySelector('.logout').addEventListener('click',function(e){
    e.preventDefault();
    let xhttp= new XMLHttpRequest();
    xhttp.open('GET','/account/logout/',true);
    xhttp.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    xhttp.send();
});
var updateBtns = document.getElementsByClassName('update-cart');

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
    var movieId = this.dataset.movie;
    var action = this.dataset.action;
    var movieName = this.dataset.name
    console.log( movieId)

    if(user === 'AnonymousUser'){
     console.log('adding cookie')
     addCookieItem(movieName, action,movieId)



    }
    else{
        UpdateUserOrder(movieId,action)
    }

    })

}


function addCookieItem(movieName, action, movieId){
    console.log('name:', movieName, 'action:', action )
    if(action === 'add'){
        cart[movieId]={'id': movieId,'name': movieName }
        }else{
        console.log('deleting')
       delete cart[movieId]
        }

         document.cookie = 'cart = ' +JSON.stringify(cart) + ";domain=;path=/"
         window.location.reload()

    }





function UpdateUserOrder(movieId,action){

 var origin   = window.location.origin
 var txt = ''

 if(action === 'add'){
 var txt = '/update/'
 }else{
 var txt = '/remove/'
 }


    fetch(origin + txt,{
    method:'POST',
    headers:{'Content-Type':'application/json',
                'X-CSRFToken': csrftoken},
    body: JSON.stringify({'movieId': movieId, 'action' :action})
    })
    .then((response)=>{
        return response.json();
    })
    .then((data)=>{
        console.log('data:' , data);
        location.reload()
    })


}







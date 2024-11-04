
document.addEventListener("DOMContentLoaded", function() {
    document.querySelector("#create").addEventListener("click" ,() => create());
    document.querySelectorAll('edit').addEventListener("click" ,() => function(){
        const postId = this.getAttribute('data-post-id');
        document.querySelector('#edit_post').style.display = 'block';
        document.querySelector("#update").addEventListener("click" ,() => edit(postId))

    });

    document.querySelector("#like").addEventListener("click" ,() => update_like());
    

   // Call the create function when the DOM is fully loaded
});

function create() {
    // Clear out composition fields
    document.querySelector('form').onsubmit = function() {
        const content = document.querySelector("#post_content").value;
        const user = document.querySelector("#post_user").value;
        console.log("user: ",user,"content :",content)
  
        fetch('/create_post', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json' // Set content type to JSON
        },
          body: JSON.stringify({
              user: user,
              content: content
          })
        })
        .then(response =>  {
            if (!response.ok){
                throw new Error('Network response was not ok')
            }
            return response.json();})
        .then(post => {
            console.log("post publish",post); 
            document.querySelector("#post_content").value = ''; 
        
        })
        .catch(error => {
            console.error("There was a problem with the fetch operation:", error);
        });
            };}


function edit(postId) {
    // Clear out composition fields
   

    document.querySelector('form').onsubmit = function() {
        event.preventDefault();
        fetch('/create_post')
        .then(response => {
            console.log("Response status:", response.status);
          return response.json()})
        .then(post => {
            document.querySelector("#post_content").value = post.content; 
        fetch(`/edit/${postId}`, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json' // Set content type to JSON
        },
          body: JSON.stringify({
              content: content
          })
        })
        .then(response =>  {
            if (!response.ok){
                throw new Error('Network response was not ok')
            }
            return response.json();})
        .then(post => {
            console.log("post publish",post); 
            
        
        })
        .catch(error => {
            console.error( error);
        });
            })}}

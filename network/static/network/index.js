
document.addEventListener("DOMContentLoaded", function() {
    document.querySelector("#create").addEventListener("click" , create());
    document.querySelectorAll(".edit").forEach(editbutton => {
        console.log("1");
        editbutton.addEventListener("click" ,function() {
       
        console.log("2");
        const postId = this.getAttribute('data-post-id');
        console.log("3");
        document.querySelector(`#edit_post-${postId}`).style.display = 'block';
        console.log("4");
        document.querySelector("#update").addEventListener("click" , edit(postId));
        console.log("5");}
        )})

        document.querySelectorAll(".like").forEach(likebutton =>{
            likebutton.addEventListener("click" , function(){
                const postId = this.getAttribute('data-post-id');
                console.log("6");
                up_like(postId);

        })})
    
    

    

   
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
          
            
            
        
        })
        .catch(error => {
            console.error("There was a problem with the fetch operation:", error);
        });
            };}


function edit(postId) {
        fetch(`/post/${postId}`)
        .then(response => {
            console.log("Fetching post data,");
            console.log("Response status:", response.status);
          return response.json()})
        .then(post => {
            console.log("Post data:", post);
            document.querySelector(`#content-${postId}`).value = post.content;
            document.querySelector(`#form_edit-${postId}`).onsubmit = function(event){
                event.preventDefault();
                const content = document.querySelector(`#content-${postId}`).value; // Get the updated content
                fetch(`/edit_post/${postId}`, {
                     method: 'PUT',
                     headers: {
                          'Content-Type': 'application/json'},
                     body: JSON.stringify({
                           content: content
                           }) })
                .then(response =>  {
                     if (!response.ok){
                          throw new Error('Network response was not ok')}
                    return response.json();})
                .then(post => {
                     console.log("poste edited", post);
                     const postelement =document.querySelector(`#post-${postId}`);
                     postelement.querySelector(`#p-${postId}`).textContent = content;
                    
                     document.querySelector(`#edit_post-${postId}`).style.display = 'none';
                    })
                .catch(error => {
                      console.error( error)})
}})
        .catch(error => 
            console.error("There was a problem with the fetch operation:", error)
          )
          
        }

function up_like(postId){
        fetch(`/post/${postId}`)
        .then(response => {
            console.log("Fetching post data,");
          return response.json()})
        .then(post => {
            console.log("Post data:", post);
                const current = post.like; 
                const likes = current + 1;
                fetch(`/like/${postId}`, {
                     method: 'PUT',
                     headers: {
                          'Content-Type': 'application/json'},
                     body: JSON.stringify({
                           like: likes
                           }) })
                .then(response =>  {
                     if (!response.ok){
                          throw new Error('Network response was not ok')}
                    return response.json();})
                .then(post => {
                     console.log("poste liked", post);
                     const postelement =document.querySelector(`#post-${postId}`);
                     postelement.querySelector(`#like-${postId}`).textContent = likes;
                    })
                .catch(error => {
                      console.error( error)})
})
        .catch(error => 
            console.error("There was a problem with the fetch operation:", error)
          )
          
        }

   

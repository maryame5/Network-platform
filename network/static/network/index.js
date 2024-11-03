document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#create').addEventListener('click', ()=>create()
    );
})

function create() {
    // Clear out composition fields
    document.querySelector('#post_content').value = '';
    document.querySelector('form').onsubmit = function() {
        const content = document.querySelector("#post_content").value;
        const user = document.querySelector("#post_user").value;
        console.log("user: ",user,"/n \ncontent :",content)
  
        fetch('/create_post', {
          method: 'POST',
          body: JSON.stringify({
              user: user,
              content: content
          })
        })
        .then(response => response.json())
        .then(post => {
            console.log("post publish",post);  
        })};}

        
var ul  = document.getElementById("tweetList");


function addTweet(event){
  var input = document.getElementById("tweetInput");
  var li = document.createElement("LI");
  var em = document.createElement("EM");
  em.innerText=" Sim"
  li.innerText = event.target.value;
  li.appendChild(em);
  ul.prepend(li);
  input.value="";
}
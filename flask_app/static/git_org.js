var github = document.querySelector("#github-username");
var githubfollowers = document.querySelector("#github-followers");
var githubphoto = document.querySelector("#github-photo");
var country = document.querySelector("#country").value;
var country_flag = document.querySelector("#country_flag");

async function getCoderData() {
    var user = github.textContent
    var response = await fetch("https://api.github.com/users/"+ user);
    var coderData = await response.json();
    githubfollowers.textContent = coderData.followers
    githubphoto.src = coderData.avatar_url
    return coderData;

}


// uncomment code to bring API
getCoderData() 



async function getCoderData2() {
    var response = await fetch("https://restcountries.com/v3.1/name/"+ country);
    var coderData = await response.json();
    country_flag.src = coderData[0].flags.png
    return coderData;
}
getCoderData2() 
var github = document.querySelector("#github");
var githubuser = document.querySelector("#githubuser");

async function getCoderData() {
    var user = github.value
    // La palabra clave await le permite a JS saber que necesita esperar (wait) hasta que obtenga una respuesta para continua
    var response = await fetch("https://api.github.com/users/"+ user);
    // Luego necesitamos convertir los datos en formato JSON
    var coderData = await response.json();
    console.log(coderData.followers)
    var githubcontainer = document.querySelector("#container2");
    if(coderData.name == undefined ) {
        githubcontainer.innerHTML = `<p style="color: red;">The user indicated does not exist in Github  </p>`
    } else {
        githubcontainer.innerHTML = ""
        githubcontainer.innerHTML += `<p style="color: green;">The user indicated is a valid user in Github  </p>`
        githubcontainer.innerHTML += "<p>"+ coderData.name + " has " + coderData.followers + " followers" +"</p>"
        githubcontainer.innerHTML += "<img src="+ coderData.avatar_url + ">"+"</img>"
        githubuser.value = user
        return coderData;
    }

}
// if(element.classList.contains("shadowx")) {


async function getCoderData2(element) {
    var user = element.value
    console.log(user)
    // La palabra clave await le permite a JS saber que necesita esperar (wait) hasta que obtenga una respuesta para continua
    var response = await fetch("https://api.github.com/users/"+ user);
    // Luego necesitamos convertir los datos en formato JSON
    var coderData = await response.json();
    console.log(coderData.followers)
    var githubcontainer = document.querySelector("#container2");
    if(coderData.name == undefined ) {
        githubcontainer.innerHTML = `<p style="color: red;">The user indicated does not exist in Github  </p>`
    } else {
        githubcontainer.innerHTML = ""
        githubcontainer.innerHTML += `<p style="color: green;">The user indicated is a valid user in Github  </p>`
        // githubcontainer.innerHTML += "<p>"+ coderData.name + " has " + coderData.followers + " followers" +"</p>"
        // githubcontainer.innerHTML += "<img src="+ coderData.avatar_url + ">"+"</img>"
        githubuser.value = user
        return coderData;
    }

}

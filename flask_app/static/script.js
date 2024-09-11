var blockaddedskills = document.querySelector("#added_skills");
var nextstepform = document.querySelector("#nextstepform");
var bio = document.querySelector("#bio2");
var postion_name = document.querySelector("#position_name2");

function addtoskills(element){
    if(element.classList.contains("shadowx")) {
        element.classList.remove("shadowx");
        newb = element.id + 2
        var newb = document.querySelector(`#`+ newb )
        newb.remove()
        newa = element.id + 3
        var newa = document.querySelector(`#`+ newa )
        newa.value = "False"
    } else {
        element.classList.add("shadowx");
        console.log(element.src)
        blockaddedskills.innerHTML += "<img src=" + element.src + ` class="icons2" alt="iconhtml" id="` + element.id +  `2">` ;
        newa = element.id + 3
        var newa = document.querySelector(`#`+ newa )
        newa.value = "True"
    }
};

function setbio(element) {
    console.log(element.value)
    bio.value = element.value
}


function setname(element) {
    console.log(element.value)
    postion_name.value = element.value
}
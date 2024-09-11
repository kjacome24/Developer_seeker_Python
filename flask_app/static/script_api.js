document.addEventListener('DOMContentLoaded', () => {

    const selectDrop = document.querySelector('#country');
    // const selectDrop = document.getElementById('countries');

    fetch('https://restcountries.com/v3.1/all').then(res => {
        return res.json();
    }).then(data => {
    let output = `<option value="none" selected hidden>Select an Option</option>`;
    data.forEach(country => {
        output += `        
        <option value="${country.name.common}">${country.name.common}</option>`;
        console.log(country.flags.png)
    })

    

    selectDrop.innerHTML = output;
    }).catch(err => {
        console.log(err);
    })
});

document.addEventListener('DOMContentLoaded', () => {

    const selectDrop = document.querySelector('#country2');
    // const selectDrop = document.getElementById('countries');

    fetch('https://restcountries.com/v3.1/all').then(res => {
        return res.json();
    }).then(data => {
    let output = `<option value="none" selected hidden>Select an Option</option>`;
    data.forEach(country => {
        output += `        
        <option value="${country.name.common}">${country.name.common}</option>`;
        console.log(country.flags.png)
    })

    

    selectDrop.innerHTML = output;
    }).catch(err => {
        console.log(err);
    })
});




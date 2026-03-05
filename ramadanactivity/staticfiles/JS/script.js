document.addEventListener('DOMContentLoaded', function() {
    var dataChoise = document.getElementById("Act-data");
    const select = document.createElement("select");
    select.name = "day";
    select.id = "day";

    dataChoise.appendChild(select);

    for (var i = 1; i <= 30; i++) {
        const option = document.createElement("option");
        option.value = i ;
        option.textContent = i + " رمضان";
        select.appendChild(option);
    }
});
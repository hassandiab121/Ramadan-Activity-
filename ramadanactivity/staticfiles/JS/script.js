document.addEventListener('DOMContentLoaded', function() {
    var dataChoise = document.getElementById("Act-data");
    const select = document.createElement("select");
    select.name = "day";
    select.id = "day";

    dataChoise.appendChild(select);

    for (var i = 15; i <= 30; i++) {
        const option = document.createElement("option");
        option.value = i ;
        option.textContent = i + " رمضان";
        select.appendChild(option);
    }
});

function phone_number_validation() {
    const form = document.getElementById('join-form');
    const card = document.getElementById('join-card');
    if (!form || !card) return;

    const phoneInput = form.querySelector('input[name="phone"]');
    const errorBox = document.getElementById('phone-error');

    form.addEventListener('submit', function (e) {
        if (!phoneInput) return;
        const digits = (phoneInput.value || '').replace(/\\D/g, '');

        if (digits.length !== 11) {
            e.preventDefault();
            if (errorBox) {
                errorBox.textContent = 'رقم الجوال يجب أن يحتوي على 11 رقمًا بالضبط.';
            } else {
                alert('رقم الجوال يجب أن يحتوي على 11 رقمًا بالضبط.');
            }
            card.classList.add('shake');
            setTimeout(function () {
                card.classList.remove('shake');
            }, 500);
        }
    });
}

document.addEventListener('DOMContentLoaded', phone_number_validation())
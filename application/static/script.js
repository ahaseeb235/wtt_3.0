

// function validateForm() {
//     var nameField = document.querySelector('input[name="name"]');
//     var nameValue = nameField.value;
//     var regex = /^[A-Za-z\s]*$/;

//     if (!regex.test(nameValue)) {
//         alert("Please enter a valid name. Only letters and spalces are allowed.");
//         nameField.focus();
//         return false;
//     }
//     return true;
// }

const ctx = document.getElementById('myChart');

new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
            label: '# of Votes',
            data: [12, 19, 3, 5, 2, 3],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});
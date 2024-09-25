// function validateEntryName(name) {
//     // Input validation: Check if the input is a string
//     if (typeof name !== 'string') {
//         throw new TypeError('Input must alphabets only.');
//     }

//     // Regular expression to validate that the name contains only alphabets (case insensitive)
//     const regex = /^[A-Za-z]+$/;

//     // Test the name against the regular expression
//     return regex.test(name);
// }

function validateForm() {
    var nameField = document.querySelector('input[name="name"]');
    var nameValue = nameField.value;
    var regex = /^[A-Za-z\s]*$/; // Regex for letters and spaces only

    if (!regex.test(nameValue)) {
        alert("Please enter a valid name. Special characters and numbers are not allowed.");
        nameField.focus();
        return false; // Prevent form submission
    }
    return true; // Allow form submission
}
function validateEntryName(name) {
    // Input validation: Check if the input is a string
    if (typeof name !== 'string') {
        throw new TypeError('Input must be a string.');
    }

    // Regular expression to validate that the name contains only alphabets (case insensitive)
    const regex = /^[A-Za-z]+$/;

    // Test the name against the regular expression
    return regex.test(name);
}
document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("scamForm");
    const analysisScreen = document.getElementById("analysisScreen");

    if (!form) {
        return;
    }

    form.addEventListener("submit", function (event) {

        const description = document
            .querySelector("textarea[name='description']")
            .value
            .trim();

        // Validate description
        if (description.length < 10) {

            alert("Please enter more details about the opportunity.");

            event.preventDefault();

            return;
        }

        // STOP normal form submission temporarily
        event.preventDefault();

        // Show Analysis page
        analysisScreen.classList.add("show");

        // Wait for analysis animation
        setTimeout(function () {

            // Now send the form data to Flask
            form.submit();

        }, 2000);

    });

});
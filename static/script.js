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

        if (description.length < 10) {

            alert("Please enter more details about the opportunity.");

            event.preventDefault();

            return;
        }

        event.preventDefault();

        analysisScreen.classList.add("show");

        setTimeout(function () {

            form.submit();

        }, 2000);

    });

});

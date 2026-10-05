/* =========================
   SEARCH NOTES
========================= */

const searchInput =
    document.getElementById("searchInput");


if (searchInput) {

    searchInput.addEventListener(
        "keyup",
        function () {

            const searchText =
                this.value.toLowerCase().trim();


            const noteCards =
                document.querySelectorAll(
                    ".note-card"
                );


            noteCards.forEach(
                function (card) {

                    const title =
                        card.querySelector("h2")
                            .textContent
                            .toLowerCase();


                    const content =
                        card.querySelector(
                            ".note-content"
                        )
                        .textContent
                        .toLowerCase();


                    if (
                        title.includes(searchText) ||
                        content.includes(searchText)
                    ) {

                        card.style.display = "";

                    } else {

                        card.style.display = "none";

                    }

                }
            );

        }
    );

}


/* =========================
   CHARACTER COUNTER
========================= */

const contentBox =
    document.getElementById("content");


const charCount =
    document.getElementById("charCount");


if (contentBox && charCount) {


    function updateCharacterCount() {

        charCount.textContent =
            contentBox.value.length;

    }


    contentBox.addEventListener(
        "input",
        updateCharacterCount
    );


    updateCharacterCount();

}


/* =========================
   FORM VALIDATION
========================= */

function validateNoteForm() {


    const title =
        document
        .getElementById("title")
        .value
        .trim();


    const content =
        document
        .getElementById("content")
        .value
        .trim();


    if (title === "") {

        alert(
            "Please enter a note title."
        );

        return false;

    }


    if (title.length < 3) {

        alert(
            "Title must contain at least 3 characters."
        );

        return false;

    }


    if (content === "") {

        alert(
            "Please enter note content."
        );

        return false;

    }


    return true;

}
document.getElementById("translate_form").addEventListener("submit", async function (event) {
    event.preventDefault();
    const sentence = document.getElementById("english_sentence").value;

    try {
        const response = await fetch(`${window.location.origin}/translate`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ sentence: sentence })
        });

        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }
        const result = await response.json();
        const translation = document.getElementById("french_sentence")
        translation.innerText = result.translation;
    } catch (error) {
        console.error("Error:", error);
    }
});

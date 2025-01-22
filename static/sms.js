document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".book-now").forEach(button => {
        button.addEventListener("click", function (event) {
            event.preventDefault();
            let userId = this.getAttribute("data-id");
            let phoneNumber = this.getAttribute("data-phone");
            function getCSRFToken() {
                // If CSRF token is set in a meta tag:
                let token = document.querySelector('meta[name="csrf-token"]');
                if (token) {
                    return token.getAttribute('content');
                }
            
                // Or get it from the cookie
                return getCookie('csrftoken');
            }
            const csrfToken = getCSRFToken();
            console.log(csrfToken)
            fetch("/book/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrfToken
                },
                body: JSON.stringify({
                    user_id: userId,
                    phone: phoneNumber
                })
                
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not OK');
                }
                return response.json();
            })
            .then(data => {
                console.log("Response data:", data);  // Debugging log

                if (data.success) {
                    alert("Booking successful! SMS Status: " + data.message);
                } else {
                    alert("Booking failed: " + (data.error || "Unknown error"));
                }
            })
            .catch(error => {
                console.error("Error:", error);
                alert("An error occurred while processing your request.");
            });
        });
    });
});
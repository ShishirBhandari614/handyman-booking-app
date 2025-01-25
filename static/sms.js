// document.addEventListener("DOMContentLoaded", function () {
//     var serviceType = document.getElementById('service-type').value;
//     document.querySelectorAll(".book-now").forEach(button => {
//         button.addEventListener("click", function (event) {
//             event.preventDefault();
//             let userId = this.getAttribute("data-id");
//             let phoneNumber = this.getAttribute("data-phone");
//             let customerId = this.getAttribute("customerid");
//             let customername=this.getAttribute("customername");
//             let customerPhone = this.getAttribute("customerphone");


//             console.log("User ID:", userId);
//             console.log("Phone Number:", phoneNumber);
//             console.log("customerId:", customerId)
//             console.log("customerphone:", customerPhone)
//             console.log("customername:", customername)
//             console.log('Service Type:', serviceType);
//             function getCSRFToken() {
//                 let token = document.querySelector('meta[name="csrf-token"]');
//                 if (token) {
//                     return token.getAttribute('content');
//                 }
//                 return document.cookie.split('; ')
//                     .find(row => row.startsWith('csrftoken='))
//                     ?.split('=')[1];
//             }

//             const csrfToken = getCSRFToken();
//             console.log("CSRF Token:", csrfToken);

//             fetch("/book/", {
//                 method: "POST",
//                 headers: {
//                     "Content-Type": "application/json",
//                     "X-CSRFToken": csrfToken
//                 },
//                 body: JSON.stringify({
//                     user_id: userId,
//                     phone: phoneNumber,
//                     customer_id: customerId,
//                     customer_phone: customerPhone,
//                     customer_name:customername,
//                     serviceType:serviceType
//                 })
//             })
//             .then(response => response.json())  // Parse JSON response
//             .then(result => {
//                 console.log("Full response:", result);  // Debugging log
//                 if (result.success) {  // Check for success key
//                     alert("Booking successful! SMS Status: " + (result.message || "No message provided"));
//                     window.location.href = /viewprofile/;
//                 } else {
//                     alert("Booking failed: " + (result.message || "Unknown error"));
//                 }
//             })
//             .catch(error => {
//                 console.error("Fetch error:", error);
//                 alert("An error occurred while processing your request.");
//             });                       
//         });
//     });
// });

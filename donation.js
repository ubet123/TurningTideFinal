// script.js

document.getElementById("nextBtn").addEventListener("click", function () {
    const amountRadios = document.getElementsByName("amount");
    let amountValue = 0;
    let customAmount = document.querySelector("input[name='custom-amount']").value;

    // Get selected amount
    for (const radio of amountRadios) {
        if (radio.checked) {
            amountValue = radio.value;
            break;
        }
    }

    if (amountValue === "0" && !customAmount) {
        alert("Please select a donation amount or enter a custom amount.");
        return;
    }

    if (customAmount) {
        amountValue = customAmount;
    }

    // Hide donation amount card and show frequency card
    document.querySelector(".amount-card").style.display = "none";
    document.getElementById("frequencyCard").style.display = "block";
});

document.getElementById("summaryBtn").addEventListener("click", function () {
    const frequencyRadios = document.getElementsByName("frequency");
    let frequencyValue = "";

    // Get selected frequency
    for (const radio of frequencyRadios) {
        if (radio.checked) {
            frequencyValue = radio.value;
            break;
        }
    }

    if (!frequencyValue) {
        alert("Please select a donation frequency.");
        return;
    }

    // Display summary
    document.getElementById("summaryAmount").innerText = `Donation Amount: $${document.querySelector("input[name='amount']:checked") ? document.querySelector("input[name='amount']:checked").value : document.querySelector("input[name='custom-amount']").value}`;
    document.getElementById("summaryFrequency").innerText = `Donation Frequency: ${frequencyValue}`;
    
    // Hide frequency card and show summary
    document.getElementById("frequencyCard").style.display = "none";
    document.getElementById("summary").style.display = "block";
});

document.getElementById("backBtn").addEventListener("click", function () {
    // Show donation amount card and hide frequency card and summary
    document.querySelector(".amount-card").style.display = "block";
    document.getElementById("frequencyCard").style.display = "none";
    document.getElementById("summary").style.display = "none";
});

document.getElementById("checkoutBtn").addEventListener("click", function () {
    alert("Proceeding to checkout...");
    // Add your checkout logic here
});

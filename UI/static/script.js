// document.getElementById('csvFile').addEventListener('change', function(e) {
//     const file = e.target.files[0];
//     if (!file) return;

//     const reader = new FileReader();
//     reader.onload = function(e) {
//         const csvData = e.target.result;
//         const rows = csvData.split('\n').slice(1, 6);
//         let previewHTML = '';

//         rows.forEach(row => {
//             const content = row.split(',')[1] || '';
//             const cleanContent = content
//                 .replace(/@\w+/g, '@xxx')  // Mask handles
//                 .replace(/#\w+/g, '');     // Remove hashtags

//             previewHTML += `
//                 <div class="tweet-preview">
//                     ${cleanContent}
//                 </div>
//             `;
//         });

//         document.getElementById('tweetsPreview').innerHTML = previewHTML;
//     };
//     reader.readAsText(file);
// });

document.getElementById("csvFile").addEventListener("change", function (e) {
  const file = e.target.files[0];
  if (!file) return;

  const reader = new FileReader();
  reader.onload = function (e) {
    const csvData = e.target.result;
    const rows = csvData.split("\n").slice(1, 6); // Get first 5 data rows
    let previewHTML = "";

    rows.forEach((row) => {
      const content = row.split(",")[1] || "";
      previewHTML += `
                <div class="tweet-preview">
                    <span class="masked-handle">@xxx</span>: 
                    ${content.substring(0, 80)}${
        content.length > 80 ? "..." : ""
      }
                </div>
            `;
    });

    document.getElementById("tweetsPreview").innerHTML = previewHTML;
  };
  reader.readAsText(file);
});

function runAnalysis() {
  const fileInput = document.getElementById("csvFile");
  const btn = document.querySelector(".run-btn");

  if (!fileInput.files.length) {
    alert("Please select a CSV file!");
    return;
  }

  btn.innerHTML = '<div class="loader"></div> Analyzing...';
  btn.disabled = true;

  const formData = new FormData();
  formData.append("csv_file", fileInput.files[0]);

  fetch("/analyze", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      btn.innerHTML = "Analyze Sentiment";
      btn.disabled = false;

      if (data.error) {
        alert(data.error);
        return;
      }

      if (window.currentChart) {
        window.currentChart.destroy();
      }

      drawPieChart(data.sentiment_counts);
    })
    .catch((error) => {
      console.error("Error:", error);
      btn.innerHTML = "Analyze Sentiment";
      btn.disabled = false;
      alert("Analysis failed. Please try again.");
    });
}

function drawPieChart(sentimentCounts) {
  const ctx = document.getElementById("sentimentChart").getContext("2d");

  window.currentChart = new Chart(ctx, {
    type: "pie",
    data: {
      labels: Object.keys(sentimentCounts),
      datasets: [
        {
          data: Object.values(sentimentCounts),
          backgroundColor: ["red", "blue", "green"],
          borderColor: "#2c3e50",
          borderWidth: 2,
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          position: "right",
          labels: {
            color: "#fff",
            font: {
              size: 14,
            },
          },
        },
      },
    },
  });
}

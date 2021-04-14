let isAnalyzing = false;
function submitData(event) {
  event.preventDefault();
  if (isAnalyzing) return false;

  let form = event.target;
  if (form.reportValidity) {
    isAnalyzing = true;
    let result = document.getElementById("results-text");
    result.innerText = "Analyzing image, please wait...";
    let fileInput = document.getElementById("fileToUpload");
    fileInput.disabled = true;
    let file = fileInput.value;
    let body = new FormData();
    body.append("image", fileInput.files[0]);
    fetch("/predict", { method: "POST", body })
      .then((response) => response.json())
      .then((response) => {
        let prediction;
        if (response.result == 0) prediction = "Negative";
        else if (response.result == 1) prediction = "Positive";
        else prediction = "Image is not a prostate MRI.";

        result.innerText = prediction;
      })
      .catch(() => {
        alert("Please make sure the server is running!");
        result.innerText = "";
      })
      .finally(() => {
        isAnalyzing = false;
        fileInput.disabled = false;
      });
  }
  return false;
}

export function detect_browser() {
  let isES6 = true;

  try {
    new Function("(a = 0) => a");
  } 
  
  catch (e) {
    isES6 = false;
  }

  if (
    typeof Symbol === "undefined" ||
    !("from" in Array) ||
    !("assign" in Object)
  ) {
    isES6 = false;
  }

  const resultDiv = document.getElementById("result");
  if (resultDiv) {
    if (isES6) {
      resultDiv.innerText = "Browser ini mendukung ES6.";
      console.log("Browser mendukung ES6.");
    } 
    
    else {
      resultDiv.innerText = "Browser ini hanya mendukung ES5 atau lebih lama.";
    }
  }

  if (!isES6) {
    // Load polyfill
    const polyfillScript = document.createElement("script");

    polyfillScript.src = "/static/polyfill/minified.js";
    polyfillScript.onload = function () {
      console.log("Custom polyfill dimuat.");
      // Lanjut jalankan app jika perlu
    };
    
    document.head.appendChild(polyfillScript);

    // Redirect
    window.location.href = "/unsupported";
  }
}

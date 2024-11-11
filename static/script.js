const form = document.getElementById('certificate-form');
const certificateDiv = document.getElementById('certificate');

form.addEventListener('submit', function (event) {
    event.preventDefault();
    const recipientName = document.getElementById('recipientName').value;
    generateCertificate(recipientName);
});

function generateCertificate(recipientName) {
    const certificateContent = `
      <div class="doc">
        <h5><i>CERTIFICATE OF APPRECIATION</i><h5>
        <p class="pp">presented to</p>
        <h1 class="rn">${recipientName}</h1>
        <p class="msg">We extend our heartfelt appreciation for your generous donation of food<br>we are thankful for your kindness</p>
        <p>---------------------*---------------------</P>
        <p class="td">on ${new Date().toDateString()}.</p>
        <p><i>from Surplus Food Management team</i></p></div>
    `;
    
    certificateDiv.innerHTML = certificateContent;
    certificateDiv.style.display = 'block';
}


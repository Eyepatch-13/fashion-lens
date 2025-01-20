function toggleInput(selection) {
    if (selection === 'file') {
        document.getElementById('file-input').style.display = 'block';
        document.getElementById('url-input').style.display = 'none';
    } else if (selection === 'url') {
        document.getElementById('file-input').style.display = 'none';
        document.getElementById('url-input').style.display = 'block';
    }
}

async function submitForm(event) {
    event.preventDefault();

    const method = document.querySelector('input[name="method"]:checked').value;
    const formData = new FormData();
    const apiUrl = '/upload';
    let responseData;

    if (method === 'file') {
        const fileInput = document.getElementById('file');
        if (!fileInput.files.length) {
            alert('Please select a file to upload.');
            return;
        }
        formData.append('file', fileInput.files[0]);

        // Send file upload request
        const response = await fetch(apiUrl, {
            method: 'POST',
            body: formData,
        });

        responseData = await response.json();

    } else if (method === 'url') {
        const url = document.getElementById('url').value;
        if (!url) {
            alert('Please enter a valid URL.');
            return;
        }

        // Send URL submission request
        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ url }),
        });

        responseData = await response.json();
    }

    // Pretty-print response data
    // document.getElementById('response-data').textContent = JSON.stringify(responseData, null, 2);

    // Render images in the gallery
    const gallery = document.getElementById('image-gallery');
    gallery.innerHTML = responseData.message
        .map(
            product => `
        <div class="col-md-4">
            <div class="card">
                <img src="/images/${product.id}.jpg" class="card-img-top" alt="${product.productDisplayName}">
                <div class="card-body">
                    <h5 class="card-title">${product.productDisplayName}</h5>
                    <p class="card-text">
                        <strong>Category:</strong> ${product.masterCategory}<br>
                        <strong>Sub-Category:</strong> ${product.subCategory}<br>
                        <strong>Color:</strong> ${product.baseColour}<br>
                        <strong>Gender:</strong> ${product.gender}<br>
                        <strong>Season:</strong> ${product.season}<br>
                        <strong>Year:</strong> ${product.year}<br>
                        <strong>Usage:</strong> ${product.usage}
                    </p>
                </div>
            </div>
        </div>
    `
        )
        .join('');
}
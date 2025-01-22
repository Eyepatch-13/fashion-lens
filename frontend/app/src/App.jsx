import React, { useState } from 'react';
import './App.css';

function App() {
    const [method, setMethod] = useState('');
    const [file, setFile] = useState(null);
    const [url, setUrl] = useState('');
    const [responseData, setResponseData] = useState([]);

    const handleMethodChange = (selection) => {
        setMethod(selection);
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        const apiUrl = 'http://127.0.0.1:5000/upload';
        let response;

        if (method === 'file') {
            if (!file) {
                alert('Please select a file to upload.');
                return;
            }
            const formData = new FormData();
            formData.append('file', file);

            response = await fetch(apiUrl, {
                method: 'POST',
                body: formData,
            });
        } else if (method === 'url') {
            if (!url) {
                alert('Please enter a valid URL.');
                return;
            }

            response = await fetch(apiUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ url }),
            });
        }

        const data = await response.json();
        setResponseData(data.message.reverse());
    };

    return (
      <div className="container my-5">
      <h2 className="text-center mb-4">Submit Image or URL</h2>
    <form
        onSubmit={handleSubmit}
        className="p-4 bg-dark text-white rounded shadow-sm form-container"
    >
        <div className="mb-4 text-center">
            <label className="form-label">Choose submission method:</label>
            <div className="d-flex justify-content-center gap-4 mt-2">
                <div className="form-check">
                    <input
                        type="radio"
                        className="form-check-input"
                        name="method"
                        id="file-method"
                        value="file"
                        onChange={() => handleMethodChange('file')}
                        required
                    />
                    <label htmlFor="file-method" className="form-check-label">
                        Upload Image
                    </label>
                </div>
                <div className="form-check">
                    <input
                        type="radio"
                        className="form-check-input"
                        name="method"
                        id="url-method"
                        value="url"
                        onChange={() => handleMethodChange('url')}
                        required
                    />
                    <label htmlFor="url-method" className="form-check-label">
                        Provide Image URL
                    </label>
                </div>
            </div>
        </div>

        {method === 'file' && (
            <div className="mb-3">
                <label htmlFor="file" className="form-label">
                    Choose an image file
                </label>
                <input
                    type="file"
                    className="form-control"
                    id="file"
                    onChange={(e) => setFile(e.target.files[0])}
                />
            </div>
        )}

        {method === 'url' && (
            <div className="mb-3">
                <label htmlFor="url" className="form-label">
                    Enter Image URL
                </label>
                <input
                    type="url"
                    className="form-control"
                    id="url"
                    value={url}
                    onChange={(e) => setUrl(e.target.value)}
                    placeholder="https://example.com/image.jpg"
                />
            </div>
        )}

        <div className="text-center">
            <button type="submit" className="btn btn-primary btn-lg">
                Submit
            </button>
        </div>
    </form>
  
      <div id="results" className="mt-5">
          {responseData.length > 0 && <h3 className="mt-4">Here's what we found:</h3>}
          <div id="image-gallery" className="row g-4">
              {responseData.map((product) => (
                  <div className="col-md-4" key={product.id}>
                      <div className="card">
                          <img
                              src={`http://localhost:5000/images/${product.id}.jpg`}
                              className="card-img-top"
                              alt={product.productDisplayName}
                          />
                          <div className="card-body">
                              <h5 className="card-title">{product.productDisplayName}</h5>
                              <p className="card-text">
                                  <strong>Category:</strong> {product.masterCategory}<br />
                                  <strong>Sub-Category:</strong> {product.subCategory}<br />
                                  <strong>Color:</strong> {product.baseColour}<br />
                                  <strong>Gender:</strong> {product.gender}<br />
                                  <strong>Season:</strong> {product.season}<br />
                                  <strong>Year:</strong> {product.year}<br />
                                  <strong>Usage:</strong> {product.usage}
                              </p>
                          </div>
                      </div>
                  </div>
              ))}
          </div>
      </div>
  </div>
    );  
}

export default App;

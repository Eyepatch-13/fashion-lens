
# Fashion Lens

A quick and easy way to discover fashion choices from everyday world. Just a click and upload or link us the url. And we'll find the most similar products for you.




## Authors

- [@Toran Jain](https://github.com/Eyepatch-13)


## Features

- Image Upload / URL input
- Results Ranking
- Quick Results
- Responsive
- Cross platform


## API Reference

#### Get landing page

```http
  GET /
```

#### Get all products

```http
  GET /products
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `page`    | `integer`| **Optional**. The Page number to retrieve |
| `limit'   | `integer`| **Optional**. The number of items per page |

#### Get item

```http
  GET /products/<int:id>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `integer` | **Required**. Id of product to fetch |

#### Post /upload

```http
  POST /upload

```

| Parameter     | Type     | Description                                                             |
| :------------ | :------- | :---------------------------------------------------------------------- |
| `method`      | `string` | The submission method: `"file"` for file upload or `"url"` for URL submission. Required. |
| `file`        | `file`   | The image file to be uploaded. Required if `method` is `"file"`.        |
| `url`         | `string` | The URL of the image to be processed. Required if `method` is `"url"`.  |




## Tech Stack

**Client:** Html, Css, Javascript

**Server:** Python

**Model:** ResNet50
## Roadmap

- Add basic filters

- Add ability to insert more data into tables

- Improve frontend design


## Installation

Install the project by cloning the repository.

```bash
  git clone https://github.com/Eyepatch-13/fashion-lens.git
  cd fashion-lens
```

Setup the database, images, and embeddings inside the Intance directory in the following way:

 ```bash
instance/database/{embeddings.pkl, filenames.pkl}

instance/images/<all images>

instance/styles/<all style.json files> optional

instance/uploads

instance/{image.csv, styles.csv}
```

Setup products.db by running one_time.py

```bash
python3 one_time.py
```
    
## Run Locally

Setup Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
python3 run.py
```


## Running Tests

To run tests, run the following command

```bash
pytest
```


## Feedback

If you have any feedback, please reach out to us at toran.jain@daffodilsw.com


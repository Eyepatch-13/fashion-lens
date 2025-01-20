
# Fashion Lens

A quick and easy way to discover fashion choices from everyday world. Just a click and upload or link us the url. And we'll find the most similar products for you.




## Authors

- Toran Jain


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


## Roadmap

- Add basic filters

- Add ability to insert more data into tables

- Improve frontend design


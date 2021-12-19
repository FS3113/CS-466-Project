# Visulization of Hirschberg Algorithm

This project implements a linear-space sequence alignment algorithm, Hirschberg Algorithm. This algorithm uses divide-and-conquer, and is a more space-efficient version of Needleman–Wunsch algorithm. The motivation of this project is to provide a way to implement and visualize each iteration of the Hirschberg Algorithm, so as to gain a better understanding of this algorithm and how it is space-efficient. We will use Python to implement Hirschberg Algorithm, and use React and Flask to build the visualization website.

## Usage

1. To begin with, let's start the Flask to serve the website;

```bash
flask run
```

2. Then let's run npm to start the React frontend;

```shell
cd my-app
npm start
```

Then npm should automatically navigate to http://localhost:3000/ in your browser.

## Project Structure

```shell
.
├── README.md
├── app.py # Flask backend
├── hirschberg.py # Hirschberg implementation
└── my-app # React frontend
```


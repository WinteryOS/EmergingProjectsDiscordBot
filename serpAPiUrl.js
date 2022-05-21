// import os;
// import requests;
// import discord;
//import GoogleSearch from serpapi;

const api_Key = "9a44608178a3b7ad9888bb12ed05a1992916835b8af2d5bc1fc164a5f8b1201d";
const googleSearch = "Coffee";

const url = `https://serpapi.com/search.json?engine=google&q=${googleSearch}&location=Salt+Lake+City%2C+Utah%2C+United+States&google_domain=google.com&gl=us&hl=en&api_key=${api_Key}`
// # params = {
// #     "q": "Coffee",
// #     "api_key": "9a44608178a3b7ad9888bb12ed05a1992916835b8af2d5bc1fc164a5f8b1201d",
// #     "engine": "google",
// #     "google_domain": "google.com",
// #     "gl": "us",
// #     "hl": "en"
// # }

//results.organic_results.[count].link;

// const search = GoogleSearch(params)
// const results = search.get_dict()

// api url
const api_url =
	"https://employeedetails.free.beeceptor.com/my/api/path";

// Defining async function
async function getapi(url) {
	
	// Storing response
	const response = await fetch(url);
	
	// Storing data in form of JSON
	var data = await response.json();
	console.log(data);
	if (response) {
		hideloader();
	}
	show(data);
}
// Calling that async function
getapi(api_url);

// Function to hide the loader
function hideloader() {
	document.getElementById('loading').style.display = 'none';
}
// Function to define innerHTML for HTML table
function show(data) {
	let tab =
	`<tr>
		<th>Name</th>
		<th>Office</th>
		<th>Position</th>
		<th>Salary</th>
		</tr>`;
	
	// Loop to access all rows
	for (let r of data.list) {
		tab += `<tr>
	<td>${r.name} </td>
	<td>${r.office}</td>
	<td>${r.position}</td>
	<td>${r.salary}</td>		
        </tr>`;
	}
	// Setting innerHTML as tab variable
	document.getElementById("employees").innerHTML = tab;
}


console.log(`Api URL: ${url}`);
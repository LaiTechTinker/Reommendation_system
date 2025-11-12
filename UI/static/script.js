document.getElementById("searchBtn").addEventListener("click", getRecommendations);

async function getRecommendations() {
  const movieName = document.getElementById("movieInput").value.trim();
  const errorDiv = document.getElementById("error");
  const loading = document.getElementById("loading");
  const resultSection = document.getElementById("resultSection");
  const recContainer = document.getElementById("recommendations");

  errorDiv.textContent = "";
  recContainer.innerHTML = "";
  resultSection.classList.add("hidden");

  if (!movieName) {
    errorDiv.textContent = "Please enter a movie name.";
    return;
  }

  loading.style.display = "block";

  try {
    const response = await fetch("/recommend", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ name: movieName })
    });

    const data = await response.json();
    loading.style.display = "none";

    if (data.status === "fail") {
      errorDiv.textContent = data.message || "Movie not found.";
      return;
    }

    // Show queried movie
    document.getElementById("queriedTitle").textContent = movieName;
    document.getElementById("queriedPoster").src = data.movieposter || "";

    // Render recommendations
    const movies = data.output;
    const posters = data.poster;

    movies.forEach((movie, index) => {
      const card = document.createElement("div");
      card.className = "movie-card";
      card.innerHTML = `
        <img src="${posters[index] || ''}" alt="${movie}">
        <p>${movie}</p>
      `;
      recContainer.appendChild(card);
    });

    resultSection.classList.remove("hidden");

  } catch (err) {
    loading.style.display = "none";
    errorDiv.textContent = "Error fetching data. Make sure backend is running.";
    console.error(err);
  }
}

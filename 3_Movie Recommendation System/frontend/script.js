async function recommend() {
  const movie = document.getElementById("movieInput").value;

  const response = await fetch("http://127.0.0.1:8000/recommend", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ movie })
  });

  const data = await response.json();

  const list = document.getElementById("results");
  list.innerHTML = "";

  data.recommendations.forEach(m => {
    const li = document.createElement("li");
    li.innerText = m;
    list.appendChild(li);
  });
}

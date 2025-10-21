const loginModal = document.getElementById("loginModal");
const openLogin = document.getElementById("openLogin");
const closeLogin = document.getElementById("closeLogin");
const doLogin = document.getElementById("doLogin");
const loginMsg = document.getElementById("loginMsg");

if (openLogin) openLogin.onclick = () => (loginModal.style.display = "flex");
if (closeLogin) closeLogin.onclick = () => (loginModal.style.display = "none");

if (doLogin) {
  doLogin.onclick = async () => {
    const username = document.getElementById("loginUser").value.trim();
    const password = document.getElementById("loginPass").value.trim();
    if (!username || !password) {
      loginMsg.textContent = "Please fill all fields";
      return;
    }

    const res = await fetch("/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password })
    });
    const data = await res.json();

    if (data.success) {
      window.location.reload();
    } else {
      loginMsg.textContent = data.message;
    }
  };
}

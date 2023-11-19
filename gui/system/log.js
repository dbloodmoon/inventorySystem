const btnLogin = document.querySelector("#btnLogin");
const btnLogout = document.querySelector("#btnLogout");
const loginSection = document.querySelector("#login-section");
const mainSection = document.querySelector("#main-section");

btnLogin.addEventListener("click", (e) => {
    e.preventDefault();
    if (
      userForm.value === "leinor" ||
      (userForm.value === "desi" && passwordForm.value === "1234")
    ) {
      loginSection.setAttribute("hidden", true);
      mainSection.removeAttribute("hidden");
      localStorage.setItem("login", true)
    } else alert("Credenciales incorrectas");
  });

  btnLogout.addEventListener("click", (e) => {
    e.preventDefault();
    loginSection.removeAttribute("hidden");
    mainSection.setAttribute("hidden", true);
    localStorage.setItem("login", false)
  })

if(localStorage.getItem("login") === "true"){
  loginSection.setAttribute("hidden", true);
  mainSection.removeAttribute("hidden");
}
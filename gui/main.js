const apiURL = "http://localhost:8000/api/v1/";
const navItems = document.querySelectorAll(".nav-item");
const render = document.querySelector(".main-container");
const prevButton = document.querySelector("#prev-button");
const nextButton = document.querySelector("#next-button");
const navPagination = document.querySelector(".nav-pagination");
const paginationButton = document.querySelectorAll(".page-item");
const userForm = document.querySelector("#usuarioForm");
const passwordForm = document.querySelector("#passwordForm");
const mainSection = document.querySelector("#main-section");
const loginSection = document.querySelector("#login-section");
const btnAdmin = document.querySelector("#btnAdmin");
const btnLogin = document.querySelector("#btnLogin");
const tableHead = document.querySelector("#tableHead");
const tableBody = document.querySelector("#tableBody");
const elementsPerPage = 10;
let actualPage = null;
let totalPages = 0;
let page = 1;
let item = [];
let departamentoSelected = "";
let isFilter = false;

const getItemFromAPI = (URL) => {
  if (item.length > 0) {
    item = [];
  }

  fetch(URL)
    .then((res) => res.json())
    .then((data) => {
      item.push(data);
      //  console.log(item);
    });
};

const getSize = () => {
  return Object.keys(item[0][0]).length;
};

const filterItems = (filter) => {
  if (actualPage === "departamento" && !isFilter) {
    item[0] = [];
    fetch(apiURL + "empleado")
      .then((res) => res.json())
      .then((data) => {
        for (const key in data) {
          if (data[key].departamento_nombre === filter) {
            item[0].push(data[key]);
          }
        }

        for (let i = 0; i < item[0].length; i++) {
          
          if (item[0][i].hasOwnProperty("departamento")){
            delete item[0][i]["departamento"];
          }
        }

        console.log(item[0][0].length);

        eraseTableContent();
        eraseTableHeader();
        insertTableContent();
        insertTableHeader(data);
        isFilter = true;
      });
  }
};

const insertTableContent = () => {
  let cont = 1;
  isFilter = false;

  for (const key in item[0]) {
    const elementTr = document.createElement("tr");
    const elementTh = document.createElement("th");

    elementTh.setAttribute("scope", "row");

    const textContent = Object.values(item[0][key]).toString();
    let textArray = textContent.split(" ");
    const formatArray = (textArray = textContent.split(","));

    formatArray.forEach((text) => {
      if (
        cont === Object.keys(item[0][key]).length &&
        actualPage !== "departamento"
      ) {
        cont = 1;
      } else {
        const elementTd = document.createElement("td");

        elementTd.textContent = text;
        elementTr.appendChild(elementTd);
        cont++;
      }
    });

    tableBody.appendChild(elementTr);

    elementTr.addEventListener("click", (e) => {
      departamentoSelected = e.target.textContent;
      filterItems(departamentoSelected);
    });
    totalPages = Math.ceil(item[0].length / elementsPerPage);
  }
};

const setCurrentPage = (pageNum) => {
  page = pageNum;
};

const showPages = () => {
  let initialIndex = (page - 1) * elementsPerPage;
  let finalIndex = page * elementsPerPage;
  let cont = 1;
  tableBody.innerHTML = "";
  // console.log(initialIndex, finalIndex);

  for (let i = initialIndex; i < finalIndex; i++) {
    if (i < item[0].length) {
      const elementTr = document.createElement("tr");
      const elementTh = document.createElement("th");
      elementTh.setAttribute("scope", "row");

      const textContent = Object.values(item[0][i]).toString();
      let textArray = textContent.split(" ");
      const formatArray = (textArray = textContent.split(","));

      formatArray.forEach((text) => {
        if (
          cont === Object.keys(item[0][i]).length &&
          actualPage !== "departamento"
        ) {
          cont = 1;
        } else {
          const elementTd = document.createElement("td");
          elementTd.textContent = text;
          elementTr.appendChild(elementTd);
          cont++;
        }
      });

      tableBody.appendChild(elementTr);
    }
  }
};

const eraseTableContent = () => {
  while (tableBody.firstChild) {
    tableBody.removeChild(tableBody.firstChild);
  }
};

const insertTableHeader = (data) => {
  for (let i = 0; i < getSize(data); i++) {
    const element = document.createElement("th");
    element.setAttribute("scope", "col");

    if (Object.keys(item[0][0])[i] === "id") element.textContent = "#";
    else if (Object.keys(item[0][0])[i] === "departamento_nombre")
      element.textContent = "departamento";
    else if (Object.keys(item[0][0])[i] === "empleado_nombre")
      element.textContent = "asignado";
    else if (Object.keys(item[0][0])[i] === "usuario") continue;
    else if (Object.keys(item[0][0])[i] === "departamento") continue;
    else if (Object.keys(item[0][0])[i] === "responsable") continue;
    else element.textContent = Object.keys(item[0][0])[i];

    tableHead.appendChild(element);
  }
};

const eraseTableHeader = () => {
  while (tableHead.firstChild) {
    tableHead.removeChild(tableHead.firstChild);
  }
};

// Coloca el evento a cada elemento de la barra de navegación
navItems.forEach((item) => {
  const link = item.querySelector("a");
  const path = link.getAttribute("href");
  link.addEventListener("click", (e) => {
    e.preventDefault();
    // console.log(apiURL + path);
    getItemFromAPI(apiURL + path);
    fetch(apiURL + path)
      .then((res) => res.json())
      .then((data) => {
        actualPage = path;
        //   console.log(data);
        eraseTableHeader();
        insertTableHeader(data);
        eraseTableContent();
        insertTableContent();
        setCurrentPage(1);
        // console.log(totalPages)
      })
      .catch((err) => {
        eraseTableContent();
        eraseTableHeader();
        //alert("No hay datos para mostrar");

        const div = document.createElement("div");
        div.setAttribute(
          "class",
          "alert alert-danger alert-dismissible fade show"
        );
        div.setAttribute("role", "alert");
        const strong = document.createElement("strong");
        strong.textContent = "Aviso!! No hay ningún dato para mostrar";
        const button = document.createElement("button");
        button.setAttribute("type", "button");
        button.setAttribute("class", "btn-close");
        button.setAttribute("data-bs-dismiss", "alert");
        button.setAttribute("aria-label", "Close");
        navPagination.setAttribute("hidden", true);
        div.appendChild(strong);
        div.appendChild(button);
        tableBody.appendChild(div);
      });

    navPagination.removeAttribute("hidden");
  });
});

prevButton.addEventListener("click", () => {
  if (page === 1) return;
  setCurrentPage(page - 1);
});

nextButton.addEventListener("click", () => {
  if (page === totalPages) return;
  setCurrentPage(page + 1);
});

// Coloca el evento a cada elemento de la barra de paginación DEPURAR
paginationButton.forEach((button) => {
  button.addEventListener("click", (e) => {
    e.preventDefault();
    //  console.log(page);
    showPages();
  });
});

btnAdmin.addEventListener("click", (e) => {
  window.location.href = "http://localhost:8000/admin";
});

btnLogin.addEventListener("click", (e) => {
  e.preventDefault();
  if (
    userForm.value === "leinor" ||
    (userForm.value === "desi" && passwordForm.value === "1234")
  ) {
    loginSection.setAttribute("hidden", true);
    mainSection.removeAttribute("hidden");
  } else alert("Credenciales incorrectas");
});

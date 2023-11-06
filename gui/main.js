const apiURL = "http://localhost:8000/api/v1/";
const navItems = document.querySelectorAll(".nav-item");
const render = document.querySelector(".main-container");
const paginationButton = document.querySelectorAll(".page-item");
const tableHead = document.querySelector("#tableHead");
const tableBody = document.querySelector("#tableBody");
const elementsPerPage = 1;
let actualPage = null;
let item = [];
const totalPages = Math.ceil(item.length / elementsPerPage);

const getItemFromAPI = (URL) => {
  if (item.length > 0) {
    item = [];
  }

  fetch(URL)
    .then((res) => res.json())
    .then((data) => {
      item.push(data);
      console.log(item);
    });
};

const getSize = () => {
  return Object.keys(item[0][0]).length;
};

const insertTableContent = () => {
  let cont = 1;

  for (const key in item[0]) {
    const elementTr = document.createElement("tr");
    const elementTh = document.createElement("th");

    elementTh.setAttribute("scope", "row");

    const textContent = Object.values(item[0][key]).toString();
    let textArray = textContent.split(" ");
    const formatArray = (textArray = textContent.split(","));

    formatArray.forEach((text) => {
      console.log(Object.keys(item[0][key]).length);

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
  }
};

const showPages = (page = 1) => {
  let initialIndex = (page - 1) * elementsPerPage;
  let finalIndex = page * elementsPerPage;
  tableBody.innerHTML = "";

  console.log(finalIndex);

  for (let i = initialIndex; i < finalIndex; i++) {
    if (i < item[0].length) {
      const elementTr = document.createElement("tr");
      const elementTh = document.createElement("th");
      elementTh.setAttribute("scope", "row");
      const elementTd = document.createElement("td");
      elementTd.textContent = item[0][i];
      elementTr.appendChild(elementTh);
      elementTr.appendChild(elementTd);
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
      });
  });
});

// Coloca el evento a cada elemento de la barra de paginación DEPURAR
paginationButton.forEach((button) => {
  button.addEventListener("click", (e) => {
    e.preventDefault();
    console.log(e.target);
    showPages();
  });
});

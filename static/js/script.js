const formulario = document.getElementById("formulario-contacto");
const mensajeExito = document.getElementById("mensaje-exito");

formulario.addEventListener("submit", function(event) {
    event.preventDefault();

    formulario.reset();

    mensajeExito.textContent = "¡Información enviada correctamente!";
});
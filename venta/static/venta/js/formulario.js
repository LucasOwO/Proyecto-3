const formulario = document.getElementById('formulario');
const inputs = document.querySelectorAll('#formulario input')


const expresiones = {
    nombre: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos con largo de 1 a 40.
    apellidos: /^[a-zA-ZÀ-ÿ\s]{1,90}$/, //Letras y espacios, pueden llevar acentos con largo de 1 a 90.
    correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
	telefono: /^\d{9,9}$/ // solo 9 numeros.
}

const campos = {
    nombre: false,
    apellidos: false,
    correo: false,
    telefono: false
}

const validarFormulario = (e) => {
    switch (e.target.name){
        case "nombre":
            validarCampo(expresiones.nombre, e.target, 'nombre');
        break;
        case "apellidos":
            validarCampo(expresiones.apellidos, e.target, 'apellidos');
        break;
        case "correo":
            validarCampo(expresiones.correo, e.target, 'correo');
        break;
        case "telefono":
            validarCampo(expresiones.telefono, e.target, 'telefono');
        break;
    }
}

const validarCampo = (expresion, input, campo) => {
    if(expresion.test(input.value)){
        document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-incorrecto')
        document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-correcto')
        document.querySelector(`#grupo__${campo} i`).classList.add('bi-check-square-fill');
        document.querySelector(`#grupo__${campo} i`).classList.remove('bi-x-square-fill');
        document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.remove('formulario__input-error-activo');
        campos[campo] = true;
    }else{
        document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-incorrecto')
        document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-correcto')
        document.querySelector(`#grupo__${campo} i`).classList.add('bi-x-square-fill');
        document.querySelector(`#grupo__${campo} i`).classList.remove('bi-check-square-fill');
        document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.add('formulario__input-error-activo'); 
        campos[campo] = false;
    }
}

inputs.forEach((inputs)=>{
    inputs.addEventListener('keyup', validarFormulario)
    //inputs.addEventListener('blur', validarFormulario)
});

formulario.addEventListener('submit',(e) => {
    e.preventDefault();

    const terminos = document.getElementById('terminos');
    if(campos.nombre && campos.apellidos && campos.correo && campos.telefono && terminos.checked){
        formulario.reset();

        document.getElementById('formulario__mensaje-exito').classList.add('formulario__mensaje-exito-activo');
        setTimeout(() =>{
            document.getElementById('formulario__mensaje-exito').classList.remove('formulario__mensaje-exito-activo');
        },5000);
    
        document.querySelectorAll('.formulario__grupo-correcto').forEach((icono)=> {
            icono.classList.remove('formulario__grupo-correcto');
        })
    }else{
        document.getElementById('formulario__mensaje').classList.add('formulario__mensaje-activo');
        setTimeout(() =>{
            document.getElementById('formulario__mensaje').classList.remove('formulario__mensaje-activo');
        },5000);
    }
    
});





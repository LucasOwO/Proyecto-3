const nombre = document.getElementById("nombre");
const correo = document.getElementById("correo");
const passw1 = document.getElementById("pass1");
const passw2 = document.getElementById("pass2");
const form = document.getElementById("form");


const expresiones = {
    nombre: /^[a-zA-ZÀ-ÿ\s]{1,20}$/, // Letras y espacios, pueden llevar acentos con largo de 1 a 40.
    apellidos: /^[a-zA-ZÀ-ÿ\s]{1,90}$/, //Letras y espacios, pueden llevar acentos con largo de 1 a 90.
    password: /^.{4,12}$/, // 4 a 12 digitos.
    correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
	telefono: /^\d{9,9}$/ // solo 9 numeros.
}

// form.addEventListener("submit", (e)=>{
//     e.preventDefault();
//     if(nombre.value.length < 6){
//         txt = "Nombre no valido";
//     }else{
//         txt = "";      
//     }
//     document.getElementById("valid_nombre").innerHTML = txt;

//     if(correo)
    
// })


form.addEventListener("submit", (e)=>{
    e.preventDefault();
    cont = 0;
    if(!expresiones.nombre.test(nombre.value)){
        txt = "Nombre no valido";
    }else{
        txt = ""; 
        cont = cont+1;    
    }
    document.getElementById("valid_nombre").innerHTML = txt;
    

    if(!expresiones.correo.test(correo.value)){
        txt = "Correo no valido";
    }else{
        txt = ""; 
        cont = cont+1;      
    }
    document.getElementById("valid_email").innerHTML = txt;

    if(!expresiones.password.test(passw1.value)){
        txt = "Contraseña debe tener de 4 a 12 digitos";
    }else{
        txt = ""; 
        cont = cont+1;      
    }
    document.getElementById("valid_pass").innerHTML = txt;


    
    if(cont == 3 ){
        document.getElementById("regCo").innerHTML = "Registro guardado";
        setTimeout(() =>{
            document.getElementById("regCo").innerHTML = "";
        },5000);
        
    }else{
        document.getElementById("regCo").innerHTML = "Faltan datos";
        setTimeout(() =>{
            document.getElementById("regCo").innerHTML = "";
        },5000);
        
    }

})





var eye = document.getElementById('Eye');
var pass1 = document.getElementById('pass1');

eye.addEventListener("click", function(){
    if(pass1.type == "password"){
        pass1.type = "text"
        eye.style.opacity=0.8
    }else{
        pass1.type = "password"
        eye.style.opacity = 0.2
    }
})
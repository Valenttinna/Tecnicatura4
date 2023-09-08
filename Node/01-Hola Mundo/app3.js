console.log('Inicio del programa'); //1
setTimeout(()=> {
console.log('Primer Timeout'); //5 lo guarda
},3000);

setTimeout(()=> {
console.log('Segundo Timeout'); //3 lo guarda
},0);

setTimeout(()=> {
console.log('Tercer Timeout'); //4 lo guarda
},0);

console.log('Fin de Programa') //2
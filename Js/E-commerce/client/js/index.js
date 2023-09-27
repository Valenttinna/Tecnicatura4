const shopContent = document.getElementById("shopContent");
const cart = []; //Este es el carrito, un array vacio

productos.forEach((product) =>{
    const content = document.createElement("div");
    content.innerHTML = `
    <img src="${product.img}">
    <h3>${product.pructName}</h3>
    <p>$ ${product.price}</p>
    `;
    shopContent.append(content);

    const buyButton = document.createElement("button");
    buyButton.innerText = "Comprar";

    content.append(buyButton);
    
    buyButton.addEventListener("click", ()=>{
        const repeat = cart.some((repeatProduct)=> repeatProduct.id === product.id);

        if(repeat){
            cart.map((prod)=> {
                if(prod.id === product.id) {
                    prod.quanty++;
                    displayCartCounter();
                }
            });
        }else{
            cart.push({
                id: product.id,
                productName: product.pructName,
                price: product.price,
                quanty: product.quanty,
                img: product.img,
            });
            displayCartCounter();
        }
    });
});
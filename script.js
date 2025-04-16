function filterProducts(category) {
    const products = document.querySelectorAll('.product-card');
    products.forEach(product => {
      const productCategory = product.getAttribute('data-category');
      if (category === 'all' || productCategory === category) {
        product.style.display = 'block';
      } else {
        product.style.display = 'none';
      }
    });
  }
  
  function addToCart(productName) {
    alert(`${productName} added to cart!`);
    // You can expand this with a real cart system later
  }


  // Local cart array
let cart = JSON.parse(localStorage.getItem("cart")) || [];

// Add product to cart
function addToCart(productName) {
  cart.push(productName);
  localStorage.setItem("cart", JSON.stringify(cart));
  alert(`${productName} added to cart!`);
}

// Display cart items on cart.html
if (window.location.pathname.includes("cart.html")) {
  const cartDiv = document.getElementById("cartItems");
  const total = document.getElementById("totalPrice");
  if (cart.length === 0) {
    cartDiv.innerHTML = "<p>Your cart is empty.</p>";
  } else {
    cartDiv.innerHTML = "<ul>" + cart.map(item => `<li>${item}</li>`).join('') + "</ul>";
    total.textContent = `Total Items: ${cart.length}`;
  }
}

  
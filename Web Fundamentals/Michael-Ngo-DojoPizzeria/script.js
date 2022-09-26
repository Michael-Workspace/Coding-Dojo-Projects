// The Pizza Oven
function pizzaOven(crustType,sauceType,cheeses,toppings) {
    var pizza = {};
    pizza.crustType = crustType;
    pizza.sauceType = sauceType;
    pizza.cheeses = cheeses;
    pizza.toppings = toppings;
    return pizza;
}

var pizza1 = pizzaOven(["deep dish"],["tranditional"],["mozzarella"],["pepperoni","sausage"]);
console.log(pizza1);

var pizza2 = pizzaOven(["hand tossed"],["marinara"],["mozzarella","feta"],["mushrooms","olives","onions"]);
console.log(pizza2);

var pizza3 = pizzaOven(["stuffed"],["pesto"],["gouda","ricotta"],["ham","pineapple","peperoni","bacon"]);
console.log(pizza3);

var pizza4 = pizzaOven(["flat bread"],["buffalo"],["goat","parmesan"],["green pepper","onion","garlic","sausage"]);
console.log(pizza4);

var crustType = [
    "deep dish", 
    "hand tossed",
    "cheesy stuffed",
    "flat bread",
    "gluten free",
];

var sauceType = [
    "tranditional",
    "marinara",
    "bbq",
    "white sauce",
    "pesto",
    "buffalo",
    "bbq"
];

var cheeses = [
    "mozzarella",
    "feta",
    "cheddar",
    "swiss cheese",
    "blue cheese",
    "goat cheese",
    "gouda",
    "ricotta",
    "parmesan"
];

var toppings = [
    "pepperoni",
    "sausage",
    "chicken",
    "bell peppers",
    "murshroom",
    "anchovies",
    "onions",
    "black olives",
    "pineapple"
];

function randomRange (max,min) {
    return Math.floor(Math.random()*max-min)+min;
}

function randomPick (arr) {
    var i = Math.floor(arr.length*Math.random());
    return arr[i];
}

function randomPizza() {
    var pizza = [];
    pizza.crustType = randomPick(crustType);
    pizza.sauceType = randomPick(sauceType);
    pizza.cheeses = [];
    pizza.toppings = [];
    for(var i=0; i<randomRange(2,1);i++) {
        pizza.cheeses.push(randomPick(cheeses));
    }
    for(var i=0; i<randomRange(4,2);i++) {
        pizza.toppings.push(randomPick(toppings));
    }
    return pizza;
}

console.log(randomPizza());
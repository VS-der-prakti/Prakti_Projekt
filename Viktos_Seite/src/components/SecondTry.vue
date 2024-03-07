<script setup lang="ts">
const clicked = (car: string) => {
  console.log(car)
  window.location.href = "https://www." + car + ".de"
}
</script>

<template>
<div class="main">
<header>
<h1 class="headline">
Viktors Seite
</h1>
</header>

<body class="cars">
<label for="germancars">
 <a href="https://www.bmw.de/de/index.html"> BMW </a>
 <a href="https://www.mercedes-benz.de/"> Mercedes </a>
 <a href="https://www.audi.de"> Audi </a>
 <img id="germancars" class="image" src="https://news-site-za.s3.af-south-1.amazonaws.com/images/2020/07/germantrio_thumb.png"/>
</label>

 <label for="japanesecars">
 <a href="https://www.nissan.de/"> Nissan </a>
 <a href="https://www.toyota.de/"> Toyota </a>
 <a href="https://www.mazda.de"> Mazda </a>
 <img id="japanesecars" class="image" src="https://imgr1.auto-motor-und-sport.de/Mazda-RX-7-Nissan-Skyline-Toyota-Supra-Frontansicht-jsonLd16x9-f99a69-1074561.jpg"/>
 </label>
 
 <label for="italiencars">
 <a href="https://lamborghini.de"> Lamborghini </a>
 <a href="https://ferrari.de"> Ferrari </a>
 <a href="https://maserati.de"> Maserati </a>
 <img id="italiencars" class="image" src="https://imgr1.auto-motor-und-sport.de/Ferrari-458-Speciale-A-Lamborghini-Aventador-Roadster-Maserati-Gran-Cabrio-MC-169FullWidth-939ff671-850949.jpg"/>
 </label>

 <label for="uscars">
 <a href="https://dodge.de"> Charger Challenger RAM </a>
 <img id="uscars" class="image" src="https://www.dodgegarage.com/news-api/wp-content/uploads/2021/09/dodge-tops-jdp-APEAL-study-576x255.jpg"/>
 </label>

<label for="brittishcars">
 <a href="https://bentley.de"> Bentley </a>
 <a href="https://rolls-royce.de"> Rolls-Royce </a>
 <a href="https://astonmartin-muenchen.de"> Aston Martin </a>
 <img id="brittishcars" class="image" src="https://i.pinimg.com/originals/21/bd/a2/21bda2f64e3b42f9c44786a499d28fe0.jpg"/>
 </label>

 </body>
 </div>
</template>

<style scoped>
.cars{
  display: flex; /* or inline-flex */
  flex-direction: column;
}

.image {
  max-width: 500px;
  -webkit-box-shadow: 5px 5px 15px 1px #000000; 
  box-shadow: 5px 5px 15px 1px #000000;
}

.headline{
  text-align: center;
  text-shadow: 2px 2px 2px #1C6EA4;
}

.main{
  display:flex;
  flex-direction: column;
  justify-content: center;
  width: 100%;
}
</style>

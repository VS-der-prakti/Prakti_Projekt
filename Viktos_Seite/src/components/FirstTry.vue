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
<div class="carsgermany">
 <label for="krakakus"@click="clicked('bmw')"> BMW </label>
 <label @click="clicked('mercedes')"> Mercedes </label>
 <label @click="clicked('audi')"> Audi </label>
 <img id="krakakus" class="image" src="https://news-site-za.s3.af-south-1.amazonaws.com/images/2020/07/germantrio_thumb.png"/>
</div>
 <div class="carsjapan">
 <label @click="clicked('nissan')"> Nissan </label>
 <label @click="clicked('toyota')"> Toyota </label>
 <label @click="clicked('mazda')"> Mazda </label>
 <img class="image" src="https://imgr1.auto-motor-und-sport.de/Mazda-RX-7-Nissan-Skyline-Toyota-Supra-Frontansicht-jsonLd16x9-f99a69-1074561.jpg"/>
 </div>
 <div class="carsitaly">
 <label @click="clicked('lamborghini')"> Lamborghini </label>
 <label @click="clicked('ferrari')"> Ferrari </label>
 <label @click="clicked('maserati')"> Maserati </label>
 <img class="image" src="https://imgr1.auto-motor-und-sport.de/Ferrari-458-Speciale-A-Lamborghini-Aventador-Roadster-Maserati-Gran-Cabrio-MC-169FullWidth-939ff671-850949.jpg"/>
 </div>
 <div class="carsusa">
 <label @click="clicked('dodge')" >Charger Challenger RAM </label>
 <img class="image" src="https://www.dodgegarage.com/news-api/wp-content/uploads/2021/09/dodge-tops-jdp-APEAL-study-576x255.jpg"/>
 </div>
<div class="carsbrittish">
 <label @click="clicked('bentley')"> Bentley </label>
 <label @click="clicked('rolls-royce')"> Rolls-Royce </label>
 <label @click="clicked('astonmartin-muenchen')"> Aston Martin </label>
 <img class="image" src="https://i.pinimg.com/originals/21/bd/a2/21bda2f64e3b42f9c44786a499d28fe0.jpg"/>
 </div>
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

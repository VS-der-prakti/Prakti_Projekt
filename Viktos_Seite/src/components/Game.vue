<script setup lang="ts">
import {ref} from "vue"


    const score = ref(0)
    const highscore = ref(0)

    let deadline = false
    let directionYSpeed = 2
    let directionXSpeed = 1

    let directionY = directionYSpeed
    let directionX = directionXSpeed
document.addEventListener("DOMContentLoaded",()=>{
    let Spielfeld = document.getElementById("Spielfeld") as HTMLElement;
    let Spieler = document.getElementById("Spieler") as HTMLElement;
    let Spielball = document.getElementById("Spielball") as HTMLElement;
    let InitpositionY=parseInt(window.getComputedStyle(Spielball).top);
    let InitpositionX=parseInt(window.getComputedStyle(Spielball).left);
    let Reset = document.getElementById("Reset") as HTMLElement;

Reset.addEventListener("click",()=>{
    deadline = !deadline
})

const get_data = async () => {
    try {
        const response = await fetch("http://localhost:8000/score", {
            method: "GET",
            cache: "no-cache",
            headers: {
                "Content-Type": "application/json"
            }
        });

        const data = await response.json(); // Parse JSON here
        console.log(data["highscore"]);
        
        highscore.value = data["highscore"]; // Use the parsed data
    } catch (error) {
        console.error("Error fetching data:", error);
    }
}
const post_data = async (new_highscore: number) => {
    try{
        const response = await fetch("http://localhost:8000/newscore/", {
            method: "POST",
            cache: "no-cache",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({highscore: new_highscore})
        })
        return response
    } catch (error) {
        console.error("Error fetching data:", error);
    }
}


document.addEventListener("keydown",(Event)=>{
    if("Enter" == Event.key){
        deadline = !deadline
    }
    
    
    if("ArrowRight" == Event.key){
        let left=parseInt(window.getComputedStyle(Spieler).left)
        Spieler.style.left=left +80 +"px"
     }
     if("ArrowLeft" == Event.key){
        let left=parseInt(window.getComputedStyle(Spieler).left)
        Spieler.style.left=left -80 +"px"
     }
    })
    setInterval(()=>{
        let positionY=parseInt(window.getComputedStyle(Spielball).top)
        let positionX=parseInt(window.getComputedStyle(Spielball).left)
        let Rect1 = Spielball.getBoundingClientRect()
        let Rect2 = Spieler.getBoundingClientRect()
        let Rect3 = document.getElementById("topborder").getBoundingClientRect()
        let Rect4 = document.getElementById("leftborder").getBoundingClientRect()
        let Rect5 = document.getElementById("rightborder").getBoundingClientRect()
        let Rect6 = document.getElementById("bottomborder").getBoundingClientRect()

        if(!(Rect1.right<Rect6.left||Rect1.left>Rect6.right)&&!(Rect1.bottom<Rect6.top||Rect1.top>Rect6.bottom)){
          
            deadline = true
        }
        if(!(Rect1.right<Rect5.left||Rect1.left>Rect5.right)&&!(Rect1.bottom<Rect5.top||Rect1.top>Rect5.bottom)){
            directionX = -(directionXSpeed)
        }
        if(!(Rect1.right<Rect4.left||Rect1.left>Rect4.right)&&!(Rect1.bottom<Rect4.top||Rect1.top>Rect4.bottom)){
            directionX = directionXSpeed
        }
        if(!(Rect1.right<Rect3.left||Rect1.left>Rect3.right)&&!(Rect1.bottom<Rect3.top||Rect1.top>Rect3.bottom)){
            directionY = directionYSpeed
        }
        if(!(Rect1.right<Rect2.left||Rect1.left>Rect2.right)&&!(Rect1.bottom<Rect2.top||Rect1.top>Rect2.bottom)){
            directionY = -(directionYSpeed)
            score.value = score.value + 1
        }
        
        if(deadline == false){
        Spielball.style.top = positionY + directionY + "px"
        Spielball.style.left = positionX + directionX + "px"
        }
        
        if (deadline == true){
            if(score.value > highscore.value) {
                post_data(score.value)
                get_data()
            }
            score.value = 0
            Spielball.style.top = InitpositionY + "px"
            Spielball.style.left = InitpositionX + "px"
            positionX = InitpositionX + "px"
            positionY = InitpositionY + "px"
        }

    },5)

    get_data()

})






</script>

<template>
    <div style="display: block; position: absolute; left: 5%; top: 5%">
        <p class="Scoreanzeige" id="Scoreanzeige"> Score: {{ score }}</p>
    <p class="Highscoreanzeige" id="Highscoreanzeige"> Highscore: {{ highscore }}</p>
</div>
    <div class="Spielfeld" id="Spielfeld">
        <div class="topborder" id="topborder"></div>
        <div class="leftborder" id="leftborder"></div>
        <div class="rightborder" id="rightborder"></div>
        <div class="bottomborder" id="bottomborder"></div>
        <div class="Spieler" id="Spieler"></div>
        <div class="Spielball" id="Spielball"></div>
        
    </div>
    <div class="Reset" id="Reset"></div>


</template>

<style scoped>
.Spielfeld{
    height: 40rem; width: 30rem;
    border-top: 4px solid #000000;
    border-right: 4px solid #000000;
    border-left: 4px solid #000000;
    border-bottom: 4px solid #FF0000;
    background-color: #FFFF;
    position: relative;
}
.Spieler{
    height: 10px; width: 100px;
    background-color: #0940FF;
    position: absolute;
    top: 88%;
    left: 50%;
    transform: translateX(-50%);
}
.Spielball{
    height: 10px; width: 10px;
    background-color: #FF0000;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translateX(-50%);
    border-radius: 100px;
    padding: 10px;
}
.topborder{
    position: absolute;
    width: 100%;
    top: 0%; left: 0%;
    height: 4px;
    
}
.leftborder{
    position: absolute;
    height: 100%;
    top: 0%; left: 0%;
    width: 4px;
    
}
.rightborder{
    position: absolute;
    height: 100%;
    top: 0%; right: 0%;
    width: 4px;
    
}
.bottomborder{
    position: absolute;
    width: 100%;
    bottom: 0%; left: 0%;
    height: 4px;
}
.Reset{
    position: relative;
    height: 2.5rem; width: 5rem;
    

}
</style>


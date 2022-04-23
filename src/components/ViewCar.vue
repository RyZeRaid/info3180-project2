<template>
    <br><br><br>
    <div class="carcontainer">
    <div class="card flex-row"  style="width: 75rem">

            
            <img class= "card-img-sm-left" v-bind:src="'/uploads/' + car.photo" alt="Card image" width="570" height="490">
              
            <div class="card-body">
                <h5  class="card-title"> {{ car.year }} {{ car.make }}</h5>
                <p>{{ car.model }}</p>

                <br>
                <p>{{ car.description }}</p>

                <div class="flex">
                    <p>{{ car.price }}</p>
                    <p id="type">{{ car.car_type }}</p>
                    
                </div>
                    
                
            
                

                <div class = "d-flex flex-row bd-highlight mb-3">
                    <div class="flex">
                         <p><i class="fa-solid fa-bed"></i> {{ car.color }} Bedrooms</p> 

                        <p id="distance"><i class="fa-solid fa-bath"></i> {{ car.transmission }} Bathrooms</p>
                    </div>  
                </div>
                

                <button class="btn btn-primary">Email Realtor</button>
                <button :class='{button: button, active:active}'
                type="submit" id='heart'  @click.prevent ="fav"></button>
            </div>
        </div>
    </div>
    
</template>

<script>
    export default {
        data(){
            return{
                car: '',
                selected: '',
                button: true,
                active: false,
                user_id: '',
                unfav: '',
            }
        },
        created() {
            this.get_data();
            this.getCsrfToken();
        },
        methods: {
            get_data(){
                
                fetch("/api/cars/" + this.$route.params.id +"/"+ this.$store.state.uid, {
                    method: 'GET',
                })
                .then((response) => response.json())
                .then((data) => {
                    console.log(data);
                    if (this.active != true && data.fav == true){
                        
                        this.active = true
                    }
                    this.car = data
                })
                .catch(function (error) {
                    console.log(error);
                });

                
            },
            fav(){
                if(this.active != true) {
                    this.active = true
                }else{
                    this.active = false
                    this.unfav= false
                }
                
                fetch("/api/cars/" + this.car.id +"/favourite", {
                    method: 'POST',
                    body: JSON.stringify({user_id: this.user_id, unfav:this.unfav}),
                    headers:{'X-CSRFToken': this.csrf_token,'Content-Type': 'application/json'},
                })
                .then((response) => response.json())
                .then((data) => {
                    console.log("show me the message",data);
                    //this.car = data
                })
                .catch(function (error) {
                    console.log(error);
                });
            },
             getCsrfToken(){
                this.sendid()
                const user = this.$store.state.auth
                console.log(user)
                let self = this;
                fetch('/api/csrf-token')
                    .then((response) => response.json())
                    .then((data) => {
                    console.log(data);
                    self.csrf_token = data.csrf_token;
                })
            },
            sendid(){
                this.user_id = this.$store.state.uid
                console.log("this is the id ", this.user_id )
            }
        }
        
    }    
</script>


<style>

.carcontainer{
    display: flex;
    justify-content: center;
    align-items: center;
}
    body {
  background-color: #f3f4f6;
}


.button{
	width: 50px;
	height: 50px;
  top:85%;
  border: none;
  position: absolute;
	left: 93%;
	margin-top: -45px;
	margin-left: -50px;
	border-radius: 5px;
	background: none;
	cursor: pointer;
	transition: background 0.8s ease;
}

.active#heart:before,.active#heart:after{
	background: red !important;
}
#heart {
    width: 100px;
    height: 90px;
    transition: background 0.5s ease;
}
#heart:before,
#heart:after {
	transition: background 0.5s ease;
    position: absolute;
    content: "";
    left: 50px;
    top: 0;
    width: 50px;
    height: 80px;
    background: dimgrey;
    border-radius: 50px 50px 0 0;
    transform: rotate(-45deg);
    transform-origin: 0 100%;
}
#heart:after {
    left: 0;
    transform: rotate(45deg);
    transform-origin :100% 100%;
}






</style>
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
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        data(){
            return{
                car: '',
            }
        },
        created() {
            this.get_data();
        },
        methods: {
            get_data(){
                fetch("/api/cars/" + this.$route.params.id, {
                    method: 'GET'
                })
                .then((response) => response.json())
                .then((data) => {
                    console.log(data);
                    this.car = data
                })
                .catch(function (error) {
                    console.log(error);
                });
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
</style>
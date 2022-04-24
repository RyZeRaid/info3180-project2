<template>

<div class="profilecontainer">
    <div class="card flex-row"  style="width: 45rem">

        <img class="card-img-sm-left profilepic" v-bind:src="'/uploads/' + user.photo" alt="Card image" width="140" height="140">
        <div class="card-body">
                <h5  class="card-title">{{ user.name }}</h5>
                <p>@{{ user.username }}</p>
                <br>
                <p>{{ user.biography }}</p>
                <p>Email {{ user.email }}</p>
                <p>Location {{ user.location}}</p>
                <p>Joined {{ user.date_joined }}2</p>  
        </div>
    </div>
    <br>
    <h2 class="favs_cars">Cars Favourited</h2>
    <br>
    <div v-if="cars != [] " >
        <div class="container_view">
        
        <div v-for="car in cars" :key="car.id">
            <div class = "grid_view">
                <div class="card text-left" style="width: 18rem;">
                    <img class="card-img-top" v-bind:src= "'/uploads/' + car.photo"  alt="Car" width="250" height="200">
                    <div class="card-body">
                        <h5 class="card-title">{{ car.year }} {{ car.make }}</h5>
                        <p>{{ car.model }}</p>
                        <div class="bubble">
                            {{ car.price }}        
                        </div>
                    </div>  
                    <div v-if="this.$store.state.uid != '' ">
                    <RouterLink class="a" v-bind:to="'/cars/' + car.id + '/'+ this.$store.state.uid">
                       
                        <div class="card-footer">
                            View more details
                        </div>
                    </RouterLink>
                    </div>
                    <div v-else>
                        <RouterLink class="a" v-bind:to="'/cars/' + car.id + '/'+ this.$store.state.id">
                       
                        <div class="card-footer">
                            View more details
                        </div>
                    </RouterLink>
                    </div>
                </div>
            </div> 
            </div>
            </div>
    </div>
</div>



</template>

<script>
    export default {
        data(){
            return{
                user_id: '',
                user: '',
                cars: [],
            }
        },
        created() {
            this.sendid();
            this.get_data();
            this.get_favs();
        
        },
        methods: {
            get_data(){
                fetch("/api/users/" + this.user_id, {
                    method: 'GET',
                })
                .then((response) => response.json())
                .then((data) => {
                    this.user = data
                    
                })
                .catch(function (error) {
                    console.log(error);
                });
            },
            sendid(){
                if(this.$store.state.uid != ''){
                    this.user_id = this.$store.state.uid
                }else{
                    this.user_id = this.$store.state.id
                }
            },
            get_favs(){
                fetch("/api/users/" + this.user_id + "/favourites", {
                    method: 'GET',
                })
                .then((response) => response.json())
                .then((data) => {
                    this.cars.push(...data)
                    
                })
                .catch(function (error) {
                    console.log(error);
                });
            }
        }
    }
</script>

<style>

    .card-img-top{
        width: 100%;
        height: 15vw;
        object-fit: cover;
    }

    .favs_cars{
        font-size: 2em;
    }

    .profilepic{
        margin: 11px;
        border-radius: 50%;
    }

    .profilecontainer{
        margin-top: 40px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    body{
        background-color: #f3f4f6;
    }

    .card-footer {
    background-color: #15b8a7;
}

.a {
    text-decoration: none;
    font-weight: bold;
    color: white;
    text-align: center;
}

.bubble {
    background-color: #5fa4fa;
    border-radius: 17px;
    width: fit-content;
    padding: 4px;
    color: white;
}

.grid_view {
    padding-left: 20px;
    padding-bottom: 20px;
}

.container_view {
    max-width: 100%;
    flex-wrap: wrap;
    display: flex;
    justify-content: center;
    align-items: center;
}

</style>
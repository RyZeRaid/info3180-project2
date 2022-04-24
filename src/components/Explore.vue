<template>
    <br>
    <h2 class="page-header" id="explore-head">Explore</h2>
    <br>
    <div id="explore-card" class="card text-left" style="width: 48rem;">
        <form id="search">
            <div class="row mb-2">
                <div class="col-auto">
                    <div class="form-group">
                        <label for="make">Make</label>
                        <input name="make" v-model="make" placeholder="Make" class="form-control explore-field">
                    </div>
                </div>
                <div class="col-auto">
                    <div class="form-group">
                        <label for="model">Model</label>
                        <input name="model" v-model="model" placeholder="Model" class="form-control explore-field">
                    </div>
                </div>
                <div class="col-auto">
                    <div class="form-group">
                        <br>
                        <button type="button" class="btn btn-success" @click.prevent= "search" >Search</button>
                    </div>
                </div>
            </div>
        </form>

    </div>
    <br>
    <div v-if="carsearch != [] " >
        <div class="container_view">
        
        <div v-for="car in carsearch" :key="car.id">
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
                    
                </div>
            </div> 
            </div>
            </div>
    </div>
   
    
</template>

<script>

    
    export default {
    data() {
        return {
          csrf_token: '',
          link: '',
          carsearch:[],
        };
    },
    created() {
        this.getCars();
        this.getCsrfToken();
        
    },
    methods: {
        search(){
            this.carsearch = []
            let searchForm = document.getElementById('search');
            let form_data = new FormData(searchForm);

             fetch('/api/search',{
                method: 'POST', 
                body: form_data,
                headers: {'X-CSRFToken': this.csrf_token}
             })

            .then((response) => response.json())
            .then((data) => {
               console.log("came to data") 
               console.log(data);
               this.carsearch.push(...data)
            //self.csrf_token = data.csrf_token;
            })
            .catch(function (error) {
                console.log(error);
            });
        },
        getCars(){
            
            this.cars = []
      let self = this;
      fetch('/api/cars')
        .then((response) => response.json())
        .then((data) => {
          console.log("this is hte car",data);
          this.carsearch.push(...data)
          //self.csrf_token = data.csrf_token;
        })
        .catch(function (error) {
              console.log(error);
          });
    },
    getCsrfToken(){
      console.log("thisis the state when logged",this.$store.state.auth)
      let self = this;
      fetch('/api/csrf-token')
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
          self.csrf_token = data.csrf_token;
        })
    },
  }  
    }


</script>

<style>

.card-img-top{
    width: 100%;
    height: 15vw;
    object-fit: cover;
}

#explore-head {
    font-size: 2em;
}

#explore-card {
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 19px;
}


#form1{
    display: flex;
    justify-content: center;
}

.explore-field{
    width: 300px;
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
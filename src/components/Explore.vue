<template>
    <br>
    <h2 class="page-header" id="explore-head">Explore</h2>
    <br>
    <div id="explore-card" class="card text-left" style="width: 48rem;">
        <form id="form1">
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
                        <button type="button" class="btn btn-success">Search</button>
                    </div>
                </div>
            </div>
        </form>

    </div>
    <br>
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

                <RouterLink class="a" v-bind:to="'/cars/' + car.id">
                    <div class="card-footer">
                        View more details
                    </div>
                </RouterLink>
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
          cars: [],
          link: '',
        };
    },
    created() {
        this.getCars();
    },
    methods: {
        getCars(){
      let self = this;
      fetch('/api/cars')
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
          this.cars.push(...data)
          //self.csrf_token = data.csrf_token;
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
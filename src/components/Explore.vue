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
    <div v-for="car in cars" :key="car.id">
            <img src="../uploads/Car.jpg" alt="">
            <p>{{ car.make }}</p>
        </div>
    
</template>

<script>

    
    export default {
    data() {
        return {
          csrf_token: '',
          cars: [],
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
    },
  }  
    }


</script>

<style>

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



</style>
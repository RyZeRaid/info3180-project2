<template>
    <h2 class="page-header" id="pgheader">Add New Car</h2>

<div class="card text-left" style="width: 48rem; " id = "card">
<div class="card-body">
<form  id = "AddNewCar" >
  
  <div class="row mb-2">
    <div class="col-auto">
      <div class="form-group">
        <label for="make">Make</label>
        <input name="make" v-model="make" placeholder="Make" class="form-control register-form">
        </div>
    </div>
    <div class="col-auto">
      <div class="form-group">
        <label for="model">Model</label>
        <input name="model" v-model="model" placeholder="Model" class="form-control register-form">
        </div>
    </div>
  </div>

  <div class="row mb-2">
    <div class="col-auto">
      <div class="form-group">
        <label for="colour">Colour</label>
        <input name="colour" v-model="colour" placeholder="Colour" class="form-control register-form">
        </div>
    </div>
    <div class="col-auto">
      <div class="form-group">
        <label for="year">Year</label>
        <input name="year" v-model="year" placeholder="2022" class="form-control register-form">
        </div>
    </div>
  </div>

    <div class="row mb-2">
        <div class="col-auto">
            <div class="form-group">
                <label for="price">Price</label>
                <input name="price" v-model="price" placeholder="62888" class="form-control register-form">
            </div>
        </div>
        <div class="col-auto">
                <div class="form-group">
                    <label for="type">Car Type</label>
                    <select name="type" id="cars" class="form-select register-form">
                        <option value="suv">SUV</option>
                        <option value="volvo">Volvo</option>
                        <option value="saab">Saab</option>
                        <option value="mercedes">Mercedes</option>
                        <option value="audi">Audi</option>
                    </select>
                </div>
        </div>
  </div>

  <div class="row mb-1">
        <div class="col-auto">
            <div class="form-group">
                <label for="transmission">Transmission</label>
                <select name="transmission" id="transmission" class="form-select register-form">
                        <option value="automatic">Automatic</option>
                        <option value="manual">Manual</option>
                    </select>
            </div>
        </div>
  </div>


    <div class="form-group">
        <label for="description">Description</label>
        <textarea name="description" v-model="description"
            id="description" class="mb-2 mr-sm-2 form-control" placeholder="Add Description"></textarea>
    </div>
   
    <div class="form-group">
      <label for="photo">Upload Photo</label>
        <input class="form-control register-form" type="file" id="photo" name="photo" @change="selectImage">
    </div>
    <input type="hidden" name="user_id" id="user_id" :value = "this.$store.state.id" >
  
  <br>
  <div class="col-12">
    <button id="btn1" typve="submit" name="submit" class="btn btn-primary" @click.prevent="addcar">Save</button>
    <button type="reset" name="reset" class="btn btn-warning">Undo all</button>
  </div>
</form>
</div>
</div>
</template>

<script>
export default {
    data() {
        return {
          csrf_token: '',
          description: '',
          photo:'',
          make: '',
          model: '',
          colour: '',
          year: '',
          price: '',
          type: '',
          transmission: '',
          user_id: '',
        }
    },
    created() {
        this.getCsrfToken();
        
    },
  methods: {
    addcar(){
      
      let newCarForm = document.getElementById('AddNewCar');
      let form_data = new FormData(newCarForm);
      
      console.log(form_data)
      
        fetch("/api/addcar", {
            method: 'POST', 
            body: form_data,
            headers: {'X-CSRFToken': this.csrf_token},
          })
          .then(function (response) {
                return response.json();
          })
          .then(() =>  {

          // display a success message
            console.log("worked success")
            this.$router.push({name: 'home'})
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
      this.user_id = this.$store.state.id
      console.log("this is the id ", this.user_id )
    }
  }  
}


</script>

<style>

label {
    font-weight: bold;
    font-size: 0.8em;
  }
.register-form {
  width: 350px;
}

.page-header{
  font-size: 2em;
}

</style>
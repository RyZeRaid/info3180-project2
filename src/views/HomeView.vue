<script>
export default {
    data() {
        return {
            
            message: "Hello World! This is Lab 7"
        };
    },
}
</script>

<template>
  <div class="con">
    <div class="home">
      <div id="text">
        <h2>Buy and Sell <br> Cars Online</h2>
        <p>United Auto Sales provies the fastest easiest firendly way to buy or sell cars online. Find a Great Price on the Vehicle on the Vehicle You Want.</p>
        <RouterLink type="button" to="/register" class="btn btn-primary" id="btn1">Register</RouterLink>
        <RouterLink type="button" to="/login" class="btn btn-success">Login</RouterLink>
      </div>
      <div id="car">
        <img class="homeimg" src="../img/Car.jpg" alt="">
      </div>
    </div>
  </div>
</template>

<style>

  h2 {
    font-size: 4em;
  }

  p {
    margin-right: 90px;
    color: gray;
  }

  #btn1{
    margin-right: 10px;
  }

  .home {
    display: flex;
    align-items: center;
    justify-content: center;
  }

  #text {
    padding-left: 6em;
  }

  body{
    padding-top: 55px;
    background-color: white;
  }

  .homeimg {
    height: calc(100vh - 55px);
  }


</style>
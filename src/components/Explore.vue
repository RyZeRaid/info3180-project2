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
</template>

<script>
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
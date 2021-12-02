<script lang="ts">
    import Days from '../components/Days.svelte'
    import Snowman from "../components/Snowman.svelte";
</script>

<div class="row">
    <Snowman/>
    <h1>Advent of Code 2021 🎄</h1>
</div>
<div class="days">
    <Days/>
</div>

<style>
    .row {
        display: flex;
        margin-top: 30px;
        justify-content: center;
    }
</style>
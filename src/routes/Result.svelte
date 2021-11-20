<script lang="ts">
    import {Link} from "svelte-routing";

    export let day = 0
    export let part1 = 0
    export let part2 = 0
</script>


<h1>Day {day}</h1>
<div class="container">
    <h2>🎁 Part 1</h2>
    <span></span>
    <h2>{part1}</h2>
    <h2>🎁 Part 2</h2>
    <span></span>
    <h2>{part2}</h2>
    <div class="center">
        <Link to="/">☃️ Back</Link>
    </div>

</div>

<style>
    .container {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        grid-column-gap: 5vw;
        grid-row-gap: 5vh;
    }

    .center {
        grid-row-start: 3;
        grid-column-start: 2;
        grid-column-end: 2;
    }
</style>
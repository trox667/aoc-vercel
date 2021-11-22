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
    {#if part1 !== 0}
        <div class="result">
            <img alt="Python Programming Language Logo" height="32" src="/python.svg" width="32">
            <h3>{part1}</h3>
        </div>
    {:else}
        <h2>🚧</h2>
    {/if}
    <h2>🎁 Part 2</h2>
    <span></span>
    {#if part2 !== 0}
        <div class="result">
            <img alt="Python Programming Language Logo" height="32" src="/python.svg" width="32">
            <h3>{part2}</h3>
        </div>
    {:else}
        <h2>🚧</h2>
    {/if}
    <div class="offset">
        <Link to="/">☃️ Back</Link>
    </div>
</div>

<style>
    .result {
        display: flex;
        justify-content: space-evenly;
        width: 30%;
        margin: 0 auto;
    }

    .result h3 {
        margin: 0;
    }

    .container {
        display: flex;
        flex-direction: column;
        width: 100%;
    }

    .offset {
        margin-top: 5vh;
    }
</style>
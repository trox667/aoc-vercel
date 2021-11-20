<script lang="ts">
    import {Link} from "svelte-routing";

    export let day = 0
    export let part1 = 0
    export let part2 = 0
</script>


<h1>Day: {day} </h1>
<h2>Part 1: {part1}</h2>
<h2>Part 2: {part2}</h2>
<Link to="/">Back</Link>
<script lang="ts">
    import Day from './Day.svelte'
    import FoldCard from "./components/FoldCard.svelte";
    import PaperCard from "./components/PaperCard.svelte";

    export let days = 25
    const dayIndices = []
    for (let i = 1; i <= days; ++i) dayIndices.push(i)
</script>

<div class="days">
    {#each dayIndices as dayIndex}
        <Day day="{dayIndex}"/>
    {/each}
</div>

<style>
    .days {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
        grid-column-gap: 5px;
        grid-row-gap: 20px;
    }
</style>
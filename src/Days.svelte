<script lang="ts">
    import Day from './Day.svelte'
    import {dayIndices as dayIndicesStore} from "./stores/days";

    let dayIndices = []
    dayIndicesStore.subscribe(value => dayIndices = [...value])

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
        grid-column-gap: 5vw;
        grid-row-gap: 5vh;
    }
</style>
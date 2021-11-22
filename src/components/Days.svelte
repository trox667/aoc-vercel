<script lang="ts">
    import Day from './Day.svelte'
    import {dayIndices as dayIndicesStore} from "../stores/days";

    let dayIndices = []
    dayIndicesStore.subscribe(value => dayIndices = [...value])

</script>

<div class="days">
    {#each dayIndices as dayIndex}
        <div class="day">
            <Day day="{dayIndex}"/>
        </div>
    {/each}
</div>

<style>
    .days {
        display: flex;
        flex-wrap: wrap;
        width: 100%;
    }

    .day {
        flex: 1 0 17%;
        margin: 1vh;
    }
</style>
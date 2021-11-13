<script>
    import Day from './day.svelte'
</script>

<div class="days">
    <Day day="1"/>
    <Day day="2"/>
    <Day day="3"/>
    <Day day="4"/>
    <Day day="5"/>
</div>

<style>
    .days {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
        grid-column-gap: 5px;
    }
</style>
<script lang="ts">
    import Day from './Day.svelte'
    import FoldCard from "./FoldCard.svelte";
    import PaperCard from "./PaperCard.svelte";
</script>

<div class="days">
    <PaperCard />
    <PaperCard />
    <PaperCard />
    <PaperCard />
    <PaperCard />
<!--    <FoldCard />-->
<!--    <FoldCard />-->
<!--    <FoldCard />-->
<!--    <FoldCard />-->
<!--    <FoldCard />-->
<!--    <Day day="1"/>-->
<!--    <Day day="2"/>-->
<!--    <Day day="3"/>-->
<!--    <Day day="4"/>-->
<!--    <Day day="5"/>-->

<!--    <Day day="6"/>-->
<!--    <Day day="7"/>-->
<!--    <Day day="8"/>-->
<!--    <Day day="9"/>-->
<!--    <Day day="10"/>-->
</div>

<style>
    .days {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
        grid-column-gap: 5px;
        grid-row-gap: 20px;
    }
</style>
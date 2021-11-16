<script lang="ts">
    import PaperCard from "./components/PaperCard.svelte";

    export let day = 0

    const openDay = (_) => {
        console.log("selected", day)
    }

</script>

<div on:click={openDay}>
    <PaperCard>
        <div slot="content">
            <div class="day-container day"></div>
        </div>
        <div slot="front">
            <h2>{day}</h2>
        </div>
    </PaperCard>
</div>

<style>
    .day {
        position: absolute;
        top: 20px;
        left: 20px;
        background-image: url("../present.png");
        background-size: cover;
        background-repeat: no-repeat;
        box-shadow: 0 0 5px 5px rgb(0 0 0 / 0.2);
        height: 60px;
        width: 60px;
        /*line-height: 10vw;*/
        color: #60483E;
    }

    .day-number {
        min-width: 50px;
        width: 10vw;
    }

    /*https://css-tricks.com/snippets/css/shake-css-keyframe-animation/*/
    @keyframes shake {
        10%, 90% {
            transform: translate3d(-1px, 1px, 0);
        }
        20%, 80% {
            transform: translate3d(2px, -2px, 0);
        }
        30%, 50%, 70% {
            transform: translate3d(-4px, 2px, 0);
        }
        40%, 60% {
            transform: translate3d(4px, -2px, 0);
        }
    }

    .day-container:hover {
        animation: shake 0.82s cubic-bezier(.36, .07, .19, .97) both;
        transform: translate3d(0, 0, 0);
        backface-visibility: hidden;
        perspective: 1000px;
    }
</style>
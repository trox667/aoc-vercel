<script lang="ts">
    export let day = 0

    const openDay = (event) => {
        console.log("selected", Day)
    }

</script>

<div on:click={openDay} class="day-container">
    <div class="day">

    </div>
    <div class="day-number">
    Day {day}
    </div>
</div>

<style>
    .day {
        background-image: url("../present.png");
        background-size: cover;
        background-repeat: no-repeat;
        min-width: 50px;
        min-height: 50px;
        height: 10vw;
        width: 10vw;
        line-height: 10vw;
        color: #60483E;
    }

    .day-number {
        min-width: 50px;
        width: 10vw;
    }

    /*https://css-tricks.com/snippets/css/shake-css-keyframe-animation/*/
    @keyframes shake {
        10%, 90% {
            transform: translate3d(-1px, 0, 0);
        }
        20%, 80% {
            transform: translate3d(2px, 0, 0);
        }
        30%, 50%, 70% {
            transform: translate3d(-4px, 0, 0);
        }
        40%, 60% {
            transform: translate3d(4px, 0, 0);
        }
    }

    .day-container:hover {
        animation: shake 0.82s cubic-bezier(.36, .07, .19, .97) both;
        transform: translate3d(0, 0, 0);
        backface-visibility: hidden;
        perspective: 1000px;
    }
</style>
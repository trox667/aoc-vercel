<script>
    export let day = 0
</script>

<div class="day">
    Day {day}
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

    .day:hover {
        animation: shake 0.82s cubic-bezier(.36, .07, .19, .97) both;
        transform: translate3d(0, 0, 0);
        backface-visibility: hidden;
        perspective: 1000px;
    }
</style>
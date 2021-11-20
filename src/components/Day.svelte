<script lang="ts">
    import PaperCard from "./PaperCard.svelte";
    import {onMount} from "svelte";
    import {navigate} from "svelte-routing";

    enum ResultCompletion {
        None,
        Part1,
        Part2,
        Done
    }

    class Result {
        constructor(public part1 = 0, public part2 = 0) {
        }

        static fromResponse(text: string): Result {
            if (text.startsWith('error: '))
                return new Result()

            const [part1, part2] = text.split(',')
            try {
                return new Result(parseInt(part1), parseInt(part2))
            } catch (e) {
                return new Result()
            }
        }

        isCompleted(): ResultCompletion {
            if (this.part1 === 0 && this.part2 === 0)
                return ResultCompletion.None
            else if (this.part1 !== 0 && this.part2 === 0)
                return ResultCompletion.Part1
            else if (this.part1 === 0 && this.part2 !== 0)
                return ResultCompletion.Part2
            else
                return ResultCompletion.Done
        }
    }

    const openDay = async (_) => {
        navigate(`/result/${day}/${result.part1}/${result.part2}`)
    }

    const canBeOpened = () => {
        const date = new Date()
        const currentDay = date.getDate()
        const currentMonth = date.getMonth() + 1
        const currentYear = date.getFullYear()

        if (currentYear === 2021) {
            if (currentMonth === 11) {
                if (currentDay >= day) {
                    return true
                }
            }
        } else if (currentYear > 2021) {
            return true
        }

        return false
    }

    onMount(async () => {
        if (canBeOpened()) {
            const response = await fetch(`/api?day=${day}`)
            if (response.status === 200) {
                result = Result.fromResponse(await response.text())
            }
        }
    })


    export let day = 0
    let result: Result = new Result()
</script>

<div on:click={openDay}>
    <PaperCard canBeOpened="{canBeOpened()}">
        <div slot="content">
            <div class="day-container day"></div>
        </div>
        <div slot="front">
            <h2 class="day-christmas">{day}</h2>
            {#if result.isCompleted() === ResultCompletion.Part1 || result.isCompleted() === ResultCompletion.Part2}
                <span>️⭐️</span>
            {:else if result.isCompleted() === ResultCompletion.Done}
                <span>⭐️⭐️</span>
            {:else}
                <span></span>
            {/if}

        </div>
    </PaperCard>
</div>

<style>
    .day-christmas {
        font-family: 'Mountains of Christmas', 'serif';
        font-size: 3em;
        font-weight: bold;
        margin: 0;
    }

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
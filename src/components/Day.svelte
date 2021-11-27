<script lang="ts">
    import PaperCard from './PaperCard.svelte'
    import { onMount } from 'svelte'

    enum ResultCompletion {
        None,
        Part1,
        Part2,
        Done,
    }

    class Result {
        constructor(public part1 = 0, public part2 = 0) {}

        static fromResponse(text: string): Result {
            if (text.startsWith('error: ')) return new Result()

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
            else return ResultCompletion.Done
        }
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

<div>
    <PaperCard canBeOpened={canBeOpened()}>
        <div slot="content" class="content">
            <div>
                <div>🎁
                    {result.part1}
                </div>
                <div>🎁
                    {result.part2}
                </div>
            </div>
        </div>
        <div slot="front">
            <h2 class="day-christmas">{day}</h2>
            {#if result.isCompleted() === ResultCompletion.Part1 || result.isCompleted() === ResultCompletion.Part2}
                <span>️⭐️</span>
            {:else if result.isCompleted() === ResultCompletion.Done}
                <span>⭐️⭐️</span>
            {:else}
                <span />
            {/if}
        </div>
    </PaperCard>
</div>

<style>
    .content {
        font-size: 1.25em;
    }

    .day-christmas {
        font-family: 'Mountains of Christmas', 'serif';
        font-size: 3em;
        font-weight: bold;
        margin: 0;
    }
</style>

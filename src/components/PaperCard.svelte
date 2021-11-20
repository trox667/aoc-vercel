<script lang="ts">
    enum PaperAction {
        OPENING,
        CLOSING,
        NONE,
    }

    enum PaperState {
        OPEN,
        COVERED,
    }

    const actionOpening = (_) => action = PaperAction.OPENING

    const actionClosing = (_) => action = PaperAction.CLOSING

    const actionTransition = (_) => {
        if (state === PaperState.COVERED)
            state = PaperState.OPEN
        else
            state = PaperState.COVERED
    }

    let action = PaperAction.NONE
    let state = PaperState.COVERED
    export let canBeOpened = false
</script>

<div class="card"
     on:mouseleave={canBeOpened ? actionClosing : () => {}}
     on:mouseover={canBeOpened ? actionOpening : () => {}}
     on:transitionend={canBeOpened ? actionTransition : () => {}}>
    <div class="content">
        <slot name="content"></slot>
    </div>
    {#if state === PaperState.COVERED}
        <div class={"inner " + (action === PaperAction.OPENING ? "opening" : "")}>
            <div class="front">
                <slot name="front"></slot>
            </div>
            <div class="back">
                <slot name="back"></slot>
            </div>
        </div>
    {:else}
        <div
                class={"inner opening " +
        (action === PaperAction.CLOSING ? "closing" : "")}
        >
            <div class="front">
                <slot name="front"></slot>
            </div>
            <div class="back">
                <slot name="back"></slot>
            </div>
        </div>
    {/if}
</div>

<style>
    .card {
        width: 100px;
        height: 100px;
        perspective: 1000px;
    }

    .content {
        position: absolute;
        background-color: #dc7652;
        text-align: center;
        width: 100%;
        height: 100%;
    }

    .inner {
        position: relative;
        width: 100%;
        height: 100%;

        transform-style: preserve-3d;
    }

    .opening {
        transform: rotateY(-100deg);
        transform-origin: 0;
        transition: transform 2s;
    }

    .closing {
        transform: rotateY(0deg);
        transform-origin: 0;
        transition: transform 2s;
    }

    .front,
    .back {
        position: absolute;
        width: 100%;
        height: 100%;
        backface-visibility: hidden;
    }

    .front {
        background-color: #60483e;
    }

    .back {
        transform: rotateY(180deg);
        background-color: #dc7652;
    }
</style>

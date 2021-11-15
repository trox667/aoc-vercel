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
  let action = PaperAction.NONE;
  let state = PaperState.COVERED;
</script>

<div
  class="card"
  on:mouseover={(e) => {
    action = PaperAction.OPENING;
  }}
  on:mouseleave={(e) => {
    action = PaperAction.CLOSING;
  }}
  on:transitionend={(e) => {
    if (state === PaperState.COVERED) state = PaperState.OPEN;
    else state = PaperState.COVERED;
  }}
>
  <div class="content">foo</div>
  {#if state === PaperState.COVERED}
    <div class={"inner " + (action == PaperAction.OPENING ? "opening" : "")}>
      <div class="front">Frontface</div>
      <div class="back">Backface</div>
    </div>
  {:else}
    <div
      class={"inner opening " +
        (action == PaperAction.CLOSING ? "closing" : "")}
    >
      <div class="front">Frontface</div>
      <div class="back">Backface</div>
    </div>
  {/if}
</div>

<style>
  .card {
    width: 10vw;
    height: 10vw;
    perspective: 1000px;
  }

  .content {
    position: absolute;
    background-color: #60483e;
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

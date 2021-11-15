<script lang="ts">
    enum PaperAnimation {
        SHOW,
        HIDE,
        BACK,
    }
    let visible = PaperAnimation.HIDE

    // https://www.w3schools.com/howto/howto_css_flip_card.asp
</script>

<div class="container" on:mouseover={(e) => {visible=PaperAnimation.SHOW}} on:mouseleave={(e) => {visible = PaperAnimation.BACK}}>
    <div class="back">
        Test
    </div>
    {#if visible === PaperAnimation.SHOW}
        <div class="open">
        </div>
    {:else if visible === PaperAnimation.BACK}
        <div class="close">
        </div>
    {:else}
        <div class="cover">
        </div>
    {/if}
</div>

<style>
    @keyframes fold {
        from {
            left: 0;
            background-color: #DC7652;
        }

        to {
            left: -10vw;
            background-color: red;
        }
    }

    .container {
        height: 10vw;
        width: 10vw;
        position: relative;
    }

    .open {
        display: inline-block;
        height: 100%;
        width: 100%;
        position: absolute;
        top: 0;
        left: 0;
        background-color: #DC7652;
        animation: fold 1s cubic-bezier(.36, .07, .19, .97) forwards;
    }

    .close {
        display: inline-block;
        height: 100%;
        width: 100%;
        position: absolute;
        top: 0;
        left: 0;
        background-color: #DC7652;
        animation: fold 1s cubic-bezier(.36, .07, .19, .97) reverse;
    }

    .cover {
        display: inline-block;
        height: 100%;
        width: 100%;
        position: absolute;
        top: 0;
        left: 0;
        background-color: #DC7652;
    }

    /*.open:hover */
    /*    animation: fold 1s cubic-bezier(.36, .07, .19, .97) forwards;*/
    /*    !*animation-iteration-count: 1;*!*/
    /*}*/

    .back {
        display: inline-block;
        height: 100%;
        width: 100%;
        position: absolute;
        top: 0;
        left: 0;
        background-color: #60483E;
    }
</style>


<script lang="ts">
    // https://www.npmjs.com/package/svelte-routing
    import {Link, Route, Router} from 'svelte-routing'
    import Home from "./routes/Home.svelte";
    import {dayIndices} from "./stores/days";
    import Result from "./routes/Result.svelte";

    dayIndices.set([12, 21, 20, 2, 7, 11, 1, 22, 13, 6, 9, 10, 23, 5, 17, 8, 4, 24, 15, 18, 14, 25, 16, 19, 3])

    export let url = ""
</script>

<Router url="{url}">
    <nav>
        <Link to="/">Home</Link>
        <div class="right">
            <a href="https://www.adventofcode.com" target="_blank">
                <img alt="Advent of Code Logo" height="32" src="adventofcode.png" width="32">
            </a>
            <a href="https://www.svelte.dev" target="_blank">
                <img alt="Svelte JS UI Framework Logo" height="32" src="svelte.svg" width="32">
            </a>
            <a href="https://www.python.org" target="_blank">
                <img alt="Python Programming Language Logo" height="32" src="python.svg" width="32">
            </a>
            <a href="https://github.com/trox667" target="_blank">
                <img alt="Github Logo" height="32" src="github.png" width="32">
            </a>
        </div>
    </nav>
    <main>
        <Route path="/">
            <Home/>
        </Route>
        <Route let:params path="/result/:day/:part1/:part2">
            <Result day="{params.day}" part1="{parseInt(params.part1)}" part2="{parseInt(params.part2)}"/>
        </Route>
    </main>
</Router>

<style>
    nav {
        display: flex;
        justify-content: space-around;
        position: fixed;
        width: 100%;
        padding: 5px;
        margin: 0 auto;
        background: #6f313c;
        min-height: 2vh;
        text-align: center;
        line-height: 2vh;
    }

    main {
        text-align: center;
        margin: 0 auto;
        width: 100%;
    }

    h1 {
        color: black;
        text-transform: uppercase;
        font-size: 4em;
        font-weight: 100;
    }

    @media (min-width: 640px) {
        main {
            max-width: none;
        }
    }

    .right {
        margin: 0 10px auto auto;
    }
</style>
<script lang="ts">
    // https://www.npmjs.com/package/svelte-routing
    import {Router, Link, Route} from 'svelte-routing'
    import Home from "./routes/Home.svelte";
    import About from "./routes/About.svelte";
    import {dayIndices} from "./stores/days";
    import Result from "./routes/Result.svelte";

    dayIndices.set([12, 21, 20, 2, 7, 11, 1, 22, 13, 6, 9, 10, 23, 5, 17, 8, 4, 24, 15, 18, 14, 25, 16, 19, 3])

    export let url = ""
</script>

<Router url="{url}">
    <nav>
        <Link to="/">Home</Link>
        <Link to="about">About</Link>
    </nav>
    <main>
        <Route path="/">
            <Home/>
        </Route>
        <Route path="/about">
            <About/>
        </Route>
        <Route path="/result/:day/:part1/:part2" let:params>
            <Result day="{params.day}" part1="{params.part1}" part2="{params.part2}"/>
        </Route>
    </main>
    <footer>
        <div class="footer-container">
            <a href="https://www.adventofcode.com" target="_blank">
                <img src="adventofcode.png" width="32" height="32" alt="Advent of Code Logo">
            </a>
            <a href="https://www.svelte.dev" target="_blank">
                <img src="svelte.svg" width="32" height="32" alt="Svelte JS UI Framework Logo">
            </a>
            <a href="https://www.python.org" target="_blank">
            <img src="python.svg" width="32" height="32" alt="Python Programming Language Logo">
            </a>
        </div>
    </footer>
</Router>

<style>
    nav {
        display: flex;
        justify-content: space-around;
        position: fixed;
        width: 100%;
        padding: 5px;
        margin: 0 auto;
        background: #DC7652;
        min-height: 2vh;
        text-align: center;
        line-height: 2vh;
    }

    main {
        text-align: center;
        padding: 1em;
        max-width: 240px;
        margin: 0 auto;
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

    footer {
        margin: auto auto 0 0;
        width: 100%;
        background: #60483e;
    }

    .footer-container {
        padding: 5px;
        min-height: 2vh;
        vertical-align: center;
        text-align: center;
    }
</style>
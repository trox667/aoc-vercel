<script lang="ts">
    // https://www.npmjs.com/package/svelte-routing
    import {Router, Link, Route} from 'svelte-routing'
    import Home from "./routes/Home.svelte";
    import About from "./routes/About.svelte";

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
    </main>
</Router>

<style>
    nav {
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
</style>
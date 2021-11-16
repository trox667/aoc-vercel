import {writable} from "svelte/store";

export let days = 25
const tmp = []
for (let i = 1; i <= days; ++i) tmp.push(i)

export const dayIndices = writable(tmp)
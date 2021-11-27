<script lang="ts">
    import * as THREE from 'three'
    import {GLTFLoader} from "three/examples/jsm/loaders/GLTFLoader";
    import {onMount} from "svelte";
    import {OrbitControls} from "three/examples/jsm/controls/OrbitControls";
    import {MathUtils} from "three";

    class SnowmanScene {
        private readonly scene: THREE.Scene
        private readonly camera: THREE.PerspectiveCamera
        private renderer: THREE.WebGLRenderer
        private loader: GLTFLoader
        private readonly ambientLight: THREE.AmbientLight
        private readonly pointLight: THREE.PointLight
        private controls: OrbitControls
        private mousePos: [number, number]
        private windowSize: [number, number]
        private canvas: HTMLElement;

        constructor(canvas: HTMLElement, width: number, height: number, windowWidth: number, windowHeight: number) {
            this.canvas = canvas;
            this.scene = new THREE.Scene()
            this.camera = new THREE.PerspectiveCamera(75, width / height, 0.1, 1000)
            this.renderer = new THREE.WebGLRenderer({canvas, alpha: true, antialias: true})
            this.renderer.setClearColor(0x000000, 0.0)

            this.loader = new GLTFLoader()

            this.ambientLight = new THREE.AmbientLight(0xFFFFFF)
            this.scene.add(this.ambientLight)

            this.pointLight = new THREE.PointLight(0xEEEEEE)
            this.pointLight.position.set(2, 2, 12)
            this.scene.add(this.pointLight)

            // this.controls = new OrbitControls(this.camera, this.renderer.domElement)
            this.mousePos = [0, 0]
            this.windowSize = [windowWidth, windowHeight]

            this.createScene()
        }

        createScene() {
            this.loader.load('../snowman.glb', (glb) => {
                glb.scene.rotation.y = THREE.MathUtils.degToRad(-90)
                glb.scene.position.y = -1.5
                const sphere = new THREE.SphereGeometry(2)
                const sphereMaterial = new THREE.MeshBasicMaterial({color: 0xCCCCCC, transparent: true, opacity: 0.5})
                const sphereMesh = new THREE.Mesh(sphere, sphereMaterial)
                sphereMesh.position.y = 2
                // glb.scene.add(sphereMesh)

                const cylinder = new THREE.CylinderGeometry(2, 2, 0.1, 32)
                const cylinderMaterial = new THREE.MeshBasicMaterial({color: 0xAAAAAA})
                const cylinderMesh = new THREE.Mesh(cylinder, cylinderMaterial)
                // glb.scene.add(cylinderMesh)

                const cylinder2 = new THREE.CylinderGeometry(1.5, 1.9, 0.1, 32)
                const cylinderMaterial2 = new THREE.MeshBasicMaterial({color: 0xCCCCCC})
                const cylinderMesh2 = new THREE.Mesh(cylinder2, cylinderMaterial2)
                cylinderMesh2.position.y = 0.1
                // glb.scene.add(cylinderMesh2)

                this.scene.add(glb.scene)
            })

            this.camera.position.x = 0
            this.camera.position.y = 0
            this.camera.position.z = 5
        }

        resize(width: number, height: number) {
            this.camera.aspect = width / height
            this.camera.updateProjectionMatrix()
            this.renderer.setSize(width, height)
        }

        render() {
            requestAnimationFrame(() => {
                // this.controls.update()
                this.renderer.render(this.scene, this.camera)
                this.render()
            })
            this.lookAt()
        }

        setWindowSize(width, height) {
            this.windowSize = [width, height]
        }

        setMousePos(x, y) {
            this.mousePos = [x, y]
        }

        lookAt() {
            if (this.windowSize.length < 2) return
            const [width, height] = this.windowSize

            const cy = this.canvas.offsetTop
            const dy = this.canvas.clientHeight

            if (this.mousePos.length < 2) return
            const [x, y] = this.mousePos

            const nx = (0.5 - x / width) * 40
            const oy = (cy + dy) / height
            const ny = (oy - y / height) * 20

            this.scene.rotation.y = MathUtils.degToRad(-nx)
            this.scene.rotation.x = MathUtils.degToRad(-ny)
        }
    }


    const canvasWidth = 200
    const canvasHeight = 200
    let canvas
    let width = 0
    let height = 0
    let snowmanScene
    onMount(() => {
        snowmanScene = new SnowmanScene(canvas, canvasWidth, canvasHeight, width, height)
        snowmanScene.render()
    })


</script>

<!--<svelte:window on:resize={(_) => snowmanScene.resize()}></svelte:window>-->

<svelte:window bind:innerWidth={width} bind:innerHeight={height}
               on:mousemove={(e) => {if (snowmanScene) snowmanScene.setMousePos(e.clientX, e.clientY)}}/>

<canvas bind:this={canvas} id="canvas" width={canvasWidth} height={canvasHeight}></canvas>

<style>
    #canvas {
        width: 200px;
        height: 200px;
    }
</style>
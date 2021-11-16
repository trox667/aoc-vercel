<script lang="ts">
    import * as THREE from 'three'
    import {GLTFLoader} from "three/examples/jsm/loaders/GLTFLoader";
    import {onMount} from "svelte";
    import {OrbitControls} from "three/examples/jsm/controls/OrbitControls";

    class SnowmanScene {
        private scene: THREE.Scene
        private snowScene: THREE.Scene
        private camera: THREE.PerspectiveCamera
        private renderer: THREE.WebGLRenderer
        private loader: GLTFLoader
        private ambientLight: THREE.AmbientLight
        private pointLight: THREE.PointLight
        private controls: OrbitControls
        private mousePos: [number, number]
        private windowSize: [number, number]

        constructor(private canvas: HTMLElement, width: number, height: number, windowWidth: number, windowHeight: number) {
            this.scene = new THREE.Scene()
            this.snowScene = new THREE.Scene()
            this.camera = new THREE.PerspectiveCamera(75, width / height, 0.1, 1000)
            this.renderer = new THREE.WebGLRenderer({canvas, alpha: true, antialias: true})
            this.renderer.setClearColor(0x000000, 0.0)
            this.loader = new GLTFLoader()
            this.ambientLight = new THREE.AmbientLight(0xFFFFFF)
            this.scene.add(this.ambientLight)
            this.pointLight = new THREE.PointLight(0xEEEEEE)
            this.pointLight.position.set(2, 2, 12)
            this.scene.add(this.pointLight)
            this.controls = new OrbitControls(this.camera, this.renderer.domElement)
            this.mousePos = [0, 0]
            this.windowSize = [windowWidth, windowHeight]

            // const axesHelper = new THREE.AxesHelper( 5 );
            // this.scene.add( axesHelper );

            this.scene.add(this.snowScene)

            this.createScene()
            // this.addSnow()
        }

        addSnow() {
            // calculate position in sphere
            const geometry = new THREE.BufferGeometry()
            const vertices = []
            for (let i = 0; i < 100; ++i) {
                const x = Math.random() * 2 - 1
                const y = Math.random() * 3 - 1
                const z = Math.random() * 2 - 1.5
                vertices.push(x, y, z)
            }
            geometry.setAttribute(
                'position',
                new THREE.Float32BufferAttribute(vertices, 3)
            )
            const material = new THREE.PointsMaterial({
                color: 0x000000,
                size: Math.random(),
            })
            const mesh = new THREE.Points(geometry, material)
            this.snowScene.add(mesh)
        }

        createScene() {
            this.loader.load('../snowman.glb', (glb) => {
                glb.scene.rotation.y = THREE.MathUtils.degToRad(-90)
                glb.scene.position.y = -1.5
                const sphere = new THREE.SphereGeometry(2)
                const sphereMaterial = new THREE.MeshBasicMaterial({color: 0xCCCCCC, transparent: true, opacity: 0.5})
                const sphereMesh = new THREE.Mesh(sphere, sphereMaterial)
                sphereMesh.position.y = 2
                glb.scene.add(sphereMesh)

                const cylinder = new THREE.CylinderGeometry(2, 2, 0.1, 16)
                const cylinderMaterial = new THREE.MeshBasicMaterial({color: 0xAAAAAA})
                const cylinderMesh = new THREE.Mesh(cylinder, cylinderMaterial)
                glb.scene.add(cylinderMesh)

                const cylinder2 = new THREE.CylinderGeometry(1.5, 1.9, 0.1, 16)
                const cylinderMaterial2 = new THREE.MeshBasicMaterial({color: 0xCCCCCC})
                const cylinderMesh2 = new THREE.Mesh(cylinder2, cylinderMaterial2)
                cylinderMesh2.position.y = 0.1
                glb.scene.add(cylinderMesh2)

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
                this.controls.update()
                this.renderer.render(this.scene, this.camera)
                this.render()
            })
            // const time = Date.now() * 0.00005
            // this.renderer.render(this.scene, this.camera)
            // for (let i = 0; i < this.snowScene.children.length; i++) {
            //     const object = this.snowScene.children[i]
            //
            //     if (object instanceof THREE.Points) {
            //         object.rotation.x = time * (i < 4 ? i + 1 : -(i + 1))
            //     }
            // }
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

            const cx = this.canvas.offsetLeft
            const cy = this.canvas.offsetTop
            const dx = this.canvas.clientWidth
            const dy = this.canvas.clientHeight

            if (this.mousePos.length < 2) return
            const [x, y] = this.mousePos

            const nx = (0.5 - x / width) * 4
            console.log(nx)

            if (x < cx) {
                // look left
                this.camera.position.x = nx
            } else if (x > cx - dx) {
                // look right
                this.camera.position.x = nx
            } else {
                // look front
                this.camera.position.x = 0
            }

            if (y < cy) {
                // look up
                this.camera.position.y = -1
            } else if (y > cy + dy) {
                // look down
                this.camera.position.y = 1
            } else {
                // look front
                this.camera.position.y = 0
            }
        }
    }


    const canvasWidth = 300
    const canvasHeight = 300
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
               on:mousemove={(e) => {if (snowmanScene) snowmanScene.setMousePos(e.clientX, e.clientY)}} />

<canvas bind:this={canvas} id="canvas" width={canvasWidth} height={canvasHeight}></canvas>

<style>
    #canvas {
        width: 300px;
        height: 300px;
    }
</style>
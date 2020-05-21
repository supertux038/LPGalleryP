window.addEventListener('DOMContentLoaded', function () {
    var canvas = document.getElementById("canvas"); // Get the canvas element
    var engine = new BABYLON.Engine(canvas, true); // Generate the BABYLON 3D engine

    var height = 1;
    var widht = 2;
    var length = 3;

    /******* Add the create scene function ******/
    var createScene = function () {

        // Create the scene space
        var scene = new BABYLON.Scene(engine);
        engine.enableOfflineSupport = false;
        // Add a camera to the scene and attach it to the canvas
        var camera = new BABYLON.ArcRotateCamera("Camera", Math.PI / 2, Math.PI / 2, 2, new BABYLON.Vector3(0, 0, 0), scene);
        camera.setPosition(new BABYLON.Vector3(4, 2, -3));
        camera.attachControl(canvas, true);
        camera.wheelPrecision = 50;


        // showWorldAxis(10);


        // Add lights to the scene
        var light = new BABYLON.PointLight("pointLight", new BABYLON.Vector3(20, 10, 20), scene);
        // var light = new BABYLON.PointLight("pointLight", new BABYLON.Vector3(20, 10, -20), scene);
        // var light = new BABYLON.PointLight("pointLight", new BABYLON.Vector3(-20, 10, 20), scene);
        var light = new BABYLON.PointLight("pointLight", new BABYLON.Vector3(-20, 10, -20), scene);
        // var light2 = new BABYLON.HemisphericLight("HemiLight", new BABYLON.Vector3(0, 0, 0), scene);
        BABYLON.SceneLoader.ImportMesh("", "", "${model_path}", scene);
        // Add and manipulate meshes in the scene
        /*BABYLON.SceneLoader.ImportMesh("","","ae86lp.babylon", scene,
            function(newMeshses){

        })*/

        return scene;
    };
    /******* End of the create scene function ******/

    var scene = createScene(); //Call the createScene function

// Register a render loop to repeatedly render the scene
    engine.runRenderLoop(function () {
        scene.render();
    });

// Watch for browser/canvas resize events
    window.addEventListener("resize", function () {
        engine.resize();
    })


    function showWorldAxis(size) {
        var makeTextPlane = function (text, color, size) {
            var dynamicTexture = new BABYLON.DynamicTexture("DynamicTexture", 50, scene, true);
            dynamicTexture.hasAlpha = true;
            dynamicTexture.drawText(text, 5, 40, "bold 36px Arial", color, "transparent", true);
            var plane = BABYLON.Mesh.CreatePlane("TextPlane", size, scene, true);
            plane.material = new BABYLON.StandardMaterial("TextPlaneMaterial", scene);
            plane.material.backFaceCulling = false;
            plane.material.specularColor = new BABYLON.Color3(0, 0, 0);
            plane.material.diffuseTexture = dynamicTexture;
            return plane;
        };
        var axisX = BABYLON.Mesh.CreateLines("axisX", [
            BABYLON.Vector3.Zero(), new BABYLON.Vector3(size, 0, 0), new BABYLON.Vector3(size * 0.95, 0.05 * size, 0),
            new BABYLON.Vector3(size, 0, 0), new BABYLON.Vector3(size * 0.95, -0.05 * size, 0)
        ], scene);
        axisX.color = new BABYLON.Color3(1, 0, 0);
        var xChar = makeTextPlane("X", "red", size / 10);
        xChar.position = new BABYLON.Vector3(0.9 * size, -0.05 * size, 0);
        var axisY = BABYLON.Mesh.CreateLines("axisY", [
            BABYLON.Vector3.Zero(), new BABYLON.Vector3(0, size, 0), new BABYLON.Vector3(-0.05 * size, size * 0.95, 0),
            new BABYLON.Vector3(0, size, 0), new BABYLON.Vector3(0.05 * size, size * 0.95, 0)
        ], scene);
        axisY.color = new BABYLON.Color3(0, 1, 0);
        var yChar = makeTextPlane("Y", "green", size / 10);
        yChar.position = new BABYLON.Vector3(0, 0.9 * size, -0.05 * size);
        var axisZ = BABYLON.Mesh.CreateLines("axisZ", [
            BABYLON.Vector3.Zero(), new BABYLON.Vector3(0, 0, size), new BABYLON.Vector3(0, -0.05 * size, size * 0.95),
            new BABYLON.Vector3(0, 0, size), new BABYLON.Vector3(0, 0.05 * size, size * 0.95)
        ], scene);
        axisZ.color = new BABYLON.Color3(0, 0, 1);
        var zChar = makeTextPlane("Z", "blue", size / 10);
        zChar.position = new BABYLON.Vector3(0, 0.05 * size, 0.9 * size);
    };
});


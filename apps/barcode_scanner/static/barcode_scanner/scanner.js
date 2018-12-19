    
    let qvga = {width: {exact: 320}, height: {exact: 240}};
    let vga = {width: {exact: 640}, height: {exact: 480}};
    let resolution = window.innerWidth < 640 ? qvga : vga;

    let streaming = false;

    let video = document.getElementById('video');
    let stream = null;
    let vcapture = null;
    console.log('scanner.js is loaded')

    function startCamera(){
        console.log('camera is started')
        let video = document.getElementById('video');
        if(streaming){return;}
        navigator.mediaDevices.getUserMedia({video:resolution, audio: false})
        .then(function(s){
            stream = s;
            video.srcObject = s;
            video.play();
        })
        .catch(function(err){
            console.log(err);
        })

        video.addEventListener("canplay", function(ev){
            console.log('video is ready to play')
            if (!streaming) {
            height = video.videoHeight;
            width = video.videoWidth;
            video.setAttribute("width", width);
            video.setAttribute("height", height);
            streaming = true;
            vcapture = new cv.VideoCapture(video);
            }
            startVideoProcessing();
        }, false)
    }

    let img 
    let barCodes = null
    let scanner = zbarProcessImageData;
    // scanner.parse_config('enable')

    function startVideoProcessing(){
        if (!streaming){ 
            console.warn('start up webcam'); return; 
        }
        img = new cv.Mat(height, width, cv.CV_8UC4)
        requestAnimationFrame(processVideo);
    }

    function scan(img){
        console.log(img)
        // console.log('scanning')
        barCodes = scanner(img);
        for(var i in barCodes){
            console.log('type : ' + i.type)
            console.log('data : ' + i.data)
            console.log(' ')
        }
        return img
    }

    function drawLocations(img, barCodes){
        let points = null
        let hull = null
        for(let i in barCodes){
            points = barCodes.polygon
            if(points.length > 4){
                hull = cv.convexHull        
            } 
        }
    }

    function processVideo(){
        vcapture.read(img);
        let result;
        result = scan(img)
        cv.imshow('scanner_output', result)
        // setTimeout(requestAnimationFrame, 2500, processVideo);
        requestAnimationFrame(processVideo)
    }

    startCamera();
    




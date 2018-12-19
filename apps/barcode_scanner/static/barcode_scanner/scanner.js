    
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
    // let scanner = zbarProcessImageData;
    // scanner.parse_config('enable')

    function startVideoProcessing(){
        if (!streaming){ 
            console.warn('start up webcam'); return; 
        }
        img = new cv.Mat(height, width, cv.CV_8UC4)
        requestAnimationFrame(processVideo);
    }

    // let canvasFrame = document.getElementById("canvasFrame"); // canvasFrame is the id of <canvas>
    // let context = canvasFrame.getContext("2d");
    // let src = new cv.Mat(height, width, cv.CV_8UC4);
    // let dst = new cv.Mat(height, width, cv.CV_8UC1);
    // let pic = document.getElementById('pic')

    function scan(img){
        // context.drawImage(pic, 0, 0, pic.width, pic.height);
        // var data = context.getImageData(0, 0, width, height);
        // console.log(img)
        // console.log(img['data'])
        // console.log(img['data'].length)
        // console.log(cv.read(img))
        // console.log('scanning')
        barCodes = zbarProcessImageData(img);
        if(barCodes.length > 0){
            console.log('barcode detected' + barCodes)
            data = {
                type : barCodes[0][0],
                data : barCodes[0][2]
            }
            $.ajax({
                url: '/scan_success',
                data: data
            })
            .done(function(){
                $('col').innerHTML('<h1 class = "text-success"> Scan Successful </h1>')
            })
        }
        
        
        // for(var i in barCodes){
        //     console.log('type : ' + i.type)
        //     console.log('data : ' + i.data)
        //     console.log(' ')
        // }
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
        // setTimeout(requestAnimationFrame, 500, processVideo);
        requestAnimationFrame(processVideo)
    }

    startCamera();
    




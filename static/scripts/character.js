const EyeState = {
    Open: 0,
    Closed: 1,
};

imageSet = null;

let stateInvalidated = true;

let eyeState = EyeState.Open;
function setEyeState(newState) {
    eyeState = newState;
    stateInvalidated = true;
}

waitTime = 0;

loaded = false;
targetElement = null;

function onLoad(element, imageSrcs) {
    if (loaded) return;

    // Preload images
    imageSet = new Array();
    for (let j in imageSrcs) {
        let i = new Image();
        i.src = imageSrcs[j];
        imageSet.push(i);
    }

    targetElement = element;
    targetElement.addEventListener("animationend", endAnimation);
    targetElement.addEventListener("animationcancel", endAnimation);

    setInterval(update, 1000 / 60) // 60 FPS

    loaded = true;
}

function endAnimation() {
    targetElement.classList.remove("bouncing");
}

function update() {
    // Handle blinking
    const blinkChance = 1 / 200;

    if (eyeState == EyeState.Open) {
        if (Math.random() <= blinkChance) {
            setEyeState(EyeState.Closed);
            waitTime = Math.floor(Math.random() * 5 + 5);
        }
    }
    else {
        if (--waitTime <= 0)
            setEyeState(EyeState.Open);
    }

    if (!stateInvalidated) return;

    updateSprite();
}


function updateSprite() {
    targetElement.src = imageSet[eyeState].src;

    stateInvalidated = false;
    bodyInvalidated = false;
}
const form = document.getElementById("form")
const input = document.getElementById("input")
const textEl = document.getElementById("text")
const ph = document.getElementById("placeholder")
const exampleBtn = document.getElementById("exampleBtn")
const popup = document.getElementById("popup")
const popupChar = document.getElementById("popupChar")
const popupText = document.getElementById("popupText")
const slider = document.getElementById("toggleContainer")
const textBoth = document.getElementById("both")
const textChars = document.getElementById("chars")
const textPinyin = document.getElementById("pinyin")

let originalText = ""
let segText = ""
let sliderState = 0

form.addEventListener("submit", async (e) => {
    e.preventDefault()
    if (input.value != "") {
        ph.style.display = "none"
        originalText = input.value
        if (sliderState === 0) {
            textEl.innerText = originalText
        }
        else if (sliderState === 1) {
            textEl.innerHTML = await getCharsAndPinyin(originalText)
        }
        else if (sliderState === 2) {
            textEl.innerText = await getPinyin(originalText)
        }
        //lookbehind (?<=...) - позиция, которая предшествует указанному шаблону
        input.value = ""
        closePopup()
    }
})

exampleBtn.addEventListener("click", () => {
    input.value = `哈喽，请进！我找娜娜，他在吗？他现在不在，但是马上就回来，请等一会儿！谢谢！不客气，哦，已经回来了！志刚你来得真巧！今天下午小王给我打电话，说他明天可以带我们去参观东方明珠。`
})

slider.addEventListener("click", async () => {
    closePopup()

    if (sliderState === 0) {
        sliderBall.style.transform = 'translateX(31px)';
        textChars.style.color = '#374151'
        textBoth.style.color = 'white'
        if (originalText) {
            if (!segText)
                textEl.innerHTML = await getCharsAndPinyin(originalText)
            else
                textEl.innerHTML = await transformCharsAndPinyin(segText)
        }
        sliderState = 1;


    } else if (sliderState === 1) {
        sliderBall.style.transform = 'translateX(60px)';
        textBoth.style.color = '#374151'
        textPinyin.style.color = 'white'
        if (originalText) {
            if (!segText)
                textEl.innerText = await getPinyin(originalText)
            else
                textEl.innerText = transformPinyin(segText['pinyin'])
        }

        sliderState = 2;

    } else {
        sliderBall.style.transform = 'translateX(0)';
        textPinyin.style.color = '#374151'
        textChars.style.color = 'white'
        if (originalText)
            textEl.innerText = originalText
        sliderState = 0;

    }
})

textEl.addEventListener('mouseup', async (e) => {
    const selectedText = document.getSelection().toString();
    if (selectedText != "") {
        const mouseX = e.clientX;
        const mouseY = e.clientY;
        addTextToPopup(selectedText, await getTranslation(selectedText))
        showPopup(mouseX, mouseY)

    }
    else {
        closePopup()
    }

});

async function getTranslation(selectedText) {
    const response = await fetch(`/api/translate/?ch=${selectedText}`)

    return await response.json()

}

async function getPinyin(text) {
    let pinyin = ""

    const response = await fetch("api/pinyin", {
        method: "POST",
        headers: { "Accept": "application/json", "Content-Type": "application/json" },
        body: JSON.stringify({
            text: text
        })
    });
    if (response.ok) {
        data = await response.json();
        segText = data
        pinyin = transformPinyin(data['pinyin'])


    } else
        console.log(response);


    return await pinyin
}

function transformPinyin(pinyin) {
    pinyin = pinyin.map(element => element.charAt(0).toUpperCase() + element.slice(1))
    pinyin = pinyin.map(sentence => sentence.replace(/\s*([，。！？])\s*/g, '$1').replace(/\s+/g, ' ').trim()).join(' ');

    return pinyin
}

function transformCharsAndPinyin(data) {
    pinyinText =""
    const simb = ['！', '？', '。', ' '];

    for (let i = 0; i < Object.keys(data['chrs']).length; i++) {
        chrs = data['chrs'][i].split(" ").filter(element => element !== '')
        pinyin = data['pinyin'][i].split(" ").filter(element => element !== '')
        pinyin[0] = pinyin[0].charAt(0).toUpperCase() + pinyin[0].slice(1)

        for (let j = 0; j < chrs.length; j++) {
            if (!chrs[j].includes(simb)) {
                pinyinText += '<ruby class="inline-flex flex-col items-center mx-[1px]">' + chrs[j] + '<rt class="text-xs text-gray-500 ">' + pinyin[j] + '</rt></ruby>'
            }
            else {
                pinyinText += chrs[j]
            }

        }
    }

    return pinyinText

}

async function getCharsAndPinyin(text) {
    let pinyinText = ''

    const response = await fetch("api/pinyin", {
        method: "POST",
        headers: { "Accept": "application/json", "Content-Type": "application/json" },
        body: JSON.stringify({
            text: text
        })
    });
    if (response.ok) {
        const data = await response.json();
        segText = data
        pinyinText = transformCharsAndPinyin(data)

    }
    else
        console.log(response);


    return await pinyinText
}

function showPopup(mouseX, mouseY) {
    popup.style.left = mouseX + 'px';
    popup.style.top = mouseY + 'px';
    popup.style.display = "block"
}

function addTextToPopup(selectedText, translation) {
    if (Object.keys(translation).length !== 0) {
        popupChar.innerText = translation['character'] + "\n" + translation['pinyin']
        popupText.innerText = ""

        for (key in translation['definitions']) {
            popupText.innerHTML += key + "<br/>"
            //for (let i = 0; i < (translation['definitions'][key]).length; i++) 
            //   popupText.innerHTML += translation['definitions'][key][i] + "<br/>"
        }
    }
    else {
        popupChar.innerText = selectedText
        popupText.innerText = "Перевод не найден"
    }



}

function closePopup() {
    popup.style.display = "none"

}


// document.addEventListener("selectionchange", (e) => {
//     if (document.getSelection().toString() == ""){
//         closePopup()
//     }
//     console.log(e.target)
// })


/*
 fetch(`/ api / translate /? ch = ${ input.value } `)
        .then(response => response.text())
        .then(text => {translate.innerText = text});
*/
const form = document.getElementById("form")
const input = document.getElementById("input")
const text = document.getElementById("text")
const ph = document.getElementById("placeholder")
const exampleBtn = document.getElementById("exampleBtn")
const popup = document.getElementById("popup")
const popupChar = document.getElementById("popupChar")
const popupText = document.getElementById("popupText")

form.addEventListener("submit", (e) => {
    e.preventDefault()
    if (input.value != "") {
        ph.style.display = "none"
        text.innerText = input.value
        input.value = ""
        closePopup()
    }
})

exampleBtn.addEventListener("click", () => {
    input.value = `眼虎流女它坐耍春
更過安筆行京民胡吧但具自童急且車朱海黑，友升占追王怕故經裏杯汁消背美爸。久太很白！男母四穴寸泉？條至左幾，連菜什黃誰晚語日包鳥珠您父士。
放做犬；動司請吧把由兄重常，樹羊找北入坡時牙友美「園畫車內法歡寺」能開菜叫呀車畫六了唱頭國外衣拉候弟神。
貫共反實葉坐五金刀急我春穴：問消國夕帽海孝飛音後、成兄尤雨母植樹兌斥刀後婆，跟只雪福吧波動次現，辛安片棵內里因燈？澡牠師哭力品假根。乞話掃！片苗面。
丁常一氣別汁青。眼即們已門刃神北八澡扒跳得，皮看拍抱自斤圓京燈：或汗胡，毛青天風學怕：飯神正住條昔尾成。
主世胡几問刃害急刀司尼昌聲明己汁直做片沒，爸麻老乍果斗月住陽丁，三工怎央蝴采弟他請詞植平發刀十又，士皮成耍院候院明洋立戊巾以鴨。里三正苦干。收蛋金用現首間能民路里化，坐重送珠澡，怪斗呢。
主長汗做和今帶！秋兔果許進節苦勿杯菜苗頭，畫爬乾申瓜朋頁；呢長由笑錯良門豆在右金鴨校鼻服百請點？六什員連姊安樹兆壯鳥頭六寫才荷；枝進害昌蝶後者巴；屋哥抱成枝會誰知尾原爪喜以蝸石菜位抄口友。
中長乍鴨入往合嗎在青？英英年故香因笑飯苗校節幾歌可後，開枝又一己拍卜發娘歡手寺用朱刀已良那習筆；公就占常秋山自：穿尾經。清誰追別功面。`
})

text.addEventListener('mouseup', async (e) => {
    const selectedText = document.getSelection().toString();
    if (selectedText != "") {
        const mouseX = e.clientX;
        const mouseY = e.clientY;
        addTextToPopup(selectedText, await getTranslation(selectedText))
        showPopup(mouseX, mouseY)      

    }
    else{
        closePopup()
    }

});

async function getTranslation(selectedText){
    const response = await fetch(`/api/translate/?ch=${selectedText}`)
    
    return await response.json()

}

function showPopup(mouseX, mouseY) {
    popup.style.left = `${mouseX}px`;
    popup.style.top = `${mouseY}px`;
    popup.style.display = "block"
}

function addTextToPopup(selectedText, translation){
    if (Object.keys(translation).length !== 0){
        popupChar.innerText = translation['character'] + "\n" + translation['pinyin']
        popupText.innerText = ""
        console.log(translation)

        for (key in translation['definitions']){
            console.log(translation['definitions'][key])
            popupText.innerHTML += key + "<br/>"
            //for (let i = 0; i < (translation['definitions'][key]).length; i++) 
            //   popupText.innerHTML += translation['definitions'][key][i] + "<br/>"
        }
    }
    else{
        popupChar.innerText = selectedText
        popupText.innerText = "Перевод не найден"
    }
    
        

}

function closePopup(){
    popup.style.display = "none"
    
}


// document.addEventListener("selectionchange", (e) => {
//     if (document.getSelection().toString() == ""){
//         closePopup()
//     }
//     console.log(e.target)
// })


/*
 fetch(`/api/translate/?ch=${input.value}`)
        .then(response => response.text())
        .then(text => {translate.innerText = text});
*/
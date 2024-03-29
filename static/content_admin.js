// constants
let elements_pk = 0;
// ========


function render_block_space(space=20){
    elements_pk += 1;
    return `
        <div class="cb_wrap cd_create" 
        data-id="${elements_pk}"
        style="height:${space}px;"></div>
    `
}
function render_block_image(){
    elements_pk += 1;
    return `
        <div class="cb_wrap cd_create" data-id="${elements_pk}">
            <input type="file" name="" accept="image/*" id="" data-id="${elements_pk}">
        </div>
    `
}
function render_block_video(){
    elements_pk += 1;
    return `
        <div class="cb_wrap cd_create" data-id="${elements_pk}">
            <input type="file" name="" accept="video/*" id="" data-id="${elements_pk}">
        </div>
    `
}
function render_block_text(){
    elements_pk += 1;
    return `
        <div class="cb_wrap cd_create" data-id="${elements_pk}">
            <textarea name="" cols="40" rows="10" class="vLargeTextField" id="" data-id="${elements_pk}"></textarea>
        </div>
    `
}

function render_wrap(){
    return `
        <div class="wrap_body">
            <div id="content_body"></div>
            <div id="content_func"></div>
            <div id="navigation_body">
                <button class="btn-nav" data-action="space">+ Space</button>
                <button class="btn-nav" data-action="image">+ Image</button>
                <button class="btn-nav" data-action="video">+ Video</button>
                <button class="btn-nav" data-action="text">+ Text</button>
            </div>
        </div>
    `
}

function action_btn_event(e){
    
    const target = e.target.closest(".btn-nav");
  
    if(target){   
        e.preventDefault();
        let content_body = document.getElementById("content_body");
        switch (target.dataset.action) {
            case "space":
                content_body.insertAdjacentHTML("beforebegin", render_block_space())
                break;
            case "image":
                content_body.insertAdjacentHTML("beforebegin", render_block_image())
                break;
            case "video":
                content_body.insertAdjacentHTML("beforebegin", render_block_video())
                break;
            case "text":
                content_body.insertAdjacentHTML("beforebegin", render_block_text())
                break;
            default:
                break;
        }
    }
}


function ready() {
    let container = document.getElementsByClassName('field-body')[0];
    if(container){
        let field = document.getElementById("id_body")
        let wrap = container.querySelector('.flex-container');
        wrap.insertAdjacentHTML("afterend", render_wrap())
        document.addEventListener("click", action_btn_event);
    }
}

document.addEventListener("DOMContentLoaded", ready);
let images = 1;
let files = 1;

function ready() {
    let img_btn = document.getElementById("add_image_btn");
    let file_btn = document.getElementById("add_file_btn");

    img_btn.addEventListener('click', function(e){
        e.preventDefault();
        let wrap = document.getElementById('image-wrap');
        images += 1;
        wrap.insertAdjacentHTML("beforeend",`
        <div class="m-3 nm-file-input">
            <input class="form-control form-control-sm" name="img_${images}" accept="image/*" type="file">
        </div>
        `);
    });
    file_btn.addEventListener('click', function(e){
        e.preventDefault();
        let wrap = document.getElementById('file-wrap');
        images += 1;
        wrap.insertAdjacentHTML("beforeend",`
        <div class="m-3 nm-file-input">
            <input class="form-control form-control-sm" name="file_${images}" type="file">
        </div>
        `);
    });
}


window.addEventListener('load', ready)
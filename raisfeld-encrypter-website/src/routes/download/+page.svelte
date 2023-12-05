<script>
    function download(file){

    let a = document.getElementById('download');

    a.download = file;
    a.href = file;

    a.click();
    }
</script>

<a id="download" style="display: none;"> </a>

<section>
    <button class="target" on:click={()=>{download('raisfeld encrypter setup.exe')}}>
        windows
    </button>
    <button class="target">
        linux
    </button>
</section>

<style>
    section{
        margin-top: auto;
        margin-bottom: auto;
        margin-left: 10px;
        margin-right: 10px;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .target{
        height: calc(10svh + 10svw);
        width: calc(10svh + 10svw);
        background-color: rgb(30, 20, 20);
        color: white;
        border-color: rgb(30, 20, 20);
        border-radius: 10px;
        font-size: calc(1.5svh + 1.5svw + 10px);
        margin: 10px;
        cursor: pointer;
    }
</style>
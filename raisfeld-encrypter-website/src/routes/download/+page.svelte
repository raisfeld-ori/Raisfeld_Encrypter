<section>
    <button class="target">
        windows
    </button>
    <button class="target">
        linux
    </button>
    <button class="target">
        source
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
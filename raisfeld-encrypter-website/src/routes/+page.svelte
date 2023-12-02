<script>
	import { goto } from '$app/navigation';
	function download(){goto('/download')}
</script>

<section>
	<h1>
		<span class="welcome">raisfeld encrypter</span>
	</h1>
	<h3>
		some explanation of the app
	</h3>
	<button on:click={download}>
			download now
	</button>
</section>

<style>
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		flex: 0.6;
	}

	h1 {
		font-size: 100px;
		font-size: 5em;
		font-weight: bold;
		margin-bottom: 0;
	}
	
	h3{
		font-size: 25px;
		font-size: 2em;
	}

	button{
		border-radius: 10px;
		background-color: #111827;
		border-color: #111827;
		width: calc(15svw + 100px);
		cursor: pointer;
		height: 20svh;
		transition: all 0.5s ease-in-out;
		text-decoration: none;
		color: #FFFFFF;
		font-size: calc(1.5svh + 1.5svw + 10px);
	}
	button:hover{
		transform: scale(1.2);
	}

	.welcome {
		display: block;
		position: relative;
		width: 100%;
	}
</style>
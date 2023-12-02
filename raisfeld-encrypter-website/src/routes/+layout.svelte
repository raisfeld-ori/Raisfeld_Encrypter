<script>
	import Header from './Header.svelte';
	import './styles.css';
</script>

<svelte:head>
	<title>Raisfeld encrypter</title>
	<meta name="description" content="main page" />
</svelte:head>

<div class="app">
	<Header />

	<main>
		<slot />
	</main>
</div>

<style>
	.app {
		display: flex;
		flex-direction: column;
		min-height: 100vh;
	}

	main {
		flex: 1;
		display: flex;
		flex-direction: column;
		padding: 1rem;
		width: 100%;
		max-width: 64rem;
		margin: 0 auto;
		box-sizing: border-box;
		padding: 0;
	}
</style>

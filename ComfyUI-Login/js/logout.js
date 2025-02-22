import { app } from "../../scripts/app.js";

app.registerExtension({
	name: "Comfy.Login.Logout",
	init() {},
	async setup() {
		await new Promise(resolve => setTimeout(resolve, 500)); // Delay for 0.5 second before appending the Logout button to the menu, ensuring it is added last.

		function logout(){
			let workflowData = localStorage.getItem('workflow'); // Save the workflow data
			localStorage.clear(); // Clear all items in localStorage
			localStorage.setItem('workflow', workflowData); // Restore the workflow data

			sessionStorage.clear(); // If you use sessionStorage
			window.location.href = "/logout"; 
		}

		// Old interface
		const menu = document.querySelector(".comfy-menu");
		if(menu)
		{
			const logoutButton = document.createElement("button");
			logoutButton.textContent = "Logout";
			logoutButton.onclick = () => {logout()}
			menu.append(logoutButton);
		}

		// New interface
		function add_button_new_interface() {
			const side_tb = document.querySelector(".side-tool-bar-end");
			const params_button = document.querySelector(".pi-cog");
			if(side_tb && params_button)
			{
				const logoutButton = params_button.parentElement.cloneNode(true);
				logoutButton.id = "bxRebootButtonNew";
				let shuticon = logoutButton.querySelector(".pi-cog");
				shuticon.classList.remove("pi-cog");
				shuticon.classList.add("pi-sign-out");
				side_tb.append(logoutButton);
				logoutButton.onclick = () => {logout()}
			}
			else
				setTimeout(add_button_new_interface, 1000);
		}

		add_button_new_interface();
	},
});

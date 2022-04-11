function setToggleState(id, state) {
  const ENABLED_CLASS = "basicdialog_On_1RyF_";
  let toggle = document.getElementById(id);

  if (state && !toggle.classList.contains(ENABLED_CLASS)) {
    toggle.classList.add(ENABLED_CLASS);
  }

  if (!state && toggle.classList.contains(ENABLED_CLASS)) {
    toggle.classList.remove(ENABLED_CLASS);
  }
}

function handleSSHToggle() {
  let toggle = document.getElementById("sshToggle");

  let isActive = toggle.classList.contains("basicdialog_On_1RyF_");

  if (isActive) {
    call_plugin_method("set_ssh_state", { state: false }).then((value) => {
      setToggleState("sshToggle", value);
    });
  } else {
    call_plugin_method("set_ssh_state", { state: true }).then((value) => {
      setToggleState("sshToggle", value);
    });
  }
}

async function handleInitialValue() {
  console.log("InitialValue");
  let state = await call_plugin_method("get_ssh_state", {});
  console.log(state);
  setToggleState("sshToggle", state);
}

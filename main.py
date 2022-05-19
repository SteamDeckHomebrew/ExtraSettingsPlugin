import subprocess

class Plugin:
    async def get_ssh_state(self):
        return subprocess.Popen("systemctl is-active sshd", stdout=subprocess.PIPE, shell=True).communicate()[0] == b'active\n'

    async def set_ssh_state(self, state):
        if state:
            subprocess.Popen("systemctl enable --now sshd", stdout=subprocess.PIPE, shell=True).wait()
        else:
            subprocess.Popen("systemctl disable --now sshd", stdout=subprocess.PIPE, shell=True).wait()

        return await self.get_ssh_state(self)

    async def set_thp_state(self, state):
        if state:
            with open("/sys/kernel/mm/transparent_hugepage/enabled", "w") as f:
                f.write("always")
        else:
            with open("/sys/kernel/mm/transparent_hugepage/enabled", "w") as f:
                f.write("madvise")

        return await self.get_thp_state(self)


    async def get_thp_state(self):
        with open("/sys/kernel/mm/transparent_hugepage/enabled", "r") as f:
            return f.read().strip().startswith("[always]")

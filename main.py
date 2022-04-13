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
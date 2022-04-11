import subprocess

class Plugin:
    name = "Extra Settings"

    author = "WerWolv"

    main_view_html = "index.html"

    tile_view_html = ""

    async def get_ssh_state(self):
        return subprocess.Popen("systemctl is-active sshd", stdout=subprocess.PIPE, shell=True).communicate()[0] == b'active\n'

    async def set_ssh_state(self, **kwargs):
        print(kwargs["state"])

        if kwargs["state"]:
            print(subprocess.Popen("systemctl start sshd", stdout=subprocess.PIPE, shell=True).communicate())
        else:
            print(subprocess.Popen("systemctl stop sshd", stdout=subprocess.PIPE, shell=True).communicate())
        
        return await self.get_ssh_state(self)

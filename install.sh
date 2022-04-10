plugin_id=com.github.SteamDeckHomebrew.ExtraSettingsPlugin
plugin_dir=/home/deck/homebrew/plugins/$plugin_id

mkdir -p $plugin_dir

# Install the plugin-related files
cp ./index.html $plugin_dir
cp ./index.js $plugin_dir
cp ./main.py $plugin_dir

# Install sudoers file to allow controlling the sshd service
sudo cp ./etc/sudoers.d/x-extra-settings-plugin /etc/sudoers.d/x-extra-settings-plugin
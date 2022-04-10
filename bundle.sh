# Delete previous bundle if exists
rm -f ./extra-settings-plugin.zip

# Bundle the plugin
zip ./extra-settings-plugin.zip \
    etc/sudoers.d/x-extra-settings-plugin \
    index.html \
    index.js \
    main.py \
    install.sh
    
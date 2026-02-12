# Commit script
commit *msg:
	git add . && git commit -m "{{msg}}" && git push

# Restart systemd for sandbox
restart:
	sudo systemctl restart sandbox

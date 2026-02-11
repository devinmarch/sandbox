# Commit script
commit *msg:
	git add . && git commit -m "{{msg}}" && git push


x="upload"

if x=="upload" then
	--os.execute("gitUpload.bat")
	os.execute("git status")
	os.execute("git add . ")
	os.execute('git commit -m "Update"')
	os.execute("git push")
elseif x=="download" then
	--os.execute("gitDownload.bat")
	os.execute("git status")
	os.execute("git add . ")
	os.execute('git commit -m "Update"')
	os.execute("git pull")
end

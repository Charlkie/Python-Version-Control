git tag <version> -m "<comment>"
git push --tags origin master
@ copy https://github.com/{username}/{module_name}/archive/{tag}.tar.gz
@ put it in download_url in setup.py
python setup.py sdist upload

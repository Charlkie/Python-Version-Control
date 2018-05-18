#!/Charlkie/bin/bash

function pvc {
    if [ $1 = init ]
    then
        python3 /Users/Charlkie/Python_Version_Control/python-version-control/pvc_init.py
    fi
	if [ $1 = stage ]
	then
		python3 /Users/Charlkie/Python_Version_Control/python-version-control/pvc_stage.py $@
	fi
	if [ $1 = commit ]
	then
		python3 /Users/Charlkie/Python_Version_Control/python-version-control/pvc_commit.py $@
	fi
}

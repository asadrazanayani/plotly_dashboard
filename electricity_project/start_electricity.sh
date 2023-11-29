export port=8081
export venv_path="/opt/data_sceince_projects/dash/"
export requirements_file_path="${venv_path}/requirement.txt"
if [ -d "${venv_path}/venv" ]; then
    echo "Venv Exists"
    else
        echo "Venv Does Not Exits"
        mkdir -p $venv_path
        cd $venv_path
        python3 -m venv venv
        source venv/bin/activate
        pip install -r requirement.txt
fi

cd ${venv_path}/electricity_dashboard

echo "starting dashboard"
python3 electricity_dashboard.py

#!/bin/bash -ex

COVERAGE_THRESHOLD=90

export PYTHONPATH=`pwd`/fabric8-analytics-version-comparator
echo "Create Virtualenv for Python deps ..."
function prepare_venv() {
    VIRTUALENV=$(which virtualenv)
    if [ $? -eq 1 ]
    then
        # python34 which is in CentOS does not have virtualenv binary
        VIRTUALENV=$(which virtualenv-3)
    fi

    ${VIRTUALENV} -p python3 venv && source venv/bin/activate
    if [ $? -ne 0 ]
    then
        printf "%sPython virtual environment can't be initialized%s" "${RED}" "${NORMAL}"
        exit 1
    fi
    pip install -U pip
    python3 $(which pip3) install -r requirements.txt

}

[ "$NOVENV" == "1" ] || prepare_venv || exit 1

$(which pip3) install pytest
$(which pip3) install pytest-cov


PYTHONDONTWRITEBYTECODE=1 python3 "$(which pytest)" --cov=f8a_version_comparator/ --cov-report term-missing --cov-fail-under=$COVERAGE_THRESHOLD -vv tests/
printf "%stests passed%s\n\n" "${GREEN}" "${NORMAL}"

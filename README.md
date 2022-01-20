# Hylkyilmoitus backend
[![GitHub Actions](https://github.com/Sukellusilmoitus/backend/workflows/CI/badge.svg)](https://github.com/Sukellusilmoitus/backend/actions)
[![codecov](https://app.codecov.io/gh/Sukellusilmoitus/backend/branch/master/graph/badge.svg?token=4EYTWGYKB4)](https://app.codecov.io/gh/Sukellusilmoitus/backend)

## Usage

Make sure you have Python 3.8 or higher and pip installed. Activate the virtual environment and install the dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r ./requirements.txt
```

After this you can start the api

```bash
python3 src/index.py
```

If `curl http://localhost:5000/api/helloworld` is successful, the api is up and running.

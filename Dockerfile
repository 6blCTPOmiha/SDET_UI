FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir \
    --default-timeout=100 \
    --retries=10 \
    --trusted-host pypi.org \
    --trusted-host files.pythonhosted.org \
    selenium pytest allure-pytest

COPY . .

CMD ["pytest", "tests", "--alluredir=allure-results", "-p", "no:cacheprovider"]

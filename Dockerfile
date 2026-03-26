FROM python:3.11 

WORKDIR /app 

COPY . . 

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install allure-pytest pytest-xdist

CMD ["pytest", "tests", "--alluredir=allure-results"] 

FROM python:3.10.1 

WORKDIR /usr/src/app 

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["univcorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
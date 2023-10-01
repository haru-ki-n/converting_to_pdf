FROM public.ecr.aws/lambda/python:3.8

COPY hello.py ${LAMBDA_TASK_ROOT}
COPY requirements.txt  .

RUN pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"
RUN pip install fastapi uvicorn

CMD [ "hello.handler" ]
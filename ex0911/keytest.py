from openai import OpenAI

# 키가 로컬PC-시스템환경설정에 저장되어 있음.
client = OpenAI()

response = client.responses.create(
    model="gpt-5-mini",
    input="API 키 연결 테스트입니다. '정상 연결'이라고만 답해주세요."
)

print(response.output_text)

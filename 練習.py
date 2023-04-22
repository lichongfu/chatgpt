import openai
openai.api_key="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"
print("歡迎光臨聯大算命中心")
name=input("請輸入你的姓名: ")
sex=input("請輸入你的性別: ")
star=input("請輸入你的星座: ")
prompt="假設你是一位專業的星座專家，現在有一位顧客，他叫做"+name+"，他的性別是"+sex+"，他的星座是"+star+"，請說明他這一週的運勢，如果他的性別是男。就強調運勢；如果他的性別是男，就強調愛情。"
#print("我們設計的提示語：",prompt)
chat_output=openai.ChatCompletion.create(
model="gpt-3.5-turbo",
messages=[{
    "role":"user",
    "content":prompt
}])
re_content=chat_output.choices[0].message.content
print("一周星座運勢:", re_content)


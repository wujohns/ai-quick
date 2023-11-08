from gradio_client import Client

client = Client("http://127.0.0.1:3000/")
result = client.predict(
	"Hello!!",	# str  in '输入' Textbox component
	api_name="/aaa_fn"
)
print('-------------')
print(result)

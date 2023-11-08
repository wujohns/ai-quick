import gradio as gr

def aaa_fn(input):
  return f'{input}-{input}'

def bbb_fn(input):
  return f'---{input}---'

with gr.Blocks() as server:
  # 简单的函数演示
  gr.Markdown('# 基础测试')

  # -----------------------------------------
  gr.Markdown('函数 aaa 的实现')
  with gr.Row():
    aaa_input = gr.Textbox(label='输入')
    aaa_output = gr.Textbox(label='输出')
    aaa_click = gr.Button('点击')

  aaa_click.click(
    aaa_fn,
    inputs=[aaa_input],
    outputs=[aaa_output]
  )

  # -----------------------------------------
  gr.Markdown('函数 bbb 的实现')
  with gr.Row():
    bbb_input = gr.Textbox(label='输入')
    bbb_output = gr.Textbox(label='输出')
    bbb_click = gr.Button('点击')

  bbb_click.click(
    bbb_fn,
    inputs=[bbb_input],
    outputs=[bbb_output]
  )

server.launch(server_port=3000, server_name='0.0.0.0')

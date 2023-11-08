import gradio as gr

def change_textbox(choice):
  # 根据不同输入对输出控件进行更新(会同时更新组件的属性)
  if choice == "short":
    return gr.update(lines=2, visible=True, value="Short story: ")
  elif choice == "long":
    return gr.update(lines=8, visible=True, value="Long story...")
  else:
    return gr.update(visible=False)

with gr.Blocks() as server:
  # 简单的函数演示
  gr.Markdown('# 组件联动')

  # ----------------------------------
  radio = gr.Radio(
    ['short', 'long', 'none'], label='Essay Length ot Write?'
  )
  text = gr.Textbox(lines=2, interactive=True)
  radio.change(fn=change_textbox, inputs=radio, outputs=text)

server.launch(server_port=3000, server_name='0.0.0.0')

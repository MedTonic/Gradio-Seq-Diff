
import gradio as gr
from gradio_seq_diff import seq_diff


example = seq_diff().example_value()

demo = gr.Interface(
    lambda x:x,
    seq_diff(),  # interactive version of your component
    seq_diff(),  # static version of your component
    # examples=[[example]],  # uncomment this line to view the "example version" of your component
)


if __name__ == "__main__":
    demo.launch()

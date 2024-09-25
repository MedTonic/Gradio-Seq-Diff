
import gradio as gr
from app import demo as app
import os

_docs = {'seq_diff': {'description': 'Creates a sequence difference component that displays MSAPlot images as output.', 'members': {'__init__': {'value': {'type': 'Optional[Union[str, PIL.Image.Image, np.ndarray, Callable]]', 'default': 'None', 'description': 'Initial value. If callable, the function will be called whenever the app loads to set the initial value of the component.'}, 'msa': {'type': 'List[str]', 'default': '[]', 'description': 'Multiple sequence alignment as a list of strings.'}, 'seq_names': {'type': 'Optional[List[str]]', 'default': 'None', 'description': 'List of sequence names.'}, 'start': {'type': 'Optional[int]', 'default': 'None', 'description': 'Start position of the alignment to display.'}, 'end': {'type': 'Optional[int]', 'default': 'None', 'description': 'End position of the alignment to display.'}, 'color_map': {'type': 'Optional[dict]', 'default': 'None', 'description': 'Custom color map for the alignment.'}, 'palette': {'type': 'Optional[str]', 'default': 'None', 'description': 'Color palette to use if color_map is not provided.'}, 'show_char': {'type': 'bool', 'default': 'True', 'description': 'Whether to show characters in the alignment.'}, 'panels': {'type': 'Optional[List[Callable]]', 'default': 'None', 'description': 'List of panel functions to include in the MSAPlot.'}, 'panel_height_ratios': {'type': 'Optional[List[float]]', 'default': 'None', 'description': 'List of height ratios for the panels.'}, 'panel_params': {'type': 'Optional[List[dict]]', 'default': 'None', 'description': 'List of parameter dictionaries for each panel.'}, 'wrap': {'type': 'Optional[int]', 'default': 'None', 'description': 'Number of positions to wrap the alignment.'}, 'format': {'type': 'str', 'default': '"png"', 'description': 'File format to save the image (e.g., "png", "jpg").'}, 'height': {'type': 'Optional[Union[int, str]]', 'default': 'None', 'description': 'Height of the displayed image.'}, 'width': {'type': 'Optional[Union[int, str]]', 'default': 'None', 'description': 'Width of the displayed image.'}, 'label': {'type': 'Optional[str]', 'default': 'None', 'description': 'The label for this component.'}, 'every': {'type': 'Optional[Union[float, "Timer"]]', 'default': 'None', 'description': 'Continuously calls `value` to recalculate it if `value` is a function.'}, 'show_label': {'type': 'Optional[bool]', 'default': 'None', 'description': 'If True, will display label.'}, 'container': {'type': 'bool', 'default': 'True', 'description': 'If True, will place the component in a container.'}, 'scale': {'type': 'Optional[int]', 'default': 'None', 'description': 'Relative size compared to adjacent Components.'}, 'min_width': {'type': 'int', 'default': '160', 'description': 'Minimum pixel width.'}, 'visible': {'type': 'bool', 'default': 'True', 'description': 'If False, component will be hidden.'}, 'elem_id': {'type': 'Optional[str]', 'default': 'None', 'description': 'An optional string that is assigned as the id of this component in the HTML DOM.'}, 'elem_classes': {'type': 'Optional[Union[List[str], str]]', 'default': 'None', 'description': 'An optional list of strings that are assigned as the classes of this component in the HTML DOM.'}, 'render': {'type': 'bool', 'default': 'True', 'description': 'If False, component will not be rendered in the Blocks context.'}, 'show_download_button': {'type': 'bool', 'default': 'True', 'description': 'If True, will display button to download image.'}, 'show_share_button': {'type': 'Optional[bool]', 'default': 'None', 'description': 'If True, will show a share icon in the corner of the component.'}}, 'postprocess': {'value': {'type': 'typing.Any', 'description': 'The value to be postprocessed.'}}, 'preprocess': {'return': {'type': 'typing.Any', 'description': None}, 'value': None}}, 'events': {'change': {'type': None, 'default': None, 'description': 'Triggered when the value of the seq_diff changes either because of user input (e.g. a user types in a textbox) OR because of a function update (e.g. an image receives a value from the output of an event trigger). See `.input()` for a listener that is only triggered by user input.'}, 'select': {'type': None, 'default': None, 'description': 'Event listener for when the user selects or deselects the seq_diff. Uses event data gradio.SelectData to carry `value` referring to the label of the seq_diff, and `selected` to refer to state of the seq_diff. See EventData documentation on how to use this event data'}}}, '__meta__': {'additional_interfaces': {}, 'user_fn_refs': {'seq_diff': []}}}

abs_path = os.path.join(os.path.dirname(__file__), "css.css")

with gr.Blocks(
    css=abs_path,
    theme=gr.themes.Default(
        font_mono=[
            gr.themes.GoogleFont("Inconsolata"),
            "monospace",
        ],
    ),
) as demo:
    gr.Markdown(
"""
# `gradio_seq_diff`

<div style="display: flex; gap: 7px;">
<img alt="Static Badge" src="https://img.shields.io/badge/version%20-%200.0.2%20-%20orange">  
</div>

Visualize Sequences and their Diffs Using MSAplot
""", elem_classes=["md-custom"], header_links=True)
    app.render()
    gr.Markdown(
"""
## Installation

```bash
pip install gradio_seq_diff
```

## Usage

```python
import gradio as gr
from gradio_seq_diff import seq_diff
import matplotlib.pyplot as plt

def generate_msaplot():
    seq1 = "CAGGTGCACCTGCAGGAGTCGGGCCCCGGACTAGTGAAGTCTTCGGAGACCCTGTCCCTCACCTGCACTGTCTCTGGTGACTCCATCAGACGTGATACTTACTACTGGAGCTGGATCCGGCAGACTCCGGGGAAGGGACTGGAGTGGCTTGGATATGTCTTTAAAAGTGGGAGCACAAAGTACAACCCCTCCTTCAAGCGTCGAGTCGACATATCAGTAGACACGTCCAAGGAGCAGTTCTCCCTGACATTGACGTCTGTGACCACTGCGGACACGGCCGTATACTTCTGTGCGAGAGAGTGGTACTATGGTTCGGGGGCCCCCCACAACTGGCTCGACTCCTGGAGCCAGGGAACCCTGGTCACCGTCTCCTCAG"
    seq2 = "CAGGTGCACCTGCAGGAGTCGGGCCCCGGACTAGTGAAGTCTTCGGAGACCCTGTCCCTCACCTGCACTGTCTCTGGTGACTCCATCAGACGTGATACTTACTACTGGAGCTGGATCCGGCAGACTCCGGGGAAGGGACTGGAGTGGCTTGGATATGTCTTTAAAAGTGGGAGCACAAAGTACAACCCCTCCTTCAAGCGTCGAGTCGACATATCAGTAGACACGTCCAAGGAGCAGTTCTCCCTGACATTGACGTCTGTGACCACTGCGGACACGGCCGTATACTTCTGTGCGAGAGAGTGGTACTATGGTTCGGGGGCCCCCCACAACTGGCTCGACTCCTGGAGCCAGGGAACCCTGGTCACCGTCTCCTCAG"
    germline = "CAGGTGCAGCTGCAGGAGTCGGGCCCAGGACTGGTGAAGCCTTCGGAGACCCTGTCCCTCACCTGCACTGTCTCTGGTGGCTCCATCAG------TAGTTACTACTGGAGCTGGATCCGGCAGCCCCCAGGGAAGGGACTGGAGTGGATTGGGTATATCTATTACAGTGGGAGCACCAACTACAACCCCTCCCTCAAGAGTCGAGTCACCATATCAGTAGACACGTCCAAGAACCAGTTCTCCCTGAAGCTGAGCTCTGTGACCGCTGCGGACACGGCCGTGTATTACTGTGCGAGAGAGTGGTACTATGGTTCGGGGGCCCCCCACAACTGGTTCGACTCCTGGGGCCAAGGAACCCTGGTCACCGTCTCCTCAG"

    fig, axes = plt.subplots(figsize=(12, 24))
    from msaplot import DrawComplexMSA, GetColorMap, DrawAnnotation, DrawSeqLogo, DrawMSA, DrawConsensusHisto

    DrawComplexMSA(
        msa=[seq1, seq2, germline],
        wrap=50,
        seq_names=['seq1', 'seq2', 'germline'],
        color_map=GetColorMap("dna"),
        panels=[DrawAnnotation, DrawSeqLogo, DrawMSA, DrawConsensusHisto],
        panel_params=[
            {"annotations": [["CDR1", 75, 104], ["CDR2", 156, 176], ["CDR3", 288, 344]]},
            {},
            {"show_char": True},
            {}
        ],
        figsize=[12, 24]
    )
    plt.close(fig)
    return fig

demo = gr.Interface(
    fn=generate_msaplot,
    inputs=None,
    outputs=seq_diff(
        msa=[
            "CAGGTGCACCTGCAGGAGTCGGGCCCCGGACTAGTGAAGTCTTCGGAGACCCTGTCCCTCACCTGCACTGTCTCTGGTGACTCCATCAGACGTGATACTTACTACTGGAGCTGGATCCGGCAGACTCCGGGGAAGGGACTGGAGTGGCTTGGATATGTCTTTAAAAGTGGGAGCACAAAGTACAACCCCTCCTTCAAGCGTCGAGTCGACATATCAGTAGACACGTCCAAGGAGCAGTTCTCCCTGACATTGACGTCTGTGACCACTGCGGACACGGCCGTATACTTCTGTGCGAGAGAGTGGTACTATGGTTCGGGGGCCCCCCACAACTGGCTCGACTCCTGGAGCCAGGGAACCCTGGTCACCGTCTCCTCAG",
            "CAGGTGCACCTGCAGGAGTCGGGCCCCGGACTAGTGAAGTCTTCGGAGACCCTGTCCCTCACCTGCACTGTCTCTGGTGACTCCATCAGACGTGATACTTACTACTGGAGCTGGATCCGGCAGACTCCGGGGAAGGGACTGGAGTGGCTTGGATATGTCTTTAAAAGTGGGAGCACAAAGTACAACCCCTCCTTCAAGCGTCGAGTCGACATATCAGTAGACACGTCCAAGGAGCAGTTCTCCCTGACATTGACGTCTGTGACCACTGCGGACACGGCCGTATACTTCTGTGCGAGAGAGTGGTACTATGGTTCGGGGGCCCCCCACAACTGGCTCGACTCCTGGAGCCAGGGAACCCTGGTCACCGTCTCCTCAG",
            "CAGGTGCAGCTGCAGGAGTCGGGCCCAGGACTGGTGAAGCCTTCGGAGACCCTGTCCCTCACCTGCACTGTCTCTGGTGGCTCCATCAG------TAGTTACTACTGGAGCTGGATCCGGCAGCCCCCAGGGAAGGGACTGGAGTGGATTGGGTATATCTATTACAGTGGGAGCACCAACTACAACCCCTCCCTCAAGAGTCGAGTCACCATATCAGTAGACACGTCCAAGAACCAGTTCTCCCTGAAGCTGAGCTCTGTGACCGCTGCGGACACGGCCGTGTATTACTGTGCGAGAGAGTGGTACTATGGTTCGGGGGCCCCCCACAACTGGTTCGACTCCTGGGGCCAAGGAACCCTGGTCACCGTCTCCTCAG"
        ],
        seq_names=['seq1', 'seq2', 'germline'],
        wrap=50,
        color_map=GetColorMap("dna"),
        panels=[DrawAnnotation, DrawSeqLogo, DrawMSA, DrawConsensusHisto],
        panel_params=[
            {"annotations": [["CDR1", 75, 104], ["CDR2", 156, 176], ["CDR3", 288, 344]]},
            {},
            {"show_char": True},
            {}
        ],
        width=800,
        height=1600
    ),
    title="Tonic's MSAPlot Demo",
    description="Displaying a Multiple Sequence Alignment plot using the seq_diff component."
)

if __name__ == "__main__":
    demo.launch()

```
""", elem_classes=["md-custom"], header_links=True)


    gr.Markdown("""
## `seq_diff`

### Initialization
""", elem_classes=["md-custom"], header_links=True)

    gr.ParamViewer(value=_docs["seq_diff"]["members"]["__init__"], linkify=[])


    gr.Markdown("### Events")
    gr.ParamViewer(value=_docs["seq_diff"]["events"], linkify=['Event'])




    gr.Markdown("""

### User function

The impact on the users predict function varies depending on whether the component is used as an input or output for an event (or both).

- When used as an Input, the component only impacts the input signature of the user function.
- When used as an output, the component only impacts the return signature of the user function.

The code snippet below is accurate in cases where the component is used as both an input and an output.

- **As output:** Should return, the value to be postprocessed.

 ```python
def predict(
    value: typing.Any
) -> typing.Any:
    return value
```
""", elem_classes=["md-custom", "seq_diff-user-fn"], header_links=True)




    demo.load(None, js=r"""function() {
    const refs = {};
    const user_fn_refs = {
          seq_diff: [], };
    requestAnimationFrame(() => {

        Object.entries(user_fn_refs).forEach(([key, refs]) => {
            if (refs.length > 0) {
                const el = document.querySelector(`.${key}-user-fn`);
                if (!el) return;
                refs.forEach(ref => {
                    el.innerHTML = el.innerHTML.replace(
                        new RegExp("\\b"+ref+"\\b", "g"),
                        `<a href="#h-${ref.toLowerCase()}">${ref}</a>`
                    );
                })
            }
        })

        Object.entries(refs).forEach(([key, refs]) => {
            if (refs.length > 0) {
                const el = document.querySelector(`.${key}`);
                if (!el) return;
                refs.forEach(ref => {
                    el.innerHTML = el.innerHTML.replace(
                        new RegExp("\\b"+ref+"\\b", "g"),
                        `<a href="#h-${ref.toLowerCase()}">${ref}</a>`
                    );
                })
            }
        })
    })
}

""")

demo.launch()

---
tags: [gradio-custom-component, Image, seq, sequence, multiple sequence alignment, MSA, seqlogo, histogram, consensus, pyplot, MSAplot, annotation]
title: gradio_seq_diff
short_description: Visualize Sequences and their Diffs Using MSAplot
colorFrom: blue
colorTo: yellow
sdk: gradio
pinned: false
app_file: space.py
---

# `gradio_seq_diff`
<img alt="Static Badge" src="https://img.shields.io/badge/version%20-%200.0.2%20-%20orange">  

Visualize Sequences and their Diffs Using MSAplot

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

## `seq_diff`

### Initialization

<table>
<thead>
<tr>
<th align="left">name</th>
<th align="left" style="width: 25%;">type</th>
<th align="left">default</th>
<th align="left">description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><code>value</code></td>
<td align="left" style="width: 25%;">

```python
Optional[Union[str, PIL.Image.Image, np.ndarray, Callable]]
```

</td>
<td align="left"><code>None</code></td>
<td align="left">Initial value. If callable, the function will be called whenever the app loads to set the initial value of the component.</td>
</tr>

<tr>
<td align="left"><code>msa</code></td>
<td align="left" style="width: 25%;">

```python
List[str]
```

</td>
<td align="left"><code>[]</code></td>
<td align="left">Multiple sequence alignment as a list of strings.</td>
</tr>

<tr>
<td align="left"><code>seq_names</code></td>
<td align="left" style="width: 25%;">

```python
Optional[List[str]]
```

</td>
<td align="left"><code>None</code></td>
<td align="left">List of sequence names.</td>
</tr>

<tr>
<td align="left"><code>start</code></td>
<td align="left" style="width: 25%;">

```python
Optional[int]
```

</td>
<td align="left"><code>None</code></td>
<td align="left">Start position of the alignment to display.</td>
</tr>

<tr>
<td align="left"><code>end</code></td>
<td align="left" style="width: 25%;">

```python
Optional[int]
```

</td>
<td align="left"><code>None</code></td>
<td align="left">End position of the alignment to display.</td>
</tr>

<tr>
<td align="left"><code>color_map</code></td>
<td align="left" style="width: 25%;">

```python
Optional[dict]
```

</td>
<td align="left"><code>None</code></td>
<td align="left">Custom color map for the alignment.</td>
</tr>

<tr>
<td align="left"><code>palette</code></td>
<td align="left" style="width: 25%;">

```python
Optional[str]
```

</td>
<td align="left"><code>None</code></td>
<td align="left">Color palette to use if color_map is not provided.</td>
</tr>

<tr>
<td align="left"><code>show_char</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">Whether to show characters in the alignment.</td>
</tr>

<tr>
<td align="left"><code>panels</code></td>
<td align="left" style="width: 25%;">

```python
Optional[List[Callable]]
```

</td>
<td align="left"><code>None</code></td>
<td align="left">List of panel functions to include in the MSAPlot.</td>
</tr>

<tr>
<td align="left"><code>panel_height_ratios</code></td>
<td align="left" style="width: 25%;">

```python
Optional[List[float]]
```

</td>
<td align="left"><code>None</code></td>
<td align="left">List of height ratios for the panels.</td>
</tr>

<tr>
<td align="left"><code>panel_params</code></td>
<td align="left" style="width: 25%;">

```python
Optional[List[dict]]
```

</td>
<td align="left"><code>None</code></td>
<td align="left">List of parameter dictionaries for each panel.</td>
</tr>

<tr>
<td align="left"><code>wrap</code></td>
<td align="left" style="width: 25%;">

```python
Optional[int]
```

</td>
<td align="left"><code>None</code></td>
<td align="left">Number of positions to wrap the alignment.</td>
</tr>

<tr>
<td align="left"><code>format</code></td>
<td align="left" style="width: 25%;">

```python
str
```

</td>
<td align="left"><code>"png"</code></td>
<td align="left">File format to save the image (e.g., "png", "jpg").</td>
</tr>

<tr>
<td align="left"><code>height</code></td>
<td align="left" style="width: 25%;">

```python
Optional[Union[int, str]]
```

</td>
<td align="left"><code>None</code></td>
<td align="left">Height of the displayed image.</td>
</tr>

<tr>
<td align="left"><code>width</code></td>
<td align="left" style="width: 25%;">

```python
Optional[Union[int, str]]
```

</td>
<td align="left"><code>None</code></td>
<td align="left">Width of the displayed image.</td>
</tr>

<tr>
<td align="left"><code>label</code></td>
<td align="left" style="width: 25%;">

```python
Optional[str]
```

</td>
<td align="left"><code>None</code></td>
<td align="left">The label for this component.</td>
</tr>

<tr>
<td align="left"><code>every</code></td>
<td align="left" style="width: 25%;">

```python
Optional[Union[float, "Timer"]]
```

</td>
<td align="left"><code>None</code></td>
<td align="left">Continuously calls `value` to recalculate it if `value` is a function.</td>
</tr>

<tr>
<td align="left"><code>show_label</code></td>
<td align="left" style="width: 25%;">

```python
Optional[bool]
```

</td>
<td align="left"><code>None</code></td>
<td align="left">If True, will display label.</td>
</tr>

<tr>
<td align="left"><code>container</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If True, will place the component in a container.</td>
</tr>

<tr>
<td align="left"><code>scale</code></td>
<td align="left" style="width: 25%;">

```python
Optional[int]
```

</td>
<td align="left"><code>None</code></td>
<td align="left">Relative size compared to adjacent Components.</td>
</tr>

<tr>
<td align="left"><code>min_width</code></td>
<td align="left" style="width: 25%;">

```python
int
```

</td>
<td align="left"><code>160</code></td>
<td align="left">Minimum pixel width.</td>
</tr>

<tr>
<td align="left"><code>visible</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If False, component will be hidden.</td>
</tr>

<tr>
<td align="left"><code>elem_id</code></td>
<td align="left" style="width: 25%;">

```python
Optional[str]
```

</td>
<td align="left"><code>None</code></td>
<td align="left">An optional string that is assigned as the id of this component in the HTML DOM.</td>
</tr>

<tr>
<td align="left"><code>elem_classes</code></td>
<td align="left" style="width: 25%;">

```python
Optional[Union[List[str], str]]
```

</td>
<td align="left"><code>None</code></td>
<td align="left">An optional list of strings that are assigned as the classes of this component in the HTML DOM.</td>
</tr>

<tr>
<td align="left"><code>render</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If False, component will not be rendered in the Blocks context.</td>
</tr>

<tr>
<td align="left"><code>show_download_button</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If True, will display button to download image.</td>
</tr>

<tr>
<td align="left"><code>show_share_button</code></td>
<td align="left" style="width: 25%;">

```python
Optional[bool]
```

</td>
<td align="left"><code>None</code></td>
<td align="left">If True, will show a share icon in the corner of the component.</td>
</tr>
</tbody></table>


### Events

| name | description |
|:-----|:------------|
| `change` | Triggered when the value of the seq_diff changes either because of user input (e.g. a user types in a textbox) OR because of a function update (e.g. an image receives a value from the output of an event trigger). See `.input()` for a listener that is only triggered by user input. |
| `select` | Event listener for when the user selects or deselects the seq_diff. Uses event data gradio.SelectData to carry `value` referring to the label of the seq_diff, and `selected` to refer to state of the seq_diff. See EventData documentation on how to use this event data |



### User function

The impact on the users predict function varies depending on whether the component is used as an input or output for an event (or both).

- When used as an Input, the component only impacts the input signature of the user function.
- When used as an output, the component only impacts the return signature of the user function.

The code snippet below is accurate in cases where the component is used as both an input and an output.

- **As input:** Should return, the value to be postprocessed.

 ```python
 def predict(
     value: typing.Any
 ) -> typing.Any:
     return value
 ```
 

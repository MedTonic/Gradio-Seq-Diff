from __future__ import annotations

import warnings
from pathlib import Path
from typing import Any, Callable, List, Literal, Optional, Union

import numpy as np
import PIL.Image
import matplotlib.pyplot as plt
from gradio_client import handle_file
from gradio_client.documentation import document

from gradio import utils, image_utils
from gradio.components.base import Component
from gradio.data_classes import FileData
from gradio.events import Events

import pandas as pd
import matplotlib.patches as patches
import matplotlib.transforms as transforms
from matplotlib.transforms import Affine2D
import math
from matplotlib.patheffects import RendererBase
import matplotlib.patheffects as PathEffects
import seaborn as sns

from .msaplot import (
    DrawMSA,
    DrawComplexMSA,
    GetColorMap,
    GetStartEnd,
    DrawConsensusHisto,
    DrawSeqLogo,
    DrawAnnotation,
)

class seq_diff(Component):
    """
    Creates a sequence difference component that displays MSAPlot images as output.
    """

    EVENTS = [Events.change, Events.select]

    data_model = FileData

    def __init__(
        self,
        value: Optional[Union[str, PIL.Image.Image, np.ndarray, Callable]] = None,
        *,
        msa: List[str],
        seq_names: Optional[List[str]] = None,
        start: Optional[int] = None,
        end: Optional[int] = None,
        color_map: Optional[dict] = None,
        palette: Optional[str] = None,
        show_char: bool = True,
        panels: Optional[List[Callable]] = None,
        panel_height_ratios: Optional[List[float]] = None,
        panel_params: Optional[List[dict]] = None,
        wrap: Optional[int] = None,
        format: str = "png",
        height: Optional[Union[int, str]] = None,
        width: Optional[Union[int, str]] = None,
        label: Optional[str] = None,
        every: Optional[Union[float, 'Timer']] = None,
        show_label: Optional[bool] = None,
        container: bool = True,
        scale: Optional[int] = None,
        min_width: int = 160,
        visible: bool = True,
        elem_id: Optional[str] = None,
        elem_classes: Optional[Union[List[str], str]] = None,
        render: bool = True,
        show_download_button: bool = True,
        show_share_button: Optional[bool] = None,
    ):
        """
        Parameters:
            value: Initial value. If callable, the function will be called whenever the app loads to set the initial value of the component.
            msa: Multiple sequence alignment as a list of strings.
            seq_names: List of sequence names.
            start: Start position of the alignment to display.
            end: End position of the alignment to display.
            color_map: Custom color map for the alignment.
            palette: Color palette to use if color_map is not provided.
            show_char: Whether to show characters in the alignment.
            panels: List of panel functions to include in the MSAPlot.
            panel_height_ratios: List of height ratios for the panels.
            panel_params: List of parameter dictionaries for each panel.
            wrap: Number of positions to wrap the alignment.
            format: File format to save the image (e.g., "png", "jpg").
            height: Height of the displayed image.
            width: Width of the displayed image.
            label: The label for this component.
            every: Continuously calls `value` to recalculate it if `value` is a function.
            show_label: If True, will display label.
            container: If True, will place the component in a container.
            scale: Relative size compared to adjacent Components.
            min_width: Minimum pixel width.
            visible: If False, component will be hidden.
            elem_id: An optional string that is assigned as the id of this component in the HTML DOM.
            elem_classes: An optional list of strings that are assigned as the classes of this component in the HTML DOM.
            render: If False, component will not be rendered in the Blocks context.
            show_download_button: If True, will display button to download image.
            show_share_button: If True, will show a share icon in the corner of the component.
        """
        self.msa = msa
        self.seq_names = seq_names
        self.start = start
        self.end = end
        self.color_map = color_map
        self.palette = palette
        self.show_char = show_char
        self.panels = panels
        self.panel_height_ratios = panel_height_ratios
        self.panel_params = panel_params
        self.wrap = wrap
        self.format = format
        self.height = height
        self.width = width
        self.show_download_button = show_download_button
        self.show_share_button = (
            (utils.get_space() is not None)
            if show_share_button is None
            else show_share_button
        )

        super().__init__(
            label=label,
            every=every,
            show_label=show_label,
            container=container,
            scale=scale,
            min_width=min_width,
            visible=visible,
            elem_id=elem_id,
            elem_classes=elem_classes,
            render=render,
            value=value,
        )

    def postprocess(self, value: Any) -> FileData:
        """
        Parameters:
            value: The value to be postprocessed.
        Returns:
            A FileData object containing the MSAPlot image.
        """
        if value is None:
            return None

        # Generate the MSAPlot image
        fig, axes = DrawComplexMSA(
            self.msa,
            panels=self.panels or [DrawMSA],
            seq_names=self.seq_names,
            panel_height_ratios=self.panel_height_ratios,
            panel_params=self.panel_params,
            color_map=self.color_map,
            start=self.start,
            end=self.end,
            wrap=self.wrap,
            figsize=(self.width, self.height) if self.width and self.height else None,
        )

        # Save the figure to a BytesIO object
        from io import BytesIO
        buf = BytesIO()
        fig.savefig(buf, format=self.format, bbox_inches='tight')
        buf.seek(0)
        plt.close(fig)

        # Save the image to the Gradio cache
        saved_path = image_utils.save_image(buf, self.GRADIO_CACHE, self.format)
        
        return FileData(path=saved_path, orig_name=f"msaplot.{self.format}")

    def preprocess(self, payload: FileData | None) -> Any:
        """
        This method is not used for output-only components, but is included for compatibility.
        """
        return payload

    def example_payload(self) -> Any:
        return FileData(path="path/to/example/msaplot.png", orig_name="example_msaplot.png")

    def example_value(self) -> Any:
        return "path/to/example/msaplot.png"
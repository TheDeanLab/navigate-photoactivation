# Copyright (c) 2021-2024  The University of Texas Southwestern Medical Center.
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted for academic and research use only (subject to the
# limitations in the disclaimer below) provided that the following conditions are met:

#      * Redistributions of source code must retain the above copyright notice,
#      this list of conditions and the following disclaimer.

#      * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.

#      * Neither the name of the copyright holders nor the names of its
#      contributors may be used to endorse or promote products derived from this
#      software without specific prior written permission.

# NO EXPRESS OR IMPLIED LICENSES TO ANY PARTY'S PATENT RIGHTS ARE GRANTED BY
# THIS LICENSE. THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND
# CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
# IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.


#  Standard Library Imports
import tkinter as tk
from tkinter import ttk

# Third Party Imports

# Local Imports
from navigate.view.custom_widgets.validation import ValidatedSpinbox
from navigate.view.custom_widgets.validation import ValidatedEntry


class PhotoactivationFrame(ttk.Frame):
    """Plugin Frame: Just an example

    This frame contains the widgets for the plugin.
    """

    def __init__(self, root, *args, **kwargs):
        """Initialization of the  Frame

        Parameters
        ----------
        root : tkinter.ttk.Frame
            The frame that this frame will be placed in.
        *args
            Variable length argument list.
        **kwargs
            Arbitrary keyword arguments.
        """
        ttk.Frame.__init__(self, root, *args, **kwargs)

        # Formatting
        tk.Grid.columnconfigure(self, "all", weight=1)
        tk.Grid.rowconfigure(self, "all", weight=1)

        #: dict: Dictionary of the widgets in the frame
        self.inputs = {}

        #: dict: Dictionary of the variables for the widgets in the frame
        self.variables = {}

        # Title, index 0, 0.
        label = ttk.Label(self, text="Photoactivation Plugin")
        label.grid(row=0, column=0, sticky=tk.NW)

        # Dictionary of widgets. Keys are labels, values are the widget classes.
        widget_dict = {
            "Laser": ttk.Combobox,
            "Power": ValidatedSpinbox,
            "Duration (ms)": ValidatedSpinbox,
            "Pattern": ttk.Combobox,
            "Pinout - X Galvo": ValidatedEntry,
            "Pinout - Y Galvo": ValidatedEntry,
            "Pinout - Laser Switch": ValidatedEntry,
            "Volts per Micron - X": ValidatedEntry,
            "Volts per Micron - Y": ValidatedEntry,
            "Photoactivation Offset X": ValidatedEntry,
            "Photoactivation Offset Y": ValidatedEntry,
        }

        # Create the widgets
        counter = 1
        for key, widget in widget_dict.items():
            label = f"{key:<30}"
            ttk.Label(self, text=label).grid(
                row=counter, column=0, pady=3, padx=5, sticky=tk.NW
            )
            self.variables[key] = tk.StringVar()
            self.inputs[key] = widget(self, textvariable=self.variables[key], width=20)
            self.inputs[key].grid(row=counter, column=1, pady=3, padx=5)
            counter += 1

    def get_variables(self):
        """Returns a dictionary of the variables for the widgets in this frame.

        The key is the widget name, value is the variable associated.

        Returns
        -------
        variables : dict
            Dictionary of the variables for the widgets in this frame.
        """
        return self.variables

    def get_widgets(self):
        """Returns a dictionary of the widgets in this frame.

        The key is the widget name, value is the LabelInput class that has all the data.

        Returns
        -------
        self.inputs : dict
            Dictionary of the widgets in this frame.
        """
        return self.inputs

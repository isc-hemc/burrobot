"""plotter.

Module dedicated to graph results from nlp process.

"""
from typing import Dict, List

import matplotlib.pyplot as plt
import numpy as np


class Plotteus:
    """Plotteus.

    Class with the necessary functionality to build from raw data, graphs for
    an easy visual understanding.

    Attributes
    ----------
    data: Dict
        Data to graph.

    """

    __slots__ = ("_data",)

    def __init__(self, data: Dict):
        """Constructor.

        Parameters
        ----------
        data: Dict
            Data to graph.

        """
        self._data = data

    @property
    def data(self) -> Dict:
        """Data.

        Class attribute `data` property.

        Returns
        -------
        Dict
            Class attribute `data`.

        """
        return self._data

    @data.setter
    def data(self, data: Dict):
        """Data.

        Class attribute `data` setter.

        Parameters
        ----------
        data: Dict
            Data to graph.

        """
        self._data = data

    @property
    def __values(self) -> List:
        """DataValues.

        Gets the values of the data attribute.

        Returns
        -------
        List
            Dictionary values.

        """
        return list(self._data.values())

    @property
    def __keys(self) -> List:
        """Data-Keys.

        Gets the keys of the data attribute.

        Returns
        -------
        List
            Dictionary keys.

        """
        return list(self._data.keys())

    @property
    def themes(self) -> List:
        """Themes.

        Get the available themes of matplotlib.pyplot library.

        Returns
        -------
        List
            Available themes.

        """
        return plt.style.available

    def style(self, theme: str):
        """Style.

        Set the styles of the plot.

        Parameters
        ----------
        theme: str
            Style to use only if exists in matplotlib.pyplot.style.available,
            otherwise uses the default.

        """
        if theme in self.themes:
            plt.style.use(theme)

    def barplot(
        self, xlim: List, xlabel: str = "", ylabel: str = "", title: str = ""
    ):
        """Barplot.

        Creates a basic barplot using the data from the class attributes.

        Parameters
        ----------
        xlim: List
            Graph limit of the `x` axis.
        xlabel: str
            `X`axis label.
        ylabel: str
            `Y`axis label.
        title: str
            Plot title.

        """
        values: List = self.__values
        keys: List = self.__keys
        _, ax = plt.subplots()
        ax.barh(keys, values)
        ax.set(xlim=xlim, xlabel=xlabel, ylabel=ylabel, title=title)
        plt.show()

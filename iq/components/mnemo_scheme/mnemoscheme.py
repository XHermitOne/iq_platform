#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Mnemoscheme manager.
"""

import os.path

from ...util import log_func
from ...util import file_func

from ...engine.wx import wxbitmap_func

__version__ = (0, 0, 0, 1)

# Conversion start command format SVG -> PNG
SVG2PNG_CONVERT_CMD_FMT = 'convert -background none -resize %dx%d -extent %dx%d -gravity center %s %s'


class iqMnemoSchemeManager(object):
    """
    Mnemoscheme manager.
    """
    def __init__(self, *args, **kwargs):
        """
        Constructor.
        """
        self._svg_background = None
        self._background_bitmap = None

        self._svg_size = (0.0, 0.0)

    def setSVGSize(self, svg_width, svg_height):
        """
        Set SVG size in original units.

        :param svg_width: SVG width in source units.
        :param svg_height: SVG height in source units.
        """
        self._svg_size = (svg_width, svg_height)

    def getSVGSize(self):
        """
        SVG size in source units.
        """
        return self._svg_size

    def setSVGBackground(self, svg_filename, auto_draw=True):
        """
        Set mnemoscheme background.

        :param svg_filename: The full name of the SVG mimic background file.
        :param auto_draw: Automatically draw on a mnemonic context?
        :return: True/False.
        """
        if not svg_filename:
            log_func.error(u'Not defined SVG mimic background file')
            return False

        if not os.path.exists(svg_filename):
            log_func.error(u'Not found SVG mimic background file <%s>' % svg_filename)
            return False

        self._svg_background = svg_filename
        if auto_draw:
            self.drawBackground()

        return True

    def getAnchors(self):
        """
        List of mnemonic anchors.
        """
        log_func.error(u'Undefined method for obtaining a list of mnemonic anchors')
        return list()

    def getControls(self):
        """
        List of active mnemonic controls.
        """
        log_func.error(u'The method for obtaining the list of controls of the mnemonic scheme is not defined')
        return list()

    def layoutAll(self, auto_refresh=True):
        """
        The method of arranging and dimensioning controls mnemonic diagrams according to the anchors.

        :param auto_refresh: Automatically refresh the mnemoscheme object.
        :return: True/False.
        """
        log_func.error(u'The method of arrangement and dimensioning of controls of the mnemonic diagram is not defined')
        return False

    def drawBackground(self, auto_rewrite=False):
        """
        Draw the background of the mnemonic on the device context.
        ATTENTION! To extract an image from an SVG file
        The external SVG -> PNG conversion utility is used.
        And PNG is already displayed on the device context.

        :param auto_rewrite: Automatically overwrite the intermediate PNG file.         :return: True/False.
        :return: True/False.
        """
        try:
            # Mimic panel size
            width, height = self.GetSize()

            png_filename = os.path.join(file_func.getProjectProfilePath(),
                                        '%s_background_%dx%d.png' % (self.getName(), width, height))
            svg_filename = os.path.join(file_func.getProjectProfilePath(),
                                        os.path.basename(self._svg_background))
            # Save SVG file to HOME folder             
            # This is done so that you can replace the mnemonic diagram on
            # the fly
            if not os.path.exists(svg_filename) or not file_func.isSameFile(svg_filename, self._svg_background):
                # If the file has changed, then overwrite it in the HOME folder
                file_func.copyFile(self._svg_background, svg_filename)
                # and delete all PNG files
                file_func.delFilesByMask(file_func.getProjectProfilePath(),
                                         '%s_background_*.png' % self.getName())

            if not os.path.exists(png_filename) or auto_rewrite:
                # Launch file conversion
                cmd = SVG2PNG_CONVERT_CMD_FMT % (width, height, width, height, svg_filename, png_filename)
                log_func.info(u'Start SVG -> PNG covert command: <%s> ' % cmd)
                os.system(cmd)
                if not os.path.exists(png_filename):
                    log_func.error(u'Conversion error SVG -> PNG (<%s> -> <%s>)' % (svg_filename, png_filename))
                    return False

            self._background_bitmap = wxbitmap_func.createBitmap(png_filename)
            return True
        except:
            log_func.fatal(u'Mnemoscheme background rendering error')
        return False

    def getBackgroundBitmap(self):
        """
        A picture object to display the background.

        :return: The wx.Bitmap object corresponding to the current background of the mnemonic.
        """
        return self._background_bitmap

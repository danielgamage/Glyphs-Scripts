#MenuTitle: Refresh Preview
# -*- coding: utf-8 -*-
__doc__ = """
Manually updates the preview window.
Useful for actions that don't automatically update the preview
like changing the interpolation settings of an instance.
"""

Glyphs.currentDocument.windowController().activeEditViewController().updatePreview()

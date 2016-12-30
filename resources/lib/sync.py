from utilities import *

LANGUAGE = sys.modules[ "__main__" ].LANGUAGE

class GUI(xbmcgui.WindowXMLDialog):
    def __init__(self, *args, **kwargs):
        self.function = kwargs['function']
        self.offset = kwargs['offset']

    def onInit(self):
        self.val = 0.0
        self._get_controls()
        self._init_values()
        self.exit = False
        while (not xbmc.Monitor().abortRequested()) and xbmc.getCondVisibility('Player.HasAudio') and (not self.exit):
            xbmc.sleep(500)
        self.close()

    def _get_controls(self):
        self.header = self.getControl(10)
        self.slider = self.getControl(11)
        self.label = self.getControl(12)

    def _init_values(self):
        self.header.setLabel(LANGUAGE(32003))
        string = self._get_string(self.offset)
        self.label.setLabel(string)
        self.slider.setPercent((self.offset * 10.0) + 50.0)

    def _get_string(self, val):
        if val > 0.0:
            string = LANGUAGE(32009) % str(val)
        elif val < 0.0:
            string = LANGUAGE(32008) % str(-val)
        else:
            string = str(val)
        return string

    def onAction(self, action):
        if action.getId() in CANCEL_DIALOG:
            self.exit = True
            self.close()
        else:
            val = self.slider.getPercent()
            self.val = round((val - 50.0) / 10.0, 1)
            string = self._get_string(self.val)
            self.label.setLabel(string)
            self.function(self.val)

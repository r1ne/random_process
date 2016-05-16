import os
import xalglib as alg
import wx
import pandas
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


class AppFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(350, 500),
                          style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))

        panel = wx.Panel(self)
        self.quote = wx.StaticText(panel, label=u'\u041a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438'
                                                u'\u043e\u043d\u043d\u0430\u044f \u0444\u0443\u043d\u043a\u0446'
                                                u'\u0438\u044f:', pos=(20, 30))
        self.quote = wx.StaticText(panel,
                                   label=u'\u0421\u0440\u0435\u0434\u043d\u0435\u043a\u0432. '
                                         u'\u043e\u0442\u043a\u043b-\u0435 \u0421\u041f:',
                                   pos=(20, 60))
        self.quote = wx.StaticText(panel, label=u'\u041c\u0430\u0442. \u043e\u0436\u0438\u0434\u0430\u043d\u0438\u0435 '
                                                u'\u0421\u0412:', pos=(20, 90))
        self.quote = wx.StaticText(panel,
                                   label=u'\u0421\u0440\u0435\u0434\u043d\u0435\u043a\u0432. '
                                         u'\u043e\u0442\u043a\u043b-\u0435 \u0421\u0412:',
                                   pos=(20, 120))
        self.quote = wx.StaticText(panel, label=u'\u041a\u043e\u044d\u0444. '
                                                u'\u043a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u0438:',
                                   pos=(20, 150))
        self.quote = wx.StaticText(panel, label="N: ", pos=(20, 180))
        self.quote = wx.StaticText(panel, label="p: ", pos=(20, 210))
        self.quote = wx.StaticText(panel, label="Size: ", pos=(20, 240))

        self.button = wx.Button(panel, wx.ID_OK, label=u'\u0421\u0442\u0430\u0440\u0442', pos=(100, 410),
                                size=(140, 50))

        self.funcList = [u'\u0425\u0430\u0431\u0438\u0431\u0438', u'\u0411\u0435\u0441\u0441\u0435\u043b\u044f',
                         u'\u042d\u043a\u0441\u043f\u043e\u043d\u0435\u043d\u0446\u0438\u0430\u043b\u044c\u043d\u0430'
                         u'\u044f', u'\u0421\u0438\u043d\u0443\u0441', 'sin(x)/x',
                         u'\u0413\u0430\u0443\u0441\u0441\u0430',
                         u'\u0422\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u0430\u044f']

        self.edit_func = wx.ComboBox(panel, pos=(180, 25), size=(140, -1), choices=self.funcList, style=wx.CB_READONLY)
        self.edit1 = wx.TextCtrl(panel, value="1", pos=(180, 55), size=(140, -1))
        self.edit2 = wx.TextCtrl(panel, value="", pos=(180, 85), size=(140, -1))
        self.edit3 = wx.TextCtrl(panel, value="", pos=(180, 115), size=(140, -1))
        self.edit4 = wx.TextCtrl(panel, value="", pos=(180, 145), size=(140, -1))
        self.edit5 = wx.TextCtrl(panel, value="20", pos=(180, 175), size=(140, -1))
        self.edit6 = wx.TextCtrl(panel, value="0.5", pos=(180, 205), size=(140, -1))
        self.edit7 = wx.TextCtrl(panel, value="2000", pos=(180, 235), size=(140, -1))

        self.Bind(wx.EVT_BUTTON, self.onClick, self.button)

        self.Show(True)

    def getR(self):
        return np.random.random()

    def onClick(self, e):
        size = int(self.edit7.Value)
        # Habibi
        if self.edit_func.Value == u'\u0425\u0430\u0431\u0438\u0431\u0438':
            pass
        # Bessel
        elif self.edit_func.Value == u'\u0411\u0435\u0441\u0441\u0435\u043b\u044f':
            p = float(self.edit6.Value)
            N = int(self.edit5.Value)
            sqrtN = 1 / np.sqrt(N)
            bessel = []

            for i in range(0, size, 1):
                sum = 0
                for x in range(1, N + 1, 1):
                    sum += np.sqrt((-2) * np.log(self.getR())) * np.cos(
                        x * p * np.cos(np.pi * (x - self.getR()) / N) + 2 * np.pi * self.getR())
                bessel.append(sqrtN * sum)

            max_p = -999
            max_n = 1

            for i in range(0, size, 1):
                if max_p < bessel[i]:
                    max_p = bessel[i]
                elif max_n > bessel[i]:
                    max_n = bessel[i]

            for i in range(0, size, 1):
                bessel[i] -= max_n
                bessel[i] /= (max_p - max_n)

            bessel_int = []
            for i in range(0, size, 1):
                bessel_int.append(int(bessel[i] * 255))

            print bessel_int
            plt.plot(range(0, size), bessel_int, alpha=0.5)
            plt.show()
        # Exponential
        elif self.edit_func.Value == \
                u'\u042d\u043a\u0441\u043f\u043e\u043d\u0435\u043d\u0446\u0438\u0430\u043b\u044c\u043d\u0430\u044f':
            pass
        # Sinus
        elif self.edit_func.Value == u'\u0421\u0438\u043d\u0443\u0441':
            pass

        # sin(x)/x
        elif self.edit_func.Value == 'sin(x)/x':
            sig = float(self.edit1.Value)
            a = float(self.edit6.Value)
            p = int(np.ceil(2 / a))
            s = np.random.standard_normal(size)
            x = []
            for i in range(0, size - p, 1):
                sum = 0
                for k in range(-p, p + 1, 1):
                    sum += s[i - k] * (sig / np.sqrt(np.pi) * a) * np.sin(a * k) / k
                x.append(sum)

            plt.title('sin(x)/x')
            plt.plot(range(0, size), s, alpha=0.5)
            plt.show()

        # Gauss
        elif self.edit_func.Value == u'\u0413\u0430\u0443\u0441\u0441\u0430':
            g = np.sqrt(0.05) * np.random.normal(0.0, 1.0, 8192)
            plt.scatter(range(0, 8192), g, alpha=0.5)
            plt.show()

        # Triangle
        elif self.edit_func.Value == u'\u0422\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u0430\u044f':
            sig = float(self.edit1.Value)
            M = int(self.edit5.Value)
            s = np.random.standard_normal(size)
            x = []
            for i in range(0, size, 1):
                sum = 0
                for k in range(0, M, 1):
                    sum += s[i - k]
                sum *= sig / np.sqrt(M)
                x.append(sum)

            for i in range(0, M, 1):
                del x[M]

            plt.title('Triangle')
            plt.plot(range(0, size - M), x, alpha=0.5)
            plt.show()
        else:
            wx.MessageBox(u'\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0444\u0443\u043d\u043a\u0446\u0438\u044e'
                          , u'\u041f\u0440\u0435\u0434\u0443\u043f\u0440\u0435\u0436\u0434\u0435\u043d\u0438\u0435',
                          wx.OK | wx.ICON_INFORMATION)


app = wx.App(False)
frame = AppFrame(None,
                 u'\u041f\u043e\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435 '
                 u'\u0441\u043b\u0443\u0447\u0430\u0439\u043d\u043e\u0433\u043e '
                 u'\u043f\u0440\u043e\u0446\u0435\u0441\u0441\u0430')

app.MainLoop()

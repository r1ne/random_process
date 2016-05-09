import wx
import pandas
import matplotlib.pyplot as plt
import numpy
import seaborn as sns


class AppFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(350, 300),
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


        self.button = wx.Button(panel, label=u'\u0421\u0442\u0430\u0440\u0442', pos=(100, 210), size=(140, 50))
        # self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)


        self.funcList = [u'\u0425\u0430\u0431\u0438\u0431\u0438', u'\u0411\u0435\u0441\u0441\u0435\u043b\u044f',
                         u'\u042d\u043a\u0441\u043f\u043e\u043d\u0435\u043d\u0446\u0438\u0430\u043b\u044c\u043d\u0430'
                         u'\u044f', u'\u0421\u0438\u043d\u0443\u0441']

        self.edit_func = wx.ComboBox(panel, pos=(180, 25), size=(140, -1), choices=self.funcList, style=wx.CB_READONLY)
        self.edit1 = wx.TextCtrl(panel, value="", pos=(180, 55), size=(140, -1))
        self.edit2 = wx.TextCtrl(panel, value="", pos=(180, 85), size=(140, -1))
        self.edit3 = wx.TextCtrl(panel, value="", pos=(180, 115), size=(140, -1))
        self.edit4 = wx.TextCtrl(panel, value="", pos=(180, 145), size=(140, -1))
        self.edit5 = wx.TextCtrl(panel, value="", pos=(180, 175), size=(140, -1))

        self.Show(True)


app = wx.App(False)
frame = AppFrame(None,
                 u'\u041f\u043e\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435 '
                 u'\u0441\u043b\u0443\u0447\u0430\u0439\u043d\u043e\u0433\u043e '
                 u'\u043f\u0440\u043e\u0446\u0435\u0441\u0441\u0430')

# X = numpy.random.uniform(0, 10, 100)
# Y = X + numpy.random.uniform(0, 2, 100)
# plt.scatter(X, Y, alpha=0.5)
# plt.show()

data = pandas.read_csv("casualties.csv")
cm = data.corr()
sns.heatmap(cm, square=True)
plt.yticks(rotation=0)
plt.xticks(rotation=90)

app.MainLoop()


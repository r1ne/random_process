#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx
import matplotlib.pyplot as plt
import numpy as np


class AppFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(350, 500),
                          style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))

        panel = wx.Panel(self)
        self.quote = wx.StaticText(panel, label='Корреляционная функция:', pos=(20, 30))
        self.quote = wx.StaticText(panel, label='Среднекв-е откл. СП:', pos=(20, 60))
        self.quote = wx.StaticText(panel, label='Мат. ожидание СВ:', pos=(20, 90))
        self.quote = wx.StaticText(panel, label='Среднекв-е откл. СВ:', pos=(20, 120))
        self.quote = wx.StaticText(panel, label='N:', pos=(20, 150))
        self.quote = wx.StaticText(panel, label="M: ", pos=(20, 180))
        self.quote = wx.StaticText(panel, label="p: ", pos=(20, 210))
        self.quote = wx.StaticText(panel, label="Кол-во точек: ", pos=(20, 240))
        self.quote = wx.StaticText(panel, label="Интервал корреляции: ", pos=(20, 270))

        self.button = wx.Button(panel, wx.ID_OK, label=u'\u0421\u0442\u0430\u0440\u0442', pos=(100, 410),
                                size=(140, 50))

        self.funcList = ['Хабиби', 'Бесселя', 'Экспоненциальная', 'Синус', 'sin(x)/x', 'N/A', 'Треугольная']

        self.edit_func = wx.ComboBox(panel, pos=(180, 25), size=(140, -1), choices=self.funcList, style=wx.CB_READONLY)
        self.edit1 = wx.TextCtrl(panel, value="1", pos=(180, 55), size=(140, -1))
        self.edit2 = wx.TextCtrl(panel, value="0", pos=(180, 85), size=(140, -1))
        self.edit3 = wx.TextCtrl(panel, value="1", pos=(180, 115), size=(140, -1))
        self.edit4 = wx.TextCtrl(panel, value="20", pos=(180, 145), size=(140, -1))
        self.edit5 = wx.TextCtrl(panel, value="20", pos=(180, 175), size=(140, -1))
        self.edit6 = wx.TextCtrl(panel, value="0.5", pos=(180, 205), size=(140, -1))
        self.edit7 = wx.TextCtrl(panel, value="2000", pos=(180, 235), size=(140, -1))
        self.edit8 = wx.TextCtrl(panel, value="50", pos=(180, 265), size=(140, -1))

        self.Bind(wx.EVT_BUTTON, self.onClick, self.button)

        self.Show(True)

    def onClick(self, e):
        size = int(self.edit7.Value)
        # Хабиби
        # Использует три поля:
        # p - для задания корреляции
        # Среднекв. откл. СП
        # Среднекв. откл. случ. величины
        if self.edit_func.Value == u'\u0425\u0430\u0431\u0438\u0431\u0438':
            p = float(self.edit6.Value)
            sig_proc = float(self.edit1.Value)
            sig_rand_value = float(self.edit3.Value)
            habibi = []
            x0 = sig_proc * np.random.normal(0, sig_rand_value)
            habibi.append(x0)
            for i in range(1, size, 1):
                habibi.append(p * habibi[i - 1] + sig_proc * np.sqrt(1 - p) * np.random.normal(0, sig_rand_value))

            np.savetxt('habibi.txt', habibi, delimiter=',')

            plt.title('Habibi')
            plt.plot(range(0, size), habibi, alpha=0.5)
        # Бессель
        # Использует два поля:
        # p - для задания корреляции
        # M - граница интегрирования
        elif self.edit_func.Value == u'\u0411\u0435\u0441\u0441\u0435\u043b\u044f':
            p = float(self.edit6.Value)
            M = int(self.edit5.Value)
            sqrtM = 1 / np.sqrt(M)
            bessel = []
            am = np.random.uniform()
            bm = np.random.uniform()

            for i in range(0, size, 1):
                sum = 0
                for x in range(1, M + 1, 1):
                    sum += np.sqrt(-2 * np.log(am)) * np.cos(
                        i * p * np.cos((x - am) / M) + 2 * np.pi * bm)
                bessel.append(sqrtM * sum)

            # max_p = -999
            # max_n = 1
            #
            # for i in range(0, size, 1):
            #     if max_p < bessel[i]:
            #         max_p = bessel[i]
            #     elif max_n > bessel[i]:
            #         max_n = bessel[i]
            #
            # for i in range(0, size, 1):
            #     bessel[i] -= max_n
            #     bessel[i] /= (max_p - max_n)
            #
            # bessel_int = []
            # for i in range(0, size, 1):
            #     bessel_int.append(int(bessel[i] * 255))

            np.savetxt('habibi.txt', bessel, delimiter=',')

            plt.title('Bessel')
            plt.plot(range(0, size), bessel, alpha=0.5)
        # Экспоненциальная
        # Использует 2 поля
        # p - для корреляции
        # sig - среднекв. откл. СП
        elif self.edit_func.Value == \
                u'\u042d\u043a\u0441\u043f\u043e\u043d\u0435\u043d\u0446\u0438\u0430\u043b\u044c\u043d\u0430\u044f':
            sig = float(self.edit1.Value)
            p = float(self.edit6.Value)

            k2 = np.exp(-p)
            k1 = sig * np.sqrt(1 - k2 * k2)
            exponent = []
            exponent.append(np.random.normal(0, p, 1))
            for i in range(1, size, 1):
                exponent.append(k1 * np.random.standard_normal() + k2 * exponent[i - 1])

            np.savetxt('exp.txt', exponent, delimiter=',')

            plt.title('exp(x)')
            plt.plot(range(0, size), exponent, alpha=0.5)
        # Синус
        # Используемые поля:
        # M, N - пределы интегрирования
        # p - корреляция
        elif self.edit_func.Value == u'\u0421\u0438\u043d\u0443\u0441':
            N = int(self.edit4.Value)
            M = int(self.edit5.Value)
            p = float(self.edit6.Value)
            sqrtM = 1 / np.sqrt(M)
            a = []
            b = []
            g = []

            for n in range(0, N, 1):
                a.append(np.random.uniform(0, 1, M))
                b.append(np.random.uniform(0, 1, M))
                g.append(np.random.uniform())

            sin = []
            for i in range(0, size, 1):
                sum = 0
                for n in range(1, N + 1, 1):
                    mu = p * np.sqrt(1 - np.square(g[n - 1] - 1))
                    for m in range(1, M + 1, 1):
                        sum += np.sqrt(-2 * np.log(a[n - 1][m - 1])) * np.cos(
                            i * mu * np.cos((m - a[n - 1][m - 1]) / M) + 2 * np.pi * b[n - 1][m - 1])

                sin.append(sum * sqrtM)

            np.savetxt('sin.txt', sin, delimiter=',')

            plt.title('sin(x)')
            plt.plot(range(0, size), sin, alpha=0.5)

        # sin(x)/x
        elif self.edit_func.Value == 'sin(x)/x':
            sig = float(self.edit1.Value)
            a = float(self.edit6.Value)
            p = int(np.ceil(2 / a))
            s = np.random.standard_normal(size)
            x = []

            for i in range(p, size - p, 1):
                sum = 0
                for k in range(-p, p + 1, 1):
                    if k != 0:
                        c = (sig / np.sqrt(np.pi) * a) * np.sin(a * k) / k
                        sum += c * s[i - k]
                x.append(sum)

            np.savetxt('sinx-1.txt', x, delimiter=',')

            plt.title('sin(x)/x')         	
            plt.plot(range(0, size - 2 * p), x, alpha=0.5)

        # N/A
        elif self.edit_func.Value == u'\u0413\u0430\u0443\u0441\u0441\u0430':
            pass

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

            np.savetxt('trig.txt', x, delimiter=',')

            plt.title('Triangle')
            plt.plot(range(0, size - M), x, alpha=0.5)
        else:
            wx.MessageBox('Выберите функцию', 'Предупреждение', wx.OK | wx.ICON_INFORMATION)

        plt.ion()
        plt.draw()
        plt.show()

app = wx.App(False)
frame = AppFrame(None, 'Построение случайных процессов')

app.MainLoop()
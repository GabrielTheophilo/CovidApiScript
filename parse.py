class Parse:
    def ParseCountryData(wdata, i):
        a = (wdata["response"][i]["continent"])
        b = (wdata["response"][i]["country"])
        c = (wdata["response"][i]["population"])
        return (f'\nContinente: {a}\nPaís: {b}\nPopulação: {c}')

    def ParseFirstData(wdata, i):
        d = (wdata["response"][i]["cases"]["new"])
        e = (wdata["response"][i]["cases"]["active"])
        f = (wdata["response"][i]["cases"]["critical"])
        g = (wdata["response"][i]["cases"]["recovered"])
        h = (wdata["response"][i]["cases"]["total"])
        return (f"\n\nNovos casos: {d}\nCasos ativos: {e}\nCasos críticos: {f}\nRecuperados: {g}\nCasos Totais: {h}\n\nMortes Totais: {i}\n")

    def ParseSecondData(wdata, i):
        i1 = (wdata["response"][i]["deaths"]["total"])
        j = (wdata["response"][i]["deaths"]["new"])
        return (f'Mortes Totais: {i1}\nMortes no período: {j}\n\n')
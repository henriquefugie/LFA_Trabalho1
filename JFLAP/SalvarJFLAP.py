import xml.etree.cElementTree as ETc
from AutomatoFD import AutomatoFD

class SalvarJFLAP():
    
    def __init__(self, afd : AutomatoFD, caminho, nome):
        self.afd = afd
        self.caminho = caminho
        self.nome = nome

    def salvarAFD(self):
        
        root = ETc.Element("structure")
        ETc.SubElement(root, "type").text = "fa"
        doc = ETc.SubElement(root, "automaton")
        
        for e in self.afd.estados:
            sub =  ETc.SubElement(doc, "state")
            sub.set('id', e)
            sub.set('name', e)
            if e == self.afd.inicial:
                ETc.SubElement(sub,"initial")
            if self.afd.estadoFinal:
                ETc.SubElement(sub, "final")
                
        for (e, step) in self.afd.transicoes.keys():
            for(a, after) in step.items():
                for d in after:
                    tran = ETc.SubElement(doc, "transition")
                    d = self.afd.transicoes[(e, a)]
                    ETc.SubElement(tran, "from").text = str(e)
                    ETc.SubElement(tran, "to").text = str(d)
                    ETc.SubElement(tran, "read").text = str(a)
        tree = ETc.ElementTree(root)

        tree.write("{}.jff".format(self.caminho) ,encoding='utf8', method='xml', short_empty_elements = True)
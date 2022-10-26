import os
import xml.etree.ElementTree as ETc
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
            sub =  ETc.SubElement(doc, "state", id=str(e), name=str(e))
            if e == self.afd.inicial:
                ETc.SubElement(sub,"initial")
            if self.afd.estadoFinal(int(e)):
                ETc.SubElement(sub, "final")
                
        for (e, a) in self.afd.transicoes.keys():
                    tran = ETc.SubElement(doc, "transition")
                    d = self.afd.transicoes[(e, a)]
                    ETc.SubElement(tran, "from").text = str(e)
                    ETc.SubElement(tran, "to").text = str(d)
                    ETc.SubElement(tran, "read").text = str(a)
        tree = ETc.ElementTree(root)
        tree.write("{}.jff".format(self.caminho+self.nome) ,encoding="UTF-8", method="xml",xml_declaration=True)
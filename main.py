import glob
import pathlib

import numpy as np

from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, \
    Plot, Figure, Matrix, Alignat, NewPage, Package, Command, TikZOptions, TikZNode
from pylatex.tikz import TikZObject, TikZCoordinate, TikZNodeAnchor
from pylatex.utils import italic, NoEscape
import os

if __name__ == '__main__':
    image_filename = pathlib.Path.cwd() / 'output.png'

    geometry_options = {"paperheight": "25cm", "paperwidth": "25cm"}
    doc = Document("memoir", geometry_options=geometry_options)
    doc.packages.append(Package('titlesec'))


    doc.append(NoEscape(r"\pagecolor{black}"))
    doc.append(NoEscape(r"\color{white}"))

    doc.append(NoEscape(r"\titleformat"))
    doc.append(NoEscape(r"{\section}"))
    doc.append(NoEscape(r"{\clearpage\null\vfil\bfseries\Huge}"))
    doc.append(NoEscape(r"{\filright\thesection}"))
    doc.append(NoEscape(r"{1 em}"))
    doc.append(NoEscape(r"{\filright\Huge}"))
    doc.append(NoEscape(r"[\vfil\newpage]"))

    #with doc.create(TikZ(options=('remember picture', 'overlay'))) as pic:
    #    pic.append(TikZNode(text=NoEscape(r"\includegraphics[width =\paperwidth, height =\paperheight]{" + r"output.png" + r"}") , at=TikZCoordinate.from_str(TikZNodeAnchor("page", "center").), options=['opacity = 1', 'inner sep = 0 pt']))
    #    # \tikz[remember picture, overlay] \node[opacity = 0.3, inner sep = 0 pt] at(current page.center){\includegraphics[width =\paperwidth, height =\paperheight]{example - image}};

    #doc.append(NoEscape(r"\tikz[remember picture, overlay] \node[opacity = 0.3, inner sep = 0 pt] at(current page.center){\includegraphics[width =\paperwidth, height =\paperheight]{output.png}};"))

    # Cover
    with doc.create(Section('The simple stuff')):
        doc.append('Some regular text and some')
        doc.append(NewPage())

    # One page per picture
    for picture in glob.glob('images/*.png'):
        print(picture)
        title = picture.split('\\')[1].strip(".png").replace('_', ' ')
        with doc.create(Section(title)):
            doc.append(NewPage())
            doc.append(NoEscape(r"\thispagestyle{empty}"))
            with doc.create(TikZ(options=('remember picture', 'overlay'))) as pic:
                pic.append(NoEscape(r"\node[opacity = 1, inner sep = 0 pt] at(current page.center){\includegraphics[width =\paperwidth, height =\paperheight]{" + picture.replace('\\', '/') + r"}};"))
            doc.append(NewPage())



    doc.generate_pdf('full', clean_tex=False)

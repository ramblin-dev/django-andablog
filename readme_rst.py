import pandoc
pandoc.core.PANDOC_PATH = 'pandoc'

doc = pandoc.Document()
doc.markdown = open('README.md').read()
rst = open('README.rst', 'w')
rst.write(doc.rst)
rst.close()

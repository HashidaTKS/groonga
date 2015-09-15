# -*- coding: utf-8 -*-
#
# groonga documentation build configuration file, created by
# sphinx-quickstart on Thu Oct 22 15:42:37 2009.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

SPHINX_VERSION_REQUIRED = "1.0.8" # 1.1 is required.
RST2PDF_VERSION_REQUIRED = "0.14.2"

import re
import sphinx
import sys, os
import gettext
from datetime import datetime
from pkg_resources import parse_version

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.append(os.path.abspath('.'))

if parse_version(sphinx.__version__) < parse_version(SPHINX_VERSION_REQUIRED):
  print 'sphinx version is old. %s is requred. exec "easy_install -U sphinx"' % SPHINX_VERSION_REQUIRED
  sys.exit(1)

#if sphinx.__version__ != SPHINX_VERSION_REQUIRED:
#  print 'sphinx version is different. %s is requred. exec "easy_install -U sphinx"' % SPHINX_VERSION_REQUIRED
#  sys.exit(1)

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = []
# extensions.append("source.rdoc")
# extensions.append("source.textile")
try:
  import rst2pdf
  if parse_version(rst2pdf.version) >= parse_version(RST2PDF_VERSION_REQUIRED):
    extensions.append('sphinx.ext.autodoc')
    extensions.append('rst2pdf.pdfbuilder')
except:
  pass

# Add any paths that contain templates here, relative to this directory.
templates_path = ['templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Groonga'
copyright = u'2009-' + unicode(datetime.today().year) + ', Brazil, Inc'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#

# The short X.Y version.
version = os.environ["DOCUMENT_VERSION"]
# The full version, including alpha/beta/rc tags.
release = os.environ["DOCUMENT_VERSION_FULL"]

# The directories that has *.mo files.
locale_dirs = ["../locale"]

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = os.environ['LOCALE']

locale_dir = os.path.dirname(__file__) + "/../locale"
try:
  catalog = gettext.Catalog("conf", localedir=locale_dir, languages=[language])
  _ = catalog.gettext
except:
  _ = lambda msgid: msgid

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = [
  '**/.#*',
  'reference/scoring_note.rst',
]

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
html_theme = 'groonga'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
  'rightsidebar': 'true',
  'stickysidebar': 'true',
#  'relbarbgcolor': '#ED4517',
#  'relbartextcolor': 'white',
#  'relbarlinkcolor': '#F8F0FF',
#  'footerbgcolor': '#ED4517',
#  'footertextcolor': 'white',
#  'sidebarbgcolor': '#FFd587',
#  'sidebartextcolor': '#ED4517',
#  'sidebarlinkcolor': '#666666',
  'bodyfont': '#666666',
}

html_context = {"language": language}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ["../themes"]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title_format = unicode(_("%(project)s v%(release)s documentation"), "utf-8")
html_title = html_title_format % {"project": project,
                                  "release": unicode(release, "utf-8")}

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = False

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_use_modindex = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'groongadoc'


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'groonga.tex', unicode(_('Groonga documentation'), "utf-8"),
   u'Brazil, Inc', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True

# -- Options for rst2pdf output --------------------------------------------------
pdf_documents = [
  ('index',
   u'Groonga-%s' % (release,),
   html_title,
   unicode(_('Groonga Project'), "utf-8"))
]
pdf_stylesheets = ['sphinx', 'kerning', 'a4']
if 'language' in dir():
  pdf_language = language
  pdf_stylesheets += ['styles/pdf/%s' % pdf_language]
pdf_font_path = []
for root, dirs, files in os.walk('/usr/share/fonts'):
  pdf_font_path += map(lambda(dir): os.path.join(root, dir), dirs)
pdf_fit_mode = "shrink"
pdf_inline_footnotes = True
pdf_break_level = 2

# -- Options for manual page output --------------------------------------------
# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'groonga', unicode(_('Groonga documentation'), "utf-8"),
     [u'Groonga Project'], 1)
]

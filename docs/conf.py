#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# ViroCon doc documentation build configuration file, created by
# sphinx-quickstart on Tue Aug 22 11:54:21 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../'))
here = os.path.abspath(os.path.dirname(__file__))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.mathjax',
              'sphinx.ext.viewcode',
              'sphinx.ext.napoleon',
              'sphinx.ext.todo',
              'sphinx.ext.autosummary',
              'sphinx.ext.intersphinx',]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
#source_suffix = ['.rst', '.md', '.py']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'viroconcom'
copyright = '2018, viroconcom'
author = 'Niklas Bergmann, Christian Castens, Andreas Haselsteiner, Martin Lechner, Jannik Lehmkuhl, Tjark Meyer, Felix Möller, Tobias Pape, Erik Rother, Kai-Lukas Windmeier'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
with open(os.path.join(here, '../viroconcom/VERSION')) as version_file:
    _version = version_file.read().strip().split(".")
    version = ".".join(_version[0:2]) # The short X.Y version.
    release = ".".join(_version) # The full version, including alpha/beta/rc tags.

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store',]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'my_classic_theme'
html_theme_path = ["_theme"]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# black = "#000000"
# white = "#FFFFFF"
# grey = "#C0C0C0"
# light_blue = "#0040FF"
# blue = "#045FB4"
# light_grey = "#E6E6E6"
# dark_grey = "#424242"
# collapse_button = "#A4A4A4"
# html_theme_options = {
#     "rightsidebar" : "False", #Put the sidebar on the right side.
#     #"stickysidebar" : "True", #Make the sidebar “fixed” so that it doesn’t scroll out of view for long body content. This may not work well with all browsers.
#     "collapsiblesidebar" : "True", #Add an experimental JavaScript snippet that makes the sidebar collapsible via a button on its side. Doesn’t work with “stickysidebar”.
#     "externalrefs" : "True", #Display external links differently from internal links.
#
#     "footerbgcolor" : white, #Background color for the footer line.
#     "footertextcolor" : dark_grey, #Text color for the footer line.
#
# 	"sidebarbgcolor" : light_grey, #Background color for the sidebar.
#     "sidebarbtncolor" : collapse_button, #Background color for the sidebar collapse button (used when "collapsiblesidebar" is True).
#     "sidebartextcolor" : dark_grey, #Text color for the sidebar.
#     "sidebarlinkcolor" : blue, #Link color for the sidebar.
#
#     "relbarbgcolor" : grey, #Background color for the relation bar.
#     "relbartextcolor" : blue, #Text color for the relation bar.
#     "relbarlinkcolor" : dark_grey, #Link color for the relation bar.
#
#     "bgcolor" : white, #Body background color.
#     "textcolor" : black, #Body text color.
#     "linkcolor" : black, #Body link color.
#     "visitedlinkcolor" : black, #Body color for visited links.
#
#     "headbgcolor" : white, #Background color for headings.
#     "headtextcolor" : black, #Text color for headings.
#     "headlinkcolor" : black,  #Link color for headings.
#
#     "codebgcolor" : light_grey, #Background color for code blocks.
#     "codetextcolor" : black, #Default text color for code blocks, if not set differently by the highlighting style.
#
#     "bodyfont" : "Helvetica, Arial, sans-serif", #Font for normal text.
#     "headfont" : "Helvetica, Arial, sans-serif", #Font for headings.
# }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
# html_sidebars = {
#     '**': [
#         'about.html',
#         'navigation.html',
#         'relations.html',  # needs 'show_related': True theme option to display
#         'searchbox.html',
#         'donate.html',
#     ]
# }


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'vicoconcomdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'viroconcom.tex', 'viroconcom Documentation',
     'viroconcom', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'viroconcom', 'viroconcom Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'viroconcom', 'viroconcom Documentation',
     author, 'viroconcom', 'One line description of project.',
     'Miscellaneous'),
]

# Napoleon settings
#napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
#napoleon_include_private_with_doc = False
#napoleon_include_special_with_doc = True
#napoleon_use_admonition_for_examples = False
#napoleon_use_admonition_for_notes = False
#napoleon_use_admonition_for_references = False
#napoleon_use_ivar = False
#napoleon_use_param = True
#napoleon_use_rtype = True

# todo settings
# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False
# If this is True, todo emits a warning for each TODO entries.
#todo_emit_warnings = False
# If this is True, todolist produce output without file path and line.
# todo_link_only = False

# Intersphinx options
intersphinx_mapping = {'python': ('https://docs.python.org/3.6', None),
                       'numpy': ('http://docs.scipy.org/doc/numpy/', None),
                       'scipy' : ('http://docs.scipy.org/doc/scipy/reference', None),
                       'matplotlib' : ('http://matplotlib.org', None),}

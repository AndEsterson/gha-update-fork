project = "gha-update"

default_role = "code"

extensions = [
    "myst_parser",
    "sphinx.ext.extlinks",
]

autodoc_member_order = "bysource"
autodoc_typehints = "description"
autodoc_preserve_defaults = True

myst_enable_extensions = [
    "colon_fence",
    "fieldlist",
]
myst_heading_anchors = 2

extlinks = {
    "issue": ("https://github.com/davidism/gha-update/issues/%s", "#%s"),
    "pr": ("https://github.com/davidism/gha-update/pull/%s", "#%s"),
}

html_theme = "furo"
html_static_path = ["_static"]
html_css_files = ["theme.css"]
html_copy_source = False
html_theme_options = {
    "source_repository": "https://github.com/davidism/gha-update/",
    "source_branch": "main",
    "source_directory": "docs/",
    "light_css_variables": {
        "font-stack": "'Atkinson Hyperlegible Next', sans-serif",
        "font-stack--monospace": "'Atkinson Hyperlegible Mono', monospace",
    },
}
pygments_style = "default"
pygments_style_dark = "github-dark"
html_show_copyright = False
html_use_index = False
html_domain_indices = False

# -*- coding: utf-8 -*-
#
# Based on the update script in plone.staticresources. This script works
# without any dependencies. You don't have to run a buildout in advance.
# Run python src/collective/icons/fontawesome/_scripts/register.py in
# the package root to generate icons_fontawesome.xml

import os

ICONSETS = [
    'fontawesome.free.brands',
    'fontawesome.free.regular',
    'fontawesome.free.solid',
]

ICONS_DIR = "src/collective/icons/fontawesome/browser/static/{}"
OUTPUT_FILE = "src/collective/icons/fontawesome/profiles/default/registry/icons_fontawesome.xml"

registry_template = """<?xml version="1.0"?>
<registry>
{}
</registry>
"""

entry = """
  <record name="plone.icon.{iconset}.{icon}">
    <field type="plone.registry.field.TextLine">
      <title>Fontawesome Icon {icon}</title>
    </field>
    <value key="resource">++plone++collective.icons.fontawesome/{iconpath}</value>
  </record>
"""


def main():
    output = ""

    for iconset in ICONSETS:

        iconset_path = iconset.replace('.', '/')
        icons = sorted(os.listdir(ICONS_DIR.format(iconset_path)))
        for item in icons:
            if item.endswith(".svg"):
                icon = item[:-4]
                iconpath = iconset_path + '/' + icon + '.svg'
                output = output + entry.format(icon=icon, iconpath=iconpath, iconset=iconset)

    output = registry_template.format(output)

    with open(OUTPUT_FILE, "w") as f:
        f.write(output)

    print("Done.")
    print("If any new icons were added also add an upgrade step!")


if __name__ == "__main__":
    main()

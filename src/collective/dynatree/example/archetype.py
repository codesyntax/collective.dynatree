from Products.Archetypes.atapi import *
from Products.Archetypes.config import PKG_NAME
from AccessControl import ClassSecurityInfo
from collective.dynatree.atwidget import DynatreeWidget

schema = BaseSchema + Schema((
    StringField('single_leafs',
        required=1,
        widget=DynatreeWidget(
            description="Select one option of tree. Only leafs allowed",
            multiple=False,
            select='leafs'),
    ),
    StringField('single_all',
        required=1,
        widget=DynatreeWidget(
            description="""Select one option of tree. Nodes allowed too.
                           Autocollapse is switched on.""",
            multiple=False,
            select='all',
            autocollapse=True),
    ),
    LinesField('multiple_leafs',
        required=1,
        widget=DynatreeWidget(
            description="""Select multiple options of tree. Leafs only.""",
            multiple=True,
            select="leafs"),
    ),
    LinesField('multiple_all',
        required=1,
        widget=DynatreeWidget(
            description="""Select one option of the tree. All selectable.
                           Starts with 2 levels expanded.""",
            multiple=True,
            select="all",
            minExpandLevel=2),
    ),
))


class DynatreeExample(BaseContent):
    """A simple archetype"""
    schema = schema

registerType(DynatreeExample, 'collective.dynatree.example')
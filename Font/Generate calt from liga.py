# logic borrows from https://github.com/tonsky/FiraCode/blob/master/gen_calt.clj

import re

#
#
#

liga_feature = None

try:
    liga_feature = next(feat for feat in Font.features if feat.name == 'liga')
except StopIteration:
    print 'no liga feature available'

try:
    calt_feature = next(feat for feat in Font.features if feat.name == 'calt')
except StopIteration:
    print 'no calt feature available'

#
#
#

statements = liga_feature.code.splitlines()

for statement in statements:
    ligature_name = re.findall("([a-z_]+)\.liga;", statement)[0]
    ligature_items = ligature_name.split('_')

    #
    #
    #

    text = None

    if (len(ligature_items) == 2):
        text = """
            lookup 1_2 {
                ignore sub 1 1' 2;
                ignore sub 1' 2 2;

                sub LIG 2' by 1_2.liga;
                sub 1'  2  by LIG;
            } 1_2;
        """

    elif (len(ligature_items) == 3):
        text = """
            lookup 1_2_3 {
                ignore sub 1 1' 2 3;
                ignore sub 1' 2 3 3;

                sub LIG LIG 3' by 1_2_3.liga;
                sub LIG  2' 3  by LIG;
                sub 1'   2  3  by LIG;
            } 1_2_3;
        """,

    elif (len(ligature_items) == 4):
        text = """
            lookup 1_2_3 {
                ignore sub 1 1' 2 3 4;
                ignore sub 1' 2 3 4 4;

                sub LIG LIG LIG 4' by 1_2_3_4.liga;
                sub LIG LIG  3' 4  by LIG;
                sub LIG  2'  3  4  by LIG;
                sub 1'   2   3  4  by LIG;
            } 1_2_3_4;
        """

    # Generate lookup containing each glyph in the current ligature
    lookup = { str(i+1): ligature_items[i] for i in range(0, len(ligature_items), 1) }

    # Create a regular expression from the dictionary keys
    regex = re.compile("(%s)" % "|".join(map(re.escape, lookup.keys())))

    # For each match, look-up corresponding value in dictionary
    result = regex.sub(lambda mo:
        lookup[mo.string[mo.start():mo.end()]],
        str(text)
    )

    print result

try:
    re.findall("# START GENERATED_FROM_LIGA #", calt_feature.code)[0]
    re.findall("# END GENERATED_FROM_LIGA #", calt_feature.code)[0]
except StopIteration:
    print 'no calt feature available'
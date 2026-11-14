---
title: "ncl_conpack_params(3)"
name: "ncl_conpack_params"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_conpack_params/"
---

Conpack_params - This document briefly describes all Conpack internal parameters. 

<h2>Description</h2>Parameter descriptions follow, in alphabetical order. Each description begins with a line giving the three-character mnemonic name of the parameter, the phrase for which the mnemonic stands, the intrinsic type of the parameter, and an indication of whether or not it is an array.
<dl COMPACT><dt>'AIA' - Area Identifier Above - Integer Array
<dd>Each element of the parameter array 'AIA' is an area identifier for the area above the contour level specified by the corresponding element of the parameter array 'CLV'. The corresponding element of the parameter array 'AIB' is an area identifier for the area below that level. If, for a particular contour level, both 'AIA' and 'AIB' are zero, that level is ignored by the routine CPCLAM; otherwise, contour lines at that level are added to the area map and the given values of 'AIA' and 'AIB' are used as right and left area identifiers, respectively. (Note that contour lines are traced with greater values to the right and lesser values to the left.) 

 There are three special elements in the parameter array 'AIA', corresponding to 'PAI' values of -1, -2, and -3; the first specifies an area identifier for the area outside the edge of the grid, the second an area identifier for any area filled with special values, and the third an area identifier for any area in which the mapping routine CPMPXY returns the &quot;out of range&quot; value 'ORV'. 

 If contour levels are chosen automatically, rather than being supplied by the user, the value supplied for the Ith element of 'AIA' is I+1 and the value supplied for the Ith element of 'AIB' is I. 

 The default value of element &quot;-1&quot; of 'AIA' is 0 and the default values of elements &quot;-2&quot; and &quot;-3&quot; are -1's.
<dt>'AIB' - Area Identifier Below - Integer Array
<dd>See the description of 'AIA', above.
<dt>'CAF' - Cell Array Flag - Integer
<dd>The parameter 'CAF' determines the way in which the routine CPCICA (which is called to store color indices in a user cell array), gets from an area identifier associated with a particular cell to a color index for that cell. Let IAID be the area identifier that is associated with a given cell. Then:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>If 'CAF' is negative, the routine CPSCAE is called. The default version of CPSCAE behaves as follows: if the value of IAID is greater than or equal to zero, it itself is stored in the cell array as a color index; otherwise, the cell array is unchanged. A user version of CPSCAE may be supplied to do something more complicated; since the value of 'CAF' is one of the arguments of CPSCAE, its value may be used to select one of a number of color-setting schemes built into the routine.
<dt>&bull;
<dd>If 'CAF' is positive, the value &quot;'CAF'+IAID&quot; is computed. If that value is positive, it is stored in the cell array as a color index; otherwise, the cell array is unchanged. In this case, 'CAF' acts as an offset, mapping the area identifiers to a unique portion of the color table.</dl></dl><dd>The default value of 'CAF' is 0.
<dt>'CFA' - Constant-Field Label Angle - Real
<dd>The parameter 'CFA' specifies the angle (in degrees counterclockwise from a vector pointing to the right) at which a constant-field label is to be written. 

 The default value of 'CFA' is 0.
<dt>'CFB' - Constant-Field Label Box Flag - Integer
<dd>If 'CFB' is zero, the constant-field label will not be boxed at all. The value 1 implies that the perimeter of the box is to be drawn (in the same color as the label) after the label is drawn. The value 2 implies that the box is to be filled (in the color specified by 'LBC') before the label is drawn. The value 3 implies both of the above. 

 The default value of 'CFB' is 0.
<dt>'CFC' - Constant-Field Label Color Index - Integer
<dd>If 'CFC' is less than zero, the constant-field label and the box, if any, around it, will be drawn in the color specified by the current text color index; if 'CFC' is greater than or equal to zero, then it specifies the desired color index for the label and the box. If a box is drawn around the label, it is made the same color as the label itself. 

 The default value of 'CFC' is -1.
<dt>'CFF' - Constant-Field-Found Flag - Integer
<dd>The parameter 'CFF' may not be set by the user; its retrieved value will be non-zero if and only if CPRECT, CPSPS1, or CPSPS2 detected a constant field. 

 The default value of 'CFF' (prior to any call to CPRECT, CPSPS1, or CPSPS2) is zero.
<dt>'CFL' - Constant-Field Label Line Width - Real
<dd>If 'CFL' is less than or equal to zero, line width will not be set before drawing a box around the constant-field label. If 'CFL' is greater than zero, it specifies the desired width, as a multiple of the &quot;normal&quot; line width. 

 The default value of 'CFL' is 0.
<dt>'CFP' - Constant-Field Label Positioning Flag - Integer
<dd>The parameter 'CFP' says how the constant-field label is to be positioned. There are nine possible values, each of which specifies a point of the label box which is to lie on the point defined by 'CFX' and 'CFY': the value -4 implies the lower left-hand corner of the label box, -3 implies the center of the bottom of the box, -2 the lower right-hand corner of the box, -1 the center of the left edge of the box, 0 the center of the box, +1 the center of the right edge of the box, +2 the upper left-hand corner of the box, +3 the center of the top edge of the box, and +4 the upper right-hand corner of the box. Left, right, bottom, and top are defined from the viewpoint of someone viewing the label right-side up. 

 The default value of 'CFP' is 0, so the constant-field label will be centered on the point whose coordinates are 'CFX' and 'CFY'.
<dt>'CFS' - Constant-Field Label Size - Real
<dd>The parameter 'CFS' specifies the nominal size (width) of a character in the constant-field label, as a fraction of the width of the viewport. This nominal size is multiplied by 'CWM'. 

 The default value of 'CFS' is 0.012.
<dt>'CFT' - Constant-Field Label Text String - Character
<dd>The parameter 'CFT' specifies the text of the constant-field label, which is written when a constant data field is detected; it is a character string of at most 40 characters. The embedded string '$ZDV$' will be replaced by the numeric value of the field. 

 If 'CFT' is given the value ' ' (a single blank), the constant-field label will not be written. 

 The default value of 'CFT' is 'CONSTANT FIELD - VALUE IS $ZDV$'.
<dt>'CFW' - Constant-Field Label White Space Width - Real
<dd>The parameter 'CFW' specifies the nominal width of white space to be left around the constant-field label, as a fraction of the width of the viewport. This nominal width is multiplied by 'CWM'. 

 The default value of 'CFW' is 0.005.
<dt>'CFX' - Constant-Field Label X Coordinate - Real
<dd>The parameter 'CFX' specifies the X coordinate of the basepoint of the constant-field label. The given value is mapped linearly onto the viewport; 0 refers to the left edge of the viewport and 1 to the right edge of the viewport. Values less than 0 or greater than 1 may be used. 

 The default value of 'CFX' is 0.5, so the constant-field label is centered horizontally in the viewport.
<dt>'CFY' - Constant-Field Label Y Coordinate - Real
<dd>The parameter 'CFY' specifies the Y coordinate of the basepoint of the constant-field label. The given value is mapped linearly onto the viewport; 0 refers to the bottom edge of the viewport and 1 to the top edge of the viewport. Values less than 0 or greater than 1 may be used. 

 The default value of 'CFY' is 0.5, so the constant-field label is centered vertically in the viewport.
<dt>'CIS' - Contour Interval Specifier - Real
<dd>See the description of 'CLS', below. When 'CLS' is greater than zero, 'CIS' is used. A value of 'CIS' less than or equal to zero indicates that Conpack is to choose the contour interval (see the descriptions of the parameter arrays 'CIT' and 'LIT'). A value of 'CIS' which is greater than zero is the actual contour interval to be used; in this case, 'LIS' may be given a non-zero value &quot;n&quot; to specify that every &quot;nth&quot; contour level should be labeled. See also the descriptions of 'CMN' and 'CMX', below. 

 The default value of 'CIS' is 0.
<dt>'CIT' - Contour Interval Table - Real Array
<dd>Each non-zero element of the ten-element parameter array 'CIT' is a real number greater than or equal to 1 and less than 10; when Conpack picks the contour interval, it chooses a number of the form &quot;c x 10**k&quot;, where &quot;c&quot; is one of the elements of 'CIT' and &quot;k&quot; is an integer. The non-zero elements of 'CIT' must be sorted in ascending order and appear at the beginning of the array. 

 The corresponding elements of the parameter array 'LIT' specify which contours are to be labeled. A contour at &quot;nc x 10**k&quot; is labeled if &quot;n&quot; is a multiple of &quot;l&quot;, where &quot;l&quot; is the element of 'LIT' corresponding to the element &quot;c&quot; of 'CIT'. For example, if the first element of 'CIT' is &quot;1.&quot; and the first element of 'LIT' is &quot;5&quot;, then Conpack is allowed to use contour levels 1., 2., 3., 4., etc., with labels at 5., 10., 15., etc. (5 x 1., 5 x 2., 5 x 3., etc.). 

 The default contents of 'CIT' and 'LIT' are as follows: 

 <table> <tr VALIGN=top><td ALIGN=center>'PAI'</td><td ALIGN=center>'CIT'</td><td ALIGN=center>'LIT'</td><td ALIGN=center>LEVELS ALLOWED</td><td ALIGN=center>LABEL INTERVAL
</td></tr><tr VALIGN=top><td ALIGN=center>-----</td><td ALIGN=center>-----</td><td ALIGN=center>-----</td><td ALIGN=center>--------------</td><td ALIGN=center>--------------
</td></tr><tr VALIGN=top><td ALIGN=center>1</td><td ALIGN=center>1.0</td><td ALIGN=center>5</td><td ALIGN=center>1.0 x 10 ** K</td><td ALIGN=center>EVERY 5TH ONE
</td></tr><tr VALIGN=top><td ALIGN=center>2</td><td ALIGN=center>2.0</td><td ALIGN=center>5</td><td ALIGN=center>2.0 x 10 ** K</td><td ALIGN=center>EVERY 5TH ONE
</td></tr><tr VALIGN=top><td ALIGN=center>3</td><td ALIGN=center>2.5</td><td ALIGN=center>4</td><td ALIGN=center>2.5 x 10 ** K</td><td ALIGN=center>EVERY 4TH ONE
</td></tr><tr VALIGN=top><td ALIGN=center>4</td><td ALIGN=center>4.0</td><td ALIGN=center>5</td><td ALIGN=center>4.0 x 10 ** K</td><td ALIGN=center>EVERY 5TH ONE
</td></tr><tr VALIGN=top><td ALIGN=center>5</td><td ALIGN=center>5.0</td><td ALIGN=center>5</td><td ALIGN=center>5.0 x 10 ** K</td><td ALIGN=center>EVERY 5TH ONE
</td></tr><tr VALIGN=top><td ALIGN=center>6</td><td ALIGN=center>0.0</td><td ALIGN=center>0</td><td ALIGN=center>FILLER TO END</td><td ALIGN=center>FILLER TO END
</td></tr><tr VALIGN=top><td ALIGN=center>7</td><td ALIGN=center>0.0</td><td ALIGN=center>0</td><td ALIGN=center>FILLER TO END</td><td ALIGN=center>FILLER TO END
</td></tr><tr VALIGN=top><td ALIGN=center>8</td><td ALIGN=center>0.0</td><td ALIGN=center>0</td><td ALIGN=center>FILLER TO END</td><td ALIGN=center>FILLER TO END
</td></tr><tr VALIGN=top><td ALIGN=center>9</td><td ALIGN=center>0.0</td><td ALIGN=center>0</td><td ALIGN=center>FILLER TO END</td><td ALIGN=center>FILLER TO END
</td></tr><tr VALIGN=top><td ALIGN=center>10</td><td ALIGN=center>0.0</td><td ALIGN=center>0</td><td ALIGN=center>FILLER TO END</td><td ALIGN=center>FILLER TO END
</td></tr> </table><dt>'CIU' - Contour Interval Used - Real
<dd>The parameter 'CIU' is normally intended for retrieval only. When the selection of the contour interval is left up to Conpack, 'CIU' is given the value chosen. When contour levels are completely set by the user, the value of 'CIU' may need to be set as well, for two reasons: 1) to make the desired value appear in an informational label (in place of the embedded string '$CIU$') and 2) so that it may be used by the penalty scheme for positioning labels. The setting of 'CIU' must be done after setting the contour levels (because, as a side effect of the setting of element 1 of 'CLV', 'CIU' is zeroed). If the user supplies contour levels, but supplies no value of 'CIU', and the penalty scheme is used to position labels, the required contour interval is estimated; in certain situations, this can lead to problems (if, for example, the same contour level appears twice in 'CLV', once to force lines at that level to be drawn and once to force that level to be used as the boundary for a shaded area). 

 The default value of 'CIU' is 0.
<dt>'CLC' - Contour Line Color Index - Integer Array
<dd>Each element of the parameter array 'CLC', if greater than or equal to zero, is a color index for contour lines at the level specified by the associated element of 'CLV'. A value less than zero implies that the lines will be drawn in the color specified by the current polyline color index. 

 There are three special elements in the parameter array 'CLC', corresponding to 'PAI' values of -1, -2, and -3; the first specifies a color index for the edge of the grid, the second a color index for the edge of any area filled with special values, and the third a color index for the edge of any area in which the mapping routine CPMPXY returns the &quot;out of range&quot; value. 

 The default value of each element of 'CLC' is -1.
<dt>'CLD' - Contour Line Dash Pattern - Character Array
<dd>Each element of the parameter array 'CLD' is a dash pattern (as expected by the package Dashline) to be used (when 'DPU' is non-zero) to draw contour lines at the level specified by the associated element of the contour level array 'CLV'. Elements of 'CLD' may be set using a call to CPSETI, with a sixteen-bit integer as the second argument, or using a call to CPSETC, with a character string of 32 or fewer characters as the second argument. In either case, the result will be a character string internally; a sixteen-bit integer will be converted to a sixteen-character string by mapping 0-bits into apostrophes and 1-bits into dollar signs. 

 There are three special elements in the parameter array 'CLD', corresponding to 'PAI' values of -1, -2, and -3; the first specifies a dash pattern for the edge of the grid, the second a dash pattern for the edge of any area filled with special values, and the third a dash pattern for the edge of any area in which the mapping routine CPMPXY returns the &quot;out of range&quot; value. 

 When Conpack picks the contour levels, the default value supplied for each associated dash pattern is the character constant '$$$$$$$$$$$$$$$$'. This is also the default value for each of the three special elements.
<dt>'CLL' - Contour Line Line Width - Real Array
<dd>Each element of the parameter array 'CLL' specifies the line width used to draw contour lines at the level specified by the associated element of the contour level array 'CLV'. Each is expressed as a multiple of the &quot;normal&quot; line width; values less than or equal to zero imply that line width should not be set. 

 There are three special elements in the parameter array 'CLL', corresponding to 'PAI' values of -1, -2, and -3; the first specifies a line width for the edge of the grid, the second a line width for the edge of any area filled with special values, and the third a line width for the edge of any area in which the mapping routine CPMPXY returns the &quot;out of range&quot; value. 

 When Conpack picks the contour levels, the default value supplied for each associated line width is 0. This is also the default value for each of the three special elements.
<dt>'CLS' - Contour Level Selection Flag - Integer
<dd>This parameter must be set prior to the call to CPRECT, CPSPS1, or CPSPS2 which initiates the process of drawing a particular contour plot; it specifies how contour levels are to be selected, as follows:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>If 'CLS' has the value &quot;0&quot;, Conpack will not pick contour levels at all; the current values of the parameters 'NCL', 'CLV', and associated arrays will not be changed. They will thus retain the values chosen by Conpack during a previous call or the values supplied by the user.
<dt>&bull;
<dd>If 'CLS' has a negative value of the form &quot;-n&quot;, Conpack will generate &quot;n&quot; contour levels, splitting the range from the minimum field value to the maximum field value into &quot;n+1&quot; equal intervals.
<dt>&bull;
<dd>If 'CLS' has a positive value of the form &quot;+n&quot; and 'CIS' is less than or equal to zero, Conpack will use values of the form &quot;bk&quot;, where &quot;b&quot; is a &quot;base&quot; value chosen by Conpack and &quot;k&quot; is an integer. The base value &quot;b&quot; will be a &quot;nice&quot; value (as defined by the contents of the parameter array 'CIT'), chosen in such a way as to give at least &quot;n&quot; contour levels (with the default contents of the array 'CIT', you may get as many as &quot;2n&quot; levels).
<dt>&bull;
<dd>If 'CLS' has a positive value of the form &quot;+n&quot; and 'CIS' is greater than zero and 'CMN' is greater than 'CMX', Conpack will use values of the form &quot;'CIS'*k&quot;, where &quot;k&quot; is an integer.
<dt>&bull;
<dd>If 'CLS' has a positive value of the form &quot;+n&quot; and 'CIS' is greater than zero and 'CMN' is less than or equal to 'CMX', Conpack will use values of the form &quot;'CMN'+'CIS'*k&quot; which are greater than or equal to 'CMN' and less than or equal to 'CMX', where &quot;k&quot; is an integer.</dl></dl><dd>The default value of 'CLS' is 16.
<dt>'CLU' - Contour Level Use Flags - Integer Array
<dd>Each element of the parameter array 'CLU' indicates how the associated contour level, in the parameter array 'CLV', is to be used. The value 0 means that no contour line is to be drawn at the associated level, the value 1 that the line is to be drawn without labels, the value 2 that the labels are to be drawn, but not the line, and the value 3 that both the line and the labels are to be drawn. 

 There are three special elements in the parameter array 'CLU', corresponding to 'PAI' values of -1, -2, and -3; the first specifies a flag for the edge of the grid, the second a flag for the edge of any area filled with special values, and the third a flag for the edge of any area in which the mapping routine CPMPXY returns the &quot;out of range&quot; value. In each case, if the flag is zero, the associated edge is not drawn; otherwise, the associated edge is drawn. 

 When Conpack chooses the contour levels, the associated elements of 'CLU' are given one of the two values 1 or 3, depending on whether the line is to be labeled or not. The default values of the special elements are all zeroes.
<dt>'CLV' - Contour Level Values - Real Array
<dd>Each of the first 'NCL' elements of the parameter array 'CLV' is a contour level for which something is to be done (the drawing of contour lines, the drawing of contour labels, and/or the addition of contour lines to an area map). 

 Only elements 1 through 'NCL' may be accessed via the parameter-setting routines. Thus, code to set the contour levels and associated quantities must begin with a call to set 'NCL'. 

 A side effect of setting the element numbered 'PAI' of 'CLV' is that the associated element number 'PAI' in each of the parameter arrays 'AIA', 'AIB', 'CLC', 'CLD', 'CLL', 'CLU', 'LLC', and 'LLT' is also given a default value, as follows:
<dl COMPACT><dd><dl COMPACT><dt>'AIA'
<dd>'PAI'+1
<dt>'AIB'
<dd>'PAI'
<dt>'CLC'
<dd>-1
<dt>'CLD'
<dd>'$$$$$$$$$$$$$$$$'
<dt>'CLL'
<dd>0
<dt>'CLU'
<dd>1
<dt>'LLC'
<dd>-1
<dt>'LLT'
<dd>' ' (a single blank)</dl></dl><dd>Thus, in code to set contour levels and associated quantities, each contour level must be set before the quantities associated with it. 

 A side effect of setting element number 1 of 'CLV' is that the parameter 'CIU', which indicates what contour interval was used, is zeroed. It is assumed that this will only happen when the user is providing all the contour levels, in which case the concept of the &quot;contour interval&quot; may or not be well defined. See the description of 'CIU' for more information.
<dt>'CMN' - Contour Minimum - Real
<dd>When 'CLS' is greater than zero and 'CIS' is also greater than zero, if 'CMN' is less than or equal to 'CMX', then the contour levels used will be of the form 'CMN', 'CMN'+'CIS', 'CMN'+2*'CIS', ... , 'CMN'+n*'CIS', where &quot;n&quot; is the largest integer such that 'CMN'+n*'CIS' is less than or equal to 'CMX'. The labeled levels will be those for which &quot;n&quot; is a multiple of 'LIS'. 

 The default values of 'CMN' and 'CMX' are 1 and 0, respectively.
<dt>'CMX' - Contour Maximum - Real
<dd>See the description of 'CMN', above.
<dt>'CTM' - Character Temporary - Character
<dd>The parameter name 'CTM' refers to a temporary character buffer in Conpack; the name may be used in the routine CPCHCL to get the dash pattern for the current line and in the routines CPCHHL, CPCHIL, and CPCHLL to get the text of the label being written or to change it. 

 The parameter 'CTM' has no meaningful default value.
<dt>'CWM' - Character Width Multiplier - Real
<dd>All character size parameters are multiplied by 'CWM'; this makes it easy to scale the sizes up or down simultaneously. Parameters affected by this are 'CFS', 'CFW', 'DPS', 'DPV', 'HLS', 'HLW', 'ILS', 'ILW', 'LLS', and 'LLW'. 

 The default value of 'CWM' is 1.
<dt>'DPS' - Dash Pattern Size - Real
<dd>The parameter 'DPS' specifies the nominal size (width) of a character in a dash pattern, as a fraction of the width of the viewport. This nominal size is multiplied by 'CWM'. 

 The default value of 'DPS' is 0.010.
<dt>'DPU' - Dash Pattern Use Flag - Integer
<dd>If 'DPU' is less than or equal to zero, it means that no dash patterns are to be used and that contour lines are to be drawn using calls to CURVE. If 'DPU' is non-zero, it means that dash patterns are to be used and that contour lines are to be drawn using calls to CURVED. When the label positioning flag ABS('LLP') = 1, contour lines are caused to be labeled by using a dash pattern formed by concatenating &quot;n&quot; repetitions of the appropriate element of 'CLD' (the nominal dash pattern for the line) and the appropriate element of 'LLT' (the numeric label for the line); in this case, 'DPU' specifies the value of &quot;n&quot;. 

 The default value of 'DPU' is 3.
<dt>'DPV' - Dash Pattern Vector Length - Real
<dd>The parameter 'DPV' specifies the nominal length of the solid vector generated by a dollar sign, or the gap vector generated by an apostrophe, in a dash pattern, as a fraction of the width of the viewport. This nominal length is multiplied by 'CWM'. 

 The default value of 'DPV' is .005.
<dt>'GIC' - Group Identifier for Contour Lines - Integer
<dd>The parameter 'GIC' specifies the group identifier for contour lines added to an area map by the routine CPCLAM. 

 The default value of 'GIC' is 3.
<dt>'GIL' - Group Identifier for Label Boxes - Integer
<dd>The parameter 'GIL' specifies the group identifier for label boxes added to an area map by the routine CPLBAM. 

 The default value of 'GIL' is 3.
<dt>'GIS' - Group Identifier for Strips - Integer
<dd>The parameter 'GIS' specifies the group identifier for a group of edges added to an area map by the routine CPCLAM to create a set of vertical strips. This is done only if the parameter 'NVS' (which is described later in this section) is non-zero. 

 The default value of 'GIS' is 4.
<dt>'HCL' - Hachure Length - Real
<dd>The parameter 'HCL' specifies the hachure length, stated as a fraction of the width of the viewport. A positive value implies the use of hachures on the downslope side of the contour. A negative value implies the use of hachures on the upslope side of the contour. 

 The default value of 'HCL' is .004.
<dt>'HCS' - Hachure Spacing - Real
<dd>The parameter 'HCS' specifies the hachure spacing, stated as a fraction of the width of the viewport. This is the distance between one hachure and the next along a contour line. 

 The default value of 'HCS' is .01.
<dt>'HCF' - Hachuring Flag - Integer
<dd>The parameter 'HCF' is the hachuring flag, with one of the following values:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>If 'HCF' = 0, hachuring is turned off (the default).
<dt>&bull;
<dd>If 'HCF' = 1, all contours will be hachured.
<dt>&bull;
<dd>If 'HCF' = 2, closed contours will be hachured only if the interior of the contour is &quot;downhill&quot;. Open contours will be unconditionally hachured.
<dt>&bull;
<dd>If 'HCF' = 3, closed contours will be hachured only if the interior of the contour is &quot;downhill&quot;. Open contours will be unconditionally unhachured.
<dt>&bull;
<dd>If 'HCF' = 4, closed contours will be hachured only if the interior of the contour is &quot;downhill&quot;. Open contours will be hachured only if the &quot;interior&quot; of the contour is &quot;downhill&quot;, where &quot;interior&quot; is defined by computing the total change in direction along the contour. If that total is positive, the &quot;interior&quot; is to the left; if it is negative, the &quot;interior&quot; is to the right.</dl></dl><dd>Negative values of 'HCF' may also be used. Each has the same effect as the corresponding positive value, except that the word &quot;downhill&quot; in the definition above is replaced by the word &quot;uphill&quot;. 

 The default value of 'HCF' is 0. 

 The user will be expected to increase the value of the internal parameter 'RWC' (&quot;Real Workspace for Contours&quot;) from its default 100 to a value large enough to accommodate any contour that can arise from his/her data field; this may require increasing the size of the real workspace array. (This is so that the hachuring routine is assured of seeing all of each contour line. Otherwise, it can't tell which way the &quot;inside&quot; and the &quot;outside&quot; of the closed contours are.) 

 Closed contours that are broken into pieces that appear to be open contours (either because portions of the closed contour disappear as a result of the mapping implied by non-zero values of the parameter 'MAP' and the out-of-range value 'ORV', or because they run through special-value areas, as defined by the internal parameter 'SPV', or because the user has forgotten to increase the value of 'RWC', as described in the previous paragraph), will be hachured. The rationale for this is that no real confusion can arise from hachuring a contour line which shouldn't be, only from not hachuring one that should be.
<dt>'HIC' - High Label Color Index - Integer
<dd>The parameter 'HIC' is used in determining the color index for high labels. See the description of 'HLC', below.
<dt>'HIT' - High Label Text String - Character
<dd>The parameter 'HIT' specifies the text string to be used in labeling a high. See the description of 'HLT', below.
<dt>'HLA' - High/Low Label Angle - Real
<dd>The parameter 'HLA' specifies the angle (in degrees counterclockwise from a vector pointing to the right) at which high and low labels are to be written. 

 The default value of 'HLA' is 0.
<dt>'HLB' - High/Low Label Box Flag - Integer
<dd>If 'HLB' is zero, high and low labels will not be boxed at all. The value 1 implies that the perimeter of the box is to be drawn (in the same color as the label) after the label is drawn. The value 2 implies that the box is to be filled (in the color specified by 'LBC') before the label is drawn. The value 3 implies both of the above. 

 The default value of 'HLB' is 0.
<dt>'HLC' - High/Low Label Color Index - Integer
<dd>The parameter 'HLC' is used in determining the color index for high and low labels. 

 The color index for high labels is determined in this manner: If 'HIC' is greater than or equal to zero, 'HIC' is used as the color index. If 'HIC' is less than zero, but 'HLC' is greater than or equal to zero, 'HLC' is used as the color index. If both 'HIC' and 'HLC' are less than zero, the current text color index is used. If a box is drawn around the label, it is made the same color as the label itself. 

 The color index for low labels is determined similarly: If 'LOC' is greater than or equal to zero, 'LOC' is used as the color index. If 'LOC' is less than zero, but 'HLC' is greater than or equal to zero, 'HLC' is used as the color index. If both 'LOC' and 'HLC' are less than zero, the current text color index is used. If a box is drawn around the label, it is made the same color as the label itself. 

 To set the color index of all high and low labels, simply supply the desired value for 'HLC'. To have highs and low labels which are colored differently, set 'HIC' and 'LOC'. 

 The default values of 'HLC', 'HIC', and 'LOC' are all -1's.
<dt>'HLE' - High/Low Equal-Value Search - Integer
<dd>If 'HLE' has the value zero, only the &quot;normal&quot; search for highs and lows, as described in the programmer document for CONPACK (in the section &quot;Searching for Highs and Lows&quot;) is performed. 

 If 'HLE' has the value one, and if the &quot;normal&quot; search for highs and lows sees evidence that an additional search should be performed, then the additional search is performed. See the section &quot;Extended High/Low Search Algorithm&quot;, in the programmer document for CONPACK. 

 If 'HLE' has the value two or greater, and if the &quot;normal&quot; search for highs and lows sees evidence that an additional search should be performed, then the additional search is performed, but the candidate regions considered are limited to those containing no more than 'HLE' grid points. 

 Whenever 'HLE' is given a non-zero value, care should be taken to provide enough space in the integer work array to hold an additional M*N elements, where M and N are the dimensions of the array being contoured. This space will be needed during a call to CPHLLB. 

 The default value of 'HLE' is zero.
<dt>'HLL' - High/Low Line Width - Real
<dd>If 'HLL' has a value less than or equal to zero, line width will not be set before drawing boxes around high and low labels. If 'HLL' has a value greater than zero, it specifies the desired width, as a multiple of the &quot;normal&quot; line width. 

 The default value of 'HLL' is 0.
<dt>'HLO' - High/Low Label Overlap Flag - Integer
<dd>The value of 'HLO' says what is to be done about the problem of high and low labels overlapping other objects. The value 0 implies that the problem will be ignored; high and low labels will not be checked for overlap with anything else. Adding 1 to the value of 'HLO' implies the omission of high and low labels which overlap the informational label. Adding 2 implies the omission of high and low labels which overlap other high and low labels found before it. Adding 4 implies the omission of high and low labels which overlap the edges of the viewport, while adding 8 implies that high and low labels which overlap the edges of the viewport should be moved inward by just enough to take care of the problem. If you add both 4 and 8, the effect will be as if you had added 4 alone. 

 The default value of 'HLO' is 3 (1 + 2).
<dt>'HLS' - High/Low Label Size - Real
<dd>The parameter 'HLS' specifies the nominal size (width) of a character in a high or low label, as a fraction of the width of the viewport. This nominal size is multiplied by 'CWM'. 

 The default value of 'HLS' is .012.
<dt>'HLT' - High/Low Label Text Strings - Character
<dd>The character strings used to label highs and lows may be specified individually, by setting 'HIT' and 'LOT', or together, by setting 'HLT'. If 'HLT' is set, and there are no apostrophes in the given character string, both 'HIT' and 'LOT' will be set equal to it and it will therefore be used as the label for both highs and lows. If there are apostrophes in the string, what precedes the first one will be used as the value of 'HIT' (the label for a high) and what follows it will be used as the value of 'LOT' (the label for a low). 

 Remember that, in FORTRAN, an apostrophe in a string which is delimited by apostrophes is represented by two apostrophes. 

 The substring $ZDV$ may be used to represent the numeric value of the high or the low, divided by the current scale factor; the substring $ZDVU$ may be used to represent the unscaled value. 

 Some examples: 

 <table> <tr VALIGN=top><td ALIGN=center>FORTRAN STRING</td><td ALIGN=center>HIGH LABEL</td><td ALIGN=center>LOW LABEL
</td></tr><tr VALIGN=top><td>------------------------</td><td>-------------</td><td>-------------
</td></tr><tr VALIGN=top><td>'H''L'</td><td>H</td><td>L
</td></tr><tr VALIGN=top><td>'HI''LO'</td><td>HI</td><td>LO
</td></tr><tr VALIGN=top><td>'$ZDV$'</td><td>1.362</td><td>0.764
</td></tr><tr VALIGN=top><td>'H($ZDV$)''L($ZDV$)'</td><td>H(1.362)</td><td>L(0.764)
</td></tr><tr VALIGN=top><td>'H:B:$ZDV$:E:''L:B:$ZDV$:E:'</td><td>H</td><td>L
</td></tr><tr VALIGN=top><td>
&nbsp;<wbr></td><td> 1.362</td><td> 0.764
</td></tr> </table><dd>Note that, in the final example, the subscripting capability of the utility Plotchar is used. The terminating function code &quot;E&quot; ensures that the &quot;H&quot; or the &quot;L&quot; will be centered on the high or low; to center the whole thing, either remove the 'E's or change them to 'N's. 

 Neither of the character strings 'HIT' and 'LOT' may contain more than 20 characters. 

 If 'HIT' is blank, highs will not be labeled. If 'LOT' is blank, lows will not be labeled. 

 The default value for 'HIT' is 'H:B:$ZDV$:E:' and the default value of 'LOT' is 'H:B:$ZDV$:E:', as shown in the final example above.
<dt>'HLW' - High/Low Label White Space Width - Real
<dd>The parameter 'HLW' specifies the nominal width of white space to be left around a high or low label, as a fraction of the width of the viewport. This nominal width is multiplied by 'CWM'. 

 The default value of 'HLW' is 0.005.
<dt>'HLX' - High/Low Search Radius in X - Integer
<dd>If 'HLX' is greater than zero, it specifies the half-width of the index-value neighborhood used in searching the contour field for highs and lows. If 'HLX' is less than or equal to zero, Conpack picks a reasonable value to use (approximately 1/8 of 'ZDM', but not less than 2 nor greater than 15). 

 As an example, if 'HLX' = 3 and 'HLY' = 4, then the values in ZDAT examined to determine if (I,J) is a high or a low are those having indices (K,L), where either K is not equal to I or L is not equal to J, K is between MAX(1,I-3) and MIN('ZDM',I+3), inclusive, and L is between MAX(1,J-4) and MIN('ZDN',J+4), inclusive. 

 The default value of 'HLX' is 0.
<dt>'HLY' - High/Low Search Radius in Y - Integer
<dd>If 'HLY' is greater than zero, it specifies the half-height of the index-value neighborhood used in searching the contour field for highs and lows. If 'HLY' is less than or equal to zero, Conpack picks a reasonable value to use (approximately 1/8 of 'ZDN', but not less than 2 nor greater than 15). 

 For an example, see the description of 'HLX', above. 

 The default value of 'HLY' is 0.
<dt>'ILA' - Informational Label Angle - Real
<dd>The parameter 'ILA' specifies the angle (in degrees counterclockwise from a vector pointing to the right) at which the informational label is to be written. 

 The default value of 'ILA' is 0. 

<dt>'ILB' - Informational Label Box Flag - Integer
<dd>If 'ILB' is zero, the informational label will not be boxed at all. The value 1 implies that the perimeter of the box is to be drawn (in the same color as the label) after the label is drawn. The value 2 implies that the box is to be filled (in the color specified by 'LBC') before the label is drawn. The value 3 implies both of the above. 

 The default value of 'ILB' is 0. 

<dt>'ILC' - Informational Label Color Index - Integer
<dd>If 'ILC' is less than zero, the informational label and the box, if any, around it, will be drawn in the color specified by the current text color index; if 'ILC' is greater than or equal to zero, then it specifies the desired color index for the label and the box. If a box is drawn around the label, it is made the same color as the label itself. 

 The default value of 'ILC' is -1. 

<dt>'ILL' - Informational Label Line Width - Real
<dd>If 'ILL' has a value less than or equal to zero, line width will not be set before drawing a box around the informational label. If 'ILL' has a value greater than zero, it specifies the desired width, as a multiple of the &quot;normal&quot; line width. 

 The default value of 'ILL' is 0.
<dt>'ILP' - Informational Label Positioning Flag - Integer
<dd>The parameter 'ILP' says how the informational label is to be positioned. There are nine possible values, each of which specifies a point of the label box which is to lie on the point defined by 'ILX' and 'ILY': the value -4 implies the lower left-hand corner of the label box, -3 implies the center of the bottom of the box, -2 the lower right-hand corner of the box, -1 the center of the left edge of the box, 0 the center of the box, +1 the center of the right edge of the box, +2 the upper left-hand corner of the box, +3 the center of the top edge of the box, and +4 the upper right-hand corner of the box. Left, right, bottom, and top are defined from the viewpoint of someone reading the label right-side up. 

 The default value of 'ILP' is 4, so the upper right-hand corner of the box will be placed on the point ('ILX','ILY'). 

<dt>'ILS' - Informational Label Size - Real
<dd>The parameter 'ILS' specifies the nominal size (width) of a character in the informational label, as a fraction of the width of the viewport. This nominal size is multiplied by 'CWM'. 

 The default value of 'ILS' is 0.012.
<dt>'ILT' - Informational Label Text String - Character
<dd>The parameter 'ILT' is a string of 100 or fewer characters, specifying the text of the informational label. The following substrings will be replaced by a numeric value:
<dl COMPACT><dd>$CIU$ - THE CONTOUR INTERVAL USED. 
 $CMN$ - THE MINIMUM CONTOUR LEVEL. 
 $CMX$ - THE MAXIMUM CONTOUR LEVEL. 
 $SFU$ - THE CURRENT SCALE FACTOR. 
 $ZMN$ - THE MINIMUM VALUE IN THE DATA ARRAY. 
 $ZMX$ - THE MAXIMUM VALUE IN THE DATA ARRAY. 
</dl><dd>In each case except $SFU$, the given value will have been divided by the current scale factor. A &quot;U&quot; may be inserted just before the final &quot;$&quot; (as in '$CIUU$', '$CMNU$', etc.) to request the use of an unscaled value. 

 The value with which $CIU$ is replaced will only be correct if Conpack itself has chosen the contour levels; otherwise, it may be necessary for the user to set the value of 'CIU' (which see, above). 

 If 'ILT' is given the value ' ' (a single blank), there will be no informational label. 

 The default value of 'ILT' is 'CONTOUR FROM $CMN$ TO $CMX$ BY $CIU$'.
<dt>'ILW' - Informational Label White Space Width - Real
<dd>The parameter 'ILW' specifies the nominal width of white space to be left around the informational label, as a fraction of the width of the viewport. This nominal width is multiplied by 'CWM'. 

 The default value of 'ILW' is 0.005.
<dt>'ILX' - Informational Label X Coordinate - Real
<dd>The parameter 'ILX' specifies the X coordinate of the basepoint of the informational label. The given value is mapped linearly onto the viewport; 0 refers to the left edge of the viewport and 1 to the right edge of the viewport. Values less than 0 or greater than 1 may be used. 

 The default value of 'ILX' is 0.98.
<dt>'ILY' - Informational Label Y Coordinate - Real
<dd>The parameter 'ILY' specifies the Y coordinate of the basepoint of the informational label. The given value is mapped linearly onto the viewport; 0 refers to the bottom edge of the viewport and 1 to the top edge of the viewport. Values less than 0 or greater than 1 may be used. 

 The default value of 'ILY' is -.02.
<dt>'IWM' - Integer Workspace for Masking - Integer
<dd>The parameter 'IWM' specifies the amount of integer workspace to be allotted for use by CPCLDM, which draws contour lines masked by an area map, in calls to the routine ARDRLN, in the package Areas. Assume a parameter value &quot;n&quot;; the space used will be &quot;2n&quot; (&quot;n&quot; for the array IAI and &quot;n&quot; for the array IAG, in calls to ARDRLN). The value &quot;n&quot; must be greater than or equal to the number of group identifiers used in generating the area map. 

 The default value of 'IWM' is 10.
<dt>'IWU' - Integer Workspace Usage - Integer
<dd>The parameter 'IWU' is intended for retrieval only. It is zeroed by the call to CPRECT, CPSPS1, or CPSPS2. Therefore, by retrieving its value after an entire plot has been constructed, one may find out how large an integer workspace was actually required.
<dt>'LBC' - Label Box Color Index - Integer
<dd>If label boxes (of whatever type) are filled, the filling is done using the color index specified by 'LBC'. If 'LBC' is less than zero, the current fill area color index is used. 

 The default value of 'LBC' is 0, which specifies the background color.
<dt>'LBX' - Label Box X Coordinate - Real
<dd>Not to be set by the user. The value may be retrieved in one of the routines CPCHCF, CPCHHL, CPCHIL, or CPCHLL. It specifies the X coordinate (in the current user coordinate system) of the center of the box surrounding the label that has caused the routine to be called. 

 The default value of 'LBX' is 0.
<dt>'LBY' - Label Box Y Coordinate - Real
<dd>Not to be set by the user. The value may be retrieved in one of the routines CPCHCF, CPCHHL, CPCHIL, or CPCHLL. It specifies the Y coordinate (in the current user coordinate system) of the center of the box surrounding the label that has caused the routine to be called. 

 The default value of 'LBY' is 0.
<dt>'LIS' - Label Interval Specifier - Integer
<dd>When 'CLS' is given a positive value, indicating that Conpack is to choose contour levels at intervals of the form &quot;bk&quot;, where &quot;b&quot; is a base value and &quot;k&quot; is an integer, and 'CIS' is given a positive value, indicating that it is the desired value of &quot;b&quot;, then 'LIS' must be set to specify the interval between labeled contour levels. 

 See the descriptions of the parameters 'CLS' and 'CIS'. 

 As an example, one might specify 'CLS'=1, 'CIS'=1/3 and 'LIS'=3 in order to get contours at values like 1/3, 2/3, 3/ 3, 4/3, etc., with labels at values like 1, 2, 3, etc. 

 The default value of 'LIS' is 5.
<dt>'LIT' - Label Interval Table - Integer Array
<dd>See the description of the parameter 'CIT'.
<dt>'LIU' - Label Interval Used - Integer
<dd>The parameter 'LIU' is for retrieval only. When Conpack chooses the contour interval and decides that every &quot;nth&quot; one should be labeled, it sets 'LIU' to &quot;n&quot;.
<dt>'LLA' - Line Label Angle - Real
<dd>The parameter 'LLA' specifies the angle (in degrees counterclockwise from a vector pointing to the right) at which contour line labels are to be written when ABS('LLP') is greater than or equal to 2 and 'LLO' is 0. 

 The default value of 'LLA' is 0.
<dt>'LLB' - Line Label Box Flag - Integer
<dd>If 'LLB' is zero, contour line labels drawn by CPLBDR will not be boxed at all. The value 1 implies that the perimeter of the box is to be drawn (in the same color as the label) after the label is drawn. The value 2 implies that the box is to be filled (in the color specified by 'LBC') before the label is drawn. The value 3 implies both of the above. 

 The default value of 'LLB' is 0.
<dt>'LLC' - Line Label Color Index - Integer Array
<dd>Each element of the parameter array 'LLC', if greater than or equal to zero, is the color index for labels on contour lines at the level specified by the associated element of 'CLV'. A value less than zero implies that the current text color index is to be used. 

 This parameter only affects line labels when ABS('LLP') = 2 or 3 and the labels are therefore drawn by CPLBDR. It does not affect line labels when ABS('LLP') = 1 and the line labels are therefore drawn by the dash package, as called by CPCLDM or CPCLDR. 

 The default values of the elements of 'LLC' are all -1's.
<dt>'LLL' - Line Label Line Width - Real
<dd>If 'LLL' has a value less than or equal to zero, line width will not be set before drawing boxes around contour line labels. If 'LLL' has a value greater than zero, it specifies the desired width, as a multiple of the &quot;normal&quot; line width. 

 The default value of 'LLL' is 0.
<dt>'LLO' - Line Label Orientation - Integer
<dd>The parameter 'LLO' only has effect when ABS('LLP') is greater than or equal to 2, specifying use of either the regular scheme or the penalty scheme for positioning labels on contour lines. If 'LLO' is zero, the labels are written at the angle specified by 'LLA'. If 'LLO' is non-zero, the labels are written in the local direction of the contour line. 

 The default value of 'LLO' is 0.
<dt>'LLP' - Line Label Positioning - Integer
<dd>The parameter 'LLP' says whether or not labels should be produced and, if so, how, as follows:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>If 'LLP' is 0, it says that no line labels should be produced.
<dt>&bull;
<dd>If ABS('LLP') is 1, it says that labels should be positioned along contour lines by using the old Conrec_family scheme of setting up a character dash pattern including the label and using the software dash package to draw the labels (which requires having 'DPU' set non-zero). This scheme has the disadvantages that one cannot control the orientation and one cannot shield the labels from having contour lines drawn through them.
<dt>&bull;
<dd>If ABS('LLP') is 2, it says that labels should be positioned at regular intervals along the line. See the descriptions of the parameters 'RC1', 'RC2', and 'RC3'.
<dt>&bull;
<dd>If ABS('LLP') is 3, it says that labels should be positioned using a penalty scheme, which gives much better results than either of the others.</dl></dl><dd>When 'LLP' is 2 or 3, the 2D smoothing, if any, implied by the value of 'T2D' is suspended during label positioning, so that fewer label positions will be considered; this is quite a bit faster and the results are nearly as good as if the smoothing were done. To force smoothing, use 'LLP' = -2 or -3. 

 The default value of 'LLP' is 1.
<dt>'LLS' - Line Label Size - Real
<dd>The parameter 'LLS' specifies the nominal size (width) of a character in a contour line label, as a fraction of the width of the viewport. This nominal size is multiplied by 'CWM'. 

 The default value of 'LLS' is 0.010.
<dt>'LLT' - Line Label Text String - Character
<dd>For each I from 1 to 'NCL', element I of the parameter array 'LLT' is a string of twenty or fewer characters, to be used as a label for the contour level specified by the Ith element of 'CLV'. Since the character string will be plotted using the routine PLCHHQ, in the package Plotchar, it may contain colon-enclosed &quot;function codes&quot; to do things like create superscripts. 

 If the elements of this array are not supplied by the user, they will be filled in by Conpack itself.
<dt>'LLW' - Line Label White Space - Real
<dd>The parameter 'LLW' specifies the nominal width of white space to be left around a contour line label, as a fraction of the width of the viewport. This nominal width is multiplied by 'CWM'. 

 The default value of 'LLW' is 0.005.
<dt>'LOC' - Low Label Color Index - Integer
<dd>The parameter 'LOC' is used in determining the color index for low labels. See the description of 'HLC', above.
<dt>'LOT' - Low Label Text String - Character
<dd>The parameter 'LOT' specifies the text string to be used in labeling a low. See 'HLT', above.
<dt>'MAP' - Mapping Flag - Integer
<dd>If 'MAP' is zero, it says that the x and y coordinates used to create the contour map are not to be transformed by the user-replaceable subroutine CPMPXY. If 'MAP' is non-zero, it says that x and y coordinates are to be so transformed. The default version of CPMPXY provides two useful mappings: 

 If the first subscript of the data array is a linear function of the longitude and the second is a linear function of the latitude, then one can transform all graphics output onto a map background created by calls to routines in the utility package Ezmap just by setting 'MAP' = 1, 'XC1' = minimum longitude, 'XCM' = maximum longitude, 'YC1' = minimum latitude, and 'YCN' = maximum latitude. Also, the parameter 'SET' must be given the value 0 in order to prevent Conpack from calling SET and thereby overriding the call done by Ezmap. 

 If the first subscript of the data array is a linear function of rho and the second is a linear function of theta, where rho and theta are polar coordinates, then to map all graphics output properly, one may set 'MAP' = 2, 'XC1' = minimum rho, 'XCM' = maximum rho, 'YC1' = minimum theta, and 'YCN' = maximum theta. In this case, one must either use 'SET' = 0 and do an appropriate SET call or use 'SET' = 1 and give the parameters 'WDB', 'WDL', 'WDR', and 'WDT' values consistent with the mapped values of X and Y, which will all be of the form &quot;rho*cos(theta)&quot; and &quot;rho*sin(theta)&quot;, respectively. 

 Using any other non-zero value of 'MAP' will result in the identity mapping. 

 Of course, one can replace the routine CPMPXY and build as many different mappings into it as desired. See the description of CPMPXY.
<dt>'NCL' - Number of Contour Levels - Integer
<dd>If Conpack is to pick contour levels (see the description of the parameter 'CLS') then the initial call to CPRECT, CPSPS1, or CPSPS2 causes 'NCL' to be zeroed. Subsequently, during the first call to a Conpack routine requiring contour levels to have been chosen, 'NCL' will be set as part of the process of choosing them. If the user elects to choose the contour levels, the first parameter which must be set to do this is 'NCL'. 

 The parameter 'NCL' has no meaningful default value.
<dt>'NEL' - Numeric Exponent Length - Integer
<dd>Giving 'NEL' a value less than or equal to zero says that exponents in numeric labels should be written in the shortest possible form; plus signs are omitted and the exponent magnitude is written with no leading zeroes. A value &quot;n&quot; which is greater than zero indicates that all exponents should be written with a sign (+ or -) and that the exponent magnitude should be padded with leading zeroes to a length of n characters. 

 The default value of 'NEL' is 0.
<dt>'NET' - Numeric Exponent Type - Integer
<dd>The parameter 'NET' says what characters are to be used between the mantissa of a numeric label and the exponent. The value 0 implies the use of an E, as in FORTRAN &quot;E format&quot;, the value 1 implies the use of function codes, as expected by the utility Plotchar, to generate &quot;x 10**n&quot;, where n is a superscript exponent, and the value 2 implies the use of &quot;x10**&quot;. 

 The default value of 'NET' is 1.
<dt>'NEU' - Numeric Exponent Use Flag - Integer
<dd>Giving 'NEU' a value less than or equal to zero forces the use of the exponential form in all numeric labels. A positive value &quot;n&quot; indicates that the form without an exponent should be used as long as it requires no more than n characters; otherwise the form requiring the fewest characters should be used. 

 The default value of 'NEU' is 5.
<dt>'NLS' - Numeric Leftmost Significant Digit Flag - Integer
<dd>Giving 'NLS' the value zero says that the leftmost non-zero digit of a number represented by a numeric label is to be considered its first significant digit. A non-zero value says that the digit in the same digit position as the leftmost non-zero digit of the largest number (in absolute value) in the data field being contoured is to be considered the leftmost significant digit. This tends to make the numeric labels more nearly consistent with one another. Consider the following example, using three significant digits: 

<dl COMPACT><dd>USING 'NLS'=0: .500 1.00 1.50 ... 9.50 10.5 ... 
 USING 'NLS'=1: .5 1.0 1.5 ... 9.5 10.5 ...</dl><dd>The default value of 'NLS' is 1.
<dt>'NLZ' - Numeric Leading Zero Flag - Integer
<dd>Giving 'NLZ' a non-zero value says that a zero is to placed before any numeric label which would otherwise begin with a decimal point (use &quot;0.345&quot;, rather than &quot;.345&quot;). 

 The default value of 'NLZ' is 0.
<dt>'NOF' - Numeric Omission Flags - Integer
<dd>The parameter 'NOF' says what parts of a numeric label may be omitted. The value 0 says that no part may be omitted. Add a 4 to indicate that a leading &quot;1&quot; or &quot;1.&quot; which is unnecessary (as in &quot;1 x 10**13&quot;) may be omitted, a 2 to indicate that a trailing decimal point (as in &quot;13.&quot;) may be omitted, and a 1 to indicate that trailing zeroes (as in &quot;46.200&quot;) may be omitted. 

 Contour line labels generated by Conpack and values in the informational label which are known to have been rounded to &quot;nice&quot; values (like '$CIU$', '$CMN$', and '$CMX$') will have trailing zeroes trimmed in any case, no matter what the value of 'NOF' is. 

 The default value of 'NOF' is 6 (4 + 2).
<dt>'NSD' - Number of Significant Digits - Integer
<dd>The parameter 'NSD' specifies the maximum number of significant digits to be used in numeric labels representing contour field values. A negative value &quot;-n&quot; indicates that n significant digits should be used. A positive value &quot;n&quot; indicates that &quot;m+n&quot; digits should be used, where &quot;m&quot; is the number of digits that are the same for all values in the contour field. (For example, if the minimum value is &quot;1123.6&quot; and the maximum value is &quot;1125.9&quot;, then the value of &quot;m&quot; is 3.) 

 The default value of 'NSD' is 4.
<dt>'NVS' - Number of Vertical Strips - Integer
<dd>When the parameter 'NVS' is non-zero, an extra group of edges, with group identifier 'GIS', is added to the area map by the routine CPCLAM. These edges include the boundary of the viewport and enough vertical lines to break the area occupied by the viewport up into 'NVS' vertical strips. The object of this is to break up the contour bands which are to be filled into smaller and simpler pieces; this may be necessary if the graphics device in use limits the number of points which may be used to define a polygon to be filled. The area identifier for the outside of the viewport is -1; all other area identifiers used are 0's. 

 The default value of 'NVS' is 1.
<dt>'ORV' - Out-of-Range Value - Real
<dd>If 'ORV' is non-zero, it specifies an out-of-range value, to be used as the value of X and Y coordinates returned by the mapping routine CPMPXY to say that a point is out-of-range (invisible) under the current mapping. 

 The default value of 'ORV' is 0.
<dt>'PAI' - Parameter Array Index - Integer
<dd>The value of 'PAI' must be set before calling CPGETC, CPGETI, CPGETR, CPSETC, CPSETI, or CPSETR to access any parameter which is an array; it indicates which element of the array is meant. For example, to set the 10th contour level to zero, use code like this:
<dl COMPACT><dd>CALL CPSETI ('PAI - PARAMETER ARRAY INDEX',10) 
 CALL CPSETR ('CLV - CONTOUR LEVEL',0.)</dl><dd>The default value of 'PAI' is 0.
<dt>'PC1' - Penalty Scheme Constant 1 - Real
<dd>The parameter 'PC1' is one of the constants used in the penalty scheme for positioning labels. The largest gradient allowed at the position of a label will be GRAV + 'PC1' * GRSD, where GRAV is the average gradient and GRSD is the standard deviation of the gradients. 

 The default value of 'PC1' is 1.
<dt>'PC2' - Penalty Scheme Constant 2 - Real
<dd>The parameter 'PC2' is one of the constants used in the penalty scheme for positioning labels. It specifies the maximum (estimated) number of contour bands allowed to cross a label. 

 The default value of 'PC2' is 5.
<dt>'PC3' - Penalty Scheme Constant 3 - Real
<dd>The parameter 'PC3' is one of the constants used in the penalty scheme for positioning labels. It specifies, in degrees, the maximum cumulative change in direction to be allowed along that portion of the contour line covered by a circle centered on a label and having a radius equal to half the width of the label. 

 The default value of 'PC3' is 60.
<dt>'PC4' - Penalty Scheme Constant 4 - Real
<dd>The parameter 'PC4' is one of the constants used in the penalty scheme for positioning labels. It specifies the &quot;optimal distance&quot; in the term in the penalty function which attempts to force labels to be at an optimal distance from each other. 

 The default value of 'PC4' is 0.05.
<dt>'PC5' - Penalty Scheme Constant 5 - Real
<dd>The parameter 'PC5' is one of the constants used in the penalty scheme for positioning labels. It specifies the &quot;folding distance&quot; in the term in the penalty function which attempts to force labels to be at an optimal distance from each other. 

 The default value of 'PC5' is 0.15.
<dt>'PC6' - Penalty Scheme Constant 6 - Real
<dd>The parameter 'PC6' is one of the constants used in the penalty scheme for positioning labels. It specifies the minimum distance to be allowed between any two labels on the same contour line, as a fraction of the width of the viewport. 

 The default value of 'PC6' is 0.30.
<dt>'PIC' - Point Interpolation Flag for Contours - Integer
<dd>The parameter 'PIC' specifies the number of points to interpolate between each pair of points defining a segment of a contour line, prior to any mapping implied by the parameter 'MAP'. It is intended that a non-zero value should normally be used only if 'MAP' is non-zero, which turns mapping on, and 'T2D' is zero, which turns the 2D smoother off; the intent is to map straight-line segments of contour lines more nearly correctly into curved-line segments on a background (one drawn by Ezmap, for example). If the 2D smoother is turned on, the additional points will be used and the smoothed curve will be constrained to pass through them; this may be useful. 

 A negative value of 'PIC' causes ABS('PIC') points to be interpolated, but the interpolated points are not, in general, used to draw the line segment; the object, in this case, is simply to do a finer search for changes in visibility (out-of-range state, as defined by values of 'ORV' returned by the routine CPMPXY) along the segment. 

 The default value of 'PIC' is 0.
<dt>'PIE' - Point Interpolation Flag for Edges - Integer
<dd>The parameter 'PIE' specifies the number of points to interpolate between each pair of points defining a segment of an &quot;edge&quot; (the edge of the grid, the edge of a special-value area, or the edge of an out-of-range area). It is intended that a non-zero value should normally be used only if 'MAP' is non-zero, which turns mapping on; the intent is to map straight-line segments of edge lines more nearly correctly into curved-line segments on a background (one drawn by Ezmap, for example). 

 A negative value of 'PIE' causes ABS('PIE') points to be interpolated, but the interpolated points are not, in general, used to draw the line segment; the object, in this case, is simply to do a finer search for changes in out-of-range state (visibility) along the segment. (The edges of out-of-range areas, however, are drawn using all such interpolated points.) 

 Using too large an (absolute) value of 'PIE' will cause the tracing of the edges of out-of-range areas to be very time-consuming, because the number of points to be examined is 'ZDM' x 'ZDN' x 'PIE' x 'PIE'. 

 The default value of 'PIE' is 0.
<dt>'PW1' - Penalty Scheme Weight 1 - Real
<dd>The parameter 'PW1' specifies the weight for the gradient term in the penalty function. 

 The default value of 'PW1' is 2.
<dt>'PW2' - Penalty Scheme Weight 2 - Real
<dd>The parameter 'PW2' specifies the weight for the number-of-contours term in the penalty function. 

 The default value of 'PW2' is 0.
<dt>'PW3' - Penalty Scheme Weight 3 - Real
<dd>The parameter 'PW3' specifies the weight for the change-in-direction term in the penalty function. 

 The default value of 'PW3' is 1.
<dt>'PW4' - Penalty Scheme Weight 4 - Real
<dd>The parameter 'PW4' specifies the weight for the optimum-distance term in the penalty function. 

 The default value of 'PW4' is 1.
<dt>'RC1' - Regular Scheme Constant 1 - Real
<dd>The parameter 'RC1' specifies the desired distance from the beginning of a contour line to the first label on that line when they are positioned using the &quot;regular&quot; scheme. The nth label on each labeled contour line will be at a distance 'RC1' + 'RC2' x (n-1) + 'RC3' x Rn units (in the fractional coordinate system) from the beginning of the line, where &quot;Rn&quot; is a random number between -1 and 1. 

 The default value of 'RC1' is 0.25.
<dt>'RC2' - Regular Scheme Constant 2 - Real
<dd>The parameter 'RC2' specifies the desired nominal distance between labels when they are positioned using the &quot;regular&quot; scheme. See the description of 'RC1', above. 

 The default value of 'RC2' is 0.25.
<dt>'RC3' - Regular Scheme Constant 3 - Real
<dd>The parameter 'RC3' specifies the desired maximum variation in the distance between labels when they are positioned using the regular scheme. See the description of 'RC1', above. 

 The default value of 'RC3' is 0.05.
<dt>'RWC' - Real Workspace for Contours - Integer
<dd>The parameter 'RWC' specifies the amount of real workspace to be allotted to hold X coordinates of points defining contour lines. Assume a parameter value &quot;n&quot;. If no 2D smoothing is requested, the total space used will be &quot;2n&quot; (&quot;n&quot; for X coordinates and another &quot;n&quot; for Y coordinates). If 2D smoothing is requested, the total space used will be &quot;7n&quot; (&quot;n&quot; for X coordinates, &quot;n&quot; for Y coordinates, and &quot;5n&quot; for scratch arrays). 

 Normally, the value of 'RWC' is of no particular interest to the user, since the same contour lines are produced with a small value as would be produced with a larger value. There are two situations in which it becomes of more interest: 1) When the penalty scheme is used to position labels, the length of the portion of the contour line over which the penalty function is evaluated is limited by the value of 'RWC'. If 'RWC' is set too small, too many labels may be put on a given contour line and some of them may be too close to each other. 2) When hachuring has been activated (by setting the value of 'HCF' non-zero), it is important that the internal routine that does the hachuring see entire contours at once, so that it may properly decide whether a contour is open or closed and, in the latter case, where the interior of the closed contour is. In both of these cases, the solution is to increase the value of 'RWC'. 

 The default value of 'RWC' is 100.
<dt>'RWG' - Real Workspace for Gradients - Integer
<dd>The parameter 'RWG' specifies the amount of real workspace to be allotted to hold gradients which are to be computed and used in positioning labels using the penalty scheme. Using a larger value provides for a more accurate representation of the gradient field, up to the point at which it exceeds 'ZDM' x 'ZDN'. 

 The default value of 'RWG' is 1000.
<dt>'RWM' - Real Workspace for Masking - Integer
<dd>The parameter 'RWM' specifies the amount of real workspace to be allotted for use by CPCLDM, which draws contour lines masked by an area map, in calls to the routine ARDRLN, in the package Areas. Assume a parameter value &quot;n&quot;; the space used will be &quot;2n&quot; (&quot;n&quot; for the X-coordinate array XCS and &quot;n&quot; for the Y-coordinate array YCS, in calls to ARDRLN). Any value of &quot;n&quot; greater than or equal to 2 will work; smaller values will cause the generation of more calls to the user routine RTPL (one of the arguments of CPCLDM). 

 The default value of 'RWM' is 100.
<dt>'RWU' - Real Workspace Usage - Integer
<dd>The parameter 'RWU' is intended for retrieval only. It is zeroed by the call to CPRECT, CPSPS1, or CPSPS2. Thereafter, as Conpack routines are called, the value of 'RWU' is updated to reflect the largest number of words of real workspace needed at any one time. Therefore, by retrieving its value after an entire plot has been constructed, one may find out how large a real workspace was actually required.
<dt>'SET' - Do-SET-Call Flag - Integer
<dd>Giving 'SET' the value 0 says that no SET call is to be done by Conpack; the value 1 says that it is to be done. In the latter case, the call is done by CPRECT, CPSPS1, or CPSPS2. 

 Arguments 5-8 of a SET call done by the user must be consistent with the ranges of the X and Y coordinates being used by Conpack, as specified by the values of the parameters 'XC1', 'XCM', 'YC1', 'YCN', and 'MAP'. See the descriptions of those parameters. 

 The default value of 'SET' is 1.
<dt>'SFS' - Scale Factor Selector - Real
<dd>The scale factor is that value (usually, but not necessarily, a power of 10) by which the actual values of contour field values are to be divided to get the value of a numeric label. If 'SFS' is given a value greater than zero, that value is the scale factor to be used. If 'SFS' is given a value less than or equal to zero, it is truncated to form an integer directing Conpack to select a scale factor, as follows:
<dl COMPACT><dd><dl COMPACT><dt>0
<dd>Implies that the scale factor should be selected in such a way as to reduce the ZDAT element having the largest absolute value to the range from 0.1 to 0.999...
<dt>-1
<dd>Implies that the scale factor should be selected in such a way as to reduce the ZDAT element having the largest absolute value to the range from 1. to 9.999...
<dt>-2
<dd>Implies that the scale factor should be selected in such a way as to place the decimal point in the ZDAT element having the largest absolute value after the rightmost significant digit of that value (as defined by the values of 'NSD' and 'NLS').
<dt>-3
<dd>Implies that the scale factor should be selected in such a way as to remove extra zeroes from the ends of the ZDAT element having the largest absolute value. For example, if that element were 0.000136, the scale factor would be 10 to the power -3; if that element were 136000 (assuming three significant digits are desired), the scale factor would be 10 to the power 3. If there are no extra zeroes on either end of the ZDAT element having the largest absolute value, the scale factor will be 1.
<dt>-4 or less
<dd>Implies that the scale factor should be selected in such a way as to reduce all contour labels to integers. 

 The default value of 'SFS' is 1.
<dt>'SFU' - Scale Factor Used - Real
<dd>The parameter 'SFU' is intended for retrieval only; it gives the value of the scale factor selected for use by Conpack.
<dt>'SPV' - Special Value - Real
<dd>If 'SPV' is non-zero, it specifies a &quot;special value&quot;, which may be used in data fields to signal missing data. No contour lines will be drawn within any grid cell with a special value at one or more of its four corners. 

 The default value of 'SPV' is 0.
<dt>'SSL' - Smoothed Segment Length - Real
<dd>The parameter 'SSL' specifies the distance between points used to draw the curves generated by 2D smoothing; it is expressed as a fraction of the width of the window in the coordinate system in which the smoothing is being done. 

 The default value of 'SSL' is 0.01.
<dt>'T2D' - Tension on 2-Dimensional Splines - Real
<dd>A non-zero value of 'T2D' says that 2D smoothing (using cubic splines under tension) should be done; the absolute value of 'T2D' is the desired tension. If 'T2D' is negative, smoothing will be done before the mapping, if any, requested by the flag 'MAP'; if 'T2D' is positive, smoothing will be done after the mapping. 

 The default value of 'T2D' is 0.
<dt>'T3D' - Tension on 3-Dimensional Splines - Real
<dd>The parameter 'T3D' specifies the tension on the 3D (bicubic) splines used by CPSPS1 or CPSPS2 to smooth the data being contoured. 

 The default value of 'T3D' is 1.
<dt>'VPB' - Viewport Bottom - Real
<dd>The parameter 'VPB' is only used when 'SET' is non-zero, saying that Conpack should do the call to SET; it specifies the position of the bottom edge of the area in which the viewport is to be placed, expressed as a fraction between 0 (the bottom edge of the plotter frame) and 1 (the top edge of the plotter frame). See also the description of 'VPS'. 

 The default value of 'VPB' is 0.05.
<dt>'VPL' - Viewport Left - Real
<dd>The parameter 'VPL' is only used when 'SET' is non-zero, saying that Conpack should do the call to SET; it specifies the position of the left edge of the area in which the viewport is to be placed, expressed as a fraction between 0 (the left edge of the plotter frame) and 1 (the right edge of the plotter frame). See also the description of 'VPS'. 

 The default value of 'VPL' is 0.05.
<dt>'VPR' - Viewport Right - Real
<dd>The parameter 'VPR' is only used when 'SET' is non-zero, saying that Conpack should do the call to SET; it specifies the position of the right edge of the area in which the viewport is to be placed, expressed as a fraction between 0 (the left edge of the plotter frame) and 1 (the right edge of the plotter frame). See also the description of 'VPS'. 

 The default value of 'VPR' is 0.95.
<dt>'VPS' - Viewport Shape - Real
<dd>The parameter 'VPS' is only used when 'SET' is non-zero, saying that Conpack should do the call to SET; it specifies the desired viewport shape, as follows:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>A negative value specifies the exact shape of the viewport; the absolute value is the ratio of the width of the viewport to its height.
<dt>&bull;
<dd>The value 0 specifies a viewport completely filling the area specified by 'VPL', 'VPR', 'VPB', and 'VPT'.
<dt>&bull;
<dd>A value &quot;s&quot; between 0 and 1 specifies a plot of the shape determined by the values of 'XC1', 'XCM', 'YC1', and 'YCN', reverting to the shape specified by 'VPL', 'VPR', 'VPB', and 'VPT' if the ratio of the shorter side to the longer side would be less than &quot;s&quot;.
<dt>&bull;
<dd>A value &quot;s&quot; greater than or equal to 1 specifies a plot of the shape determined by the values of 'XC1', 'XCM', YC1', and 'YCN', reverting to a square if the ratio of the longer side to the shorter side would be greater than &quot;s&quot;.</dl></dl><dd>The viewport, whatever its final shape, is centered in, and made as large as possible in, the area specified by the parameters 'VPB', 'VPL', 'VPR', and 'VPT'. 

 The default value of 'VPS' is 0.25.
<dt>'VPT' - Viewport Top - Real
<dd>The parameter 'VPT' is only used when 'SET' is non-zero, saying that Conpack should do the call to SET; it specifies the position of the top edge of the area in which the viewport is to be placed, expressed as a fraction between 0 (the bottom edge of the plotter frame) and 1 (the top edge of the plotter frame). See also the description of 'VPS'. 

 The default value of 'VPT' is 0.95.
<dt>'WDB' - Window Bottom - Real
<dd>When Conpack does the call to 'SET', the parameter 'WDB' is used to determine argument number 7, the user Y coordinate at the bottom of the window. If 'WDB' is not equal to 'WDT', 'WDB' is used. If 'WDB' is equal to 'WDT', but 'YC1' is not equal to 'YCN', then 'YC1' is used. Otherwise, the value 1 is used. 

 The default value of 'WDB' is 0.
<dt>'WDL' - Window Left - Real
<dd>When Conpack does the call to 'SET', the parameter 'WDL' is used to determine argument number 5, the user X coordinate at the left edge of the window. If 'WDL' is not equal to 'WDR', 'WDL' is used. If 'WDL' is equal to 'WDR', but 'XC1' is not equal to 'XCM', then 'XC1' is used. Otherwise, the value 1 is used. 

 The default value of 'WDL' is 0.
<dt>'WDR' - Window Right - Real
<dd>When Conpack does the call to 'SET', the parameter 'WDR' is used to determine argument number 6, the user X coordinate at the right edge of the window. If 'WDR' is not equal to 'WDL', 'WDR' is used. If 'WDR' is equal to 'WDL', but 'XCM' is not equal to 'XC1', then 'XCM' is used. Otherwise, the value REAL('ZDM') is used. 

 The default value of 'WDR' is 0.
<dt>'WDT' - Window Top - Real
<dd>When Conpack does the call to 'SET', the parameter 'WDB' is used to determine argument number 8, the user Y coordinate at the top of the window. If 'WDT' is not equal to 'WDB', 'WDT' is used. If 'WDT' is equal to 'WDB', but 'YCN' is not equal to 'YC1', then 'YCN' is used. Otherwise, the value REAL('ZDN') is used. 

 The default value of 'WDT' is 0.
<dt>'WSO' - Workspace Overflow Flag - Integer
<dd>The parameter 'WSO' says what to do when a real or integer workspace overflow occurs, as follows:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>The value 0 indicates that execution will terminate with a fatal-error call to SETER.
<dt>&bull;
<dd>The value 1 indicates that an error message will be written to the error file, after which execution will continue.
<dt>&bull;
<dd>The value 2 indicates that no error message will be written, and that execution will continue.</dl></dl><dd>When execution continues, the resulting plot will be incomplete. The values of 'IWU' and 'RWU' may be retrieved to find out how much workspace would have been used if the call on which the workspace overflow occurred had succeeded; note that, if these amounts are provided on a subsequent run, one is not assured that the workspace overflow will be averted. 

 The default value of 'WSO' is 1.
<dt>'XC1' - X Coordinate at Index 1 - Real
<dd>The parameter 'XC1' specifies the X coordinate value which corresponds to a value of 1 for the first subscript of the data array, prior to any mapping implied by a non-zero value of 'MAP'. If 'XC1' is equal to 'XCM', 1 will be used. 

 The default value of 'XC1' is 0.
<dt>'XCM' - X Coordinate at Index M - Real
<dd>The parameter 'XCM' specifies the X coordinate value which corresponds to a value of 'ZDM' for the first subscript of the data array, prior to any mapping implied by a non-zero value of 'MAP'. If 'XC1' is equal to 'XCM', REAL('ZDM') will be used. 

 The default value of 'XCM' is 0.
<dt>'YC1' - Y Coordinate at Index 1 - Real
<dd>The parameter 'YC1' specifies the Y coordinate value which corresponds to a value of 1 for the second subscript of the data array, prior to any mapping implied by a non-zero value of 'MAP'. If 'YC1' is equal to 'YCM', 1 will be used. 

 The default value of 'YC1' is 0.
<dt>'YCN' - Y Coordinate at Index N - Real
<dd>The parameter 'YCN' specifies the Y coordinate value which corresponds to a value of 'ZDN' for the second subscript of the data array, prior to any mapping implied by a non-zero value of 'MAP'. If 'YC1' is equal to 'YCN', REAL('ZDN') will be used. 

 The default value of 'YCN' is 0.
<dt>'ZD1' - ZDAT 1st Dimension - Integer
<dd>The parameter 'ZD1' specifies the first dimension of the array ZDAT, which contains the data to be contoured. If CPRECT is called, it sets 'ZD1' (the argument KZDT is the desired value). If CPSPS1 or CPSPS2 is called, it either picks a value of 'ZD1' (if 'ZDS' is non-zero) or expects the user to have done so (if 'ZDS' is zero). 

 The default value of 'ZD1' is 1.
<dt>'ZDM' - Z Data Array Dimension M - Integer
<dd>The parameter 'ZDM' specifies the first dimension of the array of data to be contoured. Its value will be less than or equal to the value of 'ZD1'. If CPRECT is called, it sets 'ZDM' (the argument MZDT is the desired value). If CPSPS1 or CPSPS2 is called, it either picks a value of 'ZDM' (if 'ZDS' is non-zero) or expects the user to have done so (if 'ZDS' is zero). 

 The default value of 'ZDM' is 1.
<dt>'ZDN' - Z Data Array Dimension N - Integer
<dd>The parameter 'ZDN' specifies the second dimension of the array of data to be contoured. If CPRECT is called, it sets 'ZDN' (the argument NZDT is the desired value). If CPSPS1 or CPSPS2 is called, it either picks a value of 'ZDN' (if 'ZDS' is non-zero) or expects the user to have done so (if 'ZDS' is zero). 

 The default value of 'ZDN' is 1.
<dt>'ZDS' - ZDAT Dimension Selector - Integer
<dd>If 'ZDS' is non-zero, CPSPS1 or CPSPS2 will select values for 'ZD1', 'ZDM', and 'ZDN'; otherwise, they will be expected to have been set by the user. Note that, if the size of the dense array is not a product of the size of the sparse array and some perfect square, the aspect ratio of the dense grid may be slightly different from that of the sparse grid. 

 The default value of 'ZDS' is 1.
<dt>'ZDU' - Z Data Value, Unscaled - Real
<dd>The parameter 'ZDU' is just like 'ZDV' (which see, below), but the value is unscaled.
<dt>'ZDV' - Z Data Value - Real
<dd>The parameter 'ZDV' is mostly for output. Its value may be retrieved in a user version of CPCHHL to retrieve the value of the high or low which is being labeled. If a character string representing the value is desired, CPGETC may be used to obtain it (as modified by the current scale factor); thus, to obtain the character representation of an arbitrary value in a form consistent with the other values on a contour plot, set 'ZDV' with a call to CPSETR and retrieve the value of 'ZDV' with a call to CPGETC; if an unscaled value is desired, use the parameter name 'ZDU' in the call to CPGETC.
<dt>'ZMN' - Z Minimum Value - Real
<dd>The minimum value in the field, as found by CPRECT, CPSPS1, or CPSPS2. For output only.
<dt>'ZMX' - Z Maximum Value - Real
<dd>The maximum value in the field, as found by CPRECT, CPSPS1, or CPSPS2. For output only.</dl></dl>
</dl><h2>See Also</h2>Online: cpgetc, cpgeti, cpgetr, cprset, cpsetc, cpseti, cpsetr 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

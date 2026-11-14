---
title: "ncl_autograph_params(3)"
name: "ncl_autograph_params"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_autograph_params/"
---

Autograph_params - This document briefly describes all Autograph internal parameters. 

<h2>Description</h2>The Autograph control parameters reside in the labeled common block AGCONP. There are currently 485 of them, of which 336 are &quot;primary&quot; and 149 are &quot;secondary&quot;. Primary control parameters have default values and are subject to change by a user program to produce some desired effect on the behavior of Autograph and/or on the nature of a graph being drawn. Secondary control parameters are computed by Autograph itself and are not normally subject to change by a user program. 

 User access to these parameters is provided by the routines AGGETC, AGGETF, AGGETI, AGGETP, AGGETR, AGSETC, AGSETF, AGSETI, AGSETP, and AGSETR. The first argument in a call to one of these routines is a character string naming a group of parameters (perhaps containing only a single parameter) which the user wishes to &quot;set&quot; or &quot;get&quot;. Each such string has the form 'k1/k2/k3/ . . . kn.', where k1 is a keyword identifying a major group of parameters, k2 is a keyword identifying a subgroup of that major group, k3 is a keyword identifying a further subgroup of that subgroup, and so on. Only the first three characters of k1 and the first two characters of the others need be used; also, certain keywords may be omitted. 

 Because of certain portability considerations, all of the parameters have real values. The routine AGSETP may be used to set the real values of the parameters in any group, and the routine AGGETP to retrieve those values. Either of the routines AGSETF or AGSETR may be used to set the real value of a single parameter and either of the routines AGGETF or AGGETR may be used to get the real value of a single parameter. 

 Some parameters may only take on discrete integral values (like &quot;0.&quot;, &quot;1.&quot;, &quot;-6.&quot;, or &quot;65535.&quot;) and are used in roles for which integers would normally be used. The routine AGSETI may be used to set the integer value of a single parameter of this type and the routine AGGETI may be used to get the integer value of a single parameter of this type. 

 Other parameters intrinsically represent character strings; the real value of the parameter is an identifier, generated when the character string is passed to Autograph and enabling the character string to be retrieved from Autograph's character storage space when it is needed. The routine AGSETC must be used to set the character-string value associated with a single parameter of this type and the routine AGGETC must be used to get the character-string value associated with a single parameter of this type. 

 Many parameters have a limited range of acceptable values. What generally happens when a parameter is given an out-of-range value is that Autograph (usually the routine AGSTUP) resets that value to the value at the nearer end of the acceptable range. 

 Setting certain parameters (individually, rather than as part of a multi-parameter group) implies, as a side effect, &quot;special action&quot; by the routine AGSETP (which may be called directly by the user or indirectly by way of a user call to AGSETC, AGSETF, AGSETI, or AGSETR). For example, setting the parameter 'BACKGROUND.' to request a particular background type causes a number of other parameters to be changed in order to achieve the desired result. 

 Each of the named parameter groups is described below. Square brackets are used to mark portions of a name which may be omitted; the notation 'k1/k2/ . . . [ki/]...kn.' indicates that the keyword ki and the following slash may be omitted. In each description, the simplest form of the name is given. If a multi-parameter group is named, its subgroups are listed, in the order in which they occur in the group. If a single parameter is named, the default value of that parameter is given and any &quot;special action&quot; by AGSETP is described.
<dl COMPACT><dt>'PRIMARY.'
<dd>Simplest form of name: 'PRI.' 

 This group consists of all 336 primary control parameters, in the order in which they appear below. It was originally provided to give users the capability of saving and restoring the state of Autograph. The routines AGSAVE and AGRSTR (which see) should now be used for this purpose.
<dt>'FRAME.'
<dd>Simplest form of name: 'FRA.' 

 An integral real number specifying when a frame advance is to be done by the routines EZY, EZXY, EZMY, and EZMXY and having one of three possible values:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>The value &quot;1.&quot; specifies a frame advance after drawing a graph.
<dt>&bull;
<dd>The value &quot;2.&quot; specifies no frame advance at all.
<dt>&bull;
<dd>The value &quot;3.&quot; specifies a frame advance before drawing a graph.</dl></dl><dd>Default value: &quot;1.&quot; (frame advance after drawing graph).
<dt>'SET.'
<dd>Simplest form of name: 'SET.' 

 An integral real number specifying whether or not the arguments of the last call to &quot;SET&quot; are used to determine the linear/log nature of the current graph, the position of the grid window and/or the X/Y minimum/maximum values. 

 (Note: The routine SET is part of the package called SPPS. Its first four arguments specify a portion of the plotter frame, its next four arguments specify the minimum and maximum X and Y coordinate values to be mapped to that portion, and its ninth argument specifies the linear/log nature of the mapping. The routine GETSET, which is also a part of SPPS, is used to retrieve the arguments of the last call to SET.) 

 Giving 'SET.' a value (individually, rather than as part of a group) has both an immediate effect and a delayed effect. The immediate effect, which occurs in the routine AGSETP, is to return most of the parameters in the groups 'GRID.', 'X.', and 'Y.' to their default values. (Exceptions are 'X/LOGARITHMIC.' and 'Y/LOGARITHMIC.', which may have values making them immune to such resetting.) The delayed effect, which occurs in the routine AGSTUP, depends on the value given to 'SET.'. 

 There are eight acceptable values of 'SET.', four of which are just the negatives of the other four. Using a negated value suppresses the drawing of curves by the routines EZY, EZXY, EZMY, and EZMXY. Acceptable absolute values of 'SET.' are as follows:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>The value &quot;1.&quot; means that the arguments of the last SET call are not to be used by AGSTUP.
<dt>&bull;
<dd>The value &quot;2.&quot; means that, in AGSTUP, 'X/LOGARITHMIC.' and 'Y/LOGARITHMIC.' are to be given values (&quot;0.&quot; or &quot;-1.&quot;) consistent with the ninth argument of the last SET call and that parameters in the group 'GRID.' are to be given values consistent with the first four arguments of the last SET call.
<dt>&bull;
<dd>The value &quot;3.&quot; means that, in AGSTUP, 'X/LOGARITHMIC.' and 'Y/LOGARITHMIC.' are to be given values (&quot;0.&quot; or &quot;-1.&quot;) consistent with the ninth argument of the last SET call and that the other parameters in the groups 'X.' and 'Y.' are to be given values consistent with the fifth through eighth arguments of the last SET call.
<dt>&bull;
<dd>The value &quot;4.&quot; implies a combination of the actions specified by the values &quot;2.&quot; and &quot;3.&quot;.</dl></dl><dd>Default value: &quot;1.&quot; (no arguments of last SET call used). 

 Special action by AGSETP: As described above, if 'SET.' is set (individually, rather than as part of a group) to any value by an AGSETP call, the parameters in the groups 'GRID.', 'X.', and 'Y.' are reset to their default values. The parameter 'X/LOGARITHMIC.' is reset to its default value (&quot;0.&quot;) only if it has the value &quot;+1.&quot;; a value of &quot;-1.&quot; is not changed; 'Y/LOGARITHMIC.' is treated similarly.
<dt>'ROW.'
<dd>Simplest form of name: 'ROW.' 

 An integral real number specifying the assumed dimensioning of X and Y coordinate data arrays used in calls to the routines EZMY and EZMXY. There are four possibilities:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>The value &quot;-2.&quot; means that both X and Y arrays are subscripted by curve number and point number, in that order.
<dt>&bull;
<dd>The value &quot;-1.&quot; means that Y arrays are subscripted by curve number and point number, in that order, but that X arrays are subscripted by point number only. (The same X-coordinate data is used for all the curves.)
<dt>&bull;
<dd>Either of the values &quot;0.&quot; or &quot;1.&quot; means that Y arrays are subscripted by point number and curve number, in that order, but that X arrays are subscripted by point number only. (The same X-coordinate data is used for all of the curves.)
<dt>&bull;
<dd>The value &quot;+2.&quot; means that both X and Y arrays are subscripted by point number and curve number, in that order.</dl></dl><dd>Default value: &quot;1.&quot; (Y by point and curve numbers, X by point number only).
<dt>'INVERT.'
<dd>Simplest form of name: 'INV.' 

 An integral real number having the value &quot;0.&quot; or &quot;1.&quot;; giving it the value &quot;1.&quot; causes the routines AGSTUP and AGCURV to behave as if arguments defining X-coordinate data had been interchanged with arguments defining Y-coordinate data, thus, in some sense, allowing one to graph &quot;X as a function of Y&quot;. This parameter is principally intended for users of the routines EZY, EZXY, EZMY, and EZMXY. 

 Default value: &quot;0.&quot; (no inversion of X and Y arguments).
<dt>'WINDOW.'
<dd>Simplest form of name: 'WIN.' 

 An integral real number having the value &quot;0.&quot; or &quot;1.&quot;; giving it the value &quot;1.&quot; causes the routine AGCURV to use the subroutine AGQURV, rather than AGKURV, for drawing curves. The result is that curve portions falling outside the grid window are omitted. See the AGCURV man page. 

 Default value: &quot;0.&quot; (no windowing of curves).
<dt>'BACKGROUND.'
<dd>Simplest form of name: 'BAC.' 

 An integral real number specifying the type of background to be drawn by AGBACK. There are four acceptable values:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>The value &quot;1.&quot; specifies a &quot;perimeter&quot; background.
<dt>&bull;
<dd>The value &quot;2.&quot; specifies a &quot;grid&quot; background.
<dt>&bull;
<dd>The value &quot;3.&quot; specifies a &quot;half-axis&quot; background.
<dt>&bull;
<dd>The value &quot;4.&quot; specifies no background at all.</dl></dl><dd>Default value: &quot;1.&quot; (a &quot;perimeter&quot; background). 

 Special action by AGSETP: If 'BACKGROUND.' is set (individually, rather than as part of a group) by a call to AGSETP, the desired background is created by changing the following parameters:
<dl COMPACT><dd>'[AXIS/]s/CONTROL.' 
 '[AXIS/]s/[TICKS/]MAJOR/[LENGTH/]INWARD.' 
 '[AXIS/]s/[TICKS/]MINOR/[LENGTH/]INWARD.' 
 'LABEL/CONTROL.'</dl><dd>where &quot;s&quot; stands for &quot;LEFT&quot;, &quot;RIGHT&quot;, &quot;BOTTOM&quot;, and &quot;TOP&quot;. This determines which of the axes are plotted, how long the inward-pointing portions of major and minor tick marks are to be, and whether or not informational labels are to be plotted. Values used are as follows: 

 The value &quot;1.&quot; (perimeter background) sets:
<dl COMPACT><dd>'s/CONTROL.' to &quot;4.&quot; for all s; 
 's/MAJOR/INWARD.' to &quot;.015&quot; for all s; 
 's/MINOR/INWARD.' to &quot;.010&quot; for all s; 
 'LABEL/CONTROL.' to &quot;2.&quot;.</dl><dd>The value &quot;2.&quot; (grid background) sets:
<dl COMPACT><dd>'s/CONTROL.' to &quot;4.&quot; for &quot;s&quot; = &quot;LEFT&quot; and &quot;BOTTOM&quot;, 
 's/CONTROL.' to &quot;-1.&quot; for &quot;s&quot; = &quot;RIGHT&quot; and &quot;TOP&quot;; 
 's/MAJOR/INWARD.' to &quot;1.&quot; for all s; 
 's/MINOR/INWARD.' to &quot;1.&quot; for all s; 
 'LABEL/CONTROL.' to &quot;2.&quot;.</dl><dd>The value &quot;3.&quot; (half-axis background) sets:
<dl COMPACT><dd>'s/CONTROL.' to &quot;4.&quot; for &quot;s&quot; = &quot;LEFT&quot; and &quot;BOTTOM&quot;, 
 's/CONTROL.' to &quot;-1.&quot; for &quot;s&quot; = &quot;RIGHT&quot; and &quot;TOP&quot;; 
 's/MAJOR/INWARD.' to &quot;.015&quot; for all s; 
 's/MINOR/INWARD.' to &quot;.010&quot; for all s; 
 'LABEL/CONTROL.' to &quot;2.&quot;.</dl><dd>The value &quot;4.&quot; (no background) sets:
<dl COMPACT><dd>'s/CONTROL.' to &quot;0.&quot; for all s; 
 's/MAJOR/INWARD.' to &quot;.015 for all s; 
 's/MINOR/INWARD.' to &quot;.010&quot; for all s; 
 'LABEL/CONTROL.' to &quot;0.&quot;.</dl><dd>The default values of these thirteen parameters correspond to the default value of 'BACKGROUND.'. Note that, if they are changed directly, the value of 'BACKGROUND.' may not reflect the actual nature of the background defined by them.
<dt>'NULL.'
<dd>Simplest form of name: 'NUL.' 

 This group contains the two &quot;nulls&quot; (or &quot;special values&quot;) 'NULL/1.' and 'NULL/2.'.
<dt>'NULL/1.'
<dd>Simplest form of name: 'NUL/1.' 

 A real number &quot;null 1&quot;, used in the following ways by Autograph:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>Certain parameters have by default, or may be given, the value &quot;null 1&quot;, specifying that the routine AGSTUP is to choose values for them. The value chosen for a given parameter is not back-stored in place of the &quot;null 1&quot;; thus, a unique value will be chosen for each graph drawn.
<dt>&bull;
<dd>If a curve point specified by the user has X and/or Y coordinates equal to &quot;null 1&quot;, that curve point is ignored. It is not used in computing minimum and maximum values. Curve segments on either side of it are not drawn.</dl></dl><dd>Default value: &quot;1.E36&quot; (an arbitrary value). 

 Special action by AGSETP: If 'NULL/1.' is changed (individually, rather than as part of a group) by an AGSETP call, the entire list of primary parameters is scanned - any value equal to the old &quot;null 1&quot; is replaced by the new one.
<dt>'NULL/2.'
<dd>Simplest form of name: 'NUL/2.' 

 A real number &quot;null 2&quot;. Certain parameters may be given the value &quot;null 2&quot;, specifying that the routine AGSTUP is to choose values for them. The value chosen for a given parameter is back-stored in place of the &quot;null 2&quot;; thus, a unique value may be chosen for the first graph of a series and then used for all remaining graphs in the series. 

 Default value: &quot;2.E36&quot; (an arbitrary value). 

 Special action by AGSETP: If 'NULL/2.' is changed (individually, rather than as part of a group) by an AGSETP call, the entire list of primary parameters is scanned - any value equal to the old &quot;null 2&quot; is replaced by the new one.
<dt>'GRAPH.'
<dd>Simplest form of name: 'GRA.' 

 A group of four parameters describing the position of the &quot;graph window&quot; within the plotter frame. A graph drawn by Autograph (including labels) is forced to lie entirely within this window. Subgroups and the number of parameters in each are as follows:
<dl COMPACT><dd>'GRAPH/LEFT.' (1) 
 'GRAPH/RIGHT.' (1) 
 'GRAPH/BOTTOM.' (1) 
 'GRAPH/TOP.' (1)</dl><dt>'GRAPH/LEFT.'
<dd>Simplest form of name: 'GRA/LE.' 

 A real number between &quot;0.&quot; and &quot;1.&quot; specifying the position of the left edge of the graph window as a fraction of the distance from the left edge to the right edge of the plotter frame. 

 Default value: &quot;0.&quot; (left edge of plotter frame).
<dt>'GRAPH/RIGHT.'
<dd>Simplest form of name: 'GRA/RI.' 

 A real number between &quot;0.&quot; and &quot;1.&quot; specifying the position of the right edge of the graph window as a fraction of the distance from the left edge to the right edge of the plotter frame. 

 Default value: &quot;1.&quot; (right edge of plotter frame).
<dt>'GRAPH/BOTTOM.'
<dd>Simplest form of name: 'GRA/BO.' 

 A real number between &quot;0.&quot; and &quot;1.&quot; specifying the position of the bottom edge of the graph window as a fraction of the distance from the bottom edge to the top edge of the plotter frame. 

 Default value: &quot;0.&quot; (bottom edge of plotter frame).
<dt>'GRAPH/TOP.'
<dd>Simplest form of name: 'GRA/TO.' 

 A real number between &quot;0.&quot; and &quot;1.&quot; specifying the position of the top edge of the graph window as a fraction of the distance from the bottom edge to the top edge of the plotter frame. 

 Default value: &quot;0.&quot; (top edge of plotter frame).
<dt>'GRID.'
<dd>Simplest form of name: 'GRI.' 

 A group of five parameters describing the position and shape of the &quot;grid window&quot; within the graph window. Subgroups and the number of parameters in each are as follows:
<dl COMPACT><dd>'GRID/LEFT.' (1) 
 'GRID/RIGHT.' (1) 
 'GRID/BOTTOM.' (1) 
 'GRID/TOP.' (1) 
 'GRID/SHAPE.' (1)</dl><dt>'GRID/LEFT.'
<dd>Simplest form of name: 'GRI/LE.' 

 A real number between &quot;0.&quot; and &quot;1.&quot; specifying the position of the left edge of the area in which the grid window is to be placed, stated as a fraction of the distance from the left edge to the right edge of the graph window. 

 Default value: &quot;.15&quot;.
<dt>'GRID/RIGHT.'
<dd>Simplest form of name: 'GRI/RI.' 

 A real number between &quot;0.&quot; and &quot;1.&quot; specifying the position of the right edge of the area in which the grid window is to be placed, stated as a fraction of the distance from the left edge to the right edge of the graph window. 

 Default value: &quot;.95&quot;.
<dt>'GRID/BOTTOM.'
<dd>Simplest form of name: 'GRI/BO.' 

 A real number between &quot;0.&quot; and &quot;1.&quot; specifying the position of the bottom edge of the area in which the grid window is to be placed, stated as a fraction of the distance from the bottom edge to the top edge of the graph window. 

 Default value: &quot;.15&quot;.
<dt>'GRID/TOP.'
<dd>Simplest form of name: 'GRI/TO.' 

 A real number between &quot;0.&quot; and &quot;1.&quot; specifying the position of the top edge of the area in which the grid window is to be placed, stated as a fraction of the distance from the bottom edge to the top edge of the graph window. 

 Default value: &quot;.95&quot;.
<dt>'GRID/SHAPE.'
<dd>Simplest form of name: 'GRI/SH.' 

 A real number specifying the shape of the grid window. The grid window, whatever its shape, is centered in, and made as large as possible in, the area specified by the first four parameters in the group 'GRID.'. The value of 'GRID/SHAPE.' falls in one of four possible ranges, as follows:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>A value less than &quot;0.&quot; specifies the negative of the desired ratio of the grid window's width to its height. For example, the value &quot;-2.&quot; specifies a grid window which is twice as wide as it is high.
<dt>&bull;
<dd>The value &quot;0.&quot; specifies a grid window of exactly the same shape as the area specified by the first four parameters in the group 'GRID.'. The grid window therefore fills that area completely.
<dt>&bull;
<dd>A value &quot;s&quot; between &quot;0.&quot; and &quot;1.&quot; specifies a grid window whose shape is determined by the range of the user's coordinate data, reverting to the shape of the area specified by the first four arguments in the group 'GRID.' if the ratio of the shorter side of the grid window to the longer side of the grid window would thereby be made less than &quot;s&quot;. For example, if &quot;s&quot; were given the value &quot;.5&quot; and the user X coordinate data ranged in value from &quot;0.&quot; to &quot;10.&quot; and the user Y coordinate data ranged in value from &quot;0.&quot; to &quot;15.&quot;, the grid window would be made two-thirds as wide as it was high; however, if the Y coordinate data ranged in value from &quot;0.&quot; to &quot;100.&quot;, the grid window would not be made one-tenth as wide as it is high, but would instead be made to fill the entire area specified by the first four arguments of the group 'GRID.'.
<dt>&bull;
<dd>A value &quot;s&quot; greater than or equal to &quot;1.&quot; specifies a grid window whose shape is determined by the range of the user's coordinate data, reverting to a square if the ratio of the longer side of the grid window to the shorter side of the grid window would thereby be made greater than &quot;s&quot;.</dl></dl><dd>Note that, if 'GRID/SHAPE.' is given a value greater than &quot;0.&quot;, Autograph assumes that the user's X and Y coordinate data have the same units (both in inches, for example) and that the outline of a real two-dimensional object is to be graphed without distortion. The grid window is shaped in such a way as to accomplish this. This feature should not be used when either 'X/LOGARITHMIC.' or 'Y/LOGARITHMIC.' has a non-zero value; doing so will yield strange results. 

 Note that either &quot;-1.&quot; or &quot;+1.&quot; produces a square and that &quot;-1.61803398874989&quot; produces a golden rectangle. 

 Default value: &quot;0.&quot;.
<dt>'X.'
<dd>Simplest form of name: 'X.' 

 A group of seven parameters specifying the mapping of the user's X-coordinate data onto the horizontal axis of the grid window. Subgroups and the number of parameters in each are as follows:
<dl COMPACT><dd>'X/MINIMUM.' (1) 
 'X/MAXIMUM.' (1) 
 'X/LOGARITHMIC.' (1) 
 'X/ORDER.' (1) 
 'X/NICE.' (1) 
 'X/SMALLEST.' (1) 
 'X/LARGEST.' (1)</dl><dd>See also 'SET.' and 'INVERT.', above.
<dt>'X/MINIMUM.'
<dd>Simplest form of name: 'X/MI.' 

 A real number specifying the minimum user X coordinate to be considered. This parameter normally has the value &quot;null 1&quot;, specifying that the routine AGSTUP should examine the user's X-coordinate data and find the minimum value for itself. 

 If the value &quot;null 2&quot; is used, it will be replaced, the next time AGSTUP is called, by an actual minimum value computed by AGSTUP. 

 If a non-null value is used, AGSTUP will not examine the user's X-coordinate data; the given value will be considered to be the minimum. 

 If both 'X/MINIMUM.' and 'X/MAXIMUM.' are given non-null values, the former should have a lesser value than the latter. 

 Default value: &quot;1.E36&quot; (&quot;null 1&quot;).
<dt>'X/MAXIMUM.'
<dd>Simplest form of name: 'X/MA.' 

 Analogous to 'X/MINIMUM.', above; it specifies the way in which the maximum X coordinate is to be determined. 

 Default value: &quot;1.E36&quot; (&quot;null 1&quot;).
<dt>'X/LOGARITHMIC.'
<dd>Simplest form of name: 'X/LO.' 

 An integral real number having one of the values &quot;-1.&quot;, &quot;0.&quot;, or &quot;+1.&quot;:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>The value &quot;0.&quot; specifies that the mapping of user X coordinates onto the horizontal axis of the grid window is to be linear.
<dt>&bull;
<dd>The values &quot;-1.&quot; and &quot;+1.&quot; specify that the mapping is to be logarithmic, in which case all user X-coordinate data must be greater than zero.
<dt>&bull;
<dd>The value &quot;-1.&quot; is immune to change when 'SET.' (which see, above) is reset; the value &quot;+1.&quot; is not.</dl></dl><dd>Default value: &quot;0.&quot; (linear X mapping).
<dt>'X/ORDER.'
<dd>Simplest form of name: 'X/OR.' 

 An integral real number having one of the values &quot;0.&quot; or &quot;1.&quot;:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>The value &quot;0.&quot; specifies that the values of user X coordinates mapped to the horizontal axis of the grid window should increase from left to right.
<dt>&bull;
<dd>The value &quot;1.&quot; specifies that user X coordinates should decrease from left to right.</dl></dl><dd>Default value: &quot;0.&quot; (increase from left to right).
<dt>'X/NICE.'
<dd>Simplest form of name: 'X/NI.' 

 An integral real number having one of the values &quot;-1.&quot;, &quot;0.&quot;, or &quot;+1.&quot;:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>The value &quot;-1.&quot; specifies that user X-coordinate data are to be mapped onto the horizontal axis of the grid window in such a way as to force major-tick positions at the endpoints of the bottom X axis.
<dt>&bull;
<dd>The value &quot;+1.&quot; specifies that user X-coordinate data are to be mapped onto the horizontal axis of the grid window in such a way as to force major-tick positions at the endpoints of the top X axis.
<dt>&bull;
<dd>The value &quot;0.&quot; specifies that the X-coordinate data are to be mapped so as to range from the left edge of the grid window to the right edge of the grid window; major-tick positions are not forced at the ends of either X axis.</dl></dl><dd>Default value: &quot;-1.&quot; (bottom axis &quot;nice&quot;).
<dt>'X/SMALLEST.'
<dd>Simplest form of name: 'X/SM.' 

 This parameter comes into play when AGSTUP is called upon to compute the minimum X coordinate (when 'X/MINIMUM.' has a null value); if the value of 'X/SMALLEST.' is non-null, values less than it will not be considered in the computation. 

 Default value: &quot;1.E36&quot; (&quot;null 1&quot;).
<dt>'X/LARGEST.'
<dd>Simplest form of name: 'X/LA.' 

 This parameter comes into play when AGSTUP is called upon to compute the maximum X coordinate (when 'X/MAXIMUM.' has a null value); if the value of 'X/LARGEST.' is non-null, values greater than it will not be considered in the computation. 

 Default value: &quot;1.E36&quot; (&quot;null 1&quot;).
<dt>'Y.'
<dd>Simplest form of name: 'Y.' 

 A group of seven parameters specifying the mapping of the user's Y-coordinate data onto the vertical axis of the grid window. Subgroups and the number of parameters in each are as follows:
<dl COMPACT><dd>'Y/MINIMUM.' (1) 
 'Y/MAXIMUM.' (1) 
 'Y/LOGARITHMIC.' (1) 
 'Y/ORDER.' (1) 
 'Y/NICE.' (1) 
 'Y/SMALLEST.' (1) 
 'Y/LARGEST.' (1)</dl><dd>See also 'SET.' and 'INVERT.', above.
<dt>'Y/MINIMUM.'
<dd>Simplest form of name: 'Y/MI.' 

 Analogous to 'X/MINIMUM.', above; it specifies the way in which the minimum Y coordinate is to be determined. 

 Default value: &quot;1.E36&quot; (&quot;null 1&quot;).
<dt>'Y/MAXIMUM.'
<dd>Simplest form of name: 'Y/MA.' 

 Analogous to 'X/MAXIMUM.', above; it specifies the way in which the maximum Y coordinate is to be determined. 

 Default value: &quot;1.E36&quot; (&quot;null 1&quot;).
<dt>'Y/LOGARITHMIC.'
<dd>Simplest form of name: 'Y/LO.' 

 Analogous to 'X/LOGARITHMIC.', above; it specifies whether the mapping of Y coordinates is linear or logarithmic. 

 Default value: &quot;0.&quot; (linear Y).
<dt>'Y/ORDER.'
<dd>Simplest form of name: 'Y/OR.' 

 Analogous to 'X/ORDER.', above; it specifies whether Y-coordinates increase or decrease from bottom to top. 

 Default value: &quot;0.&quot; (increase from bottom to top).
<dt>'Y/NICE.'
<dd>Simplest form of name: 'Y/NI.' 

 Analogous to 'X/NICE.', above; it specifies whether the left Y axis, the right Y axis, or neither, is to be &quot;nice&quot;. 

 Default value: &quot;-1.&quot; (left axis &quot;nice&quot;).
<dt>'Y/SMALLEST.'
<dd>Simplest form of name: 'Y/SM.' 

 Analogous to 'X/SMALLEST.', above; comes into play when AGSTUP is called upon to compute the minimum Y coordinate. 

 Default value: &quot;1.E36&quot; (&quot;null 1&quot;).
<dt>'Y/LARGEST.'
<dd>Simplest form of name: 'Y/LA.' 

 Analogous to 'X/LARGEST.', above; comes into play when AGSTUP is called upon to compute the maximum Y coordinate. 

 Default value: &quot;1.E36&quot; (&quot;null 1&quot;).
<dt>'AXIS.'
<dd>Simplest form of name: 'AXI.' 

 A group of 92 parameters describing four axes: the left axis, the right axis, the bottom axis, and the top axis. Subgroups and the number of parameters in each are as follows:
<dl COMPACT><dd>'[AXIS/]LEFT.' (23) 
 '[AXIS/]RIGHT.' (23) 
 '[AXIS/]BOTTOM.' (23) 
 '[AXIS/]TOP.' (23)</dl><dd>The elements of the subgroups are interleaved in the group; that is to say, the first elements of the four subgroups constitute elements 1 through 4 of the group, the second elements of the four subgroups constitute elements 5 through 8 of the group, and so on.
<dt>'[AXIS/]s.'
<dd>(where &quot;s&quot; means &quot;any one of the keywords LEFT, RIGHT, BOTTOM, or TOP&quot;.) 

 Simplest form of name: 's.' 

 A group of 23 parameters describing the axis specified by &quot;s&quot;. Subgroups and the number of parameters in each are as follows:
<dl COMPACT><dd>'[AXIS/]s/CONTROL.' (1) 
 '[AXIS/]s/LINE.' (1) 
 '[AXIS/]s/INTERSECTION.' (2) 
 '[AXIS/]s/FUNCTION.' (1) 
 '[AXIS/]s/TICKS.' (10) 
 '[AXIS/]s/NUMERIC.' (8)</dl><dt>'[AXIS/]s/CONTROL.'
<dd>Simplest form of name: 's/CO.' 

 An integral real number having one of the values &quot;-1.&quot;, &quot;0.&quot;, &quot;1.&quot;, &quot;2.&quot;, &quot;3.&quot;, or &quot;4.&quot; and controlling certain aspects of the drawing of the axis specified by &quot;s&quot;, as follows:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>The value &quot;-1.&quot; specifies that only the line portion of the axis may be drawn; tick marks and numeric labels are suppressed.
<dt>&bull;
<dd>The value &quot;0.&quot; specifies that no portion of the axis may be drawn.
<dt>&bull;
<dd>A positive value specifies that all portions of the axis may be drawn and specifies what actions Autograph may take to prevent numeric-label overlap problems, as follows:
<dt>&bull;
<dd>The value &quot;1.&quot; specifies that numeric labels may not be shrunk or rotated.
<dt>&bull;
<dd>The value &quot;2.&quot; specifies that numeric labels may be shrunk, but not rotated.
<dt>&bull;
<dd>The value &quot;3.&quot; specifies that numeric labels may be rotated, but not shrunk.
<dt>&bull;
<dd>The value &quot;4.&quot; specifies that numeric labels may be both shrunk and/or rotated.</dl></dl><dd>Default value: &quot;4.&quot; for all &quot;s&quot; (all axes drawn, numeric labels may be shrunk and/or rotated).
<dt>'[AXIS/]s/LINE.'
<dd>Simplest form of name: 's/LI.' 

 An integral real number having one of the values &quot;0.&quot; or &quot;1.&quot;:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>The value &quot;0.&quot; specifies that the line portion of the axis specified by &quot;s&quot; may be drawn.
<dt>&bull;
<dd>The value &quot;1.&quot; suppresses the line portion of the axis specified by &quot;s&quot;.</dl></dl><dd>Default value: &quot;0.&quot; for all &quot;s&quot; (line portions of all axes may be drawn).
<dt>'[AXIS/]s/INTERSECTION.'
<dd>Simplest form of name: 's/IN.' 

 A group of two parameters
<dl COMPACT><dd>'[AXIS/]s/INTERSECTION/GRID.' 
 '[AXIS/]s/INTERSECTION/USER.'</dl><dd>each having the default value &quot;1.E36&quot; (&quot;null 1&quot;). Giving either of them a non-null value causes the axis specified by &quot;s&quot; to be moved away from its normal position on one edge of the grid window. If both are given non-null values, '.../USER.' takes precedence over '.../GRID.'. 

 If the left Y axis or the right Y axis is moved, it remains vertical, but intersects the bottom of the grid window at a specified X coordinate. Similarly, if the bottom X axis or the top X axis is moved, it remains horizontal, but intersects the left edge of the grid at a specified Y coordinate. 

 No axis may be moved outside the current graph window; if an attempt is made to do so, the axis is moved as far as the edge and no farther.
<dt>'[AXIS/]s/INTERSECTION/GRID.'
<dd>Simplest form of name: 's/IN/GR.' 

 A real number which, if not equal to the current &quot;null 1&quot;, specifies, in the grid coordinate system, the X coordinate (if &quot;s&quot; = &quot;LEFT&quot; or &quot;RIGHT&quot;) or the Y coordinate (if &quot;s&quot; = &quot;BOTTOM&quot; or &quot;TOP&quot;) of the point of intersection of the axis specified by &quot;s&quot; with the perpendicular sides of the grid window. 

 Default value: &quot;1.E36&quot; (&quot;null 1&quot;) for all &quot;s&quot; (axes lie on the edges of the grid window).
<dt>'[AXIS/]s/INTERSECTION/USER.'
<dd>Simplest form of name: 's/IN/US.' 

 A real number which, if not equal to the current &quot;null 1&quot;, specifies, in the user coordinate system, the X coordinate (if &quot;s&quot; = &quot;LEFT&quot; or &quot;RIGHT&quot;) or the Y coordinate (if &quot;s&quot; = &quot;BOTTOM&quot; or &quot;TOP&quot;) of the point of intersection of the axis specified by &quot;s&quot; with the perpendicular sides of the grid window. 

 Default value: &quot;1.E36&quot; (&quot;null 1&quot;) for all &quot;s&quot; (axes lie on the edges of the grid window).
<dt>'[AXIS/]s/FUNCTION.'
<dd>Simplest form of name: 's/FU.' 

 A real number, passed as an argument to the subroutine AGUTOL; this subroutine defines the user-system-to-label-system mappings, and thus the label coordinate systems, for all the axes. The default version of AGUTOL defines the identity mapping for all axes; a user version may be substituted to define any desired set of mappings. It is intended that 'AXIS/s/FUNCTION.' be used within a user version of AGUTOL as a function selector. It is further recommended that the value &quot;0.&quot; select the identity mapping, thus providing a way to re-create the default situation. 

 Tick marks on the axis specified by &quot;s&quot; are positioned in the label coordinate system. Numeric labels on the axis give values in the label coordinate system. 

 See the AGUTOL man page. 

 Default value: &quot;0.&quot; for all &quot;s&quot; (identity mapping for all axes).
<dt>'[AXIS/]s/TICKS.'
<dd>Simplest form of name: 's/TI.' 

 A group of ten parameters describing the tick marks, if any, which are to be a part of the axis specified by &quot;s&quot;. Subgroups and the number of parameters in each are as follows:
<dl COMPACT><dd>'[AXIS/]s/[TICKS/]MAJOR.' (6) 
 '[AXIS/]s/[TICKS/]MINOR.' (4)</dl><dt>'[AXIS/]s/[TICKS/]MAJOR.'
<dd>Simplest form of name: 's/MA.' 

 A group of six parameters describing the major tick marks, if any, which are to be a part of the axis specified by &quot;s&quot;. Subgroups and the number of parameters in each are as follows:
<dl COMPACT><dd>'[AXIS/]s/[TICKS/]MAJOR/SPACING.' (3) 
 '[AXIS/]s/[TICKS/]MAJOR/PATTERN.' (1) 
 '[AXIS/]s/[TICKS/]MAJOR/LENGTH.' (2)</dl><dt>'[AXIS/]s/[TICKS/]MAJOR/SPACING.'
<dd>Simplest form of name: 's/MA/SP.' 

 A group of three parameters describing the way in which major tick marks, if any, are to be spaced along the axis specified by &quot;s&quot;. Subgroups and the number of parameters in each are as follows:
<dl COMPACT><dd>'[AXIS/]s/[TICKS/]MAJOR/[SPACING/]TYPE.' (1) 
 '[AXIS/]s/[TICKS/]MAJOR/[SPACING/]BASE.' (1) 
 '[AXIS/]s/[TICKS/]MAJOR/[SPACING/]COUNT.' (1)</dl><dt>'[AXIS/]s/[TICKS/]MAJOR/[SPACING/]TYPE.'
<dd>Simplest form of name: 's/MA/TY.' 

 A real number specifying where major tick marks are to be placed along the axis specified by &quot;s&quot; (that is to say, at what values in the label coordinate system along that axis). Let &quot;b&quot; represent the value of the parameter '.../BASE.' (described next) and &quot;k&quot; represent an arbitrary integer. Then, there are six acceptable values of '.../TYPE.':
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>The value &quot;0.&quot; specifies that no major tick marks are to be drawn on the axis.
<dt>&bull;
<dd>The value &quot;1.&quot; specifies major tick marks at values of the form plus or minus b times k.
<dt>&bull;
<dd>The value &quot;2.&quot; specifies major tick marks at values of the form plus or minus b times 10 to the power k.
<dt>&bull;
<dd>The value &quot;3.&quot; specifies major tick marks at values of the form plus or minus b to the power k.
<dt>&bull;
<dd>The value &quot;null 1&quot; specifies that Autograph should use a value &quot;1.&quot;, &quot;2.&quot;, or &quot;3.&quot; - whichever it considers best.
<dt>&bull;
<dd>The value &quot;null 2&quot; specifies that Autograph should use a value &quot;1.&quot;, &quot;2.&quot;, or &quot;3.&quot; - whichever it considers best - and replace the &quot;null 2&quot; by that value.</dl></dl><dd>Notice that major tick marks on a linear axis may be spaced logarithmically and that major tick marks on a logarithmic axis may be spaced linearly; this is sometimes useful. 

 Default value: &quot;1.E36&quot; (&quot;null 1&quot;) for all &quot;s&quot; (Autograph spaces major tick marks as it sees fit).
<dt>'[AXIS/]s/[TICKS/]MAJOR/[SPACING/]BASE.'
<dd>Simplest form of name: 's/MA/BA.' 

 A real number which, if greater than zero and non-null, specifies the base value (&quot;b&quot;, in the preceding parameter description) used in spacing major tick marks in the label coordinate system along the axis specified by &quot;s&quot;. A negative or zero value suppresses major tick marks on the axis. A null value causes Autograph to pick an appropriate base value and, if the null was a &quot;null 2&quot;, to backstore that value in place of the &quot;null 2&quot;. 

 Default value: &quot;1.E36&quot; (&quot;null 1&quot;) for all &quot;s&quot; (Autograph picks the base values).
<dt>'[AXIS/]s/[TICKS/]MAJOR/[SPACING/]COUNT.'
<dd>Simplest form of name: 's/MA/CO.' 

 A real number, having an integral value &quot;n&quot; greater than or equal to 0. A negative value is treated as if it were a zero. The value n is only used when major tick marks are to be spaced linearly and the base value (&quot;b&quot;, in the preceding parameter descriptions) is to be chosen by Autograph. In this case, n is a rough estimate of the minimum number of major tick marks to be placed on the axis specified by &quot;s&quot;. The actual number used may vary between &quot;n+2&quot; and &quot;5n/2+4&quot; (approximately). 

 Default value: &quot;6.&quot; for all &quot;s&quot; (somewhere between 8 and 19 major tick marks per linear axis).
<dt>'[AXIS/]s/[TICKS/]MAJOR/PATTERN.'
<dd>Simplest form of name: 's/MA/PA.' 

 A real number specifying the dashed-line pattern to be used for major tick marks on the axis specified by &quot;s&quot;. Normally, its integer equivalent is a 16-bit integer in which &quot;0&quot; bits specify &quot;pen-up&quot; segments (gaps) 3 plotter units long and &quot;1&quot; bits specify &quot;pen-down&quot; segments (solids) 3 plotter units long. The value &quot;0.&quot; turns off the major tick marks, the value &quot;65535.&quot; (decimal) = &quot;177777.&quot; (octal) makes them solid lines. If the value &quot;null 1&quot; is used, the next call to AGSTUP resets it to &quot;65535.&quot; (decimal). 

 Default value: &quot;1.E36&quot; (&quot;null 1&quot;) for all &quot;s&quot; (solid-line patterns).
<dt>'[AXIS/]s/[TICKS/]MAJOR/LENGTH.'
<dd>Simplest form of name: 's/MA/LE.' 

 A group of two parameters determining the length of the outward-pointing and inward-pointing portions of the major tick marks on the axis specified by &quot;s&quot;. Subgroups and the number of parameters in each are as follows:
<dl COMPACT><dd>'[AXIS/]s/[TICKS/]MAJOR/[LENGTH/]OUTWARD.' (1) 
 '[AXIS/]s/[TICKS/]MAJOR/[LENGTH/]INWARD.' (1)</dl><dt>'[AXIS/]s/[TICKS/]MAJOR/[LENGTH/]OUTWARD.'
<dd>Simplest form of name: 's/MA/OU.' 

 A real number specifying the length of the outward-pointing portion of each major tick mark on the axis specified by &quot;s&quot;. The value must be of the form &quot;e&quot;, &quot;1.+e&quot;, or &quot;-e&quot;, where &quot;e&quot; is greater than or equal to &quot;0.&quot; and less than &quot;1.&quot; and represents a fraction of the smaller dimension of the grid window. 

 Note: &quot;Outward&quot; is defined relative to the normal position of the axis &quot;s&quot;, even when that axis has been moved away from its normal position.
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>When a value &quot;e&quot; is used, each major tick mark extends outward &quot;e&quot; units from the axis.
<dt>&bull;
<dd>When a value &quot;1.+e&quot; is used, each major tick mark extends outward to the farther edge of the grid window and then &quot;e&quot; units beyond that edge. (If the axis is not moved away from its normal position, &quot;1.+e&quot; has the same effect as &quot;e&quot;.)
<dt>&bull;
<dd>When a value &quot;-e&quot; is used, the first &quot;e&quot; units of the inward-pointing portion of each major tick mark are erased. (This can be used to create off-axis major tick marks - for whatever that may be worth.)</dl></dl><dd>Default value: &quot;0.&quot; for all &quot;s&quot; (all major ticks point inward).
<dt>'[AXIS/]s/[TICKS/]MAJOR/[LENGTH/]INWARD.'
<dd>Simplest form of name: 's/MA/IN.' 

 A real number specifying the length of the inward-pointing portion of each tick mark on the axis specified by &quot;s&quot;. The value must be of the form &quot;e&quot;, &quot;1.+e&quot;, or &quot;-e&quot;, where e is greater than or equal to &quot;0.&quot; and less than &quot;1.&quot; and represents a fraction of the smaller dimension of the grid window. 

 Note: &quot;Inward&quot; is defined relative to the normal position of the axis &quot;s&quot;, even when that axis has been moved away from its normal position.
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>When a value &quot;e&quot; is used, each major tick mark extends inward &quot;e&quot; units from the axis.
<dt>&bull;
<dd>When a value &quot;1.+e&quot; is used, each major tick mark extends inward to the farther edge of the grid window and then &quot;e&quot; units beyond that edge. This feature is used to create grid backgrounds.
<dt>&bull;
<dd>When a value &quot;-e&quot; is used, the first &quot;e&quot; units of the outward-pointing portion of each major tick mark are erased.</dl></dl><dd>Default value: &quot;.015&quot; for all &quot;s&quot; (all major ticks point inward).
<dt>'[AXIS/]s/[TICKS/]MINOR.'
<dd>Simplest form of name: 's/MI.' 

 A group of four parameters describing the minor tick marks, if any, which are to be a part of the axis specified by &quot;s&quot;. Subgroups and the number of parameters in each are as follows:
<dl COMPACT><dd>'[AXIS/]s/[TICKS/]MINOR/SPACING.' (1) 
 '[AXIS/]s/[TICKS/]MINOR/PATTERN.' (1) 
 '[AXIS/]s/[TICKS/]MINOR/LENGTH.' (2)</dl><dt>'[AXIS/]s/[TICKS/]MINOR/SPACING.'
<dd>Simplest form of name: 's/MI/SP.' 

 A real number specifying the desired number of minor tick marks to be distributed between each pair of major tick marks on the axis specified by &quot;s&quot;. Acceptable values are as follows:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>A value less than &quot;1.&quot; suppresses minor tick marks completely.
<dt>&bull;
<dd>A value greater than or equal to &quot;1.&quot; which is non-null should be integral; it specifies the number of minor tick marks directly.
<dt>&bull;
<dd>The values &quot;null 1&quot; and &quot;null 2&quot; specify that Autograph is to choose a reasonable integral value; if a &quot;null 2&quot; is specified, it is replaced by the integral value chosen.</dl></dl><dd>The minor tick marks, if any, are spaced linearly in the label coordinate system along the axis specified by &quot;s&quot;. Note that the appropriate value for the usual sort of logarithmic axis is &quot;8.&quot;; this causes the minor tick marks between two major tick marks at label-system values 10**n and 10**n+1 to be placed at the label-system values 2*10**n, 3*10**n, 4*10**n, . . ., 9*10**n. 

 Default value: &quot;1.E36&quot; (&quot;null 1&quot;) for all &quot;s&quot; (Autograph chooses appropriate values).
<dt>'[AXIS/]s/[TICKS/]MINOR/PATTERN.'
<dd>Simplest form of name: 's/MI/PA.' 

 A real number specifying the dashed-line pattern to be used for minor tick marks on the axis specified by &quot;s&quot;; analogous to '[AXIS/]s/[TICKS/]MAJOR/PATTERN.', described above. 

 Default value: &quot;1.E36&quot; (&quot;null 1&quot;) for all &quot;s&quot; (solid-line patterns).
<dt>'[AXIS/]s/[TICKS/]MINOR/LENGTH.'
<dd>Simplest form of name: 's/MI/LE.' 

 A group of two parameters determining the length of the outward-pointing and inward-pointing portions of the minor tick marks on the axis specified by &quot;s&quot;. Subgroups and the number of parameters in each are as follows:
<dl COMPACT><dd>'[AXIS/]s/[TICKS/]MINOR/[LENGTH/]OUTWARD.' (1) 
 '[AXIS/]s/[TICKS/]MINOR/[LENGTH/]INWARD.' (1)</dl><dt>'[AXIS/]s/[TICKS/]MINOR/[LENGTH/]OUTWARD.'
<dd>Simplest form of name: 's/MI/OU.' 

 A real number specifying the length of the outward-pointing portion of each minor tick mark on the axis specified by &quot;s&quot;; analogous to '...MAJOR/[LENGTH/]OUTWARD.', described above. 

 Default value: &quot;0.&quot; for all &quot;s&quot; (all minor ticks point inward).
<dt>'[AXIS/]s/[TICKS/]MINOR/[LENGTH/]INWARD.'
<dd>Simplest form of name: 's/MI/IN.' 

 A real number specifying the length of the inward-pointing portion of each minor tick mark on the axis specified by &quot;s&quot;; analogous to '...MAJOR/[LENGTH/]INWARD.', described above. 

 Default value: &quot;.010&quot; for all &quot;s&quot; (all minor ticks point inward).
<dt>'[AXIS/]s/NUMERIC.'
<dd>Simplest form of name: 's/NU.' 

 A group of eight parameters describing the numeric labels, if any, which are to be a part of the axis specified by &quot;s&quot;. Subgroups and the number of parameters in each are as follows:
<dl COMPACT><dd>'[AXIS/]s/[NUMERIC/]TYPE.' (1) 
 '[AXIS/]s/[NUMERIC/]EXPONENT.' (1) 
 '[AXIS/]s/[NUMERIC/]FRACTION.' (1) 
 '[AXIS/]s/[NUMERIC/]ANGLE.' (2) 
 '[AXIS/]s/[NUMERIC/]OFFSET.' (1) 
 '[AXIS/]s/[NUMERIC/]WIDTH.' (2)</dl><dt>'[AXIS/]s/[NUMERIC/]TYPE.'
<dd>Simplest form of name: 's/TY.' 

 The three parameters
<dl COMPACT><dd>'[AXIS/]s/[NUMERIC/]TYPE.' 
 '[AXIS/]s/[NUMERIC/]EXPONENT.' 
 '[AXIS/]s/[NUMERIC/]FRACTION.'</dl><dd>will be described together, because they are so closely interdependent. They specify the type of numeric labels to be used (at major-tick positions) on the axis specified by &quot;s&quot;. A fourth parameter,
<dl COMPACT><dd>'[AXIS/]s/[TICKS/]MAJOR/[SPACING/]TYPE.',</dl><dd>described above, also affects the type of numeric labels to be used. I shall refer to these four parameters in the ensuing discussion using short forms of their names ('s/ TYPE.', 's/EXPO.', 's/FRAC.', and 's/MAJOR/TYPE.', respectively). 

 All four have the default value &quot;null 1&quot; (except for the first, which has the default value &quot;0.&quot; for &quot;s&quot; = &quot;RIGHT&quot; and &quot;TOP&quot;), leaving Autograph free to choose values which are consistent with each other and with other parameters describing the axis specified by &quot;s&quot;. Any one or more of them may be given the value &quot;null 2&quot; (in which case an actual value chosen by Autograph is backstored over the &quot;null 2&quot;) or an actual integral real value. 

 Setting 's/TYPE.' to &quot;0.&quot;: 

 This turns off the numeric labels on the axis specified by &quot;s&quot;. The other three parameters are then ignored. 

 Setting 's/TYPE.' to &quot;1.&quot;: 

 This selects &quot;scientific&quot; notation. Each numeric label is written in the form
<dl COMPACT><dd>[-] [i] [.] [f] x 10 e</dl><dd>where brackets enclose portions which may be independently present or absent and &quot;e&quot; is a superscript exponent. 

 The parameter 's/EXPO.' specifies the length of &quot;i&quot; (the number of characters), thus also specifying the value of the exponent &quot;e&quot;. If 's/EXPO.' has a value less than or equal to zero, &quot;i&quot; is omitted. If 's/EXPO.' is less than zero and has the integral absolute value &quot;n&quot;, the fraction &quot;f&quot; is forced to have &quot;n&quot; leading zeroes. 

 The parameter 's/FRAC.' specifies the length of &quot;f&quot; (the number of characters). If 's/FRAC.' is less than or equal to zero, &quot;f&quot; is omitted. If 's/FRAC.' is less than zero, the decimal point is omitted. 

 If &quot;[i] [.] [f]&quot; has the value &quot;1.&quot;, the first part of the label is omitted, leaving only &quot;10 e&quot;. 

 If the entire label has the value &quot;0.&quot;, the single character &quot;0&quot; is used. 

 The value of 's/MAJOR/TYPE.' is immaterial. 

 Setting 's/TYPE.' to &quot;2.&quot;: 

 This selects &quot;exponential&quot; notation, the exact nature of which depends on the value of 's/MAJOR/TYPE.', as follows:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>If 's/MAJOR/TYPE.' has the value &quot;1.&quot; (all major ticks at values of the form plus or minus b times k), each numeric label is written in the form 

 
[-]&nbsp;<wbr>[i]&nbsp;<wbr>[.]&nbsp;<wbr>[f]&nbsp;<wbr>x 10 e 

 where brackets enclose portions which may be independently present or absent and &quot;e&quot; is a superscript exponent. 

 The parameter 's/EXPO.' specifies the integral value of the exponent &quot;e&quot;. 

 The parameter 's/FRAC.' specifies the length of &quot;f&quot; (the number of characters). If 's/FRAC.' is less than or equal to zero, f is omitted. If 's/FRAC.' is less than zero, the decimal point is omitted. 

 If the label value is exactly zero, the single character &quot;0&quot; is used.
<dt>&bull;
<dd>If 's/MAJOR/TYPE.' has the value &quot;2.&quot; (all major ticks at values of the form plus or minus b times 10 to the power k), each numeric label is written in the form 

 
[-]&nbsp;<wbr>[i]&nbsp;<wbr>[.]&nbsp;<wbr>[f]&nbsp;<wbr>x 10 e 

 where brackets enclose portions which may be independently present or absent and &quot;e&quot; is a superscript exponent. 

 The parameter 's/EXPO.' specifies the integral value of the exponent &quot;e&quot; when &quot;k&quot; equals &quot;0.&quot; The value of &quot;e&quot; is 's/EXPO.' plus &quot;k&quot;. 

 The parameter 's/FRAC.' specifies the length of &quot;f&quot; (the number of characters). If 's/FRAC.' is less than or equal to zero, &quot;f&quot; is omitted. If 's/FRAC.' is less than zero, the decimal point is omitted. 

 If the label value is exactly zero, the single character &quot;0&quot; is used.
<dt>&bull;
<dd>If 's/MAJOR/TYPE.' has the value &quot;3.&quot; (all major ticks at values of the form plus or minus b to the power k), each numeric label is written in the form 

 
[-]&nbsp;<wbr>[i]&nbsp;<wbr>[.]&nbsp;<wbr>[f]&nbsp;<wbr>e 

 where brackets enclose portions which may be independently present or absent and &quot;e&quot; is a superscript exponent. 

 The parameter 's/EXPO.' is ignored. The value of &quot;e&quot; is &quot;k&quot;. 

 The parameter 's/FRAC.' specifies the length of &quot;f&quot; (the number of characters). If 's/FRAC.' is less than or equal to zero, &quot;f&quot; is omitted. If 's/FRAC.' is less than zero, the decimal point is omitted. 

 Note that &quot;[i] [.] [f]&quot; expresses the value of &quot;b&quot;.</dl></dl><dd>Setting 's/TYPE.' to &quot;3.&quot;: 

 This selects &quot;no-exponent&quot; notation, the exact nature of which depends on the value of 's/MAJOR/TYPE.', as follows:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>If 's/MAJOR/TYPE.' has the value &quot;1.&quot; (all major ticks at values of the form plus or minus b times k), each numeric label is written in the form 

 
[-]&nbsp;<wbr>[i]&nbsp;<wbr>[.]&nbsp;<wbr>[f] 

 where brackets enclose portions which may be independently present or absent. 

 The parameter 's/EXPO.' is ignored. 

 The parameter 's/FRAC.' specifies the length of &quot;f&quot; (the number of characters). If 's/FRAC.' is less than or equal to zero, &quot;f&quot; is omitted. If 's/FRAC.' is less than zero, the decimal point is omitted. 

 If the label value is exactly zero, the single character &quot;0&quot; is used.
<dt>&bull;
<dd>If 's/MAJOR/TYPE.' has the value &quot;2.&quot; (all major ticks at values of the form plus or minus b times 10 to the power k), each numeric label is written in the form 

 
[-]&nbsp;<wbr>[i]&nbsp;<wbr>[.]&nbsp;<wbr>[f] 

 where brackets enclose portions which may be independently present or absent. 

 The parameter 's/EXPO.' is ignored. 

 The length of &quot;f&quot; (the number of characters) is specified by the function 

 
MAX('s/FRAC.',0)&nbsp;<wbr>- k 

 if this quantity is greater than zero, and 

 
MIN('s/FRAC.',0) 

 otherwise. This may appear somewhat formidable, but it produces a simple, desirable result. Suppose, for example, that 's/FRAC.' = &quot;1.&quot;, &quot;b&quot; = &quot;3.6&quot;, and &quot;k&quot; ranges from &quot;-3&quot; to &quot;+3&quot;; the labels produced are 

 .0036, .036, .36, 3.6, 36., 360., and 3600. 

 The parameter 's/FRAC.' may be viewed as specifying the length of &quot;f&quot; when &quot;k&quot; is zero. If the function value is less than or equal to zero, &quot;f&quot; is omitted; if it is less than zero, the decimal point is omitted.
<dt>&bull;
<dd>If 's/MAJOR/TYPE.' has the value &quot;3.&quot; (all major ticks at values of the form plus or minus b to the power k), each numeric label is written in the form 

 
[-]&nbsp;<wbr>[i]&nbsp;<wbr>[.]&nbsp;<wbr>[f] 

 if &quot;k&quot; is greater than or equal to zero, and in the form 

 
[-]&nbsp;<wbr>1/&nbsp;<wbr>[i]&nbsp;<wbr>[.]&nbsp;<wbr>[f] 

 if &quot;k&quot; is less than zero. Brackets enclose portions which may be independently present or absent. 

 The parameter 's/EXPO.' is ignored. 

 The length of &quot;f&quot; (the number of characters) is specified by the function 

 
's/FRAC.'&nbsp;<wbr>*&nbsp;<wbr>ABS(k) 

 if &quot;k&quot; is non-zero, or 

 
MIN('s/FRAC.',0) 

 if &quot;k&quot; is zero. Again, this function produces a simple result. Suppose that 's/FRAC.' = &quot;1.&quot;, &quot;b&quot; = &quot;1.1&quot;, and &quot;k&quot; ranges from &quot;-3&quot; to &quot;+3&quot;; the labels produced are 

 1/1.331, 1/1.21, 1/1.1, 1., 1.1, 1.21, and 1.331 

 The parameter 's/FRAC.' may be viewed as specifying the length of &quot;f&quot; when &quot;k&quot; is equal to 1. If the function value is less than or equal to zero, &quot;f&quot; is omitted; if it is less than zero, the decimal point is omitted. 

 Another example: Suppose 's/FRAC.' = &quot;-1.&quot;, &quot;b&quot; = &quot;2.&quot;, and &quot;k&quot; ranges from &quot;-4&quot; to &quot;+4&quot;; the labels produced are 

 1/16, 1/8, 1/4, 1/2, 1, 2, 4, 8, and 16 

 Default value: &quot;1.E36&quot; (&quot;null 1&quot;) for all three for all &quot;s&quot; (Autograph chooses values to use), except for 

 'RIGHT/[NUMERIC/]TYPE.' and 
 'TOP/[NUMERIC/]TYPE.', 

 which are zeroed to suppress the numeric labels on the right and top axes.</dl></dl><dt>'[AXIS/]s/[NUMERIC/]EXPONENT.'
<dd>Simplest form of name: 's/EX.' 

 See the discussion of '[AXIS/]s/[NUMERIC/]TYPE.', above.
<dt>'[AXIS/]s/[NUMERIC/]FRACTION.'
<dd>Simplest form of name: 's/FR.' 

 See the discussion of '[AXIS/]s/[NUMERIC/]TYPE.', above.
<dt>'[AXIS/]s/[NUMERIC/]ANGLE.'
<dd>Simplest form of name: 's/AN.' 

 A group of two integral real numbers specifying the orientation angle of numeric labels on the axis specified by &quot;s&quot;. Subgroups and the number of parameters in each are as follows:
<dl COMPACT><dd>'[AXIS/]s/[NUMERIC/]ANGLE/1ST.' (1) 
 '[AXIS/]s/[NUMERIC/]ANGLE/2ND.' (1)</dl><dt>'[AXIS/]s/[NUMERIC/]ANGLE/1ST.'
<dd>Simplest form of name: 's/AN/1S.' 

 An integral real number having one of the values &quot;0.&quot;, &quot;90.&quot;, &quot;180.&quot;, or &quot;270.&quot; (plus or minus a small multiple of &quot;360.&quot;), specifying the user's first choice for the orientation angle of numeric labels on the axis specified by &quot;s&quot;. The value is stated in degrees counter-clockwise from a left-to-right horizontal vector. 

 The routine AGSTUP decides whether the first choice or the second choice is to be used. The second choice is used only when the first choice leads to overlap problems and the current value of '[AXIS/]s/CONTROL.' is a &quot;3.&quot; or a &quot;4.&quot; and the second choice works out better than the first. If AGSTUP decides to use the first choice, it leaves the first-choice parameter with a positive value; if it decides to use the second choice, it leaves the first-choice parameter with a negative value. Values are made positive or negative by adding and subtracting multiples of &quot;360.&quot;. 

 Default value: &quot;0.&quot; for all &quot;s&quot; (horizontal labels preferred on all axes).
<dt>'[AXIS/]s/[NUMERIC/]ANGLE/2ND.'
<dd>Simplest form of name: 's/AN/2N.' 

 An integral real number having one of the values &quot;0.&quot;, &quot;90.&quot;, &quot;180.&quot;, or &quot;270.&quot; (plus or minus a small multiple of &quot;360.&quot;), specifying the user's second choice for the orientation angle of numeric labels on the axis specified by &quot;s&quot;. The value is stated in degrees counter-clockwise from a left-to-right horizontal vector. See the description of the preceding parameter. 

 Default value: &quot;90.&quot; for all &quot;s&quot; (vertical labels, readable from the right, on all axes).
<dt>'[AXIS/]s/[NUMERIC/]OFFSET.'
<dd>Simplest form of name: 's/OF.' 

 A real number specifying the desired position of numeric labels relative to the axis specified by &quot;s&quot;. 

 If the value is positive, numeric labels are to be placed toward the outside of the grid. If the value is negative, numeric labels are to be placed toward the inside of the grid. In either of these two cases, the magnitude of the value specifies the distance from the line portion of the axis to the nearest part of any numeric label, stated as a fraction of the smaller dimension of the grid window. Note: &quot;Inside&quot; and &quot;outside&quot; are defined relative to the normal position of the axis &quot;s&quot;, even when that axis has been moved away from its normal position. 

 If the value is exactly zero, each numeric label is centered on the axis. In this case, the line portion of the axis is suppressed and major and minor tick marks are moved outward so as not to overlap the numeric labels. 

 Default value: &quot;.015&quot; for all &quot;s&quot; (all labels outside the grid).
<dt>'[AXIS/]s/[NUMERIC/]WIDTH.'
<dd>Simplest form of name: 's/WI.' 

 A group of two real parameters specifying the widths of characters to be used in numeric labels on the axis specified by &quot;s&quot;. Subgroups and the number of parameters in each are as follows:
<dl COMPACT><dd>'[AXIS/]s/[NUMERIC/]WIDTH/MANTISSA.' (1) 
 '[AXIS/]s/[NUMERIC/]WIDTH/EXPONENT.' (1)</dl><dt>'[AXIS/]s/[NUMERIC/]WIDTH/MANTISSA.'
<dd>Simplest form of name: 's/WI/MA.' 

 A real number specifying the width of characters to be used in the &quot;mantissa&quot; of each numeric label on the axis specified by &quot;s&quot;, expressed as a fraction of the smaller dimension of the grid window. 

 Default value: &quot;.015&quot; for all &quot;s&quot;.
<dt>'[AXIS/]s/[NUMERIC/]WIDTH/EXPONENT.'
<dd>Simplest form of name: 's/WI/EX.' 

 A real number specifying the width of characters to be used in the exponent of each numeric label on the axis specified by &quot;s&quot;, expressed as a fraction of the smaller dimension of the grid window. 

 Default value: &quot;.010&quot; for all &quot;s&quot;.
<dt>'DASH.'
<dd>Simplest form of name: 'DAS.' 

 A group of thirty parameters, the first of which determines what dashed-line patterns are to be used by the routines EZMY and EZMXY and the rest of which describe the &quot;user&quot; set of dashed-line patterns (as opposed to the &quot;alphabetic&quot; set, which is defined by code in the subroutine AGCURV and is not subject to change by the user). Subgroups and the number of parameters in each are as follows:
<dl COMPACT><dd>'DASH/SELECTOR.' (1) 
 'DASH/LENGTH.' (1) 
 'DASH/CHARACTER.' (1) 
 'DASH/DOLLAR-QUOTE.' (1) 
 'DASH/PATTERNS.' (26)</dl><dt>'DASH/SELECTOR.'
<dd>Simplest form of name: 'DAS/SE.' 

 The parameter 'DASH/SELECTOR.' is given a negative integral value to specify that the routines EZMY and EZMXY should use the &quot;alphabetic&quot; set of 26 dashed-line patterns for the curves they draw and a positive integral value &quot;n&quot;, less than or equal to 26, to specify that EZMY and EZMXY should use the first &quot;n&quot; patterns in the &quot;user&quot; set of dashed-line patterns, as defined by the current values of the remaining parameters in the group 'DASH.'. 

 Each of the patterns in the &quot;alphabetic&quot; set specifies a solid line interrupted periodically by a letter of the alphabet. Each of the patterns in the &quot;user&quot; set is as defined by the user. The default &quot;user&quot; set produces all solid lines. 

 The routines EZY and EZXY, which draw but one curve per call, always use the first of the patterns in the &quot;user&quot; set; they are unaffected by the value of 'DASH/SELECTOR.'. 

 The selected pattern set is used in a circular fashion. For example, if 'DASH/SELECTOR.' has the value &quot;3.&quot; and EZMY is used to draw nine curves, pattern 1 is used for curves 1, 4, and 7, pattern 2 for curves 2, 5, and 8, and pattern 3 for curves 3, 6, and 9. 

 Default value: &quot;+1.&quot; (The first element of the &quot;user&quot; set of dashed-line patterns is to be used by EZMY and EZMXY.)
<dt>'DASH/LENGTH.'
<dd>Simplest form of name: 'DAS/LE.' 

 An integral real number specifying how long character-string dashed-line patterns are expected to be. In a user call to ANOTAT with a positive fifth argument (implying that the sixth argument is an array of character-string dashed-line patterns) or in a user call to AGSETC setting 'DASH/PATTERN/n.' (in which case the second argument is such a pattern), the specified character strings must be of the length specified by the current value of 'DASH/LENGTH.'. 

 Default value: &quot;8.&quot; (dashed-line patterns are expected to be eight characters long).
<dt>'DASH/CHARACTER.'
<dd>Simplest form of name: 'DAS/CH.' 

 A real number specifying the width of each character (other than a dollar sign or a quote) which is drawn along a curve as directed by a character-string dashed-line pattern (whether from the &quot;alphabetic&quot; set or from the &quot;user&quot; set). This width is expressed as a fraction of the smaller dimension of the grid window. 

 Default value: &quot;.010&quot;
<dt>'DASH/DOLLAR-QUOTE.'
<dd>Simplest form of name: 'DAS/DO.' 

 A real number specifying the line length corresponding to a dollar sign (solid) or a quote (gap) in a character-string dashed-line pattern, expressed as a fraction of the smaller dimension of the grid window. 

 Default value: &quot;.010&quot;
<dt>'DASH/PATTERNS.'
<dd>Simplest form of name: 'DAS/PA.' 

 A group of 26 parameters defining the &quot;user&quot; set of dashed-line patterns. Subgroups and the number of parameters in each are as follows:
<dl COMPACT><dd>'DASH/PATTERNS/1.' (1) 
 'DASH/PATTERNS/2.' (1) 
 
&nbsp;<wbr>. 
 
&nbsp;<wbr>. 
 
&nbsp;<wbr>. 
 'DASH/PATTERNS/26.' (1)</dl><dt>'DASH/PATTERNS/n.'
<dd>Simplest form of name: 'DAS/PA/n.' 

 (The symbol &quot;n&quot; represents an integer between &quot;1&quot; and &quot;26&quot;, inclusive.) An integral real number defining the &quot;n&quot;th dashed-line pattern in the &quot;user&quot; set. 

 If the value is positive, it must be between &quot;0.&quot; and &quot;65535.&quot;, inclusive, and is interpreted as a 16-bit binary pattern in which each &quot;0&quot; bit specifies a &quot;pen-up&quot; gap segment 3 plotter units long and each &quot;1&quot; bit specifies a &quot;pen-down&quot; solid segment 3 plotter units long. Such a pattern may be defined by a user call to AGSETF, AGSETI, or AGSETR. 

 If the value is negative, it serves as an identifier, allowing Autograph to retrieve, from its character storage space, a character string in which each single quote specifies a &quot;pen-up&quot; gap segment, each dollar sign specifies a &quot;pen-down&quot; solid segment, and each other character is simply to be drawn as a part of the line. Such a pattern may be defined by a user call to AGSETC. 

 Note that the function &quot;AGDSHN&quot; allows a user to easily generate the name of the &quot;n&quot;th dash pattern. 

 Default values: &quot;65535.&quot; for all &quot;n&quot; (solid lines).
<dt>'LABEL.'
<dd>Simplest form of name: 'LAB.' 

 A group of 3+10n parameters, where &quot;n&quot; is the current value of 'LABEL/BUFFER/LENGTH.' (8, by default) describing up to &quot;n&quot; informational labels. These labels are a part of the background drawn by a call to the routine AGBACK. Subgroups and the number of parameters in each are as follows:
<dl COMPACT><dd>'LABEL/CONTROL.' (1) 
 'LABEL/BUFFER/LENGTH.' (1) 
 'LABEL/BUFFER/CONTENTS.' (10n) 
 'LABEL/NAME.' (1)</dl><dt>'LABEL/CONTROL.'
<dd>Simplest form of name: 'LAB/CO.' 

 An integral real number having the value &quot;0.&quot;, &quot;1.&quot;, or &quot;2.&quot;. Values greater than &quot;2.&quot; are changed to a &quot;2.&quot; by the next AGSTUP call. Values less than &quot;0.&quot; are changed to a &quot;0.&quot; by the next AGSTUP call; negative values have a special use, however (see below).
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>The value &quot;0.&quot; disables the drawing of informational labels. They remain defined, however.
<dt>&bull;
<dd>The value &quot;1.&quot; enables the drawing of informational labels and specifies that they may not be shrunk in response to overlap problems.
<dt>&bull;
<dd>The value &quot;2.&quot; enables the drawing of informational labels and specifies that they may be shrunk in response to overlap problems.</dl></dl><dd>Default value: &quot;2.&quot; (labels enabled, shrinkable). 

 Special action by AGSETP: An AGSETP call which sets this parameter (individually, rather than as part of a group) to a negative value results in the deletion of all currently defined labels. Note that the negative value is changed to a zero by the next AGSTUP call; thus, the drawing of informational labels is disabled until re-enabled by the user.
<dt>'LABEL/BUFFER.'
<dd>Simplest form of name: 'LAB/BU.' 

 A group of 1+10n parameters, where &quot;n&quot; is the current value of 'LABEL/BUFFER/LENGTH.' (8, by default). Subgroups and the number of parameters in each are as follows:
<dl COMPACT><dd>'LABEL/BUFFER/LENGTH.' (1) 
 'LABEL/BUFFER/CONTENTS.' (10n)</dl><dt>'LABEL/BUFFER/LENGTH.'
<dd>Simplest form of name: 'LAB/BU/LE.' 

 An integral real number specifying the number of 10-word label definitions the label buffer will hold. A user program may need to retrieve, but must not set, the value of this parameter, since its value must match the second dimension of the label buffer. 

 Increasing the size of the label buffer requires modifying the Autograph source code. 

 Default value: &quot;8.&quot;.
<dt>'LABEL/BUFFER/CONTENTS.'
<dd>Simplest form of name: 'LAB/BU/CO.' 

 This parameter group may be thought of as an array FLLB, dimensioned 10 x n, containing up to n 10-word label definitions. For a second subscript j,
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>FLLB(1,j) is either a real &quot;0.&quot;, saying that no label is defined by this 10-word block, or it is non-zero, in which case it identifies a character string in Autograph's character-string storage area; the character string serves as a name for the label defined by this 10-word block. When FLLB(1,j) is non-zero:
<dt>&bull;
<dd>FLLB(2,j) is either a &quot;0.&quot;, to enable drawing of the label, or a &quot;1.&quot;, to disable drawing of the label,
<dt>&bull;
<dd>FLLB(3,j) and FLLB(4,j) are the X and Y coordinates of the label's &quot;basepoint&quot;, in the grid coordinate system,
<dt>&bull;
<dd>FLLB(5,j) and FLLB(6,j) are the X and Y components of the label's &quot;offset vector&quot;, stated as signed fractions of the smaller dimension of the grid window,
<dt>&bull;
<dd>FLLB(7,j) is an integral real number &quot;0.&quot;, &quot;90.&quot;, &quot;180.&quot;, or &quot;270.&quot;, specifying the angle at which the label's &quot;baseline&quot; emanates from the end of its offset vector,
<dt>&bull;
<dd>FLLB(8,j) is an integral real number specifying how the lines of the label are to be positioned relative to the end of the offset vector (&quot;-1.&quot; to line up the left ends, &quot;0.&quot; to line up the centers, or &quot;+1.&quot; to line up the right ends),
<dt>&bull;
<dd>FLLB(9,j) is an integral real count of the number of lines belonging to the label, and
<dt>&bull;
<dd>FLLB(10,j) is an integral real pointer specifying the second subscript (in the line buffer) of the first line of the label (the one having the largest line number), or, if no lines belong to the label, a &quot;0.&quot;.</dl></dl><dd>It is not recommended that a user program change the contents of this buffer directly. Label definitions should be accessed indirectly by means of the parameters 'LABEL/NAME.' and 'LABEL/[DEFINITION/]...'. 

 Default values: The label buffer contains four pre-defined labels, corresponding to the four edges of the grid window. They are as follows: 

 <table> <tr VALIGN=top><td>Label name:</td><td ALIGN=center>'L'</td><td ALIGN=center>'R'</td><td ALIGN=center>'B'
</td></tr><tr VALIGN=top><td>Suppression flag:</td><td ALIGN=center>0.</td><td ALIGN=center>0.</td><td ALIGN=center>0.
</td></tr><tr VALIGN=top><td>Basepoint X:</td><td ALIGN=center>0.</td><td ALIGN=center>1.</td><td ALIGN=center>.5
</td></tr><tr VALIGN=top><td>Basepoint Y:</td><td ALIGN=center>.5</td><td ALIGN=center>.5</td><td ALIGN=center>0.
</td></tr><tr VALIGN=top><td>Offset X:</td><td ALIGN=center>-.015</td><td ALIGN=center>+.015</td><td ALIGN=center>0.
</td></tr><tr VALIGN=top><td>Offset Y:</td><td ALIGN=center>0.</td><td ALIGN=center>0.</td><td ALIGN=center>-.015
</td></tr><tr VALIGN=top><td>Baseline angle:</td><td ALIGN=center>90.</td><td ALIGN=center>90.</td><td ALIGN=center>0.
</td></tr><tr VALIGN=top><td>Centering option:</td><td ALIGN=center>0.</td><td ALIGN=center>0.</td><td ALIGN=center>0.
</td></tr><tr VALIGN=top><td>Line count:</td><td ALIGN=center>1.</td><td ALIGN=center>1.</td><td ALIGN=center>1.
</td></tr><tr VALIGN=top><td>First-line index:</td><td ALIGN=center>1.</td><td ALIGN=center>2.</td><td ALIGN=center>3.
</td></tr> </table> 

 The description of 'LINE/BUFFER/CONTENTS.', below, gives the default values for the definitions of the lines which belong to these labels.
<dt>'LABEL/BUFFER/NAMES.'
<dd>Simplest form of name: 'LAB/BU/NA.' 

 This group is a subset of the previous one. It provides a way of retrieving the names of all currently-defined labels.
<dt>'LABEL/NAME.'
<dd>Simplest form of name: 'LAB/NA.' 

 An integral real pointer which, if non-zero, specifies a particular label in the label buffer - the one which is to be referenced by the parameter group 'LABEL/DEFINITION.' (which see, below). 

 Setting 'LABEL/NAME.' is the required first step in accessing a particular label definition. 

 Default value: &quot;0.&quot; (undefined). 

 Special action by AGSETP: To access the definition of a particular label, one must first call AGSETC with 'LABEL/NAME.' as the first argument and the name of the label one wishes to access as the second argument. This causes AGSETP (which is called by AGSETC) to search for the definition of the desired label in the label buffer. If that definition is not found, a new one is made up and inserted in the label buffer. In either case, 'LABEL/NAME.' is given a real value whose integer equivalent specifies the second subscript of the label definition in the label buffer. 

 The definition of a new label has the name specified by the user, a suppression flag &quot;0.&quot;, a basepoint (.5,.5), an offset vector (0.,0.), a baseline angle &quot;0.&quot;, a centering option &quot;0.&quot;, a line count &quot;0.&quot;, and a first-line index &quot;0.&quot;.
<dt>'LABEL/DEFINITION.'
<dd>Simplest form of name: 'LAB/DE.' 

 A set of nine parameters defining the label specified by the current value of 'LABEL/NAME.'. If 'LABEL/NAME.' has the value &quot;0.&quot;, referencing this group or a parameter in it causes an error exit. Subgroups and the number of parameters in each are as follows:
<dl COMPACT><dd>'LABEL/[DEFINITION/]SUPPRESSION.' (1) 
 'LABEL/[DEFINITION/]BASEPOINT.' (2) 
 'LABEL/[DEFINITION/]OFFSET.' (2) 
 'LABEL/[DEFINITION/]ANGLE.' (1) 
 'LABEL/[DEFINITION/]CENTERING.' (1) 
 'LABEL/[DEFINITION/]LINES.' (1) 
 'LABEL/[DEFINITION/]INDEX.' (1)</dl><dt>'LABEL/[DEFINITION/]SUPPRESSION.'
<dd>Simplest form of name: 'LAB/SU.' 

 An integral real &quot;suppression flag&quot; having the value &quot;0.&quot; or &quot;1.&quot; and specifying whether drawing of the label specified by 'LABEL/NAME.' is enabled (&quot;0.&quot;) or disabled (&quot;1.&quot;). 

 Default value for a new label: &quot;0.&quot; (label enabled). 

 Special action by AGSETP: If a user program attempts to set this parameter (individually, rather than as part of a group) to a negative value, the lines of the label specified by 'LABEL/NAME.' are deleted and 'LINE/NUMBER.' is zeroed. If the negative value is less than &quot;-1.&quot;, the label is deleted as well and 'LABEL/NAME.' is zeroed. (Deleting a label means that its name cell is set to &quot;0.&quot;.)
<dt>'LABEL/[DEFINITION/]BASEPOINT.'
<dd>Simplest form of name: 'LAB/BA.' 

 A set of two parameters specifying the X and Y coordinates of the basepoint of the label specified by 'LABEL/NAME.', in the grid coordinate system. The label is positioned relative to this basepoint. Subgroups and the number of parameters in each are as follows:
<dl COMPACT><dd>'LABEL/[DEFINITION/]BASEPOINT/X.' (1) 
 'LABEL/[DEFINITION/]BASEPOINT/Y.' (1)</dl><dt>'LABEL/[DEFINITION/]BASEPOINT/X.'
<dd>Simplest form of name: 'LAB/BA/X.' 

 The X coordinate of the basepoint of the label specified by 'LABEL/NAME.'. The value &quot;0.&quot; refers to the left edge of the grid window, the value &quot;1.&quot; to the right edge of the grid window. 

 Default value for a new label: &quot;.5&quot; (centered).
<dt>'LABEL/[DEFINITION/]BASEPOINT/Y.'
<dd>Simplest form of name: 'LAB/BA/Y.' 

 The Y coordinate of the basepoint of the label specified by 'LABEL/NAME.'. The value &quot;0.&quot; refers to the bottom edge of the grid window, the value &quot;1.&quot; to the top edge of the grid window. 

 Default value for a new label: &quot;.5&quot; (centered).
<dt>'LABEL/[DEFINITION/]OFFSET.'
<dd>Simplest form of name: 'LAB/OF.' 

 A set of two parameters specifying the X and Y components of the offset vector of the label specified by 'LABEL/NAME.', as signed fractions of the smaller dimension of the grid window. The offset vector has its basepoint at the label basepoint. Subgroups and the number of parameters in each are as follows:
<dl COMPACT><dd>'LABEL/[DEFINITION/]OFFSET/X.' (1) 
 'LABEL/[DEFINITION/]OFFSET/Y.' (1)</dl><dt>'LABEL/[DEFINITION/]OFFSET/X.'
<dd>Simplest form of name: 'LAB/OF/X.' 

 The X component of the offset vector of the label specified by 'LABEL/NAME.' - negative toward the left edge, positive toward the right edge, of the grid window. The magnitude represents a fraction of the smaller dimension of the grid window. 

 Default value for a new label: &quot;0.&quot; (zero-length vector).
<dt>'LABEL/[DEFINITION/]OFFSET/Y.'
<dd>Simplest form of name: 'LAB/OF/Y.' 

 The Y component of the offset vector of the label specified by 'LABEL/NAME.' - negative toward the bottom edge, positive toward the top edge, of the grid window. The magnitude represents a fraction of the smaller dimension of the grid window. 

 Default value for a new label: &quot;0.&quot; (zero-length vector).
<dt>'LABEL/[DEFINITION/]ANGLE.'
<dd>Simplest form of name: 'LAB/AN.' 

 An integral real number having one of the values &quot;0.&quot;, &quot;90.&quot;, &quot;180.&quot;, or &quot;270.&quot;, and specifying the direction in which the baseline of the label specified by 'LABEL/NAME.' emanates from the end of its offset vector, measured counter-clockwise from a left-to-right horizontal vector. All the lines of a label are written parallel to its baseline and in the direction of the baseline. 

 Default value for a new label: &quot;0.&quot; (horizontal, left to right).
<dt>'LABEL/[DEFINITION/]CENTERING.'
<dd>Simplest form of name: 'LAB/CE.' 

 An integral real number specifying the alignment of the lines of the label specified by 'LABEL/NAME.' with the end of its offset vector. A negative value aligns the left ends, a zero value the centers, and a positive value the right ends, of the lines. 

 Default value for a new label: &quot;0.&quot; (centers aligned).
<dt>'LABEL/[DEFINITION/]LINES.'
<dd>Simplest form of name: 'LAB/LI.' 

 An integral real number specifying the number of lines in the label specified by 'LABEL/NAME.'. 

 This parameter is updated by Autograph as lines are added to or deleted from the label and should not be set by a user program. 

 Default value for a new label: &quot;0.&quot; (no lines).
<dt>'LABEL/[DEFINITION/]INDEX.'
<dd>Simplest form of name: 'LAB/IN.' 

 An integral real number specifying the second subscript (in the line buffer) of the first line belonging to the label specified by 'LABEL/NAME.' - a zero if no line belongs to the label. 

 This parameter is updated by Autograph as lines are added to or deleted from the label and should not be set by a user program. 

 Default value for a new label: &quot;0.&quot; (no lines).
<dt>'LINE.'
<dd>Simplest form of name: 'LIN.' 

 A group of 4+6n parameters, where &quot;n&quot; is the current value of 'LINE/BUFFER/LENGTH.' (16, by default) describing up to &quot;n&quot; lines, each of which is a part of some informational label. Subgroups and the number of parameters in each are as follows:
<dl COMPACT><dd>'LINE/MAXIMUM.' (1) 
 'LINE/END.' (1) 
 'LINE/BUFFER/LENGTH.' (1) 
 'LINE/BUFFER/CONTENTS.' (6n) 
 'LINE/NUMBER.' (1)</dl><dt>'LINE/MAXIMUM.'
<dd>Simplest form of name: 'LIN/MA.' 

 An integral real number specifying the assumed maximum length of a character string delivered to Autograph for use as the text of a label line. Such a character string may occur as the first argument of a call to ANOTAT (defining the text of line &quot;100.&quot; in the label 'L'), as the second argument of a call to ANOTAT (defining the text of line &quot;-100.&quot; in the label 'B'), as the last argument of a call to one of the routines EZY, EZXY, EZMY, or EZMXY (defining the text of line &quot;100.&quot; in the label 'T'), or as the second argument of a call to AGSETC whose first argument is 

<dl COMPACT><dd>'LINE/[DEFINITION/]TEXT.'</dl><dd>(defining the text of any line). In each of these cases, the character string must be of the length specified by 'LINE/MAXIMUM.' or shorter. If it is shorter, its last character must be the character specified by 'LINE/END.', described below. 

 This parameter may be given any desired non-negative integral value. 

 Default value: &quot;40.&quot;.
<dt>'LINE/END.'
<dd>Simplest form of name: 'LIN/EN.' 

 A character string whose first character is the one used to mark the end of a character string defining the text of a label line (in calls to ANOTAT, EZY, EZXY, EZMY, EZMXY, and AGSETC), when that character string is shorter than the current maximum specified by 'LINE/MAXIMUM.' (as described above). 

 The terminator character does not become a part of the text of the line. It is stripped off, so that only the preceding characters constitute the text of the line. 

 Default value: &quot;'$'&quot;.
<dt>'LINE/BUFFER.'
<dd>Simplest form of name: 'LIN/BU.' 

 A group of 1+6n parameters, where &quot;n&quot; is the current value of 'LINE/BUFFER/LENGTH.' (16, by default). Subgroups and the number of parameters in each are as follows:
<dl COMPACT><dd>'LINE/BUFFER/LENGTH.' (1) 
 'LINE/BUFFER/CONTENTS.' (6n)</dl><dt>'LINE/BUFFER/LENGTH.'
<dd>Simplest form of name: 'LIN/BU/LE.' 

 An integral real number specifying the number of 6-word line definitions the line buffer will hold. A user program may need to retrieve, but must not set, the value of this parameter, since its value must match the second dimension of the line buffer. 

 Increasing the size of the line buffer requires modifying the Autograph source code. 

 Default value: &quot;16.&quot;.
<dt>'LINE/BUFFER/CONTENTS.'
<dd>Simplest form of name: 'LIN/BU/CO.' 

 This group may be thought of as an array FLLN, dimensioned 6 x n, containing up to n 6-word line definitions. For a second subscript j,
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>FLLN(1,j) is either a real &quot;null 1&quot;, saying that no label line is defined by this 6-word block, or an integral real &quot;line number&quot;, saying that it does define a label line, in which case:
<dt>&bull;
<dd>FLLN(2,j) is either &quot;0.&quot;, to enable drawing of the line, or &quot;1.&quot;, to disable drawing of the line.
<dt>&bull;
<dd>FLLN(3,j) is the real width of each character of the line, stated as a fraction of the smaller dimension of the grid window.
<dt>&bull;
<dd>FLLN(4,j) is an integral real number serving as the identifier of the character string defining the text of the line and enabling it to be retrieved from Autograph's internal character storage space.
<dt>&bull;
<dd>FLLN(5,j) is an integral real count of the number of characters in the text of the line.
<dt>&bull;
<dd>FLLN(6,j) is an integral real number specifying the second subscript (in the line buffer) of the next line of the label to which this line belongs (that one of the remaining lines in the chain with the largest line number) or, if there is no next line, a &quot;0.&quot;.</dl></dl><dd>It is not recommended that a user program change the contents of this buffer directly. Line definitions should be accessed indirectly by means of the parameters 'LINE/NUMBER.' and 'LINE/[DEFINITION/]...'. 

 Default values: The line buffer contains four pre-defined lines, each of which belongs to one of the four pre-defined labels. They are as follows: 

<dl COMPACT><dd><table> <tr VALIGN=top><td>Label name</td><td>'L'</td><td>'R'</td><td>'B'</td><td>'T'
</td></tr><tr VALIGN=top><td>Line number</td><td>+100.</td><td>-100.</td><td>-100.</td><td>+100.
</td></tr><tr VALIGN=top><td>Suppression flag</td><td>0.</td><td>0.</td><td>0.</td><td>0. 
</td></tr><tr VALIGN=top><td>Character width</td><td>.015</td><td>.015</td><td>.015</td><td>.020 
</td></tr><tr VALIGN=top><td>Text pointed to</td><td>'Y'</td><td>' ' (a blank)</td><td>'X'</td><td>' ' (a blank) 
</td></tr><tr VALIGN=top><td>Text length</td><td>1.</td><td>0.</td><td>1.</td><td>0.
</td></tr><tr VALIGN=top><td>Next-line index</td><td>0.</td><td>0.</td><td>0.</td><td>0. 
</td></tr> </table><dl COMPACT><dd>The description of 'LABEL/BUFFER/CONTENTS.', above, gives default values for the definitions of the four labels which contain these lines.
<dt>'LINE/NUMBER.'
<dd>Simplest form of name: 'LIN/NU.' 

 An integral real pointer which, if non-zero, specifies a particular line in the line buffer - the one which is to be referenced by the parameter group 'LINE/DEFINITION.' (which see, below). 

 Setting this parameter is the required first step in accessing a particular line definition. 

 Default value: &quot;0.&quot; (undefined). 

 Special action by AGSETP: To access the definition of a particular line of a particular label, one must ensure that 'LABEL/NAME.' (which see, above) is set. Then, one must call AGSETI with 'LINE/NUMBER.' as the first argument and the number of the line one wishes to access as the second argument. This causes AGSETP (which is called by AGSETI) to search the line buffer for the definition of a line belonging to the label specified by the current value of 'LABEL/NAME.' and having the desired line number. If no such definition is found, a new one is made up, inserted in the line buffer, and linked into the proper place in the chain of lines belonging to the label. In either case, 'LINE/NUMBER.' is given an integral real value specifying the second subscript of the line definition in the line buffer. 

 The definition of a new line has the number specified by the user, a suppression flag &quot;0.&quot;, a character width &quot;.015&quot;, a pointer to the text string &quot;' ' (a single blank)&quot;, and a text length of &quot;1.&quot;. 

 Note: The &quot;line numbers&quot; are used to identify the lines of a label and to specify their positions relative to each other and to the baseline of the label. Lines having positive line numbers are drawn above the label baseline, lines having zero line numbers are drawn along the label baseline, and lines having negative line numbers are drawn below the label baseline. A line having a greater line number than another line is drawn above that line. (&quot;Above&quot; and &quot;below&quot; are used here from the viewpoint of someone reading the label.) The magnitudes of the line numbers in no way affect inter-line spacing, which is determined by Autograph itself.
<dt>'LINE/DEFINITION.'
<dd>Simplest form of name: 'LIN/DE.' 

 A group of five parameters defining the line specified by 'LINE/NUMBER.'. If 'LINE/NUMBER.' has the value &quot;0.&quot;, referencing a parameter in this group causes an error exit. Subgroups and the number of parameters in each are as follows:
<dl COMPACT><dd>'LINE/[DEFINITION/]SUPPRESSION.' (1) 
 'LINE/[DEFINITION/]CHARACTER.' (1) 
 'LINE/[DEFINITION/]TEXT.' (1) 
 'LINE/[DEFINITION/]LENGTH.' (1) 
 'LINE/[DEFINITION/]INDEX.' (1)</dl><dt>'LINE/[DEFINITION/]SUPPRESSION.'
<dd>Simplest form of name: 'LIN/SU.' 

 An integral real number having the value &quot;0.&quot; or &quot;1.&quot; and specifying whether drawing of the line specified by 'LINE/NUMBER.' is enabled (&quot;0.&quot;) or disabled (&quot;1.&quot;). 

 Default value for a new line: &quot;0.&quot; (line enabled). 

 Special action by AGSETP: If a user program attempts to set this parameter (individually, rather than as a part of a group) to a negative value, the line specified by 'LINE/NUMBER.' is deleted and 'LINE/NUMBER.' is reset to &quot;0.&quot;. (Deleting a line means that it is unlinked from the chain of lines belonging to its label and that its number cell is set to &quot;null 1&quot;.)
<dt>'LINE/[DEFINITION/]CHARACTER.'
<dd>Simplest form of name: 'LIN/CH.' 

 A real number specifying the desired width of each character of the line specified by 'LINE/NUMBER.', stated as a fraction of the smaller dimension of the grid window. 

 Default value for a new line: &quot;.015&quot;.
<dt>'LINE/[DEFINITION/]TEXT.'
<dd>Simplest form of name: 'LIN/TE.' 

 An integral real number serving as an identifier for a character string stored away in Autograph's internal character storage space. 

 Default value for a new line: &quot;' ' (a single blank)&quot;. 

 Special action by AGSETP: When this parameter is set by a call to AGSETC, the character string appearing as the second argument of AGSETC is stored in a character storage array inside Autograph, an identifier allowing for later retrieval of the string is generated, and the value of that identifier is stored (by AGSETP, which is called by AGSETC) as the parameter value. At that time, the length of the string is determined and 'LINE/[DEFINITION/]LENGTH.' is set. See 'LINE/MAXIMUM.' and 'LINE/TERMINATOR.', above.
<dt>'LINE/[DEFINITION/]LENGTH.'
<dd>Simplest form of name: 'LIN/LE.' 

 An integral real count of the number of characters in the text of the line specified by 'LINE/NUMBER.'. Setting this parameter less than or equal to zero suppresses the drawing of the line. See also the description of 'LINE/[DEFINITION/]TEXT.', above. 

 Default value for a new line: &quot;1.&quot; (one character - a blank).
<dt>'LINE/[DEFINITION/]INDEX.'
<dd>Simplest form of name: 'LIN/IN.' 

 An integral real number specifying the second subscript (in the line buffer) of the next line of the label - a zero if there is no next line. 

 This parameter is updated by Autograph as lines are added to or deleted from the label and should not be set by a user program.
<dt>'SECONDARY.'
<dd>Simplest form of name: 'SEC.' 

 A group of 149 &quot;secondary&quot; control parameters. These are not normally set by a user program, but are computed by Autograph itself (the routine AGSTUP). Their values may be of use in some applications. Subgroups and the number of parameters in each are as follows:
<dl COMPACT><dd>'SECONDARY/GRAPH.' (4) 
 'SECONDARY/USER.' (4) 
 'SECONDARY/CURVE.' (4) 
 'SECONDARY/DIMENSIONS.' (3) 
 'SECONDARY/AXIS.' (80) 
 'SECONDARY/LABEL.' (54)</dl><dt>'SECONDARY/GRAPH.'
<dd>Simplest form of name: 'SEC/GR.' 

 A group of four real numbers specifying the X coordinates of the left and right edges of the graph window and the Y coordinates of the bottom and top edges of the graph window, in the grid coordinate system. These values are used by Autograph to determine whether a point whose coordinates are expressed in the grid coordinate system lies inside or outside the graph window. 

 If the parameters in the group 'GRID.' have their default values (&quot;.15&quot;, &quot;.95&quot;, &quot;.15&quot;, &quot;.95&quot;, and &quot;0.&quot;), these four parameters will be given the values &quot;-.1875&quot;, &quot;1.0625&quot;, &quot;-.1875&quot;, and &quot;1.0625&quot;. Note that -.1875 = (0.-.15)/(.95-.15) and that 1.0625 = (1.-.15)/(.95-.15).
<dt>'SECONDARY/USER.'
<dd>Simplest form of name: 'SEC/US.' 

 A set of four real numbers specifying the X coordinates of the left and right edges of the grid window and the Y coordinates of the bottom and top edges of the grid window, in the user coordinate system. These values are used in mapping user curve points into the grid window. The routines AGSTUP, AGBACK, and AGCURV use these four numbers as arguments 5 through 8 in calls to the system-plot-package routine SET.
<dt>'SECONDARY/CURVE.'
<dd>Simplest form of name: 'SEC/CU.' 

 A group of four real numbers specifying the X coordinates of the left and right edges of the grid (curve) window and the Y coordinates of the bottom and top edges of the grid (curve) window. The X coordinates are stated as fractions of the distance from left to right, and the Y coordinates as fractions of the distance from bottom to top, in the plotter frame. The routines AGSTUP, AGBACK, and AGCURV use these four numbers as arguments 1 through 4 in calls to the system-plot-package routine SET. If the parameters in the groups 'GRAPH.' and 'GRID.' have their default values, these four parameters are given the values &quot;.15&quot;, &quot;.95&quot;, &quot;.15&quot;, and &quot;.95&quot;.
<dt>'SECONDARY/DIMENSIONS.'
<dd>Simplest form of name: 'SEC/DI.' 

 A group of three real numbers, the first two of which specify the width and height of the grid window and the third of which is equal to the smaller of the first two. Each is stated as a number of plotter units. If the parameters in the groups 'GRAPH.' and 'GRID.' have their default values and the plotter being used has 1024x1024 addressable positions, then each of these three parameters will be given the value 818.4 = (.95-.15) * 1023.
<dt>'SECONDARY/AXIS.'
<dd>Simplest form of name: 'SEC/AX.' 

 A group of eighty parameters having to do with the drawing of the four axes. Subgroups and the number of parameters in each are as follows:
<dl COMPACT><dd>'SECONDARY/[AXIS/]LEFT.' (20) 
 'SECONDARY/[AXIS/]RIGHT.' (20) 
 'SECONDARY/[AXIS/]BOTTOM.' (20) 
 'SECONDARY/[AXIS/]TOP.' (20)</dl><dd>The parameters from the subgroups are interleaved in the group; that is to say, the first elements of the subgroups comprise elements 1 through 4 of the group, the second elements of the subgroups comprise elements 5 through 8 of the group, and so on.
<dt>'SECONDARY/[AXIS/]s.'
<dd>Simplest form of name: 'SEC/s.' 

 A group of twenty parameters having to do with the drawing of the axis specified by &quot;s&quot;, where &quot;s&quot; is one of the keywords &quot;LEFT&quot;, &quot;RIGHT&quot;, &quot;BOTTOM&quot;, or &quot;TOP&quot;. Subgroups and the number of parameters in each are as follows:
<dl COMPACT><dd>'SECONDARY/[AXIS/]s/POSITION.' (6) 
 'SECONDARY/[AXIS/]s/TICKS.' (3) 
 'SECONDARY/[AXIS/]s/NUMERIC.' (11)</dl><dt>'SECONDARY/[AXIS/]s/POSITION.'
<dd>Simplest form of name: 'SEC/s/PO.' 

 A group of six real numbers, the first three of which describe a point at the beginning of axis &quot;s&quot; and the last three of which describe a point at the end of axis &quot;s&quot;. The first two numbers of each triplet are the X and Y coordinates of the point, in the grid coordinate system. The third number of each triplet is a user-system X or Y coordinate (an X coordinate for a horizontal axis, a Y coordinate for a vertical axis) of the point.
<dt>'SECONDARY/[AXIS/]s/TICKS.'
<dd>Simplest form of name: 'SEC/s/TI.' 

 A group of three real numbers, specifying the values Autograph has chosen to use for the primary parameters
<dl COMPACT><dd>'[AXIS/]s/[TICKS/]MAJOR/[SPACING/]TYPE.' 
 '[AXIS/]s/[TICKS/]MAJOR/[SPACING/]BASE.' 
 '[AXIS/]s/[TICKS/]MINOR/SPACING.'</dl><dd>(which see, above). These secondary parameters are used to hold the values Autograph chooses for the corresponding primary parameters so as not to disturb &quot;null 1&quot; values of those primary parameters.
<dt>'SECONDARY/[AXIS/]s/NUMERIC.'
<dd>Simplest form of name: 'SEC/s/NU.' 

 A group of eleven real numbers having to do with the generation of numeric labels on the axis specified by &quot;s&quot;. The first three of these specify the values Autograph has chosen to use for the primary parameters
<dl COMPACT><dd>'[AXIS/]s/[NUMERIC/]TYPE.' 
 '[AXIS/]s/[NUMERIC/]EXPONENT.' 
 '[AXIS/]s/[NUMERIC/]FRACTION.'</dl><dd>(which see, above). The secondary parameters are used so as not to disturb &quot;null 1&quot; values of the primary parameters. 

 The fourth parameter is an integral real count of the number of characters in the longest numeric-label mantissa on the axis &quot;s&quot;. 

 The fifth parameter is an integral real count of the number of characters in the longest numeric-label exponent on the axis &quot;s&quot;. 

 The sixth parameter is the necessary multiplicative &quot;reduction factor&quot; (between &quot;0.&quot; and &quot;1.&quot;) to be applied to the sizes of numeric labels on the axis &quot;s&quot; in order to make them fit without overlap problems. 

 The seventh, eighth, ninth, and tenth parameters are real numbers specifying the width of the space required by numeric labels to the left (outward), to the right (inward), at the beginning and at the end of the axis &quot;s&quot; - each is stated as a fraction of the width or height of the grid window, depending on the orientation of the axis &quot;s&quot;. 

 The eleventh parameter indicates the linear/log nature of the axis specified by &quot;s&quot;.
<dt>'SECONDARY/LABEL.'
<dd>Simplest form of name: 'SEC/LA.' 

 A group of fifty-four parameters describing the six &quot;label boxes&quot;, each of which provides a mechanism for moving and/or shrinking a particular group of labels in attempting to keep any label in that group from overlapping an axis or extending outside the current graph window. Subgroups and the number of parameters in each are as follows:
<dl COMPACT><dd>'SECONDARY/LABEL/LEFT.' (9) 
 'SECONDARY/LABEL/RIGHT.' (9) 
 'SECONDARY/LABEL/BOTTOM.' (9) 
 'SECONDARY/LABEL/TOP.' (9) 
 'SECONDARY/LABEL/CENTER.' (9) 
 'SECONDARY/LABEL/GRAPH.' (9)</dl><dd>The parameters of the subgroups are interleaved in the group. The first elements of the subgroups form elements 1 through 6 of the group, the second elements of the subgroups form elements 7 through 12 of the group, and so on.
<dt>'SECONDARY/LABEL/b.'
<dd>Simplest form of name: 'SEC/LA/b.' 

 where the keyword &quot;b&quot; specifies the label box, as follows:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>If &quot;b&quot; = &quot;LEFT&quot;, label box 1 is specified. It contains all labels having a basepoint on the left edge of the grid window and a leftward-pointing offset vector. These labels are to be moved leftward as required to avoid overlapping any numeric labels on either Y axis.
<dt>&bull;
<dd>If &quot;b&quot; = &quot;RIGHT&quot;, label box 2 is specified. It contains all labels having a basepoint on the right edge of the grid window and a rightward-pointing offset vector. These labels are to be moved rightward as required to avoid overlapping any numeric labels on either Y axis.
<dt>&bull;
<dd>If &quot;b&quot; = &quot;BOTTOM&quot;, label box 3 is specified. It contains all labels having a basepoint on the bottom edge of the grid window and a downward-pointing offset vector. These labels are to be moved downward as required to avoid overlapping any numeric labels on either X axis.
<dt>&bull;
<dd>If &quot;b&quot; = &quot;TOP&quot;, label box 4 is specified. It contains all labels having a basepoint on the top edge of the grid window and an upward-pointing offset vector. These labels are to be moved upward as required to avoid overlapping any numeric labels on either X axis.
<dt>&bull;
<dd>If &quot;b&quot; = &quot;CENTER&quot;, label box 5 is specified. It contains all labels having a basepoint on some edge of the grid window and an inward-pointing offset vector. These labels are to be moved inward as required to avoid overlapping numeric labels on any axis.
<dt>&bull;
<dd>If &quot;b&quot; = &quot;GRAPH&quot;, label box 6 is specified. It contains all labels not specifically assigned to one of the other boxes. These labels are not moved, but may still be shrunk as required to avoid their running outside the grid window.</dl></dl><dd>Prior to a call to AGSTUP, the nine parameters in this group are undefined. Following an AGSTUP call, but preceding an AGBACK call, they have what I shall call &quot;interim&quot; values. Following an AGBACK call, they have what I shall call &quot;final&quot; values. 

 The first parameter in the group is a &quot;reduction factor&quot; for the widths of characters in the labels in box &quot;b&quot;. This parameter may have the interim value &quot;0.&quot;, specifying that no actual value has yet been computed, or &quot;1.&quot;, specifying that the user has prohibited shrinkage of labels in box &quot;b&quot; (by giving 'LABEL/CONTROL.' the value &quot;1.&quot;). The final value of the reduction factor may be &quot;-1.&quot;, specifying that minimum-sized labels were used, but even they led to overlap problems, or a value between &quot;0.&quot; and &quot;1.&quot;, specifying the actual reduction factor applied when the labels were drawn. 

 The next four parameters in the group specify the grid-system X coordinates of the left and right edges, and the grid-system Y coordinates of the bottom and top edges, of label box &quot;b&quot;. The interim values specify the box in which the labels must be made to fit in order to avoid overlap, the final values the box in which the labels were actually made to fit. 

 The last four parameters in the group specify the grid-system X coordinates of the left and right edges, and the grid-system Y coordinates of the bottom and top edges, of the label box &quot;b&quot; which would result if all the labels were reduced to minimum size. The interim values specify an unmoved box, the final values a (possibly) moved box.</dl></dl>
</dl><h2>See Also</h2>Online: agdshn, aggetc, aggetf, aggeti, aggetp, aggetr, agrstr, agsave, agsetc, agsetf, agseti, agsetp, agsetr, anotat, displa 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

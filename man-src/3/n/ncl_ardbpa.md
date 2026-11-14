---
title: "ncl_ardbpa(3)"
name: "ncl_ardbpa"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ardbpa/"
---

ARDBPA - Produces a plot showing all of the edge segments in an area map that have a specified group identifier IGRP; if IGRP is less than or equal to zero, all groups are included. Such plots allow one to debug problems with an area map. 

<h2>Synopsis</h2>CALL ARDBPA (MAP,IGRP,LABEL)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_ardbpa (int *map, int igrp, char *label)
<h2>Description</h2><dl COMPACT><dt>MAP
<dd>(an input/output array of type INTEGER) - An array containing an area map that has at least been initialized by a call to ARINAM and to which edges will probably have been added by calls to AREDAM. 

 Note: As part of initializing the area map, ARINAM stores the dimension of MAP in <a HREF="/docs/linux/man/1-map/">MAP</a>(1); therefore, the dimension does not have to be given as an argument in calls to ARDBPA.)
<dt>IGRP
<dd>(an input expression of type INTEGER) - The group identifier of the group that you want to examine. If IGRP is less than or equal to zero, edges from all groups will be shown.
<dt>LABEL
<dd>(an input constant or variable of type CHARACTER) - The label you want put on the plot.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>When ARDBPA is called, it draws the requested picture and then calls FRAME to advance to a new frame. 

 By default, each edge segment in the plot appears in one of four different colors, depending on whether the area identifiers to the left and right are less than or equal to zero or greater than zero, as follows: 

 <table> <tr VALIGN=top><td>Color</td><td>Left area identifier</td><td>Right area identifier
</td></tr><tr VALIGN=top><td>-----</td><td>--------------------</td><td>---------------------
</td></tr><tr VALIGN=top><td>Magenta</td><td>Less than or equal to 0</td><td>Less than or equal to 0 
</td></tr><tr VALIGN=top><td>Yellow</td><td>Less than or equal to 0</td><td>Greater than 0
</td></tr><tr VALIGN=top><td>Cyan</td><td>Greater than 0</td><td>Less than or equal to 0
</td></tr><tr VALIGN=top><td>White</td><td>Greater than 0</td><td>Greater than 0
</td></tr> </table> 

 In some cases you may notice gray lines in your plot. This means that the same edge occurs in more than one group. In all but one of those groups, Areas negates the group identifier for the edge in the area map. This allows Areas to include the edge when it is looking at a particular group (as in ARPRAM), but omit it when it is looking at the union of all the groups (as in ARSCAM). 

 Color indices DC+1 through DC+5 are used for the required colors. The default value of DC is 100, so, by default, ARDBPA redefines color indices 101 through 105. If this would result in colors that you have defined being redefined, you should change the value of DC to something else. 

 Nominally, each edge segment is shown with an arrowhead, indicating the order in which the points defining the edge segment occur in the area map and therefore which side of the edge segment is to the left and which side is to the right. In regions where putting an arrowhead on each edge segment would result in too much clutter, some of them may be omitted. 

 The left and right area identifiers for each edge segment are written in the appropriate positions relative to the edge segment. Also, if IGRP is less than or equal to zero, the group identifier for each edge segment is written on the segment itself. These identifiers are intentionally written using very small characters; the idea is that you can look at the whole plot to get some idea of possible problem regions; when such a region is found, you can enlarge it, using the &quot;zoom&quot; capability of &quot;idt&quot;, for a closer look; at that point, the area identifiers become readable. 

 If ARDBPA is used for a complicated area map, the amount of output can be very large.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: arex01, cardb2.
<h2>Access</h2>To use ARDBPA or c_ardbpa, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: areas, areas_params, ardrln, aredam, argeti, argetr, argtai, arinam, armvam, arpram, arscam, arseti, arsetr, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

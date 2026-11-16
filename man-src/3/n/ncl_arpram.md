---
title: "ncl_arpram(3)"
name: "ncl_arpram"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_arpram/"
---

ARPRAM - Preprocesses an area map that has been initialized by a call to ARINAM and to which edges have been added by calls to AREDAM. 

<h2>Synopsis</h2>CALL ARPRAM (MAP,IF1,IF2,IF3)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_arpram (int *map, int if1, int if2, int if3)
<h2>Description</h2>Preprocessing an area map is a seven-step process that makes all of the area-identifier information in the area map consistent:
<dl COMPACT><dt>Step 1:
</dt><dd>ARPRAM shortens edge segments whose projections on the X axis are more than twice as long as the average. ARPRAM does this by interpolating points along their lengths. This improves efficiency when executing other parts of the algorithm.
</dd><dt>Step 2:
</dt><dd>ARPRAM locates all intersections of edge segments and interpolates the intersection points along these edge segments. This step can take a lot of time. If you set IF1 nonzero, then pairs of edge segments are examined for intersections only if one of the pair has a left or a right area identifier that is zero or negative.
</dd><dt>Step 3:
</dt><dd>ARPRAM locates coincident edge segments (edge segments with identical endpoints). If two such coincident edge segments belong to the same group, one of them is removed; if they belong to different groups, one of them is modified in such a way that it will appear to be present when looking for areas defined by edge segments in a particular group, but absent when looking for areas defined by all edge segments.
</dd><dt>Step 4:
</dt><dd>ARPRAM searches for and removes &quot;dangling&quot; edge segments (those that do not contribute to enclosing any area). This step is skipped if IF2 is nonzero.
</dd><dt>Step 5:
</dt><dd>ARPRAM looks for holes in the areas defined by each edge group and draws connecting edge segments between the edge and the hole. This step is skipped if IF3 is nonzero.
</dd><dt>Step 6:
</dt><dd>ARPRAM adjusts area identifier information in the area map. It examines all the edge segments of each area in each group to see what area identifier should be assigned to the area, and then makes adjustments.
</dd><dt>Step 7:
</dt><dd>Connecting lines that were inserted in step 5 are removed from the area map.</dd></dl>
 

 You can put edges in an area map, preprocess it, add more edges, preprocess it again, and so on. 

 Each of the routines ARDRLN, ARGTAI, and ARSCAM checks to make sure that the area map has been preprocessed since the last time that edges were added to it and, if not, calls ARPRAM; the only advantage to the user of calling ARPRAM directly is to use the time-saving shortcuts specified by the arguments IF1, IF2, and IF3. 

 The arguments of ARPRAM are as follows: 

<dl COMPACT><dt>MAP
</dt><dd>(an input/output array of type INTEGER) - An array containing an area map that has been initialized by a call to ARINAM and to which edges have been added by calls to AREDAM. 
 Note: As part of initializing the area map, ARINAM stores the dimension of MAP in <a HREF="/docs/linux/man/1-map/">MAP</a>(1); therefore, the dimension does not have to be given as an argument in calls to ARPRAM.)
</dd><dt>IF1
</dt><dd>(an input expression of type INTEGER) - If you set IF1 nonzero, ARPRAM checks a pair of edge segments for intersection only if one of the pair has a left or right area identifier that is zero or negative. This would be appropriate for contour lines, which intersect the perimeter, but do not intersect each other.
</dd><dt>IF2
</dt><dd>(an input expression of type INTEGER) - If you set IF2 nonzero, ARPRAM does not check for dangling edges. This would be appropriate for contour lines, which are known not to have any such edges. This is not appropriate for Ezmap boundary lines, because the Ezmap dataset contains some edge segments (small islands) that are formed by unclosed curves.
</dd><dt>IF3
</dt><dd>(an input expression of type INTEGER) - If you set IF3 nonzero, ARPRAM speeds up the process of adjusting area identifiers by omitting the consideration of &quot;holes&quot; in the areas examined. This is appropriate for contour lines as long as the left and right area identifiers provided at each contour level are consistent with those provided at the adjacent levels.</dd></dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: eezmpa, tareas, tezmpa, fsppoint.
<h2>Access</h2>To use ARPRAM or c_arpram, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the areas man page for a description of all Areas error messages and/or informational messages.
<h2>See Also</h2>Online: areas, areas_params, ardbpa, ardrln, aredam, argeti, argetr, argtai, arinam, armvam, arscam, arseti, arsetr, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

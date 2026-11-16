---
title: "ncl_gsmk(3)"
name: "ncl_gsmk"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gsmk/"
---

GSMK (Set marker type) - sets the type of polymarker to be used in subsequent GPM calls.
<h2>Synopsis</h2>CALL GSMK (MTYPE)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void gset_marker_type(Gint marker_type);
<h2>Description</h2><dl COMPACT><dt>MTYPE
</dt><dd>(Integer, Input) - Selects the type of marker to be drawn. Options are:
</dd><dl COMPACT><dd></dd><dl COMPACT><dt>&lt; 0
</dt><dd>implementation dependent (not used in NCAR GKS-0A)
</dd><dt> 1
</dt><dd>&nbsp;<wbr>.&nbsp;<wbr>(dot)
</dd><dt> 2
</dt><dd>&nbsp;<wbr>+&nbsp;<wbr>(plus)
</dd><dt> 3
</dt><dd>&nbsp;<wbr>*&nbsp;<wbr>(asterisk)&nbsp;<wbr>This is the default
</dd><dt> 4
</dt><dd>&nbsp;<wbr>o&nbsp;<wbr>(circle)
</dd><dt> 5
</dt><dd>&nbsp;<wbr>X&nbsp;<wbr>(cross)
</dd><dt>&ge; 6
</dt><dd>&nbsp;<wbr>reserved for registration or future standardization</dd></dl></dl>
</dl><h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gpm, gsmksc, gscr, gspmci, gqmk, gqmksc, gqpmci, point, points, ngdots, gset_marker_type 

 Hardcopy: User's Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

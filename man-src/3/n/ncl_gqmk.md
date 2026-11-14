---
title: "ncl_gqmk(3)"
name: "ncl_gqmk"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gqmk/"
---

GQMK (Inquire marker type) - retrieves the current value for the marker type.
<h2>Synopsis</h2>CALL GQMK (ERRIND, MTYPE)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void ginq_marker_type(Gint *err_ind, Gint *marker_type);
<h2>Description</h2><dl COMPACT><dt>ERRIND
<dd>(Integer, Output) - If the inquired value cannot be returned correctly, a non-zero error indicator is returned in ERRIND, otherwise a zero is returned. Consult &quot;User's Guide for NCAR GKS-0A Graphics&quot; for a description of the meaning of the error indicators.
<dt>MTYPE
<dd>(Integer, Output) - Returns the current value for the polymarker type as set by default or by a call to GSMK.
<dl COMPACT><dd><dl COMPACT><dt>1
<dd>&nbsp;<wbr>.&nbsp;<wbr>(dot)
<dt>2
<dd>&nbsp;<wbr>+&nbsp;<wbr>(plus)
<dt>3
<dd>&nbsp;<wbr>*&nbsp;<wbr>(asterisk)&nbsp;<wbr>This is the default
<dt>4
<dd>&nbsp;<wbr>o&nbsp;<wbr>(circle)
<dt>5
<dd>&nbsp;<wbr>X&nbsp;<wbr>(cross)</dl></dl>
</dl><h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gpm, gsmk, gsmksc, gscr, gspmci, gqmksc, gqpmci, point, points, ginq_marker_type 

 Hardcopy: User's Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

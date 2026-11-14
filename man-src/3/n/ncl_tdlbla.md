---
title: "ncl_tdlbla(3)"
name: "ncl_tdlbla"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_tdlbla/"
---

TDLBLA - This routine is called to put labels on a particular edge of a box.

<h2>Synopsis</h2>

CALL TDLBLA (IAXS, ILBL, NLBL, XAT0, XAT1, YAT0, YAT1, ANGD)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_tdlbla(int iaxs, char* ilbl, char* nlbl, float xat0, float xat1, float yat0, float yat1, float angd)

<h2>Description</h2>

It is assumed that TDPARA has been called to define the reference parallelogram to be a rectangle in 3-space lying in one corner of one face of the box being labelled. The sides of this rectangle are assumed to be vectors of length 1 (that is to say, the rectangle defines a unit square within that face of the box). It is also assumed that the value of the internal parameter 'CS2' has been set in the same way that TDLBLS would reset it, using a code sequence like 

 <pre> CALL TDGETR ('CS1',CSM1)
 CSM2=CSM1*MIN(UMAX-UMIN,VMAX-VMIN,WMAX-WMIN)
 CALL TDSETR ('CS2',CSM2)</pre>(where UMIN, UMAX, VMIN, VMAX, WMIN, and WMAX are as defined for a call to TDLBLS). 

 The arguments of TDLBLA are as follows:
<dl><dt>IAXS
<dd>(an input expression of type INTEGER) - says which edge of the face is being labelled (1 =&gt; left, 2 =&gt; right, 3 =&gt; bottom, and 4 =&gt; top, where the meanings of &quot;left&quot;, &quot;right&quot;, &quot;bottom&quot;, and &quot;top&quot; are defined by the orientation of the reference parallelogram).
<dt>ILBL
<dd>(input, of type CHARACTER) - a string to be used as an informational label. If the string is blank, no informational label is written.
<dt>NLBL
<dd>(input, of type CHARACTER) - a string containing numeric labels. The labels need not be in any particular order, but they have to be separated by blanks and each has to be readable using a FORTRAN format of the form &quot;En.0&quot;, where &quot;n&quot; is the length of the label. If the string is blank, no informational label is written.
<dt>XAT0 and XAT1
<dd>(input expressions of type REAL) - the values of &quot;X&quot; associated with the left and right edges of the face being labelled, where &quot;left&quot; and &quot;right&quot; are defined in terms of the current reference parallelogram.
<dt>YAT0 and YAT1
<dd>(input expressions of type REAL) - the values of &quot;Y&quot; associated with the bottom and top edges of the face being labelled, where &quot;bottom&quot; and &quot;top&quot; are defined in terms of the current reference parallelogram.
<dt>ANGD
<dd>(an input expression of type REAL) - specifies the angle, in degrees, at which the labels are to be written. This angle is defined with reference to the current reference parallelogram.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Access</h2>

To use TDLBLA or c_tdlbla, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: tdclrs, tdctri, tddtri, tdgeti, tdgetr, tdgrds, tdgrid, tdgtrs, tdinit, tditri, tdlbls, tdline, tdlnpa, tdmtri, tdotri, tdpack, tdpack_params, tdpara, tdplch, tdprpa, tdprpi, tdprpt, tdseti, tdsetr, tdsort, tdstri, tdstrs

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

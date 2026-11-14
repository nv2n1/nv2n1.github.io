---
title: "ncl_tdpara(3)"
name: "ncl_tdpara"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_tdpara/"
---

TDPARA - Initialization routine for TDPACK, called to set the value of certain internal values.

<h2>Synopsis</h2>

CALL TDPARA (UA00, VA00, WA00, UV10, VV10, WV10, UV01, VV01, WV01)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_tdpara(float ua00, float va00, float wa00, float uv10, float vv10, float wv10, float uv01, float vv01, float wv01)

<h2>Description</h2>

This routine may be thought of as an initialization routine or as just a routine to access certain internal values; it simply transfers the values of its arguments into TDPACK labelled common blocks for later use by other TDPACK routines. These values define a &quot;reference parallelogram&quot;. Each point in the plane in which the parallelogram lies can be identified by specifying its &quot;parallelogram coordinates&quot;: a pair of reals, one of which may be thought of as an &quot;X&quot; coordinate and the other of which may be thought of as a &quot;Y&quot; coordinate. 

 Calls to TDPARA may be positioned without regard to calls to TDINIT because the two routines do not affect one another. Redefining the reference parallelogram affects the behavior of each of the routines TDPRPA, TDPRPI, TDGRID, TDLBLA, and TDPLCH, each of which makes use of parallelogram coordinates in some way. Be aware that each of the routines TDGRDS and TDLBLS calls TDPARA to redefine the reference parallelogram and neither of them restores the original definition when it is done. 

 If a point has &quot;parallelogram coordinates&quot; (XIPA,YIPA), then its actual 3-space coordinates are given by the following equations: 

 <pre> U = UA00+XIPA*UV10+YIPA*UV01
 V = VA00+XIPA*VV10+YIPA*VV01
 W = WA00+XIPA*WV10+YIPA*WV01</pre>The point with parallelogram coordinates (0,0) is in what might be thought of as the &quot;lower left&quot; corner of the parallelogram, while the point with parallelogram coordinates (1,1) is in what might be thought of as the &quot;upper right&quot; corner of the parallelogram. Any point of the plane in which the reference parallelogram lies can be identified using its parallelogram coordinates, not just the points inside the parallelogram itself. 

 Note that, although the reference parallelogram doesn't have to be rectangular, a non-rectangular one is probably not very useful; in fact, a square one defined by unit vectors is probably best, particularly if one is drawing characters in the plane of the reference parallelogram. For example, suppose that you want to write the characters &quot;THE U/V PLANE&quot; in that part of the U/V plane with U values between 0 and 100 and V values between 0 and 200; it is probably best, in this case, to use a reference parallelogram with an origin at (0,0,0), an &quot;X&quot; side with components (1,0,0) and a &quot;Y&quot; side with components (0,1,0). Then, in the call to TDPLCH, one can place the character string at parallelogram coordinates (50,100) and use a character size of 1.5. If one used a reference parallelogram with an origin at (0,0,0), an &quot;X&quot; side with components (100,0,0) and a &quot;Y&quot; side with components (0,200,0), one could place the character string at parallelogram coordinates (.5,.5) and use a character size of .015, but the characters written would be twice as high as they are wide, which is undesirable. 

 The arguments of TDPARA are as follows:
<dl><dt>UA00, VA00, and WA00
<dd>(input expressions of type REAL) - the coordinates of the &quot;origin&quot; of the parallelogram: the point with parallelogram coordinates (0,0).
<dt>UV10, VV10, and WV10
<dd>(input expressions of type REAL) - the U, V, and W components of the vector from the origin of the parallelogram to the point with parallelogram coordinates (1,0).
<dt>UV01, VV10, and WV01
<dd>(input expressions of type REAL) - the U, V, and W components of the vector from the origin of the parallelogram to the point with parallelogram coordinates (0,1).</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Access</h2>

To use TDPARA or c_tdpara, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: tdclrs, tdctri, tddtri, tdgeti, tdgetr, tdgrds, tdgrid, tdgtrs, tdinit, tditri, tdlbla, tdlbls, tdline, tdlnpa, tdmtri, tdotri, tdpack, tdpack_params, tdplch, tdprpa, tdprpi, tdprpt, tdseti, tdsetr, tdsort, tdstri, tdstrs

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

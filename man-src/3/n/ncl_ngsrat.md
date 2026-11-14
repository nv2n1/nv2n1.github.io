---
title: "ncl_ngsrat(3)"
name: "ncl_ngsrat"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ngsrat/"
---

NGSRAT - save/restore/set NCAR GKS primitive attribute values in toto.

<h2>Synopsis</h2>

CALL NGSRAT(IOPT, IAT, RAT)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_ngsrat(int iopt, int *iat, float *rat)

<h2>Description</h2>

<pre><code>IOPT
(an input variable of type INTEGER) indicating the desired action:
= 0
save the current settings of all attributes
internal to the subroutine, i.e. not in the IAT and RAT arrays.
= 1
restore the context from the most recently saved state.
= 2
return the current context in the output arrays IAT (integer
attributes) and RAT (floating-point attributes) as follows:</code></pre> IAT contains integer GKS attribute settings as per:
<dd>IAT( 1) = Clip indicator
<dd>IAT( 2) = Line type
<dd>IAT( 3) = Polyline color index
<dd>IAT( 4) = Marker type
<dd>IAT( 5) = Polymarker color index
<dd>IAT( 6) = Text font
<dd>IAT( 7) = Text precision
<dd>IAT( 8) = Text color index
<dd>IAT( 9) = Text path
<dd>IAT(10) = Text horizontal alignment
<dd>IAT(11) = Text vertical alignment
<dd>IAT(12) = Fill area interior style
<dd>IAT(13) = Fill are style index
<dd>IAT(14) = Fill area color index
<dd>RAT contains REAL GKS attribute settings as per:
<dd>RAT( 1) = Linewidth scale factor
<dd>RAT( 2) = Marker scale factor
<dd>RAT( 3) = Character expansion factor
<dd>RAT( 4) = Character spacing
<dd>RAT( 5) = Character height in world coordinates
<dd>RAT( 6) = Character up vector, X component in world coordinates
<dd>RAT( 7) = Character up vector, Y component in world coordinates
<dt> = 3
<dd>set the context to the values specified in the IAT and RAT arrays (as described above).
<dt>IAT
<dd>An integer array, of length 14, that has meaning only if IOPT equals 2 or 3. The elements of the IAT array are described in the above description of IOPT.
<dt>RAT
<dd>A real array, of length 7, that has meaning only if IOPT equals 2 or 3. The elements of the IAT array are described in the above description of IOPT.</dl>

<h2>Usage</h2>

If you want to save the state of the NCAR GKS primitive attribute settings, call NGSRAT with a first argument of 0. When the first argument is 0, the IAT and RAT arrays (second and third arguments) are ignored and the state values are stored internally to NGSRAT. 

 To restore the NCAR GKS primitive attribute values to what they were as of the last time NGSRAT was called with argument IOPT = 0, then call NGSRAT with first argument of 1. IAT and RAT are ignored in this case. 

 If you call NGSRAT with a fist argument of 2, then the current settings of the NCAR GKS primitive attribute values are returned in arrays IAT and RAT as per the description of IAT and RAT above. 

 If you call NGSRAT with a fist argument of 3, then arrays IAT and RAT must be supplied and the values therein will be used to set the NCAR GKS primitive attribute values as per the description of IAT and RAT above. 

 A common use of NGSRAT would be in conjunction with NGMFTC and NGREOP for saving the GKS state after writing to one metafile, writing to a new metafile, and then restoring the GKS state when reopening the initial metafile.

<h2>Examples</h2>

The following sequence: <pre> CALL NGSRAT(0,IAT,RAT)
 ... do some setting and drawing
 CALL NGSRAT(1,IAT,RAT)</pre>would save the values of all NCAR GKS primitive attributes before the code that does setting and drawing and then restore the attribute values after the setting and drawing. 

 Use the ncargex command to see the following relevant example: pgkex27.

<h2>Access</h2>

To use NGSRAT or c_ngsrat, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>Messages</h2>

NGSRAT issues no messages apart from potential illegal setting of the attribute values when IOPT = 3.

<h2>See Also</h2>

Online: ngmftc(3NCARG), ngreop(3NCARG), 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version.

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

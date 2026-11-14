---
title: "ncl_stream(3)"
name: "ncl_stream"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_stream/"
---

STREAM - Plots a streamline representation of field flow data, based on conditions established by STINIT and the current values of a set of user-modifiable internal parameters associated with the Streamlines utility.

<h2>Synopsis</h2>

CALL STREAM (U,V,P,IAM,STUMSL,WRK)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_stream(float *u, float *v, float *p, int *iam, 
 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>int&nbsp;<wbr>(*stumsl_)(&nbsp;<wbr>float&nbsp;<wbr>*xcs, float&nbsp;<wbr>*ycs,&nbsp;<wbr> 
 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>int&nbsp;<wbr>*ncs, int&nbsp;<wbr>*iai, int&nbsp;<wbr>*iag, int&nbsp;<wbr>*nai),&nbsp;<wbr> 
 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>float&nbsp;<wbr>*wrk)

<h2>Description</h2>

<dl><dt>U
<dd>(REAL 2 dimensional array, dimensioned as specified in last call to STINIT, input): By default, assumed to contain the first dimensional axis components of the vector field. However, if PLR is non-zero, it is treated as containing the vector magnitudes.
<dt>V
<dd>(REAL 2 dimensional array, dimensioned as specified in last call to STINIT, input): By default, assumed to contain the second dimensional axis components of the vector field. However, if PLR is non-zero, it is treated as containing the vector angles.
<dt>P
<dd>(REAL, input, DUMMY): This argument is currently ignored. May be assigned a dummy value.
<dt>IAM
<dd>(INTEGER array, unknown dimension, input): Area map array previously established by calls to routines in the Areas utility. It is checked to see that the number of area groups is within the limits allowed by Streamlines, then simply passed through to an Areas routine for further processing. Required only if MSK is set to a non-zero value; otherwise it is ignored and may be assigned a dummy value.
<dt>STUMSL
<dd>(EXTERNAL subroutine, input): User-definable masked drawing subroutine. Required only if MSK is set to a non-zero value; otherwise it is ignored and may be assigned a dummy value.
<dt>WRK
<dd>(REAL array, dimensioned as specified in last call to STINIT, input/output): Work array used to store normalized values of the U and V vector components while the streamlines are calculated. It also holds bit flags indicating whether a grid location is eligible for starting a streamline or placing a directional arrowhead.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Usage</h2>

A call to STINIT must precede the first call to STREAM, and is again required any time the vector array data changes or any of the coordinate space control parameters are modified. However, you may modify certain rendering control parameters between multiple invocations of STREAM. See the streamlines_params man page for more information. 

 Arguments to STINIT establish the sizes of the vector component arrays and the WRK array. STINIT places these values into common block variables where they become available to STREAM. Therefore no size arguments need appear in the STREAM argument list. When area masking is not enabled, the third, fourth and fifth arguments to STREAM may all have dummy values and the invocation would be something like: 

 CALL STREAM(U,V,IDM,IDM,IDM,WRK) 

 where IDM is an arbitrary variable that need not have been initialized. 

 The masking capability supported by Streamlines allows you to overlay streamlines on graphics produced by other utilities, such as Conpack contour plots, without encroaching on areas, like label boxes, that should appear in the foreground. Normally the area map should be generated and used in the normal way (as described in the Areas and Conpack documentation) before calling any routines in the Streamlines utility. When the parameter MSK has a non-zero value, masking is enabled and a previously created area map must be passed to STREAM. STREAM examines the map, returning an error if the map appears to be invalid or the number of area groups is beyond the range it can handle (currently 64). Otherwise, it only uses the map as an argument to the Areas utility subroutine, ARDRLN. The user must also pass in a user-definable masked drawing subroutine. A simple version of this subroutine, named (like the argument) STUMSL, is supplied with the Streamlines utility, and may suffice for basic masked drawing operations. See the stumsl man page for more information. 

 The P array argument is intended for future enhancement of the Streamlines utility and is not currently used or examined in any way. You may pass it an uninitialized dummy argument.

<h2>Examples</h2>

Use the ncargex command to see the following relevant examples: ffex00, ffex01, ffex03, ffex04, fstream, stex01, stex02, stex03, stex03.

<h2>Access</h2>

To use STREAM or c_stream, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>Messages</h2>

See the streamlines man page for a description of all Streamlines error messages and/or informational messages.

<h2>See Also</h2>

Online: stgetc, stgeti, stgetr, stinit, streamlines, streamlines_params, strset, stsetc, stseti, stsetr, stuixy, stumsl, stumta, stumxy, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

---
title: "ncl_stumsl(3)"
name: "ncl_stumsl"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_stumsl/"
---

STUMSL - This routine is the user-definable external subroutine used to draw masked streamlines. The default version of the routine draws any polyline all of whose area identifiers are greater than or equal to zero.

<h2>Synopsis</h2>

CALL STUMSL (XCS,YCS,NCS,IAI,IAG,NAI)

<h2>Description</h2>

<dl><dt>XCS
<dd>(REAL array, assumed size NCS, input): Array of X coordinates of the points defining the polyline with the given set of area identifiers.
<dt>YCS
<dd>(REAL array, assumed size NCS, input): Array of Y coordinates of the points defining the polyline with the given set of area identifiers.
<dt>NCS
<dd>(INTEGER, input): Number of points; assumed size of the X and Y coordinate arrays, XCS and YCS.
<dt>IAI
<dd>(INTEGER array, assumed size NAI, input): Array of area identifier values. Each value represents the area identifier with respect to the area group in the area group array with the same array index.
<dt>IAG
<dd>(INTEGER array, assumed size NAI, input): Array of area- identifier groups.
<dt>NAI
<dd>(INTEGER, input): Number of area identifier groups. The current version of Streamlines supports up to 64 area groups.</dl>

<h2>Usage</h2>

'STUMSL' is the name given to the default version of the masked streamline drawing routine, and it is also the name given to the argument through which the external subroutine is passed to STREAM. However, you may choose any acceptable FORTRAN identifier as the name of a user-defined version of the routine. The substitute routine must have an argument list equivalent to the default version of STUMSL. Also, whether or not the default version is used, the subroutine that calls STREAM should contain an external declaration of the routine, such as: 

<dl><dd>EXTERNAL STUMSL</dl>
 

 If the MSK parameter is greater than 0, signifying that masking is to be performed, Streamlines sends one or more sets of X and Y polyline coordinate arrays to the area masking routine, ARDRLN, for each streamline. ARDRLN subdivides the polyline into pieces such that each smaller polyline has a single area identifier with respect to each area identifier group, then makes a call to STUMSL for each polyline piece. While the default version of STUMSL only checks to see that none of the area identifiers are negative, a user-defined version could perform more complicated decision processing based on knowledge of the meaning of specific area identifier groups and/or area identifier values. Note that, before invoking STUMSL, ARDRLN modifies the user coordinate space by making the following calls: 

 CALL GETSET(VPL,VPR,VPB,VPT,WDL,WDR,WDB,WDT,LLG) CALL SET(VPL,VPR,VPB,VPT,VPL,VPR,VPB,VPT,1) 

 These calls temporarily turn the user to NDC mapping into an identity, allowing the user to call any of the routines, CURVE, CURVED, or the GKS routine GPL, to render the polygon piece without worrying about a possible non-identity mapping between user and world coordinates. 

 The current version of Streamlines supports masked drawing with up to 64 area groups. Streamlines will exit with an error message if an area map with more than 64 groups is passed to it.

<h2>Access</h2>

To use STUMSL, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: stgetc, stgeti, stgetr, stinit, stream, streamlines, streamlines_params, strset, stsetc, stseti, stsetr, stuixy, stumta, stumxy, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

---
title: "ncl_cpmpxy(3)"
name: "ncl_cpmpxy"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_cpmpxy/"
---

CPMPXY - Maps Conpack output from a rectangular coordinate system superimposed on the data grid to some other coordinate system. 

<h2>Synopsis</h2>CALL CPMPXY (IMAP, XINP, YINP, XOTP, YOTP)
<h2>Description</h2><dl COMPACT><dt>IMAP
<dd>(INTEGER, input) is zero if the object of the call is to ask CPMPXY about its mapping capabilities, greater than zero if the object of the call is to do a forward mapping, and less than zero if the object of the call is to do an inverse mapping. When IMAP is non-zero, its absolute value matches the current value of the parameter 'MAP' and identifies the mapping to be used.
<dt>XINP
<dd>(REAL, input) is used in one of three ways:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>When IMAP is zero, the value INT(XINP) is the index of a mapping about which CPMPXY is being asked to supply information.
<dt>&bull;
<dd>When IMAP is greater than zero, XINP is the X coordinate of a point on the contour plot. If 'XC1' = 'XCM' (the default situation), then XINP will lie in the range from 1 to M, where M is the first dimension of the array being contoured (equal to the value of the parameter 'ZDM'); in this case, the X coordinate will have the same range as the first index of the data array. If the user sets 'XC1' unequal to 'XCM', then XINP will lie in the range from 'XC1' (corresponding to an index value of 1) to 'XCM' (corresponding to an index value of M).
<dt>&bull;
<dd>When IMAP is less than zero, XINP is the X coordinate of a point on the contour plot, in a coordinate system consistent with the current window, as specified by arguments 5 through 8 of the last call to the SPPS routine SET or by the equivalent call to GKS.</dl></dl><dt>YINP
<dd>(REAL, input/output) is used in one of three ways:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>When IMAP is zero, CPMPXY is expected to return one of the following values of YINP: YINP = 0. indicates that neither the forward nor the inverse transformation is defined. YINP = 1. indicates that the forward transformation is defined, but the inverse is not. YINP = 2. indicates that the forward transformation is not defined, but the inverse is. YINP = 3. indicates that both the forward and the inverse transformations are defined.
<dt>&bull;
<dd>When IMAP is greater than zero, YINP is the Y coordinate of a point on the contour plot. If 'YC1' = 'YCN' (the default situation), then YINP will lie in the range from 1 to N, where N is the second dimension of the array being contoured (equal to the value of the parameter 'ZDN'); in this case, the Y coordinate will have the same range as the second index of the data array. If the user sets 'YC1' unequal to 'YCN', then YINP will lie in the range from 'YC1' (corresponding to an index value of 1) to 'YCN' (corresponding to an index value of N).
<dt>&bull;
<dd>When IMAP is less than zero, YINP is the Y coordinate of a point on the contour plot, in a coordinate system consistent with the current window, as specified by arguments 5 through 8 of the last call to the SPPS routine SET or by the equivalent call to GKS.</dl></dl><dt>XOTP and YOTP
<dd>(REAL, output) are used in one of two ways:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>If IMAP is greater than zero, XOTP and YOTP are the X and Y coordinates of a point on the contour plot, in a coordinate system consistent with the current window, as specified by arguments 5 through 8 of the last call to the SPPS routine SET or by the equivalent call to GKS.
<dt>&bull;
<dd>When IMAP is less than zero, XOTP and YOTP are the X and Y coordinates of a point on the contour plot. If 'XC1' = 'XCM' (the default situation), then XOTP will lie in the range from 1 to M, where M is the first dimension of the array being contoured (equal to the value of the parameter 'ZDM'); in this case, the X coordinate will have the same range as the first index of the data array. If the user sets 'XC1' unequal to 'XCM', then XOTP will lie in the range from 'XC1' (corresponding to an index value of 1) to 'XCM' (corresponding to an index value of M). Similarly, if 'YC1' = 'YCN' (the default situation), then YOTP will lie in the range from 1 to N, where N is the second dimension of the array being contoured (equal to the value of the parameter 'ZDN'); in this case, the Y coordinate will have the same range as the second index of the data array. If the user sets 'YC1' unequal to 'YCN', then YOTP will lie in the range from 'YC1' (corresponding to an index value of 1) to 'YCN' (corresponding to an index value of N). 

 In any case, if the point (XINP,YINP) cannot be mapped for any reason, some recognizable impossible value should be returned for both of XOTP and YOTP and the internal parameter 'ORV' should be given that value, thereby allowing Conpack routines that call CPMPXY to determine whether or not a point being projected is visible or not. The value used for this purpose by the Ezmap routines MAPTRA and MAPTRI is 1.E12.</dl></dl>
</dl><h2>Usage</h2>CPMPXY is not to be called by the user. It is called by Conpack when the parameter 'MAP' is non-zero. Each call is intended 1) to inquire whether a given mapping is defined by CPMPXY, or 2) to map the X and Y coordinates of a single point, whose position is known relative to the data grid, to X and Y coordinates in some other coordinate system or 3) (as of version 3.1.3) to do the inverse mapping. The default version of CPMPXY is as follows: 

<dl COMPACT><dd><pre>SUBROUTINE CPMPXY (IMAP,XINP,YINP,XOTP,YOTP)
 IF (IMAP.EQ.0) THEN
 IF (INT(XINP).GE.1.AND.INT(XINP).LE.3) THEN
 YINP=3.
 ELSE
 YINP=0.
 END IF
 ELSE IF (ABS(IMAP).EQ.1) THEN
 IF (IMAP.GT.0) THEN
 CALL MAPTRA (YINP,XINP,XOTP,YOTP)
 ELSE
 CALL MAPTRI (XINP,YINP,YOTP,XOTP)
 END IF
 ELSE IF (ABS(IMAP).EQ.2) THEN
 IF (IMAP.GT.0) THEN
 XOTP=XINP*COS(.017453292519943*YINP)
 YOTP=XINP*SIN(.017453292519943*YINP)
 ELSE
 XOTP=SQRT(XINP*XINP+YINP*YINP)
 YOTP=57.2957795130823*ATAN2(YINP,XINP)
 END IF
 ELSE
 XOTP=XINP
 YOTP=YINP
 END IF
 RETURN
END
</dl>
When CPMPXY is called with IMAP = 0, it assumes it is being 
asked to return information about its mapping capabilities. 
XINP is assumed to have been given the value REAL(I), where 
I is the index of a mapping about which information is 
desired. CPMPXY sets YINP to indicate whether the mapping 
selected by I is implemented or not and whether its inverse 
is implemented or not. In the case of the default version 
of CPMPXY, mappings 1 through 3 are completely implemented 
(both forward and reverse), so a &quot;3.&quot; is returned as the 
value of YINP; other mappings are not implemented at all, 
so a &quot;0.&quot; is returned as the value of YINP.
When CPMPXY is called with IMAP = 1, the incoming X and Y 
coordinates are assumed to represent longitude and 
latitude, respectively; the Ezmap routine MAPTRA is called 
to find the X and Y coordinates of the projection of the 
specified point on the globe, and those coordinates are 
returned as the outgoing X and Y coordinates. When IMAP = 
-1, the incoming X and Y coordinates are assumed to be the X 
and Y coordinates of a projected point; the Ezmap routine 
MAPTRI is called to find the longitude and latitude of the 
original point on the globe, and those values are returned 
as the outgoing X and Y coordinates.
When IMAP = 2, the incoming X and Y coordinates are assumed 
to represent rho and theta (in degrees) in polar 
coordinates; from these are computed the output X and Y 
coordinates. When IMAP = -2, the incoming X and Y 
coordinates are used to compute rho and theta and those 
values are returned.
If IMAP is anything else, the input X and Y coordinates are 
simply returned as the output X and Y coordinates.
A user version of CPMPXY can be made to do any desired 
mapping. It should also be made, when IMAP = 0, to return 
correct information about its own capabilities.</pre><h2>Access</h2>To use CPMPXY, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: conpack, cpback, cpchcf, cpchcl, cpchhl, cpchil, cpchll, cpcica, cpclam, cpcldm, cpcldr, cpcltr, cpcnrc, cpdrpl, cpezct, cpgetc, cpgeti, cpgetr, cplbam, cplbdr, cpmviw, cpmvrw, cppkcl, cppklb, cprect, cprset, cpscae, cpsetc, cpseti, cpsetr, cpsps1, cpsps2, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.

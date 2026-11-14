---
title: "ncl_stuixy(3)"
name: "ncl_stuixy"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_stuixy/"
---

STUIXY - Inversely maps a single point on the streamline from user to data coordinate space.

<h2>Synopsis</h2>

CALL STUIXY (XUS,YUS,XDA,YDA,IST)

<h2>Description</h2>

<dl><dt>XUS
<dd>(REAL, input): The X coordinate of a point in the user coordinate system.
<dt>YUS
<dd>(REAL, input): The Y coordinate of a point in the user coordinate system.
<dt>XDA
<dd>(REAL, output): The X coordinate of the point in the data coordinate system.
<dt>YDA
<dd>(REAL, output): The Y coordinate of the point in the data coordinate system.
<dt>IST
<dd>(REAL, output): Status of the mapping operation: 0 indicates success, negative values indicate that the mapping failed; positive values are reserved and should not be used by the implementor of a mapping routine.</dl>

<h2>Usage</h2>

STUIXY is a user-modifiable routine provided to support custom mappings of the data coordinate space. The user does not invoke it directly. Instead, whenever the parameter MAP specifies a mapping not handled by Streamlines internally (i.e., when MAP is set to a value other than 0, 1, or 2), Streamlines calls STUIXY once for each incremental step in the creation of a streamline. The default version of STUIXY simply performs an identity mapping. In order to implement a custom mapping, you must pick a unique mapping code (a positive integer greater than 2), and then modify each of the three routines, STUMXY, STUIXY, and STUMTA to recognize and respond consistently to the chosen code. In the standard distribution of NCAR Graphics, these three routines reside in a single file, 'stumxy.f'. STUMXY maps a point from data to user coordinate space, STUIXY inversely maps a point from user to data coordinate space, and STUMTA, which is likely to be the most difficult to implement, finds the tangent angle of the streamline at a point in NDC space. 

 STUIXY has access to a common block called STMAP that contains a number of variables used to record the current transformation state. In order to accommodate a variety of mapping implementations, STMAP provides more information than normally required. Consider the values stored in STMAP as strictly read-only. One essential member of this common block is IMAP, which contains the value currently assigned to the MAP parameter. 

 In STUIXY, the implementor of a custom mapping needs to add code of the form:
<dl><dd><pre>IF (IMAP .EQ. &lt;chosen_map_code&gt;) THEN
 ...map XUS to XDA
 ...map YUS to YDA
 ...if error, set IST to a negative value
 RETURN
ENDIF</pre></dl>
 

 Note that after the return from STUIXY, Streamlines checks to ensure that XDA and YDA are within the current boundaries of the data coordinate system. 

 When implementing a custom mapping, you may wish to look at the coding of the pre-defined mappings (0, identity mapping; 1, Ezmap projections; and 2, polar coordinate mapping) in the file 'stmpxy.f'. For these mappings, the subroutine STIMXY is the equivalent of STUIXY; it has an identical interface and may serve as a model for your implementation.

<h2>Access</h2>

To use STUIXY, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: stgetc, stgeti, stgetr, stinit, stream, streamlines, streamlines_params, strset, stsetc, stseti, stsetr, stumsl, stumta, stumxy, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

---
title: "ncl_seti(3)"
name: "ncl_seti"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_seti/"
---

SETI - sets the exponents which define the plotting range in the plotter address unit coordinate system.

<h2>Status</h2>

Plotter Address Units (PAUs) are no longer used in NCAR Graphics; thus, SETI is considered an obsolete routine. 

 The current recognized coordinate systems are GKS world coordinates, GKS normalized device coordinates, NCAR Graphics fractional coordinates, and NCAR Graphics user coordinates. See the NCAR Graphics document &quot;NCAR Graphics Fundamentals, UNIX Version&quot; for a description of these coordinate systems. 

 SETI continues to be provided for compatibility of early NCAR Graphics codes. 

 The following definition of the PAU Coordinate System is included for the purpose of interpreting and converting PAU codes: 

 The plotter coordinates of a point are integers IPX and IPY, where IPX is between 1 and 2**MX and IPY is between 1 and 2**MY. MX and MY are internal parameters of SPPS; each has the default value 10. Values of MX and MY can be set by routine SETI and retrieved by routine GETSI.

<h2>Synopsis</h2>

CALL SETI (IX,IY)

<h2>Description</h2>

<dl><dt>IX
<dd>(an input expression of type INTEGER) is the X axis exponent for plotter coordinates defining a range of 1 to 2**IX - 1. IX has a default value of 10.
<dt>IY
<dd>(an input expression of type INTEGER) is the Y axis exponent for plotter coordinates defining a range of 1 to 2**IY - 1. IY has a default value of 10.</dl>

<h2>Access</h2>

To use SETI, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: spps, getsi 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

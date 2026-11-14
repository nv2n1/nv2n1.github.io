---
title: "ncl_areas(3)"
name: "ncl_areas"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_areas/"
---

Areas - A set of routines allowing you to create an area map from a set of edges and then to use the area map for various purposes. 

<h2>Synopsis</h2>ARINAM - Initializes an area map. 
 AREDAM - Adds edges to an area map. 
 ARMVAM - Moves an area map from one integer array to another. 
 ARPRAM - Preprocesses an area map. 
 ARSCAM - Obtains definitions of areas created by edges in an area map. 
 ARDRLN - Draws a polyline masked by a given area map. 
 ARGTAI - Gets area identifiers associated with a given point. 
 ARGETI - Retrieves the integer value of an Areas parameter. 
 ARGETR - Retrieves the real value of an Areas parameter. 
 ARSETI - Provides a new integer value for an Areas parameter. 
 ARSETR - Provides a new real value for an Areas parameter. 
 ARDBPA - Produces a picture of a specified portion of the area map.
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 c_arinam 
 c_aredam 
 c_arpram 
 c_arscam 
 c_ardrln 
 c_argtai 
 c_argeti 
 c_arseti 
 c_ardbpa
<h2>Access</h2>To use the Areas Fortran or C routines, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>When error conditions are detected, the support routine SETER is called. By default, SETER writes a message to the standard error file (as defined by <a HREF="/docs/linux/man/4-i1mach/">I1MACH</a>(4)) and then terminates execution. It is possible to put SETER into recovery mode and regain control after a recoverable error (which includes all of the possible errors). 

 The possible error messages are listed below. All errors are recoverable in the sense that a user program which has called ENTSR to set recovery mode will get control back after one of these errors occurs. 

 ARDBDA - UNCLEARED PRIOR ERROR 
 ARDBPA - BAD POINTERS IN AREA MAP 
 ARDBPA - ERROR EXIT FROM GQPLCI 
 ARDBPA - ERROR EXIT FROM GQTXCI 
 ARDBPA - INITIALIZATION DONE IMPROPERLY 
 ARDBPA - UNCLEARED PRIOR ERROR 
 ARDRLN - ALGORITHM FAILURE 
 ARDRLN - INITIALIZATION DONE IMPROPERLY 
 ARDRLN - MAI TOO SMALL 
 ARDRLN - UNCLEARED PRIOR ERROR 
 AREDAM - AREA-MAP ARRAY OVERFLOW 
 AREDAM - INITIALIZATION DONE IMPROPERLY 
 AREDAM - UNCLEARED PRIOR ERROR 
 ARGETI - PARAMETER NAME NOT KNOWN - X 
 ARGETI - PARAMETER NAME TOO SHORT - X 
 ARGETI - UNCLEARED PRIOR ERROR 
 ARGETR - PARAMETER NAME NOT KNOWN - X 
 ARGETR - PARAMETER NAME TOO SHORT - X 
 ARGETR - UNCLEARED PRIOR ERROR 
 ARGTAI - ALGORITHM FAILURE 
 ARGTAI - INITIALIZATION DONE IMPROPERLY 
 ARGTAI - MAI TOO SMALL 
 ARGTAI - UNCLEARED PRIOR ERROR 
 ARINAM - AREA-MAP ARRAY IS TOO SMALL 
 ARINAM - UNCLEARED PRIOR ERROR 
 ARINIT - VALUE OF 'LC' IS TOO LARGE 
 ARMPIA - MULTIPLE-PRECISION QUANTITY IS TOO BIG 
 ARMVAM - INITIALIZATION DONE IMPROPERLY 
 ARMVAM - NEW AREA-MAP ARRAY IS TOO SMALL 
 ARMVAM - UNCLEARED PRIOR ERROR 
 ARPRAM - ALGORITHM FAILURE 
 ARPRAM - AREA-MAP ARRAY OVERFLOW 
 ARPRAM - INITIALIZATION DONE IMPROPERLY 
 ARPRAM - NO EDGES IN AREA MAP 
 ARPRAM - UNCLEARED PRIOR ERROR 
 ARSCAM - ALGORITHM FAILURE 
 ARSCAM - AREA-MAP ARRAY OVERFLOW 
 ARSCAM - INITIALIZATION DONE IMPROPERLY 
 ARSCAM - MAI TOO SMALL 
 ARSCAM - MCS TOO SMALL 
 ARSCAM - UNCLEARED PRIOR ERROR 
 ARSETI - PARAMETER NAME NOT KNOWN - X 
 ARSETI - PARAMETER NAME TOO SHORT - X 
 ARSETI - UNCLEARED PRIOR ERROR 
 ARSETR - PARAMETER NAME NOT KNOWN - X 
 ARSETR - PARAMETER NAME TOO SHORT - X 
 ARSETR - UNCLEARED PRIOR ERROR 

<h2>See Also</h2>Online: areas_params, ardbpa, ardrln, aredam, argeti, argetr, argtai, arinam, armvam, arpram, arscam, arseti, arsetr, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

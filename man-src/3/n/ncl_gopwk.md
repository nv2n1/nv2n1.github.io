---
title: "ncl_gopwk(3)"
name: "ncl_gopwk"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gopwk/"
---

GOPWK (Open workstation) - opens a GKS workstation.
<h2>Synopsis</h2>CALL GOPWK (WKID, CONID, WKTYPE)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void gopen_ws(Gint ws_id, const char *conn_id, Gint ws_type);
<h2>Description</h2><dl COMPACT><dt>WKID
<dd>(Integer, Input) - A number assigned to a workstation as an identifier that is to be used in all subsequent calls to GKS functions that require a workstation identifier. In NCAR GKS, WKID can be any non-negative integer.
<dt>CONID
<dd>(Integer, Input) - A connection identifier that has different meanings for different workstation types (see the USAGE section below).
<dt>WKTYPE
<dd>(Integer, Input) - An identifier specifying the specific type of output device targeted. Each GKS package has an implementation-dependent set of workstation types that the package supports. The legal workstation types in NCAR GKS are:
<dt> 1
<dd>- NCGM
<dt> 3
<dd>- WISS
<dt> 7
<dd>- pre-existing X11 window.
<dt> 8
<dd>- non-existing X11 window.
<dt> 10
<dd>- text dump of graphics output.
<dt> 11
<dd>- PDF in portrait mode.
<dt> 12
<dd>- PDF in landscape mode.
<dt> 20
<dd>- color PostScript in portrait mode.
<dt> 21
<dd>- color Encapsulated PostScript (EPS) in portrait mode.
<dt> 22
<dd>- color Encapsulated PostScript Interchange format (EPSI) in portrait mode.
<dt> 23
<dd>- monochrome PostScript in portrait mode.
<dt> 24
<dd>- monochrome Encapsulated PostScript (EPS) in portrait mode.
<dt> 25
<dd>- monochrome Encapsulated PostScript Interchange format (EPSI) in portrait mode.
<dt> 26
<dd>- color PostScript in landscape mode.
<dt> 27
<dd>- color Encapsulated PostScript (EPS) in landscape mode.
<dt> 28
<dd>- color Encapsulated PostScript Interchange format (EPSI) in landscape mode.
<dt> 29
<dd>- monochrome PostScript in landscape mode.
<dt> 30
<dd>- monochrome Encapsulated PostScript (EPS) in landscape mode.
<dt> 31
<dd>- monochrome Encapsulated PostScript Interchange format (EPSI) in landscape mode.</dl><h2>Usage</h2>For workstation types of 1 (CGM) or 3 (WISS) the connection ID is used as a Fortran logical unit number. One can have at most one workstation of type 1 open at a time and this also applies to workstations of type 3. One can have workstations of types 1 and 3 open simultaneously and they must have distinct connection IDs. To use the GFLASH package or any GKS segmentation functions WISS must be opened first. 

 For workstations of type 7 the connection ID is the X11 window ID for the existing window (obtained from xwininfo for example). 

 For workstations of type 8 an X11 window will be created at open workstation time. The connection ID is irrelevant for workstations of type 8. 

 For workstations of type 10, the ASCII text is written to standard output and the connection ID is irrelevant. 

 There can be a maximum of fifteen simultaneously open workstations of all types.
<h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gopks, gacwk, gdawk, gclwk, gclks, opngks, clsgks, gopen_ws 

 Hardcopy: User's Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

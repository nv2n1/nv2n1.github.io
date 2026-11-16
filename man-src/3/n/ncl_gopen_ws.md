---
title: "ncl_gopen_ws(3)"
name: "ncl_gopen_ws"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gopen_ws/"
description: "gopen_ws (Open workstation) – opens a GKS workstation."
---

<p>gopen_ws (Open workstation) &#8211; opens a GKS workstation.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void gopen_ws(Gint ws_id, const char *conn_id, Gint ws_type);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>ws_id</dt>
<dd>(Input) &#8211; A number assigned to a workstation as an identifier that is to be used in all subsequent calls to GKS functions that require a workstation identifier. In NCAR GKS, ws_id can be any non-negative integer.</dd>
<dt>conn_id</dt>
<dd>(Input) &#8211; A connection identifier that has different meanings for different workstation types (see the USAGE section below).</dd>
<dt>ws_type</dt>
<dd>(Input) &#8211; An identifier specifying the specific type of output device targeted. Each GKS package has an implementation-dependent set of workstation types that the package supports. The legal workstation types in NCAR GKS are:</dd>
<dt> 1</dt>
<dd>&#8211; NCGM</dd>
<dt> 3</dt>
<dd>&#8211; WISS</dd>
<dt> 7</dt>
<dd>&#8211; pre-existing X11 window.</dd>
<dt> 8</dt>
<dd>&#8211; non-existing X11 window.</dd>
<dt> 10</dt>
<dd>&#8211; text dump of graphics output.</dd>
<dt> 11</dt>
<dd>&#8211; PDF in portrait mode.</dd>
<dt> 12</dt>
<dd>&#8211; PDF in landscape mode.</dd>
<dt> 20</dt>
<dd>&#8211; color PostScript in portrait mode.</dd>
<dt> 21</dt>
<dd>&#8211; color Encapsulated PostScript (EPS) in portrait mode.</dd>
<dt> 22</dt>
<dd>&#8211; color Encapsulated PostScript Interchange format (EPSI) in portrait mode.</dd>
<dt> 23</dt>
<dd>&#8211; monochrome PostScript in portrait mode.</dd>
<dt> 24</dt>
<dd>&#8211; monochrome Encapsulated PostScript (EPS) in portrait mode.</dd>
<dt> 25</dt>
<dd>&#8211; monochrome Encapsulated PostScript Interchange format (EPSI) in portrait mode.</dd>
<dt> 26</dt>
<dd>&#8211; color PostScript in landscape mode.</dd>
<dt> 27</dt>
<dd>&#8211; color Encapsulated PostScript (EPS) in landscape mode.</dd>
<dt> 28</dt>
<dd>&#8211; color Encapsulated PostScript Interchange format (EPSI) in landscape mode.</dd>
<dt> 29</dt>
<dd>&#8211; monochrome PostScript in landscape mode.</dd>
<dt> 30</dt>
<dd>&#8211; monochrome Encapsulated PostScript (EPS) in landscape mode.</dd>
<dt> 31</dt>
<dd>&#8211; monochrome Encapsulated PostScript Interchange format (EPSI) in landscape mode.</dd></dl>
<h2>Usage</h2>
<p>For workstation types of 1 (CGM) the connection ID is the name of the CGM file. One can have at most one workstation of type 1 open at a time. </p>
<p> For workstations of type 3 (WISS) the connection ID is irrelevant. One can have at most one workstation of type 3 open. One can have workstations of types 1 and 3 open simultaneously and they must have distinct connection IDs. To use the GFLASH package or any GKS segmentation functions WISS must be opened first. </p>
<p> For workstations of type 7 the connection ID is the X11 window ID for the existing window. This number should be passed as a string; for example, &quot;3&quot; for an X11 window ID of 3. </p>
<p> For workstations of type 8 an X11 window will be created at open workstation time. The connection ID is irrelevant for workstations of type 8. </p>
<p> For workstations of type 10, the ASCII text is written to standard output and the connection ID is irrelevant. </p>
<p> There can be a maximum of fifteen simultaneously open workstations of all types.</p>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>gopen_gks(3NCARG),</code> <code>gactivate_ws(3NCARG),</code> <code>gdeactivate_ws(3NCARG),</code> <code>gclose_ws(3NCARG),</code> <code>gclose_gks(3NCARG),</code> <code>opngks(3NCARG),</code> <code>clsgks(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>

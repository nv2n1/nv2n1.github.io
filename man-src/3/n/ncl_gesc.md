---
title: "ncl_gesc(3)"
name: "ncl_gesc"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gesc/"
---

GESC (Escape) - provides a standard way of implementing nonstandard GKS features. NCAR GKS has only two user-accessible escape functions defined: one for changing the name of a metafile and another for pausing in an X window.
<h2>Synopsis</h2>CALL GESC (FCTID, LIDR, IDR, MXODR, LODR, ODR)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void gescape(Gint func_id, const Gescape_in_data *in_data, Gstore *store_data,Gescape_out_data **out_data);
<h2>Description</h2><dl COMPACT><dt>FCTID
<dd>(Integer, Input) - A function identifier specifying the requested activity. The legal values for FCTID are &quot;-1391&quot; for changing a metafile name and &quot;-1396&quot; for effecting a pause in an X window.
<dt>LIDR
<dd>(Integer, Input) - Dimension of the IDR input data record array (for IDR, see below).
<dt>IDR
<dd>(Character * 80 Array, Input) - Input data record. For calls to GESC with FCTID equal to -1391 the input data record should contain the desired metafile name left justified and blank filled; for calls to GESC with FCTID equal to -1396 the input data record should contain the workstation identifier encoded as a five character number.
<dt>MXODR
<dd>(Integer, Input) - Maximum length of the ODR output data record array (for ODR, see below).
<dt>LODR
<dd>(Integer, Output) - Dimension of the ODR output data record array.
<dt>ODR (MXODR)
<dd>(Character * 80 Array, Output) - Output data record.</dl><h2>Usage</h2>LIDR, MXODR, and LODR must always be at least &quot;1&quot; in value.
<h2>Examples</h2>GESC can be used to dynamically change the name of an output metafile and to do so one should use the calls GOPKS and GOPWK instead of OPNGKS. If you are using OPNGKS, see the man page for SETUSV for changing the name of the metafile. 

 To change the name of the output metafile inside your program, you should make a call similar to the following: <pre> CHARACTER*80 MFNAME
 CALL GOPKS (6,IDUM)
 MFNAME = 'new.cgm.name'
 CALL GESC(-1391,1,MFNAME,1,1,CDUM)</pre>The call to GESC to change the metafile name must always occur just before the call to GOPWK that opens a CGM workstation. Setting the environment variable NCARG_GKS_OUTPUT overrides any attempt to change the name of an output metafile via a GESC call. 

 See the &quot;User's Guide for NCAR GKS-0A Graphics&quot; for a more complete example of changing metafile names from within a code. 

 Here is an example of a code that will create an X window, draw a line, and then pause waiting for a mouse click or a key click. <pre> CHARACTER*80 IREC,ODUM
 CALL GOPKS(6,0)
 CALL GOPWK(3,0,8)
 CALL <a HREF="//www.systutorials.com/docs/linux/man/3-GACWK/">GACWK</a>(3)
 CALL LINE(0.,0.,1.,1.)
 CALL SFLUSH
 IREC = ' 3'
 CALL GESC(-1396,1,IREC,1,1,ODUM)
 CALL <a HREF="//www.systutorials.com/docs/linux/man/3-GDAWK/">GDAWK</a>(3)
 CALL <a HREF="//www.systutorials.com/docs/linux/man/3-GCLWK/">GCLWK</a>(3)
 CALL GCLKS
 STOP
 END</pre>The functions FRAME and NGPICT are in general much easier to use and more flexible than the direct ESCAPE call for pausing in an X window. It is suggested that those functions be used.
<h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: SETUSV, FRAME, NGPICT, gescape 

 Hardcopy: User's Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

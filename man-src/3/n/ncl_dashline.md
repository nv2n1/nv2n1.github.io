---
title: "ncl_dashline(3)"
name: "ncl_dashline"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_dashline/"
---

Dashline - A set of line-drawing routines that can be used to generate various dashed line patterns (including solid), can add labels to the lines, can smooth the lines, and can suppress crowding of lines. There are four different versions of Dashline: &quot;normal&quot;, &quot;quick&quot;, &quot;smooth&quot;, and &quot;super&quot;. See the ACCESS Section for details on how to invoke the various versions. 

<h2>Synopsis</h2><dl COMPACT><dt>DASHDB -
<dd>Defines a dash pattern without labels.
<dt>DASHDC -
<dd>Defines a dash pattern with labels. If DASHDC is called when the &quot;quick&quot; version of Dashline is used, an error exit results.
<dt>FRSTD -
<dd>Defines the first of a sequence of points through which a curve is to be drawn.
<dt>VECTD -
<dd>Defines the second and following of a sequence of points through which a curve is to be drawn.
<dt>LASTD -
<dd>Terminates a sequence of calls to draw a curve (a call to FRSTD followed by one or more calls to VECTD).
<dt>LINED -
<dd>Draws a straight line segment between two points.
<dt>CURVED -
<dd>Draws a curve through a sequence of points.
<dt>RESET -
<dd>The &quot;super&quot; version of RESET zeroes the internal integer array used to detect crowded lines; other versions do nothing.</dl><h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 c_dashdb 
 c_dashdc 
 c_frstd 
 c_vectd 
 c_lastd 
 c_lined 
 c_curved 
 c_reset
<h2>Usage</h2>The Dashline utility allows you to draw various kinds of lines. In all four versions of it (quick, normal, smooth and super), you can specify an arbitrary dash pattern for the lines (including a solid line). In all but the quick version, you can also add interspersed labels to the lines for purposes such as naming lines in an XY plot or assigning contour levels to contour lines. In the smooth and super versions, the lines can also be smoothed using splines under tension.
<dl COMPACT><dt>Warning:
<dd>You must be careful when using the smoothing option. Allowing a high degree of smoothing may have serious side effects, such as XY curves with multiple valued loops and contours which cross over other contours.</dl>
 

 The super version additionally allows for the culling of crowded lines. In order for the culling process to work properly, the routine RESET must be called at the beginning of each picture; when using other versions of Dashline, the calls to RESET may be left in, as they then do nothing.
<h2>Access</h2>To use the normal version of the Dashline utility, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order. Other optional libraries to create the quick, smooth, and super versions of Dashline are automatically linked in by the ncargf77 command. If you need to know the names of these libraries for a particular version of Dashline, execute an &quot;ncargf77&quot; command with the appropriate option and a dummy input file and examine the resulting command line that is echoed and executed. 

 To run a code called mycode.f which has one or more calls to Dashline entries, issue one of the commands: 

<dl COMPACT><dt>NORMAL
<dd>Command: &quot;ncargf77 mycode.f&quot; 

 The lines will be drawn as unsmoothed dashed or solid lines. DASHDC may be called to define a dash pattern with labels. 

<dt>QUICK
<dd>Command: &quot;ncargf77 -quick mycode.f&quot; 

 The lines will be drawn as unsmoothed dashed or solid lines. The dash pattern may not include labels. If DASHDC is called, an error exit will result; DASHDB must be used instead. 

<dt>SMOOTH
<dd>Command: &quot;ncargf77 -smooth mycode.f&quot; 

 The lines will be drawn as dashed or solid lines, smoothed using splines under tension. DASHDC may be called to define a dash pattern with labels. 

<dt>SUPER
<dd>Command: &quot;ncargf77 -super mycode.f&quot; 

 The lines will be drawn as dashed or solid lines, smoothed using splines under tension. DASHDC may be called to define a dash pattern with labels. Crowded lines will be thinned; in order for this to work properly, you must remember to call RESET at the beginning of each picture.</dl><h2>Messages</h2>When error conditions are detected, the support routine SETER is called in such a way that it writes a message to the standard error file (as defined by <a HREF="/docs/linux/man/4-i1mach/">I1MACH</a>(4)) and then terminates execution. The possible error messages are as follows:
<dl COMPACT><dt>CFVLD -- VECTD CALL OCCURS BEFORE A CALL TO FRSTD
<dd>You must call FRSTD before the first call to VECTD.
<dt>DASHDB -- BLOCKDATA DASHBD APPARENTLY NOT LOADED CORRECTLY
<dd>If you have used the ncargf77 command options as discussed in the ACCESS Section, see your system administrator.
<dt>DASHDC -- BLOCKDATA DASHBD APPARENTLY NOT LOADED CORRECTLY
<dd>You have called DASHDC when using the &quot;quick&quot; version of Dashline. This is not allowed.
<dt>FDVDLD -- VECTD CALL OCCURS BEFORE A CALL TO FRSTD
<dd>You must call FRSTD before the first call to VECTD.</dl><h2>See Also</h2>Online: dashline_params, curved, dashdb, dashdc, frstd, lastd, lined, reset, vectd, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial; NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

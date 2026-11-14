---
title: "ncl_ngpict(3)"
name: "ncl_ngpict"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ngpict/"
---

NGPICT - Effects a break in the picture drawing sequence in a FORTRAN code using GKS. The actions taken depend on whether the designated workstation is a metafile or an output/input workstation. An option is provided for prompting the user when an output/input workstation is ready and waiting after a pause.

<h2>Synopsis</h2>

CALL NGPICT(WKID,ACTION)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_ngpict(int wkid, int action)

<h2>Description</h2>

<dl><dt>WKID
<dd>(an input parameter of type INTEGER) which designates the workstation identifier of a workstation as it was specified in a GOPWK call.
<dt>ACTION
<dd>(an input parameter of type INTEGER) the value of which specifies the action to be taken on the workstation WKID. Legal values are:
<dl><dd><dl><dt>0
<dd>Execute an UPDATE WORKSTATION on WKID.
<dt>1
<dd>Execute an UPDATE WORKSTATION followed by a CLEAR WORKSTATION.
<dt>2
<dd>Execute an UPDATE WORKSTATION followed by a pause waiting for a mouse click or a key click.
<dt>3
<dd>Execute an UPDATE WORKSTATION followed by a pause followed by a CLEAR WORKSTATION after the pause has been terminated by a mouse click or a key click.
<dt>4
<dd>Same as 3 except a &quot;&lt;READY&gt;&quot; prompt is issued in the lower left corner of the window after the UPDATE WORKSTATION.</dl></dl>
</dl>

<h2>C-Binding Description</h2>

The C binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Usage</h2>

If WKID designates a metafile, then a CLEAR WORKSTATION is done which inserts an END PICTURE into the metafile. The result produced in this case would be the same as that resulting from a call to FRAME. The only valid actions for a metafile workstation are 0 and 1. 

 NGPICT is designed to be used when more precise control over individual workstations is desired than that offered by FRAME. This might be desirable, for example, when an application is controlling several simultaneously active workstations. To use NGPICT one should be opening GKS workstations with GOPWK rather than with OPNGKS.

<h2>Examples</h2>

If WKID=2 designates a metafile workstation, then <pre> CALL NGPICT(2,1)</pre>would duplicate the action of a FRAME call. 

 If WKID=2 designates an X11 workstation, then <pre> CALL NGPICT(2,4)</pre>would cause a pause in the X11 window and wait for a key click or a mouse click. A &quot;&lt;READY&gt;&quot; prompt, indicating that the window is waiting for a mouse click or a key click, would appear at the lower left of the X11 window after the window has been updated. After a mouse click in the X11 window, that window will be cleared before program execution continues.

<h2>Access</h2>

To use NGPICT or c_ngpict, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>Messages</h2>

Non-fatal errors are reported for values of ACTION out of range and for values of ACTION inappropriately applied to a metafile. Also, a non-fatal error is reported if NGPICT is called while a segment is open.

<h2>See Also</h2>

Online: frame(3NCARG), gflash(3NCARG), gopwk(3NCARG), opngks(3NCARG), gclrwk(3NCARG), gupwk(3NCARG), ncarg_cbind(3NCARG) 

 Online URL: <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/gks/gkshome.html">http://ngwww.ucar.edu/ngdoc/ng/gks/gkshome.html</a> 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial; NCAR Graphics Fundamentals, UNIX Version;

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

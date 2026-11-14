---
title: "ncl_ngmftc(3)"
name: "ncl_ngmftc"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ngmftc/"
---

NGMFTC - Temporarily closes a metafile output unit allowing for subsequent reopening.

<h2>Synopsis</h2>

CALL NGMFTC(WKID)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_ngmftc(int wkid)

<h2>Description</h2>

<dl><dt>WKID
<dd>(an input variable of type INTEGER) that specifies the GKS workstation ID to be temporarily closed.</dl>

<h2>C-Binding Description</h2>

The C binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Usage</h2>

Use NGMFTC to close a metafile temporarily for reopening with NGREOP. The temporary close can be done at any time after a metafile workstation has been opened, even in the middle of drawing a picture. The primary use of NGMFTC is to allow for writing to more than one metafile in a single job execution. Since NCAR GKS does not allow for having more than a single NCGM workstation open at a time, you can use NGMFTC to stop output to one metafile while you write to another metafile and then resume output to the initial metafile. 

 If you simply want to suspend output to a metafile workstation, but do not need to write to another metafile workstation, simply use the GKS entry GDAWK to deactivate the workstation and GOPWK to reactivate it when you want to resume output. 

 For saving the state of all primitive attribute values of an NCGM workstation at the time of the temporary close and restoring them at the time of the reopen with NGREOP, see the documenation for NGSRAT. 

 If NGMFTC is used and NGREOP is not subsequently invoked to reopen the file so that it can be terminated normally in the same job step, then an improperly terminated metafile will result from the temporary close.

<h2>Examples</h2>

Assuming that an NCGM workstation, with workstation identifier 1, is open, then <pre> CALL <a HREF="//www.systutorials.com/docs/linux/man/1-NGMFTC/">NGMFTC</a>(1)</pre>would temporarily close the workstation. 

 Use the ncargex command to see the following relevant example: pgkex27.

<h2>Access</h2>

To use NGMFTC or c_ngmftc, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>Messages</h2>

The argument to NGMFTC must be an NCGM workstation that is open but not active.

<h2>See Also</h2>

Online: ngsrat(3NCARG), ngreop(3NCARG), 

 Online URL: <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/gks/gkshome.html">http://ngwww.ucar.edu/ngdoc/ng/gks/gkshome.html</a> 

 Hardcopy:

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

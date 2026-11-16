---
title: "ncl_agchcu(3)"
name: "ncl_agchcu"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_agchcu/"
---

AGCHCU - Provides a way for the user to change the color, intensity, line style, etc., of curves drawn by Autograph. 

<h2>Synopsis</h2>SUBROUTINE AGCHCU (IFLG,KDSH)
<h2>Description</h2><dl COMPACT><dt>IFLG
</dt><dd>(an input expression of type INTEGER) is zero if a particular object is about to be drawn, non-zero if it has just been drawn.
</dd><dt>KDSH
</dt><dd>(an input expression of type INTEGER) is the value of AGCURV's last argument, as follows:
</dd><dl COMPACT><dd></dd><dl COMPACT><dt>AGCURV called by
</dt><dd>Value of KDSH
</dd><dt>EZY
</dt><dd>1
</dd><dt>EZXY
</dt><dd>1
</dd><dt>EZMY
</dt><dd>&quot;n&quot; or &quot;-n&quot;, where &quot;n &quot; is the curve number
</dd><dt>EZMXY
</dt><dd>&quot;n&quot; or &quot;-n&quot;, where &quot;n&quot; is the curve number
</dd><dt>the user program
</dt><dd>a user-specified value</dd></dl></dl>
</dl><h2>Usage</h2>This routine is not called by the user program, but by Autograph itself, just before and just after each curve is drawn. The default version does nothing. The user may supply his own version to change the color, intensity, line style, etc. of selected curves. 

 Note: A user version of AGCHCU should not call any other Autograph routine.
<h2>Access</h2>To use AGCHCU, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: autograph, agback, agbnch, agchax, agchil, agchnl, agcurv, agdshn, aggetc, aggetf, aggeti, aggetp, aggetr, agpwrt, agrstr, agsave, agsetc, agsetf, agseti, agsetp, agsetr, agstup, agutol, anotat, displa, ezmxy, ezmy, ezxy, ezy 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

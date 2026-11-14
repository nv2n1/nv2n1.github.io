---
title: "ncl_labelbar_params(3)"
name: "ncl_labelbar_params"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_labelbar_params/"
---

Labelbar_params - This document briefly describes all Labelbar internal parameters. 

<h2>Description</h2>Labelbar has six internal parameters, each of which affects the behavior of LBLBAR in a particular way. The current value of one of these parameters may be retrieved by calling either LBGETI or LBGETR and the value of one of them may be reset by calling either LBSETI or LBSETR. 

 Parameter descriptions, in alphabetical order, of all Labelbar internal parameters follow. Each description begins with a line giving the parameter name and the intrinsic FORTRAN type of the parameter.
<dl COMPACT><dt>'CBL' - Integer
<dd>Color of box lines. The default value is -1.
<dt>'CFL' - Integer
<dd>Color of fill lines. The default value is -1.
<dt>'CLB' - Integer
<dd>Color of labels. The default value is -1.
<dt>'WBL' - Real
<dd>Width of box lines. The default value is 0.
<dt>'WFL' - Real
<dd>Width of fill lines. The default value is 0.
<dt>'WLB' - Real
<dd>Width of label lines. The default value is 0.</dl>
 

 Each of the &quot;color&quot; parameters may be given a negative value to indicate that color is unspecified; in this case, the color of an object drawn will be that specified by the current polyline color index (in the case of box lines and fill lines) or the current text color index (in the case of labels). A value which is zero or greater specifies the color index to be used. 

 Each of the &quot;width&quot; parameters may be given a value of zero or less to indicate that line width is unspecified; in this case, the line width used to draw an object will be that specified by the current polyline width scale factor. Note that setting polyline width before drawing the labels does affect their appearance; this is because labels are drawn by calls to the routine PLCHHQ, which strokes out characters using lines.
<h2>See Also</h2>Online: lbgeti, lbgetr, lbseti, lbsetr 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

---
title: "ncl_gqchup(3)"
name: "ncl_gqchup"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gqchup/"
---

GQCHUP (Inquire character up vector) - retrieves the current value of the character up vector.
<h2>Synopsis</h2>CALL GQCHUP (ERRIND, CHUX, CHUY)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void ginq_char_up_vec(Gint *err_ind, Gvec *char_up_vec);
<h2>Description</h2><dl COMPACT><dt>ERRIND
<dd>(Integer, Output) - If the inquired values cannot be returned correctly, a non-zero error indicator is returned in ERRIND, otherwise a zero is returned. Consult &quot;User's Guide for NCAR GKS-0A Graphics&quot; for a description of the meaning of the error indicators.
<dt>CHUX
<dd>(Real, Output) - Gives the X world coordinate of a the up vector.
<dt>CHUY
<dd>(Real, Output) - Gives the Y world coordinate of a the up vector.</dl><h2>Usage</h2>The up vector is that vector formed by the two coordinate points (0.,0.) and (CHUX,CHUY). See GSCHUP for more details on the meaning of the character up vector.
<h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gtx, gstxp, gstxal, gstxfp, gschh, gschsp, gschup, gschxp, gscr, gstxci, gqtxp, gqtxal, gqtxfp, gqchh, gqchsp, gqchxp, plotchar, ginq_char_up_vec 

 Hardcopy: User's Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

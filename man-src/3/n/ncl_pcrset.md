---
title: "ncl_pcrset(3)"
name: "ncl_pcrset"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_pcrset/"
---

PCRSET - Resets all parameters to their initial default values.

<h2>Synopsis</h2>

CALL PCRSET

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_pcrset()

<h2>Description</h2>

PCRSET has no arguments.

<h2>Usage</h2>

Calling this routine restores all Plotchar parameters to their initial default values. For a complete list of parameters available in this utility, see the plotchar_params man page.

<h2>Examples</h2>

Currently, there are no examples for this routine.

<h2>Access</h2>

To use PCRSET or c_pcrset, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>Messages</h2>

See the plotchar man page for a description of all Plotchar error messages and/or informational messages.

<h2>See Also</h2>

Online: plotchar, plotchar_params, pcdlsc, pcgetc, pcgeti, pcgetr, pchiqu, pcloqu, pcmequ, pcmpxy, pcpnwi, pcsetc, pcseti, pcsetr, ncarg_cbind. 

 Hardcopy: None.

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

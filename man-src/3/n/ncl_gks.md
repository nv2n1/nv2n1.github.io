---
title: "ncl_gks(3)"
name: "ncl_gks"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gks/"
---

GKS - GKS (the Graphical Kernel System) is a set of low-level graphics functions that are standardized by the American National Standards Institute (ANSI) and the International Standards Institute (ISO). The collection of man pages in 3NCARG reflects those GKS functions documented in the NCAR UserDoc &quot;User's Guide for NCAR GKS-0A Graphics&quot;. This collection does not contain all of the functions in GKS-0A, but merely the most frequently used ones. NCAR GKS-0A does contain all of the functions required to be implemented by the GKS Standard.
<h2>Synopsis</h2><pre>GACTM - Accumulate transformation matrix.
GACWK - Activate workstation.
GCA - Cell array.
GCLKS - Close GSK.
GCLRWK - Clear workstation.
GCLSG - Close segment.
GCLWK - Close workstation.
GCRSG - Create segment.
GCSGWK - Copy segment to workstation.
GDAWK - Deactivate workstation.
GDSG - Delete segment.
GESC - Escape.
GEVTM - Evaluate transformation matrix.
GFA - Fill area.
GOPKS - Open GKS.
GOPWK - Open workstation.
GPL - Polyline.
GPM - Polymarker.
GQASF - Inquire aspect source flags.
GQCHH - Inquire character height.
GQCHSP - Inquire character spacing.
GQCHUP - Inquire character up vector.
GQCHXP - Inquire character expansion factor.
GQCLIP - Inquire clipping indicator.
GQCNTN - Inquire current normalization transformation number.
GQCR - Inquire color representation.
GQFACI - Inquire fill area color index.
GQFAIS - Inquire fill area interior style.
GQFASI - Inquire fill area style index.
GQLN - Inquire line type.
GQLWSC - Inquire linewidth scale factor.
GQMK - Inquire marker type.
GQMKSC - Inquire marker size scale factor.
GQMNTN - Inquire maximum normalization transformation number.
GQNT - Inquire normalization transformation.
GQOPS - Inquire operating state value.
GQOPSG - Inquire name of open segment.
GQPLCI - Inquire polyline color index.
GQPMCI - Inquire polymarker color index.
GQSGUS - Inquire set of segment names in use.
GQTXAL - Inquire text alignment.
GQTXCI - Inquire text color index.
GQTXFP - Inquire text font and precision.
GQTXP - Inquire text path.
GSASF - Set aspect source flags.
GSCHH - Set character height.
GSCHSP - Set character spacing.
GSCHUP - Set character up vector.
GSCHXP - Set character expansion factor.
GSCLIP - Set clipping indicator.
GSCR - Set color representation.
GSELNT - Select normalization transformation.
GSFACI - Set fill area color index.
GSFAIS - Set fill area interior style.
GSFASI - Set fill are style index.
GSLN - Set line type.
GSLWSC - Set linewidth scale factor.
GSMK - Set marker type.
GSMKSC - Set marker size scale factor.
GSPLCI - Polyline color index.
GSPMCI - (Set polymarker color index.
GSSGT - Set segment transformation.
GSTXAL - Set text alignment.
GSTXCI - Set text color index.
GSTXFP - Set text font and precision.
GSTXP - Set text path.
GSVP - Set viewport.
GSWN - Set window.
GTX - Text.
GUWK - Update workstation.</pre><h2>Access</h2>To use any of the functions in NCAR GKS, load the NCAR GKS library ncarg_gks.
<h2>Messages</h2>See the UserDoc &quot;User's Guide for NCAR GKS-0A Graphics&quot; for a complete list of error numbers and messages.
<h2>See Also</h2>Online: gactm, gacwk, gca, gclks, gclrwk, gclsg, gclwk, gcrsg, gcsgwk, gdawk, gdsg, gesc, gevtm, gfa, gopks, gopwk, gpl, gpm, gqasf, gqchh, gqchsp, gqchup, gqchxp, gqclip, gqcntn, gqcr, gqfaci, gqfais, gqfasi, gqln, gqlwsc, gqmk, gqmksc, gqmntn, gqnt, gqops, gqopsg, gqplci, gqpmci, gqsgus, gqtxal, gqtxci, gqtxfp, gqtxp, gsasf, gschh, gschsp, gschup, gschxp, gsclip, gscr, gselnt, gsfaci, gsfais, gsfasi, gsln, gslwsc, gsmk, gsmksc, gsplci, gspmci, gssgt, gstxal, gstxci, gstxfp, gstxp, gsvp, gswn, gtx, guwk 

 Hardcopy: &quot;User's Guide for NCAR GKS-0A Graphics&quot;; &quot;Computer Graphics--Graphical Kernel System (GKS) Functional Description, ANSI X3.124-1985&quot;
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

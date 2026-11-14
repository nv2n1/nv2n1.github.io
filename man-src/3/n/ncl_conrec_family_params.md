---
title: "ncl_conrec_family_params(3)"
name: "ncl_conrec_family_params"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_conrec_family_params/"
---

Conrec_family_params - Includes a brief description of all Conrec_family internal parameters. 

<h2>Description</h2>No parameter setting functions are available for the Conrec_family utility. Parameters were set through common blocks CONRE1 and CONRE4. There are three versions of the CONREC code. The normal version is in the standard NCAR Graphics library. The other two versions are in optional libraries one of which is linked when the ncargf77 option -quick, or -super is declared on the command line. 

 The CONREC and EZCNTR entries can be invoked in four different ways to create contour plots which vary considerably in appearance. The four variations include quick, normal, smooth, and super contour lines. This progression represents a tradeoff between speed of computation and the appearance of the contour plots. These variations are specified through selected command line options of the ncargf77 command. 

 For normal or smooth options the parameter set is: <pre> COMMON /CONRE1/ IOFFP ,SPVAL
 COMMON /CONRE4/ ISIZEL ,ISIZEM ,ISIZEP ,NREP ,
1 NCRT ,ILAB ,NULBLL ,IOFFD ,
2 EXT ,IOFFM ,ISOLID ,NLA ,
3 NLM ,XLT ,YBT ,SIDE</pre>For the quick option the parameter set is: <pre> COMMON /CONRE1/ IOFFP ,SPVAL
 COMMON /CONRE4/ ISIZEM ,ISIZEP ,NLA ,NLM ,
1 XLT ,YBT ,SIDE ,ISOLID ,
2 EXT ,IOFFD ,IOFFM</pre>For the super option the parameter set is: <pre> COMMON /CONRE1/ IOFFP ,SPVAL ,IHILO
 DATA ISIZEL,ISIZEM,ISIZEP,NLA,NLM,XLT,YBT,SIDE,ISOLID,NREP,NCRT/
1 1, 2, 0, 16, 40,.05,.05, .9, 1023, 6, 4/
 DATA EXT,IOFFD,NULBLL,IOFFM,ILAB/.25,0,3,0,1/</pre>Definitions of the inclusive set follow: 

 <pre><dl COMPACT><dt>ISIZEL<dd>Size of line labels in Plotter Address Units (PAUs).
0 = 8 PAUs, 1 = 12 PAUs, 2 = 16 PAUs, 3 = 24 PAUs,
&gt; 3 means use this number of PAUs. [Default = 1]
<dt>ISIZEM<dd>Size of labels for minimums and maximums, as per
the size definitions given for ISIZEL.
[Default = 2]
<dt>ISIZEP<dd>Size of labels for data point values as per the
size definitions given for ISIZEL. [Default = 0]
<dt>NLA<dd>Approximate number of contour levels when
internally generated. [Default = 16]
<dt>NLM<dd>Maximum number of contour levels. If this is to be
increased, the dimensions of CL and RWORK in conrec.f
must be increased by the same amount. [Default = 40]
<dt>XLT<dd>Left hand edge of the plot (0.0 is the left edge of
the frame and 1.0 is the right edge of the frame.)
[Default = .05]
<dt>YBT<dd>Bottom edge of the plot (0.0 is the bottom of the
frame and 1.0 is the top of the frame.)
[Default = .05]
<dt>SIDE<dd>Length of longer edge of plot (see also EXT).
[Default = .90]
<dt>NREP<dd>Number of repetitions of the dash pattern between
line labels. [Default = 6]
<dt>NCRT<dd>Number of CRT units per element (bit) in the dash
pattern. [Default = 4]
<dt>ILAB<dd>Flag to control the drawing of line labels.
- ILAB non-zero means label the lines.
- ILAB = 0 means do not label the lines.
[Default = 1]
<dt>NULBUL<dd>Number of unlabeled lines between labeled lines.
For example, when NULBLL = 3, every fourth level
is labeled. [Default = 3]
<dt>IOFFD<dd>Flag to control normalization of label numbers.
- IOFFD = 0 means include decimal point when
 possible (do not normalize unless required).
- IOFFD non-zero means normalize all label
 numbers and output a scale factor in the
 message below the graph. [Default = 0]
<dt>EXT<dd>Lengths of the sides of the plot are proportional
to M and N (when CONREC sets the window and viewport).
In extreme cases, when MIN(M,N)/MAX(M,N) is less
than EXT, Conrec produces a square plot.
[Default = .25]
<dt>IOFFP<dd>Flag to control special value feature.
- IOFFP = 0 means the special value feature is
 not in use.
- IOFFP non-zero means the special value feature
 is in use. (SPVAL is set to the special value.)
 Contour lines will then be omitted from any cell
 with any corner equal to the special value.
[Default = 0]
<dt>SPVAL<dd>Contains the special value when IOFFP is non-zero.
[Default = 0.]
<dt>IOFFM<dd>Flag to control the message below the plot.
- IOFFM = 0 if the message is to be plotted.
- IOFFM non-zero if the message is to be omitted.
[Default = 0]
<dt>ISOLID<dd>Dash pattern for non-negative contour lines.
[Default = 1023]</pre></dl><h2>See Also</h2>Online: conrec_family, conpack, conpack_params, ezcntr, conrec Hardcopy: NCAR Graphics Contouring and Mapping Tutorial; NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

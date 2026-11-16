---
title: "ncl_ngmisc_params(3)"
name: "ncl_ngmisc_params"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ngmisc_params/"
---

Ngmisc_params - This document briefly describes all Ngmisc internal parameters.

<h2>Description</h2>

Parameter descriptions, in alphabetical order, of all Ngmisc internal parameters follow. Each entry includes the name of a parameter, its FORTRAN type, its default value, and a short description of the parameter.
<dl><dt>'CA' - Integer - 1
</dt><dd>This parameter controls the type of line cap used in PostScript output from NCAR GKS. If the value is 0, butt caps are used; if the value is 1, round caps are used; if the value is 2, projecting square caps are used. This value applies to the specific workstation specified in a previous call to NGSETI to set a value for the 'WO' parameter (see below).
</dd><dt>'CL' - Integer - 1
</dt><dd>Specifies whether clipping to NDC space is on in NCAR GKS. A value of &quot;1&quot; will turn clipping on and a value of &quot;0&quot; will turn it off. This flag controls whether filled areas and polylines are clipped if they go out of the world coordinate rectangle that gets mapped onto NDC space. This clipping is not to be confused with the clipping that is controlled by the GKS GSCLIP function - that function controls whether clipping is to be done to the viewport of the current normalization transformation, not to NDC space itself (unless the viewport of the current normalization transformation is the entirety of NDC space).
</dd><dt>'CM' - Integer - 1
</dt><dd>If CM equals 1, then the RGB color model is used for PostScript output; if CM equals 0, then the CMYK color model is used for PostScript output.<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>
</dd><dt>'CO' - Integer - 25
</dt><dd>A positive integer specifying a scale factor for the integer coordinate values in PostScript output from NCAR GKS. This value will apply to the first PostScript workstation opened with GOPWK after specifying the value for 'CO'. The default coordinates in PostScript user space represent units of 1/72 of an inch; for an 8 1/2 inch by 11 inch page in portrait mode, the default PostScript user coordinate space is 0 to 612 in X and 0 to 792 in Y. The value of 'CO' will multiply the PostScript user coordinates by the specified amount. Specifying larger values for CO will increase the accuracy of coordinate positions at the expense of larger files (more space is needed to represent the larger integer coordinate values); smaller numbers reduce the accuracy of coordinate positions, but reduce file sizes.
</dd><dt>'CT' - Integer - 0
</dt><dd>Specifies whether NGDOTS will draw filled dots or circles. If the value of CT is 0, then filled dots are drawn. If the value of CT is not 0, then circles are drawn.
</dd><dt>'ER' - Integer - 10
</dt><dd>Specifies the maximum number of error messages that will be issued by NCAR GKS before it terminates execution. ER must be larger than zero.
</dd><dt>'FI' - Real - 0.0005
</dt><dd>A real number in the range 0. to 1. (normalized device coordinate space) that specifies the spacing between fill lines used in software fill in PostScript output from NCAR GKS. This value applies to the specific workstation specified in a previous call to NGSETI to set a value for the &quot;WO&quot; parameter (see below).
</dd><dt>'FU' - Integer - 0
</dt><dd>Controls whether the background color is applied to the entirety of a page, or just the viewport area, in PostScript output from NCAR GKS. If the value is 0, then the background color applies only to the viewport area; if the value is non-zero, then the background color covers the entire page. This value applies to the specific workstation specified in a previous call to NGSETI to set a value for the 'WO' parameter (see below).
</dd><dt>'HA' - Real - 0.01
</dt><dd>A real number in the range 0. to 1. (normalized device coordinate space) that specifies the spacing between hatch lines used in hatch-pattern filled areas in PostScript output from NCAR GKS. This value applies to the specific workstation specified in a previous call to NGSETI to set a value for the 'WO' parameter (see below).
</dd><dt>'IG' - Integer - 0
</dt><dd>A flag to indicate whether the clip rectangles in segment copies should be transformed by using the current segment transformation. The GKS standard says that the clip rectangles should not be so transformed and this is the default.
</dd><dt>'JO' - Integer - 1
</dt><dd>Controls the type of line join used in PostScript output from NCAR GKS. If the value is 0, miter joins are used; if the value is 1, round joins are used; if the value is 2, bevel joins are used. This value applies to the specific workstation specified in a previous call to NGSETI to set a value for the 'WO' parameter (see below).
</dd><dt>'LB' - Integer - 1
</dt><dd>Specifies the secondary logo color (this is applicable only for logo type 5, in which case the secondary color is used for the text string &quot;UCAR&quot;).
</dd><dt>'LC' - Integer - 1
</dt><dd>Specifies the logo color (except in the case of an NCAR logo being plotted to a PostScript workstation, in which case you will get the full-color logo).
</dd><dt>'LT' - Integer - 1
</dt><dd>Specify the logo type. See the documentation for NGLOGO for a list of the logo types, or execute &quot;ncargex miex01&quot; for an example plot that lists the logo types.
</dd><dt>'LX' - Integer - 36
</dt><dd>Specifies the left X coordinate value to be used in positioning PostScript output from NCAR GKS on the output page. This value is in the default PostScript user space where one unit corresponds to 1/72 inch. This value must be specified before opening the PostScript workstation to which it will apply. See descriptions for the parameters 'LY', 'UX', and 'UY'.
</dd><dt>'LY' - Integer - 126
</dt><dd>Specifies the lower Y coordinate value to be used in positioning PostScript output from NCAR GKS on the output page. This value is in the default PostScript user space where one unit corresponds to 1/72 inch. This value must be specified before opening the PostScript workstation to which it will apply. See descriptions for the parameters 'LX', 'UX', and 'UY'.
</dd><dt>'MC' - Integer - depends on the workstation type
</dt><dd>The X11 workstation indicated by the integer should use a &quot;mixed&quot; X color model. (-1) indicates the next X11 workstation created.
</dd><dt>'ME' - Character - depends on the workstation type
</dt><dd>A character string that specifies the metafile name that will be used by the next NCAR GKS GOPWK call that opens a GKS CGM or PostScript workstation.
</dd><dt>'MI' - Real - 10.
</dt><dd>Controls the miter limit of line joins in PostScript output from NCAR GKS. This applies only if line joins are specified as mitered joins (see the description of the parameter 'JO' above). This value applies to the specific workstation specified in a previous call to NGSETI to set a value for the 'WO' parameter (see below).
</dd><dt>'NO' - Real - 1.0
</dt><dd>A positive real number specifying a scale factor for the nominal linewidth in PostScript output from NCAR GKS. Setting the value larger than 1.0 will result in all line thicknesses being fatter by that amount; setting the value smaller than 1.0 will result in all line thicknesses being narrower by that amount. This value applies to the specific workstation specified in a previous call to NGSETI to set a value for the 'WO' parameter (see below).
</dd><dt>'OS' - Real - 0.07
</dt><dd>Specifies the logo size in normalized device coordinates (a number between 0. and 1.). For example, a size specification of 0.1 would give a logo size one-tenth the maximum plot height.
</dd><dt>'OX' - Real - 0.93
</dt><dd>Specify the logo X-coordinate position in normalized device coordinates.
</dd><dt>'OY' - Real - 0.05
</dt><dd>Specify the logo Y-coordinate position in normalized device coordinates.
</dd><dt>'PA' - Integer - 1300
</dt><dd>Specifies the maximum size of paths used in PostScript output from NCAR GKS. This value controls when software fill will be used in place of hardware fill. Larger values result in significant file size and interpretation time savings. This value applies to the specific workstation specified in a previous call to NGSETI to set a value for the 'WO' parameter (see below). The default value is compatible with the minimum value specified in the Adobe PostScript specifications that is to apply to all PostScript interpreters. A specific interpreter may allow for significantly larger paths. See the documentation for your local PostScript interpreter to determine this value.
</dd><dt>'PC' - Integer - depends on the workstation type
</dt><dd>The X11 workstation indicated by the integer should use a &quot;private&quot; X color model. (-1) indicates the next X11 workstation created.
</dd><dt>'PE' - Integer - 20
</dt><dd>Percentage error allowed in matching requested colors in X Window output where the window shares a single color map with all the other current X windows. The value &quot;0&quot; is special and is the same as the value &quot;100&quot; meaning that any color may be selected. In the default environment all X11 windows share a single color map and when a request is made to allocate a new color, and there are no more colors left, then the nearest color (to within the stated percentage) is selected. The &quot;nearest color&quot; is the one in the current color table that is closest using the normal distance metric in the RGB color cube. The percentage error is measured as a percentage of lenght of a diagonal of the RGB color cube.
</dd><dt>'PH' - Integer - 792
</dt><dd>Specification, in points, of the PDF output page height.
</dd><dt>'PI' - Character - blanks
</dt><dd>A character string that will be used for the picture name of the current picture in the PICTURE NAME element of an ncgm file. The first picture must be named before the ncgm workstation is opened and subsequent pictures must be named immediately after creating the previous picture. Not all pictures need be named and any picture that is not assigned a specific name is assigned blanks in the PICTURE NAME field of the ncgm.
</dd><dt>'PW' - Integer - 612
</dt><dd>Specification, in points, of the PDF output page width.
</dd><dt>'SC' - Integer - depends on the workstation type
</dt><dd>The X11 workstation indicated by the integer should use a &quot;shared&quot; X color model. (-1) indicates the next X11 workstation created.
</dd><dt>'SH' - Integer - 612
</dt><dd>Specification, in points, of the PS output page height.
</dd><dt>'SE' - Character - 'GSEG'
</dt><dd>Specifies a root name for segments created by NCAR GKS. In the default case, the segment name used will be constructed from GSEG by appending an integer constructed from the user id, the process id, and the segment number. By default, the segments are stored in the directory specified by the environment variable TMPDIR (usually set internally at install time to /tmp). If SE is changed away from the default setting, then the segment name will be cunstructed using the value of SE as a root and appending the segment number.
</dd><dt>'SW' - Integer - 792
</dt><dd>Specification, in points, of the PS output page width.
</dd><dt>'SS' - Integer - 1
</dt><dd>Specifies whether segments should be deleted when WISS is closed. The default is to delete segments. Setting SS to a non-default value will cause segments to be saved.
</dd><dt>'ST' - Integer - 200
</dt><dd>Specifies the maximum size of the operand stack used in PostScript output from NCAR GKS. The primary effect of setting this value controls how many points can be included in a locally-defined macro for polylines and filled areas. Larger values result in space savings. This value applies to the specific workstation specified in a previous call to NGSETI to set a value for the 'WO' parameter (see below). The default value is compatible with the minimum value specified in the Adobe PostScript specifications that is to apply to all PostScript interpreters.
</dd><dt>'UX' - Integer - 576
</dt><dd>Specifies the upper X coordinate value to be used in positioning PostScript output from NCAR GKS on the output page. This value is in the default PostScript user space where one unit corresponds to 1/72 inch. This value must be specified before opening the PostScript workstation to which it will apply. See descriptions for the parameters &quot;LX&quot;, &quot;LY&quot;, and &quot;UY&quot;.
</dd><dt>'UY' - Integer - 666
</dt><dd>An integer that specifies the upper Y coordinate value to be used in positioning PostScript output from NCAR GKS on the output page. This value is in the default PostScript user space where one unit corresponds to 1/72 inch. This value must be specified before opening the PostScript workstation to which it will apply. See descriptions for the parameters &quot;LX&quot;, &quot;LY&quot;, and &quot;UX&quot;.
</dd><dt>'WO' - Integer - none
</dt><dd>An integer specifying the NCAR GKS workstation ID that will be used for subsequent parameters that apply to a specific workstation.</dd></dl>

<h2>See Also</h2>

Online: nggetc, nggeti, nggetr, ngsetc, ngseti, ngsetr, ngpswk, ncarg_cbind. 

 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/gks/gkshome.html">http://ngwww.ucar.edu/ngdoc/ng/gks/gkshome.html</a> 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version;

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.

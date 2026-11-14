---
title: "xcmsrgbi(3)"
name: "xcmsrgbi"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcmsrgbi/"
description: "XcmsColor, XcmsRGB, XcmsRGBi, XcmsCIEXYZ, XcmsCIEuvY, XcmsCIExyY, XcmsCIELab, XcmsCIELuv, XcmsTekHVC, XcmsPad – Xcms color structure"
---

<p>XcmsColor, XcmsRGB, XcmsRGBi, XcmsCIEXYZ, XcmsCIEuvY, XcmsCIExyY, XcmsCIELab, XcmsCIELuv, XcmsTekHVC, XcmsPad &#8211; Xcms color structure </p>
<h2>Structures</h2>
<p>The structure for <code>XcmsColor</code> contains: </p>
<pre>typedef unsigned long XcmsColorFormat; /* Color Specification Format */
typedef struct {
 union {
 XcmsRGB RGB;
 XcmsRGBi RGBi;
 XcmsCIEXYZ CIEXYZ;
 XcmsCIEuvY CIEuvY;
 XcmsCIExyY CIExyY;
 XcmsCIELab CIELab;
 XcmsCIELuv CIELuv;
 XcmsTekHVC TekHVC;
 XcmsPad Pad;
 } spec;
 unsigned long pixel;
 XcmsColorFormat format;
} XcmsColor; /* Xcms Color Structure */</pre>
<pre>typedef double XcmsFloat;
typedef struct {
 unsigned short red; /* 0x0000 to 0xffff */
 unsigned short green; /* 0x0000 to 0xffff */
 unsigned short blue; /* 0x0000 to 0xffff */
} XcmsRGB; /* RGB Device */</pre>
<pre>typedef struct {
 XcmsFloat red; /* 0.0 to 1.0 */
 XcmsFloat green; /* 0.0 to 1.0 */
 XcmsFloat blue; /* 0.0 to 1.0 */
} XcmsRGBi; /* RGB Intensity */</pre>
<pre>typedef struct {
 XcmsFloat X;
 XcmsFloat Y; /* 0.0 to 1.0 */
 XcmsFloat Z;
} XcmsCIEXYZ; /* CIE XYZ */</pre>
<pre>typedef struct {
 XcmsFloat u_prime; /* 0.0 to ~0.6 */
 XcmsFloat v_prime; /* 0.0 to ~0.6 */
 XcmsFloat Y; /* 0.0 to 1.0 */
} XcmsCIEuvY; /* CIE u'v'Y */</pre>
<pre>typedef struct {
 XcmsFloat x; /* 0.0 to ~.75 */
 XcmsFloat y; /* 0.0 to ~.85 */
 XcmsFloat Y; /* 0.0 to 1.0 */
} XcmsCIExyY; /* CIE xyY */</pre>
<pre>typedef struct {
 XcmsFloat L_star; /* 0.0 to 100.0 */
 XcmsFloat a_star;
 XcmsFloat b_star;
} XcmsCIELab; /* CIE L*a*b* */</pre>
<pre>typedef struct {
 XcmsFloat L_star; /* 0.0 to 100.0 */
 XcmsFloat u_star;
 XcmsFloat v_star;
} XcmsCIELuv; /* CIE L*u*v* */</pre>
<pre>typedef struct {
 XcmsFloat H; /* 0.0 to 360.0 */
 XcmsFloat V; /* 0.0 to 100.0 */
 XcmsFloat C; /* 0.0 to 100.0 */
} XcmsTekHVC; /* TekHVC */</pre>
<pre>typedef struct {
 XcmsFloat pad0;
 XcmsFloat pad1;
 XcmsFloat pad2;
 XcmsFloat pad3;
} XcmsPad; /* four doubles */</pre>
<h2>Description</h2>
<p>The <code>XcmsColor</code> structure contains a union of substructures, each supporting color specification encoding for a particular color space.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xcmsalloccolor/">XcmsAllocColor</a>(3), <a href="/docs/linux/man/3-xcmsstorecolor/">XcmsStoreColor</a>(3), <a href="/docs/linux/man/3-xcmsconvertcolors/">XcmsConvertColors</a>(3), </p>
<p> <i>Xlib &#8211; C Language X Interface</i></p>

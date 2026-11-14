---
title: "xmrendition(3)"
name: "xmrendition"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmrendition/"
description: "XmRendition — The Rendition registry"
---

<p><code>XmRendition</code> &#8212; The Rendition registry</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
XmRendition</pre>
<h2>Description</h2>
<p><code>XmRendition</code> is a pseudo widget used for the rendering of <code>XmString</code>s. <code>XmRendition</code> has two parts: <code>XmStringTag</code> and rendering information. The <code>XmStringTag</code> part can be matched with an <code>XmStringTag</code> associated with a <code>LOCALE</code>, <code>CHARSET</code>, or <code>RENDITION[BEGIN|END]</code> component within <code>XmString</code>. The rendering information contains information about the font or fontset, colors, tabs, and lines to be used in rendering a text component. </p>
<p> If a resource in a rendition is unspecified, usually by setting it to <code>XmAS_IS</code> or <code>XmUNSPECIFIED_PIXEL</code>, then the value to be used for that resource is the value of the immediately preceeding rendition in <code>XmString</code>. If that value is unspecified, then the preceding value is used, and so on. If no renditions specify a value for a resource, then a default value will be used.</p>
<h3>Classes</h3>
<p><code>XmRendition</code> does not inherit from any widget class.</p>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. To reference a resource by name or by class in a <code>.Xdefaults</code> file, remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters. To specify one of the defined values for a resource in a <code>.Xdefaults</code> file, remove the <code>Xm</code> prefix and use the remaining letters (in either lowercase or uppercase, but include any underscores between words). The codes in the access column indicate if the given resource can be set at creation time (C), set by using <code>XmRenditionUpdate</code> (S), retrieved by using <code>XmRenditionRetrieve</code> (G), or is not applicable (N/A). </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmRendition Resource Set</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>Name</code></td>
<td><code>Class</code></td>
<td><code>Type</code></td>
<td><code>Default</code></td>
<td><code>Access</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNrenditionBackground</td>
<td>XmCRenditionBackground</td>
<td>Pixel</td>
<td>XmUNSPECIFIED_PIXEL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNfont</td>
<td>XmCFont</td>
<td>XtPointer</td>
<td>XmAS_IS</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNfontName</td>
<td>XmCFontName</td>
<td>String</td>
<td>XmAS_IS</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNfontType</td>
<td>XmCFontType</td>
<td>XmFontType</td>
<td>XmAS_IS</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNrenditionForeground</td>
<td>XmCRenditionForeground</td>
<td>Pixel</td>
<td>XmUNSPECIFIED_PIXEL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNloadModel</td>
<td>XmCLoadModel</td>
<td>unsigned char</td>
<td>XmAS_IS</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNstrikethruType</td>
<td>XmCStrikethruType</td>
<td>unsigned char</td>
<td>XmAS_IS</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtabList</td>
<td>XmCTabList</td>
<td>XmTabList</td>
<td>XmAS_IS</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtag</td>
<td>XmCTag</td>
<td>XmStringTag</td>
<td>&quot;&quot;</td>
<td>G
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNunderlineType</td>
<td>XmCUnderlineType</td>
<td>unsigned char</td>
<td>XmAS_IS</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
</table>
</table>
<dl COMPACT>
<dt><code>XmNrenditionBackground</code></p>
<dd>Specifies the background drawing color. A value of <code>XmUNSPECIFIED_PIXEL</code> indicates that the background is not specified for this rendition.</p>
<dt><code>XmNfont</code></p>
<dd>Specifies the actual font or fontset to be used by this rendition. The value of this resource, if set to other than <code>XmAS_IS</code>, will be used regardless of the settings of the other font resources. Setting this resource will force <code>XmNloadModel</code> to be <code>XmLOAD_IMMEDIATE</code>. If this resource is not initially set, then it will be set subsequently by the rendition whenever the font or fontset specified by <code>XmNfontName</code> is loaded. If both <code>XmNfontName</code> and <code>XmNfont</code> are specified in a resource file, the <code>XmNfont</code> specification will take precedence.</p>
<dt><code>XmNfontName</code></p>
<dd>Specifies an X Logical Font Description (XLFD) string, which is interpreted either as a font name or as a base font name list. A base font name list is a comma-separated and NULL-terminated string. A value of <code>XmAS_IS</code> indicates that the font is not specified for this rendition. If both <code>XmNfontName</code> and <code>XmNfont</code> are specified in a resource file, the <code>XmNfont</code> specification will take precedence.</p>
<dt><code>XmNfontType</code></p>
<dd>Specifies whether the <code>XmNfontName</code> resource refers to a font name or to a base font name list. Valid values are <code>XmFONT_IS_FONT</code> and <code>XmFONT_IS_FONTSET</code>.</p>
<dt><code>XmNrenditionForeground</code></p>
<dd>Specifies the foreground drawing color. A value of <code>XmUNSPECIFIED_PIXEL</code> indicates that the foreground is not specified for this rendition.</p>
<dt><code>XmNloadModel</code></p>
<dd>Specifies whether the font or fontset specified by <code>XmNfontName</code> is to be loaded when the rendition is created (<code>XmLOAD_IMMEDIATE</code>) or only when the font is required to render an <code>XmString</code> segment (<code>XmLOAD_DEFERRED</code>). Note that specifying <code>XmLOAD_IMMEDIATE</code> for <code>XmNloadModel</code> is valid only if <code>XmNfontName</code> is specified, in which case the specified font will be loaded on creation, or if <code>XmNfont</code> is specified, in which case the font is already loaded. <code>XmLOAD_DEFERRED</code> is only valid when <code>XmNfontName</code> is specified.</p>
<dt><code>XmNstrikethruType</code></p>
<dd>Specifies the type of line to be used to strike through a text segment. Valid values are <code>XmNO_LINE</code>, <code>XmSINGLE_LINE</code>, <code>XmDOUBLE_LINE</code>, <code>XmSINGLE_DASHED_LINE</code>, and <code>XmDOUBLE_DASHED_LINE</code>. A value of <code>XmAS_IS</code> indicates that the strike-through type is not specified for this rendition.</p>
<dt><code>XmNtabList</code></p>
<dd>Specifies the tab list to be used in rendering compound strings containing tab components.</p>
<dt><code>XmNtag</code></p>
<dd>Specifies the tag string to be used in matching the renditions with other renditions or with <code>XmStringTag</code> components in <code>XmStrings</code>. This resource must always be specified. That is, NULL is not a legal value but the empty string is. This resource is automatically set to the value of the <i>tag</i> parameter in the <code>XmRenditionCreate</code> call.</p>
<dt><code>XmNunderlineType</code></p>
<dd>Specifies the type of line to be used to underline a text segment. Valid values are <code>XmNO_LINE</code>, <code>XmSINGLE_LINE</code>, <code>XmDOUBLE_LINE</code>, <code>XmSINGLE_DASHED_LINE</code>, and <code>XmDOUBLE_DASHED_LINE</code>. A value of <code>XmAS_IS</code> indicates that the underline type is not specified for this rendition.</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmrenditioncreate/">XmRenditionCreate</a></code>(3), <code><a href="/docs/linux/man/3-xmrenditionfree/">XmRenditionFree</a></code>(3), <code><a href="/docs/linux/man/3-xmrenditionretrieve/">XmRenditionRetrieve</a></code>(3), <code><a href="/docs/linux/man/3-xmrenditionupdate/">XmRenditionUpdate</a></code>(3), and <code><a href="/docs/linux/man/3-xmstring/">XmString</a></code>(3).</p>

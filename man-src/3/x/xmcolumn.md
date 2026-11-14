---
title: "xmcolumn(3)"
name: "xmcolumn"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcolumn/"
description: "XmColumn — The XmColumn widget class"
---

<p><code>XmColumn</code> &#8212; The XmColumn widget class</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Column.h&gt;</pre>
<h2>Description</h2>
<p><code>XmColumn</code> displays its children stacked in a column, each with an optional associated label: labels appear in one column, and children in another. This is useful for displaying, for example, labeled data-entry fields. It can also display all label-child pairs in a horizontal orientation.This widget offers several constraint resources that allow specification of characteristics of the label, such as displaying text or a pixmap, alignment of text, font to use, and so forth. It also offers several resources for setting defaults for children that specify no specic values.</p>
<h2>Classes</h2>
<p><code>XmColumn</code> inherits behavior and resources from Core, Composite, Constraint, XmManager, and XmBulletinBoard. </p>
<p> The class pointer is <code>xmColumnWidgetClass</code>. </p>
<p> The class name is <code>XmColumn</code>.</p>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. The programmer can also set the resource values for the inherited classes to set attributes for this widget. To reference a resource by name or by class in a <code>.Xdefaults</code> file, remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters&nbsp;<wbr>(in either lowercase or uppercase, but include any underscores between words). The codes in the access column indicate if the given resource can be at createion time (C), or is not applicable (N/A). </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmColumn Resource Set</code>
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
<td>XmNdefaultEntryLabelAlignment</td>
<td>XmCAlignment</td>
<td>unsigned char</td>
<td>XmALIGNMENT_BEGINNING</td>
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
<td>XmNdefaultEntryLabelFontList</td>
<td>XmCFontList</td>
<td>XmRFontList</td>
<td>dynamic</td>
<td>CGS
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
<td>XmNdefaultEntryLabelRenderTable</td>
<td>XmCRendertable</td>
<td>XmRFontList</td>
<td>dynamic</td>
<td>CGS
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
<td>XmNdefaultFillStyle</td>
<td>XmCFillStyle</td>
<td>unsigned char</td>
<td>XmFILL_RAGGED</td>
<td>CGS
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
<td>XmNdistribution</td>
<td>XmCDistribution</td>
<td>unsigned char</td>
<td>XmDISTRIBUTE_TIGHT</td>
<td>CGS
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
<td>XmNitemSpacing</td>
<td>XmCItemSpacing</td>
<td>Dimension</td>
<td>2</td>
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
<td>XmNlabelSpacing</td>
<td>XmCLabelSpacing</td>
<td>Dimentsion</td>
<td>10</td>
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
<td>XmNorientation</td>
<td>XmCOrientation</td>
<td>unsigned char</td>
<td>XmVERTICAL</td>
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
<dt><code>XmNdefaultEntryLabelAlignment</code></p>
<dd>Specifies the default XmNentryLabelAlignment to use when a child specifies no significant value. Resources that specify Alignment have values of XmALIGNMENT_BEGINNING,<br />
 <code>XmALIGNMENT_CENTER, XmALIGNMENT_END, and XmALIGNMENT_UNSPECIFIED. </code> Valid string values that can be used in a resources file are: alignment_unspecified, unspecified, alignment_beginning, beginning, alignment_center, center, alignment_end, end.</p>
<dt><code>XmNdefaultEntryLabelFontList</code></p>
<dd>Specifies the default XmNentryLabelFontList to use when a child specifies no significant value. If unspecified, uses XmNlabelFontList resource of the XmBulletinBoard.</p>
<dt><code>XmNdefaultFillStyle</code></p>
<dd>Specifies the default XmNfillStyle to use when a child specifies no significant value.</p>
<dt><code>XmNdistribution</code></p>
<dd>Specifies whether the spacing between each pair of rows should be increased equally (XmDISTRIBUTE_SPREAD) or remain constant (XmDISTRIBUTE_TIGHT) when the column is resized vertically to be larger than its natural size. This resource has no effect if any child has its<br />
 <code>XmNstretchable resource set to True. This resource is valid only when the orientation is vertical.</code></p>
<dt><code>XmNitemSpacing</code></p>
<dd>Specifies the spacing between each pair of rows (in vertical orientation) or between pairs of labels and children (in horizontal orientation).</p>
<dt><code>XmNlabelSpacing</code></p>
<dd>Specifies the spacing between the column containing the labels and the column containing the XmColumn&#8217;s children.</p>
<dt><code>XmNorientation</code></p>
<dd>Specifies the layout direction of the XmColumn. When XmVERTICAL, the widgets and their associated labels are laid out in two vertical columns. When XmHORIZONTAL, the widgets and their associated labels are laid out in a single row.</p>
<dd></dl>
<p> The visual appearance of columns is affected by setting constraint resources on the children of the XmColumn. These resources are derived from those supported by XmLabel; see the manual page for XmLabel for valid values and usage. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmColumn Constraint Resource Set</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>Name</code></td>
<td><code>Class</code></td>
<td><code>Type</code></td>
<td><code>Default</code></td>
<td><code>AccessfP</code>
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
<td>XmNentryLabelAlignment</td>
<td>XmCAlignment</td>
<td>unsigned char</td>
<td>XmALIGNMENT_UNSPECIFIED</td>
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
<td>XmNentryLabelFontList</td>
<td>XmCFontList</td>
<td>XmFontList</td>
<td>dynamic</td>
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
<td>XmNentryLabelRenderTable</td>
<td>XmCRenderTable</td>
<td>XmRenderTable</td>
<td>dynamic</td>
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
<td>XmNentryLabelPixmap</td>
<td>XmCLabelPixmap</td>
<td>Pixmap</td>
<td>XmUNPECIFIED_PIXMAP</td>
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
<td>XmNentryLabelString</td>
<td>XmCLabelString</td>
<td>XmString</td>
<td>NULL</td>
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
<td>XmNentryLabelType</td>
<td>XmCLabelType</td>
<td>unsigned char</td>
<td>XmSTRING</td>
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
<td>XmNfillStyle</td>
<td>XmCFillStyle</td>
<td>unsigned char</td>
<td>XmFILL_UNSPECIFIED</td>
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
<td>XmNshowEntryLabel</td>
<td>XmCShowLabel</td>
<td>Boolean</td>
<td>True</td>
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
<td>XmNstretchable</td>
<td>XmCStretchable</td>
<td>Boolean</td>
<td>False</td>
<td>CG
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
<dt><code>XmNentryLabelAlignment</code></p>
<dd>Specifies justification of text within the child&#8217;s associated label. Valid values are the same as those for XmNdefaultEntryLabelAlignment.</p>
<dt><code>mNentryLabelFontList</code></p>
<dd>Specifies fontList used to render the text within the child&#8217;s associated label.</p>
<dt><code>XmNentryLabelPixmap</code></p>
<dd>Specifies the pixmap used in the child&#8217;s associated label.</p>
<dt><code>XmNentryLabelString</code></p>
<dd>Specifies the text used in the child&#8217;s associated label.</p>
<dt><code>XmNentryLabelType</code></p>
<dd>Specifies whether to display a string (XmSTRING) or a pixmap (XmPIXMAP) in the child&#8217;s associated label.</p>
<dt><code>XmNfillStyle</code></p>
<dd>Specifies whether the child should be displayed at its natural size (XmFILL_RAGGED) or stretched to fill the entire width of the column it is displayed within (XmFILL_FLUSH).<br />
 <code>XmFILL_UNSPECIFIED uses the value of the XmColumn&#8217;s XmNdefaultFillStyle.</code></p>
<dt><code>XmNshowEntryLabel</code></p>
<dd>Specifies whether or not to display the child&#8217;s associated label.</p>
<dt><code>XmNstretchable</code></p>
<dd>Specifies whether the child should expand in size proportionately when the XmColumn is resized vertically to be larger than its natural size.</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-composite/">Composite</a></code>(3), <code><a href="/docs/linux/man/3-core/">Core</a></code>(3), <code><a href="/docs/linux/man/3-xmbulletinboard/">XmBulletinBoard</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatecolumn/">XmCreateColumn</a></code>(3), <code><a href="/docs/linux/man/3-xmmanager/">XmManager</a></code>(3), <code><a href="/docs/linux/man/3-xmvacreatecolumn/">XmVaCreateColumn</a></code>(3), and <code><a href="/docs/linux/man/3-xmvacreatemanagedcolumn/">XmVaCreateManagedColumn</a></code>(3). </p>
<h2>Version</h2>
<p>This manual page documents the XmColumn widget shipped in Motif version 2.2</p>

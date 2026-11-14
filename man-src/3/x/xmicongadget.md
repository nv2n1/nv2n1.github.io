---
title: "xmicongadget(3)"
name: "xmicongadget"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmicongadget/"
description: "XmIconGadget — The IconGadget widget class"
---

<p><code>XmIconGadget</code> &#8212; The IconGadget widget class</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/IconG.h&gt;</pre>
<h2>Description</h2>
<p>IconGadget is an instantiable widget used to display both text and a pixmap in various combinations. Other widgets that hold the <code>XmQTcontainer</code> trait, such as Container, can use IconGadget to represent objects. </p>
<p> IconGadget text is a compound string. If no text is supplied, then the compound string is generated from the gadget name. IconGadget text is placed relative to the type of associated pixmap. </p>
<p> Depending upon the <code>XmNviewType</code> resource, IconGadget can display two views:</p>
<dl COMPACT>
<dt><code>XmLARGE_ICON</code></p>
<dd>The IconGadget text string is displayed below the pixmap, and centered.</p>
<dt><code>XmSMALL_ICON</code></p>
<dd>The IconGadget text string is placed on the side of the small icon, in the widget&#8217;s <code>XmNlayoutDirection</code>.</dl>
<p> A bitmap mask can be supplied for each pixmap to clip the pixmap into some shape other than a rectangle. The <code>XmNlargeIconMask</code> and <code>XmNsmallIconMask</code> resources specify the large and small bitmap masks respectively. Visual emphasis for the IconGadget is provided with the <code>XmNvisualEmphasis</code> resource. IconGadget&#8217;s <code>XmNdetail</code> and <code>XmNdetailCount</code> resources provide a detail view for IconGadgets, enabling the display of Strings alongside the IconGadget. The exact layout ordering of the strings depends on the associated containing widget. </p>
<p> IconGadget uses the <code>XmQTcontainer</code> and <code>XmQTspecifyRenderTable</code> traits, and holds the <code>XmQTcareParentVisual</code> and <code>XmQTcontainerItem</code> traits.</p>
<h3>Classes</h3>
<p>IconGadget inherits behaviour, resources, and traits from <code>Object, RectObject</code>, and <code>XmGadget</code> classes. </p>
<p> The class pointer is <code>xmIconGadgetClass</code>. </p>
<p> The class name is <code>XmIconGadget</code>.</p>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. The programmer can also set the resource values for the inherited classes to set attributes for this widget. To reference a resource by name or by class in a <code>.Xdefaults</code> file, remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters. To specify one of the defined values for a resource in a <code>.Xdefaults</code> file, remove the <code>Xm</code> prefix and use the remaining letters (in either lowercase or uppercase, but include any underscores between words). The codes in the access column indicate whether the given resource can be set at creation time (C), set by using <code>XtSetValues</code> (S), retrieved by using <code>XtGetValues</code> (G), or is not applicable (N/A). </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmIconGadget Resource Set</code>
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
<td>Xmalignment</td>
<td>XmCAlignment</td>
<td>unsigned char</td>
<td>XmALIGNMENT_CENTER</td>
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
<td>XmNdetail</td>
<td>XmCDetail</td>
<td>XmStringTable</td>
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
<td>XmNdetailCount</td>
<td>XmCDetailCount</td>
<td>Cardinal</td>
<td>0</td>
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
<td>XmNfontList</td>
<td>XmCFontList</td>
<td>XmFontList</td>
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
<td>XmNlabelString</td>
<td>XmCXmString</td>
<td>XmString</td>
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
<td>XmNlargeIconMask</td>
<td>XmCIconMask</td>
<td>Pixmap</td>
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
<td>XmNlargeIconPixmap</td>
<td>XmCIconPixmap</td>
<td>Pixmap</td>
<td>XmUNSPECIFIED_PIXMAP</td>
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
<td>XmNmarginHeight</td>
<td>XmCMarginHeight</td>
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
<td>XmNmarginWidth</td>
<td>XmCMarginWidth</td>
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
<td>XmNrenderTable</td>
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
<td>XmNsmallIconMask</td>
<td>XmCIconMask</td>
<td>Pixmap</td>
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
<td>XmNsmallIconPixmap</td>
<td>XmCIconPixmap</td>
<td>Pixmap</td>
<td>XmUNSPECIFIED_PIXMAP</td>
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
<td>XmNviewType</td>
<td>XmCViewType</td>
<td>unsigned char</td>
<td>XmLARGE_ICON</td>
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
<td>XmNvisualEmphasis</td>
<td>XmCVisualEmphasis</td>
<td>unsigned char</td>
<td>XmNOT_SELECTED</td>
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
<td>XmNspacing</td>
<td>XmCSpacing</td>
<td>Dimension</td>
<td>4</td>
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
<dt><code>XmNalignment</code></p>
<dd>Specifies the horizontal alignment of the pixmap with respect to the label when the icon is in <code>LARGE_ICON</code> view. Valid values are <code>XmALIGNMENT_BEGINNING</code>, <code>XmALIGNMENT_CENTER</code>, and <code>XmALIGNMENT_END</code>.</p>
<dt><code>XmNdetail</code></p>
<dd>Specifies an array of <code>XmString</code>s that are the detail information associated with the gadget.</p>
<dt><code>XmNdetailCount</code></p>
<dd>Specifies the size of the <code>XmNdetail</code> array.</p>
<dt><code>XmNfontList</code></p>
<dd>Specifies the font list associated with <code>XmIconGadget</code>. The font list is an obsolete construct, and has been superseded by the render table. It is included for compatibility with earlier versions of Motif, and for applications that do not easily support render tables. The default font list is derived from the default render table, and if both a font list and a render table are specified, the render table takes precedence.</p>
<dt><code>XmNlabelString</code></p>
<dd>Specifies the compound string. If this value is NULL, it is initialized by converting the name of the gadget to a compound string. Refer to <code><a href="/docs/linux/man/3-xmstring/">XmString</a></code>(3) for more information on the creation and structure of compound strings.</p>
<dt><code>XmNlargeIconMask</code></p>
<dd>Specifies the icon mask used when <code>XmNviewType</code> is <code>XmLARGE_ICON</code>.</p>
<dt><code>XmNlargeIconPixmap</code></p>
<dd>Specifies the pixmap when <code>XmNviewType</code> is <code>XmLARGE_ICON</code>. If this resource&#8217;s value is <code>XmUNSPECIFIED_PIXMAP</code>, there is no pixmap. If a large icon pixmap is specified, and if during conversion an associated mask can be fetched, then the <code>XmNlargeIconMask</code> resource is set to that mask.</p>
<dt><code>XmNmarginHeight</code></p>
<dd>Specifies the amount of vertical space between the highlight and the inside (pixmap and label).</p>
<dt><code>XmNmarginWidth</code></p>
<dd>Specifies the amount of horizontal space between the highlight and the inside (pixmap and label).</p>
<dt><code>XmNrenderTable</code></p>
<dd>Specifies the <code>XmRenderTable</code> of the text used in the gadget. If <code>XmNrenderTable</code> is NULL when the IconGadget is created, the parent&#8217;s render table resource value is used if there is a render table. If the parent does not have a render table, the parent hierarchy of the widget is searched for a widget that holds the <code>XmQTspecifyRenderTable</code> trait. If such an ancestor is found, the render table is initialized to the <code>XmLABEL_RENDER_TABLE</code> value of the ancestor widget. If no such widget is found, the default is implementation dependent. Refer to <code><a href="/docs/linux/man/3-xmrendertable/">XmRenderTable</a></code>(3) for more information on the creation and structure of a <code>XmRenderTable</code>. If both a render table and a font list are specified, the render table will take precedence.</p>
<dt><code>XmNsmallIconMask</code></p>
<dd>Specifies the icon mask used when <code>XmNviewType</code> is <code>XmSMALL_ICON</code>.</p>
<dt><code>XmNsmallIconPixmap</code></p>
<dd>Specifies the pixmap when <code>XmNviewType</code> is <code>XmSMALL_ICON</code>. If this resource&#8217;s value is <code>XmUNSPECIFIED_PIXMAP</code>, there is no pixmap. If a small icon pixmap is specified, and if during conversion an associated mask can be fetched, then the <code>XmNsmallIconMask</code> resource is set to that mask.</p>
<dt><code>XmNspacing</code></p>
<dd>Specifies the amount of space between the pixmap and the label parts of the icon.</p>
<dt><code>XmNviewType</code></p>
<dd>Specifies the view (combination of pixmaps/text) that will be displayed. If the IconGadget is a child of a Container widget, however, then the specification of this resource will be taken from the Container&#8212; if Container&#8217;s <code>XmNentryViewType</code> is either <code>XmLARGE_ICON</code> or <code>XmSMALL_ICON</code>, then IconGadget&#8217;s <code>XmNviewType</code> takes that value; otherwise, the default is <code>XmLARGE_ICON</code>. This resource is set to one of the following:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmLARGE_ICON</code></p>
<dd>The pixmap specified by <code>XmNlargeIconPixmap</code> is displayed with the <code>XmNlabelString</code> beneath it.</p>
<dt><code>XmSMALL_ICON</code></p>
<dd>The pixmap specified by <code>XmNsmallIconPixmap</code> is displayed with the <code>XmNlabelString</code> displayed in the direction of the <code>XmNlayoutDirection</code> resource.</dl>
</dl>
<dt><code>XmNvisualEmphasis</code></p>
<dd>Specifies the visual state of the IconGadget. If the IconGadget is in a selected state all visuals are displayed using the Container <code>XmNselectColor</code> resource. It is set to one of the following:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmSELECTED</code></p>
<dd>The IconGadget is in the selected state and displays the appropriate visuals.</p>
<dt><code>XmNOT_SELECTED</code></p>
<dd>The IconGadget is not in the selected state.</dl>
</dl>
</dl>
<h3>Inherited Resources</h3>
<p>IconGadget inherits behavior and resources from the superclasses described in the following tables. For a complete description of each resource, refer to the reference page for that superclass. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmGadget Resource Set</code>
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
<td>XmNbackground</td>
<td>XmCBackground</td>
<td>Pixel</td>
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
<td>XmNbackgroundPixmap</td>
<td>XmCPixmap</td>
<td>Pixmap</td>
<td>XmUNSPECIFIED_PIXMAP</td>
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
<td>XmNbottomShadowColor</td>
<td>XmCBottomShadowColor</td>
<td>Pixel</td>
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
<td>XmNbottomShadowPixmap</td>
<td>XmCBottomShadowPixmap</td>
<td>Pixmap</td>
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
<td>XmNhelpCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>C
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
<td>XmNforeground</td>
<td>XmCForeground</td>
<td>Pixel</td>
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
<td>XmNhighlightColor</td>
<td>XmCHighlightColor</td>
<td>Pixel</td>
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
<td>XmNhighlightOnEnter</td>
<td>XmCHighlightOnEnter</td>
<td>Boolean</td>
<td>False</td>
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
<td>XmNhighlightPixmap</td>
<td>XmCHighlightPixmap</td>
<td>Pixmap</td>
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
<td>XmNhighlightThickness</td>
<td>XmCHighlightThickness</td>
<td>Dimension</td>
<td>0</td>
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
<td>XmNlayoutDirection</td>
<td>XmNCLayoutDirection</td>
<td>XmDirection</td>
<td>dynamic</td>
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
<tr VALIGN=top>
<td>XmNnavigationType</td>
<td>XmCNavigationType</td>
<td>XmNavigationType</td>
<td>XmNONE</td>
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
<td>XmNshadowThickness</td>
<td>XmCShadowThickness</td>
<td>Dimension</td>
<td>0</td>
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
<td>XmNtopShadowColor</td>
<td>XmCTopShadowColor</td>
<td>Pixel</td>
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
<td>XmNtopShadowPixmap</td>
<td>XmCTopShadowPixmap</td>
<td>Pixmap</td>
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
<td>XmNtraversalOn</td>
<td>XmCTraversalOn</td>
<td>Boolean</td>
<td>False</td>
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
<td>XmNunitType</td>
<td>XmCUnitType</td>
<td>unsigned char</td>
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
<td>XmNuserData</td>
<td>XmCUserData</td>
<td>XtPointer</td>
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
</table>
</table>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>RectObj Resource Set</code>
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
<td>XmNancestorSensitive</td>
<td>XmCSensitive</td>
<td>Boolean</td>
<td>dynamic</td>
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
<td>XmNborderWidth</td>
<td>XmCBorderWidth</td>
<td>Dimension</td>
<td>0</td>
<td>N/A
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
<td>XmNheight</td>
<td>XmCHeight</td>
<td>Dimension</td>
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
<td>XmNsensitive</td>
<td>XmCSensitive</td>
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
<td>XmNwidth</td>
<td>XmCWidth</td>
<td>Dimension</td>
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
<td>XmNx</td>
<td>XmCPosition</td>
<td>Position</td>
<td>0</td>
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
<td>XmNy</td>
<td>XmCPosition</td>
<td>Position</td>
<td>0</td>
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
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>Object Resource Set</code>
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
<td>XmNdestroyCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>C
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
<h3>Additional Behavior</h3>
<p>IconGadget has no behavior.</p>
<h3>Virtual Bindings</h3>
<p>The bindings for virtual keys are vendor specific. For information about bindings for virtual buttons and keys, see <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3).</p>
<h3>Errors/Warnings</h3>
<p>The toolkit will display a warning if an incorrect value is given for an enumeration resource.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-core/">Core</a></code>(3), <code><a href="/docs/linux/man/3-xmcontainer/">XmContainer</a></code>(3), <code><a href="/docs/linux/man/3-xmcreateicongadget/">XmCreateIconGadget</a></code>(3), <code><a href="/docs/linux/man/3-xmgadget/">XmGadget</a></code>(3), <code><a href="/docs/linux/man/3-xmvacreateicongadget/">XmVaCreateIconGadget</a></code>(3), and <code><a href="/docs/linux/man/3-xmvacreatemanagedicongadget/">XmVaCreateManagedIconGadget</a></code>(3).</p>

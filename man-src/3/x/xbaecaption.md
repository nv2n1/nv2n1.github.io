---
title: "xbaecaption(3)"
name: "xbaecaption"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xbaecaption/"
description: "XbaeCaption – The Bellcore Application Environment (BAE) XbaeCaption widget class."
---

<p>XbaeCaption &#8211; The Bellcore Application Environment (BAE) XbaeCaption widget class.</p>
<h2>Synopsis</h2>
<p>#include &lt;Xbae/Caption.h&gt;</p>
<h2>Description</h2>
<p><code>XbaeCaption</code> is a simple manager used to associate a label with its single child. The label may be either an <code>XmString</code> or a Pixmap and can be displayed in any one of twelve positions around the edge of the child. <code>XbaeCaption</code> performs geometry management so that its size always matches its child&#8217;s size plus the size of the label and label offset. By using <code>XbaeCaption</code> with an <code>XmFrame</code> child, groups of related widgets can be labeled in a visually appealing manner. <code>XbaeCaption</code> is also useful for associating labels with individual <code>XmTextFields</code>.</p>
<h3>Classes</h3>
<p><code>XbaeCaption</code> inherits behavior and resources from the <code>Core</code>, <code>Composite</code>, <code>Constraint</code> and <code>XmManager</code> widget classes.<br />
 The class pointer is <code>xbaeCaptionWidgetClass</code>.<br />
 The class name is <code>XbaeCaption</code>.</p>
<h3>New Resources</h3>
<p>The following table lists the new resources defined by <code>XbaeCaption</code>. The codes in the Access column indicate whether the given resource can be set at creation time (C), or set by using XtSetValues (S), or retrieved by using XtGetValues (G). </p>
<table BORDER>
<tr>
<td>
<table WIDTH=100%>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5>XbaeCaption Resource Set
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
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
<td COLSPAN=5>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNfontList</font></td>
<td><font SIZE="-9">XmCFontList</font></td>
<td><font SIZE="-9">FontList</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNlabelAlignment</font></td>
<td><font SIZE="-9">XmCLabelAlignment</font></td>
<td><font SIZE="-9">XbaeLabelAlignment</font></td>
<td><font SIZE="-9">XbaeAlignmentCenter</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNlabelOffset</font></td>
<td><font SIZE="-9">XmCLabelOffset</font></td>
<td><font SIZE="-9">Int</font></td>
<td><font SIZE="-9">0</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNlabelPixmap</font></td>
<td><font SIZE="-9">XmCLabelPixmap</font></td>
<td><font SIZE="-9">PrimForegroundPixmap</font></td>
<td><font SIZE="-9">XmUNSPECIFIED_PIXMAP</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNlabelPosition</font></td>
<td><font SIZE="-9">XmCLabelPosition</font></td>
<td><font SIZE="-9">XbaeLabelPosition</font></td>
<td><font SIZE="-9">XbaePositionLeft</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNlabelString</font></td>
<td><font SIZE="-9">XmCXmString</font></td>
<td><font SIZE="-9">XmString</font></td>
<td><font SIZE="-9">widget name</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNlabelTextAlignment</font></td>
<td><font SIZE="-9">XmCAlignment</font></td>
<td><font SIZE="-9">Alignment</font></td>
<td><font SIZE="-9">XmALIGNMENT_CENTER</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNlabelType</font></td>
<td><font SIZE="-9">XmCLabelType</font></td>
<td><font SIZE="-9">LabelType</font></td>
<td><font SIZE="-9">XmString</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
</table>
</table>
<dl COMPACT>
<dt><code>XmNfontList</code></p>
<dd>Specifies the font of the text used in the caption label. If this value is <font SIZE="-1">NULL</font> at initialization, it is initialized by looking up the parent hierarchy of the widget for an ancestor that is a subclass of the <code>XmBulletinBoard</code>, <code>VendorShell</code> or <code>XmMenuShell</code> widget class. If such an ancestor is found, the font list is initialized to the appropriate default font list of the ancestor widget <code>XmNdefaultFontList for</code> <code>VendorShell</code> and <code>XmMenuShell</code>, <code>XmNlabelFontList</code> or <code>XmNbuttonFontList</code> for <code>XmBulletinBoard.</code> Refer to <code><a href="//www.systutorials.com/docs/linux/man/3X-XmFontList/">XmFontList</a>(3X)</code> for more information on the creation and structure of a font list. This resource is copied.</p>
<dt><code>XmNlabelAlignment</code></p>
<dd>Specifies the alignment of the caption label along the side of the caption child. Must be one of the enumerated <code>XbaeLabelAlignment</code> types: <code>XbaeAlignmentTopOrLeft</code>, <code>XbaeAlignmentCenter</code>, <code>XbaeAlignmentBottomOrRight</code>.</p>
<dt><code>XmNlabelOffset</code></p>
<dd>Specifies the offset, in pixels, of the caption label from the caption child. If the offset is negative, then the caption label will overlap the caption child by that many pixels.</p>
<dt><code>XmNlabelPixmap</code></p>
<dd>Specifies the caption label pixmap when <code>XmNlabelType</code> is <code>XmPIXMAP</code>.</p>
<dt><code>XmNlabelPosition</code></p>
<dd>Specifies on which side of the caption child the caption label should be placed. Must be one of the enumerated <code>XbaeLabelPosition</code> types: <code>XbaePositionLeft</code>, <code>XbaePositionRight</code>, <code>XbaePositionTop</code>, <code>XbaePositionBottom</code>.</p>
<dt><code>XmNlabelString</code></p>
<dd>Specifies the compound string when the <code>XmNlabelType is</code> <code>XmSTRING</code>. If this value is <font SIZE="-1">NULL,</font> it is initialized by converting the name of the widget to a compound string. Refer to <code><a href="//www.systutorials.com/docs/linux/man/3X-XmString/">XmString</a>(3X)</code> for more information on the creation and structure of compound strings.</p>
<dt><code>XmNlabelTextAlignment</code></p>
<dd>Specifies the text alignment for the caption label. This resource is only useful for multi line caption labels. Valid values are: <code>XmALIGNMENT_BEGINNING</code> left alignment causes the left sides of the lines of text to be vertically aligned. <code>XmALIGNMENT_CENTER</code> center alignment causes the centers of the lines of text to be vertically aligned. <code>XmALIGNMENT_END</code> right alignment causes the right sides of the lines of text to be vertically aligned.</p>
<dt><code>XmNlabelType</code></p>
<dd>Specifies the caption label type. Valid values are: <code>XmSTRING</code> &#8211; the caption label will display the <code>XmNlabelString</code>. <code>XmPIXMAP</code> &#8211; the caption label will display the <code>XmNlabelPixmap</code>.</dl>
<h3>Inherited Resources</h3>
<p>The following table lists the resources which <code>XbaeCaption</code> inherits from it&#8217;s superclasses <code>XmManager</code>, <code>Compositeand</code> <code>Core</code>. For a complete description of each resource, refer to the man page for that superclass. The codes in the &quot;Access&quot; column indicate whether the given resource can be set at creation time (C), or set by using XtSetValues (S), or retrieved by using XtGetValues (G). </p>
<table BORDER>
<tr>
<td>
<table WIDTH=100%>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5>XmManager Resource Set
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
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
<td COLSPAN=5>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNbottomShadowColor</font></td>
<td><font SIZE="-9">XmCBottomShadowColor</font></td>
<td><font SIZE="-9">Pixel</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNbottomShadowPixmap</font></td>
<td><font SIZE="-9">XmCBottomShadowPixmap</font></td>
<td><font SIZE="-9">Pixmap</font></td>
<td><font SIZE="-9">XmUNSPECIFIED_PIXMAP</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNforeground</font></td>
<td><font SIZE="-9">XmCForeground</font></td>
<td><font SIZE="-9">Pixel</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNhelpCallback</font></td>
<td><font SIZE="-9">XmCCallback</font></td>
<td><font SIZE="-9">Callback</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNhighlightColor</font></td>
<td><font SIZE="-9">XmCHighlightColor</font></td>
<td><font SIZE="-9">Pixel</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNhighlightPixmap</font></td>
<td><font SIZE="-9">XmCHighlightPixmap</font></td>
<td><font SIZE="-9">Pixmap</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNnavigationType</font></td>
<td><font SIZE="-9">XmCNavigationType</font></td>
<td><font SIZE="-9">XmNavigationType</font></td>
<td><font SIZE="-9">XmTAB_GROUP</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNshadowThickness</font></td>
<td><font SIZE="-9">XmCShadowThickness</font></td>
<td><font SIZE="-9">Dimension</font></td>
<td><font SIZE="-9">2</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNstringDirection</font></td>
<td><font SIZE="-9">XmCStringDirection</font></td>
<td><font SIZE="-9">XmStringDirection</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNtopShadowColor</font></td>
<td><font SIZE="-9">XmCTopShadowColor</font></td>
<td><font SIZE="-9">Pixel</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNtopShadowPixmap</font></td>
<td><font SIZE="-9">XmCTopShadowPixmap</font></td>
<td><font SIZE="-9">Pixmap</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNtraversalOn</font></td>
<td><font SIZE="-9">XmCTraversalOn</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">True</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNunitType</font></td>
<td><font SIZE="-9">XmCUnitType</font></td>
<td><font SIZE="-9">UnsignedChar</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNuserData</font></td>
<td><font SIZE="-9">XmCUserData</font></td>
<td><font SIZE="-9">Pointer</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
</table>
</table>
<table BORDER>
<tr>
<td>
<table WIDTH=100%>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5>Composite Resource Set
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
<hr>
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
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNchildren</font></td>
<td><font SIZE="-9">XmCReadOnly</font></td>
<td><font SIZE="-9">WidgetList</font></td>
<td><font SIZE="-9">private</font></td>
<td><font SIZE="-9">G</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNinsertPosition</font></td>
<td><font SIZE="-9">XmCInsertPosition</font></td>
<td><font SIZE="-9">Function</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNnumChildren</font></td>
<td><font SIZE="-9">XmCReadOnly</font></td>
<td><font SIZE="-9">Cardinal</font></td>
<td><font SIZE="-9">4</font></td>
<td><font SIZE="-9">G</font>
</td>
</tr>
</table>
</table>
<table BORDER>
<tr>
<td>
<table WIDTH=100%>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5>Core Resource Set
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
<hr>
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
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNaccelerators</font></td>
<td><font SIZE="-9">XmCAccelerators</font></td>
<td><font SIZE="-9">AcceleratorTable</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNancestorSensitive</font></td>
<td><font SIZE="-9">XmCSensitive</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNbackground</font></td>
<td><font SIZE="-9">XmCBackground</font></td>
<td><font SIZE="-9">Pixel</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">G</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNbackgroundPixmap</font></td>
<td><font SIZE="-9">XmCPixmap</font></td>
<td><font SIZE="-9">Pixmap</font></td>
<td><font SIZE="-9">XmUNSPECIFIED_PIXMAP</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNborderColor</font></td>
<td><font SIZE="-9">XmCBorderColor</font></td>
<td><font SIZE="-9">Pixel</font></td>
<td><font SIZE="-9">XtDefaultForeground</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNborderPixmap</font></td>
<td><font SIZE="-9">XmCPixmap</font></td>
<td><font SIZE="-9">Pixmap</font></td>
<td><font SIZE="-9">XmUNSPECIFIED_PIXMAP</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNborderWidth</font></td>
<td><font SIZE="-9">XmCBorderWidth</font></td>
<td><font SIZE="-9">Dimension</font></td>
<td><font SIZE="-9">0</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNcolormap</font></td>
<td><font SIZE="-9">XmCColormap</font></td>
<td><font SIZE="-9">Colormap</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNdepth</font></td>
<td><font SIZE="-9">XmCDepth</font></td>
<td><font SIZE="-9">Int</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNdestroyCallback</font></td>
<td><font SIZE="-9">XmCCallback</font></td>
<td><font SIZE="-9">Callback</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNheight</font></td>
<td><font SIZE="-9">XmCHeight</font></td>
<td><font SIZE="-9">Dimension</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNinitialResourcesPersistent</font></td>
<td><font SIZE="-9">XmCInitialResourcesPersistent</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">True</font></td>
<td><font SIZE="-9">CG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNmappedWhenManaged</font></td>
<td><font SIZE="-9">XmCMappedWhenManaged</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">True</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNscreen</font></td>
<td><font SIZE="-9">XmCScreen</font></td>
<td><font SIZE="-9">Screen</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNsensitive</font></td>
<td><font SIZE="-9">XmCSensitive</font></td>
<td><font SIZE="-9">Boolean</font></td>
<td><font SIZE="-9">True</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNtranslations</font></td>
<td><font SIZE="-9">XmCTranslations</font></td>
<td><font SIZE="-9">TranslationTable</font></td>
<td><font SIZE="-9">internal</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNwidth</font></td>
<td><font SIZE="-9">XmCWidth</font></td>
<td><font SIZE="-9">Dimension</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNx</font></td>
<td><font SIZE="-9">XmCPosition</font></td>
<td><font SIZE="-9">Position</font></td>
<td><font SIZE="-9">0</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNy</font></td>
<td><font SIZE="-9">XmCPosition</font></td>
<td><font SIZE="-9">Position</font></td>
<td><font SIZE="-9">0</font></td>
<td><font SIZE="-9">CSG</font>
</td>
</tr>
</table>
</table>
<h3>Translations</h3>
<p><code>XbaeCaption inherits translations from</code> <code>XmManager</code>.</p>
<h3>Type Converters</h3>
<p>In addition to the standard type converters registered by Xt and Motif, <code>XbaeCaption</code> registers the following additional type converters:</p>
<dl COMPACT>
<dt>CvtStringToLabelAlignment()</p>
<dd>Converts a String to the enumerated <code>XbaeLabelAlignment</code> type. The Strings <code>TopOrLeft</code>, <code>Top </code> and <code>Left</code> are converted to <code>XbaeAlignmentTopOrLeft</code>. The String <code>Center</code> is converted to <code>XbaeAlignmentCenter</code>. The Strings <code>BottomOrRight</code>, <code>Bottom</code> and <code>Right</code> are converted to <code>XbaeAlignmentBottomOrRight</code>. This converter allows the <code>XmNlabelAlignment</code> resource to be specified in a resource file. The converter is case insensitive.</p>
<dt>CvtStringToLabelPosition()</p>
<dd>Converts a String to the enumerated <code>XbaeLabelPosition</code> type. The String <code>Left</code> is converted to <code>XbaePositionLeft</code>. The String <code>Right</code> is converted to <code>XbaePositionRight</code>. The String <code>Top is converted to</code> <code>XbaePositionTop</code>. The String <code>Bottom is converted to</code> <code>XbaePositionBottom</code>. This converter allows the <code>XmNlabelPosition</code> resource to be specified in a resource file. The converter is case insensitive. </p>
</dl>
<h3>Public Functions</h3>
<p>The following external entry points to <code>XbaeCaption</code> class methods are defined: </p>
<p> <code>XbaeCreateCaption()</code> </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td COLSPAN=3>Widget XbaeCreateCaption()
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Widget</td>
<td><i>parent;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>String</td>
<td><i>name;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>ArgList</td>
<td><i>arglist;</i>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Cardinal</td>
<td><i>argcount;</i>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>parent</i></p>
<dd>Specifies the parent widget ID.</p>
<dt><i>name</i></p>
<dd>Specifies the name of the created widget</p>
<dt><i>arglist</i></p>
<dd>Specifies the argument list</p>
<dt><i>argcount</i></p>
<dd>Specifies the number of attribute/value pairs in the argument list (arglist)</dl>
<p> <code>XbaeCreateCaption()</code> creates an instance of an XbaeCaption widget and returns the associated widget ID. </p>
</dl>
<h3>Virtual Bindings</h3>
<p>The bindings for virtual keys are vendor specific. For information about bindings for virtual buttons and keys, see <code><a href="//www.systutorials.com/docs/linux/man/3X-VirtualBindings/">VirtualBindings</a>(3X)</code>.</p>
<h2>Author</h2>
<p><code>Andrew Wason,</code> Bellcore, Piscataway NJ; author<br />
 (aw [at] bae.bellcore.com) </p>
<p> <code>Andrew Lister</code><br />
 (lister [at] db.com) </p>
<h2>Release</h2>
<p>This document describes XbaeCaption from Xbae Version 4.9.</p>
<h2>See Also</h2>
<p><code><a href="//www.systutorials.com/docs/linux/man/3X-Core/">Core</a>(3X), <a href="//www.systutorials.com/docs/linux/man/3X-Composite/">Composite</a>(3X), <a href="//www.systutorials.com/docs/linux/man/3X-XmManager/">XmManager</a>(3X), <a href="//www.systutorials.com/docs/linux/man/3X-XmLabel/">XmLabel</a>(3X)</code></p>
<h2>Notice of Limitation</h2>
<p>Bellcore, previous and current maintainers of the Xbae widgets (collectively &#8216;authors&#8217;) provide this information solely to professionals who have the appropriate degree of experience to understand and interpret its contents in accordance with generally accepted engineering or other professional standards and applicable regulations. No recommendations as to products or vendors is made or should be implied. </p>
<p> While the information contained herein has been prepared from sources deemed to be reliable, the authors reserve the right to revise the information without notice, but have no obligation to do so. Unless the recipient has been expressly granted a license by Bellcore under separate applicable written agreement with Bellcore, no license, expressed or implied, is granted under any patents, copyrights or other intellectual property rights. Use of the information is at your discretion and shall not be deemed an inducement by Bellcore to infringe any existing or later-issued patent, copyrights or other intellectual property right. </p>
<p> THE AUTHORS MAKE NO REPRESENTATIONS AND EXTENDS NO WARRANTIES, EXPRESS OR IMPLIED, WITH RESPECT TO THE INFORMATION, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR ANY PARTICULAR PURPOSE, AND THE WARRANTY AGAINST INFRINGEMENT OF PATENTS OR OTHER INTELLECTUAL PROPERTY RIGHTS. THE INFORMATION IS PROVIDED &#8220;AS IS&#8221;, AND IN NO EVENT SHALL THE AUTHORS OR ANY OF ITS AFFILIATES BE LIABLE FOR ANY DAMAGES, INCLUDING ANY LOST PROFITS OR OTHER INCIDENTAL OR CONSEQUENTIAL DAMAGES RELATING TO THE INFORMATION. </p>
<p> Copyright 1991 Bellcore. All Rights Reserved. Copyright 1995-99 Andrew Lister All Rights Reserved.<br />
 Copyright 1999-2002 LessTif Developers </p>
<p> The above no warranty extends to all additions and contributions. No contributor shall be held liable; this work is provided &#8220;as is&#8221;. If this is a problem for you, then don&#8217;t use this software.</p>

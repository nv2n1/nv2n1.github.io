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
<p><code>XbaeCaption</code> inherits behavior and resources from the <code>Core</code>, <code>Composite</code>, <code>Constraint</code> and <code>XmManager</code> widget classes.<br/>
 The class pointer is <code>xbaeCaptionWidgetClass</code>.<br/>
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
<td>XmNfontList</td>
<td>XmCFontList</td>
<td>FontList</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNlabelAlignment</td>
<td>XmCLabelAlignment</td>
<td>XbaeLabelAlignment</td>
<td>XbaeAlignmentCenter</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNlabelOffset</td>
<td>XmCLabelOffset</td>
<td>Int</td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNlabelPixmap</td>
<td>XmCLabelPixmap</td>
<td>PrimForegroundPixmap</td>
<td>XmUNSPECIFIED_PIXMAP</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNlabelPosition</td>
<td>XmCLabelPosition</td>
<td>XbaeLabelPosition</td>
<td>XbaePositionLeft</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNlabelString</td>
<td>XmCXmString</td>
<td>XmString</td>
<td>widget name</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNlabelTextAlignment</td>
<td>XmCAlignment</td>
<td>Alignment</td>
<td>XmALIGNMENT_CENTER</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNlabelType</td>
<td>XmCLabelType</td>
<td>LabelType</td>
<td>XmString</td>
<td>CSG
</td>
</tr>
</table>
</table>
<dl COMPACT>
<dt><code>XmNfontList</code></dt>
<dd>Specifies the font of the text used in the caption label. If this value is NULL at initialization, it is initialized by looking up the parent hierarchy of the widget for an ancestor that is a subclass of the <code>XmBulletinBoard</code>, <code>VendorShell</code> or <code>XmMenuShell</code> widget class. If such an ancestor is found, the font list is initialized to the appropriate default font list of the ancestor widget <code>XmNdefaultFontList for</code> <code>VendorShell</code> and <code>XmMenuShell</code>, <code>XmNlabelFontList</code> or <code>XmNbuttonFontList</code> for <code>XmBulletinBoard.</code> Refer to <code>XmFontList(3X)</code> for more information on the creation and structure of a font list. This resource is copied.</dd>
<dt><code>XmNlabelAlignment</code></dt>
<dd>Specifies the alignment of the caption label along the side of the caption child. Must be one of the enumerated <code>XbaeLabelAlignment</code> types: <code>XbaeAlignmentTopOrLeft</code>, <code>XbaeAlignmentCenter</code>, <code>XbaeAlignmentBottomOrRight</code>.</dd>
<dt><code>XmNlabelOffset</code></dt>
<dd>Specifies the offset, in pixels, of the caption label from the caption child. If the offset is negative, then the caption label will overlap the caption child by that many pixels.</dd>
<dt><code>XmNlabelPixmap</code></dt>
<dd>Specifies the caption label pixmap when <code>XmNlabelType</code> is <code>XmPIXMAP</code>.</dd>
<dt><code>XmNlabelPosition</code></dt>
<dd>Specifies on which side of the caption child the caption label should be placed. Must be one of the enumerated <code>XbaeLabelPosition</code> types: <code>XbaePositionLeft</code>, <code>XbaePositionRight</code>, <code>XbaePositionTop</code>, <code>XbaePositionBottom</code>.</dd>
<dt><code>XmNlabelString</code></dt>
<dd>Specifies the compound string when the <code>XmNlabelType is</code> <code>XmSTRING</code>. If this value is NULL, it is initialized by converting the name of the widget to a compound string. Refer to <code>XmString(3X)</code> for more information on the creation and structure of compound strings.</dd>
<dt><code>XmNlabelTextAlignment</code></dt>
<dd>Specifies the text alignment for the caption label. This resource is only useful for multi line caption labels. Valid values are: <code>XmALIGNMENT_BEGINNING</code> left alignment causes the left sides of the lines of text to be vertically aligned. <code>XmALIGNMENT_CENTER</code> center alignment causes the centers of the lines of text to be vertically aligned. <code>XmALIGNMENT_END</code> right alignment causes the right sides of the lines of text to be vertically aligned.</dd>
<dt><code>XmNlabelType</code></dt>
<dd>Specifies the caption label type. Valid values are: <code>XmSTRING</code> &#8211; the caption label will display the <code>XmNlabelString</code>. <code>XmPIXMAP</code> &#8211; the caption label will display the <code>XmNlabelPixmap</code>.</dd></dl>
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
<td>XmNbottomShadowColor</td>
<td>XmCBottomShadowColor</td>
<td>Pixel</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNbottomShadowPixmap</td>
<td>XmCBottomShadowPixmap</td>
<td>Pixmap</td>
<td>XmUNSPECIFIED_PIXMAP</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
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
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNhelpCallback</td>
<td>XmCCallback</td>
<td>Callback</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
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
<td COLSPAN=5>
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
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNnavigationType</td>
<td>XmCNavigationType</td>
<td>XmNavigationType</td>
<td>XmTAB_GROUP</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNshadowThickness</td>
<td>XmCShadowThickness</td>
<td>Dimension</td>
<td>2</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNstringDirection</td>
<td>XmCStringDirection</td>
<td>XmStringDirection</td>
<td>dynamic</td>
<td>CG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
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
<td COLSPAN=5>
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
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtraversalOn</td>
<td>XmCTraversalOn</td>
<td>Boolean</td>
<td>True</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNunitType</td>
<td>XmCUnitType</td>
<td>UnsignedChar</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNuserData</td>
<td>XmCUserData</td>
<td>Pointer</td>
<td>NULL</td>
<td>CSG
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
<td>XmNchildren</td>
<td>XmCReadOnly</td>
<td>WidgetList</td>
<td>private</td>
<td>G
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNinsertPosition</td>
<td>XmCInsertPosition</td>
<td>Function</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNnumChildren</td>
<td>XmCReadOnly</td>
<td>Cardinal</td>
<td>4</td>
<td>G
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
<td>XmNaccelerators</td>
<td>XmCAccelerators</td>
<td>AcceleratorTable</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNancestorSensitive</td>
<td>XmCSensitive</td>
<td>Boolean</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNbackground</td>
<td>XmCBackground</td>
<td>Pixel</td>
<td>dynamic</td>
<td>G
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
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
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNborderColor</td>
<td>XmCBorderColor</td>
<td>Pixel</td>
<td>XtDefaultForeground</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNborderPixmap</td>
<td>XmCPixmap</td>
<td>Pixmap</td>
<td>XmUNSPECIFIED_PIXMAP</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNborderWidth</td>
<td>XmCBorderWidth</td>
<td>Dimension</td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNcolormap</td>
<td>XmCColormap</td>
<td>Colormap</td>
<td>dynamic</td>
<td>CG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNdepth</td>
<td>XmCDepth</td>
<td>Int</td>
<td>dynamic</td>
<td>CG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNdestroyCallback</td>
<td>XmCCallback</td>
<td>Callback</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
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
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNinitialResourcesPersistent</td>
<td>XmCInitialResourcesPersistent</td>
<td>Boolean</td>
<td>True</td>
<td>CG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNmappedWhenManaged</td>
<td>XmCMappedWhenManaged</td>
<td>Boolean</td>
<td>True</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNscreen</td>
<td>XmCScreen</td>
<td>Screen</td>
<td>dynamic</td>
<td>CG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
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
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtranslations</td>
<td>XmCTranslations</td>
<td>TranslationTable</td>
<td>internal</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
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
<td COLSPAN=5>
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
<td COLSPAN=5>
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
</table>
</table>
<h3>Translations</h3>
<p><code>XbaeCaption inherits translations from</code> <code>XmManager</code>.</p>
<h3>Type Converters</h3>
<p>In addition to the standard type converters registered by Xt and Motif, <code>XbaeCaption</code> registers the following additional type converters:</p>
<dl COMPACT>
<dt>CvtStringToLabelAlignment()</dt>
<dd>Converts a String to the enumerated <code>XbaeLabelAlignment</code> type. The Strings <code>TopOrLeft</code>, <code>Top </code> and <code>Left</code> are converted to <code>XbaeAlignmentTopOrLeft</code>. The String <code>Center</code> is converted to <code>XbaeAlignmentCenter</code>. The Strings <code>BottomOrRight</code>, <code>Bottom</code> and <code>Right</code> are converted to <code>XbaeAlignmentBottomOrRight</code>. This converter allows the <code>XmNlabelAlignment</code> resource to be specified in a resource file. The converter is case insensitive.</dd>
<dt>CvtStringToLabelPosition()</dt>
<dd>Converts a String to the enumerated <code>XbaeLabelPosition</code> type. The String <code>Left</code> is converted to <code>XbaePositionLeft</code>. The String <code>Right</code> is converted to <code>XbaePositionRight</code>. The String <code>Top is converted to</code> <code>XbaePositionTop</code>. The String <code>Bottom is converted to</code> <code>XbaePositionBottom</code>. This converter allows the <code>XmNlabelPosition</code> resource to be specified in a resource file. The converter is case insensitive. </dd>
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
</dd><dl COMPACT>
<dt><i>parent</i></dt>
<dd>Specifies the parent widget ID.</dd>
<dt><i>name</i></dt>
<dd>Specifies the name of the created widget</dd>
<dt><i>arglist</i></dt>
<dd>Specifies the argument list</dd>
<dt><i>argcount</i></dt>
<dd>Specifies the number of attribute/value pairs in the argument list (arglist)</dd></dl>
<p> <code>XbaeCreateCaption()</code> creates an instance of an XbaeCaption widget and returns the associated widget ID. </p>
</dl>
<h3>Virtual Bindings</h3>
<p>The bindings for virtual keys are vendor specific. For information about bindings for virtual buttons and keys, see <code>VirtualBindings(3X)</code>.</p>
<h2>Author</h2>
<p><code>Andrew Wason,</code> Bellcore, Piscataway NJ; author<br/>
 (aw [at] bae.bellcore.com) </p>
<p> <code>Andrew Lister</code><br/>
 (lister [at] db.com) </p>
<h2>Release</h2>
<p>This document describes XbaeCaption from Xbae Version 4.9.</p>
<h2>See Also</h2>
<p><code>Core(3X), Composite(3X), XmManager(3X), XmLabel(3X)</code></p>
<h2>Notice of Limitation</h2>
<p>Bellcore, previous and current maintainers of the Xbae widgets (collectively &#8216;authors&#8217;) provide this information solely to professionals who have the appropriate degree of experience to understand and interpret its contents in accordance with generally accepted engineering or other professional standards and applicable regulations. No recommendations as to products or vendors is made or should be implied. </p>
<p> While the information contained herein has been prepared from sources deemed to be reliable, the authors reserve the right to revise the information without notice, but have no obligation to do so. Unless the recipient has been expressly granted a license by Bellcore under separate applicable written agreement with Bellcore, no license, expressed or implied, is granted under any patents, copyrights or other intellectual property rights. Use of the information is at your discretion and shall not be deemed an inducement by Bellcore to infringe any existing or later-issued patent, copyrights or other intellectual property right. </p>
<p> THE AUTHORS MAKE NO REPRESENTATIONS AND EXTENDS NO WARRANTIES, EXPRESS OR IMPLIED, WITH RESPECT TO THE INFORMATION, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR ANY PARTICULAR PURPOSE, AND THE WARRANTY AGAINST INFRINGEMENT OF PATENTS OR OTHER INTELLECTUAL PROPERTY RIGHTS. THE INFORMATION IS PROVIDED &#8220;AS IS&#8221;, AND IN NO EVENT SHALL THE AUTHORS OR ANY OF ITS AFFILIATES BE LIABLE FOR ANY DAMAGES, INCLUDING ANY LOST PROFITS OR OTHER INCIDENTAL OR CONSEQUENTIAL DAMAGES RELATING TO THE INFORMATION. </p>
<p> Copyright 1991 Bellcore. All Rights Reserved. Copyright 1995-99 Andrew Lister All Rights Reserved.<br/>
 Copyright 1999-2002 LessTif Developers </p>
<p> The above no warranty extends to all additions and contributions. No contributor shall be held liable; this work is provided &#8220;as is&#8221;. If this is a problem for you, then don&#8217;t use this software.</p>

---
title: "core(3)"
name: "core"
section: "3"
letter: "c"
url: "/docs/linux/man/3-core/"
description: "Core — The Core widget class"
---

<p><code>Core</code> &#8212; The Core widget class</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;</pre>
<h2>Description</h2>
<p>Core is the Xt Intrinsic base class for windowed widgets. The <code>Object</code> and <code>RectObj</code> classes provide support for windowless widgets.</p>
<h3>Classes</h3>
<p>All widgets are built from <code>Core</code>. </p>
<p> The class pointer is <code>widgetClass</code>. </p>
<p> The class name is <code>Core</code>.</p>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. The programmer can also set the resource values for the inherited classes to set attributes for this widget. To reference a resource by name or by class in a <code>.Xdefaults</code> file, remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters. To specify one of the defined values for a resource in a <code>.Xdefaults</code> file, remove the <code>Xm</code> prefix and use the remaining letters (in either lowercase or uppercase, but include any underscores between words). The codes in the access column indicate if the given resource can be set at creation time (C), set by using <code>XtSetValues</code> (S), retrieved by using <code>XtGetValues</code> (G), or is not applicable (N/A). </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>Core Resource Set</code>
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
<td>XmNaccelerators</td>
<td>XmCAccelerators</td>
<td>XtAccelerators</td>
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
<td>XmNborderColor</td>
<td>XmCBorderColor</td>
<td>Pixel</td>
<td>XtDefaultForeground</td>
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
<td>XmNborderPixmap</td>
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
<td>XmNborderWidth</td>
<td>XmCBorderWidth</td>
<td>Dimension</td>
<td>1</td>
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
<td>XmNcolormap</td>
<td>XmCColormap</td>
<td>Colormap</td>
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
<td>XmNdepth</td>
<td>XmCDepth</td>
<td>int</td>
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
<td>XmNinitialResourcesPersistent</td>
<td>XmCInitialResourcesPersistent</td>
<td>Boolean</td>
<td>True</td>
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
<td>XmNmappedWhenManaged</td>
<td>XmCMappedWhenManaged</td>
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
<td>XmNscreen</td>
<td>XmCScreen</td>
<td>Screen *</td>
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
<td>XmNtranslations</td>
<td>XmCTranslations</td>
<td>XtTranslations</td>
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
<dl COMPACT>
<dt><code>XmNaccelerators</code></p>
<dd>Specifies a translation table that is bound with its actions in the context of a particular widget. The accelerator table can then be installed on some destination widget. Note that the default accelerators for any widget will always be installed, no matter whether this resource is specified or not.</p>
<dt><code>XmNancestorSensitive</code></p>
<dd>Specifies whether the immediate parent of the widget receives input events. Use the function <code>XtSetSensitive</code> to change the argument to preserve data integrity (see <code>XmNsensitive</code>). For shells, the default is copied from the parent&#8217;s <code>XmNancestorSensitive</code> resource if there is a parent; otherwise, it is True. For other widgets, the default is the bitwise AND of the parent&#8217;s <code>XmNsensitive</code> and <code>XmNancestorSensitive</code> resources.</p>
<dt><code>XmNbackground</code></p>
<dd>Specifies the background color for the widget.</p>
<dt><code>XmNbackgroundPixmap</code></p>
<dd>Specifies a pixmap for tiling the background. The first tile is placed at the upper left corner of the widget&#8217;s window.</p>
<dt><code>XmNborderColor</code></p>
<dd>Specifies the color of the border in a pixel value.</p>
<dt><code>XmNborderPixmap</code></p>
<dd>Specifies a pixmap to be used for tiling the border. The first tile is placed at the upper left corner of the border.</p>
<dt><code>XmNborderWidth</code></p>
<dd>Specifies the width of the border that surrounds the widget&#8217;s window on all four sides. The width is specified in pixels. A width of 0 (zero) means that no border shows. Note that you should use resources like <code>XmNshadowThickness</code> and <code>XmNhighlightThickness</code> instead of <code>XmNborderWidth</code> to specify border widths.</p>
<dt><code>XmNcolormap</code></p>
<dd>Specifies the colormap that is used for conversions to the type <code>Pixel</code> for this widget instance. When this resource is changed, previously generated pixel values are not affected, but newly generated values are in the new colormap. For shells without parents, the default is the default colormap of the widget&#8217;s screen. Otherwise, the default is copied from the parent.</p>
<dt><code>XmNdepth</code></p>
<dd>Specifies the number of bits that can be used for each pixel in the widget&#8217;s window. Applications should not change or set the value of this resource as it is set by the Xt Intrinsics when the widget is created. For shells without parents, the default is the default depth of the widget&#8217;s screen. Otherwise, the default is copied from the parent.</p>
<dt><code>XmNdestroyCallback</code></p>
<dd>Specifies a list of callbacks that is called when the widget is destroyed.</p>
<dt><code>XmNheight</code></p>
<dd>Specifies the inside height (excluding the border) of the widget&#8217;s window.</p>
<dt><code>XmNinitialResourcesPersistent</code></p>
<dd>Specifies whether or not resources are reference counted. If the value is True when the widget is created, the resources referenced by the widget are not reference counted, regardless of how the resource type converter is registered. An application that expects to destroy the widget and wants to have resources deallocated should specify a value of False. The default is True, implying an assumption that the widget will not be destroyed during the life of the application.</p>
<dt><code>XmNmappedWhenManaged</code></p>
<dd>If this resource is set to True, it maps the widget (makes it visible) as soon as it is both realized and managed. If this resource is set to False, the client is responsible for mapping and unmapping the widget. If the value is changed from True to False after the widget has been realized and managed, the widget is unmapped.</p>
<dt><code>XmNscreen</code></p>
<dd>Specifies the screen on which a widget instance resides. It is read only. When the Toolkit is initialized, the top-level widget obtains its default value from the default screen of the display. Otherwise, the default is copied from the parent.</p>
<dt><code>XmNsensitive</code></p>
<dd>Determines whether a widget receives input events. If a widget is sensitive, the Xt Intrinsics&#8217; Event Manager dispatches to the widget all keyboard, mouse button, motion, window enter/leave, and focus events. Insensitive widgets do not receive these events. Use the function <code>XtSetSensitive</code> to change the sensitivity argument. Using <code>XtSetSensitive</code> ensures that if a parent widget has <code>XmNsensitive</code> set to False, the ancestor-sensitive flag of all its children is appropriately set.</p>
<dt><code>XmNtranslations</code></p>
<dd>Points to a translations list. A translations list is a list of events and actions that are to be performed when the events occur. Note that the default translations for any widget will always be installed, no matter whether this resource is specified or not.</p>
<dt><code>XmNwidth</code></p>
<dd>Specifies the inside width (excluding the border) of the widget&#8217;s window.</p>
<dt><code>XmNx</code></p>
<dd>Specifies the x-coordinate of the upper left outside corner of the widget&#8217;s window. The value is relative to the upper left inside corner of the parent window.</p>
<dt><code>XmNy</code></p>
<dd>Specifies the y-coordinate of the upper left outside corner of the widget&#8217;s window. The value is relative to the upper left inside corner of the parent window.</dl>
<h3>Translations</h3>
<p>There are no translations for Core.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-object/">Object</a></code>(3) and <code><a href="/docs/linux/man/3-rectobj/">RectObj</a></code>(3).</p>

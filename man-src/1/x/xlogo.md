---
title: "xlogo(1)"
name: "xlogo"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xlogo/"
description: "xlogo – X Window System logo"
---

<h2>SYNOPSIS</h2>
<p> <code>xlogo</code> [-<i>toolkitoption</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> The <i>xlogo</i> program displays the X Window System logo.</p>
<h2>OPTIONS</h2>
<p> <i>Xlogo</i> accepts all of the standard X Toolkit command line options, as well as the following:</p>
<dl>
<dt><code>-render</code></dt>
<dd> This option indicates that the logo should be drawn with anti-aliased edges using the RENDER extension.</dd>
<dt><code>-sharp</code></dt>
<dd> If -render is also specified, this forces the edges to be rendered in sharp mode, (ie. 1-bit alpha channel).</dd>
<dt><code>-shape</code></dt>
<dd> This option indicates that the logo window should be shaped rather than rectangular.</dd></dl>
<h2>RESOURCES</h2>
<p> The default width and the default height are each 100 pixels. This program uses the <i>Logo</i> widget in the Athena widget set. It understands all of the Simple widget resource names and classes as well as:</p>
<dl>
<dt><code>foreground (</code>class<code> Foreground)</code></dt>
<dd> Specifies the color for the logo. The default is depends on whether <i>reverseVideo</i> is specified. If <i>reverseVideo</i> is specified the default is <i>XtDefaultForeground</i>, otherwise the default is <i>XtDefaultBackground</i>.</dd>
<dt><code>shapeWindow (</code>class<code> ShapeWindow)</code></dt>
<dd> Specifies that the window is shaped to the X logo. The default is False.</dd></dl>
<h2>WIDGETS</h2>
<p> In order to specify resources, it is useful to know the hierarchy of the widgets which compose <i>xlogo</i>. In the notation below, indentation indicates hierarchical structure. The widget class name is given first, followed by the widget instance name. </p>
<pre>
XLogo  xlogo
        Logo  xlogo
</pre>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DISPLAY</code></dt>
<dd> to get the default host and display number.</dd>
<dt><code>XENVIRONMENT</code></dt>
<dd> to get the name of a resource file that overrides the global resources stored in the RESOURCE_MANAGER property.</dd></dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/X11/app-defaults/XLogo</i></dt>
<dd> specifies required resources</dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/1-xrdb/">xrdb</a>(1)</p>
<h2>AUTHORS</h2>
<p> Ollie Jones of Apollo Computer and Jim Fulton of the MIT X Consortium wrote the logo graphics routine, based on a graphic design by Danny Chong and Ross Chapman of Apollo Computer. </p>

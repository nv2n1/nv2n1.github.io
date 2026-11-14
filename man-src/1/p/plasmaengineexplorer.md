---
title: "plasmaengineexplorer(1)"
name: "plasmaengineexplorer"
section: "1"
letter: "p"
url: "/docs/linux/man/1-plasmaengineexplorer/"
description: "plasmaengineexplorer – Provides direct access to plasma data engines"
---

<h2>NAME</h2>
<p> plasmaengineexplorer &#8211; Provides direct access to plasma data engines</p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>plasmaengineexplorer</code> [<code>&#8211;height</code><i> pixels</i>] [<code>&#8211;width</code><i> pixels</i>] [<code>-x</code><i> pixels</i>] [<code>-y</code><i> pixels</i>] [<code>&#8211;engine</code><i> name</i>] [<code>&#8211;source</code><i> name</i>] [<code>&#8211;interval</code><i> ms</i>]</p>
<dt> <code>plasmaengineexplorer</code> [KDE Generic Options] [Qt Generic Options] </p>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>plasmaengineexplorer</code> is a graphical tool allowing developers to test Plasma data engines without writing a Plasma applet. </p>
<dd>If no options are given, it will start without any data engine selected. The required data engine can be selected from a drop-down list. </p>
<p> Only installed data engines will be found. <code>kbuildsycoca4</code> may need to be run for newly-installed data engines to be found. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;height </code><i>pixels</i></p>
<dd> Sets the height of the window, in pixels. </p>
<dt><code>&#8211;width </code><i>pixels</i></p>
<dd> Sets the width of the window, in pixels. </p>
<dt><code>-x </code><i>pixels</i></p>
<dd> Sets the x (horizontal) co-ordinate of the top left corner of the window, in pixels. </p>
<dt><code>-y </code><i>pixels</i></p>
<dd> Sets the y (vertical) co-ordinate of the top left corner of the window, in pixels. </p>
<dt><code>&#8211;engine </code><i>name</i></p>
<dd> Start <code>plasmaengineexplorer</code> with the given data engine selected. <i>name</i> is the internal name of the data engine given by the X-KDE-PluginInfo-Name key of the desktop file. </p>
<dt><code>&#8211;source </code><i>name</i></p>
<dd> Only valid in conjunction with <code>&#8211;engine</code>. Requests a specific source from the data engine when <code>plasmaengineexplorer</code> is started. </p>
<dt><code>&#8211;interval </code><i>time</i></p>
<dd> Sets the default update interval for requested sources to <i>time</i> milliseconds. If not set, the source will update on demand (for some sources, this will be when new data is available). </p>
<p> If <code>&#8211;source</code> is specified, this is the update interval that will be used when requesting that source. </p>
</dl>
<h2>SEE ALSO</h2>
<p> More detailed user documentation is available from <i>help:/plasma</i> (either enter this URL into Konqueror, or run <code>khelpcenter</code> <i>help:/plasma</i>). </p>
<h2>EXAMPLES</h2>
<p> Load the time data engine, showing the local time and updating every second: </p>
<dl>
<dt>
<dd> <code>plasmaengineexplorer</code> <code>&#8211;engine time</code> <code>&#8211;source Local</code> <code>&#8211;interval 1000</code></dl>
<h2>AUTHORS</h2>
<p> <code>plasmaengineexplorer</code> was written by Aaron Seigo &lt;aseigo [at] kde.org&gt;. </p>
<h2>Index</h2>

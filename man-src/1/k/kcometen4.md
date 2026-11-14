---
title: "kcometen4(1)"
name: "kcometen4"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kcometen4/"
description: "kcometen4.kss – An OpenGL screensaver with exploding comets."
---

<h2>NAME</h2>
<p> kcometen4.kss &#8211; An OpenGL screensaver with exploding comets.</p>
<h2>SYNOPSIS</h2>
<p> <code>kcometen4.kss</code> [<i>Qt options</i>] [<i>KDE options</i>] [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> KCometen4 is an OpenGL screensaver. A variety of multi-colored comets bounce inside a room until they explode. Occasionally lightning will also strike and blow them up. Meanwhile, a free-floating camera watches the action and sometimes enters a slow motion &quot;bullet time&quot; mode. It is suprisingly hypnotic.</p>
<h2>OPTIONS</h2>
<h3>Options:</h3>
<dl>
<dt><code>&#8211;setup</code></p>
<dd> Setup screen saver</p>
<dt><code>&#8211;window-id</code><i>&nbsp;<wbr>wid</i></p>
<dd> Run in the specified XWindow</p>
<dt><code>&#8211;root</code></p>
<dd> Run in the root XWindow</p>
<dt><code>&#8211;demo</code></p>
<dd> Start screen saver in demo mode [default]</dl>
<h3>Generic options:</h3>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Show help about options</p>
<dt><code>&#8211;help-qt</code></p>
<dd> Show Qt specific options</p>
<dt><code>&#8211;help-kde</code></p>
<dd> Show KDE specific options</p>
<dt><code>&#8211;help-all</code></p>
<dd> Show all options</p>
<dt><code>&#8211;author</code></p>
<dd> Show author information</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Show version information</p>
<dt><code>&#8211;license</code></p>
<dd> Show license information</p>
<dt><code>&#8212;</code></p>
<dd> End of options</dl>
<h3>
<h3>KDE options:</h3>
</h3>
<dl>
<dt><code>&#8211;caption</code><i>&nbsp;<wbr>caption</i></p>
<dd> Use <i>caption</i> as name in the titlebar</p>
<dt><code>&#8211;icon</code><i>&nbsp;<wbr>icon</i></p>
<dd> Use <i>icon</i> as the application icon</p>
<dt><code>&#8211;config</code><i>&nbsp;<wbr>filename</i></p>
<dd> Use alternative configuration file</p>
<dt><code>&#8211;nocrashhandler</code></p>
<dd> Disable crash handler, to get core dumps</p>
<dt><code>&#8211;waitforwm</code></p>
<dd> Waits for a <code>WM_NET</code> compatible windowmanager</p>
<dt><code>&#8211;style</code><i>&nbsp;<wbr>style</i></p>
<dd> sets the application GUI style</p>
<dt><code>&#8211;geometry</code><i>&nbsp;<wbr>geometry</i></p>
<dd> sets the client geometry of the main widget &#8211; see <code><a href="/docs/linux/man/7-x/">X</a></code>(7) for the argument format</dl>
<h3>
<h3>Qt options:</h3>
</h3>
<dl>
<dt><code>&#8211;display</code><i>&nbsp;<wbr>displayname</i></p>
<dd> Use the X-server display <i>displayname</i></p>
<dt><code>&#8211;session</code><i>&nbsp;<wbr>sessionId</i></p>
<dd> Restore the application for the given <i>sessionId</i></p>
<dt><code>&#8211;cmap</code></p>
<dd> Causes the application to install a private color map on an 8-bit display</p>
<dt><code>&#8211;ncols</code><i>&nbsp;<wbr>count</i></p>
<dd> Limits the number of colors allocated in the color cube on an 8-bit display, if the application is using the <code>QApplication::ManyColor</code> color specification</p>
<dt><code>&#8211;nograb</code></p>
<dd> tells Qt to never grab the mouse or the keyboard</p>
<dt><code>&#8211;dograb</code></p>
<dd> running under a debugger can cause an implicit <code>-nograb</code>, use<code>&nbsp;<wbr>-dograb</code> to override</p>
<dt><code>&#8211;sync</code></p>
<dd> switches to synchronous mode for debugging</p>
<dt><code>&#8211;fn, &#8211;font</code><i>&nbsp;<wbr>fontname</i></p>
<dd> defines the application font</p>
<dt><code>&#8211;bg, &#8211;background</code><i>&nbsp;<wbr>color</i></p>
<dd> sets the default background color and an application palette (light and dark shades are calculated)</p>
<dt><code>&#8211;fg, &#8211;foreground</code><i>&nbsp;<wbr>color</i></p>
<dd> sets the default foreground color</p>
<dt><code>&#8211;btn, &#8211;button</code><i>&nbsp;<wbr>color</i></p>
<dd> sets the default button color</p>
<dt><code>&#8211;name</code><i>&nbsp;<wbr>name</i></p>
<dd> sets the application name</p>
<dt><code>&#8211;title</code><i>&nbsp;<wbr>title</i></p>
<dd> sets the application caption title</p>
<dt><code>&#8211;visual TrueColor</code></p>
<dd> forces the application to use a TrueColor visual on an 8-bit display</p>
<dt><code>&#8211;inputstyle</code><i>&nbsp;<wbr>inputstyle</i></p>
<dd> sets XIM (X Input Method) input style. Possible values are <code>onthespot</code>, <code>overthespot</code>, <code>offthespot</code>, and<code>&nbsp;<wbr>root</code></p>
<dt><code>&#8211;im</code><i>&nbsp;<wbr>XIM server</i></p>
<dd> set XIM server</p>
<dt><code>&#8211;noxim</code></p>
<dd> disable XIM</p>
<dt><code>&#8211;reverse</code></p>
<dd> mirrors the whole layout of widgets</p>
<dt><code>&#8211;stylesheet</code><i>&nbsp;<wbr>file.qss</i></p>
<dd> applies the Qt stylesheet to the application widgets</dl>
<h3></h3>
<h2>AUTHORS</h2>
<p> Peter Müller &lt;pmueller [at] cs.tu-berlin.de&gt; wrote the original program for KDE3 as KCometen3.<br />
 John Stamp &lt;jstamp [at] users.sourceforge.net&gt; ported it to KDE4 and added a few bugfixes and features. </p>
<p> This manual page was written by John Stamp &lt;jstamp [at] users.sourceforge.net&gt;. Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation. </p>
<h2>Index</h2>
<dt><a href="#lbAO">AUTHORS</a></p>
<dd></dl>

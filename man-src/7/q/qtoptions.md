---
title: "qtoptions(7)"
name: "qtoptions"
section: "7"
letter: "q"
url: "/docs/linux/man/7-qtoptions/"
description: "qtoptions – Common commandline options for all applications based on the Qt toolkit"
---

<p>qtoptions &#8211; Common commandline options for all applications based on the Qt toolkit</p>
<h2>Synopsis</h2>
<dl>
<dt> <i>Qt application</i> [Qt Generic Options]</dl>
<h2>Options</h2>
<dd>The following options apply to all Qt(TM) applications: </p>
<p> <code>&#8211;display</code> <i>displayname</i></p>
<dl>
<dd>Use the X-server display <i>displayname</i>.</dl>
<p> <code>&#8211;session</code> <i>sessionId</i></p>
<dl>
<dd>Restore the application for the given <i>sessionId</i>.</dl>
<p> <code>&#8211;cmap</code></p>
<dl>
<dd>Causes the application to install a private color map on an 8-bit display.</dl>
<p> <code>&#8211;ncols</code> <i>count</i></p>
<dl>
<dd>Limits the number of colors allocated in the color cube on an 8-bit display, if the application is using the QApplication::ManyColor color specification.</dl>
<p> <code>&#8211;nograb</code></p>
<dl>
<dd>Tells Qt(TM) to never grab the mouse or the keyboard.</dl>
<p> <code>&#8211;dograb</code></p>
<dl>
<dd>Running under a debugger can cause an implicit <code>&#8211;nograb</code>, use <code>&#8211;dograb</code> to override.</dl>
<p> <code>&#8211;sync</code></p>
<dl>
<dd>Switches to synchronous mode for debugging.</dl>
<p> <code>&#8211;fn</code>,<code>&#8211;font</code> <i>fontname</i></p>
<dl>
<dd>Defines the application font.</dl>
<p> <code>&#8211;bg</code>,<code>&#8211;background</code> <i>color</i></p>
<dl>
<dd>Sets the default background color and an application palette (light and dark shades are calculated).</dl>
<p> <code>&#8211;fg</code>,<code>&#8211;foreground</code> <i>color</i></p>
<dl>
<dd>Sets the default foreground color</dl>
<p> <code>&#8211;btn</code>,<code>&#8211;button</code> <i>color</i></p>
<dl>
<dd>Sets the default button color.</dl>
<p> <code>&#8211;name</code> <i>name</i></p>
<dl>
<dd>Sets the application name.</dl>
<p> <code>&#8211;title</code> <i>title</i></p>
<dl>
<dd>Sets the application title (caption).</dl>
<p> <code>&#8211;visual</code> <i>TrueColor</i></p>
<dl>
<dd>Forces the application to use a <i>TrueColor</i> visual on an 8-bit display.</dl>
<p> <code>&#8211;inputstyle</code> <i>inputstyle</i></p>
<dl>
<dd>Sets XIM (X Input Method) input style. Possible values are <i>onthespot</i>, <i>overthespot</i>, <i>offthespot</i> and <i>root</i>.</dl>
<p> <code>&#8211;im</code> <i>XIM server</i></p>
<dl>
<dd>Set XIM server.</dl>
<p> <code>&#8211;noxim</code></p>
<dl>
<dd>Disable XIM</dl>
<p> <code>&#8211;reverse</code></p>
<dl>
<dd>mirrors the whole layout of widgets</dl>
<p> <code>&#8211;stylesheet</code> <i>file.qss</i></p>
<dl>
<dd>applies the Qt stylesheet to the application widgets</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/7-kdeoptions/">kdeoptions</a></i>(7)</p>
<h2>Authors</h2>
<p>Man page written by Lauri Watts&lt;lauri [at] kde.org&gt;</p>
<h2>Author</h2>
<p><code>Lauri Watts</code> &lt;lauri [at] kde.org&gt;</p>
<dl>
<dd>Author.</dl>

---
title: "kdesvnaskpass(1)"
name: "kdesvnaskpass"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kdesvnaskpass/"
description: "kdesvnaskpass – ssh-askpass for kdesvn"
---

<h2>NAME</h2>
<p> kdesvnaskpass &#8211; ssh-askpass for kdesvn</p>
<h2>SYNOPSIS</h2>
<p> kdesvnaskpass [Qt-options] [KDE-options] [prompt]</p>
<h2>DESCRIPTION</h2>
<p> ssh-askpass for kdesvn</p>
<h2>OPTIONS</h2>
<h3>
<h3>Arguments:</h3>
</h3>
<dl>
<dt><code>prompt</code></dt>
<dd> Prompt that is displayed to the user.</dd></dl>
<h3>Generic options:</h3>
<dl>
<dt><code>&#8211;help </code></dt>
<dd> Show help about options</dd>
<dt><code>&#8211;help-qt </code></dt>
<dd> Show Qt specific options</dd>
<dt><code>&#8211;help-kde </code></dt>
<dd> Show KDE specific options</dd>
<dt><code>&#8211;help-all </code></dt>
<dd> Show all options</dd>
<dt><code>&#8211;author </code></dt>
<dd> Show author information</dd>
<dt><code>-v, &#8211;version </code></dt>
<dd> Show version information</dd>
<dt><code>&#8211;license </code></dt>
<dd> Show license information</dd>
<dt><code>&#8212; </code></dt>
<dd> End of options</dd></dl>
<h3>
<h3>KDE options:</h3>
</h3>
<dl>
<dt><code>&#8211;caption &lt;caption&gt;</code></dt>
<dd> Use &#8216;caption&#8217; as name in the titlebar</dd>
<dt><code>&#8211;icon &lt;icon&gt;</code></dt>
<dd> Use &#8216;icon&#8217; as the application icon</dd>
<dt><code>&#8211;config &lt;filename&gt;</code></dt>
<dd> Use alternative configuration file</dd>
<dt><code>&#8211;nocrashhandler </code></dt>
<dd> Disable crash handler, to get core dumps</dd>
<dt><code>&#8211;waitforwm </code></dt>
<dd> Waits for a WM_NET compatible windowmanager</dd>
<dt><code>&#8211;style &lt;style&gt;</code></dt>
<dd> sets the application GUI style</dd>
<dt><code>&#8211;geometry &lt;geometry&gt;</code></dt>
<dd> sets the client geometry of the main widget &#8211; see man X for the argument format</dd></dl>
<h3>
<h3>Qt options:</h3>
</h3>
<dl>
<dt><code>&#8211;display &lt;displayname&gt;</code></dt>
<dd> Use the X-server display &#8216;displayname&#8217;</dd>
<dt><code>&#8211;session &lt;sessionId&gt;</code></dt>
<dd> Restore the application for the given &#8216;sessionId&#8217;</dd>
<dt><code>&#8211;cmap </code></dt>
<dd> Causes the application to install a private color map on an 8-bit display</dd>
<dt><code>&#8211;ncols &lt;count&gt;</code></dt>
<dd> Limits the number of colors allocated in the color cube on an 8-bit display, if the application is using the QApplication::ManyColor color specification</dd>
<dt><code>&#8211;nograb </code></dt>
<dd> tells Qt to never grab the mouse or the keyboard</dd>
<dt><code>&#8211;dograb </code></dt>
<dd> running under a debugger can cause an implicit -nograb, use -dograb to override</dd>
<dt><code>&#8211;sync </code></dt>
<dd> switches to synchronous mode for debugging</dd>
<dt><code>&#8211;fn, &#8211;font &lt;fontname&gt;</code></dt>
<dd> defines the application font</dd>
<dt><code>&#8211;bg, &#8211;background &lt;color&gt;</code></dt>
<dd> sets the default background color and an application palette (light and dark shades are calculated)</dd>
<dt><code>&#8211;fg, &#8211;foreground &lt;color&gt;</code></dt>
<dd> sets the default foreground color</dd>
<dt><code>&#8211;btn, &#8211;button &lt;color&gt;</code></dt>
<dd> sets the default button color</dd>
<dt><code>&#8211;name &lt;name&gt;</code></dt>
<dd> sets the application name</dd>
<dt><code>&#8211;title &lt;title&gt;</code></dt>
<dd> sets the application title (caption)</dd>
<dt><code>&#8211;visual TrueColor</code></dt>
<dd> forces the application to use a TrueColor visual on an 8-bit display</dd>
<dt><code>&#8211;inputstyle &lt;inputstyle&gt;</code></dt>
<dd> sets XIM (X Input Method) input style. Possible values are onthespot, overthespot, offthespot and root</dd>
<dt><code>&#8211;im &lt;XIM server&gt;</code></dt>
<dd> set XIM server</dd>
<dt><code>&#8211;noxim </code></dt>
<dd> disable XIM</dd>
<dt><code>&#8211;reverse </code></dt>
<dd> mirrors the whole layout of widgets</dd>
<dt><code>&#8211;stylesheet </code></dt>
<dd> &lt;file.qss&gt; applies the Qt stylesheet to the application widgets</dd></dl>
<h3></h3>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-kdesvn/">kdesvn</a>(1)</code> </p>
<h2>AUTHORS</h2>
<pre>
Rajko Albrecht &lt;ral [at] alwins-world.de&gt;
<br>
</pre>
<h2>Index</h2>
<dt><a href="#lbAQ">SEE ALSO</a></dt>
<dd>
</dd><dt><a href="#lbAR">AUTHORS</a></dt>
<dd></dd></dl>

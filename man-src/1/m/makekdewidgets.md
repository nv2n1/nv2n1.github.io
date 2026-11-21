---
title: "makekdewidgets(1)"
name: "makekdewidgets"
section: "1"
letter: "m"
url: "/docs/linux/man/1-makekdewidgets/"
description: "makekdewidgets – Builds Qt(TM) widget plugins from an ini style description file."
---

<h2>SYNOPSIS</h2>
<dl>
<dt> <code>makekdewidgets</code> [Qt(TM)-options] [KDE-options] <i>file</i></dt></dl>
<h2>DESCRIPTION</h2>
<p> <code>makekdewidgets</code></p>
<dd>builds Qt(TM) widget plugins from an ini style description file.</dd>
<h2>OPTIONS</h2>
<p> <code>Arguments:</code> </p>
<p> <i>file</i></p>
<dl>
<dt>
</dt><dd> Input file</dd></dl>
<p> <code>Options:</code> </p>
<p> <code>-o &lt;file&gt;</code></p>
<dl>
<dt>
</dt><dd> Output file</dd></dl>
<p> <code>-n &lt;plugin name&gt;</code></p>
<dl>
<dt>
</dt><dd> Name of the plugin class to generate [WidgetsPlugin]</dd></dl>
<p> <code>-g &lt;group&gt;</code></p>
<dl>
<dt>
</dt><dd> Default widget group name to display in designer [Custom]</dd></dl>
<p> <code>-p &lt;pixmap dir&gt;</code></p>
<dl>
<dt>
</dt><dd> Embed pixmaps from a source directory</dd></dl>
<p> <code>Generic options:</code> </p>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
</dt><dd> Show help about options</dd></dl>
<p> <code>&#8211;help-qt</code></p>
<dl>
<dt>
</dt><dd> Show Qt(TM) specific options</dd></dl>
<p> <code>&#8211;help-kde</code></p>
<dl>
<dt>
</dt><dd> Show KDE specific options</dd></dl>
<p> <code>&#8211;help-all</code></p>
<dl>
<dt>
</dt><dd> Show all options</dd></dl>
<p> <code>&#8211;author</code></p>
<dl>
<dt>
</dt><dd> Show author information</dd></dl>
<p> <code>-v, &#8211;version</code></p>
<dl>
<dt>
</dt><dd> Show version information</dd></dl>
<p> <code>&#8211;license</code></p>
<dl>
<dt>
</dt><dd> Show license information</dd></dl>
<p> <code>KDE Options:</code> </p>
<p> <code>&#8211;caption &lt;caption&gt;</code></p>
<dl>
<dt>
</dt><dd> Use &#8216;caption&#8217; as name in the titlebar</dd></dl>
<p> <code>&#8211;icon &lt;icon&gt;</code></p>
<dl>
<dt>
</dt><dd> Use &#8216;icon&#8217; as the application icon</dd></dl>
<p> <code>&#8211;miniicon &lt;icon&gt;</code></p>
<dl>
<dt>
</dt><dd> Use &#8216;icon&#8217; as the application icon</dd></dl>
<p> <code>&#8211;config &lt;filename&gt;</code></p>
<dl>
<dt>
</dt><dd> Use alternative configuration file</dd></dl>
<p> <code>&#8211;dcopserver &lt;server&gt;</code></p>
<dl>
<dt>
</dt><dd> Use the DCOP server specified by &#8216;server&#8217;</dd></dl>
<p> <code>&#8211;nocrashhandler</code></p>
<dl>
<dt>
</dt><dd> Disable crash handler to get core dumps</dd></dl>
<p> <code>&#8211;waitforwm</code></p>
<dl>
<dt>
</dt><dd> Waits for a WM_NET compatible windowmanager</dd></dl>
<p> <code>&#8211;style &lt;style&gt;</code></p>
<dl>
<dt>
</dt><dd> Sets the application GUI style</dd></dl>
<p> <code>&#8211;geometry &lt;geometry&gt;</code></p>
<dl>
<dt>
</dt><dd> Sets the client geometry of the main widget &#8211; see man X for the argument format</dd></dl>
<p> <code>Qt(TM) options:</code> </p>
<p> <code>&#8211;display &lt;displayname&gt;</code></p>
<dl>
<dt>
</dt><dd> Use the X-server display &#8216;displayname&#8217;</dd></dl>
<p> <code>&#8211;session &lt;sessionId&gt;</code></p>
<dl>
<dt>
</dt><dd> Restore the application for the given &#8216;sessionId&#8217;</dd></dl>
<p> <code>&#8211;cmap</code></p>
<dl>
<dt>
</dt><dd> Causes the application to install a private color map on an 8-bit display</dd></dl>
<p> <code>&#8211;ncols &lt;count&gt;</code></p>
<dl>
<dt>
</dt><dd> Limits the number of colors allocated in the color cube on an 8-bit display, if the application is using the QApplication::ManyColor color specification</dd></dl>
<p> <code>&#8211;nograb</code></p>
<dl>
<dt>
</dt><dd> Tells Qt(TM) to never grab the mouse or the keyboard</dd></dl>
<p> <code>&#8211;sync</code></p>
<dl>
<dt>
</dt><dd> Switches to synchronous mode for debugging</dd></dl>
<p> <code>&#8211;fn, &#8211;font &lt;fontname&gt;</code></p>
<dl>
<dt>
</dt><dd> Defines the application font</dd></dl>
<p> <code>&#8211;bg, &#8211;background &lt;color&gt;</code></p>
<dl>
<dt>
</dt><dd> Sets the default background color and an application palette (light and dark shades are calculated)</dd></dl>
<p> <code>&#8211;fg, &#8211;foreground &lt;color&gt;</code></p>
<dl>
<dt>
</dt><dd> Sets the default foreground color</dd></dl>
<p> <code>&#8211;btn, &#8211;button &lt;color&gt;</code></p>
<dl>
<dt>
</dt><dd> Sets the default button color</dd></dl>
<p> <code>&#8211;name &lt;name&gt;</code></p>
<dl>
<dt>
</dt><dd> Sets the application name</dd></dl>
<p> <code>&#8211;title &lt;title&gt;</code></p>
<dl>
<dt>
</dt><dd> Sets the application title (caption)</dd></dl>
<p> <code>&#8211;visual TrueColor</code></p>
<dl>
<dt>
</dt><dd> Forces the application to use a TrueColor visual on an 8-bit display</dd></dl>
<p> <code>&#8211;inputstyle &lt;inputstyle&gt;</code></p>
<dl>
<dt>
</dt><dd> Sets XIM (X Input Method) input style. Possible values are onthespot, overthespot, offthespot, and root</dd></dl>
<p> <code>&#8211;im &lt;XIM server&gt;</code></p>
<dl>
<dt>
</dt><dd> Sets XIM server</dd></dl>
<p> <code>&#8211;noxim</code></p>
<dl>
<dt>
</dt><dd> Disable XIM</dd></dl>
<p> <code>&#8211;reverse</code></p>
<dl>
<dt>
</dt><dd> Mirrors the whole layout of widgets</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a rel="nofollow" href="http://developer.kde.org">http://developer.kde.org</a></code></p>
<dl>
<dt>
</dt><dd> KDE Developer&#8217;s Corner website</dd></dl>
<h2>BUGS</h2>
<p> Please use m[blue]<code>bugs.kde.org</code>m[]<font SIZE="-2">[1]</font> to report bugs, do not mail the authors directly.</p>
<h2>AUTHOR</h2>
<p> <code>Ian Reinhart Geiser</code> &lt;geiseri [at] kde.org&gt;</p>
<dl>
<dt>
</dt><dd> Author.</dd></dl>
<h2>NOTES</h2>
<dl>
<dt> 1.</dt>
<dd> bugs.kde.org</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://bugs.kde.org">http://bugs.kde.org</a></dd></dl>
</dl>

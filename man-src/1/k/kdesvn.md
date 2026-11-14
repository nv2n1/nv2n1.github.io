---
title: "kdesvn(1)"
name: "kdesvn"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kdesvn/"
description: "kdesvn – A Subversion client for KDE (standalone application)"
---

<h2>NAME</h2>
<p> kdesvn &#8211; A Subversion client for KDE (standalone application)</p>
<h2>SYNOPSIS</h2>
<p> kdesvn [Qt-options] [KDE-options] [options] exec &lt;command&gt; [URL]</p>
<h2>DESCRIPTION</h2>
<p> A Subversion client for KDE (standalone application)</p>
<h2>OPTIONS</h2>
<h3>
<h3>Arguments:</h3>
</h3>
<dl>
<dt><code>exec</code></p>
<dd> &lt;command&gt; Execute subversion command (&quot;exec help&quot; for more information, opens KDE Help Center)</p>
<dt><code>URL</code></p>
<dd> Path to local working copy or a repository.</dl>
<h3>Options:</h3>
<dl>
<dt><code>-r startrev</code></p>
<dd> [:endrev] Execute single subversion command on specific revision(-range)</p>
<dt><code>-R </code></p>
<dd> Ask for revision when executing single command</p>
<dt><code>-f </code></p>
<dd> Force operation</p>
<dt><code>-o &lt;file&gt;</code></p>
<dd> Save output of subversion command (eg &quot;cat&quot;) into file &lt;file&gt;</p>
<dt><code>-l &lt;number&gt;</code></p>
<dd> Limit log output to &lt;number&gt;</dl>
<h3>
<h3>Generic options:</h3>
</h3>
<dl>
<dt><code>&#8211;help </code></p>
<dd> Show help about options</p>
<dt><code>&#8211;help-qt </code></p>
<dd> Show Qt specific options</p>
<dt><code>&#8211;help-kde </code></p>
<dd> Show KDE specific options</p>
<dt><code>&#8211;help-all </code></p>
<dd> Show all options</p>
<dt><code>&#8211;author </code></p>
<dd> Show author information</p>
<dt><code>-v, &#8211;version </code></p>
<dd> Show version information</p>
<dt><code>&#8211;license </code></p>
<dd> Show license information</p>
<dt><code>&#8212; </code></p>
<dd> End of options</dl>
<h3>
<h3>KDE options:</h3>
</h3>
<dl>
<dt><code>&#8211;caption &lt;caption&gt;</code></p>
<dd> Use &#8216;caption&#8217; as name in the titlebar</p>
<dt><code>&#8211;icon &lt;icon&gt;</code></p>
<dd> Use &#8216;icon&#8217; as the application icon</p>
<dt><code>&#8211;config &lt;filename&gt;</code></p>
<dd> Use alternative configuration file</p>
<dt><code>&#8211;nocrashhandler </code></p>
<dd> Disable crash handler, to get core dumps</p>
<dt><code>&#8211;waitforwm </code></p>
<dd> Waits for a WM_NET compatible windowmanager</p>
<dt><code>&#8211;style &lt;style&gt;</code></p>
<dd> sets the application GUI style</p>
<dt><code>&#8211;geometry &lt;geometry&gt;</code></p>
<dd> sets the client geometry of the main widget &#8211; see man X for the argument format</dl>
<h3>
<h3>Qt options:</h3>
</h3>
<dl>
<dt><code>&#8211;display &lt;displayname&gt;</code></p>
<dd> Use the X-server display &#8216;displayname&#8217;</p>
<dt><code>&#8211;session &lt;sessionId&gt;</code></p>
<dd> Restore the application for the given &#8216;sessionId&#8217;</p>
<dt><code>&#8211;cmap </code></p>
<dd> Causes the application to install a private color map on an 8-bit display</p>
<dt><code>&#8211;ncols &lt;count&gt;</code></p>
<dd> Limits the number of colors allocated in the color cube on an 8-bit display, if the application is using the QApplication::ManyColor color specification</p>
<dt><code>&#8211;nograb </code></p>
<dd> tells Qt to never grab the mouse or the keyboard</p>
<dt><code>&#8211;dograb </code></p>
<dd> running under a debugger can cause an implicit -nograb, use -dograb to override</p>
<dt><code>&#8211;sync </code></p>
<dd> switches to synchronous mode for debugging</p>
<dt><code>&#8211;fn, &#8211;font &lt;fontname&gt;</code></p>
<dd> defines the application font</p>
<dt><code>&#8211;bg, &#8211;background &lt;color&gt;</code></p>
<dd> sets the default background color and an application palette (light and dark shades are calculated)</p>
<dt><code>&#8211;fg, &#8211;foreground &lt;color&gt;</code></p>
<dd> sets the default foreground color</p>
<dt><code>&#8211;btn, &#8211;button &lt;color&gt;</code></p>
<dd> sets the default button color</p>
<dt><code>&#8211;name &lt;name&gt;</code></p>
<dd> sets the application name</p>
<dt><code>&#8211;title &lt;title&gt;</code></p>
<dd> sets the application title (caption)</p>
<dt><code>&#8211;visual TrueColor</code></p>
<dd> forces the application to use a TrueColor visual on an 8-bit display</p>
<dt><code>&#8211;inputstyle &lt;inputstyle&gt;</code></p>
<dd> sets XIM (X Input Method) input style. Possible values are onthespot, overthespot, offthespot and root</p>
<dt><code>&#8211;im &lt;XIM server&gt;</code></p>
<dd> set XIM server</p>
<dt><code>&#8211;noxim </code></p>
<dd> disable XIM</p>
<dt><code>&#8211;reverse </code></p>
<dd> mirrors the whole layout of widgets</p>
<dt><code>&#8211;stylesheet </code></p>
<dd> &lt;file.qss&gt; applies the Qt stylesheet to the application widgets</dl>
<h3></h3>
<h2>EXAMPLE</h2>
<p> kdesvn file:///path/to/local/working/copy<br />
 kdesvn <a rel="nofollow" href="http://remote/svn/project/trunk">http://remote/svn/project/trunk</a> </p>
<h2>SEE ALSO</h2>
<p> Full user documentation is available through the KDE Help Center. You can also enter the URL <code>help:/kdesvn/</code> directly into konqueror or you can run <code>`khelpcenter help:/kdesvn/&#8217;</code> from the command-line. </p>
<h2>AUTHORS</h2>
<pre>
Rajko Albrecht &lt;ral [at] alwins-world.de&gt;
<br>
</pre>
<h2>Index</h2>
<dt><a href="#lbAT">EXAMPLE</a></p>
<dd>
<dt><a href="#lbAU">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAV">AUTHORS</a></p>
<dd></dl>

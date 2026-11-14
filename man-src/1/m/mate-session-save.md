---
title: "mate-session-save(1)"
name: "mate-session-save"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mate-session-save/"
description: "mate-session-save – End or save the current MATE session"
---

<h2 class="name">NAME</h2>
<p> mate-session-save &#8211; End or save the current MATE session </p>
<h2>SYNOPSIS</h2>
<p> <code>mate-session-save [&#8211;logout] [&#8211;force-logout] [&#8211;logout-dialog] [&#8211;shutdown-dialog] [&#8211;gui] [&#8211;kill [&#8211;silent]]</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>mate-session-save</code> program can be used from a MATE session to either end the current MATE session or save a snapshot of the currently running applications (but not both). This session will be later restored at your next MATE session.</p>
<h2>USAGE</h2>
<p> The <code>&#8211;gui</code> option will report errors in dialog boxes instead of printing to stderr. </p>
<p> If called with the <code>&#8211;logout</code> option, the current MATE session will be ended, unless logging out has been inhibited by an application. The <code>&#8211;force-logout</code> option can be used to end the session regardless of the inhibition state. </p>
<p> When the <code>&#8211;logout-dialog</code> option is given, the standard dialog displaying logout options is displayed. When <code>&#8211;shutdown-dialog</code> option is given, the standard dialog displaying shutdown options is displayed. </p>
<p> The <code>&#8211;kill</code> and <code>&#8211;silent</code> options are deprecated. The <code>&#8211;kill</code> option is equivalent to the <code>&#8211;logout-dialog</code> option. If <code>&#8211;silent</code> is used with <code>&#8211;kill</code>, then it will behave as if <code>&#8211;logout</code> was used. </p>
<p> The session is not saved when <code>mate-session-save</code> is called with any of the options ending the session.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;logout</code></p>
<dd> Log out</p>
<dt><code>&#8211;force-logout</code></p>
<dd> Log out, ignoring any existing inhibitors</p>
<dt><code>&#8211;ogout-dialog</code></p>
<dd> Show logout dialog</p>
<dt><code>&#8211;shutdown-dialog</code></p>
<dd> Show shutdown dialog</p>
<dt><code>&#8211;gui</code></p>
<dd>
 Use dialog boxes for errors</p>
<dt><code>&#8211;display=DISPLAY</code></p>
<dd> X display to use.</p>
<dt><code>&#8211;version</code></p>
<dd> Output version information and exit.</p>
<dt><code>-?, -h, &#8211;help</code></p>
<dd> Print standard command line options.</p>
<dt><code>&#8211;help-all</code></p>
<dd> Print all command line options.</dl>
<h2>BUGS</h2>
<h3>Should you encounter any bugs, they may be reported at:</h3>
<p> <a rel="nofollow" href="http://github.com/mate-desktop/mate-session/issues">http://github.com/mate-desktop/mate-session/issues</a></p>
<h2>AUTHORS</h2>
<h3>This Man Page has been updated/re-written for the MATE Desktop Environment by:</h3>
<p> Adam Erdman &lt;hekel [at] archlinux.info&gt; (2014)</p>
<h2>HISTORY</h2>
<h3>This Manual was originally written for gnome-session by:</h3>
<pre><code>
Miguel de Icaza&lt;miguel[at] helixcode.com&gt;(2000)
    Vincent Untz&lt;vuntz[at] gnome.org&gt;(2009 - 2010)
</code></pre>
<h2>SEE ALSO</h2>
<h3>Further information may also be available at: <a rel="nofollow" href="http://wiki.mate-desktop.org/docs">http://wiki.mate-desktop.org/docs</a></h3>
<p> <code><a href="/docs/linux/man/1-mate-session-properties/">mate-session-properties</a>(1),</code> <code><a href="/docs/linux/man/1-mate-wm/">mate-wm</a>(1),</code> <code><a href="/docs/linux/man/1-mate-session/">mate-session</a>(1)</code> </p>
<h2>Index</h2>

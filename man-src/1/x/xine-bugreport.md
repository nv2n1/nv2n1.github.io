---
title: "xine-bugreport(1)"
name: "xine-bugreport"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xine-bugreport/"
description: "xine-check – a checker for the xine video player"
---

<h2 class="name">NAME</h2>
<p> xine-check &#8211; a checker for the xine video player</p>
<h2>SYNOPSIS</h2>
<p> <code>xine-check </code> [<i>-q</i>] [<i>-v</i>] [<i>-B</i>] [<i>-b</i>]<br />
 <code>xine-bugreport</code> [<i>-q</i>] [<i>-v</i>] [<i>-B</i>] </p>
<h2>DESCRIPTION</h2>
<p> This manual page explains the xine-checker program. <code>xine-check</code> is a program, which tests the xine video player installation for common problems. </p>
<p> If you experience any problem with or while running <code>xine</code>, running <code>xine-check</code> might provide useful hints for problem tracking. </p>
<p> <code>xine-check</code> tests the operating system settings, installation of plugins, CD/DVD drive settings and video support parameters. </p>
<p> If run as <code>xine-bugreport,</code> it will produce a terse system description and guide you through the process of reporting a bug. This is the preferred way to report xine bugs, as it&#8217;s easier for you and provides the developers with a more complete bugreport. </p>
<h2>OPTIONS</h2>
<p> The program follows usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options are included below. For a complete description, see <i>README</i> and <i>FAQ</i> in <i>/usr/share/doc/xine-ui-0.99.9</i> or on the xine home page. <code></p>
<dl>
<dt>-h, &#8211;help</p>
<dd> </code> Show summary of options and version number.</dl>
<p> The remaining options, labelled <code>XINE-CHECK options:</code> when listed with &quot;xine-check &#8211;help&quot;, are explained here. <code></p>
<dl>
<dt>-q, &#8211;quiet</p>
<dd> </code> Only give a single one-line messages, even if problems are found. Normally <code>xine-check</code> provides hints for every problem found to help solve the problem. <code></p>
<dt>-v, &#8211;verbose</p>
<dd> </code> Enable extended output describing each check in detail, which produces a kind of frequently asked questions (FAQ) list. <code></p>
<dt>-B, &#8211;batch</p>
<dd> </code> Turn off pause after long messages. Normally <code>xine-check</code> waits for confirmation after a problem was found or a long message was printed. <code></p>
<dt>-b, &#8211;bug</p>
<dd> </code> Produce a bug report. This is the same as calling <code>xine-bugreport</code> directly. </p>
</dl>
<h2>BUGS</h2>
<p> none, of course ;-) Well, there are surely a few of those. You can probably best ask for support (and report bugs) on our mailing list at &lt;xine-user [at] lists.sf.net&gt;. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xine/">xine</a></code>(1), <code><a href="/docs/linux/man/1-aaxine/">aaxine</a></code>(1), <code><a href="/docs/linux/man/3-xine-lib/">xine-lib</a></code>(3), <code><a rel="nofollow" href="http://www.xine-project.org/">http://www.xine-project.org/</a></code> </p>
<h2>AUTHOR</h2>
<p> This manual page was written by Philipp Hahn &lt;pmhahn [at] users.sf.net&gt; for the xine project. </p>
<h2>COPYRIGHT NOTICE</h2>
<p> Copyright &#169; 2002 Siggi Langauf </p>
<h2>Index</h2>

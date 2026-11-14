---
title: "seahorse-tool(1)"
name: "seahorse-tool"
section: "1"
letter: "s"
url: "/docs/linux/man/1-seahorse-tool/"
description: "seahorse-tool – PGP/GnuPG file encryption for the GNOME Desktop"
---

<h2 class="name">NAME</h2>
<p> seahorse-tool &#8211; PGP/GnuPG file encryption for the GNOME Desktop</p>
<h2>SYNOPSIS</h2>
<p> <code>seahorse-tool</code> [ <i>OPTION</i>&#8230; ] </p>
<h2>DESCRIPTION</h2>
<p> Seahorse is a GNOME application for managing encryption keys. <code>seahorse-tool</code> allows you to encrypt, decrypt or sign files. It is integrated into the nautilus right-click menu, but can also be used from the command line. </p>
<h2>OPTIONS</h2>
<h3>Help options</h3>
<dl>
<dt><code>-?, &#8211;help</code></p>
<dd> Show summary of all options and exit.</p>
<dt><code>&#8211;usage</code></p>
<dd> Display brief usage message and exit. </p>
</dl>
<h3>Application options</h3>
<dl>
<dt><code>-i </code><i>FILE</i>, <code>&#8211;import </code><i>FILE</i></p>
<dd> Import keys from the FILE.</p>
<dt><code>-e </code><i>FILE</i>, <code>&#8211;encrypt </code><i>FILE</i></p>
<dd> Encrypt FILE.</p>
<dt><code>-s </code><i>FILE</i>, <code>&#8211;sign </code><i>FILE</i></p>
<dd> Sign FILE with default key.</p>
<dt><code>-n </code><i>FILE</i>, <code>&#8211;encrypt-sign </code><i>FILE</i></p>
<dd> Encrypt and sign FILE with default key.</p>
<dt><code>-d </code><i>FILE</i>, <code>&#8211;decrypt </code><i>FILE</i></p>
<dd> Decrypt encrypted FILE.</p>
<dt><code>-v </code><i>FILE</i>, <code>&#8211;verify </code><i>FILE</i></p>
<dd> Verify signature FILE.</p>
<dt><code>-T, &#8211;uri-list</code></p>
<dd> Read list of URIs on standard in.</p>
<dt><code>&#8211;version</code></p>
<dd> Show version information and exit.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Show help options. </p>
</dl>
<h3>Additional options</h3>
<p> In addition, the usual GTK+ and GNOME command line options apply. See the output of &#8211;help for details. </p>
<h2>VERSION</h2>
<p> This man page describes <code>seahorse</code> version 0.9. </p>
<h2>BUGS</h2>
<p> If you find a bug, please report it at<br />
&nbsp;<wbr><i><a rel="nofollow" href="http://bugzilla.gnome.org/enter_bug.cgi?product=seahorse">http://bugzilla.gnome.org/enter_bug.cgi?product=seahorse</a></i>. </p>
<h2>AUTHORS</h2>
<p> Jacob Perkins &lt;jap1 [at] users.sourceforge.net&gt; </p>
<p> Stef Walter &lt;stef [at] memberwebs.com&gt; </p>
<p> Adam Schreiber &lt;sadam [at] clemson.edu&gt; </p>
<p> This man page was originally written by Michael Mende &lt;debian [at] menole.net&gt; for the Debian system. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2001, 2002 Jose Carlos Garcia Sogo<br />
 Copyright (C) 2002, 2003 Jacob Perkins<br />
 Copyright (C) 2004, 2006 Stef Walter, Adam Schreiber </p>
<h2>LICENSE</h2>
<p> You are free to distribute this software under the terms of the GNU General Public License.<br />
 Documentation and help files are covered by GFDL license. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-seahorse-daemon/">seahorse-daemon</a>(1)</code>, </p>
<h2>Index</h2>

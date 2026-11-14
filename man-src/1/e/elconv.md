---
title: "elconv(1)"
name: "elconv"
section: "1"
letter: "e"
url: "/docs/linux/man/1-elconv/"
description: "elconv – conversion program for ELOG messages"
---

<h2 class="name">NAME</h2>
<p> elconv &#8211; conversion program for ELOG messages </p>
<h2>SYNOPSIS</h2>
<p> <code>elconv</code> [ <code>-v</code> ]</p>
<h2>DESCRIPTION</h2>
<p> The Electronic Logbook <code>ELOG</code> can be used to store and retrieve messages through a Web interface. Depending on the configuration, the <code>ELOG</code> system can host one or more logbooks which are stored in separate sections on the server. <code>elconv</code> is a support tool which converts the <code>ELOG</code> messages in old format to the current format. Basically you simply run <code>elconv</code> in the directory where all the `*.log&#8217; files live. If you have several directories with log files, you run it once in each directory.</p>
<h2>OPTIONS</h2>
<p> <code>elconv</code> accepts the following option:</p>
<dl>
<dt><code>-v</code></p>
<dd> verbose output</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-elog/">elog</a></code>(1), <code><a href="/docs/linux/man/8-elogd/">elogd</a></code>(8). </p>
<p> The full documentation for <code>ELOG</code> is maintained as an html manual. You can reach it from the package document directory.</p>
<h2>AUTHOR</h2>
<p> Written by Stefan Ritt &lt;stefan.ritt [at] psi.ch&gt;. </p>
<p> This manual page was written by Recai Oktas &lt;roktas [at] omu.edu.tr&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>

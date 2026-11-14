---
title: "fsinfo(8)"
name: "fsinfo"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fsinfo/"
description: "fsinfo – coordinate site-wide filesystem information"
---

<p>fsinfo &#8211; coordinate site-wide filesystem information</p>
<h2>Synopsis</h2>
<p><code>fsinfo</code> [ <code>-v</code> ] [ <code>-a</code> <i>autodir</i> ] [ <code>-b</code> <i>bootparams</i> ] [ <code>-d</code> <i>dumpsets</i> ] [ <code>-e</code> <i>exports</i> ] [ <code>-f</code> <i>fstabs</i> ] [ <code>-h</code> <i>hostname</i> ] [ <code>-m</code> <i>automounts</i> ] [ <code>-I</code> <i>dir</i> ] [ <code>-D</code> <i>string[=string]</i> ] [ <code>-U</code> <i>string[=string]</i> ] <i>config</i> <i>&#8230;</i></p>
<h2>Description</h2>
<p>The <code>fsinfo</code> utility takes a set of system configuration information, and generates a coordinated set of <i>amd</i> , <i>mount</i> and <i>mountd</i> configuration files. </p>
<p> The <code>fsinfo</code> command is fully described in the document <i>Amd &#8211; The 4.4BSD Automounter</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amd/">amd</a></code>(8), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), <code><a href="/docs/linux/man/8-mountd/">mountd</a></code>(8). </p>
<p> &#8220;am-utils&#8221; <code><a href="/docs/linux/man/1-info/">info</a></code>(1) entry. </p>
<p> <i>Linux NFS and Automounter Administration</i> by Erez Zadok, ISBN 0-7821-2739-8, (Sybex, 2001). </p>
<p> <i><a rel="nofollow" href="http://www.am-utils.org">http://www.am-utils.org</a></i> </p>
<p> <i>Amd &#8211; The 4.4 BSD Automounter</i></p>
<h2>History</h2>
<p>The <code>fsinfo</code> command first appeared in 4.4BSD.</p>
<h2>Authors</h2>
<p>Jan-Simon Pendry &lt;jsp [at] doc.ic.ac.uk&gt;, Department of Computing, Imperial College, London, UK. </p>
<p> Erez Zadok &lt;ezk [at] cs.sunysb.edu&gt;, Computer Science Department, Stony Brook University, Stony Brook, New York, USA. </p>
<p> Other authors and contributors to am-utils are listed in the <code>AUTHORS</code> file distributed with am-utils.</p>

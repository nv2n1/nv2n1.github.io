---
title: "mk-amd-map(8)"
name: "mk-amd-map"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mk-amd-map/"
description: "mk-amd-map – create database maps for Amd"
---

<p><code>mk-amd-map</code> &#8211; create database maps for Amd</p>
<h2>Synopsis</h2>
<p><code>mk-amd-map</code> [ <code>-p</code> ] <i>mapname</i></p>
<h2>Description</h2>
<p><code>mk-amd-map</code> creates the database maps used by the keyed map lookups in <a href="/docs/linux/man/8-amd/">amd</a>(8). It reads input from the named file and outputs them to a correspondingly named hashed database.</p>
<dl>
<dt><code>-p</code></p>
<dd>This option prints the map on standard output instead of generating a database. This is usually used to merge continuation lines into one physical line.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amd/">amd</a></code>(8). </p>
<p> &#8220;am-utils&#8221; <code><a href="/docs/linux/man/1-info/">info</a></code>(1) entry. </p>
<p> <i>Linux NFS and Automounter Administration</i> by Erez Zadok, ISBN 0-7821-2739-8, (Sybex, 2001). </p>
<p> <i><a rel="nofollow" href="http://www.am-utils.org">http://www.am-utils.org</a></i> </p>
<p> <i>Amd &#8211; The 4.4 BSD Automounter</i></p>
<h2>Authors</h2>
<p>Jan-Simon Pendry &lt;jsp [at] doc.ic.ac.uk&gt;, Department of Computing, Imperial College, London, UK. </p>
<p> Erez Zadok &lt;ezk [at] cs.sunysb.edu&gt;, Computer Science Department, Stony Brook University, New York, USA. </p>
<p> Other authors and contributors to am-utils are listed in the <code>AUTHORS</code> file distributed with am-utils.</p>

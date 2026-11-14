---
title: "pawd(1)"
name: "pawd"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pawd/"
description: "pawd – print automounter working directory"
---

<h2>NAME</h2>
<p> pawd &#8211; print automounter working directory</p>
<h2>SYNOPSIS</h2>
<p> <code>pawd</code> [ <i>path &#8230;</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>pawd</code> is used to print the current working directory, adjusted to reflect proper paths that can be reused to go through the automounter for the shortest possible path. In particular, the path printed back does not include any of <code>Amd</code>&#8216;s local mount points. Using them is unsafe, because <code>Amd</code> may unmount managed file systems from the mount points, and thus including them in paths may not always find the files within. </p>
<p> Without any arguments, <code>pawd</code> will print the automounter adjusted current working directory. With any number of arguments, it will print the adjusted path of each one of the arguments.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pwd/">pwd</a></code>(1). <code><a href="/docs/linux/man/8-amd/">amd</a></code>(8), <code><a href="/docs/linux/man/8-amq/">amq</a></code>(8), </p>
<p> &#8220;am-utils&#8221; <code><a href="/docs/linux/man/1-info/">info</a></code>(1) entry. </p>
<p> <i>Linux NFS and Automounter Administration</i> by Erez Zadok, ISBN 0-7821-2739-8, (Sybex, 2001). </p>
<p> <i><a rel="nofollow" href="http://www.am-utils.org">http://www.am-utils.org</a></i> </p>
<p> <i>Amd &#8211; The 4.4 BSD Automounter</i></p>
<h2>AUTHORS</h2>
<p> Erez Zadok &lt;ezk [at] cs.sunysb.edu&gt;, Computer Science Department, Stony Brook University, Stony Brook, New York, USA. </p>
<p> Other authors and contributors to am-utils are listed in the <code>AUTHORS</code> file distributed with am-utils. </p>
<h2>Index</h2>

---
title: "wire-test(8)"
name: "wire-test"
section: "8"
letter: "w"
url: "/docs/linux/man/8-wire-test/"
description: "wire-test – test your network interfaces and local IP address"
---

<p>wire-test &#8211; test your network interfaces and local IP address</p>
<h2>Synopsis</h2>
<p><code>wire-test</code> [ <i>host</i> ]</p>
<h2>Description</h2>
<p><code>wire-test</code> is used to find out what amd thinks are the first two network interfaces and network names/numbers used, as well as the IP address used for amd to NFS-mount itself. If <i>host</i> is specified, then <code>wire-test</code> will test for the working combinations of NFS protocol and version from the current client to the NFS server <i>host.</i> If not specified, <i>host</i> defaults to &quot;localhost&quot;. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amd/">amd</a></code>(8). </p>
<p> &#8220;am-utils&#8221; <code><a href="/docs/linux/man/1-info/">info</a></code>(1) entry. </p>
<p> <i>Linux NFS and Automounter Administration</i> by Erez Zadok, ISBN 0-7821-2739-8, (Sybex, 2001). </p>
<p> <i><a rel="nofollow" href="http://www.am-utils.org">http://www.am-utils.org</a></i> </p>
<p> <i>Amd &#8211; The 4.4 BSD Automounter</i></p>
<h2>Authors</h2>
<p>Erez Zadok &lt;ezk [at] cs.sunysb.edu&gt;, Computer Science Department, Stony Brook University, Stony Brook, New York, USA. </p>
<p> Other authors and contributors to am-utils are listed in the <code>AUTHORS</code> file distributed with am-utils.</p>

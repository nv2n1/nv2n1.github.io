---
title: "ipmi-detect(8)"
name: "ipmi-detect"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipmi-detect/"
description: "ipmidetect – list detected and/or undetected IPMI interfaces in a cluster"
---

<p>ipmidetect &#8211; list detected and/or undetected IPMI interfaces in a cluster</p>
<h2>Synopsis</h2>
<p><code>ipmidetect</code> [<i>OPTION</i>&#8230;] [<i>NODES</i>&#8230;]</p>
<h2>Description</h2>
<p><code>ipmidetect</code> lists which IPMI nodes have been detected or undetected in a cluster. This information is provided by the <code><a href="/docs/linux/man/3-libipmidetect/">libipmidetect</a>(3)</code> library and <code><a href="/docs/linux/man/8-ipmidetectd/">ipmidetectd</a>(8)</code> daemon. </p>
<p> <code>ipmidetect</code> will output the status of each IPMI node configured with <code><a href="/docs/linux/man/8-ipmidetectd/">ipmidetectd</a>(8)</code> unless they are specified on the command line. If the first node listed is &quot;-&quot;, nodes will be read in from standard input. The nodes can be listed in hostrange format, comma separated lists, or space separated lists. See the section below on HOSTRANGED SUPPORT for instructions on how to list hosts in range format. The hostnames listed must be the shortened names of hostnames.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Print help and exit</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd>Print version and exit</p>
<dt><code>-o</code> <i>STRING</i>, <code>&#8211;hostname</code>=<i>STRING</i></p>
<dd>server hostname (default=localhost)</p>
<dt><code>-p</code> <i>INT</i>, <code>&#8211;port</code>=<i>INT</i></p>
<dd>server port (default=8649)</p>
<dt><code>-d</code>, <code>&#8211;detected</code></p>
<dd>List only detected nodes</p>
<dt><code>-u</code>, <code>&#8211;undetected</code></p>
<dd>List only undetected nodes</p>
<dt><code>-q</code>, <code>&#8211;hostrange</code></p>
<dd>List nodes in hostrange format (default)</p>
<dt><code>-c</code>, <code>&#8211;comma</code></p>
<dd>List nodes in comma separated list</p>
<dt><code>-n</code>, <code>&#8211;newline</code></p>
<dd>List nodes in newline separated list</p>
<dt><code>-s</code>, <code>&#8211;space</code></p>
<dd>List nodes in space separated list</dl>
<h2>Hostranged Support</h2>
<p>Multiple hosts can be input either as an explicit comma separated lists of hosts or a range of hostnames in the general form: prefix[n-m,l-k,&#8230;], where n &lt; m and l &lt; k, etc. The later form should not be confused with regular expression character classes (also denoted by []). For example, foo[19] does not represent foo1 or foo9, but rather represents a degenerate range: foo19. </p>
<p> This range syntax is meant only as a convenience on clusters with a prefixNN naming convention and specification of ranges should not be considered necessary &#8212; the list foo1,foo9 could be specified as such, or by the range foo[1,9]. </p>
<p> Some examples of range usage follow: </p>
<pre> foo[01-05] instead of foo01,foo02,foo03,foo04,foo05
 foo[7,9-10] instead of foo7,foo9,foo10
 foo[0-3] instead of foo0,foo1,foo2,foo3</pre>
<p>As a reminder to the reader, some shells will interpret brackets ([ and ]) for pattern matching. Depending on your shell, it may be necessary to enclose ranged lists within quotes.</p>
<h2>Diagnostics</h2>
<p>The exit value of <code>ipmidetect</code> depends on the options performed on the command line. If the default output is used, the exit value will be 0 if the command succeeds without error. If the &#8211;detected option is used and no undetected nodes have been discovered, the exit value will be 0. If undetected nodes are found, the exit value will be 1. If the &#8211;undetected option is used and no detected nodes have been discovered, the exit value will be 0. If detected nodes are found, the exit value will be 1. On errors, the exit value will be 2.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;freeipmi-users [at] gnu.org&gt; or &lt;freeipmi-devel [at] gnu.org&gt;.</p>
<h2>Copyright</h2>
<p>Copyright (C) 2007-2012 Lawrence Livermore National Security, LLC.<br />
 Copyright (C) 2007 The Regents of the University of California. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-libipmidetect/">libipmidetect</a>(3), <a href="/docs/linux/man/5-ipmidetect-conf/">ipmidetect.conf</a>(5), <a href="/docs/linux/man/8-ipmidetectd/">ipmidetectd</a>(8) <a rel="nofollow" href="http://www.gnu.org/software/freeipmi/">http://www.gnu.org/software/freeipmi/</a> </p>

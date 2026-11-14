---
title: "pq2-redistribute(1)"
name: "pq2-redistribute"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pq2-redistribute/"
description: "pq2-redistribute – Execute the file movements as determined by pq2-ana-dist"
---

<h2 class="name">NAME</h2>
<p> pq2-redistribute &#8211; Execute the file movements as determined by pq2-ana-dist </p>
<h2>SYNOPSIS</h2>
<p> <code>pq2-redistribute</code> [-b backend] -f filemv</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>pq2-redistribute</code> program. </p>
<p> <code>pq2-redistribute</code> is a script executing the file movements as determined by <i><a href="/docs/linux/man/1-pq2-ana-dist/">pq2-ana-dist</a></i>(1) using the specified backend. Currently only the XROOTD backend is supported (tag &#8216;xrd&#8217;; default). </p>
<p> More details about the input file can be found in the man page <i><a href="/docs/linux/man/1-pq2-ana-dist/">pq2-ana-dist</a></i>(1).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display help information.</p>
<dt><code>&#8211;dryrun</code></p>
<dd> Only show the action that should be done (don&#8217;t execute them).</p>
<dt><code>-b</code> &lt;<i>backend</i>&gt;</p>
<dd> Tag identifying the backend to be used. Currently only &#8216;xrd&#8217; (for XROOTD) is supported.</p>
<dt><code>-f</code> &lt;<i>filemv</i>&gt;</p>
<dd> File with the file movement directives produced by pq2-ana-dist .</p>
<dt><code>-r</code> &lt;<i>redirurl</i>&gt;, <code>&#8211;redir</code>=&lt;<i>redirurl</i>&gt;</p>
<dd> URL of the redirector from where the files should be copied and deleted.</p>
<dt><code>-t</code> &lt;<i>dir</i>&gt;, <code>&#8211;tmpdir</code>=&lt;<i>dir</i>&gt;</p>
<dd> Directory for temporary files; default is /tmp/&lt;username&gt;. Thsi is used to store temporary copies of the files during transfers.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> See <i><a href="/docs/linux/man/1-setup-pq2/">setup-pq2</a></i>(1).</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-pq2/">pq2</a></i>(1), <i><a href="/docs/linux/man/1-pq2-ls/">pq2-ls</a></i>(1), <i><a href="/docs/linux/man/1-pq2-ls-files/">pq2-ls-files</a></i>(1), <i><a href="/docs/linux/man/1-pq2-ls-files-server/">pq2-ls-files-server</a></i>(1), <i><a href="/docs/linux/man/1-pq2-info-server/">pq2-info-server</a></i>(1), <i><a href="/docs/linux/man/1-pq2-ana-dist/">pq2-ana-dist</a></i>(1), <i><a href="/docs/linux/man/1-pq2-put/">pq2-put</a></i>(1), <i><a href="/docs/linux/man/1-pq2-verify/">pq2-verify</a></i>(1), <i><a href="/docs/linux/man/1-pq2-rm/">pq2-rm</a></i>(1), <i><a href="/docs/linux/man/1-pq2-cache/">pq2-cache</a></i>(1) </p>
<p> For more information on the <code>ROOT</code> system, please refer to <i><a rel="nofollow" href="http://root.cern.ch">http://root.cern.ch</a></i></p>
<h2>ORIGINAL AUTHORS</h2>
<p> Gerardo Ganis for the ROOT team.</p>
<h2>COPYRIGHT</h2>
<p> This library is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation; either version 2.1 of the License, or (at your option) any later version. </p>
<p> This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details. </p>
<p> You should have received a copy of the GNU Lesser General Public License along with this library; if not, write to the Free Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA</p>
<h2>AUTHOR</h2>
<p> This manual page was originally written by Gerardo Ganis &lt;gerardo.ganis [at] cern.ch&gt;, for ROOT version 5. </p>
<h2>Index</h2>

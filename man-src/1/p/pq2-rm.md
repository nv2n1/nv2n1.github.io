---
title: "pq2-rm(1)"
name: "pq2-rm"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pq2-rm/"
description: "pq2-rm – Remove one or more datasets from a dataset meta-repository based on ROOT files"
---

<h2 class="name">NAME</h2>
<p> pq2-rm &#8211; Remove one or more datasets from a dataset meta-repository based on ROOT files </p>
<h2>SYNOPSIS</h2>
<p> <code>pq2-rm</code> [options] dataset</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>pq2-rm</code> program. </p>
<p> <code>pq2-rm</code> is a script invoking the <code>pq2</code> ROOT application to remove one or more datasets from a dataset meta-repository based on ROOT files; the repository can be accessed via the local file system or a remote file server daemon or a PROOF facility. </p>
<p> More details about the underlying &#8216;pq2&#8217; application can be found in the man page <i><a href="/docs/linux/man/1-pq2/">pq2</a></i>(1).</p>
<h2>ARGUMENTS</h2>
<dl>
<dt><i>dataset</i></p>
<dd> Datasets to be removed; the &#8216;*&#8217; wild card in the items (in such a case the full string, as shown by pq2-ls, should be given, e.g. &#8216;/default/ganis/h1-set5*&#8217;.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display help information.</p>
<dt><code>-k</code>, <code>&#8211;keep</code></p>
<dd> Keep the temporary files created during the analysis under $TMPDIR</p>
<dt><code>-v</code></p>
<dd> Verbose mode</p>
<dt><code>-d</code> &lt;<i>dataset</i>&gt;, <code>&#8211;dataset</code>=&lt;<i>dataset</i>&gt;</p>
<dd> Alternative way to define the datasets to be removed.</p>
<dt><code>-u</code> &lt;<i>serverurl</i>&gt;, <code>&#8211;url</code>=&lt;<i>serverurl</i>&gt;</p>
<dd> URL of the PROOF master or data server providing the information; for data servers, it must include the directory. Can also be specified via the environment variables PQ2PROOFURL or PQ2DSSRVURL (see ENVIRONMENT VARIABLES).&quot;</p>
<dt><code>-t</code> &lt;<i>dir</i>&gt;, <code>&#8211;tmpdir</code>=&lt;<i>dir</i>&gt;</p>
<dd> Directory for temporary files; defualt is /tmp/&lt;username&gt;.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> See <i><a href="/docs/linux/man/1-setup-pq2/">setup-pq2</a></i>(1).</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-pq2/">pq2</a></i>(1), <i><a href="/docs/linux/man/1-setup-pq2/">setup-pq2</a></i>(1), <i><a href="/docs/linux/man/1-pq2-ls/">pq2-ls</a></i>(1), <i><a href="/docs/linux/man/1-pq2-ls-files/">pq2-ls-files</a></i>(1), <i><a href="/docs/linux/man/1-pq2-ls-files-server/">pq2-ls-files-server</a></i>(1), <i><a href="/docs/linux/man/1-pq2-info-server/">pq2-info-server</a></i>(1), <i><a href="/docs/linux/man/1-pq2-ana-dist/">pq2-ana-dist</a></i>(1), <i><a href="/docs/linux/man/1-pq2-put/">pq2-put</a></i>(1), <i><a href="/docs/linux/man/1-pq2-verify/">pq2-verify</a></i>(1), <i><a href="/docs/linux/man/1-pq2-cache/">pq2-cache</a></i>(1) </p>
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

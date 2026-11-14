---
title: "pq2-ana-dist(1)"
name: "pq2-ana-dist"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pq2-ana-dist/"
description: "pq2-ana-dist – Analyse the file distribution of a dataset (or a set of datasets) from a dataset meta-repository based on ROOT files"
---

<h2 class="name">NAME</h2>
<p> pq2-ana-dist &#8211; Analyse the file distribution of a dataset (or a set of datasets) from a dataset meta-repository based on ROOT files </p>
<h2>SYNOPSIS</h2>
<p> <code>pq2-ana-dist</code> [options] datasets</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>pq2-ana-dist</code> program. </p>
<p> <code>pq2-ana-dist</code> is a script invoking the <code>pq2</code> ROOT application to analyse the file distribution of a dataset (or a set of datasets) over the file servers, eiher in terms of files or of file sizes. The output is a text file with the the file movements needed to make the file distribution even in the chosen metrics to be used, for example, as in input to <i><a href="/docs/linux/man/1-pq2-redistribute/">pq2-redistribute</a></i>(1). Optionally the internal objects can be saved so that they can be used as starting point for a subsequent run. An histogram and a plot can also be saved to visualize the file distribution. The repository with the dataset information can be accessed via the local file system or a remote file server daemon or a PROOF facility. </p>
<p> More details about the underlying &#8216;pq2&#8217; application can be found in the man page <i><a href="/docs/linux/man/1-pq2/">pq2</a></i>(1).</p>
<h2>ARGUMENTS</h2>
<dl>
<dt><i>datasets</i></p>
<dd> Comma-separated list of datasets to be analysed; the &#8216;*&#8217; wild card in the items (in such a case the full string &#8211; as shown by pq2-ls &#8211; should be given in quotes, e.g. &#8216;/default/ganis/h1-set5*&#8217;.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display help information.</p>
<dt><code>-k</code>, <code>&#8211;keep</code></p>
<dd> Keep the temporary files created during the analysis under $TMPDIR</p>
<dt><code>-v</code></p>
<dd> Verbose mode</p>
<dt><code>&#8211;dataset</code>=&lt;<i>datasets</i>&gt;</p>
<dd> Alternative way to define the datasets to be analysed.</p>
<dt><code>-s</code> &lt;<i>servers</i>&gt;, <code>&#8211;servers</code>=&lt;<i>servers</i>&gt;</p>
<dd> Comma-separated list of servers to be used (-s) in the analysis; a &#8216;+&#8217; in front of the list adds the specified servers to the existing ones: this can be useful when determining file movements to empty or new servers</p>
<dt><code>-e</code> &lt;<i>excsrvs</i>&gt;, <code>&#8211;exclude</code>=&lt;<i>excsrvs</i>&gt;</p>
<dd> Comma-separated list of servers to be excluded from the target servers; this can be used, for example, to determine the files movements to drain a server.</p>
<dt><code>-i</code> &lt;<i>ignsrvs</i>&gt;, <code>&#8211;ignore</code>=&lt;<i>ignsrvs</i>&gt;</p>
<dd> Comma-separated list of servers to be ignored in the analysis; this can be used, for example, to skip the redirector.</p>
<dt><code>-m</code> &lt;<i>metrics</i>&gt;, <code>&#8211;metrics</code>=&lt;<i>metrics</i>&gt;</p>
<dd> Metrics to be used to calculate the degree of evenness: </p>
<pre>
    F          use the number of files (default)
    S          use the file size
</pre>
<dt><code>-f</code> &lt;<i>filemv</i>&gt;, <code>&#8211;filemv</code>=&lt;<i>filemv</i>&gt;</p>
<dd> Defines the file where to save the result of the analysis; by the default the result is send to the screen. The output contains one line per each file that needs to be moved with the format &#8216;file source destination&#8217; where &#8216;file&#8217; is the file name, &#8216;source&#8217; is the source server URL and &#8216;destination&#8217; is the destination server URL. The file can be used as input, for example, to <i><a href="/docs/linux/man/1-pq2-redistribute/">pq2-redistribute</a></i>(1).</p>
<dt><code>&#8211;plot</code>[=&lt;<i>fileplot.fmt</i>&gt;]</p>
<dd> Defines the file with the output plot with the original distribution with the server names and the +-10% limits; the extension (if known) defines the format; the default format is &#8216;png&#8217; and the default name &#8216;plot.png&#8217;. The plot can also be obtained directly from a binary output file (saved with &#8216;&#8211;fout=&lt;outfile&gt;.root&#8217;) but just specifying &#8216;&#8211;fin=&lt;outfile&gt;.root &#8211;plot&#8217;. The available formats are those known by ROOT: png (default), eps, ps, pdf, svg, gif, xpm, jpg, tiff.</p>
<dt><code>&#8211;fout</code>[=&lt;<i>outfile</i>&gt;]</p>
<dd> Defines the file where to save the output of the analysis in binary form (ROOT file); this output can be used as starting point for a next run, allowing to run over many datasets in separate steps.</p>
<dt><code>&#8211;fin</code>[=&lt;<i>infile</i>&gt;]</p>
<dd> Defines the ROOT file from where to fetch the output of a previous run (saved with &#8211;fout=infile).</p>
<dt><code>-u</code> &lt;<i>serverurl</i>&gt;, <code>&#8211;url</code>=&lt;<i>serverurl</i>&gt;</p>
<dd> URL of the PROOF master or data server providing the information; for data servers, it must include the directory. Can also be specified via the environment variables PQ2PROOFURL or PQ2DSSRVURL (see ENVIRONMENT VARIABLES).&quot;</p>
<dt><code>-t</code> &lt;<i>dir</i>&gt;, <code>&#8211;tmpdir</code>=&lt;<i>dir</i>&gt;</p>
<dd> Directory for temporary files; defualt is /tmp/&lt;username&gt;.</dl>
<h2>FORMAT OF THE FILE WITH MOVE DIRECTIVES</h2>
<p> The out file constist of one line per file to be moved with the following format: </p>
<pre>
file-name       source-server-URL       destination-server-URL
</pre>
<h2>ENVIRONMENT VARIABLES</h2>
<p> See <i><a href="/docs/linux/man/1-setup-pq2/">setup-pq2</a></i>(1).</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-pq2/">pq2</a></i>(1), <i><a href="/docs/linux/man/1-setup-pq2/">setup-pq2</a></i>(1), <i><a href="/docs/linux/man/1-pq2-ls/">pq2-ls</a></i>(1), <i><a href="/docs/linux/man/1-pq2-ls-files/">pq2-ls-files</a></i>(1), <i><a href="/docs/linux/man/1-pq2-ls-files-server/">pq2-ls-files-server</a></i>(1), <i><a href="/docs/linux/man/1-pq2-info-server/">pq2-info-server</a></i>(1), <i><a href="/docs/linux/man/1-pq2-redistribute/">pq2-redistribute</a></i>(1), <i><a href="/docs/linux/man/1-pq2-verify/">pq2-verify</a></i>(1), <i><a href="/docs/linux/man/1-pq2-rm/">pq2-rm</a></i>(1), <i><a href="/docs/linux/man/1-pq2-cache/">pq2-cache</a></i>(1) </p>
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

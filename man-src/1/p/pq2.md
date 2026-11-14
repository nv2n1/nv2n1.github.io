---
title: "pq2(1)"
name: "pq2"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pq2/"
description: "pq2 – The command line interface to a dataset meta-repository based on ROOT files"
---

<h2 class="name">NAME</h2>
<p> pq2 &#8211; The command line interface to a dataset meta-repository based on ROOT files </p>
<h2>SYNOPSIS</h2>
<p> <code>pq2</code> action <i>options</i></p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>pq2</code> program. </p>
<p> <code>pq2</code> is a <code>ROOT</code> application providing an interface to a dataset meta-repository based on ROOT files; the repository can be accessed via the local file system or a remote file server daemon or a PROOF facility. </p>
<p> When working with a local or remote file system, <i>pq2</i> instantiates a <i>TDataSetManagerFile</i> class on the specified local or remote directory. Remote access is done via the <i>TFile</i> interface, so any implementation of <i>TFile</i> supported by the installation can in principle be used. When working with PROOF server the <i>TProof</i> dataset manager interface is used to access the dataset repository attached to the PROOF cluster.</p>
<h2>ACTIONS</h2>
<dl>
<dt>ls</p>
<dd> list compact information about all or a sample dataset.</p>
<dt>ls-files</p>
<dd> list compact information about all the files of a given dataset.</p>
<dt>ls-files-server</p>
<dd> list the file content of a dataset on a given server or list of servers.</p>
<dt>info-server</p>
<dd> display compact information about the datasets on a given server or a set of servers.</p>
<dt>ana-dist</p>
<dd> analyse the file distribution of a dataset (or a set of datasets) over the file servers, either in terms of files or of file sizes. The output is a text file with the the file movements needed to make the file distribution even in the chosen metrics to be used in input to pq2-redistribute. Optionally the internal objects can be saved so that they can be used as starting point for a subsequent run. Also an histogram and a plot can be saved to visualize the file distribution.</p>
<dt>put</p>
<dd> register one or more datasets.</p>
<dt>rm</p>
<dd> remove one or more datasets.</p>
<dt>verify</p>
<dd> scan the content one or more datasets.</p>
<dt>cache</p>
<dd> display or clear the local cache content. </p>
</dl>
<h2>COMMON OPTIONS</h2>
<p> Some of the options listed below have a slight different meaning depending on the action. Please refer to the man pages of the script interfaces to the actions for more details (see below).</p>
<dl>
<dt><code>-d</code> &lt;<i>dataset</i>&gt;</p>
<dd> For all action but <i>put</i>, the dataset to be processed. For listing actions the wildcards &#8216;*&#8217; is supported. For action <i>put</i>, <i>dataset</i> is the path to the file with the list of files in the dataset or directory with the files containing the file lists of the datasets to be registered; in the first case wildcards &#8216;*&#8217; can be specified in the file name, i.e. &#8216;&lt;dir&gt;/fil*&#8217; is ok but &#8216;&lt;dir&gt;/*/file&#8217; is not. In all cases the name of the dataset is the name of the file finally used.</p>
<dt><code>-u</code> &lt;<i>serverurl</i>&gt;</p>
<dd> URL of the PROOF master or data server providing the information; for data servers, it must include the directory. Can also be specified via the environment variables PQ2PROOFURL or PQ2DSSRVURL (see ENVIRONMENT VARIABLES).&quot;</p>
<dt><code>-o</code> &lt;<i>options</i>&gt;</p>
<dd> Specify a string of options to be passed to the instance actuatlly performing the action; the exact meaning is action dependent.</p>
<dt><code>-s</code> &lt;<i>servers</i>&gt;</p>
<dd> Specify a server or a comma-separated list of servers to be used in the analysis when required by the action.</p>
<dt><code>-k</code></p>
<dd> Keep the temporary files created during the analysis under $TMPDIR</p>
<dt><code>-v</code></p>
<dd> Verbose mode</dl>
<h2>OPTIONS for action verify</h2>
<p> The options listed below apply only to action &#8216;verify&#8217;</p>
<dl>
<dt><code>-r</code> &lt;<i>redirector</i>&gt;</p>
<dd> Force re-location of the files via the specified redirector; useful after a file redistribution on the same file server.</dl>
<h2>OPTIONS for action ana-dist</h2>
<p> The options listed below apply only to action &#8216;ana-dist&#8217;</p>
<dl>
<dt><code>-m</code> &lt;<i>metrics</i>&gt;</p>
<dd> Defines the metrics to be used in the distribution analysis. The possibilities supported currently are: &#8216;F&#8217; to use the number of files, and &#8216;S&#8217; to use the file size.</p>
<dt><code>-f</code> &lt;<i>result file</i>&gt;</p>
<dd> Defines the file where to save the result of the analysis; by the default the result is send to the screen. The output contains one line per each file that needs to be moved with the format &#8216;file source destination&#8217; where &#8216;file&#8217; is the file name, &#8216;source&#8217; is the source server URL and &#8216;destination&#8217; is the destination server URL.</p>
<dt><code>&#8211;outfile</code> &lt;<i>output file</i>&gt;</p>
<dd> Defines the file where to save the output of the analysis in binary form (ROOT file); this output can be used as starting point for a next run, allowing to run over many datasets in separate steps.</p>
<dt><code>&#8211;infile</code> &lt;<i>input file</i>&gt;</p>
<dd> Defines the ROOT file from where to fetch the output of a previous run (saved with &#8211;outfile).</p>
<dt><code>-i</code> &lt;<i>ignored servers</i>&gt;</p>
<dd> Specify a server or a comma-separated list of servers to be ignored in the analysis; this allows to exclude, for example, the redirector.</p>
<dt><code>-e</code> &lt;<i>excluded servers</i>&gt;</p>
<dd> Specify a server or a comma-separated list of servers to be excluded from the target servers; this can be used, for example, to determine the files movements to drain a server.</p>
<dt><code>&#8211;plot</code> [&lt;<i>plot file</i>&gt;]</p>
<dd> Defines the file with the output plot with the original distribution with the server names and the +-10% limits; the extension (if known) defines the format; the default format is &#8216;png&#8217; and the default name &#8216;plot.png&#8217;. The plot can also be obtained directly from a binary output file (saved with &#8216;&#8211;outfile &lt;outfile&gt;.root&#8217;) but just specifying &#8216;&#8211;infile &lt;outfile&gt;.root &#8211;plot&#8217; </p>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> See <i><a href="/docs/linux/man/1-setup-pq2/">setup-pq2</a></i>(1).</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-setup-pq2/">setup-pq2</a></i>(1), <i><a href="/docs/linux/man/1-pq2-ls/">pq2-ls</a></i>(1), <i><a href="/docs/linux/man/1-pq2-ls-files/">pq2-ls-files</a></i>(1), <i><a href="/docs/linux/man/1-pq2-ls-files-server/">pq2-ls-files-server</a></i>(1), <i><a href="/docs/linux/man/1-pq2-info-server/">pq2-info-server</a></i>(1), <i><a href="/docs/linux/man/1-pq2-ana-dist/">pq2-ana-dist</a></i>(1), <i><a href="/docs/linux/man/1-pq2-put/">pq2-put</a></i>(1), <i><a href="/docs/linux/man/1-pq2-verify/">pq2-verify</a></i>(1), <i><a href="/docs/linux/man/1-pq2-rm/">pq2-rm</a></i>(1), <i><a href="/docs/linux/man/1-pq2-cache/">pq2-cache</a></i>(1) </p>
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

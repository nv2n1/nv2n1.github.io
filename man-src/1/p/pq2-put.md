---

title: "pq2-put(1)"
name: "pq2-put"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pq2-put/"
description: "pq2-put – Register one or more datasets in a dataset meta-repository based on ROOT files"
---

<p> <code>pq2-put</code> [options] datasetfile</p>
<p> This manual page documents briefly the <code>pq2-put</code> program. </p>
<p> <code>pq2-put</code> is a script invoking the <code>pq2</code> ROOT application to register one or more datasets in a dataset meta-repository based on ROOT files; the repository can be accessed via the local file system or a remote file server daemon or a PROOF facility. </p>
<p> More details about the underlying &#8216;pq2&#8217; application can be found in the man page <i><a href="/docs/linux/man/1-pq2/">pq2</a></i>(1).</p>
<h2>ARGUMENTS</h2>
<dl>
<dt><i>datasetfile</i></dt>
<dd> Path to the file with the list of files in the dataset or directory with the files containing the file lists of the datasets to be registered; in the first case wildcards &#8216;*&#8217; can be specified in the file name, i.e. &#8216;&lt;dir&gt;/fil*&#8217; is ok but &#8216;&lt;dir&gt;/*/file&#8217; is not. In all cases the name of the dataset is the name of the file finally used. The format of the file is described below.</dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Display help information.</dd>
<dt><code>-k</code>, <code>&#8211;keep</code></dt>
<dd> Keep the temporary files created during the analysis under $TMPDIR</dd>
<dt><code>-v</code></dt>
<dd> Verbose mode</dd>
<dt><code>-d</code> &lt;<i>datasetfile</i>&gt;, <code>&#8211;dataset</code> &lt;<i>datasetfile</i>&gt;</dt>
<dd> Alternative way to define path to the file with the list of files.</dd>
<dt><code>-o</code> &lt;<i>options</i>&gt;</dt>
<dd> Options for registering datasets; a combination of: </dd>
<pre>
     O   overwrite existing dataset
     U   add information to existing dataset, if any or create a new one
     T   Trust the information already present in the dataset
     V   verify (scan) information in the dataset (can be very slow)
</pre>
<dt><code>&#8211;overwrite</code></dt>
<dd> Alternative to &#8216;-o O&#8217;.</dd>
<dt><code>&#8211;update</code></dt>
<dd> Alternative to &#8216;-o U&#8217;.</dd>
<dt><code>&#8211;trust</code></dt>
<dd> Alternative to &#8216;-o T&#8217;.</dd>
<dt><code>&#8211;tree=</code>&lt;<i>default-tree-name</i>&gt;</dt>
<dd> Set the name of the default tree name to &#8216;default-tree-name&#8217; (option &#8216;T&#8217; or &#8211;trust only); this allows to skip the tree name specification during Process when more TTree (or derivative) objects are available in the files.</dd>
<dt><code>&#8211;staged</code></dt>
<dd> Assume all files online or staged (option &#8216;T&#8217; or &#8211;trust only).</dd>
<dt><code>-u</code> &lt;<i>serverurl</i>&gt;, <code>&#8211;url</code>=&lt;<i>serverurl</i>&gt;</dt>
<dd> URL of the PROOF master or data server providing the information; for data servers, it must include the directory. Can also be specified via the environment variables PQ2PROOFURL or PQ2DSSRVURL (see ENVIRONMENT VARIABLES).&quot;</dd>
<dt><code>-t</code> &lt;<i>dir</i>&gt;, <code>&#8211;tmpdir</code>=&lt;<i>dir</i>&gt;</dt>
<dd> Directory for temporary files; defualt is /tmp/&lt;username&gt;.</dd></dl>
<h2>FORMAT OF THE FILES</h2>
<p> The name of the file defining the dataset is the name of the dataset. The files must contain one line per each file in the dataset with the full file URL. If available, additional information can be specified on the same line with the following keywords: </p>
<pre><code>
sz : &lt;size&gt; size of the file in bytes
         md5 : &lt;md5_ascii&gt;
                   MD5 sum of the file in ASCII form
                       uuid : &lt;uuid&gt;
                                  UUID of the file
                                      tree : &lt;name&gt;,
                                             &lt;entries&gt;,
                                             &lt;first&gt;,
                                             &lt;last&gt; meta - information about a tree in the file;
the should be in the form&lt;subdir&gt; / tree - name;
'entries' is the number of entries in the tree;
'first' and 'last' define the entry range.obj : &lt;name&gt;, &lt;class&gt;, &lt;entries&gt; meta - information about a generic object in the file;
the should be in
            the form&lt;subdir&gt; /
        obj -
    name;
'class' is the object class; 'entries' is
                                        the number of occurences for this object.
</code></pre>
<p> Multiple occurences of &#8216;tree:&#8217; or &#8216;obj:&#8217; can be specified.</p>
<h2>EXAMPLES</h2>
<p> The following examples show how to register information corresponding to the H1 example of the ROOT tutorials.</p>
<dl>
<dt><code>Minimal information</code></dt>
<dd> In this example the files are read from the ROOT HTTP server. Detailed information about the content of the files is not available, so only the URLs are given. If the file is called h1-http, we get </dd>
<pre>
   $ cat h1-http
   <a rel="nofollow" href="http://root.cern.ch/files/h1/dstarmb.root">http://root.cern.ch/files/h1/dstarmb.root</a>
   <a rel="nofollow" href="http://root.cern.ch/files/h1/dstarp1a.root">http://root.cern.ch/files/h1/dstarp1a.root</a>
   <a rel="nofollow" href="http://root.cern.ch/files/h1/dstarp1b.root">http://root.cern.ch/files/h1/dstarp1b.root</a>
   <a rel="nofollow" href="http://root.cern.ch/files/h1/dstarp2.root">http://root.cern.ch/files/h1/dstarp2.root</a>
</pre>
<p> The dataset is registered and verification required: </p>
<pre>
   $ pq2-put -o &quot;V&quot; h1-http
   pq2-put: 1 dataset(s) registered
</pre>
<dt><code>Full information</code></dt>
<dd> In this example the files are read from the local /data/h1 directory. Detailed information about the content of the files is available. If the file is called h1-local, we get </dd>
<pre>
   $ cat h1-local
   file:/data/h1/dstarmb.root  sz:21330730 md5:0a60055370e16d954f90fb50c2d1a801 tree:h42,21920,0,-1
   file:/data/h1/dstarp1a.root md5:e2f959b15235214be3c973c3e7a9ff2c sz:71464503 tree:h42,73243
   file:/data/h1/dstarp1b.root md5:169ea4799661696a25e73257fe8a833d sz:83827959 tree:h42,85597
   file:/data/h1/dstarp2.root md5:907d10b401a35c0240cfa76bedc31420 sz:100675234 tree:h42,103053
</pre>
<p> The dataset is registered trusting the passed information: </p>
<pre>
   $ pq2-put -o T --tree=h42 --staged h1-local
   pq2-put: 1 dataset(s) registered
</pre>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> See <i>setup-pq2</i>(1).</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-pq2/">pq2</a></i>(1), <i>setup-pq2</i>(1), <i><a href="/docs/linux/man/1-pq2-ls/">pq2-ls</a></i>(1), <i><a href="/docs/linux/man/1-pq2-ls-files/">pq2-ls-files</a></i>(1), <i><a href="/docs/linux/man/1-pq2-ls-files-server/">pq2-ls-files-server</a></i>(1), <i><a href="/docs/linux/man/1-pq2-info-server/">pq2-info-server</a></i>(1), <i><a href="/docs/linux/man/1-pq2-ana-dist/">pq2-ana-dist</a></i>(1), <i><a href="/docs/linux/man/1-pq2-verify/">pq2-verify</a></i>(1), <i><a href="/docs/linux/man/1-pq2-rm/">pq2-rm</a></i>(1), <i><a href="/docs/linux/man/1-pq2-cache/">pq2-cache</a></i>(1) </p>
<p> For more information on the <code>ROOT</code> system, please refer to <i><a rel="nofollow" href="http://root.cern.ch">http://root.cern.ch</a></i></p>
<h2>ORIGINAL AUTHORS</h2>
<p> Gerardo Ganis for the ROOT team.</p>
<h2>COPYRIGHT</h2>
<p> This library is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation; either version 2.1 of the License, or (at your option) any later version. </p>
<p> This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details. </p>
<p> You should have received a copy of the GNU Lesser General Public License along with this library; if not, write to the Free Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA</p>
<h2>AUTHOR</h2>
<p> This manual page was originally written by Gerardo Ganis &lt;gerardo.ganis [at] cern.ch&gt;, for ROOT version 5. </p>

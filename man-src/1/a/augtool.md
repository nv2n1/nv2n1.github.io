---

title: "augtool(1)"
name: "augtool"
section: "1"
letter: "a"
url: "/docs/linux/man/1-augtool/"
description: "augtool – inspect and modify configuration files"
---

<p> augtool &#8211; inspect and modify configuration files </p>
<h2>SYNOPSIS</h2>
<p> augtool [OPTIONS] [COMMAND]</p>
<h2>DESCRIPTION</h2>
<p> Augeas is a configuration editing tool. It parses configuration files in their native formats and transforms them into a tree. Configuration changes are made by manipulating this tree and saving it back into native config files. </p>
<p> augtool provides a command line interface to the generated tree. COMMAND can be a single command as described under &#8220;COMMANDS&#8221;. When called with no COMMAND, it reads commands from standard input until an end-of-file is encountered.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code>, <code>&#8211;typecheck</code></dt>
<dd> Typecheck lenses. This can be very slow, and is therefore not done by default, but is highly recommended during development.</dd>
<dt><code>-b</code>, <code>&#8211;backup</code></dt>
<dd> When files are changed, preserve the originals in a file with extension &#8216;.augsave&#8217;</dd>
<dt><code>-n</code>, <code>&#8211;new</code></dt>
<dd> Save changes in files with extension &#8216;.augnew&#8217;, do not modify the original files</dd>
<dt><code>-r</code>, <code>&#8211;root</code>=<i></i><i>ROOT</i><i></i></dt>
<dd> Use directory ROOT as the root of the filesystem. Takes precedence over a root set with the AUGEAS_ROOT environment variable.</dd>
<dt><code>-I</code>, <code>&#8211;include</code>=<i></i><i>DIR</i><i></i></dt>
<dd> Add DIR to the module loadpath. Can be given multiple times. The directories set here are searched before any directories specified in the AUGEAS_LENS_LIB environment variable, and before the default directories <i>/usr/share/augeas/lenses</i> and <i>/usr/share/augeas/lenses/dist</i>.</dd>
<dt><code>-t</code>, <code>&#8211;transform</code>=<i></i><i>XFM</i><i></i></dt>
<dd> Add a file transform; uses the &#8216;transform&#8217; command syntax, e.g. <tt>&quot;-t 'Fstab incl /etc/fstab.bak'&quot;</tt>.</dd>
<dt><code>-f</code>, <code>&#8211;file</code>=<i></i><i>FILE</i><i></i></dt>
<dd> Read commands from FILE.</dd>
<dt><code>-i</code>, <code>&#8211;interactive</code></dt>
<dd> Read commands from the terminal. When combined with <code>-f</code> or redirection of stdin, drop into an interactive session after executing the commands from the file.</dd>
<dt><code>-e</code>, <code>&#8211;echo</code></dt>
<dd> When reading commands from a file via stdin, echo the commands before printing their output.</dd>
<dt><code>-s</code>, <code>&#8211;autosave</code></dt>
<dd> Automatically save all changes at the end of the session.</dd>
<dt><code>-S</code>, <code>&#8211;nostdinc</code></dt>
<dd> Do not search any of the default directories for modules. When this option is set, only directories specified explicitly with <code>-I</code> or specified in <code>AUGEAS_LENS_LIB</code> will be searched for modules.</dd>
<dt><code>-L</code>, <code>&#8211;noload</code></dt>
<dd> Do not load any files on startup. This is generally used to fine-tune which files to load by modifying the entries in <tt>&quot;/augeas/load&quot;</tt> and then issuing a <tt>&quot;load&quot;</tt> command.</dd>
<dt><code>-A</code>, <code>&#8211;noautoload</code></dt>
<dd> Do not load any lens modules, and therefore no files, on startup. This creates no entries under <tt>&quot;/augeas/load&quot;</tt> whatsoever; to read any files, they need to be set up manually and loading must be initiated with a <tt>&quot;load&quot;</tt> command. Using this option gives the fastest startup.</dd>
<dt><code>&#8211;span</code></dt>
<dd> Load span positions for nodes in the tree, as they relate to the original file. Enables the use of the <code>span</code> command to retrieve position data.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Print version information and exit. The version is also in the tree under <tt>&quot;/augeas/version&quot;</tt>.</dd></dl>
<h2>COMMANDS</h2>
<p> In interactive mode, commands and paths can be completed by pressing <tt>&quot;TAB&quot;</tt>. </p>
<p> The paths accepted as arguments by commands use a small subset of XPath path expressions. A path expression consists of a number of segments, separated by <tt>&quot;/&quot;</tt>. In each segment, the character <tt>&quot;*&quot;</tt> can be used to match every node regardless of its label. Sibling nodes with identical labels can be distinguished by appending <tt>&quot;[N]&quot;</tt> to their label to match the N-th sibling with such a label. The last sibling with a specific label can be reached as <tt>&quot;[last()]&quot;</tt>. See &#8220;EXAMPLES&#8221; for some examples of this.</p>
<h3>ADMIN COMMANDS</h3>
<p> The following commands control the behavior of Augeas and augtool itself.</p>
<dl>
<dt><code>help</code></dt>
<dd> Print this help text</dd>
<dt><code>load</code></dt>
<dd> Load files according to the transforms in <tt>&quot;/augeas/load&quot;</tt>.</dd>
<dt><code>quit</code></dt>
<dd> Exit the program</dd>
<dt><code>retrieve</code> &lt;LENS&gt; &lt;NODE_IN&gt; &lt;PATH&gt; &lt;NODE_OUT&gt;</dt>
<dd> Transform tree at PATH back into text using lens LENS and store the resulting string at NODE_OUT. Assume that the tree was initially read in with the same lens and the string stored at NODE_IN as input.</dd>
<dt><code>save</code></dt>
<dd> Save all pending changes to disk. Unless either the <code>-b</code> or <code>-n</code> command line options are given, files are changed in place.</dd>
<dt><code>store</code> &lt;LENS&gt; &lt;NODE&gt; &lt;PATH&gt;</dt>
<dd> Parse NODE using LENS and store the resulting tree at PATH.</dd>
<dt><code>transform</code> &lt;LENS&gt; &lt;FILTER&gt; &lt;FILE&gt;</dt>
<dd> Add a transform for FILE using LENS. The LENS may be a module name or a full lens name. If a module name is given, then &#8220;lns&#8221; will be the lens assumed. The FILTER must be either &#8220;incl&#8221; or &#8220;excl&#8221;. If the filter is &#8220;incl&#8221;, the FILE will be parsed by the LENS.  If the filter is &#8220;excl&#8221;, the FILE will be excluded from the LENS. FILE may contain wildcards.</dd></dl>
<h3>READ COMMANDS</h3>
<p> The following commands are used to retrieve data from the Augeas tree.</p>
<dl>
<dt><code>dump-xml</code> <i>[&lt;</i><i>PATH</i><i>&gt;]</i></dt>
<dd> Print entries in the tree as XML. If PATH is given, printing starts there, otherwise the whole tree is printed.</dd>
<dt><code>get</code> &lt;PATH&gt;</dt>
<dd> Print the value associated with PATH</dd>
<dt><code>label</code> &lt;PATH&gt;</dt>
<dd> Get and print the label associated with PATH</dd>
<dt><code>ls</code> &lt;PATH&gt;</dt>
<dd> List the direct children of PATH</dd>
<dt><code>match</code> &lt;PATTERN&gt; [&lt;VALUE&gt;]</dt>
<dd> Find all paths that match PATTERN. If VALUE is given, only the matching paths whose value equals VALUE are printed</dd>
<dt><code>print</code> <i>[&lt;</i><i>PATH</i><i>&gt;]</i></dt>
<dd> Print entries in the tree. If PATH is given, printing starts there, otherwise the whole tree is printed</dd>
<dt><code>span</code> &lt;PATH&gt;</dt>
<dd> Print the name of the file from which the node PATH was generated, as well as information about the positions in the file corresponding to the label, the value, and the entire node. PATH must match exactly one node. </dd>
<p> You need to run &#8216;set /augeas/span enable&#8217; prior to loading files to enable recording of span information. It is disabled by default.</dl>
<h3>WRITE COMMANDS</h3>
<p> The following commands are used to modify the Augeas tree.</p>
<dl>
<dt><code>clear</code> &lt;PATH&gt;</dt>
<dd> Set the value for PATH to NULL. If PATH is not in the tree yet, it and all its ancestors will be created.</dd>
<dt><code>clearm</code> &lt;BASE&gt; &lt;SUB&gt;</dt>
<dd> Clear multiple nodes values in one operation. Find or create a node matching SUB by interpreting SUB as a path expression relative to each node matching BASE. If SUB is &#8216;.&#8217;, the nodes matching BASE will be modified.</dd>
<dt><code>ins</code> <i>&lt;</i><i>LABEL</i><i>&gt;</i> <i>&lt;</i><i>WHERE</i><i>&gt;</i> <i>&lt;</i><i>PATH</i><i>&gt;</i></dt>
<dd> Insert a new node with label LABEL right before or after PATH into the tree. WHERE must be either &#8216;before&#8217; or &#8216;after&#8217;.</dd>
<dt><code>insert</code> <i>&lt;</i><i>LABEL</i><i>&gt;</i> <i>&lt;</i><i>WHERE</i><i>&gt;</i> <i>&lt;</i><i>PATH</i><i>&gt;</i></dt>
<dd> Alias of <code>ins</code>.</dd>
<dt><code>mv</code> &lt;SRC&gt; &lt;DST&gt;</dt>
<dd> Move node SRC to DST. SRC must match exactly one node in the tree. DST must either match exactly one node in the tree, or may not exist yet. If DST exists already, it and all its descendants are deleted. If DST does not exist yet, it and all its missing ancestors are created.</dd>
<dt><code>move</code> &lt;SRC&gt; &lt;DST&gt;</dt>
<dd> Alias of <code>mv</code>.</dd>
<dt><code>cp</code> &lt;SRC&gt; &lt;DST&gt;</dt>
<dd> Copy node SRC to DST. SRC must match exactly one node in the tree. DST must either match exactly one node in the tree, or may not exist yet. If DST exists already, it and all its descendants are deleted. If DST does not exist yet, it and all its missing ancestors are created.</dd>
<dt><code>copy</code> &lt;SRC&gt; &lt;DST&gt;</dt>
<dd> Alias of <code>cp</code>.</dd>
<dt><code>rename</code> &lt;SRC&gt; &lt;LBL&gt;</dt>
<dd> Rename the label of all nodes matching SRC to LBL.</dd>
<dt><code>rm</code> &lt;PATH&gt;</dt>
<dd> Delete PATH and all its children from the tree</dd>
<dt><code>set</code> &lt;PATH&gt; &lt;VALUE&gt;</dt>
<dd> Associate VALUE with PATH. If PATH is not in the tree yet, it and all its ancestors will be created.</dd>
<dt><code>setm</code> &lt;BASE&gt; &lt;SUB&gt; [&lt;VALUE&gt;]</dt>
<dd> Set multiple nodes in one operation. Find or create a node matching SUB by interpreting SUB as a path expression relative to each node matching BASE. If SUB is &#8216;.&#8217;, the nodes matching BASE will be modified.</dd>
<dt><code>touch</code> &lt;PATH&gt;</dt>
<dd> Create PATH with the value NULL if it is not in the tree yet. All its ancestors will also be created. These new tree entries will appear last amongst their siblings.</dd></dl>
<h3>PATH EXPRESSION COMMANDS</h3>
<p> The following commands help when working with path expressions.</p>
<dl>
<dt><code>defnode</code> &lt;NAME&gt; &lt;EXPR&gt; [&lt;VALUE&gt;]</dt>
<dd> Define the variable NAME to the result of evaluating EXPR, which must be a nodeset. If no node matching EXPR exists yet, one is created and NAME will refer to it. If VALUE is given, this is the same as &#8216;set EXPR VALUE&#8216;; if VALUE is not given, the node is created as if with &#8216;clear EXPR&#8216; would and NAME refers to that node.</dd>
<dt><code>defvar</code> &lt;NAME&gt; &lt;EXPR&gt;</dt>
<dd> Define the variable NAME to the result of evaluating EXPR. The variable can be used in path expressions as <tt>$NAME</tt>. Note that EXPR is evaluated when the variable is defined, not when it is used.</dd></dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>AUGEAS_ROOT</code></dt>
<dd> The file system root, defaults to &#8216;/&#8217;. Can be overridden with the <code>-r</code> command line option</dd>
<dt><code>AUGEAS_LENS_LIB</code></dt>
<dd> Colon separated list of directories with lenses. Directories specified here are searched after any directories set with the <code>-I</code> command line option, but before the default directories <i>/usr/share/augeas/lenses</i> and <i>/usr/share/augeas/lenses/dist</i></dd></dl>
<h2>DIAGNOSTICS</h2>
<p> Normally, exit status is 0. If one or more commands fail, the exit status is set to a non-zero value. </p>
<p> Note though that failure to load some of the files specified by transforms in <tt>&quot;/augeas/load&quot;</tt> is not considered a failure. If it is important to know that all files were loaded, you need to issue a <tt>&quot;match /augeas//error&quot;</tt> after loading to find out details about what files could not be loaded and why.</p>
<h2>EXAMPLES</h2>
<pre><code>
#command line mode
augtool print / files / etc / hosts /
#interactive mode
        augtool
            augtool &gt;
    help
        augtool &gt; print / files / etc / hosts /
#Print the third entry from the second AcceptEnv line
                      augtool print '/files/etc/ssh/sshd_config/AcceptEnv[2]/3'
#Find the entry in inittab with action 'initdefault'
                      augtool &gt;
    match / files / etc / inittab /*/action initdefault
 # Print the last alias for each entry in /etc/hosts
 augtool&gt; print /files/etc/hosts/*/
                              alias[last()]
</code></pre>
<h2>FILES</h2>
<p> Lenses and schema definitions in <i>/usr/share/augeas/lenses</i> and <i>/usr/share/augeas/lenses/dist</i></p>
<h2>AUTHOR</h2>
<pre>
  David Lutterkort &lt;dlutter [at] redhat.com&gt;
</pre>
<h2>COPYRIGHT AND LICENSE</h2>
<p> Copyright 2007-2012 Red Hat Inc. </p>
<p> Augeas (and augtool) are distributed under the GNU Lesser General Public License (LGPL)</p>
<h2>SEE ALSO</h2>
<p> <code>Augeas</code> project homepage &lt;<a rel="nofollow" href="http://www.augeas.net/">http://www.augeas.net/</a>&gt; </p>
<p> augparse </p>

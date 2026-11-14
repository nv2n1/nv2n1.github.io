---
title: "augtool(1)"
name: "augtool"
section: "1"
letter: "a"
url: "/docs/linux/man/1-augtool/"
description: "augtool – inspect and modify configuration files"
---

<h2 class="name">NAME</h2>
<p> augtool &#8211; inspect and modify configuration files </p>
<h2>SYNOPSIS</h2>
<p> augtool [<font SIZE="-1">OPTIONS</font>] [<font SIZE="-1">COMMAND</font>]</p>
<h2>DESCRIPTION</h2>
<p> Augeas is a configuration editing tool. It parses configuration files in their native formats and transforms them into a tree. Configuration changes are made by manipulating this tree and saving it back into native config files. </p>
<p> augtool provides a command line interface to the generated tree. <font SIZE="-1">COMMAND</font> can be a single command as described under &#8220;<font SIZE="-1">COMMANDS&#8221;</font>. When called with no <font SIZE="-1">COMMAND,</font> it reads commands from standard input until an end-of-file is encountered.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code>, <code>&#8211;typecheck</code></p>
<dd> Typecheck lenses. This can be very slow, and is therefore not done by default, but is highly recommended during development.</p>
<dt><code>-b</code>, <code>&#8211;backup</code></p>
<dd> When files are changed, preserve the originals in a file with extension &#8216;.augsave&#8217;</p>
<dt><code>-n</code>, <code>&#8211;new</code></p>
<dd> Save changes in files with extension &#8216;.augnew&#8217;, do not modify the original files</p>
<dt><code>-r</code>, <code>&#8211;root</code>=<i></i><font SIZE="-1"><i>ROOT</i></font><i></i></p>
<dd> Use directory <font SIZE="-1">ROOT</font> as the root of the filesystem. Takes precedence over a root set with the <font SIZE="-1">AUGEAS_ROOT</font> environment variable.</p>
<dt><code>-I</code>, <code>&#8211;include</code>=<i></i><font SIZE="-1"><i>DIR</i></font><i></i></p>
<dd> Add <font SIZE="-1">DIR</font> to the module loadpath. Can be given multiple times. The directories set here are searched before any directories specified in the <font SIZE="-1">AUGEAS_LENS_LIB</font> environment variable, and before the default directories <i>/usr/share/augeas/lenses</i> and <i>/usr/share/augeas/lenses/dist</i>.</p>
<dt><code>-t</code>, <code>&#8211;transform</code>=<i></i><font SIZE="-1"><i>XFM</i></font><i></i></p>
<dd> Add a file transform; uses the &#8216;transform&#8217; command syntax, e.g. <tt>&quot;-t 'Fstab incl /etc/fstab.bak'&quot;</tt>.</p>
<dt><code>-f</code>, <code>&#8211;file</code>=<i></i><font SIZE="-1"><i>FILE</i></font><i></i></p>
<dd> Read commands from <font SIZE="-1">FILE.</font></p>
<dt><code>-i</code>, <code>&#8211;interactive</code></p>
<dd> Read commands from the terminal. When combined with <code>-f</code> or redirection of stdin, drop into an interactive session after executing the commands from the file.</p>
<dt><code>-e</code>, <code>&#8211;echo</code></p>
<dd> When reading commands from a file via stdin, echo the commands before printing their output.</p>
<dt><code>-s</code>, <code>&#8211;autosave</code></p>
<dd> Automatically save all changes at the end of the session.</p>
<dt><code>-S</code>, <code>&#8211;nostdinc</code></p>
<dd> Do not search any of the default directories for modules. When this option is set, only directories specified explicitly with <code>-I</code> or specified in <font SIZE="-1"><code>AUGEAS_LENS_LIB</code></font> will be searched for modules.</p>
<dt><code>-L</code>, <code>&#8211;noload</code></p>
<dd> Do not load any files on startup. This is generally used to fine-tune which files to load by modifying the entries in <tt>&quot;/augeas/load&quot;</tt> and then issuing a <tt>&quot;load&quot;</tt> command.</p>
<dt><code>-A</code>, <code>&#8211;noautoload</code></p>
<dd> Do not load any lens modules, and therefore no files, on startup. This creates no entries under <tt>&quot;/augeas/load&quot;</tt> whatsoever; to read any files, they need to be set up manually and loading must be initiated with a <tt>&quot;load&quot;</tt> command. Using this option gives the fastest startup.</p>
<dt><code>&#8211;span</code></p>
<dd> Load span positions for nodes in the tree, as they relate to the original file. Enables the use of the <code>span</code> command to retrieve position data.</p>
<dt><code>&#8211;version</code></p>
<dd> Print version information and exit. The version is also in the tree under <tt>&quot;/augeas/version&quot;</tt>.</dl>
<h2>COMMANDS</h2>
<p> In interactive mode, commands and paths can be completed by pressing <tt>&quot;TAB&quot;</tt>. </p>
<p> The paths accepted as arguments by commands use a small subset of XPath path expressions. A path expression consists of a number of segments, separated by <tt>&quot;/&quot;</tt>. In each segment, the character <tt>&quot;*&quot;</tt> can be used to match every node regardless of its label. Sibling nodes with identical labels can be distinguished by appending <tt>&quot;[N]&quot;</tt> to their label to match the N-th sibling with such a label. The last sibling with a specific label can be reached as <tt>&quot;[last()]&quot;</tt>. See &#8220;<font SIZE="-1">EXAMPLES&#8221;</font> for some examples of this.</p>
<h3><font SIZE="-1">ADMIN COMMANDS</font></h3>
<p> The following commands control the behavior of Augeas and augtool itself.</p>
<dl>
<dt><code>help</code></p>
<dd> Print this help text</p>
<dt><code>load</code></p>
<dd> Load files according to the transforms in <tt>&quot;/augeas/load&quot;</tt>.</p>
<dt><code>quit</code></p>
<dd> Exit the program</p>
<dt><code>retrieve</code> &lt;<font SIZE="-1">LENS</font>&gt; &lt;<font SIZE="-1">NODE_IN</font>&gt; &lt;<font SIZE="-1">PATH</font>&gt; &lt;<font SIZE="-1">NODE_OUT</font>&gt;</p>
<dd> Transform tree at <font SIZE="-1">PATH</font> back into text using lens <font SIZE="-1">LENS</font> and store the resulting string at <font SIZE="-1">NODE_OUT.</font> Assume that the tree was initially read in with the same lens and the string stored at <font SIZE="-1">NODE_IN</font> as input.</p>
<dt><code>save</code></p>
<dd> Save all pending changes to disk. Unless either the <code>-b</code> or <code>-n</code> command line options are given, files are changed in place.</p>
<dt><code>store</code> &lt;<font SIZE="-1">LENS</font>&gt; &lt;<font SIZE="-1">NODE</font>&gt; &lt;<font SIZE="-1">PATH</font>&gt;</p>
<dd> Parse <font SIZE="-1">NODE</font> using <font SIZE="-1">LENS</font> and store the resulting tree at <font SIZE="-1">PATH.</font></p>
<dt><code>transform</code> &lt;<font SIZE="-1">LENS</font>&gt; &lt;<font SIZE="-1">FILTER</font>&gt; &lt;<font SIZE="-1">FILE</font>&gt;</p>
<dd> Add a transform for <font SIZE="-1">FILE</font> using <font SIZE="-1">LENS.</font> The <font SIZE="-1">LENS</font> may be a module name or a full lens name. If a module name is given, then &#8220;lns&#8221; will be the lens assumed. The <font SIZE="-1">FILTER</font> must be either &#8220;incl&#8221; or &#8220;excl&#8221;. If the filter is &#8220;incl&#8221;, the <font SIZE="-1">FILE</font> will be parsed by the <font SIZE="-1">LENS. </font> If the filter is &#8220;excl&#8221;, the <font SIZE="-1">FILE</font> will be excluded from the <font SIZE="-1">LENS. FILE</font> may contain wildcards.</dl>
<h3><font SIZE="-1">READ COMMANDS</font></h3>
<p> The following commands are used to retrieve data from the Augeas tree.</p>
<dl>
<dt><code>dump-xml</code> <i>[&lt;</i><font SIZE="-1"><i>PATH</i></font><i>&gt;]</i></p>
<dd> Print entries in the tree as <font SIZE="-1">XML.</font> If <font SIZE="-1">PATH</font> is given, printing starts there, otherwise the whole tree is printed.</p>
<dt><code>get</code> &lt;<font SIZE="-1">PATH</font>&gt;</p>
<dd> Print the value associated with <font SIZE="-1">PATH</font></p>
<dt><code>label</code> &lt;<font SIZE="-1">PATH</font>&gt;</p>
<dd> Get and print the label associated with <font SIZE="-1">PATH</font></p>
<dt><code>ls</code> &lt;<font SIZE="-1">PATH</font>&gt;</p>
<dd> List the direct children of <font SIZE="-1">PATH</font></p>
<dt><code>match</code> &lt;<font SIZE="-1">PATTERN</font>&gt; [&lt;<font SIZE="-1">VALUE</font>&gt;]</p>
<dd> Find all paths that match <font SIZE="-1">PATTERN.</font> If <font SIZE="-1">VALUE</font> is given, only the matching paths whose value equals <font SIZE="-1">VALUE</font> are printed</p>
<dt><code>print</code> <i>[&lt;</i><font SIZE="-1"><i>PATH</i></font><i>&gt;]</i></p>
<dd> Print entries in the tree. If <font SIZE="-1">PATH</font> is given, printing starts there, otherwise the whole tree is printed</p>
<dt><code>span</code> &lt;<font SIZE="-1">PATH</font>&gt;</p>
<dd> Print the name of the file from which the node <font SIZE="-1">PATH</font> was generated, as well as information about the positions in the file corresponding to the label, the value, and the entire node. <font SIZE="-1">PATH</font> must match exactly one node. </p>
<p> You need to run &#8216;set /augeas/span enable&#8217; prior to loading files to enable recording of span information. It is disabled by default.</dl>
<h3><font SIZE="-1">WRITE COMMANDS</font></h3>
<p> The following commands are used to modify the Augeas tree.</p>
<dl>
<dt><code>clear</code> &lt;<font SIZE="-1">PATH</font>&gt;</p>
<dd> Set the value for <font SIZE="-1">PATH</font> to <font SIZE="-1">NULL.</font> If <font SIZE="-1">PATH</font> is not in the tree yet, it and all its ancestors will be created.</p>
<dt><code>clearm</code> &lt;<font SIZE="-1">BASE</font>&gt; &lt;<font SIZE="-1">SUB</font>&gt;</p>
<dd> Clear multiple nodes values in one operation. Find or create a node matching <font SIZE="-1">SUB</font> by interpreting <font SIZE="-1">SUB</font> as a path expression relative to each node matching <font SIZE="-1">BASE.</font> If <font SIZE="-1">SUB</font> is &#8216;.&#8217;, the nodes matching <font SIZE="-1">BASE</font> will be modified.</p>
<dt><code>ins</code> <i>&lt;</i><font SIZE="-1"><i>LABEL</i></font><i>&gt;</i> <i>&lt;</i><font SIZE="-1"><i>WHERE</i></font><i>&gt;</i> <i>&lt;</i><font SIZE="-1"><i>PATH</i></font><i>&gt;</i></p>
<dd> Insert a new node with label <font SIZE="-1">LABEL</font> right before or after <font SIZE="-1">PATH</font> into the tree. <font SIZE="-1">WHERE</font> must be either &#8216;before&#8217; or &#8216;after&#8217;.</p>
<dt><code>insert</code> <i>&lt;</i><font SIZE="-1"><i>LABEL</i></font><i>&gt;</i> <i>&lt;</i><font SIZE="-1"><i>WHERE</i></font><i>&gt;</i> <i>&lt;</i><font SIZE="-1"><i>PATH</i></font><i>&gt;</i></p>
<dd> Alias of <code>ins</code>.</p>
<dt><code>mv</code> &lt;<font SIZE="-1">SRC</font>&gt; &lt;<font SIZE="-1">DST</font>&gt;</p>
<dd> Move node <font SIZE="-1">SRC</font> to <font SIZE="-1">DST. SRC</font> must match exactly one node in the tree. <font SIZE="-1">DST</font> must either match exactly one node in the tree, or may not exist yet. If <font SIZE="-1">DST</font> exists already, it and all its descendants are deleted. If <font SIZE="-1">DST</font> does not exist yet, it and all its missing ancestors are created.</p>
<dt><code>move</code> &lt;<font SIZE="-1">SRC</font>&gt; &lt;<font SIZE="-1">DST</font>&gt;</p>
<dd> Alias of <code>mv</code>.</p>
<dt><code>cp</code> &lt;<font SIZE="-1">SRC</font>&gt; &lt;<font SIZE="-1">DST</font>&gt;</p>
<dd> Copy node <font SIZE="-1">SRC</font> to <font SIZE="-1">DST. SRC</font> must match exactly one node in the tree. <font SIZE="-1">DST</font> must either match exactly one node in the tree, or may not exist yet. If <font SIZE="-1">DST</font> exists already, it and all its descendants are deleted. If <font SIZE="-1">DST</font> does not exist yet, it and all its missing ancestors are created.</p>
<dt><code>copy</code> &lt;<font SIZE="-1">SRC</font>&gt; &lt;<font SIZE="-1">DST</font>&gt;</p>
<dd> Alias of <code>cp</code>.</p>
<dt><code>rename</code> &lt;<font SIZE="-1">SRC</font>&gt; &lt;<font SIZE="-1">LBL</font>&gt;</p>
<dd> Rename the label of all nodes matching <font SIZE="-1">SRC</font> to <font SIZE="-1">LBL.</font></p>
<dt><code>rm</code> &lt;<font SIZE="-1">PATH</font>&gt;</p>
<dd> Delete <font SIZE="-1">PATH</font> and all its children from the tree</p>
<dt><code>set</code> &lt;<font SIZE="-1">PATH</font>&gt; &lt;<font SIZE="-1">VALUE</font>&gt;</p>
<dd> Associate <font SIZE="-1">VALUE</font> with <font SIZE="-1">PATH.</font> If <font SIZE="-1">PATH</font> is not in the tree yet, it and all its ancestors will be created.</p>
<dt><code>setm</code> &lt;<font SIZE="-1">BASE</font>&gt; &lt;<font SIZE="-1">SUB</font>&gt; [&lt;<font SIZE="-1">VALUE</font>&gt;]</p>
<dd> Set multiple nodes in one operation. Find or create a node matching <font SIZE="-1">SUB</font> by interpreting <font SIZE="-1">SUB</font> as a path expression relative to each node matching <font SIZE="-1">BASE.</font> If <font SIZE="-1">SUB</font> is &#8216;.&#8217;, the nodes matching <font SIZE="-1">BASE</font> will be modified.</p>
<dt><code>touch</code> &lt;<font SIZE="-1">PATH</font>&gt;</p>
<dd> Create <font SIZE="-1">PATH</font> with the value <font SIZE="-1">NULL</font> if it is not in the tree yet. All its ancestors will also be created. These new tree entries will appear last amongst their siblings.</dl>
<h3><font SIZE="-1">PATH EXPRESSION COMMANDS</font></h3>
<p> The following commands help when working with path expressions.</p>
<dl>
<dt><code>defnode</code> &lt;<font SIZE="-1">NAME</font>&gt; &lt;<font SIZE="-1">EXPR</font>&gt; [&lt;<font SIZE="-1">VALUE</font>&gt;]</p>
<dd> Define the variable <font SIZE="-1">NAME</font> to the result of evaluating <font SIZE="-1">EXPR,</font> which must be a nodeset. If no node matching <font SIZE="-1">EXPR</font> exists yet, one is created and <font SIZE="-1">NAME</font> will refer to it. If <font SIZE="-1">VALUE</font> is given, this is the same as &#8216;set <font SIZE="-1">EXPR VALUE</font>&#8216;; if <font SIZE="-1">VALUE</font> is not given, the node is created as if with &#8216;clear <font SIZE="-1">EXPR</font>&#8216; would and <font SIZE="-1">NAME</font> refers to that node.</p>
<dt><code>defvar</code> &lt;<font SIZE="-1">NAME</font>&gt; &lt;<font SIZE="-1">EXPR</font>&gt;</p>
<dd> Define the variable <font SIZE="-1">NAME</font> to the result of evaluating <font SIZE="-1">EXPR.</font> The variable can be used in path expressions as <tt>$NAME</tt>. Note that <font SIZE="-1">EXPR</font> is evaluated when the variable is defined, not when it is used.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><font SIZE="-1"><code>AUGEAS_ROOT</code></font></p>
<dd> The file system root, defaults to &#8216;/&#8217;. Can be overridden with the <code>-r</code> command line option</p>
<dt><font SIZE="-1"><code>AUGEAS_LENS_LIB</code></font></p>
<dd> Colon separated list of directories with lenses. Directories specified here are searched after any directories set with the <code>-I</code> command line option, but before the default directories <i>/usr/share/augeas/lenses</i> and <i>/usr/share/augeas/lenses/dist</i></dl>
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
<p> Augeas (and augtool) are distributed under the <font SIZE="-1">GNU</font> Lesser General Public License (<font SIZE="-1">LGPL</font>)</p>
<h2>SEE ALSO</h2>
<p> <code>Augeas</code> project homepage &lt;<a rel="nofollow" href="http://www.augeas.net/">http://www.augeas.net/</a>&gt; </p>
<p> augparse </p>
<h2>Index</h2>
<dt><a href="#lbAK">ENVIRONMENT VARIABLES</a></p>
<dd>
<dt><a href="#lbAL">DIAGNOSTICS</a></p>
<dd>
<dt><a href="#lbAM">EXAMPLES</a></p>
<dd>
<dt><a href="#lbAN">FILES</a></p>
<dd>
<dt><a href="#lbAO">AUTHOR</a></p>
<dd>
<dt><a href="#lbAP">COPYRIGHT AND LICENSE</a></p>
<dd>
<dt><a href="#lbAQ">SEE ALSO</a></p>
<dd></dl>

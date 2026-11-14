---
title: "git-checkout-index(1)"
name: "git-checkout-index"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-checkout-index/"
description: "git-checkout-index – Copy files from the index to the working tree"
---

<h2 class="name">NAME</h2>
<p> git-checkout-index &#8211; Copy files from the index to the working tree </p>
<h2>SYNOPSIS</h2>
<pre><code>
git checkout - index[-u][-q][-a][-f][-n][--prefix = &lt;string&gt;]
                    [--stage = &lt;number&gt; | all]
                    [--temp]
                    [-z][--stdin]
                    [--][&lt;file&gt;...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Will copy all files listed from the index to the working directory (not overwriting existing files).</p>
<h2>OPTIONS</h2>
<p> -u, &#8211;index</p>
<dl>
<dt>
<dd> update stat information for the checked out entries in the index file.</dl>
<p> -q, &#8211;quiet</p>
<dl>
<dt>
<dd> be quiet if files exist or are not in the index</dl>
<p> -f, &#8211;force</p>
<dl>
<dt>
<dd> forces overwrite of existing files</dl>
<p> -a, &#8211;all</p>
<dl>
<dt>
<dd> checks out all files in the index. Cannot be used together with explicit filenames.</dl>
<p> -n, &#8211;no-create</p>
<dl>
<dt>
<dd> Don&#8217;t checkout new files, only refresh files already checked out.</dl>
<p> &#8211;prefix=&lt;string&gt;</p>
<dl>
<dt>
<dd> When creating files, prepend &lt;string&gt; (usually a directory including a trailing /)</dl>
<p> &#8211;stage=&lt;number&gt;|all</p>
<dl>
<dt>
<dd> Instead of checking out unmerged entries, copy out the files from named stage. &lt;number&gt; must be between 1 and 3. Note: &#8211;stage=all automatically implies &#8211;temp.</dl>
<p> &#8211;temp</p>
<dl>
<dt>
<dd> Instead of copying the files to the working directory write the content to temporary files. The temporary name associations will be written to stdout.</dl>
<p> &#8211;stdin</p>
<dl>
<dt>
<dd> Instead of taking list of paths from the command line, read list of paths from the standard input. Paths are separated by LF (i.e. one path per line) by default.</dl>
<p> -z</p>
<dl>
<dt>
<dd> Only meaningful with <code>&#8211;stdin</code>; paths are separated with NUL character instead of LF.</dl>
<p> &#8212;</p>
<dl>
<dt>
<dd> Do not interpret any more arguments as options.</dl>
<p> The order of the flags used to matter, but not anymore. </p>
<p> Just doing <code>git checkout-index</code> does nothing. You probably meant <code>git checkout-index -a</code>. And if you want to force it, you want <code>git checkout-index -f -a</code>. </p>
<p> Intuitiveness is not the goal here. Repeatability is. The reason for the &quot;no arguments means no work&quot; behavior is that from scripts you are supposed to be able to do: </p>
<dl>
<dt>
<dd>
<pre>
$ find . -name '*.h' -print0 | xargs -0 git checkout-index -f --
</pre>
</dl>
<p> which will force all existing <code>*.h</code> files to be replaced with their cached copies. If an empty command line implied &quot;all&quot;, then this would force-refresh everything in the index, which was not the point. But since <i>git checkout-index</i> accepts &#8211;stdin it would be faster to use: </p>
<dl>
<dt>
<dd>
<pre>
$ find . -name '*.h' -print0 | git checkout-index -f -z --stdin
</pre>
</dl>
<p> The <code>&#8212;</code> is just a good idea when you know the rest will be filenames; it will prevent problems with a filename of, for example, <code>-a</code>. Using <code>&#8212;</code> is probably a good policy in scripts.</p>
<h2>USING &#8211;TEMP OR &#8211;STAGE=ALL</h2>
<p> When <code>&#8211;temp</code> is used (or implied by <code>&#8211;stage=all</code>) <i>git checkout-index</i> will create a temporary file for each index entry being checked out. The index will not be updated with stat information. These options can be useful if the caller needs all stages of all unmerged entries so that the unmerged files can be processed by an external merge tool. </p>
<p> A listing will be written to stdout providing the association of temporary file names to tracked path names. The listing format has two variations: </p>
<dl>
<dt>
<dd> 1. tempname TAB path RS </p>
<p> The first format is what gets used when <code>&#8211;stage</code> is omitted or is not <code>&#8211;stage=all</code>. The field tempname is the temporary file name holding the file content and path is the tracked path name in the index. Only the requested entries are output.</dl>
<dl>
<dt>
<dd> 2. stage1temp SP stage2temp SP stage3tmp TAB path RS </p>
<p> The second format is what gets used when <code>&#8211;stage=all</code>. The three stage temporary fields (stage1temp, stage2temp, stage3temp) list the name of the temporary file if there is a stage entry in the index or <code>.</code> if there is no stage entry. Paths which only have a stage 0 entry will always be omitted from the output.</dl>
<p> In both formats RS (the record separator) is newline by default but will be the null byte if -z was passed on the command line. The temporary file names are always safe strings; they will never contain directory separators or whitespace characters. The path field is always relative to the current directory and the temporary file names are always relative to the top level directory. </p>
<p> If the object being copied out to a temporary file is a symbolic link the content of the link will be written to a normal file. It is up to the end-user or the Porcelain to make use of this information.</p>
<h2>EXAMPLES</h2>
<p> To update and refresh only the files already checked out</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
$ git checkout-index -n -f -a &amp;&amp; git update-index --ignore-missing --refresh
</pre>
</dl>
</dl>
<p> Using <i>git checkout-index</i> to &quot;export an entire tree&quot;</p>
<dl>
<dt>
<dd> The prefix ability basically makes it trivial to use <i>git checkout-index</i> as an &quot;export as tree&quot; function. Just read the desired tree into the index, and do: </p>
<dl>
<dt>
<dd>
<pre>
$ git checkout-index --prefix=git-export-dir/ -a
</pre>
</dl>
<p> <code>git checkout-index</code> will &quot;export&quot; the index into the specified directory. </p>
<p> The final &quot;/&quot; is important. The exported name is literally just prefixed with the specified string. Contrast this with the following example.</dl>
<p> Export files with a prefix</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
$ git checkout-index --prefix=.merged- Makefile
</pre>
</dl>
<p> This will check out the currently cached copy of <code>Makefile</code> into the file <code>.merged-Makefile</code>.</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>

---
title: "git-ls-tree(1)"
name: "git-ls-tree"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-ls-tree/"
description: "git-ls-tree – List the contents of a tree object"
---
<h2>SYNOPSIS</h2>
<pre><code>
 git ls-tree  [-d] [-r] [-t] [-l] [-z]
            [--name-only] [--name-status] [--full-name] [--full-tree] [--abbrev[=&lt;n&gt;]]
            &lt;tree-ish&gt; [&lt;path&gt;...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Lists the contents of a given tree object, like what &quot;/bin/ls -a&quot; does in the current working directory. Note that: </p>
<dl>
<dd> <p> &bull; the behaviour is slightly different from that of &quot;/bin/ls&quot; in that the <i>&lt;path&gt;</i> denotes just a list of patterns to match, e.g. so specifying directory name (without <code>-r</code>) will behave differently, and order of the arguments does not matter. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; the behaviour is similar to that of &quot;/bin/ls&quot; in that the <i>&lt;path&gt;</i> is taken as relative to the current working directory. E.g. when you are in a directory <i>sub</i> that has a directory <i>dir</i>, you can run <i>git ls-tree -r HEAD dir</i> to list the contents of the tree (that is <code>sub/dir</code> in <code>HEAD</code>). You don&#8217;t want to give a tree that is not at the root level (e.g. <code>git ls-tree -r HEAD:sub dir</code>) in this case, as that would result in asking for <code>sub/sub/dir</code> in the <code>HEAD</code> commit. However, the current working directory can be ignored by passing --full-tree option. </p>
 </dd></dl>
<h2>OPTIONS</h2>
<p> &lt;tree-ish&gt; </p>
<dl>
<dd> <p> Id of a tree-ish. </p>
 </dd></dl>
<p> -d </p>
<dl>
<dd> <p> Show only the named tree entry itself, not its children. </p>
 </dd></dl>
<p> -r </p>
<dl>
<dd> <p> Recurse into sub-trees. </p>
 </dd></dl>
<p> -t </p>
<dl>
<dd> <p> Show tree entries even when going to recurse them. Has no effect if <code>-r</code> was not passed. <code>-d</code> implies <code>-t</code>. </p>
 </dd></dl>
<p> -l, --long </p>
<dl>
<dd> <p> Show object size of blob (file) entries. </p>
 </dd></dl>
<p> -z </p>
<dl>
<dd> <p> \0 line termination on output and do not quote filenames. See OUTPUT FORMAT below for more information. </p>
 </dd></dl>
<p> --name-only, --name-status </p>
<dl>
<dd> <p> List only filenames (instead of the &quot;long&quot; output), one per line. </p>
 </dd></dl>
<p> --abbrev[=&lt;n&gt;] </p>
<dl>
<dd> <p> Instead of showing the full 40-byte hexadecimal object lines, show the shortest prefix that is at least <i>&lt;n&gt;</i> hexdigits long that uniquely refers the object. Non default number of digits can be specified with --abbrev=&lt;n&gt;. </p>
 </dd></dl>
<p> --full-name </p>
<dl>
<dd> <p> Instead of showing the path names relative to the current working directory, show the full path names. </p>
 </dd></dl>
<p> --full-tree </p>
<dl>
<dd> <p> Do not limit the listing to the current working directory. Implies --full-name. </p>
 </dd></dl>
<p> [&lt;path&gt;...] </p>
<dl>
<dd> <p> When paths are given, show them (note that this isn&#8217;t really raw pathnames, but rather a list of patterns to match). Otherwise implicitly uses the root level of the tree as the sole path argument. </p>
 </dd></dl>
<h2>OUTPUT FORMAT</h2>
<dl>
<dd> <pre><code>&lt;mode&gt; SP &lt;type&gt; SP &lt;object&gt; TAB &lt;file&gt;
</code></pre>
 </dd></dl>
<p> This output format is compatible with what <code>--index-info --stdin</code> of <i>git update-index</i> expects. </p>
<p> When the <code>-l</code> option is used, format changes to </p>
<dl>
<dd> <pre><code>&lt;mode&gt; SP &lt;type&gt; SP &lt;object&gt; SP &lt;object size&gt; TAB &lt;file&gt;
</code></pre>
 </dd></dl>
<p> Object size identified by &lt;object&gt; is given in bytes, and right-justified with minimum width of 7 characters. Object size is given only for blobs (file) entries; for other entries <code>-</code> character is used in place of size. </p>
<p> Without the <code>-z</code> option, pathnames with &quot;unusual&quot; characters are quoted as explained for the configuration variable <code>core.quotePath</code> (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)). Using <code>-z</code> the filename is output verbatim and the line is terminated by a NUL byte.  </p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>

---
title: "git-commit-graph(1)"
name: "git-commit-graph"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-commit-graph/"
description: "git-commit-graph – Write and verify Git commit-graph files"
---

<h2 class="name">NAME</h2>
<p> git-commit-graph &#8211; Write and verify Git commit-graph files </p>
<h2>SYNOPSIS</h2>
<pre><code>
git commit - graph verify[--object - dir&lt;dir&gt;][--shallow][--[no - ] progress] git commit - graph write&lt;options&gt;[--object - dir&lt;dir&gt;][--[no - ] progress]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Manage the serialized commit-graph file.</p>
<h2>OPTIONS</h2>
<p> &#8211;object-dir</p>
<dl>
<dt>
<dd> Use given directory for the location of packfiles and commit-graph file. This parameter exists to specify the location of an alternate that only has the objects directory, not a full <code>.git</code> directory. The commit-graph file is expected to be in the <code>&lt;dir&gt;/info</code> directory and the packfiles are expected to be in <code>&lt;dir&gt;/pack</code>. If the directory could not be made into an absolute path, or does not match any known object directory, <code>git commit-graph &#8230;</code> will exit with non-zero status.</dl>
<p> &#8211;[no-]progress</p>
<dl>
<dt>
<dd> Turn progress on/off explicitly. If neither is specified, progress is shown if standard error is connected to a terminal.</dl>
<h2>COMMANDS</h2>
<p> <i>write</i></p>
<dl>
<dt>
<dd> Write a commit-graph file based on the commits found in packfiles. If the config option <code>core.commitGraph</code> is disabled, then this command will output a warning, then return success without writing a commit-graph file. </p>
<p> With the <code>&#8211;stdin-packs</code> option, generate the new commit graph by walking objects only in the specified pack-indexes. (Cannot be combined with <code>&#8211;stdin-commits</code> or <code>&#8211;reachable</code>.) </p>
<p> With the <code>&#8211;stdin-commits</code> option, generate the new commit graph by walking commits starting at the commits specified in stdin as a list of OIDs in hex, one OID per line. OIDs that resolve to non-commits (either directly, or by peeling tags) are silently ignored. OIDs that are malformed, or do not exist generate an error. (Cannot be combined with <code>&#8211;stdin-packs</code> or <code>&#8211;reachable</code>.) </p>
<p> With the <code>&#8211;reachable</code> option, generate the new commit graph by walking commits starting at all refs. (Cannot be combined with <code>&#8211;stdin-commits</code> or <code>&#8211;stdin-packs</code>.) </p>
<p> With the <code>&#8211;append</code> option, include all commits that are present in the existing commit-graph file. </p>
<p> With the <code>&#8211;changed-paths</code> option, compute and write information about the paths changed between a commit and its first parent. This operation can take a while on large repositories. It provides significant performance gains for getting history of a directory or a file with <code>git log &#8212; &lt;path&gt;</code>. If this option is given, future commit-graph writes will automatically assume that this option was intended. Use <code>&#8211;no-changed-paths</code> to stop storing this data. </p>
<p> With the <code>&#8211;max-new-filters=&lt;n&gt;</code> option, generate at most <code>n</code> new Bloom filters (if <code>&#8211;changed-paths</code> is specified). If <code>n</code> is <code>-1</code>, no limit is enforced. Only commits present in the new layer count against this limit. To retroactively compute Bloom filters over earlier layers, it is advised to use <code>&#8211;split=replace</code>. Overrides the <code>commitGraph.maxNewFilters</code> configuration. </p>
<p> With the <code>&#8211;split[=&lt;strategy&gt;]</code> option, write the commit-graph as a chain of multiple commit-graph files stored in <code>&lt;dir&gt;/info/commit-graphs</code>. Commit-graph layers are merged based on the strategy and other splitting options. The new commits not already in the commit-graph are added in a new &quot;tip&quot; file. This file is merged with the existing file if the following merge conditions are met: </p>
<dl>
<dt>
<dd> &bull; If <code>&#8211;split=no-merge</code> is specified, a merge is never performed, and the remaining options are ignored. <code>&#8211;split=replace</code> overwrites the existing chain with a new one. A bare <code>&#8211;split</code> defers to the remaining options. (Note that merging a chain of commit graphs replaces the existing chain with a length-1 chain where the first and only incremental holds the entire graph).</dl>
<dl>
<dt>
<dd> &bull; If <code>&#8211;size-multiple=&lt;X&gt;</code> is not specified, let <code>X</code> equal 2. If the new tip file would have <code>N</code> commits and the previous tip has <code>M</code> commits and <code>X</code> times <code>N</code> is greater than <code>M</code>, instead merge the two files into a single file.</dl>
<dl>
<dt>
<dd> &bull; If <code>&#8211;max-commits=&lt;M&gt;</code> is specified with <code>M</code> a positive integer, and the new tip file would have more than <code>M</code> commits, then instead merge the new tip with the previous tip. </p>
<p> Finally, if <code>&#8211;expire-time=&lt;datetime&gt;</code> is not specified, let <code>datetime</code> be the current time. After writing the split commit-graph, delete all unused commit-graph whose modified times are older than <code>datetime</code>.</dl>
</dl>
<p> <i>verify</i></p>
<dl>
<dt>
<dd> Read the commit-graph file and verify its contents against the object database. Used to check for corrupted data. </p>
<p> With the <code>&#8211;shallow</code> option, only check the tip commit-graph file in a chain of split commit-graphs.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd> &bull; Write a commit-graph file for the packed commits in your local <code>.git</code> directory. </p>
<dl>
<dt>
<dd>
<pre>
$ git commit-graph write
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Write a commit-graph file, extending the current commit-graph file using commits in <code>&lt;pack-index&gt;</code>. </p>
<dl>
<dt>
<dd>
<pre>
$ echo &lt;pack-index&gt; | git commit-graph write --stdin-packs
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Write a commit-graph file containing all reachable commits. </p>
<dl>
<dt>
<dd>
<pre>
$ git show-ref -s | git commit-graph write --stdin-commits
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Write a commit-graph file containing all commits in the current commit-graph file along with those reachable from <code>HEAD</code>. </p>
<dl>
<dt>
<dd>
<pre>
$ git rev-parse HEAD | git commit-graph write --stdin-commits --append
</pre>
</dl>
</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>

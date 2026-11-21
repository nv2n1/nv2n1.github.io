---
title: "git-restore-mtime(1)"
name: "git-restore-mtime"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-restore-mtime/"
description: "git-restore-mtime – Restore original modification time of files based on the date of the most recent commit that modified them"
---

<h2>SYNOPSIS</h2>
<dl>
<dt><code>git-restore-mtime</code></dt>
<dd> [<code>-h</code>] [<code>&#8211;quiet</code>] [<code>&#8211;verbose</code>] [<code>&#8211;force</code>] [<code>&#8211;merge</code>] [<code>&#8211;first-parent</code>]<br />
 [<code>&#8211;skip-missing</code>] [<code>&#8211;no-directories</code>] [<code>&#8211;test</code>] [<code>&#8211;commit-time</code>]<br />
 [<code>&#8211;work-tree</code> <i>WORKDIR</i>] [<code>&#8211;git-dir</code> <i>GITDIR</i>]<br />
 [<i>pathspec</i> [<i>pathspec</i>&#8230;]]</dd></dl>
<h2>DESCRIPTION</h2>
<p> Restore original modification time of files based on the date of the most recent commit that modified them. Useful when generating release tarballs.</p>
<h2>OPTIONS</h2>
<h3>Positional arguments:</h3>
<dl>
<dt><i>pathspec</i></dt>
<dd> only modify paths (dirs or files) matching PATHSPEC, relative to current directory. Default is to modify all non-ignored, tracked files.</dd></dl>
<h3>Optional arguments:</h3>
<dl>
<dt><code>-h</code>,<code>&nbsp;<wbr>&#8211;help</code></dt>
<dd> show help message and exit</dd>
<dt><code>&#8211;quiet</code>,<code>-q</code></dt>
<dd> suppress informative messages and summary statistics.</dd>
<dt><code>&#8211;verbose</code>,<code>-v</code></dt>
<dd> print additional information for each processed file. Overwrites &#8211;quiet.</dd>
<dt><code>&#8211;force</code>,<code>-f</code></dt>
<dd> force execution on trees with uncommitted changes.</dd>
<dt><code>&#8211;merge</code>,<code>-m</code></dt>
<dd> include merge commits. Leads to more recent mtimes and more files per commit, thus with the same mtime (which may or may not be what you want). Including merge commits may lead to less commits being evaluated (all files are found sooner), which improves performance, sometimes substantially. But since merge commits are usually huge, processing them may also take longer, sometimes substantially. By default merge logs are only used for files missing from regular commit logs.</dd>
<dt><code>&#8211;first-parent</code></dt>
<dd> pass &#8211;first-parent to git whatchanged to hide the second parent from the merge commit logs. Only has any effect if &#8211;merge is also specified or &#8211;skip-missing is not specified and there were files not found in regular commit logs.</dd>
<dt><code>&#8211;skip-missing</code>,<code>-s</code></dt>
<dd> do not try to find missing files. If some files were not found in regular commit logs, by default it retries using merge commit logs for these files (if &#8211;merge was not used already). This option disables this behavior, which may slightly improve performance, but files found only in merge commits will not be updated.</dd>
<dt><code>&#8211;no-directories</code>,<code>-D</code></dt>
<dd> do not update directory mtime for files created, renamed or deleted in it. Note: just modifying a file will not update its directory mtime.</dd>
<dt><code>&#8211;test</code>,<code>-t</code></dt>
<dd> test run: do not actually update any file</dd>
<dt><code>&#8211;commit-time</code>,<code>-c</code></dt>
<dd> use commit time instead of author time</dd>
<dt><code>&#8211;work-tree&nbsp;<wbr></code><i>WORKDIR</i></dt>
<dd> specify where the work tree is. Default for most repositories is current directory.</dd>
<dt><code>&#8211;git-dir&nbsp;<wbr></code><i>GITDIR</i></dt>
<dd> specify where the git repository is. Default for most repositories &lt;work-tree&gt;/.git</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a rel="nofollow" href="https://github.com/MestreLion/git-tools">https://github.com/MestreLion/git-tools</a></code></p>
<h2>AUTHOR</h2>
<p> Rodrigo Silva (MestreLion) linux [at] rodrigosilva.com </p>

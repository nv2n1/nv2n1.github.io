---
title: "git-mv(1)"
name: "git-mv"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-mv/"
description: "git-mv – Move or rename a file, a directory, or a symlink"
---

<h2 class="name">NAME</h2>
<p> git-mv &#8211; Move or rename a file, a directory, or a symlink </p>
<h2>SYNOPSIS</h2>
<pre>
<i>git mv</i> &lt;options&gt;... &lt;args&gt;...
</pre>
<h2>DESCRIPTION</h2>
<p> Move or rename a file, directory or symlink. </p>
<dl>
<dt>
<dd>
<pre><code>
git mv[-v][-f][-n][-k]&lt;source&gt;&lt;destination&gt;
    git mv[-v][-f][-n][-k]&lt;source&gt;...&lt;destination directory&gt;
</code></pre>
</dl>
<p> In the first form, it renames &lt;source&gt;, which must exist and be either a file, symlink or directory, to &lt;destination&gt;. In the second form, the last argument has to be an existing directory; the given sources will be moved into this directory. </p>
<p> The index is updated after successful completion, but the change must still be committed.</p>
<h2>OPTIONS</h2>
<p> -f, &#8211;force</p>
<dl>
<dt>
<dd> Force renaming or moving of a file even if the target exists</dl>
<p> -k</p>
<dl>
<dt>
<dd> Skip move or rename actions which would lead to an error condition. An error happens when a source is neither existing nor controlled by Git, or when it would overwrite an existing file unless <code>-f</code> is given.</dl>
<p> -n, &#8211;dry-run</p>
<dl>
<dt>
<dd> Do nothing; only show what would happen</dl>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
<dd> Report the names of files as they are moved.</dl>
<h2>SUBMODULES</h2>
<p> Moving a submodule using a gitfile (which means they were cloned with a Git version 1.7.8 or newer) will update the gitfile and core.worktree setting to make the submodule work in the new location. It also will attempt to update the submodule.&lt;name&gt;.path setting in the <code><a href="/docs/linux/man/5-gitmodules/">gitmodules</a></code>(5) file and stage that file (unless -n is used).</p>
<h2>BUGS</h2>
<p> Each time a superproject update moves a populated submodule (e.g. when switching between commits before and after the move) a stale submodule checkout will remain in the old location and an empty directory will appear in the new location. To populate the submodule again in the new location the user will have to run &quot;git submodule update&quot; afterwards. Removing the old directory is only safe when it uses a gitfile, as otherwise the history of the submodule will be deleted too. Both steps will be obsolete when recursive submodule update has been implemented.</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>

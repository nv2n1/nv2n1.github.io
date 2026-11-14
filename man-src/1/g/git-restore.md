---
title: "git-restore(1)"
name: "git-restore"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-restore/"
description: "git-restore – Restore working tree files"
---

<h2 class="name">NAME</h2>
<p> git-restore &#8211; Restore working tree files </p>
<h2>SYNOPSIS</h2>
<pre><code>
git restore[&lt;options&gt;][--source = &lt;tree&gt;][--staged][--worktree][--]&lt;pathspec&gt;... git restore[&lt;options&gt;][--source = &lt;tree&gt;][--staged][--worktree]-- pathspec - from - file = &lt;file&gt;[--pathspec - file - nul] git restore(-p | --patch)[&lt;options&gt;][--source = &lt;tree&gt;][--staged][--worktree][--][&lt;pathspec&gt;...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Restore specified paths in the working tree with some contents from a restore source. If a path is tracked but does not exist in the restore source, it will be removed to match the source. </p>
<p> The command can also be used to restore the content in the index with <code>&#8211;staged</code>, or restore both the working tree and the index with <code>&#8211;staged &#8211;worktree</code>. </p>
<p> By default, if <code>&#8211;staged</code> is given, the contents are restored from <code>HEAD</code>, otherwise from the index. Use <code>&#8211;source</code> to restore from a different commit. </p>
<p> See &quot;Reset, restore and revert&quot; in <code><a href="/docs/linux/man/1-git/">git</a></code>(1) for the differences between the three commands. </p>
<p> THIS COMMAND IS EXPERIMENTAL. THE BEHAVIOR MAY CHANGE.</p>
<h2>OPTIONS</h2>
<p> -s &lt;tree&gt;, &#8211;source=&lt;tree&gt;</p>
<dl>
<dt>
<dd> Restore the working tree files with the content from the given tree. It is common to specify the source tree by naming a commit, branch or tag associated with it. </p>
<p> If not specified, the contents are restored from <code>HEAD</code> if <code>&#8211;staged</code> is given, otherwise from the index. </p>
<p> As a special case, you may use <code>&quot;A&#8230;B&quot;</code> as a shortcut for the merge base of <code>A</code> and <code>B</code> if there is exactly one merge base. You can leave out at most one of <code>A</code> and <code>B</code>, in which case it defaults to <code>HEAD</code>.</dl>
<p> -p, &#8211;patch</p>
<dl>
<dt>
<dd> Interactively select hunks in the difference between the restore source and the restore location. See the &#8220;Interactive Mode&#8221; section of <code><a href="/docs/linux/man/1-git-add/">git-add</a></code>(1) to learn how to operate the <code>&#8211;patch</code> mode. </p>
<p> Note that <code>&#8211;patch</code> can accept no pathspec and will prompt to restore all modified paths.</dl>
<p> -W, &#8211;worktree, -S, &#8211;staged</p>
<dl>
<dt>
<dd> Specify the restore location. If neither option is specified, by default the working tree is restored. Specifying <code>&#8211;staged</code> will only restore the index. Specifying both restores both.</dl>
<p> -q, &#8211;quiet</p>
<dl>
<dt>
<dd> Quiet, suppress feedback messages. Implies <code>&#8211;no-progress</code>.</dl>
<p> &#8211;progress, &#8211;no-progress</p>
<dl>
<dt>
<dd> Progress status is reported on the standard error stream by default when it is attached to a terminal, unless <code>&#8211;quiet</code> is specified. This flag enables progress reporting even if not attached to a terminal, regardless of <code>&#8211;quiet</code>.</dl>
<p> &#8211;ours, &#8211;theirs</p>
<dl>
<dt>
<dd> When restoring files in the working tree from the index, use stage #2 (<i>ours</i>) or #3 (<i>theirs</i>) for unmerged paths. </p>
<p> Note that during <code>git rebase</code> and <code>git pull &#8211;rebase</code>, <i>ours</i> and <i>theirs</i> may appear swapped. See the explanation of the same options in <code><a href="/docs/linux/man/1-git-checkout/">git-checkout</a></code>(1) for details.</dl>
<p> -m, &#8211;merge</p>
<dl>
<dt>
<dd> When restoring files on the working tree from the index, recreate the conflicted merge in the unmerged paths.</dl>
<p> &#8211;conflict=&lt;style&gt;</p>
<dl>
<dt>
<dd> The same as <code>&#8211;merge</code> option above, but changes the way the conflicting hunks are presented, overriding the <code>merge.conflictStyle</code> configuration variable. Possible values are &quot;merge&quot; (default) and &quot;diff3&quot; (in addition to what is shown by &quot;merge&quot; style, shows the original contents).</dl>
<p> &#8211;ignore-unmerged</p>
<dl>
<dt>
<dd> When restoring files on the working tree from the index, do not abort the operation if there are unmerged entries and neither <code>&#8211;ours</code>, <code>&#8211;theirs</code>, <code>&#8211;merge</code> or <code>&#8211;conflict</code> is specified. Unmerged paths on the working tree are left alone.</dl>
<p> &#8211;ignore-skip-worktree-bits</p>
<dl>
<dt>
<dd> In sparse checkout mode, by default is to only update entries matched by <code>&lt;pathspec&gt;</code> and sparse patterns in $GIT_DIR/info/sparse-checkout. This option ignores the sparse patterns and unconditionally restores any files in <code>&lt;pathspec&gt;</code>.</dl>
<p> &#8211;recurse-submodules, &#8211;no-recurse-submodules</p>
<dl>
<dt>
<dd> If <code>&lt;pathspec&gt;</code> names an active submodule and the restore location includes the working tree, the submodule will only be updated if this option is given, in which case its working tree will be restored to the commit recorded in the superproject, and any local modifications overwritten. If nothing (or <code>&#8211;no-recurse-submodules</code>) is used, submodules working trees will not be updated. Just like <code><a href="/docs/linux/man/1-git-checkout/">git-checkout</a></code>(1), this will detach <code>HEAD</code> of the submodule.</dl>
<p> &#8211;overlay, &#8211;no-overlay</p>
<dl>
<dt>
<dd> In overlay mode, the command never removes files when restoring. In no-overlay mode, tracked files that do not appear in the <code>&#8211;source</code> tree are removed, to make them match <code>&lt;tree&gt;</code> exactly. The default is no-overlay mode.</dl>
<p> &#8211;pathspec-from-file=&lt;file&gt;</p>
<dl>
<dt>
<dd> Pathspec is passed in <code>&lt;file&gt;</code> instead of commandline args. If <code>&lt;file&gt;</code> is exactly <code>&#8211;</code> then standard input is used. Pathspec elements are separated by LF or CR/LF. Pathspec elements can be quoted as explained for the configuration variable <code>core.quotePath</code> (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)). See also <code>&#8211;pathspec-file-nul</code> and global <code>&#8211;literal-pathspecs</code>.</dl>
<p> &#8211;pathspec-file-nul</p>
<dl>
<dt>
<dd> Only meaningful with <code>&#8211;pathspec-from-file</code>. Pathspec elements are separated with NUL character and all other characters are taken literally (including newlines and quotes).</dl>
<p> &#8212;</p>
<dl>
<dt>
<dd> Do not interpret any more arguments as options.</dl>
<p> &lt;pathspec&gt;&#8230;</p>
<dl>
<dt>
<dd> Limits the paths affected by the operation. </p>
<p> For more details, see the <i>pathspec</i> entry in <code><a href="/docs/linux/man/7-gitglossary/">gitglossary</a></code>(7).</dl>
<h2>EXAMPLES</h2>
<p> The following sequence switches to the <code>master</code> branch, reverts the <code>Makefile</code> to two revisions back, deletes hello.c by mistake, and gets it back from the index. </p>
<dl>
<dt>
<dd>
<pre>
$ git switch master
$ git restore --source master~2 Makefile  <code>(1)</code>
$ rm -f hello.c
$ git restore hello.c                     <code>(2)</code>
</pre>
</dl>
<p> <code>1. </code>take a file out of another commit<br />
 <code>2. </code>restore hello.c from the index </p>
<p> If you want to restore <i>all</i> C source files to match the version in the index, you can say </p>
<dl>
<dt>
<dd>
<pre>
$ git restore '*.c'
</pre>
</dl>
<p> Note the quotes around <code>*.c</code>. The file <code>hello.c</code> will also be restored, even though it is no longer in the working tree, because the file globbing is used to match entries in the index (not in the working tree by the shell). </p>
<p> To restore all files in the current directory </p>
<dl>
<dt>
<dd>
<pre>
$ git restore .
</pre>
</dl>
<p> or to restore all working tree files with <i>top</i> pathspec magic (see <code><a href="/docs/linux/man/7-gitglossary/">gitglossary</a></code>(7)) </p>
<dl>
<dt>
<dd>
<pre>
$ git restore :/
</pre>
</dl>
<p> To restore a file in the index to match the version in <code>HEAD</code> (this is the same as using <code><a href="/docs/linux/man/1-git-reset/">git-reset</a></code>(1)) </p>
<dl>
<dt>
<dd>
<pre>
$ git restore --staged hello.c
</pre>
</dl>
<p> or you can restore both the index and the working tree (this the same as using <code><a href="/docs/linux/man/1-git-checkout/">git-checkout</a></code>(1)) </p>
<dl>
<dt>
<dd>
<pre>
$ git restore --source=HEAD --staged --worktree hello.c
</pre>
</dl>
<p> or the short form which is more practical but less readable: </p>
<dl>
<dt>
<dd>
<pre>
$ git restore -s@ -SW hello.c
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-checkout/">git-checkout</a></code>(1), <code><a href="/docs/linux/man/1-git-reset/">git-reset</a></code>(1)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>

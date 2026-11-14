---
title: "git-switch(1)"
name: "git-switch"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-switch/"
description: "git-switch – Switch branches"
---

<h2 class="name">NAME</h2>
<p> git-switch &#8211; Switch branches </p>
<h2>SYNOPSIS</h2>
<pre><code>
git switch[&lt;options&gt;][--no - guess]&lt;branch&gt;
    git switch[&lt;options&gt;]-- detach[&lt;start - point&gt;] git switch[&lt;options&gt;](-c | -C)&lt;new - branch&gt;[&lt;start - point&gt;] git switch[&lt;options&gt;]-- orphan&lt;new - branch&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<p> Switch to a specified branch. The working tree and the index are updated to match the branch. All new commits will be added to the tip of this branch. </p>
<p> Optionally a new branch could be created with either <code>-c</code>, <code>-C</code>, automatically from a remote branch of same name (see <code>&#8211;guess</code>), or detach the working tree from any branch with <code>&#8211;detach</code>, along with switching. </p>
<p> Switching branches does not require a clean index and working tree (i.e. no differences compared to <code>HEAD</code>). The operation is aborted however if the operation leads to loss of local changes, unless told otherwise with <code>&#8211;discard-changes</code> or <code>&#8211;merge</code>. </p>
<p> THIS COMMAND IS EXPERIMENTAL. THE BEHAVIOR MAY CHANGE.</p>
<h2>OPTIONS</h2>
<p> &lt;branch&gt;</p>
<dl>
<dt>
<dd> Branch to switch to.</dl>
<p> &lt;new-branch&gt;</p>
<dl>
<dt>
<dd> Name for the new branch.</dl>
<p> &lt;start-point&gt;</p>
<dl>
<dt>
<dd> The starting point for the new branch. Specifying a <code>&lt;start-point&gt;</code> allows you to create a branch based on some other point in history than where HEAD currently points. (Or, in the case of <code>&#8211;detach</code>, allows you to inspect and detach from some other point.) </p>
<p> You can use the <code>@{-N}</code> syntax to refer to the N-th last branch/commit switched to using &quot;git switch&quot; or &quot;git checkout&quot; operation. You may also specify <code>&#8211;</code> which is synonymous to <code>@{-1}</code>. This is often used to switch quickly between two branches, or to undo a branch switch by mistake. </p>
<p> As a special case, you may use <code>A&#8230;B</code> as a shortcut for the merge base of <code>A</code> and <code>B</code> if there is exactly one merge base. You can leave out at most one of <code>A</code> and <code>B</code>, in which case it defaults to <code>HEAD</code>.</dl>
<p> -c &lt;new-branch&gt;, &#8211;create &lt;new-branch&gt;</p>
<dl>
<dt>
<dd> Create a new branch named <code>&lt;new-branch&gt;</code> starting at <code>&lt;start-point&gt;</code> before switching to the branch. This is a convenient shortcut for: </p>
<dl>
<dt>
<dd>
<pre>
$ git branch &lt;new-branch&gt;
$ git switch &lt;new-branch&gt;
</pre>
</dl>
</dl>
<p> -C &lt;new-branch&gt;, &#8211;force-create &lt;new-branch&gt;</p>
<dl>
<dt>
<dd> Similar to <code>&#8211;create</code> except that if <code>&lt;new-branch&gt;</code> already exists, it will be reset to <code>&lt;start-point&gt;</code>. This is a convenient shortcut for: </p>
<dl>
<dt>
<dd>
<pre>
$ git branch -f &lt;new-branch&gt;
$ git switch &lt;new-branch&gt;
</pre>
</dl>
</dl>
<p> -d, &#8211;detach</p>
<dl>
<dt>
<dd> Switch to a commit for inspection and discardable experiments. See the &quot;DETACHED HEAD&quot; section in <code><a href="/docs/linux/man/1-git-checkout/">git-checkout</a></code>(1) for details.</dl>
<p> &#8211;guess, &#8211;no-guess</p>
<dl>
<dt>
<dd> If <code>&lt;branch&gt;</code> is not found but there does exist a tracking branch in exactly one remote (call it <code>&lt;remote&gt;</code>) with a matching name, treat as equivalent to </p>
<dl>
<dt>
<dd>
<pre>
$ git switch -c &lt;branch&gt; --track &lt;remote&gt;/&lt;branch&gt;
</pre>
</dl>
<p> If the branch exists in multiple remotes and one of them is named by the <code>checkout.defaultRemote</code> configuration variable, we&#8217;ll use that one for the purposes of disambiguation, even if the <code>&lt;branch&gt;</code> isn&#8217;t unique across all remotes. Set it to e.g. <code>checkout.defaultRemote=origin</code> to always checkout remote branches from there if <code>&lt;branch&gt;</code> is ambiguous but exists on the <i>origin</i> remote. See also <code>checkout.defaultRemote</code> in <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1). </p>
<p> <code>&#8211;guess</code> is the default behavior. Use <code>&#8211;no-guess</code> to disable it. </p>
<p> The default behavior can be set via the <code>checkout.guess</code> configuration variable.</dl>
<p> -f, &#8211;force</p>
<dl>
<dt>
<dd> An alias for <code>&#8211;discard-changes</code>.</dl>
<p> &#8211;discard-changes</p>
<dl>
<dt>
<dd> Proceed even if the index or the working tree differs from <code>HEAD</code>. Both the index and working tree are restored to match the switching target. If <code>&#8211;recurse-submodules</code> is specified, submodule content is also restored to match the switching target. This is used to throw away local changes.</dl>
<p> -m, &#8211;merge</p>
<dl>
<dt>
<dd> If you have local modifications to one or more files that are different between the current branch and the branch to which you are switching, the command refuses to switch branches in order to preserve your modifications in context. However, with this option, a three-way merge between the current branch, your working tree contents, and the new branch is done, and you will be on the new branch. </p>
<p> When a merge conflict happens, the index entries for conflicting paths are left unmerged, and you need to resolve the conflicts and mark the resolved paths with <code>git add</code> (or <code>git rm</code> if the merge should result in deletion of the path).</dl>
<p> &#8211;conflict=&lt;style&gt;</p>
<dl>
<dt>
<dd> The same as <code>&#8211;merge</code> option above, but changes the way the conflicting hunks are presented, overriding the <code>merge.conflictStyle</code> configuration variable. Possible values are &quot;merge&quot; (default) and &quot;diff3&quot; (in addition to what is shown by &quot;merge&quot; style, shows the original contents).</dl>
<p> -q, &#8211;quiet</p>
<dl>
<dt>
<dd> Quiet, suppress feedback messages.</dl>
<p> &#8211;progress, &#8211;no-progress</p>
<dl>
<dt>
<dd> Progress status is reported on the standard error stream by default when it is attached to a terminal, unless <code>&#8211;quiet</code> is specified. This flag enables progress reporting even if not attached to a terminal, regardless of <code>&#8211;quiet</code>.</dl>
<p> -t, &#8211;track</p>
<dl>
<dt>
<dd> When creating a new branch, set up &quot;upstream&quot; configuration. <code>-c</code> is implied. See <code>&#8211;track</code> in <code><a href="/docs/linux/man/1-git-branch/">git-branch</a></code>(1) for details. </p>
<p> If no <code>-c</code> option is given, the name of the new branch will be derived from the remote-tracking branch, by looking at the local part of the refspec configured for the corresponding remote, and then stripping the initial part up to the &quot;*&quot;. This would tell us to use <code>hack</code> as the local branch when branching off of <code>origin/hack</code> (or <code>remotes/origin/hack</code>, or even <code>refs/remotes/origin/hack</code>). If the given name has no slash, or the above guessing results in an empty name, the guessing is aborted. You can explicitly give a name with <code>-c</code> in such a case.</dl>
<p> &#8211;no-track</p>
<dl>
<dt>
<dd> Do not set up &quot;upstream&quot; configuration, even if the <code>branch.autoSetupMerge</code> configuration variable is true.</dl>
<p> &#8211;orphan &lt;new-branch&gt;</p>
<dl>
<dt>
<dd> Create a new <i>orphan</i> branch, named <code>&lt;new-branch&gt;</code>. All tracked files are removed.</dl>
<p> &#8211;ignore-other-worktrees</p>
<dl>
<dt>
<dd> <code>git switch</code> refuses when the wanted ref is already checked out by another worktree. This option makes it check the ref out anyway. In other words, the ref can be held by more than one worktree.</dl>
<p> &#8211;recurse-submodules, &#8211;no-recurse-submodules</p>
<dl>
<dt>
<dd> Using <code>&#8211;recurse-submodules</code> will update the content of all active submodules according to the commit recorded in the superproject. If nothing (or <code>&#8211;no-recurse-submodules</code>) is used, submodules working trees will not be updated. Just like <code><a href="/docs/linux/man/1-git-submodule/">git-submodule</a></code>(1), this will detach <code>HEAD</code> of the submodules.</dl>
<h2>EXAMPLES</h2>
<p> The following command switches to the &quot;master&quot; branch: </p>
<dl>
<dt>
<dd>
<pre>
$ git switch master
</pre>
</dl>
<p> After working in the wrong branch, switching to the correct branch would be done using: </p>
<dl>
<dt>
<dd>
<pre>
$ git switch mytopic
</pre>
</dl>
<p> However, your &quot;wrong&quot; branch and correct &quot;mytopic&quot; branch may differ in files that you have modified locally, in which case the above switch would fail like this: </p>
<dl>
<dt>
<dd>
<pre>
$ git switch mytopic
error: You have local changes to 'frotz'; not switching branches.
</pre>
</dl>
<p> You can give the <code>-m</code> flag to the command, which would try a three-way merge: </p>
<dl>
<dt>
<dd>
<pre>
$ git switch -m mytopic
Auto-merging frotz
</pre>
</dl>
<p> After this three-way merge, the local modifications are <i>not</i> registered in your index file, so <code>git diff</code> would show you what changes you made since the tip of the new branch. </p>
<p> To switch back to the previous branch before we switched to mytopic (i.e. &quot;master&quot; branch): </p>
<dl>
<dt>
<dd>
<pre>
$ git switch -
</pre>
</dl>
<p> You can grow a new branch from any commit. For example, switch to &quot;HEAD~3&quot; and create branch &quot;fixup&quot;: </p>
<dl>
<dt>
<dd>
<pre>
$ git switch -c fixup HEAD~3
Switched to a new branch 'fixup'
</pre>
</dl>
<p> If you want to start a new branch from a remote branch of the same name: </p>
<dl>
<dt>
<dd>
<pre>
$ git switch new-topic
Branch 'new-topic' set up to track remote branch 'new-topic' from 'origin'
Switched to a new branch 'new-topic'
</pre>
</dl>
<p> To check out commit <code>HEAD~3</code> for temporary inspection or experiment without creating a new branch: </p>
<dl>
<dt>
<dd>
<pre>
$ git switch --detach HEAD~3
HEAD is now at 9fc9555312 Merge branch 'cc/shared-index-permbits'
</pre>
</dl>
<p> If it turns out whatever you have done is worth keeping, you can always create a new name for it (without switching away): </p>
<dl>
<dt>
<dd>
<pre>
$ git switch -c good-surprises
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-checkout/">git-checkout</a></code>(1), <code><a href="/docs/linux/man/1-git-branch/">git-branch</a></code>(1)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>

---
title: "git-checkout(1)"
name: "git-checkout"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-checkout/"
description: "git-checkout – Switch branches or restore working tree files"
---

<h2 class="name">NAME</h2>
<p> git-checkout &#8211; Switch branches or restore working tree files </p>
<h2>SYNOPSIS</h2>
<pre><code>
git checkout[-q][-f][-m][&lt;branch&gt;] git checkout[-q][-f][-m]-- detach[&lt;branch&gt;] git checkout[-q][-f][-m][--detach]&lt;commit&gt;
        git checkout[-q][-f][-m][[-b | -B | --orphan]&lt;new_branch&gt;][&lt;start_point&gt;] git checkout[-f | --ours | --theirs | -m | --conflict = &lt;style&gt;][&lt;tree - ish&gt;][--]&lt;pathspec&gt;... git checkout[-f | --ours | --theirs | -m | --conflict = &lt;style&gt;][&lt;tree - ish&gt;]-- pathspec - from - file = &lt;file&gt;[--pathspec - file - nul] git checkout(-p | --patch)[&lt;tree - ish&gt;][--][&lt;pathspec&gt;...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Updates files in the working tree to match the version in the index or the specified tree. If no pathspec was given, <i>git checkout</i> will also update <code>HEAD</code> to set the specified branch as the current branch. </p>
<p> <i>git checkout</i> [&lt;branch&gt;]</p>
<dl>
<dt>
<dd> To prepare for working on <code>&lt;branch&gt;</code>, switch to it by updating the index and the files in the working tree, and by pointing <code>HEAD</code> at the branch. Local modifications to the files in the working tree are kept, so that they can be committed to the <code>&lt;branch&gt;</code>. </p>
<p> If <code>&lt;branch&gt;</code> is not found but there does exist a tracking branch in exactly one remote (call it <code>&lt;remote&gt;</code>) with a matching name and <code>&#8211;no-guess</code> is not specified, treat as equivalent to </p>
<dl>
<dt>
<dd>
<pre>
$ git checkout -b &lt;branch&gt; --track &lt;remote&gt;/&lt;branch&gt;
</pre>
</dl>
<p> You could omit <code>&lt;branch&gt;</code>, in which case the command degenerates to &quot;check out the current branch&quot;, which is a glorified no-op with rather expensive side-effects to show only the tracking information, if exists, for the current branch.</dl>
<p> <i>git checkout</i> -b|-B &lt;new_branch&gt; [&lt;start point&gt;]</p>
<dl>
<dt>
<dd> Specifying <code>-b</code> causes a new branch to be created as if <code><a href="/docs/linux/man/1-git-branch/">git-branch</a></code>(1) were called and then checked out. In this case you can use the <code>&#8211;track</code> or <code>&#8211;no-track</code> options, which will be passed to <i>git branch</i>. As a convenience, <code>&#8211;track</code> without <code>-b</code> implies branch creation; see the description of <code>&#8211;track</code> below. </p>
<p> If <code>-B</code> is given, <code>&lt;new_branch&gt;</code> is created if it doesn&#8217;t exist; otherwise, it is reset. This is the transactional equivalent of </p>
<dl>
<dt>
<dd>
<pre>
$ git branch -f &lt;branch&gt; [&lt;start point&gt;]
$ git checkout &lt;branch&gt;
</pre>
</dl>
<p> that is to say, the branch is not reset/created unless &quot;git checkout&quot; is successful.</dl>
<p> <i>git checkout</i> &#8211;detach [&lt;branch&gt;], <i>git checkout</i> [&#8211;detach] &lt;commit&gt;</p>
<dl>
<dt>
<dd> Prepare to work on top of <code>&lt;commit&gt;</code>, by detaching <code>HEAD</code> at it (see &quot;DETACHED HEAD&quot; section), and updating the index and the files in the working tree. Local modifications to the files in the working tree are kept, so that the resulting working tree will be the state recorded in the commit plus the local modifications. </p>
<p> When the <code>&lt;commit&gt;</code> argument is a branch name, the <code>&#8211;detach</code> option can be used to detach <code>HEAD</code> at the tip of the branch (<code>git checkout &lt;branch&gt;</code> would check out that branch without detaching <code>HEAD</code>). </p>
<p> Omitting <code>&lt;branch&gt;</code> detaches <code>HEAD</code> at the tip of the current branch.</dl>
<p> <i>git checkout</i> [-f|&#8211;ours|&#8211;theirs|-m|&#8211;conflict=&lt;style&gt;] [&lt;tree-ish&gt;] [&#8211;] &lt;pathspec&gt;&#8230;, <i>git checkout</i> [-f|&#8211;ours|&#8211;theirs|-m|&#8211;conflict=&lt;style&gt;] [&lt;tree-ish&gt;] &#8211;pathspec-from-file=&lt;file&gt; [&#8211;pathspec-file-nul]</p>
<dl>
<dt>
<dd> Overwrite the contents of the files that match the pathspec. When the <code>&lt;tree-ish&gt;</code> (most often a commit) is not given, overwrite working tree with the contents in the index. When the <code>&lt;tree-ish&gt;</code> is given, overwrite both the index and the working tree with the contents at the <code>&lt;tree-ish&gt;</code>. </p>
<p> The index may contain unmerged entries because of a previous failed merge. By default, if you try to check out such an entry from the index, the checkout operation will fail and nothing will be checked out. Using <code>-f</code> will ignore these unmerged entries. The contents from a specific side of the merge can be checked out of the index by using <code>&#8211;ours</code> or <code>&#8211;theirs</code>. With <code>-m</code>, changes made to the working tree file can be discarded to re-create the original conflicted merge result.</dl>
<p> <i>git checkout</i> (-p|&#8211;patch) [&lt;tree-ish&gt;] [&#8211;] [&lt;pathspec&gt;&#8230;]</p>
<dl>
<dt>
<dd> This is similar to the previous mode, but lets you use the interactive interface to show the &quot;diff&quot; output and choose which hunks to use in the result. See below for the description of <code>&#8211;patch</code> option.</dl>
<h2>OPTIONS</h2>
<p> -q, &#8211;quiet</p>
<dl>
<dt>
<dd> Quiet, suppress feedback messages.</dl>
<p> &#8211;progress, &#8211;no-progress</p>
<dl>
<dt>
<dd> Progress status is reported on the standard error stream by default when it is attached to a terminal, unless <code>&#8211;quiet</code> is specified. This flag enables progress reporting even if not attached to a terminal, regardless of <code>&#8211;quiet</code>.</dl>
<p> -f, &#8211;force</p>
<dl>
<dt>
<dd> When switching branches, proceed even if the index or the working tree differs from <code>HEAD</code>, and even if there are untracked files in the way. This is used to throw away local changes and any untracked files or directories that are in the way. </p>
<p> When checking out paths from the index, do not fail upon unmerged entries; instead, unmerged entries are ignored.</dl>
<p> &#8211;ours, &#8211;theirs</p>
<dl>
<dt>
<dd> When checking out paths from the index, check out stage #2 (<i>ours</i>) or #3 (<i>theirs</i>) for unmerged paths. </p>
<p> Note that during <code>git rebase</code> and <code>git pull &#8211;rebase</code>, <i>ours</i> and <i>theirs</i> may appear swapped; <code>&#8211;ours</code> gives the version from the branch the changes are rebased onto, while <code>&#8211;theirs</code> gives the version from the branch that holds your work that is being rebased. </p>
<p> This is because <code>rebase</code> is used in a workflow that treats the history at the remote as the shared canonical one, and treats the work done on the branch you are rebasing as the third-party work to be integrated, and you are temporarily assuming the role of the keeper of the canonical history during the rebase. As the keeper of the canonical history, you need to view the history from the remote as <code>ours</code> (i.e. &quot;our shared canonical history&quot;), while what you did on your side branch as <code>theirs</code> (i.e. &quot;one contributor&#8217;s work on top of it&quot;).</dl>
<p> -b &lt;new_branch&gt;</p>
<dl>
<dt>
<dd> Create a new branch named <code>&lt;new_branch&gt;</code> and start it at <code>&lt;start_point&gt;</code>; see <code><a href="/docs/linux/man/1-git-branch/">git-branch</a></code>(1) for details.</dl>
<p> -B &lt;new_branch&gt;</p>
<dl>
<dt>
<dd> Creates the branch <code>&lt;new_branch&gt;</code> and start it at <code>&lt;start_point&gt;</code>; if it already exists, then reset it to <code>&lt;start_point&gt;</code>. This is equivalent to running &quot;git branch&quot; with &quot;-f&quot;; see <code><a href="/docs/linux/man/1-git-branch/">git-branch</a></code>(1) for details.</dl>
<p> -t, &#8211;track</p>
<dl>
<dt>
<dd> When creating a new branch, set up &quot;upstream&quot; configuration. See &quot;&#8211;track&quot; in <code><a href="/docs/linux/man/1-git-branch/">git-branch</a></code>(1) for details. </p>
<p> If no <code>-b</code> option is given, the name of the new branch will be derived from the remote-tracking branch, by looking at the local part of the refspec configured for the corresponding remote, and then stripping the initial part up to the &quot;*&quot;. This would tell us to use <code>hack</code> as the local branch when branching off of <code>origin/hack</code> (or <code>remotes/origin/hack</code>, or even <code>refs/remotes/origin/hack</code>). If the given name has no slash, or the above guessing results in an empty name, the guessing is aborted. You can explicitly give a name with <code>-b</code> in such a case.</dl>
<p> &#8211;no-track</p>
<dl>
<dt>
<dd> Do not set up &quot;upstream&quot; configuration, even if the <code>branch.autoSetupMerge</code> configuration variable is true.</dl>
<p> &#8211;guess, &#8211;no-guess</p>
<dl>
<dt>
<dd> If <code>&lt;branch&gt;</code> is not found but there does exist a tracking branch in exactly one remote (call it <code>&lt;remote&gt;</code>) with a matching name, treat as equivalent to </p>
<dl>
<dt>
<dd>
<pre>
$ git checkout -b &lt;branch&gt; --track &lt;remote&gt;/&lt;branch&gt;
</pre>
</dl>
<p> If the branch exists in multiple remotes and one of them is named by the <code>checkout.defaultRemote</code> configuration variable, we&#8217;ll use that one for the purposes of disambiguation, even if the <code>&lt;branch&gt;</code> isn&#8217;t unique across all remotes. Set it to e.g. <code>checkout.defaultRemote=origin</code> to always checkout remote branches from there if <code>&lt;branch&gt;</code> is ambiguous but exists on the <i>origin</i> remote. See also <code>checkout.defaultRemote</code> in <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1). </p>
<p> <code>&#8211;guess</code> is the default behavior. Use <code>&#8211;no-guess</code> to disable it. </p>
<p> The default behavior can be set via the <code>checkout.guess</code> configuration variable.</dl>
<p> -l</p>
<dl>
<dt>
<dd> Create the new branch&#8217;s reflog; see <code><a href="/docs/linux/man/1-git-branch/">git-branch</a></code>(1) for details.</dl>
<p> -d, &#8211;detach</p>
<dl>
<dt>
<dd> Rather than checking out a branch to work on it, check out a commit for inspection and discardable experiments. This is the default behavior of <code>git checkout &lt;commit&gt;</code> when <code>&lt;commit&gt;</code> is not a branch name. See the &quot;DETACHED HEAD&quot; section below for details.</dl>
<p> &#8211;orphan &lt;new_branch&gt;</p>
<dl>
<dt>
<dd> Create a new <i>orphan</i> branch, named <code>&lt;new_branch&gt;</code>, started from <code>&lt;start_point&gt;</code> and switch to it. The first commit made on this new branch will have no parents and it will be the root of a new history totally disconnected from all the other branches and commits. </p>
<p> The index and the working tree are adjusted as if you had previously run <code>git checkout &lt;start_point&gt;</code>. This allows you to start a new history that records a set of paths similar to <code>&lt;start_point&gt;</code> by easily running <code>git commit -a</code> to make the root commit. </p>
<p> This can be useful when you want to publish the tree from a commit without exposing its full history. You might want to do this to publish an open source branch of a project whose current tree is &quot;clean&quot;, but whose full history contains proprietary or otherwise encumbered bits of code. </p>
<p> If you want to start a disconnected history that records a set of paths that is totally different from the one of <code>&lt;start_point&gt;</code>, then you should clear the index and the working tree right after creating the orphan branch by running <code>git rm -rf .</code> from the top level of the working tree. Afterwards you will be ready to prepare your new files, repopulating the working tree, by copying them from elsewhere, extracting a tarball, etc.</dl>
<p> &#8211;ignore-skip-worktree-bits</p>
<dl>
<dt>
<dd> In sparse checkout mode, <code>git checkout &#8212; &lt;paths&gt;</code> would update only entries matched by <code>&lt;paths&gt;</code> and sparse patterns in <code>$GIT_DIR/info/sparse-checkout</code>. This option ignores the sparse patterns and adds back any files in <code>&lt;paths&gt;</code>.</dl>
<p> -m, &#8211;merge</p>
<dl>
<dt>
<dd> When switching branches, if you have local modifications to one or more files that are different between the current branch and the branch to which you are switching, the command refuses to switch branches in order to preserve your modifications in context. However, with this option, a three-way merge between the current branch, your working tree contents, and the new branch is done, and you will be on the new branch. </p>
<p> When a merge conflict happens, the index entries for conflicting paths are left unmerged, and you need to resolve the conflicts and mark the resolved paths with <code>git add</code> (or <code>git rm</code> if the merge should result in deletion of the path). </p>
<p> When checking out paths from the index, this option lets you recreate the conflicted merge in the specified paths. </p>
<p> When switching branches with <code>&#8211;merge</code>, staged changes may be lost.</dl>
<p> &#8211;conflict=&lt;style&gt;</p>
<dl>
<dt>
<dd> The same as <code>&#8211;merge</code> option above, but changes the way the conflicting hunks are presented, overriding the <code>merge.conflictStyle</code> configuration variable. Possible values are &quot;merge&quot; (default) and &quot;diff3&quot; (in addition to what is shown by &quot;merge&quot; style, shows the original contents).</dl>
<p> -p, &#8211;patch</p>
<dl>
<dt>
<dd> Interactively select hunks in the difference between the <code>&lt;tree-ish&gt;</code> (or the index, if unspecified) and the working tree. The chosen hunks are then applied in reverse to the working tree (and if a <code>&lt;tree-ish&gt;</code> was specified, the index). </p>
<p> This means that you can use <code>git checkout -p</code> to selectively discard edits from your current working tree. See the &#8220;Interactive Mode&#8221; section of <code><a href="/docs/linux/man/1-git-add/">git-add</a></code>(1) to learn how to operate the <code>&#8211;patch</code> mode. </p>
<p> Note that this option uses the no overlay mode by default (see also <code>&#8211;overlay</code>), and currently doesn&#8217;t support overlay mode.</dl>
<p> &#8211;ignore-other-worktrees</p>
<dl>
<dt>
<dd> <code>git checkout</code> refuses when the wanted ref is already checked out by another worktree. This option makes it check the ref out anyway. In other words, the ref can be held by more than one worktree.</dl>
<p> &#8211;overwrite-ignore, &#8211;no-overwrite-ignore</p>
<dl>
<dt>
<dd> Silently overwrite ignored files when switching branches. This is the default behavior. Use <code>&#8211;no-overwrite-ignore</code> to abort the operation when the new branch contains ignored files.</dl>
<p> &#8211;recurse-submodules, &#8211;no-recurse-submodules</p>
<dl>
<dt>
<dd> Using <code>&#8211;recurse-submodules</code> will update the content of all active submodules according to the commit recorded in the superproject. If local modifications in a submodule would be overwritten the checkout will fail unless <code>-f</code> is used. If nothing (or <code>&#8211;no-recurse-submodules</code>) is used, submodules working trees will not be updated. Just like <code><a href="/docs/linux/man/1-git-submodule/">git-submodule</a></code>(1), this will detach <code>HEAD</code> of the submodule.</dl>
<p> &#8211;overlay, &#8211;no-overlay</p>
<dl>
<dt>
<dd> In the default overlay mode, <code>git checkout</code> never removes files from the index or the working tree. When specifying <code>&#8211;no-overlay</code>, files that appear in the index and working tree, but not in <code>&lt;tree-ish&gt;</code> are removed, to make them match <code>&lt;tree-ish&gt;</code> exactly.</dl>
<p> &#8211;pathspec-from-file=&lt;file&gt;</p>
<dl>
<dt>
<dd> Pathspec is passed in <code>&lt;file&gt;</code> instead of commandline args. If <code>&lt;file&gt;</code> is exactly <code>&#8211;</code> then standard input is used. Pathspec elements are separated by LF or CR/LF. Pathspec elements can be quoted as explained for the configuration variable <code>core.quotePath</code> (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)). See also <code>&#8211;pathspec-file-nul</code> and global <code>&#8211;literal-pathspecs</code>.</dl>
<p> &#8211;pathspec-file-nul</p>
<dl>
<dt>
<dd> Only meaningful with <code>&#8211;pathspec-from-file</code>. Pathspec elements are separated with NUL character and all other characters are taken literally (including newlines and quotes).</dl>
<p> &lt;branch&gt;</p>
<dl>
<dt>
<dd> Branch to checkout; if it refers to a branch (i.e., a name that, when prepended with &quot;refs/heads/&quot;, is a valid ref), then that branch is checked out. Otherwise, if it refers to a valid commit, your <code>HEAD</code> becomes &quot;detached&quot; and you are no longer on any branch (see below for details). </p>
<p> You can use the <code>@{-N}</code> syntax to refer to the N-th last branch/commit checked out using &quot;git checkout&quot; operation. You may also specify <code>&#8211;</code> which is synonymous to <code>@{-1}</code>. </p>
<p> As a special case, you may use <code>A&#8230;B</code> as a shortcut for the merge base of <code>A</code> and <code>B</code> if there is exactly one merge base. You can leave out at most one of <code>A</code> and <code>B</code>, in which case it defaults to <code>HEAD</code>.</dl>
<p> &lt;new_branch&gt;</p>
<dl>
<dt>
<dd> Name for the new branch.</dl>
<p> &lt;start_point&gt;</p>
<dl>
<dt>
<dd> The name of a commit at which to start the new branch; see <code><a href="/docs/linux/man/1-git-branch/">git-branch</a></code>(1) for details. Defaults to <code>HEAD</code>. </p>
<p> As a special case, you may use <code>&quot;A&#8230;B&quot;</code> as a shortcut for the merge base of <code>A</code> and <code>B</code> if there is exactly one merge base. You can leave out at most one of <code>A</code> and <code>B</code>, in which case it defaults to <code>HEAD</code>.</dl>
<p> &lt;tree-ish&gt;</p>
<dl>
<dt>
<dd> Tree to checkout from (when paths are given). If not specified, the index will be used. </p>
<p> As a special case, you may use <code>&quot;A&#8230;B&quot;</code> as a shortcut for the merge base of <code>A</code> and <code>B</code> if there is exactly one merge base. You can leave out at most one of <code>A</code> and <code>B</code>, in which case it defaults to <code>HEAD</code>.</dl>
<p> &#8212;</p>
<dl>
<dt>
<dd> Do not interpret any more arguments as options.</dl>
<p> &lt;pathspec&gt;&#8230;</p>
<dl>
<dt>
<dd> Limits the paths affected by the operation. </p>
<p> For more details, see the <i>pathspec</i> entry in <code><a href="/docs/linux/man/7-gitglossary/">gitglossary</a></code>(7).</dl>
<h2>DETACHED HEAD</h2>
<p> <code>HEAD</code> normally refers to a named branch (e.g. <code>master</code>). Meanwhile, each branch refers to a specific commit. Let&#8217;s look at a repo with three commits, one of them tagged, and with branch <code>master</code> checked out: </p>
<dl>
<dt>
<dd>
<pre>
           HEAD (refers to branch 'master')
            |
            v
a---b---c  branch 'master' (refers to commit 'c')
    ^
    |
  tag 'v2.0' (refers to commit 'b')
</pre>
</dl>
<p> When a commit is created in this state, the branch is updated to refer to the new commit. Specifically, <i>git commit</i> creates a new commit <code>d</code>, whose parent is commit <code>c</code>, and then updates branch <code>master</code> to refer to new commit <code>d</code>. <code>HEAD</code> still refers to branch <code>master</code> and so indirectly now refers to commit <code>d</code>: </p>
<dl>
<dt>
<dd>
$ edit;<br />
git add;<br />
git commit<br />
    HEAD(refers to branch &#8216;master&#8217;) |<br />
    v<br />
            a&#8211; &#8211;<br />
            b&#8211; &#8211; c&#8211; &#8211; d branch &#8216;master'(refers to commit &#8216;d&#8217;) ^<br />
    |<br />
    tag &#8216;v2.0&#8242;(refers to commit &#8216;b&#8217;)
</dl>
<p> It is sometimes useful to be able to checkout a commit that is not at the tip of any named branch, or even to create a new commit that is not referenced by a named branch. Let&#8217;s look at what happens when we checkout commit <code>b</code> (here we show two ways this may be done): </p>
<dl>
<dt>
<dd>
<pre>
$ git checkout v2.0  # or
$ git checkout master^^
   HEAD (refers to commit 'b')
    |
    v
a---b---c---d  branch 'master' (refers to commit 'd')
    ^
    |
  tag 'v2.0' (refers to commit 'b')
</pre>
</dl>
<p> Notice that regardless of which checkout command we use, <code>HEAD</code> now refers directly to commit <code>b</code>. This is known as being in detached <code>HEAD</code> state. It means simply that <code>HEAD</code> refers to a specific commit, as opposed to referring to a named branch. Let&#8217;s see what happens when we create a commit: </p>
<dl>
<dt>
<dd>
$ edit;<br />
git add;<br />
git commit<br />
    HEAD(refers to commit &#8216;e&#8217;) |<br />
    v<br />
                e<br />
                /<br />
                a&#8211; &#8211;<br />
            b&#8211; &#8211; c&#8211; &#8211; d branch &#8216;master'(refers to commit &#8216;d&#8217;) ^<br />
    |<br />
    tag &#8216;v2.0&#8242;(refers to commit &#8216;b&#8217;)
</dl>
<p> There is now a new commit <code>e</code>, but it is referenced only by <code>HEAD</code>. We can of course add yet another commit in this state: </p>
<dl>
<dt>
<dd>
$ edit;<br />
git add;<br />
git commit<br />
    HEAD(refers to commit &#8216;f&#8217;) |<br />
    v<br />
            e&#8211; &#8211;<br />
            f<br />
                /<br />
                a&#8211; &#8211;<br />
            b&#8211; &#8211; c&#8211; &#8211; d branch &#8216;master'(refers to commit &#8216;d&#8217;) ^<br />
    |<br />
    tag &#8216;v2.0&#8242;(refers to commit &#8216;b&#8217;)
</dl>
<p> In fact, we can perform all the normal Git operations. But, let&#8217;s look at what happens when we then checkout <code>master</code>: </p>
<dl>
<dt>
<dd>
<pre><code>
$ git checkout master
        HEAD(refers to branch 'master')
            e-- -
        f
    |
    / v
                a-- -
            b-- - c-- - d branch 'master'(refers to commit 'd') ^
    |
    tag 'v2.0'(refers to commit 'b')
</code></pre>
</dl>
<p> It is important to realize that at this point nothing refers to commit <code>f</code>. Eventually commit <code>f</code> (and by extension commit <code>e</code>) will be deleted by the routine Git garbage collection process, unless we create a reference before that happens. If we have not yet moved away from commit <code>f</code>, any of these will create a reference to it: </p>
<dl>
<dt>
<dd>
<pre>
$ git checkout -b foo   <code>(1)</code>
$ git branch foo        <code>(2)</code>
$ git tag foo           <code>(3)</code>
</pre>
</dl>
<p> <code>1. </code>creates a new branch <code>foo</code>, which refers to commit <code>f</code>, and then updates <code>HEAD</code> to refer to branch <code>foo</code>. In other words, we&#8217;ll no longer be in detached <code>HEAD</code> state after this command.<br />
 <code>2. </code>similarly creates a new branch <code>foo</code>, which refers to commit <code>f</code>, but leaves <code>HEAD</code> detached.<br />
 <code>3. </code>creates a new tag <code>foo</code>, which refers to commit <code>f</code>, leaving <code>HEAD</code> detached. </p>
<p> If we have moved away from commit <code>f</code>, then we must first recover its object name (typically by using git reflog), and then we can create a reference to it. For example, to see the last two commits to which <code>HEAD</code> referred, we can use either of these commands: </p>
<dl>
<dt>
<dd>
<pre>
$ git reflog -2 HEAD # or
$ git log -g -2 HEAD
</pre>
</dl>
<h2>ARGUMENT DISAMBIGUATION</h2>
<p> When there is only one argument given and it is not <code>&#8212;</code> (e.g. <code>git checkout abc</code>), and when the argument is both a valid <code>&lt;tree-ish&gt;</code> (e.g. a branch <code>abc</code> exists) and a valid <code>&lt;pathspec&gt;</code> (e.g. a file or a directory whose name is &quot;abc&quot; exists), Git would usually ask you to disambiguate. Because checking out a branch is so common an operation, however, <code>git checkout abc</code> takes &quot;abc&quot; as a <code>&lt;tree-ish&gt;</code> in such a situation. Use <code>git checkout &#8212; &lt;pathspec&gt;</code> if you want to checkout these paths out of the index.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd> 1. The following sequence checks out the <code>master</code> branch, reverts the <code>Makefile</code> to two revisions back, deletes <code>hello.c</code> by mistake, and gets it back from the index. </p>
<dl>
<dt>
<dd>
<pre>
$ git checkout master             <code>(1)</code>
$ git checkout master~2 Makefile  <code>(2)</code>
$ rm -f hello.c
$ git checkout hello.c            <code>(3)</code>
</pre>
</dl>
<p> <code>1. </code>switch branch<br />
 <code>2. </code>take a file out of another commit<br />
 <code>3. </code>restore <code>hello.c</code> from the index </p>
<p> If you want to check out <i>all</i> C source files out of the index, you can say </p>
<dl>
<dt>
<dd>
<pre>
$ git checkout -- '*.c'
</pre>
</dl>
<p> Note the quotes around <code>*.c</code>. The file <code>hello.c</code> will also be checked out, even though it is no longer in the working tree, because the file globbing is used to match entries in the index (not in the working tree by the shell). </p>
<p> If you have an unfortunate branch that is named <code>hello.c</code>, this step would be confused as an instruction to switch to that branch. You should instead write: </p>
<dl>
<dt>
<dd>
<pre>
$ git checkout -- hello.c
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> 2. After working in the wrong branch, switching to the correct branch would be done using: </p>
<dl>
<dt>
<dd>
<pre>
$ git checkout mytopic
</pre>
</dl>
<p> However, your &quot;wrong&quot; branch and correct <code>mytopic</code> branch may differ in files that you have modified locally, in which case the above checkout would fail like this: </p>
<dl>
<dt>
<dd>
<pre>
$ git checkout mytopic
error: You have local changes to 'frotz'; not switching branches.
</pre>
</dl>
<p> You can give the <code>-m</code> flag to the command, which would try a three-way merge: </p>
<dl>
<dt>
<dd>
<pre>
$ git checkout -m mytopic
Auto-merging frotz
</pre>
</dl>
<p> After this three-way merge, the local modifications are <i>not</i> registered in your index file, so <code>git diff</code> would show you what changes you made since the tip of the new branch.</dl>
<dl>
<dt>
<dd> 3. When a merge conflict happens during switching branches with the <code>-m</code> option, you would see something like this: </p>
<dl>
<dt>
<dd>
<pre>
$ git checkout -m mytopic
Auto-merging frotz
ERROR: Merge conflict in frotz
fatal: merge program failed
</pre>
</dl>
<p> At this point, <code>git diff</code> shows the changes cleanly merged as in the previous example, as well as the changes in the conflicted files. Edit and resolve the conflict and mark it resolved with <code>git add</code> as usual: </p>
<dl>
<dt>
<dd>
<pre>
$ edit frotz
$ git add frotz
</pre>
</dl>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-switch/">git-switch</a></code>(1), <code><a href="/docs/linux/man/1-git-restore/">git-restore</a></code>(1)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>

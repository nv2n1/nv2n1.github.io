---
title: "git-worktree(1)"
name: "git-worktree"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-worktree/"
description: "git-worktree – Manage multiple working trees"
---

<h2 class="name">NAME</h2>
<p> git-worktree &#8211; Manage multiple working trees </p>
<h2>SYNOPSIS</h2>
<pre><code>
git worktree add[-f][--detach][--checkout][--lock[--reason&lt;string&gt;]][-b&lt;new - branch&gt;]&lt;path&gt;[&lt;commit - ish&gt;] git worktree list[--porcelain] git worktree lock[--reason&lt;string&gt;]&lt;worktree&gt;
    git worktree move&lt;worktree&gt;&lt;new - path&gt;
        git worktree prune[-n][-v][--expire&lt;expire&gt;] git worktree remove[-f]&lt;worktree&gt;
            git worktree repair[&lt;path&gt;...] git worktree unlock&lt;worktree&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<p> Manage multiple working trees attached to the same repository. </p>
<p> A git repository can support multiple working trees, allowing you to check out more than one branch at a time. With <code>git worktree add</code> a new working tree is associated with the repository. This new working tree is called a &quot;linked working tree&quot; as opposed to the &quot;main working tree&quot; prepared by <code><a href="/docs/linux/man/1-git-init/">git-init</a></code>(1) or <code><a href="/docs/linux/man/1-git-clone/">git-clone</a></code>(1). A repository has one main working tree (if it&#8217;s not a bare repository) and zero or more linked working trees. When you are done with a linked working tree, remove it with <code>git worktree remove</code>. </p>
<p> In its simplest form, <code>git worktree add &lt;path&gt;</code> automatically creates a new branch whose name is the final component of <code>&lt;path&gt;</code>, which is convenient if you plan to work on a new topic. For instance, <code>git worktree add ../hotfix</code> creates new branch <code>hotfix</code> and checks it out at path <code>../hotfix</code>. To instead work on an existing branch in a new working tree, use <code>git worktree add &lt;path&gt; &lt;branch&gt;</code>. On the other hand, if you just plan to make some experimental changes or do testing without disturbing existing development, it is often convenient to create a <i>throwaway</i> working tree not associated with any branch. For instance, <code>git worktree add -d &lt;path&gt;</code> creates a new working tree with a detached <code>HEAD</code> at the same commit as the current branch. </p>
<p> If a working tree is deleted without using <code>git worktree remove</code>, then its associated administrative files, which reside in the repository (see &quot;DETAILS&quot; below), will eventually be removed automatically (see <code>gc.worktreePruneExpire</code> in <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)), or you can run <code>git worktree prune</code> in the main or any linked working tree to clean up any stale administrative files. </p>
<p> If a linked working tree is stored on a portable device or network share which is not always mounted, you can prevent its administrative files from being pruned by issuing the <code>git worktree lock</code> command, optionally specifying <code>&#8211;reason</code> to explain why the working tree is locked.</p>
<h2>COMMANDS</h2>
<p> add &lt;path&gt; [&lt;commit-ish&gt;]</p>
<dl>
<dt>
<dd> Create <code>&lt;path&gt;</code> and checkout <code>&lt;commit-ish&gt;</code> into it. The new working directory is linked to the current repository, sharing everything except working directory specific files such as <code>HEAD</code>, <code>index</code>, etc. As a convenience, <code>&lt;commit-ish&gt;</code> may be a bare &quot;<code>&#8211;</code>&quot;, which is synonymous with <code>@{-1}</code>. </p>
<p> If <code>&lt;commit-ish&gt;</code> is a branch name (call it <code>&lt;branch&gt;</code>) and is not found, and neither <code>-b</code> nor <code>-B</code> nor <code>&#8211;detach</code> are used, but there does exist a tracking branch in exactly one remote (call it <code>&lt;remote&gt;</code>) with a matching name, treat as equivalent to: </p>
<dl>
<dt>
<dd>
<pre>
$ git worktree add --track -b &lt;branch&gt; &lt;path&gt; &lt;remote&gt;/&lt;branch&gt;
</pre>
</dl>
<p> If the branch exists in multiple remotes and one of them is named by the <code>checkout.defaultRemote</code> configuration variable, we&#8217;ll use that one for the purposes of disambiguation, even if the <code>&lt;branch&gt;</code> isn&#8217;t unique across all remotes. Set it to e.g. <code>checkout.defaultRemote=origin</code> to always checkout remote branches from there if <code>&lt;branch&gt;</code> is ambiguous but exists on the <code>origin</code> remote. See also <code>checkout.defaultRemote</code> in <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1). </p>
<p> If <code>&lt;commit-ish&gt;</code> is omitted and neither <code>-b</code> nor <code>-B</code> nor <code>&#8211;detach</code> used, then, as a convenience, the new working tree is associated with a branch (call it <code>&lt;branch&gt;</code>) named after <code>$(basename &lt;path&gt;)</code>. If <code>&lt;branch&gt;</code> doesn&#8217;t exist, a new branch based on <code>HEAD</code> is automatically created as if <code>-b &lt;branch&gt;</code> was given. If <code>&lt;branch&gt;</code> does exist, it will be checked out in the new working tree, if it&#8217;s not checked out anywhere else, otherwise the command will refuse to create the working tree (unless <code>&#8211;force</code> is used).</dl>
<p> list</p>
<dl>
<dt>
<dd> List details of each working tree. The main working tree is listed first, followed by each of the linked working trees. The output details include whether the working tree is bare, the revision currently checked out, the branch currently checked out (or &quot;detached HEAD&quot; if none), &quot;locked&quot; if the worktree is locked, &quot;prunable&quot; if the worktree can be pruned by <code>prune</code> command.</dl>
<p> lock</p>
<dl>
<dt>
<dd> If a working tree is on a portable device or network share which is not always mounted, lock it to prevent its administrative files from being pruned automatically. This also prevents it from being moved or deleted. Optionally, specify a reason for the lock with <code>&#8211;reason</code>.</dl>
<p> move</p>
<dl>
<dt>
<dd> Move a working tree to a new location. Note that the main working tree or linked working trees containing submodules cannot be moved with this command. (The <code>git worktree repair</code> command, however, can reestablish the connection with linked working trees if you move the main working tree manually.)</dl>
<p> prune</p>
<dl>
<dt>
<dd> Prune working tree information in <code>$GIT_DIR/worktrees</code>.</dl>
<p> remove</p>
<dl>
<dt>
<dd> Remove a working tree. Only clean working trees (no untracked files and no modification in tracked files) can be removed. Unclean working trees or ones with submodules can be removed with <code>&#8211;force</code>. The main working tree cannot be removed.</dl>
<p> repair [&lt;path&gt;&#8230;]</p>
<dl>
<dt>
<dd> Repair working tree administrative files, if possible, if they have become corrupted or outdated due to external factors. </p>
<p> For instance, if the main working tree (or bare repository) is moved, linked working trees will be unable to locate it. Running <code>repair</code> in the main working tree will reestablish the connection from linked working trees back to the main working tree. </p>
<p> Similarly, if a linked working tree is moved without using <code>git worktree move</code>, the main working tree (or bare repository) will be unable to locate it. Running <code>repair</code> within the recently-moved working tree will reestablish the connection. If multiple linked working trees are moved, running <code>repair</code> from any working tree with each tree&#8217;s new <code>&lt;path&gt;</code> as an argument, will reestablish the connection to all the specified paths. </p>
<p> If both the main working tree and linked working trees have been moved manually, then running <code>repair</code> in the main working tree and specifying the new <code>&lt;path&gt;</code> of each linked working tree will reestablish all connections in both directions.</dl>
<p> unlock</p>
<dl>
<dt>
<dd> Unlock a working tree, allowing it to be pruned, moved or deleted.</dl>
<h2>OPTIONS</h2>
<p> -f, &#8211;force</p>
<dl>
<dt>
<dd> By default, <code>add</code> refuses to create a new working tree when <code>&lt;commit-ish&gt;</code> is a branch name and is already checked out by another working tree, or if <code>&lt;path&gt;</code> is already assigned to some working tree but is missing (for instance, if <code>&lt;path&gt;</code> was deleted manually). This option overrides these safeguards. To add a missing but locked working tree path, specify <code>&#8211;force</code> twice. </p>
<p> <code>move</code> refuses to move a locked working tree unless <code>&#8211;force</code> is specified twice. If the destination is already assigned to some other working tree but is missing (for instance, if <code>&lt;new-path&gt;</code> was deleted manually), then <code>&#8211;force</code> allows the move to proceed; use <code>&#8211;force</code> twice if the destination is locked. </p>
<p> <code>remove</code> refuses to remove an unclean working tree unless <code>&#8211;force</code> is used. To remove a locked working tree, specify <code>&#8211;force</code> twice.</dl>
<p> -b &lt;new-branch&gt;, -B &lt;new-branch&gt;</p>
<dl>
<dt>
<dd> With <code>add</code>, create a new branch named <code>&lt;new-branch&gt;</code> starting at <code>&lt;commit-ish&gt;</code>, and check out <code>&lt;new-branch&gt;</code> into the new working tree. If <code>&lt;commit-ish&gt;</code> is omitted, it defaults to <code>HEAD</code>. By default, <code>-b</code> refuses to create a new branch if it already exists. <code>-B</code> overrides this safeguard, resetting <code>&lt;new-branch&gt;</code> to <code>&lt;commit-ish&gt;</code>.</dl>
<p> -d, &#8211;detach</p>
<dl>
<dt>
<dd> With <code>add</code>, detach <code>HEAD</code> in the new working tree. See &quot;DETACHED HEAD&quot; in <code><a href="/docs/linux/man/1-git-checkout/">git-checkout</a></code>(1).</dl>
<p> &#8211;[no-]checkout</p>
<dl>
<dt>
<dd> By default, <code>add</code> checks out <code>&lt;commit-ish&gt;</code>, however, <code>&#8211;no-checkout</code> can be used to suppress checkout in order to make customizations, such as configuring sparse-checkout. See &quot;Sparse checkout&quot; in <code><a href="/docs/linux/man/1-git-read-tree/">git-read-tree</a></code>(1).</dl>
<p> &#8211;[no-]guess-remote</p>
<dl>
<dt>
<dd> With <code>worktree add &lt;path&gt;</code>, without <code>&lt;commit-ish&gt;</code>, instead of creating a new branch from <code>HEAD</code>, if there exists a tracking branch in exactly one remote matching the basename of <code>&lt;path&gt;</code>, base the new branch on the remote-tracking branch, and mark the remote-tracking branch as &quot;upstream&quot; from the new branch. </p>
<p> This can also be set up as the default behaviour by using the <code>worktree.guessRemote</code> config option.</dl>
<p> &#8211;[no-]track</p>
<dl>
<dt>
<dd> When creating a new branch, if <code>&lt;commit-ish&gt;</code> is a branch, mark it as &quot;upstream&quot; from the new branch. This is the default if <code>&lt;commit-ish&gt;</code> is a remote-tracking branch. See <code>&#8211;track</code> in <code><a href="/docs/linux/man/1-git-branch/">git-branch</a></code>(1) for details.</dl>
<p> &#8211;lock</p>
<dl>
<dt>
<dd> Keep the working tree locked after creation. This is the equivalent of <code>git worktree lock</code> after <code>git worktree add</code>, but without a race condition.</dl>
<p> -n, &#8211;dry-run</p>
<dl>
<dt>
<dd> With <code>prune</code>, do not remove anything; just report what it would remove.</dl>
<p> &#8211;porcelain</p>
<dl>
<dt>
<dd> With <code>list</code>, output in an easy-to-parse format for scripts. This format will remain stable across Git versions and regardless of user configuration. See below for details.</dl>
<p> -q, &#8211;quiet</p>
<dl>
<dt>
<dd> With <code>add</code>, suppress feedback messages.</dl>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
<dd> With <code>prune</code>, report all removals. </p>
<p> With <code>list</code>, output additional information about worktrees (see below).</dl>
<p> &#8211;expire &lt;time&gt;</p>
<dl>
<dt>
<dd> With <code>prune</code>, only expire unused working trees older than <code>&lt;time&gt;</code>. </p>
<p> With <code>list</code>, annotate missing working trees as prunable if they are older than <code>&lt;time&gt;</code>.</dl>
<p> &#8211;reason &lt;string&gt;</p>
<dl>
<dt>
<dd> With <code>lock</code> or with <code>add &#8211;lock</code>, an explanation why the working tree is locked.</dl>
<p> &lt;worktree&gt;</p>
<dl>
<dt>
<dd> Working trees can be identified by path, either relative or absolute. </p>
<p> If the last path components in the working tree&#8217;s path is unique among working trees, it can be used to identify a working tree. For example if you only have two working trees, at <code>/abc/def/ghi</code> and <code>/abc/def/ggg</code>, then <code>ghi</code> or <code>def/ghi</code> is enough to point to the former working tree.</dl>
<h2>REFS</h2>
<p> In multiple working trees, some refs may be shared between all working trees and some refs are local. One example is <code>HEAD</code> which is different for each working tree. This section is about the sharing rules and how to access refs of one working tree from another. </p>
<p> In general, all pseudo refs are per working tree and all refs starting with <code>refs/</code> are shared. Pseudo refs are ones like <code>HEAD</code> which are directly under <code>$GIT_DIR</code> instead of inside <code>$GIT_DIR/refs</code>. There are exceptions, however: refs inside <code>refs/bisect</code> and <code>refs/worktree</code> are not shared. </p>
<p> Refs that are per working tree can still be accessed from another working tree via two special paths, <code>main-worktree</code> and <code>worktrees</code>. The former gives access to per-working tree refs of the main working tree, while the latter to all linked working trees. </p>
<p> For example, <code>main-worktree/HEAD</code> or <code>main-worktree/refs/bisect/good</code> resolve to the same value as the main working tree&#8217;s <code>HEAD</code> and <code>refs/bisect/good</code> respectively. Similarly, <code>worktrees/foo/HEAD</code> or <code>worktrees/bar/refs/bisect/bad</code> are the same as <code>$GIT_COMMON_DIR/worktrees/foo/HEAD</code> and <code>$GIT_COMMON_DIR/worktrees/bar/refs/bisect/bad</code>. </p>
<p> To access refs, it&#8217;s best not to look inside <code>$GIT_DIR</code> directly. Instead use commands such as <code><a href="/docs/linux/man/1-git-rev-parse/">git-rev-parse</a></code>(1) or <code><a href="/docs/linux/man/1-git-update-ref/">git-update-ref</a></code>(1) which will handle refs correctly.</p>
<h2>CONFIGURATION FILE</h2>
<p> By default, the repository <code>config</code> file is shared across all working trees. If the config variables <code>core.bare</code> or <code>core.worktree</code> are already present in the config file, they will be applied to the main working trees only. </p>
<p> In order to have configuration specific to working trees, you can turn on the <code>worktreeConfig</code> extension, e.g.: </p>
<dl>
<dt>
<dd>
<pre>
$ git config extensions.worktreeConfig true
</pre>
</dl>
<p> In this mode, specific configuration stays in the path pointed by <code>git rev-parse &#8211;git-path config.worktree</code>. You can add or update configuration in this file with <code>git config &#8211;worktree</code>. Older Git versions will refuse to access repositories with this extension. </p>
<p> Note that in this file, the exception for <code>core.bare</code> and <code>core.worktree</code> is gone. If they exist in <code>$GIT_DIR/config</code>, you must move them to the <code>config.worktree</code> of the main working tree. You may also take this opportunity to review and move other configuration that you do not want to share to all working trees: </p>
<dl>
<dt>
<dd> &bull; <code>core.worktree</code> and <code>core.bare</code> should never be shared</dl>
<dl>
<dt>
<dd> &bull; <code>core.sparseCheckout</code> is recommended per working tree, unless you are sure you always use sparse checkout for all working trees.</dl>
<h2>DETAILS</h2>
<p> Each linked working tree has a private sub-directory in the repository&#8217;s <code>$GIT_DIR/worktrees</code> directory. The private sub-directory&#8217;s name is usually the base name of the linked working tree&#8217;s path, possibly appended with a number to make it unique. For example, when <code>$GIT_DIR=/path/main/.git</code> the command <code>git worktree add /path/other/test-next next</code> creates the linked working tree in <code>/path/other/test-next</code> and also creates a <code>$GIT_DIR/worktrees/test-next</code> directory (or <code>$GIT_DIR/worktrees/test-next1</code> if <code>test-next</code> is already taken). </p>
<p> Within a linked working tree, <code>$GIT_DIR</code> is set to point to this private directory (e.g. <code>/path/main/.git/worktrees/test-next</code> in the example) and <code>$GIT_COMMON_DIR</code> is set to point back to the main working tree&#8217;s <code>$GIT_DIR</code> (e.g. <code>/path/main/.git</code>). These settings are made in a <code>.git</code> file located at the top directory of the linked working tree. </p>
<p> Path resolution via <code>git rev-parse &#8211;git-path</code> uses either <code>$GIT_DIR</code> or <code>$GIT_COMMON_DIR</code> depending on the path. For example, in the linked working tree <code>git rev-parse &#8211;git-path HEAD</code> returns <code>/path/main/.git/worktrees/test-next/HEAD</code> (not <code>/path/other/test-next/.git/HEAD</code> or <code>/path/main/.git/HEAD</code>) while <code>git rev-parse &#8211;git-path refs/heads/master</code> uses <code>$GIT_COMMON_DIR</code> and returns <code>/path/main/.git/refs/heads/master</code>, since refs are shared across all working trees, except <code>refs/bisect</code> and <code>refs/worktree</code>. </p>
<p> See <code><a href="/docs/linux/man/5-gitrepository-layout/">gitrepository-layout</a></code>(5) for more information. The rule of thumb is do not make any assumption about whether a path belongs to <code>$GIT_DIR</code> or <code>$GIT_COMMON_DIR</code> when you need to directly access something inside <code>$GIT_DIR</code>. Use <code>git rev-parse &#8211;git-path</code> to get the final path. </p>
<p> If you manually move a linked working tree, you need to update the <code>gitdir</code> file in the entry&#8217;s directory. For example, if a linked working tree is moved to <code>/newpath/test-next</code> and its <code>.git</code> file points to <code>/path/main/.git/worktrees/test-next</code>, then update <code>/path/main/.git/worktrees/test-next/gitdir</code> to reference <code>/newpath/test-next</code> instead. Better yet, run <code>git worktree repair</code> to reestablish the connection automatically. </p>
<p> To prevent a <code>$GIT_DIR/worktrees</code> entry from being pruned (which can be useful in some situations, such as when the entry&#8217;s working tree is stored on a portable device), use the <code>git worktree lock</code> command, which adds a file named <code>locked</code> to the entry&#8217;s directory. The file contains the reason in plain text. For example, if a linked working tree&#8217;s <code>.git</code> file points to <code>/path/main/.git/worktrees/test-next</code> then a file named <code>/path/main/.git/worktrees/test-next/locked</code> will prevent the <code>test-next</code> entry from being pruned. See <code><a href="/docs/linux/man/5-gitrepository-layout/">gitrepository-layout</a></code>(5) for details. </p>
<p> When <code>extensions.worktreeConfig</code> is enabled, the config file <code>.git/worktrees/&lt;id&gt;/config.worktree</code> is read after <code>.git/config</code> is.</p>
<h2>LIST OUTPUT FORMAT</h2>
<p> The <code>worktree list</code> command has two output formats. The default format shows the details on a single line with columns. For example: </p>
<dl>
<dt>
<dd>
<pre>
$ git worktree list
/path/to/bare-source            (bare)
/path/to/linked-worktree        abcd1234 [master]
/path/to/other-linked-worktree  1234abc  (detached HEAD)
</pre>
</dl>
<p> The command also shows annotations for each working tree, according to its state. These annotations are: </p>
<dl>
<dt>
<dd> &bull; <code>locked</code>, if the working tree is locked.</dl>
<dl>
<dt>
<dd> &bull; <code>prunable</code>, if the working tree can be pruned via <code>git worktree prune</code>.</dl>
<dl>
<dt>
<dd>
<pre>
$ git worktree list
/path/to/linked-worktree    abcd1234 [master]
/path/to/locked-worktree    acbd5678 (brancha) locked
/path/to/prunable-worktree  5678abc  (detached HEAD) prunable
</pre>
</dl>
<p> For these annotations, a reason might also be available and this can be seen using the verbose mode. The annotation is then moved to the next line indented followed by the additional information. </p>
<dl>
<dt>
<dd>
<pre>
$ git worktree list --verbose
/path/to/linked-worktree              abcd1234 [master]
/path/to/locked-worktree-no-reason    abcd5678 (detached HEAD) locked
/path/to/locked-worktree-with-reason  1234abcd (brancha)
        locked: working tree path is mounted on a portable device
/path/to/prunable-worktree            5678abc1 (detached HEAD)
        prunable: gitdir file points to non-existent location
</pre>
</dl>
<p> Note that the annotation is moved to the next line if the additional information is available, otherwise it stays on the same line as the working tree itself.</p>
<h3>Porcelain Format</h3>
<p> The porcelain format has a line per attribute. Attributes are listed with a label and value separated by a single space. Boolean attributes (like <code>bare</code> and <code>detached</code>) are listed as a label only, and are present only if the value is true. Some attributes (like <code>locked</code>) can be listed as a label only or with a value depending upon whether a reason is available. The first attribute of a working tree is always <code>worktree</code>, an empty line indicates the end of the record. For example: </p>
<dl>
<dt>
<dd>
<pre>
$ git worktree list --porcelain
worktree /path/to/bare-source
bare
worktree /path/to/linked-worktree
HEAD abcd1234abcd1234abcd1234abcd1234abcd1234
branch refs/heads/master
worktree /path/to/other-linked-worktree
HEAD 1234abc1234abc1234abc1234abc1234abc1234a
detached
worktree /path/to/linked-worktree-locked-no-reason
HEAD 5678abc5678abc5678abc5678abc5678abc5678c
branch refs/heads/locked-no-reason
locked
worktree /path/to/linked-worktree-locked-with-reason
HEAD 3456def3456def3456def3456def3456def3456b
branch refs/heads/locked-with-reason
locked reason why is locked
worktree /path/to/linked-worktree-prunable
HEAD 1233def1234def1234def1234def1234def1234b
detached
prunable gitdir file points to non-existent location
</pre>
</dl>
<p> If the lock reason contains &quot;unusual&quot; characters such as newline, they are escaped and the entire reason is quoted as explained for the configuration variable <code>core.quotePath</code> (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)). For Example: </p>
<dl>
<dt>
<dd>
<pre>
$ git worktree list --porcelain
...
locked &quot;reason
why is locked&quot;
...
</pre>
</dl>
<h2>EXAMPLES</h2>
<p> You are in the middle of a refactoring session and your boss comes in and demands that you fix something immediately. You might typically use <code><a href="/docs/linux/man/1-git-stash/">git-stash</a></code>(1) to store your changes away temporarily, however, your working tree is in such a state of disarray (with new, moved, and removed files, and other bits and pieces strewn around) that you don&#8217;t want to risk disturbing any of it. Instead, you create a temporary linked working tree to make the emergency fix, remove it when done, and then resume your earlier refactoring session. </p>
<dl>
<dt>
<dd>
<pre>
$ git worktree add -b emergency-fix ../temp master
$ pushd ../temp
# ... hack hack hack ...
$ git commit -a -m 'emergency fix for boss'
$ popd
$ git worktree remove ../temp
</pre>
</dl>
<h2>BUGS</h2>
<p> Multiple checkout in general is still experimental, and the support for submodules is incomplete. It is NOT recommended to make multiple checkouts of a superproject.</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>

---
title: "git-stash(1)"
name: "git-stash"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-stash/"
description: "git-stash – Stash the changes in a dirty working directory away"
---

<h2 class="name">NAME</h2>
<p> git-stash &#8211; Stash the changes in a dirty working directory away </p>
<h2>SYNOPSIS</h2>
<pre><code>
git stash list[&lt;log - options&gt;] git stash show[-u | --include - untracked | --only - untracked][&lt;diff - options&gt;][&lt;stash&gt;] git stash drop[-q | --quiet][&lt;stash&gt;] git stash(pop | apply)[--index][-q | --quiet][&lt;stash&gt;] git stash branch&lt;branchname&gt;[&lt;stash&gt;] git stash[push[-p | --patch][-k | --[no - ] keep - index][-q | --quiet]
                                                                                                                                                                                                                                                                            [-u | --include - untracked][-a | --all][-m | --message&lt;message&gt;]
                                                                                                                                                                                                                                                                            [--pathspec - from - file = &lt;file&gt;[--pathspec - file - nul]]
                                                                                                                                                                                                                                                                            [--][&lt;pathspec&gt;...]] git stash clear
    git stash create[&lt;message&gt;] git stash store[-m | --message&lt;message&gt;][-q | --quiet]&lt;commit&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<p> Use <code>git stash</code> when you want to record the current state of the working directory and the index, but want to go back to a clean working directory. The command saves your local modifications away and reverts the working directory to match the <code>HEAD</code> commit. </p>
<p> The modifications stashed away by this command can be listed with <code>git stash list</code>, inspected with <code>git stash show</code>, and restored (potentially on top of a different commit) with <code>git stash apply</code>. Calling <code>git stash</code> without any arguments is equivalent to <code>git stash push</code>. A stash is by default listed as &quot;WIP on <i>branchname</i> &#8230;&quot;, but you can give a more descriptive message on the command line when you create one. </p>
<p> The latest stash you created is stored in <code>refs/stash</code>; older stashes are found in the reflog of this reference and can be named using the usual reflog syntax (e.g. <code>stash@{0}</code> is the most recently created stash, <code>stash@{1}</code> is the one before it, <code>stash@{2.hours.ago}</code> is also possible). Stashes may also be referenced by specifying just the stash index (e.g. the integer <code>n</code> is equivalent to <code>stash@{n}</code>).</p>
<h2>COMMANDS</h2>
<p> push [-p|&#8211;patch] [-k|&#8211;[no-]keep-index] [-u|&#8211;include-untracked] [-a|&#8211;all] [-q|&#8211;quiet] [-m|&#8211;message &lt;message&gt;] [&#8211;pathspec-from-file=&lt;file&gt; [&#8211;pathspec-file-nul]] [&#8211;] [&lt;pathspec&gt;&#8230;]</p>
<dl>
<dt>
<dd> Save your local modifications to a new <i>stash entry</i> and roll them back to HEAD (in the working tree and in the index). The &lt;message&gt; part is optional and gives the description along with the stashed state. </p>
<p> For quickly making a snapshot, you can omit &quot;push&quot;. In this mode, non-option arguments are not allowed to prevent a misspelled subcommand from making an unwanted stash entry. The two exceptions to this are <code>stash -p</code> which acts as alias for <code>stash push -p</code> and pathspec elements, which are allowed after a double hyphen <code>&#8212;</code> for disambiguation.</dl>
<p> save [-p|&#8211;patch] [-k|&#8211;[no-]keep-index] [-u|&#8211;include-untracked] [-a|&#8211;all] [-q|&#8211;quiet] [&lt;message&gt;]</p>
<dl>
<dt>
<dd> This option is deprecated in favour of <i>git stash push</i>. It differs from &quot;stash push&quot; in that it cannot take pathspec. Instead, all non-option arguments are concatenated to form the stash message.</dl>
<p> list [&lt;log-options&gt;]</p>
<dl>
<dt>
<dd> List the stash entries that you currently have. Each <i>stash entry</i> is listed with its name (e.g. <code>stash@{0}</code> is the latest entry, <code>stash@{1}</code> is the one before, etc.), the name of the branch that was current when the entry was made, and a short description of the commit the entry was based on. </p>
<dl>
<dt>
<dd>
stash @{0} : WIP on submit : 6ebd0e2&#8230; Update git &#8211; stash documentation stash @{1} : On master : 9cc0589&#8230; Add git &#8211; stash
</dl>
<p> The command takes options applicable to the <i>git log</i> command to control what is shown and how. See <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1).</dl>
<p> show [-u|&#8211;include-untracked|&#8211;only-untracked] [&lt;diff-options&gt;] [&lt;stash&gt;]</p>
<dl>
<dt>
<dd> Show the changes recorded in the stash entry as a diff between the stashed contents and the commit back when the stash entry was first created. By default, the command shows the diffstat, but it will accept any format known to <i>git diff</i> (e.g., <code>git stash show -p stash@{1}</code> to view the second most recent entry in patch form). If no <code>&lt;diff-option&gt;</code> is provided, the default behavior will be given by the <code>stash.showStat</code>, and <code>stash.showPatch</code> config variables. You can also use <code>stash.showIncludeUntracked</code> to set whether <code>&#8211;include-untracked</code> is enabled by default.</dl>
<p> pop [&#8211;index] [-q|&#8211;quiet] [&lt;stash&gt;]</p>
<dl>
<dt>
<dd> Remove a single stashed state from the stash list and apply it on top of the current working tree state, i.e., do the inverse operation of <code>git stash push</code>. The working directory must match the index. </p>
<p> Applying the state can fail with conflicts; in this case, it is not removed from the stash list. You need to resolve the conflicts by hand and call <code>git stash drop</code> manually afterwards.</dl>
<p> apply [&#8211;index] [-q|&#8211;quiet] [&lt;stash&gt;]</p>
<dl>
<dt>
<dd> Like <code>pop</code>, but do not remove the state from the stash list. Unlike <code>pop</code>, <code>&lt;stash&gt;</code> may be any commit that looks like a commit created by <code>stash push</code> or <code>stash create</code>.</dl>
<p> branch &lt;branchname&gt; [&lt;stash&gt;]</p>
<dl>
<dt>
<dd> Creates and checks out a new branch named <code>&lt;branchname&gt;</code> starting from the commit at which the <code>&lt;stash&gt;</code> was originally created, applies the changes recorded in <code>&lt;stash&gt;</code> to the new working tree and index. If that succeeds, and <code>&lt;stash&gt;</code> is a reference of the form <code>stash@{&lt;revision&gt;}</code>, it then drops the <code>&lt;stash&gt;</code>. </p>
<p> This is useful if the branch on which you ran <code>git stash push</code> has changed enough that <code>git stash apply</code> fails due to conflicts. Since the stash entry is applied on top of the commit that was HEAD at the time <code>git stash</code> was run, it restores the originally stashed state with no conflicts.</dl>
<p> clear</p>
<dl>
<dt>
<dd> Remove all the stash entries. Note that those entries will then be subject to pruning, and may be impossible to recover (see <i>Examples</i> below for a possible strategy).</dl>
<p> drop [-q|&#8211;quiet] [&lt;stash&gt;]</p>
<dl>
<dt>
<dd> Remove a single stash entry from the list of stash entries.</dl>
<p> create</p>
<dl>
<dt>
<dd> Create a stash entry (which is a regular commit object) and return its object name, without storing it anywhere in the ref namespace. This is intended to be useful for scripts. It is probably not the command you want to use; see &quot;push&quot; above.</dl>
<p> store</p>
<dl>
<dt>
<dd> Store a given stash created via <i>git stash create</i> (which is a dangling merge commit) in the stash ref, updating the stash reflog. This is intended to be useful for scripts. It is probably not the command you want to use; see &quot;push&quot; above.</dl>
<h2>OPTIONS</h2>
<p> -a, &#8211;all</p>
<dl>
<dt>
<dd> This option is only valid for <code>push</code> and <code>save</code> commands. </p>
<p> All ignored and untracked files are also stashed and then cleaned up with <code>git clean</code>.</dl>
<p> -u, &#8211;include-untracked, &#8211;no-include-untracked</p>
<dl>
<dt>
<dd> When used with the <code>push</code> and <code>save</code> commands, all untracked files are also stashed and then cleaned up with <code>git clean</code>. </p>
<p> When used with the <code>show</code> command, show the untracked files in the stash entry as part of the diff.</dl>
<p> &#8211;only-untracked</p>
<dl>
<dt>
<dd> This option is only valid for the <code>show</code> command. </p>
<p> Show only the untracked files in the stash entry as part of the diff.</dl>
<p> &#8211;index</p>
<dl>
<dt>
<dd> This option is only valid for <code>pop</code> and <code>apply</code> commands. </p>
<p> Tries to reinstate not only the working tree&#8217;s changes, but also the index&#8217;s ones. However, this can fail, when you have conflicts (which are stored in the index, where you therefore can no longer apply the changes as they were originally).</dl>
<p> -k, &#8211;keep-index, &#8211;no-keep-index</p>
<dl>
<dt>
<dd> This option is only valid for <code>push</code> and <code>save</code> commands. </p>
<p> All changes already added to the index are left intact.</dl>
<p> -p, &#8211;patch</p>
<dl>
<dt>
<dd> This option is only valid for <code>push</code> and <code>save</code> commands. </p>
<p> Interactively select hunks from the diff between HEAD and the working tree to be stashed. The stash entry is constructed such that its index state is the same as the index state of your repository, and its worktree contains only the changes you selected interactively. The selected changes are then rolled back from your worktree. See the &#8220;Interactive Mode&#8221; section of <code><a href="/docs/linux/man/1-git-add/">git-add</a></code>(1) to learn how to operate the <code>&#8211;patch</code> mode. </p>
<p> The <code>&#8211;patch</code> option implies <code>&#8211;keep-index</code>. You can use <code>&#8211;no-keep-index</code> to override this.</dl>
<p> &#8211;pathspec-from-file=&lt;file&gt;</p>
<dl>
<dt>
<dd> This option is only valid for <code>push</code> command. </p>
<p> Pathspec is passed in <code>&lt;file&gt;</code> instead of commandline args. If <code>&lt;file&gt;</code> is exactly <code>&#8211;</code> then standard input is used. Pathspec elements are separated by LF or CR/LF. Pathspec elements can be quoted as explained for the configuration variable <code>core.quotePath</code> (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)). See also <code>&#8211;pathspec-file-nul</code> and global <code>&#8211;literal-pathspecs</code>.</dl>
<p> &#8211;pathspec-file-nul</p>
<dl>
<dt>
<dd> This option is only valid for <code>push</code> command. </p>
<p> Only meaningful with <code>&#8211;pathspec-from-file</code>. Pathspec elements are separated with NUL character and all other characters are taken literally (including newlines and quotes).</dl>
<p> -q, &#8211;quiet</p>
<dl>
<dt>
<dd> This option is only valid for <code>apply</code>, <code>drop</code>, <code>pop</code>, <code>push</code>, <code>save</code>, <code>store</code> commands. </p>
<p> Quiet, suppress feedback messages.</dl>
<p> &#8212;</p>
<dl>
<dt>
<dd> This option is only valid for <code>push</code> command. </p>
<p> Separates pathspec from options for disambiguation purposes.</dl>
<p> &lt;pathspec&gt;&#8230;</p>
<dl>
<dt>
<dd> This option is only valid for <code>push</code> command. </p>
<p> The new stash entry records the modified states only for the files that match the pathspec. The index entries and working tree files are then rolled back to the state in HEAD only for these files, too, leaving files that do not match the pathspec intact. </p>
<p> For more details, see the <i>pathspec</i> entry in <code><a href="/docs/linux/man/7-gitglossary/">gitglossary</a></code>(7).</dl>
<p> &lt;stash&gt;</p>
<dl>
<dt>
<dd> This option is only valid for <code>apply</code>, <code>branch</code>, <code>drop</code>, <code>pop</code>, <code>show</code> commands. </p>
<p> A reference of the form <code>stash@{&lt;revision&gt;}</code>. When no <code>&lt;stash&gt;</code> is given, the latest stash is assumed (that is, <code>stash@{0}</code>).</dl>
<h2>DISCUSSION</h2>
<p> A stash entry is represented as a commit whose tree records the state of the working directory, and its first parent is the commit at <code>HEAD</code> when the entry was created. The tree of the second parent records the state of the index when the entry is made, and it is made a child of the <code>HEAD</code> commit. The ancestry graph looks like this: </p>
<dl>
<dt>
<dd>
.&#8211; &#8211;W / /<br />
    &#8212; &#8212; -H&#8211; &#8211;I
</dl>
<p> where <code>H</code> is the <code>HEAD</code> commit, <code>I</code> is a commit that records the state of the index, and <code>W</code> is a commit that records the state of the working tree.</p>
<h2>EXAMPLES</h2>
<p> Pulling into a dirty tree</p>
<dl>
<dt>
<dd> When you are in the middle of something, you learn that there are upstream changes that are possibly relevant to what you are doing. When your local changes do not conflict with the changes in the upstream, a simple <code>git pull</code> will let you move forward. </p>
<p> However, there are cases in which your local changes do conflict with the upstream changes, and <code>git pull</code> refuses to overwrite your changes. In such a case, you can stash your changes away, perform a pull, and then unstash, like this: </p>
<dl>
<dt>
<dd>
<pre>
$ git pull
 ...
file foobar not up to date, cannot merge.
$ git stash
$ git pull
$ git stash pop
</pre>
</dl>
</dl>
<p> Interrupted workflow</p>
<dl>
<dt>
<dd> When you are in the middle of something, your boss comes in and demands that you fix something immediately. Traditionally, you would make a commit to a temporary branch to store your changes away, and return to your original branch to make the emergency fix, like this: </p>
<dl>
<dt>
<dd>
#&#8230; hack hack hack&#8230;<br />
$ git switch &#8211; c my_wip $ git commit &#8211; a &#8211; m &#8220;WIP&#8221; $ git switch master $ edit emergency fix $ git commit &#8211; a &#8211; m &#8220;Fix in a hurry&#8221; $ git switch my_wip $ git reset&#8211; soft HEAD ^<br />
#&#8230; continue hacking&#8230;
</dl>
<p> You can use <i>git stash</i> to simplify the above, like this: </p>
<dl>
<dt>
<dd>
<pre>
# ... hack hack hack ...
$ git stash
$ edit emergency fix
$ git commit -a -m &quot;Fix in a hurry&quot;
$ git stash pop
# ... continue hacking ...
</pre>
</dl>
</dl>
<p> Testing partial commits</p>
<dl>
<dt>
<dd> You can use <code>git stash push &#8211;keep-index</code> when you want to make two or more commits out of the changes in the work tree, and you want to test each change before committing: </p>
<dl>
<dt>
<dd>
<pre>
# ... hack hack hack ...
$ git add --patch foo            # add just first part to the index
$ git stash push --keep-index    # save all other changes to the stash
$ edit/build/test first part
$ git commit -m 'First part'     # commit fully tested change
$ git stash pop                  # prepare to work on all other changes
# ... repeat above five steps until one commit remains ...
$ edit/build/test remaining parts
$ git commit foo -m 'Remaining parts'
</pre>
</dl>
</dl>
<p> Recovering stash entries that were cleared/dropped erroneously</p>
<dl>
<dt>
<dd> If you mistakenly drop or clear stash entries, they cannot be recovered through the normal safety mechanisms. However, you can try the following incantation to get a list of stash entries that are still in your repository, but not reachable any more: </p>
<dl>
<dt>
<dd>
<pre><code>
git fsck-- unreachable |
    grep commit | cut - d\ - f3 |
    xargs git log-- merges-- no - walk-- grep = WIP
</code></pre>
</dl>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-checkout/">git-checkout</a></code>(1), <code><a href="/docs/linux/man/1-git-commit/">git-commit</a></code>(1), <code><a href="/docs/linux/man/1-git-reflog/">git-reflog</a></code>(1), <code><a href="/docs/linux/man/1-git-reset/">git-reset</a></code>(1), <code><a href="/docs/linux/man/1-git-switch/">git-switch</a></code>(1)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>

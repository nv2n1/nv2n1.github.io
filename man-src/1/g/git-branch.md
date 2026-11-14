---
title: "git-branch(1)"
name: "git-branch"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-branch/"
description: "git-branch – List, create, or delete branches"
---

<h2 class="name">NAME</h2>
<p> git-branch &#8211; List, create, or delete branches </p>
<h2>SYNOPSIS</h2>
<pre><code>
git branch[--color[=&lt;when&gt;] | --no - color][--show - current]
          [-v[--abbrev = &lt;n&gt; | --no - abbrev]]
          [--column[=&lt;options&gt;] | --no - column][--sort = &lt;key&gt;]
          [--merged[&lt;commit&gt;]][--no - merged[&lt;commit&gt;]]
          [--contains[&lt;commit&gt;]][--no - contains[&lt;commit&gt;]]
          [--points - at&lt;object&gt;][--format = &lt;format&gt;]
          [(-r | --remotes) | (-a | --all)]
          [--list][&lt;pattern&gt;...] git branch[--track | --no - track][-f]&lt;branchname&gt;[&lt;start - point&gt;] git branch(--set - upstream - to = &lt;upstream&gt; | -u&lt;upstream&gt;)[&lt;branchname&gt;] git branch-- unset
    - upstream[&lt;branchname&gt;] git branch(-m | -M)[&lt;oldbranch&gt;]&lt;newbranch&gt; git branch(-c | -C)[&lt;oldbranch&gt;]&lt;newbranch&gt; git branch(-d | -D)[-r]&lt;branchname&gt;... git branch-- edit - description[&lt;branchname&gt;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> If <code>&#8211;list</code> is given, or if there are no non-option arguments, existing branches are listed; the current branch will be highlighted in green and marked with an asterisk. Any branches checked out in linked worktrees will be highlighted in cyan and marked with a plus sign. Option <code>-r</code> causes the remote-tracking branches to be listed, and option <code>-a</code> shows both local and remote branches. </p>
<p> If a <code>&lt;pattern&gt;</code> is given, it is used as a shell wildcard to restrict the output to matching branches. If multiple patterns are given, a branch is shown if it matches any of the patterns. </p>
<p> Note that when providing a <code>&lt;pattern&gt;</code>, you must use <code>&#8211;list</code>; otherwise the command may be interpreted as branch creation. </p>
<p> With <code>&#8211;contains</code>, shows only the branches that contain the named commit (in other words, the branches whose tip commits are descendants of the named commit), <code>&#8211;no-contains</code> inverts it. With <code>&#8211;merged</code>, only branches merged into the named commit (i.e. the branches whose tip commits are reachable from the named commit) will be listed. With <code>&#8211;no-merged</code> only branches not merged into the named commit will be listed. If the &lt;commit&gt; argument is missing it defaults to <code>HEAD</code> (i.e. the tip of the current branch). </p>
<p> The command&#8217;s second form creates a new branch head named &lt;branchname&gt; which points to the current <code>HEAD</code>, or &lt;start-point&gt; if given. As a special case, for &lt;start-point&gt;, you may use <code>&quot;A&#8230;B&quot;</code> as a shortcut for the merge base of <code>A</code> and <code>B</code> if there is exactly one merge base. You can leave out at most one of <code>A</code> and <code>B</code>, in which case it defaults to <code>HEAD</code>. </p>
<p> Note that this will create the new branch, but it will not switch the working tree to it; use &quot;git switch &lt;newbranch&gt;&quot; to switch to the new branch. </p>
<p> When a local branch is started off a remote-tracking branch, Git sets up the branch (specifically the <code>branch.&lt;name&gt;.remote</code> and <code>branch.&lt;name&gt;.merge</code> configuration entries) so that <i>git pull</i> will appropriately merge from the remote-tracking branch. This behavior may be changed via the global <code>branch.autoSetupMerge</code> configuration flag. That setting can be overridden by using the <code>&#8211;track</code> and <code>&#8211;no-track</code> options, and changed later using <code>git branch &#8211;set-upstream-to</code>. </p>
<p> With a <code>-m</code> or <code>-M</code> option, &lt;oldbranch&gt; will be renamed to &lt;newbranch&gt;. If &lt;oldbranch&gt; had a corresponding reflog, it is renamed to match &lt;newbranch&gt;, and a reflog entry is created to remember the branch renaming. If &lt;newbranch&gt; exists, -M must be used to force the rename to happen. </p>
<p> The <code>-c</code> and <code>-C</code> options have the exact same semantics as <code>-m</code> and <code>-M</code>, except instead of the branch being renamed, it will be copied to a new name, along with its config and reflog. </p>
<p> With a <code>-d</code> or <code>-D</code> option, <code>&lt;branchname&gt;</code> will be deleted. You may specify more than one branch for deletion. If the branch currently has a reflog then the reflog will also be deleted. </p>
<p> Use <code>-r</code> together with <code>-d</code> to delete remote-tracking branches. Note, that it only makes sense to delete remote-tracking branches if they no longer exist in the remote repository or if <i>git fetch</i> was configured not to fetch them again. See also the <i>prune</i> subcommand of <code><a href="/docs/linux/man/1-git-remote/">git-remote</a></code>(1) for a way to clean up all obsolete remote-tracking branches.</p>
<h2>OPTIONS</h2>
<p> -d, &#8211;delete</p>
<dl>
<dt>
<dd> Delete a branch. The branch must be fully merged in its upstream branch, or in <code>HEAD</code> if no upstream was set with <code>&#8211;track</code> or <code>&#8211;set-upstream-to</code>.</dl>
<p> -D</p>
<dl>
<dt>
<dd> Shortcut for <code>&#8211;delete &#8211;force</code>.</dl>
<p> &#8211;create-reflog</p>
<dl>
<dt>
<dd> Create the branch&#8217;s reflog. This activates recording of all changes made to the branch ref, enabling use of date based sha1 expressions such as &quot;&lt;branchname&gt;@{yesterday}&quot;. Note that in non-bare repositories, reflogs are usually enabled by default by the <code>core.logAllRefUpdates</code> config option. The negated form <code>&#8211;no-create-reflog</code> only overrides an earlier <code>&#8211;create-reflog</code>, but currently does not negate the setting of <code>core.logAllRefUpdates</code>.</dl>
<p> -f, &#8211;force</p>
<dl>
<dt>
<dd> Reset &lt;branchname&gt; to &lt;startpoint&gt;, even if &lt;branchname&gt; exists already. Without <code>-f</code>, <i>git branch</i> refuses to change an existing branch. In combination with <code>-d</code> (or <code>&#8211;delete</code>), allow deleting the branch irrespective of its merged status, or whether it even points to a valid commit. In combination with <code>-m</code> (or <code>&#8211;move</code>), allow renaming the branch even if the new branch name already exists, the same applies for <code>-c</code> (or <code>&#8211;copy</code>).</dl>
<p> -m, &#8211;move</p>
<dl>
<dt>
<dd> Move/rename a branch, together with its config and reflog.</dl>
<p> -M</p>
<dl>
<dt>
<dd> Shortcut for <code>&#8211;move &#8211;force</code>.</dl>
<p> -c, &#8211;copy</p>
<dl>
<dt>
<dd> Copy a branch, together with its config and reflog.</dl>
<p> -C</p>
<dl>
<dt>
<dd> Shortcut for <code>&#8211;copy &#8211;force</code>.</dl>
<p> &#8211;color[=&lt;when&gt;]</p>
<dl>
<dt>
<dd> Color branches to highlight current, local, and remote-tracking branches. The value must be always (the default), never, or auto.</dl>
<p> &#8211;no-color</p>
<dl>
<dt>
<dd> Turn off branch colors, even when the configuration file gives the default to color output. Same as <code>&#8211;color=never</code>.</dl>
<p> -i, &#8211;ignore-case</p>
<dl>
<dt>
<dd> Sorting and filtering branches are case insensitive.</dl>
<p> &#8211;column[=&lt;options&gt;], &#8211;no-column</p>
<dl>
<dt>
<dd> Display branch listing in columns. See configuration variable <code>column.branch</code> for option syntax. <code>&#8211;column</code> and <code>&#8211;no-column</code> without options are equivalent to <i>always</i> and <i>never</i> respectively. </p>
<p> This option is only applicable in non-verbose mode.</dl>
<p> -r, &#8211;remotes</p>
<dl>
<dt>
<dd> List or delete (if used with -d) the remote-tracking branches. Combine with <code>&#8211;list</code> to match the optional pattern(s).</dl>
<p> -a, &#8211;all</p>
<dl>
<dt>
<dd> List both remote-tracking branches and local branches. Combine with <code>&#8211;list</code> to match optional pattern(s).</dl>
<p> -l, &#8211;list</p>
<dl>
<dt>
<dd> List branches. With optional <code>&lt;pattern&gt;&#8230;</code>, e.g. <code>git branch &#8211;list &#8216;maint-*&#8217;</code>, list only the branches that match the pattern(s).</dl>
<p> &#8211;show-current</p>
<dl>
<dt>
<dd> Print the name of the current branch. In detached HEAD state, nothing is printed.</dl>
<p> -v, -vv, &#8211;verbose</p>
<dl>
<dt>
<dd> When in list mode, show sha1 and commit subject line for each head, along with relationship to upstream branch (if any). If given twice, print the path of the linked worktree (if any) and the name of the upstream branch, as well (see also <code>git remote show &lt;remote&gt;</code>). Note that the current worktree&#8217;s HEAD will not have its path printed (it will always be your current directory).</dl>
<p> -q, &#8211;quiet</p>
<dl>
<dt>
<dd> Be more quiet when creating or deleting a branch, suppressing non-error messages.</dl>
<p> &#8211;abbrev=&lt;n&gt;</p>
<dl>
<dt>
<dd> In the verbose listing that show the commit object name, show the shortest prefix that is at least <i>&lt;n&gt;</i> hexdigits long that uniquely refers the object. The default value is 7 and can be overridden by the <code>core.abbrev</code> config option.</dl>
<p> &#8211;no-abbrev</p>
<dl>
<dt>
<dd> Display the full sha1s in the output listing rather than abbreviating them.</dl>
<p> -t, &#8211;track</p>
<dl>
<dt>
<dd> When creating a new branch, set up <code>branch.&lt;name&gt;.remote</code> and <code>branch.&lt;name&gt;.merge</code> configuration entries to mark the start-point branch as &quot;upstream&quot; from the new branch. This configuration will tell git to show the relationship between the two branches in <code>git status</code> and <code>git branch -v</code>. Furthermore, it directs <code>git pull</code> without arguments to pull from the upstream when the new branch is checked out. </p>
<p> This behavior is the default when the start point is a remote-tracking branch. Set the branch.autoSetupMerge configuration variable to <code>false</code> if you want <code>git switch</code>, <code>git checkout</code> and <code>git branch</code> to always behave as if <code>&#8211;no-track</code> were given. Set it to <code>always</code> if you want this behavior when the start-point is either a local or remote-tracking branch.</dl>
<p> &#8211;no-track</p>
<dl>
<dt>
<dd> Do not set up &quot;upstream&quot; configuration, even if the branch.autoSetupMerge configuration variable is true.</dl>
<p> &#8211;set-upstream</p>
<dl>
<dt>
<dd> As this option had confusing syntax, it is no longer supported. Please use <code>&#8211;track</code> or <code>&#8211;set-upstream-to</code> instead.</dl>
<p> -u &lt;upstream&gt;, &#8211;set-upstream-to=&lt;upstream&gt;</p>
<dl>
<dt>
<dd> Set up &lt;branchname&gt;&#8217;s tracking information so &lt;upstream&gt; is considered &lt;branchname&gt;&#8217;s upstream branch. If no &lt;branchname&gt; is specified, then it defaults to the current branch.</dl>
<p> &#8211;unset-upstream</p>
<dl>
<dt>
<dd> Remove the upstream information for &lt;branchname&gt;. If no branch is specified it defaults to the current branch.</dl>
<p> &#8211;edit-description</p>
<dl>
<dt>
<dd> Open an editor and edit the text to explain what the branch is for, to be used by various other commands (e.g. <code>format-patch</code>, <code>request-pull</code>, and <code>merge</code> (if enabled)). Multi-line explanations may be used.</dl>
<p> &#8211;contains [&lt;commit&gt;]</p>
<dl>
<dt>
<dd> Only list branches which contain the specified commit (HEAD if not specified). Implies <code>&#8211;list</code>.</dl>
<p> &#8211;no-contains [&lt;commit&gt;]</p>
<dl>
<dt>
<dd> Only list branches which don&#8217;t contain the specified commit (HEAD if not specified). Implies <code>&#8211;list</code>.</dl>
<p> &#8211;merged [&lt;commit&gt;]</p>
<dl>
<dt>
<dd> Only list branches whose tips are reachable from the specified commit (HEAD if not specified). Implies <code>&#8211;list</code>.</dl>
<p> &#8211;no-merged [&lt;commit&gt;]</p>
<dl>
<dt>
<dd> Only list branches whose tips are not reachable from the specified commit (HEAD if not specified). Implies <code>&#8211;list</code>.</dl>
<p> &lt;branchname&gt;</p>
<dl>
<dt>
<dd> The name of the branch to create or delete. The new branch name must pass all checks defined by <code><a href="/docs/linux/man/1-git-check-ref-format/">git-check-ref-format</a></code>(1). Some of these checks may restrict the characters allowed in a branch name.</dl>
<p> &lt;start-point&gt;</p>
<dl>
<dt>
<dd> The new branch head will point to this commit. It may be given as a branch name, a commit-id, or a tag. If this option is omitted, the current HEAD will be used instead.</dl>
<p> &lt;oldbranch&gt;</p>
<dl>
<dt>
<dd> The name of an existing branch to rename.</dl>
<p> &lt;newbranch&gt;</p>
<dl>
<dt>
<dd> The new name for an existing branch. The same restrictions as for &lt;branchname&gt; apply.</dl>
<p> &#8211;sort=&lt;key&gt;</p>
<dl>
<dt>
<dd> Sort based on the key given. Prefix <code>&#8211;</code> to sort in descending order of the value. You may use the &#8211;sort=&lt;key&gt; option multiple times, in which case the last key becomes the primary key. The keys supported are the same as those in <code>git for-each-ref</code>. Sort order defaults to the value configured for the <code>branch.sort</code> variable if exists, or to sorting based on the full refname (including <code>refs/&#8230;</code> prefix). This lists detached HEAD (if present) first, then local branches and finally remote-tracking branches. See <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1).</dl>
<p> &#8211;points-at &lt;object&gt;</p>
<dl>
<dt>
<dd> Only list branches of the given object.</dl>
<p> &#8211;format &lt;format&gt;</p>
<dl>
<dt>
<dd> A string that interpolates <code>%(fieldname)</code> from a branch ref being shown and the object it points at. The format is the same as that of <code><a href="/docs/linux/man/1-git-for-each-ref/">git-for-each-ref</a></code>(1).</dl>
<h2>CONFIGURATION</h2>
<p> <code>pager.branch</code> is only respected when listing branches, i.e., when <code>&#8211;list</code> is used or implied. The default is to use a pager. See <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1).</p>
<h2>EXAMPLES</h2>
<p> Start development from a known tag</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
$ git clone <a href="git://git.kernel.org/pub/scm/.../linux-2.6">git://git.kernel.org/pub/scm/.../linux-2.6</a> my2.6
$ cd my2.6
$ git branch my2.6.14 v2.6.14   <code>(1)</code>
$ git switch my2.6.14
</pre>
</dl>
<p> <code>1. </code>This step and the next one could be combined into a single step with &quot;checkout -b my2.6.14 v2.6.14&quot;.
</dl>
<p> Delete an unneeded branch</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
$ git clone <a href="git://git.kernel.org/.../git.git">git://git.kernel.org/.../git.git</a> my.git
$ cd my.git
$ git branch -d -r origin/todo origin/html origin/man   <code>(1)</code>
$ git branch -D test                                    <code>(2)</code>
</pre>
</dl>
<p> <code>1. </code>Delete the remote-tracking branches &quot;todo&quot;, &quot;html&quot; and &quot;man&quot;. The next <i>fetch</i> or <i>pull</i> will create them again unless you configure them not to. See <code><a href="/docs/linux/man/1-git-fetch/">git-fetch</a></code>(1).<br />
 <code>2. </code>Delete the &quot;test&quot; branch even if the &quot;master&quot; branch (or whichever branch is currently checked out) does not have all commits from the test branch.
</dl>
<p> Listing branches from a specific remote</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
$ git branch -r -l '&lt;remote&gt;/&lt;pattern&gt;'                 <code>(1)</code>
$ git for-each-ref 'refs/remotes/&lt;remote&gt;/&lt;pattern&gt;'    <code>(2)</code>
</pre>
</dl>
<p> <code>1. </code>Using <code>-a</code> would conflate &lt;remote&gt; with any local branches you happen to have been prefixed with the same &lt;remote&gt; pattern.<br />
 <code>2. </code><code>for-each-ref</code> can take a wide range of options. See <code><a href="/docs/linux/man/1-git-for-each-ref/">git-for-each-ref</a></code>(1)
</dl>
<p> Patterns will normally need quoting.</p>
<h2>NOTES</h2>
<p> If you are creating a branch that you want to switch to immediately, it is easier to use the &quot;git switch&quot; command with its <code>-c</code> option to do the same thing with a single command. </p>
<p> The options <code>&#8211;contains</code>, <code>&#8211;no-contains</code>, <code>&#8211;merged</code> and <code>&#8211;no-merged</code> serve four related but different purposes: </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;contains &lt;commit&gt;</code> is used to find all branches which will need special attention if &lt;commit&gt; were to be rebased or amended, since those branches contain the specified &lt;commit&gt;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;no-contains &lt;commit&gt;</code> is the inverse of that, i.e. branches that don&#8217;t contain the specified &lt;commit&gt;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;merged</code> is used to find all branches which can be safely deleted, since those branches are fully contained by HEAD.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;no-merged</code> is used to find branches which are candidates for merging into HEAD, since those branches are not fully contained by HEAD.</dl>
<p> When combining multiple <code>&#8211;contains</code> and <code>&#8211;no-contains</code> filters, only references that contain at least one of the <code>&#8211;contains</code> commits and contain none of the <code>&#8211;no-contains</code> commits are shown. </p>
<p> When combining multiple <code>&#8211;merged</code> and <code>&#8211;no-merged</code> filters, only references that are reachable from at least one of the <code>&#8211;merged</code> commits and from none of the <code>&#8211;no-merged</code> commits are shown.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-check-ref-format/">git-check-ref-format</a></code>(1), <code><a href="/docs/linux/man/1-git-fetch/">git-fetch</a></code>(1), <code><a href="/docs/linux/man/1-git-remote/">git-remote</a></code>(1), m[blue]<code>&#8220;Understanding history: What is a branch?&#8221;</code>m[]<font SIZE="-2">[1]</font> in the Git User&#8217;s Manual.</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> &#8220;Understanding history: What is a branch?&#8221;</p>
<dl>
<dt>
<dd> file:///usr/share/doc/git/html/user-manual.html#what-is-a-branch</dl>
</dl>
<h2>Index</h2>

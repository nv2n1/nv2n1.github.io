---
title: "git-commit(1)"
name: "git-commit"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-commit/"
description: "git-commit – Record changes to the repository"
---

<h2 class="name">NAME</h2>
<p> git-commit &#8211; Record changes to the repository </p>
<h2>SYNOPSIS</h2>
<pre><code>
git commit [-a | --interactive | --patch] [-s] [-v] [-u&lt;mode&gt;] [--amend]
           [--dry-run] [(-c | -C | --squash) &lt;commit&gt; | --fixup [(amend|reword):]&lt;commit&gt;)]
           [-F &lt;file&gt; | -m &lt;msg&gt;] [--reset-author] [--allow-empty]
           [--allow-empty-message] [--no-verify] [-e] [--author=&lt;author&gt;]
           [--date=&lt;date&gt;] [--cleanup=&lt;mode&gt;] [--[no-]status]
           [-i | -o] [--pathspec-from-file=&lt;file&gt; [--pathspec-file-nul]]
           [(--trailer &lt;token&gt;[(=|:)&lt;value&gt;])...] [-S[&lt;keyid&gt;]]
           [--] [&lt;pathspec&gt;...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Create a new commit containing the current contents of the index and the given log message describing the changes. The new commit is a direct child of HEAD, usually the tip of the current branch, and the branch is updated to point to it (unless no branch is associated with the working tree, in which case HEAD is &quot;detached&quot; as described in <code><a href="/docs/linux/man/1-git-checkout/">git-checkout</a></code>(1)). </p>
<p> The content to be committed can be specified in several ways: </p>
<dl>
<dt>
<dd> 1. by using <code><a href="/docs/linux/man/1-git-add/">git-add</a></code>(1) to incrementally &quot;add&quot; changes to the index before using the <i>commit</i> command (Note: even modified files must be &quot;added&quot;);</dl>
<dl>
<dt>
<dd> 2. by using <code><a href="/docs/linux/man/1-git-rm/">git-rm</a></code>(1) to remove files from the working tree and the index, again before using the <i>commit</i> command;</dl>
<dl>
<dt>
<dd> 3. by listing files as arguments to the <i>commit</i> command (without &#8211;interactive or &#8211;patch switch), in which case the commit will ignore changes staged in the index, and instead record the current content of the listed files (which must already be known to Git);</dl>
<dl>
<dt>
<dd> 4. by using the -a switch with the <i>commit</i> command to automatically &quot;add&quot; changes from all known files (i.e. all files that are already listed in the index) and to automatically &quot;rm&quot; files in the index that have been removed from the working tree, and then perform the actual commit;</dl>
<dl>
<dt>
<dd> 5. by using the &#8211;interactive or &#8211;patch switches with the <i>commit</i> command to decide one by one which files or hunks should be part of the commit in addition to contents in the index, before finalizing the operation. See the &#8220;Interactive Mode&#8221; section of <code><a href="/docs/linux/man/1-git-add/">git-add</a></code>(1) to learn how to operate these modes.</dl>
<p> The <code>&#8211;dry-run</code> option can be used to obtain a summary of what is included by any of the above for the next commit by giving the same set of parameters (options and paths). </p>
<p> If you make a commit and then find a mistake immediately after that, you can recover from it with <i>git reset</i>.</p>
<h2>OPTIONS</h2>
<p> -a, &#8211;all</p>
<dl>
<dt>
<dd> Tell the command to automatically stage files that have been modified and deleted, but new files you have not told Git about are not affected.</dl>
<p> -p, &#8211;patch</p>
<dl>
<dt>
<dd> Use the interactive patch selection interface to choose which changes to commit. See <code><a href="/docs/linux/man/1-git-add/">git-add</a></code>(1) for details.</dl>
<p> -C &lt;commit&gt;, &#8211;reuse-message=&lt;commit&gt;</p>
<dl>
<dt>
<dd> Take an existing commit object, and reuse the log message and the authorship information (including the timestamp) when creating the commit.</dl>
<p> -c &lt;commit&gt;, &#8211;reedit-message=&lt;commit&gt;</p>
<dl>
<dt>
<dd> Like <i>-C</i>, but with <code>-c</code> the editor is invoked, so that the user can further edit the commit message.</dl>
<p> &#8211;fixup=[(amend|reword):]&lt;commit&gt;</p>
<dl>
<dt>
<dd> Create a new commit which &quot;fixes up&quot; <code>&lt;commit&gt;</code> when applied with <code>git rebase &#8211;autosquash</code>. Plain <code>&#8211;fixup=&lt;commit&gt;</code> creates a &quot;fixup!&quot; commit which changes the content of <code>&lt;commit&gt;</code> but leaves its log message untouched. <code>&#8211;fixup=amend:&lt;commit&gt;</code> is similar but creates an &quot;amend!&quot; commit which also replaces the log message of <code>&lt;commit&gt;</code> with the log message of the &quot;amend!&quot; commit. <code>&#8211;fixup=reword:&lt;commit&gt;</code> creates an &quot;amend!&quot; commit which replaces the log message of <code>&lt;commit&gt;</code> with its own log message but makes no changes to the content of <code>&lt;commit&gt;</code>. </p>
<p> The commit created by plain <code>&#8211;fixup=&lt;commit&gt;</code> has a subject composed of &quot;fixup!&quot; followed by the subject line from &lt;commit&gt;, and is recognized specially by <code>git rebase &#8211;autosquash</code>. The <code>-m</code> option may be used to supplement the log message of the created commit, but the additional commentary will be thrown away once the &quot;fixup!&quot; commit is squashed into <code>&lt;commit&gt;</code> by <code>git rebase &#8211;autosquash</code>. </p>
<p> The commit created by <code>&#8211;fixup=amend:&lt;commit&gt;</code> is similar but its subject is instead prefixed with &quot;amend!&quot;. The log message of &lt;commit&gt; is copied into the log message of the &quot;amend!&quot; commit and opened in an editor so it can be refined. When <code>git rebase &#8211;autosquash</code> squashes the &quot;amend!&quot; commit into <code>&lt;commit&gt;</code>, the log message of <code>&lt;commit&gt;</code> is replaced by the refined log message from the &quot;amend!&quot; commit. It is an error for the &quot;amend!&quot; commit&#8217;s log message to be empty unless <code>&#8211;allow-empty-message</code> is specified. </p>
<p> <code>&#8211;fixup=reword:&lt;commit&gt;</code> is shorthand for <code>&#8211;fixup=amend:&lt;commit&gt; &#8211;only</code>. It creates an &quot;amend!&quot; commit with only a log message (ignoring any changes staged in the index). When squashed by <code>git rebase &#8211;autosquash</code>, it replaces the log message of <code>&lt;commit&gt;</code> without making any other changes. </p>
<p> Neither &quot;fixup!&quot; nor &quot;amend!&quot; commits change authorship of <code>&lt;commit&gt;</code> when applied by <code>git rebase &#8211;autosquash</code>. See <code><a href="/docs/linux/man/1-git-rebase/">git-rebase</a></code>(1) for details.</dl>
<p> &#8211;squash=&lt;commit&gt;</p>
<dl>
<dt>
<dd> Construct a commit message for use with <code>rebase &#8211;autosquash</code>. The commit message subject line is taken from the specified commit with a prefix of &quot;squash! &quot;. Can be used with additional commit message options (<code>-m</code>/<code>-c</code>/<code>-C</code>/<code>-F</code>). See <code><a href="/docs/linux/man/1-git-rebase/">git-rebase</a></code>(1) for details.</dl>
<p> &#8211;reset-author</p>
<dl>
<dt>
<dd> When used with -C/-c/&#8211;amend options, or when committing after a conflicting cherry-pick, declare that the authorship of the resulting commit now belongs to the committer. This also renews the author timestamp.</dl>
<p> &#8211;short</p>
<dl>
<dt>
<dd> When doing a dry-run, give the output in the short-format. See <code><a href="/docs/linux/man/1-git-status/">git-status</a></code>(1) for details. Implies <code>&#8211;dry-run</code>.</dl>
<p> &#8211;branch</p>
<dl>
<dt>
<dd> Show the branch and tracking info even in short-format.</dl>
<p> &#8211;porcelain</p>
<dl>
<dt>
<dd> When doing a dry-run, give the output in a porcelain-ready format. See <code><a href="/docs/linux/man/1-git-status/">git-status</a></code>(1) for details. Implies <code>&#8211;dry-run</code>.</dl>
<p> &#8211;long</p>
<dl>
<dt>
<dd> When doing a dry-run, give the output in the long-format. Implies <code>&#8211;dry-run</code>.</dl>
<p> -z, &#8211;null</p>
<dl>
<dt>
<dd> When showing <code>short</code> or <code>porcelain</code> status output, print the filename verbatim and terminate the entries with NUL, instead of LF. If no format is given, implies the <code>&#8211;porcelain</code> output format. Without the <code>-z</code> option, filenames with &quot;unusual&quot; characters are quoted as explained for the configuration variable <code>core.quotePath</code> (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)).</dl>
<p> -F &lt;file&gt;, &#8211;file=&lt;file&gt;</p>
<dl>
<dt>
<dd> Take the commit message from the given file. Use <i>&#8211;</i> to read the message from the standard input.</dl>
<p> &#8211;author=&lt;author&gt;</p>
<dl>
<dt>
<dd> Override the commit author. Specify an explicit author using the standard <code>A U Thor &lt;author [at] example.com&gt;</code> format. Otherwise &lt;author&gt; is assumed to be a pattern and is used to search for an existing commit by that author (i.e. rev-list &#8211;all -i &#8211;author=&lt;author&gt;); the commit author is then copied from the first such commit found.</dl>
<p> &#8211;date=&lt;date&gt;</p>
<dl>
<dt>
<dd> Override the author date used in the commit.</dl>
<p> -m &lt;msg&gt;, &#8211;message=&lt;msg&gt;</p>
<dl>
<dt>
<dd> Use the given &lt;msg&gt; as the commit message. If multiple <code>-m</code> options are given, their values are concatenated as separate paragraphs. </p>
<p> The <code>-m</code> option is mutually exclusive with <code>-c</code>, <code>-C</code>, and <code>-F</code>.</dl>
<p> -t &lt;file&gt;, &#8211;template=&lt;file&gt;</p>
<dl>
<dt>
<dd> When editing the commit message, start the editor with the contents in the given file. The <code>commit.template</code> configuration variable is often used to give this option implicitly to the command. This mechanism can be used by projects that want to guide participants with some hints on what to write in the message in what order. If the user exits the editor without editing the message, the commit is aborted. This has no effect when a message is given by other means, e.g. with the <code>-m</code> or <code>-F</code> options.</dl>
<p> -s, &#8211;signoff, &#8211;no-signoff</p>
<dl>
<dt>
<dd> Add a <code>Signed-off-by</code> trailer by the committer at the end of the commit log message. The meaning of a signoff depends on the project to which you&#8217;re committing. For example, it may certify that the committer has the rights to submit the work under the project&#8217;s license or agrees to some contributor representation, such as a Developer Certificate of Origin. (See m[blue]<code><a rel="nofollow" href="http://developercertificate.org">http://developercertificate.org</a></code>m[] for the one used by the Linux kernel and Git projects.) Consult the documentation or leadership of the project to which you&#8217;re contributing to understand how the signoffs are used in that project. </p>
<p> The &#8211;no-signoff option can be used to countermand an earlier &#8211;signoff option on the command line.</dl>
<p> &#8211;trailer &lt;token&gt;[(=|:)&lt;value&gt;]</p>
<dl>
<dt>
<dd> Specify a (&lt;token&gt;, &lt;value&gt;) pair that should be applied as a trailer. (e.g. <code>git commit &#8211;trailer &quot;Signed-off-by:C O Mitter \ &lt;committer [at] example.com&gt;&quot; &#8211;trailer &quot;Helped-by:C O Mitter \ &lt;committer [at] example.com&gt;&quot;</code> will add the &quot;Signed-off-by&quot; trailer and the &quot;Helped-by&quot; trailer to the commit message.) The <code>trailer.*</code> configuration variables (<code><a href="/docs/linux/man/1-git-interpret-trailers/">git-interpret-trailers</a></code>(1)) can be used to define if a duplicated trailer is omitted, where in the run of trailers each trailer would appear, and other details.</dl>
<p> -n, &#8211;[no-]verify</p>
<dl>
<dt>
<dd> By default, the pre-commit and commit-msg hooks are run. When any of <code>&#8211;no-verify</code> or <code>-n</code> is given, these are bypassed. See also <code><a href="/docs/linux/man/5-githooks/">githooks</a></code>(5).</dl>
<p> &#8211;allow-empty</p>
<dl>
<dt>
<dd> Usually recording a commit that has the exact same tree as its sole parent commit is a mistake, and the command prevents you from making such a commit. This option bypasses the safety, and is primarily for use by foreign SCM interface scripts.</dl>
<p> &#8211;allow-empty-message</p>
<dl>
<dt>
<dd> Like &#8211;allow-empty this command is primarily for use by foreign SCM interface scripts. It allows you to create a commit with an empty commit message without using plumbing commands like <code><a href="/docs/linux/man/1-git-commit-tree/">git-commit-tree</a></code>(1).</dl>
<p> &#8211;cleanup=&lt;mode&gt;</p>
<dl>
<dt>
<dd> This option determines how the supplied commit message should be cleaned up before committing. The <i>&lt;mode&gt;</i> can be <code>strip</code>, <code>whitespace</code>, <code>verbatim</code>, <code>scissors</code> or <code>default</code>. </p>
<p> strip</p>
<dl>
<dt>
<dd> Strip leading and trailing empty lines, trailing whitespace, commentary and collapse consecutive empty lines.</dl>
<p> whitespace</p>
<dl>
<dt>
<dd> Same as <code>strip</code> except #commentary is not removed.</dl>
<p> verbatim</p>
<dl>
<dt>
<dd> Do not change the message at all.</dl>
<p> scissors</p>
<dl>
<dt>
<dd> Same as <code>whitespace</code> except that everything from (and including) the line found below is truncated, if the message is to be edited. &quot;<code>#</code>&quot; can be customized with core.commentChar. </p>
<dl>
<dt>
<dd>
<pre><code>
#-- -- -- -- -- -- -- -- -- -- -- --&gt; 8 -- -- -- -- -- -- -- -- -- -- -- --
</code></pre>
</dl>
</dl>
<p> default</p>
<dl>
<dt>
<dd> Same as <code>strip</code> if the message is to be edited. Otherwise <code>whitespace</code>.</dl>
<p> The default can be changed by the <code>commit.cleanup</code> configuration variable (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)).</dl>
<p> -e, &#8211;edit</p>
<dl>
<dt>
<dd> The message taken from file with <code>-F</code>, command line with <code>-m</code>, and from commit object with <code>-C</code> are usually used as the commit log message unmodified. This option lets you further edit the message taken from these sources.</dl>
<p> &#8211;no-edit</p>
<dl>
<dt>
<dd> Use the selected commit message without launching an editor. For example, <code>git commit &#8211;amend &#8211;no-edit</code> amends a commit without changing its commit message.</dl>
<p> &#8211;amend</p>
<dl>
<dt>
<dd> Replace the tip of the current branch by creating a new commit. The recorded tree is prepared as usual (including the effect of the <code>-i</code> and <code>-o</code> options and explicit pathspec), and the message from the original commit is used as the starting point, instead of an empty message, when no other message is specified from the command line via options such as <code>-m</code>, <code>-F</code>, <code>-c</code>, etc. The new commit has the same parents and author as the current one (the <code>&#8211;reset-author</code> option can countermand this). </p>
<p> It is a rough equivalent for: </p>
<dl>
<dt>
<dd>
<pre>
        $ git reset --soft HEAD^
        $ ... do something else to come up with the right tree ...
        $ git commit -c ORIG_HEAD
</pre>
</dl>
<p> but can be used to amend a merge commit. </p>
<p> You should understand the implications of rewriting history if you amend a commit that has already been published. (See the &quot;RECOVERING FROM UPSTREAM REBASE&quot; section in <code><a href="/docs/linux/man/1-git-rebase/">git-rebase</a></code>(1).)</dl>
<p> &#8211;no-post-rewrite</p>
<dl>
<dt>
<dd> Bypass the post-rewrite hook.</dl>
<p> -i, &#8211;include</p>
<dl>
<dt>
<dd> Before making a commit out of staged contents so far, stage the contents of paths given on the command line as well. This is usually not what you want unless you are concluding a conflicted merge.</dl>
<p> -o, &#8211;only</p>
<dl>
<dt>
<dd> Make a commit by taking the updated working tree contents of the paths specified on the command line, disregarding any contents that have been staged for other paths. This is the default mode of operation of <i>git commit</i> if any paths are given on the command line, in which case this option can be omitted. If this option is specified together with <code>&#8211;amend</code>, then no paths need to be specified, which can be used to amend the last commit without committing changes that have already been staged. If used together with <code>&#8211;allow-empty</code> paths are also not required, and an empty commit will be created.</dl>
<p> &#8211;pathspec-from-file=&lt;file&gt;</p>
<dl>
<dt>
<dd> Pathspec is passed in <code>&lt;file&gt;</code> instead of commandline args. If <code>&lt;file&gt;</code> is exactly <code>&#8211;</code> then standard input is used. Pathspec elements are separated by LF or CR/LF. Pathspec elements can be quoted as explained for the configuration variable <code>core.quotePath</code> (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)). See also <code>&#8211;pathspec-file-nul</code> and global <code>&#8211;literal-pathspecs</code>.</dl>
<p> &#8211;pathspec-file-nul</p>
<dl>
<dt>
<dd> Only meaningful with <code>&#8211;pathspec-from-file</code>. Pathspec elements are separated with NUL character and all other characters are taken literally (including newlines and quotes).</dl>
<p> -u[&lt;mode&gt;], &#8211;untracked-files[=&lt;mode&gt;]</p>
<dl>
<dt>
<dd> Show untracked files. </p>
<p> The mode parameter is optional (defaults to <i>all</i>), and is used to specify the handling of untracked files; when -u is not used, the default is <i>normal</i>, i.e. show untracked files and directories. </p>
<p> The possible options are: </p>
<dl>
<dt>
<dd> &bull; <i>no</i> &#8211; Show no untracked files</dl>
<dl>
<dt>
<dd> &bull; <i>normal</i> &#8211; Shows untracked files and directories</dl>
<dl>
<dt>
<dd> &bull; <i>all</i> &#8211; Also shows individual files in untracked directories.</dl>
<p> The default can be changed using the status.showUntrackedFiles configuration variable documented in <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1).</dl>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
<dd> Show unified diff between the HEAD commit and what would be committed at the bottom of the commit message template to help the user describe the commit by reminding what changes the commit has. Note that this diff output doesn&#8217;t have its lines prefixed with <i>#</i>. This diff will not be a part of the commit message. See the <code>commit.verbose</code> configuration variable in <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1). </p>
<p> If specified twice, show in addition the unified diff between what would be committed and the worktree files, i.e. the unstaged changes to tracked files.</dl>
<p> -q, &#8211;quiet</p>
<dl>
<dt>
<dd> Suppress commit summary message.</dl>
<p> &#8211;dry-run</p>
<dl>
<dt>
<dd> Do not create a commit, but show a list of paths that are to be committed, paths with local changes that will be left uncommitted and paths that are untracked.</dl>
<p> &#8211;status</p>
<dl>
<dt>
<dd> Include the output of <code><a href="/docs/linux/man/1-git-status/">git-status</a></code>(1) in the commit message template when using an editor to prepare the commit message. Defaults to on, but can be used to override configuration variable commit.status.</dl>
<p> &#8211;no-status</p>
<dl>
<dt>
<dd> Do not include the output of <code><a href="/docs/linux/man/1-git-status/">git-status</a></code>(1) in the commit message template when using an editor to prepare the default commit message.</dl>
<p> -S[&lt;keyid&gt;], &#8211;gpg-sign[=&lt;keyid&gt;], &#8211;no-gpg-sign</p>
<dl>
<dt>
<dd> GPG-sign commits. The <code>keyid</code> argument is optional and defaults to the committer identity; if specified, it must be stuck to the option without a space. <code>&#8211;no-gpg-sign</code> is useful to countermand both <code>commit.gpgSign</code> configuration variable, and earlier <code>&#8211;gpg-sign</code>.</dl>
<p> &#8212;</p>
<dl>
<dt>
<dd> Do not interpret any more arguments as options.</dl>
<p> &lt;pathspec&gt;&#8230;</p>
<dl>
<dt>
<dd> When pathspec is given on the command line, commit the contents of the files that match the pathspec without recording the changes already added to the index. The contents of these files are also staged for the next commit on top of what have been staged before. </p>
<p> For more details, see the <i>pathspec</i> entry in <code><a href="/docs/linux/man/7-gitglossary/">gitglossary</a></code>(7).</dl>
<h2>EXAMPLES</h2>
<p> When recording your own work, the contents of modified files in your working tree are temporarily stored to a staging area called the &quot;index&quot; with <i>git add</i>. A file can be reverted back, only in the index but not in the working tree, to that of the last commit with <code>git restore &#8211;staged &lt;file&gt;</code>, which effectively reverts <i>git add</i> and prevents the changes to this file from participating in the next commit. After building the state to be committed incrementally with these commands, <code>git commit</code> (without any pathname parameter) is used to record what has been staged so far. This is the most basic form of the command. An example: </p>
<dl>
<dt>
<dd>
<pre>
$ edit hello.c
$ git rm goodbye.c
$ git add hello.c
$ git commit
</pre>
</dl>
<p> Instead of staging files after each individual change, you can tell <code>git commit</code> to notice the changes to the files whose contents are tracked in your working tree and do corresponding <code>git add</code> and <code>git rm</code> for you. That is, this example does the same as the earlier example if there is no other change in your working tree: </p>
<dl>
<dt>
<dd>
<pre>
$ edit hello.c
$ rm goodbye.c
$ git commit -a
</pre>
</dl>
<p> The command <code>git commit -a</code> first looks at your working tree, notices that you have modified hello.c and removed goodbye.c, and performs necessary <code>git add</code> and <code>git rm</code> for you. </p>
<p> After staging changes to many files, you can alter the order the changes are recorded in, by giving pathnames to <code>git commit</code>. When pathnames are given, the command makes a commit that only records the changes made to the named paths: </p>
<dl>
<dt>
<dd>
<pre>
$ edit hello.c hello.h
$ git add hello.c hello.h
$ edit Makefile
$ git commit Makefile
</pre>
</dl>
<p> This makes a commit that records the modification to <code>Makefile</code>. The changes staged for <code>hello.c</code> and <code>hello.h</code> are not included in the resulting commit. However, their changes are not lost &#8212; they are still staged and merely held back. After the above sequence, if you do: </p>
<dl>
<dt>
<dd>
<pre>
$ git commit
</pre>
</dl>
<p> this second commit would record the changes to <code>hello.c</code> and <code>hello.h</code> as expected. </p>
<p> After a merge (initiated by <i>git merge</i> or <i>git pull</i>) stops because of conflicts, cleanly merged paths are already staged to be committed for you, and paths that conflicted are left in unmerged state. You would have to first check which paths are conflicting with <i>git status</i> and after fixing them manually in your working tree, you would stage the result as usual with <i>git add</i>: </p>
<dl>
<dt>
<dd>
<pre>
$ git status | grep unmerged
unmerged: hello.c
$ edit hello.c
$ git add hello.c
</pre>
</dl>
<p> After resolving conflicts and staging the result, <code>git ls-files -u</code> would stop mentioning the conflicted path. When you are done, run <code>git commit</code> to finally record the merge: </p>
<dl>
<dt>
<dd>
<pre>
$ git commit
</pre>
</dl>
<p> As with the case to record your own changes, you can use <code>-a</code> option to save typing. One difference is that during a merge resolution, you cannot use <code>git commit</code> with pathnames to alter the order the changes are committed, because the merge should be recorded as a single commit. In fact, the command refuses to run when given pathnames (but see <code>-i</code> option).</p>
<h2>COMMIT INFORMATION</h2>
<p> Author and committer information is taken from the following environment variables, if set: </p>
<dl>
<dt>
<dd>
<pre>
GIT_AUTHOR_NAME
GIT_AUTHOR_EMAIL
GIT_AUTHOR_DATE
GIT_COMMITTER_NAME
GIT_COMMITTER_EMAIL
GIT_COMMITTER_DATE
</pre>
</dl>
<p> (nb &quot;&lt;&quot;, &quot;&gt;&quot; and &quot;
&quot;s are stripped) </p>
<p> The author and committer names are by convention some form of a personal name (that is, the name by which other humans refer to you), although Git does not enforce or require any particular form. Arbitrary Unicode may be used, subject to the constraints listed above. This name has no effect on authentication; for that, see the <code>credential.username</code> variable in <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1). </p>
<p> In case (some of) these environment variables are not set, the information is taken from the configuration items <code>user.name</code> and <code>user.email</code>, or, if not present, the environment variable EMAIL, or, if that is not set, system user name and the hostname used for outgoing mail (taken from <code>/etc/mailname</code> and falling back to the fully qualified hostname when that file does not exist). </p>
<p> The <code>author.name</code> and <code>committer.name</code> and their corresponding email options override <code>user.name</code> and <code>user.email</code> if set and are overridden themselves by the environment variables. </p>
<p> The typical usage is to set just the <code>user.name</code> and <code>user.email</code> variables; the other options are provided for more complex use cases.</p>
<h2>DATE FORMATS</h2>
<p> The <code>GIT_AUTHOR_DATE</code> and <code>GIT_COMMITTER_DATE</code> environment variables support the following date formats: </p>
<p> Git internal format</p>
<dl>
<dt>
<dd> It is <code>&lt;unix timestamp&gt; &lt;time zone offset&gt;</code>, where <code>&lt;unix timestamp&gt;</code> is the number of seconds since the UNIX epoch. <code>&lt;time zone offset&gt;</code> is a positive or negative offset from UTC. For example CET (which is 1 hour ahead of UTC) is <code>+0100</code>.</dl>
<p> RFC 2822</p>
<dl>
<dt>
<dd> The standard email format as described by RFC 2822, for example <code>Thu, 07 Apr 2005 22:13:13 +0200</code>.</dl>
<p> ISO 8601</p>
<dl>
<dt>
<dd> Time and date specified by the ISO 8601 standard, for example <code>2005-04-07T22:13:13</code>. The parser accepts a space instead of the <code>T</code> character as well. Fractional parts of a second will be ignored, for example <code>2005-04-07T22:13:13.019</code> will be treated as <code>2005-04-07T22:13:13</code>. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 In addition, the date part is accepted in the following formats: <code>YYYY.MM.DD</code>, <code>MM/DD/YYYY</code> and <code>DD.MM.YYYY</code>. </p>
</dl>
</dl>
<p> In addition to recognizing all date formats above, the <code>&#8211;date</code> option will also try to make sense of other, more human-centric date formats, such as relative dates like &quot;yesterday&quot; or &quot;last Friday at noon&quot;.</p>
<h2>DISCUSSION</h2>
<p> Though not required, it&#8217;s a good idea to begin the commit message with a single short (less than 50 character) line summarizing the change, followed by a blank line and then a more thorough description. The text up to the first blank line in a commit message is treated as the commit title, and that title is used throughout Git. For example, <code><a href="/docs/linux/man/1-git-format-patch/">git-format-patch</a></code>(1) turns a commit into email, and it uses the title on the Subject line and the rest of the commit in the body. </p>
<p> Git is to some extent character encoding agnostic. </p>
<dl>
<dt>
<dd> &bull; The contents of the blob objects are uninterpreted sequences of bytes. There is no encoding translation at the core level.</dl>
<dl>
<dt>
<dd> &bull; Path names are encoded in UTF-8 normalization form C. This applies to tree objects, the index file, ref names, as well as path names in command line arguments, environment variables and config files (<code>.git/config</code> (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)), <code><a href="/docs/linux/man/5-gitignore/">gitignore</a></code>(5), <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5) and <code><a href="/docs/linux/man/5-gitmodules/">gitmodules</a></code>(5)). </p>
<p> Note that Git at the core level treats path names simply as sequences of non-NUL bytes, there are no path name encoding conversions (except on Mac and Windows). Therefore, using non-ASCII path names will mostly work even on platforms and file systems that use legacy extended ASCII encodings. However, repositories created on such systems will not work properly on UTF-8-based systems (e.g. Linux, Mac, Windows) and vice versa. Additionally, many Git-based tools simply assume path names to be UTF-8 and will fail to display other encodings correctly.</dl>
<dl>
<dt>
<dd> &bull; Commit log messages are typically encoded in UTF-8, but other extended ASCII encodings are also supported. This includes ISO-8859-x, CP125x and many others, but <i>not</i> UTF-16/32, EBCDIC and CJK multi-byte encodings (GBK, Shift-JIS, Big5, EUC-x, CP9xx etc.).</dl>
<p> Although we encourage that the commit log messages are encoded in UTF-8, both the core and Git Porcelain are designed not to force UTF-8 on projects. If all participants of a particular project find it more convenient to use legacy encodings, Git does not forbid it. However, there are a few things to keep in mind. </p>
<dl>
<dt>
<dd> 1. <i>git commit</i> and <i>git commit-tree</i> issues a warning if the commit log message given to it does not look like a valid UTF-8 string, unless you explicitly say your project uses a legacy encoding. The way to say this is to have <code>i18n.commitEncoding</code> in <code>.git/config</code> file, like this: </p>
<dl>
<dt>
<dd>
<pre>
[i18n]
        commitEncoding = ISO-8859-1
</pre>
</dl>
<p> Commit objects created with the above setting record the value of <code>i18n.commitEncoding</code> in its <code>encoding</code> header. This is to help other people who look at them later. Lack of this header implies that the commit log message is encoded in UTF-8.</dl>
<dl>
<dt>
<dd> 2. <i>git log</i>, <i>git show</i>, <i>git blame</i> and friends look at the <code>encoding</code> header of a commit object, and try to re-code the log message into UTF-8 unless otherwise specified. You can specify the desired output encoding with <code>i18n.logOutputEncoding</code> in <code>.git/config</code> file, like this: </p>
<dl>
<dt>
<dd>
<pre>
[i18n]
        logOutputEncoding = ISO-8859-1
</pre>
</dl>
<p> If you do not have this configuration variable, the value of <code>i18n.commitEncoding</code> is used instead.</dl>
<p> Note that we deliberately chose not to re-code the commit log message when a commit is made to force UTF-8 at the commit object level, because re-coding to UTF-8 is not necessarily a reversible operation.</p>
<h2>ENVIRONMENT AND CONFIGURATION VARIABLES</h2>
<p> The editor used to edit the commit log message will be chosen from the <code>GIT_EDITOR</code> environment variable, the core.editor configuration variable, the <code>VISUAL</code> environment variable, or the <code>EDITOR</code> environment variable (in that order). See <code><a href="/docs/linux/man/1-git-var/">git-var</a></code>(1) for details.</p>
<h2>HOOKS</h2>
<p> This command can run <code>commit-msg</code>, <code>prepare-commit-msg</code>, <code>pre-commit</code>, <code>post-commit</code> and <code>post-rewrite</code> hooks. See <code><a href="/docs/linux/man/5-githooks/">githooks</a></code>(5) for more information.</p>
<h2>FILES</h2>
<p> <code>$GIT_DIR/COMMIT_EDITMSG</code></p>
<dl>
<dt>
<dd> This file contains the commit message of a commit in progress. If <code>git commit</code> exits due to an error before creating a commit, any commit message that has been provided by the user (e.g., in an editor session) will be available in this file, but will be overwritten by the next invocation of <code>git commit</code>.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-add/">git-add</a></code>(1), <code><a href="/docs/linux/man/1-git-rm/">git-rm</a></code>(1), <code><a href="/docs/linux/man/1-git-mv/">git-mv</a></code>(1), <code><a href="/docs/linux/man/1-git-merge/">git-merge</a></code>(1), <code><a href="/docs/linux/man/1-git-commit-tree/">git-commit-tree</a></code>(1)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>

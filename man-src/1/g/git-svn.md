---
title: "git-svn(1)"
name: "git-svn"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-svn/"
description: "git-svn – Bidirectional operation between a Subversion repository and Git"
---

<h2 class="name">NAME</h2>
<p> git-svn &#8211; Bidirectional operation between a Subversion repository and Git </p>
<h2>SYNOPSIS</h2>
<pre><code>
git svn&lt;command&gt;[options][arguments]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <i>git svn</i> is a simple conduit for changesets between Subversion and Git. It provides a bidirectional flow of changes between a Subversion and a Git repository. </p>
<p> <i>git svn</i> can track a standard Subversion repository, following the common &quot;trunk/branches/tags&quot; layout, with the &#8211;stdlayout option. It can also follow branches and tags in any layout with the -T/-t/-b options (see options to <i>init</i> below, and also the <i>clone</i> command). </p>
<p> Once tracking a Subversion repository (with any of the above methods), the Git repository can be updated from Subversion by the <i>fetch</i> command and Subversion updated from Git by the <i>dcommit</i> command.</p>
<h2>COMMANDS</h2>
<p> <i>init</i></p>
<dl>
<dt>
<dd> Initializes an empty Git repository with additional metadata directories for <i>git svn</i>. The Subversion URL may be specified as a command-line argument, or as full URL arguments to -T/-t/-b. Optionally, the target directory to operate on can be specified as a second argument. Normally this command initializes the current directory. </p>
<p> -T&lt;trunk_subdir&gt;, &#8211;trunk=&lt;trunk_subdir&gt;, -t&lt;tags_subdir&gt;, &#8211;tags=&lt;tags_subdir&gt;, -b&lt;branches_subdir&gt;, &#8211;branches=&lt;branches_subdir&gt;, -s, &#8211;stdlayout</p>
<dl>
<dt>
<dd> These are optional command-line options for init. Each of these flags can point to a relative repository path (&#8211;tags=project/tags) or a full url (&#8211;tags=<a rel="nofollow" href="https://foo.org/project/tags">https://foo.org/project/tags</a>). You can specify more than one &#8211;tags and/or &#8211;branches options, in case your Subversion repository places tags or branches under multiple paths. The option &#8211;stdlayout is a shorthand way of setting trunk,tags,branches as the relative paths, which is the Subversion default. If any of the other options are given as well, they take precedence.</dl>
<p> &#8211;no-metadata</p>
<dl>
<dt>
<dd> Set the <i>noMetadata</i> option in the [svn-remote] config. This option is not recommended, please read the <i>svn.noMetadata</i> section of this manpage before using this option.</dl>
<p> &#8211;use-svm-props</p>
<dl>
<dt>
<dd> Set the <i>useSvmProps</i> option in the [svn-remote] config.</dl>
<p> &#8211;use-svnsync-props</p>
<dl>
<dt>
<dd> Set the <i>useSvnsyncProps</i> option in the [svn-remote] config.</dl>
<p> &#8211;rewrite-root=&lt;URL&gt;</p>
<dl>
<dt>
<dd> Set the <i>rewriteRoot</i> option in the [svn-remote] config.</dl>
<p> &#8211;rewrite-uuid=&lt;UUID&gt;</p>
<dl>
<dt>
<dd> Set the <i>rewriteUUID</i> option in the [svn-remote] config.</dl>
<p> &#8211;username=&lt;user&gt;</p>
<dl>
<dt>
<dd> For transports that SVN handles authentication for (http, https, and plain svn), specify the username. For other transports (eg svn+<a href="ssh://">ssh://</a>), you must include the username in the URL, eg svn+<a href="ssh://foo@svn.bar.com/project">ssh://foo@svn.bar.com/project</a></dl>
<p> &#8211;prefix=&lt;prefix&gt;</p>
<dl>
<dt>
<dd> This allows one to specify a prefix which is prepended to the names of remotes if trunk/branches/tags are specified. The prefix does not automatically include a trailing slash, so be sure you include one in the argument if that is what you want. If &#8211;branches/-b is specified, the prefix must include a trailing slash. Setting a prefix is useful if you wish to track multiple projects that share a common repository.</dl>
<p> &#8211;ignore-paths=&lt;regex&gt;</p>
<dl>
<dt>
<dd> When passed to <i>init</i> or <i>clone</i> this regular expression will be preserved as a config key. See <i>fetch</i> for a description of <i>&#8211;ignore-paths</i>.</dl>
<p> &#8211;include-paths=&lt;regex&gt;</p>
<dl>
<dt>
<dd> When passed to <i>init</i> or <i>clone</i> this regular expression will be preserved as a config key. See <i>fetch</i> for a description of <i>&#8211;include-paths</i>.</dl>
<p> &#8211;no-minimize-url</p>
<dl>
<dt>
<dd> When tracking multiple directories (using &#8211;stdlayout, &#8211;branches, or &#8211;tags options), git svn will attempt to connect to the root (or highest allowed level) of the Subversion repository. This default allows better tracking of history if entire projects are moved within a repository, but may cause issues on repositories where read access restrictions are in place. Passing <i>&#8211;no-minimize-url</i> will allow git svn to accept URLs as-is without attempting to connect to a higher level directory. This option is off by default when only one URL/branch is tracked (it would do little good).</dl>
</dl>
<p> <i>fetch</i></p>
<dl>
<dt>
<dd> Fetch unfetched revisions from the Subversion remote we are tracking. The name of the [svn-remote &quot;&#8230;&quot;] section in the .git/config file may be specified as an optional command-line argument. </p>
<p> &#8211;localtime</p>
<dl>
<dt>
<dd> Store Git commit times in the local timezone instead of UTC. This makes <i>git log</i> (even without &#8211;date=local) show the same times that svn log would in the local timezone. </p>
<p> This doesn&#8217;t interfere with interoperating with the Subversion repository you cloned from, but if you wish for your local Git repository to be able to interoperate with someone else&#8217;s local Git repository, either don&#8217;t use this option or you should both use it in the same local timezone.</dl>
<p> &#8211;parent</p>
<dl>
<dt>
<dd> Fetch only from the SVN parent of the current HEAD.</dl>
<p> &#8211;ignore-paths=&lt;regex&gt;</p>
<dl>
<dt>
<dd> This allows one to specify a Perl regular expression that will cause skipping of all matching paths from checkout from SVN. The <i>&#8211;ignore-paths</i> option should match for every <i>fetch</i> (including automatic fetches due to <i>clone</i>, <i>dcommit</i>, <i>rebase</i>, etc) on a given repository. </p>
<dl>
<dt>
<dd>
<pre>
config key: svn-remote.&lt;name&gt;.ignore-paths
</pre>
</dl>
<p> If the ignore-paths config key is set and the command line option is also given, both regular expressions will be used. </p>
<p> Examples: </p>
<p> Skip &quot;doc*&quot; directory for every fetch</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
--ignore-paths=&quot;^doc&quot;
</pre>
</dl>
</dl>
<p> Skip &quot;branches&quot; and &quot;tags&quot; of first level directories</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
--ignore-paths=&quot;^[^/]+/(?:branches|tags)&quot;
</pre>
</dl>
</dl>
</dl>
<p> &#8211;include-paths=&lt;regex&gt;</p>
<dl>
<dt>
<dd> This allows one to specify a Perl regular expression that will cause the inclusion of only matching paths from checkout from SVN. The <i>&#8211;include-paths</i> option should match for every <i>fetch</i> (including automatic fetches due to <i>clone</i>, <i>dcommit</i>, <i>rebase</i>, etc) on a given repository. <i>&#8211;ignore-paths</i> takes precedence over <i>&#8211;include-paths</i>.</dl>
<p> &#8211;log-window-size=&lt;n&gt;</p>
<dl>
<dt>
<dd> Fetch &lt;n&gt; log entries per request when scanning Subversion history. The default is 100. For very large Subversion repositories, larger values may be needed for <i>clone</i>/<i>fetch</i> to complete in reasonable time. But overly large values may lead to higher memory usage and request timeouts.</dl>
</dl>
<p> <i>clone</i></p>
<dl>
<dt>
<dd> Runs <i>init</i> and <i>fetch</i>. It will automatically create a directory based on the basename of the URL passed to it; or if a second argument is passed; it will create a directory and work within that. It accepts all arguments that the <i>init</i> and <i>fetch</i> commands accept; with the exception of <i>&#8211;fetch-all</i> and <i>&#8211;parent</i>. After a repository is cloned, the <i>fetch</i> command will be able to update revisions without affecting the working tree; and the <i>rebase</i> command will be able to update the working tree with the latest changes. </p>
<p> &#8211;preserve-empty-dirs</p>
<dl>
<dt>
<dd> Create a placeholder file in the local Git repository for each empty directory fetched from Subversion. This includes directories that become empty by removing all entries in the Subversion repository (but not the directory itself). The placeholder files are also tracked and removed when no longer necessary.</dl>
<p> &#8211;placeholder-filename=&lt;filename&gt;</p>
<dl>
<dt>
<dd> Set the name of placeholder files created by &#8211;preserve-empty-dirs. Default: &quot;.gitignore&quot;</dl>
</dl>
<p> <i>rebase</i></p>
<dl>
<dt>
<dd> This fetches revisions from the SVN parent of the current HEAD and rebases the current (uncommitted to SVN) work against it. </p>
<p> This works similarly to svn update or <i>git pull</i> except that it preserves linear history with <i>git rebase</i> instead of <i>git merge</i> for ease of dcommitting with <i>git svn</i>. </p>
<p> This accepts all options that <i>git svn fetch</i> and <i>git rebase</i> accept. However, <i>&#8211;fetch-all</i> only fetches from the current [svn-remote], and not all [svn-remote] definitions. </p>
<p> Like <i>git rebase</i>; this requires that the working tree be clean and have no uncommitted changes. </p>
<p> -l, &#8211;local</p>
<dl>
<dt>
<dd> Do not fetch remotely; only run <i>git rebase</i> against the last fetched commit from the upstream SVN.</dl>
</dl>
<p> <i>dcommit</i></p>
<dl>
<dt>
<dd> Commit each diff from the current branch directly to the SVN repository, and then rebase or reset (depending on whether or not there is a diff between SVN and head). This will create a revision in SVN for each commit in Git. </p>
<p> When an optional Git branch name (or a Git commit object name) is specified as an argument, the subcommand works on the specified branch, not on the current branch. </p>
<p> Use of <i>dcommit</i> is preferred to <i>set-tree</i> (below). </p>
<p> &#8211;no-rebase</p>
<dl>
<dt>
<dd> After committing, do not rebase or reset.</dl>
<p> &#8211;commit-url &lt;URL&gt;</p>
<dl>
<dt>
<dd> Commit to this SVN URL (the full path). This is intended to allow existing <i>git svn</i> repositories created with one transport method (e.g. svn:// or http:// for anonymous read) to be reused if a user is later given access to an alternate transport method (e.g. svn+ssh:// or <a rel="nofollow" href="https://)">https://)</a> for commit. </p>
<dl>
<dt>
<dd>
<pre>
config key: svn-remote.&lt;name&gt;.commiturl
config key: svn.commiturl (overwrites all svn-remote.&lt;name&gt;.commiturl options)
</pre>
</dl>
<p> Using this option for any other purpose (don&#8217;t ask) is very strongly discouraged.</dl>
<p> &#8211;mergeinfo=&lt;mergeinfo&gt;</p>
<dl>
<dt>
<dd> Add the given merge information during the dcommit (e.g. &#8211;mergeinfo=&quot;/branches/foo:1-10&quot;). All svn server versions can store this information (as a property), and svn clients starting from version 1.5 can make use of it. To specify merge information from multiple branches, use a single space character between the branches (&#8211;mergeinfo=&quot;/branches/foo:1-10 /branches/bar:3,5-6,8&quot;) </p>
<dl>
<dt>
<dd>
<pre>
config key: svn.pushmergeinfo
</pre>
</dl>
<p> This option will cause git-svn to attempt to automatically populate the svn:mergeinfo property in the SVN repository when possible. Currently, this can only be done when dcommitting non-fast-forward merges where all parents but the first have already been pushed into SVN.</dl>
<p> &#8211;interactive</p>
<dl>
<dt>
<dd> Ask the user to confirm that a patch set should actually be sent to SVN. For each patch, one may answer &quot;yes&quot; (accept this patch), &quot;no&quot; (discard this patch), &quot;all&quot; (accept all patches), or &quot;quit&quot;. <i>git svn dcommit</i> returns immediately if answer if &quot;no&quot; or &quot;quit&quot;, without committing anything to SVN.</dl>
</dl>
<p> <i>branch</i></p>
<dl>
<dt>
<dd> Create a branch in the SVN repository. </p>
<p> -m, &#8211;message</p>
<dl>
<dt>
<dd> Allows to specify the commit message.</dl>
<p> -t, &#8211;tag</p>
<dl>
<dt>
<dd> Create a tag by using the tags_subdir instead of the branches_subdir specified during git svn init.</dl>
<p> -d&lt;path&gt;, &#8211;destination=&lt;path&gt;</p>
<dl>
<dt>
<dd> If more than one &#8211;branches (or &#8211;tags) option was given to the <i>init</i> or <i>clone</i> command, you must provide the location of the branch (or tag) you wish to create in the SVN repository. &lt;path&gt; specifies which path to use to create the branch or tag and should match the pattern on the left-hand side of one of the configured branches or tags refspecs. You can see these refspecs with the commands </p>
<dl>
<dt>
<dd>
<pre>
git config --get-all svn-remote.&lt;name&gt;.branches
git config --get-all svn-remote.&lt;name&gt;.tags
</pre>
</dl>
<p> where &lt;name&gt; is the name of the SVN repository as specified by the -R option to <i>init</i> (or &quot;svn&quot; by default).</dl>
<p> &#8211;username</p>
<dl>
<dt>
<dd> Specify the SVN username to perform the commit as. This option overrides the <i>username</i> configuration property.</dl>
<p> &#8211;commit-url</p>
<dl>
<dt>
<dd> Use the specified URL to connect to the destination Subversion repository. This is useful in cases where the source SVN repository is read-only. This option overrides configuration property <i>commiturl</i>. </p>
<dl>
<dt>
<dd>
<pre>
git config --get-all svn-remote.&lt;name&gt;.commiturl
</pre>
</dl>
</dl>
<p> &#8211;parents</p>
<dl>
<dt>
<dd> Create parent folders. This parameter is equivalent to the parameter &#8211;parents on svn cp commands and is useful for non-standard repository layouts.</dl>
</dl>
<p> <i>tag</i></p>
<dl>
<dt>
<dd> Create a tag in the SVN repository. This is a shorthand for <i>branch -t</i>.</dl>
<p> <i>log</i></p>
<dl>
<dt>
<dd> This should make it easy to look up svn log messages when svn users refer to -r/&#8211;revision numbers. </p>
<p> The following features from &#8216;svn log&#8217; are supported: </p>
<p> -r &lt;n&gt;[:&lt;n&gt;], &#8211;revision=&lt;n&gt;[:&lt;n&gt;]</p>
<dl>
<dt>
<dd> is supported, non-numeric args are not: HEAD, NEXT, BASE, PREV, etc &#8230;</dl>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
<dd> it&#8217;s not completely compatible with the &#8211;verbose output in svn log, but reasonably close.</dl>
<p> &#8211;limit=&lt;n&gt;</p>
<dl>
<dt>
<dd> is NOT the same as &#8211;max-count, doesn&#8217;t count merged/excluded commits</dl>
<p> &#8211;incremental</p>
<dl>
<dt>
<dd> supported</dl>
<p> New features: </p>
<p> &#8211;show-commit</p>
<dl>
<dt>
<dd> shows the Git commit sha1, as well</dl>
<p> &#8211;oneline</p>
<dl>
<dt>
<dd> our version of &#8211;pretty=oneline</dl>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 SVN itself only stores times in UTC and nothing else. The regular svn client converts the UTC time to the local time (or based on the TZ= environment). This command has the same behaviour. </p>
</dl>
<p> Any other arguments are passed directly to <i>git log</i></dl>
<p> <i>blame</i></p>
<dl>
<dt>
<dd> Show what revision and author last modified each line of a file. The output of this mode is format-compatible with the output of &#8216;svn blame&#8217; by default. Like the SVN blame command, local uncommitted changes in the working tree are ignored; the version of the file in the HEAD revision is annotated. Unknown arguments are passed directly to <i>git blame</i>. </p>
<p> &#8211;git-format</p>
<dl>
<dt>
<dd> Produce output in the same format as <i>git blame</i>, but with SVN revision numbers instead of Git commit hashes. In this mode, changes that haven&#8217;t been committed to SVN (including local working-copy edits) are shown as revision 0.</dl>
</dl>
<p> <i>find-rev</i></p>
<dl>
<dt>
<dd> When given an SVN revision number of the form <i>rN</i>, returns the corresponding Git commit hash (this can optionally be followed by a tree-ish to specify which branch should be searched). When given a tree-ish, returns the corresponding SVN revision number. </p>
<p> &#8211;before</p>
<dl>
<dt>
<dd> Don&#8217;t require an exact match if given an SVN revision, instead find the commit corresponding to the state of the SVN repository (on the current branch) at the specified revision.</dl>
<p> &#8211;after</p>
<dl>
<dt>
<dd> Don&#8217;t require an exact match if given an SVN revision; if there is not an exact match return the closest match searching forward in the history.</dl>
</dl>
<p> <i>set-tree</i></p>
<dl>
<dt>
<dd> You should consider using <i>dcommit</i> instead of this command. Commit specified commit or tree objects to SVN. This relies on your imported fetch data being up-to-date. This makes absolutely no attempts to do patching when committing to SVN, it simply overwrites files with those specified in the tree or commit. All merging is assumed to have taken place independently of <i>git svn</i> functions.</dl>
<p> <i>create-ignore</i></p>
<dl>
<dt>
<dd> Recursively finds the svn:ignore property on directories and creates matching .gitignore files. The resulting files are staged to be committed, but are not committed. Use -r/&#8211;revision to refer to a specific revision.</dl>
<p> <i>show-ignore</i></p>
<dl>
<dt>
<dd> Recursively finds and lists the svn:ignore property on directories. The output is suitable for appending to the $GIT_DIR/info/exclude file.</dl>
<p> <i>mkdirs</i></p>
<dl>
<dt>
<dd> Attempts to recreate empty directories that core Git cannot track based on information in $GIT_DIR/svn/&lt;refname&gt;/unhandled.log files. Empty directories are automatically recreated when using &quot;git svn clone&quot; and &quot;git svn rebase&quot;, so &quot;mkdirs&quot; is intended for use after commands like &quot;git checkout&quot; or &quot;git reset&quot;. (See the svn-remote.&lt;name&gt;.automkdirs config file option for more information.)</dl>
<p> <i>commit-diff</i></p>
<dl>
<dt>
<dd> Commits the diff of two tree-ish arguments from the command-line. This command does not rely on being inside an git svn init-ed repository. This command takes three arguments, (a) the original tree to diff against, (b) the new tree result, (c) the URL of the target Subversion repository. The final argument (URL) may be omitted if you are working from a <i>git svn</i>-aware repository (that has been init-ed with <i>git svn</i>). The -r&lt;revision&gt; option is required for this.</dl>
<p> <i>info</i></p>
<dl>
<dt>
<dd> Shows information about a file or directory similar to what &#8216;svn info&#8217; provides. Does not currently support a -r/&#8211;revision argument. Use the &#8211;url option to output only the value of the <i>URL:</i> field.</dl>
<p> <i>proplist</i></p>
<dl>
<dt>
<dd> Lists the properties stored in the Subversion repository about a given file or directory. Use -r/&#8211;revision to refer to a specific Subversion revision.</dl>
<p> <i>propget</i></p>
<dl>
<dt>
<dd> Gets the Subversion property given as the first argument, for a file. A specific revision can be specified with -r/&#8211;revision.</dl>
<p> <i>show-externals</i></p>
<dl>
<dt>
<dd> Shows the Subversion externals. Use -r/&#8211;revision to specify a specific revision.</dl>
<p> <i>gc</i></p>
<dl>
<dt>
<dd> Compress $GIT_DIR/svn/&lt;refname&gt;/unhandled.log files in .git/svn and remove $GIT_DIR/svn/&lt;refname&gt;index files in .git/svn.</dl>
<p> <i>reset</i></p>
<dl>
<dt>
<dd> Undoes the effects of <i>fetch</i> back to the specified revision. This allows you to re-<i>fetch</i> an SVN revision. Normally the contents of an SVN revision should never change and <i>reset</i> should not be necessary. However, if SVN permissions change, or if you alter your &#8211;ignore-paths option, a <i>fetch</i> may fail with &quot;not found in commit&quot; (file not previously visible) or &quot;checksum mismatch&quot; (missed a modification). If the problem file cannot be ignored forever (with &#8211;ignore-paths) the only way to repair the repo is to use <i>reset</i>. </p>
<p> Only the rev_map and refs/remotes/git-svn are changed. Follow <i>reset</i> with a <i>fetch</i> and then <i>git reset</i> or <i>git rebase</i> to move local branches onto the new tree. </p>
<p> -r &lt;n&gt;, &#8211;revision=&lt;n&gt;</p>
<dl>
<dt>
<dd> Specify the most recent revision to keep. All later revisions are discarded.</dl>
<p> -p, &#8211;parent</p>
<dl>
<dt>
<dd> Discard the specified revision as well, keeping the nearest parent instead.</dl>
<p> Example:</p>
<dl>
<dt>
<dd> Assume you have local changes in &quot;master&quot;, but you need to refetch &quot;r2&quot;. </p>
<dl>
<dt>
<dd>
<pre>
    r1---r2---r3 remotes/git-svn
                \
                 A---B master
</pre>
</dl>
<p> Fix the ignore-paths or SVN permissions problem that caused &quot;r2&quot; to be incomplete in the first place. Then: </p>
<dl>
<dt>
<dd>
<pre>
git svn reset -r2 -p
git svn fetch
</pre>
</dl>
<dl>
<dt>
<dd>
r1&#8211; &#8211; r2 &#8216;&#8211;r3&#8217; remotes / git &#8211; svn</p>
<p>                                     r2&#8211; &#8211;<br />
    r3&#8211; &#8211; A&#8211; &#8211; B master
</dl>
<p> Then fixup &quot;master&quot; with <i>git rebase</i>. Do NOT use <i>git merge</i> or your history will not be compatible with a future <i>dcommit</i>! </p>
<dl>
<dt>
<dd>
<pre>
git rebase --onto remotes/git-svn A^ master
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
    r1---r2'--r3' remotes/git-svn
                \
                 A'--B' master
</pre>
</dl>
</dl>
</dl>
<h2>OPTIONS</h2>
<p> &#8211;shared[=(false|true|umask|group|all|world|everybody)], &#8211;template=&lt;template_directory&gt;</p>
<dl>
<dt>
<dd> Only used with the <i>init</i> command. These are passed directly to <i>git init</i>.</dl>
<p> -r &lt;arg&gt;, &#8211;revision &lt;arg&gt;</p>
<dl>
<dt>
<dd> Used with the <i>fetch</i> command. </p>
<p> This allows revision ranges for partial/cauterized history to be supported. $NUMBER, $NUMBER1:$NUMBER2 (numeric ranges), $NUMBER:HEAD, and BASE:$NUMBER are all supported. </p>
<p> This can allow you to make partial mirrors when running fetch; but is generally not recommended because history will be skipped and lost.</dl>
<p> -, &#8211;stdin</p>
<dl>
<dt>
<dd> Only used with the <i>set-tree</i> command. </p>
<p> Read a list of commits from stdin and commit them in reverse order. Only the leading sha1 is read from each line, so <i>git rev-list &#8211;pretty=oneline</i> output can be used.</dl>
<p> &#8211;rmdir</p>
<dl>
<dt>
<dd> Only used with the <i>dcommit</i>, <i>set-tree</i> and <i>commit-diff</i> commands. </p>
<p> Remove directories from the SVN tree if there are no files left behind. SVN can version empty directories, and they are not removed by default if there are no files left in them. Git cannot version empty directories. Enabling this flag will make the commit to SVN act like Git. </p>
<dl>
<dt>
<dd>
<pre>
config key: svn.rmdir
</pre>
</dl>
</dl>
<p> -e, &#8211;edit</p>
<dl>
<dt>
<dd> Only used with the <i>dcommit</i>, <i>set-tree</i> and <i>commit-diff</i> commands. </p>
<p> Edit the commit message before committing to SVN. This is off by default for objects that are commits, and forced on when committing tree objects. </p>
<dl>
<dt>
<dd>
<pre>
config key: svn.edit
</pre>
</dl>
</dl>
<p> -l&lt;num&gt;, &#8211;find-copies-harder</p>
<dl>
<dt>
<dd> Only used with the <i>dcommit</i>, <i>set-tree</i> and <i>commit-diff</i> commands. </p>
<p> They are both passed directly to <i>git diff-tree</i>; see <code><a href="/docs/linux/man/1-git-diff-tree/">git-diff-tree</a></code>(1) for more information. </p>
<dl>
<dt>
<dd>
<pre>
config key: svn.l
config key: svn.findcopiesharder
</pre>
</dl>
</dl>
<p> -A&lt;filename&gt;, &#8211;authors-file=&lt;filename&gt;</p>
<dl>
<dt>
<dd> Syntax is compatible with the file used by <i>git cvsimport</i>: </p>
<dl>
<dt>
<dd>
<pre>
        loginname = Joe User &lt;user [at] example.com&gt;
</pre>
</dl>
<p> If this option is specified and <i>git svn</i> encounters an SVN committer name that does not exist in the authors-file, <i>git svn</i> will abort operation. The user will then have to add the appropriate entry. Re-running the previous <i>git svn</i> command after the authors-file is modified should continue operation. </p>
<dl>
<dt>
<dd>
<pre>
config key: svn.authorsfile
</pre>
</dl>
</dl>
<p> &#8211;authors-prog=&lt;filename&gt;</p>
<dl>
<dt>
<dd> If this option is specified, for each SVN committer name that does not exist in the authors file, the given file is executed with the committer name as the first argument. The program is expected to return a single line of the form &quot;Name &lt;email&gt;&quot;, which will be treated as if included in the authors file.</dl>
<p> -q, &#8211;quiet</p>
<dl>
<dt>
<dd> Make <i>git svn</i> less verbose. Specify a second time to make it even less verbose.</dl>
<p> &#8211;repack[=&lt;n&gt;], &#8211;repack-flags=&lt;flags&gt;</p>
<dl>
<dt>
<dd> These should help keep disk usage sane for large fetches with many revisions. </p>
<p> &#8211;repack takes an optional argument for the number of revisions to fetch before repacking. This defaults to repacking every 1000 commits fetched if no argument is specified. </p>
<p> &#8211;repack-flags are passed directly to <i>git repack</i>. </p>
<dl>
<dt>
<dd>
<pre>
config key: svn.repack
config key: svn.repackflags
</pre>
</dl>
</dl>
<p> -m, &#8211;merge, -s&lt;strategy&gt;, &#8211;strategy=&lt;strategy&gt;, -p, &#8211;preserve-merges</p>
<dl>
<dt>
<dd> These are only used with the <i>dcommit</i> and <i>rebase</i> commands. </p>
<p> Passed directly to <i>git rebase</i> when using <i>dcommit</i> if a <i>git reset</i> cannot be used (see <i>dcommit</i>).</dl>
<p> -n, &#8211;dry-run</p>
<dl>
<dt>
<dd> This can be used with the <i>dcommit</i>, <i>rebase</i>, <i>branch</i> and <i>tag</i> commands. </p>
<p> For <i>dcommit</i>, print out the series of Git arguments that would show which diffs would be committed to SVN. </p>
<p> For <i>rebase</i>, display the local branch associated with the upstream svn repository associated with the current branch and the URL of svn repository that will be fetched from. </p>
<p> For <i>branch</i> and <i>tag</i>, display the urls that will be used for copying when creating the branch or tag.</dl>
<p> &#8211;use-log-author</p>
<dl>
<dt>
<dd> When retrieving svn commits into Git (as part of <i>fetch</i>, <i>rebase</i>, or <i>dcommit</i> operations), look for the first From: or Signed-off-by: line in the log message and use that as the author string.</dl>
<p> &#8211;add-author-from</p>
<dl>
<dt>
<dd> When committing to svn from Git (as part of <i>commit-diff</i>, <i>set-tree</i> or <i>dcommit</i> operations), if the existing log message doesn&#8217;t already have a From: or Signed-off-by: line, append a From: line based on the Git commit&#8217;s author string. If you use this, then &#8211;use-log-author will retrieve a valid author string for all commits.</dl>
<h2>ADVANCED OPTIONS</h2>
<p> -i&lt;GIT_SVN_ID&gt;, &#8211;id &lt;GIT_SVN_ID&gt;</p>
<dl>
<dt>
<dd> This sets GIT_SVN_ID (instead of using the environment). This allows the user to override the default refname to fetch from when tracking a single URL. The <i>log</i> and <i>dcommit</i> commands no longer require this switch as an argument.</dl>
<p> -R&lt;remote name&gt;, &#8211;svn-remote &lt;remote name&gt;</p>
<dl>
<dt>
<dd> Specify the [svn-remote &quot;&lt;remote name&gt;&quot;] section to use, this allows SVN multiple repositories to be tracked. Default: &quot;svn&quot;</dl>
<p> &#8211;follow-parent</p>
<dl>
<dt>
<dd> This option is only relevant if we are tracking branches (using one of the repository layout options &#8211;trunk, &#8211;tags, &#8211;branches, &#8211;stdlayout). For each tracked branch, try to find out where its revision was copied from, and set a suitable parent in the first Git commit for the branch. This is especially helpful when we&#8217;re tracking a directory that has been moved around within the repository. If this feature is disabled, the branches created by <i>git svn</i> will all be linear and not share any history, meaning that there will be no information on where branches were branched off or merged. However, following long/convoluted histories can take a long time, so disabling this feature may speed up the cloning process. This feature is enabled by default, use &#8211;no-follow-parent to disable it. </p>
<dl>
<dt>
<dd>
<pre>
config key: svn.followparent
</pre>
</dl>
</dl>
<h2>CONFIG FILE-ONLY OPTIONS</h2>
<p> svn.noMetadata, svn-remote.&lt;name&gt;.noMetadata</p>
<dl>
<dt>
<dd> This gets rid of the <i>git-svn-id:</i> lines at the end of every commit. </p>
<p> This option can only be used for one-shot imports as <i>git svn</i> will not be able to fetch again without metadata. Additionally, if you lose your .git/svn/<code>*/.rev_map.</code> files, <i>git svn</i> will not be able to rebuild them. </p>
<p> The <i>git svn log</i> command will not work on repositories using this, either. Using this conflicts with the <i>useSvmProps</i> option for (hopefully) obvious reasons. </p>
<p> This option is NOT recommended as it makes it difficult to track down old references to SVN revision numbers in existing documentation, bug reports and archives. If you plan to eventually migrate from SVN to Git and are certain about dropping SVN history, consider <code><a href="/docs/linux/man/1-git-filter-branch/">git-filter-branch</a></code>(1) instead. filter-branch also allows reformatting of metadata for ease-of-reading and rewriting authorship info for non-&quot;svn.authorsFile&quot; users.</dl>
<p> svn.useSvmProps, svn-remote.&lt;name&gt;.useSvmProps</p>
<dl>
<dt>
<dd> This allows <i>git svn</i> to re-map repository URLs and UUIDs from mirrors created using SVN::Mirror (or svk) for metadata. </p>
<p> If an SVN revision has a property, &quot;svm:headrev&quot;, it is likely that the revision was created by SVN::Mirror (also used by SVK). The property contains a repository UUID and a revision. We want to make it look like we are mirroring the original URL, so introduce a helper function that returns the original identity URL and UUID, and use it when generating metadata in commit messages.</dl>
<p> svn.useSvnsyncProps, svn-remote.&lt;name&gt;.useSvnsyncprops</p>
<dl>
<dt>
<dd> Similar to the useSvmProps option; this is for users of the <a href="/docs/linux/man/1-svnsync/">svnsync</a>(1) command distributed with SVN 1.4.x and later.</dl>
<p> svn-remote.&lt;name&gt;.rewriteRoot</p>
<dl>
<dt>
<dd> This allows users to create repositories from alternate URLs. For example, an administrator could run <i>git svn</i> on the server locally (accessing via file://) but wish to distribute the repository with a public http:// or svn:// URL in the metadata so users of it will see the public URL.</dl>
<p> svn-remote.&lt;name&gt;.rewriteUUID</p>
<dl>
<dt>
<dd> Similar to the useSvmProps option; this is for users who need to remap the UUID manually. This may be useful in situations where the original UUID is not available via either useSvmProps or useSvnsyncProps.</dl>
<p> svn-remote.&lt;name&gt;.pushurl</p>
<dl>
<dt>
<dd> Similar to Git&#8217;s <i>remote.&lt;name&gt;.pushurl</i>, this key is designed to be used in cases where <i>url</i> points to an SVN repository via a read-only transport, to provide an alternate read/write transport. It is assumed that both keys point to the same repository. Unlike <i>commiturl</i>, <i>pushurl</i> is a base path. If either <i>commiturl</i> or <i>pushurl</i> could be used, <i>commiturl</i> takes precedence.</dl>
<p> svn.brokenSymlinkWorkaround</p>
<dl>
<dt>
<dd> This disables potentially expensive checks to workaround broken symlinks checked into SVN by broken clients. Set this option to &quot;false&quot; if you track a SVN repository with many empty blobs that are not symlinks. This option may be changed while <i>git svn</i> is running and take effect on the next revision fetched. If unset, <i>git svn</i> assumes this option to be &quot;true&quot;.</dl>
<p> svn.pathnameencoding</p>
<dl>
<dt>
<dd> This instructs git svn to recode pathnames to a given encoding. It can be used by windows users and by those who work in non-utf8 locales to avoid corrupted file names with non-ASCII characters. Valid encodings are the ones supported by Perl&#8217;s Encode module.</dl>
<p> svn-remote.&lt;name&gt;.automkdirs</p>
<dl>
<dt>
<dd> Normally, the &quot;git svn clone&quot; and &quot;git svn rebase&quot; commands attempt to recreate empty directories that are in the Subversion repository. If this option is set to &quot;false&quot;, then empty directories will only be created if the &quot;git svn mkdirs&quot; command is run explicitly. If unset, <i>git svn</i> assumes this option to be &quot;true&quot;.</dl>
<p> Since the noMetadata, rewriteRoot, rewriteUUID, useSvnsyncProps and useSvmProps options all affect the metadata generated and used by <i>git svn</i>; they <code>must</code> be set in the configuration file before any history is imported and these settings should never be changed once they are set. </p>
<p> Additionally, only one of these options can be used per svn-remote section because they affect the <i>git-svn-id:</i> metadata line, except for rewriteRoot and rewriteUUID which can be used together.</p>
<h2>BASIC EXAMPLES</h2>
<p> Tracking and contributing to the trunk of a Subversion-managed project (ignoring tags and branches): </p>
<dl>
<dt>
<dd>
<pre>
# Clone a repo (like git clone):
        git svn clone <a rel="nofollow" href="http://svn.example.com/project/trunk">http://svn.example.com/project/trunk</a>
# Enter the newly cloned directory:
        cd trunk
# You should be on master branch, double-check with 'git branch'
        git branch
# Do some work and commit locally to Git:
        git commit ...
# Something is committed to SVN, rebase your local changes against the
# latest changes in SVN:
        git svn rebase
# Now commit your changes (that were committed previously using Git) to SVN,
# as well as automatically updating your working HEAD:
        git svn dcommit
# Append svn:ignore settings to the default Git exclude file:
        git svn show-ignore &gt;&gt; .git/info/exclude
</pre>
</dl>
<p> Tracking and contributing to an entire Subversion-managed project (complete with a trunk, tags and branches): </p>
<dl>
<dt>
<dd>
<pre>
# Clone a repo with standard SVN directory layout (like git clone):
        git svn clone <a rel="nofollow" href="http://svn.example.com/project">http://svn.example.com/project</a> --stdlayout
# Or, if the repo uses a non-standard directory layout:
        git svn clone <a rel="nofollow" href="http://svn.example.com/project">http://svn.example.com/project</a> -T tr -b branch -t tag
# View all branches and tags you have cloned:
        git branch -r
# Create a new branch in SVN
    git svn branch waldo
# Reset your master to trunk (or any other branch, replacing 'trunk'
# with the appropriate name):
        git reset --hard remotes/trunk
# You may only dcommit to one branch/tag/trunk at a time.  The usage
# of dcommit/rebase/show-ignore should be the same as above.
</pre>
</dl>
<p> The initial <i>git svn clone</i> can be quite time-consuming (especially for large Subversion repositories). If multiple people (or one person with multiple machines) want to use <i>git svn</i> to interact with the same Subversion repository, you can do the initial <i>git svn clone</i> to a repository on a server and have each person clone that repository with <i>git clone</i>: </p>
<dl>
<dt>
<dd>
#Do the initial import on a server<br />
ssh server &#8220;cd /pub &amp;&amp; git svn clone http://svn.example.com/project<br />
#Clone locally &#8211; make sure the refs / remotes / space matches the server<br />
        mkdir project<br />
            cd project<br />
                git init<br />
                    git remote add origin server : /<br />
                                                   pub / project git config&#8211; replace &#8211;<br />
    all remote.origin.fetch &#8216;+refs/remotes/*:refs/remotes/*&#8217; git fetch<br />
#Prevent fetch / pull from remote Git server in the future,<br />
#we only want to use git svn for future updates<br />
        git config&#8211; remove &#8211;<br />
    section remote.origin<br />
#Create a local branch from one of the branches just fetched<br />
        git checkout &#8211;<br />
    b master FETCH_HEAD<br />
#Initialize &#8216;git svn&#8217; locally(be sure to use the same URL and -T / -b / -t options as were used on server)<br />
        git svn init http : // svn.example.com/project<br />
#Pull the latest changes from Subversion<br />
                            git svn rebase
</dl>
<h2>REBASE VS. PULL/MERGE</h2>
<p> Prefer to use <i>git svn rebase</i> or <i>git rebase</i>, rather than <i>git pull</i> or <i>git merge</i> to synchronize unintegrated commits with a <i>git svn</i> branch. Doing so will keep the history of unintegrated commits linear with respect to the upstream SVN repository and allow the use of the preferred <i>git svn dcommit</i> subcommand to push unintegrated commits back into SVN. </p>
<p> Originally, <i>git svn</i> recommended that developers pulled or merged from the <i>git svn</i> branch. This was because the author favored git svn set-tree B to commit a single head rather than the git svn set-tree A..B notation to commit multiple commits. Use of <i>git pull</i> or <i>git merge</i> with git svn set-tree A..B will cause non-linear history to be flattened when committing into SVN and this can lead to merge commits unexpectedly reversing previous commits in SVN.</p>
<h2>MERGE TRACKING</h2>
<p> While <i>git svn</i> can track copy history (including branches and tags) for repositories adopting a standard layout, it cannot yet represent merge history that happened inside git back upstream to SVN users. Therefore it is advised that users keep history as linear as possible inside Git to ease compatibility with SVN (see the CAVEATS section below).</p>
<h2>HANDLING OF SVN BRANCHES</h2>
<p> If <i>git svn</i> is configured to fetch branches (and &#8211;follow-branches is in effect), it sometimes creates multiple Git branches for one SVN branch, where the additional branches have names of the form <i>branchname@nnn</i> (with nnn an SVN revision number). These additional branches are created if <i>git svn</i> cannot find a parent commit for the first commit in an SVN branch, to connect the branch to the history of the other branches. </p>
<p> Normally, the first commit in an SVN branch consists of a copy operation. <i>git svn</i> will read this commit to get the SVN revision the branch was created from. It will then try to find the Git commit that corresponds to this SVN revision, and use that as the parent of the branch. However, it is possible that there is no suitable Git commit to serve as parent. This will happen, among other reasons, if the SVN branch is a copy of a revision that was not fetched by <i>git svn</i> (e.g. because it is an old revision that was skipped with <i>&#8211;revision</i>), or if in SVN a directory was copied that is not tracked by <i>git svn</i> (such as a branch that is not tracked at all, or a subdirectory of a tracked branch). In these cases, <i>git svn</i> will still create a Git branch, but instead of using an existing Git commit as the parent of the branch, it will read the SVN history of the directory the branch was copied from and create appropriate Git commits. This is indicated by the message &quot;Initializing parent: &lt;branchname&gt;&quot;. </p>
<p> Additionally, it will create a special branch named <i>&lt;branchname&gt;@&lt;SVN-Revision&gt;</i>, where &lt;SVN-Revision&gt; is the SVN revision number the branch was copied from. This branch will point to the newly created parent commit of the branch. If in SVN the branch was deleted and later recreated from a different version, there will be multiple such branches with an <i>@</i>. </p>
<p> Note that this may mean that multiple Git commits are created for a single SVN revision. </p>
<p> An example: in an SVN repository with a standard trunk/tags/branches layout, a directory trunk/sub is created in r.100. In r.200, trunk/sub is branched by copying it to branches/. <i>git svn clone -s</i> will then create a branch <i>sub</i>. It will also create new Git commits for r.100 through r.199 and use these as the history of branch <i>sub</i>. Thus there will be two Git commits for each revision from r.100 to r.199 (one containing trunk/, one containing trunk/sub/). Finally, it will create a branch <i>sub@200</i> pointing to the new parent commit of branch <i>sub</i> (i.e. the commit for r.200 and trunk/sub/).</p>
<h2>CAVEATS</h2>
<p> For the sake of simplicity and interoperating with Subversion, it is recommended that all <i>git svn</i> users clone, fetch and dcommit directly from the SVN server, and avoid all <i>git clone</i>/<i>pull</i>/<i>merge</i>/<i>push</i> operations between Git repositories and branches. The recommended method of exchanging code between Git branches and users is <i>git format-patch</i> and <i>git am</i>, or just &#8216;dcommit&#8217;ing to the SVN repository. </p>
<p> Running <i>git merge</i> or <i>git pull</i> is NOT recommended on a branch you plan to <i>dcommit</i> from because Subversion users cannot see any merges you&#8217;ve made. Furthermore, if you merge or pull from a Git branch that is a mirror of an SVN branch, <i>dcommit</i> may commit to the wrong branch. </p>
<p> If you do merge, note the following rule: <i>git svn dcommit</i> will attempt to commit on top of the SVN commit named in </p>
<dl>
<dt>
<dd>
<pre>
git log --grep=^git-svn-id: --first-parent -1
</pre>
</dl>
<p> You <i>must</i> therefore ensure that the most recent commit of the branch you want to dcommit to is the <i>first</i> parent of the merge. Chaos will ensue otherwise, especially if the first parent is an older commit on the same SVN branch. </p>
<p> <i>git clone</i> does not clone branches under the refs/remotes/ hierarchy or any <i>git svn</i> metadata, or config. So repositories created and managed with using <i>git svn</i> should use <i>rsync</i> for cloning, if cloning is to be done at all. </p>
<p> Since <i>dcommit</i> uses rebase internally, any Git branches you <i>git push</i> to before <i>dcommit</i> on will require forcing an overwrite of the existing ref on the remote repository. This is generally considered bad practice, see the <code><a href="/docs/linux/man/1-git-push/">git-push</a></code>(1) documentation for details. </p>
<p> Do not use the &#8211;amend option of <code><a href="/docs/linux/man/1-git-commit/">git-commit</a></code>(1) on a change you&#8217;ve already dcommitted. It is considered bad practice to &#8211;amend commits you&#8217;ve already pushed to a remote repository for other users, and dcommit with SVN is analogous to that. </p>
<p> When cloning an SVN repository, if none of the options for describing the repository layout is used (&#8211;trunk, &#8211;tags, &#8211;branches, &#8211;stdlayout), <i>git svn clone</i> will create a Git repository with completely linear history, where branches and tags appear as separate directories in the working copy. While this is the easiest way to get a copy of a complete repository, for projects with many branches it will lead to a working copy many times larger than just the trunk. Thus for projects using the standard directory structure (trunk/branches/tags), it is recommended to clone with option <i>&#8211;stdlayout</i>. If the project uses a non-standard structure, and/or if branches and tags are not required, it is easiest to only clone one directory (typically trunk), without giving any repository layout options. If the full history with branches and tags is required, the options <i>&#8211;trunk</i> / <i>&#8211;branches</i> / <i>&#8211;tags</i> must be used. </p>
<p> When using multiple &#8211;branches or &#8211;tags, <i>git svn</i> does not automatically handle name collisions (for example, if two branches from different paths have the same name, or if a branch and a tag have the same name). In these cases, use <i>init</i> to set up your Git repository then, before your first <i>fetch</i>, edit the .git/config file so that the branches and tags are associated with different name spaces. For example: </p>
<dl>
<dt>
<dd>
<pre>
branches = stable/*:refs/remotes/svn/stable/*
branches = debug/*:refs/remotes/svn/debug/*
</pre>
</dl>
<h2>BUGS</h2>
<p> We ignore all SVN properties except svn:executable. Any unhandled properties are logged to $GIT_DIR/svn/&lt;refname&gt;/unhandled.log </p>
<p> Renamed and copied directories are not detected by Git and hence not tracked when committing to SVN. I do not plan on adding support for this as it&#8217;s quite difficult and time-consuming to get working for all the possible corner cases (Git doesn&#8217;t do it, either). Committing renamed and copied files is fully supported if they&#8217;re similar enough for Git to detect them. </p>
<p> In SVN, it is possible (though discouraged) to commit changes to a tag (because a tag is just a directory copy, thus technically the same as a branch). When cloning an SVN repository, <i>git svn</i> cannot know if such a commit to a tag will happen in the future. Thus it acts conservatively and imports all SVN tags as branches, prefixing the tag name with <i>tags/</i>.</p>
<h2>CONFIGURATION</h2>
<p> <i>git svn</i> stores [svn-remote] configuration information in the repository .git/config file. It is similar the core Git [remote] sections except <i>fetch</i> keys do not accept glob arguments; but they are instead handled by the <i>branches</i> and <i>tags</i> keys. Since some SVN repositories are oddly configured with multiple projects glob expansions such those listed below are allowed: </p>
<dl>
<dt>
<dd>
<pre>
[svn-remote &quot;project-a&quot;]
        url = <a rel="nofollow" href="http://server.org/svn">http://server.org/svn</a>
        fetch = trunk/project-a:refs/remotes/project-a/trunk
        branches = branches/*/project-a:refs/remotes/project-a/branches/*
        tags = tags/*/project-a:refs/remotes/project-a/tags/*
</pre>
</dl>
<p> Keep in mind that the <i>*</i> (asterisk) wildcard of the local ref (right of the <i>:</i>) <code>must</code> be the farthest right path component; however the remote wildcard may be anywhere as long as it&#8217;s an independent path component (surrounded by <i>/</i> or EOL). This type of configuration is not automatically created by <i>init</i> and should be manually entered with a text-editor or using <i>git config</i>. </p>
<p> It is also possible to fetch a subset of branches or tags by using a comma-separated list of names within braces. For example: </p>
<dl>
<dt>
<dd>
<pre><code>
[svn - remote "huge-project"] url = http : // server.org/svn
                                           fetch = trunk / src : refs / remotes / trunk branches = branches / {red, green} / src : refs / remotes / branches/*
        tags = tags/{1.0,2.0}/src:refs/remotes/tags/*
</code></pre>
</dl>
<p> Multiple fetch, branches, and tags keys are supported: </p>
<dl>
<dt>
<dd>
<pre>
[svn-remote &quot;messy-repo&quot;]
        url = <a rel="nofollow" href="http://server.org/svn">http://server.org/svn</a>
        fetch = trunk/project-a:refs/remotes/project-a/trunk
        fetch = branches/demos/june-project-a-demo:refs/remotes/project-a/demos/june-demo
        branches = branches/server/*:refs/remotes/project-a/branches/*
        branches = branches/demos/2011/*:refs/remotes/project-a/2011-demos/*
        tags = tags/server/*:refs/remotes/project-a/tags/*
</pre>
</dl>
<p> Creating a branch in such a configuration requires disambiguating which location to use using the -d or &#8211;destination flag: </p>
<dl>
<dt>
<dd>
<pre>
$ git svn branch -d branches/server release-2-3-0
</pre>
</dl>
<p> Note that git-svn keeps track of the highest revision in which a branch or tag has appeared. If the subset of branches or tags is changed after fetching, then .git/svn/.metadata must be manually edited to remove (or reset) branches-maxRev and/or tags-maxRev as appropriate.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-rebase/">git-rebase</a></code>(1)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>

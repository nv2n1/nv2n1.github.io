---
title: "hg(1)"
name: "hg"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hg/"
description: "hg – Mercurial source code management system"
---

<h2>NAME</h2>
<p> hg &#8211; Mercurial source code management system</p>
<h2>SYNOPSIS</h2>
<p> <code>hg</code> <i>command</i> [<i>option</i>]&#8230; [<i>argument</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> The <code>hg</code> command provides a command line interface to the Mercurial system.</p>
<h2>COMMAND ELEMENTS</h2>
<dl>
<dt><code>files&#8230;</code></p>
<dd> indicates one or more filename or relative path filenames; see File Name Patterns: for information on pattern matching</p>
<dt><code>path</code></p>
<dd> indicates a path on the local machine</p>
<dt><code>revision</code></p>
<dd> indicates a changeset which can be specified as a changeset revision number, a tag, or a unique substring of the changeset hash value</p>
<dt><code>repository path</code></p>
<dd> either the pathname of a local repository or the URI of a remote repository.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-R, &#8211;repository</code></p>
<dd> repository root directory or name of overlay bundle file</p>
<dt><code>&#8211;cwd</code></p>
<dd> change working directory</p>
<dt><code>-y, &#8211;noninteractive</code></p>
<dd> do not prompt, automatically pick the first choice for all prompts</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> suppress output</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> enable additional output</p>
<dt><code>&#8211;config</code></p>
<dd> set/override config option (use &#8216;section.name=value&#8217;)</p>
<dt><code>&#8211;debug</code></p>
<dd> enable debugging output</p>
<dt><code>&#8211;debugger</code></p>
<dd> start debugger</p>
<dt><code>&#8211;encoding</code></p>
<dd> set the charset encoding (default: ascii)</p>
<dt><code>&#8211;encodingmode</code></p>
<dd> set the charset encoding mode (default: strict)</p>
<dt><code>&#8211;traceback</code></p>
<dd> always print a traceback on exception</p>
<dt><code>&#8211;time</code></p>
<dd> time how long the command takes</p>
<dt><code>&#8211;profile</code></p>
<dd> print command execution profile</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</p>
<dt><code>-h, &#8211;help</code></p>
<dd> display help and exit</p>
<dt><code>&#8211;hidden</code></p>
<dd> consider hidden changesets</dl>
<h2>COMMANDS</h2>
<h3>add</h3>
<pre><code>
hg add[OPTION]...[FILE]...
</code></pre>
<p> Schedule files to be version controlled and added to the repository. </p>
<p> The files will be added to the repository at the next commit. To undo an add before that, see <code>hg forget</code>:. </p>
<p> If no names are given, add all files to the repository. </p>
<p> An example showing how new (unknown) files are added automatically by <code>hg add</code>:: </p>
<pre>
$ ls
foo.c
$ hg status
? foo.c
$ hg add
adding foo.c
$ hg status
A foo.c
</pre>
<p> Returns 0 if all files are successfully added. </p>
<p> Options:</p>
<dl>
<dt><code>-I, &#8211;include</code></p>
<dd> include names matching the given patterns</p>
<dt><code>-X, &#8211;exclude</code></p>
<dd> exclude names matching the given patterns</p>
<dt><code>-S, &#8211;subrepos</code></p>
<dd> recurse into subrepositories</p>
<dt><code>-n, &#8211;dry-run</code></p>
<dd> do not perform actions, just print output</dl>
<h3>addremove</h3>
<p>hg addremove[OPTION]&#8230;[FILE]&#8230;</p>
<p> Add all new files and remove all missing files from the repository. </p>
<p> New files are ignored if they match any of the patterns in <code>.hgignore</code>. As with add, these changes take effect at the next commit. </p>
<p> Use the -s/&#8211;similarity option to detect renamed files. This option takes a percentage between 0 (disabled) and 100 (files must be identical) as its parameter. With a parameter greater than 0, this compares every removed file with every added file and records those similar enough as renames. Detecting renamed files this way can be expensive. After using this option, <code>hg status -C</code>: can be used to check which files were identified as moved or renamed. If not specified, -s/&#8211;similarity defaults to 100 and only renames of identical files are detected. </p>
<p> Returns 0 if all files are successfully added. </p>
<p> Options:</p>
<dl>
<dt><code>-s, &#8211;similarity</code></p>
<dd> guess renamed files by similarity (0&lt;=s&lt;=100)</p>
<dt><code>-I, &#8211;include</code></p>
<dd> include names matching the given patterns</p>
<dt><code>-X, &#8211;exclude</code></p>
<dd> exclude names matching the given patterns</p>
<dt><code>-n, &#8211;dry-run</code></p>
<dd> do not perform actions, just print output</dl>
<h3>annotate</h3>
<p>hg annotate[-r REV][-f][-a][-u][-d][-n][-c][-l] FILE&#8230;</p>
<p> List changes in files, showing the revision id responsible for each line </p>
<p> This command is useful for discovering when a change was made and by whom. </p>
<p> Without the -a/&#8211;text option, annotate will avoid processing files it detects as binary. With -a, annotate will annotate the file anyway, although the results will probably be neither useful nor desirable. </p>
<p> Returns 0 on success. </p>
<p> Options:</p>
<dl>
<dt><code>-r, &#8211;rev</code></p>
<dd> annotate the specified revision</p>
<dt><code>&#8211;follow</code></p>
<dd> follow copies/renames and list the filename (DEPRECATED)</p>
<dt><code>&#8211;no-follow</code></p>
<dd> don&#8217;t follow copies and renames</p>
<dt><code>-a, &#8211;text</code></p>
<dd> treat all files as text</p>
<dt><code>-u, &#8211;user</code></p>
<dd> list the author (long with -v)</p>
<dt><code>-f, &#8211;file</code></p>
<dd> list the filename</p>
<dt><code>-d, &#8211;date</code></p>
<dd> list the date (short with -q)</p>
<dt><code>-n, &#8211;number</code></p>
<dd> list the revision number (default)</p>
<dt><code>-c, &#8211;changeset</code></p>
<dd> list the changeset</p>
<dt><code>-l, &#8211;line-number</code></p>
<dd> show line number at the first appearance</p>
<dt><code>-w, &#8211;ignore-all-space</code></p>
<dd> ignore white space when comparing lines</p>
<dt><code>-b, &#8211;ignore-space-change</code></p>
<dd> ignore changes in the amount of white space</p>
<dt><code>-B, &#8211;ignore-blank-lines</code></p>
<dd> ignore changes whose lines are all blank</p>
<dt><code>-I, &#8211;include</code></p>
<dd> include names matching the given patterns</p>
<dt><code>-X, &#8211;exclude</code></p>
<dd> exclude names matching the given patterns </p>
<p> aliases: blame</dl>
<h3>archive</h3>
<pre>
hg archive [OPTION]... DEST
</pre>
<p> By default, the revision used is the parent of the working directory; use -r/&#8211;rev to specify a different revision. </p>
<p> The archive type is automatically detected based on file extension (or override using -t/&#8211;type). </p>
<p> Examples:</p>
<dl>
<dt>&bull;</p>
<dd> create a zip file containing the 1.0 release: </p>
<pre>
hg archive -r 1.0 project-1.0.zip
</pre>
<dt>&bull;</p>
<dd> create a tarball excluding .hg files: </p>
<pre>
hg archive project.tar.gz -X &quot;.hg*&quot;
</pre>
<p> Valid types are:</p>
<dt><code>files</code></p>
<dd>
<p> a directory full of files (default)</p>
<dt><code>tar</code></p>
<dd>
<p> tar archive, uncompressed</p>
<dt><code>tbz2</code></p>
<dd>
<p> tar archive, compressed using bzip2</p>
<dt><code>tgz</code></p>
<dd>
<p> tar archive, compressed using gzip</p>
<dt><code>uzip</code></p>
<dd>
<p> zip archive, uncompressed</p>
<dt><code>zip</code></p>
<dd>
<p> zip archive, compressed using deflate </p>
<p> The exact name of the destination archive or directory is given using a format string; see <code>hg help export</code>: for details. </p>
<p> Each member added to an archive file has a directory prefix prepended. Use -p/&#8211;prefix to specify a format string for the prefix. The default is the basename of the archive, with suffixes removed. </p>
<p> Returns 0 on success. </p>
<p> Options:</p>
<dt><code>&#8211;no-decode</code></p>
<dd> do not pass files through decoders</p>
<dt><code>-p, &#8211;prefix</code></p>
<dd> directory prefix for files in archive</p>
<dt><code>-r, &#8211;rev</code></p>
<dd> revision to distribute</p>
<dt><code>-t, &#8211;type</code></p>
<dd> type of distribution to create</p>
<dt><code>-S, &#8211;subrepos</code></p>
<dd> recurse into subrepositories</p>
<dt><code>-I, &#8211;include</code></p>
<dd> include names matching the given patterns</p>
<dt><code>-X, &#8211;exclude</code></p>
<dd> exclude names matching the given patterns</dl>
<h3>backout</h3>
<p>hg backout[OPTION]&#8230;[-r] REV</p>
<p> Prepare a new changeset with the effect of REV undone in the current working directory. </p>
<p> If REV is the parent of the working directory, then this new changeset is committed automatically. Otherwise, hg needs to merge the changes and the merged result is left uncommitted.</p>
<dl>
<dt>Note</p>
<dd> backout cannot be used to fix either an unwanted or incorrect merge. </p>
<p> By default, the pending changeset will have one parent, maintaining a linear history. With &#8211;merge, the pending changeset will instead have two parents: the old parent of the working directory and a new child of REV that simply undoes REV. </p>
<p> Before version 1.7, the behavior without &#8211;merge was equivalent to specifying &#8211;merge followed by <code>hg update &#8211;clean .</code>: to cancel the merge and leave the child of REV as a head to be merged separately. </p>
<p> See <code>hg help dates</code>: for a list of formats valid for -d/&#8211;date. </p>
<p> Returns 0 on success. </p>
<p> Options:</p>
<dt><code>&#8211;merge</code></p>
<dd> merge with old dirstate parent after backout</p>
<dt><code>&#8211;parent</code></p>
<dd> parent to choose when backing out merge (DEPRECATED)</p>
<dt><code>-r, &#8211;rev</code></p>
<dd> revision to backout</p>
<dt><code>-t, &#8211;tool</code></p>
<dd> specify merge tool</p>
<dt><code>-I, &#8211;include</code></p>
<dd> include names matching the given patterns</p>
<dt><code>-X, &#8211;exclude</code></p>
<dd> exclude names matching the given patterns</p>
<dt><code>-m, &#8211;message</code></p>
<dd> use text as commit message</p>
<dt><code>-l, &#8211;logfile</code></p>
<dd> read commit message from file</p>
<dt><code>-d, &#8211;date</code></p>
<dd> record the specified date as commit date</p>
<dt><code>-u, &#8211;user</code></p>
<dd> record the specified user as committer</dl>
<h3>bisect</h3>
<p>hg bisect[-gbsr][-U][-c CMD][REV]</p>
<p> This command helps to find changesets which introduce problems. To use, mark the earliest changeset you know exhibits the problem as bad, then mark the latest changeset which is free from the problem as good. Bisect will update your working directory to a revision for testing (unless the -U/&#8211;noupdate option is specified). Once you have performed tests, mark the working directory as good or bad, and bisect will either update to another candidate changeset or announce that it has found the bad revision. </p>
<p> As a shortcut, you can also use the revision argument to mark a revision as good or bad without checking it out first. </p>
<p> If you supply a command, it will be used for automatic bisection. The environment variable HG_NODE will contain the ID of the changeset being tested. The exit status of the command will be used to mark revisions as good or bad: status 0 means good, 125 means to skip the revision, 127 (command not found) will abort the bisection, and any other non-zero exit status means the revision is bad. </p>
<p> Some examples:</p>
<dl>
<dt>&bull;</p>
<dd> start a bisection with known bad revision 12, and good revision 34: </p>
<pre>
hg bisect --bad 34
hg bisect --good 12
</pre>
<dt>&bull;</p>
<dd> advance the current bisection by marking current revision as good or bad: </p>
<pre>
hg bisect --good
hg bisect --bad
</pre>
<dt>&bull;</p>
<dd> mark the current revision, or a known revision, to be skipped (e.g. if that revision is not usable because of another issue): </p>
<pre>
hg bisect --skip
hg bisect --skip 23
</pre>
<dt>&bull;</p>
<dd> skip all revisions that do not touch directories <code>foo</code> or <code>bar</code> </p>
<p> hg bisect &#8211;skip &#8216;!( file(&quot;path:foo&quot;) &amp; file(&quot;path:bar&quot;) )&#8217;</p>
<dt>&bull;</p>
<dd> forget the current bisection: </p>
<pre>
hg bisect --reset
</pre>
<dt>&bull;</p>
<dd> use &#8216;make &amp;&amp; make tests&#8217; to automatically find the first broken revision: </p>
<p>hg bisect&#8211; reset<br />
    hg bisect&#8211; bad 34 hg bisect&#8211; good 12 hg bisect&#8211; command &#8216;make &amp;&amp; make tests&#8217;</p>
<dt>&bull;</p>
<dd> see all changesets whose states are already known in the current bisection: </p>
<pre>
hg log -r &quot;bisect(pruned)&quot;
</pre>
<dt>&bull;</p>
<dd> see the changeset currently being bisected (especially useful if running with -U/&#8211;noupdate): </p>
<pre>
hg log -r &quot;bisect(current)&quot;
</pre>
<dt>&bull;</p>
<dd> see all changesets that took part in the current bisection: </p>
<pre>
hg log -r &quot;bisect(range)&quot;
</pre>
<dt>&bull;</p>
<dd> with the graphlog extension, you can even get a nice graph: </p>
<pre>
hg log --graph -r &quot;bisect(range)&quot;
</pre>
<p> See <code>hg help revsets</code>: for more about the <i>bisect()</i> keyword. </p>
<p> Returns 0 on success. </p>
<p> Options:</p>
<dt><code>-r, &#8211;reset</code></p>
<dd> reset bisect state</p>
<dt><code>-g, &#8211;good</code></p>
<dd> mark changeset good</p>
<dt><code>-b, &#8211;bad</code></p>
<dd> mark changeset bad</p>
<dt><code>-s, &#8211;skip</code></p>
<dd> skip testing changeset</p>
<dt><code>-e, &#8211;extend</code></p>
<dd> extend the bisect range</p>
<dt><code>-c, &#8211;command</code></p>
<dd> use command to check changeset state</p>
<dt><code>-U, &#8211;noupdate</code></p>
<dd> do not update to target</dl>
<h3>bookmarks</h3>
<p>hg bookmarks[-f][-d][-i][-m NAME][-r REV][NAME]</p>
<p> Bookmarks are pointers to certain commits that move when committing. Bookmarks are local. They can be renamed, copied and deleted. It is possible to use <code>hg merge NAME</code>: to merge from a given bookmark, and <code>hg update NAME</code>: to update to a given bookmark. </p>
<p> You can use <code>hg bookmark NAME</code>: to set a bookmark on the working directory&#8217;s parent revision with the given name. If you specify a revision using -r REV (where REV may be an existing bookmark), the bookmark is assigned to that revision. </p>
<p> Bookmarks can be pushed and pulled between repositories (see <code>hg help push</code>: and <code>hg help pull</code>:). This requires both the local and remote repositories to support bookmarks. For versions prior to 1.8, this means the bookmarks extension must be enabled. </p>
<p> If you set a bookmark called &#8216;@&#8217;, new clones of the repository will have that revision checked out (and the bookmark made active) by default. </p>
<p> With -i/&#8211;inactive, the new bookmark will not be made the active bookmark. If -r/&#8211;rev is given, the new bookmark will not be made active even if -i/&#8211;inactive is not given. If no NAME is given, the current active bookmark will be marked inactive. </p>
<p> Options:</p>
<dl>
<dt><code>-f, &#8211;force</code></p>
<dd> force</p>
<dt><code>-r, &#8211;rev</code></p>
<dd> revision</p>
<dt><code>-d, &#8211;delete</code></p>
<dd> delete a given bookmark</p>
<dt><code>-m, &#8211;rename</code></p>
<dd> rename a given bookmark</p>
<dt><code>-i, &#8211;inactive</code></p>
<dd> mark a bookmark inactive </p>
<p> aliases: bookmark</dl>
<h3>branch</h3>
<p>hg branch[-fC][NAME]</p>
<dl>
<dt>Note</p>
<dd> Branch names are permanent and global. Use <code>hg bookmark</code>: to create a light-weight bookmark instead. See <code>hg help glossary</code>: for more information about named branches and bookmarks. </p>
<p> With no argument, show the current branch name. With one argument, set the working directory branch name (the branch will not exist in the repository until the next commit). Standard practice recommends that primary development take place on the &#8216;default&#8217; branch. </p>
<p> Unless -f/&#8211;force is specified, branch will not let you set a branch name that already exists, even if it&#8217;s inactive. </p>
<p> Use -C/&#8211;clean to reset the working directory branch to that of the parent of the working directory, negating a previous branch change. </p>
<p> Use the command <code>hg update</code>: to switch to an existing branch. Use <code>hg commit &#8211;close-branch</code>: to mark this branch as closed. </p>
<p> Returns 0 on success. </p>
<p> Options:</p>
<dt><code>-f, &#8211;force</code></p>
<dd> set branch name even if it shadows an existing branch</p>
<dt><code>-C, &#8211;clean</code></p>
<dd> reset branch name to parent branch name</dl>
<h3>branches</h3>
<pre>
hg branches [-ac]
</pre>
<p> List the repository&#8217;s named branches, indicating which ones are inactive. If -c/&#8211;closed is specified, also list branches which have been marked closed (see <code>hg commit &#8211;close-branch</code>:). </p>
<p> If -a/&#8211;active is specified, only show active branches. A branch is considered active if it contains repository heads. </p>
<p> Use the command <code>hg update</code>: to switch to an existing branch. </p>
<p> Returns 0. </p>
<p> Options:</p>
<dl>
<dt><code>-a, &#8211;active</code></p>
<dd> show only branches that have unmerged heads</p>
<dt><code>-c, &#8211;closed</code></p>
<dd> show normal and closed branches</dl>
<h3>bundle</h3>
<p>hg bundle[-f][-t TYPE][-a][-r REV]&#8230;[&#8211;base REV]&#8230; FILE[DEST]</p>
<p> Generate a compressed changegroup file collecting changesets not known to be in another repository. </p>
<p> If you omit the destination repository, then hg assumes the destination will have all the nodes you specify with &#8211;base parameters. To create a bundle containing all changesets, use -a/&#8211;all (or &#8211;base null). </p>
<p> You can change compression method with the -t/&#8211;type option. The available compression methods are: none, bzip2, and gzip (by default, bundles are compressed using bzip2). </p>
<p> The bundle file can then be transferred using conventional means and applied to another repository with the unbundle or pull command. This is useful when direct push and pull are not available or when exporting an entire repository is undesirable. </p>
<p> Applying bundles preserves all changeset contents including permissions, copy/rename information, and revision history. </p>
<p> Returns 0 on success, 1 if no changes found. </p>
<p> Options:</p>
<dl>
<dt><code>-f, &#8211;force</code></p>
<dd> run even when the destination is unrelated</p>
<dt><code>-r, &#8211;rev</code></p>
<dd> a changeset intended to be added to the destination</p>
<dt><code>-b, &#8211;branch</code></p>
<dd> a specific branch you would like to bundle</p>
<dt><code>&#8211;base</code></p>
<dd> a base changeset assumed to be available at the destination</p>
<dt><code>-a, &#8211;all</code></p>
<dd> bundle all changesets in the repository</p>
<dt><code>-t, &#8211;type</code></p>
<dd> bundle compression type to use (default: bzip2)</p>
<dt><code>-e, &#8211;ssh</code></p>
<dd> specify ssh command to use</p>
<dt><code>&#8211;remotecmd</code></p>
<dd> specify hg command to run on the remote side</p>
<dt><code>&#8211;insecure</code></p>
<dd> do not verify server certificate (ignoring web.cacerts config)</dl>
<h3>cat</h3>
<pre>
hg cat [OPTION]... FILE...
</pre>
<p> Print the specified files as they were at the given revision. If no revision is given, the parent of the working directory is used, or tip if no revision is checked out. </p>
<p> Output may be to a file, in which case the name of the file is given using a format string. The formatting rules are the same as for the export command, with the following additions:</p>
<dl>
<dt><code>%s</code></p>
<dd>
<p> basename of file being printed</p>
<dt><code>%d</code></p>
<dd>
<p> dirname of file being printed, or &#8216;.&#8217; if in repository root</p>
<dt><code>%p</code></p>
<dd>
<p> root-relative path name of file being printed </p>
<p> Returns 0 on success. </p>
<p> Options:</p>
<dt><code>-o, &#8211;output</code></p>
<dd> print output to file with formatted name</p>
<dt><code>-r, &#8211;rev</code></p>
<dd> print the given revision</p>
<dt><code>&#8211;decode</code></p>
<dd> apply any matching decode filter</p>
<dt><code>-I, &#8211;include</code></p>
<dd> include names matching the given patterns</p>
<dt><code>-X, &#8211;exclude</code></p>
<dd> exclude names matching the given patterns</dl>
<h3>clone</h3>
<p>hg clone[OPTION]&#8230; SOURCE[DEST]</p>
<p> Create a copy of an existing repository in a new directory. </p>
<p> If no destination directory name is specified, it defaults to the basename of the source. </p>
<p> The location of the source is added to the new repository&#8217;s <code>.hg/hgrc</code> file, as the default to be used for future pulls. </p>
<p> Only local paths and <code>ssh://</code> URLs are supported as destinations. For <code>ssh://</code> destinations, no working directory or <code>.hg/hgrc</code> will be created on the remote side. </p>
<p> To pull only a subset of changesets, specify one or more revisions identifiers with -r/&#8211;rev or branches with -b/&#8211;branch. The resulting clone will contain only the specified changesets and their ancestors. These options (or &#8216;clone src#rev dest&#8217;) imply &#8211;pull, even for local source repositories. Note that specifying a tag will include the tagged changeset but not the changeset containing the tag. </p>
<p> If the source repository has a bookmark called &#8216;@&#8217; set, that revision will be checked out in the new repository by default. </p>
<p> To check out a particular version, use -u/&#8211;update, or -U/&#8211;noupdate to create a clone with no working directory. </p>
<p> For efficiency, hardlinks are used for cloning whenever the source and destination are on the same filesystem (note this applies only to the repository data, not to the working directory). Some filesystems, such as AFS, implement hardlinking incorrectly, but do not report errors. In these cases, use the &#8211;pull option to avoid hardlinking. </p>
<p> In some cases, you can clone repositories and the working directory using full hardlinks with </p>
<pre>
$ cp -al REPO REPOCLONE
</pre>
<p> This is the fastest way to clone, but it is not always safe. The operation is not atomic (making sure REPO is not modified during the operation is up to you) and you have to make sure your editor breaks hardlinks (Emacs and most Linux Kernel tools do so). Also, this is not compatible with certain extensions that place their metadata under the .hg directory, such as mq. </p>
<p> Mercurial will update the working directory to the first applicable revision from this list:</p>
<dl>
<dt>a.</p>
<dd> null if -U or the source repository has no changesets</p>
<dt>b.</p>
<dd> if -u . and the source repository is local, the first parent of the source repository&#8217;s working directory</p>
<dt>c.</p>
<dd> the changeset specified with -u (if a branch name, this means the latest head of that branch)</p>
<dt>d.</p>
<dd> the changeset specified with -r</p>
<dt>e.</p>
<dd> the tipmost head specified with -b</p>
<dt>f.</p>
<dd> the tipmost head specified with the url#branch source syntax</p>
<dt>g.</p>
<dd> the revision marked with the &#8216;@&#8217; bookmark, if present</p>
<dt>h.</p>
<dd> the tipmost head of the default branch</p>
<dt>i.</p>
<dd> tip </p>
<p> Examples:</p>
<dt>&bull;</p>
<dd> clone a remote repository to a new directory named hg/: </p>
<pre>
hg clone <a rel="nofollow" href="http://selenic.com/hg">http://selenic.com/hg</a>
</pre>
<dt>&bull;</p>
<dd> create a lightweight local clone: </p>
<pre>
hg clone project/ project-feature/
</pre>
<dt>&bull;</p>
<dd> clone from an absolute path on an ssh server (note double-slash): </p>
<pre>
hg clone <a href="ssh://user@server//home/projects/alpha/">ssh://user@server//home/projects/alpha/</a>
</pre>
<dt>&bull;</p>
<dd> do a high-speed clone over a LAN while checking out a specified version: </p>
<pre>
hg clone --uncompressed <a rel="nofollow" href="http://server/repo">http://server/repo</a> -u 1.5
</pre>
<dt>&bull;</p>
<dd> create a repository without changesets after a particular revision: </p>
<pre>
hg clone -r 04e544 experimental/ good/
</pre>
<dt>&bull;</p>
<dd> clone (and track) a particular named branch: </p>
<pre>
hg clone <a rel="nofollow" href="http://selenic.com/hg#stable">http://selenic.com/hg#stable</a>
</pre>
<p> See <code>hg help urls</code>: for details on specifying URLs. </p>
<p> Returns 0 on success. </p>
<p> Options:</p>
<dt><code>-U, &#8211;noupdate</code></p>
<dd> the clone will include an empty working copy (only a repository)</p>
<dt><code>-u, &#8211;updaterev</code></p>
<dd> revision, tag or branch to check out</p>
<dt><code>-r, &#8211;rev</code></p>
<dd> include the specified changeset</p>
<dt><code>-b, &#8211;branch</code></p>
<dd> clone only the specified branch</p>
<dt><code>&#8211;pull</code></p>
<dd> use pull protocol to copy metadata</p>
<dt><code>&#8211;uncompressed</code></p>
<dd> use uncompressed transfer (fast over LAN)</p>
<dt><code>-e, &#8211;ssh</code></p>
<dd> specify ssh command to use</p>
<dt><code>&#8211;remotecmd</code></p>
<dd> specify hg command to run on the remote side</p>
<dt><code>&#8211;insecure</code></p>
<dd> do not verify server certificate (ignoring web.cacerts config)</dl>
<h3>commit</h3>
<p>hg commit[OPTION]&#8230;[FILE]&#8230;</p>
<p> Commit changes to the given files into the repository. Unlike a centralized SCM, this operation is a local operation. See <code>hg push</code>: for a way to actively distribute your changes. </p>
<p> If a list of files is omitted, all changes reported by <code>hg status</code>: will be committed. </p>
<p> If you are committing the result of a merge, do not provide any filenames or -I/-X filters. </p>
<p> If no commit message is specified, Mercurial starts your configured editor where you can enter a message. In case your commit fails, you will find a backup of your message in <code>.hg/last-message.txt</code>. </p>
<p> The &#8211;amend flag can be used to amend the parent of the working directory with a new commit that contains the changes in the parent in addition to those currently reported by <code>hg status</code>:, if there are any. The old commit is stored in a backup bundle in <code>.hg/strip-backup</code> (see <code>hg help bundle</code>: and <code>hg help unbundle</code>: on how to restore it). </p>
<p> Message, user and date are taken from the amended commit unless specified. When a message isn&#8217;t specified on the command line, the editor will open with the message of the amended commit. </p>
<p> It is not possible to amend public changesets (see <code>hg help phases</code>:) or changesets that have children. </p>
<p> See <code>hg help dates</code>: for a list of formats valid for -d/&#8211;date. </p>
<p> Returns 0 on success, 1 if nothing changed. </p>
<p> Options:</p>
<dl>
<dt><code>-A, &#8211;addremove</code></p>
<dd> mark new/missing files as added/removed before committing</p>
<dt><code>&#8211;close-branch</code></p>
<dd> mark a branch as closed, hiding it from the branch list</p>
<dt><code>&#8211;amend</code></p>
<dd> amend the parent of the working dir</p>
<dt><code>-I, &#8211;include</code></p>
<dd> include names matching the given patterns</p>
<dt><code>-X, &#8211;exclude</code></p>
<dd> exclude names matching the given patterns</p>
<dt><code>-m, &#8211;message</code></p>
<dd> use text as commit message</p>
<dt><code>-l, &#8211;logfile</code></p>
<dd> read commit message from file</p>
<dt><code>-d, &#8211;date</code></p>
<dd> record the specified date as commit date</p>
<dt><code>-u, &#8211;user</code></p>
<dd> record the specified user as committer</p>
<dt><code>-S, &#8211;subrepos</code></p>
<dd> recurse into subrepositories </p>
<p> aliases: ci</dl>
<h3>copy</h3>
<p>hg copy[OPTION]&#8230;[SOURCE]&#8230; DEST</p>
<p> Mark dest as having copies of source files. If dest is a directory, copies are put in that directory. If dest is a file, the source must be a single file. </p>
<p> By default, this command copies the contents of files as they exist in the working directory. If invoked with -A/&#8211;after, the operation is recorded, but no copying is performed. </p>
<p> This command takes effect with the next commit. To undo a copy before that, see <code>hg revert</code>:. </p>
<p> Returns 0 on success, 1 if errors are encountered. </p>
<p> Options:</p>
<dl>
<dt><code>-A, &#8211;after</code></p>
<dd> record a copy that has already occurred</p>
<dt><code>-f, &#8211;force</code></p>
<dd> forcibly copy over an existing managed file</p>
<dt><code>-I, &#8211;include</code></p>
<dd> include names matching the given patterns</p>
<dt><code>-X, &#8211;exclude</code></p>
<dd> exclude names matching the given patterns</p>
<dt><code>-n, &#8211;dry-run</code></p>
<dd> do not perform actions, just print output </p>
<p> aliases: cp</dl>
<h3>diff</h3>
<p>hg diff[OPTION]&#8230;([-c REV] | [-r REV1[-r REV2]])[FILE]&#8230;</p>
<p> Show differences between revisions for the specified files. </p>
<p> Differences between files are shown using the unified diff format.</p>
<dl>
<dt>Note</p>
<dd> diff may generate unexpected results for merges, as it will default to comparing against the working directory&#8217;s first parent changeset if no revisions are specified. </p>
<p> When two revision arguments are given, then changes are shown between those revisions. If only one revision is specified then that revision is compared to the working directory, and, when no revisions are specified, the working directory files are compared to its parent. </p>
<p> Alternatively you can specify -c/&#8211;change with a revision to see the changes in that changeset relative to its first parent. </p>
<p> Without the -a/&#8211;text option, diff will avoid generating diffs of files it detects as binary. With -a, diff will generate a diff anyway, probably with undesirable results. </p>
<p> Use the -g/&#8211;git option to generate diffs in the git extended diff format. For more information, read <code>hg help diffs</code>:. </p>
<p> Examples:</p>
<dt>&bull;</p>
<dd> compare a file in the current working directory to its parent: </p>
<pre>
hg diff foo.c
</pre>
<dt>&bull;</p>
<dd> compare two historical versions of a directory, with rename info: </p>
<pre>
hg diff --git -r 1.0:1.2 lib/
</pre>
<dt>&bull;</p>
<dd> get change stats relative to the last change on some date: </p>
<pre>
hg diff --stat -r &quot;date('may 2')&quot;
</pre>
<dt>&bull;</p>
<dd> diff all newly-added files that contain a keyword: </p>
<pre>
hg diff &quot;set:added() and grep(GNU)&quot;
</pre>
<dt>&bull;</p>
<dd> compare a revision and its parents: </p>
<pre>
hg diff -c 9353         # compare against first parent
hg diff -r 9353^:9353   # same using revset syntax
hg diff -r 9353^2:9353  # compare against the second parent
</pre>
<p> Returns 0 on success. </p>
<p> Options:</p>
<dt><code>-r, &#8211;rev</code></p>
<dd> revision</p>
<dt><code>-c, &#8211;change</code></p>
<dd> change made by revision</p>
<dt><code>-a, &#8211;text</code></p>
<dd> treat all files as text</p>
<dt><code>-g, &#8211;git</code></p>
<dd> use git extended diff format</p>
<dt><code>&#8211;nodates</code></p>
<dd> omit dates from diff headers</p>
<dt><code>-p, &#8211;show-function</code></p>
<dd> show which function each change is in</p>
<dt><code>&#8211;reverse</code></p>
<dd> produce a diff that undoes the changes</p>
<dt><code>-w, &#8211;ignore-all-space</code></p>
<dd> ignore white space when comparing lines</p>
<dt><code>-b, &#8211;ignore-space-change</code></p>
<dd> ignore changes in the amount of white space</p>
<dt><code>-B, &#8211;ignore-blank-lines</code></p>
<dd> ignore changes whose lines are all blank</p>
<dt><code>-U, &#8211;unified</code></p>
<dd> number of lines of context to show</p>
<dt><code>&#8211;stat</code></p>
<dd> output diffstat-style summary of changes</p>
<dt><code>-I, &#8211;include</code></p>
<dd> include names matching the given patterns</p>
<dt><code>-X, &#8211;exclude</code></p>
<dd> exclude names matching the given patterns</p>
<dt><code>-S, &#8211;subrepos</code></p>
<dd> recurse into subrepositories</dl>
<h3>export</h3>
<p>hg export[OPTION]&#8230;[-o OUTFILESPEC][-r][REV]&#8230;</p>
<p> Print the changeset header and diffs for one or more revisions. If no revision is given, the parent of the working directory is used. </p>
<p> The information shown in the changeset header is: author, date, branch name (if non-default), changeset hash, parent(s) and commit comment.</p>
<dl>
<dt>Note</p>
<dd> export may generate unexpected diff output for merge changesets, as it will compare the merge changeset against its first parent only. </p>
<p> Output may be to a file, in which case the name of the file is given using a format string. The formatting rules are as follows:</p>
<dt><code>%%</code></p>
<dd>
<p> literal &quot;%&quot; character</p>
<dt><code>%H</code></p>
<dd>
<p> changeset hash (40 hexadecimal digits)</p>
<dt><code>%N</code></p>
<dd>
<p> number of patches being generated</p>
<dt><code>%R</code></p>
<dd>
<p> changeset revision number</p>
<dt><code>%b</code></p>
<dd>
<p> basename of the exporting repository</p>
<dt><code>%h</code></p>
<dd>
<p> short-form changeset hash (12 hexadecimal digits)</p>
<dt><code>%m</code></p>
<dd>
<p> first line of the commit message (only alphanumeric characters)</p>
<dt><code>%n</code></p>
<dd>
<p> zero-padded sequence number, starting at 1</p>
<dt><code>%r</code></p>
<dd>
<p> zero-padded changeset revision number </p>
<p> Without the -a/&#8211;text option, export will avoid generating diffs of files it detects as binary. With -a, export will generate a diff anyway, probably with undesirable results. </p>
<p> Use the -g/&#8211;git option to generate diffs in the git extended diff format. See <code>hg help diffs</code>: for more information. </p>
<p> With the &#8211;switch-parent option, the diff will be against the second parent. It can be useful to review a merge. </p>
<p> Examples:</p>
<dt>&bull;</p>
<dd> use export and import to transplant a bugfix to the current branch: </p>
<pre>
hg export -r 9353 | hg import -
</pre>
<dt>&bull;</p>
<dd> export all the changesets between two revisions to a file with rename information: </p>
<pre>
hg export --git -r 123:150 &gt; changes.txt
</pre>
<dt>&bull;</p>
<dd> split outgoing changes into a series of patches with descriptive names: </p>
<pre>
hg export -r &quot;outgoing()&quot; -o &quot;%n-%m.patch&quot;
</pre>
<p> Returns 0 on success. </p>
<p> Options:</p>
<dt><code>-o, &#8211;output</code></p>
<dd> print output to file with formatted name</p>
<dt><code>&#8211;switch-parent</code></p>
<dd> diff against the second parent</p>
<dt><code>-r, &#8211;rev</code></p>
<dd> revisions to export</p>
<dt><code>-a, &#8211;text</code></p>
<dd> treat all files as text</p>
<dt><code>-g, &#8211;git</code></p>
<dd> use git extended diff format</p>
<dt><code>&#8211;nodates</code></p>
<dd> omit dates from diff headers</dl>
<h3>forget</h3>
<pre>
hg forget [OPTION]... FILE...
</pre>
<p> Mark the specified files so they will no longer be tracked after the next commit. </p>
<p> This only removes files from the current branch, not from the entire project history, and it does not delete them from the working directory. </p>
<p> To undo a forget before the next commit, see <code>hg add</code>:. </p>
<p> Examples:</p>
<dl>
<dt>&bull;</p>
<dd> forget newly-added binary files: </p>
<pre>
hg forget &quot;set:added() and binary()&quot;
</pre>
<dt>&bull;</p>
<dd> forget files that would be excluded by .hgignore: </p>
<pre>
hg forget &quot;set:hgignore()&quot;
</pre>
<p> Returns 0 on success. </p>
<p> Options:</p>
<dt><code>-I, &#8211;include</code></p>
<dd> include names matching the given patterns</p>
<dt><code>-X, &#8211;exclude</code></p>
<dd> exclude names matching the given patterns</dl>
<h3>graft</h3>
<p>hg graft[OPTION]&#8230;[-r] REV&#8230;</p>
<p> This command uses Mercurial&#8217;s merge logic to copy individual changes from other branches without merging branches in the history graph. This is sometimes known as &#8216;backporting&#8217; or &#8216;cherry-picking&#8217;. By default, graft will copy user, date, and description from the source changesets. </p>
<p> Changesets that are ancestors of the current revision, that have already been grafted, or that are merges will be skipped. </p>
<p> If &#8211;log is specified, log messages will have a comment appended of the form: </p>
<pre>
(grafted from CHANGESETHASH)
</pre>
<p> If a graft merge results in conflicts, the graft process is interrupted so that the current merge can be manually resolved. Once all conflicts are addressed, the graft process can be continued with the -c/&#8211;continue option.</p>
<dl>
<dt>Note</p>
<dd> The -c/&#8211;continue option does not reapply earlier options. </p>
<p> Examples:</p>
<dt>&bull;</p>
<dd> copy a single change to the stable branch and edit its description: </p>
<pre>
hg update stable
hg graft --edit 9393
</pre>
<dt>&bull;</p>
<dd> graft a range of changesets with one exception, updating dates: </p>
<pre>
hg graft -D &quot;2085::2093 and not 2091&quot;
</pre>
<dt>&bull;</p>
<dd> continue a graft after resolving conflicts: </p>
<pre>
hg graft -c
</pre>
<dt>&bull;</p>
<dd> show the source of a grafted changeset: </p>
<pre>
hg log --debug -r tip
</pre>
<p> Returns 0 on successful completion. </p>
<p> Options:</p>
<dt><code>-r, &#8211;rev</code></p>
<dd> revisions to graft</p>
<dt><code>-c, &#8211;continue</code></p>
<dd> resume interrupted graft</p>
<dt><code>-e, &#8211;edit</code></p>
<dd> invoke editor on commit messages</p>
<dt><code>&#8211;log</code></p>
<dd> append graft info to log message</p>
<dt><code>-D, &#8211;currentdate</code></p>
<dd> record the current date as commit date</p>
<dt><code>-U, &#8211;currentuser</code></p>
<dd> record the current user as committer</p>
<dt><code>-d, &#8211;date</code></p>
<dd> record the specified date as commit date</p>
<dt><code>-u, &#8211;user</code></p>
<dd> record the specified user as committer</p>
<dt><code>-t, &#8211;tool</code></p>
<dd> specify merge tool</p>
<dt><code>-n, &#8211;dry-run</code></p>
<dd> do not perform actions, just print output</dl>
<h3>grep</h3>
<p>hg grep[OPTION]&#8230; PATTERN[FILE]&#8230;</p>
<p> Search revisions of files for a regular expression. </p>
<p> This command behaves differently than Unix grep. It only accepts Python/Perl regexps. It searches repository history, not the working directory. It always prints the revision number in which a match appears. </p>
<p> By default, grep only prints output for the first revision of a file in which it finds a match. To get it to print every revision that contains a change in match status (&quot;-&quot; for a match that becomes a non-match, or &quot;+&quot; for a non-match that becomes a match), use the &#8211;all flag. </p>
<p> Returns 0 if a match is found, 1 otherwise. </p>
<p> Options:</p>
<dl>
<dt><code>-0, &#8211;print0</code></p>
<dd> end fields with NUL</p>
<dt><code>&#8211;all</code></p>
<dd> print all revisions that match</p>
<dt><code>-a, &#8211;text</code></p>
<dd> treat all files as text</p>
<dt><code>-f, &#8211;follow</code></p>
<dd> follow changeset history, or file history across copies and renames</p>
<dt><code>-i, &#8211;ignore-case</code></p>
<dd> ignore case when matching</p>
<dt><code>-l, &#8211;files-with-matches</code></p>
<dd> print only filenames and revisions that match</p>
<dt><code>-n, &#8211;line-number</code></p>
<dd> print matching line numbers</p>
<dt><code>-r, &#8211;rev</code></p>
<dd> only search files changed within revision range</p>
<dt><code>-u, &#8211;user</code></p>
<dd> list the author (long with -v)</p>
<dt><code>-d, &#8211;date</code></p>
<dd> list the date (short with -q)</p>
<dt><code>-I, &#8211;include</code></p>
<dd> include names matching the given patterns</p>
<dt><code>-X, &#8211;exclude</code></p>
<dd> exclude names matching the given patterns</dl>
<h3>heads</h3>
<p>hg heads[-ct][-r STARTREV][REV]&#8230;</p>
<p> With no arguments, show all repository branch heads. </p>
<p> Repository &quot;heads&quot; are changesets with no child changesets. They are where development generally takes place and are the usual targets for update and merge operations. Branch heads are changesets that have no child changeset on the same branch. </p>
<p> If one or more REVs are given, only branch heads on the branches associated with the specified changesets are shown. This means that you can use <code>hg heads foo</code>: to see the heads on a branch named <code>foo</code>. </p>
<p> If -c/&#8211;closed is specified, also show branch heads marked closed (see <code>hg commit &#8211;close-branch</code>:). </p>
<p> If STARTREV is specified, only those heads that are descendants of STARTREV will be displayed. </p>
<p> If -t/&#8211;topo is specified, named branch mechanics will be ignored and only changesets without children will be shown. </p>
<p> Returns 0 if matching heads are found, 1 if not. </p>
<p> Options:</p>
<dl>
<dt><code>-r, &#8211;rev</code></p>
<dd> show only heads which are descendants of STARTREV</p>
<dt><code>-t, &#8211;topo</code></p>
<dd> show topological heads only</p>
<dt><code>-a, &#8211;active</code></p>
<dd> show active branchheads only (DEPRECATED)</p>
<dt><code>-c, &#8211;closed</code></p>
<dd> show normal and closed branch heads</p>
<dt><code>&#8211;style</code></p>
<dd> display using template map file</p>
<dt><code>&#8211;template</code></p>
<dd> display with template</dl>
<h3>help</h3>
<p>hg help[-ec][TOPIC]</p>
<p> With no arguments, print a list of commands with short help messages. </p>
<p> Given a topic, extension, or command name, print help for that topic. </p>
<p> Returns 0 if successful. </p>
<p> Options:</p>
<dl>
<dt><code>-e, &#8211;extension</code></p>
<dd> show only help for extensions</p>
<dt><code>-c, &#8211;command</code></p>
<dd> show only help for commands</p>
<dt><code>-k, &#8211;keyword</code></p>
<dd> show topics matching keyword</dl>
<h3>identify</h3>
<p>hg identify[-nibtB][-r REV][SOURCE]</p>
<p> Print a summary identifying the repository state at REV using one or two parent hash identifiers, followed by a &quot;+&quot; if the working directory has uncommitted changes, the branch name (if not default), a list of tags, and a list of bookmarks. </p>
<p> When REV is not given, print a summary of the current state of the repository. </p>
<p> Specifying a path to a repository root or Mercurial bundle will cause lookup to operate on that repository/bundle. </p>
<p> Examples:</p>
<dl>
<dt>&bull;</p>
<dd> generate a build identifier for the working directory: </p>
<pre>
hg id --id &gt; build-id.dat
</pre>
<dt>&bull;</p>
<dd> find the revision corresponding to a tag: </p>
<pre>
hg id -n -r 1.3
</pre>
<dt>&bull;</p>
<dd> check the most recent revision of a remote repository: </p>
<pre>
hg id -r tip <a rel="nofollow" href="http://selenic.com/hg/">http://selenic.com/hg/</a>
</pre>
<p> Returns 0 if successful. </p>
<p> Options:</p>
<dt><code>-r, &#8211;rev</code></p>
<dd> identify the specified revision</p>
<dt><code>-n, &#8211;num</code></p>
<dd> show local revision number</p>
<dt><code>-i, &#8211;id</code></p>
<dd> show global revision id</p>
<dt><code>-b, &#8211;branch</code></p>
<dd> show branch</p>
<dt><code>-t, &#8211;tags</code></p>
<dd> show tags</p>
<dt><code>-B, &#8211;bookmarks</code></p>
<dd> show bookmarks</p>
<dt><code>-e, &#8211;ssh</code></p>
<dd> specify ssh command to use</p>
<dt><code>&#8211;remotecmd</code></p>
<dd> specify hg command to run on the remote side</p>
<dt><code>&#8211;insecure</code></p>
<dd> do not verify server certificate (ignoring web.cacerts config) </p>
<p> aliases: id</dl>
<h3>import</h3>
<pre>
hg import [OPTION]... PATCH...
</pre>
<p> Import a list of patches and commit them individually (unless &#8211;no-commit is specified). </p>
<p> If there are outstanding changes in the working directory, import will abort unless given the -f/&#8211;force flag. </p>
<p> You can import a patch straight from a mail message. Even patches as attachments work (to use the body part, it must have type text/plain or text/x-patch). From and Subject headers of email message are used as default committer and commit message. All text/plain body parts before first diff are added to commit message. </p>
<p> If the imported patch was generated by <code>hg export</code>:, user and description from patch override values from message headers and body. Values given on command line with -m/&#8211;message and -u/&#8211;user override these. </p>
<p> If &#8211;exact is specified, import will set the working directory to the parent of each patch before applying it, and will abort if the resulting changeset has a different ID than the one recorded in the patch. This may happen due to character set problems or other deficiencies in the text patch format. </p>
<p> Use &#8211;bypass to apply and commit patches directly to the repository, not touching the working directory. Without &#8211;exact, patches will be applied on top of the working directory parent revision. </p>
<p> With -s/&#8211;similarity, hg will attempt to discover renames and copies in the patch in the same way as <code>hg addremove</code>:. </p>
<p> To read a patch from standard input, use &quot;-&quot; as the patch name. If a URL is specified, the patch will be downloaded from it. See <code>hg help dates</code>: for a list of formats valid for -d/&#8211;date. </p>
<p> Examples:</p>
<dl>
<dt>&bull;</p>
<dd> import a traditional patch from a website and detect renames: </p>
<pre>
hg import -s 80 <a rel="nofollow" href="http://example.com/bugfix.patch">http://example.com/bugfix.patch</a>
</pre>
<dt>&bull;</p>
<dd> import a changeset from an hgweb server: </p>
<pre>
hg import <a rel="nofollow" href="http://www.selenic.com/hg/rev/5ca8c111e9aa">http://www.selenic.com/hg/rev/5ca8c111e9aa</a>
</pre>
<dt>&bull;</p>
<dd> import all the patches in an Unix-style mbox: </p>
<pre>
hg import incoming-patches.mbox
</pre>
<dt>&bull;</p>
<dd> attempt to exactly restore an exported changeset (not always possible): </p>
<pre>
hg import --exact proposed-fix.patch
</pre>
<p> Returns 0 on success. </p>
<p> Options:</p>
<dt><code>-p, &#8211;strip</code></p>
<dd> directory strip option for patch. This has the same meaning as the corresponding patch option (default: 1)</p>
<dt><code>-b, &#8211;base</code></p>
<dd> base path (DEPRECATED)</p>
<dt><code>-e, &#8211;edit</code></p>
<dd> invoke editor on commit messages</p>
<dt><code>-f, &#8211;force</code></p>
<dd> skip check for outstanding uncommitted changes</p>
<dt><code>&#8211;no-commit</code></p>
<dd> don&#8217;t commit, just update the working directory</p>
<dt><code>&#8211;bypass</code></p>
<dd> apply patch without touching the working directory</p>
<dt><code>&#8211;exact</code></p>
<dd> apply patch to the nodes from which it was generated</p>
<dt><code>&#8211;import-branch</code></p>
<dd> use any branch information in patch (implied by &#8211;exact)</p>
<dt><code>-m, &#8211;message</code></p>
<dd> use text as commit message</p>
<dt><code>-l, &#8211;logfile</code></p>
<dd> read commit message from file</p>
<dt><code>-d, &#8211;date</code></p>
<dd> record the specified date as commit date</p>
<dt><code>-u, &#8211;user</code></p>
<dd> record the specified user as committer</p>
<dt><code>-s, &#8211;similarity</code></p>
<dd> guess renamed files by similarity (0&lt;=s&lt;=100) </p>
<p> aliases: patch</dl>
<h3>incoming</h3>
<p>hg incoming[-p][-n][-M][-f][-r REV]&#8230;[&#8211;bundle FILENAME][SOURCE]</p>
<p> Show new changesets found in the specified path/URL or the default pull location. These are the changesets that would have been pulled if a pull at the time you issued this command. </p>
<p> For remote repository, using &#8211;bundle avoids downloading the changesets twice if the incoming is followed by a pull. </p>
<p> See pull for valid source format details. </p>
<p> Returns 0 if there are incoming changes, 1 otherwise. </p>
<p> Options:</p>
<dl>
<dt><code>-f, &#8211;force</code></p>
<dd> run even if remote repository is unrelated</p>
<dt><code>-n, &#8211;newest-first</code></p>
<dd> show newest record first</p>
<dt><code>&#8211;bundle</code></p>
<dd> file to store the bundles into</p>
<dt><code>-r, &#8211;rev</code></p>
<dd> a remote changeset intended to be added</p>
<dt><code>-B, &#8211;bookmarks</code></p>
<dd> compare bookmarks</p>
<dt><code>-b, &#8211;branch</code></p>
<dd> a specific branch you would like to pull</p>
<dt><code>-p, &#8211;patch</code></p>
<dd> show patch</p>
<dt><code>-g, &#8211;git</code></p>
<dd> use git extended diff format</p>
<dt><code>-l, &#8211;limit</code></p>
<dd> limit number of changes displayed</p>
<dt><code>-M, &#8211;no-merges</code></p>
<dd> do not show merges</p>
<dt><code>&#8211;stat</code></p>
<dd> output diffstat-style summary of changes</p>
<dt><code>-G, &#8211;graph</code></p>
<dd> show the revision DAG</p>
<dt><code>&#8211;style</code></p>
<dd> display using template map file</p>
<dt><code>&#8211;template</code></p>
<dd> display with template</p>
<dt><code>-e, &#8211;ssh</code></p>
<dd> specify ssh command to use</p>
<dt><code>&#8211;remotecmd</code></p>
<dd> specify hg command to run on the remote side</p>
<dt><code>&#8211;insecure</code></p>
<dd> do not verify server certificate (ignoring web.cacerts config)</p>
<dt><code>-S, &#8211;subrepos</code></p>
<dd> recurse into subrepositories </p>
<p> aliases: in</dl>
<h3>init</h3>
<p>hg init[-e CMD][&#8211;remotecmd CMD][DEST]</p>
<p> Initialize a new repository in the given directory. If the given directory does not exist, it will be created. </p>
<p> If no directory is given, the current directory is used. </p>
<p> It is possible to specify an <code>ssh://</code> URL as the destination. See <code>hg help urls</code>: for more information. </p>
<p> Returns 0 on success. </p>
<p> Options:</p>
<dl>
<dt><code>-e, &#8211;ssh</code></p>
<dd> specify ssh command to use</p>
<dt><code>&#8211;remotecmd</code></p>
<dd> specify hg command to run on the remote side</p>
<dt><code>&#8211;insecure</code></p>
<dd> do not verify server certificate (ignoring web.cacerts config)</dl>
<h3>locate</h3>
<p>hg locate[OPTION]&#8230;[PATTERN]&#8230;</p>
<p> Print files under Mercurial control in the working directory whose names match the given patterns. </p>
<p> By default, this command searches all directories in the working directory. To search just the current directory and its subdirectories, use &quot;&#8211;include .&quot;. </p>
<p> If no patterns are given to match, this command prints the names of all files under Mercurial control in the working directory. </p>
<p> If you want to feed the output of this command into the &quot;xargs&quot; command, use the -0 option to both this command and &quot;xargs&quot;. This will avoid the problem of &quot;xargs&quot; treating single filenames that contain whitespace as multiple filenames. </p>
<p> Returns 0 if a match is found, 1 otherwise. </p>
<p> Options:</p>
<dl>
<dt><code>-r, &#8211;rev</code></p>
<dd> search the repository as it is in REV</p>
<dt><code>-0, &#8211;print0</code></p>
<dd> end filenames with NUL, for use with xargs</p>
<dt><code>-f, &#8211;fullpath</code></p>
<dd> print complete paths from the filesystem root</p>
<dt><code>-I, &#8211;include</code></p>
<dd> include names matching the given patterns</p>
<dt><code>-X, &#8211;exclude</code></p>
<dd> exclude names matching the given patterns</dl>
<h3>log</h3>
<p>hg log[OPTION]&#8230;[FILE]</p>
<p> Print the revision history of the specified files or the entire project. </p>
<p> If no revision range is specified, the default is <code>tip:0</code> unless &#8211;follow is set, in which case the working directory parent is used as the starting revision. </p>
<p> File history is shown without following rename or copy history of files. Use -f/&#8211;follow with a filename to follow history across renames and copies. &#8211;follow without a filename will only show ancestors or descendants of the starting revision. </p>
<p> By default this command prints revision number and changeset id, tags, non-trivial parents, user, date and time, and a summary for each commit. When the -v/&#8211;verbose switch is used, the list of changed files and full commit message are shown.</p>
<dl>
<dt>Note</p>
<dd> log -p/&#8211;patch may generate unexpected diff output for merge changesets, as it will only compare the merge changeset against its first parent. Also, only files different from BOTH parents will appear in files:.</p>
<dt>Note</p>
<dd> for performance reasons, log FILE may omit duplicate changes made on branches and will not show deletions. To see all changes including duplicates and deletions, use the &#8211;removed switch. </p>
<p> Some examples:</p>
<dt>&bull;</p>
<dd> changesets with full descriptions and file lists: </p>
<pre>
hg log -v
</pre>
<dt>&bull;</p>
<dd> changesets ancestral to the working directory: </p>
<pre>
hg log -f
</pre>
<dt>&bull;</p>
<dd> last 10 commits on the current branch: </p>
<pre>
hg log -l 10 -b .
</pre>
<dt>&bull;</p>
<dd> changesets showing all modifications of a file, including removals: </p>
<pre>
hg log --removed file.c
</pre>
<dt>&bull;</p>
<dd> all changesets that touch a directory, with diffs, excluding merges: </p>
<pre>
hg log -Mp lib/
</pre>
<dt>&bull;</p>
<dd> all revision numbers that match a keyword: </p>
<pre>
hg log -k bug --template &quot;{rev}
&quot;
</pre>
<dt>&bull;</p>
<dd> check if a given changeset is included is a tagged release: </p>
<pre>
hg log -r &quot;a21ccf and ancestor(1.9)&quot;
</pre>
<dt>&bull;</p>
<dd> find all changesets by some user in a date range: </p>
<pre>
hg log -k alice -d &quot;may 2008 to jul 2008&quot;
</pre>
<dt>&bull;</p>
<dd> summary of all changesets after the last tag: </p>
<pre>
hg log -r &quot;last(tagged())::&quot; --template &quot;{desc|firstline}
&quot;
</pre>
<p> See <code>hg help dates</code>: for a list of formats valid for -d/&#8211;date. </p>
<p> See <code>hg help revisions</code>: and <code>hg help revsets</code>: for more about specifying revisions. </p>
<p> See <code>hg help templates</code>: for more about pre-packaged styles and specifying custom templates. </p>
<p> Returns 0 on success. </p>
<p> Options:</p>
<dt><code>-f, &#8211;follow</code></p>
<dd> follow changeset history, or file history across copies and renames</p>
<dt><code>&#8211;follow-first</code></p>
<dd> only follow the first parent of merge changesets (DEPRECATED)</p>
<dt><code>-d, &#8211;date</code></p>
<dd> show revisions matching date spec</p>
<dt><code>-C, &#8211;copies</code></p>
<dd> show copied files</p>
<dt><code>-k, &#8211;keyword</code></p>
<dd> do case-insensitive search for a given text</p>
<dt><code>-r, &#8211;rev</code></p>
<dd> show the specified revision or range</p>
<dt><code>&#8211;removed</code></p>
<dd> include revisions where files were removed</p>
<dt><code>-m, &#8211;only-merges</code></p>
<dd> show only merges (DEPRECATED)</p>
<dt><code>-u, &#8211;user</code></p>
<dd> revisions committed by user</p>
<dt><code>&#8211;only-branch</code></p>
<dd> show only changesets within the given named branch (DEPRECATED)</p>
<dt><code>-b, &#8211;branch</code></p>
<dd> show changesets within the given named branch</p>
<dt><code>-P, &#8211;prune</code></p>
<dd> do not display revision or any of its ancestors</p>
<dt><code>-p, &#8211;patch</code></p>
<dd> show patch</p>
<dt><code>-g, &#8211;git</code></p>
<dd> use git extended diff format</p>
<dt><code>-l, &#8211;limit</code></p>
<dd> limit number of changes displayed</p>
<dt><code>-M, &#8211;no-merges</code></p>
<dd> do not show merges</p>
<dt><code>&#8211;stat</code></p>
<dd> output diffstat-style summary of changes</p>
<dt><code>-G, &#8211;graph</code></p>
<dd> show the revision DAG</p>
<dt><code>&#8211;style</code></p>
<dd> display using template map file</p>
<dt><code>&#8211;template</code></p>
<dd> display with template</p>
<dt><code>-I, &#8211;include</code></p>
<dd> include names matching the given patterns</p>
<dt><code>-X, &#8211;exclude</code></p>
<dd> exclude names matching the given patterns </p>
<p> aliases: history</dl>
<h3>manifest</h3>
<pre>
hg manifest [-r REV]
</pre>
<p> Print a list of version controlled files for the given revision. If no revision is given, the first parent of the working directory is used, or the null revision if no revision is checked out. </p>
<p> With -v, print file permissions, symlink and executable bits. With &#8211;debug, print file revision hashes. </p>
<p> If option &#8211;all is specified, the list of all files from all revisions is printed. This includes deleted and renamed files. </p>
<p> Returns 0 on success. </p>
<p> Options:</p>
<dl>
<dt><code>-r, &#8211;rev</code></p>
<dd> revision to display</p>
<dt><code>&#8211;all</code></p>
<dd> list files from all revisions</dl>
<h3>merge</h3>
<p>hg merge[-P][-f][[-r] REV]</p>
<p> The current working directory is updated with all changes made in the requested revision since the last common predecessor revision. </p>
<p> Files that changed between either parent are marked as changed for the next commit and a commit must be performed before any further updates to the repository are allowed. The next commit will have two parents. </p>
<p> <code>&#8211;tool</code> can be used to specify the merge tool used for file merges. It overrides the HGMERGE environment variable and your configuration files. See <code>hg help merge-tools</code>: for options. </p>
<p> If no revision is specified, the working directory&#8217;s parent is a head revision, and the current branch contains exactly one other head, the other head is merged with by default. Otherwise, an explicit revision with which to merge with must be provided. </p>
<p> <code>hg resolve</code>: must be used to resolve unresolved files. </p>
<p> To undo an uncommitted merge, use <code>hg update &#8211;clean .</code>: which will check out a clean copy of the original merge parent, losing all changes. </p>
<p> Returns 0 on success, 1 if there are unresolved files. </p>
<p> Options:</p>
<dl>
<dt><code>-f, &#8211;force</code></p>
<dd> force a merge with outstanding changes</p>
<dt><code>-r, &#8211;rev</code></p>
<dd> revision to merge</p>
<dt><code>-P, &#8211;preview</code></p>
<dd> review revisions to merge (no merge is performed)</p>
<dt><code>-t, &#8211;tool</code></p>
<dd> specify merge tool</dl>
<h3>outgoing</h3>
<p>hg outgoing[-M][-p][-n][-f][-r REV]&#8230;[DEST]</p>
<p> Show changesets not found in the specified destination repository or the default push location. These are the changesets that would be pushed if a push was requested. </p>
<p> See pull for details of valid destination formats. </p>
<p> Returns 0 if there are outgoing changes, 1 otherwise. </p>
<p> Options:</p>
<dl>
<dt><code>-f, &#8211;force</code></p>
<dd> run even when the destination is unrelated</p>
<dt><code>-r, &#8211;rev</code></p>
<dd> a changeset intended to be included in the destination</p>
<dt><code>-n, &#8211;newest-first</code></p>
<dd> show newest record first</p>
<dt><code>-B, &#8211;bookmarks</code></p>
<dd> compare bookmarks</p>
<dt><code>-b, &#8211;branch</code></p>
<dd> a specific branch you would like to push</p>
<dt><code>-p, &#8211;patch</code></p>
<dd> show patch</p>
<dt><code>-g, &#8211;git</code></p>
<dd> use git extended diff format</p>
<dt><code>-l, &#8211;limit</code></p>
<dd> limit number of changes displayed</p>
<dt><code>-M, &#8211;no-merges</code></p>
<dd> do not show merges</p>
<dt><code>&#8211;stat</code></p>
<dd> output diffstat-style summary of changes</p>
<dt><code>-G, &#8211;graph</code></p>
<dd> show the revision DAG</p>
<dt><code>&#8211;style</code></p>
<dd> display using template map file</p>
<dt><code>&#8211;template</code></p>
<dd> display with template</p>
<dt><code>-e, &#8211;ssh</code></p>
<dd> specify ssh command to use</p>
<dt><code>&#8211;remotecmd</code></p>
<dd> specify hg command to run on the remote side</p>
<dt><code>&#8211;insecure</code></p>
<dd> do not verify server certificate (ignoring web.cacerts config)</p>
<dt><code>-S, &#8211;subrepos</code></p>
<dd> recurse into subrepositories </p>
<p> aliases: out</dl>
<h3>parents</h3>
<p>hg parents[-r REV][FILE]</p>
<p> Print the working directory&#8217;s parent revisions. If a revision is given via -r/&#8211;rev, the parent of that revision will be printed. If a file argument is given, the revision in which the file was last changed (before the working directory revision or the argument to &#8211;rev if given) is printed. </p>
<p> Returns 0 on success. </p>
<p> Options:</p>
<dl>
<dt><code>-r, &#8211;rev</code></p>
<dd> show parents of the specified revision</p>
<dt><code>&#8211;style</code></p>
<dd> display using template map file</p>
<dt><code>&#8211;template</code></p>
<dd> display with template</dl>
<h3>paths</h3>
<pre>
hg paths [NAME]
</pre>
<p> Show definition of symbolic path name NAME. If no name is given, show definition of all available names. </p>
<p> Option -q/&#8211;quiet suppresses all output when searching for NAME and shows only the path names when listing all definitions. </p>
<p> Path names are defined in the [paths] section of your configuration file and in <code>/etc/mercurial/hgrc</code>. If run inside a repository, <code>.hg/hgrc</code> is used, too. </p>
<p> The path names <code>default</code> and <code>default-push</code> have a special meaning. When performing a push or pull operation, they are used as fallbacks if no location is specified on the command-line. When <code>default-push</code> is set, it will be used for push and <code>default</code> will be used for pull; otherwise <code>default</code> is used as the fallback for both. When cloning a repository, the clone source is written as <code>default</code> in <code>.hg/hgrc</code>. Note that <code>default</code> and <code>default-push</code> apply to all inbound (e.g. <code>hg incoming</code>:) and outbound (e.g. <code>hg outgoing</code>:, <code>hg email</code>: and <code>hg bundle</code>:) operations. </p>
<p> See <code>hg help urls</code>: for more information. </p>
<p> Returns 0 on success.</p>
<h3>phase</h3>
<p>hg phase[-p | -d | -s][-f][-r] REV&#8230;</p>
<p> With no argument, show the phase name of specified revisions. </p>
<p> With one of -p/&#8211;public, -d/&#8211;draft or -s/&#8211;secret, change the phase value of the specified revisions. </p>
<p> Unless -f/&#8211;force is specified, <code>hg phase</code>: won&#8217;t move changeset from a lower phase to an higher phase. Phases are ordered as follows: </p>
<pre>
public &lt; draft &lt; secret
</pre>
<p> Return 0 on success, 1 if no phases were changed or some could not be changed. </p>
<p> Options:</p>
<dl>
<dt><code>-p, &#8211;public</code></p>
<dd> set changeset phase to public</p>
<dt><code>-d, &#8211;draft</code></p>
<dd> set changeset phase to draft</p>
<dt><code>-s, &#8211;secret</code></p>
<dd> set changeset phase to secret</p>
<dt><code>-f, &#8211;force</code></p>
<dd> allow to move boundary backward</p>
<dt><code>-r, &#8211;rev</code></p>
<dd> target revision</dl>
<h3>pull</h3>
<p>hg pull[-u][-f][-r REV]&#8230;[-e CMD][&#8211;remotecmd CMD][SOURCE]</p>
<p> Pull changes from a remote repository to a local one. </p>
<p> This finds all changes from the repository at the specified path or URL and adds them to a local repository (the current one unless -R is specified). By default, this does not update the copy of the project in the working directory. </p>
<p> Use <code>hg incoming</code>: if you want to see what would have been added by a pull at the time you issued this command. If you then decide to add those changes to the repository, you should use <code>hg pull -r X</code>: where <code>X</code> is the last changeset listed by <code>hg incoming</code>:. </p>
<p> If SOURCE is omitted, the &#8216;default&#8217; path will be used. See <code>hg help urls</code>: for more information. </p>
<p> Returns 0 on success, 1 if an update had unresolved files. </p>
<p> Options:</p>
<dl>
<dt><code>-u, &#8211;update</code></p>
<dd> update to new branch head if changesets were pulled</p>
<dt><code>-f, &#8211;force</code></p>
<dd> run even when remote repository is unrelated</p>
<dt><code>-r, &#8211;rev</code></p>
<dd> a remote changeset intended to be added</p>
<dt><code>-B, &#8211;bookmark</code></p>
<dd> bookmark to pull</p>
<dt><code>-b, &#8211;branch</code></p>
<dd> a specific branch you would like to pull</p>
<dt><code>-e, &#8211;ssh</code></p>
<dd> specify ssh command to use</p>
<dt><code>&#8211;remotecmd</code></p>
<dd> specify hg command to run on the remote side</p>
<dt><code>&#8211;insecure</code></p>
<dd> do not verify server certificate (ignoring web.cacerts config)</dl>
<h3>push</h3>
<p>hg push[-f][-r REV]&#8230;[-e CMD][&#8211;remotecmd CMD][DEST]</p>
<p> Push changesets from the local repository to the specified destination. </p>
<p> This operation is symmetrical to pull: it is identical to a pull in the destination repository from the current one. </p>
<p> By default, push will not allow creation of new heads at the destination, since multiple heads would make it unclear which head to use. In this situation, it is recommended to pull and merge before pushing. </p>
<p> Use &#8211;new-branch if you want to allow push to create a new named branch that is not present at the destination. This allows you to only create a new branch without forcing other changes. </p>
<p> Use -f/&#8211;force to override the default behavior and push all changesets on all branches. </p>
<p> If -r/&#8211;rev is used, the specified revision and all its ancestors will be pushed to the remote repository. </p>
<p> If -B/&#8211;bookmark is used, the specified bookmarked revision, its ancestors, and the bookmark will be pushed to the remote repository. </p>
<p> Please see <code>hg help urls</code>: for important details about <code>ssh://</code> URLs. If DESTINATION is omitted, a default path will be used. </p>
<p> Returns 0 if push was successful, 1 if nothing to push. </p>
<p> Options:</p>
<dl>
<dt><code>-f, &#8211;force</code></p>
<dd> force push</p>
<dt><code>-r, &#8211;rev</code></p>
<dd> a changeset intended to be included in the destination</p>
<dt><code>-B, &#8211;bookmark</code></p>
<dd> bookmark to push</p>
<dt><code>-b, &#8211;branch</code></p>
<dd> a specific branch you would like to push</p>
<dt><code>&#8211;new-branch</code></p>
<dd> allow pushing a new branch</p>
<dt><code>-e, &#8211;ssh</code></p>
<dd> specify ssh command to use</p>
<dt><code>&#8211;remotecmd</code></p>
<dd> specify hg command to run on the remote side</p>
<dt><code>&#8211;insecure</code></p>
<dd> do not verify server certificate (ignoring web.cacerts config)</dl>
<h3>recover</h3>
<pre>
hg recover
</pre>
<p> Recover from an interrupted commit or pull. </p>
<p> This command tries to fix the repository status after an interrupted operation. It should only be necessary when Mercurial suggests it. </p>
<p> Returns 0 if successful, 1 if nothing to recover or verify fails.</p>
<h3>remove</h3>
<pre>
hg remove [OPTION]... FILE...
</pre>
<p> Schedule the indicated files for removal from the current branch. </p>
<p> This command schedules the files to be removed at the next commit. To undo a remove before that, see <code>hg revert</code>:. To undo added files, see <code>hg forget</code>:. </p>
<p> -A/&#8211;after can be used to remove only files that have already been deleted, -f/&#8211;force can be used to force deletion, and -Af can be used to remove files from the next revision without deleting them from the working directory. </p>
<p> The following table details the behavior of remove for different file states (columns) and option combinations (rows). The file states are Added [A], Clean [C], Modified [M] and Missing [!] (as reported by <code>hg status</code>:). The actions are Warn, Remove (from branch) and Delete (from disk): <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> none </td>
<td> W </td>
<td> RD </td>
<td> W </td>
<td> R
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> -f </td>
<td> R </td>
<td> RD </td>
<td> RD </td>
<td> R
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> -A </td>
<td> W </td>
<td> W </td>
<td> W </td>
<td> R
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> -Af </td>
<td> R </td>
<td> R </td>
<td> R </td>
<td> R
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> Note that remove never deletes files in Added [A] state from the working directory, not even if option &#8211;force is specified. </p>
<p> Returns 0 on success, 1 if any warnings encountered. </p>
<p> Options:</p>
<dl>
<dt><code>-A, &#8211;after</code></p>
<dd> record delete for missing files</p>
<dt><code>-f, &#8211;force</code></p>
<dd> remove (and delete) file even if added or modified</p>
<dt><code>-I, &#8211;include</code></p>
<dd> include names matching the given patterns</p>
<dt><code>-X, &#8211;exclude</code></p>
<dd> exclude names matching the given patterns </p>
<p> aliases: rm</dl>
<h3>rename</h3>
<pre>
hg rename [OPTION]... SOURCE... DEST
</pre>
<p> Mark dest as copies of sources; mark sources for deletion. If dest is a directory, copies are put in that directory. If dest is a file, there can only be one source. </p>
<p> By default, this command copies the contents of files as they exist in the working directory. If invoked with -A/&#8211;after, the operation is recorded, but no copying is performed. </p>
<p> This command takes effect at the next commit. To undo a rename before that, see <code>hg revert</code>:. </p>
<p> Returns 0 on success, 1 if errors are encountered. </p>
<p> Options:</p>
<dl>
<dt><code>-A, &#8211;after</code></p>
<dd> record a rename that has already occurred</p>
<dt><code>-f, &#8211;force</code></p>
<dd> forcibly copy over an existing managed file</p>
<dt><code>-I, &#8211;include</code></p>
<dd> include names matching the given patterns</p>
<dt><code>-X, &#8211;exclude</code></p>
<dd> exclude names matching the given patterns</p>
<dt><code>-n, &#8211;dry-run</code></p>
<dd> do not perform actions, just print output </p>
<p> aliases: move mv</dl>
<h3>resolve</h3>
<p>hg resolve[OPTION]&#8230;[FILE]&#8230;</p>
<p> Merges with unresolved conflicts are often the result of non-interactive merging using the <code>internal:merge</code> configuration setting, or a command-line merge tool like <code>diff3</code>. The resolve command is used to manage the files involved in a merge, after <code>hg merge</code>: has been run, and before <code>hg commit</code>: is run (i.e. the working directory must have two parents). See <code>hg help merge-tools</code>: for information on configuring merge tools. </p>
<p> The resolve command can be used in the following ways:</p>
<dl>
<dt>&bull;</p>
<dd> <code>hg resolve [&#8211;tool TOOL] FILE&#8230;</code>:: attempt to re-merge the specified files, discarding any previous merge attempts. Re-merging is not performed for files already marked as resolved. Use <code>&#8211;all/-a</code> to select all unresolved files. <code>&#8211;tool</code> can be used to specify the merge tool used for the given files. It overrides the HGMERGE environment variable and your configuration files. Previous file contents are saved with a <code>.orig</code> suffix.</p>
<dt>&bull;</p>
<dd> <code>hg resolve -m [FILE]</code>:: mark a file as having been resolved (e.g. after having manually fixed-up the files). The default is to mark all unresolved files.</p>
<dt>&bull;</p>
<dd> <code>hg resolve -u [FILE]&#8230;</code>:: mark a file as unresolved. The default is to mark all resolved files.</p>
<dt>&bull;</p>
<dd> <code>hg resolve -l</code>:: list files which had or still have conflicts. In the printed list, <code>U</code> = unresolved and <code>R</code> = resolved. </p>
<p> Note that Mercurial will not let you commit files with unresolved merge conflicts. You must use <code>hg resolve -m &#8230;</code>: before you can commit after a conflicting merge. </p>
<p> Returns 0 on success, 1 if any files fail a resolve attempt. </p>
<p> Options:</p>
<dt><code>-a, &#8211;all</code></p>
<dd> select all unresolved files</p>
<dt><code>-l, &#8211;list</code></p>
<dd> list state of files needing merge</p>
<dt><code>-m, &#8211;mark</code></p>
<dd> mark files as resolved</p>
<dt><code>-u, &#8211;unmark</code></p>
<dd> mark files as unresolved</p>
<dt><code>-n, &#8211;no-status</code></p>
<dd> hide status prefix</p>
<dt><code>-t, &#8211;tool</code></p>
<dd> specify merge tool</p>
<dt><code>-I, &#8211;include</code></p>
<dd> include names matching the given patterns</p>
<dt><code>-X, &#8211;exclude</code></p>
<dd> exclude names matching the given patterns</dl>
<h3>revert</h3>
<p>hg revert[OPTION]&#8230;[-r REV][NAME]&#8230;</p>
<dl>
<dt>Note</p>
<dd> To check out earlier revisions, you should use <code>hg update REV</code>:. To cancel an uncommitted merge (and lose your changes), use <code>hg update &#8211;clean .</code>:. </p>
<p> With no revision specified, revert the specified files or directories to the contents they had in the parent of the working directory. This restores the contents of files to an unmodified state and unschedules adds, removes, copies, and renames. If the working directory has two parents, you must explicitly specify a revision. </p>
<p> Using the -r/&#8211;rev or -d/&#8211;date options, revert the given files or directories to their states as of a specific revision. Because revert does not change the working directory parents, this will cause these files to appear modified. This can be helpful to &quot;back out&quot; some or all of an earlier change. See <code>hg backout</code>: for a related method. </p>
<p> Modified files are saved with a .orig suffix before reverting. To disable these backups, use &#8211;no-backup. </p>
<p> See <code>hg help dates</code>: for a list of formats valid for -d/&#8211;date. </p>
<p> Returns 0 on success. </p>
<p> Options:</p>
<dt><code>-a, &#8211;all</code></p>
<dd> revert all changes when no arguments given</p>
<dt><code>-d, &#8211;date</code></p>
<dd> tipmost revision matching date</p>
<dt><code>-r, &#8211;rev</code></p>
<dd> revert to the specified revision</p>
<dt><code>-C, &#8211;no-backup</code></p>
<dd> do not save backup copies of files</p>
<dt><code>-I, &#8211;include</code></p>
<dd> include names matching the given patterns</p>
<dt><code>-X, &#8211;exclude</code></p>
<dd> exclude names matching the given patterns</p>
<dt><code>-n, &#8211;dry-run</code></p>
<dd> do not perform actions, just print output</dl>
<h3>rollback</h3>
<pre>
hg rollback
</pre>
<p> This command should be used with care. There is only one level of rollback, and there is no way to undo a rollback. It will also restore the dirstate at the time of the last transaction, losing any dirstate changes since that time. This command does not alter the working directory. </p>
<p> Transactions are used to encapsulate the effects of all commands that create new changesets or propagate existing changesets into a repository. </p>
<p> For example, the following commands are transactional, and their effects can be rolled back:</p>
<dl>
<dt>&bull;</p>
<dd> commit</p>
<dt>&bull;</p>
<dd> import</p>
<dt>&bull;</p>
<dd> pull</p>
<dt>&bull;</p>
<dd> push (with this repository as the destination)</p>
<dt>&bull;</p>
<dd> unbundle </p>
<p> To avoid permanent data loss, rollback will refuse to rollback a commit transaction if it isn&#8217;t checked out. Use &#8211;force to override this protection. </p>
<p> This command is not intended for use on public repositories. Once changes are visible for pull by other users, rolling a transaction back locally is ineffective (someone else may already have pulled the changes). Furthermore, a race is possible with readers of the repository; for example an in-progress pull from the repository may fail if a rollback is performed. </p>
<p> Returns 0 on success, 1 if no rollback data is available. </p>
<p> Options:</p>
<dt><code>-n, &#8211;dry-run</code></p>
<dd> do not perform actions, just print output</p>
<dt><code>-f, &#8211;force</code></p>
<dd> ignore safety measures</dl>
<h3>root</h3>
<pre>
hg root
</pre>
<p> Print the root directory of the current repository. </p>
<p> Returns 0 on success.</p>
<h3>serve</h3>
<pre>
hg serve [OPTION]...
</pre>
<p> Start a local HTTP repository browser and pull server. You can use this for ad-hoc sharing and browsing of repositories. It is recommended to use a real web server to serve a repository for longer periods of time. </p>
<p> Please note that the server does not implement access control. This means that, by default, anybody can read from the server and nobody can write to it by default. Set the <code>web.allow_push</code> option to <code>*</code> to allow everybody to push to the server. You should use a real web server if you need to authenticate users. </p>
<p> By default, the server logs accesses to stdout and errors to stderr. Use the -A/&#8211;accesslog and -E/&#8211;errorlog options to log to files. </p>
<p> To have the server choose a free port number to listen on, specify a port number of 0; in this case, the server will print the port number it uses. </p>
<p> Returns 0 on success. </p>
<p> Options:</p>
<dl>
<dt><code>-A, &#8211;accesslog</code></p>
<dd> name of access log file to write to</p>
<dt><code>-d, &#8211;daemon</code></p>
<dd> run server in background</p>
<dt><code>&#8211;daemon-pipefds</code></p>
<dd> used internally by daemon mode</p>
<dt><code>-E, &#8211;errorlog</code></p>
<dd> name of error log file to write to</p>
<dt><code>-p, &#8211;port</code></p>
<dd> port to listen on (default: 8000)</p>
<dt><code>-a, &#8211;address</code></p>
<dd> address to listen on (default: all interfaces)</p>
<dt><code>&#8211;prefix</code></p>
<dd> prefix path to serve from (default: server root)</p>
<dt><code>-n, &#8211;name</code></p>
<dd> name to show in web pages (default: working directory)</p>
<dt><code>&#8211;web-conf</code></p>
<dd> name of the hgweb config file (see &quot;hg help hgweb&quot;)</p>
<dt><code>&#8211;webdir-conf</code></p>
<dd> name of the hgweb config file (DEPRECATED)</p>
<dt><code>&#8211;pid-file</code></p>
<dd> name of file to write process ID to</p>
<dt><code>&#8211;stdio</code></p>
<dd> for remote clients</p>
<dt><code>&#8211;cmdserver</code></p>
<dd> for remote clients</p>
<dt><code>-t, &#8211;templates</code></p>
<dd> web templates to use</p>
<dt><code>&#8211;style</code></p>
<dd> template style to use</p>
<dt><code>-6, &#8211;ipv6</code></p>
<dd> use IPv6 in addition to IPv4</p>
<dt><code>&#8211;certificate</code></p>
<dd> SSL certificate file</dl>
<h3>showconfig</h3>
<p>hg showconfig[-u][NAME]&#8230;</p>
<p> With no arguments, print names and values of all config items. </p>
<p> With one argument of the form section.name, print just the value of that config item. </p>
<p> With multiple arguments, print names and values of all config items with matching section names. </p>
<p> With &#8211;debug, the source (filename and line number) is printed for each config item. </p>
<p> Returns 0 on success. </p>
<p> Options:</p>
<dl>
<dt><code>-u, &#8211;untrusted</code></p>
<dd> show untrusted configuration options </p>
<p> aliases: debugconfig</dl>
<h3>status</h3>
<p>hg status[OPTION]&#8230;[FILE]&#8230;</p>
<p> Show status of files in the repository. If names are given, only files that match are shown. Files that are clean or ignored or the source of a copy/move operation, are not listed unless -c/&#8211;clean, -i/&#8211;ignored, -C/&#8211;copies or -A/&#8211;all are given. Unless options described with &quot;show only &#8230;&quot; are given, the options -mardu are used. </p>
<p> Option -q/&#8211;quiet hides untracked (unknown and ignored) files unless explicitly requested with -u/&#8211;unknown or -i/&#8211;ignored.</p>
<dl>
<dt>Note</p>
<dd> status may appear to disagree with diff if permissions have changed or a merge has occurred. The standard diff format does not report permission changes and diff only reports changes relative to one merge parent. </p>
<p> If one revision is given, it is used as the base revision. If two revisions are given, the differences between them are shown. The &#8211;change option can also be used as a shortcut to list the changed files of a revision from its first parent. </p>
<p> The codes used to show the status of files are: </p>
<pre>
M = modified
A = added
R = removed
C = clean
! = missing (deleted by non-hg command, but still tracked)
? = not tracked
I = ignored
  = origin of the previous file listed as A (added)
</pre>
<p> Examples:</p>
<dt>&bull;</p>
<dd> show changes in the working directory relative to a changeset: </p>
<pre>
hg status --rev 9353
</pre>
<dt>&bull;</p>
<dd> show all changes including copies in an existing changeset: </p>
<pre>
hg status --copies --change 9353
</pre>
<dt>&bull;</p>
<dd> get a NUL separated list of added files, suitable for xargs: </p>
<pre>
hg status -an0
</pre>
<p> Returns 0 on success. </p>
<p> Options:</p>
<dt><code>-A, &#8211;all</code></p>
<dd> show status of all files</p>
<dt><code>-m, &#8211;modified</code></p>
<dd> show only modified files</p>
<dt><code>-a, &#8211;added</code></p>
<dd> show only added files</p>
<dt><code>-r, &#8211;removed</code></p>
<dd> show only removed files</p>
<dt><code>-d, &#8211;deleted</code></p>
<dd> show only deleted (but tracked) files</p>
<dt><code>-c, &#8211;clean</code></p>
<dd> show only files without changes</p>
<dt><code>-u, &#8211;unknown</code></p>
<dd> show only unknown (not tracked) files</p>
<dt><code>-i, &#8211;ignored</code></p>
<dd> show only ignored files</p>
<dt><code>-n, &#8211;no-status</code></p>
<dd> hide status prefix</p>
<dt><code>-C, &#8211;copies</code></p>
<dd> show source of copied files</p>
<dt><code>-0, &#8211;print0</code></p>
<dd> end filenames with NUL, for use with xargs</p>
<dt><code>&#8211;rev</code></p>
<dd> show difference from revision</p>
<dt><code>&#8211;change</code></p>
<dd> list the changed files of a revision</p>
<dt><code>-I, &#8211;include</code></p>
<dd> include names matching the given patterns</p>
<dt><code>-X, &#8211;exclude</code></p>
<dd> exclude names matching the given patterns</p>
<dt><code>-S, &#8211;subrepos</code></p>
<dd> recurse into subrepositories </p>
<p> aliases: st</dl>
<h3>summary</h3>
<pre>
hg summary [--remote]
</pre>
<p> This generates a brief summary of the working directory state, including parents, branch, commit status, and available updates. </p>
<p> With the &#8211;remote option, this will check the default paths for incoming and outgoing changes. This can be time-consuming. </p>
<p> Returns 0 on success. </p>
<p> Options:</p>
<dl>
<dt><code>&#8211;remote</code></p>
<dd> check for push and pull </p>
<p> aliases: sum</dl>
<h3>tag</h3>
<p>hg tag[-f][-l][-m TEXT][-d DATE][-u USER][-r REV] NAME&#8230;</p>
<p> Name a particular revision using &lt;name&gt;. </p>
<p> Tags are used to name particular revisions of the repository and are very useful to compare different revisions, to go back to significant earlier versions or to mark branch points as releases, etc. Changing an existing tag is normally disallowed; use -f/&#8211;force to override. </p>
<p> If no revision is given, the parent of the working directory is used, or tip if no revision is checked out. </p>
<p> To facilitate version control, distribution, and merging of tags, they are stored as a file named &quot;.hgtags&quot; which is managed similarly to other project files and can be hand-edited if necessary. This also means that tagging creates a new commit. The file &quot;.hg/localtags&quot; is used for local tags (not shared among repositories). </p>
<p> Tag commits are usually made at the head of a branch. If the parent of the working directory is not a branch head, <code>hg tag</code>: aborts; use -f/&#8211;force to force the tag commit to be based on a non-head changeset. </p>
<p> See <code>hg help dates</code>: for a list of formats valid for -d/&#8211;date. </p>
<p> Since tag names have priority over branch names during revision lookup, using an existing branch name as a tag name is discouraged. </p>
<p> Returns 0 on success. </p>
<p> Options:</p>
<dl>
<dt><code>-f, &#8211;force</code></p>
<dd> force tag</p>
<dt><code>-l, &#8211;local</code></p>
<dd> make the tag local</p>
<dt><code>-r, &#8211;rev</code></p>
<dd> revision to tag</p>
<dt><code>&#8211;remove</code></p>
<dd> remove a tag</p>
<dt><code>-e, &#8211;edit</code></p>
<dd> edit commit message</p>
<dt><code>-m, &#8211;message</code></p>
<dd> use &lt;text&gt; as commit message</p>
<dt><code>-d, &#8211;date</code></p>
<dd> record the specified date as commit date</p>
<dt><code>-u, &#8211;user</code></p>
<dd> record the specified user as committer</dl>
<h3>tags</h3>
<pre>
hg tags
</pre>
<p> This lists both regular and local tags. When the -v/&#8211;verbose switch is used, a third column &quot;local&quot; is printed for local tags. </p>
<p> Returns 0 on success.</p>
<h3>tip</h3>
<p>hg tip[-p][-g]</p>
<p> The tip revision (usually just called the tip) is the changeset most recently added to the repository (and therefore the most recently changed head). </p>
<p> If you have just made a commit, that commit will be the tip. If you have just pulled changes from another repository, the tip of that repository becomes the current tip. The &quot;tip&quot; tag is special and cannot be renamed or assigned to a different changeset. </p>
<p> Returns 0 on success. </p>
<p> Options:</p>
<dl>
<dt><code>-p, &#8211;patch</code></p>
<dd> show patch</p>
<dt><code>-g, &#8211;git</code></p>
<dd> use git extended diff format</p>
<dt><code>&#8211;style</code></p>
<dd> display using template map file</p>
<dt><code>&#8211;template</code></p>
<dd> display with template</dl>
<h3>unbundle</h3>
<pre>
hg unbundle [-u] FILE...
</pre>
<p> Apply one or more compressed changegroup files generated by the bundle command. </p>
<p> Returns 0 on success, 1 if an update has unresolved files. </p>
<p> Options:</p>
<dl>
<dt><code>-u, &#8211;update</code></p>
<dd> update to new branch head if changesets were unbundled</dl>
<h3>update</h3>
<p>hg update[-c][-C][-d DATE][[-r] REV]</p>
<p> Update the repository&#8217;s working directory to the specified changeset. If no changeset is specified, update to the tip of the current named branch and move the current bookmark (see <code>hg help bookmarks</code>:). </p>
<p> Update sets the working directory&#8217;s parent revision to the specified changeset (see <code>hg help parents</code>:). </p>
<p> If the changeset is not a descendant or ancestor of the working directory&#8217;s parent, the update is aborted. With the -c/&#8211;check option, the working directory is checked for uncommitted changes; if none are found, the working directory is updated to the specified changeset. </p>
<p> The following rules apply when the working directory contains uncommitted changes:</p>
<dl>
<dt>1.</p>
<dd> If neither -c/&#8211;check nor -C/&#8211;clean is specified, and if the requested changeset is an ancestor or descendant of the working directory&#8217;s parent, the uncommitted changes are merged into the requested changeset and the merged result is left uncommitted. If the requested changeset is not an ancestor or descendant (that is, it is on another branch), the update is aborted and the uncommitted changes are preserved.</p>
<dt>2.</p>
<dd> With the -c/&#8211;check option, the update is aborted and the uncommitted changes are preserved.</p>
<dt>3.</p>
<dd> With the -C/&#8211;clean option, uncommitted changes are discarded and the working directory is updated to the requested changeset. </p>
<p> To cancel an uncommitted merge (and lose your changes), use <code>hg update &#8211;clean .</code>:. </p>
<p> Use null as the changeset to remove the working directory (like <code>hg clone -U</code>:). </p>
<p> If you want to revert just one file to an older revision, use <code>hg revert [-r REV] NAME</code>:. </p>
<p> See <code>hg help dates</code>: for a list of formats valid for -d/&#8211;date. </p>
<p> Returns 0 on success, 1 if there are unresolved files. </p>
<p> Options:</p>
<dt><code>-C, &#8211;clean</code></p>
<dd> discard uncommitted changes (no backup)</p>
<dt><code>-c, &#8211;check</code></p>
<dd> update across branches if no uncommitted changes</p>
<dt><code>-d, &#8211;date</code></p>
<dd> tipmost revision matching date</p>
<dt><code>-r, &#8211;rev</code></p>
<dd> revision </p>
<p> aliases: up checkout co</dl>
<h3>verify</h3>
<pre>
hg verify
</pre>
<p> Verify the integrity of the current repository. </p>
<p> This will perform an extensive check of the repository&#8217;s integrity, validating the hashes and checksums of each entry in the changelog, manifest, and tracked files, as well as the integrity of their crosslinks and indices. </p>
<p> Please see <a rel="nofollow" href="http://mercurial.selenic.com/wiki/RepositoryCorruption:">http://mercurial.selenic.com/wiki/RepositoryCorruption:</a> for more information about recovery from corruption of the repository. </p>
<p> Returns 0 on success, 1 if errors are encountered.</p>
<h3>version</h3>
<pre>
hg version
</pre>
<p> output version and copyright information</p>
<h2>DATE FORMATS</h2>
<p> Some commands allow the user to specify a date, e.g.:</p>
<dl>
<dt>&bull;</p>
<dd> backout, commit, import, tag: Specify the commit date.</p>
<dt>&bull;</p>
<dd> log, revert, update: Select revision(s) by date. </p>
<p> Many date formats are valid. Here are some examples:</p>
<dt>&bull;</p>
<dd> <code>Wed Dec 6 13:18:29 2006</code> (local timezone assumed)</p>
<dt>&bull;</p>
<dd> <code>Dec 6 13:18 -0600</code> (year assumed, time offset provided)</p>
<dt>&bull;</p>
<dd> <code>Dec 6 13:18 UTC</code> (UTC and GMT are aliases for +0000)</p>
<dt>&bull;</p>
<dd> <code>Dec 6</code> (midnight)</p>
<dt>&bull;</p>
<dd> <code>13:18</code> (today assumed)</p>
<dt>&bull;</p>
<dd> <code>3:39</code> (3:39AM assumed)</p>
<dt>&bull;</p>
<dd> <code>3:39pm</code> (15:39)</p>
<dt>&bull;</p>
<dd> <code>2006-12-06 13:18:29</code> (ISO 8601 format)</p>
<dt>&bull;</p>
<dd> <code>2006-12-6 13:18</code></p>
<dt>&bull;</p>
<dd> <code>2006-12-6</code></p>
<dt>&bull;</p>
<dd> <code>12-6</code></p>
<dt>&bull;</p>
<dd> <code>12/6</code></p>
<dt>&bull;</p>
<dd> <code>12/6/6</code> (Dec 6 2006)</p>
<dt>&bull;</p>
<dd> <code>today</code> (midnight)</p>
<dt>&bull;</p>
<dd> <code>yesterday</code> (midnight)</p>
<dt>&bull;</p>
<dd> <code>now</code> &#8211; right now </p>
<p> Lastly, there is Mercurial&#8217;s internal format:</p>
<dt>&bull;</p>
<dd> <code>1165432709 0</code> (Wed Dec 6 13:18:29 2006 UTC) </p>
<p> This is the internal representation format for dates. The first number is the number of seconds since the epoch (1970-01-01 00:00 UTC). The second is the offset of the local timezone, in seconds west of UTC (negative if the timezone is east of UTC). </p>
<p> The log command also accepts date ranges:</p>
<dt>&bull;</p>
<dd> <code>&lt;DATE</code> &#8211; at or before a given date/time</p>
<dt>&bull;</p>
<dd> <code>&gt;DATE</code> &#8211; on or after a given date/time</p>
<dt>&bull;</p>
<dd> <code>DATE to DATE</code> &#8211; a date range, inclusive</p>
<dt>&bull;</p>
<dd> <code>-DAYS</code> &#8211; within a given number of days of today</dl>
<h2>DIFF FORMATS</h2>
<p> Mercurial&#8217;s default format for showing changes between two versions of a file is compatible with the unified format of GNU diff, which can be used by GNU patch and many other standard tools. </p>
<p> While this standard format is often enough, it does not encode the following information:</p>
<dl>
<dt>&bull;</p>
<dd> executable status and other permission bits</p>
<dt>&bull;</p>
<dd> copy or rename information</p>
<dt>&bull;</p>
<dd> changes in binary files</p>
<dt>&bull;</p>
<dd> creation or deletion of empty files </p>
<p> Mercurial also supports the extended diff format from the git VCS which addresses these limitations. The git diff format is not produced by default because a few widespread tools still do not understand this format. </p>
<p> This means that when generating diffs from a Mercurial repository (e.g. with <code>hg export</code>:), you should be careful about things like file copies and renames or other things mentioned above, because when applying a standard diff to a different repository, this extra information is lost. Mercurial&#8217;s internal operations (like push and pull) are not affected by this, because they use an internal binary format for communicating changes. </p>
<p> To make Mercurial produce the git extended diff format, use the &#8211;git option available for many commands, or set &#8216;git = True&#8217; in the [diff] section of your configuration file. You do not need to set this option when importing diffs in this format or using them in the mq extension.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>HG</code></p>
<dd> Path to the &#8216;hg&#8217; executable, automatically passed when running hooks, extensions or external tools. If unset or empty, this is the hg executable&#8217;s name if it&#8217;s frozen, or an executable named &#8216;hg&#8217; (with %PATHEXT% [defaulting to COM/EXE/BAT/CMD] extensions on Windows) is searched.</p>
<dt><code>HGEDITOR</code></p>
<dd> This is the name of the editor to run when committing. See EDITOR. </p>
<p> (deprecated, use configuration file)</p>
<dt><code>HGENCODING</code></p>
<dd> This overrides the default locale setting detected by Mercurial. This setting is used to convert data including usernames, changeset descriptions, tag names, and branches. This setting can be overridden with the &#8211;encoding command-line option.</p>
<dt><code>HGENCODINGMODE</code></p>
<dd> This sets Mercurial&#8217;s behavior for handling unknown characters while transcoding user input. The default is &quot;strict&quot;, which causes Mercurial to abort if it can&#8217;t map a character. Other settings include &quot;replace&quot;, which replaces unknown characters, and &quot;ignore&quot;, which drops them. This setting can be overridden with the &#8211;encodingmode command-line option.</p>
<dt><code>HGENCODINGAMBIGUOUS</code></p>
<dd> This sets Mercurial&#8217;s behavior for handling characters with &quot;ambiguous&quot; widths like accented Latin characters with East Asian fonts. By default, Mercurial assumes ambiguous characters are narrow, set this variable to &quot;wide&quot; if such characters cause formatting problems.</p>
<dt><code>HGMERGE</code></p>
<dd> An executable to use for resolving merge conflicts. The program will be executed with three arguments: local file, remote file, ancestor file. </p>
<p> (deprecated, use configuration file)</p>
<dt><code>HGRCPATH</code></p>
<dd> A list of files or directories to search for configuration files. Item separator is &quot;:&quot; on Unix, &quot;;&quot; on Windows. If HGRCPATH is not set, platform default search path is used. If empty, only the .hg/hgrc from the current repository is read. </p>
<p> For each element in HGRCPATH:</p>
<dt>&bull;</p>
<dd> if it&#8217;s a directory, all files ending with .rc are added</p>
<dt>&bull;</p>
<dd> otherwise, the file itself will be added</p>
<dt><code>HGPLAIN</code></p>
<dd> When set, this disables any configuration settings that might change Mercurial&#8217;s default output. This includes encoding, defaults, verbose mode, debug mode, quiet mode, tracebacks, and localization. This can be useful when scripting against Mercurial in the face of existing user configuration. </p>
<p> Equivalent options set via command line flags or environment variables are not overridden.</p>
<dt><code>HGPLAINEXCEPT</code></p>
<dd> This is a comma-separated list of features to preserve when HGPLAIN is enabled. Currently the only value supported is &quot;i18n&quot;, which preserves internationalization in plain mode. </p>
<p> Setting HGPLAINEXCEPT to anything (even an empty string) will enable plain mode.</p>
<dt><code>HGUSER</code></p>
<dd> This is the string used as the author of a commit. If not set, available values will be considered in this order:</p>
<dt>&bull;</p>
<dd> HGUSER (deprecated)</p>
<dt>&bull;</p>
<dd> configuration files from the HGRCPATH</p>
<dt>&bull;</p>
<dd> EMAIL</p>
<dt>&bull;</p>
<dd> interactive prompt</p>
<dt>&bull;</p>
<dd> LOGNAME (with <code>@hostname</code> appended) </p>
<p> (deprecated, use configuration file)</p>
<dt><code>EMAIL</code></p>
<dd> May be used as the author of a commit; see HGUSER.</p>
<dt><code>LOGNAME</code></p>
<dd> May be used as the author of a commit; see HGUSER.</p>
<dt><code>VISUAL</code></p>
<dd> This is the name of the editor to use when committing. See EDITOR.</p>
<dt><code>EDITOR</code></p>
<dd> Sometimes Mercurial needs to open a text file in an editor for a user to modify, for example when writing commit messages. The editor it uses is determined by looking at the environment variables HGEDITOR, VISUAL and EDITOR, in that order. The first non-empty one is chosen. If all of them are empty, the editor defaults to &#8216;vi&#8217;.</p>
<dt><code>PYTHONPATH</code></p>
<dd> This is used by Python to find imported modules and may need to be set appropriately if this Mercurial is not installed system-wide.</dl>
<h2>USING ADDITIONAL FEATURES</h2>
<p> Mercurial has the ability to add new features through the use of extensions. Extensions may add new commands, add options to existing commands, change the default behavior of commands, or implement hooks. </p>
<p> Extensions are not loaded by default for a variety of reasons: they can increase startup overhead; they may be meant for advanced usage only; they may provide potentially dangerous abilities (such as letting you destroy or modify history); they might not be ready for prime time; or they may alter some usual behaviors of stock Mercurial. It is thus up to the user to activate extensions as needed. </p>
<p> To enable the &quot;foo&quot; extension, either shipped with Mercurial or in the Python search path, create an entry for it in your configuration file, like this: </p>
<pre>
[extensions]
foo =
</pre>
<p> You may also specify the full path to an extension: </p>
<pre>
[extensions]
myfeature = ~/.hgext/myfeature.py
</pre>
<p> To explicitly disable an extension enabled in a configuration file of broader scope, prepend its path with !: </p>
<pre>
[extensions]
# disabling extension bar residing in /path/to/extension/bar.py
bar = !/path/to/extension/bar.py
# ditto, but no path was supplied for extension baz
baz = !
</pre>
<p> disabled extensions:</p>
<dl>
<dt><code>acl</code></p>
<dd> hooks for controlling repository access</p>
<dt><code>blackbox</code></p>
<dd> log repository events to a blackbox for debugging</p>
<dt><code>bugzilla</code></p>
<dd> hooks for integrating with the Bugzilla bug tracker</p>
<dt><code>children</code></p>
<dd> command to display child changesets (DEPRECATED)</p>
<dt><code>churn</code></p>
<dd> command to display statistics about repository history</p>
<dt><code>color</code></p>
<dd> colorize output from some commands</p>
<dt><code>convert</code></p>
<dd> import revisions from foreign VCS repositories into Mercurial</p>
<dt><code>eol</code></p>
<dd> automatically manage newlines in repository files</p>
<dt><code>extdiff</code></p>
<dd> command to allow external programs to compare revisions</p>
<dt><code>factotum</code></p>
<dd> http authentication with factotum</p>
<dt><code>fetch</code></p>
<dd> pull, update and merge in one command (DEPRECATED)</p>
<dt><code>gpg</code></p>
<dd> commands to sign and verify changesets</p>
<dt><code>graphlog</code></p>
<dd> command to view revision graphs from a shell</p>
<dt><code>hgcia</code></p>
<dd> hooks for integrating with the CIA.vc notification service</p>
<dt><code>hgk</code></p>
<dd> browse the repository in a graphical way</p>
<dt><code>highlight</code></p>
<dd> syntax highlighting for hgweb (requires Pygments)</p>
<dt><code>histedit</code></p>
<dd> interactive history editing</p>
<dt><code>inotify</code></p>
<dd> accelerate status report using Linux&#8217;s inotify service</p>
<dt><code>interhg</code></p>
<dd> expand expressions into changelog and summaries</p>
<dt><code>keyword</code></p>
<dd> expand keywords in tracked files</p>
<dt><code>largefiles</code></p>
<dd> track large binary files</p>
<dt><code>mq</code></p>
<dd> manage a stack of patches</p>
<dt><code>notify</code></p>
<dd> hooks for sending email push notifications</p>
<dt><code>pager</code></p>
<dd> browse command output with an external pager</p>
<dt><code>patchbomb</code></p>
<dd> command to send changesets as (a series of) patch emails</p>
<dt><code>progress</code></p>
<dd> show progress bars for some actions</p>
<dt><code>purge</code></p>
<dd> command to delete untracked files from the working directory</p>
<dt><code>rebase</code></p>
<dd> command to move sets of revisions to a different ancestor</p>
<dt><code>record</code></p>
<dd> commands to interactively select changes for commit/qrefresh</p>
<dt><code>relink</code></p>
<dd> recreates hardlinks between repository clones</p>
<dt><code>schemes</code></p>
<dd> extend schemes with shortcuts to repository swarms</p>
<dt><code>share</code></p>
<dd> share a common history between several working directories</p>
<dt><code>transplant</code></p>
<dd> command to transplant changesets from another branch</p>
<dt><code>win32mbcs</code></p>
<dd> allow the use of MBCS paths with problematic encodings</p>
<dt><code>win32text</code></p>
<dd> perform automatic newline conversion</p>
<dt><code>zeroconf</code></p>
<dd> discover and advertise repositories on the local network</dl>
<h2>SPECIFYING FILE SETS</h2>
<p> Mercurial supports a functional language for selecting a set of files. </p>
<p> Like other file patterns, this pattern type is indicated by a prefix, &#8216;set:&#8217;. The language supports a number of predicates which are joined by infix operators. Parenthesis can be used for grouping. </p>
<p> Identifiers such as filenames or patterns must be quoted with single or double quotes if they contain characters outside of <code>[.*{}[]?/\_a-zA-Z0-9�-�]</code> or if they match one of the predefined predicates. This generally applies to file patterns other than globs and arguments for predicates. </p>
<p> Special characters can be used in quoted identifiers by escaping them, e.g., <code>
</code> is interpreted as a newline. To prevent them from being interpreted, strings can be prefixed with <code>r</code>, e.g. <code>r&#8217;&#8230;&#8217;</code>. </p>
<p> There is a single prefix operator:</p>
<dl>
<dt><code>not x</code></p>
<dd>
<p> Files not in x. Short form is <code>! x</code>. </p>
<p> These are the supported infix operators:</p>
<dt><code>x and y</code></p>
<dd>
<p> The intersection of files in x and y. Short form is <code>x &amp; y</code>.</p>
<dt><code>x or y</code></p>
<dd>
<p> The union of files in x and y. There are two alternative short forms: <code>x | y</code> and <code>x + y</code>.</p>
<dt><code>x &#8211; y</code></p>
<dd>
<p> Files in x but not in y. </p>
<p> The following predicates are supported:</p>
<dt><code>added()</code></p>
<dd>
<p> File that is added according to status.</p>
<dt><code>binary()</code></p>
<dd>
<p> File that appears to be binary (contains NUL bytes).</p>
<dt><code>clean()</code></p>
<dd>
<p> File that is clean according to status.</p>
<dt><code>copied()</code></p>
<dd>
<p> File that is recorded as being copied.</p>
<dt><code>deleted()</code></p>
<dd>
<p> File that is deleted according to status.</p>
<dt><code>encoding(name)</code></p>
<dd>
<p> File can be successfully decoded with the given character encoding. May not be useful for encodings other than ASCII and UTF-8.</p>
<dt><code>eol(style)</code></p>
<dd>
<p> File contains newlines of the given style (dos, unix, mac). Binary files are excluded, files with mixed line endings match multiple styles.</p>
<dt><code>exec()</code></p>
<dd>
<p> File that is marked as executable.</p>
<dt><code>grep(regex)</code></p>
<dd>
<p> File contains the given regular expression.</p>
<dt><code>hgignore()</code></p>
<dd>
<p> File that matches the active .hgignore pattern.</p>
<dt><code>ignored()</code></p>
<dd>
<p> File that is ignored according to status. These files will only be considered if this predicate is used.</p>
<dt><code>modified()</code></p>
<dd>
<p> File that is modified according to status.</p>
<dt><code>removed()</code></p>
<dd>
<p> File that is removed according to status.</p>
<dt><code>resolved()</code></p>
<dd>
<p> File that is marked resolved according to the resolve state.</p>
<dt><code>size(expression)</code></p>
<dd>
<p> File size matches the given expression. Examples:</p>
<dt>&bull;</p>
<dd> 1k (files from 1024 to 2047 bytes)</p>
<dt>&bull;</p>
<dd> &lt; 20k (files less than 20480 bytes)</p>
<dt>&bull;</p>
<dd> &gt;= .5MB (files at least 524288 bytes)</p>
<dt>&bull;</p>
<dd> 4k &#8211; 1MB (files from 4096 bytes to 1048576 bytes)</p>
<dt><code>subrepo([pattern])</code></p>
<dd>
<p> Subrepositories whose paths match the given pattern.</p>
<dt><code>symlink()</code></p>
<dd>
<p> File that is marked as a symlink.</p>
<dt><code>unknown()</code></p>
<dd>
<p> File that is unknown according to status. These files will only be considered if this predicate is used.</p>
<dt><code>unresolved()</code></p>
<dd>
<p> File that is marked unresolved according to the resolve state. </p>
<p> Some sample queries:</p>
<dt>&bull;</p>
<dd> Show status of files that appear to be binary in the working directory: </p>
<pre>
hg status -A &quot;set:binary()&quot;
</pre>
<dt>&bull;</p>
<dd> Forget files that are in .hgignore but are already tracked: </p>
<pre>
hg forget &quot;set:hgignore() and not ignored()&quot;
</pre>
<dt>&bull;</p>
<dd> Find text files that contain a string: </p>
<pre>
hg locate &quot;set:grep(magic) and not binary()&quot;
</pre>
<dt>&bull;</p>
<dd> Find C files in a non-standard encoding: </p>
<pre>
hg locate &quot;set:**.c and not encoding('UTF-8')&quot;
</pre>
<dt>&bull;</p>
<dd> Revert copies of large binary files: </p>
<pre>
hg revert &quot;set:copied() and binary() and size('&gt;1M')&quot;
</pre>
<dt>&bull;</p>
<dd> Remove files listed in foo.lst that contain the letter a or b: </p>
<pre>
hg remove &quot;set: 'listfile:foo.lst' and (**a* or **b*)&quot;
</pre>
<p> See also <code>hg help patterns</code>:.</dl>
<h2>GLOSSARY</h2>
<dl>
<dt><code>Ancestor</code></p>
<dd> Any changeset that can be reached by an unbroken chain of parent changesets from a given changeset. More precisely, the ancestors of a changeset can be defined by two properties: a parent of a changeset is an ancestor, and a parent of an ancestor is an ancestor. See also: &#8216;Descendant&#8217;.</p>
<dt><code>Bookmark</code></p>
<dd> Bookmarks are pointers to certain commits that move when committing. They are similar to tags in that it is possible to use bookmark names in all places where Mercurial expects a changeset ID, e.g., with <code>hg update</code>:. Unlike tags, bookmarks move along when you make a commit. </p>
<p> Bookmarks can be renamed, copied and deleted. Bookmarks are local, unless they are explicitly pushed or pulled between repositories. Pushing and pulling bookmarks allow you to collaborate with others on a branch without creating a named branch.</p>
<dt><code>Branch</code></p>
<dd> (Noun) A child changeset that has been created from a parent that is not a head. These are known as topological branches, see &#8216;Branch, topological&#8217;. If a topological branch is named, it becomes a named branch. If a topological branch is not named, it becomes an anonymous branch. See &#8216;Branch, anonymous&#8217; and &#8216;Branch, named&#8217;. </p>
<p> Branches may be created when changes are pulled from or pushed to a remote repository, since new heads may be created by these operations. Note that the term branch can also be used informally to describe a development process in which certain development is done independently of other development. This is sometimes done explicitly with a named branch, but it can also be done locally, using bookmarks or clones and anonymous branches. </p>
<p> Example: &quot;The experimental branch&quot;. </p>
<p> (Verb) The action of creating a child changeset which results in its parent having more than one child. </p>
<p> Example: &quot;I&#8217;m going to branch at X&quot;.</p>
<dt><code>Branch, anonymous</code></p>
<dd> Every time a new child changeset is created from a parent that is not a head and the name of the branch is not changed, a new anonymous branch is created.</p>
<dt><code>Branch, closed</code></p>
<dd> A named branch whose branch heads have all been closed.</p>
<dt><code>Branch, default</code></p>
<dd> The branch assigned to a changeset when no name has previously been assigned.</p>
<dt><code>Branch head</code></p>
<dd> See &#8216;Head, branch&#8217;.</p>
<dt><code>Branch, inactive</code></p>
<dd> If a named branch has no topological heads, it is considered to be inactive. As an example, a feature branch becomes inactive when it is merged into the default branch. The <code>hg branches</code>: command shows inactive branches by default, though they can be hidden with <code>hg branches &#8211;active</code>:. </p>
<p> NOTE: this concept is deprecated because it is too implicit. Branches should now be explicitly closed using <code>hg commit &#8211;close-branch</code>: when they are no longer needed.</p>
<dt><code>Branch, named</code></p>
<dd> A collection of changesets which have the same branch name. By default, children of a changeset in a named branch belong to the same named branch. A child can be explicitly assigned to a different branch. See <code>hg help branch</code>:, <code>hg help branches</code>: and <code>hg commit &#8211;close-branch</code>: for more information on managing branches. </p>
<p> Named branches can be thought of as a kind of namespace, dividing the collection of changesets that comprise the repository into a collection of disjoint subsets. A named branch is not necessarily a topological branch. If a new named branch is created from the head of another named branch, or the default branch, but no further changesets are added to that previous branch, then that previous branch will be a branch in name only.</p>
<dt><code>Branch tip</code></p>
<dd> See &#8216;Tip, branch&#8217;.</p>
<dt><code>Branch, topological</code></p>
<dd> Every time a new child changeset is created from a parent that is not a head, a new topological branch is created. If a topological branch is named, it becomes a named branch. If a topological branch is not named, it becomes an anonymous branch of the current, possibly default, branch.</p>
<dt><code>Changelog</code></p>
<dd> A record of the changesets in the order in which they were added to the repository. This includes details such as changeset id, author, commit message, date, and list of changed files.</p>
<dt><code>Changeset</code></p>
<dd> A snapshot of the state of the repository used to record a change.</p>
<dt><code>Changeset, child</code></p>
<dd> The converse of parent changeset: if P is a parent of C, then C is a child of P. There is no limit to the number of children that a changeset may have.</p>
<dt><code>Changeset id</code></p>
<dd> A SHA-1 hash that uniquely identifies a changeset. It may be represented as either a &quot;long&quot; 40 hexadecimal digit string, or a &quot;short&quot; 12 hexadecimal digit string.</p>
<dt><code>Changeset, merge</code></p>
<dd> A changeset with two parents. This occurs when a merge is committed.</p>
<dt><code>Changeset, parent</code></p>
<dd> A revision upon which a child changeset is based. Specifically, a parent changeset of a changeset C is a changeset whose node immediately precedes C in the DAG. Changesets have at most two parents.</p>
<dt><code>Checkout</code></p>
<dd> (Noun) The working directory being updated to a specific revision. This use should probably be avoided where possible, as changeset is much more appropriate than checkout in this context. </p>
<p> Example: &quot;I&#8217;m using checkout X.&quot; </p>
<p> (Verb) Updating the working directory to a specific changeset. See <code>hg help update</code>:. </p>
<p> Example: &quot;I&#8217;m going to check out changeset X.&quot;</p>
<dt><code>Child changeset</code></p>
<dd> See &#8216;Changeset, child&#8217;.</p>
<dt><code>Close changeset</code></p>
<dd> See &#8216;Head, closed branch&#8217;</p>
<dt><code>Closed branch</code></p>
<dd> See &#8216;Branch, closed&#8217;.</p>
<dt><code>Clone</code></p>
<dd> (Noun) An entire or partial copy of a repository. The partial clone must be in the form of a revision and its ancestors. </p>
<p> Example: &quot;Is your clone up to date?&quot;. </p>
<p> (Verb) The process of creating a clone, using <code>hg clone</code>:. </p>
<p> Example: &quot;I&#8217;m going to clone the repository&quot;.</p>
<dt><code>Closed branch head</code></p>
<dd> See &#8216;Head, closed branch&#8217;.</p>
<dt><code>Commit</code></p>
<dd> (Noun) A synonym for changeset. </p>
<p> Example: &quot;Is the bug fixed in your recent commit?&quot; </p>
<p> (Verb) The act of recording changes to a repository. When files are committed in a working directory, Mercurial finds the differences between the committed files and their parent changeset, creating a new changeset in the repository. </p>
<p> Example: &quot;You should commit those changes now.&quot;</p>
<dt><code>Cset</code></p>
<dd> A common abbreviation of the term changeset.</p>
<dt><code>DAG</code></p>
<dd> The repository of changesets of a distributed version control system (DVCS) can be described as a directed acyclic graph (DAG), consisting of nodes and edges, where nodes correspond to changesets and edges imply a parent -&gt; child relation. This graph can be visualized by graphical tools such as <code>hg glog</code>: (graphlog). In Mercurial, the DAG is limited by the requirement for children to have at most two parents.</p>
<dt><code>Default branch</code></p>
<dd> See &#8216;Branch, default&#8217;.</p>
<dt><code>Descendant</code></p>
<dd> Any changeset that can be reached by a chain of child changesets from a given changeset. More precisely, the descendants of a changeset can be defined by two properties: the child of a changeset is a descendant, and the child of a descendant is a descendant. See also: &#8216;Ancestor&#8217;.</p>
<dt><code>Diff</code></p>
<dd> (Noun) The difference between the contents and attributes of files in two changesets or a changeset and the current working directory. The difference is usually represented in a standard form called a &quot;diff&quot; or &quot;patch&quot;. The &quot;git diff&quot; format is used when the changes include copies, renames, or changes to file attributes, none of which can be represented/handled by classic &quot;diff&quot; and &quot;patch&quot;. </p>
<p> Example: &quot;Did you see my correction in the diff?&quot; </p>
<p> (Verb) Diffing two changesets is the action of creating a diff or patch. </p>
<p> Example: &quot;If you diff with changeset X, you will see what I mean.&quot;</p>
<dt><code>Directory, working</code></p>
<dd> The working directory represents the state of the files tracked by Mercurial, that will be recorded in the next commit. The working directory initially corresponds to the snapshot at an existing changeset, known as the parent of the working directory. See &#8216;Parent, working directory&#8217;. The state may be modified by changes to the files introduced manually or by a merge. The repository metadata exists in the .hg directory inside the working directory.</p>
<dt><code>Draft</code></p>
<dd> Changesets in the draft phase have not been shared with publishing repositories and may thus be safely changed by history-modifying extensions. See <code>hg help phases</code>:.</p>
<dt><code>Graph</code></p>
<dd> See DAG and <code>hg help graphlog</code>:.</p>
<dt><code>Head</code></p>
<dd> The term &#8216;head&#8217; may be used to refer to both a branch head or a repository head, depending on the context. See &#8216;Head, branch&#8217; and &#8216;Head, repository&#8217; for specific definitions. </p>
<p> Heads are where development generally takes place and are the usual targets for update and merge operations.</p>
<dt><code>Head, branch</code></p>
<dd> A changeset with no descendants on the same named branch.</p>
<dt><code>Head, closed branch</code></p>
<dd> A changeset that marks a head as no longer interesting. The closed head is no longer listed by <code>hg heads</code>:. A branch is considered closed when all its heads are closed and consequently is not listed by <code>hg branches</code>:. </p>
<p> Closed heads can be re-opened by committing new changeset as the child of the changeset that marks a head as closed.</p>
<dt><code>Head, repository</code></p>
<dd> A topological head which has not been closed.</p>
<dt><code>Head, topological</code></p>
<dd> A changeset with no children in the repository.</p>
<dt><code>History, immutable</code></p>
<dd> Once committed, changesets cannot be altered. Extensions which appear to change history actually create new changesets that replace existing ones, and then destroy the old changesets. Doing so in public repositories can result in old changesets being reintroduced to the repository.</p>
<dt><code>History, rewriting</code></p>
<dd> The changesets in a repository are immutable. However, extensions to Mercurial can be used to alter the repository, usually in such a way as to preserve changeset contents.</p>
<dt><code>Immutable history</code></p>
<dd> See &#8216;History, immutable&#8217;.</p>
<dt><code>Merge changeset</code></p>
<dd> See &#8216;Changeset, merge&#8217;.</p>
<dt><code>Manifest</code></p>
<dd> Each changeset has a manifest, which is the list of files that are tracked by the changeset.</p>
<dt><code>Merge</code></p>
<dd> Used to bring together divergent branches of work. When you update to a changeset and then merge another changeset, you bring the history of the latter changeset into your working directory. Once conflicts are resolved (and marked), this merge may be committed as a merge changeset, bringing two branches together in the DAG.</p>
<dt><code>Named branch</code></p>
<dd> See &#8216;Branch, named&#8217;.</p>
<dt><code>Null changeset</code></p>
<dd> The empty changeset. It is the parent state of newly-initialized repositories and repositories with no checked out revision. It is thus the parent of root changesets and the effective ancestor when merging unrelated changesets. Can be specified by the alias &#8216;null&#8217; or by the changeset ID &#8216;000000000000&#8217;.</p>
<dt><code>Parent</code></p>
<dd> See &#8216;Changeset, parent&#8217;.</p>
<dt><code>Parent changeset</code></p>
<dd> See &#8216;Changeset, parent&#8217;.</p>
<dt><code>Parent, working directory</code></p>
<dd> The working directory parent reflects a virtual revision which is the child of the changeset (or two changesets with an uncommitted merge) shown by <code>hg parents</code>:. This is changed with <code>hg update</code>:. Other commands to see the working directory parent are <code>hg summary</code>: and <code>hg id</code>:. Can be specified by the alias &quot;.&quot;.</p>
<dt><code>Patch</code></p>
<dd> (Noun) The product of a diff operation. </p>
<p> Example: &quot;I&#8217;ve sent you my patch.&quot; </p>
<p> (Verb) The process of using a patch file to transform one changeset into another. </p>
<p> Example: &quot;You will need to patch that revision.&quot;</p>
<dt><code>Phase</code></p>
<dd> A per-changeset state tracking how the changeset has been or should be shared. See <code>hg help phases</code>:.</p>
<dt><code>Public</code></p>
<dd> Changesets in the public phase have been shared with publishing repositories and are therefore considered immutable. See <code>hg help phases</code>:.</p>
<dt><code>Pull</code></p>
<dd> An operation in which changesets in a remote repository which are not in the local repository are brought into the local repository. Note that this operation without special arguments only updates the repository, it does not update the files in the working directory. See <code>hg help pull</code>:.</p>
<dt><code>Push</code></p>
<dd> An operation in which changesets in a local repository which are not in a remote repository are sent to the remote repository. Note that this operation only adds changesets which have been committed locally to the remote repository. Uncommitted changes are not sent. See <code>hg help push</code>:.</p>
<dt><code>Repository</code></p>
<dd> The metadata describing all recorded states of a collection of files. Each recorded state is represented by a changeset. A repository is usually (but not always) found in the <code>.hg</code> subdirectory of a working directory. Any recorded state can be recreated by &quot;updating&quot; a working directory to a specific changeset.</p>
<dt><code>Repository head</code></p>
<dd> See &#8216;Head, repository&#8217;.</p>
<dt><code>Revision</code></p>
<dd> A state of the repository at some point in time. Earlier revisions can be updated to by using <code>hg update</code>:. See also &#8216;Revision number&#8217;; See also &#8216;Changeset&#8217;.</p>
<dt><code>Revision number</code></p>
<dd> This integer uniquely identifies a changeset in a specific repository. It represents the order in which changesets were added to a repository, starting with revision number 0. Note that the revision number may be different in each clone of a repository. To identify changesets uniquely between different clones, see &#8216;Changeset id&#8217;.</p>
<dt><code>Revlog</code></p>
<dd> History storage mechanism used by Mercurial. It is a form of delta encoding, with occasional full revision of data followed by delta of each successive revision. It includes data and an index pointing to the data.</p>
<dt><code>Rewriting history</code></p>
<dd> See &#8216;History, rewriting&#8217;.</p>
<dt><code>Root</code></p>
<dd> A changeset that has only the null changeset as its parent. Most repositories have only a single root changeset.</p>
<dt><code>Secret</code></p>
<dd> Changesets in the secret phase may not be shared via push, pull, or clone. See <code>hg help phases</code>:.</p>
<dt><code>Tag</code></p>
<dd> An alternative name given to a changeset. Tags can be used in all places where Mercurial expects a changeset ID, e.g., with <code>hg update</code>:. The creation of a tag is stored in the history and will thus automatically be shared with other using push and pull.</p>
<dt><code>Tip</code></p>
<dd> The changeset with the highest revision number. It is the changeset most recently added in a repository.</p>
<dt><code>Tip, branch</code></p>
<dd> The head of a given branch with the highest revision number. When a branch name is used as a revision identifier, it refers to the branch tip. See also &#8216;Branch, head&#8217;. Note that because revision numbers may be different in different repository clones, the branch tip may be different in different cloned repositories.</p>
<dt><code>Update</code></p>
<dd> (Noun) Another synonym of changeset. </p>
<p> Example: &quot;I&#8217;ve pushed an update&quot;. </p>
<p> (Verb) This term is usually used to describe updating the state of the working directory to that of a specific changeset. See <code>hg help update</code>:. </p>
<p> Example: &quot;You should update&quot;.</p>
<dt><code>Working directory</code></p>
<dd> See &#8216;Directory, working&#8217;.</p>
<dt><code>Working directory parent</code></p>
<dd> See &#8216;Parent, working directory&#8217;.</dl>
<h2>SYNTAX FOR MERCURIAL IGNORE FILES</h2>
<h3>Synopsis</h3>
<p> The Mercurial system uses a file called <code>.hgignore</code> in the root directory of a repository to control its behavior when it searches for files that it is not currently tracking.</p>
<h3>Description</h3>
<p> The working directory of a Mercurial repository will often contain files that should not be tracked by Mercurial. These include backup files created by editors and build products created by compilers. These files can be ignored by listing them in a <code>.hgignore</code> file in the root of the working directory. The <code>.hgignore</code> file must be created manually. It is typically put under version control, so that the settings will propagate to other repositories with push and pull. </p>
<p> An untracked file is ignored if its path relative to the repository root directory, or any prefix path of that path, is matched against any pattern in <code>.hgignore</code>. </p>
<p> For example, say we have an untracked file, <code>file.c</code>, at <code>a/b/file.c</code> inside our repository. Mercurial will ignore <code>file.c</code> if any pattern in <code>.hgignore</code> matches <code>a/b/file.c</code>, <code>a/b</code> or <code>a</code>. </p>
<p> In addition, a Mercurial configuration file can reference a set of per-user or global ignore files. See the <code>ignore</code> configuration key on the <code>[ui]</code> section of <code>hg help config</code>: for details of how to configure these files. </p>
<p> To control Mercurial&#8217;s handling of files that it manages, many commands support the <code>-I</code> and <code>-X</code> options; see <code>hg help &lt;command&gt;</code>: and <code>hg help patterns</code>: for details. </p>
<p> Files that are already tracked are not affected by .hgignore, even if they appear in .hgignore. An untracked file X can be explicitly added with <code>hg add X</code>:, even if X would be excluded by a pattern in .hgignore.</p>
<h3>Syntax</h3>
<p> An ignore file is a plain text file consisting of a list of patterns, with one pattern per line. Empty lines are skipped. The <code>#</code> character is treated as a comment character, and the <code>\</code> character is treated as an escape character. </p>
<p> Mercurial supports several pattern syntaxes. The default syntax used is Python/Perl-style regular expressions. </p>
<p> To change the syntax used, use a line of the following form: </p>
<pre>
syntax: NAME
</pre>
<p> where <code>NAME</code> is one of the following:</p>
<dl>
<dt><code>regexp</code></p>
<dd>
<p> Regular expression, Python/Perl syntax.</p>
<dt><code>glob</code></p>
<dd>
<p> Shell-style glob. </p>
<p> The chosen syntax stays in effect when parsing all patterns that follow, until another syntax is selected. </p>
<p> Neither glob nor regexp patterns are rooted. A glob-syntax pattern of the form <code>*.c</code> will match a file ending in <code>.c</code> in any directory, and a regexp pattern of the form <code>\.c$</code> will do the same. To root a regexp pattern, start it with <code>^</code>.</p>
<dt>Note</p>
<dd> Patterns specified in other than <code>.hgignore</code> are always rooted. Please see <code>hg help patterns</code>: for details.</dl>
<h3>Example</h3>
<p> Here is an example ignore file. </p>
<pre>
# use glob syntax.
syntax: glob
*.elc
*.pyc
*~
# switch to regexp syntax.
syntax: regexp
^\.pc/
</pre>
<h2>CONFIGURING HGWEB</h2>
<p> Mercurial&#8217;s internal web server, hgweb, can serve either a single repository, or a tree of repositories. In the second case, repository paths and global options can be defined using a dedicated configuration file common to <code>hg serve</code>:, <code>hgweb.wsgi</code>, <code>hgweb.cgi</code> and <code>hgweb.fcgi</code>. </p>
<p> This file uses the same syntax as other Mercurial configuration files but recognizes only the following sections:</p>
<dl>
<dt>&bull;</p>
<dd> web</p>
<dt>&bull;</p>
<dd> paths</p>
<dt>&bull;</p>
<dd> collections </p>
<p> The <code>web</code> options are thoroughly described in <code>hg help config</code>:. </p>
<p> The <code>paths</code> section maps URL paths to paths of repositories in the filesystem. hgweb will not expose the filesystem directly &#8211; only Mercurial repositories can be published and only according to the configuration. </p>
<p> The left hand side is the path in the URL. Note that hgweb reserves subpaths like <code>rev</code> or <code>file</code>, try using different names for nested repositories to avoid confusing effects. </p>
<p> The right hand side is the path in the filesystem. If the specified path ends with <code>*</code> or <code>**</code> the filesystem will be searched recursively for repositories below that point. With <code>*</code> it will not recurse into the repositories it finds (except for <code>.hg/patches</code>). With <code>**</code> it will also search inside repository working directories and possibly find subrepositories. </p>
<p> In this example: </p>
<pre>
[paths]
/projects/a = /srv/tmprepos/a
/projects/b = c:/repos/b
/ = /srv/repos/*
/user/bob = /home/bob/repos/**
</pre>
<dt>&bull;</p>
<dd> The first two entries make two repositories in different directories appear under the same directory in the web interface</p>
<dt>&bull;</p>
<dd> The third entry will publish every Mercurial repository found in <code>/srv/repos/</code>, for instance the repository <code>/srv/repos/quux/</code> will appear as <code><a rel="nofollow" href="http://server/quux/">http://server/quux/</a></code></p>
<dt>&bull;</p>
<dd> The fourth entry will publish both <code><a rel="nofollow" href="http://server/user/bob/quux/">http://server/user/bob/quux/</a></code> and <code><a rel="nofollow" href="http://server/user/bob/quux/testsubrepo/">http://server/user/bob/quux/testsubrepo/</a></code> </p>
<p> The <code>collections</code> section is deprecated and has been superseded by <code>paths</code>.</dl>
<h2>MERGE TOOLS</h2>
<p> To merge files Mercurial uses merge tools. </p>
<p> A merge tool combines two different versions of a file into a merged file. Merge tools are given the two files and the greatest common ancestor of the two file versions, so they can determine the changes made on both branches. </p>
<p> Merge tools are used both for <code>hg resolve</code>:, <code>hg merge</code>:, <code>hg update</code>:, <code>hg backout</code>: and in several extensions. </p>
<p> Usually, the merge tool tries to automatically reconcile the files by combining all non-overlapping changes that occurred separately in the two different evolutions of the same initial base file. Furthermore, some interactive merge programs make it easier to manually resolve conflicting merges, either in a graphical way, or by inserting some conflict markers. Mercurial does not include any interactive merge programs but relies on external tools for that.</p>
<h3>Available merge tools</h3>
<p> External merge tools and their properties are configured in the merge-tools configuration section &#8211; see <a href="/docs/linux/man/5-hgrc/">hgrc</a>(5) &#8211; but they can often just be named by their executable. </p>
<p> A merge tool is generally usable if its executable can be found on the system and if it can handle the merge. The executable is found if it is an absolute or relative executable path or the name of an application in the executable search path. The tool is assumed to be able to handle the merge if it can handle symlinks if the file is a symlink, if it can handle binary files if the file is binary, and if a GUI is available if the tool requires a GUI. </p>
<p> There are some internal merge tools which can be used. The internal merge tools are:</p>
<dl>
<dt><code>internal:dump</code></p>
<dd>
<p> Creates three versions of the files to merge, containing the contents of local, other and base. These files can then be used to perform a merge manually. If the file to be merged is named <code>a.txt</code>, these files will accordingly be named <code>a.txt.local</code>, <code>a.txt.other</code> and <code>a.txt.base</code> and they will be placed in the same directory as <code>a.txt</code>.</p>
<dt><code>internal:fail</code></p>
<dd>
<p> Rather than attempting to merge files that were modified on both branches, it marks them as unresolved. The resolve command must be used to resolve these conflicts.</p>
<dt><code>internal:local</code></p>
<dd>
<p> Uses the local version of files as the merged version.</p>
<dt><code>internal:merge</code></p>
<dd>
<p> Uses the internal non-interactive simple merge algorithm for merging files. It will fail if there are any conflicts and leave markers in the partially merged file.</p>
<dt><code>internal:other</code></p>
<dd>
<p> Uses the other version of files as the merged version.</p>
<dt><code>internal:prompt</code></p>
<dd>
<p> Asks the user which of the local or the other version to keep as the merged version. </p>
<p> Internal tools are always available and do not require a GUI but will by default not handle symlinks or binary files.</dl>
<h3>Choosing a merge tool</h3>
<p> Mercurial uses these rules when deciding which merge tool to use:</p>
<dl>
<dt>1.</p>
<dd> If a tool has been specified with the &#8211;tool option to merge or resolve, it is used. If it is the name of a tool in the merge-tools configuration, its configuration is used. Otherwise the specified tool must be executable by the shell.</p>
<dt>2.</p>
<dd> If the <code>HGMERGE</code> environment variable is present, its value is used and must be executable by the shell.</p>
<dt>3.</p>
<dd> If the filename of the file to be merged matches any of the patterns in the merge-patterns configuration section, the first usable merge tool corresponding to a matching pattern is used. Here, binary capabilities of the merge tool are not considered.</p>
<dt>4.</p>
<dd> If ui.merge is set it will be considered next. If the value is not the name of a configured tool, the specified value is used and must be executable by the shell. Otherwise the named tool is used if it is usable.</p>
<dt>5.</p>
<dd> If any usable merge tools are present in the merge-tools configuration section, the one with the highest priority is used.</p>
<dt>6.</p>
<dd> If a program named <code>hgmerge</code> can be found on the system, it is used &#8211; but it will by default not be used for symlinks and binary files.</p>
<dt>7.</p>
<dd> If the file to be merged is not binary and is not a symlink, then <code>internal:merge</code> is used.</p>
<dt>8.</p>
<dd> The merge of the file fails and must be resolved before commit.</p>
<dt>Note</p>
<dd> After selecting a merge program, Mercurial will by default attempt to merge the files using a simple merge algorithm first. Only if it doesn&#8217;t succeed because of conflicting changes Mercurial will actually execute the merge program. Whether to use the simple merge algorithm first can be controlled by the premerge setting of the merge tool. Premerge is enabled by default unless the file is binary or a symlink. </p>
<p> See the merge-tools and ui sections of <a href="/docs/linux/man/5-hgrc/">hgrc</a>(5) for details on the configuration of merge tools.</dl>
<h2>SPECIFYING MULTIPLE REVISIONS</h2>
<p> When Mercurial accepts more than one revision, they may be specified individually, or provided as a topologically continuous range, separated by the &quot;:&quot; character. </p>
<p> The syntax of range notation is [BEGIN]:[END], where BEGIN and END are revision identifiers. Both BEGIN and END are optional. If BEGIN is not specified, it defaults to revision number 0. If END is not specified, it defaults to the tip. The range &quot;:&quot; thus means &quot;all revisions&quot;. </p>
<p> If BEGIN is greater than END, revisions are treated in reverse order. </p>
<p> A range acts as a closed interval. This means that a range of 3:5 gives 3, 4 and 5. Similarly, a range of 9:6 gives 9, 8, 7, and 6.</p>
<h2>FILE NAME PATTERNS</h2>
<p> Mercurial accepts several notations for identifying one or more files at a time. </p>
<p> By default, Mercurial treats filenames as shell-style extended glob patterns. </p>
<p> Alternate pattern notations must be specified explicitly.</p>
<dl>
<dt>Note</p>
<dd> Patterns specified in <code>.hgignore</code> are not rooted. Please see <code>hg help hgignore</code>: for details. </p>
<p> To use a plain path name without any pattern matching, start it with <code>path:</code>. These path names must completely match starting at the current repository root. </p>
<p> To use an extended glob, start a name with <code>glob:</code>. Globs are rooted at the current directory; a glob such as <code>*.c</code> will only match files in the current directory ending with <code>.c</code>. </p>
<p> The supported glob syntax extensions are <code>**</code> to match any string across path separators and <code>{a,b}</code> to mean &quot;a or b&quot;. </p>
<p> To use a Perl/Python regular expression, start a name with <code>re:</code>. Regexp pattern matching is anchored at the root of the repository. </p>
<p> To read name patterns from a file, use <code>listfile:</code> or <code>listfile0:</code>. The latter expects null delimited patterns while the former expects line feeds. Each string read from the file is itself treated as a file pattern. </p>
<p> Plain examples: </p>
<pre>
path:foo/bar   a name bar in a directory named foo in the root
               of the repository
path:path:name a file or directory named &quot;path:name&quot;
</pre>
<p> Glob examples: </p>
<pre>
glob:*.c       any name ending in &quot;.c&quot; in the current directory
*.c            any name ending in &quot;.c&quot; in the current directory
**.c           any name ending in &quot;.c&quot; in any subdirectory of the
               current directory including itself.
foo/*.c        any name ending in &quot;.c&quot; in the directory foo
foo/**.c       any name ending in &quot;.c&quot; in any subdirectory of foo
               including itself.
</pre>
<p> Regexp examples: </p>
<pre>
re:.*\.c$      any name ending in &quot;.c&quot;, anywhere in the repository
</pre>
<p> File examples: </p>
<pre>
listfile:list.txt  read list from list.txt with one file pattern per line
listfile0:list.txt read list from list.txt with null byte delimiters
</pre>
<p> See also <code>hg help filesets</code>:.</dl>
<h2>WORKING WITH PHASES</h2>
<h3>What are phases?</h3>
<p> Phases are a system for tracking which changesets have been or should be shared. This helps prevent common mistakes when modifying history (for instance, with the mq or rebase extensions). </p>
<p> Each changeset in a repository is in one of the following phases:</p>
<dl>
<dt>&bull;</p>
<dd> public : changeset is visible on a public server</p>
<dt>&bull;</p>
<dd> draft : changeset is not yet published</p>
<dt>&bull;</p>
<dd> secret : changeset should not be pushed, pulled, or cloned </p>
<p> These phases are ordered (public &lt; draft &lt; secret) and no changeset can be in a lower phase than its ancestors. For instance, if a changeset is public, all its ancestors are also public. Lastly, changeset phases should only be changed towards the public phase.</dl>
<h3>How are phases managed?</h3>
<p> For the most part, phases should work transparently. By default, a changeset is created in the draft phase and is moved into the public phase when it is pushed to another repository. </p>
<p> Once changesets become public, extensions like mq and rebase will refuse to operate on them to prevent creating duplicate changesets. Phases can also be manually manipulated with the <code>hg phase</code>: command if needed. See <code>hg help -v phase</code>: for examples.</p>
<h3>Phases and servers</h3>
<p> Normally, all servers are <code>publishing</code> by default. This means: </p>
<pre>
- all draft changesets that are pulled or cloned appear in phase
public on the client
- all draft changesets that are pushed appear as public on both
client and server
- secret changesets are neither pushed, pulled, or cloned
</pre>
<dl>
<dt>Note</p>
<dd> Pulling a draft changeset from a publishing server does not mark it as public on the server side due to the read-only nature of pull. </p>
<p> Sometimes it may be desirable to push and pull changesets in the draft phase to share unfinished work. This can be done by setting a repository to disable publishing in its configuration file: </p>
<pre>
[phases]
publish = False
</pre>
<p> See <code>hg help config</code>: for more information on config files.</p>
<dt>Note</p>
<dd> Servers running older versions of Mercurial are treated as publishing.</dl>
<h3>Examples</h3>
<dl>
<dt>&bull;</p>
<dd> list changesets in draft or secret phase: </p>
<pre>
hg log -r &quot;not public()&quot;
</pre>
<dt>&bull;</p>
<dd> change all secret changesets to draft: </p>
<pre>
hg phase --draft &quot;secret()&quot;
</pre>
<dt>&bull;</p>
<dd> forcibly move the current changeset and descendants from public to draft: </p>
<pre>
hg phase --force --draft .
</pre>
<dt>&bull;</p>
<dd> show a list of changeset revision and phase: </p>
<p>hg log&#8211; template &#8220;{rev} {phase}
&#8221;</p>
<dt>&bull;</p>
<dd> resynchronize draft changesets relative to a remote repository: </p>
<pre>
hg phase -fd 'outgoing(URL)'
</pre>
<p> See <code>hg help phase</code>: for more information on manually manipulating phases.</dl>
<h2>SPECIFYING SINGLE REVISIONS</h2>
<p> Mercurial supports several ways to specify individual revisions. </p>
<p> A plain integer is treated as a revision number. Negative integers are treated as sequential offsets from the tip, with -1 denoting the tip, -2 denoting the revision prior to the tip, and so forth. </p>
<p> A 40-digit hexadecimal string is treated as a unique revision identifier. </p>
<p> A hexadecimal string less than 40 characters long is treated as a unique revision identifier and is referred to as a short-form identifier. A short-form identifier is only valid if it is the prefix of exactly one full-length identifier. </p>
<p> Any other string is treated as a bookmark, tag, or branch name. A bookmark is a movable pointer to a revision. A tag is a permanent name associated with a revision. A branch name denotes the tipmost revision of that branch. Bookmark, tag, and branch names must not contain the &quot;:&quot; character. </p>
<p> The reserved name &quot;tip&quot; always identifies the most recent revision. </p>
<p> The reserved name &quot;null&quot; indicates the null revision. This is the revision of an empty repository, and the parent of revision 0. </p>
<p> The reserved name &quot;.&quot; indicates the working directory parent. If no working directory is checked out, it is equivalent to null. If an uncommitted merge is in progress, &quot;.&quot; is the revision of the first parent.</p>
<h2>SPECIFYING REVISION SETS</h2>
<p> Mercurial supports a functional language for selecting a set of revisions. </p>
<p> The language supports a number of predicates which are joined by infix operators. Parenthesis can be used for grouping. </p>
<p> Identifiers such as branch names may need quoting with single or double quotes if they contain characters like <code>&#8211;</code> or if they match one of the predefined predicates. </p>
<p> Special characters can be used in quoted identifiers by escaping them, e.g., <code>
</code> is interpreted as a newline. To prevent them from being interpreted, strings can be prefixed with <code>r</code>, e.g. <code>r&#8217;&#8230;&#8217;</code>. </p>
<p> There is a single prefix operator:</p>
<dl>
<dt><code>not x</code></p>
<dd>
<p> Changesets not in x. Short form is <code>! x</code>. </p>
<p> These are the supported infix operators:</p>
<dt><code>x::y</code></p>
<dd>
<p> A DAG range, meaning all changesets that are descendants of x and ancestors of y, including x and y themselves. If the first endpoint is left out, this is equivalent to <code>ancestors(y)</code>, if the second is left out it is equivalent to <code>descendants(x)</code>. </p>
<p> An alternative syntax is <code>x..y</code>.</p>
<dt><code>x:y</code></p>
<dd>
<p> All changesets with revision numbers between x and y, both inclusive. Either endpoint can be left out, they default to 0 and tip.</p>
<dt><code>x and y</code></p>
<dd>
<p> The intersection of changesets in x and y. Short form is <code>x &amp; y</code>.</p>
<dt><code>x or y</code></p>
<dd>
<p> The union of changesets in x and y. There are two alternative short forms: <code>x | y</code> and <code>x + y</code>.</p>
<dt><code>x &#8211; y</code></p>
<dd>
<p> Changesets in x but not in y.</p>
<dt><code>x^n</code></p>
<dd>
<p> The nth parent of x, n == 0, 1, or 2. For n == 0, x; for n == 1, the first parent of each changeset in x; for n == 2, the second parent of changeset in x.</p>
<dt><code>x~n</code></p>
<dd>
<p> The nth first ancestor of x; <code>x~0</code> is x; <code>x~3</code> is <code>x^^^</code>. </p>
<p> There is a single postfix operator:</p>
<dt><code>x^</code></p>
<dd>
<p> Equivalent to <code>x^1</code>, the first parent of each changeset in x. </p>
<p> The following predicates are supported:</p>
<dt><code>adds(pattern)</code></p>
<dd>
<p> Changesets that add a file matching pattern.</p>
<dt><code>all()</code></p>
<dd>
<p> All changesets, the same as <code>0:tip</code>.</p>
<dt><code>ancestor(*changeset)</code></p>
<dd>
<p> Greatest common ancestor of the changesets. </p>
<p> Accepts 0 or more changesets. Will return empty list when passed no args. Greatest common ancestor of a single changeset is that changeset.</p>
<dt><code>ancestors(set)</code></p>
<dd>
<p> Changesets that are ancestors of a changeset in set.</p>
<dt><code>author(string)</code></p>
<dd>
<p> Alias for <code>user(string)</code>.</p>
<dt><code>bisect(string)</code></p>
<dd>
<p> Changesets marked in the specified bisect status:</p>
<dt>&bull;</p>
<dd> <code>good</code>, <code>bad</code>, <code>skip</code>: csets explicitly marked as good/bad/skip</p>
<dt>&bull;</p>
<dd> <code>goods</code>, <code>bads</code> : csets topologically good/bad</p>
<dt>&bull;</p>
<dd> <code>range</code> : csets taking part in the bisection</p>
<dt>&bull;</p>
<dd> <code>pruned</code> : csets that are goods, bads or skipped</p>
<dt>&bull;</p>
<dd> <code>untested</code> : csets whose fate is yet unknown</p>
<dt>&bull;</p>
<dd> <code>ignored</code> : csets ignored due to DAG topology</p>
<dt>&bull;</p>
<dd> <code>current</code> : the cset currently being bisected</p>
<dt><code>bookmark([name])</code></p>
<dd>
<p> The named bookmark or all bookmarks. </p>
<p> If <i>name</i> starts with <i>re:</i>, the remainder of the name is treated as a regular expression. To match a bookmark that actually starts with <i>re:</i>, use the prefix <i>literal:</i>.</p>
<dt><code>branch(string or set)</code></p>
<dd>
<p> All changesets belonging to the given branch or the branches of the given changesets. </p>
<p> If <i>string</i> starts with <i>re:</i>, the remainder of the name is treated as a regular expression. To match a branch that actually starts with <i>re:</i>, use the prefix <i>literal:</i>.</p>
<dt><code>branchpoint()</code></p>
<dd>
<p> Changesets with more than one child.</p>
<dt><code>bumped()</code></p>
<dd>
<p> Mutable changesets marked as successors of public changesets. </p>
<p> Only non-public and non-obsolete changesets can be <i>bumped</i>.</p>
<dt><code>bundle()</code></p>
<dd>
<p> Changesets in the bundle. </p>
<p> Bundle must be specified by the -R option.</p>
<dt><code>children(set)</code></p>
<dd>
<p> Child changesets of changesets in set.</p>
<dt><code>closed()</code></p>
<dd>
<p> Changeset is closed.</p>
<dt><code>contains(pattern)</code></p>
<dd>
<p> Revision contains a file matching pattern. See <code>hg help patterns</code>: for information about file patterns.</p>
<dt><code>converted([id])</code></p>
<dd>
<p> Changesets converted from the given identifier in the old repository if present, or all converted changesets if no identifier is specified.</p>
<dt><code>date(interval)</code></p>
<dd>
<p> Changesets within the interval, see <code>hg help dates</code>:.</p>
<dt><code>desc(string)</code></p>
<dd>
<p> Search commit message for string. The match is case-insensitive.</p>
<dt><code>descendants(set)</code></p>
<dd>
<p> Changesets which are descendants of changesets in set.</p>
<dt><code>destination([set])</code></p>
<dd>
<p> Changesets that were created by a graft, transplant or rebase operation, with the given revisions specified as the source. Omitting the optional set is the same as passing all().</p>
<dt><code>divergent()</code></p>
<dd>
<p> Final successors of changesets with an alternative set of final successors.</p>
<dt><code>draft()</code></p>
<dd>
<p> Changeset in draft phase.</p>
<dt><code>extinct()</code></p>
<dd>
<p> Obsolete changesets with obsolete descendants only.</p>
<dt><code>extra(label, [value])</code></p>
<dd>
<p> Changesets with the given label in the extra metadata, with the given optional value. </p>
<p> If <i>value</i> starts with <i>re:</i>, the remainder of the value is treated as a regular expression. To match a value that actually starts with <i>re:</i>, use the prefix <i>literal:</i>.</p>
<dt><code>file(pattern)</code></p>
<dd>
<p> Changesets affecting files matched by pattern. </p>
<p> For a faster but less accurate result, consider using <code>filelog()</code> instead.</p>
<dt><code>filelog(pattern)</code></p>
<dd>
<p> Changesets connected to the specified filelog. </p>
<p> For performance reasons, <code>filelog()</code> does not show every changeset that affects the requested file(s). See <code>hg help log</code>: for details. For a slower, more accurate result, use <code>file()</code>.</p>
<dt><code>first(set, [n])</code></p>
<dd>
<p> An alias for limit().</p>
<dt><code>follow([file])</code></p>
<dd>
<p> An alias for <code>::.</code> (ancestors of the working copy&#8217;s first parent). If a filename is specified, the history of the given file is followed, including copies.</p>
<dt><code>grep(regex)</code></p>
<dd>
<p> Like <code>keyword(string)</code> but accepts a regex. Use <code>grep(r&#8217;&#8230;&#8217;)</code> to ensure special escape characters are handled correctly. Unlike <code>keyword(string)</code>, the match is case-sensitive.</p>
<dt><code>head()</code></p>
<dd>
<p> Changeset is a named branch head.</p>
<dt><code>heads(set)</code></p>
<dd>
<p> Members of set with no children in set.</p>
<dt><code>hidden()</code></p>
<dd>
<p> Hidden changesets.</p>
<dt><code>id(string)</code></p>
<dd>
<p> Revision non-ambiguously specified by the given hex string prefix.</p>
<dt><code>keyword(string)</code></p>
<dd>
<p> Search commit message, user name, and names of changed files for string. The match is case-insensitive.</p>
<dt><code>last(set, [n])</code></p>
<dd>
<p> Last n members of set, defaulting to 1.</p>
<dt><code>limit(set, [n])</code></p>
<dd>
<p> First n members of set, defaulting to 1.</p>
<dt><code>matching(revision [, field])</code></p>
<dd>
<p> Changesets in which a given set of fields match the set of fields in the selected revision or set. </p>
<p> To match more than one field pass the list of fields to match separated by spaces (e.g. <code>author description</code>). </p>
<p> Valid fields are most regular revision fields and some special fields. </p>
<p> Regular revision fields are <code>description</code>, <code>author</code>, <code>branch</code>, <code>date</code>, <code>files</code>, <code>phase</code>, <code>parents</code>, <code>substate</code>, <code>user</code> and <code>diff</code>. Note that <code>author</code> and <code>user</code> are synonyms. <code>diff</code> refers to the contents of the revision. Two revisions matching their <code>diff</code> will also match their <code>files</code>. </p>
<p> Special fields are <code>summary</code> and <code>metadata</code>: <code>summary</code> matches the first line of the description. <code>metadata</code> is equivalent to matching <code>description user date</code> (i.e. it matches the main metadata fields). </p>
<p> <code>metadata</code> is the default field which is used when no fields are specified. You can match more than one field at a time.</p>
<dt><code>max(set)</code></p>
<dd>
<p> Changeset with highest revision number in set.</p>
<dt><code>merge()</code></p>
<dd>
<p> Changeset is a merge changeset.</p>
<dt><code>min(set)</code></p>
<dd>
<p> Changeset with lowest revision number in set.</p>
<dt><code>modifies(pattern)</code></p>
<dd>
<p> Changesets modifying files matched by pattern.</p>
<dt><code>obsolete()</code></p>
<dd>
<p> Mutable changeset with a newer version.</p>
<dt><code>origin([set])</code></p>
<dd>
<p> Changesets that were specified as a source for the grafts, transplants or rebases that created the given revisions. Omitting the optional set is the same as passing all(). If a changeset created by these operations is itself specified as a source for one of these operations, only the source changeset for the first operation is selected.</p>
<dt><code>outgoing([path])</code></p>
<dd>
<p> Changesets not found in the specified destination repository, or the default push location.</p>
<dt><code>p1([set])</code></p>
<dd>
<p> First parent of changesets in set, or the working directory.</p>
<dt><code>p2([set])</code></p>
<dd>
<p> Second parent of changesets in set, or the working directory.</p>
<dt><code>parents([set])</code></p>
<dd>
<p> The set of all parents for all changesets in set, or the working directory.</p>
<dt><code>present(set)</code></p>
<dd>
<p> An empty set, if any revision in set isn&#8217;t found; otherwise, all revisions in set. </p>
<p> If any of specified revisions is not present in the local repository, the query is normally aborted. But this predicate allows the query to continue even in such cases.</p>
<dt><code>public()</code></p>
<dd>
<p> Changeset in public phase.</p>
<dt><code>remote([id [,path]])</code></p>
<dd>
<p> Local revision that corresponds to the given identifier in a remote repository, if present. Here, the &#8216;.&#8217; identifier is a synonym for the current local branch.</p>
<dt><code>removes(pattern)</code></p>
<dd>
<p> Changesets which remove files matching pattern.</p>
<dt><code>rev(number)</code></p>
<dd>
<p> Revision with the given numeric identifier.</p>
<dt><code>reverse(set)</code></p>
<dd>
<p> Reverse order of set.</p>
<dt><code>roots(set)</code></p>
<dd>
<p> Changesets in set with no parent changeset in set.</p>
<dt><code>secret()</code></p>
<dd>
<p> Changeset in secret phase.</p>
<dt><code>sort(set[, [-]key&#8230;])</code></p>
<dd>
<p> Sort set by keys. The default sort order is ascending, specify a key as <code>-key</code> to sort in descending order. </p>
<p> The keys can be:</p>
<dt>&bull;</p>
<dd> <code>rev</code> for the revision number,</p>
<dt>&bull;</p>
<dd> <code>branch</code> for the branch name,</p>
<dt>&bull;</p>
<dd> <code>desc</code> for the commit message (description),</p>
<dt>&bull;</p>
<dd> <code>user</code> for user name (<code>author</code> can be used as an alias),</p>
<dt>&bull;</p>
<dd> <code>date</code> for the commit date</p>
<dt><code>tag([name])</code></p>
<dd>
<p> The specified tag by name, or all tagged revisions if no name is given.</p>
<dt><code>unstable()</code></p>
<dd>
<p> Non-obsolete changesets with obsolete ancestors.</p>
<dt><code>user(string)</code></p>
<dd>
<p> User name contains string. The match is case-insensitive. </p>
<p> If <i>string</i> starts with <i>re:</i>, the remainder of the string is treated as a regular expression. To match a user that actually contains <i>re:</i>, use the prefix <i>literal:</i>. </p>
<p> New predicates (known as &quot;aliases&quot;) can be defined, using any combination of existing predicates or other aliases. An alias definition looks like: </p>
<pre>
&lt;alias&gt; = &lt;definition&gt;
</pre>
<p> in the <code>revsetalias</code> section of a Mercurial configuration file. Arguments of the form <i>$1</i>, <i>$2</i>, etc. are substituted from the alias into the definition. </p>
<p> For example, </p>
<pre>
[revsetalias]
h = heads()
d($1) = sort($1, date)
rs($1, $2) = reverse(sort($1, $2))
</pre>
<p> defines three aliases, <code>h</code>, <code>d</code>, and <code>rs</code>. <code>rs(0:tip, author)</code> is exactly equivalent to <code>reverse(sort(0:tip, author))</code>. </p>
<p> Command line equivalents for <code>hg log</code>:: </p>
<p>&#8211; f-&gt;::.- d x-&gt;date(x) &#8211; k x-&gt;keyword(x) &#8211; m-&gt;merge() &#8211; u x-&gt;user(x) &#8211; b x-&gt;branch(x) &#8211; P x-&gt;!::x<br />
    &#8211; l x-&gt;limit(expr, x)</p>
<p> Some sample queries:</p>
<dt>&bull;</p>
<dd> Changesets on the default branch: </p>
<pre>
hg log -r &quot;branch(default)&quot;
</pre>
<dt>&bull;</p>
<dd> Changesets on the default branch since tag 1.5 (excluding merges): </p>
<pre>
hg log -r &quot;branch(default) and 1.5:: and not merge()&quot;
</pre>
<dt>&bull;</p>
<dd> Open branch heads: </p>
<pre>
hg log -r &quot;head() and not closed()&quot;
</pre>
<dt>&bull;</p>
<dd> Changesets between tags 1.3 and 1.5 mentioning &quot;bug&quot; that affect <code>hgext/*</code>: </p>
<pre>
hg log -r &quot;1.3::1.5 and keyword(bug) and file('hgext/*')&quot;
</pre>
<dt>&bull;</p>
<dd> Changesets committed in May 2008, sorted by user: </p>
<pre>
hg log -r &quot;sort(date('May 2008'), user)&quot;
</pre>
<dt>&bull;</p>
<dd> Changesets mentioning &quot;bug&quot; or &quot;issue&quot; that are not in a tagged release: </p>
<pre>
hg log -r &quot;(keyword(bug) or keyword(issue)) and not ancestors(tag())&quot;
</pre>
</dl>
<h2>SUBREPOSITORIES</h2>
<p> Subrepositories let you nest external repositories or projects into a parent Mercurial repository, and make commands operate on them as a group. </p>
<p> Mercurial currently supports Mercurial, Git, and Subversion subrepositories. </p>
<p> Subrepositories are made of three components:</p>
<dl>
<dt>1.</p>
<dd> Nested repository checkouts. They can appear anywhere in the parent working directory.</p>
<dt>2.</p>
<dd> Nested repository references. They are defined in <code>.hgsub</code>, which should be placed in the root of working directory, and tell where the subrepository checkouts come from. Mercurial subrepositories are referenced like: </p>
<pre>
path/to/nested = <a rel="nofollow" href="https://example.com/nested/repo/path">https://example.com/nested/repo/path</a>
</pre>
<p> Git and Subversion subrepos are also supported: </p>
<p>path / to / nested = [git] git : // example.com/nested/repo/path<br />
                                 path /<br />
                                 to / nested = [svn] https: // example.com/nested/trunk/path</p>
<p> where <code>path/to/nested</code> is the checkout location relatively to the parent Mercurial root, and <code><a rel="nofollow" href="https://example.com/nested/repo/path">https://example.com/nested/repo/path</a></code> is the source repository path. The source can also reference a filesystem path. </p>
<p> Note that <code>.hgsub</code> does not exist by default in Mercurial repositories, you have to create and add it to the parent repository before using subrepositories.</p>
<dt>3.</p>
<dd> Nested repository states. They are defined in <code>.hgsubstate</code>, which is placed in the root of working directory, and capture whatever information is required to restore the subrepositories to the state they were committed in a parent repository changeset. Mercurial automatically record the nested repositories states when committing in the parent repository.</p>
<dt>Note</p>
<dd> The <code>.hgsubstate</code> file should not be edited manually.</dl>
<h3>Adding a Subrepository</h3>
<p> If <code>.hgsub</code> does not exist, create it and add it to the parent repository. Clone or checkout the external projects where you want it to live in the parent repository. Edit <code>.hgsub</code> and add the subrepository entry as described above. At this point, the subrepository is tracked and the next commit will record its state in <code>.hgsubstate</code> and bind it to the committed changeset.</p>
<h3>Synchronizing a Subrepository</h3>
<p> Subrepos do not automatically track the latest changeset of their sources. Instead, they are updated to the changeset that corresponds with the changeset checked out in the top-level changeset. This is so developers always get a consistent set of compatible code and libraries when they update. </p>
<p> Thus, updating subrepos is a manual process. Simply check out target subrepo at the desired revision, test in the top-level repo, then commit in the parent repository to record the new combination.</p>
<h3>Deleting a Subrepository</h3>
<p> To remove a subrepository from the parent repository, delete its reference from <code>.hgsub</code>, then remove its files.</p>
<h3>Interaction with Mercurial Commands</h3>
<dl>
<dt><code>add</code></p>
<dd> add does not recurse in subrepos unless -S/&#8211;subrepos is specified. However, if you specify the full path of a file in a subrepo, it will be added even without -S/&#8211;subrepos specified. Git and Subversion subrepositories are currently silently ignored.</p>
<dt><code>archive</code></p>
<dd> archive does not recurse in subrepositories unless -S/&#8211;subrepos is specified.</p>
<dt><code>commit</code></p>
<dd> commit creates a consistent snapshot of the state of the entire project and its subrepositories. If any subrepositories have been modified, Mercurial will abort. Mercurial can be made to instead commit all modified subrepositories by specifying -S/&#8211;subrepos, or setting &quot;ui.commitsubrepos=True&quot; in a configuration file (see <code>hg help config</code>:). After there are no longer any modified subrepositories, it records their state and finally commits it in the parent repository.</p>
<dt><code>diff</code></p>
<dd> diff does not recurse in subrepos unless -S/&#8211;subrepos is specified. Changes are displayed as usual, on the subrepositories elements. Git and Subversion subrepositories are currently silently ignored.</p>
<dt><code>forget</code></p>
<dd> forget currently only handles exact file matches in subrepos. Git and Subversion subrepositories are currently silently ignored.</p>
<dt><code>incoming</code></p>
<dd> incoming does not recurse in subrepos unless -S/&#8211;subrepos is specified. Git and Subversion subrepositories are currently silently ignored.</p>
<dt><code>outgoing</code></p>
<dd> outgoing does not recurse in subrepos unless -S/&#8211;subrepos is specified. Git and Subversion subrepositories are currently silently ignored.</p>
<dt><code>pull</code></p>
<dd> pull is not recursive since it is not clear what to pull prior to running <code>hg update</code>:. Listing and retrieving all subrepositories changes referenced by the parent repository pulled changesets is expensive at best, impossible in the Subversion case.</p>
<dt><code>push</code></p>
<dd> Mercurial will automatically push all subrepositories first when the parent repository is being pushed. This ensures new subrepository changes are available when referenced by top-level repositories. Push is a no-op for Subversion subrepositories.</p>
<dt><code>status</code></p>
<dd> status does not recurse into subrepositories unless -S/&#8211;subrepos is specified. Subrepository changes are displayed as regular Mercurial changes on the subrepository elements. Subversion subrepositories are currently silently ignored.</p>
<dt><code>update</code></p>
<dd> update restores the subrepos in the state they were originally committed in target changeset. If the recorded changeset is not available in the current subrepository, Mercurial will pull it in first before updating. This means that updating can require network access when using subrepositories.</dl>
<h3>Remapping Subrepositories Sources</h3>
<p> A subrepository source location may change during a project life, invalidating references stored in the parent repository history. To fix this, rewriting rules can be defined in parent repository <code>hgrc</code> file or in Mercurial configuration. See the <code>[subpaths]</code> section in <a href="/docs/linux/man/5-hgrc/">hgrc</a>(5) for more details.</p>
<h2>TEMPLATE USAGE</h2>
<p> Mercurial allows you to customize output of commands through templates. You can either pass in a template from the command line, via the &#8211;template option, or select an existing template-style (&#8211;style). </p>
<p> You can customize output for any &quot;log-like&quot; command: log, outgoing, incoming, tip, parents, heads and glog. </p>
<p> Four styles are packaged with Mercurial: default (the style used when no explicit preference is passed), compact, changelog, and xml. Usage: </p>
<pre>
$ hg log -r1 --style changelog
</pre>
<p> A template is a piece of text, with markup to invoke variable expansion: </p>
<pre>
$ hg log -r1 --template &quot;{node}
&quot;
b56ce7b07c52de7d5fd79fb89701ea538af65746
</pre>
<p> Strings in curly braces are called keywords. The availability of keywords depends on the exact context of the templater. These keywords are usually available for templating a log-like command:</p>
<dl>
<dt><code>author</code></p>
<dd> String. The unmodified author of the changeset.</p>
<dt><code>bisect</code></p>
<dd> String. The changeset bisection status.</p>
<dt><code>bookmarks</code></p>
<dd> List of strings. Any bookmarks associated with the changeset.</p>
<dt><code>branch</code></p>
<dd> String. The name of the branch on which the changeset was committed.</p>
<dt><code>branches</code></p>
<dd> List of strings. The name of the branch on which the changeset was committed. Will be empty if the branch name was default.</p>
<dt><code>children</code></p>
<dd> List of strings. The children of the changeset.</p>
<dt><code>date</code></p>
<dd> Date information. The date when the changeset was committed.</p>
<dt><code>desc</code></p>
<dd> String. The text of the changeset description.</p>
<dt><code>diffstat</code></p>
<dd> String. Statistics of changes with the following format: &quot;modified files: +added/-removed lines&quot;</p>
<dt><code>file_adds</code></p>
<dd> List of strings. Files added by this changeset.</p>
<dt><code>file_copies</code></p>
<dd> List of strings. Files copied in this changeset with their sources.</p>
<dt><code>file_copies_switch</code></p>
<dd> List of strings. Like &quot;file_copies&quot; but displayed only if the &#8211;copied switch is set.</p>
<dt><code>file_dels</code></p>
<dd> List of strings. Files removed by this changeset.</p>
<dt><code>file_mods</code></p>
<dd> List of strings. Files modified by this changeset.</p>
<dt><code>files</code></p>
<dd> List of strings. All files modified, added, or removed by this changeset.</p>
<dt><code>latesttag</code></p>
<dd> String. Most recent global tag in the ancestors of this changeset.</p>
<dt><code>latesttagdistance</code></p>
<dd> Integer. Longest path to the latest tag.</p>
<dt><code>node</code></p>
<dd> String. The changeset identification hash, as a 40 hexadecimal digit string.</p>
<dt><code>p1node</code></p>
<dd> String. The identification hash of the changeset&#8217;s first parent, as a 40 digit hexadecimal string. If the changeset has no parents, all digits are 0.</p>
<dt><code>p1rev</code></p>
<dd> Integer. The repository-local revision number of the changeset&#8217;s first parent, or -1 if the changeset has no parents.</p>
<dt><code>p2node</code></p>
<dd> String. The identification hash of the changeset&#8217;s second parent, as a 40 digit hexadecimal string. If the changeset has no second parent, all digits are 0.</p>
<dt><code>p2rev</code></p>
<dd> Integer. The repository-local revision number of the changeset&#8217;s second parent, or -1 if the changeset has no second parent.</p>
<dt><code>parents</code></p>
<dd> List of strings. The parents of the changeset in &quot;rev:node&quot; format. If the changeset has only one &quot;natural&quot; parent (the predecessor revision) nothing is shown.</p>
<dt><code>phase</code></p>
<dd> String. The changeset phase name.</p>
<dt><code>phaseidx</code></p>
<dd> Integer. The changeset phase index.</p>
<dt><code>rev</code></p>
<dd> Integer. The repository-local changeset revision number.</p>
<dt><code>tags</code></p>
<dd> List of strings. Any tags associated with the changeset. </p>
<p> The &quot;date&quot; keyword does not produce human-readable output. If you want to use a date in your output, you can use a filter to process it. Filters are functions which return a string based on the input variable. Be sure to use the stringify filter first when you&#8217;re applying a string-input filter to a list-like input variable. You can also use a chain of filters to get the desired output: </p>
<pre>
$ hg tip --template &quot;{date|isodate}
&quot;
2008-08-21 18:22 +0000
</pre>
<p> List of filters:</p>
<dt><code>addbreaks</code></p>
<dd> Any text. Add an XHTML &quot;&lt;br /&gt;&quot; tag before the end of every line except the last.</p>
<dt><code>age</code></p>
<dd> Date. Returns a human-readable date/time difference between the given date/time and the current date/time.</p>
<dt><code>basename</code></p>
<dd> Any text. Treats the text as a path, and returns the last component of the path after splitting by the path separator (ignoring trailing separators). For example, &quot;foo/bar/baz&quot; becomes &quot;baz&quot; and &quot;foo/bar//&quot; becomes &quot;bar&quot;.</p>
<dt><code>date</code></p>
<dd> Date. Returns a date in a Unix date format, including the timezone: &quot;Mon Sep 04 15:13:13 2006 0700&quot;.</p>
<dt><code>domain</code></p>
<dd> Any text. Finds the first string that looks like an email address, and extracts just the domain component. Example: <code>User &lt;user [at] example.com&gt;</code> becomes <code>example.com</code>.</p>
<dt><code>email</code></p>
<dd> Any text. Extracts the first string that looks like an email address. Example: <code>User &lt;user [at] example.com&gt;</code> becomes <code>user [at] example.com</code>.</p>
<dt><code>emailuser</code></p>
<dd> Any text. Returns the user portion of an email address.</p>
<dt><code>escape</code></p>
<dd> Any text. Replaces the special XML/XHTML characters &quot;&amp;&quot;, &quot;&lt;&quot; and &quot;&gt;&quot; with XML entities, and filters out NUL characters.</p>
<dt><code>fill68</code></p>
<dd> Any text. Wraps the text to fit in 68 columns.</p>
<dt><code>fill76</code></p>
<dd> Any text. Wraps the text to fit in 76 columns.</p>
<dt><code>firstline</code></p>
<dd> Any text. Returns the first line of text.</p>
<dt><code>hex</code></p>
<dd> Any text. Convert a binary Mercurial node identifier into its long hexadecimal representation.</p>
<dt><code>hgdate</code></p>
<dd> Date. Returns the date as a pair of numbers: &quot;1157407993 25200&quot; (Unix timestamp, timezone offset).</p>
<dt><code>isodate</code></p>
<dd> Date. Returns the date in ISO 8601 format: &quot;2009-08-18 13:00 +0200&quot;.</p>
<dt><code>isodatesec</code></p>
<dd> Date. Returns the date in ISO 8601 format, including seconds: &quot;2009-08-18 13:00:13 +0200&quot;. See also the rfc3339date filter.</p>
<dt><code>localdate</code></p>
<dd> Date. Converts a date to local date.</p>
<dt><code>nonempty</code></p>
<dd> Any text. Returns &#8216;(none)&#8217; if the string is empty.</p>
<dt><code>obfuscate</code></p>
<dd> Any text. Returns the input text rendered as a sequence of XML entities.</p>
<dt><code>person</code></p>
<dd> Any text. Returns the name before an email address, interpreting it as per RFC 5322.</p>
<dt><code>rfc3339date</code></p>
<dd> Date. Returns a date using the Internet date format specified in RFC 3339: &quot;2009-08-18T13:00:13+02:00&quot;.</p>
<dt><code>rfc822date</code></p>
<dd> Date. Returns a date using the same format used in email headers: &quot;Tue, 18 Aug 2009 13:00:13 +0200&quot;.</p>
<dt><code>short</code></p>
<dd> Changeset hash. Returns the short form of a changeset hash, i.e. a 12 hexadecimal digit string.</p>
<dt><code>shortbisect</code></p>
<dd> Any text. Treats <i>text</i> as a bisection status, and returns a single-character representing the status (G: good, B: bad, S: skipped, U: untested, I: ignored). Returns single space if <i>text</i> is not a valid bisection status.</p>
<dt><code>shortdate</code></p>
<dd> Date. Returns a date like &quot;2006-09-18&quot;.</p>
<dt><code>stringify</code></p>
<dd> Any type. Turns the value into text by converting values into text and concatenating them.</p>
<dt><code>strip</code></p>
<dd> Any text. Strips all leading and trailing whitespace.</p>
<dt><code>stripdir</code></p>
<dd> Treat the text as path and strip a directory level, if possible. For example, &quot;foo&quot; and &quot;foo/bar&quot; becomes &quot;foo&quot;.</p>
<dt><code>tabindent</code></p>
<dd> Any text. Returns the text, with every line except the first starting with a tab character.</p>
<dt><code>urlescape</code></p>
<dd> Any text. Escapes all &quot;special&quot; characters. For example, &quot;foo bar&quot; becomes &quot;foo%20bar&quot;.</p>
<dt><code>user</code></p>
<dd> Any text. Returns a short representation of a user name or email address. </p>
<p> Note that a filter is nothing more than a function call, i.e. <code>expr|filter</code> is equivalent to <code>filter(expr)</code>. </p>
<p> In addition to filters, there are some basic built-in functions:</p>
<dt>&bull;</p>
<dd> date(date[, fmt])</p>
<dt>&bull;</p>
<dd> fill(text[, width])</p>
<dt>&bull;</p>
<dd> get(dict, key)</p>
<dt>&bull;</p>
<dd> if(expr, then[, else])</p>
<dt>&bull;</p>
<dd> ifeq(expr, expr, then[, else])</p>
<dt>&bull;</p>
<dd> join(list, sep)</p>
<dt>&bull;</p>
<dd> label(label, expr)</p>
<dt>&bull;</p>
<dd> sub(pat, repl, expr)</p>
<dt>&bull;</p>
<dd> rstdoc(text, style) </p>
<p> Also, for any expression that returns a list, there is a list operator:</p>
<dt>&bull;</p>
<dd> expr % &quot;{template}&quot; </p>
<p> Some sample command line templates:</p>
<dt>&bull;</p>
<dd> Format lists, e.g. files: </p>
<p>$ hg log &#8211; r 0 &#8211;template &#8220;files:
{files % &#8216;  {file}
&#8217;}&#8221;</p>
<dt>&bull;</p>
<dd> Join the list of files with a &quot;, &quot;: </p>
<pre>
$ hg log -r 0 --template &quot;files: {join(files, ', ')}
&quot;
</pre>
<dt>&bull;</p>
<dd> Format date: </p>
<pre>
$ hg log -r 0 --template &quot;{date(date, '%Y')}
&quot;
</pre>
<dt>&bull;</p>
<dd> Output the description set to a fill-width of 30: </p>
<pre>
$ hg log -r 0 --template &quot;{fill(desc, '30')}&quot;
</pre>
<dt>&bull;</p>
<dd> Use a conditional to test for the default branch: </p>
<p>$ hg log -r 0 &#8211;template &#8220;{ifeq(branch, &#8216;default&#8217;, &#8216;on the main branch&#8217;,<br />
&#8216;on branch {branch}&#8217;)<br />
}<br />

 &#8221;</p>
<dt>&bull;</p>
<dd> Append a newline if not empty: </p>
<p>$ hg tip&#8211; template &#8220;{if(author, &#8216;{author}
&#8217;)}&#8221;</p>
<dt>&bull;</p>
<dd> Label the output for use with the color extension: </p>
<p>$ hg log &#8211; r 0 &#8211;template &#8220;{label(&#8216;changeset.{phase}&#8217;, node|short)}
&#8221;</p>
<dt>&bull;</p>
<dd> Invert the firstline filter, i.e. everything but the first line: </p>
<pre>
$ hg log -r 0 --template &quot;{sub(r'^.*
?
?', '', desc)}
&quot;
</pre>
</dl>
<h2>URL PATHS</h2>
<p> Valid URLs are of the form: </p>
<p>local / filesystem / path[#revision] file :                     // local/filesystem/path[#revision]<br />
                                            http :              //[user[:pass]@]host[:port]/[path][#revision]<br />
                                                   https :      //[user[:pass]@]host[:port]/[path][#revision]<br />
                                                           ssh: //[user@]host[:port]/[path][#revision]</p>
<p> Paths in the local filesystem can either point to Mercurial repositories or to bundle files (as created by <code>hg bundle</code>: or <code>hg incoming &#8211;bundle</code>:). See also <code>hg help paths</code>:. </p>
<p> An optional identifier after # indicates a particular branch, tag, or changeset to use from the remote repository. See also <code>hg help revisions</code>:. </p>
<p> Some features, such as pushing to <a rel="nofollow" href="http://:">http://:</a> and <a href="https://:">https://:</a> URLs are only possible if the feature is explicitly enabled on the remote Mercurial server. </p>
<p> Note that the security of HTTPS URLs depends on proper configuration of web.cacerts. </p>
<p> Some notes about using SSH with Mercurial:</p>
<dl>
<dt>&bull;</p>
<dd> SSH requires an accessible shell account on the destination machine and a copy of hg in the remote path or specified with as remotecmd.</p>
<dt>&bull;</p>
<dd> path is relative to the remote user&#8217;s home directory by default. Use an extra slash at the start of a path to specify an absolute path: </p>
<pre>
<a href="ssh://example.com//tmp/repository">ssh://example.com//tmp/repository</a>
</pre>
<dt>&bull;</p>
<dd> Mercurial doesn&#8217;t use its own compression via SSH; the right thing to do is to configure it in your ~/.ssh/config, e.g.: </p>
<pre>
Host *.mylocalnetwork.example.com
  Compression no
Host *
  Compression yes
</pre>
<p> Alternatively specify &quot;ssh -C&quot; as your ssh command in your configuration file or with the &#8211;ssh command line option. </p>
<p> These URLs can all be stored in your configuration file with path aliases under the [paths] section like so: </p>
<pre>
[paths]
alias1 = URL1
alias2 = URL2
...
</pre>
<p> You can then use the alias for any command that uses a URL (for example <code>hg pull alias1</code>: will be treated as <code>hg pull URL1</code>:). </p>
<p> Two path aliases are special because they are used as defaults when you do not provide the URL to a command:</p>
<dt><code>default:</code></p>
<dd> When you create a repository with hg clone, the clone command saves the location of the source repository as the new repository&#8217;s &#8216;default&#8217; path. This is then used when you omit path from push- and pull-like commands (including incoming and outgoing).</p>
<dt><code>default-push:</code></p>
<dd> The push command will look for a path named &#8216;default-push&#8217;, and prefer it over &#8216;default&#8217; if both are defined.</dl>
<h2>EXTENSIONS</h2>
<p> This section contains help for extensions that are distributed together with Mercurial. Help for other extensions is available in the help system.</p>
<h3>acl</h3>
<p> hooks for controlling repository access </p>
<p> This hook makes it possible to allow or deny write access to given branches and paths of a repository when receiving incoming changesets via pretxnchangegroup and pretxncommit. </p>
<p> The authorization is matched based on the local user name on the system where the hook runs, and not the committer of the original changeset (since the latter is merely informative). </p>
<p> The acl hook is best used along with a restricted shell like hgsh, preventing authenticating users from doing anything other than pushing or pulling. The hook is not safe to use if users have interactive shell access, as they can then disable the hook. Nor is it safe if remote users share an account, because then there is no way to distinguish them. </p>
<p> The order in which access checks are performed is:</p>
<dl>
<dt>1.</p>
<dd> Deny list for branches (section <code>acl.deny.branches</code>)</p>
<dt>2.</p>
<dd> Allow list for branches (section <code>acl.allow.branches</code>)</p>
<dt>3.</p>
<dd> Deny list for paths (section <code>acl.deny</code>)</p>
<dt>4.</p>
<dd> Allow list for paths (section <code>acl.allow</code>) </p>
<p> The allow and deny sections take key-value pairs.</dl>
<h3>Branch-based Access Control</h3>
<p> Use the <code>acl.deny.branches</code> and <code>acl.allow.branches</code> sections to have branch-based access control. Keys in these sections can be either:</p>
<dl>
<dt>&bull;</p>
<dd> a branch name, or</p>
<dt>&bull;</p>
<dd> an asterisk, to match any branch; </p>
<p> The corresponding values can be either:</p>
<dt>&bull;</p>
<dd> a comma-separated list containing users and groups, or</p>
<dt>&bull;</p>
<dd> an asterisk, to match anyone; </p>
<p> You can add the &quot;!&quot; prefix to a user or group name to invert the sense of the match.</dl>
<h3>Path-based Access Control</h3>
<p> Use the <code>acl.deny</code> and <code>acl.allow</code> sections to have path-based access control. Keys in these sections accept a subtree pattern (with a glob syntax by default). The corresponding values follow the same syntax as the other sections above.</p>
<h3>Groups</h3>
<p> Group names must be prefixed with an <code>@</code> symbol. Specifying a group name has the same effect as specifying all the users in that group. </p>
<p> You can define group members in the <code>acl.groups</code> section. If a group name is not defined there, and Mercurial is running under a Unix-like system, the list of users will be taken from the OS. Otherwise, an exception will be raised.</p>
<h3>Example Configuration</h3>
<p>[hooks]<br />
#Use this if you want to check access restrictions at commit time<br />
pretxncommit.acl = python:hgext.acl.hook<br />
#Use this if you want to check access restrictions for pull, push,<br />
#bundle and serve.<br />
pretxnchangegroup.acl = python:hgext.acl.hook<br />
[acl]<br />
#Allow or deny access for incoming changes only if their source is<br />
#listed here, let them pass otherwise.Source is &#8220;serve&#8221; for all<br />
#remote access(http or ssh), &#8220;push&#8221;, &#8220;pull&#8221; or &#8220;bundle&#8221; when the<br />
#related commands are run locally.<br />
#Default : serve<br />
sources = serve<br />
[acl.deny.branches]<br />
#Everyone is denied to the frozen branch:<br />
frozen-branch = *<br />
#A bad user is denied on all branches:<br />
* = bad-user<br />
[acl.allow.branches]<br />
#A few users are allowed on branch &#8211; a:<br />
branch-a = user-1, user-2, user-3<br />
#Only one user is allowed on branch &#8211; b:<br />
branch-b = user-1<br />
#The super user is allowed on any branch:<br />
* = super-user<br />
#Everyone is allowed on branch &#8211; for &#8211; tests:<br />
branch-for-tests = *<br />
[acl.deny]<br />
#This list is checked first.If a match is found, acl.allow is not<br />
#checked.All users are granted access if acl.deny is not present.<br />
#Format for both lists : glob pattern = user, &#8230;, @group, &#8230;<br />
#To match everyone, use an asterisk for the user:<br />
#my / glob / pattern = *<br />
#user6 will not have write access to any file:<br />
** = user6<br />
#Group &#8220;hg-denied&#8221; will not have write access to any file:<br />
** = @hg-denied<br />
#Nobody will be able to change &#8220;DONT-TOUCH-THIS.txt&#8221;, despite<br />
#everyone being able to change all other files.See below.<br />
src/main/resources/DONT-TOUCH-THIS.txt = *<br />
[acl.allow]<br />
#if acl.allow is not present, all users are allowed by default<br />
#empty acl.allow = no users allowed<br />
#User &#8220;doc_writer&#8221; has write access to any file under the &#8220;docs&#8221;<br />
#folder:<br />
docs/** = doc_writer<br />
# User &#8220;jack&#8221; and group &#8220;designers&#8221; have write access to any file<br />
# under the &#8220;images&#8221; folder:<br />
images/** = jack, @designers<br />
# Everyone (except for &#8220;user6&#8221; and &#8220;@hg-denied&#8221; &#8211; see acl.deny above)<br />
# will have write access to any file under the &#8220;resources&#8221; folder<br />
# (except for 1 file. See acl.deny):<br />
src/main/resources/** = *<br />
.hgtags = release_engineer</p>
<h3>Examples using the ! prefix</h3>
<p> Suppose there&#8217;s a branch that only a given user (or group) should be able to push to, and you don&#8217;t want to restrict access to any other branch that may be created. </p>
<p> The &quot;!&quot; prefix allows you to prevent anyone except a given user or group to push changesets in a given branch or path. </p>
<p> In the examples below, we will: 1) Deny access to branch &quot;ring&quot; to anyone but user &quot;gollum&quot; 2) Deny access to branch &quot;lake&quot; to anyone but members of the group &quot;hobbit&quot; 3) Deny access to a file to anyone but user &quot;gollum&quot; </p>
<p>[acl.allow.branches]<br />
#Empty<br />
    [acl.deny.branches]<br />
# 1) only &#8216;gollum&#8217; can commit to branch &#8216;ring&#8217;;<br />
#&#8217;gollum&#8217; and anyone else can still commit to any other branch.<br />
    ring = !gollum<br />
# 2) only members of the group &#8216;hobbit&#8217; can commit to branch &#8216;lake&#8217;;<br />
#&#8217;hobbit&#8217; members and anyone else can still commit to any other branch.<br />
               lake = !@hobbit<br />
#You can also deny access based on file paths:<br />
                          [acl.allow]<br />
#Empty<br />
                          [acl.deny]<br />
# 3) only &#8216;gollum&#8217; can change the file below;<br />
#&#8217;gollum&#8217; and anyone else can still change any other file.<br />
                      / misty / mountains / cave / ring = !gollum</p>
<h3>blackbox</h3>
<p> log repository events to a blackbox for debugging </p>
<p> Logs event information to .hg/blackbox.log to help debug and diagnose problems. The events that get logged can be configured via the blackbox.track config key. Examples: </p>
<p>[blackbox] track = *[blackbox] track = command, commandfinish, commandexception, exthook, pythonhook[blackbox] track = incoming[blackbox]<br />
#limit the size of a log file<br />
                                                                                          maxsize = 1.5 MB<br />
#rotate up to N log files when the current one gets too big<br />
                                                                                              maxfiles = 3</p>
<h3>Commands</h3>
<h3>blackbox</h3>
<pre>
hg blackbox [OPTION]...
</pre>
<p> view the recent repository events </p>
<p> Options:</p>
<dl>
<dt><code>-l, &#8211;limit</code></p>
<dd> the number of events to show (default: 10)</dl>
<h3>bugzilla</h3>
<p> hooks for integrating with the Bugzilla bug tracker </p>
<p> This hook extension adds comments on bugs in Bugzilla when changesets that refer to bugs by Bugzilla ID are seen. The comment is formatted using the Mercurial template mechanism. </p>
<p> The bug references can optionally include an update for Bugzilla of the hours spent working on the bug. Bugs can also be marked fixed. </p>
<p> Three basic modes of access to Bugzilla are provided:</p>
<dl>
<dt>1.</p>
<dd> Access via the Bugzilla XMLRPC interface. Requires Bugzilla 3.4 or later.</p>
<dt>2.</p>
<dd> Check data via the Bugzilla XMLRPC interface and submit bug change via email to Bugzilla email interface. Requires Bugzilla 3.4 or later.</p>
<dt>3.</p>
<dd> Writing directly to the Bugzilla database. Only Bugzilla installations using MySQL are supported. Requires Python MySQLdb. </p>
<p> Writing directly to the database is susceptible to schema changes, and relies on a Bugzilla contrib script to send out bug change notification emails. This script runs as the user running Mercurial, must be run on the host with the Bugzilla install, and requires permission to read Bugzilla configuration details and the necessary MySQL user and password to have full access rights to the Bugzilla database. For these reasons this access mode is now considered deprecated, and will not be updated for new Bugzilla versions going forward. Only adding comments is supported in this access mode. </p>
<p> Access via XMLRPC needs a Bugzilla username and password to be specified in the configuration. Comments are added under that username. Since the configuration must be readable by all Mercurial users, it is recommended that the rights of that user are restricted in Bugzilla to the minimum necessary to add comments. Marking bugs fixed requires Bugzilla 4.0 and later. </p>
<p> Access via XMLRPC/email uses XMLRPC to query Bugzilla, but sends email to the Bugzilla email interface to submit comments to bugs. The From: address in the email is set to the email address of the Mercurial user, so the comment appears to come from the Mercurial user. In the event that the Mercurial user email is not recognized by Bugzilla as a Bugzilla user, the email associated with the Bugzilla username used to log into Bugzilla is used instead as the source of the comment. Marking bugs fixed works on all supported Bugzilla versions. </p>
<p> Configuration items common to all access modes:</p>
<dt><code>bugzilla.version</code></p>
<dd> The access type to use. Values recognized are:</p>
<dt><code>xmlrpc</code></p>
<dd>
<p> Bugzilla XMLRPC interface.</p>
<dt><code>xmlrpc+email</code></p>
<dd>
<p> Bugzilla XMLRPC and email interfaces.</p>
<dt><code>3.0</code></p>
<dd>
<p> MySQL access, Bugzilla 3.0 and later.</p>
<dt><code>2.18</code></p>
<dd>
<p> MySQL access, Bugzilla 2.18 and up to but not including 3.0.</p>
<dt><code>2.16</code></p>
<dd>
<p> MySQL access, Bugzilla 2.16 and up to but not including 2.18.</p>
<dt><code>bugzilla.regexp</code></p>
<dd> Regular expression to match bug IDs for update in changeset commit message. It must contain one &quot;()&quot; named group <code>&lt;ids&gt;</code> containing the bug IDs separated by non-digit characters. It may also contain a named group <code>&lt;hours&gt;</code> with a floating-point number giving the hours worked on the bug. If no named groups are present, the first &quot;()&quot; group is assumed to contain the bug IDs, and work time is not updated. The default expression matches <code>Bug 1234</code>, <code>Bug no. 1234</code>, <code>Bug number 1234</code>, <code>Bugs 1234,5678</code>, <code>Bug 1234 and 5678</code> and variations thereof, followed by an hours number prefixed by <code>h</code> or <code>hours</code>, e.g. <code>hours 1.5</code>. Matching is case insensitive.</p>
<dt><code>bugzilla.fixregexp</code></p>
<dd> Regular expression to match bug IDs for marking fixed in changeset commit message. This must contain a &quot;()&quot; named group <code>&lt;ids&gt;` containing the bug IDs separated by non-digit characters. It may also contain a named group &#8220;&lt;hours&gt;</code> with a floating-point number giving the hours worked on the bug. If no named groups are present, the first &quot;()&quot; group is assumed to contain the bug IDs, and work time is not updated. The default expression matches <code>Fixes 1234</code>, <code>Fixes bug 1234</code>, <code>Fixes bugs 1234,5678</code>, <code>Fixes 1234 and 5678</code> and variations thereof, followed by an hours number prefixed by <code>h</code> or <code>hours</code>, e.g. <code>hours 1.5</code>. Matching is case insensitive.</p>
<dt><code>bugzilla.fixstatus</code></p>
<dd> The status to set a bug to when marking fixed. Default <code>RESOLVED</code>.</p>
<dt><code>bugzilla.fixresolution</code></p>
<dd> The resolution to set a bug to when marking fixed. Default <code>FIXED</code>.</p>
<dt><code>bugzilla.style</code></p>
<dd> The style file to use when formatting comments.</p>
<dt><code>bugzilla.template</code></p>
<dd> Template to use when formatting comments. Overrides style if specified. In addition to the usual Mercurial keywords, the extension specifies:</p>
<dt><code>{bug}</code></p>
<dd>
<p> The Bugzilla bug ID.</p>
<dt><code>{root}</code></p>
<dd>
<p> The full pathname of the Mercurial repository.</p>
<dt><code>{webroot}</code></p>
<dd>
<p> Stripped pathname of the Mercurial repository.</p>
<dt><code>{hgweb}</code></p>
<dd>
<p> Base URL for browsing Mercurial repositories. </p>
<p> Default <code>changeset {node|short} in repo {root} refers to bug {bug}.
details:
	{desc|tabindent}</code></p>
<dt><code>bugzilla.strip</code></p>
<dd> The number of path separator characters to strip from the front of the Mercurial repository path (<code>{root}</code> in templates) to produce <code>{webroot}</code>. For example, a repository with <code>{root}</code> <code>/var/local/my-project</code> with a strip of 2 gives a value for <code>{webroot}</code> of <code>my-project</code>. Default 0.</p>
<dt><code>web.baseurl</code></p>
<dd> Base URL for browsing Mercurial repositories. Referenced from templates as <code>{hgweb}</code>. </p>
<p> Configuration items common to XMLRPC+email and MySQL access modes:</p>
<dt><code>bugzilla.usermap</code></p>
<dd> Path of file containing Mercurial committer email to Bugzilla user email mappings. If specified, the file should contain one mapping per line: </p>
<pre>
committer = Bugzilla user
</pre>
<p> See also the <code>[usermap]</code> section. </p>
<p> The <code>[usermap]</code> section is used to specify mappings of Mercurial committer email to Bugzilla user email. See also <code>bugzilla.usermap</code>. Contains entries of the form <code>committer = Bugzilla user</code>. </p>
<p> XMLRPC access mode configuration:</p>
<dt><code>bugzilla.bzurl</code></p>
<dd> The base URL for the Bugzilla installation. Default <code><a rel="nofollow" href="http://localhost/bugzilla">http://localhost/bugzilla</a></code>.</p>
<dt><code>bugzilla.user</code></p>
<dd> The username to use to log into Bugzilla via XMLRPC. Default <code>bugs</code>.</p>
<dt><code>bugzilla.password</code></p>
<dd> The password for Bugzilla login. </p>
<p> XMLRPC+email access mode uses the XMLRPC access mode configuration items, and also:</p>
<dt><code>bugzilla.bzemail</code></p>
<dd> The Bugzilla email address. </p>
<p> In addition, the Mercurial email settings must be configured. See the documentation in <a href="/docs/linux/man/5-hgrc/">hgrc</a>(5), sections <code>[email]</code> and <code>[smtp]</code>. </p>
<p> MySQL access mode configuration:</p>
<dt><code>bugzilla.host</code></p>
<dd> Hostname of the MySQL server holding the Bugzilla database. Default <code>localhost</code>.</p>
<dt><code>bugzilla.db</code></p>
<dd> Name of the Bugzilla database in MySQL. Default <code>bugs</code>.</p>
<dt><code>bugzilla.user</code></p>
<dd> Username to use to access MySQL server. Default <code>bugs</code>.</p>
<dt><code>bugzilla.password</code></p>
<dd> Password to use to access MySQL server.</p>
<dt><code>bugzilla.timeout</code></p>
<dd> Database connection timeout (seconds). Default 5.</p>
<dt><code>bugzilla.bzuser</code></p>
<dd> Fallback Bugzilla user name to record comments with, if changeset committer cannot be found as a Bugzilla user.</p>
<dt><code>bugzilla.bzdir</code></p>
<dd> Bugzilla install directory. Used by default notify. Default <code>/var/www/html/bugzilla</code>.</p>
<dt><code>bugzilla.notify</code></p>
<dd> The command to run to get Bugzilla to send bug change notification emails. Substitutes from a map with 3 keys, <code>bzdir</code>, <code>id</code> (bug id) and <code>user</code> (committer bugzilla email). Default depends on version; from 2.18 it is &quot;cd %(bzdir)s &amp;&amp; perl -T contrib/sendbugmail.pl %(id)s %(user)s&quot;. </p>
<p> Activating the extension: </p>
<p>[extensions] bugzilla =<br />
    [hooks]<br />
#run bugzilla hook on every change pulled or pushed in here<br />
    incoming.bugzilla = python : hgext.bugzilla.hook</p>
<p> Example configurations: </p>
<p> XMLRPC example configuration. This uses the Bugzilla at <code><a rel="nofollow" href="http://my-project.org/bugzilla">http://my-project.org/bugzilla</a></code>, logging in as user <code>bugmail [at] my-project.org</code> with password <code>plugh</code>. It is used with a collection of Mercurial repositories in <code>/var/local/hg/repos/</code>, with a web interface at <code><a rel="nofollow" href="http://my-project.org/hg">http://my-project.org/hg</a></code>. </p>
<p>[bugzilla] bzurl = http : // my-project.org/bugzilla<br />
                          user = bugmail[at] my &#8211; project.org<br />
                                                      password = plugh<br />
                                     version = xmlrpc template = Changeset{node | short} in{root | basename}.{hgweb} / {webroot} / rev /<br />
{<br />
    node | short<br />
}<br />

<br />
{<br />
    desc<br />
}<br />

<br />
    strip = 5<br />
        [web] baseurl = http: // my-project.org/hg</p>
<p> XMLRPC+email example configuration. This uses the Bugzilla at <code><a rel="nofollow" href="http://my-project.org/bugzilla">http://my-project.org/bugzilla</a></code>, logging in as user <code>bugmail [at] my-project.org</code> with password <code>plugh</code>. It is used with a collection of Mercurial repositories in <code>/var/local/hg/repos/</code>, with a web interface at <code><a rel="nofollow" href="http://my-project.org/hg">http://my-project.org/hg</a></code>. Bug comments are sent to the Bugzilla email address <code>bugzilla [at] my-project.org</code>. </p>
<p>[bugzilla] bzurl = http : // my-project.org/bugzilla<br />
                          user = bugmail[at] my &#8211; project.org<br />
                                                      password = plugh<br />
                                     version = xmlrpc<br />
                                         bzemail = bugzilla[at] my &#8211; project.org template = Changeset{node | short} in{root | basename}.{hgweb} / {webroot} / rev /<br />
{<br />
    node | short<br />
}<br />

<br />
{<br />
    desc<br />
}<br />

<br />
    strip = 5<br />
        [web] baseurl = http : // my-project.org/hg<br />
                               [usermap] user[at] emaildomain.com = user.name[at] bugzilladomain.com</p>
<p> MySQL example configuration. This has a local Bugzilla 3.2 installation in <code>/opt/bugzilla-3.2</code>. The MySQL database is on <code>localhost</code>, the Bugzilla database name is <code>bugs</code> and MySQL is accessed with MySQL username <code>bugs</code> password <code>XYZZY</code>. It is used with a collection of Mercurial repositories in <code>/var/local/hg/repos/</code>, with a web interface at <code><a rel="nofollow" href="http://my-project.org/hg">http://my-project.org/hg</a></code>. </p>
<p>[bugzilla] host = localhost<br />
    password = XYZZY<br />
        version = 3.0 bzuser = unknown[at] domain.com<br />
                                   bzdir = / opt / bugzilla &#8211; 3.2 template = Changeset{node | short} in{root | basename}.{hgweb} / {webroot} / rev /<br />
{<br />
    node | short<br />
}<br />

<br />
{<br />
    desc<br />
}<br />

<br />
    strip = 5<br />
        [web] baseurl = http : // my-project.org/hg<br />
                               [usermap] user[at] emaildomain.com = user.name[at] bugzilladomain.com</p>
<p> All the above add a comment to the Bugzilla bug record of the form: </p>
<pre>
Changeset 3b16791d6642 in repository-name.
<a rel="nofollow" href="http://my-project.org/hg/repository-name/rev/3b16791d6642">http://my-project.org/hg/repository-name/rev/3b16791d6642</a>
Changeset commit comment. Bug 1234.
</pre>
</dl>
<h3>children</h3>
<p> command to display child changesets (DEPRECATED) </p>
<p> This extension is deprecated. You should use <code>hg log -r &quot;children(REV)&quot;</code>: instead.</p>
<h3>Commands</h3>
<h3>children</h3>
<p>hg children[-r REV][FILE]</p>
<p> Print the children of the working directory&#8217;s revisions. If a revision is given via -r/&#8211;rev, the children of that revision will be printed. If a file argument is given, revision in which the file was last changed (after the working directory revision or the argument to &#8211;rev if given) is printed. </p>
<p> Options:</p>
<dl>
<dt><code>-r, &#8211;rev</code></p>
<dd> show children of the specified revision</p>
<dt><code>&#8211;style</code></p>
<dd> display using template map file</p>
<dt><code>&#8211;template</code></p>
<dd> display with template</dl>
<h3>churn</h3>
<p> command to display statistics about repository history</p>
<h3>Commands</h3>
<h3>churn</h3>
<p>hg churn[-d DATE][-r REV][&#8211;aliases FILE][FILE]</p>
<p> This command will display a histogram representing the number of changed lines or revisions, grouped according to the given template. The default template will group changes by author. The &#8211;dateformat option may be used to group the results by date instead. </p>
<p> Statistics are based on the number of changed lines, or alternatively the number of matching revisions if the &#8211;changesets option is specified. </p>
<p> Examples: </p>
<pre>
# display count of changed lines for every committer
hg churn -t '{author|email}'
# display daily activity graph
hg churn -f '%H' -s -c
# display activity of developers by month
hg churn -f '%Y-%m' -s -c
# display count of lines changed in every year
hg churn -f '%Y' -s
</pre>
<p> It is possible to map alternate email addresses to a main address by providing a file using the following format: </p>
<pre>
&lt;alias email&gt; = &lt;actual email&gt;
</pre>
<p> Such a file may be specified with the &#8211;aliases option, otherwise a .hgchurn file will be looked for in the working directory root. </p>
<p> Options:</p>
<dl>
<dt><code>-r, &#8211;rev</code></p>
<dd> count rate for the specified revision or range</p>
<dt><code>-d, &#8211;date</code></p>
<dd> count rate for revisions matching date spec</p>
<dt><code>-t, &#8211;template</code></p>
<dd> template to group changesets (default: {author|email})</p>
<dt><code>-f, &#8211;dateformat</code></p>
<dd> strftime-compatible format for grouping by date</p>
<dt><code>-c, &#8211;changesets</code></p>
<dd> count rate by number of changesets</p>
<dt><code>-s, &#8211;sort</code></p>
<dd> sort by key (default: sort by count)</p>
<dt><code>&#8211;diffstat</code></p>
<dd> display added/removed lines separately</p>
<dt><code>&#8211;aliases</code></p>
<dd> file with email aliases</p>
<dt><code>-I, &#8211;include</code></p>
<dd> include names matching the given patterns</p>
<dt><code>-X, &#8211;exclude</code></p>
<dd> exclude names matching the given patterns</dl>
<h3>color</h3>
<p> colorize output from some commands </p>
<p> This extension modifies the status and resolve commands to add color to their output to reflect file status, the qseries command to add color to reflect patch status (applied, unapplied, missing), and to diff-related commands to highlight additions, removals, diff headers, and trailing whitespace. </p>
<p> Other effects in addition to color, like bold and underlined text, are also available. By default, the terminfo database is used to find the terminal codes used to change color and effect. If terminfo is not available, then effects are rendered with the ECMA-48 SGR control function (aka ANSI escape codes). </p>
<p> Default effects may be overridden from your configuration file: </p>
<pre>
[color]
status.modified = blue bold underline red_background
status.added = green bold
status.removed = red bold blue_background
status.deleted = cyan bold underline
status.unknown = magenta bold underline
status.ignored = black bold
# 'none' turns off all effects
status.clean = none
status.copied = none
qseries.applied = blue bold underline
qseries.unapplied = black bold
qseries.missing = red bold
diff.diffline = bold
diff.extended = cyan bold
diff.file_a = red bold
diff.file_b = green bold
diff.hunk = magenta
diff.deleted = red
diff.inserted = green
diff.changed = white
diff.trailingwhitespace = bold red_background
resolve.unresolved = red bold
resolve.resolved = green bold
bookmarks.current = green
branches.active = none
branches.closed = black bold
branches.current = green
branches.inactive = none
tags.normal = green
tags.local = black bold
</pre>
<p> The available effects in terminfo mode are &#8216;blink&#8217;, &#8216;bold&#8217;, &#8216;dim&#8217;, &#8216;inverse&#8217;, &#8216;invisible&#8217;, &#8216;italic&#8217;, &#8216;standout&#8217;, and &#8216;underline&#8217;; in ECMA-48 mode, the options are &#8216;bold&#8217;, &#8216;inverse&#8217;, &#8216;italic&#8217;, and &#8216;underline&#8217;. How each is rendered depends on the terminal emulator. Some may not be available for a given terminal type, and will be silently ignored. </p>
<p> Note that on some systems, terminfo mode may cause problems when using color with the pager extension and less -R. less with the -R option will only display ECMA-48 color codes, and terminfo mode may sometimes emit codes that less doesn&#8217;t understand. You can work around this by either using ansi mode (or auto mode), or by using less -r (which will pass through all terminal control codes, not just color control codes). </p>
<p> Because there are only eight standard colors, this module allows you to define color names for other color slots which might be available for your terminal type, assuming terminfo mode. For instance: </p>
<pre>
color.brightblue = 12
color.pink = 207
color.orange = 202
</pre>
<p> to set &#8216;brightblue&#8217; to color slot 12 (useful for 16 color terminals that have brighter colors defined in the upper eight) and, &#8216;pink&#8217; and &#8216;orange&#8217; to colors in 256-color xterm&#8217;s default color cube. These defined colors may then be used as any of the pre-defined eight, including appending &#8216;_background&#8217; to set the background to that color. </p>
<p> By default, the color extension will use ANSI mode (or win32 mode on Windows) if it detects a terminal. To override auto mode (to enable terminfo mode, for example), set the following configuration option: </p>
<pre>
[color]
mode = terminfo
</pre>
<p> Any value other than &#8216;ansi&#8217;, &#8216;win32&#8217;, &#8216;terminfo&#8217;, or &#8216;auto&#8217; will disable color.</p>
<h3>convert</h3>
<p> import revisions from foreign VCS repositories into Mercurial</p>
<h3>Commands</h3>
<h3>convert</h3>
<p>hg convert[OPTION]&#8230; SOURCE[DEST[REVMAP]]</p>
<p> Accepted source formats [identifiers]:</p>
<dl>
<dt>&bull;</p>
<dd> Mercurial [hg]</p>
<dt>&bull;</p>
<dd> CVS [cvs]</p>
<dt>&bull;</p>
<dd> Darcs [darcs]</p>
<dt>&bull;</p>
<dd> git [git]</p>
<dt>&bull;</p>
<dd> Subversion [svn]</p>
<dt>&bull;</p>
<dd> Monotone [mtn]</p>
<dt>&bull;</p>
<dd> GNU Arch [gnuarch]</p>
<dt>&bull;</p>
<dd> Bazaar [bzr]</p>
<dt>&bull;</p>
<dd> Perforce [p4] </p>
<p> Accepted destination formats [identifiers]:</p>
<dt>&bull;</p>
<dd> Mercurial [hg]</p>
<dt>&bull;</p>
<dd> Subversion [svn] (history on branches is not preserved) </p>
<p> If no revision is given, all revisions will be converted. Otherwise, convert will only import up to the named revision (given in a format understood by the source). </p>
<p> If no destination directory name is specified, it defaults to the basename of the source with <code>-hg</code> appended. If the destination repository doesn&#8217;t exist, it will be created. </p>
<p> By default, all sources except Mercurial will use &#8211;branchsort. Mercurial uses &#8211;sourcesort to preserve original revision numbers order. Sort modes have the following effects:</p>
<dt><code>&#8211;branchsort</code></p>
<dd> convert from parent to child revision when possible, which means branches are usually converted one after the other. It generates more compact repositories.</p>
<dt><code>&#8211;datesort</code></p>
<dd> sort revisions by date. Converted repositories have good-looking changelogs but are often an order of magnitude larger than the same ones generated by &#8211;branchsort.</p>
<dt><code>&#8211;sourcesort</code></p>
<dd> try to preserve source revisions order, only supported by Mercurial sources.</p>
<dt><code>&#8211;closesort</code></p>
<dd> try to move closed revisions as close as possible to parent branches, only supported by Mercurial sources. </p>
<p> If <code>REVMAP</code> isn&#8217;t given, it will be put in a default location (<code>&lt;dest&gt;/.hg/shamap</code> by default). The <code>REVMAP</code> is a simple text file that maps each source commit ID to the destination ID for that revision, like so: </p>
<pre>
&lt;source ID&gt; &lt;destination ID&gt;
</pre>
<p> If the file doesn&#8217;t exist, it&#8217;s automatically created. It&#8217;s updated on each commit copied, so <code>hg convert</code>: can be interrupted and can be run repeatedly to copy new commits. </p>
<p> The authormap is a simple text file that maps each source commit author to a destination commit author. It is handy for source SCMs that use unix logins to identify authors (e.g.: CVS). One line per author mapping and the line format is: </p>
<pre>
source author = destination author
</pre>
<p> Empty lines and lines starting with a <code>#</code> are ignored. </p>
<p> The filemap is a file that allows filtering and remapping of files and directories. Each line can contain one of the following directives: </p>
<pre>
include path/to/file-or-dir
exclude path/to/file-or-dir
rename path/to/source path/to/destination
</pre>
<p> Comment lines start with <code>#</code>. A specified path matches if it equals the full relative name of a file or one of its parent directories. The <code>include</code> or <code>exclude</code> directive with the longest matching path applies, so line order does not matter. </p>
<p> The <code>include</code> directive causes a file, or all files under a directory, to be included in the destination repository, and the exclusion of all other files and directories not explicitly included. The <code>exclude</code> directive causes files or directories to be omitted. The <code>rename</code> directive renames a file or directory if it is converted. To rename from a subdirectory into the root of the repository, use <code>.</code> as the path to rename to. </p>
<p> The splicemap is a file that allows insertion of synthetic history, letting you specify the parents of a revision. This is useful if you want to e.g. give a Subversion merge two parents, or graft two disconnected series of history together. Each entry contains a key, followed by a space, followed by one or two comma-separated values: </p>
<pre>
key parent1, parent2
</pre>
<p> The key is the revision ID in the source revision control system whose parents should be modified (same format as a key in .hg/shamap). The values are the revision IDs (in either the source or destination revision control system) that should be used as the new parents for that node. For example, if you have merged &quot;release-1.0&quot; into &quot;trunk&quot;, then you should specify the revision on &quot;trunk&quot; as the first parent and the one on the &quot;release-1.0&quot; branch as the second. </p>
<p> The branchmap is a file that allows you to rename a branch when it is being brought in from whatever external repository. When used in conjunction with a splicemap, it allows for a powerful combination to help fix even the most badly mismanaged repositories and turn them into nicely structured Mercurial repositories. The branchmap contains lines of the form: </p>
<pre>
original_branch_name new_branch_name
</pre>
<p> where &quot;original_branch_name&quot; is the name of the branch in the source repository, and &quot;new_branch_name&quot; is the name of the branch is the destination repository. No whitespace is allowed in the branch names. This can be used to (for instance) move code in one repository from &quot;default&quot; to a named branch.</dl>
<h3>Mercurial Source</h3>
<p> The Mercurial source recognizes the following configuration options, which you can set on the command line with <code>&#8211;config</code>:</p>
<dl>
<dt><code>convert.hg.ignoreerrors</code></p>
<dd> ignore integrity errors when reading. Use it to fix Mercurial repositories with missing revlogs, by converting from and to Mercurial. Default is False.</p>
<dt><code>convert.hg.saverev</code></p>
<dd> store original revision ID in changeset (forces target IDs to change). It takes a boolean argument and defaults to False.</p>
<dt><code>convert.hg.startrev</code></p>
<dd> convert start revision and its descendants. It takes a hg revision identifier and defaults to 0.</dl>
<h3>CVS Source</h3>
<p> CVS source will use a sandbox (i.e. a checked-out copy) from CVS to indicate the starting point of what will be converted. Direct access to the repository files is not needed, unless of course the repository is <code>:local:</code>. The conversion uses the top level directory in the sandbox to find the CVS repository, and then uses CVS rlog commands to find files to convert. This means that unless a filemap is given, all files under the starting directory will be converted, and that any directory reorganization in the CVS sandbox is ignored. </p>
<p> The following options can be used with <code>&#8211;config</code>:</p>
<dl>
<dt><code>convert.cvsps.cache</code></p>
<dd> Set to False to disable remote log caching, for testing and debugging purposes. Default is True.</p>
<dt><code>convert.cvsps.fuzz</code></p>
<dd> Specify the maximum time (in seconds) that is allowed between commits with identical user and log message in a single changeset. When very large files were checked in as part of a changeset then the default may not be long enough. The default is 60.</p>
<dt><code>convert.cvsps.mergeto</code></p>
<dd> Specify a regular expression to which commit log messages are matched. If a match occurs, then the conversion process will insert a dummy revision merging the branch on which this log message occurs to the branch indicated in the regex. Default is <code>&#123;&#123;mergetobranch ([-\w]+)}}</code></p>
<dt><code>convert.cvsps.mergefrom</code></p>
<dd> Specify a regular expression to which commit log messages are matched. If a match occurs, then the conversion process will add the most recent revision on the branch indicated in the regex as the second parent of the changeset. Default is <code>&#123;&#123;mergefrombranch ([-\w]+)}}</code></p>
<dt><code>convert.localtimezone</code></p>
<dd> use local time (as determined by the TZ environment variable) for changeset date/times. The default is False (use UTC).</p>
<dt><code>hooks.cvslog</code></p>
<dd> Specify a Python function to be called at the end of gathering the CVS log. The function is passed a list with the log entries, and can modify the entries in-place, or add or delete them.</p>
<dt><code>hooks.cvschangesets</code></p>
<dd> Specify a Python function to be called after the changesets are calculated from the CVS log. The function is passed a list with the changeset entries, and can modify the changesets in-place, or add or delete them. </p>
<p> An additional &quot;debugcvsps&quot; Mercurial command allows the builtin changeset merging code to be run without doing a conversion. Its parameters and output are similar to that of cvsps 2.1. Please see the command help for more details.</dl>
<h3>Subversion Source</h3>
<p> Subversion source detects classical trunk/branches/tags layouts. By default, the supplied <code><a href="svn://repo/path/">svn://repo/path/</a></code> source URL is converted as a single branch. If <code><a href="svn://repo/path/trunk">svn://repo/path/trunk</a></code> exists it replaces the default branch. If <code><a href="svn://repo/path/branches">svn://repo/path/branches</a></code> exists, its subdirectories are listed as possible branches. If <code><a href="svn://repo/path/tags">svn://repo/path/tags</a></code> exists, it is looked for tags referencing converted branches. Default <code>trunk</code>, <code>branches</code> and <code>tags</code> values can be overridden with following options. Set them to paths relative to the source URL, or leave them blank to disable auto detection. </p>
<p> The following options can be set with <code>&#8211;config</code>:</p>
<dl>
<dt><code>convert.svn.branches</code></p>
<dd> specify the directory containing branches. The default is <code>branches</code>.</p>
<dt><code>convert.svn.tags</code></p>
<dd> specify the directory containing tags. The default is <code>tags</code>.</p>
<dt><code>convert.svn.trunk</code></p>
<dd> specify the name of the trunk branch. The default is <code>trunk</code>.</p>
<dt><code>convert.localtimezone</code></p>
<dd> use local time (as determined by the TZ environment variable) for changeset date/times. The default is False (use UTC). </p>
<p> Source history can be retrieved starting at a specific revision, instead of being integrally converted. Only single branch conversions are supported.</p>
<dt><code>convert.svn.startrev</code></p>
<dd> specify start Subversion revision number. The default is 0.</dl>
<h3>Perforce Source</h3>
<p> The Perforce (P4) importer can be given a p4 depot path or a client specification as source. It will convert all files in the source to a flat Mercurial repository, ignoring labels, branches and integrations. Note that when a depot path is given you then usually should specify a target directory, because otherwise the target may be named <code>&#8230;-hg</code>. </p>
<p> It is possible to limit the amount of source history to be converted by specifying an initial Perforce revision:</p>
<dl>
<dt><code>convert.p4.startrev</code></p>
<dd> specify initial Perforce revision (a Perforce changelist number).</dl>
<h3>Mercurial Destination</h3>
<p> The following options are supported:</p>
<dl>
<dt><code>convert.hg.clonebranches</code></p>
<dd> dispatch source branches in separate clones. The default is False.</p>
<dt><code>convert.hg.tagsbranch</code></p>
<dd> branch name for tag revisions, defaults to <code>default</code>.</p>
<dt><code>convert.hg.usebranchnames</code></p>
<dd> preserve branch names. The default is True. </p>
<p> Options:</p>
<dt><code>&#8211;authors</code></p>
<dd> username mapping filename (DEPRECATED, use &#8211;authormap instead)</p>
<dt><code>-s, &#8211;source-type</code></p>
<dd> source repository type</p>
<dt><code>-d, &#8211;dest-type</code></p>
<dd> destination repository type</p>
<dt><code>-r, &#8211;rev</code></p>
<dd> import up to target revision REV</p>
<dt><code>-A, &#8211;authormap</code></p>
<dd> remap usernames using this file</p>
<dt><code>&#8211;filemap</code></p>
<dd> remap file names using contents of file</p>
<dt><code>&#8211;splicemap</code></p>
<dd> splice synthesized history into place</p>
<dt><code>&#8211;branchmap</code></p>
<dd> change branch names while converting</p>
<dt><code>&#8211;branchsort</code></p>
<dd> try to sort changesets by branches</p>
<dt><code>&#8211;datesort</code></p>
<dd> try to sort changesets by date</p>
<dt><code>&#8211;sourcesort</code></p>
<dd> preserve source changesets order</p>
<dt><code>&#8211;closesort</code></p>
<dd> try to reorder closed revisions</dl>
<h3>eol</h3>
<p> automatically manage newlines in repository files </p>
<p> This extension allows you to manage the type of line endings (CRLF or LF) that are used in the repository and in the local working directory. That way you can get CRLF line endings on Windows and LF on Unix/Mac, thereby letting everybody use their OS native line endings. </p>
<p> The extension reads its configuration from a versioned <code>.hgeol</code> configuration file found in the root of the working copy. The <code>.hgeol</code> file use the same syntax as all other Mercurial configuration files. It uses two sections, <code>[patterns]</code> and <code>[repository]</code>. </p>
<p> The <code>[patterns]</code> section specifies how line endings should be converted between the working copy and the repository. The format is specified by a file pattern. The first match is used, so put more specific patterns first. The available line endings are <code>LF</code>, <code>CRLF</code>, and <code>BIN</code>. </p>
<p> Files with the declared format of <code>CRLF</code> or <code>LF</code> are always checked out and stored in the repository in that format and files declared to be binary (<code>BIN</code>) are left unchanged. Additionally, <code>native</code> is an alias for checking out in the platform&#8217;s default line ending: <code>LF</code> on Unix (including Mac OS X) and <code>CRLF</code> on Windows. Note that <code>BIN</code> (do nothing to line endings) is Mercurial&#8217;s default behaviour; it is only needed if you need to override a later, more general pattern. </p>
<p> The optional <code>[repository]</code> section specifies the line endings to use for files stored in the repository. It has a single setting, <code>native</code>, which determines the storage line endings for files declared as <code>native</code> in the <code>[patterns]</code> section. It can be set to <code>LF</code> or <code>CRLF</code>. The default is <code>LF</code>. For example, this means that on Windows, files configured as <code>native</code> (<code>CRLF</code> by default) will be converted to <code>LF</code> when stored in the repository. Files declared as <code>LF</code>, <code>CRLF</code>, or <code>BIN</code> in the <code>[patterns]</code> section are always stored as-is in the repository. </p>
<p> Example versioned <code>.hgeol</code> file: </p>
<p>[patterns]<br />
    **.py = native<br />
                **.vcproj = CRLF<br />
                                **.txt = native<br />
    Makefile = LF<br />
                   **.jpg = BIN<br />
        [repository] native = LF</p>
<dl>
<dt>Note</p>
<dd> The rules will first apply when files are touched in the working copy, e.g. by updating to null and back to tip to touch all files. </p>
<p> The extension uses an optional <code>[eol]</code> section read from both the normal Mercurial configuration files and the <code>.hgeol</code> file, with the latter overriding the former. You can use that section to control the overall behavior. There are three settings:</p>
<dt>&bull;</p>
<dd> <code>eol.native</code> (default <code>os.linesep</code>) can be set to <code>LF</code> or <code>CRLF</code> to override the default interpretation of <code>native</code> for checkout. This can be used with <code>hg archive</code>: on Unix, say, to generate an archive where files have line endings for Windows.</p>
<dt>&bull;</p>
<dd> <code>eol.only-consistent</code> (default True) can be set to False to make the extension convert files with inconsistent EOLs. Inconsistent means that there is both <code>CRLF</code> and <code>LF</code> present in the file. Such files are normally not touched under the assumption that they have mixed EOLs on purpose.</p>
<dt>&bull;</p>
<dd> <code>eol.fix-trailing-newline</code> (default False) can be set to True to ensure that converted files end with a EOL character (either <code>
</code> or <code>
</code> as per the configured patterns). </p>
<p> The extension provides <code>cleverencode:</code> and <code>cleverdecode:</code> filters like the deprecated win32text extension does. This means that you can disable win32text and enable eol and your filters will still work. You only need to these filters until you have prepared a <code>.hgeol</code> file. </p>
<p> The <code>win32text.forbid*</code> hooks provided by the win32text extension have been unified into a single hook named <code>eol.checkheadshook</code>. The hook will lookup the expected line endings from the <code>.hgeol</code> file, which means you must migrate to a <code>.hgeol</code> file first before using the hook. <code>eol.checkheadshook</code> only checks heads, intermediate invalid revisions will be pushed. To forbid them completely, use the <code>eol.checkallhook</code> hook. These hooks are best used as <code>pretxnchangegroup</code> hooks. </p>
<p> See <code>hg help patterns</code>: for more information about the glob patterns used.</dl>
<h3>extdiff</h3>
<p> command to allow external programs to compare revisions </p>
<p> The extdiff Mercurial extension allows you to use external programs to compare revisions, or revision with working directory. The external diff programs are called with a configurable set of options and two non-option arguments: paths to directories containing snapshots of files to compare. </p>
<p> The extdiff extension also allows you to configure new diff commands, so you do not need to type <code>hg extdiff -p kdiff3</code>: always. </p>
<pre>
[extdiff]
# add new command that runs GNU <a href="//www.systutorials.com/docs/linux/man/1-diff/">diff</a>(1) in 'context diff' mode
cdiff = gdiff -Nprc5
## or the old way:
#cmd.cdiff = gdiff
#opts.cdiff = -Nprc5
# add new command called vdiff, runs kdiff3
vdiff = kdiff3
# add new command called meld, runs meld (no need to name twice)
meld =
# add new command called vimdiff, runs gvimdiff with DirDiff plugin
# (see <a rel="nofollow" href="http://www.vim.org/scripts/script.php?script_id=102)">http://www.vim.org/scripts/script.php?script_id=102)</a> Non
# English user, be sure to put &quot;let g:DirDiffDynamicDiffText = 1&quot; in
# your .vimrc
vimdiff = gvim -f &quot;+next&quot; \
          &quot;+execute 'DirDiff' fnameescape(argv(0)) fnameescape(<a href="//www.systutorials.com/docs/linux/man/1-argv/">argv</a>(1))&quot;
</pre>
<p> Tool arguments can include variables that are expanded at runtime: </p>
<pre>
$parent1, $plabel1 - filename, descriptive label of first parent
$child,   $clabel  - filename, descriptive label of child revision
$parent2, $plabel2 - filename, descriptive label of second parent
$root              - repository root
$parent is an alias for $parent1.
</pre>
<p> The extdiff extension will look in your [diff-tools] and [merge-tools] sections for diff tool arguments, when none are specified in [extdiff]. </p>
<p>[extdiff] kdiff3 =<br />
    [diff &#8211;<br />
        tools] kdiff3.diffargs = &#8211;L1 &#8216;$plabel1&#8217; &#8211;L2 &#8216;$clabel&#8217; $parent $child</p>
<p> You can use -I/-X and list of file or directory names like normal <code>hg diff</code>: command. The extdiff extension makes snapshots of only needed files, so running the external diff program will actually be pretty fast (at least faster than having to compare the entire tree).</p>
<h3>Commands</h3>
<h3>extdiff</h3>
<p>hg extdiff[OPT]&#8230;[FILE]&#8230;</p>
<p> Show differences between revisions for the specified files, using an external program. The default program used is diff, with default options &quot;-Npru&quot;. </p>
<p> To select a different program, use the -p/&#8211;program option. The program will be passed the names of two directories to compare. To pass additional options to the program, use -o/&#8211;option. These will be passed before the names of the directories to compare. </p>
<p> When two revision arguments are given, then changes are shown between those revisions. If only one revision is specified then that revision is compared to the working directory, and, when no revisions are specified, the working directory files are compared to its parent. </p>
<p> Options:</p>
<dl>
<dt><code>-p, &#8211;program</code></p>
<dd> comparison program to run</p>
<dt><code>-o, &#8211;option</code></p>
<dd> pass option to comparison program</p>
<dt><code>-r, &#8211;rev</code></p>
<dd> revision</p>
<dt><code>-c, &#8211;change</code></p>
<dd> change made by revision</p>
<dt><code>-I, &#8211;include</code></p>
<dd> include names matching the given patterns</p>
<dt><code>-X, &#8211;exclude</code></p>
<dd> exclude names matching the given patterns</dl>
<h3>factotum</h3>
<p> http authentication with factotum </p>
<p> This extension allows the <a href="/docs/linux/man/4-factotum/">factotum</a>(4) facility on Plan 9 from Bell Labs platforms to provide authentication information for HTTP access. Configuration entries specified in the auth section as well as authentication information provided in the repository URL are fully supported. If no prefix is specified, a value of &quot;*&quot; will be assumed. </p>
<p> By default, keys are specified as: </p>
<pre>
proto=pass service=hg prefix=&lt;prefix&gt; user=&lt;username&gt; !password=&lt;password&gt;
</pre>
<p> If the factotum extension is unable to read the required key, one will be requested interactively. </p>
<p> A configuration section is available to customize runtime behavior. By default, these entries are: </p>
<pre>
[factotum]
executable = /bin/auth/factotum
mountpoint = /mnt/factotum
service = hg
</pre>
<p> The executable entry defines the full path to the factotum binary. The mountpoint entry defines the path to the factotum file service. Lastly, the service entry controls the service name used when reading keys.</p>
<h3>fetch</h3>
<p> pull, update and merge in one command (DEPRECATED)</p>
<h3>Commands</h3>
<h3>fetch</h3>
<pre>
hg fetch [SOURCE]
</pre>
<p> This finds all changes from the repository at the specified path or URL and adds them to the local repository. </p>
<p> If the pulled changes add a new branch head, the head is automatically merged, and the result of the merge is committed. Otherwise, the working directory is updated to include the new changes. </p>
<p> When a merge is needed, the working directory is first updated to the newly pulled changes. Local changes are then merged into the pulled changes. To switch the merge order, use &#8211;switch-parent. </p>
<p> See <code>hg help dates</code>: for a list of formats valid for -d/&#8211;date. </p>
<p> Returns 0 on success. </p>
<p> Options:</p>
<dl>
<dt><code>-r, &#8211;rev</code></p>
<dd> a specific revision you would like to pull</p>
<dt><code>-e, &#8211;edit</code></p>
<dd> edit commit message</p>
<dt><code>&#8211;force-editor</code></p>
<dd> edit commit message (DEPRECATED)</p>
<dt><code>&#8211;switch-parent</code></p>
<dd> switch parents when merging</p>
<dt><code>-m, &#8211;message</code></p>
<dd> use text as commit message</p>
<dt><code>-l, &#8211;logfile</code></p>
<dd> read commit message from file</p>
<dt><code>-d, &#8211;date</code></p>
<dd> record the specified date as commit date</p>
<dt><code>-u, &#8211;user</code></p>
<dd> record the specified user as committer</p>
<dt><code>-e, &#8211;ssh</code></p>
<dd> specify ssh command to use</p>
<dt><code>&#8211;remotecmd</code></p>
<dd> specify hg command to run on the remote side</p>
<dt><code>&#8211;insecure</code></p>
<dd> do not verify server certificate (ignoring web.cacerts config)</dl>
<h3>gpg</h3>
<p> commands to sign and verify changesets</p>
<h3>Commands</h3>
<h3>sigcheck</h3>
<pre>
hg sigcheck REV
</pre>
<p> verify all the signatures there may be for a particular revision</p>
<h3>sign</h3>
<p>hg sign[OPTION]&#8230;[REV]&#8230;</p>
<p> If no revision is given, the parent of the working directory is used, or tip if no revision is checked out. </p>
<p> See <code>hg help dates</code>: for a list of formats valid for -d/&#8211;date. </p>
<p> Options:</p>
<dl>
<dt><code>-l, &#8211;local</code></p>
<dd> make the signature local</p>
<dt><code>-f, &#8211;force</code></p>
<dd> sign even if the sigfile is modified</p>
<dt><code>&#8211;no-commit</code></p>
<dd> do not commit the sigfile after signing</p>
<dt><code>-k, &#8211;key</code></p>
<dd> the key id to sign with</p>
<dt><code>-m, &#8211;message</code></p>
<dd> commit message</p>
<dt><code>-d, &#8211;date</code></p>
<dd> record the specified date as commit date</p>
<dt><code>-u, &#8211;user</code></p>
<dd> record the specified user as committer</dl>
<h3>sigs</h3>
<pre>
hg sigs
</pre>
<p> list signed changesets</p>
<h3>graphlog</h3>
<p> command to view revision graphs from a shell </p>
<p> This extension adds a &#8211;graph option to the incoming, outgoing and log commands. When this options is given, an ASCII representation of the revision graph is also shown.</p>
<h3>Commands</h3>
<h3>glog</h3>
<p>hg glog[OPTION]&#8230;[FILE]</p>
<p> Print a revision history alongside a revision graph drawn with ASCII characters. </p>
<p> Nodes printed as an @ character are parents of the working directory. </p>
<p> Options:</p>
<dl>
<dt><code>-f, &#8211;follow</code></p>
<dd> follow changeset history, or file history across copies and renames</p>
<dt><code>&#8211;follow-first</code></p>
<dd> only follow the first parent of merge changesets (DEPRECATED)</p>
<dt><code>-d, &#8211;date</code></p>
<dd> show revisions matching date spec</p>
<dt><code>-C, &#8211;copies</code></p>
<dd> show copied files</p>
<dt><code>-k, &#8211;keyword</code></p>
<dd> do case-insensitive search for a given text</p>
<dt><code>-r, &#8211;rev</code></p>
<dd> show the specified revision or range</p>
<dt><code>&#8211;removed</code></p>
<dd> include revisions where files were removed</p>
<dt><code>-m, &#8211;only-merges</code></p>
<dd> show only merges (DEPRECATED)</p>
<dt><code>-u, &#8211;user</code></p>
<dd> revisions committed by user</p>
<dt><code>&#8211;only-branch</code></p>
<dd> show only changesets within the given named branch (DEPRECATED)</p>
<dt><code>-b, &#8211;branch</code></p>
<dd> show changesets within the given named branch</p>
<dt><code>-P, &#8211;prune</code></p>
<dd> do not display revision or any of its ancestors</p>
<dt><code>-p, &#8211;patch</code></p>
<dd> show patch</p>
<dt><code>-g, &#8211;git</code></p>
<dd> use git extended diff format</p>
<dt><code>-l, &#8211;limit</code></p>
<dd> limit number of changes displayed</p>
<dt><code>-M, &#8211;no-merges</code></p>
<dd> do not show merges</p>
<dt><code>&#8211;stat</code></p>
<dd> output diffstat-style summary of changes</p>
<dt><code>-G, &#8211;graph</code></p>
<dd> show the revision DAG</p>
<dt><code>&#8211;style</code></p>
<dd> display using template map file</p>
<dt><code>&#8211;template</code></p>
<dd> display with template</p>
<dt><code>-I, &#8211;include</code></p>
<dd> include names matching the given patterns</p>
<dt><code>-X, &#8211;exclude</code></p>
<dd> exclude names matching the given patterns</dl>
<h3>hgcia</h3>
<p> hooks for integrating with the CIA.vc notification service </p>
<p> This is meant to be run as a changegroup or incoming hook. To configure it, set the following options in your hgrc: </p>
<p>[cia]<br />
#your registered CIA user name<br />
    user = foo<br />
#the name of the project in CIA<br />
        project = foo<br />
#the module(subproject)(optional)<br />
#module = foo<br />
#Append a diffstat to the log message(optional)<br />
#diffstat = False<br />
#Template to use for log messages(optional)<br />
#template = {desc }
{baseurl } {webroot } / rev / {node } &#8211;{diffstat }<br />
#Style to use(optional)<br />
#style = foo<br />
#The URL of the CIA notification service(optional)<br />
#You can use mailto : URLs to send by email, e.g.<br />
#mailto : cia[at] cia.vc<br />
#Make sure to set email.from if you do this.<br />
#url = http: // cia.vc/<br />
#print message instead of sending it(optional)<br />
#test = False<br />
#number of slashes to strip for url paths<br />
#strip = 0<br />
                      [hooks]<br />
#one of these:<br />
                  changegroup.cia = python : hgcia.hook<br />
#incoming.cia = python : hgcia.hook<br />
                                                 [web]<br />
#If you want hyperlinks(optional)<br />
                                             baseurl = http: // server/path/to/repo</p>
<h3>hgk</h3>
<p> browse the repository in a graphical way </p>
<p> The hgk extension allows browsing the history of a repository in a graphical way. It requires Tcl/Tk version 8.4 or later. (Tcl/Tk is not distributed with Mercurial.) </p>
<p> hgk consists of two parts: a Tcl script that does the displaying and querying of information, and an extension to Mercurial named hgk.py, which provides hooks for hgk to get information. hgk can be found in the contrib directory, and the extension is shipped in the hgext repository, and needs to be enabled. </p>
<p> The <code>hg view</code>: command will launch the hgk Tcl script. For this command to work, hgk must be in your search path. Alternately, you can specify the path to hgk in your configuration file: </p>
<pre>
[hgk]
path=/location/of/hgk
</pre>
<p> hgk can make use of the extdiff extension to visualize revisions. Assuming you had already configured extdiff vdiff command, just add: </p>
<pre>
[hgk]
vdiff=vdiff
</pre>
<p> Revisions context menu will now display additional entries to fire vdiff on hovered and selected revisions.</p>
<h3>Commands</h3>
<h3>view</h3>
<p>hg view[-l LIMIT][REVRANGE]</p>
<p> start interactive history viewer </p>
<p> Options:</p>
<dl>
<dt><code>-l, &#8211;limit</code></p>
<dd> limit number of changes displayed</dl>
<h3>highlight</h3>
<p> syntax highlighting for hgweb (requires Pygments) </p>
<p> It depends on the Pygments syntax highlighting library: <a rel="nofollow" href="http://pygments.org/:">http://pygments.org/:</a> </p>
<p> There is a single configuration option: </p>
<pre>
[web]
pygments_style = &lt;style&gt;
</pre>
<p> The default is &#8216;colorful&#8217;.</p>
<h3>histedit</h3>
<p> interactive history editing </p>
<p> With this extension installed, Mercurial gains one new command: histedit. Usage is as follows, assuming the following history: </p>
<pre>
@  3[tip]   7c2fd3b9020c   2009-04-27 18:04 -0500   durin42
|    Add delta
|
o  2   030b686bedc4   2009-04-27 18:04 -0500   durin42
|    Add gamma
|
o  1   c561b4e977df   2009-04-27 18:04 -0500   durin42
|    Add beta
|
o  0   d8d2fcd0e319   2009-04-27 18:04 -0500   durin42
     Add alpha
</pre>
<p> If you were to run <code>hg histedit c561b4e977df</code>, you would see the following file open in your editor: </p>
<pre>
pick c561b4e977df Add beta
pick 030b686bedc4 Add gamma
pick 7c2fd3b9020c Add delta
# Edit history between c561b4e977df and 7c2fd3b9020c
#
# Commands:
#  p, pick = use commit
#  e, edit = use commit, but stop for amending
#  f, fold = use commit, but fold into previous commit (combines N and N-1)
#  d, drop = remove commit from history
#  m, mess = edit message without changing commit content
#
</pre>
<p> In this file, lines beginning with <code>#</code> are ignored. You must specify a rule for each revision in your history. For example, if you had meant to add gamma before beta, and then wanted to add delta in the same revision as beta, you would reorganize the file to look like this: </p>
<pre>
pick 030b686bedc4 Add gamma
pick c561b4e977df Add beta
fold 7c2fd3b9020c Add delta
# Edit history between c561b4e977df and 7c2fd3b9020c
#
# Commands:
#  p, pick = use commit
#  e, edit = use commit, but stop for amending
#  f, fold = use commit, but fold into previous commit (combines N and N-1)
#  d, drop = remove commit from history
#  m, mess = edit message without changing commit content
#
</pre>
<p> At which point you close the editor and <code>histedit</code> starts working. When you specify a <code>fold</code> operation, <code>histedit</code> will open an editor when it folds those revisions together, offering you a chance to clean up the commit message: </p>
<pre>
Add beta
***
Add delta
</pre>
<p> Edit the commit message to your liking, then close the editor. For this example, let&#8217;s assume that the commit message was changed to <code>Add beta and delta.</code> After histedit has run and had a chance to remove any old or temporary revisions it needed, the history looks like this: </p>
<pre>
@  2[tip]   989b4d060121   2009-04-27 18:04 -0500   durin42
|    Add beta and delta.
|
o  1   081603921c3f   2009-04-27 18:04 -0500   durin42
|    Add gamma
|
o  0   d8d2fcd0e319   2009-04-27 18:04 -0500   durin42
     Add alpha
</pre>
<p> Note that <code>histedit</code> does <i>not</i> remove any revisions (even its own temporary ones) until after it has completed all the editing operations, so it will probably perform several strip operations when it&#8217;s done. For the above example, it had to run strip twice. Strip can be slow depending on a variety of factors, so you might need to be a little patient. You can choose to keep the original revisions by passing the <code>&#8211;keep</code> flag. </p>
<p> The <code>edit</code> operation will drop you back to a command prompt, allowing you to edit files freely, or even use <code>hg record</code> to commit some changes as a separate commit. When you&#8217;re done, any remaining uncommitted changes will be committed as well. When done, run <code>hg histedit &#8211;continue</code> to finish this step. You&#8217;ll be prompted for a new commit message, but the default commit message will be the original message for the <code>edit</code> ed revision. </p>
<p> The <code>message</code> operation will give you a chance to revise a commit message without changing the contents. It&#8217;s a shortcut for doing <code>edit</code> immediately followed by <i>hg histedit &#8211;continue`</i>. </p>
<p> If <code>histedit</code> encounters a conflict when moving a revision (while handling <code>pick</code> or <code>fold</code>), it&#8217;ll stop in a similar manner to <code>edit</code> with the difference that it won&#8217;t prompt you for a commit message when done. If you decide at this point that you don&#8217;t like how much work it will be to rearrange history, or that you made a mistake, you can use <code>hg histedit &#8211;abort</code> to abandon the new changes you have made and return to the state before you attempted to edit your history. </p>
<p> If we clone the histedit-ed example repository above and add four more changes, such that we have the following history: </p>
<pre>
@  6[tip]   038383181893   2009-04-27 18:04 -0500   stefan
|    Add theta
|
o  5   140988835471   2009-04-27 18:04 -0500   stefan
|    Add eta
|
o  4   122930637314   2009-04-27 18:04 -0500   stefan
|    Add zeta
|
o  3   836302820282   2009-04-27 18:04 -0500   stefan
|    Add epsilon
|
o  2   989b4d060121   2009-04-27 18:04 -0500   durin42
|    Add beta and delta.
|
o  1   081603921c3f   2009-04-27 18:04 -0500   durin42
|    Add gamma
|
o  0   d8d2fcd0e319   2009-04-27 18:04 -0500   durin42
     Add alpha
</pre>
<p> If you run <code>hg histedit &#8211;outgoing</code> on the clone then it is the same as running <code>hg histedit 836302820282</code>. If you need plan to push to a repository that Mercurial does not detect to be related to the source repo, you can add a <code>&#8211;force</code> option.</p>
<h3>Commands</h3>
<h3>histedit</h3>
<pre>
hg histedit [PARENT]
</pre>
<p> interactively edit changeset history </p>
<p> Options:</p>
<dl>
<dt><code>&#8211;commands</code></p>
<dd> Read history edits from the specified file.</p>
<dt><code>-c, &#8211;continue</code></p>
<dd> continue an edit already in progress</p>
<dt><code>-k, &#8211;keep</code></p>
<dd> don&#8217;t strip old nodes after edit is complete</p>
<dt><code>&#8211;abort</code></p>
<dd> abort an edit in progress</p>
<dt><code>-o, &#8211;outgoing</code></p>
<dd> changesets not found in destination</p>
<dt><code>-f, &#8211;force</code></p>
<dd> force outgoing even for unrelated repositories</p>
<dt><code>-r, &#8211;rev</code></p>
<dd> first revision to be edited</dl>
<h3>inotify</h3>
<p> accelerate status report using Linux&#8217;s inotify service</p>
<h3>Commands</h3>
<h3>inserve</h3>
<pre>
hg inserve [OPTION]...
</pre>
<p> start an inotify server for this repository </p>
<p> Options:</p>
<dl>
<dt><code>-d, &#8211;daemon</code></p>
<dd> run server in background</p>
<dt><code>&#8211;daemon-pipefds</code></p>
<dd> used internally by daemon mode</p>
<dt><code>-t, &#8211;idle-timeout</code></p>
<dd> minutes to sit idle before exiting</p>
<dt><code>&#8211;pid-file</code></p>
<dd> name of file to write process ID to</dl>
<h3>interhg</h3>
<p> None</p>
<h3>keyword</h3>
<p> expand keywords in tracked files </p>
<p> This extension expands RCS/CVS-like or self-customized $Keywords$ in tracked text files selected by your configuration. </p>
<p> Keywords are only expanded in local repositories and not stored in the change history. The mechanism can be regarded as a convenience for the current user or for archive distribution. </p>
<p> Keywords expand to the changeset data pertaining to the latest change relative to the working directory parent of each file. </p>
<p> Configuration is done in the [keyword], [keywordset] and [keywordmaps] sections of hgrc files. </p>
<p> Example: </p>
<p>[keyword]<br />
#expand keywords in every python file except those matching &#8220;x*&#8221;<br />
    **.py =<br />
    x * = ignore<br />
        [keywordset]<br />
#prefer svn &#8211; over cvs &#8211; like default keywordmaps<br />
    svn = True</p>
<dl>
<dt>Note</p>
<dd> The more specific you are in your filename patterns the less you lose speed in huge repositories. </p>
<p> For [keywordmaps] template mapping and expansion demonstration and control run <code>hg kwdemo</code>:. See <code>hg help templates</code>: for a list of available templates and filters. </p>
<p> Three additional date template filters are provided:</p>
<dt><code>utcdate</code></p>
<dd>
<p> &quot;2006/09/18 15:13:13&quot;</p>
<dt><code>svnutcdate</code></p>
<dd>
<p> &quot;2006-09-18 15:13:13Z&quot;</p>
<dt><code>svnisodate</code></p>
<dd>
<p> &quot;2006-09-18 08:13:13 -700 (Mon, 18 Sep 2006)&quot; </p>
<p> The default template mappings (view with <code>hg kwdemo -d</code>:) can be replaced with customized keywords and templates. Again, run <code>hg kwdemo</code>: to control the results of your configuration changes. </p>
<p> Before changing/disabling active keywords, you must run <code>hg kwshrink</code>: to avoid storing expanded keywords in the change history. </p>
<p> To force expansion after enabling it, or a configuration change, run <code>hg kwexpand</code>:. </p>
<p> Expansions spanning more than one line and incremental expansions, like CVS&#8217; $Log$, are not supported. A keyword template map &quot;Log = {desc}&quot; expands to the first line of the changeset description.</dl>
<h3>Commands</h3>
<h3>kwdemo</h3>
<p>hg kwdemo[-d][-f RCFILE][TEMPLATEMAP]&#8230;</p>
<p> Show current, custom, or default keyword template maps and their expansions. </p>
<p> Extend the current configuration by specifying maps as arguments and using -f/&#8211;rcfile to source an external hgrc file. </p>
<p> Use -d/&#8211;default to disable current configuration. </p>
<p> See <code>hg help templates</code>: for information on templates and filters. </p>
<p> Options:</p>
<dl>
<dt><code>-d, &#8211;default</code></p>
<dd> show default keyword template maps</p>
<dt><code>-f, &#8211;rcfile</code></p>
<dd> read maps from rcfile</dl>
<h3>kwexpand</h3>
<p>hg kwexpand[OPTION]&#8230;[FILE]&#8230;</p>
<p> Run after (re)enabling keyword expansion. </p>
<p> kwexpand refuses to run if given files contain local changes. </p>
<p> Options:</p>
<dl>
<dt><code>-I, &#8211;include</code></p>
<dd> include names matching the given patterns</p>
<dt><code>-X, &#8211;exclude</code></p>
<dd> exclude names matching the given patterns</dl>
<h3>kwfiles</h3>
<p>hg kwfiles[OPTION]&#8230;[FILE]&#8230;</p>
<p> List which files in the working directory are matched by the [keyword] configuration patterns. </p>
<p> Useful to prevent inadvertent keyword expansion and to speed up execution by including only files that are actual candidates for expansion. </p>
<p> See <code>hg help keyword</code>: on how to construct patterns both for inclusion and exclusion of files. </p>
<p> With -A/&#8211;all and -v/&#8211;verbose the codes used to show the status of files are: </p>
<pre>
K = keyword expansion candidate
k = keyword expansion candidate (not tracked)
I = ignored
i = ignored (not tracked)
</pre>
<p> Options:</p>
<dl>
<dt><code>-A, &#8211;all</code></p>
<dd> show keyword status flags of all files</p>
<dt><code>-i, &#8211;ignore</code></p>
<dd> show files excluded from expansion</p>
<dt><code>-u, &#8211;unknown</code></p>
<dd> only show unknown (not tracked) files</p>
<dt><code>-I, &#8211;include</code></p>
<dd> include names matching the given patterns</p>
<dt><code>-X, &#8211;exclude</code></p>
<dd> exclude names matching the given patterns</dl>
<h3>kwshrink</h3>
<p>hg kwshrink[OPTION]&#8230;[FILE]&#8230;</p>
<p> Must be run before changing/disabling active keywords. </p>
<p> kwshrink refuses to run if given files contain local changes. </p>
<p> Options:</p>
<dl>
<dt><code>-I, &#8211;include</code></p>
<dd> include names matching the given patterns</p>
<dt><code>-X, &#8211;exclude</code></p>
<dd> exclude names matching the given patterns</dl>
<h3>largefiles</h3>
<p> track large binary files </p>
<p> Large binary files tend to be not very compressible, not very diffable, and not at all mergeable. Such files are not handled efficiently by Mercurial&#8217;s storage format (revlog), which is based on compressed binary deltas; storing large binary files as regular Mercurial files wastes bandwidth and disk space and increases Mercurial&#8217;s memory usage. The largefiles extension addresses these problems by adding a centralized client-server layer on top of Mercurial: largefiles live in a <i>central store</i> out on the network somewhere, and you only fetch the revisions that you need when you need them. </p>
<p> largefiles works by maintaining a &quot;standin file&quot; in .hglf/ for each largefile. The standins are small (41 bytes: an SHA-1 hash plus newline) and are tracked by Mercurial. Largefile revisions are identified by the SHA-1 hash of their contents, which is written to the standin. largefiles uses that revision ID to get/put largefile revisions from/to the central store. This saves both disk space and bandwidth, since you don&#8217;t need to retrieve all historical revisions of large files when you clone or pull. </p>
<p> To start a new repository or add new large binary files, just add &#8211;large to your <code>hg add</code>: command. For example: </p>
<pre>
$ dd if=/dev/urandom of=randomdata count=2000
$ hg add --large randomdata
$ hg commit -m 'add randomdata as a largefile'
</pre>
<p> When you push a changeset that adds/modifies largefiles to a remote repository, its largefile revisions will be uploaded along with it. Note that the remote Mercurial must also have the largefiles extension enabled for this to work. </p>
<p> When you pull a changeset that affects largefiles from a remote repository, the largefiles for the changeset will by default not be pulled down. However, when you update to such a revision, any largefiles needed by that revision are downloaded and cached (if they have never been downloaded before). One way to pull largefiles when pulling is thus to use &#8211;update, which will update your working copy to the latest pulled revision (and thereby downloading any new largefiles). </p>
<p> If you want to pull largefiles you don&#8217;t need for update yet, then you can use pull with the <i>&#8211;lfrev</i> option or the <code>hg lfpull</code>: command. </p>
<p> If you know you are pulling from a non-default location and want to download all the largefiles that correspond to the new changesets at the same time, then you can pull with <i>&#8211;lfrev &quot;pulled()&quot;</i>. </p>
<p> If you just want to ensure that you will have the largefiles needed to merge or rebase with new heads that you are pulling, then you can pull with <i>&#8211;lfrev &quot;head(pulled())&quot;</i> flag to pre-emptively download any largefiles that are new in the heads you are pulling. </p>
<p> Keep in mind that network access may now be required to update to changesets that you have not previously updated to. The nature of the largefiles extension means that updating is no longer guaranteed to be a local-only operation. </p>
<p> If you already have large files tracked by Mercurial without the largefiles extension, you will need to convert your repository in order to benefit from largefiles. This is done with the <code>hg lfconvert</code>: command: </p>
<pre>
$ hg lfconvert --size 10 oldrepo newrepo
</pre>
<p> In repositories that already have largefiles in them, any new file over 10MB will automatically be added as a largefile. To change this threshold, set <code>largefiles.minsize</code> in your Mercurial config file to the minimum size in megabytes to track as a largefile, or use the &#8211;lfsize option to the add command (also in megabytes): </p>
<pre>
[largefiles]
minsize = 2
$ hg add --lfsize 2
</pre>
<p> The <code>largefiles.patterns</code> config option allows you to specify a list of filename patterns (see <code>hg help patterns</code>:) that should always be tracked as largefiles: </p>
<pre>
[largefiles]
patterns =
  *.jpg
  re:.*\.(png|bmp)$
  library.zip
  content/audio/*
</pre>
<p> Files that match one of these patterns will be added as largefiles regardless of their size. </p>
<p> The <code>largefiles.minsize</code> and <code>largefiles.patterns</code> config options will be ignored for any repositories not already containing a largefile. To add the first largefile to a repository, you must explicitly do so with the &#8211;large flag passed to the <code>hg add</code>: command.</p>
<h3>Commands</h3>
<h3>lfconvert</h3>
<pre>
hg lfconvert SOURCE DEST [FILE ...]
</pre>
<p> Convert repository SOURCE to a new repository DEST, identical to SOURCE except that certain files will be converted as largefiles: specifically, any file that matches any PATTERN <i>or</i> whose size is above the minimum size threshold is converted as a largefile. The size used to determine whether or not to track a file as a largefile is the size of the first version of the file. The minimum size can be specified either with &#8211;size or in configuration as <code>largefiles.size</code>. </p>
<p> After running this command you will need to make sure that largefiles is enabled anywhere you intend to push the new repository. </p>
<p> Use &#8211;to-normal to convert largefiles back to normal files; after this, the DEST repository can be used without largefiles at all. </p>
<p> Options:</p>
<dl>
<dt><code>-s, &#8211;size</code></p>
<dd> minimum size (MB) for files to be converted as largefiles</p>
<dt><code>&#8211;to-normal</code></p>
<dd> convert from a largefiles repo to a normal repo</dl>
<h3>lfpull</h3>
<p>hg lfpull &#8211; r REV&#8230;[-e CMD][&#8211;remotecmd CMD][SOURCE]</p>
<p> Pull largefiles that are referenced from local changesets but missing locally, pulling from a remote repository to the local cache. </p>
<p> If SOURCE is omitted, the &#8216;default&#8217; path will be used. See <code>hg help urls</code>: for more information. </p>
<p> Some examples:</p>
<dl>
<dt>&bull;</p>
<dd> pull largefiles for all branch heads: </p>
<pre>
hg lfpull -r &quot;head() and not closed()&quot;
</pre>
<dt>&bull;</p>
<dd> pull largefiles on the default branch: </p>
<pre>
hg lfpull -r &quot;branch(default)&quot;
</pre>
<p> Options:</p>
<dt><code>-r, &#8211;rev</code></p>
<dd> pull largefiles for these revisions</p>
<dt><code>-e, &#8211;ssh</code></p>
<dd> specify ssh command to use</p>
<dt><code>&#8211;remotecmd</code></p>
<dd> specify hg command to run on the remote side</p>
<dt><code>&#8211;insecure</code></p>
<dd> do not verify server certificate (ignoring web.cacerts config)</dl>
<h3>mq</h3>
<p> manage a stack of patches </p>
<p> This extension lets you work with a stack of patches in a Mercurial repository. It manages two stacks of patches &#8211; all known patches, and applied patches (subset of known patches). </p>
<p> Known patches are represented as patch files in the .hg/patches directory. Applied patches are both patch files and changesets. </p>
<p> Common tasks (use <code>hg help command</code>: for more details): </p>
<pre>
create new patch                          qnew
import existing patch                     qimport
print patch series                        qseries
print applied patches                     qapplied
add known patch to applied stack          qpush
remove patch from applied stack           qpop
refresh contents of top applied patch     qrefresh
</pre>
<p> By default, mq will automatically use git patches when required to avoid losing file mode changes, copy records, binary files or empty files creations or deletions. This behaviour can be configured with: </p>
<pre>
[mq]
git = auto/keep/yes/no
</pre>
<p> If set to &#8216;keep&#8217;, mq will obey the [diff] section configuration while preserving existing git patches upon qrefresh. If set to &#8216;yes&#8217; or &#8216;no&#8217;, mq will override the [diff] section and always generate git or regular patches, possibly losing data in the second case. </p>
<p> It may be desirable for mq changesets to be kept in the secret phase (see <code>hg help phases</code>:), which can be enabled with the following setting: </p>
<pre>
[mq]
secret = True
</pre>
<p> You will by default be managing a patch queue named &quot;patches&quot;. You can create other, independent patch queues with the <code>hg qqueue</code>: command. </p>
<p> If the working directory contains uncommitted files, qpush, qpop and qgoto abort immediately. If -f/&#8211;force is used, the changes are discarded. Setting: </p>
<pre>
[mq]
keepchanges = True
</pre>
<p> make them behave as if &#8211;keep-changes were passed, and non-conflicting local changes will be tolerated and preserved. If incompatible options such as -f/&#8211;force or &#8211;exact are passed, this setting is ignored.</p>
<h3>Commands</h3>
<h3>qapplied</h3>
<p>hg qapplied[-1][-s][PATCH]</p>
<p> Returns 0 on success. </p>
<p> Options:</p>
<dl>
<dt><code>-1, &#8211;last</code></p>
<dd> show only the preceding applied patch</p>
<dt><code>-s, &#8211;summary</code></p>
<dd> print first line of patch header</dl>
<h3>qclone</h3>
<p>hg qclone[OPTION]&#8230; SOURCE[DEST]</p>
<p> If source is local, destination will have no patches applied. If source is remote, this command can not check if patches are applied in source, so cannot guarantee that patches are not applied in destination. If you clone remote repository, be sure before that it has no patches applied. </p>
<p> Source patch repository is looked for in &lt;src&gt;/.hg/patches by default. Use -p &lt;url&gt; to change. </p>
<p> The patch directory must be a nested Mercurial repository, as would be created by <code>hg init &#8211;mq</code>:. </p>
<p> Return 0 on success. </p>
<p> Options:</p>
<dl>
<dt><code>&#8211;pull</code></p>
<dd> use pull protocol to copy metadata</p>
<dt><code>-U, &#8211;noupdate</code></p>
<dd> do not update the new working directories</p>
<dt><code>&#8211;uncompressed</code></p>
<dd> use uncompressed transfer (fast over LAN)</p>
<dt><code>-p, &#8211;patches</code></p>
<dd> location of source patch repository</p>
<dt><code>-e, &#8211;ssh</code></p>
<dd> specify ssh command to use</p>
<dt><code>&#8211;remotecmd</code></p>
<dd> specify hg command to run on the remote side</p>
<dt><code>&#8211;insecure</code></p>
<dd> do not verify server certificate (ignoring web.cacerts config)</dl>
<h3>qcommit</h3>
<p>hg qcommit[OPTION]&#8230;[FILE]&#8230;</p>
<p> This command is deprecated; use <code>hg commit &#8211;mq</code>: instead. </p>
<p> Options:</p>
<dl>
<dt><code>-A, &#8211;addremove</code></p>
<dd> mark new/missing files as added/removed before committing</p>
<dt><code>&#8211;close-branch</code></p>
<dd> mark a branch as closed, hiding it from the branch list</p>
<dt><code>&#8211;amend</code></p>
<dd> amend the parent of the working dir</p>
<dt><code>-I, &#8211;include</code></p>
<dd> include names matching the given patterns</p>
<dt><code>-X, &#8211;exclude</code></p>
<dd> exclude names matching the given patterns</p>
<dt><code>-m, &#8211;message</code></p>
<dd> use text as commit message</p>
<dt><code>-l, &#8211;logfile</code></p>
<dd> read commit message from file</p>
<dt><code>-d, &#8211;date</code></p>
<dd> record the specified date as commit date</p>
<dt><code>-u, &#8211;user</code></p>
<dd> record the specified user as committer</p>
<dt><code>-S, &#8211;subrepos</code></p>
<dd> recurse into subrepositories </p>
<p> aliases: qci</dl>
<h3>qdelete</h3>
<p>hg qdelete[-k][PATCH]&#8230;</p>
<p> The patches must not be applied, and at least one patch is required. Exact patch identifiers must be given. With -k/&#8211;keep, the patch files are preserved in the patch directory. </p>
<p> To stop managing a patch and move it into permanent history, use the <code>hg qfinish</code>: command. </p>
<p> Options:</p>
<dl>
<dt><code>-k, &#8211;keep</code></p>
<dd> keep patch file</p>
<dt><code>-r, &#8211;rev</code></p>
<dd> stop managing a revision (DEPRECATED) </p>
<p> aliases: qremove qrm</dl>
<h3>qdiff</h3>
<p>hg qdiff[OPTION]&#8230;[FILE]&#8230;</p>
<p> Shows a diff which includes the current patch as well as any changes which have been made in the working directory since the last refresh (thus showing what the current patch would become after a qrefresh). </p>
<p> Use <code>hg diff</code>: if you only want to see the changes made since the last qrefresh, or <code>hg export qtip</code>: if you want to see changes made by the current patch without including changes made since the qrefresh. </p>
<p> Returns 0 on success. </p>
<p> Options:</p>
<dl>
<dt><code>-a, &#8211;text</code></p>
<dd> treat all files as text</p>
<dt><code>-g, &#8211;git</code></p>
<dd> use git extended diff format</p>
<dt><code>&#8211;nodates</code></p>
<dd> omit dates from diff headers</p>
<dt><code>-p, &#8211;show-function</code></p>
<dd> show which function each change is in</p>
<dt><code>&#8211;reverse</code></p>
<dd> produce a diff that undoes the changes</p>
<dt><code>-w, &#8211;ignore-all-space</code></p>
<dd> ignore white space when comparing lines</p>
<dt><code>-b, &#8211;ignore-space-change</code></p>
<dd> ignore changes in the amount of white space</p>
<dt><code>-B, &#8211;ignore-blank-lines</code></p>
<dd> ignore changes whose lines are all blank</p>
<dt><code>-U, &#8211;unified</code></p>
<dd> number of lines of context to show</p>
<dt><code>&#8211;stat</code></p>
<dd> output diffstat-style summary of changes</p>
<dt><code>-I, &#8211;include</code></p>
<dd> include names matching the given patterns</p>
<dt><code>-X, &#8211;exclude</code></p>
<dd> exclude names matching the given patterns</dl>
<h3>qfinish</h3>
<p>hg qfinish[-a][REV]&#8230;</p>
<p> Finishes the specified revisions (corresponding to applied patches) by moving them out of mq control into regular repository history. </p>
<p> Accepts a revision range or the -a/&#8211;applied option. If &#8211;applied is specified, all applied mq revisions are removed from mq control. Otherwise, the given revisions must be at the base of the stack of applied patches. </p>
<p> This can be especially useful if your changes have been applied to an upstream repository, or if you are about to push your changes to upstream. </p>
<p> Returns 0 on success. </p>
<p> Options:</p>
<dl>
<dt><code>-a, &#8211;applied</code></p>
<dd> finish all applied changesets</dl>
<h3>qfold</h3>
<p>hg qfold[-e][-k][-m TEXT][-l FILE] PATCH&#8230;</p>
<p> Patches must not yet be applied. Each patch will be successively applied to the current patch in the order given. If all the patches apply successfully, the current patch will be refreshed with the new cumulative patch, and the folded patches will be deleted. With -k/&#8211;keep, the folded patch files will not be removed afterwards. </p>
<p> The header for each folded patch will be concatenated with the current patch header, separated by a line of <code>* * *</code>. </p>
<p> Returns 0 on success. </p>
<p> Options:</p>
<dl>
<dt><code>-e, &#8211;edit</code></p>
<dd> edit patch header</p>
<dt><code>-k, &#8211;keep</code></p>
<dd> keep folded patch files</p>
<dt><code>-m, &#8211;message</code></p>
<dd> use text as commit message</p>
<dt><code>-l, &#8211;logfile</code></p>
<dd> read commit message from file</dl>
<h3>qgoto</h3>
<pre>
hg qgoto [OPTION]... PATCH
</pre>
<p> Returns 0 on success. </p>
<p> Options:</p>
<dl>
<dt><code>&#8211;keep-changes</code></p>
<dd> tolerate non-conflicting local changes</p>
<dt><code>-f, &#8211;force</code></p>
<dd> overwrite any local changes</p>
<dt><code>&#8211;no-backup</code></p>
<dd> do not save backup copies of files</dl>
<h3>qguard</h3>
<p>hg qguard[-l][-n][PATCH][&#8211;[+GUARD]&#8230;[-GUARD]&#8230;]</p>
<p> Guards control whether a patch can be pushed. A patch with no guards is always pushed. A patch with a positive guard (&quot;+foo&quot;) is pushed only if the <code>hg qselect</code>: command has activated it. A patch with a negative guard (&quot;-foo&quot;) is never pushed if the <code>hg qselect</code>: command has activated it. </p>
<p> With no arguments, print the currently active guards. With arguments, set guards for the named patch.</p>
<dl>
<dt>Note</p>
<dd> Specifying negative guards now requires &#8216;&#8211;&#8216;. </p>
<p> To set guards on another patch: </p>
<pre>
hg qguard other.patch -- +2.6.17 -stable
</pre>
<p> Returns 0 on success. </p>
<p> Options:</p>
<dt><code>-l, &#8211;list</code></p>
<dd> list all patches and guards</p>
<dt><code>-n, &#8211;none</code></p>
<dd> drop all guards</dl>
<h3>qheader</h3>
<pre>
hg qheader [PATCH]
</pre>
<p> Returns 0 on success.</p>
<h3>qimport</h3>
<p>hg qimport[-e][-n NAME][-f][-g][-P][-r REV]&#8230;[FILE]&#8230;</p>
<p> The patch is inserted into the series after the last applied patch. If no patches have been applied, qimport prepends the patch to the series. </p>
<p> The patch will have the same name as its source file unless you give it a new one with -n/&#8211;name. </p>
<p> You can register an existing patch inside the patch directory with the -e/&#8211;existing flag. </p>
<p> With -f/&#8211;force, an existing patch of the same name will be overwritten. </p>
<p> An existing changeset may be placed under mq control with -r/&#8211;rev (e.g. qimport &#8211;rev tip -n patch will place tip under mq control). With -g/&#8211;git, patches imported with &#8211;rev will use the git diff format. See the diffs help topic for information on why this is important for preserving rename/copy information and permission changes. Use <code>hg qfinish</code>: to remove changesets from mq control. </p>
<p> To import a patch from standard input, pass &#8211; as the patch file. When importing from standard input, a patch name must be specified using the &#8211;name flag. </p>
<p> To import an existing patch while renaming it: </p>
<pre>
hg qimport -e existing-patch -n new-name
</pre>
<p> Returns 0 if import succeeded. </p>
<p> Options:</p>
<dl>
<dt><code>-e, &#8211;existing</code></p>
<dd> import file in patch directory</p>
<dt><code>-n, &#8211;name</code></p>
<dd> name of patch file</p>
<dt><code>-f, &#8211;force</code></p>
<dd> overwrite existing files</p>
<dt><code>-r, &#8211;rev</code></p>
<dd> place existing revisions under mq control</p>
<dt><code>-g, &#8211;git</code></p>
<dd> use git extended diff format</p>
<dt><code>-P, &#8211;push</code></p>
<dd> qpush after importing</dl>
<h3>qinit</h3>
<pre>
hg qinit [-c]
</pre>
<p> The queue repository is unversioned by default. If -c/&#8211;create-repo is specified, qinit will create a separate nested repository for patches (qinit -c may also be run later to convert an unversioned patch repository into a versioned one). You can use qcommit to commit changes to this queue repository. </p>
<p> This command is deprecated. Without -c, it&#8217;s implied by other relevant commands. With -c, use <code>hg init &#8211;mq</code>: instead. </p>
<p> Options:</p>
<dl>
<dt><code>-c, &#8211;create-repo</code></p>
<dd> create queue repository</dl>
<h3>qnew</h3>
<p>hg qnew[-e][-m TEXT][-l FILE] PATCH[FILE]&#8230;</p>
<p> qnew creates a new patch on top of the currently-applied patch (if any). The patch will be initialized with any outstanding changes in the working directory. You may also use -I/&#8211;include, -X/&#8211;exclude, and/or a list of files after the patch name to add only changes to matching files to the new patch, leaving the rest as uncommitted modifications. </p>
<p> -u/&#8211;user and -d/&#8211;date can be used to set the (given) user and date, respectively. -U/&#8211;currentuser and -D/&#8211;currentdate set user to current user and date to current date. </p>
<p> -e/&#8211;edit, -m/&#8211;message or -l/&#8211;logfile set the patch header as well as the commit message. If none is specified, the header is empty and the commit message is &#8216;[mq]: PATCH&#8217;. </p>
<p> Use the -g/&#8211;git option to keep the patch in the git extended diff format. Read the diffs help topic for more information on why this is important for preserving permission changes and copy/rename information. </p>
<p> Returns 0 on successful creation of a new patch. </p>
<p> Options:</p>
<dl>
<dt><code>-e, &#8211;edit</code></p>
<dd> edit commit message</p>
<dt><code>-f, &#8211;force</code></p>
<dd> import uncommitted changes (DEPRECATED)</p>
<dt><code>-g, &#8211;git</code></p>
<dd> use git extended diff format</p>
<dt><code>-U, &#8211;currentuser</code></p>
<dd> add &quot;From: &lt;current user&gt;&quot; to patch</p>
<dt><code>-u, &#8211;user</code></p>
<dd> add &quot;From: &lt;USER&gt;&quot; to patch</p>
<dt><code>-D, &#8211;currentdate</code></p>
<dd> add &quot;Date: &lt;current date&gt;&quot; to patch</p>
<dt><code>-d, &#8211;date</code></p>
<dd> add &quot;Date: &lt;DATE&gt;&quot; to patch</p>
<dt><code>-I, &#8211;include</code></p>
<dd> include names matching the given patterns</p>
<dt><code>-X, &#8211;exclude</code></p>
<dd> exclude names matching the given patterns</p>
<dt><code>-m, &#8211;message</code></p>
<dd> use text as commit message</p>
<dt><code>-l, &#8211;logfile</code></p>
<dd> read commit message from file</dl>
<h3>qnext</h3>
<pre>
hg qnext [-s]
</pre>
<p> Returns 0 on success. </p>
<p> Options:</p>
<dl>
<dt><code>-s, &#8211;summary</code></p>
<dd> print first line of patch header</dl>
<h3>qpop</h3>
<p>hg qpop[-a][-f][PATCH | INDEX]</p>
<p> Without argument, pops off the top of the patch stack. If given a patch name, keeps popping off patches until the named patch is at the top of the stack. </p>
<p> By default, abort if the working directory contains uncommitted changes. With &#8211;keep-changes, abort only if the uncommitted files overlap with patched files. With -f/&#8211;force, backup and discard changes made to such files. </p>
<p> Return 0 on success. </p>
<p> Options:</p>
<dl>
<dt><code>-a, &#8211;all</code></p>
<dd> pop all patches</p>
<dt><code>-n, &#8211;name</code></p>
<dd> queue name to pop (DEPRECATED)</p>
<dt><code>&#8211;keep-changes</code></p>
<dd> tolerate non-conflicting local changes</p>
<dt><code>-f, &#8211;force</code></p>
<dd> forget any local changes to patched files</p>
<dt><code>&#8211;no-backup</code></p>
<dd> do not save backup copies of files</dl>
<h3>qprev</h3>
<pre>
hg qprev [-s]
</pre>
<p> Returns 0 on success. </p>
<p> Options:</p>
<dl>
<dt><code>-s, &#8211;summary</code></p>
<dd> print first line of patch header</dl>
<h3>qpush</h3>
<p>hg qpush[-f][-l][-a][&#8211;move][PATCH | INDEX]</p>
<p> By default, abort if the working directory contains uncommitted changes. With &#8211;keep-changes, abort only if the uncommitted files overlap with patched files. With -f/&#8211;force, backup and patch over uncommitted changes. </p>
<p> Return 0 on success. </p>
<p> Options:</p>
<dl>
<dt><code>&#8211;keep-changes</code></p>
<dd> tolerate non-conflicting local changes</p>
<dt><code>-f, &#8211;force</code></p>
<dd> apply on top of local changes</p>
<dt><code>-e, &#8211;exact</code></p>
<dd> apply the target patch to its recorded parent</p>
<dt><code>-l, &#8211;list</code></p>
<dd> list patch name in commit text</p>
<dt><code>-a, &#8211;all</code></p>
<dd> apply all patches</p>
<dt><code>-m, &#8211;merge</code></p>
<dd> merge from another queue (DEPRECATED)</p>
<dt><code>-n, &#8211;name</code></p>
<dd> merge queue name (DEPRECATED)</p>
<dt><code>&#8211;move</code></p>
<dd> reorder patch series and apply only the patch</p>
<dt><code>&#8211;no-backup</code></p>
<dd> do not save backup copies of files</dl>
<h3>qqueue</h3>
<p>hg qqueue[OPTION][QUEUE]</p>
<p> Supports switching between different patch queues, as well as creating new patch queues and deleting existing ones. </p>
<p> Omitting a queue name or specifying -l/&#8211;list will show you the registered queues &#8211; by default the &quot;normal&quot; patches queue is registered. The currently active queue will be marked with &quot;(active)&quot;. Specifying &#8211;active will print only the name of the active queue. </p>
<p> To create a new queue, use -c/&#8211;create. The queue is automatically made active, except in the case where there are applied patches from the currently active queue in the repository. Then the queue will only be created and switching will fail. </p>
<p> To delete an existing queue, use &#8211;delete. You cannot delete the currently active queue. </p>
<p> Returns 0 on success. </p>
<p> Options:</p>
<dl>
<dt><code>-l, &#8211;list</code></p>
<dd> list all available queues</p>
<dt><code>&#8211;active</code></p>
<dd> print name of active queue</p>
<dt><code>-c, &#8211;create</code></p>
<dd> create new queue</p>
<dt><code>&#8211;rename</code></p>
<dd> rename active queue</p>
<dt><code>&#8211;delete</code></p>
<dd> delete reference to queue</p>
<dt><code>&#8211;purge</code></p>
<dd> delete queue, and remove patch dir</dl>
<h3>qrefresh</h3>
<p>hg qrefresh[-I][-X][-e][-m TEXT][-l FILE][-s][FILE]&#8230;</p>
<p> If any file patterns are provided, the refreshed patch will contain only the modifications that match those patterns; the remaining modifications will remain in the working directory. </p>
<p> If -s/&#8211;short is specified, files currently included in the patch will be refreshed just like matched files and remain in the patch. </p>
<p> If -e/&#8211;edit is specified, Mercurial will start your configured editor for you to enter a message. In case qrefresh fails, you will find a backup of your message in <code>.hg/last-message.txt</code>. </p>
<p> hg add/remove/copy/rename work as usual, though you might want to use git-style patches (-g/&#8211;git or [diff] git=1) to track copies and renames. See the diffs help topic for more information on the git diff format. </p>
<p> Returns 0 on success. </p>
<p> Options:</p>
<dl>
<dt><code>-e, &#8211;edit</code></p>
<dd> edit commit message</p>
<dt><code>-g, &#8211;git</code></p>
<dd> use git extended diff format</p>
<dt><code>-s, &#8211;short</code></p>
<dd> refresh only files already in the patch and specified files</p>
<dt><code>-U, &#8211;currentuser</code></p>
<dd> add/update author field in patch with current user</p>
<dt><code>-u, &#8211;user</code></p>
<dd> add/update author field in patch with given user</p>
<dt><code>-D, &#8211;currentdate</code></p>
<dd> add/update date field in patch with current date</p>
<dt><code>-d, &#8211;date</code></p>
<dd> add/update date field in patch with given date</p>
<dt><code>-I, &#8211;include</code></p>
<dd> include names matching the given patterns</p>
<dt><code>-X, &#8211;exclude</code></p>
<dd> exclude names matching the given patterns</p>
<dt><code>-m, &#8211;message</code></p>
<dd> use text as commit message</p>
<dt><code>-l, &#8211;logfile</code></p>
<dd> read commit message from file</dl>
<h3>qrename</h3>
<pre>
hg qrename PATCH1 [PATCH2]
</pre>
<p> With one argument, renames the current patch to PATCH1. With two arguments, renames PATCH1 to PATCH2. </p>
<p> Returns 0 on success. </p>
<p> aliases: qmv</p>
<h3>qrestore</h3>
<p>hg qrestore[-d][-u] REV</p>
<p> This command is deprecated, use <code>hg rebase</code>: instead. </p>
<p> Options:</p>
<dl>
<dt><code>-d, &#8211;delete</code></p>
<dd> delete save entry</p>
<dt><code>-u, &#8211;update</code></p>
<dd> update queue working directory</dl>
<h3>qsave</h3>
<p>hg qsave[-m TEXT][-l FILE][-c][-n NAME][-e][-f]</p>
<p> This command is deprecated, use <code>hg rebase</code>: instead. </p>
<p> Options:</p>
<dl>
<dt><code>-c, &#8211;copy</code></p>
<dd> copy patch directory</p>
<dt><code>-n, &#8211;name</code></p>
<dd> copy directory name</p>
<dt><code>-e, &#8211;empty</code></p>
<dd> clear queue status file</p>
<dt><code>-f, &#8211;force</code></p>
<dd> force copy</p>
<dt><code>-m, &#8211;message</code></p>
<dd> use text as commit message</p>
<dt><code>-l, &#8211;logfile</code></p>
<dd> read commit message from file</dl>
<h3>qselect</h3>
<p>hg qselect[OPTION]&#8230;[GUARD]&#8230;</p>
<p> Use the <code>hg qguard</code>: command to set or print guards on patch, then use qselect to tell mq which guards to use. A patch will be pushed if it has no guards or any positive guards match the currently selected guard, but will not be pushed if any negative guards match the current guard. For example: </p>
<pre>
qguard foo.patch -- -stable    (negative guard)
qguard bar.patch    +stable    (positive guard)
qselect stable
</pre>
<p> This activates the &quot;stable&quot; guard. mq will skip foo.patch (because it has a negative match) but push bar.patch (because it has a positive match). </p>
<p> With no arguments, prints the currently active guards. With one argument, sets the active guard. </p>
<p> Use -n/&#8211;none to deactivate guards (no other arguments needed). When no guards are active, patches with positive guards are skipped and patches with negative guards are pushed. </p>
<p> qselect can change the guards on applied patches. It does not pop guarded patches by default. Use &#8211;pop to pop back to the last applied patch that is not guarded. Use &#8211;reapply (which implies &#8211;pop) to push back to the current patch afterwards, but skip guarded patches. </p>
<p> Use -s/&#8211;series to print a list of all guards in the series file (no other arguments needed). Use -v for more information. </p>
<p> Returns 0 on success. </p>
<p> Options:</p>
<dl>
<dt><code>-n, &#8211;none</code></p>
<dd> disable all guards</p>
<dt><code>-s, &#8211;series</code></p>
<dd> list all guards in series file</p>
<dt><code>&#8211;pop</code></p>
<dd> pop to before first guarded applied patch</p>
<dt><code>&#8211;reapply</code></p>
<dd> pop, then reapply patches</dl>
<h3>qseries</h3>
<pre>
hg qseries [-ms]
</pre>
<p> Returns 0 on success. </p>
<p> Options:</p>
<dl>
<dt><code>-m, &#8211;missing</code></p>
<dd> print patches not in series</p>
<dt><code>-s, &#8211;summary</code></p>
<dd> print first line of patch header</dl>
<h3>qtop</h3>
<pre>
hg qtop [-s]
</pre>
<p> Returns 0 on success. </p>
<p> Options:</p>
<dl>
<dt><code>-s, &#8211;summary</code></p>
<dd> print first line of patch header</dl>
<h3>qunapplied</h3>
<p>hg qunapplied[-1][-s][PATCH]</p>
<p> Returns 0 on success. </p>
<p> Options:</p>
<dl>
<dt><code>-1, &#8211;first</code></p>
<dd> show only the first patch</p>
<dt><code>-s, &#8211;summary</code></p>
<dd> print first line of patch header</dl>
<h3>strip</h3>
<p>hg strip[-k][-f][-n][-B bookmark][-r] REV&#8230;</p>
<p> The strip command removes the specified changesets and all their descendants. If the working directory has uncommitted changes, the operation is aborted unless the &#8211;force flag is supplied, in which case changes will be discarded. </p>
<p> If a parent of the working directory is stripped, then the working directory will automatically be updated to the most recent available ancestor of the stripped parent after the operation completes. </p>
<p> Any stripped changesets are stored in <code>.hg/strip-backup</code> as a bundle (see <code>hg help bundle</code>: and <code>hg help unbundle</code>:). They can be restored by running <code>hg unbundle .hg/strip-backup/BUNDLE</code>:, where BUNDLE is the bundle file created by the strip. Note that the local revision numbers will in general be different after the restore. </p>
<p> Use the &#8211;no-backup option to discard the backup bundle once the operation completes. </p>
<p> Strip is not a history-rewriting operation and can be used on changesets in the public phase. But if the stripped changesets have been pushed to a remote repository you will likely pull them again. </p>
<p> Return 0 on success. </p>
<p> Options:</p>
<dl>
<dt><code>-r, &#8211;rev</code></p>
<dd> strip specified revision (optional, can specify revisions without this option)</p>
<dt><code>-f, &#8211;force</code></p>
<dd> force removal of changesets, discard uncommitted changes (no backup)</p>
<dt><code>-b, &#8211;backup</code></p>
<dd> bundle only changesets with local revision number greater than REV which are not descendants of REV (DEPRECATED)</p>
<dt><code>&#8211;no-backup</code></p>
<dd> no backups</p>
<dt><code>&#8211;nobackup</code></p>
<dd> no backups (DEPRECATED)</p>
<dt><code>-n</code></p>
<dd> ignored (DEPRECATED)</p>
<dt><code>-k, &#8211;keep</code></p>
<dd> do not modify working copy during strip</p>
<dt><code>-B, &#8211;bookmark</code></p>
<dd> remove revs only reachable from given bookmark</dl>
<h3>notify</h3>
<p> hooks for sending email push notifications </p>
<p> This extension implements hooks to send email notifications when changesets are sent from or received by the local repository. </p>
<p> First, enable the extension as explained in <code>hg help extensions</code>:, and register the hook you want to run. <code>incoming</code> and <code>changegroup</code> hooks are run when changesets are received, while <code>outgoing</code> hooks are for changesets sent to another repository: </p>
<p>[hooks]<br />
#one email for each incoming changeset<br />
    incoming.notify = python : hgext.notify.hook<br />
#one email for all incoming changesets<br />
                                   changegroup.notify = python : hgext.notify.hook<br />
#one email for all outgoing changesets<br />
                                                                     outgoing.notify = python : hgext.notify.hook</p>
<p> This registers the hooks. To enable notification, subscribers must be assigned to repositories. The <code>[usersubs]</code> section maps multiple repositories to a given recipient. The <code>[reposubs]</code> section maps multiple recipients to a single repository: </p>
<p>[usersubs]<br />
#key is subscriber email, value is a comma &#8211; separated list of repo patterns<br />
    user[at] host = pattern<br />
        [reposubs]<br />
#key is repo pattern, value is a comma &#8211; separated list of subscriber emails<br />
    pattern = user[at] host</p>
<p> A <code>pattern</code> is a <code>glob</code> matching the absolute path to a repository, optionally combined with a revset expression. A revset expression, if present, is separated from the glob by a hash. Example: </p>
<p>[reposubs] * / widgets #branch(release) = qa &#8211; team[at] example.com</p>
<p> This sends to <code>qa-team [at] example.com</code> whenever a changeset on the <code>release</code> branch triggers a notification in any repository ending in <code>widgets</code>. </p>
<p> In order to place them under direct user management, <code>[usersubs]</code> and <code>[reposubs]</code> sections may be placed in a separate <code>hgrc</code> file and incorporated by reference: </p>
<pre>
[notify]
config = /path/to/subscriptionsfile
</pre>
<p> Notifications will not be sent until the <code>notify.test</code> value is set to <code>False</code>; see below. </p>
<p> Notifications content can be tweaked with the following configuration entries:</p>
<dl>
<dt><code>notify.test</code></p>
<dd> If <code>True</code>, print messages to stdout instead of sending them. Default: True.</p>
<dt><code>notify.sources</code></p>
<dd> Space-separated list of change sources. Notifications are activated only when a changeset&#8217;s source is in this list. Sources may be:</p>
<dt><code>serve</code></p>
<dd>
<p> changesets received via http or ssh</p>
<dt><code>pull</code></p>
<dd>
<p> changesets received via <code>hg pull</code></p>
<dt><code>unbundle</code></p>
<dd>
<p> changesets received via <code>hg unbundle</code></p>
<dt><code>push</code></p>
<dd>
<p> changesets sent or received via <code>hg push</code></p>
<dt><code>bundle</code></p>
<dd>
<p> changesets sent via <code>hg unbundle</code> </p>
<p> Default: serve.</p>
<dt><code>notify.strip</code></p>
<dd> Number of leading slashes to strip from url paths. By default, notifications reference repositories with their absolute path. <code>notify.strip</code> lets you turn them into relative paths. For example, <code>notify.strip=3</code> will change <code>/long/path/repository</code> into <code>repository</code>. Default: 0.</p>
<dt><code>notify.domain</code></p>
<dd> Default email domain for sender or recipients with no explicit domain.</p>
<dt><code>notify.style</code></p>
<dd> Style file to use when formatting emails.</p>
<dt><code>notify.template</code></p>
<dd> Template to use when formatting emails.</p>
<dt><code>notify.incoming</code></p>
<dd> Template to use when run as an incoming hook, overriding <code>notify.template</code>.</p>
<dt><code>notify.outgoing</code></p>
<dd> Template to use when run as an outgoing hook, overriding <code>notify.template</code>.</p>
<dt><code>notify.changegroup</code></p>
<dd> Template to use when running as a changegroup hook, overriding <code>notify.template</code>.</p>
<dt><code>notify.maxdiff</code></p>
<dd> Maximum number of diff lines to include in notification email. Set to 0 to disable the diff, or -1 to include all of it. Default: 300.</p>
<dt><code>notify.maxsubject</code></p>
<dd> Maximum number of characters in email&#8217;s subject line. Default: 67.</p>
<dt><code>notify.diffstat</code></p>
<dd> Set to True to include a diffstat before diff content. Default: True.</p>
<dt><code>notify.merge</code></p>
<dd> If True, send notifications for merge changesets. Default: True.</p>
<dt><code>notify.mbox</code></p>
<dd> If set, append mails to this mbox file instead of sending. Default: None.</p>
<dt><code>notify.fromauthor</code></p>
<dd> If set, use the committer of the first changeset in a changegroup for the &quot;From&quot; field of the notification mail. If not set, take the user from the pushing repo. Default: False. </p>
<p> If set, the following entries will also be used to customize the notifications:</p>
<dt><code>email.from</code></p>
<dd> Email <code>From</code> address to use if none can be found in the generated email content.</p>
<dt><code>web.baseurl</code></p>
<dd> Root repository URL to combine with repository paths when making references. See also <code>notify.strip</code>.</dl>
<h3>pager</h3>
<p> browse command output with an external pager </p>
<p> To set the pager that should be used, set the application variable: </p>
<pre>
[pager]
pager = less -FRX
</pre>
<p> If no pager is set, the pager extensions uses the environment variable $PAGER. If neither pager.pager, nor $PAGER is set, no pager is used. </p>
<p> You can disable the pager for certain commands by adding them to the pager.ignore list: </p>
<pre>
[pager]
ignore = version, help, update
</pre>
<p> You can also enable the pager only for certain commands using pager.attend. Below is the default list of commands to be paged: </p>
<pre>
[pager]
attend = annotate, cat, diff, export, glog, log, qdiff
</pre>
<p> Setting pager.attend to an empty value will cause all commands to be paged. </p>
<p> If pager.attend is present, pager.ignore will be ignored. </p>
<p> To ignore global commands like <code>hg version</code>: or <code>hg help</code>:, you have to specify them in your user configuration file. </p>
<p> The &#8211;pager=&#8230; option can also be used to control when the pager is used. Use a boolean value like yes, no, on, off, or use auto for normal behavior.</p>
<h3>patchbomb</h3>
<p> command to send changesets as (a series of) patch emails </p>
<p> The series is started off with a &quot;[PATCH 0 of N]&quot; introduction, which describes the series as a whole. </p>
<p> Each patch email has a Subject line of &quot;[PATCH M of N] &#8230;&quot;, using the first line of the changeset description as the subject text. The message contains two or three body parts:</p>
<dl>
<dt>&bull;</p>
<dd> The changeset description.</p>
<dt>&bull;</p>
<dd> [Optional] The result of running diffstat on the patch.</p>
<dt>&bull;</p>
<dd> The patch itself, as generated by <code>hg export</code>:. </p>
<p> Each message refers to the first in the series using the In-Reply-To and References headers, so they will show up as a sequence in threaded mail and news readers, and in mail archives. </p>
<p> To configure other defaults, add a section like this to your configuration file: </p>
<p>[email] from = My Name&lt;my[at] email&gt;<br />
    to = recipient1,<br />
        recipient2, &#8230; cc = cc1, cc2, &#8230; bcc = bcc1, bcc2, &#8230; reply &#8211; to = address1, address2, &#8230;</p>
<p> Use <code>[patchbomb]</code> as configuration section name if you need to override global <code>[email]</code> address settings. </p>
<p> Then you can use the <code>hg email</code>: command to mail a series of changesets as a patchbomb. </p>
<p> You can also either configure the method option in the email section to be a sendmail compatible mailer or fill out the [smtp] section so that the patchbomb extension can automatically send patchbombs directly from the commandline. See the [email] and [smtp] sections in <a href="/docs/linux/man/5-hgrc/">hgrc</a>(5) for details.</dl>
<h3>Commands</h3>
<h3>email</h3>
<p>hg email[OPTION]&#8230;[DEST]&#8230;</p>
<p> By default, diffs are sent in the format generated by <code>hg export</code>:, one per message. The series starts with a &quot;[PATCH 0 of N]&quot; introduction, which describes the series as a whole. </p>
<p> Each patch email has a Subject line of &quot;[PATCH M of N] &#8230;&quot;, using the first line of the changeset description as the subject text. The message contains two or three parts. First, the changeset description. </p>
<p> With the -d/&#8211;diffstat option, if the diffstat program is installed, the result of running diffstat on the patch is inserted. </p>
<p> Finally, the patch itself, as generated by <code>hg export</code>:. </p>
<p> With the -d/&#8211;diffstat or &#8211;confirm options, you will be presented with a final summary of all messages and asked for confirmation before the messages are sent. </p>
<p> By default the patch is included as text in the email body for easy reviewing. Using the -a/&#8211;attach option will instead create an attachment for the patch. With -i/&#8211;inline an inline attachment will be created. You can include a patch both as text in the email body and as a regular or an inline attachment by combining the -a/&#8211;attach or -i/&#8211;inline with the &#8211;body option. </p>
<p> With -o/&#8211;outgoing, emails will be generated for patches not found in the destination repository (or only those which are ancestors of the specified revisions if any are provided) </p>
<p> With -b/&#8211;bundle, changesets are selected as for &#8211;outgoing, but a single email containing a binary Mercurial bundle as an attachment will be sent. </p>
<p> With -m/&#8211;mbox, instead of previewing each patchbomb message in a pager or sending the messages directly, it will create a UNIX mailbox file with the patch emails. This mailbox file can be previewed with any mail user agent which supports UNIX mbox files. </p>
<p> With -n/&#8211;test, all steps will run, but mail will not be sent. You will be prompted for an email recipient address, a subject and an introductory message describing the patches of your patchbomb. Then when all is done, patchbomb messages are displayed. If the PAGER environment variable is set, your pager will be fired up once for each patchbomb message, so you can verify everything is alright. </p>
<p> In case email sending fails, you will find a backup of your series introductory message in <code>.hg/last-email.txt</code>. </p>
<p> Examples: </p>
<pre>
hg email -r 3000          # send patch 3000 only
hg email -r 3000 -r 3001  # send patches 3000 and 3001
hg email -r 3000:3005     # send patches 3000 through 3005
hg email 3000             # send patch 3000 (deprecated)
hg email -o               # send all patches not in default
hg email -o DEST          # send all patches not in DEST
hg email -o -r 3000       # send all ancestors of 3000 not in default
hg email -o -r 3000 DEST  # send all ancestors of 3000 not in DEST
hg email -b               # send bundle of all patches not in default
hg email -b DEST          # send bundle of all patches not in DEST
hg email -b -r 3000       # bundle of all ancestors of 3000 not in default
hg email -b -r 3000 DEST  # bundle of all ancestors of 3000 not in DEST
hg email -o -m mbox &amp;&amp;    # generate an mbox file...
  mutt -R -f mbox         # ... and view it with mutt
hg email -o -m mbox &amp;&amp;    # generate an mbox file ...
  formail -s sendmail \   # ... and use formail to send from the mbox
    -bm -t &lt; mbox         # ... using sendmail
</pre>
<p> Before using this command, you will need to enable email in your hgrc. See the [email] section in <a href="/docs/linux/man/5-hgrc/">hgrc</a>(5) for details. </p>
<p> Options:</p>
<dl>
<dt><code>-g, &#8211;git</code></p>
<dd> use git extended diff format</p>
<dt><code>&#8211;plain</code></p>
<dd> omit hg patch header</p>
<dt><code>-o, &#8211;outgoing</code></p>
<dd> send changes not found in the target repository</p>
<dt><code>-b, &#8211;bundle</code></p>
<dd> send changes not in target as a binary bundle</p>
<dt><code>&#8211;bundlename</code></p>
<dd> name of the bundle attachment file (default: bundle)</p>
<dt><code>-r, &#8211;rev</code></p>
<dd> a revision to send</p>
<dt><code>&#8211;force</code></p>
<dd> run even when remote repository is unrelated (with -b/&#8211;bundle)</p>
<dt><code>&#8211;base</code></p>
<dd> a base changeset to specify instead of a destination (with -b/&#8211;bundle)</p>
<dt><code>&#8211;intro</code></p>
<dd> send an introduction email for a single patch</p>
<dt><code>&#8211;body</code></p>
<dd> send patches as inline message text (default)</p>
<dt><code>-a, &#8211;attach</code></p>
<dd> send patches as attachments</p>
<dt><code>-i, &#8211;inline</code></p>
<dd> send patches as inline attachments</p>
<dt><code>&#8211;bcc</code></p>
<dd> email addresses of blind carbon copy recipients</p>
<dt><code>-c, &#8211;cc</code></p>
<dd> email addresses of copy recipients</p>
<dt><code>&#8211;confirm</code></p>
<dd> ask for confirmation before sending</p>
<dt><code>-d, &#8211;diffstat</code></p>
<dd> add diffstat output to messages</p>
<dt><code>&#8211;date</code></p>
<dd> use the given date as the sending date</p>
<dt><code>&#8211;desc</code></p>
<dd> use the given file as the series description</p>
<dt><code>-f, &#8211;from</code></p>
<dd> email address of sender</p>
<dt><code>-n, &#8211;test</code></p>
<dd> print messages that would be sent</p>
<dt><code>-m, &#8211;mbox</code></p>
<dd> write messages to mbox file instead of sending them</p>
<dt><code>&#8211;reply-to</code></p>
<dd> email addresses replies should be sent to</p>
<dt><code>-s, &#8211;subject</code></p>
<dd> subject of first message (intro or single patch)</p>
<dt><code>&#8211;in-reply-to</code></p>
<dd> message identifier to reply to</p>
<dt><code>&#8211;flag</code></p>
<dd> flags to add in subject prefixes</p>
<dt><code>-t, &#8211;to</code></p>
<dd> email addresses of recipients</p>
<dt><code>-e, &#8211;ssh</code></p>
<dd> specify ssh command to use</p>
<dt><code>&#8211;remotecmd</code></p>
<dd> specify hg command to run on the remote side</p>
<dt><code>&#8211;insecure</code></p>
<dd> do not verify server certificate (ignoring web.cacerts config)</dl>
<h3>progress</h3>
<p> show progress bars for some actions </p>
<p> This extension uses the progress information logged by hg commands to draw progress bars that are as informative as possible. Some progress bars only offer indeterminate information, while others have a definite end point. </p>
<p> The following settings are available: </p>
<p>[progress] delay = 3 #number of seconds(float) before showing the progress bar<br />
    changedelay = 1 #changedelay : minimum delay before showing a new topic.<br />
#If set to less than 3 * refresh, that value will<br />
#be used instead.<br />
                                   refresh = 0.1 #time in seconds between refreshes of the progress bar<br />
        format = topic bar number estimate #format of the progress bar<br />
            width = &lt;none&gt; #if set,<br />
           the maximum width of the progress information<br />
#(that is, min(width, term width) will be used)<br />
                   clear &#8211;<br />
               complete = True #clear the progress bar after it&#8217;s done disable = False #if true,<br />
           don&#8217;t show a progress bar assume &#8211; tty = False #if true, ALWAYS show a progress bar, unless<br />
#disable is given</p>
<p> Valid entries for the format field are topic, bar, number, unit, estimate, speed, and item. item defaults to the last 20 characters of the item, but this can be changed by adding either <code>-&lt;num&gt;</code> which would take the last num characters, or <code>+&lt;num&gt;</code> for the first num characters.</p>
<h3>purge</h3>
<p> command to delete untracked files from the working directory</p>
<h3>Commands</h3>
<h3>purge</h3>
<p>hg purge[OPTION]&#8230;[DIR]&#8230;</p>
<p> Delete files not known to Mercurial. This is useful to test local and uncommitted changes in an otherwise-clean source tree. </p>
<p> This means that purge will delete:</p>
<dl>
<dt>&bull;</p>
<dd> Unknown files: files marked with &quot;?&quot; by <code>hg status</code>:</p>
<dt>&bull;</p>
<dd> Empty directories: in fact Mercurial ignores directories unless they contain files under source control management </p>
<p> But it will leave untouched:</p>
<dt>&bull;</p>
<dd> Modified and unmodified tracked files</p>
<dt>&bull;</p>
<dd> Ignored files (unless &#8211;all is specified)</p>
<dt>&bull;</p>
<dd> New files added to the repository (with <code>hg add</code>:) </p>
<p> If directories are given on the command line, only files in these directories are considered. </p>
<p> Be careful with purge, as you could irreversibly delete some files you forgot to add to the repository. If you only want to print the list of files that this program would delete, use the &#8211;print option. </p>
<p> Options:</p>
<dt><code>-a, &#8211;abort-on-err</code></p>
<dd> abort if an error occurs</p>
<dt><code>&#8211;all</code></p>
<dd> purge ignored files too</p>
<dt><code>-p, &#8211;print</code></p>
<dd> print filenames instead of deleting them</p>
<dt><code>-0, &#8211;print0</code></p>
<dd> end filenames with NUL, for use with xargs (implies -p/&#8211;print)</p>
<dt><code>-I, &#8211;include</code></p>
<dd> include names matching the given patterns</p>
<dt><code>-X, &#8211;exclude</code></p>
<dd> exclude names matching the given patterns </p>
<p> aliases: clean</dl>
<h3>rebase</h3>
<p> command to move sets of revisions to a different ancestor </p>
<p> This extension lets you rebase changesets in an existing Mercurial repository. </p>
<p> For more information: <a rel="nofollow" href="http://mercurial.selenic.com/wiki/RebaseExtension:">http://mercurial.selenic.com/wiki/RebaseExtension:</a></p>
<h3>Commands</h3>
<h3>rebase</h3>
<p>hg rebase[-s REV | -b REV][-d REV][OPTION]</p>
<p> Rebase uses repeated merging to graft changesets from one part of history (the source) onto another (the destination). This can be useful for linearizing <i>local</i> changes relative to a master development tree. </p>
<p> You should not rebase changesets that have already been shared with others. Doing so will force everybody else to perform the same rebase or they will end up with duplicated changesets after pulling in your rebased changesets. </p>
<p> In its default configuration, Mercurial will prevent you from rebasing published changes. See <code>hg help phases</code>: for details. </p>
<p> If you don&#8217;t specify a destination changeset (<code>-d/&#8211;dest</code>), rebase uses the tipmost head of the current named branch as the destination. (The destination changeset is not modified by rebasing, but new changesets are added as its descendants.) </p>
<p> You can specify which changesets to rebase in two ways: as a &quot;source&quot; changeset or as a &quot;base&quot; changeset. Both are shorthand for a topologically related set of changesets (the &quot;source branch&quot;). If you specify source (<code>-s/&#8211;source</code>), rebase will rebase that changeset and all of its descendants onto dest. If you specify base (<code>-b/&#8211;base</code>), rebase will select ancestors of base back to but not including the common ancestor with dest. Thus, <code>-b</code> is less precise but more convenient than <code>-s</code>: you can specify any changeset in the source branch, and rebase will select the whole branch. If you specify neither <code>-s</code> nor <code>-b</code>, rebase uses the parent of the working directory as the base. </p>
<p> For advanced usage, a third way is available through the <code>&#8211;rev</code> option. It allows you to specify an arbitrary set of changesets to rebase. Descendants of revs you specify with this option are not automatically included in the rebase. </p>
<p> By default, rebase recreates the changesets in the source branch as descendants of dest and then destroys the originals. Use <code>&#8211;keep</code> to preserve the original source changesets. Some changesets in the source branch (e.g. merges from the destination branch) may be dropped if they no longer contribute any change. </p>
<p> One result of the rules for selecting the destination changeset and source branch is that, unlike <code>merge</code>, rebase will do nothing if you are at the latest (tipmost) head of a named branch with two heads. You need to explicitly specify source and/or destination (or <code>update</code> to the other head, if it&#8217;s the head of the intended source branch). </p>
<p> If a rebase is interrupted to manually resolve a merge, it can be continued with &#8211;continue/-c or aborted with &#8211;abort/-a. </p>
<p> Returns 0 on success, 1 if nothing to rebase. </p>
<p> Options:</p>
<dl>
<dt><code>-s, &#8211;source</code></p>
<dd> rebase from the specified changeset</p>
<dt><code>-b, &#8211;base</code></p>
<dd> rebase from the base of the specified changeset (up to greatest common ancestor of base and dest)</p>
<dt><code>-r, &#8211;rev</code></p>
<dd> rebase these revisions</p>
<dt><code>-d, &#8211;dest</code></p>
<dd> rebase onto the specified changeset</p>
<dt><code>&#8211;collapse</code></p>
<dd> collapse the rebased changesets</p>
<dt><code>-m, &#8211;message</code></p>
<dd> use text as collapse commit message</p>
<dt><code>-e, &#8211;edit</code></p>
<dd> invoke editor on commit messages</p>
<dt><code>-l, &#8211;logfile</code></p>
<dd> read collapse commit message from file</p>
<dt><code>&#8211;keep</code></p>
<dd> keep original changesets</p>
<dt><code>&#8211;keepbranches</code></p>
<dd> keep original branch names</p>
<dt><code>-D, &#8211;detach</code></p>
<dd> (DEPRECATED)</p>
<dt><code>-t, &#8211;tool</code></p>
<dd> specify merge tool</p>
<dt><code>-c, &#8211;continue</code></p>
<dd> continue an interrupted rebase</p>
<dt><code>-a, &#8211;abort</code></p>
<dd> abort an interrupted rebase</p>
<dt><code>&#8211;style</code></p>
<dd> display using template map file</p>
<dt><code>&#8211;template</code></p>
<dd> display with template</dl>
<h3>record</h3>
<p> commands to interactively select changes for commit/qrefresh</p>
<h3>Commands</h3>
<h3>qrecord</h3>
<p>hg qrecord[OPTION]&#8230; PATCH[FILE]&#8230;</p>
<p> See <code>hg help qnew</code>: &amp; <code>hg help record</code>: for more information and usage.</p>
<h3>record</h3>
<p>hg record[OPTION]&#8230;[FILE]&#8230;</p>
<p> If a list of files is omitted, all changes reported by <code>hg status</code>: will be candidates for recording. </p>
<p> See <code>hg help dates</code>: for a list of formats valid for -d/&#8211;date. </p>
<p> You will be prompted for whether to record changes to each modified file, and for files with multiple changes, for each change to use. For each query, the following responses are possible: </p>
<pre>
y - record this change
n - skip this change
e - edit this change manually
s - skip remaining changes to this file
f - record remaining changes to this file
d - done, skip remaining changes and files
a - record all changes to all remaining files
q - quit, recording no changes
? - display help
</pre>
<p> This command is not available when committing a merge. </p>
<p> Options:</p>
<dl>
<dt><code>-A, &#8211;addremove</code></p>
<dd> mark new/missing files as added/removed before committing</p>
<dt><code>&#8211;close-branch</code></p>
<dd> mark a branch as closed, hiding it from the branch list</p>
<dt><code>&#8211;amend</code></p>
<dd> amend the parent of the working dir</p>
<dt><code>-I, &#8211;include</code></p>
<dd> include names matching the given patterns</p>
<dt><code>-X, &#8211;exclude</code></p>
<dd> exclude names matching the given patterns</p>
<dt><code>-m, &#8211;message</code></p>
<dd> use text as commit message</p>
<dt><code>-l, &#8211;logfile</code></p>
<dd> read commit message from file</p>
<dt><code>-d, &#8211;date</code></p>
<dd> record the specified date as commit date</p>
<dt><code>-u, &#8211;user</code></p>
<dd> record the specified user as committer</p>
<dt><code>-S, &#8211;subrepos</code></p>
<dd> recurse into subrepositories</p>
<dt><code>-w, &#8211;ignore-all-space</code></p>
<dd> ignore white space when comparing lines</p>
<dt><code>-b, &#8211;ignore-space-change</code></p>
<dd> ignore changes in the amount of white space</p>
<dt><code>-B, &#8211;ignore-blank-lines</code></p>
<dd> ignore changes whose lines are all blank</dl>
<h3>relink</h3>
<p> recreates hardlinks between repository clones</p>
<h3>Commands</h3>
<h3>relink</h3>
<pre>
hg relink [ORIGIN]
</pre>
<p> When repositories are cloned locally, their data files will be hardlinked so that they only use the space of a single repository. </p>
<p> Unfortunately, subsequent pulls into either repository will break hardlinks for any files touched by the new changesets, even if both repositories end up pulling the same changes. </p>
<p> Similarly, passing &#8211;rev to &quot;hg clone&quot; will fail to use any hardlinks, falling back to a complete copy of the source repository. </p>
<p> This command lets you recreate those hardlinks and reclaim that wasted space. </p>
<p> This repository will be relinked to share space with ORIGIN, which must be on the same local disk. If ORIGIN is omitted, looks for &quot;default-relink&quot;, then &quot;default&quot;, in [paths]. </p>
<p> Do not attempt any read operations on this repository while the command is running. (Both repositories will be locked against writes.)</p>
<h3>schemes</h3>
<p> extend schemes with shortcuts to repository swarms </p>
<p> This extension allows you to specify shortcuts for parent URLs with a lot of repositories to act like a scheme, for example: </p>
<pre>
[schemes]
py = <a rel="nofollow" href="http://code.python.org/hg/">http://code.python.org/hg/</a>
</pre>
<p> After that you can use it like: </p>
<pre>
hg clone py://trunk/
</pre>
<p> Additionally there is support for some more complex schemas, for example used by Google Code: </p>
<p>[schemes] gcode = http: //{1}.googlecode.com/hg/</p>
<p> The syntax is taken from Mercurial templates, and you have unlimited number of variables, starting with <code>{1}</code> and continuing with <code>{2}</code>, <code>{3}</code> and so on. This variables will receive parts of URL supplied, split by <code>/</code>. Anything not specified as <code>{part}</code> will be just appended to an URL. </p>
<p> For convenience, the extension adds these schemes by default: </p>
<p>[schemes] py = http :              // hg.python.org/<br />
                      bb = https : // bitbucket.org/<br />
                                   bb +<br />
                                   ssh = ssh :                               // hg@bitbucket.org/<br />
                                               gcode = https :               //{1}.googlecode.com/hg/<br />
                                                               kiln = https: //{1}.kilnhg.com/Repo/</p>
<p> You can override a predefined scheme by defining a new scheme with the same name.</p>
<h3>share</h3>
<p> share a common history between several working directories</p>
<h3>Commands</h3>
<h3>share</h3>
<p>hg share[-U] SOURCE[DEST]</p>
<p> Initialize a new repository and working directory that shares its history with another repository.</p>
<dl>
<dt>Note</p>
<dd> using rollback or extensions that destroy/modify history (mq, rebase, etc.) can cause considerable confusion with shared clones. In particular, if two shared clones are both updated to the same changeset, and one of them destroys that changeset with rollback, the other clone will suddenly stop working: all operations will fail with &quot;abort: working directory has unknown parent&quot;. The only known workaround is to use debugsetparents on the broken clone to reset it to a changeset that still exists (e.g. tip). </p>
<p> Options:</p>
<dt><code>-U, &#8211;noupdate</code></p>
<dd> do not create a working copy</dl>
<h3>unshare</h3>
<pre>
hg unshare
</pre>
<p> Copy the store data to the repo and remove the sharedpath data.</p>
<h3>transplant</h3>
<p> command to transplant changesets from another branch </p>
<p> This extension allows you to transplant changes to another parent revision, possibly in another repository. The transplant is done using &#8216;diff&#8217; patches. </p>
<p> Transplanted patches are recorded in .hg/transplant/transplants, as a map from a changeset hash to its hash in the source repository.</p>
<h3>Commands</h3>
<h3>transplant</h3>
<p>hg transplant[-s REPO][-b BRANCH[-a]][-p REV][-m REV][REV]&#8230;</p>
<p> Selected changesets will be applied on top of the current working directory with the log of the original changeset. The changesets are copied and will thus appear twice in the history with different identities. </p>
<p> Consider using the graft command if everything is inside the same repository &#8211; it will use merges and will usually give a better result. Use the rebase extension if the changesets are unpublished and you want to move them instead of copying them. </p>
<p> If &#8211;log is specified, log messages will have a comment appended of the form: </p>
<pre>
(transplanted from CHANGESETHASH)
</pre>
<p> You can rewrite the changelog message with the &#8211;filter option. Its argument will be invoked with the current changelog message as $1 and the patch as $2. </p>
<p> &#8211;source/-s specifies another repository to use for selecting changesets, just as if it temporarily had been pulled. If &#8211;branch/-b is specified, these revisions will be used as heads when deciding which changsets to transplant, just as if only these revisions had been pulled. If &#8211;all/-a is specified, all the revisions up to the heads specified with &#8211;branch will be transplanted. </p>
<p> Example:</p>
<dl>
<dt>&bull;</p>
<dd> transplant all changes up to REV on top of your current revision: </p>
<pre>
hg transplant --branch REV --all
</pre>
<p> You can optionally mark selected transplanted changesets as merge changesets. You will not be prompted to transplant any ancestors of a merged transplant, and you can merge descendants of them normally instead of transplanting them. </p>
<p> Merge changesets may be transplanted directly by specifying the proper parent changeset by calling <code>hg transplant &#8211;parent</code>:. </p>
<p> If no merges or revisions are provided, <code>hg transplant</code>: will start an interactive changeset browser. </p>
<p> If a changeset application fails, you can fix the merge by hand and then resume where you left off by calling <code>hg transplant &#8211;continue/-c</code>:. </p>
<p> Options:</p>
<dt><code>-s, &#8211;source</code></p>
<dd> transplant changesets from REPO</p>
<dt><code>-b, &#8211;branch</code></p>
<dd> use this source changeset as head</p>
<dt><code>-a, &#8211;all</code></p>
<dd> pull all changesets up to the &#8211;branch revisions</p>
<dt><code>-p, &#8211;prune</code></p>
<dd> skip over REV</p>
<dt><code>-m, &#8211;merge</code></p>
<dd> merge at REV</p>
<dt><code>&#8211;parent</code></p>
<dd> parent to choose when transplanting merge</p>
<dt><code>-e, &#8211;edit</code></p>
<dd> invoke editor on commit messages</p>
<dt><code>&#8211;log</code></p>
<dd> append transplant info to log message</p>
<dt><code>-c, &#8211;continue</code></p>
<dd> continue last transplant session after fixing conflicts</p>
<dt><code>&#8211;filter</code></p>
<dd> filter changesets through command</dl>
<h3>win32mbcs</h3>
<p> allow the use of MBCS paths with problematic encodings </p>
<p> Some MBCS encodings are not good for some path operations (i.e. splitting path, case conversion, etc.) with its encoded bytes. We call such a encoding (i.e. shift_jis and big5) as &quot;problematic encoding&quot;. This extension can be used to fix the issue with those encodings by wrapping some functions to convert to Unicode string before path operation. </p>
<p> This extension is useful for:</p>
<dl>
<dt>&bull;</p>
<dd> Japanese Windows users using shift_jis encoding.</p>
<dt>&bull;</p>
<dd> Chinese Windows users using big5 encoding.</p>
<dt>&bull;</p>
<dd> All users who use a repository with one of problematic encodings on case-insensitive file system. </p>
<p> This extension is not needed for:</p>
<dt>&bull;</p>
<dd> Any user who use only ASCII chars in path.</p>
<dt>&bull;</p>
<dd> Any user who do not use any of problematic encodings. </p>
<p> Note that there are some limitations on using this extension:</p>
<dt>&bull;</p>
<dd> You should use single encoding in one repository.</p>
<dt>&bull;</p>
<dd> If the repository path ends with 0x5c, .hg/hgrc cannot be read.</p>
<dt>&bull;</p>
<dd> win32mbcs is not compatible with fixutf8 extension. </p>
<p> By default, win32mbcs uses encoding.encoding decided by Mercurial. You can specify the encoding by config option: </p>
<pre>
[win32mbcs]
encoding = sjis
</pre>
<p> It is useful for the users who want to commit with UTF-8 log message.</dl>
<h3>win32text</h3>
<p> perform automatic newline conversion </p>
<p> Deprecation: The win32text extension requires each user to configure the extension again and again for each clone since the configuration is not copied when cloning. </p>
<p> We have therefore made the <code>eol</code> as an alternative. The <code>eol</code> uses a version controlled file for its configuration and each clone will therefore use the right settings from the start. </p>
<p> To perform automatic newline conversion, use: </p>
<pre><code>
[extensions] win32text =
    [encode]
        ** = cleverencode :
# or ** = macencode:
    [decode]
        ** = cleverdecode:
# or ** = macdecode:
</code></pre>
<p> If not doing conversion, to make sure you do not commit CRLF/CR by accident: </p>
<pre>
[hooks]
pretxncommit.crlf = python:hgext.win32text.forbidcrlf
# or pretxncommit.cr = python:hgext.win32text.forbidcr
</pre>
<p> To do the same check on a server to prevent CRLF/CR from being pushed or pulled: </p>
<pre>
[hooks]
pretxnchangegroup.crlf = python:hgext.win32text.forbidcrlf
# or pretxnchangegroup.cr = python:hgext.win32text.forbidcr
</pre>
<h3>zeroconf</h3>
<p> discover and advertise repositories on the local network </p>
<p> Zeroconf-enabled repositories will be announced in a network without the need to configure a server or a service. They can be discovered without knowing their actual IP address. </p>
<p> To allow other people to discover your repository using run <code>hg serve</code>: in your repository: </p>
<pre>
$ cd test
$ hg serve
</pre>
<p> You can discover Zeroconf-enabled repositories by running <code>hg paths</code>:: </p>
<pre>
$ hg paths
zc-test = <a rel="nofollow" href="http://example.com:8000/test">http://example.com:8000/test</a>
</pre>
<h2>FILES</h2>
<dl>
<dt><code>/etc/mercurial/hgrc</code>, <code>$HOME/.hgrc</code>, <code>.hg/hgrc</code></p>
<dd>
<p> This file contains defaults and configuration. Values in <code>.hg/hgrc</code> override those in <code>$HOME/.hgrc</code>, and these override settings made in the global <code>/etc/mercurial/hgrc</code> configuration. See <code><a href="/docs/linux/man/5-hgrc/">hgrc</a></code>(5): for details of the contents and format of these files.</p>
<dt><code>.hgignore</code></p>
<dd>
<p> This file contains regular expressions (one per line) that describe file names that should be ignored by <code>hg</code>. For details, see <code><a href="/docs/linux/man/5-hgignore/">hgignore</a></code>(5):.</p>
<dt><code>.hgsub</code></p>
<dd>
<p> This file defines the locations of all subrepositories, and tells where the subrepository checkouts came from. For details, see <code>hg help subrepos</code>:.</p>
<dt><code>.hgsubstate</code></p>
<dd>
<p> This file is where Mercurial stores all nested repository states. <i>NB: This file should not be edited manually.</i></p>
<dt><code>.hgtags</code></p>
<dd>
<p> This file contains changeset hash values and text tag names (one of each separated by spaces) that correspond to tagged versions of the repository contents. The file content is encoded using UTF-8.</p>
<dt><code>.hg/last-message.txt</code></p>
<dd>
<p> This file is used by <code>hg commit</code>: to store a backup of the commit message in case the commit fails.</p>
<dt><code>.hg/localtags</code></p>
<dd>
<p> This file can be used to define local tags which are not shared among repositories. The file format is the same as for <code>.hgtags</code>, but it is encoded using the local system encoding. </p>
<p> Some commands (e.g. revert) produce backup files ending in <code>.orig</code>, if the <code>.orig</code> file already exists and is not tracked by Mercurial, it will be overwritten.</dl>
<h2>BUGS</h2>
<p> Probably lots, please post them to the mailing list (see Resources: below) when you find them.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-hgignore/">hgignore</a></code>(5):, <code><a href="/docs/linux/man/5-hgrc/">hgrc</a></code>(5):</p>
<h2>AUTHOR</h2>
<p> Written by Matt Mackall &lt;mpm [at] selenic.com:&gt;</p>
<h2>RESOURCES</h2>
<p> Main Web Site: <a rel="nofollow" href="http://mercurial.selenic.com/:">http://mercurial.selenic.com/:</a> </p>
<p> Source code repository: <a rel="nofollow" href="http://selenic.com/hg:">http://selenic.com/hg:</a> </p>
<p> Mailing list: <a rel="nofollow" href="http://selenic.com/mailman/listinfo/mercurial:">http://selenic.com/mailman/listinfo/mercurial:</a></p>
<h2>COPYING</h2>
<p> Copyright (C) 2005-2012 Matt Mackall. Free use of this software is granted under the terms of the GNU General Public License version 2 or any later version.</p>
<h2>AUTHOR</h2>
<p> Matt Mackall &lt;mpm [at] selenic.com&gt; </p>
<p> Organization: Mercurial </p>
<h2>Index</h2>

---
title: "bzr(1)"
name: "bzr"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bzr/"
description: "bzr – Bazaar next-generation distributed version control"
---

<h2>NAME</h2>
<p> bzr &#8211; Bazaar next-generation distributed version control</p>
<h2>SYNOPSIS</h2>
<p> <code>bzr</code> <i>command</i> [ <i>command_options</i> ]<br />
 <code>bzr</code> <code>help</code><br />
 <code>bzr</code> <code>help</code> <i>command</i></p>
<h2>DESCRIPTION</h2>
<p> Bazaar (or bzr) is a distributed version control system that is powerful, friendly, and scalable. Bazaar is a project of Canonical Ltd and part of the GNU Project to develop a free operating system. </p>
<p> Bazaar keeps track of changes to software source code (or similar information); lets you explore who changed it, when, and why; merges concurrent changes; and helps people work together in a team.</p>
<h2>COMMAND OVERVIEW</h2>
<dl>
<dt><code>bzr add [FILE&#8230;]</code></p>
<dd> Add specified files or directories.</p>
<dt><code>bzr alias [NAME]</code></p>
<dd> Set/unset and display aliases.</p>
<dt><code>bzr annotate FILENAME</code></p>
<dd> Show the origin of each line in a file.</p>
<dt><code>bzr bind [LOCATION]</code></p>
<dd> Convert the current branch into a checkout of the supplied branch.</p>
<dt><code>bzr branch FROM_LOCATION [TO_LOCATION]</code></p>
<dd> Create a new branch that is a copy of an existing branch.</p>
<dt><code>bzr branches [LOCATION]</code></p>
<dd> List the branches available at the current location.</p>
<dt><code>bzr break-lock [LOCATION]</code></p>
<dd> Break a dead lock.</p>
<dt><code>bzr cat FILENAME</code></p>
<dd> Write the contents of a file as of a given revision to standard output.</p>
<dt><code>bzr check [PATH]</code></p>
<dd> Validate working tree structure, branch consistency and repository history.</p>
<dt><code>bzr checkout [BRANCH_LOCATION] [TO_LOCATION]</code></p>
<dd> Create a new checkout of an existing branch.</p>
<dt><code>bzr clean-tree</code></p>
<dd> Remove unwanted files from working tree.</p>
<dt><code>bzr commit [SELECTED&#8230;]</code></p>
<dd> Commit changes into a new revision.</p>
<dt><code>bzr config [NAME]</code></p>
<dd> Display, set or remove a configuration option.</p>
<dt><code>bzr conflicts</code></p>
<dd> List files with conflicts.</p>
<dt><code>bzr deleted</code></p>
<dd> List files deleted in the working tree.</p>
<dt><code>bzr diff [FILE&#8230;]</code></p>
<dd> Show differences in the working tree, between revisions or branches.</p>
<dt><code>bzr dpush [LOCATION]</code></p>
<dd> Push into a different VCS without any custom bzr metadata.</p>
<dt><code>bzr export DEST [BRANCH_OR_SUBDIR]</code></p>
<dd> Export current or past revision to a destination directory or archive.</p>
<dt><code>bzr help [TOPIC]</code></p>
<dd> Show help on a command or other topic.</p>
<dt><code>bzr ignore [NAME_PATTERN&#8230;]</code></p>
<dd> Ignore specified files or patterns.</p>
<dt><code>bzr ignored</code></p>
<dd> List ignored files and the patterns that matched them.</p>
<dt><code>bzr info [LOCATION]</code></p>
<dd> Show information about a working tree, branch or repository.</p>
<dt><code>bzr init [LOCATION]</code></p>
<dd> Make a directory into a versioned branch.</p>
<dt><code>bzr init-repository LOCATION</code></p>
<dd> Create a shared repository for branches to share storage space.</p>
<dt><code>bzr join TREE</code></p>
<dd> Combine a tree into its containing tree.</p>
<dt><code>bzr log [FILE&#8230;]</code></p>
<dd> Show historical log for a branch or subset of a branch.</p>
<dt><code>bzr ls [PATH]</code></p>
<dd> List files in a tree.</p>
<dt><code>bzr merge [LOCATION]</code></p>
<dd> Perform a three-way merge.</p>
<dt><code>bzr missing [OTHER_BRANCH]</code></p>
<dd> Show unmerged/unpulled revisions between two branches.</p>
<dt><code>bzr mkdir DIR&#8230;</code></p>
<dd> Create a new versioned directory.</p>
<dt><code>bzr mv [NAMES&#8230;]</code></p>
<dd> Move or rename a file.</p>
<dt><code>bzr nick [NICKNAME]</code></p>
<dd> Print or set the branch nickname.</p>
<dt><code>bzr pack [BRANCH_OR_REPO]</code></p>
<dd> Compress the data within a repository.</p>
<dt><code>bzr plugins</code></p>
<dd> List the installed plugins.</p>
<dt><code>bzr pull [LOCATION]</code></p>
<dd> Turn this branch into a mirror of another branch.</p>
<dt><code>bzr push [LOCATION]</code></p>
<dd> Update a mirror of this branch.</p>
<dt><code>bzr reconcile [BRANCH]</code></p>
<dd> Reconcile bzr metadata in a branch.</p>
<dt><code>bzr reconfigure [LOCATION]</code></p>
<dd> Reconfigure the type of a bzr directory.</p>
<dt><code>bzr remerge [FILE&#8230;]</code></p>
<dd> Redo a merge.</p>
<dt><code>bzr remove [FILE&#8230;]</code></p>
<dd> Remove files or directories.</p>
<dt><code>bzr remove-branch [LOCATION]</code></p>
<dd> Remove a branch.</p>
<dt><code>bzr remove-tree [LOCATION&#8230;]</code></p>
<dd> Remove the working tree from a given branch/checkout.</p>
<dt><code>bzr renames [DIR]</code></p>
<dd> Show list of renamed files.</p>
<dt><code>bzr resolve [FILE&#8230;]</code></p>
<dd> Mark a conflict as resolved.</p>
<dt><code>bzr revert [FILE&#8230;]</code></p>
<dd> Revert files to a previous revision.</p>
<dt><code>bzr revno [LOCATION]</code></p>
<dd> Show current revision number.</p>
<dt><code>bzr root [FILENAME]</code></p>
<dd> Show the tree root directory.</p>
<dt><code>bzr send [SUBMIT_BRANCH] [PUBLIC_BRANCH]</code></p>
<dd> Mail or create a merge-directive for submitting changes.</p>
<dt><code>bzr serve</code></p>
<dd> Run the bzr server.</p>
<dt><code>bzr shelve [FILE&#8230;]</code></p>
<dd> Temporarily set aside some changes from the current tree.</p>
<dt><code>bzr sign-my-commits [LOCATION] [COMMITTER]</code></p>
<dd> Sign all commits by a given committer.</p>
<dt><code>bzr split TREE</code></p>
<dd> Split a subdirectory of a tree into a separate tree.</p>
<dt><code>bzr status [FILE&#8230;]</code></p>
<dd> Display status summary.</p>
<dt><code>bzr switch [TO_LOCATION]</code></p>
<dd> Set the branch of a checkout and update.</p>
<dt><code>bzr tag [TAG_NAME]</code></p>
<dd> Create, remove or modify a tag naming a revision.</p>
<dt><code>bzr tags</code></p>
<dd> List tags.</p>
<dt><code>bzr testament [BRANCH]</code></p>
<dd> Show testament (signing-form) of a revision.</p>
<dt><code>bzr unbind</code></p>
<dd> Convert the current checkout into a regular branch.</p>
<dt><code>bzr uncommit [LOCATION]</code></p>
<dd> Remove the last committed revision.</p>
<dt><code>bzr unshelve [SHELF_ID]</code></p>
<dd> Restore shelved changes.</p>
<dt><code>bzr update [DIR]</code></p>
<dd> Update a working tree to a new revision.</p>
<dt><code>bzr upgrade [URL]</code></p>
<dd> Upgrade a repository, branch or working tree to a newer format.</p>
<dt><code>bzr verify-signatures [LOCATION]</code></p>
<dd> Verify all commit signatures.</p>
<dt><code>bzr version</code></p>
<dd> Show version of bzr.</p>
<dt><code>bzr version-info [LOCATION]</code></p>
<dd> Show version information about this tree.</p>
<dt><code>bzr view [FILE&#8230;]</code></p>
<dd> Manage filtered views.</p>
<dt><code>bzr whoami [NAME]</code></p>
<dd> Show or set bzr user id.</dl>
<h2>COMMAND REFERENCE</h2>
<h3>bzr &#8211;help</h3>
<p> Alias for &quot;help&quot;, see &quot;bzr help&quot;.</p>
<h3>bzr -?</h3>
<p> Alias for &quot;help&quot;, see &quot;bzr help&quot;.</p>
<h3>bzr -h</h3>
<p> Alias for &quot;help&quot;, see &quot;bzr help&quot;.</p>
<h3>bzr ?</h3>
<p> Alias for &quot;help&quot;, see &quot;bzr help&quot;.</p>
<h3>bzr add [FILE&#8230;]</h3>
<p> Options:<br />
&nbsp;<wbr>&#8211;dry-run&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show what would be done, but don&#8217;t<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>actually do anything.<br />
&nbsp;<wbr>&#8211;file-ids-from ARG&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Lookup file ids from this tree.<br />
&nbsp;<wbr>&#8211;help, -h&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show help message.<br />
&nbsp;<wbr>&#8211;no-recurse&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Don&#8217;t recursively add the contents of<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>directories.<br />
&nbsp;<wbr>&#8211;quiet, -q&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Only display errors and warnings.<br />
&nbsp;<wbr>&#8211;usage&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show usage message and options.<br />
&nbsp;<wbr>&#8211;verbose, -v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Display more information. </p>
<p> See also: ignore, remove </p>
<p> Add specified files or directories. </p>
<p> In non-recursive mode, all the named items are added, regardless of whether they were previously ignored. A warning is given if any of the named files are already versioned. </p>
<p> In recursive mode (the default), files are treated the same way but the behaviour for directories is different. Directories that are already versioned do not give a warning. All directories, whether already versioned or not, are searched for files or subdirectories that are neither versioned or ignored, and these are added. This search proceeds recursively into versioned directories. If no names are given &#8216;.&#8217; is assumed. </p>
<p> A warning will be printed when nested trees are encountered, unless they are explicitly ignored. </p>
<p> Therefore simply saying &#8216;bzr add&#8217; will version all files that are currently unknown. </p>
<p> Adding a file whose parent directory is not versioned will implicitly add the parent, and so on up to the root. This means you should never need to explicitly add a directory, they&#8217;ll just get added when you add a file in the directory. </p>
<p> &#8211;dry-run will show which files would be added, but not actually add them. </p>
<p> &#8211;file-ids-from will try to use the file ids from the supplied path. It looks up ids trying to find a matching parent directory with the same filename, and then by pure path. This option is rarely needed but can be useful when adding the same logical file into two branches that will be merged later (without showing the two different adds as a conflict). It is also useful when merging another project into a subdirectory of this one. </p>
<p> Any files matching patterns in the ignore list will not be added unless they are explicitly mentioned. </p>
<p> In recursive mode, files larger than the configuration option add.maximum_file_size will be skipped. Named items are never skipped due to file size. </p>
<h3>bzr alias [NAME]</h3>
<p> Options:<br />
&nbsp;<wbr>&#8211;help, -h&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show help message.<br />
&nbsp;<wbr>&#8211;quiet, -q&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Only display errors and warnings.<br />
&nbsp;<wbr>&#8211;remove&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Remove the alias.<br />
&nbsp;<wbr>&#8211;usage&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show usage message and options.<br />
&nbsp;<wbr>&#8211;verbose, -v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Display more information. </p>
<p> Set/unset and display aliases. </p>
<p> Examples:<br />
&nbsp;<wbr>Show the current aliases: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>bzr alias </p>
<p>&nbsp;<wbr>Show the alias specified for&nbsp;<wbr>&#8216;ll&#8217;: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>bzr alias ll </p>
<p>&nbsp;<wbr>Set an alias for&nbsp;<wbr>&#8216;ll&#8217;: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>bzr alias ll=&quot;log &#8211;line -r-10..-1&quot; </p>
<p>&nbsp;<wbr>To remove an alias for&nbsp;<wbr>&#8216;ll&#8217;: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>bzr alias &#8211;remove ll </p>
<h3>bzr ann</h3>
<p> Alias for &quot;annotate&quot;, see &quot;bzr annotate&quot;.</p>
<h3>bzr annotate FILENAME</h3>
<p> Options:<br />
&nbsp;<wbr>&#8211;all&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show annotations on all lines.<br />
&nbsp;<wbr>&#8211;directory ARG, -d&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Branch to operate on, instead of working<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>directory.<br />
&nbsp;<wbr>&#8211;help, -h&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show help message.<br />
&nbsp;<wbr>&#8211;long&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show commit date in annotations.<br />
&nbsp;<wbr>&#8211;quiet, -q&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Only display errors and warnings.<br />
&nbsp;<wbr>&#8211;revision ARG, -r&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr>&quot;help revisionspec&quot;&nbsp;<wbr>for details.<br />
&nbsp;<wbr>&#8211;show-ids&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show internal object ids.<br />
&nbsp;<wbr>&#8211;usage&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show usage message and options.<br />
&nbsp;<wbr>&#8211;verbose, -v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Display more information. </p>
<p> Aliases: ann, blame, praise </p>
<p> Show the origin of each line in a file. </p>
<p> This prints out the given file with an annotation on the left side indicating which revision, author and date introduced the change. </p>
<p> If the origin is the same for a run of consecutive lines, it is shown only at the top, unless the &#8211;all option is given. </p>
<h3>bzr bind [LOCATION]</h3>
<p> Options:<br />
&nbsp;<wbr>&#8211;directory ARG, -d&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Branch to operate on, instead of working<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>directory.<br />
&nbsp;<wbr>&#8211;help, -h&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show help message.<br />
&nbsp;<wbr>&#8211;quiet, -q&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Only display errors and warnings.<br />
&nbsp;<wbr>&#8211;usage&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show usage message and options.<br />
&nbsp;<wbr>&#8211;verbose, -v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Display more information. </p>
<p> See also: checkouts, unbind </p>
<p> Convert the current branch into a checkout of the supplied branch. If no branch is supplied, rebind to the last bound location. </p>
<p> Once converted into a checkout, commits must succeed on the master branch before they will be applied to the local branch. </p>
<p> Bound branches use the nickname of its master branch unless it is set locally, in which case binding will update the local nickname to be that of the master. </p>
<h3>bzr blame</h3>
<p> Alias for &quot;annotate&quot;, see &quot;bzr annotate&quot;.</p>
<h3>bzr branch FROM_LOCATION [TO_LOCATION]</h3>
<p> Options:<br />
&nbsp;<wbr>&#8211;bind&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Bind new branch to from location.<br />
&nbsp;<wbr>&#8211;files-from ARG&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Get file contents from this tree.<br />
&nbsp;<wbr>&#8211;hardlink&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Hard-link working tree files where<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>possible.<br />
&nbsp;<wbr>&#8211;help, -h&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show help message.<br />
&nbsp;<wbr>&#8211;no-tree&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Create a branch without a working-tree.<br />
&nbsp;<wbr>&#8211;quiet, -q&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Only display errors and warnings.<br />
&nbsp;<wbr>&#8211;revision ARG, -r&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr>&quot;help revisionspec&quot;&nbsp;<wbr>for details.<br />
&nbsp;<wbr>&#8211;stacked&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Create a stacked branch referring to the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>source branch. The new branch will<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>depend on the availability of the source<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>branch for all operations.<br />
&nbsp;<wbr>&#8211;standalone&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Do not use a shared repository, even if<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>available.<br />
&nbsp;<wbr>&#8211;switch&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Switch the checkout in the current<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>directory to the new branch.<br />
&nbsp;<wbr>&#8211;usage&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show usage message and options.<br />
&nbsp;<wbr>&#8211;use-existing-dir&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>By default branch will fail if the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>target directory exists, but does not<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>already have a control directory.&nbsp;<wbr>&nbsp;<wbr>This<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>flag will allow branch to proceed.<br />
&nbsp;<wbr>&#8211;verbose, -v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Display more information. </p>
<p> Aliases: get, clone </p>
<p> See also: checkout </p>
<p> Create a new branch that is a copy of an existing branch. </p>
<p> If the TO_LOCATION is omitted, the last component of the FROM_LOCATION will be used. In other words, &quot;branch ../foo/bar&quot; will attempt to create ./bar. If the FROM_LOCATION has no / or path separator embedded, the TO_LOCATION is derived from the FROM_LOCATION by stripping a leading scheme or drive identifier, if any. For example, &quot;branch lp:foo-bar&quot; will attempt to create ./foo-bar. </p>
<p> To retrieve the branch as of a particular revision, supply the &#8211;revision parameter, as in &quot;branch foo/bar -r 5&quot;. </p>
<p> The synonyms &#8216;clone&#8217; and &#8216;get&#8217; for this command are deprecated. </p>
<h3>bzr branches [LOCATION]</h3>
<p> Options:<br />
&nbsp;<wbr>&#8211;help, -h&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show help message.<br />
&nbsp;<wbr>&#8211;quiet, -q&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Only display errors and warnings.<br />
&nbsp;<wbr>&#8211;recursive, -R&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Recursively scan for branches rather<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>than just looking in the specified<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>location.<br />
&nbsp;<wbr>&#8211;usage&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show usage message and options.<br />
&nbsp;<wbr>&#8211;verbose, -v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Display more information. </p>
<p> List the branches available at the current location. </p>
<p> This command will print the names of all the branches at the current location. </p>
<h3>bzr break-lock [LOCATION]</h3>
<p> Options:<br />
&nbsp;<wbr>&#8211;config&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>LOCATION is the directory where the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>config lock is.<br />
&nbsp;<wbr>&#8211;force&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Do not ask for confirmation before<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>breaking the lock.<br />
&nbsp;<wbr>&#8211;help, -h&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show help message.<br />
&nbsp;<wbr>&#8211;quiet, -q&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Only display errors and warnings.<br />
&nbsp;<wbr>&#8211;usage&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show usage message and options.<br />
&nbsp;<wbr>&#8211;verbose, -v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Display more information. </p>
<p> Break a dead lock. </p>
<p> This command breaks a lock on a repository, branch, working directory or config file. </p>
<p> CAUTION: Locks should only be broken when you are sure that the process holding the lock has been stopped. </p>
<p> You can get information on what locks are open via the &#8216;bzr info [location]&#8217; command. </p>
<p> Examples:<br />
&nbsp;<wbr>bzr break-lock<br />
&nbsp;<wbr>bzr break-lock bzr+<a href="ssh://example.com/bzr/foo">ssh://example.com/bzr/foo</a><br />
&nbsp;<wbr>bzr break-lock &#8211;conf&nbsp;<wbr>~/.bazaar </p>
<h3>bzr cat FILENAME</h3>
<p> Options:<br />
&nbsp;<wbr>&#8211;directory ARG, -d&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Branch to operate on, instead of working<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>directory.<br />
&nbsp;<wbr>&#8211;filters&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Apply content filters to display the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>convenience form.<br />
&nbsp;<wbr>&#8211;help, -h&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show help message.<br />
&nbsp;<wbr>&#8211;name-from-revision&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>The path name in the old tree.<br />
&nbsp;<wbr>&#8211;quiet, -q&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Only display errors and warnings.<br />
&nbsp;<wbr>&#8211;revision ARG, -r&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr>&quot;help revisionspec&quot;&nbsp;<wbr>for details.<br />
&nbsp;<wbr>&#8211;usage&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show usage message and options.<br />
&nbsp;<wbr>&#8211;verbose, -v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Display more information. </p>
<p> See also: ls </p>
<p> Write the contents of a file as of a given revision to standard output. </p>
<p> If no revision is nominated, the last revision is used. </p>
<p> Note: Take care to redirect standard output when using this command on a binary file. </p>
<h3>bzr check [PATH]</h3>
<p> Options:<br />
&nbsp;<wbr>&#8211;branch&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Check the branch related to the current<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>directory.<br />
&nbsp;<wbr>&#8211;help, -h&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show help message.<br />
&nbsp;<wbr>&#8211;quiet, -q&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Only display errors and warnings.<br />
&nbsp;<wbr>&#8211;repo&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Check the repository related to the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>current directory.<br />
&nbsp;<wbr>&#8211;tree&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Check the working tree related to the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>current directory.<br />
&nbsp;<wbr>&#8211;usage&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show usage message and options.<br />
&nbsp;<wbr>&#8211;verbose, -v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Display more information. </p>
<p> See also: reconcile </p>
<p> Validate working tree structure, branch consistency and repository history. </p>
<p> This command checks various invariants about branch and repository storage to detect data corruption or bzr bugs. </p>
<p> The working tree and branch checks will only give output if a problem is detected. The output fields of the repository check are: </p>
<p> revisions<br />
&nbsp;<wbr>This is just the number of revisions checked.&nbsp;<wbr>&nbsp;<wbr>It doesn&#8217;t<br />
&nbsp;<wbr>indicate a problem. </p>
<p> versionedfiles<br />
&nbsp;<wbr>This is just the number of versionedfiles checked.&nbsp;<wbr>&nbsp;<wbr>It<br />
&nbsp;<wbr>doesn&#8217;t indicate a problem. </p>
<p> unreferenced ancestors<br />
&nbsp;<wbr>Texts that are ancestors of other texts, but<br />
&nbsp;<wbr>are not properly referenced by the revision ancestry.&nbsp;<wbr>&nbsp;<wbr>This is a<br />
&nbsp;<wbr>subtle problem that Bazaar can work around. </p>
<p> unique file texts<br />
&nbsp;<wbr>This is the total number of unique file contents<br />
&nbsp;<wbr>seen in the checked revisions.&nbsp;<wbr>&nbsp;<wbr>It does not indicate a problem. </p>
<p> repeated file texts<br />
&nbsp;<wbr>This is the total number of repeated texts seen<br />
&nbsp;<wbr>in the checked revisions.&nbsp;<wbr>&nbsp;<wbr>Texts can be repeated when their file<br />
&nbsp;<wbr>entries are modified, but the file contents are not.&nbsp;<wbr>&nbsp;<wbr>It does not<br />
&nbsp;<wbr>indicate a problem. </p>
<p> If no restrictions are specified, all Bazaar data that is found at the given location will be checked. </p>
<p> Examples: </p>
<p>&nbsp;<wbr>Check the tree and branch at&nbsp;<wbr>&#8216;foo&#8217;: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>bzr check &#8211;tree &#8211;branch foo </p>
<p>&nbsp;<wbr>Check only the repository at&nbsp;<wbr>&#8216;bar&#8217;: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>bzr check &#8211;repo bar </p>
<p>&nbsp;<wbr>Check everything at&nbsp;<wbr>&#8216;baz&#8217;: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>bzr check baz </p>
<h3>bzr checkin</h3>
<p> Alias for &quot;commit&quot;, see &quot;bzr commit&quot;.</p>
<h3>bzr checkout [BRANCH_LOCATION] [TO_LOCATION]</h3>
<p> Options:<br />
&nbsp;<wbr>&#8211;files-from ARG&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Get file contents from this tree.<br />
&nbsp;<wbr>&#8211;hardlink&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Hard-link working tree files where<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>possible.<br />
&nbsp;<wbr>&#8211;help, -h&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show help message.<br />
&nbsp;<wbr>&#8211;lightweight&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Perform a lightweight checkout.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Lightweight checkouts depend on access<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>to the branch for every operation.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Normal checkouts can perform common<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>operations like diff and status without<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>such access, and also support local<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>commits.<br />
&nbsp;<wbr>&#8211;quiet, -q&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Only display errors and warnings.<br />
&nbsp;<wbr>&#8211;revision ARG, -r&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr>&quot;help revisionspec&quot;&nbsp;<wbr>for details.<br />
&nbsp;<wbr>&#8211;usage&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show usage message and options.<br />
&nbsp;<wbr>&#8211;verbose, -v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Display more information. </p>
<p> Alias: co </p>
<p> See also: branch, checkouts </p>
<p> Create a new checkout of an existing branch. </p>
<p> If BRANCH_LOCATION is omitted, checkout will reconstitute a working tree for the branch found in &#8216;.&#8217;. This is useful if you have removed the working tree or if it was never created &#8211; i.e. if you pushed the branch to its current location using SFTP. </p>
<p> If the TO_LOCATION is omitted, the last component of the BRANCH_LOCATION will be used. In other words, &quot;checkout ../foo/bar&quot; will attempt to create ./bar. If the BRANCH_LOCATION has no / or path separator embedded, the TO_LOCATION is derived from the BRANCH_LOCATION by stripping a leading scheme or drive identifier, if any. For example, &quot;checkout lp:foo-bar&quot; will attempt to create ./foo-bar. </p>
<p> To retrieve the branch as of a particular revision, supply the &#8211;revision parameter, as in &quot;checkout foo/bar -r 5&quot;. Note that this will be immediately out of date [so you cannot commit] but it may be useful (i.e. to examine old code.) </p>
<h3>bzr ci</h3>
<p> Alias for &quot;commit&quot;, see &quot;bzr commit&quot;.</p>
<h3>bzr clean-tree</h3>
<p> Options:<br />
&nbsp;<wbr>&#8211;detritus&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Delete conflict files, merge and revert<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>backups, and failed selftest dirs.<br />
&nbsp;<wbr>&#8211;directory ARG, -d&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Branch to operate on, instead of working<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>directory.<br />
&nbsp;<wbr>&#8211;dry-run&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show files to delete instead of deleting<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>them.<br />
&nbsp;<wbr>&#8211;force&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Do not prompt before deleting.<br />
&nbsp;<wbr>&#8211;help, -h&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show help message.<br />
&nbsp;<wbr>&#8211;ignored&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Delete all ignored files.<br />
&nbsp;<wbr>&#8211;quiet, -q&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Only display errors and warnings.<br />
&nbsp;<wbr>&#8211;unknown&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Delete files unknown to bzr&nbsp;<wbr>(default).<br />
&nbsp;<wbr>&#8211;usage&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show usage message and options.<br />
&nbsp;<wbr>&#8211;verbose, -v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Display more information. </p>
<p> Remove unwanted files from working tree. </p>
<p> By default, only unknown files, not ignored files, are deleted. Versioned files are never deleted. </p>
<p> Another class is &#8216;detritus&#8217;, which includes files emitted by bzr during normal operations and selftests. (The value of these files decreases with time.) </p>
<p> If no options are specified, unknown files are deleted. Otherwise, option flags are respected, and may be combined. </p>
<p> To check what clean-tree will do, use &#8211;dry-run. </p>
<h3>bzr clone</h3>
<p> Alias for &quot;branch&quot;, see &quot;bzr branch&quot;.</p>
<h3>bzr co</h3>
<p> Alias for &quot;checkout&quot;, see &quot;bzr checkout&quot;.</p>
<h3>bzr commit [SELECTED&#8230;]</h3>
<p> Options:<br />
&nbsp;<wbr>&#8211;author ARG&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Set the author&#8217;s name, if it&#8217;s different<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>from the committer.<br />
&nbsp;<wbr>&#8211;commit-time ARG&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Manually set a commit time using commit<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>date format, e.g.&nbsp;<wbr>&#8216;2009-10-10 08:00:00<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+0100&#8242;.<br />
&nbsp;<wbr>&#8211;exclude ARG, -x&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Do not consider changes made to a given<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>path.<br />
&nbsp;<wbr>&#8211;file MSGFILE, -F&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Take commit message from this file.<br />
&nbsp;<wbr>&#8211;fixes ARG&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Mark a bug as being fixed by this<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>revision&nbsp;<wbr>(see&nbsp;<wbr>&quot;bzr help bugs&quot;).<br />
&nbsp;<wbr>&#8211;help, -h&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show help message.<br />
&nbsp;<wbr>&#8211;local&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Perform a local commit in a bound<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>branch.&nbsp;<wbr>&nbsp;<wbr>Local commits are not pushed to<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the master branch until a normal commit<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>is performed.<br />
&nbsp;<wbr>&#8211;lossy&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>When committing to a foreign version<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>control system do not push data that can<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>not be natively represented.<br />
&nbsp;<wbr>&#8211;message ARG, -m&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Description of the new revision.<br />
&nbsp;<wbr>&#8211;quiet, -q&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Only display errors and warnings.<br />
&nbsp;<wbr>&#8211;show-diff, -p&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>When no message is supplied, show the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>diff along with the status summary in<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the message editor.<br />
&nbsp;<wbr>&#8211;strict&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Refuse to commit if there are unknown<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>files in the working tree.<br />
&nbsp;<wbr>&#8211;unchanged&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Commit even if nothing has changed.<br />
&nbsp;<wbr>&#8211;usage&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show usage message and options.<br />
&nbsp;<wbr>&#8211;verbose, -v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Display more information. </p>
<p> Aliases: ci, checkin </p>
<p> See also: add, bugs, hooks, uncommit </p>
<p> Commit changes into a new revision. </p>
<p> An explanatory message needs to be given for each commit. This is often done by using the &#8211;message option (getting the message from the command line) or by using the &#8211;file option (getting the message from a file). If neither of these options is given, an editor is opened for the user to enter the message. To see the changed files in the boilerplate text loaded into the editor, use the &#8211;show-diff option. </p>
<p> By default, the entire tree is committed and the person doing the commit is assumed to be the author. These defaults can be overridden as explained below. </p>
<p> Selective commits: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>If selected files are specified, only changes to those files are<br />
&nbsp;<wbr>&nbsp;<wbr>committed.&nbsp;<wbr>&nbsp;<wbr>If a directory is specified then the directory and<br />
&nbsp;<wbr>&nbsp;<wbr>everything within it is committed. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>When excludes are given, they take precedence over selected files.<br />
&nbsp;<wbr>&nbsp;<wbr>For example, to commit only changes within foo, but not changes<br />
&nbsp;<wbr>&nbsp;<wbr>within foo/bar: </p>
<p>&nbsp;<wbr>bzr commit foo -x foo/bar </p>
<p>&nbsp;<wbr>&nbsp;<wbr>A selective commit after a merge is not yet supported. </p>
<p> Custom authors: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>If the author of the change is not the same person as the committer,<br />
&nbsp;<wbr>&nbsp;<wbr>you can specify the author&#8217;s name using the &#8211;author option. The<br />
&nbsp;<wbr>&nbsp;<wbr>name should be in the same format as a committer-id, e.g.<br />
&nbsp;<wbr>&nbsp;<wbr>&quot;John Doe&nbsp;<wbr>&lt;jdoe [at] example.com&gt;&quot;. If there is more than one author of<br />
&nbsp;<wbr>&nbsp;<wbr>the change you can specify the option multiple times, once for each<br />
&nbsp;<wbr>&nbsp;<wbr>author. </p>
<p> Checks: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>A common mistake is to forget to add a new file or directory before<br />
&nbsp;<wbr>&nbsp;<wbr>running the commit command. The &#8211;strict option checks for unknown<br />
&nbsp;<wbr>&nbsp;<wbr>files and aborts the commit if any are found. More advanced pre-commit<br />
&nbsp;<wbr>&nbsp;<wbr>checks can be implemented by defining hooks. See&nbsp;<wbr>&#8220;bzr help hooks&#8220;<br />
&nbsp;<wbr>&nbsp;<wbr>for details. </p>
<p> Things to note: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>If you accidentially commit the wrong changes or make a spelling<br />
&nbsp;<wbr>&nbsp;<wbr>mistake in the commit message say, you can use the uncommit command<br />
&nbsp;<wbr>&nbsp;<wbr>to undo it. See&nbsp;<wbr>&#8220;bzr help uncommit&#8220;&nbsp;<wbr>for details. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Hooks can also be configured to run after a commit. This allows you<br />
&nbsp;<wbr>&nbsp;<wbr>to trigger updates to external systems like bug trackers. The &#8211;fixes<br />
&nbsp;<wbr>&nbsp;<wbr>option can be used to record the association between a revision and<br />
&nbsp;<wbr>&nbsp;<wbr>one or more bugs. See&nbsp;<wbr>&#8220;bzr help bugs&#8220;&nbsp;<wbr>for details. </p>
<h3>bzr config [NAME]</h3>
<p> Options:<br />
&nbsp;<wbr>&#8211;all&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Display all the defined values for the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>matching options.<br />
&nbsp;<wbr>&#8211;directory ARG, -d&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Branch to operate on, instead of working<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>directory.<br />
&nbsp;<wbr>&#8211;help, -h&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show help message.<br />
&nbsp;<wbr>&#8211;quiet, -q&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Only display errors and warnings.<br />
&nbsp;<wbr>&#8211;remove&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Remove the option from the configuration<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>file.<br />
&nbsp;<wbr>&#8211;scope ARG&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Reduce the scope to the specified<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>configuration file.<br />
&nbsp;<wbr>&#8211;usage&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show usage message and options.<br />
&nbsp;<wbr>&#8211;verbose, -v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Display more information. </p>
<p> See also: configuration </p>
<p> Display, set or remove a configuration option. </p>
<p> Display the active value for a given option. </p>
<p> If &#8211;all is specified, NAME is interpreted as a regular expression and all matching options are displayed mentioning their scope. The active value that bzr will take into account is the first one displayed for each option. </p>
<p> If no NAME is given, &#8211;all .* is implied. </p>
<p> Setting a value is achieved by using name=value without spaces. The value is set in the most relevant scope and can be checked by displaying the option again. </p>
<h3>bzr conflicts</h3>
<p> Options:<br />
&nbsp;<wbr>&#8211;directory ARG, -d&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Branch to operate on, instead of working<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>directory.<br />
&nbsp;<wbr>&#8211;help, -h&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show help message.<br />
&nbsp;<wbr>&#8211;quiet, -q&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Only display errors and warnings.<br />
&nbsp;<wbr>&#8211;text&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>List paths of files with text conflicts.<br />
&nbsp;<wbr>&#8211;usage&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show usage message and options.<br />
&nbsp;<wbr>&#8211;verbose, -v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Display more information. </p>
<p> See also: conflict-types, resolve </p>
<p> List files with conflicts. </p>
<p> Merge will do its best to combine the changes in two branches, but there are some kinds of problems only a human can fix. When it encounters those, it will mark a conflict. A conflict means that you need to fix something, before you can commit. </p>
<p> Conflicts normally are listed as short, human-readable messages. If &#8211;text is supplied, the pathnames of files with text conflicts are listed, instead. (This is useful for editing all files with text conflicts.) </p>
<p> Use bzr resolve when you have fixed a problem. </p>
<h3>bzr del</h3>
<p> Alias for &quot;remove&quot;, see &quot;bzr remove&quot;.</p>
<h3>bzr deleted</h3>
<p> Options:<br />
&nbsp;<wbr>&#8211;directory ARG, -d&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Branch to operate on, instead of working<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>directory.<br />
&nbsp;<wbr>&#8211;help, -h&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show help message.<br />
&nbsp;<wbr>&#8211;quiet, -q&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Only display errors and warnings.<br />
&nbsp;<wbr>&#8211;show-ids&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show internal object ids.<br />
&nbsp;<wbr>&#8211;usage&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show usage message and options.<br />
&nbsp;<wbr>&#8211;verbose, -v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Display more information. </p>
<p> See also: ls, status </p>
<p> List files deleted in the working tree.<br />
&nbsp;<wbr> </p>
<h3>bzr di</h3>
<p> Alias for &quot;diff&quot;, see &quot;bzr diff&quot;.</p>
<h3>bzr dif</h3>
<p> Alias for &quot;diff&quot;, see &quot;bzr diff&quot;.</p>
<h3>bzr diff [FILE&#8230;]</h3>
<p> Options:<br />
&nbsp;<wbr>&#8211;change ARG, -c&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Select changes introduced by the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>specified revision. See also&nbsp;<wbr>&quot;help<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>revisionspec&quot;.<br />
&nbsp;<wbr>&#8211;diff-options ARG&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Pass these options to the external diff<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>program.<br />
&nbsp;<wbr>&#8211;format ARG, -F&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Diff format to use.<br />
&nbsp;<wbr>&#8211;help, -h&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show help message.<br />
&nbsp;<wbr>&#8211;new ARG&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Branch/tree to compare to.<br />
&nbsp;<wbr>&#8211;old ARG&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Branch/tree to compare from.<br />
&nbsp;<wbr>&#8211;prefix ARG, -p&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Set prefixes added to old and new<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>filenames, as two values separated by a<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>colon.&nbsp;<wbr>(eg&nbsp;<wbr>&quot;old/:new/&quot;).<br />
&nbsp;<wbr>&#8211;quiet, -q&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Only display errors and warnings.<br />
&nbsp;<wbr>&#8211;revision ARG, -r&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr>&quot;help revisionspec&quot;&nbsp;<wbr>for details.<br />
&nbsp;<wbr>&#8211;usage&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show usage message and options.<br />
&nbsp;<wbr>&#8211;using ARG&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Use this command to compare files.<br />
&nbsp;<wbr>&#8211;verbose, -v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Display more information. </p>
<p> Aliases: di, dif </p>
<p> See also: status </p>
<p> Show differences in the working tree, between revisions or branches. </p>
<p> If no arguments are given, all changes for the current tree are listed. If files are given, only the changes in those files are listed. Remote and multiple branches can be compared by using the &#8211;old and &#8211;new options. If not provided, the default for both is derived from the first argument, if any, or the current tree if no arguments are given. </p>
<p> &quot;bzr diff -p1&quot; is equivalent to &quot;bzr diff &#8211;prefix old/:new/&quot;, and produces patches suitable for &quot;patch -p1&quot;. </p>
<p> Note that when using the -r argument with a range of revisions, the differences are computed between the two specified revisions. That is, the command does not show the changes introduced by the first revision in the range. This differs from the interpretation of revision ranges used by &quot;bzr log&quot; which includes the first revision in the range. </p>
<p> Exit values:<br />
&nbsp;<wbr>1 &#8211; changed<br />
&nbsp;<wbr>2 &#8211; unrepresentable changes<br />
&nbsp;<wbr>3 &#8211; error<br />
&nbsp;<wbr>0 &#8211; no change </p>
<p> Examples:<br />
&nbsp;<wbr>Shows the difference in the working tree versus the last commit: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>bzr diff </p>
<p>&nbsp;<wbr>Difference between the working tree and revision 1: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>bzr diff -r1 </p>
<p>&nbsp;<wbr>Difference between revision 3 and revision 1: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>bzr diff -r1..3 </p>
<p>&nbsp;<wbr>Difference between revision 3 and revision 1 for branch xxx: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>bzr diff -r1..3 xxx </p>
<p>&nbsp;<wbr>The changes introduced by revision 2&nbsp;<wbr>(equivalent to -r1..2): </p>
<p>&nbsp;<wbr>&nbsp;<wbr>bzr diff -c2 </p>
<p>&nbsp;<wbr>To see the changes introduced by revision X:<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>bzr diff -cX </p>
<p>&nbsp;<wbr>Note that in the case of a merge, the -c option shows the changes<br />
&nbsp;<wbr>compared to the left hand parent. To see the changes against<br />
&nbsp;<wbr>another parent, use: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>bzr diff -r&lt;chosen_parent&gt;..X </p>
<p>&nbsp;<wbr>The changes between the current revision and the previous revision<br />
&nbsp;<wbr>(equivalent to -c-1 and -r-2..-1) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>bzr diff -r-2.. </p>
<p>&nbsp;<wbr>Show just the differences for file NEWS: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>bzr diff NEWS </p>
<p>&nbsp;<wbr>Show the differences in working tree xxx for file NEWS: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>bzr diff xxx/NEWS </p>
<p>&nbsp;<wbr>Show the differences from branch xxx to this working tree: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>bzr diff &#8211;old xxx </p>
<p>&nbsp;<wbr>Show the differences between two branches for file NEWS: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>bzr diff &#8211;old xxx &#8211;new yyy NEWS </p>
<p>&nbsp;<wbr>Same as&nbsp;<wbr>&#8216;bzr diff&#8217;&nbsp;<wbr>but prefix paths with old/&nbsp;<wbr>and new/: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>bzr diff &#8211;prefix old/:new/<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>Show the differences using a custom diff program with options:<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>bzr diff &#8211;using&nbsp;<wbr>/usr/bin/diff &#8211;diff-options -wu </p>
<h3>bzr dpush [LOCATION]</h3>
<p> Options:<br />
&nbsp;<wbr>&#8211;directory ARG, -d&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Branch to push from, rather than the one<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>containing the working directory.<br />
&nbsp;<wbr>&#8211;help, -h&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show help message.<br />
&nbsp;<wbr>&#8211;no-rebase&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Do not rebase after push.<br />
&nbsp;<wbr>&#8211;quiet, -q&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Only display errors and warnings.<br />
&nbsp;<wbr>&#8211;remember&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Remember the specified location as a<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>default.<br />
&nbsp;<wbr>&#8211;strict&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Refuse to push if there are uncommitted<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>changes in the working tree, &#8211;no-strict<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>disables the check.<br />
&nbsp;<wbr>&#8211;usage&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show usage message and options.<br />
&nbsp;<wbr>&#8211;verbose, -v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Display more information. </p>
<p> Push into a different VCS without any custom bzr metadata. </p>
<p> This will afterwards rebase the local branch on the remote branch unless the &#8211;no-rebase option is used, in which case the two branches will be out of sync after the push. </p>
<h3>bzr export DEST [BRANCH_OR_SUBDIR]</h3>
<p> Options:<br />
&nbsp;<wbr>&#8211;directory ARG, -d&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Branch to operate on, instead of working<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>directory.<br />
&nbsp;<wbr>&#8211;filters&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Apply content filters to export the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>convenient form.<br />
&nbsp;<wbr>&#8211;format ARG&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Type of file to export to.<br />
&nbsp;<wbr>&#8211;help, -h&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show help message.<br />
&nbsp;<wbr>&#8211;per-file-timestamps&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Set modification time of files to that<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>of the last revision in which it was<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>changed.<br />
&nbsp;<wbr>&#8211;quiet, -q&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Only display errors and warnings.<br />
&nbsp;<wbr>&#8211;revision ARG, -r&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr>&quot;help revisionspec&quot;&nbsp;<wbr>for details.<br />
&nbsp;<wbr>&#8211;root ARG&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Name of the root directory inside the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>exported file.<br />
&nbsp;<wbr>&#8211;uncommitted&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Export the working tree contents rather<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>than that of the last revision.<br />
&nbsp;<wbr>&#8211;usage&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show usage message and options.<br />
&nbsp;<wbr>&#8211;verbose, -v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Display more information. </p>
<p> Export current or past revision to a destination directory or archive. </p>
<p> If no revision is specified this exports the last committed revision. </p>
<p> Format may be an &quot;exporter&quot; name, such as tar, tgz, tbz2. If none is given, try to find the format with the extension. If no extension is found exports to a directory (equivalent to &#8211;format=dir). </p>
<p> If root is supplied, it will be used as the root directory inside container formats (tar, zip, etc). If it is not supplied it will default to the exported filename. The root option has no effect for &#8216;dir&#8217; format. </p>
<p> If branch is omitted then the branch containing the current working directory will be used. </p>
<p> Note: Export of tree with non-ASCII filenames to zip is not supported. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>=================&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=========================<br />
&nbsp;<wbr>&nbsp;<wbr>Supported formats&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Autodetected by extension<br />
&nbsp;<wbr>&nbsp;<wbr>=================&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=========================<br />
&nbsp;<wbr>&nbsp;<wbr>dir&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(none)<br />
&nbsp;<wbr>&nbsp;<wbr>tar&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>.tar<br />
&nbsp;<wbr>&nbsp;<wbr>tbz2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>.tar.bz2, .tbz2<br />
&nbsp;<wbr>&nbsp;<wbr>tgz&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>.tar.gz, .tgz<br />
&nbsp;<wbr>&nbsp;<wbr>zip&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>.zip<br />
&nbsp;<wbr>&nbsp;<wbr>=================&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>========================= </p>
<h3>bzr get</h3>
<p> Alias for &quot;branch&quot;, see &quot;bzr branch&quot;.</p>
<h3>bzr help [TOPIC]</h3>
<p> Options:<br />
&nbsp;<wbr>&#8211;help, -h&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show help message.<br />
&nbsp;<wbr>&#8211;long&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show help on all commands.<br />
&nbsp;<wbr>&#8211;quiet, -q&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Only display errors and warnings.<br />
&nbsp;<wbr>&#8211;usage&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show usage message and options.<br />
&nbsp;<wbr>&#8211;verbose, -v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Display more information. </p>
<p> Aliases: ?, &#8211;help, -?, -h </p>
<p> See also: topics </p>
<p> Show help on a command or other topic.<br />
&nbsp;<wbr> </p>
<h3>bzr ignore [NAME_PATTERN&#8230;]</h3>
<p> Options:<br />
&nbsp;<wbr>&#8211;default-rules&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Display the default ignore rules that<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>bzr uses.<br />
&nbsp;<wbr>&#8211;directory ARG, -d&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Branch to operate on, instead of working<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>directory.<br />
&nbsp;<wbr>&#8211;help, -h&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show help message.<br />
&nbsp;<wbr>&#8211;quiet, -q&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Only display errors and warnings.<br />
&nbsp;<wbr>&#8211;usage&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show usage message and options.<br />
&nbsp;<wbr>&#8211;verbose, -v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Display more information. </p>
<p> See also: ignored, patterns, status </p>
<p> Ignore specified files or patterns. </p>
<p> See &#8220;bzr help patterns&#8220; for details on the syntax of patterns. </p>
<p> If a .bzrignore file does not exist, the ignore command will create one and add the specified files or patterns to the newly created file. The ignore command will also automatically add the the use of the ignore command will require an explicit add command. </p>
<p> To remove patterns from the ignore list, edit the .bzrignore file. After adding, editing or deleting that file either indirectly by using this command or directly by using an editor, be sure to commit it. </p>
<p> Bazaar also supports a global ignore file ~/.bazaar/ignore. On Windows the global ignore file can be found in the application data directory as C:\Documents and Settings\&lt;user&gt;\Application Data\Bazaar\2.0\ignore. Global ignores are not touched by this command. The global ignore file can be edited directly using an editor. </p>
<p> Patterns prefixed with &#8216;!&#8217; are exceptions to ignore patterns and take precedence over regular ignores. Such exceptions are used to specify files that should be versioned which would otherwise be ignored. </p>
<p> Patterns prefixed with &#8216;!!&#8217; act as regular ignore patterns, but have precedence over the &#8216;!&#8217; exception patterns. </p>
<p> Notes:<br />
&nbsp;<wbr> * Ignore patterns containing shell wildcards must be quoted from<br />
&nbsp;<wbr>&nbsp;<wbr>the shell on Unix. </p>
<p> * Ignore patterns starting with &quot;#&quot; act as comments in the ignore file.<br />
&nbsp;<wbr>&nbsp;<wbr>To ignore patterns that begin with that character, use the&nbsp;<wbr>&quot;RE:&quot;&nbsp;<wbr>prefix. </p>
<p> Examples:<br />
&nbsp;<wbr>Ignore the top level Makefile: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>bzr ignore ./Makefile </p>
<p>&nbsp;<wbr>Ignore .class files in all directories&#8230;: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>bzr ignore&nbsp;<wbr>&quot;*.class&quot; </p>
<p>&nbsp;<wbr>&#8230;but do not ignore&nbsp;<wbr>&quot;special.class&quot;: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>bzr ignore&nbsp;<wbr>&quot;!special.class&quot; </p>
<p>&nbsp;<wbr>Ignore files whose name begins with the&nbsp;<wbr>&quot;#&quot;&nbsp;<wbr>character: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>bzr ignore&nbsp;<wbr>&quot;RE:^#&quot; </p>
<p>&nbsp;<wbr>Ignore .o files under the lib directory: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>bzr ignore&nbsp;<wbr>&quot;lib/**/*.o&quot; </p>
<p>&nbsp;<wbr>Ignore .o files under the lib directory: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>bzr ignore&nbsp;<wbr>&quot;RE:lib/.*\.o&quot; </p>
<p>&nbsp;<wbr>Ignore everything but the&nbsp;<wbr>&quot;debian&quot;&nbsp;<wbr>toplevel directory: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>bzr ignore&nbsp;<wbr>&quot;RE:(?!debian/).*&quot;<br />
&nbsp;<wbr><br />
&nbsp;<wbr>Ignore everything except the&nbsp;<wbr>&quot;local&quot;&nbsp;<wbr>toplevel directory,<br />
&nbsp;<wbr>but always ignore autosave files ending in&nbsp;<wbr>~, even under local/:<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>bzr ignore&nbsp;<wbr>&quot;*&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>bzr ignore&nbsp;<wbr>&quot;!./local&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>bzr ignore&nbsp;<wbr>&quot;!!*~&quot; </p>
<h3>bzr ignored</h3>
<p> Options:<br />
&nbsp;<wbr>&#8211;directory ARG, -d&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Branch to operate on, instead of working<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>directory.<br />
&nbsp;<wbr>&#8211;help, -h&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show help message.<br />
&nbsp;<wbr>&#8211;quiet, -q&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Only display errors and warnings.<br />
&nbsp;<wbr>&#8211;usage&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show usage message and options.<br />
&nbsp;<wbr>&#8211;verbose, -v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Display more information. </p>
<p> See also: ignore, ls </p>
<p> List ignored files and the patterns that matched them. </p>
<p> List all the ignored files and the ignore pattern that caused the file to be ignored. </p>
<p> Alternatively, to list just the files: </p>
<p>&nbsp;<wbr>bzr ls &#8211;ignored </p>
<h3>bzr info [LOCATION]</h3>
<p> Options:<br />
&nbsp;<wbr>&#8211;help, -h&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show help message.<br />
&nbsp;<wbr>&#8211;quiet, -q&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Only display errors and warnings.<br />
&nbsp;<wbr>&#8211;usage&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show usage message and options.<br />
&nbsp;<wbr>&#8211;verbose, -v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Display more information. </p>
<p> See also: repositories, revno, working-trees </p>
<p> Show information about a working tree, branch or repository. </p>
<p> This command will show all known locations and formats associated to the tree, branch or repository. </p>
<p> In verbose mode, statistical information is included with each report. To see extended statistic information, use a verbosity level of 2 or higher by specifying the verbose option multiple times, e.g. -vv. </p>
<p> Branches and working trees will also report any missing revisions. </p>
<p> Examples: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Display information on the format and related locations: </p>
<p>&nbsp;<wbr>bzr info </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Display the above together with extended format information and<br />
&nbsp;<wbr>&nbsp;<wbr>basic statistics&nbsp;<wbr>(like the number of files in the working tree and<br />
&nbsp;<wbr>&nbsp;<wbr>number of revisions in the branch and repository): </p>
<p>&nbsp;<wbr>bzr info -v </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Display the above together with number of committers to the branch: </p>
<p>&nbsp;<wbr>bzr info -vv </p>
<h3>bzr init [LOCATION]</h3>
<p> Options:<br />
&nbsp;<wbr>&#8211;append-revisions-only&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Never change revnos or the existing log.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Append revisions to it only.<br />
&nbsp;<wbr>&#8211;create-prefix&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Create the path leading up to the branch<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>if it does not already exist.<br />
&nbsp;<wbr>&#8211;format ARG&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Specify a format for this branch. See<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&quot;help formats&quot;.<br />
&nbsp;<wbr>&#8211;2a&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Format for the bzr 2.0 series. Uses<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>group-compress storage. Provides rich<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>roots which are a one-way transition.<br />
&nbsp;<wbr>&#8211;default&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Format for the bzr 2.0 series. Uses<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>group-compress storage. Provides rich<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>roots which are a one-way transition.<br />
&nbsp;<wbr>&#8211;development-colo&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>The 2a format with experimental support<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>for colocated branches.<br />
&nbsp;<wbr>&#8211;pack-0.92&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Pack-based format used in 1.x series.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Introduced in 0.92. Interoperates with<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>bzr repositories before 0.92 but cannot<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>be read by bzr&nbsp;<wbr>&lt;&nbsp;<wbr>0.92.<br />
&nbsp;<wbr>&#8211;help, -h&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show help message.<br />
&nbsp;<wbr>&#8211;no-tree&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Create a branch without a working tree.<br />
&nbsp;<wbr>&#8211;quiet, -q&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Only display errors and warnings.<br />
&nbsp;<wbr>&#8211;usage&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show usage message and options.<br />
&nbsp;<wbr>&#8211;verbose, -v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Display more information. </p>
<p> See also: branch, checkout, init-repository </p>
<p> Make a directory into a versioned branch. </p>
<p> Use this to create an empty branch, or before importing an existing project. </p>
<p> If there is a repository in a parent directory of the location, then the history of the branch will be stored in the repository. Otherwise init creates a standalone branch which carries its own history in the .bzr directory. </p>
<p> If there is already a branch at the location but it has no working tree, the tree can be populated with &#8216;bzr checkout&#8217;. </p>
<p> Recipe for importing a tree of files: </p>
<p>&nbsp;<wbr>cd&nbsp;<wbr>~/project<br />
&nbsp;<wbr>bzr init<br />
&nbsp;<wbr>bzr add .<br />
&nbsp;<wbr>bzr status<br />
&nbsp;<wbr>bzr commit -m&nbsp;<wbr>&quot;imported project&quot; </p>
<h3>bzr init-repo</h3>
<p> Alias for &quot;init-repository&quot;, see &quot;bzr init-repository&quot;.</p>
<h3>bzr init-repository LOCATION</h3>
<p> Options:<br />
&nbsp;<wbr>&#8211;format ARG&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Specify a format for this repository.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr>&quot;bzr help formats&quot;&nbsp;<wbr>for details.<br />
&nbsp;<wbr>&#8211;2a&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Format for the bzr 2.0 series. Uses<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>group-compress storage. Provides rich<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>roots which are a one-way transition.<br />
&nbsp;<wbr>&#8211;default&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Format for the bzr 2.0 series. Uses<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>group-compress storage. Provides rich<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>roots which are a one-way transition.<br />
&nbsp;<wbr>&#8211;development-colo&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>The 2a format with experimental support<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>for colocated branches.<br />
&nbsp;<wbr>&#8211;pack-0.92&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Pack-based format used in 1.x series.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Introduced in 0.92. Interoperates with<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>bzr repositories before 0.92 but cannot<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>be read by bzr&nbsp;<wbr>&lt;&nbsp;<wbr>0.92.<br />
&nbsp;<wbr>&#8211;help, -h&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show help message.<br />
&nbsp;<wbr>&#8211;no-trees&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Branches in the repository will default<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>to not having a working tree.<br />
&nbsp;<wbr>&#8211;quiet, -q&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Only display errors and warnings.<br />
&nbsp;<wbr>&#8211;usage&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show usage message and options.<br />
&nbsp;<wbr>&#8211;verbose, -v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Display more information. </p>
<p> Alias: init-repo </p>
<p> See also: branch, checkout, init, repositories </p>
<p> Create a shared repository for branches to share storage space. </p>
<p> New branches created under the repository directory will store their revisions in the repository, not in the branch directory. For branches with shared history, this reduces the amount of storage needed and speeds up the creation of new branches. </p>
<p> If the &#8211;no-trees option is given then the branches in the repository will not have working trees by default. They will still exist as directories on disk, but they will not have separate copies of the files at a certain revision. This can be useful for repositories that store branches which are interacted with through checkouts or remote branches, such as on a server. </p>
<p> Examples:<br />
&nbsp;<wbr>Create a shared repository holding just branches: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>bzr init-repo &#8211;no-trees repo<br />
&nbsp;<wbr>&nbsp;<wbr>bzr init repo/trunk </p>
<p>&nbsp;<wbr>Make a lightweight checkout elsewhere: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>bzr checkout &#8211;lightweight repo/trunk trunk-checkout<br />
&nbsp;<wbr>&nbsp;<wbr>cd trunk-checkout<br />
&nbsp;<wbr>&nbsp;<wbr>(add files here) </p>
<h3>bzr join TREE</h3>
<p> Options:<br />
&nbsp;<wbr>&#8211;help, -h&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show help message.<br />
&nbsp;<wbr>&#8211;quiet, -q&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Only display errors and warnings.<br />
&nbsp;<wbr>&#8211;usage&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show usage message and options.<br />
&nbsp;<wbr>&#8211;verbose, -v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Display more information. </p>
<p> See also: split </p>
<p> Combine a tree into its containing tree. </p>
<p> This command requires the target tree to be in a rich-root format. </p>
<p> The TREE argument should be an independent tree, inside another tree, but not part of it. (Such trees can be produced by &quot;bzr split&quot;, but also by running &quot;bzr branch&quot; with the target inside a tree.) </p>
<p> The result is a combined tree, with the subtree no longer an independent part. This is marked as a merge of the subtree into the containing tree, and all history is preserved. </p>
<h3>bzr log [FILE&#8230;]</h3>
<p> Options:<br />
&nbsp;<wbr>&#8211;authors ARG&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>What names to list as authors &#8211; first,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>all or committer.<br />
&nbsp;<wbr>&#8211;change ARG, -c&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show just the specified revision. See<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>also&nbsp;<wbr>&quot;help revisionspec&quot;.<br />
&nbsp;<wbr>&#8211;exclude-common-ancestry Display only the revisions that are not<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>part of both ancestries&nbsp;<wbr>(require<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-rX..Y).<br />
&nbsp;<wbr>&#8211;forward&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show from oldest to newest.<br />
&nbsp;<wbr>&#8211;help, -h&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show help message.<br />
&nbsp;<wbr>&#8211;include-merged&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show merged revisions like &#8211;levels 0<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>does.<br />
&nbsp;<wbr>&#8211;levels N, -n&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Number of levels to display &#8211; 0 for all,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1 for flat.<br />
&nbsp;<wbr>&#8211;limit N, -l&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Limit the output to the first N<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>revisions.<br />
&nbsp;<wbr>&#8211;log-format ARG&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Use specified log format.<br />
&nbsp;<wbr>&#8211;gnu-changelog&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Format used by GNU ChangeLog files.<br />
&nbsp;<wbr>&#8211;line&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Log format with one line per revision.<br />
&nbsp;<wbr>&#8211;long&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Detailed log format.<br />
&nbsp;<wbr>&#8211;short&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Moderately short log format.<br />
&nbsp;<wbr>&#8211;match ARG, -m&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show revisions whose properties match<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>this expression.<br />
&nbsp;<wbr>&#8211;match-author ARG&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show revisions whose authors match this<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>expression.<br />
&nbsp;<wbr>&#8211;match-bugs ARG&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show revisions whose bugs match this<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>expression.<br />
&nbsp;<wbr>&#8211;match-committer ARG&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show revisions whose committer matches<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>this expression.<br />
&nbsp;<wbr>&#8211;match-message ARG&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show revisions whose message matches<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>this expression.<br />
&nbsp;<wbr>&#8211;omit-merges&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Do not report commits with more than one<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>parent.<br />
&nbsp;<wbr>&#8211;quiet, -q&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Only display errors and warnings.<br />
&nbsp;<wbr>&#8211;revision ARG, -r&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr>&quot;help revisionspec&quot;&nbsp;<wbr>for details.<br />
&nbsp;<wbr>&#8211;show-diff, -p&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show changes made in each revision as a<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>patch.<br />
&nbsp;<wbr>&#8211;show-ids&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show internal object ids.<br />
&nbsp;<wbr>&#8211;signatures&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show digital signature validity.<br />
&nbsp;<wbr>&#8211;timezone ARG&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Display timezone as local, original, or<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>utc.<br />
&nbsp;<wbr>&#8211;usage&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show usage message and options.<br />
&nbsp;<wbr>&#8211;verbose, -v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show files changed in each revision. </p>
<p> See also: log-formats, revisionspec </p>
<p> Show historical log for a branch or subset of a branch. </p>
<p> log is bzr&#8217;s default tool for exploring the history of a branch. The branch to use is taken from the first parameter. If no parameters are given, the branch containing the working directory is logged. Here are some simple examples: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>bzr log&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>log the current branch<br />
&nbsp;<wbr>&nbsp;<wbr>bzr log foo.py&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>log a file in its branch<br />
&nbsp;<wbr>&nbsp;<wbr>bzr log&nbsp;<wbr><a rel="nofollow" href="http://server/branch">http://server/branch</a>&nbsp;<wbr>&nbsp;<wbr>log a branch on a server </p>
<p> The filtering, ordering and information shown for each revision can be controlled as explained below. By default, all revisions are shown sorted (topologically) so that newer revisions appear before older ones and descendants always appear before ancestors. If displayed, merged revisions are shown indented under the revision in which they were merged. </p>
<p> Output control: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>The log format controls how information about each revision is<br />
&nbsp;<wbr>&nbsp;<wbr>displayed. The standard log formats are called&nbsp;<wbr>&#8220;long&#8220;,&nbsp;<wbr>&#8220;short&#8220;<br />
&nbsp;<wbr>&nbsp;<wbr>and&nbsp;<wbr>&#8220;line&#8220;. The default is long. See&nbsp;<wbr>&#8220;bzr help log-formats&#8220;<br />
&nbsp;<wbr>&nbsp;<wbr>for more details on log formats. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>The following options can be used to control what information is<br />
&nbsp;<wbr>&nbsp;<wbr>displayed: </p>
<p>&nbsp;<wbr>-l N&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>display a maximum of N revisions<br />
&nbsp;<wbr>-n N&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>display N levels of revisions&nbsp;<wbr>(0 for all, 1 for collapsed)<br />
&nbsp;<wbr>-v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>display a status summary&nbsp;<wbr>(delta)&nbsp;<wbr>for each revision<br />
&nbsp;<wbr>-p&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>display a diff&nbsp;<wbr>(patch)&nbsp;<wbr>for each revision<br />
&nbsp;<wbr>&#8211;show-ids&nbsp;<wbr>&nbsp;<wbr>display revision-ids&nbsp;<wbr>(and file-ids), not just revnos </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Note that the default number of levels to display is a function of the<br />
&nbsp;<wbr>&nbsp;<wbr>log format. If the -n option is not used, the standard log formats show<br />
&nbsp;<wbr>&nbsp;<wbr>just the top level&nbsp;<wbr>(mainline). </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Status summaries are shown using status flags like A, M, etc. To see<br />
&nbsp;<wbr>&nbsp;<wbr>the changes explained using words like&nbsp;<wbr>&#8220;added&#8220;&nbsp;<wbr>and&nbsp;<wbr>&#8220;modified&#8220;<br />
&nbsp;<wbr>&nbsp;<wbr>instead, use the -vv option. </p>
<p> Ordering control: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>To display revisions from oldest to newest, use the &#8211;forward option.<br />
&nbsp;<wbr>&nbsp;<wbr>In most cases, using this option will have little impact on the total<br />
&nbsp;<wbr>&nbsp;<wbr>time taken to produce a log, though &#8211;forward does not incrementally<br />
&nbsp;<wbr>&nbsp;<wbr>display revisions like &#8211;reverse does when it can. </p>
<p> Revision filtering: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>The -r option can be used to specify what revision or range of revisions<br />
&nbsp;<wbr>&nbsp;<wbr>to filter against. The various forms are shown below: </p>
<p>&nbsp;<wbr>-rX&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>display revision X<br />
&nbsp;<wbr>-rX..&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>display revision X and later<br />
&nbsp;<wbr>-r..Y&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>display up to and including revision Y<br />
&nbsp;<wbr>-rX..Y&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>display from X to Y inclusive </p>
<p>&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr>&#8220;bzr help revisionspec&#8220;&nbsp;<wbr>for details on how to specify X and Y.<br />
&nbsp;<wbr>&nbsp;<wbr>Some common examples are given below: </p>
<p>&nbsp;<wbr>-r-1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show just the tip<br />
&nbsp;<wbr>-r-10..&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show the last 10 mainline revisions<br />
&nbsp;<wbr>-rsubmit:..&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show what&#8217;s new on this branch<br />
&nbsp;<wbr>-rancestor:path..&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show changes since the common ancestor of this<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>branch and the one at location path<br />
&nbsp;<wbr>-rdate:yesterday..&nbsp;<wbr>&nbsp;<wbr>show changes since yesterday </p>
<p>&nbsp;<wbr>&nbsp;<wbr>When logging a range of revisions using -rX..Y, log starts at<br />
&nbsp;<wbr>&nbsp;<wbr>revision Y and searches back in history through the primary<br />
&nbsp;<wbr>&nbsp;<wbr>(&quot;left-hand&quot;)&nbsp;<wbr>parents until it finds X. When logging just the<br />
&nbsp;<wbr>&nbsp;<wbr>top level&nbsp;<wbr>(using -n1), an error is reported if X is not found<br />
&nbsp;<wbr>&nbsp;<wbr>along the way. If multi-level logging is used&nbsp;<wbr>(-n0), X may be<br />
&nbsp;<wbr>&nbsp;<wbr>a nested merge revision and the log will be truncated accordingly. </p>
<p> Path filtering: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>If parameters are given and the first one is not a branch, the log<br />
&nbsp;<wbr>&nbsp;<wbr>will be filtered to show only those revisions that changed the<br />
&nbsp;<wbr>&nbsp;<wbr>nominated files or directories. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Filenames are interpreted within their historical context. To log a<br />
&nbsp;<wbr>&nbsp;<wbr>deleted file, specify a revision range so that the file existed at<br />
&nbsp;<wbr>&nbsp;<wbr>the end or start of the range. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Historical context is also important when interpreting pathnames of<br />
&nbsp;<wbr>&nbsp;<wbr>renamed files/directories. Consider the following example: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>revision 1: add tutorial.txt<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>revision 2: modify tutorial.txt<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>revision 3: rename tutorial.txt to guide.txt;&nbsp;<wbr>add tutorial.txt </p>
<p>&nbsp;<wbr>&nbsp;<wbr>In this case: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>&#8220;bzr log guide.txt&#8220;&nbsp;<wbr>will log the file added in revision 1 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>&#8220;bzr log tutorial.txt&#8220;&nbsp;<wbr>will log the new file added in revision 3 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>&#8220;bzr log -r2 -p tutorial.txt&#8220;&nbsp;<wbr>will show the changes made to<br />
&nbsp;<wbr>the original file in revision 2. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>&#8220;bzr log -r2 -p guide.txt&#8220;&nbsp;<wbr>will display an error message as there<br />
&nbsp;<wbr>was no file called guide.txt in revision 2. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Renames are always followed by log. By design, there is no need to<br />
&nbsp;<wbr>&nbsp;<wbr>explicitly ask for this&nbsp;<wbr>(and no way to stop logging a file back<br />
&nbsp;<wbr>&nbsp;<wbr>until it was last renamed). </p>
<p> Other filtering: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>The &#8211;match option can be used for finding revisions that match a<br />
&nbsp;<wbr>&nbsp;<wbr>regular expression in a commit message, committer, author or bug.<br />
&nbsp;<wbr>&nbsp;<wbr>Specifying the option several times will match any of the supplied<br />
&nbsp;<wbr>&nbsp;<wbr>expressions. &#8211;match-author, &#8211;match-bugs, &#8211;match-committer and<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;match-message can be used to only match a specific field. </p>
<p> Tips &amp; tricks: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>GUI tools and IDEs are often better at exploring history than command<br />
&nbsp;<wbr>&nbsp;<wbr>line tools: you may prefer qlog or viz from qbzr or bzr-gtk, the<br />
&nbsp;<wbr>&nbsp;<wbr>bzr-explorer shell, or the Loggerhead web interface.&nbsp;<wbr>&nbsp;<wbr>See the Plugin<br />
&nbsp;<wbr>&nbsp;<wbr>Guide&nbsp;<wbr>&lt;<a rel="nofollow" href="http://doc.bazaar.canonical.com/plugins/en/">http://doc.bazaar.canonical.com/plugins/en/</a>&gt;&nbsp;<wbr>and<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;<a rel="nofollow" href="http://wiki.bazaar.canonical.com/IDEIntegration">http://wiki.bazaar.canonical.com/IDEIntegration</a>&gt;.&nbsp;<wbr>&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>You may find it useful to add the aliases below to&nbsp;<wbr>&#8220;bazaar.conf&#8220;: </p>
<p>&nbsp;<wbr>[ALIASES]<br />
&nbsp;<wbr>tip&nbsp;<wbr>=&nbsp;<wbr>log -r-1<br />
&nbsp;<wbr>top&nbsp;<wbr>=&nbsp;<wbr>log -l10 &#8211;line<br />
&nbsp;<wbr>show&nbsp;<wbr>=&nbsp;<wbr>log -v -p </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8220;bzr tip&#8220;&nbsp;<wbr>will then show the latest revision while&nbsp;<wbr>&#8220;bzr top&#8220;<br />
&nbsp;<wbr>&nbsp;<wbr>will show the last 10 mainline revisions. To see the details of a<br />
&nbsp;<wbr>&nbsp;<wbr>particular revision X,&nbsp;<wbr>&nbsp;<wbr>&#8220;bzr show -rX&#8220;. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>If you are interested in looking deeper into a particular merge X,<br />
&nbsp;<wbr>&nbsp;<wbr>use&nbsp;<wbr>&#8220;bzr log -n0 -rX&#8220;. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8220;bzr log -v&#8220;&nbsp;<wbr>on a branch with lots of history is currently<br />
&nbsp;<wbr>&nbsp;<wbr>very slow. A fix for this issue is currently under development.<br />
&nbsp;<wbr>&nbsp;<wbr>With or without that fix, it is recommended that a revision range<br />
&nbsp;<wbr>&nbsp;<wbr>be given when using the -v option. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>bzr has a generic full-text matching plugin, bzr-search, that can be<br />
&nbsp;<wbr>&nbsp;<wbr>used to find revisions matching user names, commit messages, etc.<br />
&nbsp;<wbr>&nbsp;<wbr>Among other features, this plugin can find all revisions containing<br />
&nbsp;<wbr>&nbsp;<wbr>a list of words but not others. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>When exploring non-mainline history on large projects with deep<br />
&nbsp;<wbr>&nbsp;<wbr>history, the performance of log can be greatly improved by installing<br />
&nbsp;<wbr>&nbsp;<wbr>the historycache plugin. This plugin buffers historical information<br />
&nbsp;<wbr>&nbsp;<wbr>trading disk space for faster speed. </p>
<h3>bzr ls [PATH]</h3>
<p> Options:<br />
&nbsp;<wbr>&#8211;directory ARG, -d&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Branch to operate on, instead of working<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>directory.<br />
&nbsp;<wbr>&#8211;from-root&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Print paths relative to the root of the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>branch.<br />
&nbsp;<wbr>&#8211;help, -h&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show help message.<br />
&nbsp;<wbr>&#8211;ignored, -i&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Print ignored files.<br />
&nbsp;<wbr>&#8211;kind ARG, -k&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>List entries of a particular kind: file,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>directory, symlink.<br />
&nbsp;<wbr>&#8211;null, -0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Use an ASCII NUL&nbsp;<wbr>(

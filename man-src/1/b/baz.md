---
title: "baz(1)"
name: "baz"
section: "1"
letter: "b"
url: "/docs/linux/man/1-baz/"
description: "baz – arch command line client tool"
---

<h2>NAME</h2>
<p> baz &#8211; arch command line client tool</p>
<h2>SYNOPSIS</h2>
<p> <code>baz</code> <i>command</i> [ <i>command_options</i> ]<br />
 <code>baz</code> <i>command</i> [-h|&#8211;help|-H]<br />
 <code>baz</code> [-h|&#8211;help|-H|-V|&#8211;version]</p>
<h2>DESCRIPTION</h2>
<p> <code>baz</code> is an implementation of <code>arch.</code> </p>
<p> <code>arch</code> is a version control system, which allows you to keep old versions of files and directories (usually source code), keep a log of who, when, and why changes occurred, etc., like SVN, CVS, or RCS. </p>
<p> <code>arch</code> has a number of advantages compared to competing systems. Among these are:<br />
&nbsp;<wbr></p>
<h3>Works on Whole Trees</h3>
<p> <code>arch</code> keeps track of whole trees &#8212; not just individual files. For example, if you change many files in a tree, <code>arch</code> can record all of those changes as a group rather than file-by-file; if you rename files or reorganize a tree, <code>arch</code> can record those tree arrangements along with your changes to file contents. </p>
<h3>Changeset Oriented</h3>
<p> <code>arch</code> doesn&#8217;t simply &quot;snapshot&quot; your project trees. Instead, <code>arch</code> associates each revision with a particular changeset: a description of exactly what has changed. <code>arch</code> provides changeset oriented commands to help you review changesets, merge trees by applying changesets, examine the history of a tree by asking what changesets have been applied to it, and so forth. </p>
<h3>Fully Distributed</h3>
<p> <code>arch</code> doesn&#8217;t rely on a central repository. For example, there is no need to give write access to a project&#8217;s archive to all significant contributors. Instead, each contributor can have their own archive for their work. <code>arch</code> seamlessly operates across archive boundaries.</p>
<h2>COMMAND OVERVIEW</h2>
<h3>Help</h3>
<dl>
<dt><code>baz help [options]</code></p>
<dd> provide help with arch </p>
</dl>
<h3>User Commands</h3>
<dl>
<dt><code>baz my-id [options] [id]</code></p>
<dd> print or change your id </p>
<dt><code>baz my-default-archive [options] [archive]</code></p>
<dd> print or change your default archive </p>
<dt><code>baz register-archive [options] [-d name] location</code></p>
<dd> change an archive location registration </p>
<dt><code>baz whereis-archive [options] archive</code></p>
<dd> print an archive location registration </p>
<dt><code>baz archives [options] [search regular expression]</code></p>
<dd> report registered archives and their locations </p>
<dt><code>baz upgrade [options]</code></p>
<dd> perform an upgrade of local baz settings and data. </p>
</dl>
<h3>Project Tree Commands</h3>
<dl>
<dt><code>baz annotate [options] [path &#8230;]</code></p>
<dd> display the changesets that last modified lines in the tree </p>
<dt><code>baz diff [options] [revision] [&#8211; limit&#8230;]</code></p>
<dd> report about local changes in a project tree </p>
<dt><code>baz init-tree [options] [[archive]/version]</code></p>
<dd> initialize a new project tree </p>
<dt><code>baz tree-id [options] [dir]</code></p>
<dd> Print the tree identifier for a project tree-&gt; </p>
<dt><code>baz tree-root [options] [dir]</code></p>
<dd> find and print the root of a project tree </p>
<dt><code>baz tree-version [options] [NEW VERSION]</code></p>
<dd> Print the default version for a project tree </p>
<dt><code>baz set-tree-version [options] [&#8230;]</code></p>
<dd> This command has been removed; you can use &#8216;baz tree-version &lt;version&gt;&#8217; instead. </p>
<dt><code>baz undo [options] [revision] [&#8211; file &#8230;]</code></p>
<dd> undo and save changes in a project tree </p>
<dt><code>baz redo [options] [changeset]</code></p>
<dd> redo changes in project tree </p>
<dt><code>baz file-diff [options] file [revision]</code></p>
<dd> show local changes to a file </p>
<dt><code>baz switch [options] [package]</code></p>
<dd> change the working trees version to that of package </p>
</dl>
<h3>Project Tree Inventory Commands</h3>
<dl>
<dt><code>baz inventory [options] [dir]*</code></p>
<dd> inventory a source tree </p>
<dt><code>baz status [options] [dir]</code></p>
<dd> scan a project tree and show the tree status. </p>
<dt><code>baz lint [options] [dir]</code></p>
<dd> audit a source tree </p>
<dt><code>baz resolved [options] FILE [FILE &#8230;]</code></p>
<dd> Tell bazaar one or more tree problems have been resolved </p>
<dt><code>baz id [options] file &#8230;</code></p>
<dd> report the inventory id for a file </p>
<dt><code>baz id-tagging-method [options] [method]</code></p>
<dd> print or change a project tree id tagging method </p>
<dt><code>baz add-id [options] file &#8230;</code></p>
<dd> add an explicit inventory id </p>
<dt><code>baz delete-id [options] file &#8230;</code></p>
<dd> remove an explicit inventory id </p>
<dt><code>baz rm [options] file&#8230;</code></p>
<dd> remove a file (or dir, or symlink) and its explicit inventory tag (if any) </p>
<dt><code>baz move-id [options] from to</code></p>
<dd> move an explicit inventory id </p>
<dt><code>baz mv [options] from to OR from1 from2 &#8230; dir</code></p>
<dd> move a file (or dir, or symlink) and its explicit inventory tag (if any) </p>
<dt><code>baz explicit-default [options] [TAG-PREFIX]</code></p>
<dd> print or modify default ids </p>
<dt><code>baz id-tagging-defaults [options]</code></p>
<dd> print the default =tagging-method contents </p>
<dt><code>baz inode-sig [options] [dir]</code></p>
<dd> output the inode signature for a source tree. </p>
</dl>
<h3>Patch Set Commands</h3>
<dl>
<dt><code>baz changeset [options] ORIG MOD DEST [files]</code></p>
<dd> compute a whole-tree changeset </p>
<dt><code>baz apply-changeset [options] CHANGESET [TARGET]</code></p>
<dd> apply a whole-tree changeset </p>
<dt><code>baz show-changeset [options] [dir]</code></p>
<dd> generate a report from a changeset </p>
</dl>
<h3>Archive Transaction Commands</h3>
<dl>
<dt><code>baz make-archive [options] [name] location</code></p>
<dd> create a new archive directory </p>
<dt><code>baz import [options] [[archive]/version]</code></p>
<dd> archive a full-source base-0 revision </p>
<dt><code>baz export [options] [revision] [dir]</code></p>
<dd> export all or some of a tree revision </p>
<dt><code>baz commit [options] [file &#8230;]</code></p>
<dd> archive a changeset-based revision </p>
<dt><code>baz get [options] revision [dir]</code></p>
<dd> construct a project tree for a revision </p>
<dt><code>baz get-changeset [options] revision [dir]</code></p>
<dd> retrieve a changeset from an archive </p>
<dt><code>baz lock-revision [options] VERSION|REVISION</code></p>
<dd> lock (or unlock) an archive revision </p>
<dt><code>baz archive-mirror [options] [from [to] [limit]]</code></p>
<dd> update an archive mirror </p>
</dl>
<h3>Archive Commands</h3>
<dl>
<dt><code>baz abrowse [options] [limit]</code></p>
<dd> print an outline describing archive contents </p>
<dt><code>baz rbrowse [options] [[ARCHIVE_NAME/]LIMIT_REGEX]</code></p>
<dd> print an outline describing an archive&#8217;s contents </p>
<dt><code>baz categories [options] [archive]</code></p>
<dd> list the categories in an archive </p>
<dt><code>baz branches [options] [[archive/]category]</code></p>
<dd> list the branches in an archive category </p>
<dt><code>baz versions [options] [branch]</code></p>
<dd> list the versions in an archive branch </p>
<dt><code>baz revisions [options] [[archive/]version]</code></p>
<dd> list the revisions in an archive version </p>
<dt><code>baz ancestry [options] [revision]</code></p>
<dd> display the ancestory of a revision </p>
<dt><code>baz ancestry-graph [options] [revision]</code></p>
<dd> display the ancestory of a revision </p>
<dt><code>baz change-archive [options] archivename|URL</code></p>
<dd> Alter properties of an archive. For instance, add signatures to an unsigned archive. </p>
<dt><code>baz cat-archive-log [options] revision</code></p>
<dd> print the contents of an archived log entry </p>
<dt><code>baz cacherev [options] [ARCHIVE/[PACKAGE[&#8211;VERSION[&#8211;PATCHLEVEL]]]] or [PATCHLEVEL]</code></p>
<dd> cache a full source tree in an archive </p>
<dt><code>baz cachedrevs [options] [version]</code></p>
<dd> list cached revisions in an archive </p>
<dt><code>baz uncacherev [options] revision [dir]</code></p>
<dd> remove a cached full source tree from an archive </p>
<dt><code>baz archive-meta-info [options] [archive/]item-name</code></p>
<dd> report meta-info from an archive </p>
<dt><code>baz archive-snapshot [options] dir [[archive/]limit]</code></p>
<dd> update an archive snapshot </p>
<dt><code>baz archive-version [options] [archive]</code></p>
<dd> list the archive-version in an archive </p>
<dt><code>baz archive-fixup [options] [archive]</code></p>
<dd> fix ancillary files (e.g. .listing files) in an archive </p>
</dl>
<h3>Patch Log Commands</h3>
<dl>
<dt><code>baz make-log [options] [version]</code></p>
<dd> initialize a new log file entry </p>
<dt><code>baz log-versions [options]</code></p>
<dd> list patch log versions in a project tree </p>
<dt><code>baz add-log-version [options] [archive]/version</code></p>
<dd> add a patch log version to a project tree </p>
<dt><code>baz remove-log-version [options] [archive]/version</code></p>
<dd> remove a version&#8217;s patch log from a project tree </p>
<dt><code>baz log [-f|&#8211;full] [-r start[:end]]</code></p>
<dd> Show the log messages for the working directory or given </p>
<dt><code>baz logs [options] [[archive]/version &#8230;]</code></p>
<dd> list patch logs for a version in a project tree </p>
<dt><code>baz cat-log [options] revision-spec</code></p>
<dd> print the contents of a project tree log entry </p>
<dt><code>baz changelog [options] [[archive]/version]</code></p>
<dd> generate a ChangeLog from a patch log </p>
<dt><code>baz log-for-merge [options] [[archive]/version]</code></p>
<dd> generate a log entry body for a merge </p>
<dt><code>baz merges [options] INTO [FROM]</code></p>
<dd> report where two branches have been merged </p>
<dt><code>baz new-merges [options] [[archive]/version]</code></p>
<dd> list tree patches new to a version </p>
</dl>
<h3>Multi-project Configuration Commands</h3>
<dl>
<dt><code>baz build-config [options] config</code></p>
<dd> instantiate a multi-project config </p>
<dt><code>baz cat-config [options] config</code></p>
<dd> output information about a multi-project config </p>
</dl>
<h3>Commands for Branching and Merging</h3>
<dl>
<dt><code>baz branch [options] [SOURCE] BRANCH</code></p>
<dd> create a branch </p>
<dt><code>baz merge [options] [FROM]</code></p>
<dd> merge from another branch </p>
<dt><code>baz update [options] [version/revision]</code></p>
<dd> update a project tree to reflect recent archived changes </p>
<dt><code>baz replay [options] [version/revision&#8230;]</code></p>
<dd> apply revision changesets to a project tree </p>
<dt><code>baz apply-delta [options] FROM(REVISION|DIR) TO(REVISION|DIR)</code></p>
<dd> compute a changeset between any two trees or revisions and apply it to a project tree </p>
<dt><code>baz missing [options] [version]</code></p>
<dd> print patches missing from a project tree </p>
<dt><code>baz join-branch [options] version</code></p>
<dd> add a version as an ancestor of a project tree </p>
<dt><code>baz sync-tree [options] revision</code></p>
<dd> unify a project tree&#8217;s patch-log with a given revision </p>
<dt><code>baz delta [options] (REVISION|TREE)-A (REVISION|TREE)-B [DESTDIR]</code></p>
<dd> compute a changeset (or diff) between any two trees or revisions </p>
</dl>
<h3>Local Cache Commands</h3>
<dl>
<dt><code>baz file-find [options] file [revision]</code></p>
<dd> find given version of file </p>
<dt><code>baz pristines [options] [limit]</code></p>
<dd> list pristine trees in a project tree </p>
<dt><code>baz add-pristine [options] revision</code></p>
<dd> ensure that a project tree has a particular pristine revision </p>
<dt><code>baz find-pristine [options] revision</code></p>
<dd> find and print the path to a pristine revision </p>
</dl>
<h3>Revision Library Commands</h3>
<dl>
<dt><code>baz my-revision-library [options] [dir]</code></p>
<dd> print or change your revision library path </p>
<dt><code>baz library-config [options] library-dir</code></p>
<dd> configure parameters of a revision library </p>
<dt><code>baz library-find [options] revision</code></p>
<dd> find and print the location of a revision in the revision library </p>
<dt><code>baz library-add [options] revision</code></p>
<dd> add a revision to the revision library </p>
<dt><code>baz library-remove [options] revision</code></p>
<dd> remove a revision from the revision library </p>
<dt><code>baz library-archives [options]</code></p>
<dd> list the archives in your revision library </p>
<dt><code>baz library-categories [options] [archive]</code></p>
<dd> list the categories in your revision library </p>
<dt><code>baz library-branches [options] [category]</code></p>
<dd> list the branches in a library category </p>
<dt><code>baz library-versions [options] [branch]</code></p>
<dd> list the versions in a library branch </p>
<dt><code>baz library-revisions [options] [version]</code></p>
<dd> list the revisions in a library version </p>
<dt><code>baz library-log [options] revision</code></p>
<dd> output a log message from the revision library </p>
<dt><code>baz library-file [options] file revision</code></p>
<dd> find a file in a revision library </p>
</dl>
<h3>Cache Commands</h3>
<dl>
<dt><code>baz cache-config [options] [dir]</code></p>
<dd> Print or change your cache settings </p>
</dl>
<h3>Published Revisions Commands</h3>
<dl>
<dt><code>baz grab [options] location</code></p>
<dd> grab a published revision </p>
</dl>
<h3>Miscellaneous Scripting Support</h3>
<dl>
<dt><code>baz parse-package-name [options] name</code></p>
<dd> parse a package name </p>
<dt><code>baz valid-package-name [options] name</code></p>
<dd> test a package name for validity </p>
<dt><code>baz escape [&#8211;unescaped] string</code></p>
<dd> print strings in escaped or unescaped form </p>
</dl>
<h2>HELP</h2>
<h3>baz help</h3>
<p> <code>provide help with arch</code> </p>
<p> <code>Usage:</code> baz help [options] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-h, &#8211;help&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Display a help message and exit.<br />
&nbsp;<wbr>&nbsp;<wbr>-H&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Display a verbose help message and exit.<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;aliases&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Display command aliases<br />
&nbsp;<wbr>&nbsp;<wbr>-V, &#8211;version&nbsp;<wbr>&nbsp;<wbr>Display a release identifier string<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>and exit. </p>
<p> This command prints a list of the available commands. </p>
<p> To see just a list of the options to a particular command, use: </p>
<p>&nbsp;<wbr>baz&nbsp;<wbr>$cmd -h </p>
<p> (where $cmd is the name of the command). For additional explanation about a given command, use: </p>
<p>&nbsp;<wbr>baz&nbsp;<wbr>$cmd -H </p>
<h2>USER COMMANDS</h2>
<h3>baz my-id</h3>
<p> <code>print or change your id</code> </p>
<p> <code>Usage:</code> baz my-id [options] [id] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-e, &#8211;errname&nbsp;<wbr>&nbsp;<wbr>specify program name for errors<br />
&nbsp;<wbr>&nbsp;<wbr>-u, &#8211;uid&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>print only the UID portion of the ID </p>
<p> With no argument print your arch id. </p>
<p> With an argument, record ID-STRING as your id in ~/.arch-params/=id </p>
<p> Your id is recorded in various archives and log messages as you use arch. It must consist entirely of printable characters and fit on one line. By convention, it should have the form of an email address, as in this example: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Jane Hacker&nbsp;<wbr>&lt;jane.hacker [at] gnu.org&gt; </p>
<p> The portion of an id string between &lt; and &gt; is called your uid. arch sometimes uses your uid as a fragment when generating unique file names. </p>
<p> The option -u (&#8211;uid) causes only the uid part of your id string to be printed. </p>
<h3>baz my-default-archive</h3>
<p> <code>print or change your default archive</code> </p>
<p> <code>Usage:</code> baz my-default-archive [options] [archive] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-A, &#8211;archive&nbsp;<wbr>&nbsp;<wbr>Override&nbsp;<wbr>`my-default-archive&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>-e, &#8211;errname&nbsp;<wbr>&nbsp;<wbr>specify program name for errors<br />
&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;delete&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>unspecify your default archive<br />
&nbsp;<wbr>&nbsp;<wbr>-s, &#8211;silent&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>suppress reassuring messages </p>
<p> With no argument, and without -d, print the name of your default archive. </p>
<p> With an argument, record ARCHIVE as your default archive in ~/.arch-params/=default-archive </p>
<p> With the option -d (&#8211;delete) and no argument, ensure that you do not have a default archive set in ~/.arch-params. </p>
<p> Your default archive is determined this way: </p>
<p> If the option -A (&#8211;archive) is given and not empty, that archive is the default (which makes this script useful for processing a -A argument that was passed to another script). </p>
<p> If -A is not given, but ~/.arch-params/=default-archive exists and is not empty, that is your default archive. </p>
<p> Otherwise, your default archive is the name of the local archive rooted at the argument to -R (&#8211;root) or specified in the environment variable ARCHROOT. </p>
<p> If no default archive can be found by any of these means, the program exits with status 1, printing an error message unless the -s (&#8211;silent) option is given. </p>
<h3>baz register-archive</h3>
<p> <code>change an archive location registration</code> </p>
<p> <code>Usage:</code> baz register-archive [options] [-d name] location </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-f, &#8211;force&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>overwrite existing location<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;present-ok&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>return 0 even if archive exists<br />
&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;delete&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>delete archive registration </p>
<p> Record the location of ARCHIVE. </p>
<p> With -d, remove the registration of a previously registered archive. When accompanied by -f, override permissions on the registration file and don&#8217;t complain if the archive is not registered. If you are deleting a location that is inaccesible, you may provide the name of the archive that the location belongs to This may not be provided when registering an archive: inaccessible archives may not be registered. </p>
<p> A LOCATION should be either a directory name or a distant URL. </p>
<p> When registering a new archive, then the archive&#8217;s name will be read automatically from the archive&#8217;s meta data. </p>
<p> Archive locations are stored in ~/.arch-params/archives/ARCHIVENAME. </p>
<p> Registering archives is optional. If you use a url to a command, the archive will be automatically registered. </p>
<h3>baz whereis-archive</h3>
<p> <code>print an archive location registration</code> </p>
<p> <code>Usage:</code> baz whereis-archive [options] archive </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211;all-locations&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show all known locations for this archive name </p>
<p> Print the registered location of an archive. </p>
<p> Usually the archive must have been previously registered with &quot;baz register-archive&quot;. </p>
<p> As a special exception, the the archive is not registered, but is the name of the archive rooted at the location given with the option -R (&#8211;root) or in the environment variable ARCHROOT then print that root directory. </p>
<h3>baz archives</h3>
<p> <code>report registered archives and their locations</code> </p>
<p> <code>Usage:</code> baz archives [options] [search regular expression] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-n, &#8211;names&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>print archive names only<br />
&nbsp;<wbr>&nbsp;<wbr>-R, &#8211;exclude-remote&nbsp;<wbr>&nbsp;<wbr>Exclude MIRROR and SOURCE archives.<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;all-locations&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show all known locations for archives </p>
<p> Print a list of registered archives and their locations </p>
<p> If [search regex] is given then only archives with names that match [search regex] will be shown </p>
<h3>baz upgrade</h3>
<p> <code>perform an upgrade of local baz settings and data.</code> </p>
<p> <code>Usage:</code> baz upgrade [options] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211;leave-old-config&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Leave the old config in place. this may interfere with normal operation and is not recommended.<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;move-old-config&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Move the config data to&nbsp;<wbr>~/.arch-params/upgraded-by-baz-1.3 after it is upgraded </p>
<p> By default, nothing is done. You must supply &#8211;move-old-config (recommended) or &#8211;leave-old-config </p>
<p> For baz 1.3 this: Scans all the archives listed in ~/.arch-params/=locations and writes consolidated configuration details to ~/.arch-params/archives. After upgrading, the previous configuration details are saved in ~/.arch-params/upgraded-by-baz-1.3/ </p>
<p> If an archive cannot be connected to, its configuration details are left untouched </p>
<h2>PROJECT TREE COMMANDS</h2>
<h3>baz annotate</h3>
<p> <code>display the changesets that last modified lines in the tree</code> </p>
<p> <code>Usage:</code> baz annotate [options] [path &#8230;] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;dir DIR&nbsp;<wbr>&nbsp;<wbr>cd to DIR first </p>
<h3>baz diff</h3>
<p> <code>report about local changes in a project tree</code> </p>
<p> <code>Usage:</code> baz diff [options] [revision] [&#8211; limit&#8230;] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;dir DIR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Change to DIR first.<br />
&nbsp;<wbr>&nbsp;<wbr>-o, &#8211;output DIR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Save changeset in DIR.<br />
&nbsp;<wbr>&nbsp;<wbr>-v, &#8211;verbose&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Verbose changeset report.<br />
&nbsp;<wbr>&nbsp;<wbr>-q, &#8211;quiet&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Suppress progress information<br />
&nbsp;<wbr>&nbsp;<wbr>-s, &#8211;summary&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Do not include diffs in the output.<br />
&nbsp;<wbr>&nbsp;<wbr>-p, &#8211;show-c-function&nbsp;<wbr>&nbsp;<wbr>Show which C function each change is in.<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;link&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>hardlink unchanged files to revision library<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;unescaped&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show filenames in unescaped form </p>
<p> Generate a patch report describing the differences between the current project tree (or DIR if it is supplied) and the project trees current revision (or REVISION if supplied). </p>
<h3>baz init-tree</h3>
<p> <code>initialize a new project tree</code> </p>
<p> <code>Usage:</code> baz init-tree [options] [[archive]/version] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-A, &#8211;archive&nbsp;<wbr>&nbsp;<wbr>Override&nbsp;<wbr>`my-default-archive&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;dir DIR&nbsp;<wbr>&nbsp;<wbr>cd to DIR first<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;nested&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>initialize a nested project tree. </p>
<p> Initialize DIR as a new project tree. </p>
<p> An empty patch-log for VERSION will be created, and VERSION will be made the default location for check-ins. </p>
<h3>baz tree-id</h3>
<p> <code>Print the tree identifier for a project tree-&gt;</code> </p>
<p> <code>Usage:</code> baz tree-id [options] [dir] </p>
<p> Print the patchset identifier that represents the current tree-&gt; I.e. foo [at] example.com/demo&#8211;1.0&#8211;patch-4. Defaults to the tree the current directory is in. </p>
<h3>baz tree-root</h3>
<p> <code>find and print the root of a project tree</code> </p>
<p> <code>Usage:</code> baz tree-root [options] [dir] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211;accurate&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>error for mid-txn trees<br />
&nbsp;<wbr>&nbsp;<wbr>-s, &#8211;silent&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>exit status only </p>
<p> Find and print the root of the project tree that contains DIR (or the current directory). The option &#8211;accurate checks for three possibilities: </p>
<p>&nbsp;<wbr>1)&nbsp;<wbr>The project tree was the subject of a commit that<br />
&nbsp;<wbr>was killed before the log entry was added to the<br />
&nbsp;<wbr>tree&#8217;s patch log.&nbsp;<wbr>&nbsp;<wbr>It is unknown whether or not<br />
&nbsp;<wbr>the commit took place in the archive.&nbsp;<wbr>&nbsp;<wbr>The&nbsp;<wbr>{arch}<br />
&nbsp;<wbr>directory contains the log file as&nbsp;<wbr>&quot;++mid-commit&quot;. </p>
<p>&nbsp;<wbr>2)&nbsp;<wbr>The project tree was the subject of a killed commit, but<br />
&nbsp;<wbr>it is certain the commit took place.&nbsp;<wbr>&nbsp;<wbr>The log file<br />
&nbsp;<wbr>is stored as&nbsp;<wbr>&quot;++commit-definite&quot;. </p>
<p>&nbsp;<wbr>3)&nbsp;<wbr>The project tree patch log is fully up-to-date&nbsp;<wbr>(as far as<br />
&nbsp;<wbr>arch knows). </p>
<p> In case 1, exit with an error and error message. </p>
<p> In case 2, install the log file before printing the tree root and exiting normally. </p>
<p> In case 3, print the tree root and exit normally. </p>
<h3>baz tree-version</h3>
<p> <code>Print the default version for a project tree</code> </p>
<p> <code>Usage:</code> baz tree-version [options] [NEW VERSION] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;dir DIR&nbsp;<wbr>&nbsp;<wbr>cd to DIR first </p>
<p> Print the default version of project tree DIR (or the current directory). </p>
<p> (Advanced Usage) If [NEW VERSION] is given, then the version of the working tree is changed to the supplied one </p>
<h3>baz set-tree-version</h3>
<p> <code>This command has been removed; you can use &#8216;baz tree-version &lt;version&gt;&#8217; instead.</code> </p>
<p> <code>Usage:</code> baz set-tree-version [options] [&#8230;]</p>
<h3>baz undo</h3>
<p> <code>undo and save changes in a project tree</code> </p>
<p> <code>Usage:</code> baz undo [options] [revision] [&#8211; file &#8230;] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-A, &#8211;archive&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Override&nbsp;<wbr>`my-default-archive&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;dir DIR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>cd to DIR first<br />
&nbsp;<wbr>&nbsp;<wbr>-o, &#8211;output PATCH-DIR&nbsp;<wbr>&nbsp;<wbr>save changeset in PATCH-DIR<br />
&nbsp;<wbr>&nbsp;<wbr>-n, &#8211;no-output&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>do not save the changeset<br />
&nbsp;<wbr>&nbsp;<wbr>-q, &#8211;quiet&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>no progress reports while computing changeset<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;unescaped&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show filenames in unescaped form </p>
<p> Compute a patch set describing the changes from REVISION to the project tree containing DIR. Save the patch in PATCH-DIR (which must not already exist) and apply the patch in reverse to the project tree containing DIR. </p>
<p> The effect is to remove local changes in the DIR project tree but save them in a convenient form. </p>
<p> If REVISION is not specified, the latest ancestor of the default version of project tree is used. </p>
<p> If REVISION is specified as a VERSION, the latest ancestor of the project tree in that VERSION is used. </p>
<p> If DIR is not specified, &quot;.&quot; is assumed. </p>
<p> If PATCH-DIR is not specified, a temporary file-name of the matching ,,undo-* is used. </p>
<p> If &#8211;no-output is specified, the patch set is not saved. </p>
<p> See also &quot;baz redo -H&quot; and &quot;baz diff -H&quot;. </p>
<h3>baz redo</h3>
<p> <code>redo changes in project tree</code> </p>
<p> <code>Usage:</code> baz redo [options] [changeset] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-k, &#8211;keep&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>do not delete the patch<br />
&nbsp;<wbr>&nbsp;<wbr>-q, &#8211;quiet&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>no progress reports while computing changeset<br />
&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;dir DIR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Operate on project tree in DIR&nbsp;<wbr>(default&nbsp;<wbr>`.&#8217;)<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;unescaped&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show filenames in unescaped form </p>
<p> Apply CHANGESET to the project tree and then delete CHANGESET. </p>
<p> If CHANGESET is not specified, the highest numbered ,,undo-N directory in the project tree root is used. </p>
<p> If &#8211;keep is given, the changeset directory is not deleted. </p>
<p> See also &quot;baz undo &#8211;help&quot; and &quot;baz apply-changeset &#8211;help&quot;. </p>
<h3>baz file-diff</h3>
<p> <code>show local changes to a file</code> </p>
<p> <code>Usage:</code> baz file-diff [options] file [revision] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-A, &#8211;archive&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Override&nbsp;<wbr>`my-default-archive&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>-N, &#8211;new-file&nbsp;<wbr>&nbsp;<wbr>Treat missing file as empty </p>
<p> Print diffs between FILE and the corresponding file in a cached copy of REVISION. </p>
<p> The default patch level for a given version is the latest level for which the project tree has a patch. The default archive and version is as printed by &quot;baz tree-version&quot;. </p>
<h3>baz switch</h3>
<p> <code>change the working trees version to that of package</code> </p>
<p> <code>Usage:</code> baz switch [options] [package] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;dir DIR&nbsp;<wbr>&nbsp;<wbr>Change to DIR first.<br />
&nbsp;<wbr>&nbsp;<wbr>-q, &#8211;quiet&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Suppress progress information </p>
<p> change the working trees version to that of package, and make equivalent to revision. Preserves uncommitted changes. </p>
<p> Note: baz automatically switches to the _latest_ revision in the supplied version. </p>
<h2>PROJECT TREE INVENTORY COMMANDS</h2>
<h3>baz inventory</h3>
<p> <code>inventory a source tree</code> </p>
<p> <code>Usage:</code> baz inventory [options] [dir]* </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>-s, &#8211;source&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list source files<br />
&nbsp;<wbr>&nbsp;<wbr>-p, &#8211;precious&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list precious files<br />
&nbsp;<wbr>&nbsp;<wbr>-b, &#8211;backups&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list backup files<br />
&nbsp;<wbr>&nbsp;<wbr>-j, &#8211;junk&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list junk files<br />
&nbsp;<wbr>&nbsp;<wbr>-u, &#8211;unrecognized&nbsp;<wbr>&nbsp;<wbr>list unrecognized files<br />
&nbsp;<wbr>&nbsp;<wbr>-t, &#8211;trees&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list roots of nested trees<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;directories&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list only directories<br />
&nbsp;<wbr>&nbsp;<wbr>-f, &#8211;files&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list only non-directories<br />
&nbsp;<wbr>&nbsp;<wbr>-B, &#8211;both&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list both dirs and files<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;kind&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>indicate file kinds<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;all&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>include arch control files<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;nested&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>include nested trees<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;no-recursion&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>do not list content of directory<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;ids&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list with ids&nbsp;<wbr>(source files only)<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;untagged&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>include files that are missing ids<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;explicit&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>use explicit file ids<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;implicit&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>permit implicit file ids<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;tagline&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>permit tagline file ids<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;names&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>use name-based file ids<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;unescaped&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show filenames in unescaped form </p>
<p> With no arguments, print a human-readable inventory report. </p>
<p> With category options (&#8211;source etc) limit the report to just those files. With no other options, the report includes all sections and files. </p>
<p> The options -d, -f, and -b cancel each other. </p>
<p> The options &#8211;nested and &#8211;no-recursion cancel each other. </p>
<p> If a directory is precious, junk, or unrecognized, only the directory name itself is printed &#8212; its contents are not searched. </p>
<h3>baz status</h3>
<p> <code>scan a project tree and show the tree status.</code> </p>
<p> <code>Usage:</code> baz status [options] [dir] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-V, &#8211;version&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Display a release identifier string and exit<br />
&nbsp;<wbr>&nbsp;<wbr>-s, &#8211;broken-symlinks&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Just list broken symlinks<br />
&nbsp;<wbr>&nbsp;<wbr>-u, &#8211;unrecognized-files&nbsp;<wbr>&nbsp;<wbr>Just list files violating naming conventions<br />
&nbsp;<wbr>&nbsp;<wbr>-t, &#8211;untagged-files&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Just list files lacking inventory ids<br />
&nbsp;<wbr>&nbsp;<wbr>-m, &#8211;missing-files&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Just list inventory ids lacking corresponding files<br />
&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;duplicate-ids&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Just list duplicated ids<br />
&nbsp;<wbr>&nbsp;<wbr>-c, &#8211;conflicted&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Just list conflicted files<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;lint&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Only lint the project tree<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;diffs&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>deprecated. use baz diff instead<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;strict&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>exit with non-0 status on&nbsp;<wbr>_any_&nbsp;<wbr>oddity<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;unescaped&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show filenames in unescaped form </p>
<p> Audit a source tree for various changes, the characters in the first column mean: C &#8211; conflicts R &#8211; renames A &#8211; adds D &#8211; deletes P &#8211; permissions ? &#8211; unexpected files By default, changes will report the status for everything within a tree. Specific changes may be ignored by passing options to the changes command </p>
<p> Note: If conflicts have occurred, when you have resolved them, notify baz by run baz resolved &#8211;all </p>
<h3>baz lint</h3>
<p> <code>audit a source tree</code> </p>
<p> <code>Usage:</code> baz lint [options] [dir] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-s, &#8211;broken-symlinks&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Just list broken symlinks<br />
&nbsp;<wbr>&nbsp;<wbr>-u, &#8211;unrecognized-files&nbsp;<wbr>&nbsp;<wbr>Just list files violating naming conventions<br />
&nbsp;<wbr>&nbsp;<wbr>-t, &#8211;untagged-files&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Just list files lacking inventory ids<br />
&nbsp;<wbr>&nbsp;<wbr>-m, &#8211;missing-files&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Just list inventory ids lacking corresponding files<br />
&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;duplicate-ids&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Just list duplicated ids<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;strict&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>exit with non-0 status on&nbsp;<wbr>_any_&nbsp;<wbr>oddity<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;unescaped&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show filenames in unescaped form </p>
<p> Audit a source tree for missing files, untagged files, duplicate ids, and files not matching recognized naming conventions. </p>
<p> The default is to list files failing any of those tests. Enabling any of the `specific&#8217; tests disables the rest, unless they&#8217;re explicitly enabled on the command line. Therefore, &quot;lint&quot; is equivalent to &quot;lint -sutmd&quot;</p>
<h3>baz resolved</h3>
<p> <code>Tell bazaar one or more tree problems have been resolved</code> </p>
<p> <code>Usage:</code> baz resolved [options] FILE [FILE &#8230;] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;dir DIR&nbsp;<wbr>&nbsp;<wbr>Change to DIR first.<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;all&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Mark all problems as resolved<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;rejects&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Mark rejects as resolved<br />
&nbsp;<wbr>&nbsp;<wbr>-q, &#8211;quiet&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Suppress progress information </p>
<p> This command is used to tell bazaar that one or more tree problems has been solved. In this version of bazaar, &#8211;all is equivalent to &#8211;rejects</p>
<h3>baz id</h3>
<p> <code>report the inventory id for a file</code> </p>
<p> <code>Usage:</code> baz id [options] file &#8230; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211;implicit&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Use the implicit id tagging method.<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;tagline&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Use the tagline id tagging method&nbsp;<wbr>(default).<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;explicit&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Use the explicit id tagging method.<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;names&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Use the names id tagging method.<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;silent&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>No output &#8212; exit status only.<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;unescaped&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show filenames in unescaped form </p>
<p> Print a file&#8217;s inventory id. </p>
<h3>baz id-tagging-method</h3>
<p> <code>print or change a project tree id tagging method</code> </p>
<p> <code>Usage:</code> baz id-tagging-method [options] [method] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;dir DIR&nbsp;<wbr>&nbsp;<wbr>cd to DIR first<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;strict&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>exit with error if method not set </p>
<p> Print or change the method by which source files are identified in DIR (or the current directory). </p>
<p> When setting, METHOD must be one of: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>names&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8212; use naming conventions only<br />
&nbsp;<wbr>&nbsp;<wbr>implicit&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8212; use naming conventions but permit<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>for inventory tags<br />
&nbsp;<wbr>&nbsp;<wbr>explicit&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8212; require explicit designation of source<br />
&nbsp;<wbr>&nbsp;<wbr>tagline&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8212; mix names, explicit and arch-tag: methods </p>
<p> When printing, if &#8211;strict is provided but no id tagging method is explicitly set, print an error. </p>
<h3>baz add-id</h3>
<p> <code>add an explicit inventory id</code> </p>
<p> <code>Usage:</code> baz add-id [options] file &#8230; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211;escaped&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Provided file names may be escaped.<br />
&nbsp;<wbr>&nbsp;<wbr>-i, &#8211;id ID&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Specify ID, instead of using auto-generated id. </p>
<p> Create an explicit inventory id for FILE (which may be a regular file, symbolic link, or directory). </p>
<h3>baz delete-id</h3>
<p> <code>remove an explicit inventory id</code> </p>
<p> <code>Usage:</code> baz delete-id [options] file &#8230; </p>
<p> Remove an explicit inventory id for FILE (which may be a regular file, symbolic link, or directory). </p>
<h3>baz rm</h3>
<p> <code>remove a file (or dir, or symlink) and its explicit inventory tag (if any)</code> </p>
<p> <code>Usage:</code> baz rm [options] file&#8230; </p>
<h3>baz move-id</h3>
<p> <code>move an explicit inventory id</code> </p>
<p> <code>Usage:</code> baz move-id [options] from to </p>
<p> Move an explicit inventory id for FILE (which may be a regular file or symbolic link but which must not be a directory). </p>
<h3>baz mv</h3>
<p> <code>move a file (or dir, or symlink) and its explicit inventory tag (if any)</code> </p>
<p> <code>Usage:</code> baz mv [options] from to OR from1 from2 &#8230; dir </p>
<p> This command is suitable as a replacement for <a href="/docs/linux/man/1-mv/">mv</a>(1) within any baz tree for any move operation, regardless of id tagging method. </p>
<h3>baz explicit-default</h3>
<p> <code>print or modify default ids</code> </p>
<p> <code>Usage:</code> baz explicit-default [options] [TAG-PREFIX] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-D, &#8211;dir DIR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>cd to DIR first<br />
&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;delete&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>remove the default<br />
&nbsp;<wbr>&nbsp;<wbr>-s, &#8211;strong&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>use the strong default&nbsp;<wbr>(default)<br />
&nbsp;<wbr>&nbsp;<wbr>-w, &#8211;weak&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>use the weak default<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;dont-care&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>use the dont-care default </p>
<p> For files in this directory, use: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>ID-PREFIX__BASENAME </p>
<p> as the default explicit id for all files in this directory that do not have an explicit explicit id. </p>
<p> With no arguments, print the previously set ID-PREFIX. </p>
<p> By default, this command sets, prints or deletes a &quot;strong default&quot; &#8212; a default explicit id which overrides implicit ids. </p>
<p> With &#8211;weak, set (or print) a weak default id which is overridden by explicit ids. </p>
<p> The &#8211;dont-care option sets (or with -d, clears) a flag for that directory that causes unidged files not to be reported as such in &quot;baz lint&quot; reports. </p>
<h3>baz id-tagging-defaults</h3>
<p> <code>print the default =tagging-method contents</code> </p>
<p> <code>Usage:</code> baz id-tagging-defaults [options] </p>
<p> Print the boilerplate contents that are used to initialize new =tagging-method files. </p>
<h3>baz inode-sig</h3>
<p> <code>output the inode signature for a source tree.</code> </p>
<p> <code>Usage:</code> baz inode-sig [options] [dir] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<h2>PATCH SET COMMANDS</h2>
<h3>baz changeset</h3>
<p> <code>compute a whole-tree changeset</code> </p>
<p> <code>Usage:</code> baz changeset [options] ORIG MOD DEST [files] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211;file-list FILES&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>record only diffs of selected files<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;unescaped&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show filenames in unescaped form </p>
<p> Compares the source trees ORIG and MOD, and produces a changeset tree in DEST, which must not already exist. </p>
<p> See also &quot;baz apply-changeset -H&quot;. </p>
<h3>baz apply-changeset</h3>
<p> <code>apply a whole-tree changeset</code> </p>
<p> <code>Usage:</code> baz apply-changeset [options] CHANGESET [TARGET] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-N, &#8211;forward&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pass the &#8211;forward option to&nbsp;<wbr>`patch&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>-r, &#8211;reverse&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Apply the changeset in reverse<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;unescaped&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show filenames in unescaped form </p>
<p> Apply the changeset CHANGESET to the source tree TARGET (default `.&#8217;). </p>
<p> See also &quot;baz changeset -H&quot;. </p>
<h3>baz show-changeset</h3>
<p> <code>generate a report from a changeset</code> </p>
<p> <code>Usage:</code> baz show-changeset [options] [dir] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211;diffs&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>include diff output<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;unescaped&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show filenames in unescaped form </p>
<p> Produce a human-readable summary of a changeset. </p>
<h2>ARCHIVE TRANSACTION COMMANDS</h2>
<h3>baz make-archive</h3>
<p> <code>create a new archive directory</code> </p>
<p> <code>Usage:</code> baz make-archive [options] [name] location </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-m, &#8211;mirror MASTER&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>create mirror of specified archive<br />
&nbsp;<wbr>&nbsp;<wbr>-M, &#8211;mirror-from MASTER-SOURCE&nbsp;<wbr>&nbsp;<wbr>create pull-based mirror of specified archive<br />
&nbsp;<wbr>&nbsp;<wbr>-l, &#8211;listing&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Keep .listing files up-to-date in this archive.<br />
&nbsp;<wbr>&nbsp;<wbr>-t, &#8211;tla&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Create a tla format archive.<br />
&nbsp;<wbr>&nbsp;<wbr>-s, &#8211;signed&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>GPG sign the contents of this archive. </p>
<p> NAME is the global name for the archive. It must be an email address with a fully qualified domain name, optionally followed by &quot;&#8211;&quot; and a string of letters, digits, periods and dashes. </p>
<p> With &#8211;mirror, label the new archive as a mirror of MASTER. Ordinary commits can not be made to a mirror archive, however the command &quot;baz archive-mirror&quot; can write to a mirror. </p>
<p> Two special forms of this command are available: </p>
<p>baz make-archive &#8211;mirror MASTER LOCATION </p>
<p> is equivalent to: </p>
<p>baz make-archive &#8211;mirror MASTER MASTER-MIRROR LOCATION </p>
<p> and thus &quot;baz archive-mirror MASTER&quot; will push changes from MASTER to the newly created mirror. </p>
<p>baz make-archive &#8211;mirror-from MASTER-SOURCE LOCATION </p>
<p> is equivalent to: </p>
<p>baz make-archive &#8211;mirror MASTER-SOURCE MASTER LOCATION </p>
<p> and thus &quot;baz archive-mirror MASTER&quot; will pull changes from MASTER-SOURCE to the newly created mirror. </p>
<p> The first of these two special forms is especially handy when creating a remote mirror in which to publish a local repository. </p>
<p> The second special form is handy when creating a local mirror of a remote archive, locally bound to the remote archive&#8217;s name. </p>
<p> The &#8211;tla option creates a tla format archive, the default is to create a Bazaar archive. </p>
<h3>baz import</h3>
<p> <code>archive a full-source base-0 revision</code> </p>
<p> <code>Usage:</code> baz import [options] [[archive]/version] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;dir DIR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Import the directory DIR.<br />
&nbsp;<wbr>&nbsp;<wbr>-l, &#8211;log FILE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Commit with log file FILE.<br />
&nbsp;<wbr>&nbsp;<wbr>-s, &#8211;summary TEXT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>log with summary TEXT plus log-for-merge output<br />
&nbsp;<wbr>&nbsp;<wbr>-a, &#8211;automatic&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Initialise dir as a working tree, add all source-looking files in dir and import. This operation requires VERSION.<br />
&nbsp;<wbr>&nbsp;<wbr>-L, &#8211;log-message TEXT&nbsp;<wbr>&nbsp;<wbr>log with TEXT </p>
<p> Archive a from-scratch base revision of the tree DIR (or the current directory). Use this command to create the first revision of a new project. </p>
<p> If &#8211;log-message is specified without &#8211;summary, then TEXT is used both as the summary and the first line of the log body. </p>
<h3>baz export</h3>
<p> <code>export all or some of a tree revision</code> </p>
<p> <code>Usage:</code> baz export [options] [revision] [dir] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-s, &#8211;silent&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>no output </p>
<p> Extract REVISION from an archive, creating a new source tree with no control information. </p>
<h3>baz commit</h3>
<p> <code>archive a changeset-based revision</code> </p>
<p> <code>Usage:</code> baz commit [options] [file &#8230;] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;dir DIR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>cd to DIR first<br />
&nbsp;<wbr>&nbsp;<wbr>-l, &#8211;log FILE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>commit with log file FILE<br />
&nbsp;<wbr>&nbsp;<wbr>-s, &#8211;summary TEXT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>log with summary TEXT plus log-for-merge output<br />
&nbsp;<wbr>&nbsp;<wbr>-L, &#8211;log-message TEXT&nbsp;<wbr>&nbsp;<wbr>log with TEXT plus log-for-merge output<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;strict&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>strict tree-lint<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;seal&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>create a version-0 revision<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;fix&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>create a versionfix revision<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;out-of-date-ok&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>commit even if out of date<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;just-commit&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>only commit a simple changeset, do not add other files&nbsp;<wbr>(such as ancestry,cached revisions.<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;file-list FILE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>commit only changes to files listed in FILE<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;unescaped&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show filenames in unescaped form<br />
&nbsp;<wbr>&nbsp;<wbr>-b, &#8211;branch&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>commit to a different branch </p>
<p> Archive a revision of the project tree containing DIR (or the current directory) </p>
<p> If there are any automated ChangeLog files, update them before computing the patch set. </p>
<p> If &#8211;log-message is specified without &#8211;summary, then TEXT is used both as the summary and the first line of the log body. </p>
<h3>baz get</h3>
<p> <code>construct a project tree for a revision</code> </p>
<p> <code>Usage:</code> baz get [options] revision [dir] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-A, &#8211;archive&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Override&nbsp;<wbr>`my-default-archive&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;no-pristine&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>don&#8217;t save a pristine copy<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;link&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>hardlink files to revision library instead of copying<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;library&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ensure the revision is in a revision library<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;sparse&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>add library entries sparsely&nbsp;<wbr>(&#8211;link, &#8211;library)<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;non-sparse&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>add library entries densely&nbsp;<wbr>(&#8211;link, &#8211;library)<br />
&nbsp;<wbr>&nbsp;<wbr>-s, &#8211;silent&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>no output<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;no-greedy-add&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>do not allow greedy libraries to add revisions<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;unescaped&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show filenames in unescaped form </p>
<p> Extract REVISION from an archive, creating the new project tree DIR. If DIR is not specified, store the working copy in a subdirectory of the current directory, giving it the name of the revision. CAUTION: when using the links option be sure to use copy-on-write on your editor or the revision library will be corrupted. Either way, the project tree must not already exist. </p>
<h3>baz get-changeset</h3>
<p> <code>retrieve a changeset from an archive</code> </p>
<p> <code>Usage:</code> baz get-changeset [options] revision [dir] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-A, &#8211;archive&nbsp;<wbr>&nbsp;<wbr>Override&nbsp;<wbr>`my-default-archive&#8217; </p>
<p> Retrieve the changeset for REVISION and store it in the directory DIR (or a directory named REVISION.patches). DIR must not already exist. </p>
<h3>baz lock-revision</h3>
<p> <code>lock (or unlock) an archive revision</code> </p>
<p> <code>Usage:</code> baz lock-revision [options] VERSION|REVISION </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-A, &#8211;archive&nbsp;<wbr>&nbsp;<wbr>Override&nbsp;<wbr>`my-default-archive&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>-u, &#8211;unlock&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>release a lock owned by you<br />
&nbsp;<wbr>&nbsp;<wbr>-b, &#8211;break&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>break any existing lock </p>
<p> Acquire the lock needed to create REVISION. </p>
<p> Revision must be the next patch-level in sequence, however, if no patch level is specified, the revision is automatically calculated </p>
<h3>baz archive-mirror</h3>
<p> <code>update an archive mirror</code> </p>
<p> <code>Usage:</code> baz archive-mirror [options] [from [to] [limit]] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211;no-cached&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>don&#8217;t copy cached revisions<br />
&nbsp;<wbr>&nbsp;<wbr>-s, &#8211;summary&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>print the summary of each patch<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;cached-tags&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>copy only cachedrevs for tags to other archives<br />
&nbsp;<wbr>&nbsp;<wbr>-a, &#8211;all-mirrors&nbsp;<wbr>&nbsp;<wbr>mirror to all known mirrors </p>
<p> If no arguments are given, update either the archive for the project tree you are in, or your `my-default-archive&#8217;-MIRROR archive with the contents of `my-default-archive&#8217;. </p>
<p> If a [FROM] archive is given, update the [FROM]-MIRROR archive with the contents of the [FROM] archive </p>
<p> If both [FROM] and [TO] archives are specified, update [TO] with the contents of [FROM] </p>
<p> If LIMIT is provided, it should be a category, branch, version, or revision name. Only the indicated part of FROM will be copied to TO. If LIMIT is a revision, then cached revisions will be copied and deleted to TO. </p>
<p> (see &quot;baz make-archive -H&quot;.). </p>
<h2>ARCHIVE COMMANDS</h2>
<h3>baz abrowse</h3>
<p> <code>print an outline describing archive contents</code> </p>
<p> <code>Usage:</code> baz abrowse [options] [limit] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-r, &#8211;reverse&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>sort revisions from newest to oldest<br />
&nbsp;<wbr>&nbsp;<wbr>-s, &#8211;summary&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>print a summary of each patch<br />
&nbsp;<wbr>&nbsp;<wbr>-c, &#8211;creator&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>print the creator of each patch<br />
&nbsp;<wbr>&nbsp;<wbr>-D, &#8211;date&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>print the date of each patch<br />
&nbsp;<wbr>&nbsp;<wbr>-k, &#8211;kind&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show each revision kind&nbsp;<wbr>(import, changeset or id)<br />
&nbsp;<wbr>&nbsp;<wbr>-C, &#8211;cacherevs&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show cached revisions<br />
&nbsp;<wbr>&nbsp;<wbr>-f, &#8211;full&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>print full patch level names<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;desc&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>implies -s -c -D -k -C<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;local-merges&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list merges from the same archive<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;foreign-merges&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list merges from other archives<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;merges&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list all merges<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;categories&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show category names only<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;branches&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show branch names only<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;versions&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show version names only<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;omit-empty&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>omit empty or unchanged-since items<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;since SNAP-FILE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show revisions after those listed in SNAP-FILE<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;since-limits&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>limit output to items in the since file<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;snap SNAP-FILE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>record the highest revisions shown<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;force&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>overwrite an existing snap-file </p>
<p> Describe the contents of an archive in outline format. </p>
<p> With LIMIT, look only that part of the archive. </p>
<p> LIMIT may be a fully qualified name and may be an archive name. </p>
<h3>baz rbrowse</h3>
<p> <code>print an outline describing an archive&#8217;s contents</code> </p>
<p> <code>Usage:</code> baz rbrowse [options] [[ARCHIVE_NAME/]LIMIT_REGEX] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211;all&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Search all archives<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;since SNAP-FILE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Only show differences since SNAP-FILE<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;snap SNAP-FILE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Snap an archive<br />
&nbsp;<wbr>&nbsp;<wbr>-f, &#8211;snap-force&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Force snap writing<br />
&nbsp;<wbr>&nbsp;<wbr>-r&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Reverse patch logs<br />
&nbsp;<wbr>&nbsp;<wbr>-s&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Print the summary of matching patches<br />
&nbsp;<wbr>&nbsp;<wbr>-c&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Print the creator of matching patches<br />
&nbsp;<wbr>&nbsp;<wbr>-D&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Print the date of matching patches<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;patch-regex REGEX&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Only show revisions that contain&nbsp;<wbr>[REGEX]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(implies -s)<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;show-sealed&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Do not hide sealed branches </p>
<p> an outline of an archive will be printed, showing the categories, branches and revisions of the specified archive if no archive is given then `my-default-archive` is used. </p>
<p> If [LIMIT REGEX] is specified, revisions will only be shown if the category, branch or version matches [LIMIT REGEX]. If &#8211;patch-regex [REGEX] is given, then only patchlogs matching [REGEX] will be given</p>
<h3>baz categories</h3>
<p> <code>list the categories in an archive</code> </p>
<p> <code>Usage:</code> baz categories [options] [archive] </p>
<p> Print a list of the categories present in an archive. </p>
<h3>baz branches</h3>
<p> <code>list the branches in an archive category</code> </p>
<p> <code>Usage:</code> baz branches [options] [[archive/]category] </p>
<p> Print a list of the branches within CATEGORY </p>
<h3>baz versions</h3>
<p> <code>list the versions in an archive branch</code> </p>
<p> <code>Usage:</code> baz versions [options] [branch] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-A, &#8211;archive&nbsp;<wbr>&nbsp;<wbr>Override&nbsp;<wbr>`my-default-archive&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>-r, &#8211;reverse&nbsp;<wbr>&nbsp;<wbr>sort from newest to oldest </p>
<p> Print a list of versions within an archive branch. </p>
<p> The list is ordinarily sorted from oldest to newest, but the order can be changed with -r (&#8211;reverse). </p>
<h3>baz revisions</h3>
<p> <code>list the revisions in an archive version</code> </p>
<p> <code>Usage:</code> baz revisions [options] [[archive/]version] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-r, &#8211;reverse&nbsp;<wbr>&nbsp;<wbr>sort from newest to oldest<br />
&nbsp;<wbr>&nbsp;<wbr>-f, &#8211;full&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list fully qualified names<br />
&nbsp;<wbr>&nbsp;<wbr>-s, &#8211;summary&nbsp;<wbr>&nbsp;<wbr>print a summary of each patch<br />
&nbsp;<wbr>&nbsp;<wbr>-c, &#8211;creator&nbsp;<wbr>&nbsp;<wbr>print the creator of each patch<br />
&nbsp;<wbr>&nbsp;<wbr>-D, &#8211;date&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>print the date of each patch </p>
<p> Print a list of revisions within an archive version. </p>
<p> The list is ordinarily sorted from oldest to newest, but the order can be changed with -r (&#8211;reverse). </p>
<p> With optional arguments specifying patches, list only those patches, if they exist. If a listed patch does not exist, exit with status 1. The -r (&#8211;reverse) flag has no effect with optional arguments. </p>
<h3>baz ancestry</h3>
<p> <code>display the ancestory of a revision</code> </p>
<p> <code>Usage:</code> baz ancestry [options] [revision] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;dir DIR&nbsp;<wbr>&nbsp;<wbr>cd to DIR first<br />
&nbsp;<wbr>&nbsp;<wbr>-m, &#8211;merges&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show merges into this development line<br />
&nbsp;<wbr>&nbsp;<wbr>-r, &#8211;reverse&nbsp;<wbr>&nbsp;<wbr>list oldest to newest<br />
&nbsp;<wbr>&nbsp;<wbr>-s, &#8211;summary&nbsp;<wbr>&nbsp;<wbr>print a summary of each patch<br />
&nbsp;<wbr>&nbsp;<wbr>-c, &#8211;creator&nbsp;<wbr>&nbsp;<wbr>print the creator of each patch<br />
&nbsp;<wbr>&nbsp;<wbr>-t, &#8211;tree&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>generate or print the tree ancestry file<br />
&nbsp;<wbr>&nbsp;<wbr>-D, &#8211;date&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>print the date of each patch </p>
<p> Print the ancestry of a revision. </p>
<h3>baz ancestry-graph</h3>
<p> <code>display the ancestory of a revision</code> </p>
<p> <code>Usage:</code> baz ancestry-graph [options] [revision] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;dir DIR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>cd to DIR first<br />
&nbsp;<wbr>&nbsp;<wbr>-m, &#8211;merges&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show merges into this development line<br />
&nbsp;<wbr>&nbsp;<wbr>-r, &#8211;reverse&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list oldest to newest<br />
&nbsp;<wbr>&nbsp;<wbr>-i, &#8211;immediate&nbsp;<wbr>&nbsp;<wbr>show only the immediate ancestor<br />
&nbsp;<wbr>&nbsp;<wbr>-p, &#8211;previous&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show the&nbsp;<wbr>(namespace)&nbsp;<wbr>previous revision </p>
<p> Print a list describing the ancestry of a revision. </p>
<h3>baz change-archive</h3>
<p> <code>Alter properties of an archive. For instance, add signatures to an unsigned archive.</code> </p>
<p> <code>Usage:</code> baz change-archive [options] archivename|URL </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211;add-signatures&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>turn this archve into a signed archive<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;remove-signatures&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>remove digital signatures from this archive </p>
<p> The following operations involve making a temporary mirror of the archive: &#8211; adding signatures &#8211; removing signatures &#8211; changing the archive format They may take some time as they involve a full mirror of the archive and all its contents The following operations will automatically propogate their changes to all writeable mirrors listed in ~/.arch-params/archives/NAME, and must have the master archive available to operate at all: &#8211; adding signatures &#8211; removing signatures </p>
<h3>baz cat-archive-log</h3>
<p> <code>print the contents of an archived log entry</code> </p>
<p> <code>Usage:</code> baz cat-archive-log [options] revision </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211;headers&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show only log headers </p>
<p> Retrieve and print the log message for the indicated revision from its archive. </p>
<h3>baz cacherev</h3>
<p> <code>cache a full source tree in an archive</code> </p>
<p> <code>Usage:</code> baz cacherev [options] [ARCHIVE/[PACKAGE[&#8211;VERSION[&#8211;PATCHLEVEL]]]] or [PATCHLEVEL] </p>
<p> Cache a full-text copy of the indicated revision in the archive. This can speed up subsequent calls to &quot;baz get&quot; for that and subsequent revisions. </p>
<p> If no nothing is specified, but the command is run from within a project tree, cache the latest revision in the default version of that tree. </p>
<h3>baz cachedrevs</h3>
<p> <code>list cached revisions in an archive</code> </p>
<p> <code>Usage:</code> baz cachedrevs [options] [version] </p>
<p> Report which revisions of VERSION have been cached as whole trees in the archive. </p>
<p> See also &quot;baz cacherev -H&quot;. </p>
<h3>baz uncacherev</h3>
<p> <code>remove a cached full source tree from an archive</code> </p>
<p> <code>Usage:</code> baz uncacherev [options] revision [dir] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-A, &#8211;archive&nbsp;<wbr>&nbsp;<wbr>Override&nbsp;<wbr>`my-default-archive&#8217; </p>
<p> Remove the cached form of REVISION from its archive. </p>
<p> If REVISION is not specified, but the command is run from within a project tree, uncache the latest revision in the default version of that tree. </p>
<p> Also see &quot;baz cacherev -H&quot;. </p>
<h3>baz archive-meta-info</h3>
<p> <code>report meta-info from an archive</code> </p>
<p> <code>Usage:</code> baz archive-meta-info [options] [archive/]item-name </p>
<p> Print the contents of a meta-info file from an archive. For example, </p>
<p>&nbsp;<wbr>%&nbsp;<wbr>baz archive-meta-info name </p>
<p> prints the official name of your default archive. </p>
<h3>baz archive-snapshot</h3>
<p> <code>update an archive snapshot</code> </p>
<p> <code>Usage:</code> baz archive-snapshot [options] dir [[archive/]limit] </p>
<p> Update the directory DIR with a &quot;snapshot&quot; of of an archive (or the part of the archive indicated by LIMIT </p>
<p> For each archive snapshotted, DIR will contain a file and subdirectory (where $ARCH is the name of the archive): </p>
<p>&nbsp;<wbr>./$ARCH.added<br />
&nbsp;<wbr>./$ARCH/ </p>
<p> Similarly, for each category snapshotted, DIR will contain: </p>
<p>&nbsp;<wbr>./$ARCH/$CAT.added<br />
&nbsp;<wbr>./$ARCH/$CAT/ </p>
<p> and so on, recursively, for branches and versions. </p>
<p> For each revision, the snapshot contains: </p>
<p>&nbsp;<wbr>./$ARCH/$CAT/$BRANCH/$VERSION/$REVISION.added </p>
<p> and that file contains a copy of the patch log entry for that revision. </p>
<p> Snapshots can be used in combination with other tools (&#8216;make&#8217; is suggested) to trigger one-time events in response to new additions to an archive. </p>
<h3>baz archive-version</h3>
<p> <code>list the archive-version in an archive</code> </p>
<p> <code>Usage:</code> baz archive-version [options] [archive] </p>
<p> Print the archive format identifier string of an arch archive. </p>
<h3>baz archive-fixup</h3>
<p> <code>fix ancillary files (e.g. .listing files) in an archive</code> </p>
<p> <code>Usage:</code> baz archive-fixup [options] [archive] </p>
<p> This is a kind of &quot;catch-all&quot; command to fix the non-standard, non-transactional state of an archive. Currently its sole function is to repair .listing files in archives that use them. </p>
<h2>PATCH LOG COMMANDS</h2>
<h3>baz make-log</h3>
<p> <code>initialize a new log file entry</code> </p>
<p> <code>Usage:</code> baz make-log [options] [version] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-A, &#8211;archive&nbsp;<wbr>&nbsp;<wbr>Override&nbsp;<wbr>`my-default-archive&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;dir DIR&nbsp;<wbr>&nbsp;<wbr>cd to DIR first<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;no-file&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Display filename, but do not create file. </p>
<p> Create (if needed) a log entry file in the root of the project tree containing DIR, for the indicated VERSION. </p>
<p> The name of the new log file is printed to standard output. </p>
<h3>baz log-versions</h3>
<p> <code>list patch log versions in a project tree</code> </p>
<p> <code>Usage:</code> baz log-versions [options] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;dir DIR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>cd to DIR first<br />
&nbsp;<wbr>&nbsp;<wbr>-a, &#8211;archive ARCHIVE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list only logs for ARCHIVE<br />
&nbsp;<wbr>&nbsp;<wbr>-c, &#8211;category CATEGORY&nbsp;<wbr>&nbsp;<wbr>list only logs for CATEGORY<br />
&nbsp;<wbr>&nbsp;<wbr>-b, &#8211;branch BRANCH&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list only logs for BRANCH<br />
&nbsp;<wbr>&nbsp;<wbr>-v, &#8211;vsn VERSION&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list only logs for VERSION<br />
&nbsp;<wbr>&nbsp;<wbr>-r, &#8211;reverse&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>reverse the sort order </p>
<p> Print the list of versions for which there are patch logs in the project tree containing DIR (or the current directory). </p>
<h3>baz add-log-version</h3>
<p> <code>add a patch log version to a project tree</code> </p>
<p> <code>Usage:</code> baz add-log-version [options] [archive]/version </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-A, &#8211;archive&nbsp;<wbr>&nbsp;<wbr>Override&nbsp;<wbr>`my-default-archive&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;dir DIR&nbsp;<wbr>&nbsp;<wbr>cd to DIR first </p>
<p> Add an initially empty list of patch log for VERSION to the project tree containing DIR (or the current directory). </p>
<p> A project tree patch log is a pre-requisite for checking the directory in on that version, or updating with patches from that version. </p>
<p> Note that versions recorded for a project tree are recorded by fully qualified version names: an archive name plus the name of a version within that archive. </p>
<h3>baz remove-log-version</h3>
<p> <code>remove a version&#8217;s patch log from a project tree</code> </p>
<p> <code>Usage:</code> baz remove-log-version [options] [archive]/version </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-A, &#8211;archive&nbsp;<wbr>&nbsp;<wbr>Override&nbsp;<wbr>`my-default-archive&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;dir DIR&nbsp;<wbr>&nbsp;<wbr>cd to DIR first </p>
<p> Remove the patch log for VERSION from the project tree containing DIR (or the current directory). </p>
<p> Use this command with caution &#8212; it erases revision history from the project tree! </p>
<h3>baz log</h3>
<p> <code>Show the log messages for the working directory or given</code> </p>
<p> <code>Usage:</code> baz log [-f|&#8211;full] [-r start[:end]] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-r, &#8211;range&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-r start[:end], where start+end are PATCH or PACKAGE<br />
&nbsp;<wbr>&nbsp;<wbr>-f, &#8211;full&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show the entire log message rather than the summary </p>
<p> files/directories, since the beginning of time (crossing copies/renames) or since/between the revisions/dates given. Can also be run out of a working directory to<br />
&nbsp;<wbr>interrogate an archive instead of a working tree-&gt; </p>
<p> Examples: Show me the changes made to scripts/dpkg-source.pl in the archive:<br />
%%&nbsp;<wbr>baz log -r dpkg&#8211;devel&#8211;1.13 scripts/dpkg-source.pl </p>
<p> Show me the changes between a different branch&#8217;s patch-4, my branches patch-2:<br />
&nbsp;<wbr>%%&nbsp;<wbr>baz log -r dpkg&#8211;devel&#8211;1.13&#8211;patch-4:patch-2 </p>
<p> Show me the changes in all revisions of the tree-version after and including patch-123.<br />
&nbsp;<wbr>%%&nbsp;<wbr>baz log -r patch-123: </p>
<p>&nbsp;<wbr>Show me the last ten changes:<br />
&nbsp;<wbr>%%&nbsp;<wbr>baz log -r 10 </p>
<h3>baz logs</h3>
<p> <code>list patch logs for a version in a project tree</code> </p>
<p> <code>Usage:</code> baz logs [options] [[archive]/version &#8230;] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-A, &#8211;archive&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Override&nbsp;<wbr>`my-default-archive&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;dir DIR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>cd to DIR first<br />
&nbsp;<wbr>&nbsp;<wbr>-r, &#8211;reverse&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>sort from newest to oldest<br />
&nbsp;<wbr>&nbsp;<wbr>-s, &#8211;summary&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>print the summary of each patch<br />
&nbsp;<wbr>&nbsp;<wbr>-c, &#8211;creator&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>print the creator of each patch<br />
&nbsp;<wbr>&nbsp;<wbr>-D, &#8211;date&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>print the date of each patch<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;local-merges&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list merges from the same archive<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;foreign-merges&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list merges from other archives<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;merges&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list all merges<br />
&nbsp;<wbr>&nbsp;<wbr>-f, &#8211;full&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>print full patch level names </p>
<p> Print the list of patches applied to a project tree DIR (or the current directory) from VERSION. </p>
<h3>baz cat-log</h3>
<p> <code>print the contents of a project tree log entry</code> </p>
<p> <code>Usage:</code> baz cat-log [options] revision-spec </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-A, &#8211;archive&nbsp;<wbr>&nbsp;<wbr>Override&nbsp;<wbr>`my-default-archive&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;dir DIR&nbsp;<wbr>&nbsp;<wbr>cd to DIR first </p>
<p> Retrieve and print the patch log for the indicated revision from a project tree. </p>
<h3>baz changelog</h3>
<p> <code>generate a ChangeLog from a patch log</code> </p>
<p> <code>Usage:</code> baz changelog [options] [[archive]/version] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-A, &#8211;archive&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Override&nbsp;<wbr>`my-default-archive&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;dir DIR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>cd to DIR first<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;no-files&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>exclude file lists from ChangeLog<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;untagged&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>don&#8217;t implicitly tag the output file<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;new-entry PATCH,FILE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>make FILE the first&nbsp;<wbr>(top)&nbsp;<wbr>entry<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>for patch level PATCH </p>
<p> Generate a ChangeLog for VERSION from the patch log for DIR. </p>
<h3>baz log-for-merge</h3>
<p> <code>generate a log entry body for a merge</code> </p>
<p> <code>Usage:</code> baz log-for-merge [options] [[archive]/version] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-A, &#8211;archive&nbsp;<wbr>&nbsp;<wbr>Override&nbsp;<wbr>`my-default-archive&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;dir DIR&nbsp;<wbr>&nbsp;<wbr>cd to DIR first<br />
&nbsp;<wbr>&nbsp;<wbr>-r, &#8211;reverse&nbsp;<wbr>&nbsp;<wbr>sort from newest to oldest </p>
<p> Generate a log entry body describing a merge into VERSION. </p>
<h3>baz merges</h3>
<p> <code>report where two branches have been merged</code> </p>
<p> <code>Usage:</code> baz merges [options] INTO [FROM] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;dir DIR&nbsp;<wbr>&nbsp;<wbr>cd to DIR first<br />
&nbsp;<wbr>&nbsp;<wbr>-r, &#8211;reverse&nbsp;<wbr>&nbsp;<wbr>sort from newest to oldest<br />
&nbsp;<wbr>&nbsp;<wbr>-f, &#8211;full&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>print full patch level names </p>
<p> Print a list of pairs of patch level names: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>%s<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>%s&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>INTO-RVN&nbsp;<wbr>&nbsp;<wbr>FROM-RVN</p>
<p> where each pair indicates that at patch level INTO-RVN of INTO, the patch log entry FROM-RVN was added. </p>
<p> FROM may be a branch name, version name, or revision name. If a branch or version name, all merges from that branch or version are reported. If a revision name, only the merge points for that specific revision are reported. </p>
<p> INTO may be a version name or revision name. If a version name, all merge points within that version are printed. If a revision name, all merge points at that revision or earlier are printed. </p>
<p> Output is sorted using patch-level ordering of the first column. </p>
<p> Included patches are listed by full name unless FROM is a revision name. If FROM is a revision, &#8211;full causes its full name to be printed. </p>
<h3>baz new-merges</h3>
<p> <code>list tree patches new to a version</code> </p>
<p> <code>Usage:</code> baz new-merges [options] [[archive]/version] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-A, &#8211;archive&nbsp;<wbr>&nbsp;<wbr>Override&nbsp;<wbr>`my-default-archive&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;dir DIR&nbsp;<wbr>&nbsp;<wbr>cd to DIR first<br />
&nbsp;<wbr>&nbsp;<wbr>-r, &#8211;reverse&nbsp;<wbr>&nbsp;<wbr>sort from newest to oldest </p>
<p> List all patch log entries in the tree containing DIR that have not already been merged with VERSION. </p>
<h2>MULTI-PROJECT CONFIGURATION COMMANDS</h2>
<h3>baz build-config</h3>
<p> <code>instantiate a multi-project config</code> </p>
<p> <code>Usage:</code> baz build-config [options] config </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;dir DIR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>cd to DIR first<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;no-pristines&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>don&#8217;t create pristine copies<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;link&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>hardlink files to revision library instead of copying<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;library&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ensure revisions are in the revision library<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;sparse&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>add library entries sparsely&nbsp;<wbr>(&#8211;link, &#8211;library)<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;no-greedy-add&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>do not allow greedy libraries to add revisions<br />
&nbsp;<wbr>&nbsp;<wbr>-r, &#8211;release-id&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>overwrite ./=RELEASE-ID for this config </p>
<p> Build the named configuration. See also baz cat-config -H&quot;. </p>
<h3>baz cat-config</h3>
<p> <code>output information about a multi-project config</code> </p>
<p> <code>Usage:</code> baz cat-config [options] config </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;dir DIR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>cd to DIR first<br />
&nbsp;<wbr>&nbsp;<wbr>-o, &#8211;output CFG&nbsp;<wbr>&nbsp;<wbr>write the output as config CFG<br />
&nbsp;<wbr>&nbsp;<wbr>-f, &#8211;force&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>overwrite an exiting config&nbsp;<wbr>(with &#8211;output)<br />
&nbsp;<wbr>&nbsp;<wbr>-s, &#8211;snap&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Show current patch levels of subtree packages.<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;unescaped&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show filenames in unescaped form </p>
<p> Parse and print the indicate config file from a project tree </p>
<p> A config file contains blank lines, comment lines starting with &quot;#&quot;, and config specification lines. The config file called $NAME is stored in a project tree as ./configs/$NAME or as ./$NAME. </p>
<p> A config specification line contains a relative path within a project tree, and a specification of the project or revision to store in that location. </p>
<p> For example, the line: </p>
<p>./src/arch&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>lord [at] emf.net&#8211;2003b/arch&#8211;devo&#8211;1.0 </p>
<p> means that, when building the configuration, the latest revision of arch&#8211;devo&#8211;1.0 should be created within the tree as ./src/arch. </p>
<p> The project specification can be a branch name, version name or the name of a specific revision. </p>
<p> The option &#8211;snap says to examine the project tree to find out which revisions of configured project are printed, and generate a new config specification that references those specific revisions. For example, the output for the line shown above might be: </p>
<p>&nbsp;<wbr>./src/arch&nbsp;<wbr>&nbsp;<wbr>lord [at] emf.net&#8211;2003b/arch&#8211;devo&#8211;1.0&#8211;patch-21 </p>
<p> The option &#8211;output causes the output from this command to be recorded as a new configuration file (or to replace an existing file if &#8211;force is provided). </p>
<h2>COMMANDS FOR BRANCHING AND MERGING</h2>
<h3>baz branch</h3>
<p> <code>create a branch</code> </p>
<p> <code>Usage:</code> baz branch [options] [SOURCE] BRANCH </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-l, &#8211;log FILE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>commit with log file FILE<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;no-cacherev&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Do not cacherev tag even if different archive<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;seal&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>create a version-0 revision<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;fix&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>create a versionfix revision<br />
&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;dir DIR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>cd to DIR first </p>
<p> Create the continuation at the next patch level of BRANCH which is equivalent to SOURCE. </p>
<p> If SOURCE is not specified, the current project tree revision is used, and the project tree is switched to BRANCH </p>
<h3>baz merge</h3>
<p> <code>merge from another branch</code> </p>
<p> <code>Usage:</code> baz merge [options] [FROM] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-c, &#8211;changes OUTPUT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Generate but don&#8217;t apply the changeset.<br />
&nbsp;<wbr>&nbsp;<wbr>-r, &#8211;reference VERSION&nbsp;<wbr>&nbsp;<wbr>Set reference version&nbsp;<wbr>(default: project tree version)<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;show-merge-points&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Calculate the trees to use for merging, show their ids and exit.<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;star-merge&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Use the more restrictive star merge algorithm for choosing the common ancestor<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;trace&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Trace the selection of the merge points.<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;two-way&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Perform a 2-way merge.<br />
&nbsp;<wbr>&nbsp;<wbr>-t, &#8211;three-way&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(Deprecated &#8211; now default)&nbsp;<wbr>Perform a 3-way merge.<br />
&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;dir DIR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Operate on project tree in DIR&nbsp;<wbr>(default&nbsp;<wbr>`.&#8217;)<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;unescaped&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show filenames in unescaped form </p>
<p> Merge changes from FROM into the project tree, considering common ancestry from the project tree reference version, REFERENCE (which defaults to the tree version of the project tree). If FROM is not given, it defaults to the tree revision. </p>
<p> The &#8211;star-merge option is for use in situations where the pattern of merges between branches is strictly a star. If you desire standard external rejection hunks, you should use &#8211;star-merge &#8211;two-way. </p>
<p> By default, merge will perform a three way merge, using any of the &#8216;best&#8217; common ancestors available. When used in a star development model, the results will be the same as with &#8211;star-merge. However when used in a mesh model, where teams of developers are collaborating with each other, the chosen common ancestor will be the closest commont text, reducing spurious conflicts. </p>
<p> FROM indicates a revision (it may be specified as a version name, indicating the latest revision in that version). </p>
<p> TREE is the project tree into which the merge will occur. </p>
<p> The mesh or graph algorithm details: merge works by computing the closest common ancestor. This is defined as the common ancestor that is reachable in a minimal number of hops from Both FROM and TREE. When multiple ancestors are reachable in the same number of hops, only ancestors with no children reachable in the same number of hops are chosen. If there are multiple ancestors left to choose from, an arbitrary one is chosen. This is optimised for diff3 merges, use of &#8211;two-way is NOT RECOMMENDED without also specifying &#8211;star-merge. </p>
<p> The &#8211;star-merge option details: Star-merge works by computing the most recent ANCESTOR revision of REFERENCE and FROM and then applying the changeset: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>delta&nbsp;<wbr>(ANCESTOR, FROM) </p>
<p> to TREE. </p>
<p> The &quot;most recent ancestor&quot; is defined as follows: </p>
<p> MAYBE_ANCESTOR_1 is defined as the highest patch level of FROM in REFERENCE for which both TREE and FROM have a patch log. In other words, it is the latest REFERENCE revision of FROM&#8217;s version already merged into TREE. </p>
<p> MAYBE_ANCESTOR_2 is defined as the highest patch level in REFERENCE for which both FROM and REFERENCE have a patch log. In other words, it is the latest revision of REFERENCE already merged into FROM. </p>
<p> MAYBE_ANCESTOR_2, if it is not &quot;nil&quot;, was merged into FROM at some revision of FROM&#8217;s version, which we can call LAST_MERGE_INTO_FROM. </p>
<p> If both MAYBE_ANCESTOR_1 or MAYBE_ANCESTOR_2 are nil, star-merge can do nothing. </p>
<p> If just one of MAYBE_ANCESTOR_1 is MAYBE_ANCESTOR_2 is not nil, then that non-nil value is ANCESTOR. </p>
<p> If both MAYBE_ANCESTOR_1 and MAYBE_ANCESTOR_2 are not nil, then LAST_MERGE_INTO_FROM and MAYBE_ANCESTOR_1 are compared (both are revisions in FROM&#8217;s version). If MAYBE_ANCESTOR_1 is the later revision, then MAYBE_ANCESTOR_1 is ANCESTOR, otherwise, MAYBE_ANCESTOR_2 is ANCESTOR. </p>
<h3>baz update</h3>
<p> <code>update a project tree to reflect recent archived changes</code> </p>
<p> <code>Usage:</code> baz update [options] [version/revision] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;dir DIR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Update project tree in DIR&nbsp;<wbr>(default&nbsp;<wbr>`.&#8217;)<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;dest DEST&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Instead of modifying the project tree in-place,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>make a copy of it to DEST and apply the result to that<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;unescaped&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show filenames in unescaped form </p>
<p> Update a project tree by getting the latest revision of VERSION (or the default version of the project tree) and then applying a patch set of the differences between the project tree and the highest revision with which it is up-to-date. </p>
<p> If the merge involves conflicts, a warning message is printed, and the new project tree will contain &quot;.rej&quot; files. </p>
<h3>baz replay</h3>
<p> <code>apply revision changesets to a project tree</code> </p>
<p> <code>Usage:</code> baz replay [options] [version/revision&#8230;] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211;list FILE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>read a list of patches to apply<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;new&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>replay only new patches<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;reverse&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>reverse the named patch<br />
&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;dir DIR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Operate on project tree in DIR&nbsp;<wbr>(default&nbsp;<wbr>`.&#8217;)<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;dest DEST&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Instead of modifying the project tree in-place,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>make a copy of it to DEST and apply the result to that<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;skip-present&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>skip patches that contain 1 or more patch logs already in this tree<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;unescaped&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show filenames in unescaped form </p>
<p> The result is formed by applying patches in the latest revision of VERSION (or the default version of the project tree), stopping after the first patch that causes conflicts. If multiple VERSIONs are specified, they are applied in turn. </p>
<p> If one or more specific REVISIONs (including patch-levels) is specified instead, only those patch sets, and no others, will be applied. </p>
<p> With the &#8211;list option, read a list of patches to apply from FILE (- for standard input). Complete revision names should be listed, one per line. replay will stop at the first patch in the list that causes a merge conflict, leaving behind files with names of the form: </p>
<p>,,replay.conflicts-in &#8212;&nbsp;<wbr>&nbsp;<wbr>the name of the patch that caused conflicts </p>
<p>,,replay.remaining&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8212;&nbsp;<wbr>&nbsp;<wbr>the list of patches not yet applied </p>
<h3>baz apply-delta</h3>
<p> <code>compute a changeset between any two trees or revisions and apply it to a project tree</code> </p>
<p> <code>Usage:</code> baz apply-delta [options] FROM(REVISION|DIR) TO(REVISION|DIR) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-A, &#8211;archive&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Override&nbsp;<wbr>`my-default-archive&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>-q, &#8211;quiet&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>instruct command to be quieter when applying delta<br />
&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;dir DIR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Operate on project tree in DIR&nbsp;<wbr>(default&nbsp;<wbr>`.&#8217;)<br />
&nbsp;<wbr>&nbsp;<wbr>-t, &#8211;three-way&nbsp;<wbr>&nbsp;<wbr>Perform a 3-way&nbsp;<wbr>(diff3-style)&nbsp;<wbr>merge.<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;dest DEST&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Instead of modifying the project tree in-place,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>make a copy of it to DEST and apply the result to that<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;unescaped&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show filenames in unescaped form </p>
<p> A delta between A and B (both of which may be either a full revision or a project tree) is computed, and then applied to the project tree. </p>
<p> Exit Status Codes: </p>
<p>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>No conflict during patch<br />
&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>Conflicts occurred during patch<br />
&nbsp;<wbr>3&nbsp;<wbr>&nbsp;<wbr>Internal Error </p>
<h3>baz missing</h3>
<p> <code>print patches missing from a project tree</code> </p>
<p> <code>Usage:</code> baz missing [options] [version] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-A, &#8211;archive&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Override&nbsp;<wbr>`my-default-archive&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;dir DIR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>cd to DIR first<br />
&nbsp;<wbr>&nbsp;<wbr>-r, &#8211;reverse&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>sort from newest to oldest<br />
&nbsp;<wbr>&nbsp;<wbr>-s, &#8211;summary&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>display a summary of each missing patch<br />
&nbsp;<wbr>&nbsp;<wbr>-c, &#8211;creator&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>display the creator of each missing patch<br />
&nbsp;<wbr>&nbsp;<wbr>-D, &#8211;date&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>display the date of each missing patch<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;unqualified&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>print unqualified revision names<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;skip-present&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>skip patches that contain 1 or more patch logs already in this tree </p>
<p> Print a list of patches missing in the project tree containing DIR (or the current directory) for VERSION (or the default version. of the project tree). </p>
<h3>baz join-branch</h3>
<p> <code>add a version as an ancestor of a project tree</code> </p>
<p> <code>Usage:</code> baz join-branch [options] version </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-A, &#8211;archive&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Override&nbsp;<wbr>`my-default-archive&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;dir DIR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Operate on project tree in DIR&nbsp;<wbr>(default&nbsp;<wbr>`.&#8217;)<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;dest DEST&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Instead of modifying the project tree in-place,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>make a copy of it to DEST and apply the result to that<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;unescaped&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show filenames in unescaped form </p>
<p> VERSION&#8211;base-0 must be a continuation (e.g. tag). The command replays the changeset for VERSION&#8211;base-0 in the project tree, which has the effect of adding the log for the branch (making the tag an ancestor of the resulting tree). </p>
<h3>baz sync-tree</h3>
<p> <code>unify a project tree&#8217;s patch-log with a given revision</code> </p>
<p> <code>Usage:</code> baz sync-tree [options] revision </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;dir DIR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Operate on project tree in DIR&nbsp;<wbr>(default&nbsp;<wbr>`.&#8217;)<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;dest DEST&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Instead of modifying the project tree in-place,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>make a copy of it to DEST and apply the result to that<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;unescaped&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show filenames in unescaped form </p>
<p> The new project tree is formed by getting the REVISION and adding all patch-log entries from REVISION. No actual merging is performed &#8212; only the patch-log is changed. </p>
<h3>baz delta</h3>
<p> <code>compute a changeset (or diff) between any two trees or revisions</code> </p>
<p> <code>Usage:</code> baz delta [options] (REVISION|TREE)-A (REVISION|TREE)-B [DESTDIR] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-A, &#8211;archive&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Override&nbsp;<wbr>`my-default-archive&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>-q, &#8211;quiet&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>quiet down progress reports while computing changeset<br />
&nbsp;<wbr>&nbsp;<wbr>-n, &#8211;no-changeset&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>do not generate a changeset<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;diffs&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>print changeset report with diffs&nbsp;<wbr>(implies -n)<br />
&nbsp;<wbr>&nbsp;<wbr>-p, &#8211;show-c-function&nbsp;<wbr>&nbsp;<wbr>Show which C function each change is in.<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;unescaped&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show filenames in unescaped form </p>
<p> Given (REVISION|TREE)-A and (REVISION|TREE)-B, baz will build a changeset that comprises the changes between REVISION-A and REVISION-B </p>
<p> Example:<br />
&nbsp;<wbr>&nbsp;<wbr>baz delta baz&#8211;devo&#8211;1.1&#8211;patch-6&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>baz&#8211;devo&#8211;1.1&#8211;patch-8 ,,changes </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Will pull patch-6 and patch-8 from baz&#8211;devo&#8211;1.1 and compute<br />
&nbsp;<wbr>&nbsp;<wbr>a changeset, which will be saved in a newly created ,,changes<br />
&nbsp;<wbr>&nbsp;<wbr>directory. If you would like a report instead,<br />
&nbsp;<wbr>&nbsp;<wbr>append the &#8211;diffs option</p>
<h2>LOCAL CACHE COMMANDS</h2>
<h3>baz file-find</h3>
<p> <code>find given version of file</code> </p>
<p> <code>Usage:</code> baz file-find [options] file [revision] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-A, &#8211;archive&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Override&nbsp;<wbr>`my-default-archive&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>-N, &#8211;new-file&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Print missing file as&nbsp;<wbr>`/dev/null&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>-s, &#8211;silent&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>suppress reasuring messages<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;unescaped&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show filenames in unescaped form </p>
<p> Print location of file corresponding to FILE in a cached copy of REVISION </p>
<p> The default patch level for a given version is the latest level for which the project tree has a patch. The default archive and version is as printed by &quot;baz tree-version&quot;. </p>
<h3>baz pristines</h3>
<p> <code>list pristine trees in a project tree</code> </p>
<p> <code>Usage:</code> baz pristines [options] [limit] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;dir DIR&nbsp;<wbr>&nbsp;<wbr>cd to DIR first<br />
&nbsp;<wbr>&nbsp;<wbr>-r, &#8211;reverse&nbsp;<wbr>&nbsp;<wbr>reverse sort order </p>
<p> Print the list of pristine revisions cached in project tree DIR (or the current directory). </p>
<h3>baz add-pristine</h3>
<p> <code>ensure that a project tree has a particular pristine revision</code> </p>
<p> <code>Usage:</code> baz add-pristine [options] revision </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-A, &#8211;archive&nbsp;<wbr>&nbsp;<wbr>Override&nbsp;<wbr>`my-default-archive&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;dir DIR&nbsp;<wbr>&nbsp;<wbr>cd to DIR first </p>
<p> Extract REVISION from an archive, creating a pristine copy. Store that pristine copy in the current directory&#8217;s project tree </p>
<h3>baz find-pristine</h3>
<p> <code>find and print the path to a pristine revision</code> </p>
<p> <code>Usage:</code> baz find-pristine [options] revision </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-A, &#8211;archive&nbsp;<wbr>&nbsp;<wbr>Override&nbsp;<wbr>`my-default-archive&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;dir DIR&nbsp;<wbr>&nbsp;<wbr>cd to DIR first<br />
&nbsp;<wbr>&nbsp;<wbr>-s, &#8211;silent&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>exit status only </p>
<p> Print the location of a pristine copy of the indicated revision </p>
<h2>REVISION LIBRARY COMMANDS</h2>
<h3>baz my-revision-library</h3>
<p> <code>print or change your revision library path</code> </p>
<p> <code>Usage:</code> baz my-revision-library [options] [dir] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-e, &#8211;errname&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>specify program name for errors<br />
&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;delete&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>unspecify your revision library<br />
&nbsp;<wbr>&nbsp;<wbr>-s, &#8211;silent&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>suppress reassuring messages<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;search&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>use the full search path<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;add&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>use the full add path<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;search-only&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>use the search-only path<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;add-only&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>use the add-only path<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;first&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>prepend to the path if setting&nbsp;<wbr>(default appends) </p>
<p> With no argument, and without -d, print the path to your revision library. </p>
<p> With an argument, record DIR as the path to your revision library in ~/.arch-params/=revision-library </p>
<p> With the option -d (&#8211;delete) and no argument, ensure that you do not have a revision library path set in ~/.arch-params. </p>
<p> If no revision library is set, the program exits with status 1, printing an error message unless the -s (&#8211;silent) option is given. </p>
<h3>baz library-config</h3>
<p> <code>configure parameters of a revision library</code> </p>
<p> <code>Usage:</code> baz library-config [options] library-dir </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211;greedy&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>make the library greedy<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;non-greedy&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>make the library not greedy<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;sparse&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>make the library sparse<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;non-sparse&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>make the library not sparse </p>
<p> Set/show various parameters for a revision library. </p>
<h3>baz library-find</h3>
<p> <code>find and print the location of a revision in the revision library</code> </p>
<p> <code>Usage:</code> baz library-find [options] revision </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-A, &#8211;archive&nbsp;<wbr>&nbsp;<wbr>Override&nbsp;<wbr>`my-default-archive&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>-e, &#8211;errname&nbsp;<wbr>&nbsp;<wbr>specify program name for errors<br />
&nbsp;<wbr>&nbsp;<wbr>-s, &#8211;silent&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>suppress reassuring messages </p>
<p> Find REVISION in your revision library and print its path. If the revision is not present, print an error message (unless &#8211;silent is specified) and exit with non-0 status. </p>
<h3>baz library-add</h3>
<p> <code>add a revision to the revision library</code> </p>
<p> <code>Usage:</code> baz library-add [options] revision </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-s, &#8211;sparse&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Don&#8217;t fill in gaps in the library.<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;non-sparse&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Fill in gaps in the library.<br />
&nbsp;<wbr>&nbsp;<wbr>-L, &#8211;library LIB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>specify which library to add to<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;for-links PATH&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>require a lib on the same device as PATH<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;unescaped&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show filenames in unescaped form </p>
<p> Add REVISION to your revision library. </p>
<p> This command has no effect and exits with status 0 if the indicated revision is already in the library. </p>
<h3>baz library-remove</h3>
<p> <code>remove a revision from the revision library</code> </p>
<p> <code>Usage:</code> baz library-remove [options] revision </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-A, &#8211;archive&nbsp;<wbr>&nbsp;<wbr>Override&nbsp;<wbr>`my-default-archive&#8217; </p>
<p> Remove REVISION from your revision library. </p>
<p> If the revision is not present, print an error message and exit with non-0 status. </p>
<h3>baz library-archives</h3>
<p> <code>list the archives in your revision library</code> </p>
<p> <code>Usage:</code> baz library-archives [options] </p>
<p> List all archives with records in the revision library. </p>
<h3>baz library-categories</h3>
<p> <code>list the categories in your revision library</code> </p>
<p> <code>Usage:</code> baz library-categories [options] [archive] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-A, &#8211;archive&nbsp;<wbr>&nbsp;<wbr>Override&nbsp;<wbr>`my-default-archive&#8217; </p>
<p> List all categories within a given archive in the revision library. </p>
<h3>baz library-branches</h3>
<p> <code>list the branches in a library category</code> </p>
<p> <code>Usage:</code> baz library-branches [options] [category] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-A, &#8211;archive&nbsp;<wbr>&nbsp;<wbr>Override&nbsp;<wbr>`my-default-archive&#8217; </p>
<p> List all branches within CATEGORY in the revision library. </p>
<h3>baz library-versions</h3>
<p> <code>list the versions in a library branch</code> </p>
<p> <code>Usage:</code> baz library-versions [options] [branch] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-A, &#8211;archive&nbsp;<wbr>&nbsp;<wbr>Override&nbsp;<wbr>`my-default-archive&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>-r, &#8211;reverse&nbsp;<wbr>&nbsp;<wbr>sort from newest to oldest </p>
<p> List all versions within a particular archive/branch with records in the revision library. </p>
<h3>baz library-revisions</h3>
<p> <code>list the revisions in a library version</code> </p>
<p> <code>Usage:</code> baz library-revisions [options] [version] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-A, &#8211;archive&nbsp;<wbr>&nbsp;<wbr>Override&nbsp;<wbr>`my-default-archive&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>-r, &#8211;reverse&nbsp;<wbr>&nbsp;<wbr>sort from newest to oldest<br />
&nbsp;<wbr>&nbsp;<wbr>-f, &#8211;full&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list fully qualified names<br />
&nbsp;<wbr>&nbsp;<wbr>-s, &#8211;summary&nbsp;<wbr>&nbsp;<wbr>print a summary of each patch<br />
&nbsp;<wbr>&nbsp;<wbr>-c, &#8211;creator&nbsp;<wbr>&nbsp;<wbr>print the creator of each patch<br />
&nbsp;<wbr>&nbsp;<wbr>-D, &#8211;date&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>print the date of each patch </p>
<p> List all revisions within a particular archive/version with records in the revision library. </p>
<h3>baz library-log</h3>
<p> <code>output a log message from the revision library</code> </p>
<p> <code>Usage:</code> baz library-log [options] revision </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-A, &#8211;archive&nbsp;<wbr>&nbsp;<wbr>Override&nbsp;<wbr>`my-default-archive&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>-s, &#8211;silent&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>suppress reassuring messages </p>
<p> Print the log message for REVISION from the library. </p>
<h3>baz library-file</h3>
<p> <code>find a file in a revision library</code> </p>
<p> <code>Usage:</code> baz library-file [options] file revision </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-A, &#8211;archive&nbsp;<wbr>&nbsp;<wbr>Override&nbsp;<wbr>`my-default-archive&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;id&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>interpret FILE as an inventory id<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;this&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>interpret FILE as a file within a project tree </p>
<p> Find FILE in REVISION in your revision library and print its path. If the revision or file is not present, print an error message and exit with non-0 status. </p>
<h2>CACHE COMMANDS</h2>
<h3>baz cache-config</h3>
<p> <code>Print or change your cache settings</code> </p>
<p> <code>Usage:</code> baz cache-config [options] [dir] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;disable&nbsp;<wbr>&nbsp;<wbr>Disable caching, and forget the directory </p>
<p> With no argument, and without -d, print the path to your cache. </p>
<p> With an argument, record DIR as the path to your </p>
<p> With the option -d (&#8211;disable) and no argument, disable caching and forget the cache directory </p>
<h2>PUBLISHED REVISIONS COMMANDS</h2>
<h3>baz grab</h3>
<p> <code>grab a published revision</code> </p>
<p> <code>Usage:</code> baz grab [options] location </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211;no-pristines&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>don&#8217;t create pristine copies<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;link&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>hardlink files to revision library instead of copying<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;library&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ensure revisions are in the revision library<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;sparse&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>add library entries sparsely&nbsp;<wbr>(&#8211;link, &#8211;library)<br />
&nbsp;<wbr>&nbsp;<wbr>-r, &#8211;release-id&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>overwrite ./=RELEASE-ID for this config </p>
<p> Grabs a published revision from LOCATION. </p>
<p> A grab file has the following syntax: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Archive-Name:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[the name of the archive]<br />
&nbsp;<wbr>&nbsp;<wbr>Archive-Location:&nbsp;<wbr>[the location of the archive]<br />
&nbsp;<wbr>&nbsp;<wbr>Target-Revision:&nbsp;<wbr>&nbsp;<wbr>[PACKAGE|VERSION|REVISION to get]<br />
&nbsp;<wbr>&nbsp;<wbr>Target-Directory:&nbsp;<wbr>[optional][The suggested directory to get into]<br />
&nbsp;<wbr>&nbsp;<wbr>Target-Config:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[optional][A configuration to build upon grabbing] </p>
<h2>MISCELLANEOUS SCRIPTING SUPPORT</h2>
<h3>baz parse-package-name</h3>
<p> <code>parse a package name</code> </p>
<p> <code>Usage:</code> baz parse-package-name [options] name </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-A, &#8211;archive&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Override&nbsp;<wbr>`my-default-archive&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>-a, &#8211;arch&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>print the archive name<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;non-arch&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>print the non-archive part of the name<br />
&nbsp;<wbr>&nbsp;<wbr>-c, &#8211;category&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>print the category name<br />
&nbsp;<wbr>&nbsp;<wbr>-b, &#8211;branch&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>print the branch name<br />
&nbsp;<wbr>&nbsp;<wbr>-p, &#8211;package&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>print the package name<br />
&nbsp;<wbr>&nbsp;<wbr>-v, &#8211;vsn&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>print the version id<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;package-version&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>print the category&#8211;branch&#8211;version<br />
&nbsp;<wbr>&nbsp;<wbr>-l, &#8211;lvl&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>print the patch level<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;patch-level&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>synonym for &#8211;lvl </p>
<p> Options -b, -B, -p, -v, and -l cancel each other. </p>
<p> For -b, -v, and -l, just the id string is printed without &quot;&#8211;&quot;. </p>
<p> For -p, the output is &quot;&lt;basename&gt;&#8211;&lt;branch&gt;&quot;. </p>
<h3>baz valid-package-name</h3>
<p> <code>test a package name for validity</code> </p>
<p> <code>Usage:</code> baz valid-package-name [options] name </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-e, &#8211;errname&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>specify program name for errors<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;archive&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>require and explicit archive<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;no-archive&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>prohibit and explicit archive<br />
&nbsp;<wbr>&nbsp;<wbr>-c, &#8211;category&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>require a category<br />
&nbsp;<wbr>&nbsp;<wbr>-p, &#8211;package&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>require category, permit branch<br />
&nbsp;<wbr>&nbsp;<wbr>-v, &#8211;vsn&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>require a version number<br />
&nbsp;<wbr>&nbsp;<wbr>-l, &#8211;patch-level&nbsp;<wbr>&nbsp;<wbr>require a patch level<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;lvl&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>synonym for &#8211;patch-level<br />
&nbsp;<wbr>&nbsp;<wbr>-t, &#8211;tolerant&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>tolerate more specific names </p>
<p> Exit with status 0 if PACKAGE is a valid package name, status 1 otherwise. </p>
<p> By default, require a basename or basename plus branch label. </p>
<p> Options -v and -l cancel -b and vice versa. </p>
<p> Option -l implies -v. </p>
<p> If an error name is specified (-e or &#8211;errname), then invalid names cause an error message on stdout. Otherwise, the exit status is the only output. </p>
<p> By default, validation is strict. For example, -b checks for a valid basename and does not permit a branch label or version number. </p>
<p> With -t, more specific names are permitted. For example, -b will permit a branch name, version number, and patch level. </p>
<h3>baz escape</h3>
<p> <code>print strings in escaped or unescaped form</code> </p>
<p> <code>Usage:</code> baz escape [&#8211;unescaped] string </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211;unescaped&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show filenames in unescaped form </p>
<p> Using Pika escaping rules. </p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><i>EDITOR</i></p>
<dd> If $<code>EDITOR</code> is set, use its value as the path of the text editor <code>arch</code> is to run when asking the user for text input. If unset, log messages must be given on the command line using the `-L&#8217; parameter or in the file created by `baz make-log&#8217;.</p>
<dt><i>HOME</i></p>
<dd> User&#8217;s home directory, where <code>arch</code> looks for <i>.arch-cache/</i> and <i>.arch-params/ .</i> </p>
<dt><i>http_proxy HTTP_PROXY</i></p>
<dd> If $<code>http_proxy</code> or $<code>HTTP_PROXY</code> is set, <code>arch</code> used its value as the URL of the proxy to use for WebDAV accesses. $<code>http_proxy</code> has higher priority than $<code>HTTP_PROXY</code>. If unset, no proxy is used.</p>
<dt><i>TMPDIR</i></p>
<dd> If $<code>TMPDIR</code> is set, <code>arch</code> creates temporary files in the given directory. Otherwise, it uses `/tmp&#8217;.</dl>
<h2>FILES</h2>
<dl>
<dt><i>${HOME}/.arch-cache/</i></p>
<dd> Directory where <code>arch</code> caches archive data</p>
<dt><i>${HOME}/.arch-params/</i></p>
<dd> Directory where all the user&#8217;s settings are stored.</p>
<dt><i>${HOME}/.arch-params/hook</i></p>
<dd> Hook script called after every execution of baz.</p>
<dt><i>${HOME}/.arch-params/signing/</i></p>
<dd> Directory where the commands for signing and checking signatures are stored.</dl>
<h2>SEE ALSO</h2>
<p> <code><a rel="nofollow" href="http://bazaar.canonical.com/,">http://bazaar.canonical.com/,</a></code> <code><a rel="nofollow" href="http://wiki.gnuarch.org/,">http://wiki.gnuarch.org/,</a></code> <code><a rel="nofollow" href="http://gnuarch.org/">http://gnuarch.org/</a></code></p>
<h2>Index</h2>

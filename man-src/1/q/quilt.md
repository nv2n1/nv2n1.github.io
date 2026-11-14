---
title: "quilt(1)"
name: "quilt"
section: "1"
letter: "q"
url: "/docs/linux/man/1-quilt/"
description: "quilt – tool to manage series of patches"
---

<h2 class="name">NAME</h2>
<p> quilt &#8211; tool to manage series of patches</p>
<h2>SYNOPSIS</h2>
<p> <code>quilt</code> [-h] command [options] </p>
<h2>DESCRIPTION</h2>
<p> Quilt is a tool to manage large sets of patches by keeping track of the changes each patch makes. Patches can be applied, un-applied, refreshed, etc. The key philosophical concept is that your primary output is patches. </p>
<p> With quilt, all work occurs within a single directory tree. Commands can be invoked from anywhere within the source tree. They are of the form <code>quilt cmd</code> similar to CVS, svn or git commands. They can be abbreviated as long as the specified part of the command is unique. All commands print some help text with <code>quilt cmd -h.</code> </p>
<p> Quilt manages a stack of patches. Patches are applied incrementally on top of the base tree plus all preceding patches. They can be pushed on top of the stack (<code>quilt push</code>), and popped off the stack (<code>quilt pop</code>). Commands are available for querying the contents of the series file (<code>quilt series</code>, see below), the contents of the stack (<code>quilt applied</code>,<code> quilt previous</code>,<code> quilt top</code>), and the patches that are not applied at a particular moment (<code>quilt next</code>,<code> quilt unapplied</code>). By default, most commands apply to the topmost patch on the stack. </p>
<p> Patch files are located in the <i>patches</i> sub-directory of the source tree (see EXAMPLE OF WORKING TREE below). The <i>QUILT_PATCHES</i> environment variable can be used to override this location. When not found in the current directory, that subdirectory is searched recursively in the parent directories (this is similar to the way <i>git</i> searches for its configuration files). The <i>patches</i> directory may contain sub-directories. It may also be a symbolic link instead of a directory. </p>
<p> A file called <i>series</i> contains a list of patch file names that defines the order in which patches are applied. Unless there are means by which series files can be generated automatically, it is usually provided along with a set of patches. In this file, each patch file name is on a separate line. Patch files are identified by path names that are relative to the <i>patches</i> directory; patches may be in sub-directories below this directory. Lines in the series file that start with a hash character (#) are ignored. You can also add a comment after each patch file name, introduced by a space followed by a hash character. When quilt adds, removes, or renames patches, it automatically updates the series file. Users of quilt can modify series files while some patches are applied, as long as the applied patches remain in their original order. </p>
<p> Different series files can be used to assemble patches in different ways, corresponding for example to different development branches. </p>
<p> Before a patch is applied (or &#8220;pushed on the stack&#8221;), copies of all files the patch modifies are saved to the .pc/<i>patch</i> directory. The patch is added to the list of currently applied patches (.pc/applied-patches). Later when a patch is regenerated (<code>quilt refresh</code>), the backup copies in .pc/<i>patch</i> are compared with the current versions of the files in the source tree using GNU diff. </p>
<p> Documentation related to a patch can be put at the beginning of a patch file. Quilt is careful to preserve all text that precedes the actual patch when doing a refresh. (This is limited to patches in unified format; see <code>diff</code> documentation). </p>
<p> The series file is looked up in the .pc directory, in the root of the source tree, and in the patches directory. The first series file that is found is used. This may also be a symbolic link, or a file with multiple hard links. Usually, only one series file is used for a set of patches, so the patches sub-directory is a convenient location. </p>
<p> The .pc directory and its sub-directories cannot be relocated, but it can be a symbolic link. While patches are applied to the source tree, this directory is essential for many operations, including taking patches off the stack (<code>quilt pop</code>), and refreshing patches (<code>quilt refresh</code>). Files in the .pc directory are automatically removed when they are no longer needed, so there is no need to clean up manually. </p>
<h2>QUILT COMMANDS REFERENCE</h2>
<dl>
<dt><code>add</code> [-P patch] {file} &#8230;</p>
<dd>
<p> Add one or more files to the topmost or named patch. Files must be added to the patch before being modified. Files that are modified by patches already applied on top of the specified patch cannot be added. </p>
<dt> -P patch</p>
<dd>
<p> Patch to add files to. </p>
<dt><code>annotate</code> [-P patch] {file}</p>
<dd>
<p> Print an annotated listing of the specified file showing which patches modify which lines. Only applied patches are included. </p>
<dt> -P patch</p>
<dd>
<p> Stop checking for changes at the specified rather than the topmost patch. </p>
<dt><code>applied</code> [patch]</p>
<dd>
<p> Print a list of applied patches, or all patches up to and including the specified patch in the file series. </p>
<dt><code>delete</code> [-r] [&#8211;backup] [patch|-n]</p>
<dd>
<p> Remove the specified or topmost patch from the series file. If the patch is applied, quilt will attempt to remove it first. (Only the topmost patch can be removed right now.) </p>
<dt> -n</p>
<dd> Delete the next patch after topmost, rather than the specified or topmost patch. </p>
<dt> -r</p>
<dd> Remove the deleted patch file from the patches directory as well. </p>
<dt> &#8211;backup</p>
<dd>
<p> Rename the patch file to patch~ rather than deleting it. Ignored if not used with `-r&#8217;. </p>
<dt><code>diff</code> [-p n|-p ab] [-u|-U num|-c|-C num] [&#8211;combine patch|-z] [-R] [-P patch] [&#8211;snapshot] [&#8211;diff=utility] [&#8211;no-timestamps] [&#8211;no-index] [&#8211;sort] [&#8211;color[=always|auto|never]] [file &#8230;]</p>
<dd>
<p> Produces a diff of the specified file(s) in the topmost or specified patch. If no files are specified, all files that are modified are included. </p>
<dt> -p n</p>
<dd> Create a -p n style patch (-p0 or -p1 are supported). </p>
<dt> -p ab</p>
<dd> Create a -p1 style patch, but use a/file and b/file as the original and new filenames instead of the default dir.orig/file and dir/file names. </p>
<dt> -u, -U num, -c, -C num</p>
<dd>
<p> Create a unified diff (-u, -U) with num lines of context. Create a context diff (-c, -C) with num lines of context. The number of context lines defaults to 3. </p>
<dt> &#8211;no-timestamps</p>
<dd>
<p> Do not include file timestamps in patch headers. </p>
<dt> &#8211;no-index</p>
<dd>
<p> Do not output Index: lines. </p>
<dt> -z</p>
<dd> Write to standard output the changes that have been made relative to the topmost or specified patch. </p>
<dt> -R</p>
<dd> Create a reverse diff. </p>
<dt> -P patch</p>
<dd>
<p> Create a diff for the specified patch. (Defaults to the topmost patch.) </p>
<dt> &#8211;combine patch</p>
<dd>
<p> Create a combined diff for all patches between this patch and the patch specified with -P. A patch name of `-&#8216; is equivalent to specifying the first applied patch. </p>
<dt> &#8211;snapshot</p>
<dd>
<p> Diff against snapshot (see `quilt snapshot -h&#8217;). </p>
<dt> &#8211;diff=utility</p>
<dd>
<p> Use the specified utility for generating the diff. The utility is invoked with the original and new file name as arguments. </p>
<dt> &#8211;color[=always|auto|never]</p>
<dd>
<p> Use syntax coloring (auto activates it only if the output is a tty). </p>
<dt> &#8211;sort</p>
<dd> Sort files by their name instead of preserving the original order. </p>
<dt><code>edit</code> file &#8230;</p>
<dd>
<p> Edit the specified file(s) in $EDITOR after adding it (them) to the topmost patch. </p>
<dt><code>files</code> [-v] [-a] [-l] [&#8211;combine patch] [patch]</p>
<dd>
<p> Print the list of files that the topmost or specified patch changes. </p>
<dt> -a</p>
<dd> List all files in all applied patches. </p>
<dt> -l</p>
<dd> Add patch name to output. </p>
<dt> -v</p>
<dd> Verbose, more user friendly output. </p>
<dt> &#8211;combine patch</p>
<dd>
<p> Create a listing for all patches between this patch and the topmost or specified patch. A patch name of `-&#8216; is equivalent to specifying the first applied patch. </p>
<dt><code>fold</code> [-R] [-q] [-f] [-p strip-level]</p>
<dd>
<p> Integrate the patch read from standard input into the topmost patch: After making sure that all files modified are part of the topmost patch, the patch is applied with the specified strip level (which defaults to 1). </p>
<dt> -R</p>
<dd> Apply patch in reverse. </p>
<dt> -q</p>
<dd> Quiet operation. </p>
<dt> -f</p>
<dd> Force apply, even if the patch has rejects. Unless in quiet mode, apply the patch interactively: the patch utility may ask questions. </p>
<dt> -p strip-level</p>
<dd>
<p> The number of pathname components to strip from file names when applying patchfile. </p>
<dt><code>fork</code> [new_name]</p>
<dd>
<p> Fork the topmost patch. Forking a patch means creating a verbatim copy of it under a new name, and use that new name instead of the original one in the current series. This is useful when a patch has to be modified, but the original version of it should be preserved, e.g. because it is used in another series, or for the history. A typical sequence of commands would be: fork, edit, refresh. </p>
<p> If new_name is missing, the name of the forked patch will be the current patch name, followed by `-2&#8242;. If the patch name already ends in a dash-and-number, the number is further incremented (e.g., patch.diff, patch-2.diff, patch-3.diff). </p>
<dt><code>graph</code> [&#8211;all] [&#8211;reduce] [&#8211;lines[=num]] [&#8211;edge-labels=files] [-T ps] [patch]</p>
<dd>
<p> Generate a <a href="/docs/linux/man/1-dot/">dot</a>(1) directed graph showing the dependencies between applied patches. A patch depends on another patch if both touch the same file or, with the &#8211;lines option, if their modifications overlap. Unless otherwise specified, the graph includes all patches that the topmost patch depends on. When a patch name is specified, instead of the topmost patch, create a graph for the specified patch. The graph will include all other patches that this patch depends on, as well as all patches that depend on this patch. </p>
<dt> &#8211;all</p>
<dd> Generate a graph including all applied patches and their dependencies. (Unapplied patches are not included.) </p>
<dt> &#8211;reduce</p>
<dd>
<p> Eliminate transitive edges from the graph. </p>
<dt> &#8211;lines[=num]</p>
<dd>
<p> Compute dependencies by looking at the lines the patches modify. Unless a different num is specified, two lines of context are included. </p>
<dt> &#8211;edge-labels=files</p>
<dd>
<p> Label graph edges with the file names that the adjacent patches modify. </p>
<dt> -T ps</p>
<dd> Directly produce a PostScript output file. </p>
<dt><code>grep</code> [-h|options] {pattern}</p>
<dd>
<p> Grep through the source files, recursively, skipping patches and quilt meta-information. If no filename argument is given, the whole source tree is searched. Please see the <a href="/docs/linux/man/1-grep/">grep</a>(1) manual page for options. </p>
<dt> -h</p>
<dd> Print this help. The grep -h option can be passed after a double-dash (&#8211;). Search expressions that start with a dash can be passed after a second double-dash (&#8211; &#8211;). </p>
<dt><code>header</code> [-a|-r|-e] [&#8211;backup] [&#8211;strip-diffstat] [&#8211;strip-trailing-whitespace] [patch]</p>
<dd>
<p> Print or change the header of the topmost or specified patch. </p>
<dt> -a, -r, -e</p>
<dd>
<p> Append to (-a) or replace (-r) the exiting patch header, or edit (-e) the header in $EDITOR. If none of these options is given, print the patch header. </p>
<dt> &#8211;strip-diffstat</p>
<dd>
<p> Strip diffstat output from the header. </p>
<dt> &#8211;strip-trailing-whitespace</p>
<dd>
<p> Strip trailing whitespace at the end of lines of the header. </p>
<dt> &#8211;backup</p>
<dd>
<p> Create a backup copy of the old version of a patch as patch~. </p>
<dt><code>import</code> [-p num] [-R] [-P patch] [-f] [-d {o|a|n}] patchfile &#8230;</p>
<dd>
<p> Import external patches. The patches will be inserted following the current top patch, and must be pushed after import to apply them. </p>
<dt> -p num</p>
<dd>
<p> Number of directory levels to strip when applying (default=1) </p>
<dt> -R</p>
<dd>
<p> Apply patch in reverse. </p>
<dt> -P patch</p>
<dd>
<p> Patch filename to use inside quilt. This option can only be used when importing a single patch. </p>
<dt> -f</p>
<dd> Overwrite/update existing patches. </p>
<dt> -d {o|a|n}</p>
<dd>
<p> When overwriting in existing patch, keep the old (o), all (a), or new (n) patch header. If both patches include headers, this option must be specified. This option is only effective when -f is used. </p>
<dt><code>mail</code> {&#8211;mbox file|&#8211;send} [-m text] [-M file] [&#8211;prefix prefix] [&#8211;sender &#8230;] [&#8211;from &#8230;] [&#8211;to &#8230;] [&#8211;cc &#8230;] [&#8211;bcc &#8230;] [&#8211;subject &#8230;] [&#8211;reply-to message] [first_patch [last_patch]]</p>
<dd>
<p> Create mail messages from a specified range of patches, or all patches in the series file, and either store them in a mailbox file, or send them immediately. The editor is opened with a template for the introduction. Please see /usr/share/doc/quilt-0.63/README.MAIL for details. When specifying a range of patches, a first patch name of `-&#8216; denotes the first, and a last patch name of `-&#8216; denotes the last patch in the series. </p>
<dt> -m text</p>
<dd>
<p> Text to use as the text in the introduction. When this option is used, the editor will not be invoked, and the patches will be processed immediately. </p>
<dt> -M file</p>
<dd>
<p> Like the -m option, but read the introduction from file. </p>
<dt> &#8211;prefix prefix</p>
<dd>
<p> Use an alternate prefix in the bracketed part of the subjects generated. Defaults to `patch&#8217;. </p>
<dt> &#8211;mbox file</p>
<dd>
<p> Store all messages in the specified file in mbox format. The mbox can later be sent using formail, for example. </p>
<dt> &#8211;send</p>
<dd>
<p> Send the messages directly. </p>
<dt> &#8211;sender</p>
<dd>
<p> The envelope sender address to use. The address must be of the form `user [at] domain.name&#8217;. No display name is allowed. </p>
<dt> &#8211;from, &#8211;subject</p>
<dd>
<p> The values for the From and Subject headers to use. If no &#8211;from option is given, the value of the &#8211;sender option is used. </p>
<dt> &#8211;to, &#8211;cc, &#8211;bcc</p>
<dd>
<p> Append a recipient to the To, Cc, or Bcc header. </p>
<dt> &#8211;signature file</p>
<dd>
<p> Append the specified signature to messages (defaults to ~/.signature if found; use `-&#8216; for no signature). </p>
<dt> &#8211;reply-to message</p>
<dd>
<p> Add the appropriate headers to reply to the specified message. </p>
<dt><code>new</code> [-p n|-p ab] {patchname}</p>
<dd>
<p> Create a new patch with the specified file name, and insert it after the topmost patch. The name can be prefixed with a sub-directory name, allowing for grouping related patches together. </p>
<dt> -p n</p>
<dd> Create a -p n style patch (-p0 or -p1 are supported). </p>
<dt> -p ab</p>
<dd> Create a -p1 style patch, but use a/file and b/file as the original and new filenames instead of the default dir.orig/file and dir/file names. </p>
<p> Quilt can be used in sub-directories of a source tree. It determines the root of a source tree by searching for a patches directory above the current working directory. Create a patches directory in the intended root directory if quilt chooses a top-level directory that is too high up in the directory tree. </p>
<dt><code>next</code> [patch]</p>
<dd>
<p> Print the name of the next patch after the specified or topmost patch in the series file. </p>
<dt><code>patches</code> [-v] [&#8211;color[=always|auto|never]] {file} [files&#8230;]</p>
<dd>
<p> Print the list of patches that modify any of the specified files. (Uses a heuristic to determine which files are modified by unapplied patches. Note that this heuristic is much slower than scanning applied patches.) </p>
<dt> -v</p>
<dd> Verbose, more user friendly output. </p>
<dt> &#8211;color[=always|auto|never]</p>
<dd>
<p> Use syntax coloring (auto activates it only if the output is a tty). </p>
<dt><code>pop</code> [-afRqv] [num|patch]</p>
<dd>
<p> Remove patch(es) from the stack of applied patches. Without options, the topmost patch is removed. When a number is specified, remove the specified number of patches. When a patch name is specified, remove patches until the specified patch end up on top of the stack. Patch names may include the patches/ prefix, which means that filename completion can be used. </p>
<dt> -a</p>
<dd> Remove all applied patches. </p>
<dt> -f</p>
<dd> Force remove. The state before the patch(es) were applied will be restored from backup files. </p>
<dt> -R</p>
<dd> Always verify if the patch removes cleanly; don&#8217;t rely on timestamp checks. </p>
<dt> -q</p>
<dd> Quiet operation. </p>
<dt> -v</p>
<dd> Verbose operation. </p>
<dt><code>previous</code> [patch]</p>
<dd>
<p> Print the name of the previous patch before the specified or topmost patch in the series file. </p>
<dt><code>push</code> [-afqv] [&#8211;merge[=merge|diff3]] [&#8211;leave-rejects] [&#8211;color[=always|auto|never]] [num|patch]</p>
<dd>
<p> Apply patch(es) from the series file. Without options, the next patch in the series file is applied. When a number is specified, apply the specified number of patches. When a patch name is specified, apply all patches up to and including the specified patch. Patch names may include the patches/ prefix, which means that filename completion can be used. </p>
<dt> -a</p>
<dd> Apply all patches in the series file. </p>
<dt> -q</p>
<dd> Quiet operation. </p>
<dt> -f</p>
<dd> Force apply, even if the patch has rejects. Unless in quiet mode, apply the patch interactively: the patch utility may ask questions. </p>
<dt> -v</p>
<dd> Verbose operation. </p>
<dt> &#8211;fuzz=N</p>
<dd>
<p> Set the maximum fuzz factor (default: 2). </p>
<dt> -m, &#8211;merge[=merge|diff3]</p>
<dd>
<p> Merge the patch file into the original files (see <a href="/docs/linux/man/1-patch/">patch</a>(1)). </p>
<dt> &#8211;leave-rejects</p>
<dd>
<p> Leave around the reject files patch produced, even if the patch is not actually applied. </p>
<dt> &#8211;color[=always|auto|never]</p>
<dd>
<p> Use syntax coloring (auto activates it only if the output is a tty). </p>
<dt><code>refresh</code> [-p n|-p ab] [-u|-U num|-c|-C num] [-z[new_name]] [-f] [&#8211;no-timestamps] [&#8211;no-index] [&#8211;diffstat] [&#8211;sort] [&#8211;backup] [&#8211;strip-trailing-whitespace] [patch]</p>
<dd>
<p> Refreshes the specified patch, or the topmost patch by default. Documentation that comes before the actual patch in the patch file is retained. </p>
<p> It is possible to refresh patches that are not on top. If any patches on top of the patch to refresh modify the same files, the script aborts by default. Patches can still be refreshed with -f. In that case this script will print a warning for each shadowed file, changes by more recent patches will be ignored, and only changes in files that have not been modified by any more recent patches will end up in the specified patch. </p>
<dt> -p n</p>
<dd> Create a -p n style patch (-p0 or -p1 supported). </p>
<dt> -p ab</p>
<dd> Create a -p1 style patch, but use a/file and b/file as the original and new filenames instead of the default dir.orig/file and dir/file names. </p>
<dt> -u, -U num, -c, -C num</p>
<dd>
<p> Create a unified diff (-u, -U) with num lines of context. Create a context diff (-c, -C) with num lines of context. The number of context lines defaults to 3. </p>
<dt> -z[new_name]</p>
<dd>
<p> Create a new patch containing the changes instead of refreshing the topmost patch. If no new name is specified, `-2&#8242; is added to the original patch name, etc. (See the fork command.) </p>
<dt> &#8211;no-timestamps</p>
<dd>
<p> Do not include file timestamps in patch headers. </p>
<dt> &#8211;no-index</p>
<dd>
<p> Do not output Index: lines. </p>
<dt> &#8211;diffstat</p>
<dd>
<p> Add a diffstat section to the patch header, or replace the existing diffstat section. </p>
<dt> -f</p>
<dd> Enforce refreshing of a patch that is not on top. </p>
<dt> &#8211;backup</p>
<dd>
<p> Create a backup copy of the old version of a patch as patch~. </p>
<dt> &#8211;sort</p>
<dd> Sort files by their name instead of preserving the original order. </p>
<dt> &#8211;strip-trailing-whitespace</p>
<dd>
<p> Strip trailing whitespace at the end of lines. </p>
<dt><code>remove</code> [-P patch] {file} &#8230;</p>
<dd>
<p> Remove one or more files from the topmost or named patch. Files that are modified by patches on top of the specified patch cannot be removed. </p>
<dt> -P patch</p>
<dd>
<p> Remove named files from the named patch. </p>
<dt><code>rename</code> [-P patch] new_name</p>
<dd>
<p> Rename the topmost or named patch. </p>
<dt> -P patch</p>
<dd>
<p> Patch to rename. </p>
<dt><code>revert</code> [-P patch] {file} &#8230;</p>
<dd>
<p> Revert uncommitted changes to the topmost or named patch for the specified file(s): after the revert, &#8216;quilt diff -z&#8217; will show no differences for those files. Changes to files that are modified by patches on top of the specified patch cannot be reverted. </p>
<dt> -P patch</p>
<dd>
<p> Revert changes in the named patch. </p>
<dt><code>series</code> [&#8211;color[=always|auto|never]] [-v]</p>
<dd>
<p> Print the names of all patches in the series file. </p>
<dt> &#8211;color[=always|auto|never]</p>
<dd>
<p> Use syntax coloring (auto activates it only if the output is a tty). </p>
<dt> -v</p>
<dd> Verbose, more user friendly output. </p>
<dt><code>setup</code> [-d path-prefix] [-v] [&#8211;sourcedir dir] [&#8211;fuzz=N] {specfile|seriesfile}</p>
<dd>
<p> Initializes a source tree from an rpm spec file or a quilt series file. </p>
<dt> -d</p>
<dd> Optional path prefix for the resulting source tree. </p>
<dt> &#8211;sourcedir</p>
<dd>
<p> Directory that contains the package sources. Defaults to `.&#8217;. </p>
<dt> -v</p>
<dd> Verbose debug output. </p>
<dt> &#8211;fuzz=N</p>
<dd>
<p> Set the maximum fuzz factor (needs rpm 4.6 or later). </p>
<dt><code>snapshot</code> [-d]</p>
<dd>
<p> Take a snapshot of the current working state. After taking the snapshot, the tree can be modified in the usual ways, including pushing and popping patches. A diff against the tree at the moment of the snapshot can be generated with `quilt diff &#8211;snapshot&#8217;. </p>
<dt> -d</p>
<dd> Only remove current snapshot. </p>
<dt><code>top</code></p>
<dd>
<p> Print the name of the topmost patch on the current stack of applied patches. </p>
<dt><code>unapplied</code> [patch]</p>
<dd>
<p> Print a list of patches that are not applied, or all patches that follow the specified patch in the series file. </p>
<dt><code>upgrade</code></p>
<dd>
<p> Upgrade the meta-data in a working tree from an old version of quilt to the current version. This command is only needed when the quilt meta-data format has changed, and the working tree still contains old-format meta-data. In that case, quilt will request to run `quilt upgrade&#8217;. </p>
</dl>
<h2>COMMON OPTIONS TO ALL COMMANDS</h2>
<dl>
<dt><code>&#8211;trace</code></p>
<dd>
<p> Runs the command in bash trace mode (-x). For internal debugging. </p>
<dt><code>&#8211;quiltrc</code> file</p>
<dd>
<p> Use the specified configuration file instead of ~/.quiltrc (or /etc/quilt.quiltrc if ~/.quiltrc does not exist). See the pdf documentation for details about its possible contents. The special value &quot;-&quot; causes quilt not to read any configuration file. </p>
<dt><code>&#8211;version</code></p>
<dd>
<p> Print the version number and exit immediately. </p>
</dl>
<h2>EXIT STATUS</h2>
<p> The exit status is 0 if the sub-command was successfully executed, and 1 in case of error. </p>
<p> An exit status of 2 denotes that quilt did not do anything to complete the command. This happens in particular when asking to push when the whole stack is already pushed, or asking to pop when the whole stack is already popped. This behavior is intended to ease the scripting around quilt. </p>
<h2>EXAMPLE OF WORKING TREE</h2>
<dl>
<dt>
<dd>
<pre>
work/
├── patches/
│    ├── series         (list of patches to apply)
│    ├── patch1.diff    (one particular patch)
│    ├── patch2.diff
│    └── ...
├── .pc/
│    ├── .quilt_patches (content of QUILT_PATCHES)
│    ├── .quilt_series  (content of QUILT_SERIES)
│    ├── patch1.diff/   (copy of patched files)
│    │    └── ...
│    ├── patch2.diff/
│    │    └── ...
│    └── ...
└── ...
</pre>
</dl>
<p> The patches/ directory is precious as it contains all your patches as well as the order in which it should be applied. </p>
<p> The .pc/ directory contains some metadata about the current state of your patch serie. Changing its content is not advised. This directory can usually be regenerated from the initial files and the content of the patches/ directory (provided that all patches were regenerated before the removal). </p>
<h2>EXAMPLE</h2>
<p> Please refer to the pdf documentation for a full example of use. </p>
<h2>CONFIGURATION FILE</h2>
<p> Upon startup, quilt evaluates the file .quiltrc in the user&#8217;s home directory, or the file specified with the &#8211;quiltrc option. This file is a regular bash script. Default options can be passed to any COMMAND by defining a QUILT_${COMMAND}_ARGS variable. For example, QUILT_DIFF_ARGS=&quot;&#8211;color=auto&quot; causes the output of quilt diff to be syntax colored when writing to a terminal. </p>
<p> In addition to that, quilt recognizes the following variables: </p>
<dl>
<dt>EDITOR</p>
<dd>
<p> The program to run to edit files. If it isn&#8217;t redefined in the configuration file, $EDITOR as defined in the environment will be used. </p>
<dt>LESS</p>
<dd>
<p> The arguments used to invoke the pager. Inherits the existing value of $LESS if LESS is already set in the environment, otherwise defaults to &quot;-FRSX&quot;. </p>
<dt>QUILT_DIFF_OPTS</p>
<dd>
<p> Additional options that quilt shall pass to GNU diff when generating patches. A useful setting for C source code is &quot;-p&quot;, which causes GNU diff to show in the resulting patch which function a change is in. </p>
<dt>QUILT_PATCH_OPTS</p>
<dd>
<p> Additional options that quilt shall pass to GNU patch when applying patches. For example, recent versions of GNU patch support the &quot;&#8211;reject-format=unified&quot; option for generating reject files in unified diff style (older patch versions used &quot;&#8211;unified-reject-files&quot; for that). </p>
<p> You may also want to add the &quot;-E&quot; option if you have issues with quilt not deleting empty files when you think it should. The documentation of GNU patch says that &quot;normally this option is unnecessary&quot;, but when patch is in POSIX mode or if the patch format doesn&#8217;t allow to distinguish empty files from deleted files, patch deletes empty files only if the -E option is given. Beware that when passing -E to patch, quilt will no longer be able to deal with empty files, which is why using -E is no longer the default. </p>
<dt>QUILT_DIFFSTAT_OPTS</p>
<dd>
<p> Additional options that quilt shall pass to diffstat when generating patch statistics. For example, &quot;-f0&quot; can be used for an alternative output format. Recent versions of diffstat also support alternative rounding methods (&quot;-r1&quot;, &quot;-r2&quot;). </p>
<dt>QUILT_PATCHES</p>
<dd>
<p> The location of patch files, defaulting to &quot;patches&quot;. </p>
<dt>QUILT_SERIES</p>
<dd>
<p> The name of the series file, defaulting to &quot;series&quot;. Unless an absolute path is used, the search algorithm described above applies. </p>
<dt>QUILT_PATCHES_PREFIX</p>
<dd>
<p> If set to anything, quilt will prefix patch names it prints with their directory (QUILT_PATCHES). </p>
<dt>QUILT_NO_DIFF_INDEX</p>
<dd>
<p> By default, quilt prepends an Index: line to the patches it generates. If this variable is set to anything, no line is prepended. This is a shortcut to adding &#8211;no-index to both QUILT_DIFF_ARGS and QUILT_REFRESH_ARGS. </p>
<dt>QUILT_NO_DIFF_TIMESTAMPS</p>
<dd>
<p> By default, quilt includes timestamps in headers when generating patches. If this variable is set to anything, no timestamp will be included. This is a shortcut to adding &#8211;no-timestamps to both QUILT_DIFF_ARGS and QUILT_REFRESH_ARGS. </p>
<dt>QUILT_PAGER</p>
<dd>
<p> The pager quilt shall use for commands which produce paginated output. If unset, the values of GIT_PAGER or PAGER is used. If none of these variables is set, &quot;less -R&quot; is used. An empty value indicates that no pager should be used. </p>
<dt>QUILT_COLORS</p>
<dd>
<p> By default, quilt uses its predefined color set in order to be more comprehensible when distiguishing various types of patches, eg. applied/unapplied, failed, etc. </p>
<p> To override one or more color settings, set the QUILT_COLORS variable in following syntax &#8211; colon (:) separated list of elements, each being of the form &lt;format name&gt;=&lt;foreground color&gt;[;&lt;background color&gt;] </p>
<p> Format names with their respective default values are listed below, along with their usage(s). Color codes(values) are standard bash coloring escape codes. See more at <a rel="nofollow" href="http://tldp.org/LDP/abs/html/colorizing.html#AEN20229">http://tldp.org/LDP/abs/html/colorizing.html#AEN20229</a> </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>diff_hdr</code></p>
<dd> Used in &#8216;quilt diff&#8217; to color the index line. Defaults to 32 (green). </p>
<dt><code>diff_add</code></p>
<dd> Used in &#8216;quilt diff&#8217; to color added lines. Defaults to 36 (azure). </p>
<dt><code>diff_mod</code></p>
<dd> Used in &#8216;quilt diff&#8217; to color modified lines. Defaults to 35 (purple). </p>
<dt><code>diff_rem</code></p>
<dd> Used in &#8216;quilt diff&#8217; to color removed lines. Defaults to 35 (purple). </p>
<dt><code>diff_hunk</code></p>
<dd> Used in &#8216;quilt diff&#8217; to color hunk header. Defaults to 33 (brown/orange). </p>
<dt><code>diff_ctx</code></p>
<dd> Used in &#8216;quilt diff&#8217; to color the text after end of hunk header (diff &#8211;show-c-function generates this). Defaults to 35 (purple). </p>
<dt><code>diff_cctx</code></p>
<dd> Used in &#8216;quilt diff&#8217; to color the 15-asterisk sequence before or after a hunk. Defaults to 33 (brown/orange). </p>
<dt><code>patch_fuzz</code></p>
<dd> Used in &#8216;quilt push&#8217; to color the patch fuzz information. Defaults to 35 (purple). </p>
<dt><code>patch_fail</code></p>
<dd> Used in &#8216;quilt push&#8217; to color the fail message. Defaults to 31 (red). </p>
<dt><code>series_app</code></p>
<dd> Used in &#8216;quilt series&#8217; and &#8216;quilt patches&#8217; to color the applied patch names. Defaults to 32 (green). </p>
<dt><code>series_top</code></p>
<dd> Used in &#8216;quilt series&#8217; and &#8216;quilt patches&#8217; to color the top patch name. Defaults to 33 (brown/orange). </p>
<dt><code>series_una</code></p>
<dd> Used in &#8216;quilt series&#8217; and &#8216;quilt patches&#8217; to color unapplied patch names. Defaults to 0 (no special color). </p>
</dl>
</dl>
<dl>
<dt>
<dd> In addition, the <code>clear</code> format name is used to turn off special coloring. Its value is 0; it is not advised to modify it. </p>
<p> The content of QUILT_COLORS supersedes default values. So the value diff_hdr=35;44 will get you the diff headers in magenta over blue instead of the default green over unchanged background. For that, add the following content to ~/.quiltrc (or /etc/quilt.quiltrc): </p>
<pre>
QUILT_DIFF_ARGS=&quot;--color&quot;
QUILT_COLORS='diff_hdr=35;44'
</pre>
</dl>
</dl>
<h2>AUTHORS</h2>
<p> Quilt started as a series of scripts written by Andrew Morton (patch-scripts). Based on Andrew&#8217;s ideas, Andreas Gruenbacher completely rewrote the scripts, with the help of several other contributors (see AUTHORS file in the distribution). </p>
<p> This man page was written by Martin Quinson, based on information found in the pdf documentation, and in the help messages of each commands. </p>
<h2>SEE ALSO</h2>
<p> The pdf documentation, which should be under /usr/share/doc/quilt-0.63/quilt.pdf. Note that some distributors compress this file. <code>zxpdf</code>(<code>1</code>) can be used to display compressed pdf files. </p>
<p> <code>diff</code>(<code>1</code>), <code>patch</code>(<code>1</code>). </p>
<h2>Index</h2>

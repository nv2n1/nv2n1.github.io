---
title: "git-update-index(1)"
name: "git-update-index"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-update-index/"
description: "git-update-index – Register file contents in the working tree to the index"
---

<h2 class="name">NAME</h2>
<p> git-update-index &#8211; Register file contents in the working tree to the index </p>
<h2>SYNOPSIS</h2>
<pre><code>
git update - index
                 [--add][--remove | --force - remove][--replace]
                 [--refresh][-q][--unmerged][--ignore - missing]
                 [(--cacheinfo&lt;mode&gt;, &lt;object&gt;, &lt;file&gt;)...]
                 [--chmod = (+ | -) x]
                 [--[no - ] assume - unchanged]
                 [--[no - ] skip - worktree]
                 [--[no - ] ignore - skip - worktree - entries]
                 [--[no - ] fsmonitor - valid]
                 [--ignore - submodules]
                 [--[no - ] split - index]
                 [--[no - | test - | force - ] untracked - cache]
                 [--[no - ] fsmonitor]
                 [--really - refresh][--unresolve][--again | -g]
                 [--info - only][--index - info]
                 [-z][--stdin][--index - version&lt;n&gt;]
                 [--verbose]
                 [--][&lt;file&gt;...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Modifies the index. Each file mentioned is updated into the index and any <i>unmerged</i> or <i>needs updating</i> state is cleared. </p>
<p> See also <code><a href="/docs/linux/man/1-git-add/">git-add</a></code>(1) for a more user-friendly way to do some of the most common operations on the index. </p>
<p> The way <i>git update-index</i> handles files it is told about can be modified using the various options:</p>
<h2>OPTIONS</h2>
<p> &#8211;add</p>
<dl>
<dt>
<dd> If a specified file isn&#8217;t in the index already then it&#8217;s added. Default behaviour is to ignore new files.</dl>
<p> &#8211;remove</p>
<dl>
<dt>
<dd> If a specified file is in the index but is missing then it&#8217;s removed. Default behavior is to ignore removed file.</dl>
<p> &#8211;refresh</p>
<dl>
<dt>
<dd> Looks at the current index and checks to see if merges or updates are needed by checking stat() information.</dl>
<p> -q</p>
<dl>
<dt>
<dd> Quiet. If &#8211;refresh finds that the index needs an update, the default behavior is to error out. This option makes <i>git update-index</i> continue anyway.</dl>
<p> &#8211;ignore-submodules</p>
<dl>
<dt>
<dd> Do not try to update submodules. This option is only respected when passed before &#8211;refresh.</dl>
<p> &#8211;unmerged</p>
<dl>
<dt>
<dd> If &#8211;refresh finds unmerged changes in the index, the default behavior is to error out. This option makes <i>git update-index</i> continue anyway.</dl>
<p> &#8211;ignore-missing</p>
<dl>
<dt>
<dd> Ignores missing files during a &#8211;refresh</dl>
<p> &#8211;cacheinfo &lt;mode&gt;,&lt;object&gt;,&lt;path&gt;, &#8211;cacheinfo &lt;mode&gt; &lt;object&gt; &lt;path&gt;</p>
<dl>
<dt>
<dd> Directly insert the specified info into the index. For backward compatibility, you can also give these three arguments as three separate parameters, but new users are encouraged to use a single-parameter form.</dl>
<p> &#8211;index-info</p>
<dl>
<dt>
<dd> Read index information from stdin.</dl>
<p> &#8211;chmod=(+|-)x</p>
<dl>
<dt>
<dd> Set the execute permissions on the updated files.</dl>
<p> &#8211;[no-]assume-unchanged</p>
<dl>
<dt>
<dd> When this flag is specified, the object names recorded for the paths are not updated. Instead, this option sets/unsets the &quot;assume unchanged&quot; bit for the paths. When the &quot;assume unchanged&quot; bit is on, the user promises not to change the file and allows Git to assume that the working tree file matches what is recorded in the index. If you want to change the working tree file, you need to unset the bit to tell Git. This is sometimes helpful when working with a big project on a filesystem that has very slow <a href="/docs/linux/man/2-lstat/">lstat</a>(2) system call (e.g. cifs). </p>
<p> Git will fail (gracefully) in case it needs to modify this file in the index e.g. when merging in a commit; thus, in case the assumed-untracked file is changed upstream, you will need to handle the situation manually.</dl>
<p> &#8211;really-refresh</p>
<dl>
<dt>
<dd> Like <code>&#8211;refresh</code>, but checks stat information unconditionally, without regard to the &quot;assume unchanged&quot; setting.</dl>
<p> &#8211;[no-]skip-worktree</p>
<dl>
<dt>
<dd> When one of these flags is specified, the object name recorded for the paths are not updated. Instead, these options set and unset the &quot;skip-worktree&quot; bit for the paths. See section &quot;Skip-worktree bit&quot; below for more information.</dl>
<p> &#8211;[no-]ignore-skip-worktree-entries</p>
<dl>
<dt>
<dd> Do not remove skip-worktree (AKA &quot;index-only&quot;) entries even when the <code>&#8211;remove</code> option was specified.</dl>
<p> &#8211;[no-]fsmonitor-valid</p>
<dl>
<dt>
<dd> When one of these flags is specified, the object name recorded for the paths are not updated. Instead, these options set and unset the &quot;fsmonitor valid&quot; bit for the paths. See section &quot;File System Monitor&quot; below for more information.</dl>
<p> -g, &#8211;again</p>
<dl>
<dt>
<dd> Runs <i>git update-index</i> itself on the paths whose index entries are different from those from the <code>HEAD</code> commit.</dl>
<p> &#8211;unresolve</p>
<dl>
<dt>
<dd> Restores the <i>unmerged</i> or <i>needs updating</i> state of a file during a merge if it was cleared by accident.</dl>
<p> &#8211;info-only</p>
<dl>
<dt>
<dd> Do not create objects in the object database for all &lt;file&gt; arguments that follow this flag; just insert their object IDs into the index.</dl>
<p> &#8211;force-remove</p>
<dl>
<dt>
<dd> Remove the file from the index even when the working directory still has such a file. (Implies &#8211;remove.)</dl>
<p> &#8211;replace</p>
<dl>
<dt>
<dd> By default, when a file <code>path</code> exists in the index, <i>git update-index</i> refuses an attempt to add <code>path/file</code>. Similarly if a file <code>path/file</code> exists, a file <code>path</code> cannot be added. With &#8211;replace flag, existing entries that conflict with the entry being added are automatically removed with warning messages.</dl>
<p> &#8211;stdin</p>
<dl>
<dt>
<dd> Instead of taking list of paths from the command line, read list of paths from the standard input. Paths are separated by LF (i.e. one path per line) by default.</dl>
<p> &#8211;verbose</p>
<dl>
<dt>
<dd> Report what is being added and removed from index.</dl>
<p> &#8211;index-version &lt;n&gt;</p>
<dl>
<dt>
<dd> Write the resulting index out in the named on-disk format version. Supported versions are 2, 3 and 4. The current default version is 2 or 3, depending on whether extra features are used, such as <code>git add -N</code>. </p>
<p> Version 4 performs a simple pathname compression that reduces index size by 30%-50% on large repositories, which results in faster load time. Version 4 is relatively young (first released in 1.8.0 in October 2012). Other Git implementations such as JGit and libgit2 may not support it yet.</dl>
<p> -z</p>
<dl>
<dt>
<dd> Only meaningful with <code>&#8211;stdin</code> or <code>&#8211;index-info</code>; paths are separated with NUL character instead of LF.</dl>
<p> &#8211;split-index, &#8211;no-split-index</p>
<dl>
<dt>
<dd> Enable or disable split index mode. If split-index mode is already enabled and <code>&#8211;split-index</code> is given again, all changes in $GIT_DIR/index are pushed back to the shared index file. </p>
<p> These options take effect whatever the value of the <code>core.splitIndex</code> configuration variable (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)). But a warning is emitted when the change goes against the configured value, as the configured value will take effect next time the index is read and this will remove the intended effect of the option.</dl>
<p> &#8211;untracked-cache, &#8211;no-untracked-cache</p>
<dl>
<dt>
<dd> Enable or disable untracked cache feature. Please use <code>&#8211;test-untracked-cache</code> before enabling it. </p>
<p> These options take effect whatever the value of the <code>core.untrackedCache</code> configuration variable (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)). But a warning is emitted when the change goes against the configured value, as the configured value will take effect next time the index is read and this will remove the intended effect of the option.</dl>
<p> &#8211;test-untracked-cache</p>
<dl>
<dt>
<dd> Only perform tests on the working directory to make sure untracked cache can be used. You have to manually enable untracked cache using <code>&#8211;untracked-cache</code> or <code>&#8211;force-untracked-cache</code> or the <code>core.untrackedCache</code> configuration variable afterwards if you really want to use it. If a test fails the exit code is 1 and a message explains what is not working as needed, otherwise the exit code is 0 and OK is printed.</dl>
<p> &#8211;force-untracked-cache</p>
<dl>
<dt>
<dd> Same as <code>&#8211;untracked-cache</code>. Provided for backwards compatibility with older versions of Git where <code>&#8211;untracked-cache</code> used to imply <code>&#8211;test-untracked-cache</code> but this option would enable the extension unconditionally.</dl>
<p> &#8211;fsmonitor, &#8211;no-fsmonitor</p>
<dl>
<dt>
<dd> Enable or disable files system monitor feature. These options take effect whatever the value of the <code>core.fsmonitor</code> configuration variable (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)). But a warning is emitted when the change goes against the configured value, as the configured value will take effect next time the index is read and this will remove the intended effect of the option.</dl>
<p> &#8212;</p>
<dl>
<dt>
<dd> Do not interpret any more arguments as options.</dl>
<p> &lt;file&gt;</p>
<dl>
<dt>
<dd> Files to act on. Note that files beginning with <i>.</i> are discarded. This includes <code>./file</code> and <code>dir/./file</code>. If you don&#8217;t want this, then use cleaner names. The same applies to directories ending <i>/</i> and paths with <i>//</i></dl>
<h2>USING &#8211;REFRESH</h2>
<p> <code>&#8211;refresh</code> does not calculate a new sha1 file or bring the index up to date for mode/content changes. But what it <code>does</code> do is to &quot;re-match&quot; the stat information of a file with the index, so that you can refresh the index for a file that hasn&#8217;t been changed but where the stat entry is out of date. </p>
<p> For example, you&#8217;d want to do this after doing a <i>git read-tree</i>, to link up the stat index details with the proper files.</p>
<h2>USING &#8211;CACHEINFO OR &#8211;INFO-ONLY</h2>
<p> <code>&#8211;cacheinfo</code> is used to register a file that is not in the current working directory. This is useful for minimum-checkout merging. </p>
<p> To pretend you have a file at path with mode and sha1, say: </p>
<dl>
<dt>
<dd>
<pre>
$ git update-index --add --cacheinfo &lt;mode&gt;,&lt;sha1&gt;,&lt;path&gt;
</pre>
</dl>
<p> <code>&#8211;info-only</code> is used to register files without placing them in the object database. This is useful for status-only repositories. </p>
<p> Both <code>&#8211;cacheinfo</code> and <code>&#8211;info-only</code> behave similarly: the index is updated but the object database isn&#8217;t. <code>&#8211;cacheinfo</code> is useful when the object is in the database but the file isn&#8217;t available locally. <code>&#8211;info-only</code> is useful when the file is available, but you do not wish to update the object database.</p>
<h2>USING &#8211;INDEX-INFO</h2>
<p> <code>&#8211;index-info</code> is a more powerful mechanism that lets you feed multiple entry definitions from the standard input, and designed specifically for scripts. It can take inputs of three formats: </p>
<dl>
<dt>
<dd> 1. mode SP type SP sha1 TAB path </p>
<p> This format is to stuff <code>git ls-tree</code> output into the index.</dl>
<dl>
<dt>
<dd> 2. mode SP sha1 SP stage TAB path </p>
<p> This format is to put higher order stages into the index file and matches <i>git ls-files &#8211;stage</i> output.</dl>
<dl>
<dt>
<dd> 3. mode SP sha1 TAB path </p>
<p> This format is no longer produced by any Git command, but is and will continue to be supported by <code>update-index &#8211;index-info</code>.</dl>
<p> To place a higher stage entry to the index, the path should first be removed by feeding a mode=0 entry for the path, and then feeding necessary input lines in the third format. </p>
<p> For example, starting with this index: </p>
<dl>
<dt>
<dd>
<pre>
$ git ls-files -s
100644 8a1218a1024a212bb3db30becd860315f9f3ac52 0       frotz
</pre>
</dl>
<p> you can feed the following input to <code>&#8211;index-info</code>: </p>
<dl>
<dt>
<dd>
<pre>
$ git update-index --index-info
0 0000000000000000000000000000000000000000      frotz
100644 8a1218a1024a212bb3db30becd860315f9f3ac52 1       frotz
100755 8a1218a1024a212bb3db30becd860315f9f3ac52 2       frotz
</pre>
</dl>
<p> The first line of the input feeds 0 as the mode to remove the path; the SHA-1 does not matter as long as it is well formatted. Then the second and third line feeds stage 1 and stage 2 entries for that path. After the above, we would end up with this: </p>
<dl>
<dt>
<dd>
<pre>
$ git ls-files -s
100644 8a1218a1024a212bb3db30becd860315f9f3ac52 1       frotz
100755 8a1218a1024a212bb3db30becd860315f9f3ac52 2       frotz
</pre>
</dl>
<h2>USING &#8220;ASSUME UNCHANGED&#8221; BIT</h2>
<p> Many operations in Git depend on your filesystem to have an efficient <code><a href="/docs/linux/man/2-lstat/">lstat</a>(2)</code> implementation, so that <code>st_mtime</code> information for working tree files can be cheaply checked to see if the file contents have changed from the version recorded in the index file. Unfortunately, some filesystems have inefficient <code><a href="/docs/linux/man/2-lstat/">lstat</a>(2)</code>. If your filesystem is one of them, you can set &quot;assume unchanged&quot; bit to paths you have not changed to cause Git not to do this check. Note that setting this bit on a path does not mean Git will check the contents of the file to see if it has changed &#8212; it makes Git to omit any checking and assume it has <code>not</code> changed. When you make changes to working tree files, you have to explicitly tell Git about it by dropping &quot;assume unchanged&quot; bit, either before or after you modify them. </p>
<p> In order to set &quot;assume unchanged&quot; bit, use <code>&#8211;assume-unchanged</code> option. To unset, use <code>&#8211;no-assume-unchanged</code>. To see which files have the &quot;assume unchanged&quot; bit set, use <code>git ls-files -v</code> (see <code><a href="/docs/linux/man/1-git-ls-files/">git-ls-files</a></code>(1)). </p>
<p> The command looks at <code>core.ignorestat</code> configuration variable. When this is true, paths updated with <code>git update-index paths&#8230;</code> and paths updated with other Git commands that update both index and working tree (e.g. <i>git apply &#8211;index</i>, <i>git checkout-index -u</i>, and <i>git read-tree -u</i>) are automatically marked as &quot;assume unchanged&quot;. Note that &quot;assume unchanged&quot; bit is <code>not</code> set if <code>git update-index &#8211;refresh</code> finds the working tree file matches the index (use <code>git update-index &#8211;really-refresh</code> if you want to mark them as &quot;assume unchanged&quot;).</p>
<h2>EXAMPLES</h2>
<p> To update and refresh only the files already checked out: </p>
<dl>
<dt>
<dd>
<pre>
$ git checkout-index -n -f -a &amp;&amp; git update-index --ignore-missing --refresh
</pre>
</dl>
<p> On an inefficient filesystem with <code>core.ignorestat</code> set</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre><code>
$ git update - index-- really - refresh(1) $ git update - index-- no - assume - unchanged foo.c(2) $ git diff-- name - only(3) $ edit foo.c $ git diff-- name - only(4) M foo.c $ git update - index foo.c(5) $ git diff-- name - only(6) $ edit foo.c $ git diff-- name - only(7) $ git update - index-- no - assume - unchanged foo.c(8) $ git diff-- name - only(9) M foo.c
</code></pre>
</dl>
<p> <code>1. </code>forces <a href="/docs/linux/man/2-lstat/">lstat</a>(2) to set &quot;assume unchanged&quot; bits for paths that match index.<br />
 <code>2. </code>mark the path to be edited.<br />
 <code>3. </code>this does <a href="/docs/linux/man/2-lstat/">lstat</a>(2) and finds index matches the path.<br />
 <code>4. </code>this does <a href="/docs/linux/man/2-lstat/">lstat</a>(2) and finds index does <code>not</code> match the path.<br />
 <code>5. </code>registering the new version to index sets &quot;assume unchanged&quot; bit.<br />
 <code>6. </code>and it is assumed unchanged.<br />
 <code>7. </code>even after you edit it.<br />
 <code>8. </code>you can tell about the change after the fact.<br />
 <code>9. </code>now it checks with <a href="/docs/linux/man/2-lstat/">lstat</a>(2) and finds it has been changed.
</dl>
<h2>SKIP-WORKTREE BIT</h2>
<p> Skip-worktree bit can be defined in one (long) sentence: When reading an entry, if it is marked as skip-worktree, then Git pretends its working directory version is up to date and read the index version instead. </p>
<p> To elaborate, &quot;reading&quot; means checking for file existence, reading file attributes or file content. The working directory version may be present or absent. If present, its content may match against the index version or not. Writing is not affected by this bit, content safety is still first priority. Note that Git <i>can</i> update working directory file, that is marked skip-worktree, if it is safe to do so (i.e. working directory version matches index version) </p>
<p> Although this bit looks similar to assume-unchanged bit, its goal is different from assume-unchanged bit&#8217;s. Skip-worktree also takes precedence over assume-unchanged bit when both are set.</p>
<h2>SPLIT INDEX</h2>
<p> This mode is designed for repositories with very large indexes, and aims at reducing the time it takes to repeatedly write these indexes. </p>
<p> In this mode, the index is split into two files, $GIT_DIR/index and $GIT_DIR/sharedindex.&lt;SHA-1&gt;. Changes are accumulated in $GIT_DIR/index, the split index, while the shared index file contains all index entries and stays unchanged. </p>
<p> All changes in the split index are pushed back to the shared index file when the number of entries in the split index reaches a level specified by the splitIndex.maxPercentChange config variable (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)). </p>
<p> Each time a new shared index file is created, the old shared index files are deleted if their modification time is older than what is specified by the splitIndex.sharedIndexExpire config variable (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)). </p>
<p> To avoid deleting a shared index file that is still used, its modification time is updated to the current time every time a new split index based on the shared index file is either created or read from.</p>
<h2>UNTRACKED CACHE</h2>
<p> This cache is meant to speed up commands that involve determining untracked files such as <code>git status</code>. </p>
<p> This feature works by recording the mtime of the working tree directories and then omitting reading directories and stat calls against files in those directories whose mtime hasn&#8217;t changed. For this to work the underlying operating system and file system must change the <code>st_mtime</code> field of directories if files in the directory are added, modified or deleted. </p>
<p> You can test whether the filesystem supports that with the <code>&#8211;test-untracked-cache</code> option. The <code>&#8211;untracked-cache</code> option used to implicitly perform that test in older versions of Git, but that&#8217;s no longer the case. </p>
<p> If you want to enable (or disable) this feature, it is easier to use the <code>core.untrackedCache</code> configuration variable (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)) than using the <code>&#8211;untracked-cache</code> option to <code>git update-index</code> in each repository, especially if you want to do so across all repositories you use, because you can set the configuration variable to <code>true</code> (or <code>false</code>) in your <code>$HOME/.gitconfig</code> just once and have it affect all repositories you touch. </p>
<p> When the <code>core.untrackedCache</code> configuration variable is changed, the untracked cache is added to or removed from the index the next time a command reads the index; while when <code>&#8211;[no-|force-]untracked-cache</code> are used, the untracked cache is immediately added to or removed from the index. </p>
<p> Before 2.17, the untracked cache had a bug where replacing a directory with a symlink to another directory could cause it to incorrectly show files tracked by git as untracked. See the &quot;status: add a failing test showing a core.untrackedCache bug&quot; commit to git.git. A workaround for that is (and this might work for other undiscovered bugs in the future): </p>
<dl>
<dt>
<dd>
<pre>
$ git -c core.untrackedCache=false status
</pre>
</dl>
<p> This bug has also been shown to affect non-symlink cases of replacing a directory with a file when it comes to the internal structures of the untracked cache, but no case has been reported where this resulted in wrong &quot;git status&quot; output. </p>
<p> There are also cases where existing indexes written by git versions before 2.17 will reference directories that don&#8217;t exist anymore, potentially causing many &quot;could not open directory&quot; warnings to be printed on &quot;git status&quot;. These are new warnings for existing issues that were previously silently discarded. </p>
<p> As with the bug described above the solution is to one-off do a &quot;git status&quot; run with <code>core.untrackedCache=false</code> to flush out the leftover bad data.</p>
<h2>FILE SYSTEM MONITOR</h2>
<p> This feature is intended to speed up git operations for repos that have large working directories. </p>
<p> It enables git to work together with a file system monitor (see the &quot;fsmonitor-watchman&quot; section of <code><a href="/docs/linux/man/5-githooks/">githooks</a></code>(5)) that can inform it as to what files have been modified. This enables git to avoid having to lstat() every file to find modified files. </p>
<p> When used in conjunction with the untracked cache, it can further improve performance by avoiding the cost of scanning the entire working directory looking for new files. </p>
<p> If you want to enable (or disable) this feature, it is easier to use the <code>core.fsmonitor</code> configuration variable (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)) than using the <code>&#8211;fsmonitor</code> option to <code>git update-index</code> in each repository, especially if you want to do so across all repositories you use, because you can set the configuration variable in your <code>$HOME/.gitconfig</code> just once and have it affect all repositories you touch. </p>
<p> When the <code>core.fsmonitor</code> configuration variable is changed, the file system monitor is added to or removed from the index the next time a command reads the index. When <code>&#8211;[no-]fsmonitor</code> are used, the file system monitor is immediately added to or removed from the index.</p>
<h2>CONFIGURATION</h2>
<p> The command honors <code>core.filemode</code> configuration variable. If your repository is on a filesystem whose executable bits are unreliable, this should be set to <i>false</i> (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)). This causes the command to ignore differences in file modes recorded in the index and the file mode on the filesystem if they differ only on executable bit. On such an unfortunate filesystem, you may need to use <i>git update-index &#8211;chmod=</i>. </p>
<p> Quite similarly, if <code>core.symlinks</code> configuration variable is set to <i>false</i> (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)), symbolic links are checked out as plain files, and this command does not modify a recorded file mode from symbolic link to regular file. </p>
<p> The command looks at <code>core.ignorestat</code> configuration variable. See <i>Using &quot;assume unchanged&quot; bit</i> section above. </p>
<p> The command also looks at <code>core.trustctime</code> configuration variable. It can be useful when the inode change time is regularly modified by something outside Git (file system crawlers and backup systems use ctime for marking files processed) (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)). </p>
<p> The untracked cache extension can be enabled by the <code>core.untrackedCache</code> configuration variable (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)).</p>
<h2>NOTES</h2>
<p> Users often try to use the assume-unchanged and skip-worktree bits to tell Git to ignore changes to files that are tracked. This does not work as expected, since Git may still check working tree files against the index when performing certain operations. In general, Git does not provide a way to ignore changes to tracked files, so alternate solutions are recommended. </p>
<p> For example, if the file you want to change is some sort of config file, the repository can include a sample config file that can then be copied into the ignored name and modified. The repository can even include a script to treat the sample file as a template, modifying and copying it automatically.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1), <code><a href="/docs/linux/man/1-git-add/">git-add</a></code>(1), <code><a href="/docs/linux/man/1-git-ls-files/">git-ls-files</a></code>(1)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>

---
title: "git-rm(1)"
name: "git-rm"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-rm/"
description: "git-rm – Remove files from the working tree and from the index"
---

<h2 class="name">NAME</h2>
<p> git-rm &#8211; Remove files from the working tree and from the index </p>
<h2>SYNOPSIS</h2>
<pre><code>
git rm[-f | --force][-n][-r][--cached][--ignore - unmatch]
      [--quiet][--pathspec - from - file = &lt;file&gt;[--pathspec - file - nul]]
      [--][&lt;pathspec&gt;...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Remove files matching pathspec from the index, or from the working tree and the index. <code>git rm</code> will not remove a file from just your working directory. (There is no option to remove a file only from the working tree and yet keep it in the index; use <code>/bin/rm</code> if you want to do that.) The files being removed have to be identical to the tip of the branch, and no updates to their contents can be staged in the index, though that default behavior can be overridden with the <code>-f</code> option. When <code>&#8211;cached</code> is given, the staged content has to match either the tip of the branch or the file on disk, allowing the file to be removed from just the index. When sparse-checkouts are in use (see <code><a href="/docs/linux/man/1-git-sparse-checkout/">git-sparse-checkout</a></code>(1)), <code>git rm</code> will only remove paths within the sparse-checkout patterns.</p>
<h2>OPTIONS</h2>
<p> &lt;pathspec&gt;&#8230;</p>
<dl>
<dt>
<dd> Files to remove. A leading directory name (e.g. <code>dir</code> to remove <code>dir/file1</code> and <code>dir/file2</code>) can be given to remove all files in the directory, and recursively all sub-directories, but this requires the <code>-r</code> option to be explicitly given. </p>
<p> The command removes only the paths that are known to Git. </p>
<p> File globbing matches across directory boundaries. Thus, given two directories <code>d</code> and <code>d2</code>, there is a difference between using <code>git rm &#8216;d*&#8217;</code> and <code>git rm &#8216;d/*&#8217;</code>, as the former will also remove all of directory <code>d2</code>. </p>
<p> For more details, see the <i>pathspec</i> entry in <code><a href="/docs/linux/man/7-gitglossary/">gitglossary</a></code>(7).</dl>
<p> -f, &#8211;force</p>
<dl>
<dt>
<dd> Override the up-to-date check.</dl>
<p> -n, &#8211;dry-run</p>
<dl>
<dt>
<dd> Don&#8217;t actually remove any file(s). Instead, just show if they exist in the index and would otherwise be removed by the command.</dl>
<p> -r</p>
<dl>
<dt>
<dd> Allow recursive removal when a leading directory name is given.</dl>
<p> &#8212;</p>
<dl>
<dt>
<dd> This option can be used to separate command-line options from the list of files, (useful when filenames might be mistaken for command-line options).</dl>
<p> &#8211;cached</p>
<dl>
<dt>
<dd> Use this option to unstage and remove paths only from the index. Working tree files, whether modified or not, will be left alone.</dl>
<p> &#8211;ignore-unmatch</p>
<dl>
<dt>
<dd> Exit with a zero status even if no files matched.</dl>
<p> &#8211;sparse</p>
<dl>
<dt>
<dd> Allow updating index entries outside of the sparse-checkout cone. Normally, <code>git rm</code> refuses to update index entries whose paths do not fit within the sparse-checkout cone. See <code><a href="/docs/linux/man/1-git-sparse-checkout/">git-sparse-checkout</a></code>(1) for more.</dl>
<p> -q, &#8211;quiet</p>
<dl>
<dt>
<dd> <code>git rm</code> normally outputs one line (in the form of an <code>rm</code> command) for each file removed. This option suppresses that output.</dl>
<p> &#8211;pathspec-from-file=&lt;file&gt;</p>
<dl>
<dt>
<dd> Pathspec is passed in <code>&lt;file&gt;</code> instead of commandline args. If <code>&lt;file&gt;</code> is exactly <code>&#8211;</code> then standard input is used. Pathspec elements are separated by LF or CR/LF. Pathspec elements can be quoted as explained for the configuration variable <code>core.quotePath</code> (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)). See also <code>&#8211;pathspec-file-nul</code> and global <code>&#8211;literal-pathspecs</code>.</dl>
<p> &#8211;pathspec-file-nul</p>
<dl>
<dt>
<dd> Only meaningful with <code>&#8211;pathspec-from-file</code>. Pathspec elements are separated with NUL character and all other characters are taken literally (including newlines and quotes).</dl>
<h2>REMOVING FILES THAT HAVE DISAPPEARED FROM THE FILESYSTEM</h2>
<p> There is no option for <code>git rm</code> to remove from the index only the paths that have disappeared from the filesystem. However, depending on the use case, there are several ways that can be done.</p>
<h3>Using &#8220;git commit -a&#8221;</h3>
<p> If you intend that your next commit should record all modifications of tracked files in the working tree and record all removals of files that have been removed from the working tree with <code>rm</code> (as opposed to <code>git rm</code>), use <code>git commit -a</code>, as it will automatically notice and record all removals. You can also have a similar effect without committing by using <code>git add -u</code>.</p>
<h3>Using &#8220;git add -A&#8221;</h3>
<p> When accepting a new code drop for a vendor branch, you probably want to record both the removal of paths and additions of new paths as well as modifications of existing paths. </p>
<p> Typically you would first remove all tracked files from the working tree using this command: </p>
<dl>
<dt>
<dd>
<pre>
git ls-files -z | xargs -0 rm -f
</pre>
</dl>
<p> and then untar the new code in the working tree. Alternately you could <i>rsync</i> the changes into the working tree. </p>
<p> After that, the easiest way to record all removals, additions, and modifications in the working tree is: </p>
<dl>
<dt>
<dd>
<pre>
git add -A
</pre>
</dl>
<p> See <code><a href="/docs/linux/man/1-git-add/">git-add</a></code>(1).</p>
<h3>Other ways</h3>
<p> If all you really want to do is to remove from the index the files that are no longer present in the working tree (perhaps because your working tree is dirty so that you cannot use <code>git commit -a</code>), use the following command: </p>
<dl>
<dt>
<dd>
<pre>
git diff --name-only --diff-filter=D -z | xargs -0 git rm --cached
</pre>
</dl>
<h2>SUBMODULES</h2>
<p> Only submodules using a gitfile (which means they were cloned with a Git version 1.7.8 or newer) will be removed from the work tree, as their repository lives inside the .git directory of the superproject. If a submodule (or one of those nested inside it) still uses a .git directory, <code>git rm</code> will move the submodules git directory into the superprojects git directory to protect the submodule&#8217;s history. If it exists the submodule.&lt;name&gt; section in the <code><a href="/docs/linux/man/5-gitmodules/">gitmodules</a></code>(5) file will also be removed and that file will be staged (unless &#8211;cached or -n are used). </p>
<p> A submodule is considered up to date when the HEAD is the same as recorded in the index, no tracked files are modified and no untracked files that aren&#8217;t ignored are present in the submodules work tree. Ignored files are deemed expendable and won&#8217;t stop a submodule&#8217;s work tree from being removed. </p>
<p> If you only want to remove the local checkout of a submodule from your work tree without committing the removal, use <code><a href="/docs/linux/man/1-git-submodule/">git-submodule</a></code>(1) <code>deinit</code> instead. Also see <code><a href="/docs/linux/man/7-gitsubmodules/">gitsubmodules</a></code>(7) for details on submodule removal.</p>
<h2>EXAMPLES</h2>
<p> <code>git rm Documentation/\*.txt</code></p>
<dl>
<dt>
<dd> Removes all <code>*.txt</code> files from the index that are under the <code>Documentation</code> directory and any of its subdirectories. </p>
<p> Note that the asterisk <code>*</code> is quoted from the shell in this example; this lets Git, and not the shell, expand the pathnames of files and subdirectories under the <code>Documentation/</code> directory.</dl>
<p> <code>git rm -f git-*.sh</code></p>
<dl>
<dt>
<dd> Because this example lets the shell expand the asterisk (i.e. you are listing the files explicitly), it does not remove <code>subdir/git-foo.sh</code>.</dl>
<h2>BUGS</h2>
<p> Each time a superproject update removes a populated submodule (e.g. when switching between commits before and after the removal) a stale submodule checkout will remain in the old location. Removing the old directory is only safe when it uses a gitfile, as otherwise the history of the submodule will be deleted too. This step will be obsolete when recursive submodule update has been implemented.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-add/">git-add</a></code>(1)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>

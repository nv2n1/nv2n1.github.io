---
title: "git-add(1)"
name: "git-add"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-add/"
description: "git-add – Add file contents to the index"
---

<h2 class="name">NAME</h2>
<p> git-add &#8211; Add file contents to the index </p>
<h2>SYNOPSIS</h2>
<pre><code>
git add[--verbose | -v][--dry - run | -n][--force | -f][--interactive | -i][--patch | -p]
       [--edit | -e][--[no - ] all | --[no - ] ignore - removal | [--update | -u]][--sparse]
       [--intent - to - add | -N][--refresh][--ignore - errors][--ignore - missing][--renormalize]
       [--chmod = (+ | -) x][--pathspec - from - file = &lt;file&gt;[--pathspec - file - nul]]
       [--][&lt;pathspec&gt;...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> This command updates the index using the current content found in the working tree, to prepare the content staged for the next commit. It typically adds the current content of existing paths as a whole, but with some options it can also be used to add content with only part of the changes made to the working tree files applied, or remove paths that do not exist in the working tree anymore. </p>
<p> The &quot;index&quot; holds a snapshot of the content of the working tree, and it is this snapshot that is taken as the contents of the next commit. Thus after making any changes to the working tree, and before running the commit command, you must use the <code>add</code> command to add any new or modified files to the index. </p>
<p> This command can be performed multiple times before a commit. It only adds the content of the specified file(s) at the time the add command is run; if you want subsequent changes included in the next commit, then you must run <code>git add</code> again to add the new content to the index. </p>
<p> The <code>git status</code> command can be used to obtain a summary of which files have changes that are staged for the next commit. </p>
<p> The <code>git add</code> command will not add ignored files by default. If any ignored files were explicitly specified on the command line, <code>git add</code> will fail with a list of ignored files. Ignored files reached by directory recursion or filename globbing performed by Git (quote your globs before the shell) will be silently ignored. The <i>git add</i> command can be used to add ignored files with the <code>-f</code> (force) option. </p>
<p> Please see <code><a href="/docs/linux/man/1-git-commit/">git-commit</a></code>(1) for alternative ways to add content to a commit.</p>
<h2>OPTIONS</h2>
<p> &lt;pathspec&gt;&#8230;</p>
<dl>
<dt>
<dd> Files to add content from. Fileglobs (e.g. <code>*.c</code>) can be given to add all matching files. Also a leading directory name (e.g. <code>dir</code> to add <code>dir/file1</code> and <code>dir/file2</code>) can be given to update the index to match the current state of the directory as a whole (e.g. specifying <code>dir</code> will record not just a file <code>dir/file1</code> modified in the working tree, a file <code>dir/file2</code> added to the working tree, but also a file <code>dir/file3</code> removed from the working tree). Note that older versions of Git used to ignore removed files; use <code>&#8211;no-all</code> option if you want to add modified or new files but ignore removed ones. </p>
<p> For more details about the &lt;pathspec&gt; syntax, see the <i>pathspec</i> entry in <code><a href="/docs/linux/man/7-gitglossary/">gitglossary</a></code>(7).</dl>
<p> -n, &#8211;dry-run</p>
<dl>
<dt>
<dd> Don&#8217;t actually add the file(s), just show if they exist and/or will be ignored.</dl>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
<dd> Be verbose.</dl>
<p> -f, &#8211;force</p>
<dl>
<dt>
<dd> Allow adding otherwise ignored files.</dl>
<p> &#8211;sparse</p>
<dl>
<dt>
<dd> Allow updating index entries outside of the sparse-checkout cone. Normally, <code>git add</code> refuses to update index entries whose paths do not fit within the sparse-checkout cone, since those files might be removed from the working tree without warning. See <code><a href="/docs/linux/man/1-git-sparse-checkout/">git-sparse-checkout</a></code>(1) for more details.</dl>
<p> -i, &#8211;interactive</p>
<dl>
<dt>
<dd> Add modified contents in the working tree interactively to the index. Optional path arguments may be supplied to limit operation to a subset of the working tree. See &#8220;Interactive mode&#8221; for details.</dl>
<p> -p, &#8211;patch</p>
<dl>
<dt>
<dd> Interactively choose hunks of patch between the index and the work tree and add them to the index. This gives the user a chance to review the difference before adding modified contents to the index. </p>
<p> This effectively runs <code>add &#8211;interactive</code>, but bypasses the initial command menu and directly jumps to the <code>patch</code> subcommand. See &#8220;Interactive mode&#8221; for details.</dl>
<p> -e, &#8211;edit</p>
<dl>
<dt>
<dd> Open the diff vs. the index in an editor and let the user edit it. After the editor was closed, adjust the hunk headers and apply the patch to the index. </p>
<p> The intent of this option is to pick and choose lines of the patch to apply, or even to modify the contents of lines to be staged. This can be quicker and more flexible than using the interactive hunk selector. However, it is easy to confuse oneself and create a patch that does not apply to the index. See EDITING PATCHES below.</dl>
<p> -u, &#8211;update</p>
<dl>
<dt>
<dd> Update the index just where it already has an entry matching &lt;pathspec&gt;. This removes as well as modifies index entries to match the working tree, but adds no new files. </p>
<p> If no &lt;pathspec&gt; is given when <code>-u</code> option is used, all tracked files in the entire working tree are updated (old versions of Git used to limit the update to the current directory and its subdirectories).</dl>
<p> -A, &#8211;all, &#8211;no-ignore-removal</p>
<dl>
<dt>
<dd> Update the index not only where the working tree has a file matching &lt;pathspec&gt; but also where the index already has an entry. This adds, modifies, and removes index entries to match the working tree. </p>
<p> If no &lt;pathspec&gt; is given when <code>-A</code> option is used, all files in the entire working tree are updated (old versions of Git used to limit the update to the current directory and its subdirectories).</dl>
<p> &#8211;no-all, &#8211;ignore-removal</p>
<dl>
<dt>
<dd> Update the index by adding new files that are unknown to the index and files modified in the working tree, but ignore files that have been removed from the working tree. This option is a no-op when no &lt;pathspec&gt; is used. </p>
<p> This option is primarily to help users who are used to older versions of Git, whose &quot;git add &lt;pathspec&gt;&#8230;&quot; was a synonym for &quot;git add &#8211;no-all &lt;pathspec&gt;&#8230;&quot;, i.e. ignored removed files.</dl>
<p> -N, &#8211;intent-to-add</p>
<dl>
<dt>
<dd> Record only the fact that the path will be added later. An entry for the path is placed in the index with no content. This is useful for, among other things, showing the unstaged content of such files with <code>git diff</code> and committing them with <code>git commit -a</code>.</dl>
<p> &#8211;refresh</p>
<dl>
<dt>
<dd> Don&#8217;t add the file(s), but only refresh their stat() information in the index.</dl>
<p> &#8211;ignore-errors</p>
<dl>
<dt>
<dd> If some files could not be added because of errors indexing them, do not abort the operation, but continue adding the others. The command shall still exit with non-zero status. The configuration variable <code>add.ignoreErrors</code> can be set to true to make this the default behaviour.</dl>
<p> &#8211;ignore-missing</p>
<dl>
<dt>
<dd> This option can only be used together with &#8211;dry-run. By using this option the user can check if any of the given files would be ignored, no matter if they are already present in the work tree or not.</dl>
<p> &#8211;no-warn-embedded-repo</p>
<dl>
<dt>
<dd> By default, <code>git add</code> will warn when adding an embedded repository to the index without using <code>git submodule add</code> to create an entry in <code>.gitmodules</code>. This option will suppress the warning (e.g., if you are manually performing operations on submodules).</dl>
<p> &#8211;renormalize</p>
<dl>
<dt>
<dd> Apply the &quot;clean&quot; process freshly to all tracked files to forcibly add them again to the index. This is useful after changing <code>core.autocrlf</code> configuration or the <code>text</code> attribute in order to correct files added with wrong CRLF/LF line endings. This option implies <code>-u</code>.</dl>
<p> &#8211;chmod=(+|-)x</p>
<dl>
<dt>
<dd> Override the executable bit of the added files. The executable bit is only changed in the index, the files on disk are left unchanged.</dl>
<p> &#8211;pathspec-from-file=&lt;file&gt;</p>
<dl>
<dt>
<dd> Pathspec is passed in <code>&lt;file&gt;</code> instead of commandline args. If <code>&lt;file&gt;</code> is exactly <code>&#8211;</code> then standard input is used. Pathspec elements are separated by LF or CR/LF. Pathspec elements can be quoted as explained for the configuration variable <code>core.quotePath</code> (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)). See also <code>&#8211;pathspec-file-nul</code> and global <code>&#8211;literal-pathspecs</code>.</dl>
<p> &#8211;pathspec-file-nul</p>
<dl>
<dt>
<dd> Only meaningful with <code>&#8211;pathspec-from-file</code>. Pathspec elements are separated with NUL character and all other characters are taken literally (including newlines and quotes).</dl>
<p> &#8212;</p>
<dl>
<dt>
<dd> This option can be used to separate command-line options from the list of files, (useful when filenames might be mistaken for command-line options).</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd> &bull; Adds content from all <code>*.txt</code> files under <code>Documentation</code> directory and its subdirectories: </p>
<dl>
<dt>
<dd>
<pre>
$ git add Documentation/\*.txt
</pre>
</dl>
<p> Note that the asterisk <code>*</code> is quoted from the shell in this example; this lets the command include the files from subdirectories of <code>Documentation/</code> directory.</dl>
<dl>
<dt>
<dd> &bull; Considers adding content from all git-*.sh scripts: </p>
<dl>
<dt>
<dd>
<pre>
$ git add git-*.sh
</pre>
</dl>
<p> Because this example lets the shell expand the asterisk (i.e. you are listing the files explicitly), it does not consider <code>subdir/git-foo.sh</code>.</dl>
<h2>INTERACTIVE MODE</h2>
<p> When the command enters the interactive mode, it shows the output of the <i>status</i> subcommand, and then goes into its interactive command loop. </p>
<p> The command loop shows the list of subcommands available, and gives a prompt &quot;What now&gt; &quot;. In general, when the prompt ends with a single <i>&gt;</i>, you can pick only one of the choices given and type return, like this: </p>
<dl>
<dt>
<dd>
<pre>
    *** Commands ***
      1: status       2: update       3: revert       4: add untracked
      5: patch        6: diff         7: quit         8: help
    What now&gt; 1
</pre>
</dl>
<p> You also could say <code>s</code> or <code>sta</code> or <code>status</code> above as long as the choice is unique. </p>
<p> The main command loop has 6 subcommands (plus help and quit). </p>
<p> status</p>
<dl>
<dt>
<dd> This shows the change between HEAD and index (i.e. what will be committed if you say <code>git commit</code>), and between index and working tree files (i.e. what you could stage further before <code>git commit</code> using <code>git add</code>) for each path. A sample output looks like this: </p>
<dl>
<dt>
<dd>
<pre>
              staged     unstaged path
     1:       binary      nothing foo.png
     2:     +403/-35        +1/-1 git-add--interactive.perl
</pre>
</dl>
<p> It shows that foo.png has differences from HEAD (but that is binary so line count cannot be shown) and there is no difference between indexed copy and the working tree version (if the working tree version were also different, <i>binary</i> would have been shown in place of <i>nothing</i>). The other file, git-add&#8211;interactive.perl, has 403 lines added and 35 lines deleted if you commit what is in the index, but working tree file has further modifications (one addition and one deletion).</dl>
<p> update</p>
<dl>
<dt>
<dd> This shows the status information and issues an &quot;Update&gt;&gt;&quot; prompt. When the prompt ends with double <i>&gt;&gt;</i>, you can make more than one selection, concatenated with whitespace or comma. Also you can say ranges. E.g. &quot;2-5 7,9&quot; to choose 2,3,4,5,7,9 from the list. If the second number in a range is omitted, all remaining patches are taken. E.g. &quot;7-&quot; to choose 7,8,9 from the list. You can say <i>*</i> to choose everything. </p>
<p> What you chose are then highlighted with <i>*</i>, like this: </p>
<dl>
<dt>
<dd>
<pre>
           staged     unstaged path
  1:       binary      nothing foo.png
* 2:     +403/-35        +1/-1 git-add--interactive.perl
</pre>
</dl>
<p> To remove selection, prefix the input with <code>&#8211;</code> like this: </p>
<dl>
<dt>
<dd>
<pre>
Update&gt;&gt; -2
</pre>
</dl>
<p> After making the selection, answer with an empty line to stage the contents of working tree files for selected paths in the index.</dl>
<p> revert</p>
<dl>
<dt>
<dd> This has a very similar UI to <i>update</i>, and the staged information for selected paths are reverted to that of the HEAD version. Reverting new paths makes them untracked.</dl>
<p> add untracked</p>
<dl>
<dt>
<dd> This has a very similar UI to <i>update</i> and <i>revert</i>, and lets you add untracked paths to the index.</dl>
<p> patch</p>
<dl>
<dt>
<dd> This lets you choose one path out of a <i>status</i> like selection. After choosing the path, it presents the diff between the index and the working tree file and asks you if you want to stage the change of each hunk. You can select one of the following options and type return: </p>
<dl>
<dt>
<dd>
<pre>
y - stage this hunk
n - do not stage this hunk
q - quit; do not stage this hunk or any of the remaining ones
a - stage this hunk and all later hunks in the file
d - do not stage this hunk or any of the later hunks in the file
g - select a hunk to go to
/ - search for a hunk matching the given regex
j - leave this hunk undecided, see next undecided hunk
J - leave this hunk undecided, see next hunk
k - leave this hunk undecided, see previous undecided hunk
K - leave this hunk undecided, see previous hunk
s - split the current hunk into smaller hunks
e - manually edit the current hunk
? - print help
</pre>
</dl>
<p> After deciding the fate for all hunks, if there is any hunk that was chosen, the index is updated with the selected hunks. </p>
<p> You can omit having to type return here, by setting the configuration variable <code>interactive.singleKey</code> to <code>true</code>.</dl>
<p> diff</p>
<dl>
<dt>
<dd> This lets you review what will be committed (i.e. between HEAD and index).</dl>
<h2>EDITING PATCHES</h2>
<p> Invoking <code>git add -e</code> or selecting <code>e</code> from the interactive hunk selector will open a patch in your editor; after the editor exits, the result is applied to the index. You are free to make arbitrary changes to the patch, but note that some changes may have confusing results, or even result in a patch that cannot be applied. If you want to abort the operation entirely (i.e., stage nothing new in the index), simply delete all lines of the patch. The list below describes some common things you may see in a patch, and which editing operations make sense on them. </p>
<p> added content</p>
<dl>
<dt>
<dd> Added content is represented by lines beginning with &quot;+&quot;. You can prevent staging any addition lines by deleting them.</dl>
<p> removed content</p>
<dl>
<dt>
<dd> Removed content is represented by lines beginning with &quot;-&quot;. You can prevent staging their removal by converting the &quot;-&quot; to a &quot; &quot; (space).</dl>
<p> modified content</p>
<dl>
<dt>
<dd> Modified content is represented by &quot;-&quot; lines (removing the old content) followed by &quot;+&quot; lines (adding the replacement content). You can prevent staging the modification by converting &quot;-&quot; lines to &quot; &quot;, and removing &quot;+&quot; lines. Beware that modifying only half of the pair is likely to introduce confusing changes to the index.</dl>
<p> There are also more complex operations that can be performed. But beware that because the patch is applied only to the index and not the working tree, the working tree will appear to &quot;undo&quot; the change in the index. For example, introducing a new line into the index that is in neither the HEAD nor the working tree will stage the new line for commit, but the line will appear to be reverted in the working tree. </p>
<p> Avoid using these constructs, or do so with extreme caution. </p>
<p> removing untouched content</p>
<dl>
<dt>
<dd> Content which does not differ between the index and working tree may be shown on context lines, beginning with a &quot; &quot; (space). You can stage context lines for removal by converting the space to a &quot;-&quot;. The resulting working tree file will appear to re-add the content.</dl>
<p> modifying existing content</p>
<dl>
<dt>
<dd> One can also modify context lines by staging them for removal (by converting &quot; &quot; to &quot;-&quot;) and adding a &quot;+&quot; line with the new content. Similarly, one can modify &quot;+&quot; lines for existing additions or modifications. In all cases, the new modification will appear reverted in the working tree.</dl>
<p> new content</p>
<dl>
<dt>
<dd> You may also add new content that does not exist in the patch; simply add new lines, each starting with &quot;+&quot;. The addition will appear reverted in the working tree.</dl>
<p> There are also several operations which should be avoided entirely, as they will make the patch impossible to apply: </p>
<dl>
<dt>
<dd> &bull; adding context (&quot; &quot;) or removal (&quot;-&quot;) lines</dl>
<dl>
<dt>
<dd> &bull; deleting context or removal lines</dl>
<dl>
<dt>
<dd> &bull; modifying the contents of context or removal lines</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-status/">git-status</a></code>(1) <code><a href="/docs/linux/man/1-git-rm/">git-rm</a></code>(1) <code><a href="/docs/linux/man/1-git-reset/">git-reset</a></code>(1) <code><a href="/docs/linux/man/1-git-mv/">git-mv</a></code>(1) <code><a href="/docs/linux/man/1-git-commit/">git-commit</a></code>(1) <code><a href="/docs/linux/man/1-git-update-index/">git-update-index</a></code>(1)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>

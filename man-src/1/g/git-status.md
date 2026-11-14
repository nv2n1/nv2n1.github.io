---
title: "git-status(1)"
name: "git-status"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-status/"
description: "git-status – Show the working tree status"
---

<h2 class="name">NAME</h2>
<p> git-status &#8211; Show the working tree status </p>
<h2>SYNOPSIS</h2>
<pre><code>
git status[&lt;options&gt;...][--][&lt;pathspec&gt;...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Displays paths that have differences between the index file and the current HEAD commit, paths that have differences between the working tree and the index file, and paths in the working tree that are not tracked by Git (and are not ignored by <code><a href="/docs/linux/man/5-gitignore/">gitignore</a></code>(5)). The first are what you <i>would</i> commit by running <code>git commit</code>; the second and third are what you <i>could</i> commit by running <i>git add</i> before running <code>git commit</code>.</p>
<h2>OPTIONS</h2>
<p> -s, &#8211;short</p>
<dl>
<dt>
<dd> Give the output in the short-format.</dl>
<p> -b, &#8211;branch</p>
<dl>
<dt>
<dd> Show the branch and tracking info even in short-format.</dl>
<p> &#8211;show-stash</p>
<dl>
<dt>
<dd> Show the number of entries currently stashed away.</dl>
<p> &#8211;porcelain[=&lt;version&gt;]</p>
<dl>
<dt>
<dd> Give the output in an easy-to-parse format for scripts. This is similar to the short output, but will remain stable across Git versions and regardless of user configuration. See below for details. </p>
<p> The version parameter is used to specify the format version. This is optional and defaults to the original version <i>v1</i> format.</dl>
<p> &#8211;long</p>
<dl>
<dt>
<dd> Give the output in the long-format. This is the default.</dl>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
<dd> In addition to the names of files that have been changed, also show the textual changes that are staged to be committed (i.e., like the output of <code>git diff &#8211;cached</code>). If <code>-v</code> is specified twice, then also show the changes in the working tree that have not yet been staged (i.e., like the output of <code>git diff</code>).</dl>
<p> -u[&lt;mode&gt;], &#8211;untracked-files[=&lt;mode&gt;]</p>
<dl>
<dt>
<dd> Show untracked files. </p>
<p> The mode parameter is used to specify the handling of untracked files. It is optional: it defaults to <i>all</i>, and if specified, it must be stuck to the option (e.g. <code>-uno</code>, but not <code>-u no</code>). </p>
<p> The possible options are: </p>
<dl>
<dt>
<dd> &bull; <i>no</i> &#8211; Show no untracked files.</dl>
<dl>
<dt>
<dd> &bull; <i>normal</i> &#8211; Shows untracked files and directories.</dl>
<dl>
<dt>
<dd> &bull; <i>all</i> &#8211; Also shows individual files in untracked directories.</dl>
<p> When <code>-u</code> option is not used, untracked files and directories are shown (i.e. the same as specifying <code>normal</code>), to help you avoid forgetting to add newly created files. Because it takes extra work to find untracked files in the filesystem, this mode may take some time in a large working tree. Consider enabling untracked cache and split index if supported (see <code>git update-index &#8211;untracked-cache</code> and <code>git update-index &#8211;split-index</code>), Otherwise you can use <code>no</code> to have <code>git status</code> return more quickly without showing untracked files. </p>
<p> The default can be changed using the status.showUntrackedFiles configuration variable documented in <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1).</dl>
<p> &#8211;ignore-submodules[=&lt;when&gt;]</p>
<dl>
<dt>
<dd> Ignore changes to submodules when looking for changes. &lt;when&gt; can be either &quot;none&quot;, &quot;untracked&quot;, &quot;dirty&quot; or &quot;all&quot;, which is the default. Using &quot;none&quot; will consider the submodule modified when it either contains untracked or modified files or its HEAD differs from the commit recorded in the superproject and can be used to override any settings of the <i>ignore</i> option in <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1) or <code><a href="/docs/linux/man/5-gitmodules/">gitmodules</a></code>(5). When &quot;untracked&quot; is used submodules are not considered dirty when they only contain untracked content (but they are still scanned for modified content). Using &quot;dirty&quot; ignores all changes to the work tree of submodules, only changes to the commits stored in the superproject are shown (this was the behavior before 1.7.0). Using &quot;all&quot; hides all changes to submodules (and suppresses the output of submodule summaries when the config option <code>status.submoduleSummary</code> is set).</dl>
<p> &#8211;ignored[=&lt;mode&gt;]</p>
<dl>
<dt>
<dd> Show ignored files as well. </p>
<p> The mode parameter is used to specify the handling of ignored files. It is optional: it defaults to <i>traditional</i>. </p>
<p> The possible options are: </p>
<dl>
<dt>
<dd> &bull; <i>traditional</i> &#8211; Shows ignored files and directories, unless &#8211;untracked-files=all is specified, in which case individual files in ignored directories are displayed.</dl>
<dl>
<dt>
<dd> &bull; <i>no</i> &#8211; Show no ignored files.</dl>
<dl>
<dt>
<dd> &bull; <i>matching</i> &#8211; Shows ignored files and directories matching an ignore pattern.</dl>
<p> When <i>matching</i> mode is specified, paths that explicitly match an ignored pattern are shown. If a directory matches an ignore pattern, then it is shown, but not paths contained in the ignored directory. If a directory does not match an ignore pattern, but all contents are ignored, then the directory is not shown, but all contents are shown.</dl>
<p> -z</p>
<dl>
<dt>
<dd> Terminate entries with NUL, instead of LF. This implies the <code>&#8211;porcelain=v1</code> output format if no other format is given.</dl>
<p> &#8211;column[=&lt;options&gt;], &#8211;no-column</p>
<dl>
<dt>
<dd> Display untracked files in columns. See configuration variable <code>column.status</code> for option syntax. <code>&#8211;column</code> and <code>&#8211;no-column</code> without options are equivalent to <i>always</i> and <i>never</i> respectively.</dl>
<p> &#8211;ahead-behind, &#8211;no-ahead-behind</p>
<dl>
<dt>
<dd> Display or do not display detailed ahead/behind counts for the branch relative to its upstream branch. Defaults to true.</dl>
<p> &#8211;renames, &#8211;no-renames</p>
<dl>
<dt>
<dd> Turn on/off rename detection regardless of user configuration. See also <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1) <code>&#8211;no-renames</code>.</dl>
<p> &#8211;find-renames[=&lt;n&gt;]</p>
<dl>
<dt>
<dd> Turn on rename detection, optionally setting the similarity threshold. See also <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1) <code>&#8211;find-renames</code>.</dl>
<p> &lt;pathspec&gt;&#8230;</p>
<dl>
<dt>
<dd> See the <i>pathspec</i> entry in <code><a href="/docs/linux/man/7-gitglossary/">gitglossary</a></code>(7).</dl>
<h2>OUTPUT</h2>
<p> The output from this command is designed to be used as a commit template comment. The default, long format, is designed to be human readable, verbose and descriptive. Its contents and format are subject to change at any time. </p>
<p> The paths mentioned in the output, unlike many other Git commands, are made relative to the current directory if you are working in a subdirectory (this is on purpose, to help cutting and pasting). See the status.relativePaths config option below.</p>
<h3>Short Format</h3>
<p> In the short-format, the status of each path is shown as one of these forms </p>
<dl>
<dt>
<dd>
<pre>
XY PATH
XY ORIG_PATH -&gt; PATH
</pre>
</dl>
<p> where <code>ORIG_PATH</code> is where the renamed/copied contents came from. <code>ORIG_PATH</code> is only shown when the entry is renamed or copied. The <code>XY</code> is a two-letter status code. </p>
<p> The fields (including the <code>-&gt;</code>) are separated from each other by a single space. If a filename contains whitespace or other nonprintable characters, that field will be quoted in the manner of a C string literal: surrounded by ASCII double quote (34) characters, and with interior special characters backslash-escaped. </p>
<p> There are three different types of states that are shown using this format, and each one uses the <code>XY</code> syntax differently: </p>
<dl>
<dt>
<dd> &bull; When a merge is occurring and the merge was successful, or outside of a merge situation, <code>X</code> shows the status of the index and <code>Y</code> shows the status of the working tree.</dl>
<dl>
<dt>
<dd> &bull; When a merge conflict has occurred and has not yet been resolved, <code>X</code> and <code>Y</code> show the state introduced by each head of the merge, relative to the common ancestor. These paths are said to be <i>unmerged</i>.</dl>
<dl>
<dt>
<dd> &bull; When a path is untracked, <code>X</code> and <code>Y</code> are always the same, since they are unknown to the index. <code>??</code> is used for untracked paths. Ignored files are not listed unless <code>&#8211;ignored</code> is used; if it is, ignored files are indicated by <code>!!</code>.</dl>
<p> Note that the term <i>merge</i> here also includes rebases using the default <code>&#8211;merge</code> strategy, cherry-picks, and anything else using the merge machinery. </p>
<p> In the following table, these three classes are shown in separate sections, and these characters are used for <code>X</code> and <code>Y</code> fields for the first two sections that show tracked paths: </p>
<dl>
<dt>
<dd> &bull; &#8216; &#8216; = unmodified</dl>
<dl>
<dt>
<dd> &bull; <i>M</i> = modified</dl>
<dl>
<dt>
<dd> &bull; <i>T</i> = file type changed (regular file, symbolic link or submodule)</dl>
<dl>
<dt>
<dd> &bull; <i>A</i> = added</dl>
<dl>
<dt>
<dd> &bull; <i>D</i> = deleted</dl>
<dl>
<dt>
<dd> &bull; <i>R</i> = renamed</dl>
<dl>
<dt>
<dd> &bull; <i>C</i> = copied (if config option status.renames is set to &quot;copies&quot;)</dl>
<dl>
<dt>
<dd> &bull; <i>U</i> = updated but unmerged</dl>
<dl>
<dt>
<dd>
X Y Meaning&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -[AMD] not updated<br />
        M[MTD] updated in index<br />
            T[MTD] type changed in index<br />
                A[MTD] added to index<br />
                    D deleted from index<br />
                        R[MTD] renamed in index<br />
                            C[MTD] copied in index<br />
                                [MTARC] index and<br />
    work tree matches<br />
        [MTARC] M work tree changed since index<br />
            [MTARC] T type changed in work tree since index<br />
                [MTARC] D deleted in work tree<br />
                    R renamed in work tree<br />
                        C copied in work tree&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -D D unmerged,<br />
    both deleted<br />
        A U unmerged,<br />
    added by us<br />
        U D unmerged,<br />
    deleted by them<br />
        U A unmerged,<br />
    added by them<br />
        D U unmerged,<br />
    deleted by us<br />
        A A unmerged,<br />
    both added<br />
        U U unmerged,<br />
    both modified&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;<br />
    ? ? untracked !!ignored&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;
</dl>
<p> Submodules have more state and instead report M the submodule has a different HEAD than recorded in the index m the submodule has modified content ? the submodule has untracked files since modified content or untracked files in a submodule cannot be added via <code>git add</code> in the superproject to prepare a commit. </p>
<p> <i>m</i> and <i>?</i> are applied recursively. For example if a nested submodule in a submodule contains an untracked file, this is reported as <i>?</i> as well. </p>
<p> If -b is used the short-format status is preceded by a line </p>
<dl>
<dt>
<dd>
<pre>
## branchname tracking info
</pre>
</dl>
<h3>Porcelain Format Version 1</h3>
<p> Version 1 porcelain format is similar to the short format, but is guaranteed not to change in a backwards-incompatible way between Git versions or based on user configuration. This makes it ideal for parsing by scripts. The description of the short format above also describes the porcelain format, with a few exceptions: </p>
<dl>
<dt>
<dd> 1. The user&#8217;s color.status configuration is not respected; color will always be off.</dl>
<dl>
<dt>
<dd> 2. The user&#8217;s status.relativePaths configuration is not respected; paths shown will always be relative to the repository root.</dl>
<p> There is also an alternate -z format recommended for machine parsing. In that format, the status field is the same, but some other things change. First, the <i>-&gt;</i> is omitted from rename entries and the field order is reversed (e.g <i>from -&gt; to</i> becomes <i>to from</i>). Second, a NUL (ASCII 0) follows each filename, replacing space as a field separator and the terminating newline (but a space still separates the status field from the first filename). Third, filenames containing special characters are not specially formatted; no quoting or backslash-escaping is performed. </p>
<p> Any submodule changes are reported as modified <code>M</code> instead of <code>m</code> or single <code>?</code>.</p>
<h3>Porcelain Format Version 2</h3>
<p> Version 2 format adds more detailed information about the state of the worktree and changed items. Version 2 also defines an extensible set of easy to parse optional headers. </p>
<p> Header lines start with &quot;#&quot; and are added in response to specific command line arguments. Parsers should ignore headers they don&#8217;t recognize. </p>
<p> <font SIZE="+1"> <code>Branch Headers</code></p>
<dl>
<dt>
<dd>
<p> If <code>&#8211;branch</code> is given, a series of header lines are printed with information about the current branch. </p>
<dl>
<dt>
<dd> </font><br />
Line Notes&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212;<br />
#branch.oid &lt; commit&gt; | (initial)Current commit.<br />
#branch.head &lt; branch&gt; | (detached)Current branch.<br />
#branch.upstream &lt; upstream_branch&gt; If upstream is set.<br />
#branch.ab + &lt; ahead&gt; &#8211; &lt; behind&gt; If upstream is set and<br />
    the commit is present.&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212;
</dl>
</dl>
<p> <font SIZE="+1"> <code>Changed Tracked Entries</code></p>
<dl>
<dt>
<dd>
<p> Following the headers, a series of lines are printed for tracked entries. One of three different line formats may be used to describe an entry depending on the type of change. Tracked entries are printed in an undefined order; parsers should allow for a mixture of the 3 line types in any order. </p>
<p> Ordinary changed entries have the following format: </p>
<dl>
<dt>
<dd> </font></p>
<pre>
1 &lt;XY&gt; &lt;sub&gt; &lt;mH&gt; &lt;mI&gt; &lt;mW&gt; &lt;hH&gt; &lt;hI&gt; &lt;path&gt;
</pre>
</dl>
<p> Renamed or copied entries have the following format: </p>
<dl>
<dt>
<dd>
<pre>
2 &lt;XY&gt; &lt;sub&gt; &lt;mH&gt; &lt;mI&gt; &lt;mW&gt; &lt;hH&gt; &lt;hI&gt; &lt;X&gt;&lt;score&gt; &lt;path&gt;&lt;sep&gt;&lt;origPath&gt;
</pre>
</dl>
<dl>
<dt>
<dd>
Field Meaning&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;&lt;XY&gt; A 2 character field containing the staged and<br />
    unstaged XY values described in the short format,<br />
    with unchanged indicated by a &#8220;.&#8221; rather than<br />
        a space.&lt;sub&gt;A 4 character field describing the submodule state.&#8221;N&#8230;&#8221; when the entry is not a submodule.&#8221;S&lt;c&gt;&lt;m&gt;&lt;u&gt;&#8221; when the entry is a submodule.&lt;c&gt;is &#8220;C&#8221; if the commit changed;<br />
otherwise &#8220;.&#8221;.&lt;m&gt;is &#8220;M&#8221; if it has tracked changes;<br />
otherwise &#8220;.&#8221;.&lt;u&gt;is &#8220;U&#8221; if there are untracked changes;<br />
otherwise &#8220;.&#8221;.&lt;mH&gt;The octal file mode in HEAD.&lt;mI&gt;The octal file mode in the index.&lt;mW&gt;The octal file mode in the worktree.&lt;hH&gt;The object name in HEAD.&lt;hI&gt;The object name in the index.&lt;X&gt;&lt;score&gt; The rename or copy score(denoting the percentage of similarity between the source and target of the move or copy).For example &#8220;R100&#8221; or &#8220;C75&#8221;.&lt;path&gt;The pathname.In a renamed / copied entry, this is the target path.&lt;sep&gt;When the `- z` option is used, the 2 pathnames are separated with a NUL(ASCII 0x00) byte;<br />
otherwise, a tab(ASCII 0x09) byte separates them.&lt;origPath&gt;The pathname in the commit at HEAD or in the index.This is only present in a renamed / copied entry, and tells where the renamed / copied contents came from.&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212;
</dl>
<p> Unmerged entries have the following format; the first character is a &quot;u&quot; to distinguish from ordinary changed entries. </p>
<dl>
<dt>
<dd>
<pre>
u &lt;XY&gt; &lt;sub&gt; &lt;m1&gt; &lt;m2&gt; &lt;m3&gt; &lt;mW&gt; &lt;h1&gt; &lt;h2&gt; &lt;h3&gt; &lt;path&gt;
</pre>
</dl>
<dl>
<dt>
<dd>
<pre><code>
Field Meaning-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --&lt;XY&gt; A 2 character field describing the conflict type
        as described in the short format.&lt;sub&gt;A 4 character field describing the submodule state
            as described above.&lt;m1&gt;The octal file mode in stage 1. &lt; m2 &gt; The octal file mode in stage 2. &lt; m3 &gt; The octal file mode in stage 3. &lt; mW &gt; The octal file mode in the worktree.&lt;h1&gt;The object name in stage 1. &lt; h2 &gt; The object name in stage 2. &lt; h3 &gt; The object name in stage 3. &lt; path &gt; The pathname.-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
</code></pre>
</dl>
</dl>
<p> <font SIZE="+1"> <code>Other Items</code></p>
<dl>
<dt>
<dd>
<p> Following the tracked entries (and if requested), a series of lines will be printed for untracked and then ignored items found in the worktree. </p>
<p> Untracked items have the following format: </p>
<dl>
<dt>
<dd> </font></p>
<pre>
? &lt;path&gt;
</pre>
</dl>
<p> Ignored items have the following format: </p>
<dl>
<dt>
<dd>
<pre>
! &lt;path&gt;
</pre>
</dl>
</dl>
<p> <font SIZE="+1"> <code>Pathname Format Notes and -z</code></p>
<dl>
<dt>
<dd>
<p> When the <code>-z</code> option is given, pathnames are printed as is and without any quoting and lines are terminated with a NUL (ASCII 0x00) byte. </p>
<p> Without the <code>-z</code> option, pathnames with &quot;unusual&quot; characters are quoted as explained for the configuration variable <code>core.quotePath</code> (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)).</dl>
<p> </font></p>
<h2>CONFIGURATION</h2>
<p> The command honors <code>color.status</code> (or <code>status.color</code> &#8212; they mean the same thing and the latter is kept for backward compatibility) and <code>color.status.&lt;slot&gt;</code> configuration variables to colorize its output. </p>
<p> If the config variable <code>status.relativePaths</code> is set to false, then all paths shown are relative to the repository root, not to the current directory. </p>
<p> If <code>status.submoduleSummary</code> is set to a non zero number or true (identical to -1 or an unlimited number), the submodule summary will be enabled for the long format and a summary of commits for modified submodules will be shown (see &#8211;summary-limit option of <code><a href="/docs/linux/man/1-git-submodule/">git-submodule</a></code>(1)). Please note that the summary output from the status command will be suppressed for all submodules when <code>diff.ignoreSubmodules</code> is set to <i>all</i> or only for those submodules where <code>submodule.&lt;name&gt;.ignore=all</code>. To also view the summary for ignored submodules you can either use the &#8211;ignore-submodules=dirty command line option or the <i>git submodule summary</i> command, which shows a similar output but does not honor these settings.</p>
<h2>BACKGROUND REFRESH</h2>
<p> By default, <code>git status</code> will automatically refresh the index, updating the cached stat information from the working tree and writing out the result. Writing out the updated index is an optimization that isn&#8217;t strictly necessary (<code>status</code> computes the values for itself, but writing them out is just to save subsequent programs from repeating our computation). When <code>status</code> is run in the background, the lock held during the write may conflict with other simultaneous processes, causing them to fail. Scripts running <code>status</code> in the background should consider using <code>git &#8211;no-optional-locks status</code> (see <code><a href="/docs/linux/man/1-git/">git</a></code>(1) for details).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-gitignore/">gitignore</a></code>(5)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>

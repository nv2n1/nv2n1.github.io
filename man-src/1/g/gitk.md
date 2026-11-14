---
title: "gitk(1)"
name: "gitk"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gitk/"
description: "gitk – The Git repository browser"
---

<h2 class="name">NAME</h2>
<p> gitk &#8211; The Git repository browser </p>
<h2>SYNOPSIS</h2>
<pre><code>
gitk[&lt;options&gt;][&lt;revision range&gt;][--][&lt;path&gt;...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Displays changes in a repository or a selected set of commits. This includes visualizing the commit graph, showing information related to each commit, and the files in the trees of each revision.</p>
<h2>OPTIONS</h2>
<p> To control which revisions to show, gitk supports most options applicable to the <i>git rev-list</i> command. It also supports a few options applicable to the <i>git diff-*</i> commands to control how the changes each commit introduces are shown. Finally, it supports some gitk-specific options. </p>
<p> gitk generally only understands options with arguments in the <i>sticked</i> form (see <code><a href="/docs/linux/man/7-gitcli/">gitcli</a></code>(7)) due to limitations in the command-line parser.</p>
<h3>rev-list options and arguments</h3>
<p> This manual page describes only the most frequently used options. See <code><a href="/docs/linux/man/1-git-rev-list/">git-rev-list</a></code>(1) for a complete list. </p>
<p> &#8211;all</p>
<dl>
<dt>
<dd> Show all refs (branches, tags, etc.).</dl>
<p> &#8211;branches[=&lt;pattern&gt;], &#8211;tags[=&lt;pattern&gt;], &#8211;remotes[=&lt;pattern&gt;]</p>
<dl>
<dt>
<dd> Pretend as if all the branches (tags, remote branches, resp.) are listed on the command line as <i>&lt;commit&gt;</i>. If <i>&lt;pattern&gt;</i> is given, limit refs to ones matching given shell glob. If pattern lacks <i>?</i>, <i>*</i>, or <i>[</i>, <i>/*</i> at the end is implied.</dl>
<p> &#8211;since=&lt;date&gt;</p>
<dl>
<dt>
<dd> Show commits more recent than a specific date.</dl>
<p> &#8211;until=&lt;date&gt;</p>
<dl>
<dt>
<dd> Show commits older than a specific date.</dl>
<p> &#8211;date-order</p>
<dl>
<dt>
<dd> Sort commits by date when possible.</dl>
<p> &#8211;merge</p>
<dl>
<dt>
<dd> After an attempt to merge stops with conflicts, show the commits on the history between two branches (i.e. the HEAD and the MERGE_HEAD) that modify the conflicted files and do not exist on all the heads being merged.</dl>
<p> &#8211;left-right</p>
<dl>
<dt>
<dd> Mark which side of a symmetric difference a commit is reachable from. Commits from the left side are prefixed with a <code>&lt;</code> symbol and those from the right with a <code>&gt;</code> symbol.</dl>
<p> &#8211;full-history</p>
<dl>
<dt>
<dd> When filtering history with <i>&lt;path&gt;&#8230;</i>, does not prune some history. (See &quot;History simplification&quot; in <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1) for a more detailed explanation.)</dl>
<p> &#8211;simplify-merges</p>
<dl>
<dt>
<dd> Additional option to <code>&#8211;full-history</code> to remove some needless merges from the resulting history, as there are no selected commits contributing to this merge. (See &quot;History simplification&quot; in <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1) for a more detailed explanation.)</dl>
<p> &#8211;ancestry-path</p>
<dl>
<dt>
<dd> When given a range of commits to display (e.g. <i>commit1..commit2</i> or <i>commit2 ^commit1</i>), only display commits that exist directly on the ancestry chain between the <i>commit1</i> and <i>commit2</i>, i.e. commits that are both descendants of <i>commit1</i>, and ancestors of <i>commit2</i>. (See &quot;History simplification&quot; in <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1) for a more detailed explanation.)</dl>
<p> -L&lt;start&gt;,&lt;end&gt;:&lt;file&gt;, -L:&lt;funcname&gt;:&lt;file&gt;</p>
<dl>
<dt>
<dd> Trace the evolution of the line range given by <i>&lt;start&gt;,&lt;end&gt;</i>, or by the function name regex <i>&lt;funcname&gt;</i>, within the <i>&lt;file&gt;</i>. You may not give any pathspec limiters. This is currently limited to a walk starting from a single revision, i.e., you may only give zero or one positive revision arguments, and <i>&lt;start&gt;</i> and <i>&lt;end&gt;</i> (or <i>&lt;funcname&gt;</i>) must exist in the starting revision. You can specify this option more than once. Implies <code>&#8211;patch</code>. Patch output can be suppressed using <code>&#8211;no-patch</code>, but other diff formats (namely <code>&#8211;raw</code>, <code>&#8211;numstat</code>, <code>&#8211;shortstat</code>, <code>&#8211;dirstat</code>, <code>&#8211;summary</code>, <code>&#8211;name-only</code>, <code>&#8211;name-status</code>, <code>&#8211;check</code>) are not currently implemented. </p>
<p> <i>&lt;start&gt;</i> and <i>&lt;end&gt;</i> can take one of these forms: </p>
<dl>
<dt>
<dd> &bull; number </p>
<p> If <i>&lt;start&gt;</i> or <i>&lt;end&gt;</i> is a number, it specifies an absolute line number (lines count from 1).</dl>
<dl>
<dt>
<dd> &bull; <code>/regex/</code> </p>
<p> This form will use the first line matching the given POSIX regex. If <i>&lt;start&gt;</i> is a regex, it will search from the end of the previous <code>-L</code> range, if any, otherwise from the start of file. If <i>&lt;start&gt;</i> is <code>^/regex/</code>, it will search from the start of file. If <i>&lt;end&gt;</i> is a regex, it will search starting at the line given by <i>&lt;start&gt;</i>.</dl>
<dl>
<dt>
<dd> &bull; +offset or -offset </p>
<p> This is only valid for <i>&lt;end&gt;</i> and will specify a number of lines before or after the line given by <i>&lt;start&gt;</i>.</dl>
<p> If <code>:&lt;funcname&gt;</code> is given in place of <i>&lt;start&gt;</i> and <i>&lt;end&gt;</i>, it is a regular expression that denotes the range from the first funcname line that matches <i>&lt;funcname&gt;</i>, up to the next funcname line. <code>:&lt;funcname&gt;</code> searches from the end of the previous <code>-L</code> range, if any, otherwise from the start of file. <code>^:&lt;funcname&gt;</code> searches from the start of file. The function names are determined in the same way as <code>git diff</code> works out patch hunk headers (see <i>Defining a custom hunk-header</i> in <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5)).</dl>
<p> &lt;revision range&gt;</p>
<dl>
<dt>
<dd> Limit the revisions to show. This can be either a single revision meaning show from the given revision and back, or it can be a range in the form &quot;<i>&lt;from&gt;</i>..<i>&lt;to&gt;</i>&quot; to show all revisions between <i>&lt;from&gt;</i> and back to <i>&lt;to&gt;</i>. Note, more advanced revision selection can be applied. For a more complete list of ways to spell object names, see <code><a href="/docs/linux/man/7-gitrevisions/">gitrevisions</a></code>(7).</dl>
<p> &lt;path&gt;&#8230;</p>
<dl>
<dt>
<dd> Limit commits to the ones touching files in the given paths. Note, to avoid ambiguity with respect to revision names use &quot;&#8211;&quot; to separate the paths from any preceding options.</dl>
<h3>gitk-specific options</h3>
<p> &#8211;argscmd=&lt;command&gt;</p>
<dl>
<dt>
<dd> Command to be run each time gitk has to determine the revision range to show. The command is expected to print on its standard output a list of additional revisions to be shown, one per line. Use this instead of explicitly specifying a <i>&lt;revision range&gt;</i> if the set of commits to show may vary between refreshes.</dl>
<p> &#8211;select-commit=&lt;ref&gt;</p>
<dl>
<dt>
<dd> Select the specified commit after loading the graph. Default behavior is equivalent to specifying <i>&#8211;select-commit=HEAD</i>.</dl>
<h2>EXAMPLES</h2>
<p> gitk v2.6.12.. include/scsi drivers/scsi</p>
<dl>
<dt>
<dd> Show the changes since version <i>v2.6.12</i> that changed any file in the include/scsi or drivers/scsi subdirectories</dl>
<p> gitk &#8211;since=&quot;2 weeks ago&quot; &#8212; gitk</p>
<dl>
<dt>
<dd> Show the changes during the last two weeks to the file <i>gitk</i>. The &quot;&#8211;&quot; is necessary to avoid confusion with the <code>branch</code> named <i>gitk</i></dl>
<p> gitk &#8211;max-count=100 &#8211;all &#8212; Makefile</p>
<dl>
<dt>
<dd> Show at most 100 changes made to the file <i>Makefile</i>. Instead of only looking for changes in the current branch look in all branches.</dl>
<h2>FILES</h2>
<p> User configuration and preferences are stored at: </p>
<dl>
<dt>
<dd> &bull; <code>$XDG_CONFIG_HOME/git/gitk</code> if it exists, otherwise</dl>
<dl>
<dt>
<dd> &bull; <code>$HOME/.gitk</code> if it exists</dl>
<p> If neither of the above exist then <code>$XDG_CONFIG_HOME/git/gitk</code> is created and used by default. If <i>$XDG_CONFIG_HOME</i> is not set it defaults to <code>$HOME/.config</code> in all cases.</p>
<h2>HISTORY</h2>
<p> Gitk was the first graphical repository browser. It&#8217;s written in tcl/tk. </p>
<p> <i>gitk</i> is actually maintained as an independent project, but stable versions are distributed as part of the Git suite for the convenience of end users. </p>
<p> gitk-git/ comes from Paul Mackerras&#8217;s gitk project: </p>
<dl>
<dt>
<dd>
<pre>
<a href="git://ozlabs.org/~paulus/gitk">git://ozlabs.org/~paulus/gitk</a>
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-qgit/">qgit</a>(1)</i></p>
<dl>
<dt>
<dd> A repository browser written in C++ using Qt.</dl>
<p> <i><a href="/docs/linux/man/1-tig/">tig</a>(1)</i></p>
<dl>
<dt>
<dd> A minimal repository browser and Git tool output highlighter written in C using Ncurses.</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>

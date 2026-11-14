---
title: "git-log(1)"
name: "git-log"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-log/"
description: "git-log – Show commit logs"
---

<h2 class="name">NAME</h2>
<p> git-log &#8211; Show commit logs </p>
<h2>SYNOPSIS</h2>
<pre><code>
git log[&lt;options&gt;][&lt;revision range&gt;][[--]&lt;path&gt;...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Shows the commit logs. </p>
<p> List commits that are reachable by following the <code>parent</code> links from the given commit(s), but exclude commits that are reachable from the one(s) given with a <i>^</i> in front of them. The output is given in reverse chronological order by default. </p>
<p> You can think of this as a set operation. Commits reachable from any of the commits given on the command line form a set, and then commits reachable from any of the ones given with <i>^</i> in front are subtracted from that set. The remaining commits are what comes out in the command&#8217;s output. Various other options and paths parameters can be used to further limit the result. </p>
<p> Thus, the following command: </p>
<dl>
<dt>
<dd>
<pre>
$ git log foo bar ^baz
</pre>
</dl>
<p> means &quot;list all the commits which are reachable from <i>foo</i> or <i>bar</i>, but not from <i>baz</i>&quot;. </p>
<p> A special notation &quot;<i>&lt;commit1&gt;</i>..<i>&lt;commit2&gt;</i>&quot; can be used as a short-hand for &quot;^<i>&lt;commit1&gt;</i> <i>&lt;commit2&gt;</i>&quot;. For example, either of the following may be used interchangeably: </p>
<dl>
<dt>
<dd>
<pre>
$ git log origin..HEAD
$ git log HEAD ^origin
</pre>
</dl>
<p> Another special notation is &quot;<i>&lt;commit1&gt;</i>&#8230;<i>&lt;commit2&gt;</i>&quot; which is useful for merges. The resulting set of commits is the symmetric difference between the two operands. The following two commands are equivalent: </p>
<dl>
<dt>
<dd>
<pre>
$ git log A B --not $(git merge-base --all A B)
$ git log A...B
</pre>
</dl>
<p> The command takes options applicable to the <code><a href="/docs/linux/man/1-git-rev-list/">git-rev-list</a></code>(1) command to control what is shown and how, and options applicable to the <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1) command to control how the changes each commit introduces are shown.</p>
<h2>OPTIONS</h2>
<p> &#8211;follow</p>
<dl>
<dt>
<dd> Continue listing the history of a file beyond renames (works only for a single file).</dl>
<p> &#8211;no-decorate, &#8211;decorate[=short|full|auto|no]</p>
<dl>
<dt>
<dd> Print out the ref names of any commits that are shown. If <i>short</i> is specified, the ref name prefixes <i>refs/heads/</i>, <i>refs/tags/</i> and <i>refs/remotes/</i> will not be printed. If <i>full</i> is specified, the full ref name (including prefix) will be printed. If <i>auto</i> is specified, then if the output is going to a terminal, the ref names are shown as if <i>short</i> were given, otherwise no ref names are shown. The option <code>&#8211;decorate</code> is short-hand for <code>&#8211;decorate=short</code>. Default to configuration value of <code>log.decorate</code> if configured, otherwise, <code>auto</code>.</dl>
<p> &#8211;decorate-refs=&lt;pattern&gt;, &#8211;decorate-refs-exclude=&lt;pattern&gt;</p>
<dl>
<dt>
<dd> If no <code>&#8211;decorate-refs</code> is given, pretend as if all refs were included. For each candidate, do not use it for decoration if it matches any patterns given to <code>&#8211;decorate-refs-exclude</code> or if it doesn&#8217;t match any of the patterns given to <code>&#8211;decorate-refs</code>. The <code>log.excludeDecoration</code> config option allows excluding refs from the decorations, but an explicit <code>&#8211;decorate-refs</code> pattern will override a match in <code>log.excludeDecoration</code>.</dl>
<p> &#8211;source</p>
<dl>
<dt>
<dd> Print out the ref name given on the command line by which each commit was reached.</dl>
<p> &#8211;[no-]mailmap, &#8211;[no-]use-mailmap</p>
<dl>
<dt>
<dd> Use mailmap file to map author and committer names and email addresses to canonical real names and email addresses. See <code><a href="/docs/linux/man/1-git-shortlog/">git-shortlog</a></code>(1).</dl>
<p> &#8211;full-diff</p>
<dl>
<dt>
<dd> Without this flag, <code>git log -p &lt;path&gt;&#8230;</code> shows commits that touch the specified paths, and diffs about the same specified paths. With this, the full diff is shown for commits that touch the specified paths; this means that &quot;&lt;path&gt;&#8230;&quot; limits only commits, and doesn&#8217;t limit diff for those commits. </p>
<p> Note that this affects all diff-based output types, e.g. those produced by <code>&#8211;stat</code>, etc.</dl>
<p> &#8211;log-size</p>
<dl>
<dt>
<dd> Include a line &#8220;log size &lt;number&gt;&#8221; in the output for each commit, where &lt;number&gt; is the length of that commit&#8217;s message in bytes. Intended to speed up tools that read log messages from <code>git log</code> output by allowing them to allocate space in advance.</dl>
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
<dd> Show only commits in the specified revision range. When no &lt;revision range&gt; is specified, it defaults to <code>HEAD</code> (i.e. the whole history leading to the current commit). <code>origin..HEAD</code> specifies all the commits reachable from the current commit (i.e. <code>HEAD</code>), but not from <code>origin</code>. For a complete list of ways to spell &lt;revision range&gt;, see the <i>Specifying Ranges</i> section of <code><a href="/docs/linux/man/7-gitrevisions/">gitrevisions</a></code>(7).</dl>
<p> [&#8211;] &lt;path&gt;&#8230;</p>
<dl>
<dt>
<dd> Show only commits that are enough to explain how the files that match the specified paths came to be. See <i>History Simplification</i> below for details and other simplification modes. </p>
<p> Paths may need to be prefixed with <code>&#8212;</code> to separate them from options or the revision range, when confusion arises.</dl>
<h3>Commit Limiting</h3>
<p> Besides specifying a range of commits that should be listed using the special notations explained in the description, additional commit limiting may be applied. </p>
<p> Using more options generally further limits the output (e.g. <code>&#8211;since=&lt;date1&gt;</code> limits to commits newer than <code>&lt;date1&gt;</code>, and using it with <code>&#8211;grep=&lt;pattern&gt;</code> further limits to commits whose log message has a line that matches <code>&lt;pattern&gt;</code>), unless otherwise noted. </p>
<p> Note that these are applied before commit ordering and formatting options, such as <code>&#8211;reverse</code>. </p>
<p> -&lt;number&gt;, -n &lt;number&gt;, &#8211;max-count=&lt;number&gt;</p>
<dl>
<dt>
<dd> Limit the number of commits to output.</dl>
<p> &#8211;skip=&lt;number&gt;</p>
<dl>
<dt>
<dd> Skip <i>number</i> commits before starting to show the commit output.</dl>
<p> &#8211;since=&lt;date&gt;, &#8211;after=&lt;date&gt;</p>
<dl>
<dt>
<dd> Show commits more recent than a specific date.</dl>
<p> &#8211;until=&lt;date&gt;, &#8211;before=&lt;date&gt;</p>
<dl>
<dt>
<dd> Show commits older than a specific date.</dl>
<p> &#8211;author=&lt;pattern&gt;, &#8211;committer=&lt;pattern&gt;</p>
<dl>
<dt>
<dd> Limit the commits output to ones with author/committer header lines that match the specified pattern (regular expression). With more than one <code>&#8211;author=&lt;pattern&gt;</code>, commits whose author matches any of the given patterns are chosen (similarly for multiple <code>&#8211;committer=&lt;pattern&gt;</code>).</dl>
<p> &#8211;grep-reflog=&lt;pattern&gt;</p>
<dl>
<dt>
<dd> Limit the commits output to ones with reflog entries that match the specified pattern (regular expression). With more than one <code>&#8211;grep-reflog</code>, commits whose reflog message matches any of the given patterns are chosen. It is an error to use this option unless <code>&#8211;walk-reflogs</code> is in use.</dl>
<p> &#8211;grep=&lt;pattern&gt;</p>
<dl>
<dt>
<dd> Limit the commits output to ones with log message that matches the specified pattern (regular expression). With more than one <code>&#8211;grep=&lt;pattern&gt;</code>, commits whose message matches any of the given patterns are chosen (but see <code>&#8211;all-match</code>). </p>
<p> When <code>&#8211;notes</code> is in effect, the message from the notes is matched as if it were part of the log message.</dl>
<p> &#8211;all-match</p>
<dl>
<dt>
<dd> Limit the commits output to ones that match all given <code>&#8211;grep</code>, instead of ones that match at least one.</dl>
<p> &#8211;invert-grep</p>
<dl>
<dt>
<dd> Limit the commits output to ones with log message that do not match the pattern specified with <code>&#8211;grep=&lt;pattern&gt;</code>.</dl>
<p> -i, &#8211;regexp-ignore-case</p>
<dl>
<dt>
<dd> Match the regular expression limiting patterns without regard to letter case.</dl>
<p> &#8211;basic-regexp</p>
<dl>
<dt>
<dd> Consider the limiting patterns to be basic regular expressions; this is the default.</dl>
<p> -E, &#8211;extended-regexp</p>
<dl>
<dt>
<dd> Consider the limiting patterns to be extended regular expressions instead of the default basic regular expressions.</dl>
<p> -F, &#8211;fixed-strings</p>
<dl>
<dt>
<dd> Consider the limiting patterns to be fixed strings (don&#8217;t interpret pattern as a regular expression).</dl>
<p> -P, &#8211;perl-regexp</p>
<dl>
<dt>
<dd> Consider the limiting patterns to be Perl-compatible regular expressions. </p>
<p> Support for these types of regular expressions is an optional compile-time dependency. If Git wasn&#8217;t compiled with support for them providing this option will cause it to die.</dl>
<p> &#8211;remove-empty</p>
<dl>
<dt>
<dd> Stop when a given path disappears from the tree.</dl>
<p> &#8211;merges</p>
<dl>
<dt>
<dd> Print only merge commits. This is exactly the same as <code>&#8211;min-parents=2</code>.</dl>
<p> &#8211;no-merges</p>
<dl>
<dt>
<dd> Do not print commits with more than one parent. This is exactly the same as <code>&#8211;max-parents=1</code>.</dl>
<p> &#8211;min-parents=&lt;number&gt;, &#8211;max-parents=&lt;number&gt;, &#8211;no-min-parents, &#8211;no-max-parents</p>
<dl>
<dt>
<dd> Show only commits which have at least (or at most) that many parent commits. In particular, <code>&#8211;max-parents=1</code> is the same as <code>&#8211;no-merges</code>, <code>&#8211;min-parents=2</code> is the same as <code>&#8211;merges</code>. <code>&#8211;max-parents=0</code> gives all root commits and <code>&#8211;min-parents=3</code> all octopus merges. </p>
<p> <code>&#8211;no-min-parents</code> and <code>&#8211;no-max-parents</code> reset these limits (to no limit) again. Equivalent forms are <code>&#8211;min-parents=0</code> (any commit has 0 or more parents) and <code>&#8211;max-parents=-1</code> (negative numbers denote no upper limit).</dl>
<p> &#8211;first-parent</p>
<dl>
<dt>
<dd> Follow only the first parent commit upon seeing a merge commit. This option can give a better overview when viewing the evolution of a particular topic branch, because merges into a topic branch tend to be only about adjusting to updated upstream from time to time, and this option allows you to ignore the individual commits brought in to your history by such a merge. </p>
<p> This option also changes default diff format for merge commits to <code>first-parent</code>, see <code>&#8211;diff-merges=first-parent</code> for details.</dl>
<p> &#8211;not</p>
<dl>
<dt>
<dd> Reverses the meaning of the <i>^</i> prefix (or lack thereof) for all following revision specifiers, up to the next <code>&#8211;not</code>.</dl>
<p> &#8211;all</p>
<dl>
<dt>
<dd> Pretend as if all the refs in <code>refs/</code>, along with <code>HEAD</code>, are listed on the command line as <i>&lt;commit&gt;</i>.</dl>
<p> &#8211;branches[=&lt;pattern&gt;]</p>
<dl>
<dt>
<dd> Pretend as if all the refs in <code>refs/heads</code> are listed on the command line as <i>&lt;commit&gt;</i>. If <i>&lt;pattern&gt;</i> is given, limit branches to ones matching given shell glob. If pattern lacks <i>?</i>, <i>*</i>, or <i>[</i>, <i>/*</i> at the end is implied.</dl>
<p> &#8211;tags[=&lt;pattern&gt;]</p>
<dl>
<dt>
<dd> Pretend as if all the refs in <code>refs/tags</code> are listed on the command line as <i>&lt;commit&gt;</i>. If <i>&lt;pattern&gt;</i> is given, limit tags to ones matching given shell glob. If pattern lacks <i>?</i>, <i>*</i>, or <i>[</i>, <i>/*</i> at the end is implied.</dl>
<p> &#8211;remotes[=&lt;pattern&gt;]</p>
<dl>
<dt>
<dd> Pretend as if all the refs in <code>refs/remotes</code> are listed on the command line as <i>&lt;commit&gt;</i>. If <i>&lt;pattern&gt;</i> is given, limit remote-tracking branches to ones matching given shell glob. If pattern lacks <i>?</i>, <i>*</i>, or <i>[</i>, <i>/*</i> at the end is implied.</dl>
<p> &#8211;glob=&lt;glob-pattern&gt;</p>
<dl>
<dt>
<dd> Pretend as if all the refs matching shell glob <i>&lt;glob-pattern&gt;</i> are listed on the command line as <i>&lt;commit&gt;</i>. Leading <i>refs/</i>, is automatically prepended if missing. If pattern lacks <i>?</i>, <i>*</i>, or <i>[</i>, <i>/*</i> at the end is implied.</dl>
<p> &#8211;exclude=&lt;glob-pattern&gt;</p>
<dl>
<dt>
<dd> Do not include refs matching <i>&lt;glob-pattern&gt;</i> that the next <code>&#8211;all</code>, <code>&#8211;branches</code>, <code>&#8211;tags</code>, <code>&#8211;remotes</code>, or <code>&#8211;glob</code> would otherwise consider. Repetitions of this option accumulate exclusion patterns up to the next <code>&#8211;all</code>, <code>&#8211;branches</code>, <code>&#8211;tags</code>, <code>&#8211;remotes</code>, or <code>&#8211;glob</code> option (other options or arguments do not clear accumulated patterns). </p>
<p> The patterns given should not begin with <code>refs/heads</code>, <code>refs/tags</code>, or <code>refs/remotes</code> when applied to <code>&#8211;branches</code>, <code>&#8211;tags</code>, or <code>&#8211;remotes</code>, respectively, and they must begin with <code>refs/</code> when applied to <code>&#8211;glob</code> or <code>&#8211;all</code>. If a trailing <i>/*</i> is intended, it must be given explicitly.</dl>
<p> &#8211;reflog</p>
<dl>
<dt>
<dd> Pretend as if all objects mentioned by reflogs are listed on the command line as <code>&lt;commit&gt;</code>.</dl>
<p> &#8211;alternate-refs</p>
<dl>
<dt>
<dd> Pretend as if all objects mentioned as ref tips of alternate repositories were listed on the command line. An alternate repository is any repository whose object directory is specified in <code>objects/info/alternates</code>. The set of included objects may be modified by <code>core.alternateRefsCommand</code>, etc. See <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1).</dl>
<p> &#8211;single-worktree</p>
<dl>
<dt>
<dd> By default, all working trees will be examined by the following options when there are more than one (see <code><a href="/docs/linux/man/1-git-worktree/">git-worktree</a></code>(1)): <code>&#8211;all</code>, <code>&#8211;reflog</code> and <code>&#8211;indexed-objects</code>. This option forces them to examine the current working tree only.</dl>
<p> &#8211;ignore-missing</p>
<dl>
<dt>
<dd> Upon seeing an invalid object name in the input, pretend as if the bad input was not given.</dl>
<p> &#8211;bisect</p>
<dl>
<dt>
<dd> Pretend as if the bad bisection ref <code>refs/bisect/bad</code> was listed and as if it was followed by <code>&#8211;not</code> and the good bisection refs <code>refs/bisect/good-*</code> on the command line.</dl>
<p> &#8211;stdin</p>
<dl>
<dt>
<dd> In addition to the <i>&lt;commit&gt;</i> listed on the command line, read them from the standard input. If a <code>&#8212;</code> separator is seen, stop reading commits and start reading paths to limit the result.</dl>
<p> &#8211;cherry-mark</p>
<dl>
<dt>
<dd> Like <code>&#8211;cherry-pick</code> (see below) but mark equivalent commits with <code>=</code> rather than omitting them, and inequivalent ones with <code>+</code>.</dl>
<p> &#8211;cherry-pick</p>
<dl>
<dt>
<dd> Omit any commit that introduces the same change as another commit on the &#8220;other side&#8221; when the set of commits are limited with symmetric difference. </p>
<p> For example, if you have two branches, <code>A</code> and <code>B</code>, a usual way to list all commits on only one side of them is with <code>&#8211;left-right</code> (see the example below in the description of the <code>&#8211;left-right</code> option). However, it shows the commits that were cherry-picked from the other branch (for example, &#8220;3rd on b&#8221; may be cherry-picked from branch A). With this option, such pairs of commits are excluded from the output.</dl>
<p> &#8211;left-only, &#8211;right-only</p>
<dl>
<dt>
<dd> List only commits on the respective side of a symmetric difference, i.e. only those which would be marked <code>&lt;</code> resp. <code>&gt;</code> by <code>&#8211;left-right</code>. </p>
<p> For example, <code>&#8211;cherry-pick &#8211;right-only A&#8230;B</code> omits those commits from <code>B</code> which are in <code>A</code> or are patch-equivalent to a commit in <code>A</code>. In other words, this lists the <code>+</code> commits from <code>git cherry A B</code>. More precisely, <code>&#8211;cherry-pick &#8211;right-only &#8211;no-merges</code> gives the exact list.</dl>
<p> &#8211;cherry</p>
<dl>
<dt>
<dd> A synonym for <code>&#8211;right-only &#8211;cherry-mark &#8211;no-merges</code>; useful to limit the output to the commits on our side and mark those that have been applied to the other side of a forked history with <code>git log &#8211;cherry upstream&#8230;mybranch</code>, similar to <code>git cherry upstream mybranch</code>.</dl>
<p> -g, &#8211;walk-reflogs</p>
<dl>
<dt>
<dd> Instead of walking the commit ancestry chain, walk reflog entries from the most recent one to older ones. When this option is used you cannot specify commits to exclude (that is, <i>^commit</i>, <i>commit1..commit2</i>, and <i>commit1&#8230;commit2</i> notations cannot be used). </p>
<p> With <code>&#8211;pretty</code> format other than <code>oneline</code> and <code>reference</code> (for obvious reasons), this causes the output to have two extra lines of information taken from the reflog. The reflog designator in the output may be shown as <code>ref@{Nth}</code> (where <code>Nth</code> is the reverse-chronological index in the reflog) or as <code>ref@{timestamp}</code> (with the timestamp for that entry), depending on a few rules: </p>
<dl>
<dt>
<dd> 1. If the starting point is specified as <code>ref@{Nth}</code>, show the index format.</dl>
<dl>
<dt>
<dd> 2. If the starting point was specified as <code>ref@{now}</code>, show the timestamp format.</dl>
<dl>
<dt>
<dd> 3. If neither was used, but <code>&#8211;date</code> was given on the command line, show the timestamp in the format requested by <code>&#8211;date</code>.</dl>
<dl>
<dt>
<dd> 4. Otherwise, show the index format.</dl>
<p> Under <code>&#8211;pretty=oneline</code>, the commit message is prefixed with this information on the same line. This option cannot be combined with <code>&#8211;reverse</code>. See also <code><a href="/docs/linux/man/1-git-reflog/">git-reflog</a></code>(1). </p>
<p> Under <code>&#8211;pretty=reference</code>, this information will not be shown at all.</dl>
<p> &#8211;merge</p>
<dl>
<dt>
<dd> After a failed merge, show refs that touch files having a conflict and don&#8217;t exist on all heads to merge.</dl>
<p> &#8211;boundary</p>
<dl>
<dt>
<dd> Output excluded boundary commits. Boundary commits are prefixed with <code>&#8211;</code>.</dl>
<h3>History Simplification</h3>
<p> Sometimes you are only interested in parts of the history, for example the commits modifying a particular &lt;path&gt;. But there are two parts of <i>History Simplification</i>, one part is selecting the commits and the other is how to do it, as there are various strategies to simplify the history. </p>
<p> The following options select the commits to be shown: </p>
<p> &lt;paths&gt;</p>
<dl>
<dt>
<dd> Commits modifying the given &lt;paths&gt; are selected.</dl>
<p> &#8211;simplify-by-decoration</p>
<dl>
<dt>
<dd> Commits that are referred by some branch or tag are selected.</dl>
<p> Note that extra commits can be shown to give a meaningful history. </p>
<p> The following options affect the way the simplification is performed: </p>
<p> Default mode</p>
<dl>
<dt>
<dd> Simplifies the history to the simplest history explaining the final state of the tree. Simplest because it prunes some side branches if the end result is the same (i.e. merging branches with the same content)</dl>
<p> &#8211;show-pulls</p>
<dl>
<dt>
<dd> Include all commits from the default mode, but also any merge commits that are not TREESAME to the first parent but are TREESAME to a later parent. This mode is helpful for showing the merge commits that &quot;first introduced&quot; a change to a branch.</dl>
<p> &#8211;full-history</p>
<dl>
<dt>
<dd> Same as the default mode, but does not prune some history.</dl>
<p> &#8211;dense</p>
<dl>
<dt>
<dd> Only the selected commits are shown, plus some to have a meaningful history.</dl>
<p> &#8211;sparse</p>
<dl>
<dt>
<dd> All commits in the simplified history are shown.</dl>
<p> &#8211;simplify-merges</p>
<dl>
<dt>
<dd> Additional option to <code>&#8211;full-history</code> to remove some needless merges from the resulting history, as there are no selected commits contributing to this merge.</dl>
<p> &#8211;ancestry-path</p>
<dl>
<dt>
<dd> When given a range of commits to display (e.g. <i>commit1..commit2</i> or <i>commit2 ^commit1</i>), only display commits that exist directly on the ancestry chain between the <i>commit1</i> and <i>commit2</i>, i.e. commits that are both descendants of <i>commit1</i>, and ancestors of <i>commit2</i>.</dl>
<p> A more detailed explanation follows. </p>
<p> Suppose you specified <code>foo</code> as the &lt;paths&gt;. We shall call commits that modify <code>foo</code> !TREESAME, and the rest TREESAME. (In a diff filtered for <code>foo</code>, they look different and equal, respectively.) </p>
<p> In the following, we will always refer to the same example history to illustrate the differences between simplification settings. We assume that you are filtering for a file <code>foo</code> in this commit graph: </p>
<dl>
<dt>
<dd>
.- A&#8211; &#8211; M&#8211; &#8211; N&#8211; &#8211; O&#8211; &#8211; P&#8211; &#8211; Q / / / / / / I B C D E Y<br />
         \ / / / / /<br />
          `&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; -&#8216;   X
</dl>
<p> The horizontal line of history A&#8212;Q is taken to be the first parent of each merge. The commits are: </p>
<dl>
<dt>
<dd> &bull; <code>I</code> is the initial commit, in which <code>foo</code> exists with contents &#8220;asdf&#8221;, and a file <code>quux</code> exists with contents &#8220;quux&#8221;. Initial commits are compared to an empty tree, so <code>I</code> is !TREESAME.</dl>
<dl>
<dt>
<dd> &bull; In <code>A</code>, <code>foo</code> contains just &#8220;foo&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>B</code> contains the same change as <code>A</code>. Its merge <code>M</code> is trivial and hence TREESAME to all parents.</dl>
<dl>
<dt>
<dd> &bull; <code>C</code> does not change <code>foo</code>, but its merge <code>N</code> changes it to &#8220;foobar&#8221;, so it is not TREESAME to any parent.</dl>
<dl>
<dt>
<dd> &bull; <code>D</code> sets <code>foo</code> to &#8220;baz&#8221;. Its merge <code>O</code> combines the strings from <code>N</code> and <code>D</code> to &#8220;foobarbaz&#8221;; i.e., it is not TREESAME to any parent.</dl>
<dl>
<dt>
<dd> &bull; <code>E</code> changes <code>quux</code> to &#8220;xyzzy&#8221;, and its merge <code>P</code> combines the strings to &#8220;quux xyzzy&#8221;. <code>P</code> is TREESAME to <code>O</code>, but not to <code>E</code>.</dl>
<dl>
<dt>
<dd> &bull; <code>X</code> is an independent root commit that added a new file <code>side</code>, and <code>Y</code> modified it. <code>Y</code> is TREESAME to <code>X</code>. Its merge <code>Q</code> added <code>side</code> to <code>P</code>, and <code>Q</code> is TREESAME to <code>P</code>, but not to <code>Y</code>.</dl>
<p> <code>rev-list</code> walks backwards through history, including or excluding commits based on whether <code>&#8211;full-history</code> and/or parent rewriting (via <code>&#8211;parents</code> or <code>&#8211;children</code>) are used. The following settings are available. </p>
<p> Default mode</p>
<dl>
<dt>
<dd> Commits are included if they are not TREESAME to any parent (though this can be changed, see <code>&#8211;sparse</code> below). If the commit was a merge, and it was TREESAME to one parent, follow only that parent. (Even if there are several TREESAME parents, follow only one of them.) Otherwise, follow all parents. </p>
<p> This results in: </p>
<dl>
<dt>
<dd>
.- A&#8211; &#8211; N&#8211; &#8211; O / / / I&#8211; &#8212; &#8212; &#8212; -D
</dl>
<p> Note how the rule to only follow the TREESAME parent, if one is available, removed <code>B</code> from consideration entirely. <code>C</code> was considered via <code>N</code>, but is TREESAME. Root commits are compared to an empty tree, so <code>I</code> is !TREESAME. </p>
<p> Parent/child relations are only visible with <code>&#8211;parents</code>, but that does not affect the commits selected in default mode, so we have shown the parent lines.</dl>
<p> &#8211;full-history without parent rewriting</p>
<dl>
<dt>
<dd> This mode differs from the default in one point: always follow all parents of a merge, even if it is TREESAME to one of them. Even if more than one side of the merge has commits that are included, this does not imply that the merge itself is! In the example, we get </p>
<dl>
<dt>
<dd>
<pre>
        I  A  B  N  D  O  P  Q
</pre>
</dl>
<p> <code>M</code> was excluded because it is TREESAME to both parents. <code>E</code>, <code>C</code> and <code>B</code> were all walked, but only <code>B</code> was !TREESAME, so the others do not appear. </p>
<p> Note that without parent rewriting, it is not really possible to talk about the parent/child relationships between the commits, so we show them disconnected.</dl>
<p> &#8211;full-history with parent rewriting</p>
<dl>
<dt>
<dd> Ordinary commits are only included if they are !TREESAME (though this can be changed, see <code>&#8211;sparse</code> below). </p>
<p> Merges are always included. However, their parent list is rewritten: Along each parent, prune away commits that are not included themselves. This results in </p>
<dl>
<dt>
<dd>
.- A&#8211; &#8211; M&#8211; &#8211; N&#8211; &#8211; O&#8211; &#8211; P&#8211; &#8211; Q / / / / / I B / D /<br />
         \ / / / /<br />
          `&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; -&#8216;
</dl>
<p> Compare to <code>&#8211;full-history</code> without rewriting above. Note that <code>E</code> was pruned away because it is TREESAME, but the parent list of P was rewritten to contain <code>E</code>&#8216;s parent <code>I</code>. The same happened for <code>C</code> and <code>N</code>, and <code>X</code>, <code>Y</code> and <code>Q</code>.</dl>
<p> In addition to the above settings, you can change whether TREESAME affects inclusion: </p>
<p> &#8211;dense</p>
<dl>
<dt>
<dd> Commits that are walked are included if they are not TREESAME to any parent.</dl>
<p> &#8211;sparse</p>
<dl>
<dt>
<dd> All commits that are walked are included. </p>
<p> Note that without <code>&#8211;full-history</code>, this still simplifies merges: if one of the parents is TREESAME, we follow only that one, so the other sides of the merge are never walked.</dl>
<p> &#8211;simplify-merges</p>
<dl>
<dt>
<dd> First, build a history graph in the same way that <code>&#8211;full-history</code> with parent rewriting does (see above). </p>
<p> Then simplify each commit <code>C</code> to its replacement <code>C&#8217;</code> in the final history according to the following rules: </p>
<dl>
<dt>
<dd> &bull; Set <code>C&#8217;</code> to <code>C</code>.</dl>
<dl>
<dt>
<dd> &bull; Replace each parent <code>P</code> of <code>C&#8217;</code> with its simplification <code>P&#8217;</code>. In the process, drop parents that are ancestors of other parents or that are root commits TREESAME to an empty tree, and remove duplicates, but take care to never drop all parents that we are TREESAME to.</dl>
<dl>
<dt>
<dd> &bull; If after this parent rewriting, <code>C&#8217;</code> is a root or merge commit (has zero or &gt;1 parents), a boundary commit, or !TREESAME, it remains. Otherwise, it is replaced with its only parent.</dl>
<p> The effect of this is best shown by way of comparing to <code>&#8211;full-history</code> with parent rewriting. The example turns into: </p>
<dl>
<dt>
<dd>
.- A&#8211; &#8211; M&#8211; &#8211; N&#8211; &#8211; O / / / I B D<br />
         \ / /<br />
          `&#8211; &#8212; &#8212; &#8212; -&#8216;
</dl>
<p> Note the major differences in <code>N</code>, <code>P</code>, and <code>Q</code> over <code>&#8211;full-history</code>: </p>
<dl>
<dt>
<dd> &bull; <code>N</code>&#8216;s parent list had <code>I</code> removed, because it is an ancestor of the other parent <code>M</code>. Still, <code>N</code> remained because it is !TREESAME.</dl>
<dl>
<dt>
<dd> &bull; <code>P</code>&#8216;s parent list similarly had <code>I</code> removed. <code>P</code> was then removed completely, because it had one parent and is TREESAME.</dl>
<dl>
<dt>
<dd> &bull; <code>Q</code>&#8216;s parent list had <code>Y</code> simplified to <code>X</code>. <code>X</code> was then removed, because it was a TREESAME root. <code>Q</code> was then removed completely, because it had one parent and is TREESAME.</dl>
</dl>
<p> There is another simplification mode available: </p>
<p> &#8211;ancestry-path</p>
<dl>
<dt>
<dd> Limit the displayed commits to those directly on the ancestry chain between the &#8220;from&#8221; and &#8220;to&#8221; commits in the given commit range. I.e. only display commits that are ancestor of the &#8220;to&#8221; commit and descendants of the &#8220;from&#8221; commit. </p>
<p> As an example use case, consider the following commit history: </p>
<dl>
<dt>
<dd>
D&#8211; &#8211; E&#8211; &#8212; &#8212; -F /     \ B&#8211; &#8211; C&#8211; &#8211; G&#8211; &#8211; H&#8211; &#8211; I&#8211; &#8211; J / A&#8211; &#8212; &#8212; -K&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -L&#8211; M
</dl>
<p> A regular <i>D..M</i> computes the set of commits that are ancestors of <code>M</code>, but excludes the ones that are ancestors of <code>D</code>. This is useful to see what happened to the history leading to <code>M</code> since <code>D</code>, in the sense that &#8220;what does <code>M</code> have that did not exist in <code>D</code>&#8220;. The result in this example would be all the commits, except <code>A</code> and <code>B</code> (and <code>D</code> itself, of course). </p>
<p> When we want to find out what commits in <code>M</code> are contaminated with the bug introduced by <code>D</code> and need fixing, however, we might want to view only the subset of <i>D..M</i> that are actually descendants of <code>D</code>, i.e. excluding <code>C</code> and <code>K</code>. This is exactly what the <code>&#8211;ancestry-path</code> option does. Applied to the <i>D..M</i> range, it results in: </p>
<dl>
<dt>
<dd>
E&#8211; &#8212; &#8212; -F<br />
                 \ G&#8211; &#8211; H&#8211; &#8211; I&#8211; &#8211; J</p>
<p>                                          L&#8211; M
</dl>
</dl>
<p> Before discussing another option, <code>&#8211;show-pulls</code>, we need to create a new example history. </p>
<p> A common problem users face when looking at simplified history is that a commit they know changed a file somehow does not appear in the file&#8217;s simplified history. Let&#8217;s demonstrate a new example and show how options such as <code>&#8211;full-history</code> and <code>&#8211;simplify-merges</code> works in that case: </p>
<dl>
<dt>
<dd>
.- A&#8211; &#8211; M&#8211; &#8212; -C&#8211; N&#8211; &#8211; O&#8211; &#8211; P / / \  \  \/ / / I B   \ R &#8211; &#8216;`-Z&#8217; /<br />
         \ /     \/ /<br />
          \ / /\ /<br />
           `&#8211; -X&#8211; &#8216;  `&#8212;Y&#8211;&#8216;
</dl>
<p> For this example, suppose <code>I</code> created <code>file.txt</code> which was modified by <code>A</code>, <code>B</code>, and <code>X</code> in different ways. The single-parent commits <code>C</code>, <code>Z</code>, and <code>Y</code> do not change <code>file.txt</code>. The merge commit <code>M</code> was created by resolving the merge conflict to include both changes from <code>A</code> and <code>B</code> and hence is not TREESAME to either. The merge commit <code>R</code>, however, was created by ignoring the contents of <code>file.txt</code> at <code>M</code> and taking only the contents of <code>file.txt</code> at <code>X</code>. Hence, <code>R</code> is TREESAME to <code>X</code> but not <code>M</code>. Finally, the natural merge resolution to create <code>N</code> is to take the contents of <code>file.txt</code> at <code>R</code>, so <code>N</code> is TREESAME to <code>R</code> but not <code>C</code>. The merge commits <code>O</code> and <code>P</code> are TREESAME to their first parents, but not to their second parents, <code>Z</code> and <code>Y</code> respectively. </p>
<p> When using the default mode, <code>N</code> and <code>R</code> both have a TREESAME parent, so those edges are walked and the others are ignored. The resulting history graph is: </p>
<dl>
<dt>
<dd>
<pre>
        I---X
</pre>
</dl>
<p> When using <code>&#8211;full-history</code>, Git walks every edge. This will discover the commits <code>A</code> and <code>B</code> and the merge <code>M</code>, but also will reveal the merge commits <code>O</code> and <code>P</code>. With parent rewriting, the resulting graph is: </p>
<dl>
<dt>
<dd>
.- A&#8211; &#8211; M&#8211; &#8212; &#8212; &#8211;N&#8211; &#8211; O&#8211; &#8211; P / / \  \  \/ / / I B   \ R &#8211; &#8216;`&#8211;&#8216; /<br />
         \ /     \/ /<br />
          \ / /\ /<br />
           `&#8211; -X&#8211; &#8216;  `&#8212;&#8212;&#8216;
</dl>
<p> Here, the merge commits <code>O</code> and <code>P</code> contribute extra noise, as they did not actually contribute a change to <code>file.txt</code>. They only merged a topic that was based on an older version of <code>file.txt</code>. This is a common issue in repositories using a workflow where many contributors work in parallel and merge their topic branches along a single trunk: manu unrelated merges appear in the <code>&#8211;full-history</code> results. </p>
<p> When using the <code>&#8211;simplify-merges</code> option, the commits <code>O</code> and <code>P</code> disappear from the results. This is because the rewritten second parents of <code>O</code> and <code>P</code> are reachable from their first parents. Those edges are removed and then the commits look like single-parent commits that are TREESAME to their parent. This also happens to the commit <code>N</code>, resulting in a history view as follows: </p>
<dl>
<dt>
<dd>
.- A&#8211; &#8211; M&#8211;./ / I B R<br />
         \ / /<br />
          \ / /<br />
           `&#8211; -X&#8211;&#8216;
</dl>
<p> In this view, we see all of the important single-parent changes from <code>A</code>, <code>B</code>, and <code>X</code>. We also see the carefully-resolved merge <code>M</code> and the not-so-carefully-resolved merge <code>R</code>. This is usually enough information to determine why the commits <code>A</code> and <code>B</code> &quot;disappeared&quot; from history in the default view. However, there are a few issues with this approach. </p>
<p> The first issue is performance. Unlike any previous option, the <code>&#8211;simplify-merges</code> option requires walking the entire commit history before returning a single result. This can make the option difficult to use for very large repositories. </p>
<p> The second issue is one of auditing. When many contributors are working on the same repository, it is important which merge commits introduced a change into an important branch. The problematic merge <code>R</code> above is not likely to be the merge commit that was used to merge into an important branch. Instead, the merge <code>N</code> was used to merge <code>R</code> and <code>X</code> into the important branch. This commit may have information about why the change <code>X</code> came to override the changes from <code>A</code> and <code>B</code> in its commit message. </p>
<p> &#8211;show-pulls</p>
<dl>
<dt>
<dd> In addition to the commits shown in the default history, show each merge commit that is not TREESAME to its first parent but is TREESAME to a later parent. </p>
<p> When a merge commit is included by <code>&#8211;show-pulls</code>, the merge is treated as if it &quot;pulled&quot; the change from another branch. When using <code>&#8211;show-pulls</code> on this example (and no other options) the resulting graph is: </p>
<dl>
<dt>
<dd>
<pre>
        I---X---R---N
</pre>
</dl>
<p> Here, the merge commits <code>R</code> and <code>N</code> are included because they pulled the commits <code>X</code> and <code>R</code> into the base branch, respectively. These merges are the reason the commits <code>A</code> and <code>B</code> do not appear in the default history. </p>
<p> When <code>&#8211;show-pulls</code> is paired with <code>&#8211;simplify-merges</code>, the graph includes all of the necessary information: </p>
<dl>
<dt>
<dd>
.- A&#8211; &#8211; M&#8211;.N / /    \ / I B R<br />
         \ / /<br />
          \ / /<br />
           `&#8211; -X&#8211;&#8216;
</dl>
<p> Notice that since <code>M</code> is reachable from <code>R</code>, the edge from <code>N</code> to <code>M</code> was simplified away. However, <code>N</code> still appears in the history as an important commit because it &quot;pulled&quot; the change <code>R</code> into the main branch.</dl>
<p> The <code>&#8211;simplify-by-decoration</code> option allows you to view only the big picture of the topology of the history, by omitting commits that are not referenced by tags. Commits are marked as !TREESAME (in other words, kept after history simplification rules described above) if (1) they are referenced by tags, or (2) they change the contents of the paths given on the command line. All other commits are marked as TREESAME (subject to be simplified away).</p>
<h3>Commit Ordering</h3>
<p> By default, the commits are shown in reverse chronological order. </p>
<p> &#8211;date-order</p>
<dl>
<dt>
<dd> Show no parents before all of its children are shown, but otherwise show commits in the commit timestamp order.</dl>
<p> &#8211;author-date-order</p>
<dl>
<dt>
<dd> Show no parents before all of its children are shown, but otherwise show commits in the author timestamp order.</dl>
<p> &#8211;topo-order</p>
<dl>
<dt>
<dd> Show no parents before all of its children are shown, and avoid showing commits on multiple lines of history intermixed. </p>
<p> For example, in a commit history like this: </p>
<dl>
<dt>
<dd>
&#8212; -1 &#8212; &#8211;2 &#8212; &#8211;4 &#8212; &#8211;7<br />
        \ 3 &#8212; &#8211;5 &#8212; &#8211;6 &#8212; &#8211;8 &#8212; &#8211;
</dl>
<p> where the numbers denote the order of commit timestamps, <code>git rev-list</code> and friends with <code>&#8211;date-order</code> show the commits in the timestamp order: 8 7 6 5 4 3 2 1. </p>
<p> With <code>&#8211;topo-order</code>, they would show 8 6 5 3 7 4 2 1 (or 8 7 4 2 6 5 3 1); some older commits are shown before newer ones in order to avoid showing the commits from two parallel development track mixed together.</dl>
<p> &#8211;reverse</p>
<dl>
<dt>
<dd> Output the commits chosen to be shown (see Commit Limiting section above) in reverse order. Cannot be combined with <code>&#8211;walk-reflogs</code>.</dl>
<h3>Object Traversal</h3>
<p> These options are mostly targeted for packing of Git repositories. </p>
<p> &#8211;no-walk[=(sorted|unsorted)]</p>
<dl>
<dt>
<dd> Only show the given commits, but do not traverse their ancestors. This has no effect if a range is specified. If the argument <code>unsorted</code> is given, the commits are shown in the order they were given on the command line. Otherwise (if <code>sorted</code> or no argument was given), the commits are shown in reverse chronological order by commit time. Cannot be combined with <code>&#8211;graph</code>.</dl>
<p> &#8211;do-walk</p>
<dl>
<dt>
<dd> Overrides a previous <code>&#8211;no-walk</code>.</dl>
<h3>Commit Formatting</h3>
<p> &#8211;pretty[=&lt;format&gt;], &#8211;format=&lt;format&gt;</p>
<dl>
<dt>
<dd> Pretty-print the contents of the commit logs in a given format, where <i>&lt;format&gt;</i> can be one of <i>oneline</i>, <i>short</i>, <i>medium</i>, <i>full</i>, <i>fuller</i>, <i>reference</i>, <i>email</i>, <i>raw</i>, <i>format:&lt;string&gt;</i> and <i>tformat:&lt;string&gt;</i>. When <i>&lt;format&gt;</i> is none of the above, and has <i>%placeholder</i> in it, it acts as if <i>&#8211;pretty=tformat:&lt;format&gt;</i> were given. </p>
<p> See the &quot;PRETTY FORMATS&quot; section for some additional details for each format. When <i>=&lt;format&gt;</i> part is omitted, it defaults to <i>medium</i>. </p>
<p> Note: you can specify the default pretty format in the repository configuration (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)).</dl>
<p> &#8211;abbrev-commit</p>
<dl>
<dt>
<dd> Instead of showing the full 40-byte hexadecimal commit object name, show a prefix that names the object uniquely. &quot;&#8211;abbrev=&lt;n&gt;&quot; (which also modifies diff output, if it is displayed) option can be used to specify the minimum length of the prefix. </p>
<p> This should make &quot;&#8211;pretty=oneline&quot; a whole lot more readable for people using 80-column terminals.</dl>
<p> &#8211;no-abbrev-commit</p>
<dl>
<dt>
<dd> Show the full 40-byte hexadecimal commit object name. This negates <code>&#8211;abbrev-commit</code>, either explicit or implied by other options such as &quot;&#8211;oneline&quot;. It also overrides the <code>log.abbrevCommit</code> variable.</dl>
<p> &#8211;oneline</p>
<dl>
<dt>
<dd> This is a shorthand for &quot;&#8211;pretty=oneline &#8211;abbrev-commit&quot; used together.</dl>
<p> &#8211;encoding=&lt;encoding&gt;</p>
<dl>
<dt>
<dd> Commit objects record the character encoding used for the log message in their encoding header; this option can be used to tell the command to re-code the commit log message in the encoding preferred by the user. For non plumbing commands this defaults to UTF-8. Note that if an object claims to be encoded in <code>X</code> and we are outputting in <code>X</code>, we will output the object verbatim; this means that invalid sequences in the original commit may be copied to the output. Likewise, if <a href="/docs/linux/man/3-iconv/">iconv</a>(3) fails to convert the commit, we will quietly output the original object verbatim.</dl>
<p> &#8211;expand-tabs=&lt;n&gt;, &#8211;expand-tabs, &#8211;no-expand-tabs</p>
<dl>
<dt>
<dd> Perform a tab expansion (replace each tab with enough spaces to fill to the next display column that is multiple of <i>&lt;n&gt;</i>) in the log message before showing it in the output. <code>&#8211;expand-tabs</code> is a short-hand for <code>&#8211;expand-tabs=8</code>, and <code>&#8211;no-expand-tabs</code> is a short-hand for <code>&#8211;expand-tabs=0</code>, which disables tab expansion. </p>
<p> By default, tabs are expanded in pretty formats that indent the log message by 4 spaces (i.e. <i>medium</i>, which is the default, <i>full</i>, and <i>fuller</i>).</dl>
<p> &#8211;notes[=&lt;ref&gt;]</p>
<dl>
<dt>
<dd> Show the notes (see <code><a href="/docs/linux/man/1-git-notes/">git-notes</a></code>(1)) that annotate the commit, when showing the commit log message. This is the default for <code>git log</code>, <code>git show</code> and <code>git whatchanged</code> commands when there is no <code>&#8211;pretty</code>, <code>&#8211;format</code>, or <code>&#8211;oneline</code> option given on the command line. </p>
<p> By default, the notes shown are from the notes refs listed in the <code>core.notesRef</code> and <code>notes.displayRef</code> variables (or corresponding environment overrides). See <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1) for more details. </p>
<p> With an optional <i>&lt;ref&gt;</i> argument, use the ref to find the notes to display. The ref can specify the full refname when it begins with <code>refs/notes/</code>; when it begins with <code>notes/</code>, <code>refs/</code> and otherwise <code>refs/notes/</code> is prefixed to form a full name of the ref. </p>
<p> Multiple &#8211;notes options can be combined to control which notes are being displayed. Examples: &quot;&#8211;notes=foo&quot; will show only notes from &quot;refs/notes/foo&quot;; &quot;&#8211;notes=foo &#8211;notes&quot; will show both notes from &quot;refs/notes/foo&quot; and from the default notes ref(s).</dl>
<p> &#8211;no-notes</p>
<dl>
<dt>
<dd> Do not show notes. This negates the above <code>&#8211;notes</code> option, by resetting the list of notes refs from which notes are shown. Options are parsed in the order given on the command line, so e.g. &quot;&#8211;notes &#8211;notes=foo &#8211;no-notes &#8211;notes=bar&quot; will only show notes from &quot;refs/notes/bar&quot;.</dl>
<p> &#8211;show-notes[=&lt;ref&gt;], &#8211;[no-]standard-notes</p>
<dl>
<dt>
<dd> These options are deprecated. Use the above &#8211;notes/&#8211;no-notes options instead.</dl>
<p> &#8211;show-signature</p>
<dl>
<dt>
<dd> Check the validity of a signed commit object by passing the signature to <code>gpg &#8211;verify</code> and show the output.</dl>
<p> &#8211;relative-date</p>
<dl>
<dt>
<dd> Synonym for <code>&#8211;date=relative</code>.</dl>
<p> &#8211;date=&lt;format&gt;</p>
<dl>
<dt>
<dd> Only takes effect for dates shown in human-readable format, such as when using <code>&#8211;pretty</code>. <code>log.date</code> config variable sets a default value for the log command&#8217;s <code>&#8211;date</code> option. By default, dates are shown in the original time zone (either committer&#8217;s or author&#8217;s). If <code>-local</code> is appended to the format (e.g., <code>iso-local</code>), the user&#8217;s local time zone is used instead. </p>
<p> <code>&#8211;date=relative</code> shows dates relative to the current time, e.g. &#8220;2 hours ago&#8221;. The <code>-local</code> option has no effect for <code>&#8211;date=relative</code>. </p>
<p> <code>&#8211;date=local</code> is an alias for <code>&#8211;date=default-local</code>. </p>
<p> <code>&#8211;date=iso</code> (or <code>&#8211;date=iso8601</code>) shows timestamps in a ISO 8601-like format. The differences to the strict ISO 8601 format are: </p>
<dl>
<dt>
<dd> &bull; a space instead of the <code>T</code> date/time delimiter</dl>
<dl>
<dt>
<dd> &bull; a space between time and time zone</dl>
<dl>
<dt>
<dd> &bull; no colon between hours and minutes of the time zone</dl>
<p> <code>&#8211;date=iso-strict</code> (or <code>&#8211;date=iso8601-strict</code>) shows timestamps in strict ISO 8601 format. </p>
<p> <code>&#8211;date=rfc</code> (or <code>&#8211;date=rfc2822</code>) shows timestamps in RFC 2822 format, often found in email messages. </p>
<p> <code>&#8211;date=short</code> shows only the date, but not the time, in <code>YYYY-MM-DD</code> format. </p>
<p> <code>&#8211;date=raw</code> shows the date as seconds since the epoch (1970-01-01 00:00:00 UTC), followed by a space, and then the timezone as an offset from UTC (a <code>+</code> or <code>&#8211;</code> with four digits; the first two are hours, and the second two are minutes). I.e., as if the timestamp were formatted with <code>strftime(&quot;%s %z&quot;)</code>). Note that the <code>-local</code> option does not affect the seconds-since-epoch value (which is always measured in UTC), but does switch the accompanying timezone value. </p>
<p> <code>&#8211;date=human</code> shows the timezone if the timezone does not match the current time-zone, and doesn&#8217;t print the whole date if that matches (ie skip printing year for dates that are &quot;this year&quot;, but also skip the whole date itself if it&#8217;s in the last few days and we can just say what weekday it was). For older dates the hour and minute is also omitted. </p>
<p> <code>&#8211;date=unix</code> shows the date as a Unix epoch timestamp (seconds since 1970). As with <code>&#8211;raw</code>, this is always in UTC and therefore <code>-local</code> has no effect. </p>
<p> <code>&#8211;date=format:&#8230;</code> feeds the format <code>&#8230;</code> to your system <code>strftime</code>, except for %z and %Z, which are handled internally. Use <code>&#8211;date=format:%c</code> to show the date in your system locale&#8217;s preferred format. See the <code>strftime</code> manual for a complete list of format placeholders. When using <code>-local</code>, the correct syntax is <code>&#8211;date=format-local:&#8230;</code>. </p>
<p> <code>&#8211;date=default</code> is the default format, and is similar to <code>&#8211;date=rfc2822</code>, with a few exceptions: </p>
<dl>
<dt>
<dd> &bull; there is no comma after the day-of-week</dl>
<dl>
<dt>
<dd> &bull; the time zone is omitted when the local time zone is used</dl>
</dl>
<p> &#8211;parents</p>
<dl>
<dt>
<dd> Print also the parents of the commit (in the form &quot;commit parent&#8230;&quot;). Also enables parent rewriting, see <i>History Simplification</i> above.</dl>
<p> &#8211;children</p>
<dl>
<dt>
<dd> Print also the children of the commit (in the form &quot;commit child&#8230;&quot;). Also enables parent rewriting, see <i>History Simplification</i> above.</dl>
<p> &#8211;left-right</p>
<dl>
<dt>
<dd> Mark which side of a symmetric difference a commit is reachable from. Commits from the left side are prefixed with <code>&lt;</code> and those from the right with <code>&gt;</code>. If combined with <code>&#8211;boundary</code>, those commits are prefixed with <code>&#8211;</code>. </p>
<p> For example, if you have this topology: </p>
<dl>
<dt>
<dd>
y&#8211; &#8211; b&#8211; &#8211; b branch B / \ / /./ / o&#8211; &#8211; x&#8211; &#8211; a&#8211; &#8211; a branch A
</dl>
<p> you would get an output like this: </p>
<dl>
<dt>
<dd>
<pre>
        $ git rev-list --left-right --boundary --pretty=oneline A...B
        &gt;bbbbbbb... 3rd on b
        &gt;bbbbbbb... 2nd on b
        &lt;aaaaaaa... 3rd on a
        &lt;aaaaaaa... 2nd on a
        -yyyyyyy... 1st on b
        -xxxxxxx... 1st on a
</pre>
</dl>
</dl>
<p> &#8211;graph</p>
<dl>
<dt>
<dd> Draw a text-based graphical representation of the commit history on the left hand side of the output. This may cause extra lines to be printed in between commits, in order for the graph history to be drawn properly. Cannot be combined with <code>&#8211;no-walk</code>. </p>
<p> This enables parent rewriting, see <i>History Simplification</i> above. </p>
<p> This implies the <code>&#8211;topo-order</code> option by default, but the <code>&#8211;date-order</code> option may also be specified.</dl>
<p> &#8211;show-linear-break[=&lt;barrier&gt;]</p>
<dl>
<dt>
<dd> When &#8211;graph is not used, all history branches are flattened which can make it hard to see that the two consecutive commits do not belong to a linear branch. This option puts a barrier in between them in that case. If <code>&lt;barrier&gt;</code> is specified, it is the string that will be shown instead of the default one.</dl>
<h2>PRETTY FORMATS</h2>
<p> If the commit is a merge, and if the pretty-format is not <i>oneline</i>, <i>email</i> or <i>raw</i>, an additional line is inserted before the <i>Author:</i> line. This line begins with &quot;Merge: &quot; and the hashes of ancestral commits are printed, separated by spaces. Note that the listed commits may not necessarily be the list of the <code>direct</code> parent commits if you have limited your view of history: for example, if you are only interested in changes related to a certain directory or file. </p>
<p> There are several built-in formats, and you can define additional formats by setting a pretty.&lt;name&gt; config option to either another format name, or a <i>format:</i> string, as described below (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)). Here are the details of the built-in formats: </p>
<dl>
<dt>
<dd> &bull; <i>oneline</i> </p>
<dl>
<dt>
<dd>
<pre>
&lt;hash&gt; &lt;title line&gt;
</pre>
</dl>
<p> This is designed to be as compact as possible.</dl>
<dl>
<dt>
<dd> &bull; <i>short</i> </p>
<dl>
<dt>
<dd>
<pre>
commit &lt;hash&gt;
Author: &lt;author&gt;
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
&lt;title line&gt;
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <i>medium</i> </p>
<dl>
<dt>
<dd>
<pre>
commit &lt;hash&gt;
Author: &lt;author&gt;
Date:   &lt;author date&gt;
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
&lt;title line&gt;
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
&lt;full commit message&gt;
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <i>full</i> </p>
<dl>
<dt>
<dd>
<pre>
commit &lt;hash&gt;
Author: &lt;author&gt;
Commit: &lt;committer&gt;
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
&lt;title line&gt;
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
&lt;full commit message&gt;
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <i>fuller</i> </p>
<dl>
<dt>
<dd>
<pre>
commit &lt;hash&gt;
Author:     &lt;author&gt;
AuthorDate: &lt;author date&gt;
Commit:     &lt;committer&gt;
CommitDate: &lt;committer date&gt;
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
&lt;title line&gt;
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
&lt;full commit message&gt;
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <i>reference</i> </p>
<dl>
<dt>
<dd>
<pre>
&lt;abbrev hash&gt; (&lt;title line&gt;, &lt;short author date&gt;)
</pre>
</dl>
<p> This format is used to refer to another commit in a commit message and is the same as <code>&#8211;pretty=&#8217;format:%C(auto)%h (%s, %ad)&#8217;</code>. By default, the date is formatted with <code>&#8211;date=short</code> unless another <code>&#8211;date</code> option is explicitly specified. As with any <code>format:</code> with format placeholders, its output is not affected by other options like <code>&#8211;decorate</code> and <code>&#8211;walk-reflogs</code>.</dl>
<dl>
<dt>
<dd> &bull; <i>email</i> </p>
<dl>
<dt>
<dd>
<pre>
From &lt;hash&gt; &lt;date&gt;
From: &lt;author&gt;
Date: &lt;author date&gt;
Subject: [PATCH] &lt;title line&gt;
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
&lt;full commit message&gt;
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <i>mboxrd</i> </p>
<p> Like <i>email</i>, but lines in the commit message starting with &quot;From &quot; (preceded by zero or more &quot;&gt;&quot;) are quoted with &quot;&gt;&quot; so they aren&#8217;t confused as starting a new commit.</dl>
<dl>
<dt>
<dd> &bull; <i>raw</i> </p>
<p> The <i>raw</i> format shows the entire commit exactly as stored in the commit object. Notably, the hashes are displayed in full, regardless of whether &#8211;abbrev or &#8211;no-abbrev are used, and <i>parents</i> information show the true parent commits, without taking grafts or history simplification into account. Note that this format affects the way commits are displayed, but not the way the diff is shown e.g. with <code>git log &#8211;raw</code>. To get full object names in a raw diff format, use <code>&#8211;no-abbrev</code>.</dl>
<dl>
<dt>
<dd> &bull; <i>format:&lt;string&gt;</i> </p>
<p> The <i>format:&lt;string&gt;</i> format allows you to specify which information you want to show. It works a little bit like printf format, with the notable exception that you get a newline with <i>%n</i> instead of <i>
</i>. </p>
<p> E.g, <i>format:&quot;The author of %h was %an, %ar%nThe title was &gt;&gt;%s&lt;&lt;%n&quot;</i> would show something like this: </p>
<dl>
<dt>
<dd>
<pre>
The author of fe6e0ee was Junio C Hamano, 23 hours ago
The title was &gt;&gt;t4119: test autocomputing -p&lt;n&gt; for traditional diff input.&lt;&lt;
</pre>
</dl>
<p> The placeholders are: </p>
<dl>
<dt>
<dd> &bull; Placeholders that expand to a single literal character: </p>
<p> <i>%n</i></p>
<dl>
<dt>
<dd> newline</dl>
<p> <i>%%</i></p>
<dl>
<dt>
<dd> a raw <i>%</i></dl>
<p> <i>%x00</i></p>
<dl>
<dt>
<dd> print a byte from a hex code</dl>
</dl>
<dl>
<dt>
<dd> &bull; Placeholders that affect formatting of later placeholders: </p>
<p> <i>%Cred</i></p>
<dl>
<dt>
<dd> switch color to red</dl>
<p> <i>%Cgreen</i></p>
<dl>
<dt>
<dd> switch color to green</dl>
<p> <i>%Cblue</i></p>
<dl>
<dt>
<dd> switch color to blue</dl>
<p> <i>%Creset</i></p>
<dl>
<dt>
<dd> reset color</dl>
<p> <i>%C(&#8230;)</i></p>
<dl>
<dt>
<dd> color specification, as described under Values in the &quot;CONFIGURATION FILE&quot; section of <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1). By default, colors are shown only when enabled for log output (by <code>color.diff</code>, <code>color.ui</code>, or <code>&#8211;color</code>, and respecting the <code>auto</code> settings of the former if we are going to a terminal). <code>%C(auto,&#8230;)</code> is accepted as a historical synonym for the default (e.g., <code>%C(auto,red)</code>). Specifying <code>%C(always,&#8230;)</code> will show the colors even when color is not otherwise enabled (though consider just using <code>&#8211;color=always</code> to enable color for the whole output, including this format and anything else git might color). <code>auto</code> alone (i.e. <code>%C(auto)</code>) will turn on auto coloring on the next placeholders until the color is switched again.</dl>
<p> <i>%m</i></p>
<dl>
<dt>
<dd> left (<code>&lt;</code>), right (<code>&gt;</code>) or boundary (<code>&#8211;</code>) mark</dl>
<p> <i>%w([&lt;w&gt;[,&lt;i1&gt;[,&lt;i2&gt;]]])</i></p>
<dl>
<dt>
<dd> switch line wrapping, like the -w option of <code><a href="/docs/linux/man/1-git-shortlog/">git-shortlog</a></code>(1).</dl>
<p> <i>%&lt;(&lt;N&gt;[,trunc|ltrunc|mtrunc])</i></p>
<dl>
<dt>
<dd> make the next placeholder take at least N columns, padding spaces on the right if necessary. Optionally truncate at the beginning (ltrunc), the middle (mtrunc) or the end (trunc) if the output is longer than N columns. Note that truncating only works correctly with N &gt;= 2.</dl>
<p> <i>%&lt;|(&lt;N&gt;)</i></p>
<dl>
<dt>
<dd> make the next placeholder take at least until Nth columns, padding spaces on the right if necessary</dl>
<p> <i>%&gt;(&lt;N&gt;)</i>, <i>%&gt;|(&lt;N&gt;)</i></p>
<dl>
<dt>
<dd> similar to <i>%&lt;(&lt;N&gt;)</i>, <i>%&lt;|(&lt;N&gt;)</i> respectively, but padding spaces on the left</dl>
<p> <i>%&gt;&gt;(&lt;N&gt;)</i>, <i>%&gt;&gt;|(&lt;N&gt;)</i></p>
<dl>
<dt>
<dd> similar to <i>%&gt;(&lt;N&gt;)</i>, <i>%&gt;|(&lt;N&gt;)</i> respectively, except that if the next placeholder takes more spaces than given and there are spaces on its left, use those spaces</dl>
<p> <i>%&gt;&lt;(&lt;N&gt;)</i>, <i>%&gt;&lt;|(&lt;N&gt;)</i></p>
<dl>
<dt>
<dd> similar to <i>%&lt;(&lt;N&gt;)</i>, <i>%&lt;|(&lt;N&gt;)</i> respectively, but padding both sides (i.e. the text is centered)</dl>
</dl>
<dl>
<dt>
<dd> &bull; Placeholders that expand to information extracted from the commit: </p>
<p> <i>%H</i></p>
<dl>
<dt>
<dd> commit hash</dl>
<p> <i>%h</i></p>
<dl>
<dt>
<dd> abbreviated commit hash</dl>
<p> <i>%T</i></p>
<dl>
<dt>
<dd> tree hash</dl>
<p> <i>%t</i></p>
<dl>
<dt>
<dd> abbreviated tree hash</dl>
<p> <i>%P</i></p>
<dl>
<dt>
<dd> parent hashes</dl>
<p> <i>%p</i></p>
<dl>
<dt>
<dd> abbreviated parent hashes</dl>
<p> <i>%an</i></p>
<dl>
<dt>
<dd> author name</dl>
<p> <i>%aN</i></p>
<dl>
<dt>
<dd> author name (respecting .mailmap, see <code><a href="/docs/linux/man/1-git-shortlog/">git-shortlog</a></code>(1) or <code><a href="/docs/linux/man/1-git-blame/">git-blame</a></code>(1))</dl>
<p> <i>%ae</i></p>
<dl>
<dt>
<dd> author email</dl>
<p> <i>%aE</i></p>
<dl>
<dt>
<dd> author email (respecting .mailmap, see <code><a href="/docs/linux/man/1-git-shortlog/">git-shortlog</a></code>(1) or <code><a href="/docs/linux/man/1-git-blame/">git-blame</a></code>(1))</dl>
<p> <i>%al</i></p>
<dl>
<dt>
<dd> author email local-part (the part before the <i>@</i> sign)</dl>
<p> <i>%aL</i></p>
<dl>
<dt>
<dd> author local-part (see <i>%al</i>) respecting .mailmap, see <code><a href="/docs/linux/man/1-git-shortlog/">git-shortlog</a></code>(1) or <code><a href="/docs/linux/man/1-git-blame/">git-blame</a></code>(1))</dl>
<p> <i>%ad</i></p>
<dl>
<dt>
<dd> author date (format respects &#8211;date= option)</dl>
<p> <i>%aD</i></p>
<dl>
<dt>
<dd> author date, RFC2822 style</dl>
<p> <i>%ar</i></p>
<dl>
<dt>
<dd> author date, relative</dl>
<p> <i>%at</i></p>
<dl>
<dt>
<dd> author date, UNIX timestamp</dl>
<p> <i>%ai</i></p>
<dl>
<dt>
<dd> author date, ISO 8601-like format</dl>
<p> <i>%aI</i></p>
<dl>
<dt>
<dd> author date, strict ISO 8601 format</dl>
<p> <i>%as</i></p>
<dl>
<dt>
<dd> author date, short format (<code>YYYY-MM-DD</code>)</dl>
<p> <i>%ah</i></p>
<dl>
<dt>
<dd> author date, human style (like the <code>&#8211;date=human</code> option of <code><a href="/docs/linux/man/1-git-rev-list/">git-rev-list</a></code>(1))</dl>
<p> <i>%cn</i></p>
<dl>
<dt>
<dd> committer name</dl>
<p> <i>%cN</i></p>
<dl>
<dt>
<dd> committer name (respecting .mailmap, see <code><a href="/docs/linux/man/1-git-shortlog/">git-shortlog</a></code>(1) or <code><a href="/docs/linux/man/1-git-blame/">git-blame</a></code>(1))</dl>
<p> <i>%ce</i></p>
<dl>
<dt>
<dd> committer email</dl>
<p> <i>%cE</i></p>
<dl>
<dt>
<dd> committer email (respecting .mailmap, see <code><a href="/docs/linux/man/1-git-shortlog/">git-shortlog</a></code>(1) or <code><a href="/docs/linux/man/1-git-blame/">git-blame</a></code>(1))</dl>
<p> <i>%cl</i></p>
<dl>
<dt>
<dd> committer email local-part (the part before the <i>@</i> sign)</dl>
<p> <i>%cL</i></p>
<dl>
<dt>
<dd> committer local-part (see <i>%cl</i>) respecting .mailmap, see <code><a href="/docs/linux/man/1-git-shortlog/">git-shortlog</a></code>(1) or <code><a href="/docs/linux/man/1-git-blame/">git-blame</a></code>(1))</dl>
<p> <i>%cd</i></p>
<dl>
<dt>
<dd> committer date (format respects &#8211;date= option)</dl>
<p> <i>%cD</i></p>
<dl>
<dt>
<dd> committer date, RFC2822 style</dl>
<p> <i>%cr</i></p>
<dl>
<dt>
<dd> committer date, relative</dl>
<p> <i>%ct</i></p>
<dl>
<dt>
<dd> committer date, UNIX timestamp</dl>
<p> <i>%ci</i></p>
<dl>
<dt>
<dd> committer date, ISO 8601-like format</dl>
<p> <i>%cI</i></p>
<dl>
<dt>
<dd> committer date, strict ISO 8601 format</dl>
<p> <i>%cs</i></p>
<dl>
<dt>
<dd> committer date, short format (<code>YYYY-MM-DD</code>)</dl>
<p> <i>%ch</i></p>
<dl>
<dt>
<dd> committer date, human style (like the <code>&#8211;date=human</code> option of <code><a href="/docs/linux/man/1-git-rev-list/">git-rev-list</a></code>(1))</dl>
<p> <i>%d</i></p>
<dl>
<dt>
<dd> ref names, like the &#8211;decorate option of <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1)</dl>
<p> <i>%D</i></p>
<dl>
<dt>
<dd> ref names without the &quot; (&quot;, &quot;)&quot; wrapping.</dl>
<p> <i>%(describe[:options])</i></p>
<dl>
<dt>
<dd> human-readable name, like <code><a href="/docs/linux/man/1-git-describe/">git-describe</a></code>(1); empty string for undescribable commits. The <code>describe</code> string may be followed by a colon and zero or more comma-separated options. Descriptions can be inconsistent when tags are added or removed at the same time. </p>
<dl>
<dt>
<dd> &bull; <i>match=&lt;pattern&gt;</i>: Only consider tags matching the given <code><a href="/docs/linux/man/7-glob/">glob</a>(7)</code> pattern, excluding the &quot;refs/tags/&quot; prefix.</dl>
<dl>
<dt>
<dd> &bull; <i>exclude=&lt;pattern&gt;</i>: Do not consider tags matching the given <code><a href="/docs/linux/man/7-glob/">glob</a>(7)</code> pattern, excluding the &quot;refs/tags/&quot; prefix.</dl>
</dl>
<p> <i>%S</i></p>
<dl>
<dt>
<dd> ref name given on the command line by which the commit was reached (like <code>git log &#8211;source</code>), only works with <code>git log</code></dl>
<p> <i>%e</i></p>
<dl>
<dt>
<dd> encoding</dl>
<p> <i>%s</i></p>
<dl>
<dt>
<dd> subject</dl>
<p> <i>%f</i></p>
<dl>
<dt>
<dd> sanitized subject line, suitable for a filename</dl>
<p> <i>%b</i></p>
<dl>
<dt>
<dd> body</dl>
<p> <i>%B</i></p>
<dl>
<dt>
<dd> raw body (unwrapped subject and body)</dl>
<p> <i>%N</i></p>
<dl>
<dt>
<dd> commit notes</dl>
<p> <i>%GG</i></p>
<dl>
<dt>
<dd> raw verification message from GPG for a signed commit</dl>
<p> <i>%G?</i></p>
<dl>
<dt>
<dd> show &quot;G&quot; for a good (valid) signature, &quot;B&quot; for a bad signature, &quot;U&quot; for a good signature with unknown validity, &quot;X&quot; for a good signature that has expired, &quot;Y&quot; for a good signature made by an expired key, &quot;R&quot; for a good signature made by a revoked key, &quot;E&quot; if the signature cannot be checked (e.g. missing key) and &quot;N&quot; for no signature</dl>
<p> <i>%GS</i></p>
<dl>
<dt>
<dd> show the name of the signer for a signed commit</dl>
<p> <i>%GK</i></p>
<dl>
<dt>
<dd> show the key used to sign a signed commit</dl>
<p> <i>%GF</i></p>
<dl>
<dt>
<dd> show the fingerprint of the key used to sign a signed commit</dl>
<p> <i>%GP</i></p>
<dl>
<dt>
<dd> show the fingerprint of the primary key whose subkey was used to sign a signed commit</dl>
<p> <i>%GT</i></p>
<dl>
<dt>
<dd> show the trust level for the key used to sign a signed commit</dl>
<p> <i>%gD</i></p>
<dl>
<dt>
<dd> reflog selector, e.g., <code>refs/stash@{1}</code> or <code>refs/stash@{2 minutes ago}</code>; the format follows the rules described for the <code>-g</code> option. The portion before the <code>@</code> is the refname as given on the command line (so <code>git log -g refs/heads/master</code> would yield <code>refs/heads/master@{0}</code>).</dl>
<p> <i>%gd</i></p>
<dl>
<dt>
<dd> shortened reflog selector; same as <code>%gD</code>, but the refname portion is shortened for human readability (so <code>refs/heads/master</code> becomes just <code>master</code>).</dl>
<p> <i>%gn</i></p>
<dl>
<dt>
<dd> reflog identity name</dl>
<p> <i>%gN</i></p>
<dl>
<dt>
<dd> reflog identity name (respecting .mailmap, see <code><a href="/docs/linux/man/1-git-shortlog/">git-shortlog</a></code>(1) or <code><a href="/docs/linux/man/1-git-blame/">git-blame</a></code>(1))</dl>
<p> <i>%ge</i></p>
<dl>
<dt>
<dd> reflog identity email</dl>
<p> <i>%gE</i></p>
<dl>
<dt>
<dd> reflog identity email (respecting .mailmap, see <code><a href="/docs/linux/man/1-git-shortlog/">git-shortlog</a></code>(1) or <code><a href="/docs/linux/man/1-git-blame/">git-blame</a></code>(1))</dl>
<p> <i>%gs</i></p>
<dl>
<dt>
<dd> reflog subject</dl>
<p> <i>%(trailers[:options])</i></p>
<dl>
<dt>
<dd> display the trailers of the body as interpreted by <code><a href="/docs/linux/man/1-git-interpret-trailers/">git-interpret-trailers</a></code>(1). The <code>trailers</code> string may be followed by a colon and zero or more comma-separated options. If any option is provided multiple times the last occurrence wins. </p>
<p> The boolean options accept an optional value <code>[=&lt;BOOL&gt;]</code>. The values <code>true</code>, <code>false</code>, <code>on</code>, <code>off</code> etc. are all accepted. See the &quot;boolean&quot; sub-section in &quot;EXAMPLES&quot; in <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1). If a boolean option is given with no value, it&#8217;s enabled. </p>
<dl>
<dt>
<dd> &bull; <i>key=&lt;K&gt;</i>: only show trailers with specified key. Matching is done case-insensitively and trailing colon is optional. If option is given multiple times trailer lines matching any of the keys are shown. This option automatically enables the <code>only</code> option so that non-trailer lines in the trailer block are hidden. If that is not desired it can be disabled with <code>only=false</code>. E.g., <code>%(trailers:key=Reviewed-by)</code> shows trailer lines with key <code>Reviewed-by</code>.</dl>
<dl>
<dt>
<dd> &bull; <i>only[=&lt;BOOL&gt;]</i>: select whether non-trailer lines from the trailer block should be included.</dl>
<dl>
<dt>
<dd> &bull; <i>separator=&lt;SEP&gt;</i>: specify a separator inserted between trailer lines. When this option is not given each trailer line is terminated with a line feed character. The string SEP may contain the literal formatting codes described above. To use comma as separator one must use <code>%x2C</code> as it would otherwise be parsed as next option. E.g., <code>%(trailers:key=Ticket,separator=%x2C )</code> shows all trailer lines whose key is &quot;Ticket&quot; separated by a comma and a space.</dl>
<dl>
<dt>
<dd> &bull; <i>unfold[=&lt;BOOL&gt;]</i>: make it behave as if interpret-trailer&#8217;s <code>&#8211;unfold</code> option was given. E.g., <code>%(trailers:only,unfold=true)</code> unfolds and shows all trailer lines.</dl>
<dl>
<dt>
<dd> &bull; <i>keyonly[=&lt;BOOL&gt;]</i>: only show the key part of the trailer.</dl>
<dl>
<dt>
<dd> &bull; <i>valueonly[=&lt;BOOL&gt;]</i>: only show the value part of the trailer.</dl>
<dl>
<dt>
<dd> &bull; <i>key_value_separator=&lt;SEP&gt;</i>: specify a separator inserted between trailer lines. When this option is not given each trailer key-value pair is separated by &quot;: &quot;. Otherwise it shares the same semantics as <i>separator=&lt;SEP&gt;</i> above.</dl>
</dl>
</dl>
</dl>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> Some placeholders may depend on other options given to the revision traversal engine. For example, the <code>%g*</code> reflog options will insert an empty string unless we are traversing reflog entries (e.g., by <code>git log -g</code>). The <code>%d</code> and <code>%D</code> placeholders will use the &quot;short&quot; decoration format if <code>&#8211;decorate</code> was not already provided on the command line. </p>
</dl>
<p> If you add a <code>+</code> (plus sign) after <i>%</i> of a placeholder, a line-feed is inserted immediately before the expansion if and only if the placeholder expands to a non-empty string. </p>
<p> If you add a <code>&#8211;</code> (minus sign) after <i>%</i> of a placeholder, all consecutive line-feeds immediately preceding the expansion are deleted if and only if the placeholder expands to an empty string. </p>
<p> If you add a ` ` (space) after <i>%</i> of a placeholder, a space is inserted immediately before the expansion if and only if the placeholder expands to a non-empty string. </p>
<dl>
<dt>
<dd> &bull; <i>tformat:</i> </p>
<p> The <i>tformat:</i> format works exactly like <i>format:</i>, except that it provides &quot;terminator&quot; semantics instead of &quot;separator&quot; semantics. In other words, each commit has the message terminator character (usually a newline) appended, rather than a separator placed between entries. This means that the final entry of a single-line format will be properly terminated with a new line, just as the &quot;oneline&quot; format does. For example: </p>
<dl>
<dt>
<dd>
$ git log &#8211; 2 &#8211;pretty = format : % h 4da45bef | perl &#8211; pe &#8216;$_ .= &#8221; &#8212; NO NEWLINE
&#8221; unless /
/&#8217; 4da45be 7134973 &#8211;NO NEWLINE $ git log &#8211; 2 &#8211;pretty = tformat : % h 4da45bef | perl &#8211; pe &#8216;$_ .= &#8221; &#8212; NO NEWLINE
&#8221; unless /
/&#8217; 4da45be 7134973
</dl>
<p> In addition, any unrecognized string that has a <code>%</code> in it is interpreted as if it has <code>tformat:</code> in front of it. For example, these two are equivalent: </p>
<dl>
<dt>
<dd>
<pre>
$ git log -2 --pretty=tformat:%h 4da45bef
$ git log -2 --pretty=%h 4da45bef
</pre>
</dl>
</dl>
<h2>DIFF FORMATTING</h2>
<p> By default, <code>git log</code> does not generate any diff output. The options below can be used to show the changes made by each commit. </p>
<p> Note that unless one of <code>&#8211;diff-merges</code> variants (including short <code>-m</code>, <code>-c</code>, and <code>&#8211;cc</code> options) is explicitly given, merge commits will not show a diff, even if a diff format like <code>&#8211;patch</code> is selected, nor will they match search options like <code>-S</code>. The exception is when <code>&#8211;first-parent</code> is in use, in which case <code>first-parent</code> is the default format. </p>
<p> -p, -u, &#8211;patch</p>
<dl>
<dt>
<dd> Generate patch (see section on generating patches).</dl>
<p> -s, &#8211;no-patch</p>
<dl>
<dt>
<dd> Suppress diff output. Useful for commands like <code>git show</code> that show the patch by default, or to cancel the effect of <code>&#8211;patch</code>.</dl>
<p> &#8211;diff-merges=(off|none|on|first-parent|1|separate|m|combined|c|dense-combined|cc), &#8211;no-diff-merges</p>
<dl>
<dt>
<dd> Specify diff format to be used for merge commits. Default is <code>off</code> unless <code>&#8211;first-parent</code> is in use, in which case <code>first-parent</code> is the default. </p>
<p> &#8211;diff-merges=(off|none), &#8211;no-diff-merges</p>
<dl>
<dt>
<dd> Disable output of diffs for merge commits. Useful to override implied value.</dl>
<p> &#8211;diff-merges=on, &#8211;diff-merges=m, -m</p>
<dl>
<dt>
<dd> This option makes diff output for merge commits to be shown in the default format. <code>-m</code> will produce the output only if <code>-p</code> is given as well. The default format could be changed using <code>log.diffMerges</code> configuration parameter, which default value is <code>separate</code>.</dl>
<p> &#8211;diff-merges=first-parent, &#8211;diff-merges=1</p>
<dl>
<dt>
<dd> This option makes merge commits show the full diff with respect to the first parent only.</dl>
<p> &#8211;diff-merges=separate</p>
<dl>
<dt>
<dd> This makes merge commits show the full diff with respect to each of the parents. Separate log entry and diff is generated for each parent.</dl>
<p> &#8211;diff-merges=combined, &#8211;diff-merges=c, -c</p>
<dl>
<dt>
<dd> With this option, diff output for a merge commit shows the differences from each of the parents to the merge result simultaneously instead of showing pairwise diff between a parent and the result one at a time. Furthermore, it lists only files which were modified from all parents. <code>-c</code> implies <code>-p</code>.</dl>
<p> &#8211;diff-merges=dense-combined, &#8211;diff-merges=cc, &#8211;cc</p>
<dl>
<dt>
<dd> With this option the output produced by <code>&#8211;diff-merges=combined</code> is further compressed by omitting uninteresting hunks whose contents in the parents have only two variants and the merge result picks one of them without modification. <code>&#8211;cc</code> implies <code>-p</code>.</dl>
</dl>
<p> &#8211;combined-all-paths</p>
<dl>
<dt>
<dd> This flag causes combined diffs (used for merge commits) to list the name of the file from all parents. It thus only has effect when <code>&#8211;diff-merges=[dense-]combined</code> is in use, and is likely only useful if filename changes are detected (i.e. when either rename or copy detection have been requested).</dl>
<p> -U&lt;n&gt;, &#8211;unified=&lt;n&gt;</p>
<dl>
<dt>
<dd> Generate diffs with &lt;n&gt; lines of context instead of the usual three. Implies <code>&#8211;patch</code>.</dl>
<p> &#8211;output=&lt;file&gt;</p>
<dl>
<dt>
<dd> Output to a specific file instead of stdout.</dl>
<p> &#8211;output-indicator-new=&lt;char&gt;, &#8211;output-indicator-old=&lt;char&gt;, &#8211;output-indicator-context=&lt;char&gt;</p>
<dl>
<dt>
<dd> Specify the character used to indicate new, old or context lines in the generated patch. Normally they are <i>+</i>, <i>&#8211;</i> and &#8216; &#8216; respectively.</dl>
<p> &#8211;raw</p>
<dl>
<dt>
<dd> For each commit, show a summary of changes using the raw diff format. See the &quot;RAW OUTPUT FORMAT&quot; section of <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1). This is different from showing the log itself in raw format, which you can achieve with <code>&#8211;format=raw</code>.</dl>
<p> &#8211;patch-with-raw</p>
<dl>
<dt>
<dd> Synonym for <code>-p &#8211;raw</code>.</dl>
<p> -t</p>
<dl>
<dt>
<dd> Show the tree objects in the diff output.</dl>
<p> &#8211;indent-heuristic</p>
<dl>
<dt>
<dd> Enable the heuristic that shifts diff hunk boundaries to make patches easier to read. This is the default.</dl>
<p> &#8211;no-indent-heuristic</p>
<dl>
<dt>
<dd> Disable the indent heuristic.</dl>
<p> &#8211;minimal</p>
<dl>
<dt>
<dd> Spend extra time to make sure the smallest possible diff is produced.</dl>
<p> &#8211;patience</p>
<dl>
<dt>
<dd> Generate a diff using the &quot;patience diff&quot; algorithm.</dl>
<p> &#8211;histogram</p>
<dl>
<dt>
<dd> Generate a diff using the &quot;histogram diff&quot; algorithm.</dl>
<p> &#8211;anchored=&lt;text&gt;</p>
<dl>
<dt>
<dd> Generate a diff using the &quot;anchored diff&quot; algorithm. </p>
<p> This option may be specified more than once. </p>
<p> If a line exists in both the source and destination, exists only once, and starts with this text, this algorithm attempts to prevent it from appearing as a deletion or addition in the output. It uses the &quot;patience diff&quot; algorithm internally.</dl>
<p> &#8211;diff-algorithm={patience|minimal|histogram|myers}</p>
<dl>
<dt>
<dd> Choose a diff algorithm. The variants are as follows: </p>
<p> <code>default</code>, <code>myers</code></p>
<dl>
<dt>
<dd> The basic greedy diff algorithm. Currently, this is the default.</dl>
<p> <code>minimal</code></p>
<dl>
<dt>
<dd> Spend extra time to make sure the smallest possible diff is produced.</dl>
<p> <code>patience</code></p>
<dl>
<dt>
<dd> Use &quot;patience diff&quot; algorithm when generating patches.</dl>
<p> <code>histogram</code></p>
<dl>
<dt>
<dd> This algorithm extends the patience algorithm to &quot;support low-occurrence common elements&quot;.</dl>
<p> For instance, if you configured the <code>diff.algorithm</code> variable to a non-default value and want to use the default one, then you have to use <code>&#8211;diff-algorithm=default</code> option.</dl>
<p> &#8211;stat[=&lt;width&gt;[,&lt;name-width&gt;[,&lt;count&gt;]]]</p>
<dl>
<dt>
<dd> Generate a diffstat. By default, as much space as necessary will be used for the filename part, and the rest for the graph part. Maximum width defaults to terminal width, or 80 columns if not connected to a terminal, and can be overridden by <code>&lt;width&gt;</code>. The width of the filename part can be limited by giving another width <code>&lt;name-width&gt;</code> after a comma. The width of the graph part can be limited by using <code>&#8211;stat-graph-width=&lt;width&gt;</code> (affects all commands generating a stat graph) or by setting <code>diff.statGraphWidth=&lt;width&gt;</code> (does not affect <code>git format-patch</code>). By giving a third parameter <code>&lt;count&gt;</code>, you can limit the output to the first <code>&lt;count&gt;</code> lines, followed by <code>&#8230;</code> if there are more. </p>
<p> These parameters can also be set individually with <code>&#8211;stat-width=&lt;width&gt;</code>, <code>&#8211;stat-name-width=&lt;name-width&gt;</code> and <code>&#8211;stat-count=&lt;count&gt;</code>.</dl>
<p> &#8211;compact-summary</p>
<dl>
<dt>
<dd> Output a condensed summary of extended header information such as file creations or deletions (&quot;new&quot; or &quot;gone&quot;, optionally &quot;+l&quot; if it&#8217;s a symlink) and mode changes (&quot;+x&quot; or &quot;-x&quot; for adding or removing executable bit respectively) in diffstat. The information is put between the filename part and the graph part. Implies <code>&#8211;stat</code>.</dl>
<p> &#8211;numstat</p>
<dl>
<dt>
<dd> Similar to <code>&#8211;stat</code>, but shows number of added and deleted lines in decimal notation and pathname without abbreviation, to make it more machine friendly. For binary files, outputs two <code>&#8211;</code> instead of saying <code>0 0</code>.</dl>
<p> &#8211;shortstat</p>
<dl>
<dt>
<dd> Output only the last line of the <code>&#8211;stat</code> format containing total number of modified files, as well as number of added and deleted lines.</dl>
<p> -X[&lt;param1,param2,&#8230;&gt;], &#8211;dirstat[=&lt;param1,param2,&#8230;&gt;]</p>
<dl>
<dt>
<dd> Output the distribution of relative amount of changes for each sub-directory. The behavior of <code>&#8211;dirstat</code> can be customized by passing it a comma separated list of parameters. The defaults are controlled by the <code>diff.dirstat</code> configuration variable (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)). The following parameters are available: </p>
<p> <code>changes</code></p>
<dl>
<dt>
<dd> Compute the dirstat numbers by counting the lines that have been removed from the source, or added to the destination. This ignores the amount of pure code movements within a file. In other words, rearranging lines in a file is not counted as much as other changes. This is the default behavior when no parameter is given.</dl>
<p> <code>lines</code></p>
<dl>
<dt>
<dd> Compute the dirstat numbers by doing the regular line-based diff analysis, and summing the removed/added line counts. (For binary files, count 64-byte chunks instead, since binary files have no natural concept of lines). This is a more expensive <code>&#8211;dirstat</code> behavior than the <code>changes</code> behavior, but it does count rearranged lines within a file as much as other changes. The resulting output is consistent with what you get from the other <code>&#8211;*stat</code> options.</dl>
<p> <code>files</code></p>
<dl>
<dt>
<dd> Compute the dirstat numbers by counting the number of files changed. Each changed file counts equally in the dirstat analysis. This is the computationally cheapest <code>&#8211;dirstat</code> behavior, since it does not have to look at the file contents at all.</dl>
<p> <code>cumulative</code></p>
<dl>
<dt>
<dd> Count changes in a child directory for the parent directory as well. Note that when using <code>cumulative</code>, the sum of the percentages reported may exceed 100%. The default (non-cumulative) behavior can be specified with the <code>noncumulative</code> parameter.</dl>
<p> &lt;limit&gt;</p>
<dl>
<dt>
<dd> An integer parameter specifies a cut-off percent (3% by default). Directories contributing less than this percentage of the changes are not shown in the output.</dl>
<p> Example: The following will count changed files, while ignoring directories with less than 10% of the total amount of changed files, and accumulating child directory counts in the parent directories: <code>&#8211;dirstat=files,10,cumulative</code>.</dl>
<p> &#8211;cumulative</p>
<dl>
<dt>
<dd> Synonym for &#8211;dirstat=cumulative</dl>
<p> &#8211;dirstat-by-file[=&lt;param1,param2&gt;&#8230;]</p>
<dl>
<dt>
<dd> Synonym for &#8211;dirstat=files,param1,param2&#8230;</dl>
<p> &#8211;summary</p>
<dl>
<dt>
<dd> Output a condensed summary of extended header information such as creations, renames and mode changes.</dl>
<p> &#8211;patch-with-stat</p>
<dl>
<dt>
<dd> Synonym for <code>-p &#8211;stat</code>.</dl>
<p> -z</p>
<dl>
<dt>
<dd> Separate the commits with NULs instead of with new newlines. </p>
<p> Also, when <code>&#8211;raw</code> or <code>&#8211;numstat</code> has been given, do not munge pathnames and use NULs as output field terminators. </p>
<p> Without this option, pathnames with &quot;unusual&quot; characters are quoted as explained for the configuration variable <code>core.quotePath</code> (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)).</dl>
<p> &#8211;name-only</p>
<dl>
<dt>
<dd> Show only names of changed files. The file names are often encoded in UTF-8. For more information see the discussion about encoding in the <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1) manual page.</dl>
<p> &#8211;name-status</p>
<dl>
<dt>
<dd> Show only names and status of changed files. See the description of the <code>&#8211;diff-filter</code> option on what the status letters mean. Just like <code>&#8211;name-only</code> the file names are often encoded in UTF-8.</dl>
<p> &#8211;submodule[=&lt;format&gt;]</p>
<dl>
<dt>
<dd> Specify how differences in submodules are shown. When specifying <code>&#8211;submodule=short</code> the <i>short</i> format is used. This format just shows the names of the commits at the beginning and end of the range. When <code>&#8211;submodule</code> or <code>&#8211;submodule=log</code> is specified, the <i>log</i> format is used. This format lists the commits in the range like <code><a href="/docs/linux/man/1-git-submodule/">git-submodule</a></code>(1) <code>summary</code> does. When <code>&#8211;submodule=diff</code> is specified, the <i>diff</i> format is used. This format shows an inline diff of the changes in the submodule contents between the commit range. Defaults to <code>diff.submodule</code> or the <i>short</i> format if the config option is unset.</dl>
<p> &#8211;color[=&lt;when&gt;]</p>
<dl>
<dt>
<dd> Show colored diff. <code>&#8211;color</code> (i.e. without <i>=&lt;when&gt;</i>) is the same as <code>&#8211;color=always</code>. <i>&lt;when&gt;</i> can be one of <code>always</code>, <code>never</code>, or <code>auto</code>.</dl>
<p> &#8211;no-color</p>
<dl>
<dt>
<dd> Turn off colored diff. It is the same as <code>&#8211;color=never</code>.</dl>
<p> &#8211;color-moved[=&lt;mode&gt;]</p>
<dl>
<dt>
<dd> Moved lines of code are colored differently. The &lt;mode&gt; defaults to <i>no</i> if the option is not given and to <i>zebra</i> if the option with no mode is given. The mode must be one of: </p>
<p> no</p>
<dl>
<dt>
<dd> Moved lines are not highlighted.</dl>
<p> default</p>
<dl>
<dt>
<dd> Is a synonym for <code>zebra</code>. This may change to a more sensible mode in the future.</dl>
<p> plain</p>
<dl>
<dt>
<dd> Any line that is added in one location and was removed in another location will be colored with <i>color.diff.newMoved</i>. Similarly <i>color.diff.oldMoved</i> will be used for removed lines that are added somewhere else in the diff. This mode picks up any moved line, but it is not very useful in a review to determine if a block of code was moved without permutation.</dl>
<p> blocks</p>
<dl>
<dt>
<dd> Blocks of moved text of at least 20 alphanumeric characters are detected greedily. The detected blocks are painted using either the <i>color.diff.{old,new}Moved</i> color. Adjacent blocks cannot be told apart.</dl>
<p> zebra</p>
<dl>
<dt>
<dd> Blocks of moved text are detected as in <i>blocks</i> mode. The blocks are painted using either the <i>color.diff.{old,new}Moved</i> color or <i>color.diff.{old,new}MovedAlternative</i>. The change between the two colors indicates that a new block was detected.</dl>
<p> dimmed-zebra</p>
<dl>
<dt>
<dd> Similar to <i>zebra</i>, but additional dimming of uninteresting parts of moved code is performed. The bordering lines of two adjacent blocks are considered interesting, the rest is uninteresting. <code>dimmed_zebra</code> is a deprecated synonym.</dl>
</dl>
<p> &#8211;no-color-moved</p>
<dl>
<dt>
<dd> Turn off move detection. This can be used to override configuration settings. It is the same as <code>&#8211;color-moved=no</code>.</dl>
<p> &#8211;color-moved-ws=&lt;modes&gt;</p>
<dl>
<dt>
<dd> This configures how whitespace is ignored when performing the move detection for <code>&#8211;color-moved</code>. These modes can be given as a comma separated list: </p>
<p> no</p>
<dl>
<dt>
<dd> Do not ignore whitespace when performing move detection.</dl>
<p> ignore-space-at-eol</p>
<dl>
<dt>
<dd> Ignore changes in whitespace at EOL.</dl>
<p> ignore-space-change</p>
<dl>
<dt>
<dd> Ignore changes in amount of whitespace. This ignores whitespace at line end, and considers all other sequences of one or more whitespace characters to be equivalent.</dl>
<p> ignore-all-space</p>
<dl>
<dt>
<dd> Ignore whitespace when comparing lines. This ignores differences even if one line has whitespace where the other line has none.</dl>
<p> allow-indentation-change</p>
<dl>
<dt>
<dd> Initially ignore any whitespace in the move detection, then group the moved code blocks only into a block if the change in whitespace is the same per line. This is incompatible with the other modes.</dl>
</dl>
<p> &#8211;no-color-moved-ws</p>
<dl>
<dt>
<dd> Do not ignore whitespace when performing move detection. This can be used to override configuration settings. It is the same as <code>&#8211;color-moved-ws=no</code>.</dl>
<p> &#8211;word-diff[=&lt;mode&gt;]</p>
<dl>
<dt>
<dd> Show a word diff, using the &lt;mode&gt; to delimit changed words. By default, words are delimited by whitespace; see <code>&#8211;word-diff-regex</code> below. The &lt;mode&gt; defaults to <i>plain</i>, and must be one of: </p>
<p> color</p>
<dl>
<dt>
<dd> Highlight changed words using only colors. Implies <code>&#8211;color</code>.</dl>
<p> plain</p>
<dl>
<dt>
<dd> Show words as <code>[-removed-]</code> and <code>{+added+}</code>. Makes no attempts to escape the delimiters if they appear in the input, so the output may be ambiguous.</dl>
<p> porcelain</p>
<dl>
<dt>
<dd> Use a special line-based format intended for script consumption. Added/removed/unchanged runs are printed in the usual unified diff format, starting with a <code>+</code>/<code>&#8211;</code>/` ` character at the beginning of the line and extending to the end of the line. Newlines in the input are represented by a tilde <code>~</code> on a line of its own.</dl>
<p> none</p>
<dl>
<dt>
<dd> Disable word diff again.</dl>
<p> Note that despite the name of the first mode, color is used to highlight the changed parts in all modes if enabled.</dl>
<p> &#8211;word-diff-regex=&lt;regex&gt;</p>
<dl>
<dt>
<dd> Use &lt;regex&gt; to decide what a word is, instead of considering runs of non-whitespace to be a word. Also implies <code>&#8211;word-diff</code> unless it was already enabled. </p>
<p> Every non-overlapping match of the &lt;regex&gt; is considered a word. Anything between these matches is considered whitespace and ignored(!) for the purposes of finding differences. You may want to append <code>|[^[:space:]]</code> to your regular expression to make sure that it matches all non-whitespace characters. A match that contains a newline is silently truncated(!) at the newline. </p>
<p> For example, <code>&#8211;word-diff-regex=.</code> will treat each character as a word and, correspondingly, show differences character by character. </p>
<p> The regex can also be set via a diff driver or configuration option, see <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5) or <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1). Giving it explicitly overrides any diff driver or configuration setting. Diff drivers override configuration settings.</dl>
<p> &#8211;color-words[=&lt;regex&gt;]</p>
<dl>
<dt>
<dd> Equivalent to <code>&#8211;word-diff=color</code> plus (if a regex was specified) <code>&#8211;word-diff-regex=&lt;regex&gt;</code>.</dl>
<p> &#8211;no-renames</p>
<dl>
<dt>
<dd> Turn off rename detection, even when the configuration file gives the default to do so.</dl>
<p> &#8211;[no-]rename-empty</p>
<dl>
<dt>
<dd> Whether to use empty blobs as rename source.</dl>
<p> &#8211;check</p>
<dl>
<dt>
<dd> Warn if changes introduce conflict markers or whitespace errors. What are considered whitespace errors is controlled by <code>core.whitespace</code> configuration. By default, trailing whitespaces (including lines that consist solely of whitespaces) and a space character that is immediately followed by a tab character inside the initial indent of the line are considered whitespace errors. Exits with non-zero status if problems are found. Not compatible with &#8211;exit-code.</dl>
<p> &#8211;ws-error-highlight=&lt;kind&gt;</p>
<dl>
<dt>
<dd> Highlight whitespace errors in the <code>context</code>, <code>old</code> or <code>new</code> lines of the diff. Multiple values are separated by comma, <code>none</code> resets previous values, <code>default</code> reset the list to <code>new</code> and <code>all</code> is a shorthand for <code>old,new,context</code>. When this option is not given, and the configuration variable <code>diff.wsErrorHighlight</code> is not set, only whitespace errors in <code>new</code> lines are highlighted. The whitespace errors are colored with <code>color.diff.whitespace</code>.</dl>
<p> &#8211;full-index</p>
<dl>
<dt>
<dd> Instead of the first handful of characters, show the full pre- and post-image blob object names on the &quot;index&quot; line when generating patch format output.</dl>
<p> &#8211;binary</p>
<dl>
<dt>
<dd> In addition to <code>&#8211;full-index</code>, output a binary diff that can be applied with <code>git-apply</code>. Implies <code>&#8211;patch</code>.</dl>
<p> &#8211;abbrev[=&lt;n&gt;]</p>
<dl>
<dt>
<dd> Instead of showing the full 40-byte hexadecimal object name in diff-raw format output and diff-tree header lines, show the shortest prefix that is at least <i>&lt;n&gt;</i> hexdigits long that uniquely refers the object. In diff-patch output format, <code>&#8211;full-index</code> takes higher precedence, i.e. if <code>&#8211;full-index</code> is specified, full blob names will be shown regardless of <code>&#8211;abbrev</code>. Non default number of digits can be specified with <code>&#8211;abbrev=&lt;n&gt;</code>.</dl>
<p> -B[&lt;n&gt;][/&lt;m&gt;], &#8211;break-rewrites[=[&lt;n&gt;][/&lt;m&gt;]]</p>
<dl>
<dt>
<dd> Break complete rewrite changes into pairs of delete and create. This serves two purposes: </p>
<p> It affects the way a change that amounts to a total rewrite of a file not as a series of deletion and insertion mixed together with a very few lines that happen to match textually as the context, but as a single deletion of everything old followed by a single insertion of everything new, and the number <code>m</code> controls this aspect of the -B option (defaults to 60%). <code>-B/70%</code> specifies that less than 30% of the original should remain in the result for Git to consider it a total rewrite (i.e. otherwise the resulting patch will be a series of deletion and insertion mixed together with context lines). </p>
<p> When used with -M, a totally-rewritten file is also considered as the source of a rename (usually -M only considers a file that disappeared as the source of a rename), and the number <code>n</code> controls this aspect of the -B option (defaults to 50%). <code>-B20%</code> specifies that a change with addition and deletion compared to 20% or more of the file&#8217;s size are eligible for being picked up as a possible source of a rename to another file.</dl>
<p> -M[&lt;n&gt;], &#8211;find-renames[=&lt;n&gt;]</p>
<dl>
<dt>
<dd> If generating diffs, detect and report renames for each commit. For following files across renames while traversing history, see <code>&#8211;follow</code>. If <code>n</code> is specified, it is a threshold on the similarity index (i.e. amount of addition/deletions compared to the file&#8217;s size). For example, <code>-M90%</code> means Git should consider a delete/add pair to be a rename if more than 90% of the file hasn&#8217;t changed. Without a <code>%</code> sign, the number is to be read as a fraction, with a decimal point before it. I.e., <code>-M5</code> becomes 0.5, and is thus the same as <code>-M50%</code>. Similarly, <code>-M05</code> is the same as <code>-M5%</code>. To limit detection to exact renames, use <code>-M100%</code>. The default similarity index is 50%.</dl>
<p> -C[&lt;n&gt;], &#8211;find-copies[=&lt;n&gt;]</p>
<dl>
<dt>
<dd> Detect copies as well as renames. See also <code>&#8211;find-copies-harder</code>. If <code>n</code> is specified, it has the same meaning as for <code>-M&lt;n&gt;</code>.</dl>
<p> &#8211;find-copies-harder</p>
<dl>
<dt>
<dd> For performance reasons, by default, <code>-C</code> option finds copies only if the original file of the copy was modified in the same changeset. This flag makes the command inspect unmodified files as candidates for the source of copy. This is a very expensive operation for large projects, so use it with caution. Giving more than one <code>-C</code> option has the same effect.</dl>
<p> -D, &#8211;irreversible-delete</p>
<dl>
<dt>
<dd> Omit the preimage for deletes, i.e. print only the header but not the diff between the preimage and <code>/dev/null</code>. The resulting patch is not meant to be applied with <code>patch</code> or <code>git apply</code>; this is solely for people who want to just concentrate on reviewing the text after the change. In addition, the output obviously lacks enough information to apply such a patch in reverse, even manually, hence the name of the option. </p>
<p> When used together with <code>-B</code>, omit also the preimage in the deletion part of a delete/create pair.</dl>
<p> -l&lt;num&gt;</p>
<dl>
<dt>
<dd> The <code>-M</code> and <code>-C</code> options involve some preliminary steps that can detect subsets of renames/copies cheaply, followed by an exhaustive fallback portion that compares all remaining unpaired destinations to all relevant sources. (For renames, only remaining unpaired sources are relevant; for copies, all original sources are relevant.) For N sources and destinations, this exhaustive check is O(N^2). This option prevents the exhaustive portion of rename/copy detection from running if the number of source/destination files involved exceeds the specified number. Defaults to diff.renameLimit. Note that a value of 0 is treated as unlimited.</dl>
<p> &#8211;diff-filter=[(A|C|D|M|R|T|U|X|B)&#8230;[*]]</p>
<dl>
<dt>
<dd> Select only files that are Added (<code>A</code>), Copied (<code>C</code>), Deleted (<code>D</code>), Modified (<code>M</code>), Renamed (<code>R</code>), have their type (i.e. regular file, symlink, submodule, &#8230;) changed (<code>T</code>), are Unmerged (<code>U</code>), are Unknown (<code>X</code>), or have had their pairing Broken (<code>B</code>). Any combination of the filter characters (including none) can be used. When <code>*</code> (All-or-none) is added to the combination, all paths are selected if there is any file that matches other criteria in the comparison; if there is no file that matches other criteria, nothing is selected. </p>
<p> Also, these upper-case letters can be downcased to exclude. E.g. <code>&#8211;diff-filter=ad</code> excludes added and deleted paths. </p>
<p> Note that not all diffs can feature all types. For instance, diffs from the index to the working tree can never have Added entries (because the set of paths included in the diff is limited by what is in the index). Similarly, copied and renamed entries cannot appear if detection for those types is disabled.</dl>
<p> -S&lt;string&gt;</p>
<dl>
<dt>
<dd> Look for differences that change the number of occurrences of the specified string (i.e. addition/deletion) in a file. Intended for the scripter&#8217;s use. </p>
<p> It is useful when you&#8217;re looking for an exact block of code (like a struct), and want to know the history of that block since it first came into being: use the feature iteratively to feed the interesting block in the preimage back into <code>-S</code>, and keep going until you get the very first version of the block. </p>
<p> Binary files are searched as well.</dl>
<p> -G&lt;regex&gt;</p>
<dl>
<dt>
<dd> Look for differences whose patch text contains added/removed lines that match &lt;regex&gt;. </p>
<p> To illustrate the difference between <code>-S&lt;regex&gt; &#8211;pickaxe-regex</code> and <code>-G&lt;regex&gt;</code>, consider a commit with the following diff in the same file: </p>
<dl>
<dt>
<dd>
+ return frotz(nitfol, two-&gt;ptr, 1, 0);<br />
&#8230; &#8211; hit = frotz(nitfol, mf2.ptr, 1, 0);
</dl>
<p> While <code>git log -G&quot;frotz\(nitfol&quot;</code> will show this commit, <code>git log -S&quot;frotz\(nitfol&quot; &#8211;pickaxe-regex</code> will not (because the number of occurrences of that string did not change). </p>
<p> Unless <code>&#8211;text</code> is supplied patches of binary files without a textconv filter will be ignored. </p>
<p> See the <i>pickaxe</i> entry in <code><a href="/docs/linux/man/7-gitdiffcore/">gitdiffcore</a></code>(7) for more information.</dl>
<p> &#8211;find-object=&lt;object-id&gt;</p>
<dl>
<dt>
<dd> Look for differences that change the number of occurrences of the specified object. Similar to <code>-S</code>, just the argument is different in that it doesn&#8217;t search for a specific string but for a specific object id. </p>
<p> The object can be a blob or a submodule commit. It implies the <code>-t</code> option in <code>git-log</code> to also find trees.</dl>
<p> &#8211;pickaxe-all</p>
<dl>
<dt>
<dd> When <code>-S</code> or <code>-G</code> finds a change, show all the changes in that changeset, not just the files that contain the change in &lt;string&gt;.</dl>
<p> &#8211;pickaxe-regex</p>
<dl>
<dt>
<dd> Treat the &lt;string&gt; given to <code>-S</code> as an extended POSIX regular expression to match.</dl>
<p> -O&lt;orderfile&gt;</p>
<dl>
<dt>
<dd> Control the order in which files appear in the output. This overrides the <code>diff.orderFile</code> configuration variable (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)). To cancel <code>diff.orderFile</code>, use <code>-O/dev/null</code>. </p>
<p> The output order is determined by the order of glob patterns in &lt;orderfile&gt;. All files with pathnames that match the first pattern are output first, all files with pathnames that match the second pattern (but not the first) are output next, and so on. All files with pathnames that do not match any pattern are output last, as if there was an implicit match-all pattern at the end of the file. If multiple pathnames have the same rank (they match the same pattern but no earlier patterns), their output order relative to each other is the normal order. </p>
<p> &lt;orderfile&gt; is parsed as follows: </p>
<dl>
<dt>
<dd> &bull; Blank lines are ignored, so they can be used as separators for readability.</dl>
<dl>
<dt>
<dd> &bull; Lines starting with a hash (&quot;<code>#</code>&quot;) are ignored, so they can be used for comments. Add a backslash (&quot;<code>\</code>&quot;) to the beginning of the pattern if it starts with a hash.</dl>
<dl>
<dt>
<dd> &bull; Each other line contains a single pattern.</dl>
<p> Patterns have the same syntax and semantics as patterns used for <a href="/docs/linux/man/3-fnmatch/">fnmatch</a>(3) without the FNM_PATHNAME flag, except a pathname also matches a pattern if removing any number of the final pathname components matches the pattern. For example, the pattern &quot;<code>foo*bar</code>&quot; matches &quot;<code>fooasdfbar</code>&quot; and &quot;<code>foo/bar/baz/asdf</code>&quot; but not &quot;<code>foobarx</code>&quot;.</dl>
<p> &#8211;skip-to=&lt;file&gt;, &#8211;rotate-to=&lt;file&gt;</p>
<dl>
<dt>
<dd> Discard the files before the named &lt;file&gt; from the output (i.e. <i>skip to</i>), or move them to the end of the output (i.e. <i>rotate to</i>). These were invented primarily for use of the <code>git difftool</code> command, and may not be very useful otherwise.</dl>
<p> -R</p>
<dl>
<dt>
<dd> Swap two inputs; that is, show differences from index or on-disk file to tree contents.</dl>
<p> &#8211;relative[=&lt;path&gt;], &#8211;no-relative</p>
<dl>
<dt>
<dd> When run from a subdirectory of the project, it can be told to exclude changes outside the directory and show pathnames relative to it with this option. When you are not in a subdirectory (e.g. in a bare repository), you can name which subdirectory to make the output relative to by giving a &lt;path&gt; as an argument. <code>&#8211;no-relative</code> can be used to countermand both <code>diff.relative</code> config option and previous <code>&#8211;relative</code>.</dl>
<p> -a, &#8211;text</p>
<dl>
<dt>
<dd> Treat all files as text.</dl>
<p> &#8211;ignore-cr-at-eol</p>
<dl>
<dt>
<dd> Ignore carriage-return at the end of line when doing a comparison.</dl>
<p> &#8211;ignore-space-at-eol</p>
<dl>
<dt>
<dd> Ignore changes in whitespace at EOL.</dl>
<p> -b, &#8211;ignore-space-change</p>
<dl>
<dt>
<dd> Ignore changes in amount of whitespace. This ignores whitespace at line end, and considers all other sequences of one or more whitespace characters to be equivalent.</dl>
<p> -w, &#8211;ignore-all-space</p>
<dl>
<dt>
<dd> Ignore whitespace when comparing lines. This ignores differences even if one line has whitespace where the other line has none.</dl>
<p> &#8211;ignore-blank-lines</p>
<dl>
<dt>
<dd> Ignore changes whose lines are all blank.</dl>
<p> -I&lt;regex&gt;, &#8211;ignore-matching-lines=&lt;regex&gt;</p>
<dl>
<dt>
<dd> Ignore changes whose all lines match &lt;regex&gt;. This option may be specified more than once.</dl>
<p> &#8211;inter-hunk-context=&lt;lines&gt;</p>
<dl>
<dt>
<dd> Show the context between diff hunks, up to the specified number of lines, thereby fusing hunks that are close to each other. Defaults to <code>diff.interHunkContext</code> or 0 if the config option is unset.</dl>
<p> -W, &#8211;function-context</p>
<dl>
<dt>
<dd> Show whole function as context lines for each change. The function names are determined in the same way as <code>git diff</code> works out patch hunk headers (see <i>Defining a custom hunk-header</i> in <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5)).</dl>
<p> &#8211;ext-diff</p>
<dl>
<dt>
<dd> Allow an external diff helper to be executed. If you set an external diff driver with <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5), you need to use this option with <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1) and friends.</dl>
<p> &#8211;no-ext-diff</p>
<dl>
<dt>
<dd> Disallow external diff drivers.</dl>
<p> &#8211;textconv, &#8211;no-textconv</p>
<dl>
<dt>
<dd> Allow (or disallow) external text conversion filters to be run when comparing binary files. See <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5) for details. Because textconv filters are typically a one-way conversion, the resulting diff is suitable for human consumption, but cannot be applied. For this reason, textconv filters are enabled by default only for <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1) and <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1), but not for <code><a href="/docs/linux/man/1-git-format-patch/">git-format-patch</a></code>(1) or diff plumbing commands.</dl>
<p> &#8211;ignore-submodules[=&lt;when&gt;]</p>
<dl>
<dt>
<dd> Ignore changes to submodules in the diff generation. &lt;when&gt; can be either &quot;none&quot;, &quot;untracked&quot;, &quot;dirty&quot; or &quot;all&quot;, which is the default. Using &quot;none&quot; will consider the submodule modified when it either contains untracked or modified files or its HEAD differs from the commit recorded in the superproject and can be used to override any settings of the <i>ignore</i> option in <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1) or <code><a href="/docs/linux/man/5-gitmodules/">gitmodules</a></code>(5). When &quot;untracked&quot; is used submodules are not considered dirty when they only contain untracked content (but they are still scanned for modified content). Using &quot;dirty&quot; ignores all changes to the work tree of submodules, only changes to the commits stored in the superproject are shown (this was the behavior until 1.7.0). Using &quot;all&quot; hides all changes to submodules.</dl>
<p> &#8211;src-prefix=&lt;prefix&gt;</p>
<dl>
<dt>
<dd> Show the given source prefix instead of &quot;a/&quot;.</dl>
<p> &#8211;dst-prefix=&lt;prefix&gt;</p>
<dl>
<dt>
<dd> Show the given destination prefix instead of &quot;b/&quot;.</dl>
<p> &#8211;no-prefix</p>
<dl>
<dt>
<dd> Do not show any source or destination prefix.</dl>
<p> &#8211;line-prefix=&lt;prefix&gt;</p>
<dl>
<dt>
<dd> Prepend an additional prefix to every line of output.</dl>
<p> &#8211;ita-invisible-in-index</p>
<dl>
<dt>
<dd> By default entries added by &quot;git add -N&quot; appear as an existing empty file in &quot;git diff&quot; and a new file in &quot;git diff &#8211;cached&quot;. This option makes the entry appear as a new file in &quot;git diff&quot; and non-existent in &quot;git diff &#8211;cached&quot;. This option could be reverted with <code>&#8211;ita-visible-in-index</code>. Both options are experimental and could be removed in future.</dl>
<p> For more detailed explanation on these common options, see also <code><a href="/docs/linux/man/7-gitdiffcore/">gitdiffcore</a></code>(7).</p>
<h2>GENERATING PATCH TEXT WITH -P</h2>
<p> Running <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1), <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1), <code><a href="/docs/linux/man/1-git-show/">git-show</a></code>(1), <code><a href="/docs/linux/man/1-git-diff-index/">git-diff-index</a></code>(1), <code><a href="/docs/linux/man/1-git-diff-tree/">git-diff-tree</a></code>(1), or <code><a href="/docs/linux/man/1-git-diff-files/">git-diff-files</a></code>(1) with the <code>-p</code> option produces patch text. You can customize the creation of patch text via the <code>GIT_EXTERNAL_DIFF</code> and the <code>GIT_DIFF_OPTS</code> environment variables (see <code><a href="/docs/linux/man/1-git/">git</a></code>(1)), and the <code>diff</code> attribute (see <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5)). </p>
<p> What the -p option produces is slightly different from the traditional diff format: </p>
<dl>
<dt>
<dd> 1. It is preceded with a &quot;git diff&quot; header that looks like this: </p>
<dl>
<dt>
<dd>
<pre>
diff --git a/file1 b/file2
</pre>
</dl>
<p> The <code>a/</code> and <code>b/</code> filenames are the same unless rename/copy is involved. Especially, even for a creation or a deletion, <code>/dev/null</code> is <i>not</i> used in place of the <code>a/</code> or <code>b/</code> filenames. </p>
<p> When rename/copy is involved, <code>file1</code> and <code>file2</code> show the name of the source file of the rename/copy and the name of the file that rename/copy produces, respectively.</dl>
<dl>
<dt>
<dd> 2. It is followed by one or more extended header lines: </p>
<dl>
<dt>
<dd>
<pre>
old mode &lt;mode&gt;
new mode &lt;mode&gt;
deleted file mode &lt;mode&gt;
new file mode &lt;mode&gt;
copy from &lt;path&gt;
copy to &lt;path&gt;
rename from &lt;path&gt;
rename to &lt;path&gt;
similarity index &lt;number&gt;
dissimilarity index &lt;number&gt;
index &lt;hash&gt;..&lt;hash&gt; &lt;mode&gt;
</pre>
</dl>
<p> File modes are printed as 6-digit octal numbers including the file type and file permission bits. </p>
<p> Path names in extended headers do not include the <code>a/</code> and <code>b/</code> prefixes. </p>
<p> The similarity index is the percentage of unchanged lines, and the dissimilarity index is the percentage of changed lines. It is a rounded down integer, followed by a percent sign. The similarity index value of 100% is thus reserved for two equal files, while 100% dissimilarity means that no line from the old file made it into the new one. </p>
<p> The index line includes the blob object names before and after the change. The &lt;mode&gt; is included if the file mode does not change; otherwise, separate lines indicate the old and the new mode.</dl>
<dl>
<dt>
<dd> 3. Pathnames with &quot;unusual&quot; characters are quoted as explained for the configuration variable <code>core.quotePath</code> (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)).</dl>
<dl>
<dt>
<dd> 4. All the <code>file1</code> files in the output refer to files before the commit, and all the <code>file2</code> files refer to files after the commit. It is incorrect to apply each change to each file sequentially. For example, this patch will swap a and b: </p>
<dl>
<dt>
<dd>
<pre>
diff --git a/a b/b
rename from a
rename to b
diff --git a/b b/a
rename from b
rename to a
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> 5. Hunk headers mention the name of the function to which the hunk applies. See &quot;Defining a custom hunk-header&quot; in <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5) for details of how to tailor to this to specific languages.</dl>
<h2>COMBINED DIFF FORMAT</h2>
<p> Any diff-generating command can take the <code>-c</code> or <code>&#8211;cc</code> option to produce a <i>combined diff</i> when showing a merge. This is the default format when showing merges with <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1) or <code><a href="/docs/linux/man/1-git-show/">git-show</a></code>(1). Note also that you can give suitable <code>&#8211;diff-merges</code> option to any of these commands to force generation of diffs in specific format. </p>
<p> A &quot;combined diff&quot; format looks like this: </p>
<dl>
<dt>
<dd>
diff&#8211; combined describe.c<br />
    index fabadb8,<br />
    cc95eb0..4866510 &#8212; -a / describe.c++ + b / describe.c<br />
                                                @ @ @-98,<br />
    20 &#8211; 98, 12 + 98, 20 @ @ @ return (a_date &gt; b_date) ? -1 : (a_date == b_date) ? 0<br />
                                                                                  : 1;<br />
}<br />
&#8211; static void describe(char *arg) &#8211; static void describe(struct commit *cmit, int last_one)++ static void describe(char *arg, int last_one)<br />
{<br />
    +unsigned char sha1[20];<br />
    +struct commit *cmit;<br />
    struct commit_list *list;<br />
    static int initialized = 0;<br />
    struct commit_name *n;<br />
    +if (get_sha1(arg, sha1) &lt; 0) + usage(describe_usage);<br />
    +cmit = lookup_commit_reference(sha1);<br />
    +if (!cmit) + usage(describe_usage);<br />
    +if (!initialized)<br />
    {<br />
        initialized = 1;<br />
        for_each_ref(get_name);
</dl>
<dl>
<dt>
<dd> 1. It is preceded with a &quot;git diff&quot; header, that looks like this (when the <code>-c</code> option is used): </p>
<dl>
<dt>
<dd>
<pre>
diff --combined file
</pre>
</dl>
<p> or like this (when the <code>&#8211;cc</code> option is used): </p>
<dl>
<dt>
<dd>
<pre>
diff --cc file
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> 2. It is followed by one or more extended header lines (this example shows a merge with two parents): </p>
<dl>
<dt>
<dd>
<pre>
index &lt;hash&gt;,&lt;hash&gt;..&lt;hash&gt;
mode &lt;mode&gt;,&lt;mode&gt;..&lt;mode&gt;
new file mode &lt;mode&gt;
deleted file mode &lt;mode&gt;,&lt;mode&gt;
</pre>
</dl>
<p> The <code>mode &lt;mode&gt;,&lt;mode&gt;..&lt;mode&gt;</code> line appears only if at least one of the &lt;mode&gt; is different from the rest. Extended headers with information about detected contents movement (renames and copying detection) are designed to work with diff of two &lt;tree-ish&gt; and are not used by combined diff format.</dl>
<dl>
<dt>
<dd> 3. It is followed by two-line from-file/to-file header </p>
<dl>
<dt>
<dd>
<pre>
--- a/file
+++ b/file
</pre>
</dl>
<p> Similar to two-line header for traditional <i>unified</i> diff format, <code>/dev/null</code> is used to signal created or deleted files. </p>
<p> However, if the &#8211;combined-all-paths option is provided, instead of a two-line from-file/to-file you get a N+1 line from-file/to-file header, where N is the number of parents in the merge commit </p>
<dl>
<dt>
<dd>
<pre><code>
-- -a / file-- - a / file-- - a / file++ + b / file
</code></pre>
</dl>
<p> This extended format can be useful if rename or copy detection is active, to allow you to see the original name of the file in different parents.</dl>
<dl>
<dt>
<dd> 4. Chunk header format is modified to prevent people from accidentally feeding it to <code>patch -p1</code>. Combined diff format was created for review of merge commit changes, and was not meant to be applied. The change is similar to the change in the extended <i>index</i> header: </p>
<dl>
<dt>
<dd>
<pre>
@@@ &lt;from-file-range&gt; &lt;from-file-range&gt; &lt;to-file-range&gt; @@@
</pre>
</dl>
<p> There are (number of parents + 1) <code>@</code> characters in the chunk header for combined diff format.</dl>
<p> Unlike the traditional <i>unified</i> diff format, which shows two files A and B with a single column that has <code>&#8211;</code> (minus &#8212; appears in A but removed in B), <code>+</code> (plus &#8212; missing in A but added to B), or <code>&quot; &quot;</code> (space &#8212; unchanged) prefix, this format compares two or more files file1, file2,&#8230; with one file X, and shows how X differs from each of fileN. One column for each of fileN is prepended to the output line to note how X&#8217;s line is different from it. </p>
<p> A <code>&#8211;</code> character in the column N means that the line appears in fileN but it does not appear in the result. A <code>+</code> character in the column N means that the line appears in the result, and fileN does not have that line (in other words, the line was added, from the point of view of that parent). </p>
<p> In the above example output, the function signature was changed from both files (hence two <code>&#8211;</code> removals from both file1 and file2, plus <code>++</code> to mean one line that was added does not appear in either file1 or file2). Also eight other lines are the same from file1 but do not appear in file2 (hence prefixed with <code>+</code>). </p>
<p> When shown by <code>git diff-tree -c</code>, it compares the parents of a merge commit with the merge result (i.e. file1..fileN are the parents). When shown by <code>git diff-files -c</code>, it compares the two unresolved merge parents with the working tree file (i.e. file1 is stage 2 aka &quot;our version&quot;, file2 is stage 3 aka &quot;their version&quot;).</p>
<h2>EXAMPLES</h2>
<p> <code>git log &#8211;no-merges</code></p>
<dl>
<dt>
<dd> Show the whole commit history, but skip any merges</dl>
<p> <code>git log v2.6.12.. include/scsi drivers/scsi</code></p>
<dl>
<dt>
<dd> Show all commits since version <i>v2.6.12</i> that changed any file in the <code>include/scsi</code> or <code>drivers/scsi</code> subdirectories</dl>
<p> <code>git log &#8211;since=&quot;2 weeks ago&quot; &#8212; gitk</code></p>
<dl>
<dt>
<dd> Show the changes during the last two weeks to the file <i>gitk</i>. The <code>&#8212;</code> is necessary to avoid confusion with the <code>branch</code> named <i>gitk</i></dl>
<p> <code>git log &#8211;name-status release..test</code></p>
<dl>
<dt>
<dd> Show the commits that are in the &quot;test&quot; branch but not yet in the &quot;release&quot; branch, along with the list of paths each commit modifies.</dl>
<p> <code>git log &#8211;follow builtin/rev-list.c</code></p>
<dl>
<dt>
<dd> Shows the commits that changed <code>builtin/rev-list.c</code>, including those commits that occurred before the file was given its present name.</dl>
<p> <code>git log &#8211;branches &#8211;not &#8211;remotes=origin</code></p>
<dl>
<dt>
<dd> Shows all commits that are in any of local branches but not in any of remote-tracking branches for <i>origin</i> (what you have that origin doesn&#8217;t).</dl>
<p> <code>git log master &#8211;not &#8211;remotes=*/master</code></p>
<dl>
<dt>
<dd> Shows all commits that are in local master but not in any remote repository master branches.</dl>
<p> <code>git log -p -m &#8211;first-parent</code></p>
<dl>
<dt>
<dd> Shows the history including change diffs, but only from the &#8220;main branch&#8221; perspective, skipping commits that come from merged branches, and showing full diffs of changes introduced by the merges. This makes sense only when following a strict policy of merging all topic branches when staying on a single integration branch.</dl>
<p> <code>git log -L &#8216;/int main/&#8217;,/^}/:main.c</code></p>
<dl>
<dt>
<dd> Shows how the function <code>main()</code> in the file <code>main.c</code> evolved over time.</dl>
<p> <code>git log -3</code></p>
<dl>
<dt>
<dd> Limits the number of commits to show to 3.</dl>
<h2>DISCUSSION</h2>
<p> Git is to some extent character encoding agnostic. </p>
<dl>
<dt>
<dd> &bull; The contents of the blob objects are uninterpreted sequences of bytes. There is no encoding translation at the core level.</dl>
<dl>
<dt>
<dd> &bull; Path names are encoded in UTF-8 normalization form C. This applies to tree objects, the index file, ref names, as well as path names in command line arguments, environment variables and config files (<code>.git/config</code> (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)), <code><a href="/docs/linux/man/5-gitignore/">gitignore</a></code>(5), <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5) and <code><a href="/docs/linux/man/5-gitmodules/">gitmodules</a></code>(5)). </p>
<p> Note that Git at the core level treats path names simply as sequences of non-NUL bytes, there are no path name encoding conversions (except on Mac and Windows). Therefore, using non-ASCII path names will mostly work even on platforms and file systems that use legacy extended ASCII encodings. However, repositories created on such systems will not work properly on UTF-8-based systems (e.g. Linux, Mac, Windows) and vice versa. Additionally, many Git-based tools simply assume path names to be UTF-8 and will fail to display other encodings correctly.</dl>
<dl>
<dt>
<dd> &bull; Commit log messages are typically encoded in UTF-8, but other extended ASCII encodings are also supported. This includes ISO-8859-x, CP125x and many others, but <i>not</i> UTF-16/32, EBCDIC and CJK multi-byte encodings (GBK, Shift-JIS, Big5, EUC-x, CP9xx etc.).</dl>
<p> Although we encourage that the commit log messages are encoded in UTF-8, both the core and Git Porcelain are designed not to force UTF-8 on projects. If all participants of a particular project find it more convenient to use legacy encodings, Git does not forbid it. However, there are a few things to keep in mind. </p>
<dl>
<dt>
<dd> 1. <i>git commit</i> and <i>git commit-tree</i> issues a warning if the commit log message given to it does not look like a valid UTF-8 string, unless you explicitly say your project uses a legacy encoding. The way to say this is to have <code>i18n.commitEncoding</code> in <code>.git/config</code> file, like this: </p>
<dl>
<dt>
<dd>
<pre>
[i18n]
        commitEncoding = ISO-8859-1
</pre>
</dl>
<p> Commit objects created with the above setting record the value of <code>i18n.commitEncoding</code> in its <code>encoding</code> header. This is to help other people who look at them later. Lack of this header implies that the commit log message is encoded in UTF-8.</dl>
<dl>
<dt>
<dd> 2. <i>git log</i>, <i>git show</i>, <i>git blame</i> and friends look at the <code>encoding</code> header of a commit object, and try to re-code the log message into UTF-8 unless otherwise specified. You can specify the desired output encoding with <code>i18n.logOutputEncoding</code> in <code>.git/config</code> file, like this: </p>
<dl>
<dt>
<dd>
<pre>
[i18n]
        logOutputEncoding = ISO-8859-1
</pre>
</dl>
<p> If you do not have this configuration variable, the value of <code>i18n.commitEncoding</code> is used instead.</dl>
<p> Note that we deliberately chose not to re-code the commit log message when a commit is made to force UTF-8 at the commit object level, because re-coding to UTF-8 is not necessarily a reversible operation.</p>
<h2>CONFIGURATION</h2>
<p> See <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1) for core variables and <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1) for settings related to diff generation. </p>
<p> format.pretty</p>
<dl>
<dt>
<dd> Default for the <code>&#8211;format</code> option. (See <i>Pretty Formats</i> above.) Defaults to <code>medium</code>.</dl>
<p> i18n.logOutputEncoding</p>
<dl>
<dt>
<dd> Encoding to use when displaying logs. (See <i>Discussion</i> above.) Defaults to the value of <code>i18n.commitEncoding</code> if set, and UTF-8 otherwise.</dl>
<p> log.date</p>
<dl>
<dt>
<dd> Default format for human-readable dates. (Compare the <code>&#8211;date</code> option.) Defaults to &quot;default&quot;, which means to write dates like <code>Sat May 8 19:35:34 2010 -0500</code>. </p>
<p> If the format is set to &quot;auto:foo&quot; and the pager is in use, format &quot;foo&quot; will be the used for the date format. Otherwise &quot;default&quot; will be used.</dl>
<p> log.follow</p>
<dl>
<dt>
<dd> If <code>true</code>, <code>git log</code> will act as if the <code>&#8211;follow</code> option was used when a single &lt;path&gt; is given. This has the same limitations as <code>&#8211;follow</code>, i.e. it cannot be used to follow multiple files and does not work well on non-linear history.</dl>
<p> log.showRoot</p>
<dl>
<dt>
<dd> If <code>false</code>, <code>git log</code> and related commands will not treat the initial commit as a big creation event. Any root commits in <code>git log -p</code> output would be shown without a diff attached. The default is <code>true</code>.</dl>
<p> log.showSignature</p>
<dl>
<dt>
<dd> If <code>true</code>, <code>git log</code> and related commands will act as if the <code>&#8211;show-signature</code> option was passed to them.</dl>
<p> mailmap.*</p>
<dl>
<dt>
<dd> See <code><a href="/docs/linux/man/1-git-shortlog/">git-shortlog</a></code>(1).</dl>
<p> notes.displayRef</p>
<dl>
<dt>
<dd> Which refs, in addition to the default set by <code>core.notesRef</code> or <code>GIT_NOTES_REF</code>, to read notes from when showing commit messages with the <code>log</code> family of commands. See <code><a href="/docs/linux/man/1-git-notes/">git-notes</a></code>(1). </p>
<p> May be an unabbreviated ref name or a glob and may be specified multiple times. A warning will be issued for refs that do not exist, but a glob that does not match any refs is silently ignored. </p>
<p> This setting can be disabled by the <code>&#8211;no-notes</code> option, overridden by the <code>GIT_NOTES_DISPLAY_REF</code> environment variable, and overridden by the <code>&#8211;notes=&lt;ref&gt;</code> option.</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>

---
title: "git-shortlog(1)"
name: "git-shortlog"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-shortlog/"
description: "git-shortlog – Summarize ‘git log’ output"
---

<h2 class="name">NAME</h2>
<p> git-shortlog &#8211; Summarize &#8216;git log&#8217; output </p>
<h2>SYNOPSIS</h2>
<pre><code>
git shortlog[&lt;options&gt;][&lt;revision range&gt;][[--]&lt;path&gt;...] git log-- pretty = short | git shortlog[&lt;options&gt;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Summarizes <i>git log</i> output in a format suitable for inclusion in release announcements. Each commit will be grouped by author and title. </p>
<p> Additionally, &quot;[PATCH]&quot; will be stripped from the commit description. </p>
<p> If no revisions are passed on the command line and either standard input is not a terminal or there is no current branch, <i>git shortlog</i> will output a summary of the log read from standard input, without reference to the current repository.</p>
<h2>OPTIONS</h2>
<p> -n, &#8211;numbered</p>
<dl>
<dt>
<dd> Sort output according to the number of commits per author instead of author alphabetic order.</dl>
<p> -s, &#8211;summary</p>
<dl>
<dt>
<dd> Suppress commit description and provide a commit count summary only.</dl>
<p> -e, &#8211;email</p>
<dl>
<dt>
<dd> Show the email address of each author.</dl>
<p> &#8211;format[=&lt;format&gt;]</p>
<dl>
<dt>
<dd> Instead of the commit subject, use some other information to describe each commit. <i>&lt;format&gt;</i> can be any string accepted by the <code>&#8211;format</code> option of <i>git log</i>, such as <i>* [%h] %s</i>. (See the &quot;PRETTY FORMATS&quot; section of <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1).) </p>
<dl>
<dt>
<dd>
<pre>
Each pretty-printed commit will be rewrapped before it is shown.
</pre>
</dl>
</dl>
<p> &#8211;group=&lt;type&gt;</p>
<dl>
<dt>
<dd> Group commits based on <code>&lt;type&gt;</code>. If no <code>&#8211;group</code> option is specified, the default is <code>author</code>. <code>&lt;type&gt;</code> is one of: </p>
<dl>
<dt>
<dd> &bull; <code>author</code>, commits are grouped by author</dl>
<dl>
<dt>
<dd> &bull; <code>committer</code>, commits are grouped by committer (the same as <code>-c</code>)</dl>
<dl>
<dt>
<dd> &bull; <code>trailer:&lt;field&gt;</code>, the <code>&lt;field&gt;</code> is interpreted as a case-insensitive commit message trailer (see <code><a href="/docs/linux/man/1-git-interpret-trailers/">git-interpret-trailers</a></code>(1)). For example, if your project uses <code>Reviewed-by</code> trailers, you might want to see who has been reviewing with <code>git shortlog -ns &#8211;group=trailer:reviewed-by</code>. </p>
<p> Note that commits that do not include the trailer will not be counted. Likewise, commits with multiple trailers (e.g., multiple signoffs) may be counted more than once (but only once per unique trailer value in that commit). </p>
<p> Shortlog will attempt to parse each trailer value as a <code>name &lt;email&gt;</code> identity. If successful, the mailmap is applied and the email is omitted unless the <code>&#8211;email</code> option is specified. If the value cannot be parsed as an identity, it will be taken literally and completely.</dl>
<p> If <code>&#8211;group</code> is specified multiple times, commits are counted under each value (but again, only once per unique value in that commit). For example, <code>git shortlog &#8211;group=author &#8211;group=trailer:co-authored-by</code> counts both authors and co-authors.</dl>
<p> -c, &#8211;committer</p>
<dl>
<dt>
<dd> This is an alias for <code>&#8211;group=committer</code>.</dl>
<p> -w[&lt;width&gt;[,&lt;indent1&gt;[,&lt;indent2&gt;]]]</p>
<dl>
<dt>
<dd> Linewrap the output by wrapping each line at <code>width</code>. The first line of each entry is indented by <code>indent1</code> spaces, and the second and subsequent lines are indented by <code>indent2</code> spaces. <code>width</code>, <code>indent1</code>, and <code>indent2</code> default to 76, 6 and 9 respectively. </p>
<p> If width is <code>0</code> (zero) then indent the lines of the output without wrapping them.</dl>
<p> &lt;revision range&gt;</p>
<dl>
<dt>
<dd> Show only commits in the specified revision range. When no &lt;revision range&gt; is specified, it defaults to <code>HEAD</code> (i.e. the whole history leading to the current commit). <code>origin..HEAD</code> specifies all the commits reachable from the current commit (i.e. <code>HEAD</code>), but not from <code>origin</code>. For a complete list of ways to spell &lt;revision range&gt;, see the &quot;Specifying Ranges&quot; section of <code><a href="/docs/linux/man/7-gitrevisions/">gitrevisions</a></code>(7).</dl>
<p> [&#8211;] &lt;path&gt;&#8230;</p>
<dl>
<dt>
<dd> Consider only commits that are enough to explain how the files that match the specified paths came to be. </p>
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
<dd> Follow only the first parent commit upon seeing a merge commit. This option can give a better overview when viewing the evolution of a particular topic branch, because merges into a topic branch tend to be only about adjusting to updated upstream from time to time, and this option allows you to ignore the individual commits brought in to your history by such a merge.</dl>
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
<pre><code>
.- A-- - M--.N / /    \ / I B R
         \ / /
          \ / /
           `-- -X--'
</code></pre>
</dl>
<p> Notice that since <code>M</code> is reachable from <code>R</code>, the edge from <code>N</code> to <code>M</code> was simplified away. However, <code>N</code> still appears in the history as an important commit because it &quot;pulled&quot; the change <code>R</code> into the main branch.</dl>
<p> The <code>&#8211;simplify-by-decoration</code> option allows you to view only the big picture of the topology of the history, by omitting commits that are not referenced by tags. Commits are marked as !TREESAME (in other words, kept after history simplification rules described above) if (1) they are referenced by tags, or (2) they change the contents of the paths given on the command line. All other commits are marked as TREESAME (subject to be simplified away).</p>
<h2>MAPPING AUTHORS</h2>
<p> See <code><a href="/docs/linux/man/5-gitmailmap/">gitmailmap</a></code>(5). </p>
<p> Note that if <code>git shortlog</code> is run outside of a repository (to process log contents on standard input), it will look for a <code>.mailmap</code> file in the current directory.</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>

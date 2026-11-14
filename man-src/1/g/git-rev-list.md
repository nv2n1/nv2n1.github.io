---
title: "git-rev-list(1)"
name: "git-rev-list"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-rev-list/"
description: "git-rev-list – Lists commit objects in reverse chronological order"
---

<h2 class="name">NAME</h2>
<p> git-rev-list &#8211; Lists commit objects in reverse chronological order </p>
<h2>SYNOPSIS</h2>
<pre><code>
git rev - list[&lt;options&gt;]&lt;commit&gt;...[[--]&lt;path&gt;...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> List commits that are reachable by following the <code>parent</code> links from the given commit(s), but exclude commits that are reachable from the one(s) given with a <i>^</i> in front of them. The output is given in reverse chronological order by default. </p>
<p> You can think of this as a set operation. Commits reachable from any of the commits given on the command line form a set, and then commits reachable from any of the ones given with <i>^</i> in front are subtracted from that set. The remaining commits are what comes out in the command&#8217;s output. Various other options and paths parameters can be used to further limit the result. </p>
<p> Thus, the following command: </p>
<dl>
<dt>
<dd>
<pre>
$ git rev-list foo bar ^baz
</pre>
</dl>
<p> means &quot;list all the commits which are reachable from <i>foo</i> or <i>bar</i>, but not from <i>baz</i>&quot;. </p>
<p> A special notation &quot;<i>&lt;commit1&gt;</i>..<i>&lt;commit2&gt;</i>&quot; can be used as a short-hand for &quot;^<i>&lt;commit1&gt;</i> <i>&lt;commit2&gt;</i>&quot;. For example, either of the following may be used interchangeably: </p>
<dl>
<dt>
<dd>
<pre>
$ git rev-list origin..HEAD
$ git rev-list HEAD ^origin
</pre>
</dl>
<p> Another special notation is &quot;<i>&lt;commit1&gt;</i>&#8230;<i>&lt;commit2&gt;</i>&quot; which is useful for merges. The resulting set of commits is the symmetric difference between the two operands. The following two commands are equivalent: </p>
<dl>
<dt>
<dd>
<pre>
$ git rev-list A B --not $(git merge-base --all A B)
$ git rev-list A...B
</pre>
</dl>
<p> <i>rev-list</i> is a very essential Git command, since it provides the ability to build and traverse commit ancestry graphs. For this reason, it has a lot of different options that enables it to be used by commands as different as <i>git bisect</i> and <i>git repack</i>.</p>
<h2>OPTIONS</h2>
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
<p> &#8211;max-age=&lt;timestamp&gt;, &#8211;min-age=&lt;timestamp&gt;</p>
<dl>
<dt>
<dd> Limit the commits output to specified time range.</dl>
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
<dd> Limit the commits output to ones with log message that matches the specified pattern (regular expression). With more than one <code>&#8211;grep=&lt;pattern&gt;</code>, commits whose message matches any of the given patterns are chosen (but see <code>&#8211;all-match</code>).</dl>
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
<p> &#8211;stdin</p>
<dl>
<dt>
<dd> In addition to the <i>&lt;commit&gt;</i> listed on the command line, read them from the standard input. If a <code>&#8212;</code> separator is seen, stop reading commits and start reading paths to limit the result.</dl>
<p> &#8211;quiet</p>
<dl>
<dt>
<dd> Don&#8217;t print anything to standard output. This form is primarily meant to allow the caller to test the exit status to see if a range of objects is fully connected (or not). It is faster than redirecting stdout to <code>/dev/null</code> as the output does not have to be formatted.</dl>
<p> &#8211;disk-usage</p>
<dl>
<dt>
<dd> Suppress normal output; instead, print the sum of the bytes used for on-disk storage by the selected commits or objects. This is equivalent to piping the output into <code>git cat-file &#8211;batch-check=&#8217;%(objectsize:disk)&#8217;</code>, except that it runs much faster (especially with <code>&#8211;use-bitmap-index</code>). See the <code>CAVEATS</code> section in <code><a href="/docs/linux/man/1-git-cat-file/">git-cat-file</a></code>(1) for the limitations of what &quot;on-disk storage&quot; means.</dl>
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
<p> &#8211;use-bitmap-index</p>
<dl>
<dt>
<dd> Try to speed up the traversal using the pack bitmap index (if one is available). Note that when traversing with <code>&#8211;objects</code>, trees and blobs will not have their associated path printed.</dl>
<p> &#8211;progress=&lt;header&gt;</p>
<dl>
<dt>
<dd> Show progress reports on stderr as objects are considered. The <code>&lt;header&gt;</code> text will be printed with each progress update.</dl>
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
<h3>Bisection Helpers</h3>
<p> &#8211;bisect</p>
<dl>
<dt>
<dd> Limit output to the one commit object which is roughly halfway between included and excluded commits. Note that the bad bisection ref <code>refs/bisect/bad</code> is added to the included commits (if it exists) and the good bisection refs <code>refs/bisect/good-*</code> are added to the excluded commits (if they exist). Thus, supposing there are no refs in <code>refs/bisect/</code>, if </p>
<dl>
<dt>
<dd>
<pre>
        $ git rev-list --bisect foo ^bar ^baz
</pre>
</dl>
<p> outputs <i>midpoint</i>, the output of the two commands </p>
<dl>
<dt>
<dd>
<pre>
        $ git rev-list foo ^midpoint
        $ git rev-list midpoint ^bar ^baz
</pre>
</dl>
<p> would be of roughly the same length. Finding the change which introduces a regression is thus reduced to a binary search: repeatedly generate and test new &#8216;midpoint&#8217;s until the commit chain is of length one.</dl>
<p> &#8211;bisect-vars</p>
<dl>
<dt>
<dd> This calculates the same as <code>&#8211;bisect</code>, except that refs in <code>refs/bisect/</code> are not used, and except that this outputs text ready to be eval&#8217;ed by the shell. These lines will assign the name of the midpoint revision to the variable <code>bisect_rev</code>, and the expected number of commits to be tested after <code>bisect_rev</code> is tested to <code>bisect_nr</code>, the expected number of commits to be tested if <code>bisect_rev</code> turns out to be good to <code>bisect_good</code>, the expected number of commits to be tested if <code>bisect_rev</code> turns out to be bad to <code>bisect_bad</code>, and the number of commits we are bisecting right now to <code>bisect_all</code>.</dl>
<p> &#8211;bisect-all</p>
<dl>
<dt>
<dd> This outputs all the commit objects between the included and excluded commits, ordered by their distance to the included and excluded commits. Refs in <code>refs/bisect/</code> are not used. The farthest from them is displayed first. (This is the only one displayed by <code>&#8211;bisect</code>.) </p>
<p> This is useful because it makes it easy to choose a good commit to test when you want to avoid to test some of them for some reason (they may not compile for example). </p>
<p> This option can be used along with <code>&#8211;bisect-vars</code>, in this case, after all the sorted commit objects, there will be the same text as if <code>&#8211;bisect-vars</code> had been used alone.</dl>
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
<p> &#8211;objects</p>
<dl>
<dt>
<dd> Print the object IDs of any object referenced by the listed commits. <code>&#8211;objects foo ^bar</code> thus means &#8220;send me all object IDs which I need to download if I have the commit object <i>bar</i> but not <i>foo</i>&#8220;.</dl>
<p> &#8211;in-commit-order</p>
<dl>
<dt>
<dd> Print tree and blob ids in order of the commits. The tree and blob ids are printed after they are first referenced by a commit.</dl>
<p> &#8211;objects-edge</p>
<dl>
<dt>
<dd> Similar to <code>&#8211;objects</code>, but also print the IDs of excluded commits prefixed with a &#8220;-&#8221; character. This is used by <code><a href="/docs/linux/man/1-git-pack-objects/">git-pack-objects</a></code>(1) to build a &#8220;thin&#8221; pack, which records objects in deltified form based on objects contained in these excluded commits to reduce network traffic.</dl>
<p> &#8211;objects-edge-aggressive</p>
<dl>
<dt>
<dd> Similar to <code>&#8211;objects-edge</code>, but it tries harder to find excluded commits at the cost of increased time. This is used instead of <code>&#8211;objects-edge</code> to build &#8220;thin&#8221; packs for shallow repositories.</dl>
<p> &#8211;indexed-objects</p>
<dl>
<dt>
<dd> Pretend as if all trees and blobs used by the index are listed on the command line. Note that you probably want to use <code>&#8211;objects</code>, too.</dl>
<p> &#8211;unpacked</p>
<dl>
<dt>
<dd> Only useful with <code>&#8211;objects</code>; print the object IDs that are not in packs.</dl>
<p> &#8211;object-names</p>
<dl>
<dt>
<dd> Only useful with <code>&#8211;objects</code>; print the names of the object IDs that are found. This is the default behavior.</dl>
<p> &#8211;no-object-names</p>
<dl>
<dt>
<dd> Only useful with <code>&#8211;objects</code>; does not print the names of the object IDs that are found. This inverts <code>&#8211;object-names</code>. This flag allows the output to be more easily parsed by commands such as <code><a href="/docs/linux/man/1-git-cat-file/">git-cat-file</a></code>(1).</dl>
<p> &#8211;filter=&lt;filter-spec&gt;</p>
<dl>
<dt>
<dd> Only useful with one of the <code>&#8211;objects*</code>; omits objects (usually blobs) from the list of printed objects. The <i>&lt;filter-spec&gt;</i> may be one of the following: </p>
<p> The form <i>&#8211;filter=blob:none</i> omits all blobs. </p>
<p> The form <i>&#8211;filter=blob:limit=&lt;n&gt;[kmg]</i> omits blobs larger than n bytes or units. n may be zero. The suffixes k, m, and g can be used to name units in KiB, MiB, or GiB. For example, <i>blob:limit=1k</i> is the same as <i>blob:limit=1024</i>. </p>
<p> The form <i>&#8211;filter=object:type=(tag|commit|tree|blob)</i> omits all objects which are not of the requested type. </p>
<p> The form <i>&#8211;filter=sparse:oid=&lt;blob-ish&gt;</i> uses a sparse-checkout specification contained in the blob (or blob-expression) <i>&lt;blob-ish&gt;</i> to omit blobs that would not be required for a sparse checkout on the requested refs. </p>
<p> The form <i>&#8211;filter=tree:&lt;depth&gt;</i> omits all blobs and trees whose depth from the root tree is &gt;= &lt;depth&gt; (minimum depth if an object is located at multiple depths in the commits traversed). &lt;depth&gt;=0 will not include any trees or blobs unless included explicitly in the command-line (or standard input when &#8211;stdin is used). &lt;depth&gt;=1 will include only the tree and blobs which are referenced directly by a commit reachable from &lt;commit&gt; or an explicitly-given object. &lt;depth&gt;=2 is like &lt;depth&gt;=1 while also including trees and blobs one more level removed from an explicitly-given commit or tree. </p>
<p> Note that the form <i>&#8211;filter=sparse:path=&lt;path&gt;</i> that wants to read from an arbitrary path on the filesystem has been dropped for security reasons. </p>
<p> Multiple <i>&#8211;filter=</i> flags can be specified to combine filters. Only objects which are accepted by every filter are included. </p>
<p> The form <i>&#8211;filter=combine:&lt;filter1&gt;+&lt;filter2&gt;+&#8230;&lt;filterN&gt;</i> can also be used to combined several filters, but this is harder than just repeating the <i>&#8211;filter</i> flag and is usually not necessary. Filters are joined by <i>+</i> and individual filters are %-encoded (i.e. URL-encoded). Besides the <i>+</i> and <i>%</i> characters, the following characters are reserved and also must be encoded: <code>~!@#$^&amp;*()[]{}\;&quot;,&lt;&gt;?</code><code>&#8216;`</code> as well as all characters with ASCII code &lt;= <code>0x20</code>, which includes space and newline. </p>
<p> Other arbitrary characters can also be encoded. For instance, <i>combine:tree:3+blob:none</i> and <i>combine:tree%3A3+blob%3Anone</i> are equivalent.</dl>
<p> &#8211;no-filter</p>
<dl>
<dt>
<dd> Turn off any previous <code>&#8211;filter=</code> argument.</dl>
<p> &#8211;filter-provided-objects</p>
<dl>
<dt>
<dd> Filter the list of explicitly provided objects, which would otherwise always be printed even if they did not match any of the filters. Only useful with <code>&#8211;filter=</code>.</dl>
<p> &#8211;filter-print-omitted</p>
<dl>
<dt>
<dd> Only useful with <code>&#8211;filter=</code>; prints a list of the objects omitted by the filter. Object IDs are prefixed with a &#8220;~&#8221; character.</dl>
<p> &#8211;missing=&lt;missing-action&gt;</p>
<dl>
<dt>
<dd> A debug option to help with future &quot;partial clone&quot; development. This option specifies how missing objects are handled. </p>
<p> The form <i>&#8211;missing=error</i> requests that rev-list stop with an error if a missing object is encountered. This is the default action. </p>
<p> The form <i>&#8211;missing=allow-any</i> will allow object traversal to continue if a missing object is encountered. Missing objects will silently be omitted from the results. </p>
<p> The form <i>&#8211;missing=allow-promisor</i> is like <i>allow-any</i>, but will only allow object traversal to continue for EXPECTED promisor missing objects. Unexpected missing objects will raise an error. </p>
<p> The form <i>&#8211;missing=print</i> is like <i>allow-any</i>, but will also print a list of the missing objects. Object IDs are prefixed with a &#8220;?&#8221; character.</dl>
<p> &#8211;exclude-promisor-objects</p>
<dl>
<dt>
<dd> (For internal use only.) Prefilter object traversal at promisor boundary. This is used with partial clone. This is stronger than <code>&#8211;missing=allow-promisor</code> because it limits the traversal, rather than just silencing errors about missing objects.</dl>
<p> &#8211;no-walk[=(sorted|unsorted)]</p>
<dl>
<dt>
<dd> Only show the given commits, but do not traverse their ancestors. This has no effect if a range is specified. If the argument <code>unsorted</code> is given, the commits are shown in the order they were given on the command line. Otherwise (if <code>sorted</code> or no argument was given), the commits are shown in reverse chronological order by commit time. Cannot be combined with <code>&#8211;graph</code>.</dl>
<p> &#8211;do-walk</p>
<dl>
<dt>
<dd> Overrides a previous <code>&#8211;no-walk</code>.</dl>
<h3>Commit Formatting</h3>
<p> Using these options, <code><a href="/docs/linux/man/1-git-rev-list/">git-rev-list</a></code>(1) will act similar to the more specialized family of commit log tools: <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1), <code><a href="/docs/linux/man/1-git-show/">git-show</a></code>(1), and <code><a href="/docs/linux/man/1-git-whatchanged/">git-whatchanged</a></code>(1) </p>
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
<p> &#8211;header</p>
<dl>
<dt>
<dd> Print the contents of the commit in raw-format; each record is separated with a NUL character.</dl>
<p> &#8211;no-commit-header</p>
<dl>
<dt>
<dd> Suppress the header line containing &quot;commit&quot; and the object ID printed before the specified format. This has no effect on the built-in formats; only custom formats are affected.</dl>
<p> &#8211;commit-header</p>
<dl>
<dt>
<dd> Overrides a previous <code>&#8211;no-commit-header</code>.</dl>
<p> &#8211;parents</p>
<dl>
<dt>
<dd> Print also the parents of the commit (in the form &quot;commit parent&#8230;&quot;). Also enables parent rewriting, see <i>History Simplification</i> above.</dl>
<p> &#8211;children</p>
<dl>
<dt>
<dd> Print also the children of the commit (in the form &quot;commit child&#8230;&quot;). Also enables parent rewriting, see <i>History Simplification</i> above.</dl>
<p> &#8211;timestamp</p>
<dl>
<dt>
<dd> Print the raw commit timestamp.</dl>
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
<p> &#8211;count</p>
<dl>
<dt>
<dd> Print a number stating how many commits would have been listed, and suppress all other output. When used together with <code>&#8211;left-right</code>, instead print the counts for left and right commits, separated by a tab. When used together with <code>&#8211;cherry-mark</code>, omit patch equivalent commits from these counts and print the count for equivalent commits separated by a tab.</dl>
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
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd> &bull; Print the list of commits reachable from the current branch. </p>
<dl>
<dt>
<dd>
<pre>
git rev-list HEAD
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Print the list of commits on this branch, but not present in the upstream branch. </p>
<dl>
<dt>
<dd>
<pre>
git rev-list @{upstream}..HEAD
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Format commits with their author and commit message (see also the porcelain <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1)). </p>
<dl>
<dt>
<dd>
<pre>
git rev-list --format=medium HEAD
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Format commits along with their diffs (see also the porcelain <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1), which can do this in a single process). </p>
<dl>
<dt>
<dd>
<pre>
git rev-list HEAD |
git diff-tree --stdin --format=medium -p
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Print the list of commits on the current branch that touched any file in the <code>Documentation</code> directory. </p>
<dl>
<dt>
<dd>
<pre>
git rev-list HEAD -- Documentation/
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Print the list of commits authored by you in the past year, on any branch, tag, or other ref. </p>
<dl>
<dt>
<dd>
git rev &#8211; list&#8211; author = you[at] example.com&#8211; since = 1.year.ago &#8211;all
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Print the list of objects reachable from the current branch (i.e., all commits and the blobs and trees they contain). </p>
<dl>
<dt>
<dd>
<pre>
git rev-list --objects HEAD
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Compare the disk size of all reachable objects, versus those reachable from reflogs, versus the total packed size. This can tell you whether running <code>git repack -ad</code> might reduce the repository size (by dropping unreachable objects), and whether expiring reflogs might help. </p>
<dl>
<dt>
<dd>
#reachable objects<br />
git rev &#8211; list&#8211; disk &#8211; usage&#8211; objects&#8211; all<br />
#plus reflogs<br />
                            git rev &#8211;<br />
    list&#8211; disk &#8211; usage&#8211; objects&#8211; all&#8211; reflog<br />
#total disk size used<br />
                      du &#8211;<br />
    c.git / objects / pack/*.pack .git/objects/??/*<br />
# alternative to du: add up &#8220;size&#8221; and &#8220;size-pack&#8221; fields<br />
git count-objects -v
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Report the disk size of each branch, not including objects used by the current branch. This can find outliers that are contributing to a bloated repository size (e.g., because somebody accidentally committed large build artifacts). </p>
<dl>
<dt>
<dd>
git for-each-ref &#8211;format=&#8217;%(refname)&#8217; |<br />
while read branch<br />
do<br />
        size=$(git rev-list &#8211;disk-usage &#8211;objects HEAD..$branch)<br />
        echo &#8220;$size $branch&#8221;<br />
done |<br />
sort -n
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Compare the on-disk size of branches in one group of refs, excluding another. If you co-mingle objects from multiple remotes in a single repository, this can show which remotes are contributing to the repository size (taking the size of <code>origin</code> as a baseline). </p>
<dl>
<dt>
<dd>
<pre><code>
git rev - list-- disk - usage-- objects-- remotes = $suspect-- not --remotes = origin
</code></pre>
</dl>
</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>

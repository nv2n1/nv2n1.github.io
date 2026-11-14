---
title: "git-range-diff(1)"
name: "git-range-diff"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-range-diff/"
description: "git-range-diff – Compare two commit ranges (e.g. two versions of a branch)"
---

<h2 class="name">NAME</h2>
<p> git-range-diff &#8211; Compare two commit ranges (e.g. two versions of a branch) </p>
<h2>SYNOPSIS</h2>
<pre><code>
git range - diff[--color = [&lt;when&gt;]][--no - color][&lt;diff - options&gt;]
                [--no - dual - color][--creation - factor = &lt;factor&gt;]
                [--left - only | --right - only](&lt;range1&gt;&lt;range2&gt; | &lt;rev1&gt;...&lt;rev2&gt; | &lt;base&gt;&lt;rev1&gt;&lt;rev2&gt;)
</code></pre>
<h2>DESCRIPTION</h2>
<p> This command shows the differences between two versions of a patch series, or more generally, two commit ranges (ignoring merge commits). </p>
<p> To that end, it first finds pairs of commits from both commit ranges that correspond with each other. Two commits are said to correspond when the diff between their patches (i.e. the author information, the commit message and the commit diff) is reasonably small compared to the patches&#8217; size. See &#8220;Algorithm&#8220; below for details. </p>
<p> Finally, the list of matching commits is shown in the order of the second commit range, with unmatched commits being inserted just after all of their ancestors have been shown. </p>
<p> There are three ways to specify the commit ranges: </p>
<dl>
<dt>
<dd> &bull; <code>&lt;range1&gt; &lt;range2&gt;</code>: Either commit range can be of the form <code>&lt;base&gt;..&lt;rev&gt;</code>, <code>&lt;rev&gt;^!</code> or <code>&lt;rev&gt;^-&lt;n&gt;</code>. See <code>SPECIFYING RANGES</code> in <code><a href="/docs/linux/man/7-gitrevisions/">gitrevisions</a></code>(7) for more details.</dl>
<dl>
<dt>
<dd> &bull; <code>&lt;rev1&gt;&#8230;&lt;rev2&gt;</code>. This is equivalent to <code>&lt;rev2&gt;..&lt;rev1&gt; &lt;rev1&gt;..&lt;rev2&gt;</code>.</dl>
<dl>
<dt>
<dd> &bull; <code>&lt;base&gt; &lt;rev1&gt; &lt;rev2&gt;</code>: This is equivalent to <code>&lt;base&gt;..&lt;rev1&gt; &lt;base&gt;..&lt;rev2&gt;</code>.</dl>
<h2>OPTIONS</h2>
<p> &#8211;no-dual-color</p>
<dl>
<dt>
<dd> When the commit diffs differ, &#8216;git range-diff` recreates the original diffs&#8217; coloring, and adds outer -/+ diff markers with the <code>background</code> being red/green to make it easier to see e.g. when there was a change in what exact lines were added. </p>
<p> Additionally, the commit diff lines that are only present in the first commit range are shown &quot;dimmed&quot; (this can be overridden using the <code>color.diff.&lt;slot&gt;</code> config setting where <code>&lt;slot&gt;</code> is one of <code>contextDimmed</code>, <code>oldDimmed</code> and <code>newDimmed</code>), and the commit diff lines that are only present in the second commit range are shown in bold (which can be overridden using the config settings <code>color.diff.&lt;slot&gt;</code> with <code>&lt;slot&gt;</code> being one of <code>contextBold</code>, <code>oldBold</code> or <code>newBold</code>). </p>
<p> This is known to <code>range-diff</code> as &quot;dual coloring&quot;. Use <code>&#8211;no-dual-color</code> to revert to color all lines according to the outer diff markers (and completely ignore the inner diff when it comes to color).</dl>
<p> &#8211;creation-factor=&lt;percent&gt;</p>
<dl>
<dt>
<dd> Set the creation/deletion cost fudge factor to <code>&lt;percent&gt;</code>. Defaults to 60. Try a larger value if <code>git range-diff</code> erroneously considers a large change a total rewrite (deletion of one commit and addition of another), and a smaller one in the reverse case. See the &#8220;Algorithm&#8220; section below for an explanation why this is needed.</dl>
<p> &#8211;left-only</p>
<dl>
<dt>
<dd> Suppress commits that are missing from the first specified range (or the &quot;left range&quot; when using the <code>&lt;rev1&gt;&#8230;&lt;rev2&gt;</code> format).</dl>
<p> &#8211;right-only</p>
<dl>
<dt>
<dd> Suppress commits that are missing from the second specified range (or the &quot;right range&quot; when using the <code>&lt;rev1&gt;&#8230;&lt;rev2&gt;</code> format).</dl>
<p> &#8211;[no-]notes[=&lt;ref&gt;]</p>
<dl>
<dt>
<dd> This flag is passed to the <code>git log</code> program (see <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1)) that generates the patches.</dl>
<p> &lt;range1&gt; &lt;range2&gt;</p>
<dl>
<dt>
<dd> Compare the commits specified by the two ranges, where <code>&lt;range1&gt;</code> is considered an older version of <code>&lt;range2&gt;</code>.</dl>
<p> &lt;rev1&gt;&#8230;&lt;rev2&gt;</p>
<dl>
<dt>
<dd> Equivalent to passing <code>&lt;rev2&gt;..&lt;rev1&gt;</code> and <code>&lt;rev1&gt;..&lt;rev2&gt;</code>.</dl>
<p> &lt;base&gt; &lt;rev1&gt; &lt;rev2&gt;</p>
<dl>
<dt>
<dd> Equivalent to passing <code>&lt;base&gt;..&lt;rev1&gt;</code> and <code>&lt;base&gt;..&lt;rev2&gt;</code>. Note that <code>&lt;base&gt;</code> does not need to be the exact branch point of the branches. Example: after rebasing a branch <code>my-topic</code>, <code>git range-diff my-topic@{u} my-topic@{1} my-topic</code> would show the differences introduced by the rebase.</dl>
<p> <code>git range-diff</code> also accepts the regular diff options (see <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1)), most notably the <code>&#8211;color=[&lt;when&gt;]</code> and <code>&#8211;no-color</code> options. These options are used when generating the &quot;diff between patches&quot;, i.e. to compare the author, commit message and diff of corresponding old/new commits. There is currently no means to tweak most of the diff options passed to <code>git log</code> when generating those patches.</p>
<h2>OUTPUT STABILITY</h2>
<p> The output of the <code>range-diff</code> command is subject to change. It is intended to be human-readable porcelain output, not something that can be used across versions of Git to get a textually stable <code>range-diff</code> (as opposed to something like the <code>&#8211;stable</code> option to <code><a href="/docs/linux/man/1-git-patch-id/">git-patch-id</a></code>(1)). There&#8217;s also no equivalent of <code><a href="/docs/linux/man/1-git-apply/">git-apply</a></code>(1) for <code>range-diff</code>, the output is not intended to be machine-readable. </p>
<p> This is particularly true when passing in diff options. Currently some options like <code>&#8211;stat</code> can, as an emergent effect, produce output that&#8217;s quite useless in the context of <code>range-diff</code>. Future versions of <code>range-diff</code> may learn to interpret such options in a manner specific to <code>range-diff</code> (e.g. for <code>&#8211;stat</code> producing human-readable output which summarizes how the diffstat changed).</p>
<h2>CONFIGURATION</h2>
<p> This command uses the <code>diff.color.*</code> and <code>pager.range-diff</code> settings (the latter is on by default). See <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1).</p>
<h2>EXAMPLES</h2>
<p> When a rebase required merge conflicts to be resolved, compare the changes introduced by the rebase directly afterwards using: </p>
<dl>
<dt>
<dd>
$ git range &#8211; diff @{u} @{1} @
</dl>
<p> A typical output of <code>git range-diff</code> would look like this: </p>
<dl>
<dt>
<dd>
-:  &#8212;&#8212;- &gt; 1:  0ddba11 Prepare for the inevitable!<br />
1:  c0debee = 2:  cab005e Add a helpful message at the start<br />
2:  f00dbal ! 3:  decafe1 Describe a bug<br />
    @@ -1,3 +1,3 @@<br />
     Author: A U Thor &lt;author [at] example.com&gt;<br />
    -TODO: Describe a bug<br />
    +Describe a bug<br />
    @@ -324,5 +324,6<br />
      This is expected.<br />
    -+What is unexpected is that it will also crash.<br />
    ++Unexpectedly, it also crashes. This is a bug, and the jury is<br />
    ++still out there how to fix it best. See ticket #314 for details.<br />
      Contact<br />
3:  bedead &lt; -:  &#8212;&#8212;- TO-UNDO
</dl>
<p> In this example, there are 3 old and 3 new commits, where the developer removed the 3rd, added a new one before the first two, and modified the commit message of the 2nd commit as well its diff. </p>
<p> When the output goes to a terminal, it is color-coded by default, just like regular <code>git diff</code>&#8216;s output. In addition, the first line (adding a commit) is green, the last line (deleting a commit) is red, the second line (with a perfect match) is yellow like the commit header of <code>git show</code>&#8216;s output, and the third line colors the old commit red, the new one green and the rest like <code>git show</code>&#8216;s commit header. </p>
<p> A naive color-coded diff of diffs is actually a bit hard to read, though, as it colors the entire lines red or green. The line that added &quot;What is unexpected&quot; in the old commit, for example, is completely red, even if the intent of the old commit was to add something. </p>
<p> To help with that, <code>range</code> uses the <code>&#8211;dual-color</code> mode by default. In this mode, the diff of diffs will retain the original diff colors, and prefix the lines with -/+ markers that have their <code>background</code> red or green, to make it more obvious that they describe how the diff itself changed.</p>
<h2>ALGORITHM</h2>
<p> The general idea is this: we generate a cost matrix between the commits in both commit ranges, then solve the least-cost assignment. </p>
<p> The cost matrix is populated thusly: for each pair of commits, both diffs are generated and the &quot;diff of diffs&quot; is generated, with 3 context lines, then the number of lines in that diff is used as cost. </p>
<p> To avoid false positives (e.g. when a patch has been removed, and an unrelated patch has been added between two iterations of the same patch series), the cost matrix is extended to allow for that, by adding fixed-cost entries for wholesale deletes/adds. </p>
<p> Example: Let commits <code>1&#8211;2</code> be the first iteration of a patch series and <code>A&#8211;C</code> the second iteration. Let&#8217;s assume that <code>A</code> is a cherry-pick of <code>2,</code> and <code>C</code> is a cherry-pick of <code>1</code> but with a small modification (say, a fixed typo). Visualize the commits as a bipartite graph: </p>
<dl>
<dt>
<dd>
<pre>
    1            A
    2            B
                 C
</pre>
</dl>
<p> We are looking for a &quot;best&quot; explanation of the new series in terms of the old one. We can represent an &quot;explanation&quot; as an edge in the graph: </p>
<dl>
<dt>
<dd>
1 A /<br />
    2 &#8212; &#8212; &#8212; &#8211;&#8216;  B C
</dl>
<p> This explanation comes for &quot;free&quot; because there was no change. Similarly <code>C</code> could be explained using <code>1</code>, but that comes at some cost c&gt;0 because of the modification: </p>
<dl>
<dt>
<dd>
1 &#8212; &#8211;.A | /<br />
                2 &#8212; &#8211;+&#8211; -&#8216;  B |<br />
          `&#8211; &#8212; -C<br />
                    c &gt; 0
</dl>
<p> In mathematical terms, what we are looking for is some sort of a minimum cost bipartite matching; &#8216;1` is matched to <code>C</code> at some cost, etc. The underlying graph is in fact a complete bipartite graph; the cost we associate with every edge is the size of the diff between the two commits&#8217; patches. To explain also new commits, we introduce dummy nodes on both sides: </p>
<dl>
<dt>
<dd>
1 &#8212; &#8211;.A | /<br />
                2 &#8212; &#8211;+&#8211; -&#8216;  B |<br />
    o     `&#8211; &#8212; -C<br />
            c &gt; 0 o o<br />
                    o o
</dl>
<p> The cost of an edge <code>o&#8211;C</code> is the size of <code>C</code>&#8216;s diff, modified by a fudge factor that should be smaller than 100%. The cost of an edge <code>o&#8211;o</code> is free. The fudge factor is necessary because even if <code>1</code> and <code>C</code> have nothing in common, they may still share a few empty lines and such, possibly making the assignment <code>1&#8211;C</code>, <code>o&#8211;o</code> slightly cheaper than <code>1&#8211;o</code>, <code>o&#8211;C</code> even if <code>1</code> and <code>C</code> have nothing in common. With the fudge factor we require a much larger common part to consider patches as corresponding. </p>
<p> The overall time needed to compute this algorithm is the time needed to compute n+m commit diffs and then n*m diffs of patches, plus the time needed to compute the least-cost assignment between n and m diffs. Git uses an implementation of the Jonker-Volgenant algorithm to solve the assignment problem, which has cubic runtime complexity. The matching found in this case will look like this: </p>
<dl>
<dt>
<dd>
<pre><code>
1 -- --.A | /
                        2 -- --+-- -'  B
                            .--+-- -- -' o -'  `----- C c &gt;
                0 o-- -- -- -- --o
                    o-- -- -- -- --o
</code></pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>

---
title: "git-merge-base(1)"
name: "git-merge-base"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-merge-base/"
description: "git-merge-base – Find as good common ancestors as possible for a merge"
---

<h2 class="name">NAME</h2>
<p> git-merge-base &#8211; Find as good common ancestors as possible for a merge </p>
<h2>SYNOPSIS</h2>
<pre><code>
git merge - base[-a | --all]&lt;commit&gt;&lt;commit&gt;... git merge - base[-a | --all]-- octopus&lt;commit&gt;... git merge - base-- is - ancestor&lt;commit&gt;&lt;commit&gt; git merge - base-- independent&lt;commit&gt;... git merge - base-- fork - point&lt;ref&gt;[&lt;commit&gt;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <i>git merge-base</i> finds best common ancestor(s) between two commits to use in a three-way merge. One common ancestor is <i>better</i> than another common ancestor if the latter is an ancestor of the former. A common ancestor that does not have any better common ancestor is a <i>best common ancestor</i>, i.e. a <i>merge base</i>. Note that there can be more than one merge base for a pair of commits.</p>
<h2>OPERATION MODES</h2>
<p> As the most common special case, specifying only two commits on the command line means computing the merge base between the given two commits. </p>
<p> More generally, among the two commits to compute the merge base from, one is specified by the first commit argument on the command line; the other commit is a (possibly hypothetical) commit that is a merge across all the remaining commits on the command line. </p>
<p> As a consequence, the <i>merge base</i> is not necessarily contained in each of the commit arguments if more than two commits are specified. This is different from <code><a href="/docs/linux/man/1-git-show-branch/">git-show-branch</a></code>(1) when used with the <code>&#8211;merge-base</code> option. </p>
<p> &#8211;octopus</p>
<dl>
<dt>
<dd> Compute the best common ancestors of all supplied commits, in preparation for an n-way merge. This mimics the behavior of <i>git show-branch &#8211;merge-base</i>.</dl>
<p> &#8211;independent</p>
<dl>
<dt>
<dd> Instead of printing merge bases, print a minimal subset of the supplied commits with the same ancestors. In other words, among the commits given, list those which cannot be reached from any other. This mimics the behavior of <i>git show-branch &#8211;independent</i>.</dl>
<p> &#8211;is-ancestor</p>
<dl>
<dt>
<dd> Check if the first &lt;commit&gt; is an ancestor of the second &lt;commit&gt;, and exit with status 0 if true, or with status 1 if not. Errors are signaled by a non-zero status that is not 1.</dl>
<p> &#8211;fork-point</p>
<dl>
<dt>
<dd> Find the point at which a branch (or any history that leads to &lt;commit&gt;) forked from another branch (or any reference) &lt;ref&gt;. This does not just look for the common ancestor of the two commits, but also takes into account the reflog of &lt;ref&gt; to see if the history leading to &lt;commit&gt; forked from an earlier incarnation of the branch &lt;ref&gt; (see discussion on this mode below).</dl>
<h2>OPTIONS</h2>
<p> -a, &#8211;all</p>
<dl>
<dt>
<dd> Output all merge bases for the commits, instead of just one.</dl>
<h2>DISCUSSION</h2>
<p> Given two commits <i>A</i> and <i>B</i>, <code>git merge-base A B</code> will output a commit which is reachable from both <i>A</i> and <i>B</i> through the parent relationship. </p>
<p> For example, with this topology: </p>
<dl>
<dt>
<dd>
o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; B / &#8212; -o&#8211; &#8211; 1 &#8212; -o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; A
</dl>
<p> the merge base between <i>A</i> and <i>B</i> is <i>1</i>. </p>
<p> Given three commits <i>A</i>, <i>B</i> and <i>C</i>, <code>git merge-base A B C</code> will compute the merge base between <i>A</i> and a hypothetical commit <i>M</i>, which is a merge between <i>B</i> and <i>C</i>. For example, with this topology: </p>
<dl>
<dt>
<dd>
o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; C / / o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; B / / &#8212; -2 &#8212; -1 &#8212; -o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; A
</dl>
<p> the result of <code>git merge-base A B C</code> is <i>1</i>. This is because the equivalent topology with a merge commit <i>M</i> between <i>B</i> and <i>C</i> is: </p>
<dl>
<dt>
<dd>
o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; o / / o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; M / / &#8212; -2 &#8212; -1 &#8212; -o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; A
</dl>
<p> and the result of <code>git merge-base A M</code> is <i>1</i>. Commit <i>2</i> is also a common ancestor between <i>A</i> and <i>M</i>, but <i>1</i> is a better common ancestor, because <i>2</i> is an ancestor of <i>1</i>. Hence, <i>2</i> is not a merge base. </p>
<p> The result of <code>git merge-base &#8211;octopus A B C</code> is <i>2</i>, because <i>2</i> is the best common ancestor of all commits. </p>
<p> When the history involves criss-cross merges, there can be more than one <i>best</i> common ancestor for two commits. For example, with this topology: </p>
<dl>
<dt>
<dd>
&#8212; -1 &#8212; -o&#8211; &#8211; A<br />
    \ / X / &#8212; -2 &#8212; -o&#8211; &#8211; o&#8211; &#8211; B
</dl>
<p> both <i>1</i> and <i>2</i> are merge-bases of A and B. Neither one is better than the other (both are <i>best</i> merge bases). When the <code>&#8211;all</code> option is not given, it is unspecified which best one is output. </p>
<p> A common idiom to check &quot;fast-forward-ness&quot; between two commits A and B is (or at least used to be) to compute the merge base between A and B, and check if it is the same as A, in which case, A is an ancestor of B. You will see this idiom used often in older scripts. </p>
<dl>
<dt>
<dd>
<pre>
A=$(git rev-parse --verify A)
if test &quot;$A&quot; = &quot;$(git merge-base A B)&quot;
then
        ... A is an ancestor of B ...
fi
</pre>
</dl>
<p> In modern git, you can say this in a more direct way: </p>
<dl>
<dt>
<dd>
<pre>
if git merge-base --is-ancestor A B
then
        ... A is an ancestor of B ...
fi
</pre>
</dl>
<p> instead.</p>
<h2>DISCUSSION ON FORK-POINT MODE</h2>
<p> After working on the <code>topic</code> branch created with <code>git switch -c topic origin/master</code>, the history of remote-tracking branch <code>origin/master</code> may have been rewound and rebuilt, leading to a history of this shape: </p>
<dl>
<dt>
<dd>
o&#8211; &#8211; B2 / &#8212; -o&#8211; &#8211; o&#8211; &#8211; B1&#8211; o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; B(origin / master)</p>
<p>                                                      B0</p>
<p>    D0&#8211; &#8211;<br />
    D1&#8211; &#8211; D(topic)
</dl>
<p> where <code>origin/master</code> used to point at commits B0, B1, B2 and now it points at B, and your <code>topic</code> branch was started on top of it back when <code>origin/master</code> was at B0, and you built three commits, D0, D1, and D, on top of it. Imagine that you now want to rebase the work you did on the topic on top of the updated origin/master. </p>
<p> In such a case, <code>git merge-base origin/master topic</code> would return the parent of B0 in the above picture, but B0^..D is <code>not</code> the range of commits you would want to replay on top of B (it includes B0, which is not what you wrote; it is a commit the other side discarded when it moved its tip from B0 to B1). </p>
<p> <code>git merge-base &#8211;fork-point origin/master topic</code> is designed to help in such a case. It takes not only B but also B0, B1, and B2 (i.e. old tips of the remote-tracking branches your repository&#8217;s reflog knows about) into account to see on which commit your topic branch was built and finds B0, allowing you to replay only the commits on your topic, excluding the commits the other side later discarded. </p>
<p> Hence </p>
<dl>
<dt>
<dd>
<pre>
$ fork_point=$(git merge-base --fork-point origin/master topic)
</pre>
</dl>
<p> will find B0, and </p>
<dl>
<dt>
<dd>
<pre>
$ git rebase --onto origin/master $fork_point topic
</pre>
</dl>
<p> will replay D0, D1 and D on top of B to create a new history of this shape: </p>
<dl>
<dt>
<dd>
<pre><code>
o-- - B2 / -- -o-- - o-- - B1-- o-- - o-- - o-- - B(origin / master)
        \ B0 D0 '--D1' --D' (topic - updated)

    D0-- -
    D1-- - D(topic - old)
</code></pre>
</dl>
<p> A caveat is that older reflog entries in your repository may be expired by <code>git gc</code>. If B0 no longer appears in the reflog of the remote-tracking branch <code>origin/master</code>, the <code>&#8211;fork-point</code> mode obviously cannot find it and fails, avoiding to give a random and useless result (such as the parent of B0, like the same command without the <code>&#8211;fork-point</code> option gives). </p>
<p> Also, the remote-tracking branch you use the <code>&#8211;fork-point</code> mode with must be the one your topic forked from its tip. If you forked from an older commit than the tip, this mode would not find the fork point (imagine in the above sample history B0 did not exist, origin/master started at B1, moved to B2 and then B, and you forked your topic at origin/master^ when origin/master was B1; the shape of the history would be the same as above, without B0, and the parent of B1 is what <code>git merge-base origin/master topic</code> correctly finds, but the <code>&#8211;fork-point</code> mode will not, because it is not one of the commits that used to be at the tip of origin/master).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-rev-list/">git-rev-list</a></code>(1), <code><a href="/docs/linux/man/1-git-show-branch/">git-show-branch</a></code>(1), <code><a href="/docs/linux/man/1-git-merge/">git-merge</a></code>(1)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>

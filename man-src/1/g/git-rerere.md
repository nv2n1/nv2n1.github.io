---
title: "git-rerere(1)"
name: "git-rerere"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-rerere/"
description: "git-rerere – Reuse recorded resolution of conflicted merges"
---

<h2 class="name">NAME</h2>
<p> git-rerere &#8211; Reuse recorded resolution of conflicted merges </p>
<h2>SYNOPSIS</h2>
<pre>
<i>git rerere</i> [<i>clear</i>|<i>forget</i> &lt;pathspec&gt;|<i>diff</i>|<i>remaining</i>|<i>status</i>|<i>gc</i>]
</pre>
<h2>DESCRIPTION</h2>
<p> In a workflow employing relatively long lived topic branches, the developer sometimes needs to resolve the same conflicts over and over again until the topic branches are done (either merged to the &quot;release&quot; branch, or sent out and accepted upstream). </p>
<p> This command assists the developer in this process by recording conflicted automerge results and corresponding hand resolve results on the initial manual merge, and applying previously recorded hand resolutions to their corresponding automerge results. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> You need to set the configuration variable <code>rerere.enabled</code> in order to enable this command. </p>
</dl>
<h2>COMMANDS</h2>
<p> Normally, <i>git rerere</i> is run without arguments or user-intervention. However, it has several commands that allow it to interact with its working state. </p>
<p> <i>clear</i></p>
<dl>
<dt>
<dd> Reset the metadata used by rerere if a merge resolution is to be aborted. Calling <i>git am [&#8211;skip|&#8211;abort]</i> or <i>git rebase [&#8211;skip|&#8211;abort]</i> will automatically invoke this command.</dl>
<p> <i>forget</i> &lt;pathspec&gt;</p>
<dl>
<dt>
<dd> Reset the conflict resolutions which rerere has recorded for the current conflict in &lt;pathspec&gt;.</dl>
<p> <i>diff</i></p>
<dl>
<dt>
<dd> Display diffs for the current state of the resolution. It is useful for tracking what has changed while the user is resolving conflicts. Additional arguments are passed directly to the system <i>diff</i> command installed in PATH.</dl>
<p> <i>status</i></p>
<dl>
<dt>
<dd> Print paths with conflicts whose merge resolution rerere will record.</dl>
<p> <i>remaining</i></p>
<dl>
<dt>
<dd> Print paths with conflicts that have not been autoresolved by rerere. This includes paths whose resolutions cannot be tracked by rerere, such as conflicting submodules.</dl>
<p> <i>gc</i></p>
<dl>
<dt>
<dd> Prune records of conflicted merges that occurred a long time ago. By default, unresolved conflicts older than 15 days and resolved conflicts older than 60 days are pruned. These defaults are controlled via the <code>gc.rerereUnresolved</code> and <code>gc.rerereResolved</code> configuration variables respectively.</dl>
<h2>DISCUSSION</h2>
<p> When your topic branch modifies an overlapping area that your master branch (or upstream) touched since your topic branch forked from it, you may want to test it with the latest master, even before your topic branch is ready to be pushed upstream: </p>
<dl>
<dt>
<dd>
<pre><code>
o-- - *-- -o topic / o-- - o-- - o-- - *-- -o-- - o master
</code></pre>
</dl>
<p> For such a test, you need to merge master and topic somehow. One way to do it is to pull master into the topic branch: </p>
<dl>
<dt>
<dd>
$ git switch topic<br />
        $ git merge master<br />
            o&#8211; &#8211;<br />
    *&#8211; -o&#8211; &#8211; +topic / / o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; *&#8211; -o&#8211; &#8211; o master
</dl>
<p> The commits marked with <code>*</code> touch the same area in the same file; you need to resolve the conflicts when creating the commit marked with <code>+</code>. Then you can test the result to make sure your work-in-progress still works with what is in the latest master. </p>
<p> After this test merge, there are two ways to continue your work on the topic. The easiest is to build on top of the test merge commit <code>+</code>, and when your work in the topic branch is finally ready, pull the topic branch into master, and/or ask the upstream to pull from you. By that time, however, the master or the upstream might have been advanced since the test merge <code>+</code>, in which case the final commit graph would look like this: </p>
<dl>
<dt>
<dd>
$ git switch topic<br />
        $ git merge master<br />
            $&#8230; work on both topic and master branches<br />
                $ git switch master<br />
                    $ git merge topic<br />
                        o&#8211; &#8211;<br />
    *&#8211; -o&#8211; &#8211; +&#8211; -o&#8211; &#8211; o topic / / o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; *&#8211; -o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; +master
</dl>
<p> When your topic branch is long-lived, however, your topic branch would end up having many such &quot;Merge from master&quot; commits on it, which would unnecessarily clutter the development history. Readers of the Linux kernel mailing list may remember that Linus complained about such too frequent test merges when a subsystem maintainer asked to pull from a branch full of &quot;useless merges&quot;. </p>
<p> As an alternative, to keep the topic branch clean of test merges, you could blow away the test merge, and keep building on top of the tip before the test merge: </p>
<dl>
<dt>
<dd>
$ git switch topic<br />
        $ git merge master<br />
            $ git reset&#8211; hard HEAD ^<br />
    ;<br />
#rewind the test merge<br />
        $&#8230; work on both topic and master branches<br />
            $ git switch master<br />
                $ git merge topic<br />
                    o&#8211; &#8211;<br />
    *&#8211; -o&#8211; &#8212; &#8212; -o&#8211; &#8211; o topic / o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; *&#8211; -o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; +master
</dl>
<p> This would leave only one merge commit when your topic branch is finally ready and merged into the master branch. This merge would require you to resolve the conflict, introduced by the commits marked with <code>*</code>. However, this conflict is often the same conflict you resolved when you created the test merge you blew away. <i>git rerere</i> helps you resolve this final conflicted merge using the information from your earlier hand resolve. </p>
<p> Running the <i>git rerere</i> command immediately after a conflicted automerge records the conflicted working tree files, with the usual conflict markers <code>&lt;&lt;&lt;&lt;&lt;&lt;&lt;</code>, <code>=======</code>, and <code>&gt;&gt;&gt;&gt;&gt;&gt;&gt;</code> in them. Later, after you are done resolving the conflicts, running <i>git rerere</i> again will record the resolved state of these files. Suppose you did this when you created the test merge of master into the topic branch. </p>
<p> Next time, after seeing the same conflicted automerge, running <i>git rerere</i> will perform a three-way merge between the earlier conflicted automerge, the earlier manual resolution, and the current conflicted automerge. If this three-way merge resolves cleanly, the result is written out to your working tree file, so you do not have to manually resolve it. Note that <i>git rerere</i> leaves the index file alone, so you still need to do the final sanity checks with <code>git diff</code> (or <code>git diff -c</code>) and <i>git add</i> when you are satisfied. </p>
<p> As a convenience measure, <i>git merge</i> automatically invokes <i>git rerere</i> upon exiting with a failed automerge and <i>git rerere</i> records the hand resolve when it is a new conflict, or reuses the earlier hand resolve when it is not. <i>git commit</i> also invokes <i>git rerere</i> when committing a merge result. What this means is that you do not have to do anything special yourself (besides enabling the rerere.enabled config variable). </p>
<p> In our example, when you do the test merge, the manual resolution is recorded, and it will be reused when you do the actual merge later with the updated master and topic branch, as long as the recorded resolution is still applicable. </p>
<p> The information <i>git rerere</i> records is also used when running <i>git rebase</i>. After blowing away the test merge and continuing development on the topic branch: </p>
<dl>
<dt>
<dd>
<pre><code>
o-- - *-- -o-- -- -- -o-- - o topic / o-- - o-- - o-- - *-- -o-- - o-- - o-- - o master $ git rebase master topic o-- - *-- -o-- -- -- -o-- - o topic / o-- - o-- - o-- - *-- -o-- - o-- - o-- - o master
</code></pre>
</dl>
<p> you could run <code>git rebase master topic</code>, to bring yourself up to date before your topic is ready to be sent upstream. This would result in falling back to a three-way merge, and it would conflict the same way as the test merge you resolved earlier. <i>git rerere</i> will be run by <i>git rebase</i> to help you resolve this conflict. </p>
<p> [NOTE] <i>git rerere</i> relies on the conflict markers in the file to detect the conflict. If the file already contains lines that look the same as lines with conflict markers, <i>git rerere</i> may fail to record a conflict resolution. To work around this, the <code>conflict-marker-size</code> setting in <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5) can be used.</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>

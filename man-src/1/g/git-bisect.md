---
title: "git-bisect(1)"
name: "git-bisect"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-bisect/"
description: "git-bisect – Use binary search to find the commit that introduced a bug"
---

<h2 class="name">NAME</h2>
<p> git-bisect &#8211; Use binary search to find the commit that introduced a bug </p>
<h2>SYNOPSIS</h2>
<pre>
<i>git bisect</i> &lt;subcommand&gt; &lt;options&gt;
</pre>
<h2>DESCRIPTION</h2>
<p> The command takes various subcommands, and different options depending on the subcommand: </p>
<dl>
<dt>
<dd>
<pre><code>
git bisect start[--term - {new, bad} = &lt;term&gt; --term - {old, good} = &lt;term&gt;]
                [--no - checkout][--first - parent][&lt;bad&gt;[&lt;good&gt;...]][--][&lt;paths&gt;...] git
                bisect(bad | new | &lt;term - new&gt;)[&lt;rev&gt;] git bisect(good | old | &lt;term - old&gt;)[&lt;rev&gt;...] git bisect terms[--term - good | --term - bad] git bisect skip[(&lt;rev&gt; | &lt;range&gt;)...] git bisect reset[&lt;commit&gt;] git bisect(visualize | view)
                    git bisect replay&lt;logfile&gt; git bisect log
    git bisect run&lt;cmd&gt;... git bisect help
</code></pre>
</dl>
<p> This command uses a binary search algorithm to find which commit in your project&#8217;s history introduced a bug. You use it by first telling it a &quot;bad&quot; commit that is known to contain the bug, and a &quot;good&quot; commit that is known to be before the bug was introduced. Then <code>git bisect</code> picks a commit between those two endpoints and asks you whether the selected commit is &quot;good&quot; or &quot;bad&quot;. It continues narrowing down the range until it finds the exact commit that introduced the change. </p>
<p> In fact, <code>git bisect</code> can be used to find the commit that changed <code>any</code> property of your project; e.g., the commit that fixed a bug, or the commit that caused a benchmark&#8217;s performance to improve. To support this more general usage, the terms &quot;old&quot; and &quot;new&quot; can be used in place of &quot;good&quot; and &quot;bad&quot;, or you can choose your own terms. See section &quot;Alternate terms&quot; below for more information.</p>
<h3>Basic bisect commands: start, bad, good</h3>
<p> As an example, suppose you are trying to find the commit that broke a feature that was known to work in version <code>v2.6.13-rc2</code> of your project. You start a bisect session as follows: </p>
<dl>
<dt>
<dd>
<pre>
$ git bisect start
$ git bisect bad                 # Current version is bad
$ git bisect good v2.6.13-rc2    # v2.6.13-rc2 is known to be good
</pre>
</dl>
<p> Once you have specified at least one bad and one good commit, <code>git bisect</code> selects a commit in the middle of that range of history, checks it out, and outputs something similar to the following: </p>
<dl>
<dt>
<dd>
<pre>
Bisecting: 675 revisions left to test after this (roughly 10 steps)
</pre>
</dl>
<p> You should now compile the checked-out version and test it. If that version works correctly, type </p>
<dl>
<dt>
<dd>
<pre>
$ git bisect good
</pre>
</dl>
<p> If that version is broken, type </p>
<dl>
<dt>
<dd>
<pre>
$ git bisect bad
</pre>
</dl>
<p> Then <code>git bisect</code> will respond with something like </p>
<dl>
<dt>
<dd>
<pre>
Bisecting: 337 revisions left to test after this (roughly 9 steps)
</pre>
</dl>
<p> Keep repeating the process: compile the tree, test it, and depending on whether it is good or bad run <code>git bisect good</code> or <code>git bisect bad</code> to ask for the next commit that needs testing. </p>
<p> Eventually there will be no more revisions left to inspect, and the command will print out a description of the first bad commit. The reference <code>refs/bisect/bad</code> will be left pointing at that commit.</p>
<h3>Bisect reset</h3>
<p> After a bisect session, to clean up the bisection state and return to the original HEAD, issue the following command: </p>
<dl>
<dt>
<dd>
<pre>
$ git bisect reset
</pre>
</dl>
<p> By default, this will return your tree to the commit that was checked out before <code>git bisect start</code>. (A new <code>git bisect start</code> will also do that, as it cleans up the old bisection state.) </p>
<p> With an optional argument, you can return to a different commit instead: </p>
<dl>
<dt>
<dd>
<pre>
$ git bisect reset &lt;commit&gt;
</pre>
</dl>
<p> For example, <code>git bisect reset bisect/bad</code> will check out the first bad revision, while <code>git bisect reset HEAD</code> will leave you on the current bisection commit and avoid switching commits at all.</p>
<h3>Alternate terms</h3>
<p> Sometimes you are not looking for the commit that introduced a breakage, but rather for a commit that caused a change between some other &quot;old&quot; state and &quot;new&quot; state. For example, you might be looking for the commit that introduced a particular fix. Or you might be looking for the first commit in which the source-code filenames were finally all converted to your company&#8217;s naming standard. Or whatever. </p>
<p> In such cases it can be very confusing to use the terms &quot;good&quot; and &quot;bad&quot; to refer to &quot;the state before the change&quot; and &quot;the state after the change&quot;. So instead, you can use the terms &quot;old&quot; and &quot;new&quot;, respectively, in place of &quot;good&quot; and &quot;bad&quot;. (But note that you cannot mix &quot;good&quot; and &quot;bad&quot; with &quot;old&quot; and &quot;new&quot; in a single session.) </p>
<p> In this more general usage, you provide <code>git bisect</code> with a &quot;new&quot; commit that has some property and an &quot;old&quot; commit that doesn&#8217;t have that property. Each time <code>git bisect</code> checks out a commit, you test if that commit has the property. If it does, mark the commit as &quot;new&quot;; otherwise, mark it as &quot;old&quot;. When the bisection is done, <code>git bisect</code> will report which commit introduced the property. </p>
<p> To use &quot;old&quot; and &quot;new&quot; instead of &quot;good&quot; and bad, you must run <code>git bisect start</code> without commits as argument and then run the following commands to add the commits: </p>
<dl>
<dt>
<dd>
<pre>
git bisect old [&lt;rev&gt;]
</pre>
</dl>
<p> to indicate that a commit was before the sought change, or </p>
<dl>
<dt>
<dd>
<pre>
git bisect new [&lt;rev&gt;...]
</pre>
</dl>
<p> to indicate that it was after. </p>
<p> To get a reminder of the currently used terms, use </p>
<dl>
<dt>
<dd>
<pre>
git bisect terms
</pre>
</dl>
<p> You can get just the old (respectively new) term with <code>git bisect terms &#8211;term-old</code> or <code>git bisect terms &#8211;term-good</code>. </p>
<p> If you would like to use your own terms instead of &quot;bad&quot;/&quot;good&quot; or &quot;new&quot;/&quot;old&quot;, you can choose any names you like (except existing bisect subcommands like <code>reset</code>, <code>start</code>, &#8230;) by starting the bisection using </p>
<dl>
<dt>
<dd>
<pre>
git bisect start --term-old &lt;term-old&gt; --term-new &lt;term-new&gt;
</pre>
</dl>
<p> For example, if you are looking for a commit that introduced a performance regression, you might use </p>
<dl>
<dt>
<dd>
<pre>
git bisect start --term-old fast --term-new slow
</pre>
</dl>
<p> Or if you are looking for the commit that fixed a bug, you might use </p>
<dl>
<dt>
<dd>
<pre>
git bisect start --term-new fixed --term-old broken
</pre>
</dl>
<p> Then, use <code>git bisect &lt;term-old&gt;</code> and <code>git bisect &lt;term-new&gt;</code> instead of <code>git bisect good</code> and <code>git bisect bad</code> to mark commits.</p>
<h3>Bisect visualize/view</h3>
<p> To see the currently remaining suspects in <i>gitk</i>, issue the following command during the bisection process (the subcommand <code>view</code> can be used as an alternative to <code>visualize</code>): </p>
<dl>
<dt>
<dd>
<pre>
$ git bisect visualize
</pre>
</dl>
<p> If the <code>DISPLAY</code> environment variable is not set, <i>git log</i> is used instead. You can also give command-line options such as <code>-p</code> and <code>&#8211;stat</code>. </p>
<dl>
<dt>
<dd>
<pre>
$ git bisect visualize --stat
</pre>
</dl>
<h3>Bisect log and bisect replay</h3>
<p> After having marked revisions as good or bad, issue the following command to show what has been done so far: </p>
<dl>
<dt>
<dd>
<pre>
$ git bisect log
</pre>
</dl>
<p> If you discover that you made a mistake in specifying the status of a revision, you can save the output of this command to a file, edit it to remove the incorrect entries, and then issue the following commands to return to a corrected state: </p>
<dl>
<dt>
<dd>
<pre>
$ git bisect reset
$ git bisect replay that-file
</pre>
</dl>
<h3>Avoiding testing a commit</h3>
<p> If, in the middle of a bisect session, you know that the suggested revision is not a good one to test (e.g. it fails to build and you know that the failure does not have anything to do with the bug you are chasing), you can manually select a nearby commit and test that one instead. </p>
<p> For example: </p>
<dl>
<dt>
<dd>
<pre>
$ git bisect good/bad                   # previous round was good or bad.
Bisecting: 337 revisions left to test after this (roughly 9 steps)
$ git bisect visualize                  # oops, that is uninteresting.
$ git reset --hard HEAD~3               # try 3 revisions before what
                                        # was suggested
</pre>
</dl>
<p> Then compile and test the chosen revision, and afterwards mark the revision as good or bad in the usual manner.</p>
<h3>Bisect skip</h3>
<p> Instead of choosing a nearby commit by yourself, you can ask Git to do it for you by issuing the command: </p>
<dl>
<dt>
<dd>
<pre>
$ git bisect skip                 # Current version cannot be tested
</pre>
</dl>
<p> However, if you skip a commit adjacent to the one you are looking for, Git will be unable to tell exactly which of those commits was the first bad one. </p>
<p> You can also skip a range of commits, instead of just one commit, using range notation. For example: </p>
<dl>
<dt>
<dd>
<pre>
$ git bisect skip v2.5..v2.6
</pre>
</dl>
<p> This tells the bisect process that no commit after <code>v2.5</code>, up to and including <code>v2.6</code>, should be tested. </p>
<p> Note that if you also want to skip the first commit of the range you would issue the command: </p>
<dl>
<dt>
<dd>
<pre>
$ git bisect skip v2.5 v2.5..v2.6
</pre>
</dl>
<p> This tells the bisect process that the commits between <code>v2.5</code> and <code>v2.6</code> (inclusive) should be skipped.</p>
<h3>Cutting down bisection by giving more parameters to bisect start</h3>
<p> You can further cut down the number of trials, if you know what part of the tree is involved in the problem you are tracking down, by specifying path parameters when issuing the <code>bisect start</code> command: </p>
<dl>
<dt>
<dd>
<pre>
$ git bisect start -- arch/i386 include/asm-i386
</pre>
</dl>
<p> If you know beforehand more than one good commit, you can narrow the bisect space down by specifying all of the good commits immediately after the bad commit when issuing the <code>bisect start</code> command: </p>
<dl>
<dt>
<dd>
<pre>
$ git bisect start v2.6.20-rc6 v2.6.20-rc4 v2.6.20-rc1 --
                   # v2.6.20-rc6 is bad
                   # v2.6.20-rc4 and v2.6.20-rc1 are good
</pre>
</dl>
<h3>Bisect run</h3>
<p> If you have a script that can tell if the current source code is good or bad, you can bisect by issuing the command: </p>
<dl>
<dt>
<dd>
<pre>
$ git bisect run my_script arguments
</pre>
</dl>
<p> Note that the script (<code>my_script</code> in the above example) should exit with code 0 if the current source code is good/old, and exit with a code between 1 and 127 (inclusive), except 125, if the current source code is bad/new. </p>
<p> Any other exit code will abort the bisect process. It should be noted that a program that terminates via <code>exit(-1)</code> leaves $? = 255, (see the <a href="/docs/linux/man/3-exit/">exit</a>(3) manual page), as the value is chopped with <code>&amp; 0377</code>. </p>
<p> The special exit code 125 should be used when the current source code cannot be tested. If the script exits with this code, the current revision will be skipped (see <code>git bisect skip</code> above). 125 was chosen as the highest sensible value to use for this purpose, because 126 and 127 are used by POSIX shells to signal specific error status (127 is for command not found, 126 is for command found but not executable&#8212;these details do not matter, as they are normal errors in the script, as far as <code>bisect run</code> is concerned). </p>
<p> You may often find that during a bisect session you want to have temporary modifications (e.g. s/#define DEBUG 0/#define DEBUG 1/ in a header file, or &quot;revision that does not have this commit needs this patch applied to work around another problem this bisection is not interested in&quot;) applied to the revision being tested. </p>
<p> To cope with such a situation, after the inner <i>git bisect</i> finds the next revision to test, the script can apply the patch before compiling, run the real test, and afterwards decide if the revision (possibly with the needed patch) passed the test and then rewind the tree to the pristine state. Finally the script should exit with the status of the real test to let the <code>git bisect run</code> command loop determine the eventual outcome of the bisect session.</p>
<h2>OPTIONS</h2>
<p> &#8211;no-checkout</p>
<dl>
<dt>
<dd> Do not checkout the new working tree at each iteration of the bisection process. Instead just update a special reference named <code>BISECT_HEAD</code> to make it point to the commit that should be tested. </p>
<p> This option may be useful when the test you would perform in each step does not require a checked out tree. </p>
<p> If the repository is bare, <code>&#8211;no-checkout</code> is assumed.</dl>
<p> &#8211;first-parent</p>
<dl>
<dt>
<dd> Follow only the first parent commit upon seeing a merge commit. </p>
<p> In detecting regressions introduced through the merging of a branch, the merge commit will be identified as introduction of the bug and its ancestors will be ignored. </p>
<p> This option is particularly useful in avoiding false positives when a merged branch contained broken or non-buildable commits, but the merge itself was OK.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd> &bull; Automatically bisect a broken build between v1.2 and HEAD: </p>
<dl>
<dt>
<dd>
<pre>
$ git bisect start HEAD v1.2 --      # HEAD is bad, v1.2 is good
$ git bisect run make                # &quot;make&quot; builds the app
$ git bisect reset                   # quit the bisect session
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Automatically bisect a test failure between origin and HEAD: </p>
<dl>
<dt>
<dd>
<pre>
$ git bisect start HEAD origin --    # HEAD is bad, origin is good
$ git bisect run make test           # &quot;make test&quot; builds and tests
$ git bisect reset                   # quit the bisect session
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Automatically bisect a broken test case: </p>
<dl>
<dt>
<dd>
<pre>
$ cat ~/test.sh
#!/bin/sh
make || exit 125                     # this skips broken builds
~/check_test_case.sh                 # does the test case pass?
$ git bisect start HEAD HEAD~10 --   # culprit is among the last 10
$ git bisect run ~/test.sh
$ git bisect reset                   # quit the bisect session
</pre>
</dl>
<p> Here we use a <code>test.sh</code> custom script. In this script, if <code>make</code> fails, we skip the current commit. <code>check_test_case.sh</code> should <code>exit 0</code> if the test case passes, and <code>exit 1</code> otherwise. </p>
<p> It is safer if both <code>test.sh</code> and <code>check_test_case.sh</code> are outside the repository to prevent interactions between the bisect, make and test processes and the scripts.</dl>
<dl>
<dt>
<dd> &bull; Automatically bisect with temporary modifications (hot-fix): </p>
<dl>
<dt>
<dd>
$ cat ~ / test.sh<br />
#!/ bin / sh<br />
#tweak the working tree by merging the hot &#8211; fix branch<br />
#and then attempt a build<br />
          if git merge&#8211; no &#8211;<br />
    commit&#8211; no &#8211; ff hot &#8211; fix &amp;&amp;make then<br />
#run project specific test and report its status<br />
                               ~ /<br />
                               check_test_case.sh status = $<br />
    ? else<br />
#tell the caller this is untestable<br />
      status = 125 fi<br />
#undo the tweak to allow clean flipping to the next commit<br />
          git reset&#8211; hard<br />
#return control<br />
              exit $status
</dl>
<p> This applies modifications from a hot-fix branch before each test run, e.g. in case your build or test environment changed so that older revisions may need a fix which newer ones have already. (Make sure the hot-fix branch is based off a commit which is contained in all revisions which you are bisecting, so that the merge does not pull in too much, or use <code>git cherry-pick</code> instead of <code>git merge</code>.)</dl>
<dl>
<dt>
<dd> &bull; Automatically bisect a broken test case: </p>
<dl>
<dt>
<dd>
<pre>
$ git bisect start HEAD HEAD~10 --   # culprit is among the last 10
$ git bisect run sh -c &quot;make || exit 125; ~/check_test_case.sh&quot;
$ git bisect reset                   # quit the bisect session
</pre>
</dl>
<p> This shows that you can do without a run script if you write the test on a single line.</dl>
<dl>
<dt>
<dd> &bull; Locate a good region of the object graph in a damaged repository </p>
<dl>
<dt>
<dd>
<pre><code>
$ git bisect start HEAD &lt;known-good-commit&gt; [ &lt;boundary-commit&gt; ... ] --no-checkout
$ git bisect run sh -c '
        GOOD=$(git for-each-ref "--format=%(objectname)" refs/bisect/good-*) &amp;&amp;
        git rev-list --objects BISECT_HEAD --not $GOOD &gt;tmp.$$ &amp;&amp;
        git pack-objects --stdout &gt;/dev/null &lt;tmp.$$
        rc=$?
        rm -f tmp.$$
        test $rc = 0'
$ git bisect reset                   # quit the bisect session
</code></pre>
</dl>
<p> In this case, when <i>git bisect run</i> finishes, bisect/bad will refer to a commit that has at least one parent whose reachable graph is fully traversable in the sense required by <i>git pack objects</i>.</dl>
<dl>
<dt>
<dd> &bull; Look for a fix instead of a regression in the code </p>
<dl>
<dt>
<dd>
<pre>
$ git bisect start
$ git bisect new HEAD    # current commit is marked as new
$ git bisect old HEAD~10 # the tenth commit from now is marked as old
</pre>
</dl>
<p> or:</dl>
<dl>
<dt>
<dd>
<pre>
$ git bisect start --term-old broken --term-new fixed
$ git bisect fixed
$ git bisect broken HEAD~10
</pre>
</dl>
<h3>Getting help</h3>
<p> Use <code>git bisect</code> to get a short usage description, and <code>git bisect help</code> or <code>git bisect -h</code> to get a long usage description.</p>
<h2>SEE ALSO</h2>
<p> m[blue]<code>Fighting regressions with git bisect</code>m[]<font SIZE="-2">[1]</font>, <code><a href="/docs/linux/man/1-git-blame/">git-blame</a></code>(1).</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> Fighting regressions with git bisect</p>
<dl>
<dt>
<dd> file:///usr/share/doc/git/html/git-bisect-lk2009.html</dl>
</dl>
<h2>Index</h2>

---
title: "gitworkflows(7)"
name: "gitworkflows"
section: "7"
letter: "g"
url: "/docs/linux/man/7-gitworkflows/"
description: "gitworkflows – An overview of recommended workflows with Git"
---

<p>gitworkflows &#8211; An overview of recommended workflows with Git</p>
<h2>Synopsis</h2>
<pre>git *</pre>
<h2>Description</h2>
<p>This document attempts to write down and motivate some of the workflow elements used for <code>git.git</code> itself. Many ideas apply in general, though the full workflow is rarely required for smaller projects with fewer people involved. </p>
<p> We formulate a set of <i>rules</i> for quick reference, while the prose tries to motivate each of them. Do not always take them literally; you should value good reasons for your actions higher than manpages such as this one.</p>
<h2>Separate Changes</h2>
<p>As a general rule, you should try to split your changes into small logical steps, and commit each of them. They should be consistent, working independently of any later commits, pass the test suite, etc. This makes the review process much easier, and the history much more useful for later inspection and analysis, for example with <code><a href="/docs/linux/man/1-git-blame/">git-blame</a></code>(1) and <code><a href="/docs/linux/man/1-git-bisect/">git-bisect</a></code>(1). </p>
<p> To achieve this, try to split your work into small steps from the very beginning. It is always easier to squash a few commits together than to split one big commit into several. Don&#8217;t be afraid of making too small or imperfect steps along the way. You can always go back later and edit the commits with <code>git rebase &#8211;interactive</code> before you publish them. You can use <code>git stash push &#8211;keep-index</code> to run the test suite independent of other uncommitted changes; see the EXAMPLES section of <code><a href="/docs/linux/man/1-git-stash/">git-stash</a></code>(1).</p>
<h2>Managing Branches</h2>
<p>There are two main tools that can be used to include changes from one branch on another: <code><a href="/docs/linux/man/1-git-merge/">git-merge</a></code>(1) and <code><a href="/docs/linux/man/1-git-cherry-pick/">git-cherry-pick</a></code>(1). </p>
<p> Merges have many advantages, so we try to solve as many problems as possible with merges alone. Cherry-picking is still occasionally useful; see &quot;Merging upwards&quot; below for an example. </p>
<p> Most importantly, merging works at the branch level, while cherry-picking works at the commit level. This means that a merge can carry over the changes from 1, 10, or 1000 commits with equal ease, which in turn means the workflow scales much better to a large number of contributors (and contributions). Merges are also easier to understand because a merge commit is a &quot;promise&quot; that all changes from all its parents are now included. </p>
<p> There is a tradeoff of course: merges require a more careful branch management. The following subsections discuss the important points.</p>
<h3>Graduation</h3>
<p>As a given feature goes from experimental to stable, it also &quot;graduates&quot; between the corresponding branches of the software. <code>git.git</code> uses the following <i>integration branches</i>: </p>
<dl>
<dd>&bull; <i>maint</i> tracks the commits that should go into the next &quot;maintenance release&quot;, i.e., update of the last released stable version;</dl>
<dl>
<dd>&bull; <i>master</i> tracks the commits that should go into the next release;</dl>
<dl>
<dd>&bull; <i>next</i> is intended as a testing branch for topics being tested for stability for master.</dl>
<p> There is a fourth official branch that is used slightly differently: </p>
<dl>
<dd>&bull; <i>seen</i> (patches seen by the maintainer) is an integration branch for things that are not quite ready for inclusion yet (see &quot;Integration Branches&quot; below).</dl>
<p> Each of the four branches is usually a direct descendant of the one above it. </p>
<p> Conceptually, the feature enters at an unstable branch (usually <i>next</i> or <i>seen</i>), and &quot;graduates&quot; to <i>master</i> for the next release once it is considered stable enough.</p>
<h3>Merging upwards</h3>
<p>The &quot;downwards graduation&quot; discussed above cannot be done by actually merging downwards, however, since that would merge <i>all</i> changes on the unstable branch into the stable one. Hence the following: </p>
<p> <code>Example 1. Merge upwards</code> </p>
<p> Always commit your fixes to the oldest supported branch that requires them. Then (periodically) merge the integration branches upwards into each other. </p>
<p> This gives a very controlled flow of fixes. If you notice that you have applied a fix to e.g. <i>master</i> that is also required in <i>maint</i>, you will need to cherry-pick it (using <code><a href="/docs/linux/man/1-git-cherry-pick/">git-cherry-pick</a></code>(1)) downwards. This will happen a few times and is nothing to worry about unless you do it very frequently.</p>
<h3>Topic branches</h3>
<p>Any nontrivial feature will require several patches to implement, and may get extra bugfixes or improvements during its lifetime. </p>
<p> Committing everything directly on the integration branches leads to many problems: Bad commits cannot be undone, so they must be reverted one by one, which creates confusing histories and further error potential when you forget to revert part of a group of changes. Working in parallel mixes up the changes, creating further confusion. </p>
<p> Use of &quot;topic branches&quot; solves these problems. The name is pretty self explanatory, with a caveat that comes from the &quot;merge upwards&quot; rule above: </p>
<p> <code>Example 2. Topic branches</code> </p>
<p> Make a side branch for every topic (feature, bugfix, &#8230;). Fork it off at the oldest integration branch that you will eventually want to merge it into. </p>
<p> Many things can then be done very naturally: </p>
<dl>
<dd>&bull; To get the feature/bugfix into an integration branch, simply merge it. If the topic has evolved further in the meantime, merge again. (Note that you do not necessarily have to merge it to the oldest integration branch first. For example, you can first merge a bugfix to <i>next</i>, give it some testing time, and merge to <i>maint</i> when you know it is stable.)</dl>
<dl>
<dd>&bull; If you find you need new features from the branch <i>other</i> to continue working on your topic, merge <i>other</i> to <i>topic</i>. (However, do not do this &quot;just habitually&quot;, see below.)</dl>
<dl>
<dd>&bull; If you find you forked off the wrong branch and want to move it &quot;back in time&quot;, use <code><a href="/docs/linux/man/1-git-rebase/">git-rebase</a></code>(1).</dl>
<p> Note that the last point clashes with the other two: a topic that has been merged elsewhere should not be rebased. See the section on RECOVERING FROM UPSTREAM REBASE in <code><a href="/docs/linux/man/1-git-rebase/">git-rebase</a></code>(1). </p>
<p> We should point out that &quot;habitually&quot; (regularly for no real reason) merging an integration branch into your topics &#8212; and by extension, merging anything upstream into anything downstream on a regular basis &#8212; is frowned upon: </p>
<p> <code>Example 3. Merge to downstream only at well-defined points</code> </p>
<p> Do not merge to downstream except with a good reason: upstream API changes affect your branch; your branch no longer merges to upstream cleanly; etc. </p>
<p> Otherwise, the topic that was merged to suddenly contains more than a single (well-separated) change. The many resulting small merges will greatly clutter up history. Anyone who later investigates the history of a file will have to find out whether that merge affected the topic in development. An upstream might even inadvertently be merged into a &quot;more stable&quot; branch. And so on.</p>
<h3>Throw-away integration</h3>
<p>If you followed the last paragraph, you will now have many small topic branches, and occasionally wonder how they interact. Perhaps the result of merging them does not even work? But on the other hand, we want to avoid merging them anywhere &quot;stable&quot; because such merges cannot easily be undone. </p>
<p> The solution, of course, is to make a merge that we can undo: merge into a throw-away branch. </p>
<p> <code>Example 4. Throw-away integration branches</code> </p>
<p> To test the interaction of several topics, merge them into a throw-away branch. You must never base any work on such a branch! </p>
<p> If you make it (very) clear that this branch is going to be deleted right after the testing, you can even publish this branch, for example to give the testers a chance to work with it, or other developers a chance to see if their in-progress work will be compatible. <code>git.git</code> has such an official throw-away integration branch called <i>seen</i>.</p>
<h3>Branch management for a release</h3>
<p>Assuming you are using the merge approach discussed above, when you are releasing your project you will need to do some additional branch management work. </p>
<p> A feature release is created from the <i>master</i> branch, since <i>master</i> tracks the commits that should go into the next feature release. </p>
<p> The <i>master</i> branch is supposed to be a superset of <i>maint</i>. If this condition does not hold, then <i>maint</i> contains some commits that are not included on <i>master</i>. The fixes represented by those commits will therefore not be included in your feature release. </p>
<p> To verify that <i>master</i> is indeed a superset of <i>maint</i>, use git log: </p>
<p> <code>Example 5. Verify </code><i>master</i> is a superset of <i>maint</i> </p>
<p> <code>git log master..maint</code> </p>
<p> This command should not list any commits. Otherwise, check out <i>master</i> and merge <i>maint</i> into it. </p>
<p> Now you can proceed with the creation of the feature release. Apply a tag to the tip of <i>master</i> indicating the release version: </p>
<p> <code>Example 6. Release tagging</code> </p>
<p> <code>git tag -s -m &quot;Git X.Y.Z&quot; vX.Y.Z master</code> </p>
<p> You need to push the new tag to a public Git server (see &quot;DISTRIBUTED WORKFLOWS&quot; below). This makes the tag available to others tracking your project. The push could also trigger a post-update hook to perform release-related items such as building release tarballs and preformatted documentation pages. </p>
<p> Similarly, for a maintenance release, <i>maint</i> is tracking the commits to be released. Therefore, in the steps above simply tag and push <i>maint</i> rather than <i>master</i>.</p>
<h3>Maintenance branch management after a feature release</h3>
<p>After a feature release, you need to manage your maintenance branches. </p>
<p> First, if you wish to continue to release maintenance fixes for the feature release made before the recent one, then you must create another branch to track commits for that previous release. </p>
<p> To do this, the current maintenance branch is copied to another branch named with the previous release version number (e.g. maint-X.Y.(Z-1) where X.Y.Z is the current release). </p>
<p> <code>Example 7. Copy maint</code> </p>
<p> <code>git branch maint-X.Y.(Z-1) maint</code> </p>
<p> The <i>maint</i> branch should now be fast-forwarded to the newly released code so that maintenance fixes can be tracked for the current release: </p>
<p> <code>Example 8. Update maint to new release</code> </p>
<dl>
<dd>&bull; <code>git checkout maint</code></dl>
<dl>
<dd>&bull; <code>git merge &#8211;ff-only master</code></dl>
<p> If the merge fails because it is not a fast-forward, then it is possible some fixes on <i>maint</i> were missed in the feature release. This will not happen if the content of the branches was verified as described in the previous section.</p>
<h3>Branch management for next and seen after a feature release</h3>
<p>After a feature release, the integration branch <i>next</i> may optionally be rewound and rebuilt from the tip of <i>master</i> using the surviving topics on <i>next</i>: </p>
<p> <code>Example 9. Rewind and rebuild next</code> </p>
<dl>
<dd>&bull; <code>git switch -C next master</code></dl>
<dl>
<dd>&bull; <code>git merge ai/topic_in_next1</code></dl>
<dl>
<dd>&bull; <code>git merge ai/topic_in_next2</code></dl>
<dl>
<dd>&bull; &#8230;</dl>
<p> The advantage of doing this is that the history of <i>next</i> will be clean. For example, some topics merged into <i>next</i> may have initially looked promising, but were later found to be undesirable or premature. In such a case, the topic is reverted out of <i>next</i> but the fact remains in the history that it was once merged and reverted. By recreating <i>next</i>, you give another incarnation of such topics a clean slate to retry, and a feature release is a good point in history to do so. </p>
<p> If you do this, then you should make a public announcement indicating that <i>next</i> was rewound and rebuilt. </p>
<p> The same rewind and rebuild process may be followed for <i>seen</i>. A public announcement is not necessary since <i>seen</i> is a throw-away branch, as described above.</p>
<h2>Distributed Workflows</h2>
<p>After the last section, you should know how to manage topics. In general, you will not be the only person working on the project, so you will have to share your work. </p>
<p> Roughly speaking, there are two important workflows: merge and patch. The important difference is that the merge workflow can propagate full history, including merges, while patches cannot. Both workflows can be used in parallel: in <code>git.git</code>, only subsystem maintainers use the merge workflow, while everyone else sends patches. </p>
<p> Note that the maintainer(s) may impose restrictions, such as &quot;Signed-off-by&quot; requirements, that all commits/patches submitted for inclusion must adhere to. Consult your project&#8217;s documentation for more information.</p>
<h3>Merge workflow</h3>
<p>The merge workflow works by copying branches between upstream and downstream. Upstream can merge contributions into the official history; downstream base their work on the official history. </p>
<p> There are three main tools that can be used for this: </p>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/1-git-push/">git-push</a></code>(1) copies your branches to a remote repository, usually to one that can be read by all involved parties;</dl>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/1-git-fetch/">git-fetch</a></code>(1) that copies remote branches to your repository; and</dl>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/1-git-pull/">git-pull</a></code>(1) that does fetch and merge in one go.</dl>
<p> Note the last point. Do <i>not</i> use <i>git pull</i> unless you actually want to merge the remote branch. </p>
<p> Getting changes out is easy: </p>
<p> <code>Example 10. Push/pull: Publishing branches/topics</code> </p>
<p> <code>git push &lt;remote&gt; &lt;branch&gt;</code> and tell everyone where they can fetch from. </p>
<p> You will still have to tell people by other means, such as mail. (Git provides the <code><a href="/docs/linux/man/1-git-request-pull/">git-request-pull</a></code>(1) to send preformatted pull requests to upstream maintainers to simplify this task.) </p>
<p> If you just want to get the newest copies of the integration branches, staying up to date is easy too: </p>
<p> <code>Example 11. Push/pull: Staying up to date</code> </p>
<p> Use <code>git fetch &lt;remote&gt;</code> or <code>git remote update</code> to stay up to date. </p>
<p> Then simply fork your topic branches from the stable remotes as explained earlier. </p>
<p> If you are a maintainer and would like to merge other people&#8217;s topic branches to the integration branches, they will typically send a request to do so by mail. Such a request looks like </p>
<dl>
<dd>
<pre>Please pull from
 &lt;url&gt; &lt;branch&gt;</pre>
</dl>
<p> In that case, <i>git pull</i> can do the fetch and merge in one go, as follows. </p>
<p> <code>Example 12. Push/pull: Merging remote topics</code> </p>
<p> <code>git pull &lt;url&gt; &lt;branch&gt;</code> </p>
<p> Occasionally, the maintainer may get merge conflicts when they try to pull changes from downstream. In this case, they can ask downstream to do the merge and resolve the conflicts themselves (perhaps they will know better how to resolve them). It is one of the rare cases where downstream <i>should</i> merge from upstream.</p>
<h3>Patch workflow</h3>
<p>If you are a contributor that sends changes upstream in the form of emails, you should use topic branches as usual (see above). Then use <code><a href="/docs/linux/man/1-git-format-patch/">git-format-patch</a></code>(1) to generate the corresponding emails (highly recommended over manually formatting them because it makes the maintainer&#8217;s life easier). </p>
<p> <code>Example 13. format-patch/am: Publishing branches/topics</code> </p>
<dl>
<dd>&bull; <code>git format-patch -M upstream..topic</code> to turn them into preformatted patch files</dl>
<dl>
<dd>&bull; <code>git send-email &#8211;to=&lt;recipient&gt; &lt;patches&gt;</code></dl>
<p> See the <code><a href="/docs/linux/man/1-git-format-patch/">git-format-patch</a></code>(1) and <code><a href="/docs/linux/man/1-git-send-email/">git-send-email</a></code>(1) manpages for further usage notes. </p>
<p> If the maintainer tells you that your patch no longer applies to the current upstream, you will have to rebase your topic (you cannot use a merge because you cannot format-patch merges): </p>
<p> <code>Example 14. format-patch/am: Keeping topics up to date</code> </p>
<p> <code>git pull &#8211;rebase &lt;url&gt; &lt;branch&gt;</code> </p>
<p> You can then fix the conflicts during the rebase. Presumably you have not published your topic other than by mail, so rebasing it is not a problem. </p>
<p> If you receive such a patch series (as maintainer, or perhaps as a reader of the mailing list it was sent to), save the mails to files, create a new topic branch and use <i>git am</i> to import the commits: </p>
<p> <code>Example 15. format-patch/am: Importing patches</code> </p>
<p> <code>git am &lt; patch</code> </p>
<p> One feature worth pointing out is the three-way merge, which can help if you get conflicts: <code>git am -3</code> will use index information contained in patches to figure out the merge base. See <code><a href="/docs/linux/man/1-git-am/">git-am</a></code>(1) for other options.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-gittutorial/">gittutorial</a></code>(7), <code><a href="/docs/linux/man/1-git-push/">git-push</a></code>(1), <code><a href="/docs/linux/man/1-git-pull/">git-pull</a></code>(1), <code><a href="/docs/linux/man/1-git-merge/">git-merge</a></code>(1), <code><a href="/docs/linux/man/1-git-rebase/">git-rebase</a></code>(1), <code><a href="/docs/linux/man/1-git-format-patch/">git-format-patch</a></code>(1), <code><a href="/docs/linux/man/1-git-send-email/">git-send-email</a></code>(1), <code><a href="/docs/linux/man/1-git-am/">git-am</a></code>(1)</p>
<h2>Git</h2>
<p>Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite</p>

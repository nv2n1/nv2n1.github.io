---
title: "git-rebase(1)"
name: "git-rebase"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-rebase/"
description: "git-rebase – Reapply commits on top of another base tip"
---

<h2 class="name">NAME</h2>
<p> git-rebase &#8211; Reapply commits on top of another base tip </p>
<h2>SYNOPSIS</h2>
<pre><code>
git rebase[-i | --interactive][&lt;options&gt;][--exec&lt;cmd&gt;]
          [--onto&lt;newbase&gt; | --keep - base][&lt;upstream&gt;[&lt;branch&gt;]] git rebase[-i | --interactive][&lt;options&gt;][--exec&lt;cmd&gt;][--onto&lt;newbase&gt;]-- root[&lt;branch&gt;] git rebase(--continue | --skip | --abort | --quit | --edit - todo | --show - current - patch)
</code></pre>
<h2>DESCRIPTION</h2>
<p> If &lt;branch&gt; is specified, <i>git rebase</i> will perform an automatic <code>git switch &lt;branch&gt;</code> before doing anything else. Otherwise it remains on the current branch. </p>
<p> If &lt;upstream&gt; is not specified, the upstream configured in branch.&lt;name&gt;.remote and branch.&lt;name&gt;.merge options will be used (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1) for details) and the <code>&#8211;fork-point</code> option is assumed. If you are currently not on any branch or if the current branch does not have a configured upstream, the rebase will abort. </p>
<p> All changes made by commits in the current branch but that are not in &lt;upstream&gt; are saved to a temporary area. This is the same set of commits that would be shown by <code>git log &lt;upstream&gt;..HEAD</code>; or by <code>git log &#8216;fork_point&#8217;..HEAD</code>, if <code>&#8211;fork-point</code> is active (see the description on <code>&#8211;fork-point</code> below); or by <code>git log HEAD</code>, if the <code>&#8211;root</code> option is specified. </p>
<p> The current branch is reset to &lt;upstream&gt;, or &lt;newbase&gt; if the &#8211;onto option was supplied. This has the exact same effect as <code>git reset &#8211;hard &lt;upstream&gt;</code> (or &lt;newbase&gt;). ORIG_HEAD is set to point at the tip of the branch before the reset. </p>
<p> The commits that were previously saved into the temporary area are then reapplied to the current branch, one by one, in order. Note that any commits in HEAD which introduce the same textual changes as a commit in HEAD..&lt;upstream&gt; are omitted (i.e., a patch already accepted upstream with a different commit message or timestamp will be skipped). </p>
<p> It is possible that a merge failure will prevent this process from being completely automatic. You will have to resolve any such merge failure and run <code>git rebase &#8211;continue</code>. Another option is to bypass the commit that caused the merge failure with <code>git rebase &#8211;skip</code>. To check out the original &lt;branch&gt; and remove the .git/rebase-apply working files, use the command <code>git rebase &#8211;abort</code> instead. </p>
<p> Assume the following history exists and the current branch is &quot;topic&quot;: </p>
<dl>
<dt>
<dd>
A&#8211; &#8211; B&#8211; &#8211; C topic / D&#8211; &#8211; E&#8211; &#8211; F&#8211; &#8211; G master
</dl>
<p> From this point, the result of either of the following commands: </p>
<dl>
<dt>
<dd>
<pre>
git rebase master
git rebase master topic
</pre>
</dl>
<p> would be: </p>
<dl>
<dt>
<dd>
A &#8216;&#8211;B&#8217; &#8211;C&#8217; topic /<br />
        D&#8211; &#8211;<br />
    E&#8211; &#8211; F&#8211; &#8211; G master
</dl>
<p> <code>NOTE:</code> The latter form is just a short-hand of <code>git checkout topic</code> followed by <code>git rebase master</code>. When rebase exits <code>topic</code> will remain the checked-out branch. </p>
<p> If the upstream branch already contains a change you have made (e.g., because you mailed a patch which was applied upstream), then that commit will be skipped and warnings will be issued (if the <code>merge</code> backend is used). For example, running <code>git rebase master</code> on the following history (in which <code>A&#8217;</code> and <code>A</code> introduce the same set of changes, but have different committer information): </p>
<dl>
<dt>
<dd>
A&#8211; &#8211; B&#8211; &#8211; C topic / D&#8211; &#8211; E&#8211; &#8211; A&#8217;&#8212;F master
</dl>
<p> will result in: </p>
<dl>
<dt>
<dd>
B &#8216;&#8212;C&#8217; topic /<br />
        D&#8211; &#8211;<br />
    E&#8211; &#8211; A&#8217;&#8212;F master
</dl>
<p> Here is how you would transplant a topic branch based on one branch to another, to pretend that you forked the topic branch from the latter branch, using <code>rebase &#8211;onto</code>. </p>
<p> First let&#8217;s assume your <i>topic</i> is based on branch <i>next</i>. For example, a feature developed in <i>topic</i> depends on some functionality which is found in <i>next</i>. </p>
<dl>
<dt>
<dd>
o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; o master</p>
<p>                            o&#8211; &#8211;<br />
    o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; o next</p>
<p>                          o&#8211; &#8211;<br />
    o&#8211; &#8211; o topic
</dl>
<p> We want to make <i>topic</i> forked from branch <i>master</i>; for example, because the functionality on which <i>topic</i> depends was merged into the more stable <i>master</i> branch. We want our tree to look like this: </p>
<dl>
<dt>
<dd>
o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; o master |<br />
    | o &#8216;&#8211;o&#8217; &#8211;o&#8217;  topic</p>
<p>          o&#8211; &#8211;<br />
          o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; o next
</dl>
<p> We can get this using the following command: </p>
<dl>
<dt>
<dd>
<pre>
git rebase --onto master next topic
</pre>
</dl>
<p> Another example of &#8211;onto option is to rebase part of a branch. If we have the following situation: </p>
<dl>
<dt>
<dd>
H&#8211; &#8211; I&#8211; &#8211; J topicB / E&#8211; &#8211; F&#8211; &#8211; G topicA / A&#8211; &#8211; B&#8211; &#8211; C&#8211; &#8211; D master
</dl>
<p> then the command </p>
<dl>
<dt>
<dd>
<pre>
git rebase --onto master topicA topicB
</pre>
</dl>
<p> would result in: </p>
<dl>
<dt>
<dd>
H &#8216;&#8211;I&#8217; &#8211;J&#8217;  topicB /<br />
    | E&#8211; &#8211; F&#8211; &#8211; G topicA | /<br />
                                     A&#8211; &#8211;<br />
                                 B&#8211; &#8211; C&#8211; &#8211; D master
</dl>
<p> This is useful when topicB does not depend on topicA. </p>
<p> A range of commits could also be removed with rebase. If we have the following situation: </p>
<dl>
<dt>
<dd>
E&#8211; &#8211; F&#8211; &#8211; G&#8211; &#8211; H&#8211; &#8211; I&#8211; &#8211; J topicA
</dl>
<p> then the command </p>
<dl>
<dt>
<dd>
<pre>
git rebase --onto topicA~5 topicA~3 topicA
</pre>
</dl>
<p> would result in the removal of commits F and G: </p>
<dl>
<dt>
<dd>
<pre>
    E---H'---I'---J'  topicA
</pre>
</dl>
<p> This is useful if F and G were flawed in some way, or should not be part of topicA. Note that the argument to &#8211;onto and the &lt;upstream&gt; parameter can be any valid commit-ish. </p>
<p> In case of conflict, <i>git rebase</i> will stop at the first problematic commit and leave conflict markers in the tree. You can use <i>git diff</i> to locate the markers (&lt;&lt;&lt;&lt;&lt;&lt;) and make edits to resolve the conflict. For each file you edit, you need to tell Git that the conflict has been resolved, typically this would be done with </p>
<dl>
<dt>
<dd>
<pre>
git add &lt;filename&gt;
</pre>
</dl>
<p> After resolving the conflict manually and updating the index with the desired resolution, you can continue the rebasing process with </p>
<dl>
<dt>
<dd>
<pre>
git rebase --continue
</pre>
</dl>
<p> Alternatively, you can undo the <i>git rebase</i> with </p>
<dl>
<dt>
<dd>
<pre>
git rebase --abort
</pre>
</dl>
<h2>OPTIONS</h2>
<p> &#8211;onto &lt;newbase&gt;</p>
<dl>
<dt>
<dd> Starting point at which to create the new commits. If the &#8211;onto option is not specified, the starting point is &lt;upstream&gt;. May be any valid commit, and not just an existing branch name. </p>
<p> As a special case, you may use &quot;A&#8230;B&quot; as a shortcut for the merge base of A and B if there is exactly one merge base. You can leave out at most one of A and B, in which case it defaults to HEAD.</dl>
<p> &#8211;keep-base</p>
<dl>
<dt>
<dd> Set the starting point at which to create the new commits to the merge base of &lt;upstream&gt; &lt;branch&gt;. Running <i>git rebase &#8211;keep-base &lt;upstream&gt; &lt;branch&gt;</i> is equivalent to running <i>git rebase &#8211;onto &lt;upstream&gt;&#8230; &lt;upstream&gt;</i>. </p>
<p> This option is useful in the case where one is developing a feature on top of an upstream branch. While the feature is being worked on, the upstream branch may advance and it may not be the best idea to keep rebasing on top of the upstream but to keep the base commit as-is. </p>
<p> Although both this option and &#8211;fork-point find the merge base between &lt;upstream&gt; and &lt;branch&gt;, this option uses the merge base as the <i>starting point</i> on which new commits will be created, whereas &#8211;fork-point uses the merge base to determine the <i>set of commits</i> which will be rebased. </p>
<p> See also INCOMPATIBLE OPTIONS below.</dl>
<p> &lt;upstream&gt;</p>
<dl>
<dt>
<dd> Upstream branch to compare against. May be any valid commit, not just an existing branch name. Defaults to the configured upstream for the current branch.</dl>
<p> &lt;branch&gt;</p>
<dl>
<dt>
<dd> Working branch; defaults to HEAD.</dl>
<p> &#8211;continue</p>
<dl>
<dt>
<dd> Restart the rebasing process after having resolved a merge conflict.</dl>
<p> &#8211;abort</p>
<dl>
<dt>
<dd> Abort the rebase operation and reset HEAD to the original branch. If &lt;branch&gt; was provided when the rebase operation was started, then HEAD will be reset to &lt;branch&gt;. Otherwise HEAD will be reset to where it was when the rebase operation was started.</dl>
<p> &#8211;quit</p>
<dl>
<dt>
<dd> Abort the rebase operation but HEAD is not reset back to the original branch. The index and working tree are also left unchanged as a result. If a temporary stash entry was created using &#8211;autostash, it will be saved to the stash list.</dl>
<p> &#8211;apply</p>
<dl>
<dt>
<dd> Use applying strategies to rebase (calling <code>git-am</code> internally). This option may become a no-op in the future once the merge backend handles everything the apply one does. </p>
<p> See also INCOMPATIBLE OPTIONS below.</dl>
<p> &#8211;empty={drop,keep,ask}</p>
<dl>
<dt>
<dd> How to handle commits that are not empty to start and are not clean cherry-picks of any upstream commit, but which become empty after rebasing (because they contain a subset of already upstream changes). With drop (the default), commits that become empty are dropped. With keep, such commits are kept. With ask (implied by &#8211;interactive), the rebase will halt when an empty commit is applied allowing you to choose whether to drop it, edit files more, or just commit the empty changes. Other options, like &#8211;exec, will use the default of drop unless -i/&#8211;interactive is explicitly specified. </p>
<p> Note that commits which start empty are kept (unless &#8211;no-keep-empty is specified), and commits which are clean cherry-picks (as determined by <code>git log &#8211;cherry-mark &#8230;</code>) are detected and dropped as a preliminary step (unless &#8211;reapply-cherry-picks is passed). </p>
<p> See also INCOMPATIBLE OPTIONS below.</dl>
<p> &#8211;no-keep-empty, &#8211;keep-empty</p>
<dl>
<dt>
<dd> Do not keep commits that start empty before the rebase (i.e. that do not change anything from its parent) in the result. The default is to keep commits which start empty, since creating such commits requires passing the &#8211;allow-empty override flag to <code>git commit</code>, signifying that a user is very intentionally creating such a commit and thus wants to keep it. </p>
<p> Usage of this flag will probably be rare, since you can get rid of commits that start empty by just firing up an interactive rebase and removing the lines corresponding to the commits you don&#8217;t want. This flag exists as a convenient shortcut, such as for cases where external tools generate many empty commits and you want them all removed. </p>
<p> For commits which do not start empty but become empty after rebasing, see the &#8211;empty flag. </p>
<p> See also INCOMPATIBLE OPTIONS below.</dl>
<p> &#8211;reapply-cherry-picks, &#8211;no-reapply-cherry-picks</p>
<dl>
<dt>
<dd> Reapply all clean cherry-picks of any upstream commit instead of preemptively dropping them. (If these commits then become empty after rebasing, because they contain a subset of already upstream changes, the behavior towards them is controlled by the <code>&#8211;empty</code> flag.) </p>
<p> By default (or if <code>&#8211;no-reapply-cherry-picks</code> is given), these commits will be automatically dropped. Because this necessitates reading all upstream commits, this can be expensive in repos with a large number of upstream commits that need to be read. When using the <code>merge</code> backend, warnings will be issued for each dropped commit (unless <code>&#8211;quiet</code> is given). Advice will also be issued unless <code>advice.skippedCherryPicks</code> is set to false (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)). </p>
<p> <code>&#8211;reapply-cherry-picks</code> allows rebase to forgo reading all upstream commits, potentially improving performance. </p>
<p> See also INCOMPATIBLE OPTIONS below.</dl>
<p> &#8211;allow-empty-message</p>
<dl>
<dt>
<dd> No-op. Rebasing commits with an empty message used to fail and this option would override that behavior, allowing commits with empty messages to be rebased. Now commits with an empty message do not cause rebasing to halt. </p>
<p> See also INCOMPATIBLE OPTIONS below.</dl>
<p> &#8211;skip</p>
<dl>
<dt>
<dd> Restart the rebasing process by skipping the current patch.</dl>
<p> &#8211;edit-todo</p>
<dl>
<dt>
<dd> Edit the todo list during an interactive rebase.</dl>
<p> &#8211;show-current-patch</p>
<dl>
<dt>
<dd> Show the current patch in an interactive rebase or when rebase is stopped because of conflicts. This is the equivalent of <code>git show REBASE_HEAD</code>.</dl>
<p> -m, &#8211;merge</p>
<dl>
<dt>
<dd> Using merging strategies to rebase (default). </p>
<p> Note that a rebase merge works by replaying each commit from the working branch on top of the &lt;upstream&gt; branch. Because of this, when a merge conflict happens, the side reported as <i>ours</i> is the so-far rebased series, starting with &lt;upstream&gt;, and <i>theirs</i> is the working branch. In other words, the sides are swapped. </p>
<p> See also INCOMPATIBLE OPTIONS below.</dl>
<p> -s &lt;strategy&gt;, &#8211;strategy=&lt;strategy&gt;</p>
<dl>
<dt>
<dd> Use the given merge strategy, instead of the default <code>ort</code>. This implies <code>&#8211;merge</code>. </p>
<p> Because <i>git rebase</i> replays each commit from the working branch on top of the &lt;upstream&gt; branch using the given strategy, using the <i>ours</i> strategy simply empties all patches from the &lt;branch&gt;, which makes little sense. </p>
<p> See also INCOMPATIBLE OPTIONS below.</dl>
<p> -X &lt;strategy-option&gt;, &#8211;strategy-option=&lt;strategy-option&gt;</p>
<dl>
<dt>
<dd> Pass the &lt;strategy-option&gt; through to the merge strategy. This implies <code>&#8211;merge</code> and, if no strategy has been specified, <code>-s ort</code>. Note the reversal of <i>ours</i> and <i>theirs</i> as noted above for the <code>-m</code> option. </p>
<p> See also INCOMPATIBLE OPTIONS below.</dl>
<p> &#8211;rerere-autoupdate, &#8211;no-rerere-autoupdate</p>
<dl>
<dt>
<dd> Allow the rerere mechanism to update the index with the result of auto-conflict resolution if possible.</dl>
<p> -S[&lt;keyid&gt;], &#8211;gpg-sign[=&lt;keyid&gt;], &#8211;no-gpg-sign</p>
<dl>
<dt>
<dd> GPG-sign commits. The <code>keyid</code> argument is optional and defaults to the committer identity; if specified, it must be stuck to the option without a space. <code>&#8211;no-gpg-sign</code> is useful to countermand both <code>commit.gpgSign</code> configuration variable, and earlier <code>&#8211;gpg-sign</code>.</dl>
<p> -q, &#8211;quiet</p>
<dl>
<dt>
<dd> Be quiet. Implies &#8211;no-stat.</dl>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
<dd> Be verbose. Implies &#8211;stat.</dl>
<p> &#8211;stat</p>
<dl>
<dt>
<dd> Show a diffstat of what changed upstream since the last rebase. The diffstat is also controlled by the configuration option rebase.stat.</dl>
<p> -n, &#8211;no-stat</p>
<dl>
<dt>
<dd> Do not show a diffstat as part of the rebase process.</dl>
<p> &#8211;no-verify</p>
<dl>
<dt>
<dd> This option bypasses the pre-rebase hook. See also <code><a href="/docs/linux/man/5-githooks/">githooks</a></code>(5).</dl>
<p> &#8211;verify</p>
<dl>
<dt>
<dd> Allows the pre-rebase hook to run, which is the default. This option can be used to override &#8211;no-verify. See also <code><a href="/docs/linux/man/5-githooks/">githooks</a></code>(5).</dl>
<p> -C&lt;n&gt;</p>
<dl>
<dt>
<dd> Ensure at least &lt;n&gt; lines of surrounding context match before and after each change. When fewer lines of surrounding context exist they all must match. By default no context is ever ignored. Implies &#8211;apply. </p>
<p> See also INCOMPATIBLE OPTIONS below.</dl>
<p> &#8211;no-ff, &#8211;force-rebase, -f</p>
<dl>
<dt>
<dd> Individually replay all rebased commits instead of fast-forwarding over the unchanged ones. This ensures that the entire history of the rebased branch is composed of new commits. </p>
<p> You may find this helpful after reverting a topic branch merge, as this option recreates the topic branch with fresh commits so it can be remerged successfully without needing to &quot;revert the reversion&quot; (see the m[blue]<code>revert-a-faulty-merge How-To</code>m[]<font SIZE="-2">[1]</font> for details).</dl>
<p> &#8211;fork-point, &#8211;no-fork-point</p>
<dl>
<dt>
<dd> Use reflog to find a better common ancestor between &lt;upstream&gt; and &lt;branch&gt; when calculating which commits have been introduced by &lt;branch&gt;. </p>
<p> When &#8211;fork-point is active, <i>fork_point</i> will be used instead of &lt;upstream&gt; to calculate the set of commits to rebase, where <i>fork_point</i> is the result of <code>git merge-base &#8211;fork-point &lt;upstream&gt; &lt;branch&gt;</code> command (see <code><a href="/docs/linux/man/1-git-merge-base/">git-merge-base</a></code>(1)). If <i>fork_point</i> ends up being empty, the &lt;upstream&gt; will be used as a fallback. </p>
<p> If &lt;upstream&gt; is given on the command line, then the default is <code>&#8211;no-fork-point</code>, otherwise the default is <code>&#8211;fork-point</code>. See also <code>rebase.forkpoint</code> in <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1). </p>
<p> If your branch was based on &lt;upstream&gt; but &lt;upstream&gt; was rewound and your branch contains commits which were dropped, this option can be used with <code>&#8211;keep-base</code> in order to drop those commits from your branch. </p>
<p> See also INCOMPATIBLE OPTIONS below.</dl>
<p> &#8211;ignore-whitespace</p>
<dl>
<dt>
<dd> Ignore whitespace differences when trying to reconcile differences. Currently, each backend implements an approximation of this behavior: </p>
<p> apply backend: When applying a patch, ignore changes in whitespace in context lines. Unfortunately, this means that if the &quot;old&quot; lines being replaced by the patch differ only in whitespace from the existing file, you will get a merge conflict instead of a successful patch application. </p>
<p> merge backend: Treat lines with only whitespace changes as unchanged when merging. Unfortunately, this means that any patch hunks that were intended to modify whitespace and nothing else will be dropped, even if the other side had no changes that conflicted.</dl>
<p> &#8211;whitespace=&lt;option&gt;</p>
<dl>
<dt>
<dd> This flag is passed to the <i>git apply</i> program (see <code><a href="/docs/linux/man/1-git-apply/">git-apply</a></code>(1)) that applies the patch. Implies &#8211;apply. </p>
<p> See also INCOMPATIBLE OPTIONS below.</dl>
<p> &#8211;committer-date-is-author-date</p>
<dl>
<dt>
<dd> Instead of using the current time as the committer date, use the author date of the commit being rebased as the committer date. This option implies <code>&#8211;force-rebase</code>.</dl>
<p> &#8211;ignore-date, &#8211;reset-author-date</p>
<dl>
<dt>
<dd> Instead of using the author date of the original commit, use the current time as the author date of the rebased commit. This option implies <code>&#8211;force-rebase</code>. </p>
<p> See also INCOMPATIBLE OPTIONS below.</dl>
<p> &#8211;signoff</p>
<dl>
<dt>
<dd> Add a <code>Signed-off-by</code> trailer to all the rebased commits. Note that if <code>&#8211;interactive</code> is given then only commits marked to be picked, edited or reworded will have the trailer added. </p>
<p> See also INCOMPATIBLE OPTIONS below.</dl>
<p> -i, &#8211;interactive</p>
<dl>
<dt>
<dd> Make a list of the commits which are about to be rebased. Let the user edit that list before rebasing. This mode can also be used to split commits (see SPLITTING COMMITS below). </p>
<p> The commit list format can be changed by setting the configuration option rebase.instructionFormat. A customized instruction format will automatically have the long commit hash prepended to the format. </p>
<p> See also INCOMPATIBLE OPTIONS below.</dl>
<p> -r, &#8211;rebase-merges[=(rebase-cousins|no-rebase-cousins)]</p>
<dl>
<dt>
<dd> By default, a rebase will simply drop merge commits from the todo list, and put the rebased commits into a single, linear branch. With <code>&#8211;rebase-merges</code>, the rebase will instead try to preserve the branching structure within the commits that are to be rebased, by recreating the merge commits. Any resolved merge conflicts or manual amendments in these merge commits will have to be resolved/re-applied manually. </p>
<p> By default, or when <code>no-rebase-cousins</code> was specified, commits which do not have <code>&lt;upstream&gt;</code> as direct ancestor will keep their original branch point, i.e. commits that would be excluded by <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1)&#8217;s <code>&#8211;ancestry-path</code> option will keep their original ancestry by default. If the <code>rebase-cousins</code> mode is turned on, such commits are instead rebased onto <code>&lt;upstream&gt;</code> (or <code>&lt;onto&gt;</code>, if specified). </p>
<p> It is currently only possible to recreate the merge commits using the <code>ort</code> merge strategy; different merge strategies can be used only via explicit <code>exec git merge -s &lt;strategy&gt; [&#8230;]</code> commands. </p>
<p> See also REBASING MERGES and INCOMPATIBLE OPTIONS below.</dl>
<p> -x &lt;cmd&gt;, &#8211;exec &lt;cmd&gt;</p>
<dl>
<dt>
<dd> Append &quot;exec &lt;cmd&gt;&quot; after each line creating a commit in the final history. &lt;cmd&gt; will be interpreted as one or more shell commands. Any command that fails will interrupt the rebase, with exit code 1. </p>
<p> You may execute several commands by either using one instance of <code>&#8211;exec</code> with several commands: </p>
<dl>
<dt>
<dd>
<pre>
git rebase -i --exec &quot;cmd1 &amp;&amp; cmd2 &amp;&amp; ...&quot;
</pre>
</dl>
<p> or by giving more than one <code>&#8211;exec</code>: </p>
<dl>
<dt>
<dd>
<pre>
git rebase -i --exec &quot;cmd1&quot; --exec &quot;cmd2&quot; --exec ...
</pre>
</dl>
<p> If <code>&#8211;autosquash</code> is used, &quot;exec&quot; lines will not be appended for the intermediate commits, and will only appear at the end of each squash/fixup series. </p>
<p> This uses the <code>&#8211;interactive</code> machinery internally, but it can be run without an explicit <code>&#8211;interactive</code>. </p>
<p> See also INCOMPATIBLE OPTIONS below.</dl>
<p> &#8211;root</p>
<dl>
<dt>
<dd> Rebase all commits reachable from &lt;branch&gt;, instead of limiting them with an &lt;upstream&gt;. This allows you to rebase the root commit(s) on a branch. When used with &#8211;onto, it will skip changes already contained in &lt;newbase&gt; (instead of &lt;upstream&gt;) whereas without &#8211;onto it will operate on every change. </p>
<p> See also INCOMPATIBLE OPTIONS below.</dl>
<p> &#8211;autosquash, &#8211;no-autosquash</p>
<dl>
<dt>
<dd> When the commit log message begins with &quot;squash! &#8230;&quot; or &quot;fixup! &#8230;&quot; or &quot;amend! &#8230;&quot;, and there is already a commit in the todo list that matches the same <code>&#8230;</code>, automatically modify the todo list of <code>rebase -i</code>, so that the commit marked for squashing comes right after the commit to be modified, and change the action of the moved commit from <code>pick</code> to <code>squash</code> or <code>fixup</code> or <code>fixup -C</code> respectively. A commit matches the <code>&#8230;</code> if the commit subject matches, or if the <code>&#8230;</code> refers to the commit&#8217;s hash. As a fall-back, partial matches of the commit subject work, too. The recommended way to create fixup/amend/squash commits is by using the <code>&#8211;fixup</code>, <code>&#8211;fixup=amend:</code> or <code>&#8211;fixup=reword:</code> and <code>&#8211;squash</code> options respectively of <code><a href="/docs/linux/man/1-git-commit/">git-commit</a></code>(1). </p>
<p> If the <code>&#8211;autosquash</code> option is enabled by default using the configuration variable <code>rebase.autoSquash</code>, this option can be used to override and disable this setting. </p>
<p> See also INCOMPATIBLE OPTIONS below.</dl>
<p> &#8211;autostash, &#8211;no-autostash</p>
<dl>
<dt>
<dd> Automatically create a temporary stash entry before the operation begins, and apply it after the operation ends. This means that you can run rebase on a dirty worktree. However, use with care: the final stash application after a successful rebase might result in non-trivial conflicts.</dl>
<p> &#8211;reschedule-failed-exec, &#8211;no-reschedule-failed-exec</p>
<dl>
<dt>
<dd> Automatically reschedule <code>exec</code> commands that failed. This only makes sense in interactive mode (or when an <code>&#8211;exec</code> option was provided). </p>
<p> Even though this option applies once a rebase is started, it&#8217;s set for the whole rebase at the start based on either the <code>rebase.rescheduleFailedExec</code> configuration (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1) or &quot;CONFIGURATION&quot; below) or whether this option is provided. Otherwise an explicit <code>&#8211;no-reschedule-failed-exec</code> at the start would be overridden by the presence of <code>rebase.rescheduleFailedExec=true</code> configuration.</dl>
<h2>INCOMPATIBLE OPTIONS</h2>
<p> The following options: </p>
<dl>
<dt>
<dd> &bull; &#8211;apply</dl>
<dl>
<dt>
<dd> &bull; &#8211;whitespace</dl>
<dl>
<dt>
<dd> &bull; -C</dl>
<p> are incompatible with the following options: </p>
<dl>
<dt>
<dd> &bull; &#8211;merge</dl>
<dl>
<dt>
<dd> &bull; &#8211;strategy</dl>
<dl>
<dt>
<dd> &bull; &#8211;strategy-option</dl>
<dl>
<dt>
<dd> &bull; &#8211;allow-empty-message</dl>
<dl>
<dt>
<dd> &bull; &#8211;[no-]autosquash</dl>
<dl>
<dt>
<dd> &bull; &#8211;rebase-merges</dl>
<dl>
<dt>
<dd> &bull; &#8211;interactive</dl>
<dl>
<dt>
<dd> &bull; &#8211;exec</dl>
<dl>
<dt>
<dd> &bull; &#8211;no-keep-empty</dl>
<dl>
<dt>
<dd> &bull; &#8211;empty=</dl>
<dl>
<dt>
<dd> &bull; &#8211;reapply-cherry-picks</dl>
<dl>
<dt>
<dd> &bull; &#8211;edit-todo</dl>
<dl>
<dt>
<dd> &bull; &#8211;root when used in combination with &#8211;onto</dl>
<p> In addition, the following pairs of options are incompatible: </p>
<dl>
<dt>
<dd> &bull; &#8211;keep-base and &#8211;onto</dl>
<dl>
<dt>
<dd> &bull; &#8211;keep-base and &#8211;root</dl>
<dl>
<dt>
<dd> &bull; &#8211;fork-point and &#8211;root</dl>
<h2>BEHAVIORAL DIFFERENCES</h2>
<p> git rebase has two primary backends: apply and merge. (The apply backend used to be known as the <i>am</i> backend, but the name led to confusion as it looks like a verb instead of a noun. Also, the merge backend used to be known as the interactive backend, but it is now used for non-interactive cases as well. Both were renamed based on lower-level functionality that underpinned each.) There are some subtle differences in how these two backends behave:</p>
<h3>Empty commits</h3>
<p> The apply backend unfortunately drops intentionally empty commits, i.e. commits that started empty, though these are rare in practice. It also drops commits that become empty and has no option for controlling this behavior. </p>
<p> The merge backend keeps intentionally empty commits by default (though with -i they are marked as empty in the todo list editor, or they can be dropped automatically with &#8211;no-keep-empty). </p>
<p> Similar to the apply backend, by default the merge backend drops commits that become empty unless -i/&#8211;interactive is specified (in which case it stops and asks the user what to do). The merge backend also has an &#8211;empty={drop,keep,ask} option for changing the behavior of handling commits that become empty.</p>
<h3>Directory rename detection</h3>
<p> Due to the lack of accurate tree information (arising from constructing fake ancestors with the limited information available in patches), directory rename detection is disabled in the apply backend. Disabled directory rename detection means that if one side of history renames a directory and the other adds new files to the old directory, then the new files will be left behind in the old directory without any warning at the time of rebasing that you may want to move these files into the new directory. </p>
<p> Directory rename detection works with the merge backend to provide you warnings in such cases.</p>
<h3>Context</h3>
<p> The apply backend works by creating a sequence of patches (by calling <code>format-patch</code> internally), and then applying the patches in sequence (calling <code>am</code> internally). Patches are composed of multiple hunks, each with line numbers, a context region, and the actual changes. The line numbers have to be taken with some fuzz, since the other side will likely have inserted or deleted lines earlier in the file. The context region is meant to help find how to adjust the line numbers in order to apply the changes to the right lines. However, if multiple areas of the code have the same surrounding lines of context, the wrong one can be picked. There are real-world cases where this has caused commits to be reapplied incorrectly with no conflicts reported. Setting diff.context to a larger value may prevent such types of problems, but increases the chance of spurious conflicts (since it will require more lines of matching context to apply). </p>
<p> The merge backend works with a full copy of each relevant file, insulating it from these types of problems.</p>
<h3>Labelling of conflicts markers</h3>
<p> When there are content conflicts, the merge machinery tries to annotate each side&#8217;s conflict markers with the commits where the content came from. Since the apply backend drops the original information about the rebased commits and their parents (and instead generates new fake commits based off limited information in the generated patches), those commits cannot be identified; instead it has to fall back to a commit summary. Also, when merge.conflictStyle is set to diff3, the apply backend will use &quot;constructed merge base&quot; to label the content from the merge base, and thus provide no information about the merge base commit whatsoever. </p>
<p> The merge backend works with the full commits on both sides of history and thus has no such limitations.</p>
<h3>Hooks</h3>
<p> The apply backend has not traditionally called the post-commit hook, while the merge backend has. Both have called the post-checkout hook, though the merge backend has squelched its output. Further, both backends only call the post-checkout hook with the starting point commit of the rebase, not the intermediate commits nor the final commit. In each case, the calling of these hooks was by accident of implementation rather than by design (both backends were originally implemented as shell scripts and happened to invoke other commands like <i>git checkout</i> or <i>git commit</i> that would call the hooks). Both backends should have the same behavior, though it is not entirely clear which, if any, is correct. We will likely make rebase stop calling either of these hooks in the future.</p>
<h3>Interruptability</h3>
<p> The apply backend has safety problems with an ill-timed interrupt; if the user presses Ctrl-C at the wrong time to try to abort the rebase, the rebase can enter a state where it cannot be aborted with a subsequent <code>git rebase &#8211;abort</code>. The merge backend does not appear to suffer from the same shortcoming. (See m[blue]<code><a rel="nofollow" href="https://lore.kernel.org/git/20200207132152.GC2868@szeder.dev/">https://lore.kernel.org/git/20200207132152.GC2868@szeder.dev/</a></code>m[] for details.)</p>
<h3>Commit Rewording</h3>
<p> When a conflict occurs while rebasing, rebase stops and asks the user to resolve. Since the user may need to make notable changes while resolving conflicts, after conflicts are resolved and the user has run <code>git rebase &#8211;continue</code>, the rebase should open an editor and ask the user to update the commit message. The merge backend does this, while the apply backend blindly applies the original commit message.</p>
<h3>Miscellaneous differences</h3>
<p> There are a few more behavioral differences that most folks would probably consider inconsequential but which are mentioned for completeness: </p>
<dl>
<dt>
<dd> &bull; Reflog: The two backends will use different wording when describing the changes made in the reflog, though both will make use of the word &quot;rebase&quot;.</dl>
<dl>
<dt>
<dd> &bull; Progress, informational, and error messages: The two backends provide slightly different progress and informational messages. Also, the apply backend writes error messages (such as &quot;Your files would be overwritten&#8230;&quot;) to stdout, while the merge backend writes them to stderr.</dl>
<dl>
<dt>
<dd> &bull; State directories: The two backends keep their state in different directories under .git/</dl>
<h2>MERGE STRATEGIES</h2>
<p> The merge mechanism (<code>git merge</code> and <code>git pull</code> commands) allows the backend <i>merge strategies</i> to be chosen with <code>-s</code> option. Some strategies can also take their own options, which can be passed by giving <code>-X&lt;option&gt;</code> arguments to <code>git merge</code> and/or <code>git pull</code>. </p>
<p> ort</p>
<dl>
<dt>
<dd> This is the default merge strategy when pulling or merging one branch. This strategy can only resolve two heads using a 3-way merge algorithm. When there is more than one common ancestor that can be used for 3-way merge, it creates a merged tree of the common ancestors and uses that as the reference tree for the 3-way merge. This has been reported to result in fewer merge conflicts without causing mismerges by tests done on actual merge commits taken from Linux 2.6 kernel development history. Additionally this strategy can detect and handle merges involving renames. It does not make use of detected copies. The name for this algorithm is an acronym (&quot;Ostensibly Recursive&#8217;s Twin&quot;) and came from the fact that it was written as a replacement for the previous default algorithm, <code>recursive</code>. </p>
<p> The <i>ort</i> strategy can take the following options: </p>
<p> ours</p>
<dl>
<dt>
<dd> This option forces conflicting hunks to be auto-resolved cleanly by favoring <i>our</i> version. Changes from the other tree that do not conflict with our side are reflected in the merge result. For a binary file, the entire contents are taken from our side. </p>
<p> This should not be confused with the <i>ours</i> merge strategy, which does not even look at what the other tree contains at all. It discards everything the other tree did, declaring <i>our</i> history contains all that happened in it.</dl>
<p> theirs</p>
<dl>
<dt>
<dd> This is the opposite of <i>ours</i>; note that, unlike <i>ours</i>, there is no <i>theirs</i> merge strategy to confuse this merge option with.</dl>
<p> ignore-space-change, ignore-all-space, ignore-space-at-eol, ignore-cr-at-eol</p>
<dl>
<dt>
<dd> Treats lines with the indicated type of whitespace change as unchanged for the sake of a three-way merge. Whitespace changes mixed with other changes to a line are not ignored. See also <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1) <code>-b</code>, <code>-w</code>, <code>&#8211;ignore-space-at-eol</code>, and <code>&#8211;ignore-cr-at-eol</code>. </p>
<dl>
<dt>
<dd> &bull; If <i>their</i> version only introduces whitespace changes to a line, <i>our</i> version is used;</dl>
<dl>
<dt>
<dd> &bull; If <i>our</i> version introduces whitespace changes but <i>their</i> version includes a substantial change, <i>their</i> version is used;</dl>
<dl>
<dt>
<dd> &bull; Otherwise, the merge proceeds in the usual way.</dl>
</dl>
<p> renormalize</p>
<dl>
<dt>
<dd> This runs a virtual check-out and check-in of all three stages of a file when resolving a three-way merge. This option is meant to be used when merging branches with different clean filters or end-of-line normalization rules. See &quot;Merging branches with differing checkin/checkout attributes&quot; in <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5) for details.</dl>
<p> no-renormalize</p>
<dl>
<dt>
<dd> Disables the <code>renormalize</code> option. This overrides the <code>merge.renormalize</code> configuration variable.</dl>
<p> find-renames[=&lt;n&gt;]</p>
<dl>
<dt>
<dd> Turn on rename detection, optionally setting the similarity threshold. This is the default. This overrides the <i>merge.renames</i> configuration variable. See also <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1) <code>&#8211;find-renames</code>.</dl>
<p> rename-threshold=&lt;n&gt;</p>
<dl>
<dt>
<dd> Deprecated synonym for <code>find-renames=&lt;n&gt;</code>.</dl>
<p> subtree[=&lt;path&gt;]</p>
<dl>
<dt>
<dd> This option is a more advanced form of <i>subtree</i> strategy, where the strategy makes a guess on how two trees must be shifted to match with each other when merging. Instead, the specified path is prefixed (or stripped from the beginning) to make the shape of two trees to match.</dl>
</dl>
<p> recursive</p>
<dl>
<dt>
<dd> This can only resolve two heads using a 3-way merge algorithm. When there is more than one common ancestor that can be used for 3-way merge, it creates a merged tree of the common ancestors and uses that as the reference tree for the 3-way merge. This has been reported to result in fewer merge conflicts without causing mismerges by tests done on actual merge commits taken from Linux 2.6 kernel development history. Additionally this can detect and handle merges involving renames. It does not make use of detected copies. This was the default strategy for resolving two heads from Git v0.99.9k until v2.33.0. </p>
<p> The <i>recursive</i> strategy takes the same options as <i>ort</i>. However, there are three additional options that <i>ort</i> ignores (not documented above) that are potentially useful with the <i>recursive</i> strategy: </p>
<p> patience</p>
<dl>
<dt>
<dd> Deprecated synonym for <code>diff-algorithm=patience</code>.</dl>
<p> diff-algorithm=[patience|minimal|histogram|myers]</p>
<dl>
<dt>
<dd> Use a different diff algorithm while merging, which can help avoid mismerges that occur due to unimportant matching lines (such as braces from distinct functions). See also <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1) <code>&#8211;diff-algorithm</code>. Note that <code>ort</code> specifically uses <code>diff-algorithm=histogram</code>, while <code>recursive</code> defaults to the <code>diff.algorithm</code> config setting.</dl>
<p> no-renames</p>
<dl>
<dt>
<dd> Turn off rename detection. This overrides the <code>merge.renames</code> configuration variable. See also <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1) <code>&#8211;no-renames</code>.</dl>
</dl>
<p> resolve</p>
<dl>
<dt>
<dd> This can only resolve two heads (i.e. the current branch and another branch you pulled from) using a 3-way merge algorithm. It tries to carefully detect criss-cross merge ambiguities. It does not handle renames.</dl>
<p> octopus</p>
<dl>
<dt>
<dd> This resolves cases with more than two heads, but refuses to do a complex merge that needs manual resolution. It is primarily meant to be used for bundling topic branch heads together. This is the default merge strategy when pulling or merging more than one branch.</dl>
<p> ours</p>
<dl>
<dt>
<dd> This resolves any number of heads, but the resulting tree of the merge is always that of the current branch head, effectively ignoring all changes from all other branches. It is meant to be used to supersede old development history of side branches. Note that this is different from the -Xours option to the <i>recursive</i> merge strategy.</dl>
<p> subtree</p>
<dl>
<dt>
<dd> This is a modified <code>ort</code> strategy. When merging trees A and B, if B corresponds to a subtree of A, B is first adjusted to match the tree structure of A, instead of reading the trees at the same level. This adjustment is also done to the common ancestor tree.</dl>
<p> With the strategies that use 3-way merge (including the default, <i>ort</i>), if a change is made on both branches, but later reverted on one of the branches, that change will be present in the merged result; some people find this behavior confusing. It occurs because only the heads and the merge base are considered when performing a merge, not the individual commits. The merge algorithm therefore considers the reverted change as no change at all, and substitutes the changed version instead.</p>
<h2>NOTES</h2>
<p> You should understand the implications of using <i>git rebase</i> on a repository that you share. See also RECOVERING FROM UPSTREAM REBASE below. </p>
<p> When the git-rebase command is run, it will first execute a &quot;pre-rebase&quot; hook if one exists. You can use this hook to do sanity checks and reject the rebase if it isn&#8217;t appropriate. Please see the template pre-rebase hook script for an example. </p>
<p> Upon completion, &lt;branch&gt; will be the current branch.</p>
<h2>INTERACTIVE MODE</h2>
<p> Rebasing interactively means that you have a chance to edit the commits which are rebased. You can reorder the commits, and you can remove them (weeding out bad or otherwise unwanted patches). </p>
<p> The interactive mode is meant for this type of workflow: </p>
<dl>
<dt>
<dd> 1. have a wonderful idea</dl>
<dl>
<dt>
<dd> 2. hack on the code</dl>
<dl>
<dt>
<dd> 3. prepare a series for submission</dl>
<dl>
<dt>
<dd> 4. submit</dl>
<p> where point 2. consists of several instances of </p>
<p> a) regular use </p>
<dl>
<dt>
<dd> 1. finish something worthy of a commit</dl>
<dl>
<dt>
<dd> 2. commit</dl>
<p> b) independent fixup </p>
<dl>
<dt>
<dd> 1. realize that something does not work</dl>
<dl>
<dt>
<dd> 2. fix that</dl>
<dl>
<dt>
<dd> 3. commit it</dl>
<p> Sometimes the thing fixed in b.2. cannot be amended to the not-quite perfect commit it fixes, because that commit is buried deeply in a patch series. That is exactly what interactive rebase is for: use it after plenty of &quot;a&quot;s and &quot;b&quot;s, by rearranging and editing commits, and squashing multiple commits into one. </p>
<p> Start it with the last commit you want to retain as-is: </p>
<dl>
<dt>
<dd>
<pre>
git rebase -i &lt;after-this-commit&gt;
</pre>
</dl>
<p> An editor will be fired up with all the commits in your current branch (ignoring merge commits), which come after the given commit. You can reorder the commits in this list to your heart&#8217;s content, and you can remove them. The list looks more or less like this: </p>
<dl>
<dt>
<dd>
<pre>
pick deadbee The oneline of this commit
pick fa1afe1 The oneline of the next commit
...
</pre>
</dl>
<p> The oneline descriptions are purely for your pleasure; <i>git rebase</i> will not look at them but at the commit names (&quot;deadbee&quot; and &quot;fa1afe1&quot; in this example), so do not delete or edit the names. </p>
<p> By replacing the command &quot;pick&quot; with the command &quot;edit&quot;, you can tell <i>git rebase</i> to stop after applying that commit, so that you can edit the files and/or the commit message, amend the commit, and continue rebasing. </p>
<p> To interrupt the rebase (just like an &quot;edit&quot; command would do, but without cherry-picking any commit first), use the &quot;break&quot; command. </p>
<p> If you just want to edit the commit message for a commit, replace the command &quot;pick&quot; with the command &quot;reword&quot;. </p>
<p> To drop a commit, replace the command &quot;pick&quot; with &quot;drop&quot;, or just delete the matching line. </p>
<p> If you want to fold two or more commits into one, replace the command &quot;pick&quot; for the second and subsequent commits with &quot;squash&quot; or &quot;fixup&quot;. If the commits had different authors, the folded commit will be attributed to the author of the first commit. The suggested commit message for the folded commit is the concatenation of the first commit&#8217;s message with those identified by &quot;squash&quot; commands, omitting the messages of commits identified by &quot;fixup&quot; commands, unless &quot;fixup -c&quot; is used. In that case the suggested commit message is only the message of the &quot;fixup -c&quot; commit, and an editor is opened allowing you to edit the message. The contents (patch) of the &quot;fixup -c&quot; commit are still incorporated into the folded commit. If there is more than one &quot;fixup -c&quot; commit, the message from the final one is used. You can also use &quot;fixup -C&quot; to get the same behavior as &quot;fixup -c&quot; except without opening an editor. </p>
<p> <i>git rebase</i> will stop when &quot;pick&quot; has been replaced with &quot;edit&quot; or when a command fails due to merge errors. When you are done editing and/or resolving conflicts you can continue with <code>git rebase &#8211;continue</code>. </p>
<p> For example, if you want to reorder the last 5 commits, such that what was HEAD~4 becomes the new HEAD. To achieve that, you would call <i>git rebase</i> like this: </p>
<dl>
<dt>
<dd>
<pre>
$ git rebase -i HEAD~5
</pre>
</dl>
<p> And move the first patch to the end of the list. </p>
<p> You might want to recreate merge commits, e.g. if you have a history like this: </p>
<dl>
<dt>
<dd>
X</p>
<p>        A&#8211; &#8211;<br />
    M&#8211; &#8211; B / &#8212; -o&#8211; &#8211; O&#8211; &#8211; P&#8211; &#8211; Q
</dl>
<p> Suppose you want to rebase the side branch starting at &quot;A&quot; to &quot;Q&quot;. Make sure that the current HEAD is &quot;B&quot;, and call </p>
<dl>
<dt>
<dd>
<pre>
$ git rebase -i -r --onto Q O
</pre>
</dl>
<p> Reordering and editing commits usually creates untested intermediate steps. You may want to check that your history editing did not break anything by running a test, or at least recompiling at intermediate points in history by using the &quot;exec&quot; command (shortcut &quot;x&quot;). You may do so by creating a todo list like this one: </p>
<dl>
<dt>
<dd>
<pre>
pick deadbee Implement feature XXX
fixup f1a5c00 Fix to feature XXX
exec make
pick c0ffeee The oneline of the next commit
edit deadbab The oneline of the commit after
exec cd subdir; make test
...
</pre>
</dl>
<p> The interactive rebase will stop when a command fails (i.e. exits with non-0 status) to give you an opportunity to fix the problem. You can continue with <code>git rebase &#8211;continue</code>. </p>
<p> The &quot;exec&quot; command launches the command in a shell (the one specified in <code>$SHELL</code>, or the default shell if <code>$SHELL</code> is not set), so you can use shell features (like &quot;cd&quot;, &quot;&gt;&quot;, &quot;;&quot; &#8230;). The command is run from the root of the working tree. </p>
<dl>
<dt>
<dd>
<pre>
$ git rebase -i --exec &quot;make test&quot;
</pre>
</dl>
<p> This command lets you check that intermediate commits are compilable. The todo list becomes like that: </p>
<dl>
<dt>
<dd>
<pre>
pick 5928aea one
exec make test
pick 04d0fda two
exec make test
pick ba46169 three
exec make test
pick f4593f9 four
exec make test
</pre>
</dl>
<h2>SPLITTING COMMITS</h2>
<p> In interactive mode, you can mark commits with the action &quot;edit&quot;. However, this does not necessarily mean that <i>git rebase</i> expects the result of this edit to be exactly one commit. Indeed, you can undo the commit, or you can add other commits. This can be used to split a commit into two: </p>
<dl>
<dt>
<dd> &bull; Start an interactive rebase with <code>git rebase -i &lt;commit&gt;^</code>, where &lt;commit&gt; is the commit you want to split. In fact, any commit range will do, as long as it contains that commit.</dl>
<dl>
<dt>
<dd> &bull; Mark the commit you want to split with the action &quot;edit&quot;.</dl>
<dl>
<dt>
<dd> &bull; When it comes to editing that commit, execute <code>git reset HEAD^</code>. The effect is that the HEAD is rewound by one, and the index follows suit. However, the working tree stays the same.</dl>
<dl>
<dt>
<dd> &bull; Now add the changes to the index that you want to have in the first commit. You can use <code>git add</code> (possibly interactively) or <i>git gui</i> (or both) to do that.</dl>
<dl>
<dt>
<dd> &bull; Commit the now-current index with whatever commit message is appropriate now.</dl>
<dl>
<dt>
<dd> &bull; Repeat the last two steps until your working tree is clean.</dl>
<dl>
<dt>
<dd> &bull; Continue the rebase with <code>git rebase &#8211;continue</code>.</dl>
<p> If you are not absolutely sure that the intermediate revisions are consistent (they compile, pass the testsuite, etc.) you should use <i>git stash</i> to stash away the not-yet-committed changes after each commit, test, and amend the commit if fixes are necessary.</p>
<h2>RECOVERING FROM UPSTREAM REBASE</h2>
<p> Rebasing (or any other form of rewriting) a branch that others have based work on is a bad idea: anyone downstream of it is forced to manually fix their history. This section explains how to do the fix from the downstream&#8217;s point of view. The real fix, however, would be to avoid rebasing the upstream in the first place. </p>
<p> To illustrate, suppose you are in a situation where someone develops a <i>subsystem</i> branch, and you are working on a <i>topic</i> that is dependent on this <i>subsystem</i>. You might end up with a history like the following: </p>
<dl>
<dt>
<dd>
o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; o master</p>
<p>                                              o&#8211; &#8211;<br />
    o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; o subsystem</p>
<p>                          * &#8212; -*&#8211; -*topic
</dl>
<p> If <i>subsystem</i> is rebased against <i>master</i>, the following happens: </p>
<dl>
<dt>
<dd>
o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; o master<br />
         \ o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; o o &#8216;&#8211;o&#8217; &#8211;o &#8216;&#8211;o&#8217; &#8211;o&#8217;  subsystem</p>
<p>                                        * &#8212; -*&#8211; -*topic
</dl>
<p> If you now continue development as usual, and eventually merge <i>topic</i> to <i>subsystem</i>, the commits from <i>subsystem</i> will remain duplicated forever: </p>
<dl>
<dt>
<dd>
o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; o master<br />
         \ o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; o&#8211; &#8211; o o &#8216;&#8211;o&#8217; &#8211;o &#8216;&#8211;o&#8217; &#8211;o&#8217;&#8211;M  subsystem<br />
                           \ / *&#8211; -*&#8211; -*-&#8230;&#8230;&#8230;.- *&#8211;*topic
</dl>
<p> Such duplicates are generally frowned upon because they clutter up history, making it harder to follow. To clean things up, you need to transplant the commits on <i>topic</i> to the new <i>subsystem</i> tip, i.e., rebase <i>topic</i>. This becomes a ripple effect: anyone downstream from <i>topic</i> is forced to rebase too, and so on! </p>
<p> There are two kinds of fixes, discussed in the following subsections: </p>
<p> Easy case: The changes are literally the same.</p>
<dl>
<dt>
<dd> This happens if the <i>subsystem</i> rebase was a simple rebase and had no conflicts.</dl>
<p> Hard case: The changes are not the same.</p>
<dl>
<dt>
<dd> This happens if the <i>subsystem</i> rebase had conflicts, or used <code>&#8211;interactive</code> to omit, edit, squash, or fixup commits; or if the upstream used one of <code>commit &#8211;amend</code>, <code>reset</code>, or a full history rewriting command like m[blue]<code>filter-repo</code>m[]<font SIZE="-2">[2]</font>.</dl>
<h3>The easy case</h3>
<p> Only works if the changes (patch IDs based on the diff contents) on <i>subsystem</i> are literally the same before and after the rebase <i>subsystem</i> did. </p>
<p> In that case, the fix is easy because <i>git rebase</i> knows to skip changes that are already present in the new upstream (unless <code>&#8211;reapply-cherry-picks</code> is given). So if you say (assuming you&#8217;re on <i>topic</i>) </p>
<dl>
<dt>
<dd>
<pre>
    $ git rebase subsystem
</pre>
</dl>
<p> you will end up with the fixed history </p>
<dl>
<dt>
<dd>
<pre><code>
o-- - o-- - o-- - o-- - o-- - o-- - o-- - o master

                                                  o '--o' --o '--o' --o'  subsystem

                                              * -- -*-- -*topic
</code></pre>
</dl>
<h3>The hard case</h3>
<p> Things get more complicated if the <i>subsystem</i> changes do not exactly correspond to the ones before the rebase. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> While an &quot;easy case recovery&quot; sometimes appears to be successful even in the hard case, it may have unintended consequences. For example, a commit that was removed via <code>git rebase &#8211;interactive</code> will be <code>resurrected</code>! </p>
</dl>
<p> The idea is to manually tell <i>git rebase</i> &quot;where the old <i>subsystem</i> ended and your <i>topic</i> began&quot;, that is, what the old merge base between them was. You will have to find a way to name the last commit of the old <i>subsystem</i>, for example: </p>
<dl>
<dt>
<dd> &bull; With the <i>subsystem</i> reflog: after <i>git fetch</i>, the old tip of <i>subsystem</i> is at <code>subsystem@{1}</code>. Subsequent fetches will increase the number. (See <code><a href="/docs/linux/man/1-git-reflog/">git-reflog</a></code>(1).)</dl>
<dl>
<dt>
<dd> &bull; Relative to the tip of <i>topic</i>: knowing that your <i>topic</i> has three commits, the old tip of <i>subsystem</i> must be <code>topic~3</code>.</dl>
<p> You can then transplant the old <code>subsystem..topic</code> to the new tip by saying (for the reflog case, and assuming you are on <i>topic</i> already): </p>
<dl>
<dt>
<dd>
<pre>
    $ git rebase --onto subsystem subsystem@{1}
</pre>
</dl>
<p> The ripple effect of a &quot;hard case&quot; recovery is especially bad: <i>everyone</i> downstream from <i>topic</i> will now have to perform a &quot;hard case&quot; recovery too!</p>
<h2>REBASING MERGES</h2>
<p> The interactive rebase command was originally designed to handle individual patch series. As such, it makes sense to exclude merge commits from the todo list, as the developer may have merged the then-current <code>master</code> while working on the branch, only to rebase all the commits onto <code>master</code> eventually (skipping the merge commits). </p>
<p> However, there are legitimate reasons why a developer may want to recreate merge commits: to keep the branch structure (or &quot;commit topology&quot;) when working on multiple, inter-related branches. </p>
<p> In the following example, the developer works on a topic branch that refactors the way buttons are defined, and on another topic branch that uses that refactoring to implement a &quot;Report a bug&quot; button. The output of <code>git log &#8211;graph &#8211;format=%s -5</code> may look like this: </p>
<dl>
<dt>
<dd>
<pre>
*   Merge branch 'report-a-bug'
|\
| * Add the feedback button
* | Merge branch 'refactor-button'
|\ \
| |/
| * Use the Button class for all buttons
| * Extract a generic Button class from the DownloadButton one
</pre>
</dl>
<p> The developer might want to rebase those commits to a newer <code>master</code> while keeping the branch topology, for example when the first topic branch is expected to be integrated into <code>master</code> much earlier than the second one, say, to resolve merge conflicts with changes to the DownloadButton class that made it into <code>master</code>. </p>
<p> This rebase can be performed using the <code>&#8211;rebase-merges</code> option. It will generate a todo list looking like this: </p>
<dl>
<dt>
<dd>
<pre>
label onto
# Branch: refactor-button
reset onto
pick 123456 Extract a generic Button class from the DownloadButton one
pick 654321 Use the Button class for all buttons
label refactor-button
# Branch: report-a-bug
reset refactor-button # Use the Button class for all buttons
pick abcdef Add the feedback button
label report-a-bug
reset onto
merge -C a1b2c3 refactor-button # Merge 'refactor-button'
merge -C 6f5e4d report-a-bug # Merge 'report-a-bug'
</pre>
</dl>
<p> In contrast to a regular interactive rebase, there are <code>label</code>, <code>reset</code> and <code>merge</code> commands in addition to <code>pick</code> ones. </p>
<p> The <code>label</code> command associates a label with the current HEAD when that command is executed. These labels are created as worktree-local refs (<code>refs/rewritten/&lt;label&gt;</code>) that will be deleted when the rebase finishes. That way, rebase operations in multiple worktrees linked to the same repository do not interfere with one another. If the <code>label</code> command fails, it is rescheduled immediately, with a helpful message how to proceed. </p>
<p> The <code>reset</code> command resets the HEAD, index and worktree to the specified revision. It is similar to an <code>exec git reset &#8211;hard &lt;label&gt;</code>, but refuses to overwrite untracked files. If the <code>reset</code> command fails, it is rescheduled immediately, with a helpful message how to edit the todo list (this typically happens when a <code>reset</code> command was inserted into the todo list manually and contains a typo). </p>
<p> The <code>merge</code> command will merge the specified revision(s) into whatever is HEAD at that time. With <code>-C &lt;original-commit&gt;</code>, the commit message of the specified merge commit will be used. When the <code>-C</code> is changed to a lower-case <code>-c</code>, the message will be opened in an editor after a successful merge so that the user can edit the message. </p>
<p> If a <code>merge</code> command fails for any reason other than merge conflicts (i.e. when the merge operation did not even start), it is rescheduled immediately. </p>
<p> By default, the <code>merge</code> command will use the <code>ort</code> merge strategy for regular merges, and <code>octopus</code> for octopus merges. One can specify a default strategy for all merges using the <code>&#8211;strategy</code> argument when invoking rebase, or can override specific merges in the interactive list of commands by using an <code>exec</code> command to call <code>git merge</code> explicitly with a <code>&#8211;strategy</code> argument. Note that when calling <code>git merge</code> explicitly like this, you can make use of the fact that the labels are worktree-local refs (the ref <code>refs/rewritten/onto</code> would correspond to the label <code>onto</code>, for example) in order to refer to the branches you want to merge. </p>
<p> Note: the first command (<code>label onto</code>) labels the revision onto which the commits are rebased; The name <code>onto</code> is just a convention, as a nod to the <code>&#8211;onto</code> option. </p>
<p> It is also possible to introduce completely new merge commits from scratch by adding a command of the form <code>merge &lt;merge-head&gt;</code>. This form will generate a tentative commit message and always open an editor to let the user edit it. This can be useful e.g. when a topic branch turns out to address more than a single concern and wants to be split into two or even more topic branches. Consider this todo list: </p>
<dl>
<dt>
<dd>
<pre>
pick 192837 Switch from GNU Makefiles to CMake
pick 5a6c7e Document the switch to CMake
pick 918273 Fix detection of OpenSSL in CMake
pick afbecd http: add support for TLS v1.3
pick fdbaec Fix detection of cURL in CMake on Windows
</pre>
</dl>
<p> The one commit in this list that is not related to CMake may very well have been motivated by working on fixing all those bugs introduced by switching to CMake, but it addresses a different concern. To split this branch into two topic branches, the todo list could be edited like this: </p>
<dl>
<dt>
<dd>
<pre>
label onto
pick afbecd http: add support for TLS v1.3
label tlsv1.3
reset onto
pick 192837 Switch from GNU Makefiles to CMake
pick 918273 Fix detection of OpenSSL in CMake
pick fdbaec Fix detection of cURL in CMake on Windows
pick 5a6c7e Document the switch to CMake
label cmake
reset onto
merge tlsv1.3
merge cmake
</pre>
</dl>
<h2>CONFIGURATION</h2>
<p> rebase.backend</p>
<dl>
<dt>
<dd> Default backend to use for rebasing. Possible choices are <i>apply</i> or <i>merge</i>. In the future, if the merge backend gains all remaining capabilities of the apply backend, this setting may become unused.</dl>
<p> rebase.stat</p>
<dl>
<dt>
<dd> Whether to show a diffstat of what changed upstream since the last rebase. False by default.</dl>
<p> rebase.autoSquash</p>
<dl>
<dt>
<dd> If set to true enable <code>&#8211;autosquash</code> option by default.</dl>
<p> rebase.autoStash</p>
<dl>
<dt>
<dd> When set to true, automatically create a temporary stash entry before the operation begins, and apply it after the operation ends. This means that you can run rebase on a dirty worktree. However, use with care: the final stash application after a successful rebase might result in non-trivial conflicts. This option can be overridden by the <code>&#8211;no-autostash</code> and <code>&#8211;autostash</code> options of <code><a href="/docs/linux/man/1-git-rebase/">git-rebase</a></code>(1). Defaults to false.</dl>
<p> rebase.missingCommitsCheck</p>
<dl>
<dt>
<dd> If set to &quot;warn&quot;, git rebase -i will print a warning if some commits are removed (e.g. a line was deleted), however the rebase will still proceed. If set to &quot;error&quot;, it will print the previous warning and stop the rebase, <i>git rebase &#8211;edit-todo</i> can then be used to correct the error. If set to &quot;ignore&quot;, no checking is done. To drop a commit without warning or error, use the <code>drop</code> command in the todo list. Defaults to &quot;ignore&quot;.</dl>
<p> rebase.instructionFormat</p>
<dl>
<dt>
<dd> A format string, as specified in <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1), to be used for the todo list during an interactive rebase. The format will automatically have the long commit hash prepended to the format.</dl>
<p> rebase.abbreviateCommands</p>
<dl>
<dt>
<dd> If set to true, <code>git rebase</code> will use abbreviated command names in the todo list resulting in something like this: </p>
<dl>
<dt>
<dd>
<pre>
        p deadbee The oneline of the commit
        p fa1afe1 The oneline of the next commit
        ...
</pre>
</dl>
<p> instead of: </p>
<dl>
<dt>
<dd>
<pre>
        pick deadbee The oneline of the commit
        pick fa1afe1 The oneline of the next commit
        ...
</pre>
</dl>
<p> Defaults to false.</dl>
<p> rebase.rescheduleFailedExec</p>
<dl>
<dt>
<dd> Automatically reschedule <code>exec</code> commands that failed. This only makes sense in interactive mode (or when an <code>&#8211;exec</code> option was provided). This is the same as specifying the <code>&#8211;reschedule-failed-exec</code> option.</dl>
<p> rebase.forkPoint</p>
<dl>
<dt>
<dd> If set to false set <code>&#8211;no-fork-point</code> option by default.</dl>
<p> sequence.editor</p>
<dl>
<dt>
<dd> Text editor used by <code>git rebase -i</code> for editing the rebase instruction file. The value is meant to be interpreted by the shell when it is used. It can be overridden by the <code>GIT_SEQUENCE_EDITOR</code> environment variable. When not configured the default commit message editor is used instead.</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> revert-a-faulty-merge How-To</p>
<dl>
<dt>
<dd> file:///usr/share/doc/git/html/howto/revert-a-faulty-merge.html</dl>
<dt> 2.</p>
<dd> <code>filter-repo</code></p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://github.com/newren/git-filter-repo">https://github.com/newren/git-filter-repo</a></dl>
</dl>
<h2>Index</h2>

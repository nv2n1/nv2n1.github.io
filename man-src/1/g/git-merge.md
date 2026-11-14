---
title: "git-merge(1)"
name: "git-merge"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-merge/"
description: "git-merge – Join two or more development histories together"
---

<h2 class="name">NAME</h2>
<p> git-merge &#8211; Join two or more development histories together </p>
<h2>SYNOPSIS</h2>
<pre><code>
git merge[-n][--stat][--no - commit][--squash][--[no - ] edit]
         [--no - verify][-s&lt;strategy&gt;][-X&lt;strategy - option&gt;][-S[&lt;keyid&gt;]]
         [--[no - ] allow - unrelated - histories]
         [--[no - ] rerere - autoupdate][-m&lt;msg&gt;][-F&lt;file&gt;][&lt;commit&gt;...] git merge(--continue | --abort | --quit)
</code></pre>
<h2>DESCRIPTION</h2>
<p> Incorporates changes from the named commits (since the time their histories diverged from the current branch) into the current branch. This command is used by <i>git pull</i> to incorporate changes from another repository and can be used by hand to merge changes from one branch into another. </p>
<p> Assume the following history exists and the current branch is &quot;<code>master</code>&quot;: </p>
<dl>
<dt>
<dd>
A&#8211; &#8211; B&#8211; &#8211; C topic / D&#8211; &#8211; E&#8211; &#8211; F&#8211; &#8211; G master
</dl>
<p> Then &quot;<code>git merge topic</code>&quot; will replay the changes made on the <code>topic</code> branch since it diverged from <code>master</code> (i.e., <code>E</code>) until its current commit (<code>C</code>) on top of <code>master</code>, and record the result in a new commit along with the names of the two parent commits and a log message from the user describing the changes. </p>
<dl>
<dt>
<dd>
A&#8211; &#8211; B&#8211; &#8211; C topic / D&#8211; &#8211; E&#8211; &#8211; F&#8211; &#8211; G&#8211; &#8211; H master
</dl>
<p> The second syntax (&quot;<code>git merge &#8211;abort</code>&quot;) can only be run after the merge has resulted in conflicts. <i>git merge &#8211;abort</i> will abort the merge process and try to reconstruct the pre-merge state. However, if there were uncommitted changes when the merge started (and especially if those changes were further modified after the merge was started), <i>git merge &#8211;abort</i> will in some cases be unable to reconstruct the original (pre-merge) changes. Therefore: </p>
<p> <code>Warning</code>: Running <i>git merge</i> with non-trivial uncommitted changes is discouraged: while possible, it may leave you in a state that is hard to back out of in the case of a conflict. </p>
<p> The third syntax (&quot;<code>git merge &#8211;continue</code>&quot;) can only be run after the merge has resulted in conflicts.</p>
<h2>OPTIONS</h2>
<p> &#8211;commit, &#8211;no-commit</p>
<dl>
<dt>
<dd> Perform the merge and commit the result. This option can be used to override &#8211;no-commit. </p>
<p> With &#8211;no-commit perform the merge and stop just before creating a merge commit, to give the user a chance to inspect and further tweak the merge result before committing. </p>
<p> Note that fast-forward updates do not create a merge commit and therefore there is no way to stop those merges with &#8211;no-commit. Thus, if you want to ensure your branch is not changed or updated by the merge command, use &#8211;no-ff with &#8211;no-commit.</dl>
<p> &#8211;edit, -e, &#8211;no-edit</p>
<dl>
<dt>
<dd> Invoke an editor before committing successful mechanical merge to further edit the auto-generated merge message, so that the user can explain and justify the merge. The <code>&#8211;no-edit</code> option can be used to accept the auto-generated message (this is generally discouraged). The <code>&#8211;edit</code> (or <code>-e</code>) option is still useful if you are giving a draft message with the <code>-m</code> option from the command line and want to edit it in the editor. </p>
<p> Older scripts may depend on the historical behaviour of not allowing the user to edit the merge log message. They will see an editor opened when they run <code>git merge</code>. To make it easier to adjust such scripts to the updated behaviour, the environment variable <code>GIT_MERGE_AUTOEDIT</code> can be set to <code>no</code> at the beginning of them.</dl>
<p> &#8211;cleanup=&lt;mode&gt;</p>
<dl>
<dt>
<dd> This option determines how the merge message will be cleaned up before committing. See <code><a href="/docs/linux/man/1-git-commit/">git-commit</a></code>(1) for more details. In addition, if the <i>&lt;mode&gt;</i> is given a value of <code>scissors</code>, scissors will be appended to <code>MERGE_MSG</code> before being passed on to the commit machinery in the case of a merge conflict.</dl>
<p> &#8211;ff, &#8211;no-ff, &#8211;ff-only</p>
<dl>
<dt>
<dd> Specifies how a merge is handled when the merged-in history is already a descendant of the current history. <code>&#8211;ff</code> is the default unless merging an annotated (and possibly signed) tag that is not stored in its natural place in the <code>refs/tags/</code> hierarchy, in which case <code>&#8211;no-ff</code> is assumed. </p>
<p> With <code>&#8211;ff</code>, when possible resolve the merge as a fast-forward (only update the branch pointer to match the merged branch; do not create a merge commit). When not possible (when the merged-in history is not a descendant of the current history), create a merge commit. </p>
<p> With <code>&#8211;no-ff</code>, create a merge commit in all cases, even when the merge could instead be resolved as a fast-forward. </p>
<p> With <code>&#8211;ff-only</code>, resolve the merge as a fast-forward when possible. When not possible, refuse to merge and exit with a non-zero status.</dl>
<p> -S[&lt;keyid&gt;], &#8211;gpg-sign[=&lt;keyid&gt;], &#8211;no-gpg-sign</p>
<dl>
<dt>
<dd> GPG-sign the resulting merge commit. The <code>keyid</code> argument is optional and defaults to the committer identity; if specified, it must be stuck to the option without a space. <code>&#8211;no-gpg-sign</code> is useful to countermand both <code>commit.gpgSign</code> configuration variable, and earlier <code>&#8211;gpg-sign</code>.</dl>
<p> &#8211;log[=&lt;n&gt;], &#8211;no-log</p>
<dl>
<dt>
<dd> In addition to branch names, populate the log message with one-line descriptions from at most &lt;n&gt; actual commits that are being merged. See also <code><a href="/docs/linux/man/1-git-fmt-merge-msg/">git-fmt-merge-msg</a></code>(1). </p>
<p> With &#8211;no-log do not list one-line descriptions from the actual commits being merged.</dl>
<p> &#8211;signoff, &#8211;no-signoff</p>
<dl>
<dt>
<dd> Add a <code>Signed-off-by</code> trailer by the committer at the end of the commit log message. The meaning of a signoff depends on the project to which you&#8217;re committing. For example, it may certify that the committer has the rights to submit the work under the project&#8217;s license or agrees to some contributor representation, such as a Developer Certificate of Origin. (See m[blue]<code><a rel="nofollow" href="http://developercertificate.org">http://developercertificate.org</a></code>m[] for the one used by the Linux kernel and Git projects.) Consult the documentation or leadership of the project to which you&#8217;re contributing to understand how the signoffs are used in that project. </p>
<p> The &#8211;no-signoff option can be used to countermand an earlier &#8211;signoff option on the command line.</dl>
<p> &#8211;stat, -n, &#8211;no-stat</p>
<dl>
<dt>
<dd> Show a diffstat at the end of the merge. The diffstat is also controlled by the configuration option merge.stat. </p>
<p> With -n or &#8211;no-stat do not show a diffstat at the end of the merge.</dl>
<p> &#8211;squash, &#8211;no-squash</p>
<dl>
<dt>
<dd> Produce the working tree and index state as if a real merge happened (except for the merge information), but do not actually make a commit, move the <code>HEAD</code>, or record <code>$GIT_DIR/MERGE_HEAD</code> (to cause the next <code>git commit</code> command to create a merge commit). This allows you to create a single commit on top of the current branch whose effect is the same as merging another branch (or more in case of an octopus). </p>
<p> With &#8211;no-squash perform the merge and commit the result. This option can be used to override &#8211;squash. </p>
<p> With &#8211;squash, &#8211;commit is not allowed, and will fail.</dl>
<p> &#8211;[no-]verify</p>
<dl>
<dt>
<dd> By default, the pre-merge and commit-msg hooks are run. When <code>&#8211;no-verify</code> is given, these are bypassed. See also <code><a href="/docs/linux/man/5-githooks/">githooks</a></code>(5).</dl>
<p> -s &lt;strategy&gt;, &#8211;strategy=&lt;strategy&gt;</p>
<dl>
<dt>
<dd> Use the given merge strategy; can be supplied more than once to specify them in the order they should be tried. If there is no <code>-s</code> option, a built-in list of strategies is used instead (<code>ort</code> when merging a single head, <code>octopus</code> otherwise).</dl>
<p> -X &lt;option&gt;, &#8211;strategy-option=&lt;option&gt;</p>
<dl>
<dt>
<dd> Pass merge strategy specific option through to the merge strategy.</dl>
<p> &#8211;verify-signatures, &#8211;no-verify-signatures</p>
<dl>
<dt>
<dd> Verify that the tip commit of the side branch being merged is signed with a valid key, i.e. a key that has a valid uid: in the default trust model, this means the signing key has been signed by a trusted key. If the tip commit of the side branch is not signed with a valid key, the merge is aborted.</dl>
<p> &#8211;summary, &#8211;no-summary</p>
<dl>
<dt>
<dd> Synonyms to &#8211;stat and &#8211;no-stat; these are deprecated and will be removed in the future.</dl>
<p> -q, &#8211;quiet</p>
<dl>
<dt>
<dd> Operate quietly. Implies &#8211;no-progress.</dl>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
<dd> Be verbose.</dl>
<p> &#8211;progress, &#8211;no-progress</p>
<dl>
<dt>
<dd> Turn progress on/off explicitly. If neither is specified, progress is shown if standard error is connected to a terminal. Note that not all merge strategies may support progress reporting.</dl>
<p> &#8211;autostash, &#8211;no-autostash</p>
<dl>
<dt>
<dd> Automatically create a temporary stash entry before the operation begins, record it in the special ref <code>MERGE_AUTOSTASH</code> and apply it after the operation ends. This means that you can run the operation on a dirty worktree. However, use with care: the final stash application after a successful merge might result in non-trivial conflicts.</dl>
<p> &#8211;allow-unrelated-histories</p>
<dl>
<dt>
<dd> By default, <code>git merge</code> command refuses to merge histories that do not share a common ancestor. This option can be used to override this safety when merging histories of two projects that started their lives independently. As that is a very rare occasion, no configuration variable to enable this by default exists and will not be added.</dl>
<p> -m &lt;msg&gt;</p>
<dl>
<dt>
<dd> Set the commit message to be used for the merge commit (in case one is created). </p>
<p> If <code>&#8211;log</code> is specified, a shortlog of the commits being merged will be appended to the specified message. </p>
<p> The <i>git fmt-merge-msg</i> command can be used to give a good default for automated <i>git merge</i> invocations. The automated message can include the branch description.</dl>
<p> -F &lt;file&gt;, &#8211;file=&lt;file&gt;</p>
<dl>
<dt>
<dd> Read the commit message to be used for the merge commit (in case one is created). </p>
<p> If <code>&#8211;log</code> is specified, a shortlog of the commits being merged will be appended to the specified message.</dl>
<p> &#8211;rerere-autoupdate, &#8211;no-rerere-autoupdate</p>
<dl>
<dt>
<dd> Allow the rerere mechanism to update the index with the result of auto-conflict resolution if possible.</dl>
<p> &#8211;overwrite-ignore, &#8211;no-overwrite-ignore</p>
<dl>
<dt>
<dd> Silently overwrite ignored files from the merge result. This is the default behavior. Use <code>&#8211;no-overwrite-ignore</code> to abort.</dl>
<p> &#8211;abort</p>
<dl>
<dt>
<dd> Abort the current conflict resolution process, and try to reconstruct the pre-merge state. If an autostash entry is present, apply it to the worktree. </p>
<p> If there were uncommitted worktree changes present when the merge started, <i>git merge &#8211;abort</i> will in some cases be unable to reconstruct these changes. It is therefore recommended to always commit or stash your changes before running <i>git merge</i>. </p>
<p> <i>git merge &#8211;abort</i> is equivalent to <i>git reset &#8211;merge</i> when <code>MERGE_HEAD</code> is present unless <code>MERGE_AUTOSTASH</code> is also present in which case <i>git merge &#8211;abort</i> applies the stash entry to the worktree whereas <i>git reset &#8211;merge</i> will save the stashed changes in the stash list.</dl>
<p> &#8211;quit</p>
<dl>
<dt>
<dd> Forget about the current merge in progress. Leave the index and the working tree as-is. If <code>MERGE_AUTOSTASH</code> is present, the stash entry will be saved to the stash list.</dl>
<p> &#8211;continue</p>
<dl>
<dt>
<dd> After a <i>git merge</i> stops due to conflicts you can conclude the merge by running <i>git merge &#8211;continue</i> (see &quot;HOW TO RESOLVE CONFLICTS&quot; section below).</dl>
<p> &lt;commit&gt;&#8230;</p>
<dl>
<dt>
<dd> Commits, usually other branch heads, to merge into our branch. Specifying more than one commit will create a merge with more than two parents (affectionately called an Octopus merge). </p>
<p> If no commit is given from the command line, merge the remote-tracking branches that the current branch is configured to use as its upstream. See also the configuration section of this manual page. </p>
<p> When <code>FETCH_HEAD</code> (and no other commit) is specified, the branches recorded in the <code>.git/FETCH_HEAD</code> file by the previous invocation of <code>git fetch</code> for merging are merged to the current branch.</dl>
<h2>PRE-MERGE CHECKS</h2>
<p> Before applying outside changes, you should get your own work in good shape and committed locally, so it will not be clobbered if there are conflicts. See also <code><a href="/docs/linux/man/1-git-stash/">git-stash</a></code>(1). <i>git pull</i> and <i>git merge</i> will stop without doing anything when local uncommitted changes overlap with files that <i>git pull</i>/<i>git merge</i> may need to update. </p>
<p> To avoid recording unrelated changes in the merge commit, <i>git pull</i> and <i>git merge</i> will also abort if there are any changes registered in the index relative to the <code>HEAD</code> commit. (Special narrow exceptions to this rule may exist depending on which merge strategy is in use, but generally, the index must match HEAD.) </p>
<p> If all named commits are already ancestors of <code>HEAD</code>, <i>git merge</i> will exit early with the message &quot;Already up to date.&quot;</p>
<h2>FAST-FORWARD MERGE</h2>
<p> Often the current branch head is an ancestor of the named commit. This is the most common case especially when invoked from <i>git pull</i>: you are tracking an upstream repository, you have committed no local changes, and now you want to update to a newer upstream revision. In this case, a new commit is not needed to store the combined history; instead, the <code>HEAD</code> (along with the index) is updated to point at the named commit, without creating an extra merge commit. </p>
<p> This behavior can be suppressed with the <code>&#8211;no-ff</code> option.</p>
<h2>TRUE MERGE</h2>
<p> Except in a fast-forward merge (see above), the branches to be merged must be tied together by a merge commit that has both of them as its parents. </p>
<p> A merged version reconciling the changes from all branches to be merged is committed, and your <code>HEAD</code>, index, and working tree are updated to it. It is possible to have modifications in the working tree as long as they do not overlap; the update will preserve them. </p>
<p> When it is not obvious how to reconcile the changes, the following happens: </p>
<dl>
<dt>
<dd> 1. The <code>HEAD</code> pointer stays the same.</dl>
<dl>
<dt>
<dd> 2. The <code>MERGE_HEAD</code> ref is set to point to the other branch head.</dl>
<dl>
<dt>
<dd> 3. Paths that merged cleanly are updated both in the index file and in your working tree.</dl>
<dl>
<dt>
<dd> 4. For conflicting paths, the index file records up to three versions: stage 1 stores the version from the common ancestor, stage 2 from <code>HEAD</code>, and stage 3 from <code>MERGE_HEAD</code> (you can inspect the stages with <code>git ls-files -u</code>). The working tree files contain the result of the &quot;merge&quot; program; i.e. 3-way merge results with familiar conflict markers <code>&lt;&lt;&lt;</code> <code>===</code> <code>&gt;&gt;&gt;</code>.</dl>
<dl>
<dt>
<dd> 5. No other changes are made. In particular, the local modifications you had before you started merge will stay the same and the index entries for them stay as they were, i.e. matching <code>HEAD</code>.</dl>
<p> If you tried a merge which resulted in complex conflicts and want to start over, you can recover with <code>git merge &#8211;abort</code>.</p>
<h2>MERGING TAG</h2>
<p> When merging an annotated (and possibly signed) tag, Git always creates a merge commit even if a fast-forward merge is possible, and the commit message template is prepared with the tag message. Additionally, if the tag is signed, the signature check is reported as a comment in the message template. See also <code><a href="/docs/linux/man/1-git-tag/">git-tag</a></code>(1). </p>
<p> When you want to just integrate with the work leading to the commit that happens to be tagged, e.g. synchronizing with an upstream release point, you may not want to make an unnecessary merge commit. </p>
<p> In such a case, you can &quot;unwrap&quot; the tag yourself before feeding it to <code>git merge</code>, or pass <code>&#8211;ff-only</code> when you do not have any work on your own. e.g. </p>
<dl>
<dt>
<dd>
<pre>
git fetch origin
git merge v1.2.3^0
git merge --ff-only v1.2.3
</pre>
</dl>
<h2>HOW CONFLICTS ARE PRESENTED</h2>
<p> During a merge, the working tree files are updated to reflect the result of the merge. Among the changes made to the common ancestor&#8217;s version, non-overlapping ones (that is, you changed an area of the file while the other side left that area intact, or vice versa) are incorporated in the final result verbatim. When both sides made changes to the same area, however, Git cannot randomly pick one side over the other, and asks you to resolve it by leaving what both sides did to that area. </p>
<p> By default, Git uses the same style as the one used by the &quot;merge&quot; program from the RCS suite to present such a conflicted hunk, like this: </p>
<dl>
<dt>
<dd>
<pre>
Here are lines that are either unchanged from the common
ancestor, or cleanly resolved because only one side changed.
&lt;&lt;&lt;&lt;&lt;&lt;&lt; yours:sample.txt
Conflict resolution is hard;
let's go shopping.
=======
Git makes conflict resolution easy.
&gt;&gt;&gt;&gt;&gt;&gt;&gt; theirs:sample.txt
And here is another line that is cleanly resolved or unmodified.
</pre>
</dl>
<p> The area where a pair of conflicting changes happened is marked with markers <code>&lt;&lt;&lt;&lt;&lt;&lt;&lt;</code>, <code>=======</code>, and <code>&gt;&gt;&gt;&gt;&gt;&gt;&gt;</code>. The part before the <code>=======</code> is typically your side, and the part afterwards is typically their side. </p>
<p> The default format does not show what the original said in the conflicting area. You cannot tell how many lines are deleted and replaced with Barbie&#8217;s remark on your side. The only thing you can tell is that your side wants to say it is hard and you&#8217;d prefer to go shopping, while the other side wants to claim it is easy. </p>
<p> An alternative style can be used by setting the &quot;merge.conflictStyle&quot; configuration variable to &quot;diff3&quot;. In &quot;diff3&quot; style, the above conflict may look like this: </p>
<dl>
<dt>
<dd>
<pre><code>
Here are lines that are either unchanged from the common
    ancestor,
    or cleanly resolved because only one side changed.
&lt;&lt;&lt;&lt;&lt;&lt;&lt; yours:sample.txt
        Conflict resolution is hard;
let's go shopping.
|||||||
        Conflict resolution is hard.
=======
        Git makes conflict resolution easy.
&gt;&gt;&gt;&gt;&gt;&gt;&gt; theirs:sample.txt
    And here is another line that is cleanly resolved or
    unmodified.
</code></pre>
</dl>
<p> In addition to the <code>&lt;&lt;&lt;&lt;&lt;&lt;&lt;</code>, <code>=======</code>, and <code>&gt;&gt;&gt;&gt;&gt;&gt;&gt;</code> markers, it uses another <code>|||||||</code> marker that is followed by the original text. You can tell that the original just stated a fact, and your side simply gave in to that statement and gave up, while the other side tried to have a more positive attitude. You can sometimes come up with a better resolution by viewing the original.</p>
<h2>HOW TO RESOLVE CONFLICTS</h2>
<p> After seeing a conflict, you can do two things: </p>
<dl>
<dt>
<dd> &bull; Decide not to merge. The only clean-ups you need are to reset the index file to the <code>HEAD</code> commit to reverse 2. and to clean up working tree changes made by 2. and 3.; <code>git merge &#8211;abort</code> can be used for this.</dl>
<dl>
<dt>
<dd> &bull; Resolve the conflicts. Git will mark the conflicts in the working tree. Edit the files into shape and <i>git add</i> them to the index. Use <i>git commit</i> or <i>git merge &#8211;continue</i> to seal the deal. The latter command checks whether there is a (interrupted) merge in progress before calling <i>git commit</i>.</dl>
<p> You can work through the conflict with a number of tools: </p>
<dl>
<dt>
<dd> &bull; Use a mergetool. <code>git mergetool</code> to launch a graphical mergetool which will work you through the merge.</dl>
<dl>
<dt>
<dd> &bull; Look at the diffs. <code>git diff</code> will show a three-way diff, highlighting changes from both the <code>HEAD</code> and <code>MERGE_HEAD</code> versions.</dl>
<dl>
<dt>
<dd> &bull; Look at the diffs from each branch. <code>git log &#8211;merge -p &lt;path&gt;</code> will show diffs first for the <code>HEAD</code> version and then the <code>MERGE_HEAD</code> version.</dl>
<dl>
<dt>
<dd> &bull; Look at the originals. <code>git show :1:filename</code> shows the common ancestor, <code>git show :2:filename</code> shows the <code>HEAD</code> version, and <code>git show :3:filename</code> shows the <code>MERGE_HEAD</code> version.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd> &bull; Merge branches <code>fixes</code> and <code>enhancements</code> on top of the current branch, making an octopus merge: </p>
<dl>
<dt>
<dd>
<pre>
$ git merge fixes enhancements
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Merge branch <code>obsolete</code> into the current branch, using <code>ours</code> merge strategy: </p>
<dl>
<dt>
<dd>
<pre>
$ git merge -s ours obsolete
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Merge branch <code>maint</code> into the current branch, but do not make a new commit automatically: </p>
<dl>
<dt>
<dd>
<pre>
$ git merge --no-commit maint
</pre>
</dl>
<p> This can be used when you want to include further changes to the merge, or want to write your own merge commit message. </p>
<p> You should refrain from abusing this option to sneak substantial changes into a merge commit. Small fixups like bumping release/version name would be acceptable.</dl>
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
<h2>CONFIGURATION</h2>
<p> merge.conflictStyle</p>
<dl>
<dt>
<dd> Specify the style in which conflicted hunks are written out to working tree files upon merge. The default is &quot;merge&quot;, which shows a <code>&lt;&lt;&lt;&lt;&lt;&lt;&lt;</code> conflict marker, changes made by one side, a <code>=======</code> marker, changes made by the other side, and then a <code>&gt;&gt;&gt;&gt;&gt;&gt;&gt;</code> marker. An alternate style, &quot;diff3&quot;, adds a <code>|||||||</code> marker and the original text before the <code>=======</code> marker.</dl>
<p> merge.defaultToUpstream</p>
<dl>
<dt>
<dd> If merge is called without any commit argument, merge the upstream branches configured for the current branch by using their last observed values stored in their remote-tracking branches. The values of the <code>branch.&lt;current branch&gt;.merge</code> that name the branches at the remote named by <code>branch.&lt;current branch&gt;.remote</code> are consulted, and then they are mapped via <code>remote.&lt;remote&gt;.fetch</code> to their corresponding remote-tracking branches, and the tips of these tracking branches are merged. Defaults to true.</dl>
<p> merge.ff</p>
<dl>
<dt>
<dd> By default, Git does not create an extra merge commit when merging a commit that is a descendant of the current commit. Instead, the tip of the current branch is fast-forwarded. When set to <code>false</code>, this variable tells Git to create an extra merge commit in such a case (equivalent to giving the <code>&#8211;no-ff</code> option from the command line). When set to <code>only</code>, only such fast-forward merges are allowed (equivalent to giving the <code>&#8211;ff-only</code> option from the command line).</dl>
<p> merge.verifySignatures</p>
<dl>
<dt>
<dd> If true, this is equivalent to the &#8211;verify-signatures command line option. See <code><a href="/docs/linux/man/1-git-merge/">git-merge</a></code>(1) for details.</dl>
<p> merge.branchdesc</p>
<dl>
<dt>
<dd> In addition to branch names, populate the log message with the branch description text associated with them. Defaults to false.</dl>
<p> merge.log</p>
<dl>
<dt>
<dd> In addition to branch names, populate the log message with at most the specified number of one-line descriptions from the actual commits that are being merged. Defaults to false, and true is a synonym for 20.</dl>
<p> merge.suppressDest</p>
<dl>
<dt>
<dd> By adding a glob that matches the names of integration branches to this multi-valued configuration variable, the default merge message computed for merges into these integration branches will omit &quot;into &lt;branch name&gt;&quot; from its title. </p>
<p> An element with an empty value can be used to clear the list of globs accumulated from previous configuration entries. When there is no <code>merge.suppressDest</code> variable defined, the default value of <code>master</code> is used for backward compatibility.</dl>
<p> merge.renameLimit</p>
<dl>
<dt>
<dd> The number of files to consider in the exhaustive portion of rename detection during a merge. If not specified, defaults to the value of diff.renameLimit. If neither merge.renameLimit nor diff.renameLimit are specified, currently defaults to 7000. This setting has no effect if rename detection is turned off.</dl>
<p> merge.renames</p>
<dl>
<dt>
<dd> Whether Git detects renames. If set to &quot;false&quot;, rename detection is disabled. If set to &quot;true&quot;, basic rename detection is enabled. Defaults to the value of diff.renames.</dl>
<p> merge.directoryRenames</p>
<dl>
<dt>
<dd> Whether Git detects directory renames, affecting what happens at merge time to new files added to a directory on one side of history when that directory was renamed on the other side of history. If merge.directoryRenames is set to &quot;false&quot;, directory rename detection is disabled, meaning that such new files will be left behind in the old directory. If set to &quot;true&quot;, directory rename detection is enabled, meaning that such new files will be moved into the new directory. If set to &quot;conflict&quot;, a conflict will be reported for such paths. If merge.renames is false, merge.directoryRenames is ignored and treated as false. Defaults to &quot;conflict&quot;.</dl>
<p> merge.renormalize</p>
<dl>
<dt>
<dd> Tell Git that canonical representation of files in the repository has changed over time (e.g. earlier commits record text files with CRLF line endings, but recent ones use LF line endings). In such a repository, Git can convert the data recorded in commits to a canonical form before performing a merge to reduce unnecessary conflicts. For more information, see section &quot;Merging branches with differing checkin/checkout attributes&quot; in <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5).</dl>
<p> merge.stat</p>
<dl>
<dt>
<dd> Whether to print the diffstat between ORIG_HEAD and the merge result at the end of the merge. True by default.</dl>
<p> merge.autoStash</p>
<dl>
<dt>
<dd> When set to true, automatically create a temporary stash entry before the operation begins, and apply it after the operation ends. This means that you can run merge on a dirty worktree. However, use with care: the final stash application after a successful merge might result in non-trivial conflicts. This option can be overridden by the <code>&#8211;no-autostash</code> and <code>&#8211;autostash</code> options of <code><a href="/docs/linux/man/1-git-merge/">git-merge</a></code>(1). Defaults to false.</dl>
<p> merge.tool</p>
<dl>
<dt>
<dd> Controls which merge tool is used by <code><a href="/docs/linux/man/1-git-mergetool/">git-mergetool</a></code>(1). The list below shows the valid built-in values. Any other value is treated as a custom merge tool and requires that a corresponding mergetool.&lt;tool&gt;.cmd variable is defined.</dl>
<p> merge.guitool</p>
<dl>
<dt>
<dd> Controls which merge tool is used by <code><a href="/docs/linux/man/1-git-mergetool/">git-mergetool</a></code>(1) when the -g/&#8211;gui flag is specified. The list below shows the valid built-in values. Any other value is treated as a custom merge tool and requires that a corresponding mergetool.&lt;guitool&gt;.cmd variable is defined. </p>
<dl>
<dt>
<dd> &bull; araxis</dl>
<dl>
<dt>
<dd> &bull; bc</dl>
<dl>
<dt>
<dd> &bull; bc3</dl>
<dl>
<dt>
<dd> &bull; bc4</dl>
<dl>
<dt>
<dd> &bull; codecompare</dl>
<dl>
<dt>
<dd> &bull; deltawalker</dl>
<dl>
<dt>
<dd> &bull; diffmerge</dl>
<dl>
<dt>
<dd> &bull; diffuse</dl>
<dl>
<dt>
<dd> &bull; ecmerge</dl>
<dl>
<dt>
<dd> &bull; emerge</dl>
<dl>
<dt>
<dd> &bull; examdiff</dl>
<dl>
<dt>
<dd> &bull; guiffy</dl>
<dl>
<dt>
<dd> &bull; gvimdiff</dl>
<dl>
<dt>
<dd> &bull; gvimdiff1</dl>
<dl>
<dt>
<dd> &bull; gvimdiff2</dl>
<dl>
<dt>
<dd> &bull; gvimdiff3</dl>
<dl>
<dt>
<dd> &bull; kdiff3</dl>
<dl>
<dt>
<dd> &bull; meld</dl>
<dl>
<dt>
<dd> &bull; nvimdiff</dl>
<dl>
<dt>
<dd> &bull; nvimdiff1</dl>
<dl>
<dt>
<dd> &bull; nvimdiff2</dl>
<dl>
<dt>
<dd> &bull; nvimdiff3</dl>
<dl>
<dt>
<dd> &bull; opendiff</dl>
<dl>
<dt>
<dd> &bull; p4merge</dl>
<dl>
<dt>
<dd> &bull; smerge</dl>
<dl>
<dt>
<dd> &bull; tkdiff</dl>
<dl>
<dt>
<dd> &bull; tortoisemerge</dl>
<dl>
<dt>
<dd> &bull; vimdiff</dl>
<dl>
<dt>
<dd> &bull; vimdiff1</dl>
<dl>
<dt>
<dd> &bull; vimdiff2</dl>
<dl>
<dt>
<dd> &bull; vimdiff3</dl>
<dl>
<dt>
<dd> &bull; winmerge</dl>
<dl>
<dt>
<dd> &bull; xxdiff</dl>
</dl>
<p> merge.verbosity</p>
<dl>
<dt>
<dd> Controls the amount of output shown by the recursive merge strategy. Level 0 outputs nothing except a final error message if conflicts were detected. Level 1 outputs only conflicts, 2 outputs conflicts and file changes. Level 5 and above outputs debugging information. The default is level 2. Can be overridden by the <code>GIT_MERGE_VERBOSITY</code> environment variable.</dl>
<p> merge.&lt;driver&gt;.name</p>
<dl>
<dt>
<dd> Defines a human-readable name for a custom low-level merge driver. See <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5) for details.</dl>
<p> merge.&lt;driver&gt;.driver</p>
<dl>
<dt>
<dd> Defines the command that implements a custom low-level merge driver. See <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5) for details.</dl>
<p> merge.&lt;driver&gt;.recursive</p>
<dl>
<dt>
<dd> Names a low-level merge driver to be used when performing an internal merge between common ancestors. See <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5) for details.</dl>
<p> branch.&lt;name&gt;.mergeOptions</p>
<dl>
<dt>
<dd> Sets default options for merging into branch &lt;name&gt;. The syntax and supported options are the same as those of <i>git merge</i>, but option values containing whitespace characters are currently not supported.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-fmt-merge-msg/">git-fmt-merge-msg</a></code>(1), <code><a href="/docs/linux/man/1-git-pull/">git-pull</a></code>(1), <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5), <code><a href="/docs/linux/man/1-git-reset/">git-reset</a></code>(1), <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1), <code><a href="/docs/linux/man/1-git-ls-files/">git-ls-files</a></code>(1), <code><a href="/docs/linux/man/1-git-add/">git-add</a></code>(1), <code><a href="/docs/linux/man/1-git-rm/">git-rm</a></code>(1), <code><a href="/docs/linux/man/1-git-mergetool/">git-mergetool</a></code>(1)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>

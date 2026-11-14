---
title: "git-revert(1)"
name: "git-revert"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-revert/"
description: "git-revert – Revert some existing commits"
---

<h2 class="name">NAME</h2>
<p> git-revert &#8211; Revert some existing commits </p>
<h2>SYNOPSIS</h2>
<pre><code>
git revert[--[no - ] edit][-n][-m parent - number][-s][-S[&lt;keyid&gt;]]&lt;commit&gt;... git revert(--continue | --skip | --abort | --quit)
</code></pre>
<h2>DESCRIPTION</h2>
<p> Given one or more existing commits, revert the changes that the related patches introduce, and record some new commits that record them. This requires your working tree to be clean (no modifications from the HEAD commit). </p>
<p> Note: <i>git revert</i> is used to record some new commits to reverse the effect of some earlier commits (often only a faulty one). If you want to throw away all uncommitted changes in your working directory, you should see <code><a href="/docs/linux/man/1-git-reset/">git-reset</a></code>(1), particularly the <code>&#8211;hard</code> option. If you want to extract specific files as they were in another commit, you should see <code><a href="/docs/linux/man/1-git-restore/">git-restore</a></code>(1), specifically the <code>&#8211;source</code> option. Take care with these alternatives as both will discard uncommitted changes in your working directory. </p>
<p> See &quot;Reset, restore and revert&quot; in <code><a href="/docs/linux/man/1-git/">git</a></code>(1) for the differences between the three commands.</p>
<h2>OPTIONS</h2>
<p> &lt;commit&gt;&#8230;</p>
<dl>
<dt>
<dd> Commits to revert. For a more complete list of ways to spell commit names, see <code><a href="/docs/linux/man/7-gitrevisions/">gitrevisions</a></code>(7). Sets of commits can also be given but no traversal is done by default, see <code><a href="/docs/linux/man/1-git-rev-list/">git-rev-list</a></code>(1) and its <code>&#8211;no-walk</code> option.</dl>
<p> -e, &#8211;edit</p>
<dl>
<dt>
<dd> With this option, <i>git revert</i> will let you edit the commit message prior to committing the revert. This is the default if you run the command from a terminal.</dl>
<p> -m parent-number, &#8211;mainline parent-number</p>
<dl>
<dt>
<dd> Usually you cannot revert a merge because you do not know which side of the merge should be considered the mainline. This option specifies the parent number (starting from 1) of the mainline and allows revert to reverse the change relative to the specified parent. </p>
<p> Reverting a merge commit declares that you will never want the tree changes brought in by the merge. As a result, later merges will only bring in tree changes introduced by commits that are not ancestors of the previously reverted merge. This may or may not be what you want. </p>
<p> See the m[blue]<code>revert-a-faulty-merge How-To</code>m[]<font SIZE="-2">[1]</font> for more details.</dl>
<p> &#8211;no-edit</p>
<dl>
<dt>
<dd> With this option, <i>git revert</i> will not start the commit message editor.</dl>
<p> &#8211;cleanup=&lt;mode&gt;</p>
<dl>
<dt>
<dd> This option determines how the commit message will be cleaned up before being passed on to the commit machinery. See <code><a href="/docs/linux/man/1-git-commit/">git-commit</a></code>(1) for more details. In particular, if the <i>&lt;mode&gt;</i> is given a value of <code>scissors</code>, scissors will be appended to <code>MERGE_MSG</code> before being passed on in the case of a conflict.</dl>
<p> -n, &#8211;no-commit</p>
<dl>
<dt>
<dd> Usually the command automatically creates some commits with commit log messages stating which commits were reverted. This flag applies the changes necessary to revert the named commits to your working tree and the index, but does not make the commits. In addition, when this option is used, your index does not have to match the HEAD commit. The revert is done against the beginning state of your index. </p>
<p> This is useful when reverting more than one commits&#8217; effect to your index in a row.</dl>
<p> -S[&lt;keyid&gt;], &#8211;gpg-sign[=&lt;keyid&gt;], &#8211;no-gpg-sign</p>
<dl>
<dt>
<dd> GPG-sign commits. The <code>keyid</code> argument is optional and defaults to the committer identity; if specified, it must be stuck to the option without a space. <code>&#8211;no-gpg-sign</code> is useful to countermand both <code>commit.gpgSign</code> configuration variable, and earlier <code>&#8211;gpg-sign</code>.</dl>
<p> -s, &#8211;signoff</p>
<dl>
<dt>
<dd> Add a <code>Signed-off-by</code> trailer at the end of the commit message. See the signoff option in <code><a href="/docs/linux/man/1-git-commit/">git-commit</a></code>(1) for more information.</dl>
<p> &#8211;strategy=&lt;strategy&gt;</p>
<dl>
<dt>
<dd> Use the given merge strategy. Should only be used once. See the MERGE STRATEGIES section in <code><a href="/docs/linux/man/1-git-merge/">git-merge</a></code>(1) for details.</dl>
<p> -X&lt;option&gt;, &#8211;strategy-option=&lt;option&gt;</p>
<dl>
<dt>
<dd> Pass the merge strategy-specific option through to the merge strategy. See <code><a href="/docs/linux/man/1-git-merge/">git-merge</a></code>(1) for details.</dl>
<p> &#8211;rerere-autoupdate, &#8211;no-rerere-autoupdate</p>
<dl>
<dt>
<dd> Allow the rerere mechanism to update the index with the result of auto-conflict resolution if possible.</dl>
<h2>SEQUENCER SUBCOMMANDS</h2>
<p> &#8211;continue</p>
<dl>
<dt>
<dd> Continue the operation in progress using the information in <code>.git/sequencer</code>. Can be used to continue after resolving conflicts in a failed cherry-pick or revert.</dl>
<p> &#8211;skip</p>
<dl>
<dt>
<dd> Skip the current commit and continue with the rest of the sequence.</dl>
<p> &#8211;quit</p>
<dl>
<dt>
<dd> Forget about the current operation in progress. Can be used to clear the sequencer state after a failed cherry-pick or revert.</dl>
<p> &#8211;abort</p>
<dl>
<dt>
<dd> Cancel the operation and return to the pre-sequence state.</dl>
<h2>EXAMPLES</h2>
<p> <code>git revert HEAD~3</code></p>
<dl>
<dt>
<dd> Revert the changes specified by the fourth last commit in HEAD and create a new commit with the reverted changes.</dl>
<p> <code>git revert -n master~5..master~2</code></p>
<dl>
<dt>
<dd> Revert the changes done by commits from the fifth last commit in master (included) to the third last commit in master (included), but do not create any commit with the reverted changes. The revert only modifies the working tree and the index.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-cherry-pick/">git-cherry-pick</a></code>(1)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> revert-a-faulty-merge How-To</p>
<dl>
<dt>
<dd> file:///usr/share/doc/git/html/howto/revert-a-faulty-merge.html</dl>
</dl>
<h2>Index</h2>

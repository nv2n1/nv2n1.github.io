---
title: "git-read-tree(1)"
name: "git-read-tree"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-read-tree/"
description: "git-read-tree – Reads tree information into the index"
---

<h2 class="name">NAME</h2>
<p> git-read-tree &#8211; Reads tree information into the index </p>
<h2>SYNOPSIS</h2>
<pre><code>
git read - tree[[-m[--trivial][--aggressive] | --reset | --prefix = &lt;prefix&gt;]
                    [-u | -i]][--index - output = &lt;file&gt;][--no - sparse - checkout](--empty | &lt;tree - ish1&gt;[&lt;tree - ish2&gt;[&lt;tree - ish3&gt;]])
</code></pre>
<h2>DESCRIPTION</h2>
<p> Reads the tree information given by &lt;tree-ish&gt; into the index, but does not actually <code>update</code> any of the files it &quot;caches&quot;. (see: <code><a href="/docs/linux/man/1-git-checkout-index/">git-checkout-index</a></code>(1)) </p>
<p> Optionally, it can merge a tree into the index, perform a fast-forward (i.e. 2-way) merge, or a 3-way merge, with the <code>-m</code> flag. When used with <code>-m</code>, the <code>-u</code> flag causes it to also update the files in the work tree with the result of the merge. </p>
<p> Trivial merges are done by <i>git read-tree</i> itself. Only conflicting paths will be in unmerged state when <i>git read-tree</i> returns.</p>
<h2>OPTIONS</h2>
<p> -m</p>
<dl>
<dt>
<dd> Perform a merge, not just a read. The command will refuse to run if your index file has unmerged entries, indicating that you have not finished previous merge you started.</dl>
<p> &#8211;reset</p>
<dl>
<dt>
<dd> Same as -m, except that unmerged entries are discarded instead of failing. When used with <code>-u</code>, updates leading to loss of working tree changes or untracked files or directories will not abort the operation.</dl>
<p> -u</p>
<dl>
<dt>
<dd> After a successful merge, update the files in the work tree with the result of the merge.</dl>
<p> -i</p>
<dl>
<dt>
<dd> Usually a merge requires the index file as well as the files in the working tree to be up to date with the current head commit, in order not to lose local changes. This flag disables the check with the working tree and is meant to be used when creating a merge of trees that are not directly related to the current working tree status into a temporary index file.</dl>
<p> -n, &#8211;dry-run</p>
<dl>
<dt>
<dd> Check if the command would error out, without updating the index or the files in the working tree for real.</dl>
<p> -v</p>
<dl>
<dt>
<dd> Show the progress of checking files out.</dl>
<p> &#8211;trivial</p>
<dl>
<dt>
<dd> Restrict three-way merge by <i>git read-tree</i> to happen only if there is no file-level merging required, instead of resolving merge for trivial cases and leaving conflicting files unresolved in the index.</dl>
<p> &#8211;aggressive</p>
<dl>
<dt>
<dd> Usually a three-way merge by <i>git read-tree</i> resolves the merge for really trivial cases and leaves other cases unresolved in the index, so that porcelains can implement different merge policies. This flag makes the command resolve a few more cases internally: </p>
<dl>
<dt>
<dd> &bull; when one side removes a path and the other side leaves the path unmodified. The resolution is to remove that path.</dl>
<dl>
<dt>
<dd> &bull; when both sides remove a path. The resolution is to remove that path.</dl>
<dl>
<dt>
<dd> &bull; when both sides add a path identically. The resolution is to add that path.</dl>
</dl>
<p> &#8211;prefix=&lt;prefix&gt;</p>
<dl>
<dt>
<dd> Keep the current index contents, and read the contents of the named tree-ish under the directory at <code>&lt;prefix&gt;</code>. The command will refuse to overwrite entries that already existed in the original index file.</dl>
<p> &#8211;index-output=&lt;file&gt;</p>
<dl>
<dt>
<dd> Instead of writing the results out to <code>$GIT_INDEX_FILE</code>, write the resulting index in the named file. While the command is operating, the original index file is locked with the same mechanism as usual. The file must allow to be <a href="/docs/linux/man/2-rename/">rename</a>(2)ed into from a temporary file that is created next to the usual index file; typically this means it needs to be on the same filesystem as the index file itself, and you need write permission to the directories the index file and index output file are located in.</dl>
<p> &#8211;[no-]recurse-submodules</p>
<dl>
<dt>
<dd> Using &#8211;recurse-submodules will update the content of all active submodules according to the commit recorded in the superproject by calling read-tree recursively, also setting the submodules&#8217; HEAD to be detached at that commit.</dl>
<p> &#8211;no-sparse-checkout</p>
<dl>
<dt>
<dd> Disable sparse checkout support even if <code>core.sparseCheckout</code> is true.</dl>
<p> &#8211;empty</p>
<dl>
<dt>
<dd> Instead of reading tree object(s) into the index, just empty it.</dl>
<p> -q, &#8211;quiet</p>
<dl>
<dt>
<dd> Quiet, suppress feedback messages.</dl>
<p> &lt;tree-ish#&gt;</p>
<dl>
<dt>
<dd> The id of the tree object(s) to be read/merged.</dl>
<h2>MERGING</h2>
<p> If <code>-m</code> is specified, <i>git read-tree</i> can perform 3 kinds of merge, a single tree merge if only 1 tree is given, a fast-forward merge with 2 trees, or a 3-way merge if 3 or more trees are provided.</p>
<h3>Single Tree Merge</h3>
<p> If only 1 tree is specified, <i>git read-tree</i> operates as if the user did not specify <code>-m</code>, except that if the original index has an entry for a given pathname, and the contents of the path match with the tree being read, the stat info from the index is used. (In other words, the index&#8217;s stat()s take precedence over the merged tree&#8217;s). </p>
<p> That means that if you do a <code>git read-tree -m &lt;newtree&gt;</code> followed by a <code>git checkout-index -f -u -a</code>, the <i>git checkout-index</i> only checks out the stuff that really changed. </p>
<p> This is used to avoid unnecessary false hits when <i>git diff-files</i> is run after <i>git read-tree</i>.</p>
<h3>Two Tree Merge</h3>
<p> Typically, this is invoked as <code>git read-tree -m $H $M</code>, where $H is the head commit of the current repository, and $M is the head of a foreign tree, which is simply ahead of $H (i.e. we are in a fast-forward situation). </p>
<p> When two trees are specified, the user is telling <i>git read-tree</i> the following: </p>
<dl>
<dt>
<dd> 1. The current index and work tree is derived from $H, but the user may have local changes in them since $H.</dl>
<dl>
<dt>
<dd> 2. The user wants to fast-forward to $M.</dl>
<p> In this case, the <code>git read-tree -m $H $M</code> command makes sure that no local change is lost as the result of this &quot;merge&quot;. Here are the &quot;carry forward&quot; rules, where &quot;I&quot; denotes the index, &quot;clean&quot; means that index and work tree coincide, and &quot;exists&quot;/&quot;nothing&quot; refer to the presence of a path in the specified commit: </p>
<dl>
<dt>
<dd>
<pre><code>
I H M Result-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -0 nothing nothing nothing(does not happen) 1 nothing nothing exists use M
    2 nothing exists nothing remove path from index
    3 nothing exists exists,
    use M if "initial checkout",
    H == M keep index otherwise
        exists,
    fail
        H
        != M clean I == H I == M-- -- -- -- -- -- -- -- --4 yes N / A N / A nothing nothing keep index 5 no N / A N / A nothing nothing keep index 6 yes N / A yes nothing exists keep index 7 no N / A yes nothing exists keep index 8 yes N / A no nothing exists fail 9 no N / A no nothing exists fail 10 yes yes N / A exists nothing remove path from index 11 no yes N / A exists nothing fail 12 yes no N / A exists nothing fail 13 no no N / A exists nothing fail clean(H == M)-- -- --14 yes exists exists keep index 15 no exists exists keep index clean I == H I == M(H != M)-- -- -- -- -- -- -- -- --16 yes no no exists exists fail 17 no no no exists exists fail 18 yes no yes exists exists keep index 19 no no yes exists exists keep index 20 yes yes no exists exists use M 21 no yes no exists exists fail
</code></pre>
</dl>
<p> In all &quot;keep index&quot; cases, the index entry stays as in the original index file. If the entry is not up to date, <i>git read-tree</i> keeps the copy in the work tree intact when operating under the -u flag. </p>
<p> When this form of <i>git read-tree</i> returns successfully, you can see which of the &quot;local changes&quot; that you made were carried forward by running <code>git diff-index &#8211;cached $M</code>. Note that this does not necessarily match what <code>git diff-index &#8211;cached $H</code> would have produced before such a two tree merge. This is because of cases 18 and 19 &#8212; if you already had the changes in $M (e.g. maybe you picked it up via e-mail in a patch form), <code>git diff-index &#8211;cached $H</code> would have told you about the change before this merge, but it would not show in <code>git diff-index &#8211;cached $M</code> output after the two-tree merge. </p>
<p> Case 3 is slightly tricky and needs explanation. The result from this rule logically should be to remove the path if the user staged the removal of the path and then switching to a new branch. That however will prevent the initial checkout from happening, so the rule is modified to use M (new tree) only when the content of the index is empty. Otherwise the removal of the path is kept as long as $H and $M are the same.</p>
<h3>3-Way Merge</h3>
<p> Each &quot;index&quot; entry has two bits worth of &quot;stage&quot; state. stage 0 is the normal one, and is the only one you&#8217;d see in any kind of normal use. </p>
<p> However, when you do <i>git read-tree</i> with three trees, the &quot;stage&quot; starts out at 1. </p>
<p> This means that you can do </p>
<dl>
<dt>
<dd>
<pre>
$ git read-tree -m &lt;tree1&gt; &lt;tree2&gt; &lt;tree3&gt;
</pre>
</dl>
<p> and you will end up with an index with all of the &lt;tree1&gt; entries in &quot;stage1&quot;, all of the &lt;tree2&gt; entries in &quot;stage2&quot; and all of the &lt;tree3&gt; entries in &quot;stage3&quot;. When performing a merge of another branch into the current branch, we use the common ancestor tree as &lt;tree1&gt;, the current branch head as &lt;tree2&gt;, and the other branch head as &lt;tree3&gt;. </p>
<p> Furthermore, <i>git read-tree</i> has special-case logic that says: if you see a file that matches in all respects in the following states, it &quot;collapses&quot; back to &quot;stage0&quot;: </p>
<dl>
<dt>
<dd> &bull; stage 2 and 3 are the same; take one or the other (it makes no difference &#8211; the same work has been done on our branch in stage 2 and their branch in stage 3)</dl>
<dl>
<dt>
<dd> &bull; stage 1 and stage 2 are the same and stage 3 is different; take stage 3 (our branch in stage 2 did not do anything since the ancestor in stage 1 while their branch in stage 3 worked on it)</dl>
<dl>
<dt>
<dd> &bull; stage 1 and stage 3 are the same and stage 2 is different take stage 2 (we did something while they did nothing)</dl>
<p> The <i>git write-tree</i> command refuses to write a nonsensical tree, and it will complain about unmerged entries if it sees a single entry that is not stage 0. </p>
<p> OK, this all sounds like a collection of totally nonsensical rules, but it&#8217;s actually exactly what you want in order to do a fast merge. The different stages represent the &quot;result tree&quot; (stage 0, aka &quot;merged&quot;), the original tree (stage 1, aka &quot;orig&quot;), and the two trees you are trying to merge (stage 2 and 3 respectively). </p>
<p> The order of stages 1, 2 and 3 (hence the order of three &lt;tree-ish&gt; command-line arguments) are significant when you start a 3-way merge with an index file that is already populated. Here is an outline of how the algorithm works: </p>
<dl>
<dt>
<dd> &bull; if a file exists in identical format in all three trees, it will automatically collapse to &quot;merged&quot; state by <i>git read-tree</i>.</dl>
<dl>
<dt>
<dd> &bull; a file that has <i>any</i> difference what-so-ever in the three trees will stay as separate entries in the index. It&#8217;s up to &quot;porcelain policy&quot; to determine how to remove the non-0 stages, and insert a merged version.</dl>
<dl>
<dt>
<dd> &bull; the index file saves and restores with all this information, so you can merge things incrementally, but as long as it has entries in stages 1/2/3 (i.e., &quot;unmerged entries&quot;) you can&#8217;t write the result. So now the merge algorithm ends up being really simple: </p>
<dl>
<dt>
<dd> &bull; you walk the index in order, and ignore all entries of stage 0, since they&#8217;ve already been done.</dl>
<dl>
<dt>
<dd> &bull; if you find a &quot;stage1&quot;, but no matching &quot;stage2&quot; or &quot;stage3&quot;, you know it&#8217;s been removed from both trees (it only existed in the original tree), and you remove that entry.</dl>
<dl>
<dt>
<dd> &bull; if you find a matching &quot;stage2&quot; and &quot;stage3&quot; tree, you remove one of them, and turn the other into a &quot;stage0&quot; entry. Remove any matching &quot;stage1&quot; entry if it exists too. .. all the normal trivial rules ..</dl>
</dl>
<p> You would normally use <i>git merge-index</i> with supplied <i>git merge-one-file</i> to do this last step. The script updates the files in the working tree as it merges each path and at the end of a successful merge. </p>
<p> When you start a 3-way merge with an index file that is already populated, it is assumed that it represents the state of the files in your work tree, and you can even have files with changes unrecorded in the index file. It is further assumed that this state is &quot;derived&quot; from the stage 2 tree. The 3-way merge refuses to run if it finds an entry in the original index file that does not match stage 2. </p>
<p> This is done to prevent you from losing your work-in-progress changes, and mixing your random changes in an unrelated merge commit. To illustrate, suppose you start from what has been committed last to your repository: </p>
<dl>
<dt>
<dd>
<pre>
$ JC=`git rev-parse --verify &quot;HEAD^0&quot;`
$ git checkout-index -f -u -a $JC
</pre>
</dl>
<p> You do random edits, without running <i>git update-index</i>. And then you notice that the tip of your &quot;upstream&quot; tree has advanced since you pulled from him: </p>
<dl>
<dt>
<dd>
<pre>
$ git fetch <a href="git://....">git://....</a> linus
$ LT=`git rev-parse FETCH_HEAD`
</pre>
</dl>
<p> Your work tree is still based on your HEAD ($JC), but you have some edits since. Three-way merge makes sure that you have not added or modified index entries since $JC, and if you haven&#8217;t, then does the right thing. So with the following sequence: </p>
<dl>
<dt>
<dd>
<pre>
$ git read-tree -m -u `git merge-base $JC $LT` $JC $LT
$ git merge-index git-merge-one-file -a
$ echo &quot;Merge with Linus&quot; | \
  git commit-tree `git write-tree` -p $JC -p $LT
</pre>
</dl>
<p> what you would commit is a pure merge between $JC and $LT without your work-in-progress changes, and your work tree would be updated to the result of the merge. </p>
<p> However, if you have local changes in the working tree that would be overwritten by this merge, <i>git read-tree</i> will refuse to run to prevent your changes from being lost. </p>
<p> In other words, there is no need to worry about what exists only in the working tree. When you have local changes in a part of the project that is not involved in the merge, your changes do not interfere with the merge, and are kept intact. When they <code>do</code> interfere, the merge does not even start (<i>git read-tree</i> complains loudly and fails without modifying anything). In such a case, you can simply continue doing what you were in the middle of doing, and when your working tree is ready (i.e. you have finished your work-in-progress), attempt the merge again.</p>
<h2>SPARSE CHECKOUT</h2>
<p> &quot;Sparse checkout&quot; allows populating the working directory sparsely. It uses the skip-worktree bit (see <code><a href="/docs/linux/man/1-git-update-index/">git-update-index</a></code>(1)) to tell Git whether a file in the working directory is worth looking at. </p>
<p> <i>git read-tree</i> and other merge-based commands (<i>git merge</i>, <i>git checkout</i>&#8230;) can help maintaining the skip-worktree bitmap and working directory update. <code>$GIT_DIR/info/sparse-checkout</code> is used to define the skip-worktree reference bitmap. When <i>git read-tree</i> needs to update the working directory, it resets the skip-worktree bit in the index based on this file, which uses the same syntax as .gitignore files. If an entry matches a pattern in this file, skip-worktree will not be set on that entry. Otherwise, skip-worktree will be set. </p>
<p> Then it compares the new skip-worktree value with the previous one. If skip-worktree turns from set to unset, it will add the corresponding file back. If it turns from unset to set, that file will be removed. </p>
<p> While <code>$GIT_DIR/info/sparse-checkout</code> is usually used to specify what files are in, you can also specify what files are <i>not</i> in, using negate patterns. For example, to remove the file <code>unwanted</code>: </p>
<dl>
<dt>
<dd>
<pre>
/*
!unwanted
</pre>
</dl>
<p> Another tricky thing is fully repopulating the working directory when you no longer want sparse checkout. You cannot just disable &quot;sparse checkout&quot; because skip-worktree bits are still in the index and your working directory is still sparsely populated. You should re-populate the working directory with the <code>$GIT_DIR/info/sparse-checkout</code> file content as follows: </p>
<dl>
<dt>
<dd>
<pre>
/*
</pre>
</dl>
<p> Then you can disable sparse checkout. Sparse checkout support in <i>git read-tree</i> and similar commands is disabled by default. You need to turn <code>core.sparseCheckout</code> on in order to have sparse checkout support.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-write-tree/">git-write-tree</a></code>(1); <code><a href="/docs/linux/man/1-git-ls-files/">git-ls-files</a></code>(1); <code><a href="/docs/linux/man/5-gitignore/">gitignore</a></code>(5); <code><a href="/docs/linux/man/1-git-sparse-checkout/">git-sparse-checkout</a></code>(1);</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>

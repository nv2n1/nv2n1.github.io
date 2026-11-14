---
title: "git-reset(1)"
name: "git-reset"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-reset/"
description: "git-reset – Reset current HEAD to the specified state"
---

<h2 class="name">NAME</h2>
<p> git-reset &#8211; Reset current HEAD to the specified state </p>
<h2>SYNOPSIS</h2>
<pre><code>
git reset[-q][&lt;tree - ish&gt;][--]&lt;pathspec&gt;... git reset[-q][--pathspec - from - file = &lt;file&gt;[--pathspec - file - nul]][&lt;tree - ish&gt;] git reset(--patch | -p)[&lt;tree - ish&gt;][--][&lt;pathspec&gt;...] git reset[--soft | --mixed[-N] | --hard | --merge | --keep][-q][&lt;commit&gt;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> In the first three forms, copy entries from <code>&lt;tree-ish&gt;</code> to the index. In the last form, set the current branch head (<code>HEAD</code>) to <code>&lt;commit&gt;</code>, optionally modifying index and working tree to match. The <code>&lt;tree-ish&gt;</code>/<code>&lt;commit&gt;</code> defaults to <code>HEAD</code> in all forms. </p>
<p> <i>git reset</i> [-q] [&lt;tree-ish&gt;] [&#8211;] &lt;pathspec&gt;&#8230;, <i>git reset</i> [-q] [&#8211;pathspec-from-file=&lt;file&gt; [&#8211;pathspec-file-nul]] [&lt;tree-ish&gt;]</p>
<dl>
<dt>
<dd> These forms reset the index entries for all paths that match the <code>&lt;pathspec&gt;</code> to their state at <code>&lt;tree-ish&gt;</code>. (It does not affect the working tree or the current branch.) </p>
<p> This means that <code>git reset &lt;pathspec&gt;</code> is the opposite of <code>git add &lt;pathspec&gt;</code>. This command is equivalent to <code>git restore [&#8211;source=&lt;tree-ish&gt;] &#8211;staged &lt;pathspec&gt;&#8230;</code>. </p>
<p> After running <code>git reset &lt;pathspec&gt;</code> to update the index entry, you can use <code><a href="/docs/linux/man/1-git-restore/">git-restore</a></code>(1) to check the contents out of the index to the working tree. Alternatively, using <code><a href="/docs/linux/man/1-git-restore/">git-restore</a></code>(1) and specifying a commit with <code>&#8211;source</code>, you can copy the contents of a path out of a commit to the index and to the working tree in one go.</dl>
<p> <i>git reset</i> (&#8211;patch | -p) [&lt;tree-ish&gt;] [&#8211;] [&lt;pathspec&gt;&#8230;]</p>
<dl>
<dt>
<dd> Interactively select hunks in the difference between the index and <code>&lt;tree-ish&gt;</code> (defaults to <code>HEAD</code>). The chosen hunks are applied in reverse to the index. </p>
<p> This means that <code>git reset -p</code> is the opposite of <code>git add -p</code>, i.e. you can use it to selectively reset hunks. See the &#8220;Interactive Mode&#8221; section of <code><a href="/docs/linux/man/1-git-add/">git-add</a></code>(1) to learn how to operate the <code>&#8211;patch</code> mode.</dl>
<p> <i>git reset</i> [&lt;mode&gt;] [&lt;commit&gt;]</p>
<dl>
<dt>
<dd> This form resets the current branch head to <code>&lt;commit&gt;</code> and possibly updates the index (resetting it to the tree of <code>&lt;commit&gt;</code>) and the working tree depending on <code>&lt;mode&gt;</code>. If <code>&lt;mode&gt;</code> is omitted, defaults to <code>&#8211;mixed</code>. The <code>&lt;mode&gt;</code> must be one of the following: </p>
<p> &#8211;soft</p>
<dl>
<dt>
<dd> Does not touch the index file or the working tree at all (but resets the head to <code>&lt;commit&gt;</code>, just like all modes do). This leaves all your changed files &quot;Changes to be committed&quot;, as <code>git status</code> would put it.</dl>
<p> &#8211;mixed</p>
<dl>
<dt>
<dd> Resets the index but not the working tree (i.e., the changed files are preserved but not marked for commit) and reports what has not been updated. This is the default action. </p>
<p> If <code>-N</code> is specified, removed paths are marked as intent-to-add (see <code><a href="/docs/linux/man/1-git-add/">git-add</a></code>(1)).</dl>
<p> &#8211;hard</p>
<dl>
<dt>
<dd> Resets the index and working tree. Any changes to tracked files in the working tree since <code>&lt;commit&gt;</code> are discarded. Any untracked files or directories in the way of writing any tracked files are simply deleted.</dl>
<p> &#8211;merge</p>
<dl>
<dt>
<dd> Resets the index and updates the files in the working tree that are different between <code>&lt;commit&gt;</code> and <code>HEAD</code>, but keeps those which are different between the index and working tree (i.e. which have changes which have not been added). If a file that is different between <code>&lt;commit&gt;</code> and the index has unstaged changes, reset is aborted. </p>
<p> In other words, <code>&#8211;merge</code> does something like a <code>git read-tree -u -m &lt;commit&gt;</code>, but carries forward unmerged index entries.</dl>
<p> &#8211;keep</p>
<dl>
<dt>
<dd> Resets index entries and updates files in the working tree that are different between <code>&lt;commit&gt;</code> and <code>HEAD</code>. If a file that is different between <code>&lt;commit&gt;</code> and <code>HEAD</code> has local changes, reset is aborted.</dl>
<p> &#8211;[no-]recurse-submodules</p>
<dl>
<dt>
<dd> When the working tree is updated, using &#8211;recurse-submodules will also recursively reset the working tree of all active submodules according to the commit recorded in the superproject, also setting the submodules&#8217; HEAD to be detached at that commit.</dl>
</dl>
<p> See &quot;Reset, restore and revert&quot; in <code><a href="/docs/linux/man/1-git/">git</a></code>(1) for the differences between the three commands.</p>
<h2>OPTIONS</h2>
<p> -q, &#8211;quiet, &#8211;no-quiet</p>
<dl>
<dt>
<dd> Be quiet, only report errors. The default behavior is set by the <code>reset.quiet</code> config option. <code>&#8211;quiet</code> and <code>&#8211;no-quiet</code> will override the default behavior.</dl>
<p> &#8211;pathspec-from-file=&lt;file&gt;</p>
<dl>
<dt>
<dd> Pathspec is passed in <code>&lt;file&gt;</code> instead of commandline args. If <code>&lt;file&gt;</code> is exactly <code>&#8211;</code> then standard input is used. Pathspec elements are separated by LF or CR/LF. Pathspec elements can be quoted as explained for the configuration variable <code>core.quotePath</code> (see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)). See also <code>&#8211;pathspec-file-nul</code> and global <code>&#8211;literal-pathspecs</code>.</dl>
<p> &#8211;pathspec-file-nul</p>
<dl>
<dt>
<dd> Only meaningful with <code>&#8211;pathspec-from-file</code>. Pathspec elements are separated with NUL character and all other characters are taken literally (including newlines and quotes).</dl>
<p> &#8212;</p>
<dl>
<dt>
<dd> Do not interpret any more arguments as options.</dl>
<p> &lt;pathspec&gt;&#8230;</p>
<dl>
<dt>
<dd> Limits the paths affected by the operation. </p>
<p> For more details, see the <i>pathspec</i> entry in <code><a href="/docs/linux/man/7-gitglossary/">gitglossary</a></code>(7).</dl>
<h2>EXAMPLES</h2>
<p> Undo add</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
$ edit                                     <code>(1)</code>
$ git add frotz.c filfre.c
$ mailx                                    <code>(2)</code>
$ git reset                                <code>(3)</code>
$ git pull <a href="git://info.example.com/">git://info.example.com/</a> nitfol  <code>(4)</code>
</pre>
</dl>
<p> <code>1. </code>You are happily working on something, and find the changes in these files are in good order. You do not want to see them when you run <code>git diff</code>, because you plan to work on other files and changes with these files are distracting.<br />
 <code>2. </code>Somebody asks you to pull, and the changes sound worthy of merging.<br />
 <code>3. </code>However, you already dirtied the index (i.e. your index does not match the <code>HEAD</code> commit). But you know the pull you are going to make does not affect <code>frotz.c</code> or <code>filfre.c</code>, so you revert the index changes for these two files. Your changes in working tree remain there.<br />
 <code>4. </code>Then you can pull and merge, leaving <code>frotz.c</code> and <code>filfre.c</code> changes still in the working tree.
</dl>
<p> Undo a commit and redo</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
$ git commit ...
$ git reset --soft HEAD^      <code>(1)</code>
$ edit                        <code>(2)</code>
$ git commit -a -c ORIG_HEAD  <code>(3)</code>
</pre>
</dl>
<p> <code>1. </code>This is most often done when you remembered what you just committed is incomplete, or you misspelled your commit message, or both. Leaves working tree as it was before &quot;reset&quot;.<br />
 <code>2. </code>Make corrections to working tree files.<br />
 <code>3. </code>&quot;reset&quot; copies the old head to <code>.git/ORIG_HEAD</code>; redo the commit by starting with its log message. If you do not need to edit the message further, you can give <code>-C</code> option instead. </p>
<p> See also the <code>&#8211;amend</code> option to <code><a href="/docs/linux/man/1-git-commit/">git-commit</a></code>(1).
</dl>
<p> Undo a commit, making it a topic branch</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
$ git branch topic/wip          <code>(1)</code>
$ git reset --hard HEAD~3       <code>(2)</code>
$ git switch topic/wip          <code>(3)</code>
</pre>
</dl>
<p> <code>1. </code>You have made some commits, but realize they were premature to be in the <code>master</code> branch. You want to continue polishing them in a topic branch, so create <code>topic/wip</code> branch off of the current <code>HEAD</code>.<br />
 <code>2. </code>Rewind the master branch to get rid of those three commits.<br />
 <code>3. </code>Switch to <code>topic/wip</code> branch and keep working.
</dl>
<p> Undo commits permanently</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
$ git commit ...
$ git reset --hard HEAD~3   <code>(1)</code>
</pre>
</dl>
<p> <code>1. </code>The last three commits (<code>HEAD</code>, <code>HEAD^</code>, and <code>HEAD~2</code>) were bad and you do not want to ever see them again. Do <code>not</code> do this if you have already given these commits to somebody else. (See the &quot;RECOVERING FROM UPSTREAM REBASE&quot; section in <code><a href="/docs/linux/man/1-git-rebase/">git-rebase</a></code>(1) for the implications of doing so.)
</dl>
<p> Undo a merge or pull</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
$ git pull                         <code>(1)</code>
Auto-merging nitfol
CONFLICT (content): Merge conflict in nitfol
Automatic merge failed; fix conflicts and then commit the result.
$ git reset --hard                 <code>(2)</code>
$ git pull . topic/branch          <code>(3)</code>
Updating from 41223... to 13134...
Fast-forward
$ git reset --hard ORIG_HEAD       <code>(4)</code>
</pre>
</dl>
<p> <code>1. </code>Try to update from the upstream resulted in a lot of conflicts; you were not ready to spend a lot of time merging right now, so you decide to do that later.<br />
 <code>2. </code>&quot;pull&quot; has not made merge commit, so <code>git reset &#8211;hard</code> which is a synonym for <code>git reset &#8211;hard HEAD</code> clears the mess from the index file and the working tree.<br />
 <code>3. </code>Merge a topic branch into the current branch, which resulted in a fast-forward.<br />
 <code>4. </code>But you decided that the topic branch is not ready for public consumption yet. &quot;pull&quot; or &quot;merge&quot; always leaves the original tip of the current branch in <code>ORIG_HEAD</code>, so resetting hard to it brings your index file and the working tree back to that state, and resets the tip of the branch to that commit.
</dl>
<p> Undo a merge or pull inside a dirty working tree</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
$ git pull(1)<br />
            Auto<br />
        &#8211; merging nitfol<br />
          Merge made by recursive.nitfol<br />
    | 20 ++ ++ +&#8211; &#8211;&#8230; $ git reset&#8211; merge ORIG_HEAD(2)
</dl>
<p> <code>1. </code>Even if you may have local modifications in your working tree, you can safely say <code>git pull</code> when you know that the change in the other branch does not overlap with them.<br />
 <code>2. </code>After inspecting the result of the merge, you may find that the change in the other branch is unsatisfactory. Running <code>git reset &#8211;hard ORIG_HEAD</code> will let you go back to where you were, but it will discard your local changes, which you do not want. <code>git reset &#8211;merge</code> keeps your local changes.
</dl>
<p> Interrupted workflow</p>
<dl>
<dt>
<dd> Suppose you are interrupted by an urgent fix request while you are in the middle of a large change. The files in your working tree are not in any shape to be committed yet, but you need to get to the other branch for a quick bugfix. </p>
<dl>
<dt>
<dd>
$ git switch feature;<br />
#you were working in &#8220;feature&#8221; branch and<br />
    $ work work work;<br />
#got interrupted<br />
        $ git commit &#8211;<br />
    a &#8211; m &#8220;snapshot WIP&#8221;(1)$ git switch master $ fix fix fix $ git commit;<br />
#commit with real log<br />
        $ git switch feature<br />
            $ git reset&#8211; soft HEAD ^<br />
    ;<br />
#go back to WIP state(2)<br />
    $ git reset(3)
</dl>
<p> <code>1. </code>This commit will get blown away so a throw-away log message is OK.<br />
 <code>2. </code>This removes the <i>WIP</i> commit from the commit history, and sets your working tree to the state just before you made that snapshot.<br />
 <code>3. </code>At this point the index file still has all the WIP changes you committed as <i>snapshot WIP</i>. This updates the index to show your WIP files as uncommitted. </p>
<p> See also <code><a href="/docs/linux/man/1-git-stash/">git-stash</a></code>(1).
</dl>
<p> Reset a single file in the index</p>
<dl>
<dt>
<dd> Suppose you have added a file to your index, but later decide you do not want to add it to your commit. You can remove the file from the index while keeping your changes with git reset. </p>
<dl>
<dt>
<dd>
<pre>
$ git reset -- frotz.c                      <code>(1)</code>
$ git commit -m &quot;Commit files in index&quot;     <code>(2)</code>
$ git add frotz.c                           <code>(3)</code>
</pre>
</dl>
<p> <code>1. </code>This removes the file from the index while keeping it in the working directory.<br />
 <code>2. </code>This commits all other changes in the index.<br />
 <code>3. </code>Adds the file to the index again.
</dl>
<p> Keep changes in working tree while discarding some previous commits</p>
<dl>
<dt>
<dd> Suppose you are working on something and you commit it, and then you continue working a bit more, but now you think that what you have in your working tree should be in another branch that has nothing to do with what you committed previously. You can start a new branch and reset it while keeping the changes in your working tree. </p>
<dl>
<dt>
<dd>
<pre>
$ git tag start
$ git switch -c branch1
$ edit
$ git commit ...                            <code>(1)</code>
$ edit
$ git switch -c branch2                     <code>(2)</code>
$ git reset --keep start                    <code>(3)</code>
</pre>
</dl>
<p> <code>1. </code>This commits your first edits in <code>branch1</code>.<br />
 <code>2. </code>In the ideal world, you could have realized that the earlier commit did not belong to the new topic when you created and switched to <code>branch2</code> (i.e. <code>git switch -c branch2 start</code>), but nobody is perfect.<br />
 <code>3. </code>But you can use <code>reset &#8211;keep</code> to remove the unwanted commit after you switched to <code>branch2</code>.
</dl>
<p> Split a commit apart into a sequence of commits</p>
<dl>
<dt>
<dd> Suppose that you have created lots of logically separate changes and committed them together. Then, later you decide that it might be better to have each logical chunk associated with its own commit. You can use git reset to rewind history without changing the contents of your local files, and then successively use <code>git add -p</code> to interactively select which hunks to include into each commit, using <code>git commit -c</code> to pre-populate the commit message. </p>
<dl>
<dt>
<dd>
$ git reset &#8211; N HEAD ^ (1)<br />
                               $ git add<br />
                           &#8211; p(2) $ git diff&#8211; cached(3) $ git commit &#8211; c HEAD @{1}(4)&#8230;(5) $ git add&#8230;(6) $ git diff&#8211; cached(7) $ git commit&#8230;(8)
</dl>
<p> <code>1. </code>First, reset the history back one commit so that we remove the original commit, but leave the working tree with all the changes. The -N ensures that any new files added with <code>HEAD</code> are still marked so that <code>git add -p</code> will find them.<br />
 <code>2. </code>Next, we interactively select diff hunks to add using the <code>git add -p</code> facility. This will ask you about each diff hunk in sequence and you can use simple commands such as &quot;yes, include this&quot;, &quot;No don&#8217;t include this&quot; or even the very powerful &quot;edit&quot; facility.<br />
 <code>3. </code>Once satisfied with the hunks you want to include, you should verify what has been prepared for the first commit by using <code>git diff &#8211;cached</code>. This shows all the changes that have been moved into the index and are about to be committed.<br />
 <code>4. </code>Next, commit the changes stored in the index. The <code>-c</code> option specifies to pre-populate the commit message from the original message that you started with in the first commit. This is helpful to avoid retyping it. The <code>HEAD@{1}</code> is a special notation for the commit that <code>HEAD</code> used to be at prior to the original reset commit (1 change ago). See <code><a href="/docs/linux/man/1-git-reflog/">git-reflog</a></code>(1) for more details. You may also use any other valid commit reference.<br />
 <code>5. </code>You can repeat steps 2-4 multiple times to break the original code into any number of commits.<br />
 <code>6. </code>Now you&#8217;ve split out many of the changes into their own commits, and might no longer use the patch mode of <code>git add</code>, in order to select all remaining uncommitted changes.<br />
 <code>7. </code>Once again, check to verify that you&#8217;ve included what you want to. You may also wish to verify that git diff doesn&#8217;t show any remaining changes to be committed later.<br />
 <code>8. </code>And finally create the final commit.
</dl>
<h2>DISCUSSION</h2>
<p> The tables below show what happens when running: </p>
<dl>
<dt>
<dd>
<pre>
git reset --option target
</pre>
</dl>
<p> to reset the <code>HEAD</code> to another commit (<code>target</code>) with the different reset options depending on the state of the files. </p>
<p> In these tables, <code>A</code>, <code>B</code>, <code>C</code> and <code>D</code> are some different states of a file. For example, the first line of the first table means that if a file is in state <code>A</code> in the working tree, in state <code>B</code> in the index, in state <code>C</code> in <code>HEAD</code> and in state <code>D</code> in the target, then <code>git reset &#8211;soft target</code> will leave the file in the working tree in state <code>A</code> and in the index in state <code>B</code>. It resets (i.e. moves) the <code>HEAD</code> (i.e. the tip of the current branch, if you are on one) to <code>target</code> (which has the file in state <code>D</code>). </p>
<dl>
<dt>
<dd>
working index HEAD target working index HEAD&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;A B C D&#8211; soft A B D&#8211; mixed A D D&#8211; hard D D D&#8211; merge(disallowed)&#8211; keep(disallowed)
</dl>
<dl>
<dt>
<dd>
working index HEAD target working index HEAD&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;A B C C&#8211; soft A B C&#8211; mixed A C C&#8211; hard C C C&#8211; merge(disallowed)&#8211; keep A C C
</dl>
<dl>
<dt>
<dd>
working index HEAD target working index HEAD&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;B B C D&#8211; soft B B D&#8211; mixed B D D&#8211; hard D D D&#8211; merge D D D&#8211; keep(disallowed)
</dl>
<dl>
<dt>
<dd>
working index HEAD target working index HEAD&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;B B C C&#8211; soft B B C&#8211; mixed B C C&#8211; hard C C C&#8211; merge C C C&#8211; keep B C C
</dl>
<dl>
<dt>
<dd>
working index HEAD target working index HEAD&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;B C C D&#8211; soft B C D&#8211; mixed B D D&#8211; hard D D D&#8211; merge(disallowed)&#8211; keep(disallowed)
</dl>
<dl>
<dt>
<dd>
working index HEAD target working index HEAD&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;B C C C&#8211; soft B C C&#8211; mixed B C C&#8211; hard C C C&#8211; merge B C C&#8211; keep B C C
</dl>
<p> <code>reset &#8211;merge</code> is meant to be used when resetting out of a conflicted merge. Any mergy operation guarantees that the working tree file that is involved in the merge does not have a local change with respect to the index before it starts, and that it writes the result out to the working tree. So if we see some difference between the index and the target and also between the index and the working tree, then it means that we are not resetting out from a state that a mergy operation left after failing with a conflict. That is why we disallow <code>&#8211;merge</code> option in this case. </p>
<p> <code>reset &#8211;keep</code> is meant to be used when removing some of the last commits in the current branch while keeping changes in the working tree. If there could be conflicts between the changes in the commit we want to remove and the changes in the working tree we want to keep, the reset is disallowed. That&#8217;s why it is disallowed if there are both changes between the working tree and <code>HEAD</code>, and between <code>HEAD</code> and the target. To be safe, it is also disallowed when there are unmerged entries. </p>
<p> The following tables show what happens when there are unmerged entries: </p>
<dl>
<dt>
<dd>
working index HEAD target working index HEAD&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;X U A B&#8211; soft(disallowed)&#8211; mixed X B B<br />
    &#8212; hard B B B<br />
    &#8212; merge B B B<br />
    &#8212; keep(disallowed)
</dl>
<dl>
<dt>
<dd>
<pre><code>
working index HEAD target working index HEAD-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --X U A A-- soft(disallowed)-- mixed X A A
    -- hard A A A
    -- merge A A A
    -- keep(disallowed)
</code></pre>
</dl>
<p> <code>X</code> means any state and <code>U</code> means an unmerged index.</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>

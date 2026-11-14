---
title: "git-filter-branch(1)"
name: "git-filter-branch"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-filter-branch/"
description: "git-filter-branch – Rewrite branches"
---

<h2 class="name">NAME</h2>
<p> git-filter-branch &#8211; Rewrite branches </p>
<h2>SYNOPSIS</h2>
<pre><code>
git filter - branch[--setup&lt;command&gt;][--subdirectory - filter&lt;directory&gt;]
                   [--env - filter&lt;command&gt;][--tree - filter&lt;command&gt;]
                   [--index - filter&lt;command&gt;][--parent - filter&lt;command&gt;]
                   [--msg - filter&lt;command&gt;][--commit - filter&lt;command&gt;]
                   [--tag - name - filter&lt;command&gt;][--prune - empty]
                   [--original&lt;namespace&gt;][-d&lt;directory&gt;][-f | --force]
                   [--state - branch&lt;branch&gt;][--][&lt;rev - list options&gt;...]
</code></pre>
<h2>WARNING</h2>
<p> <i>git filter-branch</i> has a plethora of pitfalls that can produce non-obvious manglings of the intended history rewrite (and can leave you with little time to investigate such problems since it has such abysmal performance). These safety and performance issues cannot be backward compatibly fixed and as such, its use is not recommended. Please use an alternative history filtering tool such as m[blue]<code>git filter-repo</code>m[]<font SIZE="-2">[1]</font>. If you still need to use <i>git filter-branch</i>, please carefully read the section called &#8220;SAFETY&#8221; (and the section called &#8220;PERFORMANCE&#8221;) to learn about the land mines of filter-branch, and then vigilantly avoid as many of the hazards listed there as reasonably possible.</p>
<h2>DESCRIPTION</h2>
<p> Lets you rewrite Git revision history by rewriting the branches mentioned in the &lt;rev-list options&gt;, applying custom filters on each revision. Those filters can modify each tree (e.g. removing a file or running a perl rewrite on all files) or information about each commit. Otherwise, all information (including original commit times or merge information) will be preserved. </p>
<p> The command will only rewrite the <i>positive</i> refs mentioned in the command line (e.g. if you pass <i>a..b</i>, only <i>b</i> will be rewritten). If you specify no filters, the commits will be recommitted without any changes, which would normally have no effect. Nevertheless, this may be useful in the future for compensating for some Git bugs or such, therefore such a usage is permitted. </p>
<p> <code>NOTE</code>: This command honors <code>.git/info/grafts</code> file and refs in the <code>refs/replace/</code> namespace. If you have any grafts or replacement refs defined, running this command will make them permanent. </p>
<p> <code>WARNING</code>! The rewritten history will have different object names for all the objects and will not converge with the original branch. You will not be able to easily push and distribute the rewritten branch on top of the original branch. Please do not use this command if you do not know the full implications, and avoid using it anyway, if a simple single commit would suffice to fix your problem. (See the &quot;RECOVERING FROM UPSTREAM REBASE&quot; section in <code><a href="/docs/linux/man/1-git-rebase/">git-rebase</a></code>(1) for further information about rewriting published history.) </p>
<p> Always verify that the rewritten version is correct: The original refs, if different from the rewritten ones, will be stored in the namespace <i>refs/original/</i>. </p>
<p> Note that since this operation is very I/O expensive, it might be a good idea to redirect the temporary directory off-disk with the <code>-d</code> option, e.g. on tmpfs. Reportedly the speedup is very noticeable.</p>
<h3>Filters</h3>
<p> The filters are applied in the order as listed below. The &lt;command&gt; argument is always evaluated in the shell context using the <i>eval</i> command (with the notable exception of the commit filter, for technical reasons). Prior to that, the <code>$GIT_COMMIT</code> environment variable will be set to contain the id of the commit being rewritten. Also, GIT_AUTHOR_NAME, GIT_AUTHOR_EMAIL, GIT_AUTHOR_DATE, GIT_COMMITTER_NAME, GIT_COMMITTER_EMAIL, and GIT_COMMITTER_DATE are taken from the current commit and exported to the environment, in order to affect the author and committer identities of the replacement commit created by <code><a href="/docs/linux/man/1-git-commit-tree/">git-commit-tree</a></code>(1) after the filters have run. </p>
<p> If any evaluation of &lt;command&gt; returns a non-zero exit status, the whole operation will be aborted. </p>
<p> A <i>map</i> function is available that takes an &quot;original sha1 id&quot; argument and outputs a &quot;rewritten sha1 id&quot; if the commit has been already rewritten, and &quot;original sha1 id&quot; otherwise; the <i>map</i> function can return several ids on separate lines if your commit filter emitted multiple commits.</p>
<h2>OPTIONS</h2>
<p> &#8211;setup &lt;command&gt;</p>
<dl>
<dt>
<dd> This is not a real filter executed for each commit but a one time setup just before the loop. Therefore no commit-specific variables are defined yet. Functions or variables defined here can be used or modified in the following filter steps except the commit filter, for technical reasons.</dl>
<p> &#8211;subdirectory-filter &lt;directory&gt;</p>
<dl>
<dt>
<dd> Only look at the history which touches the given subdirectory. The result will contain that directory (and only that) as its project root. Implies the section called &#8220;Remap to ancestor&#8221;.</dl>
<p> &#8211;env-filter &lt;command&gt;</p>
<dl>
<dt>
<dd> This filter may be used if you only need to modify the environment in which the commit will be performed. Specifically, you might want to rewrite the author/committer name/email/time environment variables (see <code><a href="/docs/linux/man/1-git-commit-tree/">git-commit-tree</a></code>(1) for details).</dl>
<p> &#8211;tree-filter &lt;command&gt;</p>
<dl>
<dt>
<dd> This is the filter for rewriting the tree and its contents. The argument is evaluated in shell with the working directory set to the root of the checked out tree. The new tree is then used as-is (new files are auto-added, disappeared files are auto-removed &#8211; neither .gitignore files nor any other ignore rules <code>HAVE ANY EFFECT</code>!).</dl>
<p> &#8211;index-filter &lt;command&gt;</p>
<dl>
<dt>
<dd> This is the filter for rewriting the index. It is similar to the tree filter but does not check out the tree, which makes it much faster. Frequently used with <code>git rm &#8211;cached &#8211;ignore-unmatch &#8230;</code>, see EXAMPLES below. For hairy cases, see <code><a href="/docs/linux/man/1-git-update-index/">git-update-index</a></code>(1).</dl>
<p> &#8211;parent-filter &lt;command&gt;</p>
<dl>
<dt>
<dd> This is the filter for rewriting the commit&#8217;s parent list. It will receive the parent string on stdin and shall output the new parent string on stdout. The parent string is in the format described in <code><a href="/docs/linux/man/1-git-commit-tree/">git-commit-tree</a></code>(1): empty for the initial commit, &quot;-p parent&quot; for a normal commit and &quot;-p parent1 -p parent2 -p parent3 &#8230;&quot; for a merge commit.</dl>
<p> &#8211;msg-filter &lt;command&gt;</p>
<dl>
<dt>
<dd> This is the filter for rewriting the commit messages. The argument is evaluated in the shell with the original commit message on standard input; its standard output is used as the new commit message.</dl>
<p> &#8211;commit-filter &lt;command&gt;</p>
<dl>
<dt>
<dd> This is the filter for performing the commit. If this filter is specified, it will be called instead of the <i>git commit-tree</i> command, with arguments of the form &quot;&lt;TREE_ID&gt; [(-p &lt;PARENT_COMMIT_ID&gt;)&#8230;]&quot; and the log message on stdin. The commit id is expected on stdout. </p>
<p> As a special extension, the commit filter may emit multiple commit ids; in that case, the rewritten children of the original commit will have all of them as parents. </p>
<p> You can use the <i>map</i> convenience function in this filter, and other convenience functions, too. For example, calling <i>skip_commit &quot;$@&quot;</i> will leave out the current commit (but not its changes! If you want that, use <i>git rebase</i> instead). </p>
<p> You can also use the <code>git_commit_non_empty_tree &quot;$@&quot;</code> instead of <code>git commit-tree &quot;$@&quot;</code> if you don&#8217;t wish to keep commits with a single parent and that makes no change to the tree.</dl>
<p> &#8211;tag-name-filter &lt;command&gt;</p>
<dl>
<dt>
<dd> This is the filter for rewriting tag names. When passed, it will be called for every tag ref that points to a rewritten object (or to a tag object which points to a rewritten object). The original tag name is passed via standard input, and the new tag name is expected on standard output. </p>
<p> The original tags are not deleted, but can be overwritten; use &quot;&#8211;tag-name-filter cat&quot; to simply update the tags. In this case, be very careful and make sure you have the old tags backed up in case the conversion has run afoul. </p>
<p> Nearly proper rewriting of tag objects is supported. If the tag has a message attached, a new tag object will be created with the same message, author, and timestamp. If the tag has a signature attached, the signature will be stripped. It is by definition impossible to preserve signatures. The reason this is &quot;nearly&quot; proper, is because ideally if the tag did not change (points to the same object, has the same name, etc.) it should retain any signature. That is not the case, signatures will always be removed, buyer beware. There is also no support for changing the author or timestamp (or the tag message for that matter). Tags which point to other tags will be rewritten to point to the underlying commit.</dl>
<p> &#8211;prune-empty</p>
<dl>
<dt>
<dd> Some filters will generate empty commits that leave the tree untouched. This option instructs git-filter-branch to remove such commits if they have exactly one or zero non-pruned parents; merge commits will therefore remain intact. This option cannot be used together with <code>&#8211;commit-filter</code>, though the same effect can be achieved by using the provided <code>git_commit_non_empty_tree</code> function in a commit filter.</dl>
<p> &#8211;original &lt;namespace&gt;</p>
<dl>
<dt>
<dd> Use this option to set the namespace where the original commits will be stored. The default value is <i>refs/original</i>.</dl>
<p> -d &lt;directory&gt;</p>
<dl>
<dt>
<dd> Use this option to set the path to the temporary directory used for rewriting. When applying a tree filter, the command needs to temporarily check out the tree to some directory, which may consume considerable space in case of large projects. By default it does this in the <code>.git-rewrite/</code> directory but you can override that choice by this parameter.</dl>
<p> -f, &#8211;force</p>
<dl>
<dt>
<dd> <i>git filter-branch</i> refuses to start with an existing temporary directory or when there are already refs starting with <i>refs/original/</i>, unless forced.</dl>
<p> &#8211;state-branch &lt;branch&gt;</p>
<dl>
<dt>
<dd> This option will cause the mapping from old to new objects to be loaded from named branch upon startup and saved as a new commit to that branch upon exit, enabling incremental of large trees. If <i>&lt;branch&gt;</i> does not exist it will be created.</dl>
<p> &lt;rev-list options&gt;&#8230;</p>
<dl>
<dt>
<dd> Arguments for <i>git rev-list</i>. All positive refs included by these options are rewritten. You may also specify options such as <code>&#8211;all</code>, but you must use <code>&#8212;</code> to separate them from the <i>git filter-branch</i> options. Implies the section called &#8220;Remap to ancestor&#8221;.</dl>
<h3>Remap to ancestor</h3>
<p> By using <code><a href="/docs/linux/man/1-git-rev-list/">git-rev-list</a></code>(1) arguments, e.g., path limiters, you can limit the set of revisions which get rewritten. However, positive refs on the command line are distinguished: we don&#8217;t let them be excluded by such limiters. For this purpose, they are instead rewritten to point at the nearest ancestor that was not excluded.</p>
<h2>EXIT STATUS</h2>
<p> On success, the exit status is <code>0</code>. If the filter can&#8217;t find any commits to rewrite, the exit status is <code>2</code>. On any other error, the exit status may be any other non-zero value.</p>
<h2>EXAMPLES</h2>
<p> Suppose you want to remove a file (containing confidential information or copyright violation) from all commits: </p>
<dl>
<dt>
<dd>
<pre>
git filter-branch --tree-filter 'rm filename' HEAD
</pre>
</dl>
<p> However, if the file is absent from the tree of some commit, a simple <code>rm filename</code> will fail for that tree and commit. Thus you may instead want to use <code>rm -f filename</code> as the script. </p>
<p> Using <code>&#8211;index-filter</code> with <i>git rm</i> yields a significantly faster version. Like with using <code>rm filename</code>, <code>git rm &#8211;cached filename</code> will fail if the file is absent from the tree of a commit. If you want to &quot;completely forget&quot; a file, it does not matter when it entered history, so we also add <code>&#8211;ignore-unmatch</code>: </p>
<dl>
<dt>
<dd>
<pre>
git filter-branch --index-filter 'git rm --cached --ignore-unmatch filename' HEAD
</pre>
</dl>
<p> Now, you will get the rewritten history saved in HEAD. </p>
<p> To rewrite the repository to look as if <code>foodir/</code> had been its project root, and discard all other history: </p>
<dl>
<dt>
<dd>
<pre>
git filter-branch --subdirectory-filter foodir -- --all
</pre>
</dl>
<p> Thus you can, e.g., turn a library subdirectory into a repository of its own. Note the <code>&#8212;</code> that separates <i>filter-branch</i> options from revision options, and the <code>&#8211;all</code> to rewrite all branches and tags. </p>
<p> To set a commit (which typically is at the tip of another history) to be the parent of the current initial commit, in order to paste the other history behind the current history: </p>
<dl>
<dt>
<dd>
<pre>
git filter-branch --parent-filter 'sed &quot;s/^\$/-p &lt;graft-id&gt;/&quot;' HEAD
</pre>
</dl>
<p> (if the parent string is empty &#8211; which happens when we are dealing with the initial commit &#8211; add graftcommit as a parent). Note that this assumes history with a single root (that is, no merge without common ancestors happened). If this is not the case, use: </p>
<dl>
<dt>
<dd>
<pre>
git filter-branch --parent-filter \
        'test $GIT_COMMIT = &lt;commit-id&gt; &amp;&amp; echo &quot;-p &lt;graft-id&gt;&quot; || cat' HEAD
</pre>
</dl>
<p> or even simpler: </p>
<dl>
<dt>
<dd>
<pre>
git replace --graft $commit-id $graft-id
git filter-branch $graft-id..HEAD
</pre>
</dl>
<p> To remove commits authored by &quot;Darl McBribe&quot; from the history: </p>
<dl>
<dt>
<dd>
git filter &#8211; branch&#8211; commit &#8211; filter &#8216; if[&#8220;$GIT_AUTHOR_NAME&#8221; = &#8220;Darl McBribe&#8221;];<br />
then<br />
    skip_commit &#8220;$@&#8221;;<br />
else git commit &#8211; tree &#8220;$@&#8221;;<br />
fi&#8217; HEAD
</dl>
<p> The function <i>skip_commit</i> is defined as follows: </p>
<dl>
<dt>
<dd>
skip_commit()<br />
{<br />
    shift;<br />
    while<br />
        [-n &#8220;$1&#8221;];<br />
    do<br />
        shift;<br />
    map &#8220;$1&#8221;;<br />
    shift;<br />
    done;<br />
}
</dl>
<p> The shift magic first throws away the tree id and then the -p parameters. Note that this handles merges properly! In case Darl committed a merge between P1 and P2, it will be propagated properly and all children of the merge will become merge commits with P1,P2 as their parents instead of the merge commit. </p>
<p> <code>NOTE</code> the changes introduced by the commits, and which are not reverted by subsequent commits, will still be in the rewritten branch. If you want to throw out <i>changes</i> together with the commits, you should use the interactive mode of <i>git rebase</i>. </p>
<p> You can rewrite the commit log messages using <code>&#8211;msg-filter</code>. For example, <i>git svn-id</i> strings in a repository created by <i>git svn</i> can be removed this way: </p>
<dl>
<dt>
<dd>
<pre>
git filter-branch --msg-filter '
        sed -e &quot;/^git-svn-id:/d&quot;
'
</pre>
</dl>
<p> If you need to add <i>Acked-by</i> lines to, say, the last 10 commits (none of which is a merge), use this command: </p>
<dl>
<dt>
<dd>
git filter &#8211; branch&#8211; msg &#8211; filter &#8216; cat &amp;&amp;echo &#8220;Acked-by: Bugs Bunny &lt;bunny [at] bugzilla.org&gt;&#8221;<br />
&#8216; HEAD~10..HEAD
</dl>
<p> The <code>&#8211;env-filter</code> option can be used to modify committer and/or author identity. For example, if you found out that your commits have the wrong identity due to a misconfigured user.email, you can make a correction, before publishing the project, like this: </p>
<dl>
<dt>
<dd>
git filter &#8211; branch&#8211; env &#8211; filter &#8216; if test &#8220;$GIT_AUTHOR_EMAIL&#8221; = &#8220;root [at] localhost&#8221; then<br />
    GIT_AUTHOR_EMAIL = john[at] example.com<br />
                           fi if test &#8220;$GIT_COMMITTER_EMAIL&#8221; = &#8220;root [at] localhost&#8221; then<br />
        GIT_COMMITTER_EMAIL = john[at] example.com<br />
                                  fi<br />
&#8216; &#8212; &#8211;all
</dl>
<p> To restrict rewriting to only part of the history, specify a revision range in addition to the new branch name. The new branch name will point to the top-most revision that a <i>git rev-list</i> of this range will print. </p>
<p> Consider this history: </p>
<dl>
<dt>
<dd>
<pre><code>
D-- E-- F-- G-- H / /
    A-- B-- -- -C
</code></pre>
</dl>
<p> To rewrite only commits D,E,F,G,H, but leave A, B and C alone, use: </p>
<dl>
<dt>
<dd>
<pre>
git filter-branch ... C..H
</pre>
</dl>
<p> To rewrite commits E,F,G,H, use one of these: </p>
<dl>
<dt>
<dd>
<pre>
git filter-branch ... C..H --not D
git filter-branch ... D..H --not C
</pre>
</dl>
<p> To move the whole tree into a subdirectory, or remove it from there: </p>
<dl>
<dt>
<dd>
<pre>
git filter-branch --index-filter \
        'git ls-files -s | sed &quot;s-	\&quot;*-&amp;newsubdir/-&quot; |
                GIT_INDEX_FILE=$GIT_INDEX_FILE.new \
                        git update-index --index-info &amp;&amp;
         mv &quot;$GIT_INDEX_FILE.new&quot; &quot;$GIT_INDEX_FILE&quot;' HEAD
</pre>
</dl>
<h2>CHECKLIST FOR SHRINKING A REPOSITORY</h2>
<p> git-filter-branch can be used to get rid of a subset of files, usually with some combination of <code>&#8211;index-filter</code> and <code>&#8211;subdirectory-filter</code>. People expect the resulting repository to be smaller than the original, but you need a few more steps to actually make it smaller, because Git tries hard not to lose your objects until you tell it to. First make sure that: </p>
<dl>
<dt>
<dd> &bull; You really removed all variants of a filename, if a blob was moved over its lifetime. <code>git log &#8211;name-only &#8211;follow &#8211;all &#8212; filename</code> can help you find renames.</dl>
<dl>
<dt>
<dd> &bull; You really filtered all refs: use <code>&#8211;tag-name-filter cat &#8212; &#8211;all</code> when calling git-filter-branch.</dl>
<p> Then there are two ways to get a smaller repository. A safer way is to clone, that keeps your original intact. </p>
<dl>
<dt>
<dd> &bull; Clone it with <code>git clone file:///path/to/repo</code>. The clone will not have the removed objects. See <code><a href="/docs/linux/man/1-git-clone/">git-clone</a></code>(1). (Note that cloning with a plain path just hardlinks everything!)</dl>
<p> If you really don&#8217;t want to clone it, for whatever reasons, check the following points instead (in this order). This is a very destructive approach, so <code>make a backup</code> or go back to cloning it. You have been warned. </p>
<dl>
<dt>
<dd> &bull; Remove the original refs backed up by git-filter-branch: say <code>git for-each-ref &#8211;format=&quot;%(refname)&quot; refs/original/ | xargs -n 1 git update-ref -d</code>.</dl>
<dl>
<dt>
<dd> &bull; Expire all reflogs with <code>git reflog expire &#8211;expire=now &#8211;all</code>.</dl>
<dl>
<dt>
<dd> &bull; Garbage collect all unreferenced objects with <code>git gc &#8211;prune=now</code> (or if your git-gc is not new enough to support arguments to <code>&#8211;prune</code>, use <code>git repack -ad; git prune</code> instead).</dl>
<h2>PERFORMANCE</h2>
<p> The performance of git-filter-branch is glacially slow; its design makes it impossible for a backward-compatible implementation to ever be fast: </p>
<dl>
<dt>
<dd> &bull; In editing files, git-filter-branch by design checks out each and every commit as it existed in the original repo. If your repo has <code>10^5</code> files and <code>10^5</code> commits, but each commit only modifies five files, then git-filter-branch will make you do <code>10^10</code> modifications, despite only having (at most) <code>5*10^5</code> unique blobs.</dl>
<dl>
<dt>
<dd> &bull; If you try and cheat and try to make git-filter-branch only work on files modified in a commit, then two things happen </p>
<dl>
<dt>
<dd> &bull; you run into problems with deletions whenever the user is simply trying to rename files (because attempting to delete files that don&#8217;t exist looks like a no-op; it takes some chicanery to remap deletes across file renames when the renames happen via arbitrary user-provided shell)</dl>
<dl>
<dt>
<dd> &bull; even if you succeed at the map-deletes-for-renames chicanery, you still technically violate backward compatibility because users are allowed to filter files in ways that depend upon topology of commits instead of filtering solely based on file contents or names (though this has not been observed in the wild).</dl>
</dl>
<dl>
<dt>
<dd> &bull; Even if you don&#8217;t need to edit files but only want to e.g. rename or remove some and thus can avoid checking out each file (i.e. you can use &#8211;index-filter), you still are passing shell snippets for your filters. This means that for every commit, you have to have a prepared git repo where those filters can be run. That&#8217;s a significant setup.</dl>
<dl>
<dt>
<dd> &bull; Further, several additional files are created or updated per commit by git-filter-branch. Some of these are for supporting the convenience functions provided by git-filter-branch (such as map()), while others are for keeping track of internal state (but could have also been accessed by user filters; one of git-filter-branch&#8217;s regression tests does so). This essentially amounts to using the filesystem as an IPC mechanism between git-filter-branch and the user-provided filters. Disks tend to be a slow IPC mechanism, and writing these files also effectively represents a forced synchronization point between separate processes that we hit with every commit.</dl>
<dl>
<dt>
<dd> &bull; The user-provided shell commands will likely involve a pipeline of commands, resulting in the creation of many processes per commit. Creating and running another process takes a widely varying amount of time between operating systems, but on any platform it is very slow relative to invoking a function.</dl>
<dl>
<dt>
<dd> &bull; git-filter-branch itself is written in shell, which is kind of slow. This is the one performance issue that could be backward-compatibly fixed, but compared to the above problems that are intrinsic to the design of git-filter-branch, the language of the tool itself is a relatively minor issue. </p>
<dl>
<dt>
<dd> &bull; Side note: Unfortunately, people tend to fixate on the written-in-shell aspect and periodically ask if git-filter-branch could be rewritten in another language to fix the performance issues. Not only does that ignore the bigger intrinsic problems with the design, it&#8217;d help less than you&#8217;d expect: if git-filter-branch itself were not shell, then the convenience functions (map(), skip_commit(), etc) and the <code>&#8211;setup</code> argument could no longer be executed once at the beginning of the program but would instead need to be prepended to every user filter (and thus re-executed with every commit).</dl>
</dl>
<p> The m[blue]<code>git filter-repo</code>m[]<font SIZE="-2">[1]</font> tool is an alternative to git-filter-branch which does not suffer from these performance problems or the safety problems (mentioned below). For those with existing tooling which relies upon git-filter-branch, <i>git filter-repo</i> also provides m[blue]<code>filter-lamely</code>m[]<font SIZE="-2">[2]</font>, a drop-in git-filter-branch replacement (with a few caveats). While filter-lamely suffers from all the same safety issues as git-filter-branch, it at least ameliorates the performance issues a little.</p>
<h2>SAFETY</h2>
<p> git-filter-branch is riddled with gotchas resulting in various ways to easily corrupt repos or end up with a mess worse than what you started with: </p>
<dl>
<dt>
<dd> &bull; Someone can have a set of &quot;working and tested filters&quot; which they document or provide to a coworker, who then runs them on a different OS where the same commands are not working/tested (some examples in the git-filter-branch manpage are also affected by this). BSD vs. GNU userland differences can really bite. If lucky, error messages are spewed. But just as likely, the commands either don&#8217;t do the filtering requested, or silently corrupt by making some unwanted change. The unwanted change may only affect a few commits, so it&#8217;s not necessarily obvious either. (The fact that problems won&#8217;t necessarily be obvious means they are likely to go unnoticed until the rewritten history is in use for quite a while, at which point it&#8217;s really hard to justify another flag-day for another rewrite.)</dl>
<dl>
<dt>
<dd> &bull; Filenames with spaces are often mishandled by shell snippets since they cause problems for shell pipelines. Not everyone is familiar with find -print0, xargs -0, git-ls-files -z, etc. Even people who are familiar with these may assume such flags are not relevant because someone else renamed any such files in their repo back before the person doing the filtering joined the project. And often, even those familiar with handling arguments with spaces may not do so just because they aren&#8217;t in the mindset of thinking about everything that could possibly go wrong.</dl>
<dl>
<dt>
<dd> &bull; Non-ascii filenames can be silently removed despite being in a desired directory. Keeping only wanted paths is often done using pipelines like <code>git ls-files | grep -v ^WANTED_DIR/ | xargs git rm</code>. ls-files will only quote filenames if needed, so folks may not notice that one of the files didn&#8217;t match the regex (at least not until it&#8217;s much too late). Yes, someone who knows about core.quotePath can avoid this (unless they have other special characters like 	, 
, or &quot;), and people who use ls-files -z with something other than grep can avoid this, but that doesn&#8217;t mean they will.</dl>
<dl>
<dt>
<dd> &bull; Similarly, when moving files around, one can find that filenames with non-ascii or special characters end up in a different directory, one that includes a double quote character. (This is technically the same issue as above with quoting, but perhaps an interesting different way that it can and has manifested as a problem.)</dl>
<dl>
<dt>
<dd> &bull; It&#8217;s far too easy to accidentally mix up old and new history. It&#8217;s still possible with any tool, but git-filter-branch almost invites it. If lucky, the only downside is users getting frustrated that they don&#8217;t know how to shrink their repo and remove the old stuff. If unlucky, they merge old and new history and end up with multiple &quot;copies&quot; of each commit, some of which have unwanted or sensitive files and others which don&#8217;t. This comes about in multiple different ways: </p>
<dl>
<dt>
<dd> &bull; the default to only doing a partial history rewrite (<i>&#8211;all</i> is not the default and few examples show it)</dl>
<dl>
<dt>
<dd> &bull; the fact that there&#8217;s no automatic post-run cleanup</dl>
<dl>
<dt>
<dd> &bull; the fact that &#8211;tag-name-filter (when used to rename tags) doesn&#8217;t remove the old tags but just adds new ones with the new name</dl>
<dl>
<dt>
<dd> &bull; the fact that little educational information is provided to inform users of the ramifications of a rewrite and how to avoid mixing old and new history. For example, this man page discusses how users need to understand that they need to rebase their changes for all their branches on top of new history (or delete and reclone), but that&#8217;s only one of multiple concerns to consider. See the &quot;DISCUSSION&quot; section of the git filter-repo manual page for more details.</dl>
</dl>
<dl>
<dt>
<dd> &bull; Annotated tags can be accidentally converted to lightweight tags, due to either of two issues: </p>
<dl>
<dt>
<dd> &bull; Someone can do a history rewrite, realize they messed up, restore from the backups in refs/original/, and then redo their git-filter-branch command. (The backup in refs/original/ is not a real backup; it dereferences tags first.)</dl>
<dl>
<dt>
<dd> &bull; Running git-filter-branch with either &#8211;tags or &#8211;all in your &lt;rev-list options&gt;. In order to retain annotated tags as annotated, you must use &#8211;tag-name-filter (and must not have restored from refs/original/ in a previously botched rewrite).</dl>
</dl>
<dl>
<dt>
<dd> &bull; Any commit messages that specify an encoding will become corrupted by the rewrite; git-filter-branch ignores the encoding, takes the original bytes, and feeds it to commit-tree without telling it the proper encoding. (This happens whether or not &#8211;msg-filter is used.)</dl>
<dl>
<dt>
<dd> &bull; Commit messages (even if they are all UTF-8) by default become corrupted due to not being updated &#8212; any references to other commit hashes in commit messages will now refer to no-longer-extant commits.</dl>
<dl>
<dt>
<dd> &bull; There are no facilities for helping users find what unwanted crud they should delete, which means they are much more likely to have incomplete or partial cleanups that sometimes result in confusion and people wasting time trying to understand. (For example, folks tend to just look for big files to delete instead of big directories or extensions, and once they do so, then sometime later folks using the new repository who are going through history will notice a build artifact directory that has some files but not others, or a cache of dependencies (node_modules or similar) which couldn&#8217;t have ever been functional since it&#8217;s missing some files.)</dl>
<dl>
<dt>
<dd> &bull; If &#8211;prune-empty isn&#8217;t specified, then the filtering process can create hoards of confusing empty commits</dl>
<dl>
<dt>
<dd> &bull; If &#8211;prune-empty is specified, then intentionally placed empty commits from before the filtering operation are also pruned instead of just pruning commits that became empty due to filtering rules.</dl>
<dl>
<dt>
<dd> &bull; If &#8211;prune-empty is specified, sometimes empty commits are missed and left around anyway (a somewhat rare bug, but it happens&#8230;)</dl>
<dl>
<dt>
<dd> &bull; A minor issue, but users who have a goal to update all names and emails in a repository may be led to &#8211;env-filter which will only update authors and committers, missing taggers.</dl>
<dl>
<dt>
<dd> &bull; If the user provides a &#8211;tag-name-filter that maps multiple tags to the same name, no warning or error is provided; git-filter-branch simply overwrites each tag in some undocumented pre-defined order resulting in only one tag at the end. (A git-filter-branch regression test requires this surprising behavior.)</dl>
<p> Also, the poor performance of git-filter-branch often leads to safety issues: </p>
<dl>
<dt>
<dd> &bull; Coming up with the correct shell snippet to do the filtering you want is sometimes difficult unless you&#8217;re just doing a trivial modification such as deleting a couple files. Unfortunately, people often learn if the snippet is right or wrong by trying it out, but the rightness or wrongness can vary depending on special circumstances (spaces in filenames, non-ascii filenames, funny author names or emails, invalid timezones, presence of grafts or replace objects, etc.), meaning they may have to wait a long time, hit an error, then restart. The performance of git-filter-branch is so bad that this cycle is painful, reducing the time available to carefully re-check (to say nothing about what it does to the patience of the person doing the rewrite even if they do technically have more time available). This problem is extra compounded because errors from broken filters may not be shown for a long time and/or get lost in a sea of output. Even worse, broken filters often just result in silent incorrect rewrites.</dl>
<dl>
<dt>
<dd> &bull; To top it all off, even when users finally find working commands, they naturally want to share them. But they may be unaware that their repo didn&#8217;t have some special cases that someone else&#8217;s does. So, when someone else with a different repository runs the same commands, they get hit by the problems above. Or, the user just runs commands that really were vetted for special cases, but they run it on a different OS where it doesn&#8217;t work, as noted above.</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> git filter-repo</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://github.com/newren/git-filter-repo/">https://github.com/newren/git-filter-repo/</a></dl>
<dt> 2.</p>
<dd> filter-lamely</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://github.com/newren/git-filter-repo/blob/master/contrib/filter-repo-demos/filter-lamely">https://github.com/newren/git-filter-repo/blob/master/contrib/filter-repo-demos/filter-lamely</a></dl>
</dl>
<h2>Index</h2>

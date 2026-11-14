---
title: "git-subtree(1)"
name: "git-subtree"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-subtree/"
description: "git-subtree – Merge subtrees together and split repository into subtrees"
---

<h2 class="name">NAME</h2>
<p> git-subtree &#8211; Merge subtrees together and split repository into subtrees </p>
<h2>SYNOPSIS</h2>
<pre><code>
git subtree[&lt;options&gt;] - P&lt;prefix&gt; add&lt;local - commit&gt; git subtree[&lt;options&gt;] - P&lt;prefix&gt; add&lt;repository&gt;&lt;remote - ref&gt; git subtree[&lt;options&gt;] - P&lt;prefix&gt; merge&lt;local - commit&gt; git subtree[&lt;options&gt;] - P&lt;prefix&gt; split[&lt;local - commit&gt;]
</code></pre>
<p>git subtree[&lt;options&gt;] &#8211; P&lt;prefix&gt; pull&lt;repository&gt;&lt;remote &#8211; ref&gt; git subtree[&lt;options&gt;] &#8211; P&lt;prefix&gt; push&lt;repository&gt;&lt;refspec&gt;</p>
<h2>DESCRIPTION</h2>
<p> Subtrees allow subprojects to be included within a subdirectory of the main project, optionally including the subproject&#8217;s entire history. </p>
<p> For example, you could include the source code for a library as a subdirectory of your application. </p>
<p> Subtrees are not to be confused with submodules, which are meant for the same task. Unlike submodules, subtrees do not need any special constructions (like <i>.gitmodules</i> files or gitlinks) be present in your repository, and do not force end-users of your repository to do anything special or to understand how subtrees work. A subtree is just a subdirectory that can be committed to, branched, and merged along with your project in any way you want. </p>
<p> They are also not to be confused with using the subtree merge strategy. The main difference is that, besides merging the other project as a subdirectory, you can also extract the entire history of a subdirectory from your project and make it into a standalone project. Unlike the subtree merge strategy you can alternate back and forth between these two operations. If the standalone library gets updated, you can automatically merge the changes into your project; if you update the library inside your project, you can &quot;split&quot; the changes back out again and merge them back into the library project. </p>
<p> For example, if a library you made for one application ends up being useful elsewhere, you can extract its entire history and publish that as its own git repository, without accidentally intermingling the history of your application project. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Tip</code> </font> </p>
<p> In order to keep your commit messages clean, we recommend that people split their commits between the subtrees and the main project as much as possible. That is, if you make a change that affects both the library and the main application, commit it in two pieces. That way, when you split the library commits out later, their descriptions will still make sense. But if this isn&#8217;t important to you, it&#8217;s not <code>necessary</code>. <i>git subtree</i> will simply leave out the non-library-related parts of the commit when it splits it out into the subproject later. </p>
</dl>
<h2>COMMANDS</h2>
<p> add &lt;local-commit&gt;, add &lt;repository&gt; &lt;remote-ref&gt;</p>
<dl>
<dt>
<dd> Create the &lt;prefix&gt; subtree by importing its contents from the given &lt;local-commit&gt; or &lt;repository&gt; and &lt;remote-ref&gt;. A new commit is created automatically, joining the imported project&#8217;s history with your own. With <i>&#8211;squash</i>, import only a single commit from the subproject, rather than its entire history.</dl>
<p> merge &lt;local-commit&gt;</p>
<dl>
<dt>
<dd> Merge recent changes up to &lt;local-commit&gt; into the &lt;prefix&gt; subtree. As with normal <i>git merge</i>, this doesn&#8217;t remove your own local changes; it just merges those changes into the latest &lt;local-commit&gt;. With <i>&#8211;squash</i>, create only one commit that contains all the changes, rather than merging in the entire history. </p>
<p> If you use <i>&#8211;squash</i>, the merge direction doesn&#8217;t always have to be forward; you can use this command to go back in time from v2.5 to v2.4, for example. If your merge introduces a conflict, you can resolve it in the usual ways.</dl>
<p> split [&lt;local-commit&gt;]</p>
<dl>
<dt>
<dd> Extract a new, synthetic project history from the history of the &lt;prefix&gt; subtree of &lt;local-commit&gt;, or of HEAD if no &lt;local-commit&gt; is given. The new history includes only the commits (including merges) that affected &lt;prefix&gt;, and each of those commits now has the contents of &lt;prefix&gt; at the root of the project instead of in a subdirectory. Thus, the newly created history is suitable for export as a separate git repository. </p>
<p> After splitting successfully, a single commit ID is printed to stdout. This corresponds to the HEAD of the newly created tree, which you can manipulate however you want. </p>
<p> Repeated splits of exactly the same history are guaranteed to be identical (i.e. to produce the same commit IDs) as long as the settings passed to <i>split</i> (such as <i>&#8211;annotate</i>) are the same. Because of this, if you add new commits and then re-split, the new commits will be attached as commits on top of the history you generated last time, so <i>git merge</i> and friends will work as expected.</dl>
<p> pull &lt;repository&gt; &lt;remote-ref&gt;</p>
<dl>
<dt>
<dd> Exactly like <i>merge</i>, but parallels <i>git pull</i> in that it fetches the given ref from the specified remote repository.</dl>
<p> push &lt;repository&gt; [+][&lt;local-commit&gt;:]&lt;remote-ref&gt;</p>
<dl>
<dt>
<dd> Does a <i>split</i> using the &lt;prefix&gt; subtree of &lt;local-commit&gt; and then does a <i>git push</i> to push the result to the &lt;repository&gt; and &lt;remote-ref&gt;. This can be used to push your subtree to different branches of the remote repository. Just as with <i>split</i>, if no &lt;local-commit&gt; is given, then HEAD is used. The optional leading <i>+</i> is ignored.</dl>
<h2>OPTIONS FOR ALL COMMANDS</h2>
<p> -q, &#8211;quiet</p>
<dl>
<dt>
<dd> Suppress unnecessary output messages on stderr.</dl>
<p> -d, &#8211;debug</p>
<dl>
<dt>
<dd> Produce even more unnecessary output messages on stderr.</dl>
<p> -P &lt;prefix&gt;, &#8211;prefix=&lt;prefix&gt;</p>
<dl>
<dt>
<dd> Specify the path in the repository to the subtree you want to manipulate. This option is mandatory for all commands.</dl>
<h2>OPTIONS FOR FIADDFR AND FIMERGEFR (ALSO: FIPULLFR, FISPLIT &#8211;REJOINFR, AND FIPUSH &#8211;REJOINFR)</h2>
<p> These options for <i>add</i> and <i>merge</i> may also be given to <i>pull</i> (which wraps <i>merge</i>), <i>split &#8211;rejoin</i> (which wraps either <i>add</i> or <i>merge</i> as appropriate), and <i>push &#8211;rejoin</i> (which wraps <i>split &#8211;rejoin</i>). </p>
<p> &#8211;squash</p>
<dl>
<dt>
<dd> Instead of merging the entire history from the subtree project, produce only a single commit that contains all the differences you want to merge, and then merge that new commit into your project. </p>
<p> Using this option helps to reduce log clutter. People rarely want to see every change that happened between v1.0 and v1.1 of the library they&#8217;re using, since none of the interim versions were ever included in their application. </p>
<p> Using <i>&#8211;squash</i> also helps avoid problems when the same subproject is included multiple times in the same project, or is removed and then re-added. In such a case, it doesn&#8217;t make sense to combine the histories anyway, since it&#8217;s unclear which part of the history belongs to which subtree. </p>
<p> Furthermore, with <i>&#8211;squash</i>, you can switch back and forth between different versions of a subtree, rather than strictly forward. <i>git subtree merge &#8211;squash</i> always adjusts the subtree to match the exactly specified commit, even if getting to that commit would require undoing some changes that were added earlier. </p>
<p> Whether or not you use <i>&#8211;squash</i>, changes made in your local repository remain intact and can be later split and send upstream to the subproject.</dl>
<p> -m &lt;message&gt;, &#8211;message=&lt;message&gt;</p>
<dl>
<dt>
<dd> Specify &lt;message&gt; as the commit message for the merge commit.</dl>
<h2>OPTIONS FOR FISPLITFR (ALSO: FIPUSHFR)</h2>
<p> These options for <i>split</i> may also be given to <i>push</i> (which wraps <i>split</i>). </p>
<p> &#8211;annotate=&lt;annotation&gt;</p>
<dl>
<dt>
<dd> When generating synthetic history, add &lt;annotation&gt; as a prefix to each commit message. Since we&#8217;re creating new commits with the same commit message, but possibly different content, from the original commits, this can help to differentiate them and avoid confusion. </p>
<p> Whenever you split, you need to use the same &lt;annotation&gt;, or else you don&#8217;t have a guarantee that the new re-created history will be identical to the old one. That will prevent merging from working correctly. git subtree tries to make it work anyway, particularly if you use <i>&#8211;rejoin</i>, but it may not always be effective.</dl>
<p> -b &lt;branch&gt;, &#8211;branch=&lt;branch&gt;</p>
<dl>
<dt>
<dd> After generating the synthetic history, create a new branch called &lt;branch&gt; that contains the new history. This is suitable for immediate pushing upstream. &lt;branch&gt; must not already exist.</dl>
<p> &#8211;ignore-joins</p>
<dl>
<dt>
<dd> If you use <i>&#8211;rejoin</i>, git subtree attempts to optimize its history reconstruction to generate only the new commits since the last <i>&#8211;rejoin</i>. <i>&#8211;ignore-joins</i> disables this behavior, forcing it to regenerate the entire history. In a large project, this can take a long time.</dl>
<p> &#8211;onto=&lt;onto&gt;</p>
<dl>
<dt>
<dd> If your subtree was originally imported using something other than git subtree, its history may not match what git subtree is expecting. In that case, you can specify the commit ID &lt;onto&gt; that corresponds to the first revision of the subproject&#8217;s history that was imported into your project, and git subtree will attempt to build its history from there. </p>
<p> If you used <i>git subtree add</i>, you should never need this option.</dl>
<p> &#8211;rejoin</p>
<dl>
<dt>
<dd> After splitting, merge the newly created synthetic history back into your main project. That way, future splits can search only the part of history that has been added since the most recent <i>&#8211;rejoin</i>. </p>
<p> If your split commits end up merged into the upstream subproject, and then you want to get the latest upstream version, this will allow git&#8217;s merge algorithm to more intelligently avoid conflicts (since it knows these synthetic commits are already part of the upstream repository). </p>
<p> Unfortunately, using this option results in <i>git log</i> showing an extra copy of every new commit that was created (the original, and the synthetic one). </p>
<p> If you do all your merges with <i>&#8211;squash</i>, make sure you also use <i>&#8211;squash</i> when you <i>split &#8211;rejoin</i>.</dl>
<h2>EXAMPLE 1. FIADDFR COMMAND</h2>
<p> Let&#8217;s assume that you have a local repository that you would like to add an external vendor library to. In this case we will add the git-subtree repository as a subdirectory of your already existing git-extensions repository in ~/git-extensions/: </p>
<dl>
<dt>
<dd>
<pre>
$ git subtree add --prefix=git-subtree --squash \
        <a href="git://github.com/apenwarr/git-subtree.git">git://github.com/apenwarr/git-subtree.git</a> master
</pre>
</dl>
<p> <i>master</i> needs to be a valid remote ref and can be a different branch name </p>
<p> You can omit the <i>&#8211;squash</i> flag, but doing so will increase the number of commits that are included in your local repository. </p>
<p> We now have a ~/git-extensions/git-subtree directory containing code from the master branch of <a href="git://github.com/apenwarr/git-subtree.git">git://github.com/apenwarr/git-subtree.git</a> in our git-extensions repository.</p>
<h2>EXAMPLE 2. EXTRACT A SUBTREE USING FICOMMITFR, FIMERGEFR AND FIPULLFR</h2>
<p> Let&#8217;s use the repository for the git source code as an example. First, get your own copy of the git.git repository: </p>
<dl>
<dt>
<dd>
<pre>
$ git clone <a href="git://git.kernel.org/pub/scm/git/git.git">git://git.kernel.org/pub/scm/git/git.git</a> test-git
$ cd test-git
</pre>
</dl>
<p> gitweb (commit 1130ef3) was merged into git as of commit 0a8f4f0, after which it was no longer maintained separately. But imagine it had been maintained separately, and we wanted to extract git&#8217;s changes to gitweb since that time, to share with the upstream. You could do this: </p>
<dl>
<dt>
<dd>
$ git subtree split&#8211; prefix = gitweb&#8211; annotate = &#8216;(split) &#8216; 0a8f4f0 ^..&#8211;onto = 1130ef3 &#8211;rejoin&#8211; branch gitweb &#8211; latest $ gitk gitweb &#8211; latest $ git push git[at] github.com : whatever / gitweb.git gitweb &#8211; latest : master
</dl>
<p> (We use <i>0a8f4f0^..</i> because that means &quot;all the changes from 0a8f4f0 to the current version, including 0a8f4f0 itself.&quot;) </p>
<p> If gitweb had originally been merged using <i>git subtree add</i> (or a previous split had already been done with <i>&#8211;rejoin</i> specified) then you can do all your splits without having to remember any weird commit IDs: </p>
<dl>
<dt>
<dd>
<pre><code>
$ git subtree split-- prefix = gitweb-- annotate = '(split) ' --rejoin-- branch gitweb - latest2
</code></pre>
</dl>
<p> And you can merge changes back in from the upstream project just as easily: </p>
<dl>
<dt>
<dd>
<pre>
$ git subtree pull --prefix=gitweb \
        git [at] github.com:whatever/gitweb.git master
</pre>
</dl>
<p> Or, using <i>&#8211;squash</i>, you can actually rewind to an earlier version of gitweb: </p>
<dl>
<dt>
<dd>
<pre>
$ git subtree merge --prefix=gitweb --squash gitweb-latest~10
</pre>
</dl>
<p> Then make some changes: </p>
<dl>
<dt>
<dd>
<pre>
$ date &gt;gitweb/myfile
$ git add gitweb/myfile
$ git commit -m 'created myfile'
</pre>
</dl>
<p> And fast forward again: </p>
<dl>
<dt>
<dd>
<pre>
$ git subtree merge --prefix=gitweb --squash gitweb-latest
</pre>
</dl>
<p> And notice that your change is still intact: </p>
<dl>
<dt>
<dd>
<pre>
$ ls -l gitweb/myfile
</pre>
</dl>
<p> And you can split it out and look at your changes versus the standard gitweb: </p>
<dl>
<dt>
<dd>
<pre>
git log gitweb-latest..$(git subtree split --prefix=gitweb)
</pre>
</dl>
<h2>EXAMPLE 3. EXTRACT A SUBTREE USING A BRANCH</h2>
<p> Suppose you have a source directory with many files and subdirectories, and you want to extract the lib directory to its own git project. Here&#8217;s a short way to do it: </p>
<p> First, make the new repository wherever you want: </p>
<dl>
<dt>
<dd>
<pre>
$ &lt;go to the new location&gt;
$ git init --bare
</pre>
</dl>
<p> Back in your original directory: </p>
<dl>
<dt>
<dd>
<pre>
$ git subtree split --prefix=lib --annotate=&quot;(split)&quot; -b split
</pre>
</dl>
<p> Then push the new branch onto the new empty repository: </p>
<dl>
<dt>
<dd>
<pre>
$ git push &lt;new-repo&gt; split:master
</pre>
</dl>
<h2>AUTHOR</h2>
<p> Written by Avery Pennarun &lt;m[blue]<code>apenwarr [at] gmail.com</code>m[]<font SIZE="-2">[1]</font>&gt;</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> apenwarr [at] gmail.com</p>
<dl>
<dt>
<dd> mailto:apenwarr [at] gmail.com</dl>
</dl>
<h2>Index</h2>

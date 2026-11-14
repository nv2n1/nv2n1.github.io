---
title: "gittutorial(7)"
name: "gittutorial"
section: "7"
letter: "g"
url: "/docs/linux/man/7-gittutorial/"
description: "gittutorial – A tutorial introduction to Git"
---

<p>gittutorial &#8211; A tutorial introduction to Git</p>
<h2>Synopsis</h2>
<pre>git *</pre>
<h2>Description</h2>
<p>This tutorial explains how to import a new project into Git, make changes to it, and share changes with other developers. If you are instead primarily interested in using Git to fetch a project, for example, to test the latest version, you may prefer to start with the first two chapters of m[blue]<code>The Git User&#8217;s Manual</code>m[]<font SIZE="-2">[1]</font>. First, note that you can get documentation for a command such as <code>git log &#8211;graph</code> with:</p>
<dl>
<dd>
<pre>$ man git-log</pre>
</dl>
<p> or:</p>
<dl>
<dd>
<pre>$ git help log</pre>
</dl>
<p> With the latter, you can use the manual viewer of your choice; see <code><a href="/docs/linux/man/1-git-help/">git-help</a></code>(1) for more information. It is a good idea to introduce yourself to Git with your name and public email address before doing any operation. The easiest way to do so is:</p>
<dl>
<dd>
<pre>$ git config --global user.name &quot;Your Name Comes Here&quot;
$ git config --global user.email you [at] yourdomain.example.com</pre>
</dl>
<h2>Importing A New Project</h2>
<p>Assume you have a tarball project.tar.gz with your initial work. You can place it under Git revision control as follows. </p>
<dl>
<dd>
<pre>$ tar xzf project.tar.gz
$ cd project
$ git init</pre>
</dl>
<p> Git will reply </p>
<dl>
<dd>
<pre>Initialized empty Git repository in .git/</pre>
</dl>
<p> You&#8217;ve now initialized the working directory&#8212;you may notice a new directory created, named &quot;.git&quot;. </p>
<p> Next, tell Git to take a snapshot of the contents of all files under the current directory (note the <i>.</i>), with <i>git add</i>: </p>
<dl>
<dd>
<pre>$ git add .</pre>
</dl>
<p> This snapshot is now stored in a temporary staging area which Git calls the &quot;index&quot;. You can permanently store the contents of the index in the repository with <i>git commit</i>: </p>
<dl>
<dd>
<pre>$ git commit</pre>
</dl>
<p> This will prompt you for a commit message. You&#8217;ve now stored the first version of your project in Git.</p>
<h2>Making Changes</h2>
<p>Modify some files, then add their updated contents to the index: </p>
<dl>
<dd>
<pre>$ git add file1 file2 file3</pre>
</dl>
<p> You are now ready to commit. You can see what is about to be committed using <i>git diff</i> with the &#8211;cached option: </p>
<dl>
<dd>
<pre>$ git diff --cached</pre>
</dl>
<p> (Without &#8211;cached, <i>git diff</i> will show you any changes that you&#8217;ve made but not yet added to the index.) You can also get a brief summary of the situation with <i>git status</i>: </p>
<dl>
<dd>
<pre>$ git status
On branch master
Changes to be committed:
Your branch is up to date with 'origin/master'.
 (use &quot;git restore --staged &lt;file&gt;...&quot; to unstage)
 modified: file1
 modified: file2
 modified: file3</pre>
</dl>
<p> If you need to make any further adjustments, do so now, and then add any newly modified content to the index. Finally, commit your changes with: </p>
<dl>
<dd>
<pre>$ git commit</pre>
</dl>
<p> This will again prompt you for a message describing the change, and then record a new version of the project. </p>
<p> Alternatively, instead of running <i>git add</i> beforehand, you can use </p>
<dl>
<dd>
<pre>$ git commit -a</pre>
</dl>
<p> which will automatically notice any modified (but not new) files, add them to the index, and commit, all in one step. </p>
<p> A note on commit messages: Though not required, it&#8217;s a good idea to begin the commit message with a single short (less than 50 character) line summarizing the change, followed by a blank line and then a more thorough description. The text up to the first blank line in a commit message is treated as the commit title, and that title is used throughout Git. For example, <code><a href="/docs/linux/man/1-git-format-patch/">git-format-patch</a></code>(1) turns a commit into email, and it uses the title on the Subject line and the rest of the commit in the body.</p>
<h2>Git Tracks Content Not Files</h2>
<p>Many revision control systems provide an <code>add</code> command that tells the system to start tracking changes to a new file. Git&#8217;s <code>add</code> command does something simpler and more powerful: <i>git add</i> is used both for new and newly modified files, and in both cases it takes a snapshot of the given files and stages that content in the index, ready for inclusion in the next commit.</p>
<h2>Viewing Project History</h2>
<p>At any point you can view the history of your changes using </p>
<dl>
<dd>
<pre>$ git log</pre>
</dl>
<p> If you also want to see complete diffs at each step, use </p>
<dl>
<dd>
<pre>$ git log -p</pre>
</dl>
<p> Often the overview of the change is useful to get a feel of each step </p>
<dl>
<dd>
<pre>$ git log --stat --summary</pre>
</dl>
<h2>Managing Branches</h2>
<p>A single Git repository can maintain multiple branches of development. To create a new branch named &quot;experimental&quot;, use </p>
<dl>
<dd>
<pre>$ git branch experimental</pre>
</dl>
<p> If you now run </p>
<dl>
<dd>
<pre>$ git branch</pre>
</dl>
<p> you&#8217;ll get a list of all existing branches: </p>
<dl>
<dd>
<pre> experimental
* master</pre>
</dl>
<p> The &quot;experimental&quot; branch is the one you just created, and the &quot;master&quot; branch is a default branch that was created for you automatically. The asterisk marks the branch you are currently on; type </p>
<dl>
<dd>
<pre>$ git switch experimental</pre>
</dl>
<p> to switch to the experimental branch. Now edit a file, commit the change, and switch back to the master branch: </p>
<dl>
<dd>
<pre>(edit file)
$ git commit -a
$ git switch master</pre>
</dl>
<p> Check that the change you made is no longer visible, since it was made on the experimental branch and you&#8217;re back on the master branch. </p>
<p> You can make a different change on the master branch: </p>
<dl>
<dd>
<pre>(edit file)
$ git commit -a</pre>
</dl>
<p> at this point the two branches have diverged, with different changes made in each. To merge the changes made in experimental into master, run </p>
<dl>
<dd>
<pre>$ git merge experimental</pre>
</dl>
<p> If the changes don&#8217;t conflict, you&#8217;re done. If there are conflicts, markers will be left in the problematic files showing the conflict; </p>
<dl>
<dd>
<pre>$ git diff</pre>
</dl>
<p> will show this. Once you&#8217;ve edited the files to resolve the conflicts, </p>
<dl>
<dd>
<pre>$ git commit -a</pre>
</dl>
<p> will commit the result of the merge. Finally, </p>
<dl>
<dd>
<pre>$ gitk</pre>
</dl>
<p> will show a nice graphical representation of the resulting history. </p>
<p> At this point you could delete the experimental branch with </p>
<dl>
<dd>
<pre>$ git branch -d experimental</pre>
</dl>
<p> This command ensures that the changes in the experimental branch are already in the current branch. </p>
<p> If you develop on a branch crazy-idea, then regret it, you can always delete the branch with </p>
<dl>
<dd>
<pre>$ git branch -D crazy-idea</pre>
</dl>
<p> Branches are cheap and easy, so this is a good way to try something out.</p>
<h2>Using Git For Collaboration</h2>
<p>Suppose that Alice has started a new project with a Git repository in /home/alice/project, and that Bob, who has a home directory on the same machine, wants to contribute. </p>
<p> Bob begins with: </p>
<dl>
<dd>
<pre>bob$ git clone /home/alice/project myrepo</pre>
</dl>
<p> This creates a new directory &quot;myrepo&quot; containing a clone of Alice&#8217;s repository. The clone is on an equal footing with the original project, possessing its own copy of the original project&#8217;s history. </p>
<p> Bob then makes some changes and commits them: </p>
<dl>
<dd>
<pre>(edit files)
bob$ git commit -a
(repeat as necessary)</pre>
</dl>
<p> When he&#8217;s ready, he tells Alice to pull changes from the repository at /home/bob/myrepo. She does this with: </p>
<dl>
<dd>
<pre>alice$ cd /home/alice/project
alice$ git pull /home/bob/myrepo master</pre>
</dl>
<p> This merges the changes from Bob&#8217;s &quot;master&quot; branch into Alice&#8217;s current branch. If Alice has made her own changes in the meantime, then she may need to manually fix any conflicts. </p>
<p> The &quot;pull&quot; command thus performs two operations: it fetches changes from a remote branch, then merges them into the current branch. </p>
<p> Note that in general, Alice would want her local changes committed before initiating this &quot;pull&quot;. If Bob&#8217;s work conflicts with what Alice did since their histories forked, Alice will use her working tree and the index to resolve conflicts, and existing local changes will interfere with the conflict resolution process (Git will still perform the fetch but will refuse to merge &#8212; Alice will have to get rid of her local changes in some way and pull again when this happens). </p>
<p> Alice can peek at what Bob did without merging first, using the &quot;fetch&quot; command; this allows Alice to inspect what Bob did, using a special symbol &quot;FETCH_HEAD&quot;, in order to determine if he has anything worth pulling, like this: </p>
<dl>
<dd>
<pre>alice$ git fetch /home/bob/myrepo master
alice$ git log -p HEAD..FETCH_HEAD</pre>
</dl>
<p> This operation is safe even if Alice has uncommitted local changes. The range notation &quot;HEAD..FETCH_HEAD&quot; means &quot;show everything that is reachable from the FETCH_HEAD but exclude anything that is reachable from HEAD&quot;. Alice already knows everything that leads to her current state (HEAD), and reviews what Bob has in his state (FETCH_HEAD) that she has not seen with this command. </p>
<p> If Alice wants to visualize what Bob did since their histories forked she can issue the following command: </p>
<dl>
<dd>
<pre>$ gitk HEAD..FETCH_HEAD</pre>
</dl>
<p> This uses the same two-dot range notation we saw earlier with <i>git log</i>. </p>
<p> Alice may want to view what both of them did since they forked. She can use three-dot form instead of the two-dot form: </p>
<dl>
<dd>
<pre>$ gitk HEAD...FETCH_HEAD</pre>
</dl>
<p> This means &quot;show everything that is reachable from either one, but exclude anything that is reachable from both of them&quot;. </p>
<p> Please note that these range notation can be used with both gitk and &quot;git log&quot;. </p>
<p> After inspecting what Bob did, if there is nothing urgent, Alice may decide to continue working without pulling from Bob. If Bob&#8217;s history does have something Alice would immediately need, Alice may choose to stash her work-in-progress first, do a &quot;pull&quot;, and then finally unstash her work-in-progress on top of the resulting history. </p>
<p> When you are working in a small closely knit group, it is not unusual to interact with the same repository over and over again. By defining <i>remote</i> repository shorthand, you can make it easier: </p>
<dl>
<dd>
<pre>alice$ git remote add bob /home/bob/myrepo</pre>
</dl>
<p> With this, Alice can perform the first part of the &quot;pull&quot; operation alone using the <i>git fetch</i> command without merging them with her own branch, using: </p>
<dl>
<dd>
<pre>alice$ git fetch bob</pre>
</dl>
<p> Unlike the longhand form, when Alice fetches from Bob using a remote repository shorthand set up with <i>git remote</i>, what was fetched is stored in a remote-tracking branch, in this case <code>bob/master</code>. So after this: </p>
<dl>
<dd>
<pre>alice$ git log -p master..bob/master</pre>
</dl>
<p> shows a list of all the changes that Bob made since he branched from Alice&#8217;s master branch. </p>
<p> After examining those changes, Alice could merge the changes into her master branch: </p>
<dl>
<dd>
<pre>alice$ git merge bob/master</pre>
</dl>
<p> This <code>merge</code> can also be done by <i>pulling from her own remote-tracking branch</i>, like this: </p>
<dl>
<dd>
<pre>alice$ git pull . remotes/bob/master</pre>
</dl>
<p> Note that git pull always merges into the current branch, regardless of what else is given on the command line. </p>
<p> Later, Bob can update his repo with Alice&#8217;s latest changes using </p>
<dl>
<dd>
<pre>bob$ git pull</pre>
</dl>
<p> Note that he doesn&#8217;t need to give the path to Alice&#8217;s repository; when Bob cloned Alice&#8217;s repository, Git stored the location of her repository in the repository configuration, and that location is used for pulls: </p>
<dl>
<dd>
<pre>bob$ git config --get remote.origin.url
/home/alice/project</pre>
</dl>
<p> (The complete configuration created by <i>git clone</i> is visible using <code>git config -l</code>, and the <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1) man page explains the meaning of each option.) </p>
<p> Git also keeps a pristine copy of Alice&#8217;s master branch under the name &quot;origin/master&quot;: </p>
<dl>
<dd>
<pre>bob$ git branch -r
 origin/master</pre>
</dl>
<p> If Bob later decides to work from a different host, he can still perform clones and pulls using the ssh protocol: </p>
<dl>
<dd>
<pre>bob$ git clone alice.org:/home/alice/project myrepo</pre>
</dl>
<p> Alternatively, Git has a native protocol, or can use http; see <code><a href="/docs/linux/man/1-git-pull/">git-pull</a></code>(1) for details. </p>
<p> Git can also be used in a CVS-like mode, with a central repository that various users push changes to; see <code><a href="/docs/linux/man/1-git-push/">git-push</a></code>(1) and <code><a href="/docs/linux/man/7-gitcvs-migration/">gitcvs-migration</a></code>(7).</p>
<h2>Exploring History</h2>
<p>Git history is represented as a series of interrelated commits. We have already seen that the <i>git log</i> command can list those commits. Note that first line of each git log entry also gives a name for the commit: </p>
<dl>
<dd>
<pre>$ git log
commit c82a22c39cbc32576f64f5c6b3f24b99ea8149c7
Author: Junio C Hamano &lt;junkio [at] cox.net&gt;
Date: Tue May 16 17:18:22 2006 -0700
 merge-base: Clarify the comments on post processing.</pre>
</dl>
<p> We can give this name to <i>git show</i> to see the details about this commit. </p>
<dl>
<dd>
<pre>$ git show c82a22c39cbc32576f64f5c6b3f24b99ea8149c7</pre>
</dl>
<p> But there are other ways to refer to commits. You can use any initial part of the name that is long enough to uniquely identify the commit: </p>
<dl>
<dd>
<pre>$ git show c82a22c39c # the first few characters of the name are
 # usually enough
$ git show HEAD # the tip of the current branch
$ git show experimental # the tip of the &quot;experimental&quot; branch</pre>
</dl>
<p> Every commit usually has one &quot;parent&quot; commit which points to the previous state of the project: </p>
<dl>
<dd>
<pre>$ git show HEAD^ # to see the parent of HEAD
$ git show HEAD^^ # to see the grandparent of HEAD
$ git show HEAD~4 # to see the great-great grandparent of HEAD</pre>
</dl>
<p> Note that merge commits may have more than one parent: </p>
<dl>
<dd>
<pre>$ git show HEAD^1 # show the first parent of HEAD (same as HEAD^)
$ git show HEAD^2 # show the second parent of HEAD</pre>
</dl>
<p> You can also give commits names of your own; after running </p>
<dl>
<dd>
<pre>$ git tag v2.5 1b2e1d63ff</pre>
</dl>
<p> you can refer to 1b2e1d63ff by the name &quot;v2.5&quot;. If you intend to share this name with other people (for example, to identify a release version), you should create a &quot;tag&quot; object, and perhaps sign it; see <code><a href="/docs/linux/man/1-git-tag/">git-tag</a></code>(1) for details. </p>
<p> Any Git command that needs to know a commit can take any of these names. For example: </p>
<dl>
<dd>
<pre>$ git diff v2.5 HEAD # compare the current HEAD to v2.5
$ git branch stable v2.5 # start a new branch named &quot;stable&quot; based
 # at v2.5
$ git reset --hard HEAD^ # reset your current branch and working
 # directory to its state at HEAD^</pre>
</dl>
<p> Be careful with that last command: in addition to losing any changes in the working directory, it will also remove all later commits from this branch. If this branch is the only branch containing those commits, they will be lost. Also, don&#8217;t use <i>git reset</i> on a publicly-visible branch that other developers pull from, as it will force needless merges on other developers to clean up the history. If you need to undo changes that you have pushed, use <i>git revert</i> instead. </p>
<p> The <i>git grep</i> command can search for strings in any version of your project, so </p>
<dl>
<dd>
<pre>$ git grep &quot;hello&quot; v2.5</pre>
</dl>
<p> searches for all occurrences of &quot;hello&quot; in v2.5. </p>
<p> If you leave out the commit name, <i>git grep</i> will search any of the files it manages in your current directory. So </p>
<dl>
<dd>
<pre>$ git grep &quot;hello&quot;</pre>
</dl>
<p> is a quick way to search just the files that are tracked by Git. </p>
<p> Many Git commands also take sets of commits, which can be specified in a number of ways. Here are some examples with <i>git log</i>: </p>
<dl>
<dd>
<pre>$ git log v2.5..v2.6 # commits between v2.5 and v2.6
$ git log v2.5.. # commits since v2.5
$ git log --since=&quot;2 weeks ago&quot; # commits from the last 2 weeks
$ git log v2.5.. Makefile # commits since v2.5 which modify
 # Makefile</pre>
</dl>
<p> You can also give <i>git log</i> a &quot;range&quot; of commits where the first is not necessarily an ancestor of the second; for example, if the tips of the branches &quot;stable&quot; and &quot;master&quot; diverged from a common commit some time ago, then </p>
<dl>
<dd>
<pre>$ git log stable..master</pre>
</dl>
<p> will list commits made in the master branch but not in the stable branch, while </p>
<dl>
<dd>
<pre>$ git log master..stable</pre>
</dl>
<p> will show the list of commits made on the stable branch but not the master branch. </p>
<p> The <i>git log</i> command has a weakness: it must present commits in a list. When the history has lines of development that diverged and then merged back together, the order in which <i>git log</i> presents those commits is meaningless. </p>
<p> Most projects with multiple contributors (such as the Linux kernel, or Git itself) have frequent merges, and <i>gitk</i> does a better job of visualizing their history. For example, </p>
<dl>
<dd>
<pre>$ gitk --since=&quot;2 weeks ago&quot; drivers/</pre>
</dl>
<p> allows you to browse any commits from the last 2 weeks of commits that modified files under the &quot;drivers&quot; directory. (Note: you can adjust gitk&#8217;s fonts by holding down the control key while pressing &quot;-&quot; or &quot;+&quot;.) </p>
<p> Finally, most commands that take filenames will optionally allow you to precede any filename by a commit, to specify a particular version of the file: </p>
<dl>
<dd>
<pre>$ git diff v2.5:Makefile HEAD:Makefile.in</pre>
</dl>
<p> You can also use <i>git show</i> to see any such file: </p>
<dl>
<dd>
<pre>$ git show v2.5:Makefile</pre>
</dl>
<h2>Next Steps</h2>
<p>This tutorial should be enough to perform basic distributed revision control for your projects. However, to fully understand the depth and power of Git you need to understand two simple ideas on which it is based: </p>
<dl>
<dd>&bull; The object database is the rather elegant system used to store the history of your project&#8212;files, directories, and commits.</dl>
<dl>
<dd>&bull; The index file is a cache of the state of a directory tree, used to create commits, check out working directories, and hold the various trees involved in a merge.</dl>
<p> Part two of this tutorial explains the object database, the index file, and a few other odds and ends that you&#8217;ll need to make the most of Git. You can find it at <code><a href="/docs/linux/man/7-gittutorial-2/">gittutorial-2</a></code>(7). </p>
<p> If you don&#8217;t want to continue with that right away, a few other digressions that may be interesting at this point are: </p>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/1-git-format-patch/">git-format-patch</a></code>(1), <code><a href="/docs/linux/man/1-git-am/">git-am</a></code>(1): These convert series of git commits into emailed patches, and vice versa, useful for projects such as the Linux kernel which rely heavily on emailed patches.</dl>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/1-git-bisect/">git-bisect</a></code>(1): When there is a regression in your project, one way to track down the bug is by searching through the history to find the exact commit that&#8217;s to blame. Git bisect can help you perform a binary search for that commit. It is smart enough to perform a close-to-optimal search even in the case of complex non-linear history with lots of merged branches.</dl>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/7-gitworkflows/">gitworkflows</a></code>(7): Gives an overview of recommended workflows.</dl>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/7-giteveryday/">giteveryday</a></code>(7): Everyday Git with 20 Commands Or So.</dl>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/7-gitcvs-migration/">gitcvs-migration</a></code>(7): Git for CVS users.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-gittutorial-2/">gittutorial-2</a></code>(7), <code><a href="/docs/linux/man/7-gitcvs-migration/">gitcvs-migration</a></code>(7), <code><a href="/docs/linux/man/7-gitcore-tutorial/">gitcore-tutorial</a></code>(7), <code><a href="/docs/linux/man/7-gitglossary/">gitglossary</a></code>(7), <code><a href="/docs/linux/man/1-git-help/">git-help</a></code>(1), <code><a href="/docs/linux/man/7-gitworkflows/">gitworkflows</a></code>(7), <code><a href="/docs/linux/man/7-giteveryday/">giteveryday</a></code>(7), m[blue]<code>The Git User&#8217;s Manual</code>m[]<font SIZE="-2">[1]</font></p>
<h2>Git</h2>
<p>Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>The Git User&#8217;s Manual</p>
<dl>
<dd>file:///usr/share/doc/git/html/user-manual.html</dl>

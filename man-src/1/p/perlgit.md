---
title: "perlgit(1)"
name: "perlgit"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlgit/"
description: "perlgit – Detailed information about git and the Perl repository"
---

<h2 class="name">NAME</h2>
<p> perlgit &#8211; Detailed information about git and the Perl repository </p>
<h2>DESCRIPTION</h2>
<p> This document provides details on using git to develop Perl. If you are just interested in working on a quick patch, see perlhack first. This document is intended for people who are regular contributors to Perl, including those with write access to the git repository.</p>
<h2>CLONING THE REPOSITORY</h2>
<p> All of Perl&#8217;s source code is kept centrally in a Git repository at <i>perl5.git.perl.org</i>. </p>
<p> You can make a read-only clone of the repository by running: </p>
<pre>
  % git clone <a href="git://perl5.git.perl.org/perl.git">git://perl5.git.perl.org/perl.git</a> perl
</pre>
<p> This uses the git protocol (port 9418). </p>
<p> If you cannot use the git protocol for firewall reasons, you can also clone via http, though this is much slower: </p>
<pre>
  % git clone <a rel="nofollow" href="http://perl5.git.perl.org/perl.git">http://perl5.git.perl.org/perl.git</a> perl
</pre>
<h2>WORKING WITH THE REPOSITORY</h2>
<p> Once you have changed into the repository directory, you can inspect it. After a clone the repository will contain a single local branch, which will be the current branch as well, as indicated by the asterisk. </p>
<pre>
  % git branch
  * blead
</pre>
<p> Using the -a switch to <tt>&quot;branch&quot;</tt> will also show the remote tracking branches in the repository: </p>
<pre>
  % git branch -a
  * blead
    origin/HEAD
    origin/blead
  ...
</pre>
<p> The branches that begin with &#8220;origin&#8221; correspond to the &#8220;git remote&#8221; that you cloned from (which is named &#8220;origin&#8221;). Each branch on the remote will be exactly tracked by these branches. You should <font SIZE="-1">NEVER</font> do work on these remote tracking branches. You only ever do work in a local branch. Local branches can be configured to automerge (on pull) from a designated remote tracking branch. This is the case with the default branch <tt>&quot;blead&quot;</tt> which will be configured to merge from the remote tracking branch <tt>&quot;origin/blead&quot;</tt>. </p>
<p> You can see recent commits: </p>
<pre>
  % git log
</pre>
<p> And pull new changes from the repository, and update your local repository (must be clean first) </p>
<pre>
  % git pull
</pre>
<p> Assuming we are on the branch <tt>&quot;blead&quot;</tt> immediately after a pull, this command would be more or less equivalent to: </p>
<pre>
  % git fetch
  % git merge origin/blead
</pre>
<p> In fact if you want to update your local repository without touching your working directory you do: </p>
<pre>
  % git fetch
</pre>
<p> And if you want to update your remote-tracking branches for all defined remotes simultaneously you can do </p>
<pre>
  % git remote update
</pre>
<p> Neither of these last two commands will update your working directory, however both will update the remote-tracking branches in your repository. </p>
<p> To make a local branch of a remote branch: </p>
<pre>
  % git checkout -b maint-5.10 origin/maint-5.10
</pre>
<p> To switch back to blead: </p>
<pre>
  % git checkout blead
</pre>
<h3>Finding out your status</h3>
<p> The most common git command you will use will probably be </p>
<pre>
  % git status
</pre>
<p> This command will produce as output a description of the current state of the repository, including modified files and unignored untracked files, and in addition it will show things like what files have been staged for the next commit, and usually some useful information about how to change things. For instance the following: </p>
<pre>
 % git status
 On branch blead
 Your branch is ahead of 'origin/blead' by 1 commit.
 Changes to be committed:
   (use &quot;git reset HEAD &lt;file&gt;...&quot; to unstage)
       modified:   pod/perlgit.pod
 Changes not staged for commit:
   (use &quot;git add &lt;file&gt;...&quot; to update what will be committed)
   (use &quot;git checkout -- &lt;file&gt;...&quot; to discard changes in working
                                                              directory)
       modified:   pod/perlgit.pod
 Untracked files:
   (use &quot;git add &lt;file&gt;...&quot; to include in what will be committed)
       deliberate.untracked
</pre>
<p> This shows that there were changes to this document staged for commit, and that there were further changes in the working directory not yet staged. It also shows that there was an untracked file in the working directory, and as you can see shows how to change all of this. It also shows that there is one commit on the working branch <tt>&quot;blead&quot;</tt> which has not been pushed to the <tt>&quot;origin&quot;</tt> remote yet. <font SIZE="-1"><code>NOTE</code></font>: This output is also what you see as a template if you do not provide a message to <tt>&quot;git commit&quot;</tt>.</p>
<h3>Patch workflow</h3>
<p> First, please read perlhack for details on hacking the Perl core. That document covers many details on how to create a good patch. </p>
<p> If you already have a Perl repository, you should ensure that you&#8217;re on the <i>blead</i> branch, and your repository is up to date: </p>
<pre>
  % git checkout blead
  % git pull
</pre>
<p> It&#8217;s preferable to patch against the latest blead version, since this is where new development occurs for all changes other than critical bug fixes. Critical bug fix patches should be made against the relevant maint branches, or should be submitted with a note indicating all the branches where the fix should be applied. </p>
<p> Now that we have everything up to date, we need to create a temporary new branch for these changes and switch into it: </p>
<pre>
  % git checkout -b orange
</pre>
<p> which is the short form of </p>
<pre>
  % git branch orange
  % git checkout orange
</pre>
<p> Creating a topic branch makes it easier for the maintainers to rebase or merge back into the master blead for a more linear history. If you don&#8217;t work on a topic branch the maintainer has to manually cherry pick your changes onto blead before they can be applied. </p>
<p> That&#8217;ll get you scolded on perl5-porters, so don&#8217;t do that. Be Awesome. </p>
<p> Then make your changes. For example, if Leon Brocard changes his name to Orange Brocard, we should change his name in the <font SIZE="-1">AUTHORS</font> file: </p>
<pre><code>
% perl - pi - e 's{Leon Brocard}{Orange Brocard}' AUTHORS
</code></pre>
<p> You can see what files are changed: </p>
<pre>
  % git status
  On branch orange
  Changes to be committed:
    (use &quot;git reset HEAD &lt;file&gt;...&quot; to unstage)
     modified:   AUTHORS
</pre>
<p> And you can see the changes: </p>
<p>% git diff diff&#8211; git a / AUTHORS b / AUTHORS index 293dd70..722c93e 100644 &#8212; -a / AUTHORS++ + b / AUTHORS<br />
                                                                                                    @ @-541,<br />
    7 + 541, 7 @ @Lars Hecking&lt;lhecking[at] nmrc.ucc.ie&gt; Laszlo Molnar&lt;laszlo.molnar[at] eth.ericsson.se&gt; Leif Huhn&lt;leif[at] hale.dkstat.com&gt; Len Johnson&lt;lenjay[at] ibm.net&gt; &#8211; Leon Brocard&lt;acme[at] astray.com&gt; + Orange Brocard&lt;acme[at] astray.com&gt; Les Peters&lt;lpeters[at] aol.net&gt; Lesley Binks&lt;lesley.binks[at] gmail.com&gt; Lincoln D.Stein&lt;lstein[at] cshl.org&gt;</p>
<p> Now commit your change locally: </p>
<pre>
 % git commit -a -m 'Rename Leon Brocard to Orange Brocard'
 Created commit 6196c1d: Rename Leon Brocard to Orange Brocard
  1 files changed, 1 insertions(+), 1 deletions(-)
</pre>
<p> The <tt>&quot;-a&quot;</tt> option is used to include all files that git tracks that you have changed. If at this time, you only want to commit some of the files you have worked on, you can omit the <tt>&quot;-a&quot;</tt> and use the command <tt>&quot;git add </tt>FILE &#8230;<tt>&quot;</tt> before doing the commit. <tt>&quot;git add --interactive&quot;</tt> allows you to even just commit portions of files instead of all the changes in them. </p>
<p> The <tt>&quot;-m&quot;</tt> option is used to specify the commit message. If you omit it, git will open a text editor for you to compose the message interactively. This is useful when the changes are more complex than the sample given here, and, depending on the editor, to know that the first line of the commit message doesn&#8217;t exceed the 50 character legal maximum. </p>
<p> Once you&#8217;ve finished writing your commit message and exited your editor, git will write your change to disk and tell you something like this: </p>
<pre>
 Created commit daf8e63: explain git status and stuff about remotes
  1 files changed, 83 insertions(+), 3 deletions(-)
</pre>
<p> If you re-run <tt>&quot;git status&quot;</tt>, you should see something like this: </p>
<pre>
 % git status
 On branch orange
 Untracked files:
   (use &quot;git add &lt;file&gt;...&quot; to include in what will be committed)
       deliberate.untracked
 nothing added to commit but untracked files present (use &quot;git add&quot; to
                                                                  track)
</pre>
<p> When in doubt, before you do anything else, check your status and read it carefully, many questions are answered directly by the git status output. </p>
<p> You can examine your last commit with: </p>
<pre>
  % git show HEAD
</pre>
<p> and if you are not happy with either the description or the patch itself you can fix it up by editing the files once more and then issue: </p>
<pre>
  % git commit -a --amend
</pre>
<p> Now you should create a patch file for all your local changes: </p>
<pre>
  % git format-patch -M blead..
  0001-Rename-Leon-Brocard-to-Orange-Brocard.patch
</pre>
<p> Or for a lot of changes, e.g. from a topic branch: </p>
<pre>
  % git format-patch --stdout -M blead.. &gt; topic-branch-changes.patch
</pre>
<p> You should now send an email to perlbug [at] perl.org &lt;mailto:perlbug [at] perl.org&gt; with a description of your changes, and include this patch file as an attachment. In addition to being tracked by <font SIZE="-1">RT,</font> mail to perlbug will automatically be forwarded to perl5-porters (with manual moderation, so please be patient). You should only send patches to perl5-porters [at] perl.org &lt;mailto:perl5-porters [at] perl.org&gt; directly if the patch is not ready to be applied, but intended for discussion. </p>
<p> Please do not use <code><a href="/docs/linux/man/1-git-send-email/">git-send-email</a></code>(1) to send your patch. See Sending patch emails for more information. </p>
<p> If you want to delete your temporary branch, you may do so with: </p>
<pre>
 % git checkout blead
 % git branch -d orange
 error: The branch 'orange' is not an ancestor of your current HEAD.
 If you are sure you want to delete it, run 'git branch -D orange'.
 % git branch -D orange
 Deleted branch orange.
</pre>
<h3>Committing your changes</h3>
<p> Assuming that you&#8217;d like to commit all the changes you&#8217;ve made as a single atomic unit, run this command: </p>
<pre>
  % git commit -a
</pre>
<p> (That <tt>&quot;-a&quot;</tt> tells git to add every file you&#8217;ve changed to this commit. New files aren&#8217;t automatically added to your commit when you use <tt>&quot;commit -a&quot;</tt> If you want to add files or to commit some, but not all of your changes, have a look at the documentation for <tt>&quot;git add&quot;</tt>.) </p>
<p> Git will start up your favorite text editor, so that you can craft a commit message for your change. See &#8220;Commit message&#8221; in perlhack for more information about what makes a good commit message. </p>
<p> Once you&#8217;ve finished writing your commit message and exited your editor, git will write your change to disk and tell you something like this: </p>
<pre>
 Created commit daf8e63: explain git status and stuff about remotes
  1 files changed, 83 insertions(+), 3 deletions(-)
</pre>
<p> If you re-run <tt>&quot;git status&quot;</tt>, you should see something like this: </p>
<pre>
 % git status
 On branch blead
 Your branch is ahead of 'origin/blead' by 2 commits.
   (use &quot;git push&quot; to publish your local commits)
 Untracked files:
   (use &quot;git add &lt;file&gt;...&quot; to include in what will be committed)
       deliberate.untracked
 nothing added to commit but untracked files present (use &quot;git add&quot; to
                                                                  track)
</pre>
<p> When in doubt, before you do anything else, check your status and read it carefully, many questions are answered directly by the git status output.</p>
<h3>Sending patch emails</h3>
<p> After you&#8217;ve generated your patch you should send it to perlbug [at] perl.org &lt;mailto:perlbug [at] perl.org&gt; (as discussed in the previous section) with a normal mail client as an attachment, along with a description of the patch. </p>
<p> You <code>must not</code> use <code><a href="/docs/linux/man/1-git-send-email/">git-send-email</a></code>(1) to send patches generated with <code><a href="/docs/linux/man/1-git-format-patch/">git-format-patch</a></code>(1). The <font SIZE="-1">RT</font> ticketing system living behind perlbug [at] perl.org &lt;mailto:perlbug [at] perl.org&gt; does not respect the inline contents of E-Mails, sending an inline patch to <font SIZE="-1">RT</font> guarantees that your patch will be destroyed. </p>
<p> Someone may download your patch from <font SIZE="-1">RT,</font> which will result in the subject (the first line of the commit message) being omitted. See <font SIZE="-1">RT</font> #74192 &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=74192">https://rt.perl.org/Ticket/Display.html?id=74192</a>&gt; and commit a4583001 &lt;<a rel="nofollow" href="http://perl5.git.perl.org/perl.git/commitdiff/a4583001">http://perl5.git.perl.org/perl.git/commitdiff/a4583001</a>&gt; for an example. Alternatively someone may apply your patch from <font SIZE="-1">RT</font> after it arrived in their mailbox, by which time <font SIZE="-1">RT</font> will have modified the inline content of the message. See <font SIZE="-1">RT</font> #74532 &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=74532">https://rt.perl.org/Ticket/Display.html?id=74532</a>&gt; and commit f9bcfeac &lt;<a rel="nofollow" href="http://perl5.git.perl.org/perl.git/commitdiff/f9bcfeac">http://perl5.git.perl.org/perl.git/commitdiff/f9bcfeac</a>&gt; for a bad example of this failure mode.</p>
<h3>A note on derived files</h3>
<p> Be aware that many files in the distribution are derivative&#8212;avoid patching them, because git won&#8217;t see the changes to them, and the build process will overwrite them. Patch the originals instead. Most utilities (like perldoc) are in this category, i.e. patch <i>utils/perldoc.PL</i> rather than <i>utils/perldoc</i>. Similarly, don&#8217;t create patches for files under <i></i>$src_root<i>/ext</i> from their copies found in <i></i>$install_root<i>/lib</i>. If you are unsure about the proper location of a file that may have gotten copied while building the source distribution, consult the <i></i><font SIZE="-1"><i>MANIFEST</i></font><i></i>.</p>
<h3>Cleaning a working directory</h3>
<p> The command <tt>&quot;git clean&quot;</tt> can with varying arguments be used as a replacement for <tt>&quot;make clean&quot;</tt>. </p>
<p> To reset your working directory to a pristine condition you can do: </p>
<pre>
  % git clean -dxf
</pre>
<p> However, be aware this will delete <font SIZE="-1">ALL</font> untracked content. You can use </p>
<pre>
  % git clean -Xf
</pre>
<p> to remove all ignored untracked files, such as build and test byproduct, but leave any manually created files alone. </p>
<p> If you only want to cancel some uncommitted edits, you can use <tt>&quot;git checkout&quot;</tt> and give it a list of files to be reverted, or <tt>&quot;git checkout -f&quot;</tt> to revert them all. </p>
<p> If you want to cancel one or several commits, you can use <tt>&quot;git reset&quot;</tt>.</p>
<h3>Bisecting</h3>
<p> <tt>&quot;git&quot;</tt> provides a built-in way to determine which commit should be blamed for introducing a given bug. <tt>&quot;git bisect&quot;</tt> performs a binary search of history to locate the first failing commit. It is fast, powerful and flexible, but requires some setup and to automate the process an auxiliary shell script is needed. </p>
<p> The core provides a wrapper program, <i>Porting/bisect.pl</i>, which attempts to simplify as much as possible, making bisecting as simple as running a Perl one-liner. For example, if you want to know when this became an error: </p>
<pre>
    perl -e 'my $a := 2'
</pre>
<p> you simply run this: </p>
<pre>
    .../Porting/bisect.pl -e 'my $a := 2;'
</pre>
<p> Using <i>Porting/bisect.pl</i>, with one command (and no other files) it&#8217;s easy to find out</p>
<dl>
<dt>&bull;</p>
<dd> Which commit caused this example code to break?</p>
<dt>&bull;</p>
<dd> Which commit caused this example code to start working?</p>
<dt>&bull;</p>
<dd> Which commit added the first file to match this regex?</p>
<dt>&bull;</p>
<dd> Which commit removed the last file to match this regex?</dl>
<p> usually without needing to know which versions of perl to use as start and end revisions, as <i>Porting/bisect.pl</i> automatically searches to find the earliest stable version for which the test case passes. Run <tt>&quot;Porting/bisect.pl --help&quot;</tt> for the full documentation, including how to set the <tt>&quot;Configure&quot;</tt> and build time options. </p>
<p> If you require more flexibility than <i>Porting/bisect.pl</i> has to offer, you&#8217;ll need to run <tt>&quot;git bisect&quot;</tt> yourself. It&#8217;s most useful to use <tt>&quot;git bisect run&quot;</tt> to automate the building and testing of perl revisions. For this you&#8217;ll need a shell script for <tt>&quot;git&quot;</tt> to call to test a particular revision. An example script is <i>Porting/bisect-example.sh</i>, which you should copy <code>outside</code> of the repository, as the bisect process will reset the state to a clean checkout as it runs. The instructions below assume that you copied it as <i>~/run</i> and then edited it as appropriate. </p>
<p> You first enter in bisect mode with: </p>
<pre>
  % git bisect start
</pre>
<p> For example, if the bug is present on <tt>&quot;HEAD&quot;</tt> but wasn&#8217;t in 5.10.0, <tt>&quot;git&quot;</tt> will learn about this when you enter: </p>
<pre>
  % git bisect bad
  % git bisect good perl-5.10.0
  Bisecting: 853 revisions left to test after this
</pre>
<p> This results in checking out the median commit between <tt>&quot;HEAD&quot;</tt> and <tt>&quot;perl-5.10.0&quot;</tt>. You can then run the bisecting process with: </p>
<pre>
  % git bisect run ~/run
</pre>
<p> When the first bad commit is isolated, <tt>&quot;git bisect&quot;</tt> will tell you so: </p>
<p>ca4cfd28534303b82a216cfe83a1c80cbc3b9dc5 is first bad commit<br />
        commit ca4cfd28534303b82a216cfe83a1c80cbc3b9dc5<br />
            Author : Dave Mitchell&lt;davem[at] fdisolutions.com&gt;<br />
                         Date : Sat Feb 9 14 : 56 : 23 2008 +<br />
                                0000<br />
                                    [perl #49472] Attributes +<br />
                                Unknown Error&#8230; bisect run success</p>
<p> You can peek into the bisecting process with <tt>&quot;git bisect log&quot;</tt> and <tt>&quot;git bisect visualize&quot;</tt>. <tt>&quot;git bisect reset&quot;</tt> will get you out of bisect mode. </p>
<p> Please note that the first <tt>&quot;good&quot;</tt> state must be an ancestor of the first <tt>&quot;bad&quot;</tt> state. If you want to search for the commit that <i>solved</i> some bug, you have to negate your test case (i.e. exit with <tt>1</tt> if <font SIZE="-1">OK</font> and <tt>0</tt> if not) and still mark the lower bound as <tt>&quot;good&quot;</tt> and the upper as <tt>&quot;bad&quot;</tt>. The &#8220;first bad commit&#8221; has then to be understood as the &#8220;first commit where the bug is solved&#8221;. </p>
<p> <tt>&quot;git help bisect&quot;</tt> has much more information on how you can tweak your binary searches. </p>
<p> Following bisection you may wish to configure, build and test perl at commits identified by the bisection process. Sometimes, particularly with older perls, <tt>&quot;make&quot;</tt> may fail during this process. In this case you may be able to patch the source code at the older commit point. To do so, please follow the suggestions provided in &#8220;Building perl at older commits&#8221; in perlhack.</p>
<h3>Topic branches and rewriting history</h3>
<p> Individual committers should create topic branches under <code>yourname</code>/<code>some_descriptive_name</code>: </p>
<pre>
  % branch=&quot;$yourname/$some_descriptive_name&quot;
  % git checkout -b $branch
  ... do local edits, commits etc ...
  % git push origin -u $branch
</pre>
<p> Should you be stuck with an ancient version of git (prior to 1.7), then <tt>&quot;git push&quot;</tt> will not have the <tt>&quot;-u&quot;</tt> switch, and you have to replace the last step with the following sequence: </p>
<pre>
  % git push origin $branch:refs/heads/$branch
  % git config branch.$branch.remote origin
  % git config branch.$branch.merge refs/heads/$branch
</pre>
<p> If you want to make changes to someone else&#8217;s topic branch, you should check with its creator before making any change to it. </p>
<p> You might sometimes find that the original author has edited the branch&#8217;s history. There are lots of good reasons for this. Sometimes, an author might simply be rebasing the branch onto a newer source point. Sometimes, an author might have found an error in an early commit which they wanted to fix before merging the branch to blead. </p>
<p> Currently the master repository is configured to forbid non-fast-forward merges. This means that the branches within can not be rebased and pushed as a single step. </p>
<p> The only way you will ever be allowed to rebase or modify the history of a pushed branch is to delete it and push it as a new branch under the same name. Please think carefully about doing this. It may be better to sequentially rename your branches so that it is easier for others working with you to cherry-pick their local changes onto the new version. (<font SIZE="-1">XXX:</font> needs explanation). </p>
<p> If you want to rebase a personal topic branch, you will have to delete your existing topic branch and push as a new version of it. You can do this via the following formula (see the explanation about <tt>&quot;refspec&quot;</tt>&#8216;s in the git push documentation for details) after you have rebased your branch: </p>
<pre>
  # first rebase
  % git checkout $user/$topic
  % git fetch
  % git rebase origin/blead
  # then &quot;delete-and-push&quot;
  % git push origin :$user/$topic
  % git push origin $user/$topic
</pre>
<p> <font SIZE="-1"><code>NOTE:</code></font> it is forbidden at the repository level to delete any of the &#8220;primary&#8221; branches. That is any branch matching <tt>&quot;m!^(blead|maint|perl)!&quot;</tt>. Any attempt to do so will result in git producing an error like this: </p>
<pre>
  % git push origin :blead
  *** It is forbidden to delete blead/maint branches in this repository
  error: hooks/update exited with error code 1
  error: hook declined to update refs/heads/blead
  To <a href="ssh://perl5.git.perl.org/perl">ssh://perl5.git.perl.org/perl</a>
   ! [remote rejected] blead (hook declined)
   error: failed to push some refs to '<a href="ssh://perl5.git.perl.org/perl'">ssh://perl5.git.perl.org/perl'</a>
</pre>
<p> As a matter of policy we do <code>not</code> edit the history of the blead and maint-* branches. If a typo (or worse) sneaks into a commit to blead or maint-*, we&#8217;ll fix it in another commit. The only types of updates allowed on these branches are &#8220;fast-forwards&#8221;, where all history is preserved. </p>
<p> Annotated tags in the canonical perl.git repository will never be deleted or modified. Think long and hard about whether you want to push a local tag to perl.git before doing so. (Pushing simple tags is not allowed.)</p>
<h3>Grafts</h3>
<p> The perl history contains one mistake which was not caught in the conversion: a merge was recorded in the history between blead and maint-5.10 where no merge actually occurred. Due to the nature of git, this is now impossible to fix in the public repository. You can remove this mis-merge locally by adding the following line to your <tt>&quot;.git/info/grafts&quot;</tt> file: </p>
<pre>
 296f12bbbbaa06de9be9d09d3dcf8f4528898a49 434946e0cb7a32589ed92d18008aaa1d88515930
</pre>
<p> It is particularly important to have this graft line if any bisecting is done in the area of the &#8220;merge&#8221; in question.</p>
<h2>WRITE ACCESS TO THE GIT REPOSITORY</h2>
<p> Once you have write access, you will need to modify the <font SIZE="-1">URL</font> for the origin remote to enable pushing. Edit <i>.git/config</i> with the <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1) command: </p>
<pre>
  % git config remote.origin.url <a href="ssh://perl5.git.perl.org/perl.git">ssh://perl5.git.perl.org/perl.git</a>
</pre>
<p> You can also set up your user name and e-mail address. Most people do this once globally in their <i>~/.gitconfig</i> by doing something like: </p>
<p>% git config&#8211; global user.name &#8220;Ævar Arnfjörð Bjarmason&#8221; % git config&#8211; global user.email avarab[at] gmail.com</p>
<p> However, if you&#8217;d like to override that just for perl, execute something like the following in <i>perl</i>: </p>
<pre>
  % git config user.email avar [at] cpan.org
</pre>
<p> It is also possible to keep <tt>&quot;origin&quot;</tt> as a git remote, and add a new remote for ssh access: </p>
<pre>
  % git remote add camel perl5.git.perl.org:/perl.git
</pre>
<p> This allows you to update your local repository by pulling from <tt>&quot;origin&quot;</tt>, which is faster and doesn&#8217;t require you to authenticate, and to push your changes back with the <tt>&quot;camel&quot;</tt> remote: </p>
<pre>
  % git fetch camel
  % git push camel
</pre>
<p> The <tt>&quot;fetch&quot;</tt> command just updates the <tt>&quot;camel&quot;</tt> refs, as the objects themselves should have been fetched when pulling from <tt>&quot;origin&quot;</tt>.</p>
<h3>Accepting a patch</h3>
<p> If you have received a patch file generated using the above section, you should try out the patch. </p>
<p> First we need to create a temporary new branch for these changes and switch into it: </p>
<pre>
 % git checkout -b experimental
</pre>
<p> Patches that were formatted by <tt>&quot;git format-patch&quot;</tt> are applied with <tt>&quot;git am&quot;</tt>: </p>
<pre>
 % git am 0001-Rename-Leon-Brocard-to-Orange-Brocard.patch
 Applying Rename Leon Brocard to Orange Brocard
</pre>
<p> Note that some <font SIZE="-1">UNIX</font> mail systems can mess with text attachments containing &#8216;From &#8216;. This will fix them up: </p>
<pre>
 % perl -pi -e's/^&gt;From /From /' \
                        0001-Rename-Leon-Brocard-to-Orange-Brocard.patch
</pre>
<p> If just a raw diff is provided, it is also possible use this two-step process: </p>
<pre>
 % git apply bugfix.diff
 % git commit -a -m &quot;Some fixing&quot; \
                            --author=&quot;That Guy &lt;that.guy [at] internets.com&gt;&quot;
</pre>
<p> Now we can inspect the change: </p>
<p>% git show HEAD<br />
            commit b1b3dab48344cff6de4087efca3dbd63548ab5e2<br />
                Author : Leon Brocard&lt;acme[at] astray.com&gt;<br />
                             Date : Fri Dec 19 17 : 02 : 59 2008 +<br />
    0000 Rename Leon Brocard to Orange Brocard<br />
            diff&#8211; git a /<br />
        AUTHORS b / AUTHORS index 293dd70..722c93e 100644 &#8212; -a / AUTHORS++ +<br />
    b / AUTHORS<br />
        @ @-541,<br />
    7 + 541, 7 @ @Lars Hecking&lt;lhecking[at] nmrc.ucc.ie&gt; Laszlo Molnar&lt;laszlo.molnar[at] eth.ericsson.se&gt; Leif Huhn&lt;leif[at] hale.dkstat.com&gt; Len Johnson&lt;lenjay[at] ibm.net&gt; &#8211; Leon Brocard&lt;acme[at] astray.com&gt; + Orange Brocard&lt;acme[at] astray.com&gt; Les Peters&lt;lpeters[at] aol.net&gt; Lesley Binks&lt;lesley.binks[at] gmail.com&gt; Lincoln D.Stein&lt;lstein[at] cshl.org&gt;</p>
<p> If you are a committer to Perl and you think the patch is good, you can then merge it into blead then push it out to the main repository: </p>
<pre>
  % git checkout blead
  % git merge experimental
  % git push origin blead
</pre>
<p> If you want to delete your temporary branch, you may do so with: </p>
<pre>
 % git checkout blead
 % git branch -d experimental
 error: The branch 'experimental' is not an ancestor of your current
 HEAD.  If you are sure you want to delete it, run 'git branch -D
 experimental'.
 % git branch -D experimental
 Deleted branch experimental.
</pre>
<h3>Committing to blead</h3>
<p> The &#8216;blead&#8217; branch will become the next production release of Perl. </p>
<p> Before pushing <i>any</i> local change to blead, it&#8217;s incredibly important that you do a few things, lest other committers come after you with pitchforks and torches:</p>
<dl>
<dt>&bull;</p>
<dd> Make sure you have a good commit message. See &#8220;Commit message&#8221; in perlhack for details.</p>
<dt>&bull;</p>
<dd> Run the test suite. You might not think that one typo fix would break a test file. You&#8217;d be wrong. Here&#8217;s an example of where not running the suite caused problems. A patch was submitted that added a couple of tests to an existing <i>.t</i>. It couldn&#8217;t possibly affect anything else, so no need to test beyond the single affected <i>.t</i>, right? But, the submitter&#8217;s email address had changed since the last of their submissions, and this caused other tests to fail. Running the test target given in the next item would have caught this problem.</p>
<dt>&bull;</p>
<dd> If you don&#8217;t run the full test suite, at least <tt>&quot;make test_porting&quot;</tt>. This will run basic sanity checks. To see which sanity checks, have a look in <i>t/porting</i>.</p>
<dt>&bull;</p>
<dd> If you make any changes that affect miniperl or core routines that have different code paths for miniperl, be sure to run <tt>&quot;make minitest&quot;</tt>. This will catch problems that even the full test suite will not catch because it runs a subset of tests under miniperl rather than perl.</dl>
<h3>On merging and rebasing</h3>
<p> Simple, one-off commits pushed to the &#8216;blead&#8217; branch should be simple commits that apply cleanly. In other words, you should make sure your work is committed against the current position of blead, so that you can push back to the master repository without merging. </p>
<p> Sometimes, blead will move while you&#8217;re building or testing your changes. When this happens, your push will be rejected with a message like this: </p>
<pre><code>
 To ssh://perl5.git.perl.org/perl.git
  ! [rejected]        blead -&gt; blead (non-fast-forward)
 error: failed to push some refs to 'ssh://perl5.git.perl.org/perl.git'
 To prevent you from losing history, non-fast-forward updates were
 rejected Merge the remote changes (e.g. 'git pull') before pushing
 again.  See the 'Note about fast-forwards' section of 'git push --help'
 for details.
</code></pre>
<p> When this happens, you can just <i>rebase</i> your work against the new position of blead, like this (assuming your remote for the master repository is &#8220;p5p&#8221;): </p>
<pre>
  % git fetch p5p
  % git rebase p5p/blead
</pre>
<p> You will see your commits being re-applied, and you will then be able to push safely. More information about rebasing can be found in the documentation for the <code><a href="/docs/linux/man/1-git-rebase/">git-rebase</a></code>(1) command. </p>
<p> For larger sets of commits that only make sense together, or that would benefit from a summary of the set&#8217;s purpose, you should use a merge commit. You should perform your work on a topic branch, which you should regularly rebase against blead to ensure that your code is not broken by blead moving. When you have finished your work, please perform a final rebase and test. Linear history is something that gets lost with every commit on blead, but a final rebase makes the history linear again, making it easier for future maintainers to see what has happened. Rebase as follows (assuming your work was on the branch <tt>&quot;committer/somework&quot;</tt>): </p>
<pre>
  % git checkout committer/somework
  % git rebase blead
</pre>
<p> Then you can merge it into master like this: </p>
<pre>
  % git checkout blead
  % git merge --no-ff --no-commit committer/somework
  % git commit -a
</pre>
<p> The switches above deserve explanation. <tt>&quot;--no-ff&quot;</tt> indicates that even if all your work can be applied linearly against blead, a merge commit should still be prepared. This ensures that all your work will be shown as a side branch, with all its commits merged into the mainstream blead by the merge commit. </p>
<p> <tt>&quot;--no-commit&quot;</tt> means that the merge commit will be <i>prepared</i> but not <i>committed</i>. The commit is then actually performed when you run the next command, which will bring up your editor to describe the commit. Without <tt>&quot;--no-commit&quot;</tt>, the commit would be made with nearly no useful message, which would greatly diminish the value of the merge commit as a placeholder for the work&#8217;s description. </p>
<p> When describing the merge commit, explain the purpose of the branch, and keep in mind that this description will probably be used by the eventual release engineer when reviewing the next perldelta document.</p>
<h3>Committing to maintenance versions</h3>
<p> Maintenance versions should only be altered to add critical bug fixes, see perlpolicy. </p>
<p> To commit to a maintenance version of perl, you need to create a local tracking branch: </p>
<pre>
  % git checkout --track -b maint-5.005 origin/maint-5.005
</pre>
<p> This creates a local branch named <tt>&quot;maint-5.005&quot;</tt>, which tracks the remote branch <tt>&quot;origin/maint-5.005&quot;</tt>. Then you can pull, commit, merge and push as before. </p>
<p> You can also cherry-pick commits from blead and another branch, by using the <tt>&quot;git cherry-pick&quot;</tt> command. It is recommended to use the <code>-x</code> option to <tt>&quot;git cherry-pick&quot;</tt> in order to record the <font SIZE="-1">SHA1</font> of the original commit in the new commit message. </p>
<p> Before pushing any change to a maint version, make sure you&#8217;ve satisfied the steps in &#8220;Committing to blead&#8221; above.</p>
<h3>Merging from a branch via GitHub</h3>
<p> While we don&#8217;t encourage the submission of patches via GitHub, that will still happen. Here is a guide to merging patches from a GitHub repository. </p>
<pre>
  % git remote add avar <a href="git://github.com/avar/perl.git">git://github.com/avar/perl.git</a>
  % git fetch avar
</pre>
<p> Now you can see the differences between the branch and blead: </p>
<pre>
  % git diff avar/orange
</pre>
<p> And you can see the commits: </p>
<pre>
  % git log avar/orange
</pre>
<p> If you approve of a specific commit, you can cherry pick it: </p>
<pre>
  % git cherry-pick 0c24b290ae02b2ab3304f51d5e11e85eb3659eae
</pre>
<p> Or you could just merge the whole branch if you like it all: </p>
<pre>
  % git merge avar/orange
</pre>
<p> And then push back to the repository: </p>
<pre>
  % git push origin blead
</pre>
<h3>Using a smoke-me branch to test changes</h3>
<p> Sometimes a change affects code paths which you cannot test on the OSes which are directly available to you and it would be wise to have users on other OSes test the change before you commit it to blead. </p>
<p> Fortunately, there is a way to get your change smoke-tested on various OSes: push it to a &#8220;smoke-me&#8221; branch and wait for certain automated smoke-testers to report the results from their OSes. A &#8220;smoke-me&#8221; branch is identified by the branch name: specifically, as seen on perl5.git.perl.org it must be a local branch whose first name component is precisely <tt>&quot;smoke-me&quot;</tt>. </p>
<p> The procedure for doing this is roughly as follows (using the example of of tonyc&#8217;s smoke-me branch called win32stat): </p>
<p> First, make a local branch and switch to it: </p>
<pre>
  % git checkout -b win32stat
</pre>
<p> Make some changes, build perl and test your changes, then commit them to your local branch. Then push your local branch to a remote smoke-me branch: </p>
<pre>
  % git push origin win32stat:smoke-me/tonyc/win32stat
</pre>
<p> Now you can switch back to blead locally: </p>
<pre>
  % git checkout blead
</pre>
<p> and continue working on other things while you wait a day or two, keeping an eye on the results reported for your smoke-me branch at &lt;<a rel="nofollow" href="http://perl.develop-help.com/?b=smoke-me/tonyc/win32state">http://perl.develop-help.com/?b=smoke-me/tonyc/win32state</a>&gt;. </p>
<p> If all is well then update your blead branch: </p>
<pre>
  % git pull
</pre>
<p> then checkout your smoke-me branch once more and rebase it on blead: </p>
<pre>
  % git rebase blead win32stat
</pre>
<p> Now switch back to blead and merge your smoke-me branch into it: </p>
<pre>
  % git checkout blead
  % git merge win32stat
</pre>
<p> As described earlier, if there are many changes on your smoke-me branch then you should prepare a merge commit in which to give an overview of those changes by using the following command instead of the last command above: </p>
<pre>
  % git merge win32stat --no-ff --no-commit
</pre>
<p> You should now build perl and test your (merged) changes one last time (ideally run the whole test suite, but failing that at least run the <i>t/porting/*.t</i> tests) before pushing your changes as usual: </p>
<pre>
  % git push origin blead
</pre>
<p> Finally, you should then delete the remote smoke-me branch: </p>
<pre>
  % git push origin :smoke-me/tonyc/win32stat
</pre>
<p> (which is likely to produce a warning like this, which can be ignored: </p>
<pre>
 remote: fatal: ambiguous argument
                                  'refs/heads/smoke-me/tonyc/win32stat':
 unknown revision or path not in the working tree.
 remote: Use '--' to separate paths from revisions
</pre>
<p> ) and then delete your local branch: </p>
<pre>
  % git branch -d win32stat
</pre>
<h3>A note on camel and dromedary</h3>
<p> The committers have <font SIZE="-1">SSH</font> access to the two servers that serve <tt>&quot;perl5.git.perl.org&quot;</tt>. One is <tt>&quot;perl5.git.perl.org&quot;</tt> itself (<i>camel</i>), which is the &#8216;master&#8217; repository. The second one is <tt>&quot;users.perl5.git.perl.org&quot;</tt> (<i>dromedary</i>), which can be used for general testing and development. Dromedary syncs the git tree from camel every few minutes, you should not push there. Both machines also have a full <font SIZE="-1">CPAN</font> mirror in <i>/srv/CPAN</i>, please use this. To share files with the general public, dromedary serves your <i>~/public_html/</i> as <tt>&quot;&lt;<a rel="nofollow" href="http://users.perl5.git.perl.org/~yourlogin/">http://users.perl5.git.perl.org/~yourlogin/</a>&gt;&quot;</tt> </p>
<p> These hosts have fairly strict firewalls to the outside. Outgoing, only rsync, ssh and git are allowed. For http and ftp, you can use &lt;<a rel="nofollow" href="http://webproxy:3128">http://webproxy:3128</a>&gt; as proxy. Incoming, the firewall tries to detect attacks and blocks <font SIZE="-1">IP</font> addresses with suspicious activity. This sometimes (but very rarely) has false positives and you might get blocked. The quickest way to get unblocked is to notify the admins. </p>
<p> These two boxes are owned, hosted, and operated by booking.com. You can reach the sysadmins in #p5p on irc.perl.org or via mail to perl5-porters [at] perl.org &lt;mailto:perl5-porters [at] perl.org&gt;. </p>
<h2>Index</h2>

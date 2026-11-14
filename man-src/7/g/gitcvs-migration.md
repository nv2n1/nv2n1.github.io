---
title: "gitcvs-migration(7)"
name: "gitcvs-migration"
section: "7"
letter: "g"
url: "/docs/linux/man/7-gitcvs-migration/"
description: "gitcvs-migration – Git for CVS users"
---

<p>gitcvs-migration &#8211; Git for CVS users</p>
<h2>Synopsis</h2>
<pre><i>git cvsimport</i> *</pre>
<h2>Description</h2>
<p>Git differs from CVS in that every working tree contains a repository with a full copy of the project history, and no repository is inherently more important than any other. However, you can emulate the CVS model by designating a single shared repository which people can synchronize with; this document explains how to do that. </p>
<p> Some basic familiarity with Git is required. Having gone through <code><a href="/docs/linux/man/7-gittutorial/">gittutorial</a></code>(7) and <code><a href="/docs/linux/man/7-gitglossary/">gitglossary</a></code>(7) should be sufficient.</p>
<h2>Developing Against A Shared Repository</h2>
<p>Suppose a shared repository is set up in /pub/repo.git on the host foo.com. Then as an individual committer you can clone the shared repository over ssh with: </p>
<dl>
<dd>
<pre>$ git clone foo.com:/pub/repo.git/ my-project
$ cd my-project</pre>
</dl>
<p> and hack away. The equivalent of <i>cvs update</i> is </p>
<dl>
<dd>
<pre>$ git pull origin</pre>
</dl>
<p> which merges in any work that others might have done since the clone operation. If there are uncommitted changes in your working tree, commit them first before running git pull. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> The <i>pull</i> command knows where to get updates from because of certain configuration variables that were set by the first <i>git clone</i> command; see <code>git config -l</code> and the <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1) man page for details. </p>
</dl>
<p> You can update the shared repository with your changes by first committing your changes, and then using the <i>git push</i> command: </p>
<dl>
<dd>
<pre>$ git push origin master</pre>
</dl>
<p> to &quot;push&quot; those commits to the shared repository. If someone else has updated the repository more recently, <i>git push</i>, like <i>cvs commit</i>, will complain, in which case you must pull any changes before attempting the push again. </p>
<p> In the <i>git push</i> command above we specify the name of the remote branch to update (<code>master</code>). If we leave that out, <i>git push</i> tries to update any branches in the remote repository that have the same name as a branch in the local repository. So the last <i>push</i> can be done with either of: </p>
<dl>
<dd>
<pre>$ git push origin
$ git push foo.com:/pub/project.git/</pre>
</dl>
<p> as long as the shared repository does not have any branches other than <code>master</code>.</p>
<h2>Setting Up A Shared Repository</h2>
<p>We assume you have already created a Git repository for your project, possibly created from scratch or from a tarball (see <code><a href="/docs/linux/man/7-gittutorial/">gittutorial</a></code>(7)), or imported from an already existing CVS repository (see the next section). </p>
<p> Assume your existing repo is at /home/alice/myproject. Create a new &quot;bare&quot; repository (a repository without a working tree) and fetch your project into it: </p>
<dl>
<dd>
<pre>$ mkdir /pub/my-repo.git
$ cd /pub/my-repo.git
$ git --bare init --shared
$ git --bare fetch /home/alice/myproject master:master</pre>
</dl>
<p> Next, give every team member read/write access to this repository. One easy way to do this is to give all the team members ssh access to the machine where the repository is hosted. If you don&#8217;t want to give them a full shell on the machine, there is a restricted shell which only allows users to do Git pushes and pulls; see <code><a href="/docs/linux/man/1-git-shell/">git-shell</a></code>(1). </p>
<p> Put all the committers in the same group, and make the repository writable by that group: </p>
<dl>
<dd>
<pre>$ chgrp -R $group /pub/my-repo.git</pre>
</dl>
<p> Make sure committers have a umask of at most 027, so that the directories they create are writable and searchable by other group members.</p>
<h2>Importing A Cvs Archive</h2>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> These instructions use the <code>git-cvsimport</code> script which ships with git, but other importers may provide better results. See the note in <code><a href="/docs/linux/man/1-git-cvsimport/">git-cvsimport</a></code>(1) for other options. </p>
</dl>
<p> First, install version 2.1 or higher of cvsps from m[blue]<code><a rel="nofollow" href="https://github.com/andreyvit/cvsps">https://github.com/andreyvit/cvsps</a></code>m[] and make sure it is in your path. Then cd to a checked out CVS working directory of the project you are interested in and run <code><a href="/docs/linux/man/1-git-cvsimport/">git-cvsimport</a></code>(1): </p>
<dl>
<dd>
<pre>$ git cvsimport -C &lt;destination&gt; &lt;module&gt;</pre>
</dl>
<p> This puts a Git archive of the named CVS module in the directory &lt;destination&gt;, which will be created if necessary. </p>
<p> The import checks out from CVS every revision of every file. Reportedly cvsimport can average some twenty revisions per second, so for a medium-sized project this should not take more than a couple of minutes. Larger projects or remote repositories may take longer. </p>
<p> The main trunk is stored in the Git branch named <code>origin</code>, and additional CVS branches are stored in Git branches with the same names. The most recent version of the main trunk is also left checked out on the <code>master</code> branch, so you can start adding your own changes right away. </p>
<p> The import is incremental, so if you call it again next month it will fetch any CVS updates that have been made in the meantime. For this to work, you must not modify the imported branches; instead, create new branches for your own changes, and merge in the imported branches as necessary. </p>
<p> If you want a shared repository, you will need to make a bare clone of the imported directory, as described above. Then treat the imported directory as another development clone for purposes of merging incremental imports.</p>
<h2>Advanced Shared Repository Management</h2>
<p>Git allows you to specify scripts called &quot;hooks&quot; to be run at certain points. You can use these, for example, to send all commits to the shared repository to a mailing list. See <code><a href="/docs/linux/man/5-githooks/">githooks</a></code>(5). </p>
<p> You can enforce finer grained permissions using update hooks. See m[blue]<code>Controlling access to branches using update hooks</code>m[]<font SIZE="-2">[1]</font>.</p>
<h2>Providing Cvs Access To A Git Repository</h2>
<p>It is also possible to provide true CVS access to a Git repository, so that developers can still use CVS; see <code><a href="/docs/linux/man/1-git-cvsserver/">git-cvsserver</a></code>(1) for details.</p>
<h2>Alternative Development Models</h2>
<p>CVS users are accustomed to giving a group of developers commit access to a common repository. As we&#8217;ve seen, this is also possible with Git. However, the distributed nature of Git allows other development models, and you may want to first consider whether one of them might be a better fit for your project. </p>
<p> For example, you can choose a single person to maintain the project&#8217;s primary public repository. Other developers then clone this repository and each work in their own clone. When they have a series of changes that they&#8217;re happy with, they ask the maintainer to pull from the branch containing the changes. The maintainer reviews their changes and pulls them into the primary repository, which other developers pull from as necessary to stay coordinated. The Linux kernel and other projects use variants of this model. </p>
<p> With a small group, developers may just pull changes from each other&#8217;s repositories without the need for a central maintainer.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-gittutorial/">gittutorial</a></code>(7), <code><a href="/docs/linux/man/7-gittutorial-2/">gittutorial-2</a></code>(7), <code><a href="/docs/linux/man/7-gitcore-tutorial/">gitcore-tutorial</a></code>(7), <code><a href="/docs/linux/man/7-gitglossary/">gitglossary</a></code>(7), <code><a href="/docs/linux/man/7-giteveryday/">giteveryday</a></code>(7), m[blue]<code>The Git User&#8217;s Manual</code>m[]<font SIZE="-2">[2]</font></p>
<h2>Git</h2>
<p>Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>Controlling access to branches using update hooks</p>
<dl>
<dd>file:///usr/share/doc/git/html/howto/update-hook-example.html</dl>
<dt> 2.</p>
<dd>The Git User&#8217;s Manual</p>
<dl>
<dd>file:///usr/share/doc/git/html/user-manual.html</dl>

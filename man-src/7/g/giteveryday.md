---
title: "giteveryday(7)"
name: "giteveryday"
section: "7"
letter: "g"
url: "/docs/linux/man/7-giteveryday/"
description: "giteveryday – A useful minimum set of commands for Everyday Git"
---

<p>giteveryday &#8211; A useful minimum set of commands for Everyday Git</p>
<h2>Synopsis</h2>
<p>Everyday Git With 20 Commands Or So</p>
<h2>Description</h2>
<p>Git users can broadly be grouped into four categories for the purposes of describing here a small set of useful command for everyday Git. </p>
<dl>
<dd>&bull; Individual Developer (Standalone) commands are essential for anybody who makes a commit, even for somebody who works alone.</dl>
<dl>
<dd>&bull; If you work with other people, you will need commands listed in the Individual Developer (Participant) section as well.</dl>
<dl>
<dd>&bull; People who play the Integrator role need to learn some more commands in addition to the above.</dl>
<dl>
<dd>&bull; Repository Administration commands are for system administrators who are responsible for the care and feeding of Git repositories.</dl>
<h2>Individual Developer (Standalone)</h2>
<p>A standalone individual developer does not exchange patches with other people, and works alone in a single repository, using the following commands. </p>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/1-git-init/">git-init</a></code>(1) to create a new repository.</dl>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1) to see what happened.</dl>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/1-git-switch/">git-switch</a></code>(1) and <code><a href="/docs/linux/man/1-git-branch/">git-branch</a></code>(1) to switch branches.</dl>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/1-git-add/">git-add</a></code>(1) to manage the index file.</dl>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/1-git-diff/">git-diff</a></code>(1) and <code><a href="/docs/linux/man/1-git-status/">git-status</a></code>(1) to see what you are in the middle of doing.</dl>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/1-git-commit/">git-commit</a></code>(1) to advance the current branch.</dl>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/1-git-restore/">git-restore</a></code>(1) to undo changes.</dl>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/1-git-merge/">git-merge</a></code>(1) to merge between local branches.</dl>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/1-git-rebase/">git-rebase</a></code>(1) to maintain topic branches.</dl>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/1-git-tag/">git-tag</a></code>(1) to mark a known point.</dl>
<h3>Examples</h3>
<p>Use a tarball as a starting point for a new repository.</p>
<dl>
<dd>
<dl>
<dd>
<pre>$ tar zxf frotz.tar.gz
$ cd frotz
$ git init
$ git add . <code>(1)</code>
$ git commit -m &quot;import of frotz source tree.&quot;
$ git tag v2.43 <code>(2)</code></pre>
</dl>
<p> <code>1. </code>add everything under the current directory.<br />
 <code>2. </code>make a lightweight, unannotated tag.
</dl>
<p> Create a topic branch and develop.</p>
<dl>
<dd>
<dl>
<dd>
<pre>$ git switch -c alsa-audio <code>(1)</code>
$ edit/compile/test
$ git restore curses/ux_audio_oss.c <code>(2)</code>
$ git add curses/ux_audio_alsa.c <code>(3)</code>
$ edit/compile/test
$ git diff HEAD <code>(4)</code>
$ git commit -a -s <code>(5)</code>
$ edit/compile/test
$ git diff HEAD^ <code>(6)</code>
$ git commit -a --amend <code>(7)</code>
$ git switch master <code>(8)</code>
$ git merge alsa-audio <code>(9)</code>
$ git log --since='3 days ago' <code>(10)</code>
$ git log v2.43.. curses/ <code>(11)</code></pre>
</dl>
<p> <code>1. </code>create a new topic branch.<br />
 <code>2. </code>revert your botched changes in <code>curses/ux_audio_oss.c</code>.<br />
 <code>3. </code>you need to tell Git if you added a new file; removal and modification will be caught if you do <code>git commit -a</code> later.<br />
 <code>4. </code>to see what changes you are committing.<br />
 <code>5. </code>commit everything, as you have tested, with your sign-off.<br />
 <code>6. </code>look at all your changes including the previous commit.<br />
 <code>7. </code>amend the previous commit, adding all your new changes, using your original message.<br />
 <code>8. </code>switch to the master branch.<br />
 <code>9. </code>merge a topic branch into your master branch.<br />
 <code>10. </code>review commit logs; other forms to limit output can be combined and include <code>-10</code> (to show up to 10 commits), <code>&#8211;until=2005-12-10</code>, etc.<br />
 <code>11. </code>view only the changes that touch what&#8217;s in <code>curses/</code> directory, since <code>v2.43</code> tag.
</dl>
<h2>Individual Developer (Participant)</h2>
<p>A developer working as a participant in a group project needs to learn how to communicate with others, and uses these commands in addition to the ones needed by a standalone developer. </p>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/1-git-clone/">git-clone</a></code>(1) from the upstream to prime your local repository.</dl>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/1-git-pull/">git-pull</a></code>(1) and <code><a href="/docs/linux/man/1-git-fetch/">git-fetch</a></code>(1) from &quot;origin&quot; to keep up-to-date with the upstream.</dl>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/1-git-push/">git-push</a></code>(1) to shared repository, if you adopt CVS style shared repository workflow.</dl>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/1-git-format-patch/">git-format-patch</a></code>(1) to prepare e-mail submission, if you adopt Linux kernel-style public forum workflow.</dl>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/1-git-send-email/">git-send-email</a></code>(1) to send your e-mail submission without corruption by your MUA.</dl>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/1-git-request-pull/">git-request-pull</a></code>(1) to create a summary of changes for your upstream to pull.</dl>
<h3>Examples</h3>
<p>Clone the upstream and work on it. Feed changes to upstream.</p>
<dl>
<dd>
<dl>
<dd>
<pre>$ git clone <a href="git://git.kernel.org/pub/scm/.../torvalds/linux-2.6">git://git.kernel.org/pub/scm/.../torvalds/linux-2.6</a> my2.6
$ cd my2.6
$ git switch -c mine master <code>(1)</code>
$ edit/compile/test; git commit -a -s <code>(2)</code>
$ git format-patch master <code>(3)</code>
$ git send-email --to=&quot;person &lt;email [at] example.com&gt;&quot; 00*.patch <code>(4)</code>
$ git switch master <code>(5)</code>
$ git pull <code>(6)</code>
$ git log -p ORIG_HEAD.. arch/i386 include/asm-i386 <code>(7)</code>
$ git ls-remote --heads <a rel="nofollow" href="http://git.kernel.org/.../jgarzik/libata-dev.git">http://git.kernel.org/.../jgarzik/libata-dev.git</a> <code>(8)</code>
$ git pull <a href="git://git.kernel.org/pub/.../jgarzik/libata-dev.git">git://git.kernel.org/pub/.../jgarzik/libata-dev.git</a> ALL <code>(9)</code>
$ git reset --hard ORIG_HEAD <code>(10)</code>
$ git gc <code>(11)</code></pre>
</dl>
<p> <code>1. </code>checkout a new branch <code>mine</code> from master.<br />
 <code>2. </code>repeat as needed.<br />
 <code>3. </code>extract patches from your branch, relative to master,<br />
 <code>4. </code>and email them.<br />
 <code>5. </code>return to <code>master</code>, ready to see what&#8217;s new<br />
 <code>6. </code><code>git pull</code> fetches from <code>origin</code> by default and merges into the current branch.<br />
 <code>7. </code>immediately after pulling, look at the changes done upstream since last time we checked, only in the area we are interested in.<br />
 <code>8. </code>check the branch names in an external repository (if not known).<br />
 <code>9. </code>fetch from a specific branch <code>ALL</code> from a specific repository and merge it.<br />
 <code>10. </code>revert the pull.<br />
 <code>11. </code>garbage collect leftover objects from reverted pull.
</dl>
<p> Push into another repository.</p>
<dl>
<dd>
<dl>
<dd>
<pre>satellite$ git clone mothership:frotz frotz <code>(1)</code>
satellite$ cd frotz
satellite$ git config --get-regexp '^(remote|branch)\.' <code>(2)</code>
remote.origin.url mothership:frotz
remote.origin.fetch refs/heads/*:refs/remotes/origin/*
branch.master.remote origin
branch.master.merge refs/heads/master
satellite$ git config remote.origin.push \
 +refs/heads/*:refs/remotes/satellite/* <code>(3)</code>
satellite$ edit/compile/test/commit
satellite$ git push origin <code>(4)</code>
mothership$ cd frotz
mothership$ git switch master
mothership$ git merge satellite/master <code>(5)</code></pre>
</dl>
<p> <code>1. </code>mothership machine has a frotz repository under your home directory; clone from it to start a repository on the satellite machine.<br />
 <code>2. </code>clone sets these configuration variables by default. It arranges <code>git pull</code> to fetch and store the branches of mothership machine to local <code>remotes/origin/*</code> remote-tracking branches.<br />
 <code>3. </code>arrange <code>git push</code> to push all local branches to their corresponding branch of the mothership machine.<br />
 <code>4. </code>push will stash all our work away on <code>remotes/satellite/*</code> remote-tracking branches on the mothership machine. You could use this as a back-up method. Likewise, you can pretend that mothership &quot;fetched&quot; from you (useful when access is one sided).<br />
 <code>5. </code>on mothership machine, merge the work done on the satellite machine into the master branch.
</dl>
<p> Branch off of a specific tag.</p>
<dl>
<dd>
<dl>
<dd>
<pre>$ git switch -c private2.6.14 v2.6.14 <code>(1)</code>
$ edit/compile/test; git commit -a
$ git checkout master
$ git cherry-pick v2.6.14..private2.6.14 <code>(2)</code></pre>
</dl>
<p> <code>1. </code>create a private branch based on a well known (but somewhat behind) tag.<br />
 <code>2. </code>forward port all changes in <code>private2.6.14</code> branch to <code>master</code> branch without a formal &quot;merging&quot;. Or longhand </p>
<p> <code>git format-patch -k -m &#8211;stdout v2.6.14..private2.6.14 | git am -3 -k</code>
</dl>
<p> An alternate participant submission mechanism is using the <code>git request-pull</code> or pull-request mechanisms (e.g as used on GitHub (<a rel="nofollow" href="http://www.github.com">www.github.com</a>) to notify your upstream of your contribution.</p>
<h2>Integrator</h2>
<p>A fairly central person acting as the integrator in a group project receives changes made by others, reviews and integrates them and publishes the result for others to use, using these commands in addition to the ones needed by participants. </p>
<p> This section can also be used by those who respond to <code>git request-pull</code> or pull-request on GitHub (<a rel="nofollow" href="http://www.github.com">www.github.com</a>) to integrate the work of others into their history. A sub-area lieutenant for a repository will act both as a participant and as an integrator. </p>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/1-git-am/">git-am</a></code>(1) to apply patches e-mailed in from your contributors.</dl>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/1-git-pull/">git-pull</a></code>(1) to merge from your trusted lieutenants.</dl>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/1-git-format-patch/">git-format-patch</a></code>(1) to prepare and send suggested alternative to contributors.</dl>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/1-git-revert/">git-revert</a></code>(1) to undo botched commits.</dl>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/1-git-push/">git-push</a></code>(1) to publish the bleeding edge.</dl>
<h3>Examples</h3>
<p>A typical integrator&#8217;s Git day.</p>
<dl>
<dd>
<dl>
<dd>
<pre>$ git status <code>(1)</code>
$ git branch --no-merged master <code>(2)</code>
$ mailx <code>(3)</code>
&amp; s 2 3 4 5 ./+to-apply
&amp; s 7 8 ./+hold-linus
&amp; q
$ git switch -c topic/one master
$ git am -3 -i -s ./+to-apply <code>(4)</code>
$ compile/test
$ git switch -c hold/linus &amp;&amp; git am -3 -i -s ./+hold-linus <code>(5)</code>
$ git switch topic/one &amp;&amp; git rebase master <code>(6)</code>
$ git switch -C seen next <code>(7)</code>
$ git merge topic/one topic/two &amp;&amp; git merge hold/linus <code>(8)</code>
$ git switch maint
$ git cherry-pick master~4 <code>(9)</code>
$ compile/test
$ git tag -s -m &quot;GIT 0.99.9x&quot; v0.99.9x <code>(10)</code>
$ git fetch ko &amp;&amp; for branch in master maint next seen <code>(11)</code>
 do
 git show-branch ko/$branch $branch <code>(12)</code>
 done
$ git push --follow-tags ko <code>(13)</code></pre>
</dl>
<p> <code>1. </code>see what you were in the middle of doing, if anything.<br />
 <code>2. </code>see which branches haven&#8217;t been merged into <code>master</code> yet. Likewise for any other integration branches e.g. <code>maint</code>, <code>next</code> and <code>seen</code>.<br />
 <code>3. </code>read mails, save ones that are applicable, and save others that are not quite ready (other mail readers are available).<br />
 <code>4. </code>apply them, interactively, with your sign-offs.<br />
 <code>5. </code>create topic branch as needed and apply, again with sign-offs.<br />
 <code>6. </code>rebase internal topic branch that has not been merged to the master or exposed as a part of a stable branch.<br />
 <code>7. </code>restart <code>seen</code> every time from the next.<br />
 <code>8. </code>and bundle topic branches still cooking.<br />
 <code>9. </code>backport a critical fix.<br />
 <code>10. </code>create a signed tag.<br />
 <code>11. </code>make sure master was not accidentally rewound beyond that already pushed out.<br />
 <code>12. </code>In the output from <code>git show-branch</code>, <code>master</code> should have everything <code>ko/master</code> has, and <code>next</code> should have everything <code>ko/next</code> has, etc.<br />
 <code>13. </code>push out the bleeding edge, together with new tags that point into the pushed history.
</dl>
<p> In this example, the <code>ko</code> shorthand points at the Git maintainer&#8217;s repository at kernel.org, and looks like this: </p>
<dl>
<dd>
<pre>(in .git/config)
[remote &quot;ko&quot;]
 url = kernel.org:/pub/scm/git/git.git
 fetch = refs/heads/*:refs/remotes/ko/*
 push = refs/heads/master
 push = refs/heads/next
 push = +refs/heads/seen
 push = refs/heads/maint</pre>
</dl>
<h2>Repository Administration</h2>
<p>A repository administrator uses the following tools to set up and maintain access to the repository by developers. </p>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/1-git-daemon/">git-daemon</a></code>(1) to allow anonymous download from repository.</dl>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/1-git-shell/">git-shell</a></code>(1) can be used as a <i>restricted login shell</i> for shared central repository users.</dl>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/1-git-http-backend/">git-http-backend</a></code>(1) provides a server side implementation of Git-over-HTTP (&quot;Smart http&quot;) allowing both fetch and push services.</dl>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/1-gitweb/">gitweb</a></code>(1) provides a web front-end to Git repositories, which can be set-up using the <code><a href="/docs/linux/man/1-git-instaweb/">git-instaweb</a></code>(1) script.</dl>
<p> m[blue]<code>update hook howto</code>m[]<font SIZE="-2">[1]</font> has a good example of managing a shared central repository. </p>
<p> In addition there are a number of other widely deployed hosting, browsing and reviewing solutions such as: </p>
<dl>
<dd>&bull; gitolite, gerrit code review, cgit and others.</dl>
<h3>Examples</h3>
<p>We assume the following in /etc/services</p>
<dl>
<dd>
<dl>
<dd>
<pre>$ grep 9418 /etc/services
git 9418/tcp # Git Version Control System</pre>
</dl>
</dl>
<p> Run git-daemon to serve /pub/scm from inetd.</p>
<dl>
<dd>
<dl>
<dd>
<pre>$ grep git /etc/inetd.conf
git stream tcp nowait nobody \
 /usr/bin/git-daemon git-daemon --inetd --export-all /pub/scm</pre>
</dl>
<p> The actual configuration line should be on one line.</dl>
<p> Run git-daemon to serve /pub/scm from xinetd.</p>
<dl>
<dd>
<dl>
<dd>
<pre>$ cat /etc/xinetd.d/git-daemon
# default: off
# description: The Git server offers access to Git repositories
service git
{
 disable = no
 type = UNLISTED
 port = 9418
 socket_type = stream
 wait = no
 user = nobody
 server = /usr/bin/git-daemon
 server_args = --inetd --export-all --base-path=/pub/scm
 log_on_failure += USERID
}</pre>
</dl>
<p> Check your <a href="/docs/linux/man/8-xinetd/">xinetd</a>(8) documentation and setup, this is from a Fedora system. Others might be different.</dl>
<p> Give push/pull only access to developers using git-over-ssh.</p>
<dl>
<dd>e.g. those using: <code>$ git push/pull <a href="ssh://host.xz/pub/scm/project">ssh://host.xz/pub/scm/project</a></code> </p>
<dl>
<dd>
<pre>$ grep git /etc/passwd <code>(1)</code>
alice:x:1000:1000::/home/alice:/usr/bin/git-shell
bob:x:1001:1001::/home/bob:/usr/bin/git-shell
cindy:x:1002:1002::/home/cindy:/usr/bin/git-shell
david:x:1003:1003::/home/david:/usr/bin/git-shell
$ grep git /etc/shells <code>(2)</code>
/usr/bin/git-shell</pre>
</dl>
<p> <code>1. </code>log-in shell is set to /usr/bin/git-shell, which does not allow anything but <code>git push</code> and <code>git pull</code>. The users require ssh access to the machine.<br />
 <code>2. </code>in many distributions /etc/shells needs to list what is used as the login shell.
</dl>
<p> CVS-style shared repository.</p>
<dl>
<dd>
<dl>
<dd>
<pre>$ grep git /etc/group <code>(1)</code>
git:x:9418:alice,bob,cindy,david
$ cd /home/devo.git
$ ls -l <code>(2)</code>
 lrwxrwxrwx 1 david git 17 Dec 4 22:40 HEAD -&gt; refs/heads/master
 drwxrwsr-x 2 david git 4096 Dec 4 22:40 branches
 -rw-rw-r-- 1 david git 84 Dec 4 22:40 config
 -rw-rw-r-- 1 david git 58 Dec 4 22:40 description
 drwxrwsr-x 2 david git 4096 Dec 4 22:40 hooks
 -rw-rw-r-- 1 david git 37504 Dec 4 22:40 index
 drwxrwsr-x 2 david git 4096 Dec 4 22:40 info
 drwxrwsr-x 4 david git 4096 Dec 4 22:40 objects
 drwxrwsr-x 4 david git 4096 Nov 7 14:58 refs
 drwxrwsr-x 2 david git 4096 Dec 4 22:40 remotes
$ ls -l hooks/update <code>(3)</code>
 -r-xr-xr-x 1 david git 3536 Dec 4 22:40 update
$ cat info/allowed-users <code>(4)</code>
refs/heads/master alice\|cindy
refs/heads/doc-update bob
refs/tags/v[0-9]* david</pre>
</dl>
<p> <code>1. </code>place the developers into the same git group.<br />
 <code>2. </code>and make the shared repository writable by the group.<br />
 <code>3. </code>use update-hook example by Carl from Documentation/howto/ for branch policy control.<br />
 <code>4. </code>alice and cindy can push into master, only bob can push into doc-update. david is the release manager and is the only person who can create and push version tags.
</dl>
<h2>Git</h2>
<p>Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>update hook howto</p>
<dl>
<dd>file:///usr/share/doc/git/html/howto/update-hook-example.html</dl>

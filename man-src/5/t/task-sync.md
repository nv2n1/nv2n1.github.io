---
title: "task-sync(5)"
name: "task-sync"
section: "5"
letter: "t"
url: "/docs/linux/man/5-task-sync/"
description: "task-sync – A discussion and tutorial for the various"
---

<p>task-sync &#8211; A discussion and tutorial for the various </p>
<p><a href="/docs/linux/man/1-task/">task</a>(1) data synchronization capabilities. </p>
<h2>Introduction</h2>
<p>Taskwarrior has several sync options, external and internal. If you wish to sync your data, choose one method only; mixing methods is only going to lead to problems. Each of the methods discussed have their own strengths.</p>
<h2>Alternatives</h2>
<p>There are three alternatives for syncing data, which are: </p>
<p> 1) Version control systems, such as git, hg, svn<br />
 2) File hosting systems, such as DropBox<br />
 3) Using the Taskserver and the &#8216;sync&#8217; command</p>
<h2>Option 1: Version Control Systems</h2>
<p>There are several good, distributed VCS systems (git, hg, &#8230;) and centralized VCS systems (svn &#8230;), and they function in a similar fashion for our purposes. </p>
<p> Setup is straightforward. You place your .task directory under revision control. You then need to perform a regular commit/push/pull/update to make sure that the data is propagated when needed. You can even do this using shell scripts so that every task command is preceded by a &#8216;pull&#8217; and followed by a &#8216;push&#8217;. </p>
<p> Strengths: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211; Good data transport mechanisms </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211; Secure transport options </p>
<p> Weaknesses: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211; You need proficiency with VCS tools </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211; You will need to manually resolve conflicts frequently </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211; You need to provide the mechanism for making sure copies are up to date</p>
<h2>Option 2: File Hosting Services</h2>
<p>There are many file hosting services, such as DropBox, Amazon S3, Google Drive, SkyDrive and more. This technique involves storing your .task directory in a shared directory under the control of the file hosting services. </p>
<p> Syncing happens quickly, although it is possible to run into conflict situations when there is no network connectivity, and the tasks are modified in two separate locations. This is because the file hosting service knows only about files, and it has no idea how to merge tasks. Avoid this problem by never modifying the same task on two machines, without an intervening sync. </p>
<p> Setup simply involves creating the directory and modifying your data.location configuration variable like this: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>task config data.location&nbsp;<wbr>/path/to/shared/directory </p>
<p> Strengths: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211; Always secure </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211; Good client support </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211; Easy setup </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211; Transparent use </p>
<p> Weaknesses: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211; Tasks are not properly merged</p>
<h2>Option 3: Taskserver</h2>
<p>The Taskserver was designed for this purpose to be secure, fast and conflict free, allowing data interchange between assorted Taskwarrior clients, and tolerant of network connectivity problems. </p>
<p> There is a &#8216;sync&#8217; command built in to Taskwarrior (provided the GnuTLS library is installed), and with a server account and client configuration, syncing is done on demand. </p>
<p> Setup is a matter of creating an account on a Taskserver (see your Taskserver provider or operate your own &#8211; see <a rel="nofollow" href="http://taskwarrior.org/docs/server_setup.html)">http://taskwarrior.org/docs/server_setup.html)</a> </p>
<p> Once you have an account, you&#8217;ll receive a certificate, key, and credentials. You&#8217;ll need to put the certificate and key somewhere like this: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>cp&nbsp;<wbr>&lt;name&gt;.cert.pem&nbsp;<wbr>~/.task<br />
&nbsp;<wbr>$&nbsp;<wbr>cp&nbsp;<wbr>&lt;name&gt;.key.pem&nbsp;<wbr>~/.task </p>
<p> Then you configure Taskwarrior, using the provided details: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>task config taskd.certificate&nbsp;<wbr>~/.task/&lt;name&gt;.cert.pem<br />
&nbsp;<wbr>$&nbsp;<wbr>task config taskd.key&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>~/.task/&lt;name&gt;.key.pem<br />
&nbsp;<wbr>$&nbsp;<wbr>task config taskd.credentials&nbsp;<wbr>&lt;organization&gt;/&lt;name&gt;/&lt;UUID&gt;<br />
&nbsp;<wbr>$&nbsp;<wbr>task config taskd.server&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&lt;server domain&gt;:&lt;port&gt; </p>
<p> If you are using a private server, you are likely also using a self-signed certificate, which means you will need one of the following additional entries: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>task config taskd.ca&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>~/.task/ca.cert.pem </p>
<p> The CA (Certificate Authority) will be used to verify the server certificate. Alternatively, you can override the cert verification process using: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>task config taskd.trust&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8216;allow all&#8217; </p>
<p> This is an insecure option that should be used with caution, because it directs Taskwarrior to trust any certificate. </p>
<p> After setup, you run a one-time sync initialization, like this: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>task sync initialize </p>
<p> This will make sure your client and the server are properly in sync to begin with. From this point on, you never run the &#8216;initialize&#8217; command again, just go about your business, and when you want to sync, run this: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>task sync </p>
<p> You&#8217;ll see a summary of how many tasks were uploaded and downloaded. You can safely run the command as often as you like. When there are no changes to sync, nothing happens. If you do not have connectivity, your task changes accumulate so that when you next run &#8216;sync&#8217; with proper connectivity, the changes are properly handled, in the right order. </p>
<p> Strengths: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211; Always secure </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211; Minimal bandwidth </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211; Tolerates connectivity outage </p>
<p> Weaknesses: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211; You need to manage your own server, or gain access to a hosted server.</p>
<h2>CREDITS &amp; COPYRIGHTS</h2>
<p>Copyright (C) 2006 &#8211; 2016 P. Beckingham, F. Hernandez. </p>
<p> Taskwarrior is distributed under the MIT license. See <a rel="nofollow" href="http://www.opensource.org/licenses/mit-license.php">http://www.opensource.org/licenses/mit-license.php</a> for more information.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-task/">task</a>(1),</code> <code><a href="/docs/linux/man/5-taskrc/">taskrc</a>(5),</code> <code><a href="/docs/linux/man/5-task-color/">task-color</a>(5),</code> For more information regarding task, the following may be referenced:</p>
<dl>
<dt>The official site at</p>
<dd>&lt;<a rel="nofollow" href="http://taskwarrior.org">http://taskwarrior.org</a>&gt;</p>
<dt>The official code repository at</p>
<dd>&lt;<a rel="nofollow" href="https://git.tasktools.org/scm/tm/task.git">https://git.tasktools.org/scm/tm/task.git</a>&gt;</p>
<dt>You can contact the project by writing an email to</p>
<dd>&lt;support [at] taskwarrior.org&gt; </p>
<h2>Reporting Bugs</h2>
<dl>
<dt>Bugs in task may be reported to the issue-tracker at</p>
<dd>&lt;<a rel="nofollow" href="http://taskwarrior.org">http://taskwarrior.org</a>&gt; </p>
</dl>

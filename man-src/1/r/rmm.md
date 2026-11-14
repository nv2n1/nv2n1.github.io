---
title: "rmm(1)"
name: "rmm"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rmm/"
description: "rmm – remove messages"
---

<h2 class="name">NAME</h2>
<p> rmm &#8211; remove messages </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>rmm</code> [<i>+folder</i>] [<i>msgs</i>] [<code>-unlink</code> | <code>-nounlink</code>] [<code>-rmmproc</code> <i>program</i>] [<code>-normmproc</code>] [<code>-version</code>] [<code>-help</code>]</dl>
<h2>DESCRIPTION</h2>
<dd>By default, <code>rmm</code> will remove the specified messages by renaming each of the message files with a site-dependent prefix (usually a comma). Such files will then need to be removed in some manner after a certain amount of time. Many sites arrange for <code>cron</code> to remove these files once a day, so check with your system administrator. </p>
<p> Alternately, if you wish for <code>rmm</code> to really remove the files representing these messages, you can use the <code>-unlink</code> switch. But messages removed by this method cannot be later recovered. </p>
<p> If you prefer a more sophisticated method of `removing&#8217; messages, you can define the <i>rmmproc</i> profile component. For example, you can add a profile component such as </p>
<dl>
<dt>
<dd> rmmproc:<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/foouser/bin/rmm_msgs
</dl>
<p> Then instead of simply renaming the message file, <code>rmm</code> will call the named program or script to handle the files that represent the messages to be deleted. The <code>-rmmproc</code> switch may be used to override this profile component. The <code>-normmproc</code> switch disables the use of any <i>rmmproc</i> profile component and negates all prior <code>-rmmproc</code> switches. </p>
<p> An example of a <i>rmmproc</i> script that saves a message based in its Message-ID is provided in /etc/nmh/rmmproc.messageid. To enable it, simply add a <i>rmmproc</i> component that names it to your profile. </p>
<p> Some users of <code>csh</code> prefer the following: </p>
<dl>
<dt>
<dd> alias rmm &#8216;refile +d&#8217;</dl>
<p> where folder `+d&#8217; is a folder for deleted messages, and </p>
<dl>
<dt>
<dd> alias mexp &#8216;rm `mhpath +d all`&#8217;</dl>
<p> is used to &#8220;expunge&#8221; deleted messages. </p>
<p> The current message is not changed by <code>rmm</code>, so a <code>next</code> will advance to the next message in the folder as expected.</p>
<h2>FILES</h2>
<pre>
^$HOME/.mh_profile~^The user profile
</pre>
<h2>PROFILE COMPONENTS</h2>
<pre>
^Path:~^To determine the user's nmh directory
^Current-Folder:~^To find the default current folder
^rmmproc:~^Program to delete the message
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-rmf/">rmf</a></i>(1)</p>
<h2>DEFAULTS</h2>
<pre>
`<code>+folder</code>' defaults to the current folder
`<code>msgs</code>' defaults to cur
`<code>-nounlink</code>'
</pre>
<h2>CONTEXT</h2>
<p> If a folder is given, it will become the current folder.</p>
<h2>BUGS</h2>
<p> Since <code>rmm</code> and <code>refile</code> use your <i>rmmproc</i> to delete the message, the <i>rmmproc</i> must <code>NOT</code> call <code>rmm</code> or <code>refile</code> without specifying <code>-normmproc</code>, or you will create an infinite loop. </p>
<h2>Index</h2>

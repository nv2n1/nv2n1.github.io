---
title: "iceccd(1)"
name: "iceccd"
section: "1"
letter: "i"
url: "/docs/linux/man/1-iceccd/"
description: "iceccd – Icecream daemon"
---

<h2>NAME</h2>
<p> iceccd &#8211; Icecream daemon</p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>iceccd</code> [<code>-n&nbsp;<wbr></code><i>netname</i>] [<code>-m&nbsp;<wbr></code><i>max_processes</i>] [<code>&#8211;no-remote</code>] [<code>-w</code>] [<code>-d</code> | <code>&#8211;daemonize</code>] [<code>-l&nbsp;<wbr></code><i>logfile</i>] [<code>-s&nbsp;<wbr></code><i>schedulerhost</i>] [-v&nbsp;<wbr>[v&nbsp;<wbr>[v]]] [<code>-r</code> | <code>&#8211;run-as-user</code>] [<code>-b&nbsp;<wbr></code><i>env-basedir</i>] [<code>-u</code> | <code>&#8211;nobody-uid</code><i> nobodyuid</i>] [<code>&#8211;cache-limit&nbsp;<wbr></code><i>MB</i>] [<code>-N&nbsp;<wbr></code><i>hostname</i>] </p>
</dl>
<h2>DESCRIPTION</h2>
<dd>The Icecream daemon has to run on all nodes being part of the Icecream compile cluster. It receives compile jobs and executes them in a chroot environment. The compile clients send their compile environment the first time they send a job to a particular daemon, so that the environment of the daemon doesn&#8217;t have to match the one of the client. </p>
<p> The daemon also has to run on clients sending compile jobs to the Icecream network. If a node should be able to send compile jobs, but never receive any, start the daemon with the option -m 0. </p>
<p> All Icecream daemons need to have contact to the Icecream scheduler which controls the distribution of data between compile nodes. Normally the daemon will automatically find the right scheduler. If this is not the case you can explicitly specify the name of the Icecream network and the host running the scheduler. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-n</code> <i>netname</i></p>
<dd> The name of the icecream network the daemon should connect to. There has to be a scheduler running for the network under the same network name. </p>
<dt><code>-m</code> <i>max_processes</i></p>
<dd> Maximum number of compile jobs started in parallel on machine running the daemon. </p>
<dt><code>&#8211;no-remote</code></p>
<dd> Prevents jobs from other nodes being scheduled on this one. </p>
<dt><code>-w</code></p>
<dd>
<dt><code>-d</code>, <code>&#8211;daemonize</code></p>
<dd> Detach daemon from shell. </p>
<dt><code>-l</code> <i>logfile</i></p>
<dd> Name of file where log output is written to. </p>
<dt><code>-s</code> <i>scheduler_host</i></p>
<dd> Name of host running the scheduler for the network the daemon should connect to. This option might help if the scheduler can&#8217;t broadcast its presence to the clients due to firewall settings or similar reasons. </p>
<dt><code>-v</code>, <code>-vv</code>, <code>-vvv</code></p>
<dd> Control verbosity of daemon. The more v the more verbose. </p>
<dt><code>-r</code>, <code>&#8211;run-as-user</code></p>
<dd> Force running the daemon with user rights. Usually you will need to run the daemon with root rights. </p>
<dt><code>-b</code> <i>env_basedir</i></p>
<dd> Base directory for storing compile environments sent to the daemon by the compile clients. </p>
<dt><code>-u</code>, <code>&#8211;nobody-uid</code> <i>nobodyuid</i></p>
<dd> Id of user nobody. This user id is used when the daemon is dropping privileges. </p>
<dt><code>&#8211;cache-limit</code> <i>MB</i></p>
<dd> Maximum size in Mega Bytes of cache used to store compile environments of compile clients. </p>
<dt><code>-N</code> <i>hostname</i></p>
<dd> The name of the icecream host on the network. </p>
</dl>
<h2>SEE ALSO</h2>
<p> icecream, scheduler, iceccd, icemon </p>
<h2>AUTHOR</h2>
<p> Cornelius Schumacher </p>
<h2>Index</h2>

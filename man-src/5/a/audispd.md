---
title: "audispd(5)"
name: "audispd"
section: "5"
letter: "a"
url: "/docs/linux/man/5-audispd/"
description: "audispd.conf – the audit event dispatcher configuration file"
---

<p>audispd.conf &#8211; the audit event dispatcher configuration file</p>
<h2>Description</h2>
<p><code>audispd.conf</code> is the file that controls the configuration of the audit event dispatcher. Each line should contain one configuration keyword, an equal sign, and then followed by appropriate configuration information. All option names and values are case insensitive. The keywords recognized are listed and described below. Each line should be limited to 160 characters or the line will be skipped. You may add comments to the file by starting the line with a &#8216;#&#8217; character. </p>
<dl>
<dt><i>q_depth</i></p>
<dd>This is a numeric value that tells how big to make the internal queue of the audit event dispatcher. A bigger queue lets it handle a flood of events better, but could hold events that are not processed when the daemon is terminated. If you get messages in syslog about events getting dropped, increase this value. The default value is 80.</p>
<dt><i>overflow_action</i></p>
<dd>This option determines how the daemon should react to overflowing its internal queue. When this happens, it means that more events are being received than it can get rid of. This error means that it is going to lose the current event its trying to dispatch. It has the following choices: <i>ignore</i>, <i>syslog</i>, <i>suspend</i>, <i>single</i>, and <i>halt</i>. If set to <i>ignore</i>, the audisp daemon does nothing. <i>syslog</i> means that it will issue a warning to syslog. <i>suspend</i> will cause the audisp daemon to stop processing events. The daemon will still be alive. The <i>single</i> option will cause the audisp daemon to put the computer system in single user mode. <i>halt</i> option will cause the audisp daemon to shutdown the computer system.</p>
<dt><i>priority_boost</i></p>
<dd>This is a non-negative number that tells the audit event dispatcher how much of a priority boost it should take. This boost is in addition to the boost provided from the audit daemon. The default is 4. No change is 0.</p>
<dt><i>max_restarts</i></p>
<dd>This is a non-negative number that tells the audit event dispatcher how many times it can try to restart a crashed plugin. The default is 10.</p>
<dt><i>name_format</i></p>
<dd>This option controls how computer node names are inserted into the audit event stream. It has the following choices: <i>none</i>, <i>hostname</i>, <i>fqd</i>, <i>numeric</i>, and <i>user</i>. <i>None</i> means that no computer name is inserted into the audit event. <i>hostname</i> is the name returned by the gethostname syscall. The <i>fqd</i> means that it takes the hostname and resolves it with dns for a fully qualified domain name of that machine. <i>Numeric</i> is similar to fqd except it resolves the IP address of the machine. <i>User</i> is an admin defined string from the name option. The default value is <i>none</i>.</p>
<dt><i>name</i></p>
<dd>This is the admin defined string that identifies the machine if user is given as the name_format option.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-audispd/">audispd</a></code>(8) </p>

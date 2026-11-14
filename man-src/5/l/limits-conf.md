---
title: "limits-conf(5)"
name: "limits-conf"
section: "5"
letter: "l"
url: "/docs/linux/man/5-limits-conf/"
description: "limits.conf – configuration file for the pam_limits module"
---

<p>limits.conf &#8211; configuration file for the pam_limits module</p>
<h2>Description</h2>
<p>The <i>pam_limits.so</i> module applies ulimit limits, nice priority and number of simultaneous login sessions limit to user login sessions. This description of the configuration file syntax applies to the /etc/security/limits.conf file and *.conf files in the /etc/security/limits.d directory. The syntax of the lines is as follows: </p>
<pre><code>&lt;domain&gt;
&lt;type&gt;
&lt;item&gt;
&lt;value&gt;</code></pre>
<p> The fields listed above should be filled as follows: &lt;domain&gt;</p>
<dl>
<dd>&bull; a username</dl>
<dl>
<dd>&bull; a groupname, with <code>@group</code> syntax. This should not be confused with netgroups.</dl>
<dl>
<dd>&bull; the wildcard <code>*</code>, for default entry.</dl>
<dl>
<dd>&bull; the wildcard <code>%</code>, for maxlogins limit only, can also be used with <code>%group</code> syntax. If the <code>%</code> wildcard is used alone it is identical to using <code>*</code> with maxsyslogins limit. With a group specified after <code>%</code> it limits the total number of logins of all users that are member of the group.</dl>
<dl>
<dd>&bull; an uid range specified as <i>&lt;min_uid&gt;</i><code>:</code><i>&lt;max_uid&gt;</i>. If min_uid is omitted, the match is exact for the max_uid. If max_uid is omitted, all uids greater than or equal min_uid match.</dl>
<dl>
<dd>&bull; a gid range specified as <code>@</code><i>&lt;min_gid&gt;</i><code>:</code><i>&lt;max_gid&gt;</i>. If min_gid is omitted, the match is exact for the max_gid. If max_gid is omitted, all gids greater than or equal min_gid match. For the exact match all groups including the user&#8217;s supplementary groups are examined. For the range matches only the user&#8217;s primary group is examined.</dl>
<dl>
<dd>&bull; a gid specified as <code>%:</code><i>&lt;gid&gt;</i> applicable to maxlogins limit only. It limits the total number of logins of all users that are member of the group with the specified gid.</dl>
<p> <code>NOTE:</code> group and wildcard limits are not applied to the root user. To set a limit for the root user, this field must contain the literal username <code>root</code>.</dl>
<p> &lt;type&gt; <code>hard</code></p>
<dl>
<dd>for enforcing <code>hard</code> resource limits. These limits are set by the superuser and enforced by the Kernel. The user cannot raise his requirement of system resources above such values.</dl>
<p> <code>soft</code></p>
<dl>
<dd>for enforcing <code>soft</code> resource limits. These limits are ones that the user can move up or down within the permitted range by any pre-existing <code>hard</code> limits. The values specified with this token can be thought of as <i>default</i> values, for normal system usage.</dl>
<p> <code>&#8211;</code></p>
<dl>
<dd>for enforcing both <code>soft</code> and <code>hard</code> resource limits together. Note, if you specify a type of &#8216;-&#8216; but neglect to supply the item and value fields then the module will never enforce any limits on the specified user/group etc. .</dl>
</dl>
<pre><code>&lt;item&gt;</code></pre>
<p> <code>core</code></p>
<dl>
<dd>limits the core file size (KB)</dl>
<p> <code>data</code></p>
<dl>
<dd>maximum data size (KB)</dl>
<p> <code>fsize</code></p>
<dl>
<dd>maximum filesize (KB)</dl>
<p> <code>memlock</code></p>
<dl>
<dd>maximum locked-in-memory address space (KB)</dl>
<p> <code>nofile</code></p>
<dl>
<dd>maximum number of open file descriptors</dl>
<p> <code>rss</code></p>
<dl>
<dd>maximum resident set size (KB) (Ignored in Linux 2.4.30 and higher)</dl>
<p> <code>stack</code></p>
<dl>
<dd>maximum stack size (KB)</dl>
<p> <code>cpu</code></p>
<dl>
<dd>maximum CPU time (minutes)</dl>
<p> <code>nproc</code></p>
<dl>
<dd>maximum number of processes</dl>
<p> <code>as</code></p>
<dl>
<dd>address space limit (KB)</dl>
<p> <code>maxlogins</code></p>
<dl>
<dd>maximum number of logins for this user (this limit does not apply to user with <i>uid=0</i>)</dl>
<p> <code>maxsyslogins</code></p>
<dl>
<dd>maximum number of all logins on system; user is not allowed to log-in if total number of all user logins is greater than specified number (this limit does not apply to user with <i>uid=0</i>)</dl>
<p> <code>priority</code></p>
<dl>
<dd>the priority to run user process with (negative values boost process priority)</dl>
<p> <code>locks</code></p>
<dl>
<dd>maximum locked files (Linux 2.4 and higher)</dl>
<p> <code>sigpending</code></p>
<dl>
<dd>maximum number of pending signals (Linux 2.6 and higher)</dl>
<p> <code>msgqueue</code></p>
<dl>
<dd>maximum memory used by POSIX message queues (bytes) (Linux 2.6 and higher)</dl>
<p> <code>nice</code></p>
<dl>
<dd>maximum nice priority allowed to raise to (Linux 2.6.12 and higher) values: [-20,19]</dl>
<p> <code>rtprio</code></p>
<dl>
<dd>maximum realtime priority allowed for non-privileged processes (Linux 2.6.12 and higher)</dl>
<p> <code>chroot</code></p>
<dl>
<dd>the directory to chroot the user to</dl>
</dl>
<p> All items support the values <i>-1</i>, <i>unlimited</i> or <i>infinity</i> indicating no limit, except for <code>priority</code> and <code>nice</code>. If a hard limit or soft limit of a resource is set to a valid value, but outside of the supported range of the local system, the system may reject the new limit or unexpected behavior may occur. If the control value <i>required</i> is used, the module will reject the login if a limit could not be set. In general, individual limits have priority over group limits, so if you impose no limits for <i>admin</i> group, but one of the members in this group have a limits line, the user will have its limits set according to this line. Also, please note that all limit settings are set <i>per login</i>. They are not global, nor are they permanent; existing only for the duration of the session. One exception is the <i>maxlogin</i> option, this one is system wide. But there is a race, concurrent logins at the same time will not always be detect as such but only counted as one. In the <i>limits</i> configuration file, the &#8216;<code>#</code>&#8216; character introduces a comment &#8211; after which the rest of the line is ignored. The pam_limits module does report configuration problems found in its configuration file and errors via <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3).</p>
<h2>Examples</h2>
<p>These are some example lines which might be specified in /etc/security/limits.conf. </p>
<dl>
<dd>
<pre>* soft core 0
root hard core 100000
* hard nofile 512
@student hard nproc 20
@faculty soft nproc 20
@faculty hard nproc 50
ftp hard nproc 0
@student - maxlogins 4
:123 hard cpu 5000
@500: soft cpu 10000
600:700 hard locks 10</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-pam_limits/">pam_limits</a></code>(8), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7), <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2), <code><a href="//www.systutorials.com/docs/linux/man/3p-getrlimit/">getrlimit</a></code>(3p)</p>
<h2>Author</h2>
<p>pam_limits was initially written by Cristian Gafton &lt;gafton [at] redhat.com&gt;</p>

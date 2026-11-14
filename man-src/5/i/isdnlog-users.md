---
title: "isdnlog-users(5)"
name: "isdnlog-users"
section: "5"
letter: "i"
url: "/docs/linux/man/5-isdnlog-users/"
description: "/etc/isdn/isdnlog.users – user base isdnlog config file"
---

<p>/etc/isdn/isdnlog.users &#8211; user base isdnlog config file</p>
<h2>Description</h2>
<p>This file is only needed if isdnlog is started with the &quot;-xX&quot; / &quot;xisdn=&quot; option. If this file does not exist, isdnlog will create a default file and print a warning. This file contains information about which users are permitted to use isdnlog clients, and what their privileges are. This file is checked every time a connection to isdnlog is made; thus, it is possible to edit this file and have the changes effective immediately without having to stop and start isdnlog. For now there are no real usable clients for isdnlog, so this file isn&#8217;t very useful at the moment. </p>
<h2>Format</h2>
<p>Warning: the format of this file may change in the future. </p>
<p> Blank lines are ignored. If a line has a &quot;#&quot;, this char and the rest of the line is ignored as comment. If the last char of a line is a &quot;line and the next line are considered one line. These characters are considered special: &quot;$@#,;</p>
<p> The file consists of lines; each line begins with the name of a user. After the user&#8217;s name the privileges given to this user are specified (on the same line). The following privileges are possible, separated by semicolons &quot;;&quot; : </p>
<dl>
<dd>
<dl>
<dt><code>ALL</code></p>
<dd>All of the privileges below are given. Should only be given to root. </p>
<dt><code>MSN=msn[,msn&#8230;]</code></p>
<dd>Only information about events concerning the specified msns is given. This includes incoming and outgoing calls, and protocol information. Any number of msns may be given. Wildcards (such as used in isdn.conf) are permitted. With &quot;MSN=*&quot; all msns are allowed.<br />
 Unknown numbers (e.g. from outgoing calls from other isdn devices or incoming calls from analog connections) cannot be specified with MSN=. The only way to allow these calls to be seen is by giving &quot;MSN=*&quot;. </p>
<dt><code>PROTOCOL</code></p>
<dd>The information specified to isdnlog by the -xX flag (see <a href="/docs/linux/man/8-isdnlog/">isdnlog</a>(8)) is allowed. </p>
<dt><code>I4LCONF</code> (planned)</p>
<dd>This gives permission to change isdn4linux properties. This should only be allowed to root. </p>
<dt><code>ADDRESSBOOK</code> (planned)</p>
<dd>This makes it possible to retrieve / store information about a caller or called number.</dl>
</dl>
<p> <code>Users</code><br />
 At the beginning of the file it is possible to specify users with hostnames: </p>
<pre>fred [at] vom.jupiter MSN=4711?
root [at] host1.at.home ALL</pre>
<p>Here the user &quot;fred&quot; can only connect to isdnlog from the host &quot;vom.jupiter&quot;. Similarly, the user &quot;root&quot; is only allowed when on host &quot;host1.at.home&quot;. </p>
<p> <code>Groups</code><br />
 After the lines with hostnames, it is possible to define groups of users and hostnames. A group looks like a section as described in <a href="/docs/linux/man/5-isdn-conf/">isdn.conf</a>(5). It begins with a line such as: </p>
<p> [My_Group] </p>
<p> and ends with the beginning of the next group or the end of the file. Group names are not case sensitive. In fact, group names are not actually used (except for <code>[world]</code>, see below). </p>
<p> In a group, lines consist of a username <i>or</i> a hostname. Lines with a username must also contain those privileges that the user has. No privileges can be listed with a hostname. </p>
<pre>heinz MSN=*;PROTOCOL
@host1
@host2
otto MSN=47111,47112
@host3</pre>
<p>The above example allows the users heinz and otto to connect from any of the hosts host1, host2 and host3. The user heinz can see information about all msns, user otto can only see information about msns 47111 and 47112. </p>
<p> If anyone is allowed to do anything, then it is enough to put only the following line into the file &quot;isdnlog.users&quot;: </p>
<p> [world]</p>
<h2>Files</h2>
<dl>
<dt><code>/etc/isdn/isdnlog.users</code></p>
<dd>This file. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-isdnlog/">isdnlog</a>(1) </code></p>
<h2>Author</h2>
<p>This manual page was written by Andreas Jellinghaus &lt;aj [at] dungeon.inka.de&gt;, for Debian GNU/Linux and isdn4linux.</p>

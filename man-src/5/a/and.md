---
title: "and(5)"
name: "and"
section: "5"
letter: "a"
url: "/docs/linux/man/5-and/"
description: "/etc/and/and.priorities – priority database for the auto nice daemon."
---

<p>/etc/and/and.priorities &#8211; priority database for the auto nice daemon. </p>
<h2>Version</h2>
<p>This manual page documents and.priorities for <code>and</code> version 1.2.2.</p>
<h2>Description</h2>
<p>This is the priority database file for <code>and.</code> It stores (user, group, command, parent, nicelevels) tuples (hereafter called entries) to determine the new nice level (or the kill signal, for that matter) when a job reaches one of the time limits defined in <i>/etc/and/and.conf.</i> (See lv1time, lv2time, and lv3time on the and.conf manual page for details.) See the <code>affinity</code> setting in <i>/etc/and/and.conf</i> for how ambiguities between the fields (user, group, command, parent) are dealt with when searching the database to determine the new nice level for a job. Note that if more than one entry matches with the same accuracy (e.g. with a parent= entry and an ancestor= entry), the <code>last entry wins!</code> Comments start with a # in the <code>first column.</code> Empty lines are ignored. Unlike with other configuration files, lines <code>cannot be concatenated</code> with a backslash. Furthermore, this file is <code>case sensitive.</code> <code>and</code> allows for host-specific sections in the configuration file. These work as lines of the form <i>on somehost</i> and work as follows: the parser determines if the host name (as returned by gethostname) matches the extended regular expression that follows the <i>on</i> keyword. If it does, it just keeps processing the file as if nothing had happened. If it does not match, however, everything up to the next <i>on</i> keyword is skipped. So if you want to end a host-specific section, you must write <i>on .*</i> (which matches all hosts) to switch back to normal. Don&#8217;t forget to <code>kill -HUP</code> the auto nice daemon to enable the changes. </p>
<h2>Settings</h2>
<p>A valid entry consists of a line of six columns, separated by one or more spaces. These columns are: (in that order) </p>
<dl>
<dt><code>user</code></p>
<dd>The user ID the command is running under. May be a user name (which will be looked up in the password file and, if enabled, via NIS), or a numeric user ID, or an asterisk for any user. </p>
<dt><code>group</code></p>
<dd>The group ID the command is running under. May be a group name (which will be looked up in the group file and again, if enabled, via NIS), or a numeric group ID, or an asterisk for any group. </p>
<dt><code>command</code></p>
<dd>The name of the command, without path. May be a command, a regular expression to match multiple commands, or an asterisk for any command. Note that &quot;foobar&quot; will <code>not</code> match &quot;/usr/bin/foobar&quot; &#8211; you probably mean &quot;.*foobar&quot; or even &quot;.*foobar.*&quot;. </p>
<dt><code>parent</code></p>
<dd>There are two modes of operation for the parent field, determined by a keyword: <code>parent=foobar</code> will match if a process&#8217; direct parent process matches the command or regular expression after the equal sign, whereas <code>ancestor=foobar</code> will match if <i>any </i> ancestor process matches. After the keyword and the equal sign goes the name of the parent process, without path. May be a command, a regular expression to match multiple commands, or an asterisk for any command. (You can just use the asterisk if you want to ignore parents for this entry.) Note that again &quot;foobar&quot; will <code>not</code> match &quot;/usr/bin/foobar&quot;, as with command. </p>
<dt><code>nicelevel 1</code></p>
<dd>The nice level after lv1time CPU time was used by the command. Positive numbers and 0 are interpreted as nice levels; negative numbers are interpreted as signals to be sent to the command. A &quot;nice level&quot; of 19 will almost stop the job, -9 will actually kill it. (Like in kill -9.) lv1time can be set in <i>/etc/and.conf</i> </p>
<dt><code>nicelevel 2</code></p>
<dd>Same but after lv2time. </p>
<dt><code>nicelevel 3</code></p>
<dd>Same but after lv3time. </p>
</dl>
<h2>Examples</h2>
<p>Here are some entries from the real world (i.e. from &quot;my&quot; cluster at the Institute). As lv[123]time, 5 min., 20 min., and 1 hour is assumed. (Which is the default. See <i>/etc/and.conf</i> for details.) You might also check the default priority database that comes with <code>and.</code> # A finer default nice level<br />
 * * * * 4 8 12<br />
 # User dau is an idiot, so treat him like accordingly<br />
 dau * * * 19 19 19<br />
 # Netscape sometimes goes berserk, we must stop it<br />
 * * netscape * 4 -9 -9<br />
 # Most hosts are free for everyone but some are<br />
 # especially for the FOO group<br />
 * * * * 4 8 12<br />
 on (bar|baz)<br />
 * * * * 8 12 16<br />
 # &#8230; or, more radical: * * * * -9 -9 -9<br />
 * foo * * 4 8 12<br />
 on .*<br />
 # KDE screen savers&#8230;<br />
 * * .*kss * 16 16 16<br />
 # Grid jobs (assuming they are started by a master<br />
 # process)<br />
 * * * ancestor=grid_master 10 10 10<br />
 # Now some clever yet deceitful user might start all<br />
 # his jobs using a shell script named grid_master.<br />
 # He shall regret&#8230; whereas the original grid_master<br />
 # (owned by grid) is left alone.<br />
 * * grid_master * -9 -9 -9<br />
 grid * grid_master * 0 0 0 </p>
<h2>Files</h2>
<dl>
<dt><code>/etc/and/and.priorities</code></p>
<dd>The priority database (in plain text). Contains the (user, group, command, nicelevels) tuples. This is what this manual page is about. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-and/">and</a></code>(8), <code><a href="/docs/linux/man/5-and-conf/">and.conf</a></code>(5), <code><a href="/docs/linux/man/1-kill/">kill</a></code>(1), <code><a href="/docs/linux/man/7-regex/">regex</a></code>(7), <code><a href="/docs/linux/man/8-renice/">renice</a></code>(8) </p>
<h2>Internet</h2>
<p><code><a rel="nofollow" href="http://and.sourceforge.net/">http://and.sourceforge.net/</a></code></p>
<h2>Author</h2>
<p>The auto nice daemon and this manual page were written by Patrick Schemitz &lt;schemitz [at] users.sourceforge.net&gt;</p>

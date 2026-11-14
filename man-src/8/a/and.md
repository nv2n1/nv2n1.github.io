---
title: "and(8)"
name: "and"
section: "8"
letter: "a"
url: "/docs/linux/man/8-and/"
description: "and – auto nice daemon"
---

<p>and &#8211; auto nice daemon</p>
<h2>Synopsis</h2>
<p><code>and</code> [<code>-htvsx</code>] [<code>-i</code> <i>interval</i>] [<code>-c</code> <i>/path/to/and.conf</i>] [<code>-d</code> <i>/path/to/and.priorities</i>] </p>
<h2>Version</h2>
<p>This manual page documents <code>and</code> version 1.2.2.</p>
<h2>Description</h2>
<p>The auto nice daemon activates itself in certain intervals and renices and even kills jobs according to their priority and CPU usage. Renice levels and kill signals can be defined in terms of users, groups, and commands. Wildcards can be specified for any of these. In addition, commands can be specified using POSIX regular expressions. To allow for network-wide configuration and priority files, a mechanism for hostname-based evaluation is provided, again supporting regular expressions for specifying host names. Jobs owned by root are left alone. Jobs are never increased in their priority. Here are some real-world examples: A certain user is notorious for wasting CPU with next-to-irrelevant jobs. One line is sufficient to renice all of his jobs to about 19. This is a typical situation for a LART (Luser&#8217;s Attitude Readjustment Tool) like <code>and.</code> A CPU server is dedicated to a certain group, but others may also use it when it&#8217;s idle. Just define default nice levels of e.g. 18 and a lower nice level for the privilegued group, say nice level 12. A certain web browser who shall remain unnamed tends to go berserk once in a while. You can configure <code>and</code> to kill -9 it after e.g. 20 CPU minutes. </p>
<h2>Command-Line Options</h2>
<dl>
<dt><code>-c /path/to/and.conf</code></p>
<dd>Specifies the configuration file. If this flag is omitted, <i>/etc/and/and.conf</i> is used instead. </p>
<dt><code>-d /path/to/and.priorities</code></p>
<dd>Specifies the priority database file. If this flag is omitted, <i>/etc/and/and.priorities</i> is used instead. </p>
<dt><code>-h</code></p>
<dd>Produces a short help text. </p>
<dt><code>-i interval</code></p>
<dd>Sets the interval between nice level checks. This flag overrides the interval specified in the configuration file, if any. The default interval of <i>60</i> seconds is used if neither -i nor an interval directive in the configuration file is given. </p>
<dt><code>-s</code></p>
<dd>Log to stdout. Without this switch, logging goes to syslog (normal operations) or <i>./debug.and</i> (test mode). Useful for debugging config files. </p>
<dt><code>-t</code></p>
<dd>Run in test mode only, i.e. don&#8217;t really renice or kill anything. In this mode, logging goes into <i>./debug.and</i> instead of syslog. </p>
<dt><code>-v</code></p>
<dd>Increase verbosity. For maximum verbosity, this flag can be specified multiple times. Be warned that this will blow up your log files, so you should use it in test mode only. </p>
<dt><code>-x</code></p>
<dd>Run in full operational mode, i.e. really renice or kill things. This is the default. </p>
</dl>
<h2>Signals</h2>
<p>On <code>kill -HUP</code> the auto nice daemon will reload its configuration file and priority database.</p>
<h2>Files</h2>
<dl>
<dt><code>/etc/and/and.conf</code></p>
<dd>General configuration file. Stores default nice level, default interval, the &quot;time zones&quot; and the database lookup affinity. </p>
<dt><code>/etc/and/and.priorities</code></p>
<dd>The priority database (in plain text). Contains the (user, group, command, nicelevels) tuples. </p>
<dt>Both files have their own manual pages.</p>
<dd>
<dt><code>./debug.and</code></p>
<dd>Contains logging and status information for debugging purposes. Used in test mode only. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-and-conf/">and.conf</a></code>(5), <code><a href="/docs/linux/man/5-and-priorities/">and.priorities</a></code>(5), <code><a href="/docs/linux/man/1-kill/">kill</a></code>(1), <code><a href="/docs/linux/man/7-regex/">regex</a></code>(7), <code><a href="/docs/linux/man/8-renice/">renice</a></code>(8) </p>
<h2>Internet</h2>
<p><code><a rel="nofollow" href="http://and.sourceforge.net/">http://and.sourceforge.net/</a></code></p>
<h2>Author</h2>
<p>The auto nice daemon and this manual page were written by Patrick Schemitz &lt;schemitz [at] users.sourceforge.net&gt;</p>

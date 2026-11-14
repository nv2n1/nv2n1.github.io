---
title: "cgrulesengd(8)"
name: "cgrulesengd"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cgrulesengd/"
description: "cgrulesengd – control group rules daemon"
---

<p>cgrulesengd &#8211; control group rules daemon </p>
<h2>Synopsis</h2>
<p><code>cgrulesengd</code> [options] </p>
<h2>Description</h2>
<p><code>cgrulesengd</code> is a daemon, which distributes processes to control groups. When any process changes its effective UID or GID, <code>cgrulesengd</code> inspects the list of rules loaded from the <i>cgrules.conf</i> file and moves the process to the appropriate control group. The list of rules is read during the daemon startup is are cached in the daemon&#8217;s memory. The daemon reloads the list of rules when it receives SIGUSR2 signal. The daemon reloads the list of templates when it receives SIGUSR1 signal. The daemon opens a standard unix socket to receive &#8216;sticky&#8217; requests from <code>cgexec</code>. </p>
<h2>Options</h2>
<dl>
<dt><code>-h|&#8211;help</code></p>
<dd>Display help.</p>
<dt><code>-f &lt;path&gt;|&#8211;logfile=&lt;path&gt;</code></p>
<dd>Write log messages to the given log file. When &#8216;-&#8216; is used as &lt;path&gt;, log messages are written to the standard output. If &#8216;<code>-f</code>&#8216; and &#8216;<code>-s</code>&#8216; are used together, the logs are sent to both destinations. </p>
<dt><code>-s[facility]|&#8211;syslog=[facility]</code></p>
<dd>Write log messages to syslog. The default facility is DAEMON. If &#8216;<code>-f</code>&#8216; and &#8216;<code>-s</code>&#8216; are used together, the logs are sent to both destinations.</p>
<dt><code>-n|&#8211;nodaemon</code></p>
<dd>Don&#8217;t fork the daemon, stay in the foreground.</p>
<dt><code>-v|&#8211;verbose</code></p>
<dd>Display more log messages. This option can be used three times to enable more verbose log messages.</p>
<dt><code>-q|&#8211;quiet</code></p>
<dd>Display less log messages.</p>
<dt><code>-Q|&#8211;nolog</code></p>
<dd>Disable logging.</p>
<dt><code>-d|&#8211;debug</code></p>
<dd>Equivalent to &#8216;-nvvvf -&#8216;, i.e. don&#8217;t fork the daemon, display all log messages and write them to the standard output.</p>
<dt><code>-u &lt;user&gt;|&#8211;socket-user=&lt;user&gt;</code></p>
<dd><code>-g &lt;group&gt;|&#8211;socket-group=&lt;group&gt;</code> Set the owner of cgrulesengd socket. Assumes that <code>cgexec</code> runs with proper suid permissions so it can write to the socket when <code>cgexec</code> &#8211;sticky is used. </p>
</dl>
<h2>Environment Variables</h2>
<dl>
<dt><code>CGROUP_LOGLEVEL</code></p>
<dd>controls verbosity of the tool. Allowed values are <code>DEBUG</code>, <code>INFO</code>, <code>WARNING</code> or <code>ERROR</code>. </p>
</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/cgrules.conf</code></p>
<dd>the default libcgroup configuration file</p>
<dt><code>/etc/cgconfig.conf</code></p>
<dd>the default templates file</p>
<dt><code>/etc/cgconfig.d/</code></p>
<dd>the default templates directory </p>
</dl>
<h2>See Also</h2>
<p>cgrules.conf (5) </p>

---
title: "rootsh(1)"
name: "rootsh"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rootsh/"
description: "rootsh – a logging wrapper for shells"
---

<h2>NAME</h2>
<p> rootsh &#8211; a logging wrapper for shells</p>
<h2>SYNOPSIS</h2>
<p> <code>rootsh</code> [<i>OPTION</i>]&#8230; [<i>&#8212;</i>] [<i>COMMANDS</i>]</p>
<h2>DESCRIPTION</h2>
<p> Start a shell with logging of input/output. Rootsh must be started via sudo if you want to become root. It does not raise your privileges on it&#8217;s own. You can run rootsh as a standalone application if you only want to log your own user&#8217;s session. If you call rootsh with additional commands, these will be passed to the shell.</p>
<dl>
<dt><code>-i</code>, <code>&#8211;initial</code></p>
<dd> Make the shell a login shell</p>
<dt><code>-u</code>, <code>&#8211;user</code>=<i>USER</i></p>
<dd> Run the shell as a non-root user</p>
<dt><code>-f</code>, <code>&#8211;logfile=</code><i>FILE</i></p>
<dd> Name of the file you want to write the logs (standalone only)</p>
<dt><code>-d</code>, <code>&#8211;logdir=</code><i>DIR</i></p>
<dd> Directory where you want your logfile written (standalone only)</p>
<dt><code>&#8211;no-logfile</code></p>
<dd> Switch off logging to a file (standalone only)</p>
<dt><code>&#8211;no-syslog</code></p>
<dd> Switch off logging to syslog (standalone only)</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display this help and exit</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Output version and capability information and exit</p>
<dt><code>&#8212;</code></p>
<dd> Stop scanning for command line options. Everything found after &#8212; will be passed to the shell with -c</dl>
<p> No parameters mean start a rootshell</p>
<h2>EXAMPLES</h2>
<dl>
<dt><code>sudo rootsh</code></p>
<dd> Start a logged root shell</p>
<dt><code>sudo rootsh -u oracle</code></p>
<dd> Start a logged shell in the context of user oracle.</p>
<dt><code>rootsh -f mysession.log &#8211;no-syslog</code></p>
<dd> Start a new shell for your user id, write protocol into mysession.log, do not send anything to syslog. This is identical to &quot;script -f mysession.log&quot;</p>
<dt><code>rootsh -i -u oracle lsnrctl stop</code></p>
<dd> Run command &quot;lsnrctl stop&quot; as user oracle. (this will call sh -c &quot;lsnrctl stop&quot;)</p>
<dt><code>rootsh -i -u oracle &#8212; ls -l</code></p>
<dd> Run command &quot;ls -l&quot; as user oracle. (this will call sh -c &quot;ls -l&quot;)</dl>
<h2>REPORTING BUGS</h2>
<p> Report bugs to Corey Henderson &lt;corman [at] cormander.com&gt;</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>rootsh</code> can be found at <a rel="nofollow" href="http://www.sourceforge.net/projects/rootsh">http://www.sourceforge.net/projects/rootsh</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2007 Free Software Foundation, Inc.<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>

---
title: "bacula-dir(8)"
name: "bacula-dir"
section: "8"
letter: "b"
url: "/docs/linux/man/8-bacula-dir/"
description: "bacula-dir – Bacula Director"
---

<p><code>bacula-dir</code> &#8211; Bacula Director</p>
<h2>Synopsis</h2>
<p><code>bacula-dir</code> [<i>options</i>]</p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>bacula-dir</code> command.<br />
 Bacula&#8217;s Director Daemon acts as the controller of the network backup system: it is responsible for scheduling and coordinating backups across the network.</p>
<h2>Options</h2>
<dl>
<dt><code>-c&nbsp;<wbr></code><i>file</i></p>
<dd>Specify the configuration file to use.</p>
<dt><code>-d&nbsp;<wbr></code><i>nn</i></p>
<dd>Set debug level to <i>nn</i>.</p>
<dt><code>-dt</code></p>
<dd>Print timestamp in debug output.</p>
<dt><code>-f</code></p>
<dd>Run in foreground (for debugging).</p>
<dt><code>-g&nbsp;<wbr></code><i>group</i></p>
<dd>Set the group/gid to run as.</p>
<dt><code>-m</code></p>
<dd>Print kaboom output (for debugging)</p>
<dt><code>-r&nbsp;<wbr></code><i>job</i></p>
<dd>Run &lt;job&gt;.</p>
<dt><code>-s</code></p>
<dd>No signals (for debugging).</p>
<dt><code>-t</code></p>
<dd>Test the configuration file and report errors.</p>
<dt><code>-u&nbsp;<wbr></code><i>user</i></p>
<dd>Set the username/uid to run as.</p>
<dt><code>-v</code></p>
<dd>Set verbose mode.</p>
<dt><code>-?</code></p>
<dd>Show version and usage of program.</dl>
<h2>Tcp-Wrappers Configuration</h2>
<p>Tcpwrappers looks for the service name of the bacula daemons in <i>hosts.allow</i> , and the service names of these daemons is configured to be different from the binary. The service names are configured to be <code>%hostname%-%component%</code> rather than <code>bacula-dir</code> (As defined in the bacula-dir.conf.in file) </p>
<p> So the hosts.allow entry has to match <code>%hostname%-%component%</code> (servername-dir for example) instead of bacula-%component% </p>
<p> <code>WARNING:</code> This means that if the hosts.allow file has the entry: </p>
<p> <code>bacula-dir: ALL</code> </p>
<p> you will not be able to run bconsole to connect to the local director! </p>
<p> The entry would have to read: </p>
<p> <code>server-dir: ALL</code> </p>
<p> and this will allow the console to connect to the director. (The process running is bacula-dir.)</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-bacula-fd/">bacula-fd</a></code>(8), <code><a href="/docs/linux/man/8-bacula-sd/">bacula-sd</a></code>(8). </p>
<h2>Author</h2>
<p>This manual page was written by Jose Luis Tallon &lt;jltallon [at] adv-solutions.net&gt;.</p>

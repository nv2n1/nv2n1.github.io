---
title: "fail2ban-client(1)"
name: "fail2ban-client"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fail2ban-client/"
description: "fail2ban-client – configure and control the server"
---

<h2>NAME</h2>
<p> fail2ban-client &#8211; configure and control the server</p>
<h2>SYNOPSIS</h2>
<p> <code>fail2ban-client</code> [<i>,OPTIONS/</i>] <i>,&lt;COMMAND&gt;/</i></p>
<h2>DESCRIPTION</h2>
<p> Fail2Ban v0.9.6 reads log file that contains password failure report and bans the corresponding IP addresses using firewall rules.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code> &lt;DIR&gt;</p>
<dd> configuration directory</p>
<dt><code>-s</code> &lt;FILE&gt;</p>
<dd> socket path</p>
<dt><code>-p</code> &lt;FILE&gt;</p>
<dd> pidfile path</p>
<dt><code>-d</code></p>
<dd> dump configuration. For debugging</p>
<dt><code>-i</code></p>
<dd> interactive mode</p>
<dt><code>-v</code></p>
<dd> increase verbosity</p>
<dt><code>-q</code></p>
<dd> decrease verbosity</p>
<dt><code>-x</code></p>
<dd> force execution of the server (remove socket file)</p>
<dt><code>-b</code></p>
<dd> start server in background (default)</p>
<dt><code>-f</code></p>
<dd> start server in foreground (note that the client forks once itself)</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> display this help message</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> print the version</dl>
<h2>COMMAND</h2>
<dl>
<dt>
<dd> BASIC</p>
<dt><code>start</code></p>
<dd> starts the server and the jails</p>
<dt><code>reload</code></p>
<dd> reloads the configuration</p>
<dt><code>reload &lt;JAIL&gt;</code></p>
<dd> reloads the jail &lt;JAIL&gt;</p>
<dt><code>stop</code></p>
<dd> stops all jails and terminate the server</p>
<dt><code>status</code></p>
<dd> gets the current status of the server</p>
<dt><code>ping</code></p>
<dd> tests if the server is alive</p>
<dt><code>help</code></p>
<dd> return this output</p>
<dt><code>version</code></p>
<dd> return the server version</p>
<dt>
<dd> LOGGING</p>
<dt><code>set loglevel &lt;LEVEL&gt;</code></p>
<dd> sets logging level to &lt;LEVEL&gt;. Levels: CRITICAL, ERROR, WARNING, NOTICE, INFO, DEBUG</p>
<dt><code>get loglevel</code></p>
<dd> gets the logging level</p>
<dt><code>set logtarget &lt;TARGET&gt;</code></p>
<dd> sets logging target to &lt;TARGET&gt;. Can be STDOUT, STDERR, SYSLOG or a file</p>
<dt><code>get logtarget</code></p>
<dd> gets logging target</p>
<dt><code>set syslogsocket auto|&lt;SOCKET&gt;</code></p>
<dd> sets the syslog socket path to auto or &lt;SOCKET&gt;. Only used if logtarget is SYSLOG</p>
<dt><code>get syslogsocket</code></p>
<dd> gets syslog socket path</p>
<dt><code>flushlogs</code></p>
<dd> flushes the logtarget if a file and reopens it. For log rotation.</p>
<dt>
<dd> DATABASE</p>
<dt><code>set dbfile &lt;FILE&gt;</code></p>
<dd> set the location of fail2ban persistent datastore. Set to &quot;None&quot; to disable</p>
<dt><code>get dbfile</code></p>
<dd> get the location of fail2ban persistent datastore</p>
<dt><code>set dbpurgeage &lt;SECONDS&gt;</code></p>
<dd> sets the max age in &lt;SECONDS&gt; that history of bans will be kept</p>
<dt><code>get dbpurgeage</code></p>
<dd> gets the max age in seconds that history of bans will be kept</p>
<dt>
<dd> JAIL CONTROL</p>
<dt><code>add &lt;JAIL&gt; &lt;BACKEND&gt;</code></p>
<dd> creates &lt;JAIL&gt; using &lt;BACKEND&gt;</p>
<dt><code>start &lt;JAIL&gt;</code></p>
<dd> starts the jail &lt;JAIL&gt;</p>
<dt><code>stop &lt;JAIL&gt;</code></p>
<dd> stops the jail &lt;JAIL&gt;. The jail is removed</p>
<dt><code>status &lt;JAIL&gt; [FLAVOR]</code></p>
<dd> gets the current status of &lt;JAIL&gt;, with optional flavor or extended info</p>
<dt>
<dd> JAIL CONFIGURATION</p>
<dt><code>set &lt;JAIL&gt; idle on|off</code></p>
<dd> sets the idle state of &lt;JAIL&gt;</p>
<dt><code>set &lt;JAIL&gt; addignoreip &lt;IP&gt;</code></p>
<dd> adds &lt;IP&gt; to the ignore list of &lt;JAIL&gt;</p>
<dt><code>set &lt;JAIL&gt; delignoreip &lt;IP&gt;</code></p>
<dd> removes &lt;IP&gt; from the ignore list of &lt;JAIL&gt;</p>
<dt><code>set &lt;JAIL&gt; addlogpath &lt;FILE&gt; [&#8216;tail&#8217;]</code></p>
<dd> adds &lt;FILE&gt; to the monitoring list of &lt;JAIL&gt;, optionally starting at the &#8216;tail&#8217; of the file (default &#8216;head&#8217;).</p>
<dt><code>set &lt;JAIL&gt; dellogpath &lt;FILE&gt;</code></p>
<dd> removes &lt;FILE&gt; from the monitoring list of &lt;JAIL&gt;</p>
<dt><code>set &lt;JAIL&gt; logencoding &lt;ENCODING&gt;</code></p>
<dd> sets the &lt;ENCODING&gt; of the log files for &lt;JAIL&gt;</p>
<dt><code>set &lt;JAIL&gt; addjournalmatch &lt;MATCH&gt;</code></p>
<dd> adds &lt;MATCH&gt; to the journal filter of &lt;JAIL&gt;</p>
<dt><code>set &lt;JAIL&gt; deljournalmatch &lt;MATCH&gt;</code></p>
<dd> removes &lt;MATCH&gt; from the journal filter of &lt;JAIL&gt;</p>
<dt><code>set &lt;JAIL&gt; addfailregex &lt;REGEX&gt;</code></p>
<dd> adds the regular expression &lt;REGEX&gt; which must match failures for &lt;JAIL&gt;</p>
<dt><code>set &lt;JAIL&gt; delfailregex &lt;INDEX&gt;</code></p>
<dd> removes the regular expression at &lt;INDEX&gt; for failregex</p>
<dt><code>set &lt;JAIL&gt; ignorecommand &lt;VALUE&gt;</code></p>
<dd> sets ignorecommand of &lt;JAIL&gt;</p>
<dt><code>set &lt;JAIL&gt; addignoreregex &lt;REGEX&gt;</code></p>
<dd> adds the regular expression &lt;REGEX&gt; which should match pattern to exclude for &lt;JAIL&gt;</p>
<dt><code>set &lt;JAIL&gt; delignoreregex &lt;INDEX&gt;</code></p>
<dd> removes the regular expression at &lt;INDEX&gt; for ignoreregex</p>
<dt><code>set &lt;JAIL&gt; findtime &lt;TIME&gt;</code></p>
<dd> sets the number of seconds &lt;TIME&gt; for which the filter will look back for &lt;JAIL&gt;</p>
<dt><code>set &lt;JAIL&gt; bantime &lt;TIME&gt;</code></p>
<dd> sets the number of seconds &lt;TIME&gt; a host will be banned for &lt;JAIL&gt;</p>
<dt><code>set &lt;JAIL&gt; datepattern &lt;PATTERN&gt;</code></p>
<dd> sets the &lt;PATTERN&gt; used to match date/times for &lt;JAIL&gt;</p>
<dt><code>set &lt;JAIL&gt; usedns &lt;VALUE&gt;</code></p>
<dd> sets the usedns mode for &lt;JAIL&gt;</p>
<dt><code>set &lt;JAIL&gt; banip &lt;IP&gt;</code></p>
<dd> manually Ban &lt;IP&gt; for &lt;JAIL&gt;</p>
<dt><code>set &lt;JAIL&gt; unbanip &lt;IP&gt;</code></p>
<dd> manually Unban &lt;IP&gt; in &lt;JAIL&gt;</p>
<dt><code>set &lt;JAIL&gt; maxretry &lt;RETRY&gt;</code></p>
<dd> sets the number of failures &lt;RETRY&gt; before banning the host for &lt;JAIL&gt;</p>
<dt><code>set &lt;JAIL&gt; maxlines &lt;LINES&gt;</code></p>
<dd> sets the number of &lt;LINES&gt; to buffer for regex search for &lt;JAIL&gt;</p>
<dt><code>set &lt;JAIL&gt; addaction &lt;ACT&gt;[ &lt;PYTHONFILE&gt; &lt;JSONKWARGS&gt;]</code></p>
<dd> adds a new action named &lt;ACT&gt; for &lt;JAIL&gt;. Optionally for a Python based action, a &lt;PYTHONFILE&gt; and &lt;JSONKWARGS&gt; can be specified, else will be a Command Action</p>
<dt><code>set &lt;JAIL&gt; delaction &lt;ACT&gt;</code></p>
<dd> removes the action &lt;ACT&gt; from &lt;JAIL&gt;</p>
<dt>
<dd> COMMAND ACTION CONFIGURATION</p>
<dt><code>set &lt;JAIL&gt; action &lt;ACT&gt; actionstart &lt;CMD&gt;</code></p>
<dd> sets the start command &lt;CMD&gt; of the action &lt;ACT&gt; for &lt;JAIL&gt;</p>
<dt><code>set &lt;JAIL&gt; action &lt;ACT&gt; actionstop &lt;CMD&gt; sets the stop command &lt;CMD&gt; of the</code></p>
<dd> action &lt;ACT&gt; for &lt;JAIL&gt;</p>
<dt><code>set &lt;JAIL&gt; action &lt;ACT&gt; actioncheck &lt;CMD&gt;</code></p>
<dd> sets the check command &lt;CMD&gt; of the action &lt;ACT&gt; for &lt;JAIL&gt;</p>
<dt><code>set &lt;JAIL&gt; action &lt;ACT&gt; actionban &lt;CMD&gt;</code></p>
<dd> sets the ban command &lt;CMD&gt; of the action &lt;ACT&gt; for &lt;JAIL&gt;</p>
<dt><code>set &lt;JAIL&gt; action &lt;ACT&gt; actionunban &lt;CMD&gt;</code></p>
<dd> sets the unban command &lt;CMD&gt; of the action &lt;ACT&gt; for &lt;JAIL&gt;</p>
<dt><code>set &lt;JAIL&gt; action &lt;ACT&gt; timeout &lt;TIMEOUT&gt;</code></p>
<dd> sets &lt;TIMEOUT&gt; as the command timeout in seconds for the action &lt;ACT&gt; for &lt;JAIL&gt;</p>
<dt>
<dd> GENERAL ACTION CONFIGURATION</p>
<dt><code>set &lt;JAIL&gt; action &lt;ACT&gt; &lt;PROPERTY&gt; &lt;VALUE&gt;</code></p>
<dd> sets the &lt;VALUE&gt; of &lt;PROPERTY&gt; for the action &lt;ACT&gt; for &lt;JAIL&gt;</p>
<dt><code>set &lt;JAIL&gt; action &lt;ACT&gt; &lt;METHOD&gt;[ &lt;JSONKWARGS&gt;]</code></p>
<dd> calls the &lt;METHOD&gt; with &lt;JSONKWARGS&gt; for the action &lt;ACT&gt; for &lt;JAIL&gt;</p>
<dt>
<dd> JAIL INFORMATION</p>
<dt><code>get &lt;JAIL&gt; logpath</code></p>
<dd> gets the list of the monitored files for &lt;JAIL&gt;</p>
<dt><code>get &lt;JAIL&gt; logencoding</code></p>
<dd> gets the encoding of the log files for &lt;JAIL&gt;</p>
<dt><code>get &lt;JAIL&gt; journalmatch</code></p>
<dd> gets the journal filter match for &lt;JAIL&gt;</p>
<dt><code>get &lt;JAIL&gt; ignoreip</code></p>
<dd> gets the list of ignored IP addresses for &lt;JAIL&gt;</p>
<dt><code>get &lt;JAIL&gt; ignorecommand</code></p>
<dd> gets ignorecommand of &lt;JAIL&gt;</p>
<dt><code>get &lt;JAIL&gt; failregex</code></p>
<dd> gets the list of regular expressions which matches the failures for &lt;JAIL&gt;</p>
<dt><code>get &lt;JAIL&gt; ignoreregex</code></p>
<dd> gets the list of regular expressions which matches patterns to ignore for &lt;JAIL&gt;</p>
<dt><code>get &lt;JAIL&gt; findtime</code></p>
<dd> gets the time for which the filter will look back for failures for &lt;JAIL&gt;</p>
<dt><code>get &lt;JAIL&gt; bantime</code></p>
<dd> gets the time a host is banned for &lt;JAIL&gt;</p>
<dt><code>get &lt;JAIL&gt; datepattern</code></p>
<dd> gets the patern used to match date/times for &lt;JAIL&gt;</p>
<dt><code>get &lt;JAIL&gt; usedns</code></p>
<dd> gets the usedns setting for &lt;JAIL&gt;</p>
<dt><code>get &lt;JAIL&gt; maxretry</code></p>
<dd> gets the number of failures allowed for &lt;JAIL&gt;</p>
<dt><code>get &lt;JAIL&gt; maxlines</code></p>
<dd> gets the number of lines to buffer for &lt;JAIL&gt;</p>
<dt><code>get &lt;JAIL&gt; actions</code></p>
<dd> gets a list of actions for &lt;JAIL&gt;</p>
<dt>
<dd> COMMAND ACTION INFORMATION</p>
<dt><code>get &lt;JAIL&gt; action &lt;ACT&gt; actionstart</code></p>
<dd> gets the start command for the action &lt;ACT&gt; for &lt;JAIL&gt;</p>
<dt><code>get &lt;JAIL&gt; action &lt;ACT&gt; actionstop</code></p>
<dd> gets the stop command for the action &lt;ACT&gt; for &lt;JAIL&gt;</p>
<dt><code>get &lt;JAIL&gt; action &lt;ACT&gt; actioncheck</code></p>
<dd> gets the check command for the action &lt;ACT&gt; for &lt;JAIL&gt;</p>
<dt><code>get &lt;JAIL&gt; action &lt;ACT&gt; actionban</code></p>
<dd> gets the ban command for the action &lt;ACT&gt; for &lt;JAIL&gt;</p>
<dt><code>get &lt;JAIL&gt; action &lt;ACT&gt; actionunban</code></p>
<dd> gets the unban command for the action &lt;ACT&gt; for &lt;JAIL&gt;</p>
<dt><code>get &lt;JAIL&gt; action &lt;ACT&gt; timeout</code></p>
<dd> gets the command timeout in seconds for the action &lt;ACT&gt; for &lt;JAIL&gt;</p>
<dt>
<dd> GENERAL ACTION INFORMATION</p>
<dt><code>get &lt;JAIL&gt; actionproperties &lt;ACT&gt;</code></p>
<dd> gets a list of properties for the action &lt;ACT&gt; for &lt;JAIL&gt;</p>
<dt><code>get &lt;JAIL&gt; actionmethods &lt;ACT&gt;</code></p>
<dd> gets a list of methods for the action &lt;ACT&gt; for &lt;JAIL&gt;</p>
<dt><code>get &lt;JAIL&gt; action &lt;ACT&gt; &lt;PROPERTY&gt;</code></p>
<dd> gets the value of &lt;PROPERTY&gt; for the action &lt;ACT&gt; for &lt;JAIL&gt;</dl>
<h2>FILES</h2>
<p> <i>/etc/fail2ban/*</i></p>
<h2>AUTHOR</h2>
<p> Written by Cyril Jaquier &lt;cyril.jaquier [at] fail2ban.org&gt;. Many contributions by Yaroslav O. Halchenko &lt;debian [at] onerussian.com&gt;.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to <a rel="nofollow" href="https://github.com/fail2ban/fail2ban/issues">https://github.com/fail2ban/fail2ban/issues</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2004-2008 Cyril Jaquier, 2008- Fail2Ban Contributors<br />
 Copyright of modifications held by their respective authors. Licensed under the GNU General Public License v2 (GPL).</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-fail2ban-server/">fail2ban-server</a>(1) <a href="/docs/linux/man/5-jail-conf/">jail.conf</a>(5) </p>
<h2>Index</h2>

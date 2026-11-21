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
<p> <code>fail2ban-client</code> [<i>,OPTIONS/</i>] <i>,&lt;COMMAND&gt;/</i></p>
<p> Fail2Ban v0.9.6 reads log file that contains password failure report and bans the corresponding IP addresses using firewall rules.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code> &lt;DIR&gt;</dt>
<dd> configuration directory</dd>
<dt><code>-s</code> &lt;FILE&gt;</dt>
<dd> socket path</dd>
<dt><code>-p</code> &lt;FILE&gt;</dt>
<dd> pidfile path</dd>
<dt><code>-d</code></dt>
<dd> dump configuration. For debugging</dd>
<dt><code>-i</code></dt>
<dd> interactive mode</dd>
<dt><code>-v</code></dt>
<dd> increase verbosity</dd>
<dt><code>-q</code></dt>
<dd> decrease verbosity</dd>
<dt><code>-x</code></dt>
<dd> force execution of the server (remove socket file)</dd>
<dt><code>-b</code></dt>
<dd> start server in background (default)</dd>
<dt><code>-f</code></dt>
<dd> start server in foreground (note that the client forks once itself)</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> display this help message</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> print the version</dd></dl>
<h2>COMMAND</h2>
<dl>
<dt>
</dt><dd> BASIC</dd>
<dt><code>start</code></dt>
<dd> starts the server and the jails</dd>
<dt><code>reload</code></dt>
<dd> reloads the configuration</dd>
<dt><code>reload &lt;JAIL&gt;</code></dt>
<dd> reloads the jail &lt;JAIL&gt;</dd>
<dt><code>stop</code></dt>
<dd> stops all jails and terminate the server</dd>
<dt><code>status</code></dt>
<dd> gets the current status of the server</dd>
<dt><code>ping</code></dt>
<dd> tests if the server is alive</dd>
<dt><code>help</code></dt>
<dd> return this output</dd>
<dt><code>version</code></dt>
<dd> return the server version</dd>
<dt>
</dt><dd> LOGGING</dd>
<dt><code>set loglevel &lt;LEVEL&gt;</code></dt>
<dd> sets logging level to &lt;LEVEL&gt;. Levels: CRITICAL, ERROR, WARNING, NOTICE, INFO, DEBUG</dd>
<dt><code>get loglevel</code></dt>
<dd> gets the logging level</dd>
<dt><code>set logtarget &lt;TARGET&gt;</code></dt>
<dd> sets logging target to &lt;TARGET&gt;. Can be STDOUT, STDERR, SYSLOG or a file</dd>
<dt><code>get logtarget</code></dt>
<dd> gets logging target</dd>
<dt><code>set syslogsocket auto|&lt;SOCKET&gt;</code></dt>
<dd> sets the syslog socket path to auto or &lt;SOCKET&gt;. Only used if logtarget is SYSLOG</dd>
<dt><code>get syslogsocket</code></dt>
<dd> gets syslog socket path</dd>
<dt><code>flushlogs</code></dt>
<dd> flushes the logtarget if a file and reopens it. For log rotation.</dd>
<dt>
</dt><dd> DATABASE</dd>
<dt><code>set dbfile &lt;FILE&gt;</code></dt>
<dd> set the location of fail2ban persistent datastore. Set to &quot;None&quot; to disable</dd>
<dt><code>get dbfile</code></dt>
<dd> get the location of fail2ban persistent datastore</dd>
<dt><code>set dbpurgeage &lt;SECONDS&gt;</code></dt>
<dd> sets the max age in &lt;SECONDS&gt; that history of bans will be kept</dd>
<dt><code>get dbpurgeage</code></dt>
<dd> gets the max age in seconds that history of bans will be kept</dd>
<dt>
</dt><dd> JAIL CONTROL</dd>
<dt><code>add &lt;JAIL&gt; &lt;BACKEND&gt;</code></dt>
<dd> creates &lt;JAIL&gt; using &lt;BACKEND&gt;</dd>
<dt><code>start &lt;JAIL&gt;</code></dt>
<dd> starts the jail &lt;JAIL&gt;</dd>
<dt><code>stop &lt;JAIL&gt;</code></dt>
<dd> stops the jail &lt;JAIL&gt;. The jail is removed</dd>
<dt><code>status &lt;JAIL&gt; [FLAVOR]</code></dt>
<dd> gets the current status of &lt;JAIL&gt;, with optional flavor or extended info</dd>
<dt>
</dt><dd> JAIL CONFIGURATION</dd>
<dt><code>set &lt;JAIL&gt; idle on|off</code></dt>
<dd> sets the idle state of &lt;JAIL&gt;</dd>
<dt><code>set &lt;JAIL&gt; addignoreip &lt;IP&gt;</code></dt>
<dd> adds &lt;IP&gt; to the ignore list of &lt;JAIL&gt;</dd>
<dt><code>set &lt;JAIL&gt; delignoreip &lt;IP&gt;</code></dt>
<dd> removes &lt;IP&gt; from the ignore list of &lt;JAIL&gt;</dd>
<dt><code>set &lt;JAIL&gt; addlogpath &lt;FILE&gt; [&#8216;tail&#8217;]</code></dt>
<dd> adds &lt;FILE&gt; to the monitoring list of &lt;JAIL&gt;, optionally starting at the &#8216;tail&#8217; of the file (default &#8216;head&#8217;).</dd>
<dt><code>set &lt;JAIL&gt; dellogpath &lt;FILE&gt;</code></dt>
<dd> removes &lt;FILE&gt; from the monitoring list of &lt;JAIL&gt;</dd>
<dt><code>set &lt;JAIL&gt; logencoding &lt;ENCODING&gt;</code></dt>
<dd> sets the &lt;ENCODING&gt; of the log files for &lt;JAIL&gt;</dd>
<dt><code>set &lt;JAIL&gt; addjournalmatch &lt;MATCH&gt;</code></dt>
<dd> adds &lt;MATCH&gt; to the journal filter of &lt;JAIL&gt;</dd>
<dt><code>set &lt;JAIL&gt; deljournalmatch &lt;MATCH&gt;</code></dt>
<dd> removes &lt;MATCH&gt; from the journal filter of &lt;JAIL&gt;</dd>
<dt><code>set &lt;JAIL&gt; addfailregex &lt;REGEX&gt;</code></dt>
<dd> adds the regular expression &lt;REGEX&gt; which must match failures for &lt;JAIL&gt;</dd>
<dt><code>set &lt;JAIL&gt; delfailregex &lt;INDEX&gt;</code></dt>
<dd> removes the regular expression at &lt;INDEX&gt; for failregex</dd>
<dt><code>set &lt;JAIL&gt; ignorecommand &lt;VALUE&gt;</code></dt>
<dd> sets ignorecommand of &lt;JAIL&gt;</dd>
<dt><code>set &lt;JAIL&gt; addignoreregex &lt;REGEX&gt;</code></dt>
<dd> adds the regular expression &lt;REGEX&gt; which should match pattern to exclude for &lt;JAIL&gt;</dd>
<dt><code>set &lt;JAIL&gt; delignoreregex &lt;INDEX&gt;</code></dt>
<dd> removes the regular expression at &lt;INDEX&gt; for ignoreregex</dd>
<dt><code>set &lt;JAIL&gt; findtime &lt;TIME&gt;</code></dt>
<dd> sets the number of seconds &lt;TIME&gt; for which the filter will look back for &lt;JAIL&gt;</dd>
<dt><code>set &lt;JAIL&gt; bantime &lt;TIME&gt;</code></dt>
<dd> sets the number of seconds &lt;TIME&gt; a host will be banned for &lt;JAIL&gt;</dd>
<dt><code>set &lt;JAIL&gt; datepattern &lt;PATTERN&gt;</code></dt>
<dd> sets the &lt;PATTERN&gt; used to match date/times for &lt;JAIL&gt;</dd>
<dt><code>set &lt;JAIL&gt; usedns &lt;VALUE&gt;</code></dt>
<dd> sets the usedns mode for &lt;JAIL&gt;</dd>
<dt><code>set &lt;JAIL&gt; banip &lt;IP&gt;</code></dt>
<dd> manually Ban &lt;IP&gt; for &lt;JAIL&gt;</dd>
<dt><code>set &lt;JAIL&gt; unbanip &lt;IP&gt;</code></dt>
<dd> manually Unban &lt;IP&gt; in &lt;JAIL&gt;</dd>
<dt><code>set &lt;JAIL&gt; maxretry &lt;RETRY&gt;</code></dt>
<dd> sets the number of failures &lt;RETRY&gt; before banning the host for &lt;JAIL&gt;</dd>
<dt><code>set &lt;JAIL&gt; maxlines &lt;LINES&gt;</code></dt>
<dd> sets the number of &lt;LINES&gt; to buffer for regex search for &lt;JAIL&gt;</dd>
<dt><code>set &lt;JAIL&gt; addaction &lt;ACT&gt;[ &lt;PYTHONFILE&gt; &lt;JSONKWARGS&gt;]</code></dt>
<dd> adds a new action named &lt;ACT&gt; for &lt;JAIL&gt;. Optionally for a Python based action, a &lt;PYTHONFILE&gt; and &lt;JSONKWARGS&gt; can be specified, else will be a Command Action</dd>
<dt><code>set &lt;JAIL&gt; delaction &lt;ACT&gt;</code></dt>
<dd> removes the action &lt;ACT&gt; from &lt;JAIL&gt;</dd>
<dt>
</dt><dd> COMMAND ACTION CONFIGURATION</dd>
<dt><code>set &lt;JAIL&gt; action &lt;ACT&gt; actionstart &lt;CMD&gt;</code></dt>
<dd> sets the start command &lt;CMD&gt; of the action &lt;ACT&gt; for &lt;JAIL&gt;</dd>
<dt><code>set &lt;JAIL&gt; action &lt;ACT&gt; actionstop &lt;CMD&gt; sets the stop command &lt;CMD&gt; of the</code></dt>
<dd> action &lt;ACT&gt; for &lt;JAIL&gt;</dd>
<dt><code>set &lt;JAIL&gt; action &lt;ACT&gt; actioncheck &lt;CMD&gt;</code></dt>
<dd> sets the check command &lt;CMD&gt; of the action &lt;ACT&gt; for &lt;JAIL&gt;</dd>
<dt><code>set &lt;JAIL&gt; action &lt;ACT&gt; actionban &lt;CMD&gt;</code></dt>
<dd> sets the ban command &lt;CMD&gt; of the action &lt;ACT&gt; for &lt;JAIL&gt;</dd>
<dt><code>set &lt;JAIL&gt; action &lt;ACT&gt; actionunban &lt;CMD&gt;</code></dt>
<dd> sets the unban command &lt;CMD&gt; of the action &lt;ACT&gt; for &lt;JAIL&gt;</dd>
<dt><code>set &lt;JAIL&gt; action &lt;ACT&gt; timeout &lt;TIMEOUT&gt;</code></dt>
<dd> sets &lt;TIMEOUT&gt; as the command timeout in seconds for the action &lt;ACT&gt; for &lt;JAIL&gt;</dd>
<dt>
</dt><dd> GENERAL ACTION CONFIGURATION</dd>
<dt><code>set &lt;JAIL&gt; action &lt;ACT&gt; &lt;PROPERTY&gt; &lt;VALUE&gt;</code></dt>
<dd> sets the &lt;VALUE&gt; of &lt;PROPERTY&gt; for the action &lt;ACT&gt; for &lt;JAIL&gt;</dd>
<dt><code>set &lt;JAIL&gt; action &lt;ACT&gt; &lt;METHOD&gt;[ &lt;JSONKWARGS&gt;]</code></dt>
<dd> calls the &lt;METHOD&gt; with &lt;JSONKWARGS&gt; for the action &lt;ACT&gt; for &lt;JAIL&gt;</dd>
<dt>
</dt><dd> JAIL INFORMATION</dd>
<dt><code>get &lt;JAIL&gt; logpath</code></dt>
<dd> gets the list of the monitored files for &lt;JAIL&gt;</dd>
<dt><code>get &lt;JAIL&gt; logencoding</code></dt>
<dd> gets the encoding of the log files for &lt;JAIL&gt;</dd>
<dt><code>get &lt;JAIL&gt; journalmatch</code></dt>
<dd> gets the journal filter match for &lt;JAIL&gt;</dd>
<dt><code>get &lt;JAIL&gt; ignoreip</code></dt>
<dd> gets the list of ignored IP addresses for &lt;JAIL&gt;</dd>
<dt><code>get &lt;JAIL&gt; ignorecommand</code></dt>
<dd> gets ignorecommand of &lt;JAIL&gt;</dd>
<dt><code>get &lt;JAIL&gt; failregex</code></dt>
<dd> gets the list of regular expressions which matches the failures for &lt;JAIL&gt;</dd>
<dt><code>get &lt;JAIL&gt; ignoreregex</code></dt>
<dd> gets the list of regular expressions which matches patterns to ignore for &lt;JAIL&gt;</dd>
<dt><code>get &lt;JAIL&gt; findtime</code></dt>
<dd> gets the time for which the filter will look back for failures for &lt;JAIL&gt;</dd>
<dt><code>get &lt;JAIL&gt; bantime</code></dt>
<dd> gets the time a host is banned for &lt;JAIL&gt;</dd>
<dt><code>get &lt;JAIL&gt; datepattern</code></dt>
<dd> gets the patern used to match date/times for &lt;JAIL&gt;</dd>
<dt><code>get &lt;JAIL&gt; usedns</code></dt>
<dd> gets the usedns setting for &lt;JAIL&gt;</dd>
<dt><code>get &lt;JAIL&gt; maxretry</code></dt>
<dd> gets the number of failures allowed for &lt;JAIL&gt;</dd>
<dt><code>get &lt;JAIL&gt; maxlines</code></dt>
<dd> gets the number of lines to buffer for &lt;JAIL&gt;</dd>
<dt><code>get &lt;JAIL&gt; actions</code></dt>
<dd> gets a list of actions for &lt;JAIL&gt;</dd>
<dt>
</dt><dd> COMMAND ACTION INFORMATION</dd>
<dt><code>get &lt;JAIL&gt; action &lt;ACT&gt; actionstart</code></dt>
<dd> gets the start command for the action &lt;ACT&gt; for &lt;JAIL&gt;</dd>
<dt><code>get &lt;JAIL&gt; action &lt;ACT&gt; actionstop</code></dt>
<dd> gets the stop command for the action &lt;ACT&gt; for &lt;JAIL&gt;</dd>
<dt><code>get &lt;JAIL&gt; action &lt;ACT&gt; actioncheck</code></dt>
<dd> gets the check command for the action &lt;ACT&gt; for &lt;JAIL&gt;</dd>
<dt><code>get &lt;JAIL&gt; action &lt;ACT&gt; actionban</code></dt>
<dd> gets the ban command for the action &lt;ACT&gt; for &lt;JAIL&gt;</dd>
<dt><code>get &lt;JAIL&gt; action &lt;ACT&gt; actionunban</code></dt>
<dd> gets the unban command for the action &lt;ACT&gt; for &lt;JAIL&gt;</dd>
<dt><code>get &lt;JAIL&gt; action &lt;ACT&gt; timeout</code></dt>
<dd> gets the command timeout in seconds for the action &lt;ACT&gt; for &lt;JAIL&gt;</dd>
<dt>
</dt><dd> GENERAL ACTION INFORMATION</dd>
<dt><code>get &lt;JAIL&gt; actionproperties &lt;ACT&gt;</code></dt>
<dd> gets a list of properties for the action &lt;ACT&gt; for &lt;JAIL&gt;</dd>
<dt><code>get &lt;JAIL&gt; actionmethods &lt;ACT&gt;</code></dt>
<dd> gets a list of methods for the action &lt;ACT&gt; for &lt;JAIL&gt;</dd>
<dt><code>get &lt;JAIL&gt; action &lt;ACT&gt; &lt;PROPERTY&gt;</code></dt>
<dd> gets the value of &lt;PROPERTY&gt; for the action &lt;ACT&gt; for &lt;JAIL&gt;</dd></dl>
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

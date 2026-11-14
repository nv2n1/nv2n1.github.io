---
title: "jail-conf(5)"
name: "jail-conf"
section: "5"
letter: "j"
url: "/docs/linux/man/5-jail-conf/"
description: "jail.conf – configuration for the fail2ban server"
---

<p>jail.conf &#8211; configuration for the fail2ban server</p>
<h2>Synopsis</h2>
<p><i>fail2ban.conf fail2ban.d/*.conf fail2ban.local fail2ban.d/*.local</i> <i>jail.conf jail.d/*.conf jail.local jail.d/*.local</i> <i>action.d/*.conf action.d/*.local action.d/*.py</i> <i>filter.d/*.conf filter.d/*.local</i> </p>
<h2>Description</h2>
<p>Fail2ban has four configuration file types:</p>
<dl>
<dt><i>fail2ban.conf</i></p>
<dd>Fail2Ban global configuration (such as logging)</p>
<dt><i>filter.d/*.conf</i></p>
<dd>Filters specifying how to detect authentication failures</p>
<dt><i>action.d/*.conf</i></p>
<dd>Actions defining the commands for banning and unbanning of IP address</p>
<dt><i>jail.conf</i></p>
<dd>Jails defining combinations of Filters with Actions. </p>
<h2>Configuration Files Format</h2>
<p><i>*.conf</i> files are distributed by Fail2Ban. It is recommended that *.conf files should remain unchanged to ease upgrades. If needed, customizations should be provided in <i>*.local</i> files. For example, if you would like to enable the [ssh-iptables-ipset] jail specified in jail.conf, create jail.local containing </p>
<dl>
<dt><i>jail.local</i></p>
<dd>[ssh-iptables-ipset] </p>
<p> enabled = true </p>
</dl>
<p> In .local files specify only the settings you would like to change and the rest of the configuration will then come from the corresponding .conf file which is parsed first. </p>
<dl>
<dt><i>jail.d/</i> and <i>fail2ban.d/</i></p>
<dd>In addition to .local, for jail.conf or fail2ban.conf file there can be a corresponding <i>.d/</i> directory containing additional .conf files. The order e.g. for <i>jail</i> configuration would be: </p>
<dl>
<dd>jail.conf</dl>
<dl>
<dd>jail.d/*.conf (in alphabetical order)</dl>
<dl>
<dd>jail.local</dl>
<dl>
<dd>jail.d/*.local (in alphabetical order). </p>
<p> i.e. all .local files are parsed after .conf files in the original configuration file and files under .d directory. Settings in the file parsed later take precedence over identical entries in previously parsed files. Files are ordered alphabetically, e.g. </p>
<p> <i>fail2ban.d/01_custom_log.conf</i> &#8211; to use a different log path</dl>
<dl>
<dd><i>jail.d/01_enable.conf</i> &#8211; to enable a specific jail</dl>
<dl>
<dd><i>jail.d/02_custom_port.conf</i> &#8211; to change the port(s) of a jail.</dl>
<p> Configuration files have sections, those specified with [section name], and name = value pairs. For those name items that can accept multiple values, specify the values separated by spaces, or in separate lines space indented at the beginning of the line before the second value. </p>
</dl>
<p> Configuration files can include other (defining common variables) configuration files, which is often used in Filters and Actions. Such inclusions are defined in a section called [INCLUDES]: </p>
<dl>
<dt><code>before</code></p>
<dd>indicates that the specified file is to be parsed before the current file.</p>
<dt><code>after</code></p>
<dd>indicates that the specified file is to be parsed after the current file. </p>
<p> Using Python &quot;string interpolation&quot; mechanisms, other definitions are allowed and can later be used within other definitions as %(name)s. Additionally fail2ban has an extended interpolation feature named <code>%(known/parameter)s</code> (means last known option with name <code>parameter</code>). This interpolation makes possible to extend a stock filter or jail regexp in .local file (opposite to simply set failregex/ignoreregex that overwrites it), e.g. </p>
<dl>
<dd>
<pre>baduseragents = IE|wget
failregex = %(known/failregex)s
 useragent=%(baduseragents)s</pre>
</dl>
<p> Additionally to interpolation <code>%(known/parameter)s</code>, that does not works for filter/action init parameters, an interpolation tag <code>&lt;known/parameter&gt;</code> can be used (means last known init definition of filters or actions with name <code>parameter</code>). This interpolation makes possible to extend a parameters of stock filter or action directly in jail inside <i>jail.conf/jail.local</i> file without creating a separately filter.d/*.local file, e.g. </p>
<dl>
<dd># filter.d/test.conf: </p>
<pre>[Init]
test.method = GET
baduseragents = IE|wget
[Definition]
failregex = ^%(__prefix_line)\s+&quot;&lt;test.method&gt;&quot;\s+test\s+regexp\s+-\s+useragent=(?:&lt;baduseragents&gt;)
# jail.local:
[test]
# use filter &quot;test&quot;, overwrite method to &quot;POST&quot; and extend known bad agents with &quot;badagent&quot;:
filter = test[test.method=POST, baduseragents=&quot;badagent|&lt;known/baduseragents&gt;&quot;]</pre>
</dl>
<p> Comments: use &#8216;#&#8217; for comment lines and &#8216;; &#8216; (space is important) for inline comments. When using Python2.X, &#8216;; &#8216; can only be used on the first line due to an Python library bug. </p>
</dl>
<h2>FAIL2BAN CONFIGURATION FILE(S) (</code><i>fail2ban.conf</i><code>)</h2>
<p>These files have one section, [Definition]. </p>
<p> The items that can be set are:</p>
<dl>
<dt>loglevel</code></p>
<dd>verbosity level of log output: CRITICAL, ERROR, WARNING, NOTICE, INFO, DEBUG. Default: ERROR</p>
<dt><code>logtarget</code></p>
<dd>log target: filename, SYSLOG, STDERR or STDOUT. Default: STDERR<br />
 Only a single log target can be specified. If you change logtarget from the default value and you are using logrotate &#8212; also adjust or disable rotation in the corresponding configuration file (e.g. /etc/logrotate.d/fail2ban on Debian systems).</p>
<dt><code>socket</code></p>
<dd>socket filename. Default: /var/run/fail2ban/fail2ban.sock<br />
 This is used for communication with the fail2ban server daemon. Do not remove this file when Fail2ban is running. It will not be possible to communicate with the server afterwards.</p>
<dt><code>pidfile</code></p>
<dd>PID filename. Default: /var/run/fail2ban/fail2ban.pid<br />
 This is used to store the process ID of the fail2ban server.</p>
<dt><code>dbfile</code></p>
<dd>Database filename. Default: /var/lib/fail2ban/fail2ban.sqlite3<br />
 This defines where the persistent data for fail2ban is stored. This persistent data allows bans to be reinstated and continue reading log files from the last read position when fail2ban is restarted. A value of <i>None</i> disables this feature.</p>
<dt><code>dbpurgeage</code></p>
<dd>Database purge age in seconds. Default: 86400 (24hours)<br />
 This sets the age at which bans should be purged from the database. </p>
</dl>
<h2>JAIL CONFIGURATION FILE(S) (</code><i>jail.conf</i><code>)</h2>
<p>The following options are applicable to any jail. They appear in a section specifying the jail name or in the </code><i>[DEFAULT]</i> section which defines default values to be used if not specified in the individual section.</p>
<dl>
<dt><code>filter</code></p>
<dd>name of the filter &#8212; filename of the filter in /etc/fail2ban/filter.d/ without the .conf/.local extension.<br />
 Only one filter can be specified.</p>
<dt><code>logpath</code></p>
<dd>filename(s) of the log files to be monitored, separated by new lines.<br />
 Globs &#8212; paths containing * and ? or [0-9] &#8212; can be used however only the files that exist at start up matching this glob pattern will be considered. </p>
<p> Optional space separated option &#8216;tail&#8217; can be added to the end of the path to cause the log file to be read from the end, else default &#8216;head&#8217; option reads file from the beginning </p>
<p> Ensure syslog or the program that generates the log file isn&#8217;t configured to compress repeated log messages to &quot;<i>*last message repeated 5 time*s</i>&quot; otherwise it will fail to detect. This is called <i>RepeatedMsgReduction</i> in rsyslog and should be <i>Off</i>.</p>
<dt><code>logencoding</code></p>
<dd>encoding of log files used for decoding. Default value of &quot;auto&quot; uses current system locale.</p>
<dt><code>banaction</code></p>
<dd>banning action (default iptables-multiport) typically specified in the <i>[DEFAULT]</i> section for all jails.<br />
 This parameter will be used by the standard substitution of <i>action</i> and can be redefined central in the <i>[DEFAULT]</i> section inside <i>jail.local</i> (to apply it to all jails at once) or separately in each jail, where this substitution will be used.</p>
<dt><code>banaction_allports</code></p>
<dd>the same as <i>banaction</i> but for some &quot;allports&quot; jails like &quot;pam-generic&quot; or &quot;recidive&quot; (default iptables-allports).</p>
<dt><code>action</code></p>
<dd>action(s) from <i>/etc/fail2ban/action.d/</i> without the <i>.conf</i>/<i>.local</i> extension.<br />
 Arguments can be passed to actions to override the default values from the [Init] section in the action file. Arguments are specified by:</p>
<dl>
<dd>
<dl>
<dd>[name=value,name2=value,name3=&quot;values,values&quot;] </p>
</dl>
<p> Values can also be quoted (required when value includes a &quot;,&quot;). More that one action can be specified (in separate lines).</dl>
<dt><code>ignoreip</code></p>
<dd>list of IPs not to ban. They can include a CIDR mask too.</p>
<dt><code>ignorecommand</code></p>
<dd>command that is executed to determine if the current candidate IP for banning should not be banned.<br />
 IP will not be banned if command returns successfully (exit code 0). Like ACTION FILES, tags like &lt;ip&gt; are can be included in the ignorecommand value and will be substituted before execution. Currently only &lt;ip&gt; is supported however more will be added later.</p>
<dt><code>bantime</code></p>
<dd>effective ban duration (in seconds).</p>
<dt><code>findtime</code></p>
<dd>time interval (in seconds) before the current time where failures will count towards a ban.</p>
<dt><code>maxretry</code></p>
<dd>number of failures that have to occur in the last <code>findtime</code> seconds to ban then IP.</p>
<dt><code>backend</code></p>
<dd>backend to be used to detect changes in the logpath.<br />
 It defaults to &quot;auto&quot; which will try &quot;pyinotify&quot;, &quot;gamin&quot;, &quot;systemd&quot; before &quot;polling&quot;. Any of these can be specified. &quot;pyinotify&quot; is only valid on Linux systems with the &quot;pyinotify&quot; Python libraries. &quot;gamin&quot; requires the &quot;gamin&quot; libraries.</p>
<dt><code>usedns</code></p>
<dd>use DNS to resolve HOST names that appear in the logs. By default it is &quot;warn&quot; which will resolve hostnames to IPs however it will also log a warning. If you are using DNS here you could be blocking the wrong IPs due to the asymmetric nature of reverse DNS (that the application used to write the domain name to log) compared to forward DNS that fail2ban uses to resolve this back to an IP (but not necessarily the same one). Ideally you should configure your applications to log a real IP. This can be set to &quot;yes&quot; to prevent warnings in the log or &quot;no&quot; to disable DNS resolution altogether (thus ignoring entries where hostname, not an IP is logged)..</p>
<dt><code>failregex</code></p>
<dd>regex (Python <code>reg</code>ular <code>ex</code>pression) to be added to the filter&#8217;s failregexes. If this is useful for others using your application please share you regular expression with the fail2ban developers by reporting an issue (see REPORTING BUGS below).</p>
<dt><code>ignoreregex</code></p>
<dd>regex which, if the log line matches, would cause Fail2Ban not consider that line. This line will be ignored even if it matches a failregex of the jail or any of its filters. </p>
</dl>
<h3>Backends</h3>
<p>Available options are listed below.</p>
<dl>
<dt><code>pyinotify</code></p>
<dd>requires pyinotify (a file alteration monitor) to be installed. If pyinotify is not installed, Fail2ban will use auto.</p>
<dt><code>gamin</code></p>
<dd>requires Gamin (a file alteration monitor) to be installed. If Gamin is not installed, Fail2ban will use auto.</p>
<dt><code>polling</code></p>
<dd>uses a polling algorithm which does not require external libraries.</p>
<dt><code>systemd</code></p>
<dd>uses systemd python library to access the systemd journal. Specifying <code>logpath</code> is not valid for this backend and instead utilises <code>journalmatch</code> from the jails associated filter config. </p>
</dl>
<h3>Actions</h3>
<p>Each jail can be configured with only a single filter, but may have multiple actions. By default, the name of a action is the action filename, and in the case of Python actions, the &quot;.py&quot; file extension is stripped. Where multiple of the same action are to be used, the <code>actname</code> option can be assigned to the action to avoid duplication e.g.: </p>
<pre>[ssh-iptables-ipset]
enabled = true
action = smtp.py[dest=chris [at] example.com, actname=smtp-chris]
 smtp.py[dest=sally [at] example.com, actname=smtp-sally]</pre>
<h2>ACTION CONFIGURATION FILES (</code><i>action.d/*.conf</i><code>)</h2>
<p>Action files specify which commands are executed to ban and unban an IP address. </p>
<p> Like with jail.conf files, if you desire local changes create an </code><i>[actionname].local</i> file in the <i>/etc/fail2ban/action.d</i> directory and override the required settings. </p>
<p> Action files have two sections, <code>Definition</code> and <code>Init</code> . </p>
<p> The [Init] section enables action-specific settings. In <i>jail.conf/jail.local</i> these can be overridden for a particular jail as options of the action&#8217;s specification in that jail. </p>
<p> The following commands can be present in the [Definition] section.</p>
<dl>
<dt><code>actionstart</code></p>
<dd>command(s) executed when the jail starts.</p>
<dt><code>actionstop</code></p>
<dd>command(s) executed when the jail stops.</p>
<dt><code>actioncheck</code></p>
<dd>command(s) ran before any other action. It aims to verify if the environment is still ok.</p>
<dt><code>actionban</code></p>
<dd>command(s) that bans the IP address after <code>maxretry</code> log lines matches within last <code>findtime</code> seconds.</p>
<dt><code>actionunban</code></p>
<dd>command(s) that unbans the IP address after <code>bantime</code>.</dl>
<p> The [Init] section allows for action-specific settings. In <i>jail.conf/jail.local</i> these can be overwritten for a particular jail as options to the jail. The following are special tags which can be set in the [Init] section:</p>
<dl>
<dt><code>timeout</code></p>
<dd>The maximum period of time in seconds that a command can executed, before being killed.</dl>
<p> Commands specified in the [Definition] section are executed through a system shell so shell redirection and process control is allowed. The commands should return 0, otherwise error would be logged. Moreover if <code>actioncheck</code> exits with non-0 status, it is taken as indication that firewall status has changed and fail2ban needs to reinitialize itself (i.e. issue <code>actionstop</code> and <code>actionstart</code> commands). Tags are enclosed in &lt;&gt;. All the elements of [Init] are tags that are replaced in all action commands. Tags can be added by the <code>fail2ban-client</code> using the &quot;set &lt;JAIL&gt; action &lt;ACT&gt;&quot; command. <code>&lt;br&gt;</code> is a tag that is always a new line (
). </p>
<p> More than a single command is allowed to be specified. Each command needs to be on a separate line and indented with whitespace(s) without blank lines. The following example defines two commands to be executed. </p>
<p>&nbsp;<wbr>actionban&nbsp;<wbr>=&nbsp;<wbr>iptables -I fail2ban-&lt;name&gt;&nbsp;<wbr>&#8211;source&nbsp;<wbr>&lt;ip&gt;&nbsp;<wbr>-j DROP<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>echo ip=&lt;ip&gt;, match=&lt;match&gt;, time=&lt;time&gt;&nbsp;<wbr>&gt;&gt;&nbsp;<wbr>/var/log/fail2ban.log</p>
<h3>Action Tags</h3>
<p>The following tags are substituted in the actionban, actionunban and actioncheck (when called before actionban/actionunban) commands.</p>
<dl>
<dt><code>ip</code></p>
<dd>IPv4 IP address to be banned. e.g. 192.168.0.2</p>
<dt><code>failures</code></p>
<dd>number of times the failure occurred in the log file. e.g. 3</p>
<dt><code>ipfailures</code></p>
<dd>As per <code>failures</code>, but total of all failures for that ip address across all jails from the fail2ban persistent database. Therefore the database must be set for this tag to function.</p>
<dt><code>ipjailfailures</code></p>
<dd>As per <code>ipfailures</code>, but total based on the IPs failures for the current jail.</p>
<dt><code>time</code></p>
<dd>UNIX (epoch) time of the ban. e.g. 1357508484</p>
<dt><code>matches</code></p>
<dd>concatenated string of the log file lines of the matches that generated the ban. Many characters interpreted by shell get escaped to prevent injection, nevertheless use with caution.</p>
<dt><code>ipmatches</code></p>
<dd>As per <code>matches</code>, but includes all lines for the IP which are contained with the fail2ban persistent database. Therefore the database must be set for this tag to function.</p>
<dt><code>ipjailmatches</code></p>
<dd>As per <code>ipmatches</code>, but matches are limited for the IP and for the current jail. </p>
</dl>
<h2>Python Action Files</h2>
<p>Python based actions can also be used, where the file name must be <i>[actionname].py</i>. The Python file must contain a variable <i>Action</i> which points to Python class. This class must implement a minimum interface as described by <i>fail2ban.server.action.ActionBase</i>, which can be inherited from to ease implementation.</p>
<h2>FILTER FILES (</code><i>filter.d/*.conf</i><code>)</h2>
<p>Filter definitions are those in </code><i>/etc/fail2ban/filter.d/*.conf</i> and <i>filter.d/*.local</i>. </p>
<p> These are used to identify failed authentication attempts in log files and to extract the host IP address (or hostname if <code>usedns</code> is <code>true</code>). </p>
<p> Like action files, filter files are ini files. The main section is the [Definition] section. </p>
<p> There are two filter definitions used in the [Definition] section:</p>
<dl>
<dt><code>failregex</code></p>
<dd>is the regex (<code>reg</code>ular <code>ex</code>pression) that will match failed attempts. The tag <i>&lt;HOST&gt;</i> is used as part of the regex and is itself a regex for IPv4 addresses (and hostnames if <code>usedns</code>). Fail2Ban will work out which one of these it actually is. For multiline regexs the tag <i>&lt;SKIPLINES&gt;</i> should be used to separate lines. This allows lines between the matched lines to continue to be searched for other failures. The tag can be used multiple times. </p>
<dt><code>ignoreregex</code></p>
<dd>is the regex to identify log entries that should be ignored by Fail2Ban, even if they match failregex. </p>
</dl>
<p> Similar to actions, filters have an [Init] section which can be overridden in <i>jail.conf/jail.local</i>. Besides the filter-specific settings, the filter [Init] section can be used to set following standard options:</p>
<dl>
<dt><code>maxlines</code></p>
<dd>specifies the maximum number of lines to buffer to match multi-line regexs. For some log formats this will not required to be changed. Other logs may require to increase this value if a particular log file is frequently written to.</p>
<dt><code>datepattern</code></p>
<dd>specifies a custom date pattern/regex as an alternative to the default date detectors e.g. %Y-%m-%d %H:%M(?::%S)?. For a list of valid format directives, see Python library documentation for strptime behaviour.<br />
 Also, special values of <i>Epoch</i> (UNIX Timestamp), <i>TAI64N</i> and <i>ISO8601</i> can be used.<br />
 <code>NOTE:</code> due to config file string substitution, that %&#8217;s must be escaped by an % in config files.</p>
<dt><code>journalmatch</code></p>
<dd>specifies the systemd journal match used to filter the journal entries. See <code><a href="/docs/linux/man/1-journalctl/">journalctl</a>(1)</code> and <code><a href="/docs/linux/man/7-systemd-journal-fields/">systemd.journal-fields</a>(7)</code> for matches syntax and more details on special journal fields. This option is only valid for the <i>systemd</i> backend.</dl>
<p> Similar to actions [Init] section enables filter-specific settings. All parameters specified in [Init] section can be redefined or extended in <i>jail.conf/jail.local</i>. </p>
<p> Filters can also have a section called [INCLUDES]. This is used to read other configuration files. </p>
<dl>
<dt><code>before</code></p>
<dd>indicates that this file is read before the [Definition] section. </p>
<dt><code>after</code></p>
<dd>indicates that this file is read after the [Definition] section. </p>
</dl>
<h2>Author</h2>
<p>Fail2ban was originally written by Cyril Jaquier &lt;cyril.jaquier [at] fail2ban.org&gt;. At the moment it is maintained and further developed by Yaroslav O. Halchenko &lt;debian [at] onerussian.com&gt;, Daniel Black &lt;daniel.subs [at] internode.on.net&gt; and Steven Hiscocks &lt;steven-fail2ban [at] hiscocks.me.uk&gt; along with a number of contributors. See <code>THANKS</code> file shipped with Fail2Ban for a full list. Manual page written by Daniel Black and Yaroslav Halchenko.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="https://github.com/fail2ban/fail2ban/issues">https://github.com/fail2ban/fail2ban/issues</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 the Fail2Ban Team<br />
 Copyright of modifications held by their respective authors.<br />
 Licensed under the GNU General Public License v2 (GPL) or (at your option) any later version.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-fail2ban-server/">fail2ban-server</a>(1) </p>

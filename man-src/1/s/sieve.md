---

title: "sieve(1)"
name: "sieve"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sieve/"
description: "sieve – a mail filtering tool."
---

<p> sieve &#8211; a mail filtering tool. </p>
<h2>SYNOPSIS</h2>
<p> <code>sieve</code> [<i>,OPTION/</i>&#8230;] <i>,SCRIPT/</i></p>
<h2>DESCRIPTION</h2>
<p> GNU sieve <code>&#8212;</code> a mail filtering tool.</p>
<dl>
<dt><code>-c</code>, <code>&#8211;[no-]compile-only</code></dt>
<dd> compile script and exit</dd>
<dt><code>-D</code>, <code>&#8211;dump</code></dt>
<dd> compile script, dump disassembled sieve code to terminal and exit</dd>
<dt><code>-d</code>, <code>&#8211;debug</code>[=<i>,FLAGS/</i>]</dt>
<dd> debug flags (defaults to &quot;TPt&quot;)</dd>
<dt><code>-E</code>, <code>&#8211;[no-]expression</code></dt>
<dd> treat SCRIPT as Sieve program text</dd>
<dt><code>-e</code>, <code>&#8211;email</code>=<i>,ADDRESS/</i></dt>
<dd> override user email address</dd>
<dt><code>&#8211;environment</code>=<i>,NAME=VALUE/</i></dt>
<dd> set sieve environment value</dd>
<dt><code>-f</code>, <code>&#8211;mbox-url</code>=<i>,MBOX/</i></dt>
<dd> mailbox to sieve (defaults to user&#8217;s mail spool)</dd>
<dt><code>-k</code>, <code>&#8211;[no-]keep-going</code></dt>
<dd> keep on going if execution fails on a message</dd>
<dt><code>&#8211;line-info</code>=<i>,BOOL/</i></dt>
<dd> print source location along with action logs (default)</dd>
<dt><code>-n</code>, <code>&#8211;[no-]dry-run</code>, <code>&#8211;no-actions</code></dt>
<dd> do not execute any actions, just print what would be done</dd>
<dt><code>&#8211;no-program-name</code></dt>
<dd> do not prefix diagnostic messages with the program name</dd>
<dt><code>-t</code>, <code>&#8211;ticket</code>=<i>,TICKET/</i></dt>
<dd> ticket file for user authentication</dd>
<dt><code>-v</code>, <code>&#8211;[no-]verbose</code></dt>
<dd> log all actions</dd>
<dt><code>&#8211;variable</code>=<i>,NAME=VALUE/</i></dt>
<dd> set sieve variable</dd>
<dt>
</dt><dd> Global debugging settings</dd>
<dt><code>&#8211;debug-level</code>=<i>,LEVEL/</i></dt>
<dd> set Mailutils debugging level</dd>
<dt> <code>&#8211;[no-]debug-line-info</code> show source info with debugging messages</dt>
<dt><code>&#8211;log-facility</code>=<i>,FACILITY/</i></dt>
<dd>
</dd><dd>output logs to syslog FACILITY</dd>
<dt><code>-M</code>, <code>&#8211;mailer</code>=<i>,MAILER/</i></dt>
<dd> use specified URL as the default mailer</dd>
<dt>
</dt><dd> Sieve options</dd>
<dt><code>&#8211;clear-include-path</code></dt>
<dd> clear Sieve include path</dd>
<dt><code>&#8211;clear-library-path</code>, <code>&#8211;clearpath</code></dt>
<dd> clear Sieve library path</dd>
<dt><code>-I</code>, <code>&#8211;includedir</code>=<i>,DIR/</i></dt>
<dd> append DIR to the list of directories searched for include files</dd>
<dt><code>-L</code>, <code>&#8211;libdir</code>=<i>,DIR/</i></dt>
<dd> append DIR to the list of directories searched for library files</dd>
<dt><code>&#8211;libdir-prefix</code>=<i>,DIR/</i></dt>
<dd> add DIR to the beginning of the list of directories searched for library files</dd>
<dt>
</dt><dd> Configuration handling</dd>
<dt><code>&#8211;config-file</code>=<i>,FILE/</i></dt>
<dd> load this configuration file; implies <code>&#8211;no-config</code></dd>
<dt><code>&#8211;config-lint</code></dt>
<dd> check configuration file syntax and exit</dd>
<dt><code>&#8211;config-verbose</code></dt>
<dd> verbosely log parsing of the configuration files</dd>
<dt><code>&#8211;no-config</code></dt>
<dd> do not load site and user configuration files</dd>
<dt><code>&#8211;no-site-config</code></dt>
<dd> do not load site-wide configuration file</dd>
<dt><code>&#8211;no-user-config</code></dt>
<dd> do not load user configuration file</dd>
<dt><code>&#8211;set</code>=<i>,PARAM=VALUE/</i></dt>
<dd> set configuration parameter</dd>
<dt>
</dt><dd> Informational options</dd>
<dt><code>&#8211;config-help</code></dt>
<dd> show configuration file summary</dd>
<dt><code>&#8211;show-config-options</code></dt>
<dd> show compilation options</dd>
<dt>-?, <code>&#8211;help</code></dt>
<dd> give this help list</dd>
<dt><code>&#8211;usage</code></dt>
<dd> give a short usage message</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> print program version</dd></dl>
<p> Mandatory or optional arguments to long options are also mandatory or optional for any corresponding short options. </p>
<p> Sieve-specific debug levels: </p>
<p> trace1 &#8211; print parse tree before optimization trace2 &#8211; print parse tree after optimization trace3 &#8211; print parser traces trace4 &#8211; print tests and actions being executed trace9 &#8211; print each Sieve instruction being executed </p>
<p> Compatibility debug flags: g &#8211; main parser traces T &#8211; mailutils traces (same as <code>&#8211;debug-level</code>=<i>,sieve/</i>.trace0-trace1) P &#8211; network protocols (same as <code>&#8211;debug-level</code>=<i>,sieve/</i>.=prot) t &#8211; sieve trace (same as <code>&#8211;debug-level</code>=<i>,sieve/</i>.=trace4) i &#8211; sieve instructions trace (same as <code>&#8211;debug-level</code>=<i>,sieve/</i>.=trace9)</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-mailutils [at] gnu.org&gt;.<br />
 GNU Mailutils home page: &lt;<a rel="nofollow" href="http://mailutils.org">http://mailutils.org</a>&gt;<br />
 General help using GNU software: &lt;<a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2007-2019 Free Software Foundation, inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> The complete GNU mailutils documentation is maintained as a Texinfo manual. If the <code>mailutils-doc</code> package is installed, the command</p>
<dl>
<dt>
</dt><dd> <code>info mailutils</code></dd></dl>
<p> should give you access to the complete manual.<br />
 You can also find this manual online in the GNU mailutils webpage:<br />
 <a rel="nofollow" href="https://www.gnu.org/software/mailutils/manual/index.html.">https://www.gnu.org/software/mailutils/manual/index.html.</a><br />
 Please note this manpage was automatically generated by the Debian mailutils packagers. Do not file bugs for its content to the GNU Mailutils upstream authors. </p>

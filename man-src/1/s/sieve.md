---
title: "sieve(1)"
name: "sieve"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sieve/"
description: "sieve – a mail filtering tool."
---

<h2 class="name">NAME</h2>
<p> sieve &#8211; a mail filtering tool. </p>
<h2>SYNOPSIS</h2>
<p> <code>sieve</code> [<i>,OPTION/</i>&#8230;] <i>,SCRIPT/</i></p>
<h2>DESCRIPTION</h2>
<p> GNU sieve <code>&#8212;</code> a mail filtering tool.</p>
<dl>
<dt><code>-c</code>, <code>&#8211;[no-]compile-only</code></p>
<dd> compile script and exit</p>
<dt><code>-D</code>, <code>&#8211;dump</code></p>
<dd> compile script, dump disassembled sieve code to terminal and exit</p>
<dt><code>-d</code>, <code>&#8211;debug</code>[=<i>,FLAGS/</i>]</p>
<dd> debug flags (defaults to &quot;TPt&quot;)</p>
<dt><code>-E</code>, <code>&#8211;[no-]expression</code></p>
<dd> treat SCRIPT as Sieve program text</p>
<dt><code>-e</code>, <code>&#8211;email</code>=<i>,ADDRESS/</i></p>
<dd> override user email address</p>
<dt><code>&#8211;environment</code>=<i>,NAME=VALUE/</i></p>
<dd> set sieve environment value</p>
<dt><code>-f</code>, <code>&#8211;mbox-url</code>=<i>,MBOX/</i></p>
<dd> mailbox to sieve (defaults to user&#8217;s mail spool)</p>
<dt><code>-k</code>, <code>&#8211;[no-]keep-going</code></p>
<dd> keep on going if execution fails on a message</p>
<dt><code>&#8211;line-info</code>=<i>,BOOL/</i></p>
<dd> print source location along with action logs (default)</p>
<dt><code>-n</code>, <code>&#8211;[no-]dry-run</code>, <code>&#8211;no-actions</code></p>
<dd> do not execute any actions, just print what would be done</p>
<dt><code>&#8211;no-program-name</code></p>
<dd> do not prefix diagnostic messages with the program name</p>
<dt><code>-t</code>, <code>&#8211;ticket</code>=<i>,TICKET/</i></p>
<dd> ticket file for user authentication</p>
<dt><code>-v</code>, <code>&#8211;[no-]verbose</code></p>
<dd> log all actions</p>
<dt><code>&#8211;variable</code>=<i>,NAME=VALUE/</i></p>
<dd> set sieve variable</p>
<dt>
<dd> Global debugging settings</p>
<dt><code>&#8211;debug-level</code>=<i>,LEVEL/</i></p>
<dd> set Mailutils debugging level</p>
<dt> <code>&#8211;[no-]debug-line-info</code> show source info with debugging messages</p>
<dt><code>&#8211;log-facility</code>=<i>,FACILITY/</i></p>
<dd>
<dd>output logs to syslog FACILITY</p>
<dt><code>-M</code>, <code>&#8211;mailer</code>=<i>,MAILER/</i></p>
<dd> use specified URL as the default mailer</p>
<dt>
<dd> Sieve options</p>
<dt><code>&#8211;clear-include-path</code></p>
<dd> clear Sieve include path</p>
<dt><code>&#8211;clear-library-path</code>, <code>&#8211;clearpath</code></p>
<dd> clear Sieve library path</p>
<dt><code>-I</code>, <code>&#8211;includedir</code>=<i>,DIR/</i></p>
<dd> append DIR to the list of directories searched for include files</p>
<dt><code>-L</code>, <code>&#8211;libdir</code>=<i>,DIR/</i></p>
<dd> append DIR to the list of directories searched for library files</p>
<dt><code>&#8211;libdir-prefix</code>=<i>,DIR/</i></p>
<dd> add DIR to the beginning of the list of directories searched for library files</p>
<dt>
<dd> Configuration handling</p>
<dt><code>&#8211;config-file</code>=<i>,FILE/</i></p>
<dd> load this configuration file; implies <code>&#8211;no-config</code></p>
<dt><code>&#8211;config-lint</code></p>
<dd> check configuration file syntax and exit</p>
<dt><code>&#8211;config-verbose</code></p>
<dd> verbosely log parsing of the configuration files</p>
<dt><code>&#8211;no-config</code></p>
<dd> do not load site and user configuration files</p>
<dt><code>&#8211;no-site-config</code></p>
<dd> do not load site-wide configuration file</p>
<dt><code>&#8211;no-user-config</code></p>
<dd> do not load user configuration file</p>
<dt><code>&#8211;set</code>=<i>,PARAM=VALUE/</i></p>
<dd> set configuration parameter</p>
<dt>
<dd> Informational options</p>
<dt><code>&#8211;config-help</code></p>
<dd> show configuration file summary</p>
<dt><code>&#8211;show-config-options</code></p>
<dd> show compilation options</p>
<dt>-?, <code>&#8211;help</code></p>
<dd> give this help list</p>
<dt><code>&#8211;usage</code></p>
<dd> give a short usage message</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> print program version</dl>
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
<dd> <code>info mailutils</code></dl>
<p> should give you access to the complete manual.<br />
 You can also find this manual online in the GNU mailutils webpage:<br />
 <a rel="nofollow" href="https://www.gnu.org/software/mailutils/manual/index.html.">https://www.gnu.org/software/mailutils/manual/index.html.</a><br />
 Please note this manpage was automatically generated by the Debian mailutils packagers. Do not file bugs for its content to the GNU Mailutils upstream authors. </p>
<h2>Index</h2>

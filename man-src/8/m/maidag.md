---
title: "maidag(8)"
name: "maidag"
section: "8"
letter: "m"
url: "/docs/linux/man/8-maidag/"
description: "maidag – the mail delivery agent."
---

<p>maidag &#8211; the mail delivery agent.</p>
<h2>Synopsis</h2>
<p><code>maidag</code> [<i>,OPTION/</i>&#8230;] [<i>,recipient/</i>&#8230;]</p>
<h2>Description</h2>
<p>GNU maidag <code>&#8212;</code> the mail delivery agent.</p>
<dl>
<dd>General options</p>
<dt><code>-d</code>, <code>&#8211;daemon</code>[=<i>,NUMBER/</i>]</p>
<dd>runs in daemon mode with a maximum of NUMBER children</p>
<dt><code>&#8211;[no-]foreground</code></p>
<dd>remain in foreground</p>
<dt><code>-f</code>, <code>-r</code>, <code>&#8211;from</code>=<i>,EMAIL/</i></p>
<dd>specify the sender&#8217;s name</p>
<dt><code>-i</code>, <code>&#8211;[no-]inetd</code></p>
<dd>run in inetd mode</p>
<dt><code>&#8211;lmtp</code>[=<i>,URL/</i>]</p>
<dd>operate in LMTP mode</p>
<dt><code>&#8211;mda</code></p>
<dd>force MDA mode even if not started as root</p>
<dt><code>&#8211;stderr</code></p>
<dd>log to standard error</p>
<dt><code>&#8211;[no-]transcript</code></p>
<dd>enable session transcript</p>
<dt><code>&#8211;url</code></p>
<dd>deliver to given URLs</p>
<dt><code>-x</code>, <code>&#8211;debug</code>=<i>,FLAGS/</i></p>
<dd>enable debugging</p>
<dd>Scripting options</p>
<dt><code>-l</code>, <code>&#8211;language</code>=<i>,STRING/</i></p>
<dd>define scripting language for the next <code>&#8211;script</code> option</p>
<dt><code>&#8211;message-id-header</code>=<i>,STRING/</i></p>
<dd>use this header to identify messages when logging Sieve actions</p>
<dt><code>-s</code>, <code>&#8211;script</code>=<i>,PATTERN/</i></p>
<dd>set name pattern for user-defined mail filter</p>
<dd>Global debugging settings</p>
<dt><code>&#8211;debug-level</code>=<i>,LEVEL/</i></p>
<dd>set Mailutils debugging level</p>
<dt> <code>&#8211;[no-]debug-line-info</code> show source info with debugging messages</p>
<dt><code>&#8211;log-facility</code>=<i>,FACILITY/</i></p>
<dd>
<dd>output logs to syslog FACILITY</p>
<dt><code>-M</code>, <code>&#8211;mailer</code>=<i>,MAILER/</i></p>
<dd>use specified URL as the default mailer</p>
<dd>Sieve options</p>
<dt><code>&#8211;clear-include-path</code></p>
<dd>clear Sieve include path</p>
<dt><code>&#8211;clear-library-path</code>, <code>&#8211;clearpath</code></p>
<dd>clear Sieve library path</p>
<dt><code>-I</code>, <code>&#8211;includedir</code>=<i>,DIR/</i></p>
<dd>append DIR to the list of directories searched for include files</p>
<dt><code>-L</code>, <code>&#8211;libdir</code>=<i>,DIR/</i></p>
<dd>append DIR to the list of directories searched for library files</p>
<dt><code>&#8211;libdir-prefix</code>=<i>,DIR/</i></p>
<dd>add DIR to the beginning of the list of directories searched for library files</p>
<dd>Configuration handling</p>
<dt><code>&#8211;config-file</code>=<i>,FILE/</i></p>
<dd>load this configuration file; implies <code>&#8211;no-config</code></p>
<dt><code>&#8211;config-lint</code></p>
<dd>check configuration file syntax and exit</p>
<dt><code>&#8211;config-verbose</code></p>
<dd>verbosely log parsing of the configuration files</p>
<dt><code>&#8211;no-config</code></p>
<dd>do not load site and user configuration files</p>
<dt><code>&#8211;no-site-config</code></p>
<dd>do not load site-wide configuration file</p>
<dt><code>&#8211;no-user-config</code></p>
<dd>do not load user configuration file</p>
<dt><code>&#8211;set</code>=<i>,PARAM=VALUE/</i></p>
<dd>set configuration parameter</p>
<dd>Informational options</p>
<dt><code>&#8211;config-help</code></p>
<dd>show configuration file summary</p>
<dt><code>&#8211;show-config-options</code></p>
<dd>show compilation options</p>
<dt>-?, <code>&#8211;help</code></p>
<dd>give this help list</p>
<dt><code>&#8211;usage</code></p>
<dd>give a short usage message</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print program version</dl>
<p> Mandatory or optional arguments to long options are also mandatory or optional for any corresponding short options. </p>
<p> Debug flags are: g &#8211; guile stack traces t &#8211; sieve trace (MU_SIEVE_DEBUG_TRACE) i &#8211; sieve instructions trace (MU_SIEVE_DEBUG_INSTR) l &#8211; sieve action logs 0-9 &#8211; Set maidag debugging level</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;bug-mailutils [at] gnu.org&gt;.<br />
 GNU Mailutils home page: &lt;<a rel="nofollow" href="http://mailutils.org">http://mailutils.org</a>&gt;<br />
 General help using GNU software: &lt;<a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a>&gt;</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2007-2017 Free Software Foundation, inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>See Also</h2>
<p>The complete GNU mailutils documentation is maintained as a Texinfo manual. If the <code>mailutils-doc</code> package is installed, the command</p>
<dl>
<dd><code>info mailutils</code></dl>
<p> should give you access to the complete manual.<br />
 You can also find this manual online in the GNU mailutils webpage:<br />
 <a rel="nofollow" href="https://www.gnu.org/software/mailutils/manual/index.html.">https://www.gnu.org/software/mailutils/manual/index.html.</a><br />
 Please note this manpage was automatically generated by the Debian mailutils packagers. Do not file bugs for its content to the GNU Mailutils upstream authors. </p>

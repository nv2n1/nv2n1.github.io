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
<dd>General options</dd>
<dt><code>-d</code>, <code>&#8211;daemon</code>[=<i>,NUMBER/</i>]</dt>
<dd>runs in daemon mode with a maximum of NUMBER children</dd>
<dt><code>&#8211;[no-]foreground</code></dt>
<dd>remain in foreground</dd>
<dt><code>-f</code>, <code>-r</code>, <code>&#8211;from</code>=<i>,EMAIL/</i></dt>
<dd>specify the sender&#8217;s name</dd>
<dt><code>-i</code>, <code>&#8211;[no-]inetd</code></dt>
<dd>run in inetd mode</dd>
<dt><code>&#8211;lmtp</code>[=<i>,URL/</i>]</dt>
<dd>operate in LMTP mode</dd>
<dt><code>&#8211;mda</code></dt>
<dd>force MDA mode even if not started as root</dd>
<dt><code>&#8211;stderr</code></dt>
<dd>log to standard error</dd>
<dt><code>&#8211;[no-]transcript</code></dt>
<dd>enable session transcript</dd>
<dt><code>&#8211;url</code></dt>
<dd>deliver to given URLs</dd>
<dt><code>-x</code>, <code>&#8211;debug</code>=<i>,FLAGS/</i></dt>
<dd>enable debugging</dd>
<dd>Scripting options</dd>
<dt><code>-l</code>, <code>&#8211;language</code>=<i>,STRING/</i></dt>
<dd>define scripting language for the next <code>&#8211;script</code> option</dd>
<dt><code>&#8211;message-id-header</code>=<i>,STRING/</i></dt>
<dd>use this header to identify messages when logging Sieve actions</dd>
<dt><code>-s</code>, <code>&#8211;script</code>=<i>,PATTERN/</i></dt>
<dd>set name pattern for user-defined mail filter</dd>
<dd>Global debugging settings</dd>
<dt><code>&#8211;debug-level</code>=<i>,LEVEL/</i></dt>
<dd>set Mailutils debugging level</dd>
<dt> <code>&#8211;[no-]debug-line-info</code> show source info with debugging messages</dt>
<dt><code>&#8211;log-facility</code>=<i>,FACILITY/</i></dt>
<dd>
</dd><dd>output logs to syslog FACILITY</dd>
<dt><code>-M</code>, <code>&#8211;mailer</code>=<i>,MAILER/</i></dt>
<dd>use specified URL as the default mailer</dd>
<dd>Sieve options</dd>
<dt><code>&#8211;clear-include-path</code></dt>
<dd>clear Sieve include path</dd>
<dt><code>&#8211;clear-library-path</code>, <code>&#8211;clearpath</code></dt>
<dd>clear Sieve library path</dd>
<dt><code>-I</code>, <code>&#8211;includedir</code>=<i>,DIR/</i></dt>
<dd>append DIR to the list of directories searched for include files</dd>
<dt><code>-L</code>, <code>&#8211;libdir</code>=<i>,DIR/</i></dt>
<dd>append DIR to the list of directories searched for library files</dd>
<dt><code>&#8211;libdir-prefix</code>=<i>,DIR/</i></dt>
<dd>add DIR to the beginning of the list of directories searched for library files</dd>
<dd>Configuration handling</dd>
<dt><code>&#8211;config-file</code>=<i>,FILE/</i></dt>
<dd>load this configuration file; implies <code>&#8211;no-config</code></dd>
<dt><code>&#8211;config-lint</code></dt>
<dd>check configuration file syntax and exit</dd>
<dt><code>&#8211;config-verbose</code></dt>
<dd>verbosely log parsing of the configuration files</dd>
<dt><code>&#8211;no-config</code></dt>
<dd>do not load site and user configuration files</dd>
<dt><code>&#8211;no-site-config</code></dt>
<dd>do not load site-wide configuration file</dd>
<dt><code>&#8211;no-user-config</code></dt>
<dd>do not load user configuration file</dd>
<dt><code>&#8211;set</code>=<i>,PARAM=VALUE/</i></dt>
<dd>set configuration parameter</dd>
<dd>Informational options</dd>
<dt><code>&#8211;config-help</code></dt>
<dd>show configuration file summary</dd>
<dt><code>&#8211;show-config-options</code></dt>
<dd>show compilation options</dd>
<dt>-?, <code>&#8211;help</code></dt>
<dd>give this help list</dd>
<dt><code>&#8211;usage</code></dt>
<dd>give a short usage message</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd>print program version</dd></dl>
<p> Mandatory or optional arguments to long options are also mandatory or optional for any corresponding short options. </p>
<p> Debug flags are: g &#8211; guile stack traces t &#8211; sieve trace (MU_SIEVE_DEBUG_TRACE) i &#8211; sieve instructions trace (MU_SIEVE_DEBUG_INSTR) l &#8211; sieve action logs 0-9 &#8211; Set maidag debugging level</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;bug-mailutils [at] gnu.org&gt;.<br/>
 GNU Mailutils home page: &lt;<a rel="nofollow" href="http://mailutils.org">http://mailutils.org</a>&gt;<br/>
 General help using GNU software: &lt;<a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a>&gt;</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2007-2017 Free Software Foundation, inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;<br/>
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>See Also</h2>
<p>The complete GNU mailutils documentation is maintained as a Texinfo manual. If the <code>mailutils-doc</code> package is installed, the command</p>
<dl>
<dd><code>info mailutils</code></dd></dl>
<p> should give you access to the complete manual.<br/>
 You can also find this manual online in the GNU mailutils webpage:<br/>
 <a rel="nofollow" href="https://www.gnu.org/software/mailutils/manual/index.html.">https://www.gnu.org/software/mailutils/manual/index.html.</a><br/>
 Please note this manpage was automatically generated by the Debian mailutils packagers. Do not file bugs for its content to the GNU Mailutils upstream authors. </p>

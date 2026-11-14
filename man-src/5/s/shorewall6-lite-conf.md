---
title: "shorewall6-lite-conf(5)"
name: "shorewall6-lite-conf"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall6-lite-conf/"
description: "shorewall6-lite.conf – Shorewall6 Lite global configuration file"
---

<p>shorewall6-lite.conf &#8211; Shorewall6 Lite global configuration file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/etc/shorewall6-lite/shorewall6-lite.conf</code></dl>
<h2>Description</h2>
<dd>This file sets options that apply to Shorewall6 Lite as a whole. </p>
<p> The file consists of Shell comments (lines beginning with &#8216;#&#8217;), blank lines and assignment statements (<i>variable</i>=<i>value</i>). Each variable&#8217;s setting is preceded by comments that describe the variable and it&#8217;s effect. </p>
<p> Any option not specified in this file gets its value from the shorewall6.conf file used during compilation of /var/lib/shorewall6-lite/firewall. Those settings may be found in the file /var/lib/shorewall6-lite/firewall.conf.</p>
<h2>Options</h2>
<p>The following options may be set in shorewall6.conf. </p>
<p> <code>IP6TABLES=</code>[<i>pathname</i>]</p>
<dl>
<dd>This parameter names the ip6tables executable to be used by Shorewall6. If not specified or if specified as a null value, then the ip6tables executable located using the PATH option is used.</dl>
<p> <code>LOGFILE=</code>[<i>pathname</i>]</p>
<dl>
<dd>This parameter tells the /sbin/shorewall6 program where to look for Shorewall6 messages when processing the <code>dump</code>, <code>logwatch</code>, <code>show log</code>, and <code>hits</code> commands. If not assigned or if assigned an empty value, /var/log/messages is assumed.</dl>
<p> <code>LOGFORMAT=</code>[<code>&quot;</code><i>formattemplate</i><code>&quot;</code>]</p>
<dl>
<dd>The value of this variable generate the &#8211;log-prefix setting for Shorewall6 logging rules. It contains a &#8220;printf&#8221; formatting template which accepts three arguments (the chain name, logging rule number (optional) and the disposition). To use LOGFORMAT with fireparse, set it as: </p>
<dl>
<dd>
<pre> LOGFORMAT=&quot;fp=%s:%d a=%s &quot;</pre>
</dl>
<p> If the LOGFORMAT value contains the substring &#8220;%d&#8221; then the logging rule number is calculated and formatted in that position; if that substring is not included then the rule number is not included. If not supplied or supplied as empty (LOGFORMAT=&quot;&quot;) then &#8220;Shorewall6:%s:%s:&#8221; is assumed.</dl>
<p> <code>PATH</code><code>=</code><i>pathname</i><code>[</code><code>:</code><i>pathname</i><code>]&#8230;</code></p>
<dl>
<dd>Determines the order in which Shorewall6 searches directories for executable files.</dl>
<p> <code>RESTOREFILE=</code>[<i>filename</i>]</p>
<dl>
<dd>Specifies the simple name of a file in /var/lib/shorewall6 to be used as the default restore script in the <code>shorewall6 save</code>, <code>shorewall6 restore</code>, <code>shorewall6 forget </code>and <code>shorewall6 -f start</code> commands.</dl>
<p> <code>SHOREWALL_SHELL=</code>[<i>pathname</i>]</p>
<dl>
<dd>This option is used to specify the shell program to be used to interpret the compiled script. If not specified or specified as a null value, /bin/sh is assumed. Using a light-weight shell such as ash or dash can significantly improve performance.</dl>
<p> <code>SUBSYSLOCK=</code>[<i>pathname</i>]</p>
<dl>
<dd>This parameter should be set to the name of a file that the firewall should create if it starts successfully and remove when it stops. Creating and removing this file allows Shorewall6 to work with your distribution&#8217;s initscripts. For RedHat, this should be set to /var/lock/subsys/shorewall6. For Debian, the value is /var/state/shorewall6 and in LEAF it is /var/run/shorewall.</dl>
<p> <code>VERBOSITY=</code>[<i>number</i>]</p>
<dl>
<dd>Shorewall6 has traditionally been very noisy (produced lots of output). You may set the default level of verbosity using the VERBOSITY OPTION. </p>
<p> Values are:</p>
<dl>
<dd>0 &#8211; Silent. You may make it more verbose using the -v<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>option</dl>
<dl>
<dd>1 &#8211; Major progress messages displayed</dl>
<dl>
<dd>2 &#8211; All progress messages displayed (old default<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>behavior)</dl>
<p> If not specified, then 2 is assumed.</dl>
<h2>Files</h2>
<p>/etc/shorewall6-lite/shorewall6.conf</p>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/Documentation_Index.html">http://www.shorewall.net/Documentation_Index.html</a></code>m[] <a href="/docs/linux/man/8-shorewall6-lite/">shorewall6-lite</a>(8), <a href="/docs/linux/man/5-shorewall6-accounting/">shorewall6-accounting</a>(5), <a href="/docs/linux/man/5-shorewall6-actions/">shorewall6-actions</a>(5), <a href="/docs/linux/man/5-shorewall6-blacklist/">shorewall6-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall6-hosts/">shorewall6-hosts</a>(5), <a href="/docs/linux/man/5-shorewall6-interfaces/">shorewall6-interfaces</a>(5), <a href="/docs/linux/man/5-shorewall6-ipsec/">shorewall6-ipsec</a>(5), <a href="/docs/linux/man/5-shorewall6-maclist/">shorewall6-maclist</a>(5), <a href="/docs/linux/man/5-shorewall6-masq/">shorewall6-masq</a>(5), <a href="/docs/linux/man/5-shorewall6-nat/">shorewall6-nat</a>(5), <a href="/docs/linux/man/5-shorewall6-netmap/">shorewall6-netmap</a>(5), <a href="/docs/linux/man/5-shorewall6-params/">shorewall6-params</a>(5), <a href="/docs/linux/man/5-shorewall6-policy/">shorewall6-policy</a>(5), <a href="/docs/linux/man/5-shorewall6-providers/">shorewall6-providers</a>(5), <a href="/docs/linux/man/5-shorewall6-proxyarp/">shorewall6-proxyarp</a>(5), <a href="/docs/linux/man/5-shorewall6-route_rules/">shorewall6-route_rules</a>(5), <a href="/docs/linux/man/5-shorewall6-routestopped/">shorewall6-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall6-rules/">shorewall6-rules</a>(5), <a href="/docs/linux/man/5-shorewall6-tcclasses/">shorewall6-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall6-tcdevices/">shorewall6-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall6-tcrules/">shorewall6-tcrules</a>(5), <a href="/docs/linux/man/5-shorewall6-tos/">shorewall6-tos</a>(5), <a href="/docs/linux/man/5-shorewall6-tunnels/">shorewall6-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall6-zones/">shorewall6-zones</a>(5) </p>

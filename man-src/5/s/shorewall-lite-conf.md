---
title: "shorewall-lite-conf(5)"
name: "shorewall-lite-conf"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall-lite-conf/"
description: "shorewall-lite.conf – Shorewall Lite global configuration file"
---

<p>shorewall-lite.conf &#8211; Shorewall Lite global configuration file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/etc/shorewall-lite/shorewall-lite.conf</code></dl>
<h2>Description</h2>
<dd>This file sets options that apply to Shorewall Lite as a whole. </p>
<p> The file consists of Shell comments (lines beginning with &#8216;#&#8217;), blank lines and assignment statements (<i>variable</i>=<i>value</i>). Each variable&#8217;s setting is preceded by comments that describe the variable and it&#8217;s effect. </p>
<p> Any option not specified in this file gets its value from the shorewall.conf file used during compilation of /var/lib/shorewall-lite/firewall. Those settings may be found in the file /var/lib/shorewall-lite/firewall.conf.</p>
<h2>Options</h2>
<p>The following options may be set in shorewall.conf. </p>
<p> <code>IPTABLES=</code>[<i>pathname</i>]</p>
<dl>
<dd>This parameter names the iptables executable to be used by Shorewall. If not specified or if specified as a null value, then the iptables executable located using the PATH option is used.</dl>
<p> <code>LOGFILE=</code>[<i>pathname</i>]</p>
<dl>
<dd>This parameter tells the /sbin/shorewall program where to look for Shorewall messages when processing the <code>dump</code>, <code>logwatch</code>, <code>show log</code>, and <code>hits</code> commands. If not assigned or if assigned an empty value, /var/log/messages is assumed.</dl>
<p> <code>LOGFORMAT=</code>[<code>&quot;</code><i>formattemplate</i><code>&quot;</code>]</p>
<dl>
<dd>The value of this variable generate the &#8211;log-prefix setting for Shorewall logging rules. It contains a &#8220;printf&#8221; formatting template which accepts three arguments (the chain name, logging rule number (optional) and the disposition). To use LOGFORMAT with fireparse, set it as: </p>
<dl>
<dd>
<pre> LOGFORMAT=&quot;fp=%s:%d a=%s &quot;</pre>
</dl>
<p> If the LOGFORMAT value contains the substring &#8220;%d&#8221; then the logging rule number is calculated and formatted in that position; if that substring is not included then the rule number is not included. If not supplied or supplied as empty (LOGFORMAT=&quot;&quot;) then &#8220;Shorewall:%s:%s:&#8221; is assumed.</dl>
<p> <code>PATH=</code><i>pathname</i><code>[</code><code>:</code><i>pathname</i><code>]&#8230;</code></p>
<dl>
<dd>Determines the order in which Shorewall searches directories for executable files.</dl>
<p> <code>RESTOREFILE=</code>[<i>filename</i>]</p>
<dl>
<dd>Specifies the simple name of a file in /var/lib/shorewall to be used as the default restore script in the <code>shorewall save</code>, <code>shorewall restore</code>, <code>shorewall forget </code>and <code>shorewall -f start</code> commands.</dl>
<p> <code>SHOREWALL_SHELL=</code>[<i>pathname</i>]</p>
<dl>
<dd>This option is used to specify the shell program to be used to run the Shorewall compiler and to interpret the compiled script. If not specified or specified as a null value, /bin/sh is assumed. Using a light-weight shell such as ash or dash can significantly improve performance.</dl>
<p> <code>SUBSYSLOCK=</code>[<i>pathname</i>]</p>
<dl>
<dd>This parameter should be set to the name of a file that the firewall should create if it starts successfully and remove when it stops. Creating and removing this file allows Shorewall to work with your distribution&#8217;s initscripts. For RedHat, this should be set to /var/lock/subsys/shorewall. For Debian, the value is /var/state/shorewall and in LEAF it is /var/run/shorewall.</dl>
<p> VERBOSITY=[<code>number</code>]</p>
<dl>
<dd>Shorewall has traditionally been very noisy (produced lots of output). You may set the default level of verbosity using the VERBOSITY OPTION. </p>
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
<p>/etc/shorewall-lite/shorewall.conf</p>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/Documentation_Index.html">http://www.shorewall.net/Documentation_Index.html</a></code>m[] <a href="/docs/linux/man/8-shorewall-lite/">shorewall-lite</a>(8), <a href="/docs/linux/man/5-shorewall-accounting/">shorewall-accounting</a>(5), <a href="/docs/linux/man/5-shorewall-actions/">shorewall-actions</a>(5), <a href="/docs/linux/man/5-shorewall-blacklist/">shorewall-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall-hosts/">shorewall-hosts</a>(5), <a href="/docs/linux/man/5-shorewall-interfaces/">shorewall-interfaces</a>(5), <a href="/docs/linux/man/5-shorewall-ipsec/">shorewall-ipsec</a>(5), <a href="/docs/linux/man/5-shorewall-maclist/">shorewall-maclist</a>(5), <a href="/docs/linux/man/5-shorewall-masq/">shorewall-masq</a>(5), <a href="/docs/linux/man/5-shorewall-nat/">shorewall-nat</a>(5), <a href="/docs/linux/man/5-shorewall-netmap/">shorewall-netmap</a>(5), <a href="/docs/linux/man/5-shorewall-params/">shorewall-params</a>(5), <a href="/docs/linux/man/5-shorewall-policy/">shorewall-policy</a>(5), <a href="/docs/linux/man/5-shorewall-providers/">shorewall-providers</a>(5), <a href="/docs/linux/man/5-shorewall-proxyarp/">shorewall-proxyarp</a>(5), <a href="/docs/linux/man/5-shorewall-route_rules/">shorewall-route_rules</a>(5), <a href="/docs/linux/man/5-shorewall-routestopped/">shorewall-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall-rules/">shorewall-rules</a>(5), <a href="/docs/linux/man/5-shorewall-tcclasses/">shorewall-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall-tcdevices/">shorewall-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall-tcrules/">shorewall-tcrules</a>(5), <a href="/docs/linux/man/5-shorewall-tos/">shorewall-tos</a>(5), <a href="/docs/linux/man/5-shorewall-tunnels/">shorewall-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall-zones/">shorewall-zones</a>(5) </p>

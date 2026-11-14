---
title: "elogin(1)"
name: "elogin"
section: "1"
letter: "e"
url: "/docs/linux/man/1-elogin/"
description: "clogin – Cisco login script"
---

<h2>NAME</h2>
<p> clogin &#8211; Cisco login script</p>
<h2>SYNOPSIS</h2>
<p> <code>clogin</code> [<code>-autoenable</code>] [<code>-noenable</code>] [<code>-dSV</code>] [<code>-c&nbsp;<wbr></code> command] [<code>-E&nbsp;<wbr></code> var=x] [<code>-e&nbsp;<wbr></code> enable-password] [<code>-f&nbsp;<wbr></code> cloginrc-file] [<code>-p&nbsp;<wbr></code> user-password] [<code>-s&nbsp;<wbr></code> script-file] [<code>-t&nbsp;<wbr></code> timeout] [<code>-u&nbsp;<wbr></code> username] [<code>-v&nbsp;<wbr></code> vty-password] [<code>-w&nbsp;<wbr></code> enable-username] [<code>-x&nbsp;<wbr></code> command-file] [<code>-y&nbsp;<wbr></code> ssh_cypher_type] router [router&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>clogin</code> is an <code><a href="/docs/linux/man/1-expect/">expect</a></code>(1) script to automate the process of logging into a Cisco router, Catalyst switch, Extreme switch, Juniper ERX/E-series, Procket Networks, or Redback router. There are complementary scripts for Alteon, Avocent (Cyclades), Bay Networks (nortel), ADC-kentrox EZ-T3 mux, Foundry, HP Procurve switches and Cisco AGMs, Hitachi routers, Juniper Networks, MRV optical switch, Mikrotik routers, Netscreen firewalls, Netscaler, Riverstone, Netopia, Cisco WLCs and Xirrus arrays, named <code>alogin,</code> <code>avologin,</code> <code>blogin,</code> <code>elogin,</code> <code>flogin,</code> <code>fnlogin,</code> <code>hlogin,</code> <code>htlogin,</code> <code>jlogin,</code> <code>mrvlogin,</code> <code>mtlogin,</code> <code>nlogin,</code> <code>nslogin,</code> <code>rivlogin,</code> <code>tlogin,</code> <code>wlogin,</code> and <code>xilogin,</code> respectively. Lastly, <code>plogin</code> is a poly-login script using the <code><a href="/docs/linux/man/5-router-db/">router.db</a></code>(5) files of rancid groups and the <code><a href="/docs/linux/man/5-rancid-types-base/">rancid.types.base</a></code>(5) and <code><a href="/docs/linux/man/5-rancid-types-conf/">rancid.types.conf</a></code>(5) files to determine which login script to execute for the device type of the given device. </p>
<p> <code>clogin</code> reads the <i>.cloginrc</i> file for its configuration, then connects and logs into each of the routers specified on the command line in the order listed. Command-line options exist to override some of the directives found in the <i>.cloginrc</i> configuration file. </p>
<p> The command-line options are as follows:</p>
<dl>
<dt><code>-S</code></p>
<dd> Save the configuration on exit, if the device prompts at logout time. This only has affect when used with -s.</p>
<dt><code>-V</code></p>
<dd> Prints package name and version strings.</p>
<dt><code>-c</code></p>
<dd> Command to be run on each router list on the command-line. Multiple commands maybe listed by separating them with semi-colons (;). The argument should be quoted to avoid shell expansion.</p>
<dt><code>-d</code></p>
<dd> Enable expect debugging.</p>
<dt><code>-E</code></p>
<dd> Specifies a variable to pass through to scripts (-s). For example, the command-line option -Efoo=bar will produce a global variable by the name Efoo with the initial value &quot;bar&quot;.</p>
<dt><code>-e</code></p>
<dd> Specify a password to be supplied when gaining enable privileges on the router(s). Also see the password directive of the <i>.cloginrc</i> file.</p>
<dt><code>-f</code></p>
<dd> Specifies an alternate configuration file. The default is <i>$HOME/.cloginrc</i>.</p>
<dt><code>-p</code></p>
<dd> Specifies a password associated with the user specified by the <code>-u</code> option, user directive of the <i>.cloginrc</i> file, or the Unix username of the user.</p>
<dt><code>-s</code></p>
<dd> The filename of an <code><a href="/docs/linux/man/1-expect/">expect</a></code>(1) script which will be sourced after the login is successful and is expected to return control to <code>clogin,</code> with the connection to the router intact, when it is done. Note that <code>clogin</code> disables <i>log_user</i> of <code><a href="/docs/linux/man/1-expect/">expect</a></code>(1)<code>when</code> <code>-s</code> is used. Example script(s) can be found in share/rancid/*.exp.</p>
<dt><code>-t</code></p>
<dd> Alters the timeout interval; the period that <code>clogin</code> waits for an individual command to return a prompt or the login process to produce a prompt or failure. The argument is in seconds.</p>
<dt><code>-u</code></p>
<dd> Specifies the username used when prompted. The command-line option overrides any user directive found in <i>.cloginrc</i>. The default is the current Unix username.</p>
<dt><code>-v</code></p>
<dd> Specifies a vty password, that which is prompted for upon connection to the router. This overrides the vty password of the <i>.cloginrc</i> file&#8217;s password directive.</p>
<dt><code>-w</code></p>
<dd> Specifies the username used if prompted when gaining enable privileges. The command-line option overrides any user or enauser directives found in <i>.cloginrc</i>. The default is the current Unix username.</p>
<dt><code>-x</code></p>
<dd> Similar to the <code>-c</code> option; <code>-x</code> specifies a file with commands to run on each of the routers. The commands must not expect additional input, such as &#8216;copy rcp startup-config&#8217; does. For example:</dl>
<pre>
show version
show logging
</pre>
<dl>
<dt><code>-y</code></p>
<dd> Specifies the encryption algorithm for use with the <code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1) -c option. The default encryption type is often not supported. See the <code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1) man page for details. The default is 3des. </p>
</dl>
<h2>RETURNS</h2>
<p> If the login script fails for any of the devices on the command-line, the exit value of the script will be non-zero and the value will be the number of failures.</p>
<h2>ENVIRONMENT</h2>
<p> <code>clogin</code> recognizes the following environment variables. </p>
<dl>
<dt><code>CISCO_USER</code></p>
<dd> Overrides the user directive found in the <i>.cloginrc</i> file, but may be overridden by the <code>-u</code> option.</p>
<dt><code>CLOGIN</code></p>
<dd> <code>clogin</code> will not change the banner on your xterm window if this includes the character &#8216;x&#8217;.</p>
<dt><code>CLOGINRC</code></p>
<dd> Specifies an alternative location for the <i>.cloginrc</i> file, like the <code>-f</code> option.</p>
<dt><code>HOME</code></p>
<dd> Normally set by <code><a href="/docs/linux/man/1-login/">login</a></code>(1) to the user&#8217;s home directory, HOME is used by <code>clogin</code> to locate the <i>.cloginrc</i> configuration file. </p>
</dl>
<h2>FILES</h2>
<p> <i>$HOME/.cloginrc</i> Configuration file.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-cloginrc/">cloginrc</a></code>(5), <code><a href="/docs/linux/man/1-expect/">expect</a></code>(1)</p>
<h2>CAVEATS</h2>
<p> <code>clogin</code> expects CatOS devices to have a prompt which includes a &#8216;&gt;&#8217;, such as &quot;router&gt; (enable)&quot;. It uses this to determine, for example, whether the command to disable the pager is &quot;set length 0&quot; or &quot;term length 0&quot;. </p>
<p> The HP Procurve switches that are Foundry OEMs use flogin, not hlogin. </p>
<p> The Extreme is supported by <code>clogin,</code> but it has no concept of an &quot;enabled&quot; privilege level. You must set autoenable for these devices in your <i>.cloginrc</i>. </p>
<p> The -S option is a recent addition, it may not be supported in all of the login scripts or for every target device.</p>
<h2>BUGS</h2>
<p> Do not use greater than (&gt;) or pound sign (#) in device banners or hostnames or prompts. These are the normal terminating characters of device prompts and the login scripts need to locate the initial prompt. Afterward, the full prompt is collected and makes a more precise match so that the scripts know when the device is ready for the next command. </p>
<p> All these login scripts for separate devices should be rolled into one. This goal is exceedingly difficult. </p>
<p> The HP Procurve switch, Motorola BSR, and Cisco AGM CLIs rely heavily upon terminal escape codes for cursor/screen manipulation and assumes a vt100 terminal type. They do not provide a way to set a different terminal type or adjust this behavior. The resulting escape codes make automating interaction with these devices very difficult or impossible. Thus bin/hpuifilter, which must be found in the user&#8217;s PATH, is used by hlogin to filter these escape sequences. While this works for rancid&#8217;s collection, there are side effects for interactive logins via hlogin; most of which are formatting annoyances that may be remedied by typing CTRL-R to reprint the current line. </p>
<p> WARNING: repeated ssh login failures to HP Procurves cause the switch&#8217;s management interface to lock-up (this includes snmp, ping) and sometimes it will crash. This is with the latest firmware; 5.33 at the time of this writing. </p>
<h2>Index</h2>

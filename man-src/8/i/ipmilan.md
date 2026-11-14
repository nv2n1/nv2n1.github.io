---
title: "ipmilan(8)"
name: "ipmilan"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipmilan/"
description: "ipmilan – IPMI LAN to System Interface Converter"
---

<p>ipmilan &#8211; IPMI LAN to System Interface Converter</p>
<h2>Synopsis</h2>
<p><code>ipmilan</code> [<code>-c</code> <i>configfile</i>] [<code>-i</code> <i>ipmidevice</i>] [<code>-d</code>] [<code>-n</code>] </p>
<h2>Description</h2>
<p>The <code>ipmilan</code> daemon allows an IPMI system interface using the OpenIPMI device driver to be accessed using the IPMI 1.5 LAN protocol. <code>ipmilan</code> supports the full authentication capabilities of the IPMI LAN protocol. <code>ipmilan</code> supports multiple IP addresses for fault-tolerance. Note that messages coming in on an address are always sent back out on the same address they came in. </p>
<h2>Options</h2>
<dl>
<dt><code>-c</code> file,&nbsp;<wbr><code>&#8211;config-file</code> file</p>
<dd>Set the configuration file to one other than the default of <i>/etc/ipmi_lan.conf</i></p>
<dt><code>-i</code> device,&nbsp;<wbr><code>&#8211;ipmi-dev</code> device</p>
<dd>Sets the desired device</p>
<dt><code>-n</code>,&nbsp;<wbr><code>&#8211;daemonize</code></p>
<dd>Stops the daemon from forking and detaching from the controlling terminal. This is useful for running from init.</p>
<dt><code>-d</code>,&nbsp;<wbr><code>&#8211;debug</code></p>
<dd>Turns on debugging to standard output. You generally have to use <code>-n</code> with this.</p>
<dt><code>-?</code>,&nbsp;<wbr><code>&#8211;help</code>,&nbsp;<wbr><code>&#8211;usage</code></p>
<dd>Prints brief usage hints message. </p>
</dl>
<h2>Configuration</h2>
<p>Configuration is accomplished through the file <i>/etc/ipmi_lan.conf</i>. A file with another name or path may be specified using the <code>-c</code> option. </p>
<p> The following fields are used in many commands: </p>
<p> <i>boolean</i> May be &quot;<code>true</code>&quot;, &quot;<code>false</code>&quot;, &quot;<code>on</code>&quot; or &quot;<code>off</code>&quot;. </p>
<p> <i>priv</i> An IPMI privilege level. This may be &quot;<code>callback</code>&quot;, &quot;<code>user</code>&quot;, &quot;<code>operator</code>&quot;, or &quot;<code>admin</code>&quot;. </p>
<p> <i>auth</i> An IPMI authorization type. This may be &quot;<code>none</code>&quot; for no authentication, &quot;<code>straight</code>&quot; for straight, in-the-clear password authentication, &quot;<code>md2</code>&quot; for use MD2 message digest authentication, or &quot;<code>md5</code>&quot; for using MD5 message digest authentication. </p>
<dl>
<dt><code>addr</code> <i>IP-address</i> [<i>UDP-port</i>]</p>
<dd><i>IP-address</i> specifies the IP address to use for an IP port. Up to 4 addresses may be specified. If no address is specified, it defaults to one port at <code>0.0.0.0</code> (for every address on the machine) at port <code>623</code>. </p>
<p> <i>UDP-port</i> specifies an optional port to listen on. It defaults to <code>623</code> (the standard port). </p>
<dt><code>PEF_alerting&nbsp;<wbr></code><i>boolean</i></p>
<dd>Turn PEF alerting on or off (not currently supported). </p>
<dt><code>per_msg_auth&nbsp;<wbr></code><i>boolean</i></p>
<dd>Turn per-message authentication on or off. </p>
<dt><code>priv_limit&nbsp;<wbr></code><i>priv</i></p>
<dd>The maximum privilege allowed on this interface. </p>
<dt><code>allowed_auths_callback</code> [<i>auth</i> [<i>auth</i> [&#8230;]]]</p>
<dd><i>auth</i> specifies allowed authorization levels for the callback privilege level. Only the levels specified on this line are allowed for the authorization level. If this line is not present, callback authorization cannot be used. </p>
<dt><code>allowed_auths_user</code> [<i>auth</i> [<i>auth</i> [&#8230;]]]</p>
<dd><i>auth</i> specifies allowed authorization levels for the user privilege level. Only the levels specified on this line are allowed for the authorization level. If this line is not present, user authorization cannot be used. </p>
<dt><code>allowed_auths_operator</code> [<i>auth</i> [<i>auth</i> [&#8230;]]]</p>
<dd><i>auth</i> specifies allowed authorization levels for the operator privilege level. Only the levels specified on this line are allowed for the authorization level. If this line is not present, operator authorization cannot be used. </p>
<dt><code>allowed_auths_admin</code> [<i>auth</i> [<i>auth</i> [&#8230;]]]</p>
<dd><i>auth</i> specifies allowed authorization levels for the admin privilege level. Only the levels specified on this line are allowed for the authorization level. If this line is not present, user authorization cannot be used. </p>
<dt><code>user</code> <i>usernum</i> <i>enabled</i> <i>username</i> <i>password</i> <i>max-priv</i> <i>max-session</i> [<i>auth</i> [<i>auth</i> [&#8230;]]]</p>
<dd><i>usernum</i> specifies the user number for the user. Note that user number <code>0</code> is invalid, and user number <code>1</code> is the special &quot;anonymous&quot; user, whose username is ignored. This value may be up to <code>63</code>, the maximum possible IPMI user. If you want anonymous access, you <code>must</code> have a user number <code>1</code><i>. </p>
<p> enabled</i> is a boolean that specified whether the user is enabled or not. </p>
<p> <i>username</i> specifies the name of the user, specified as a name. </p>
<p> <i>password</i> specifies the password of the user, specified as a name. </p>
<p> <i>max-priv</i> specifies the maximum privilege level allowed for the user. </p>
<p> <i>max.sessions</i> specifies the maximum number of session the user may open. </p>
<p> <i>auth</i> specifies the allowed authorization types for the user. Only the specified ones are allowed, so if none are specified, the user will be disabled. </p>
<dt><code>guid</code> <i>name</i></p>
<dd>Allows the 16-byte GUID for the IPMI LAN connection to be specified. If this is not specified, then the GUID command is not supported. </p>
</dl>
<p> Blank lines and lines starting with `#&#8217; are ignored.</p>
<h2>Security</h2>
<p><code>ipmilan</code> implements normal IPMI security. The default is no access for anyone, so the default is pretty safe, but be careful what you add, because this is access to control your box. <code>straight</code> and <code>none</code> authorizations are not recommended, you should probably stick with <code>md2</code> or <code>md5</code>.</p>
<h2>Signals</h2>
<dl>
<dt><code>SIGHUP</code></p>
<dd><code>ipmilan</code> should handle SIGHUP and reread it&#8217;s configuration files. However, it doesn&#8217;t right now. It might in the future, for now you will have to kill it and restart it. Clients should handle reconnecting in this case. If they don&#8217;t, they are broken. </p>
</dl>
<h2>Error Output</h2>
<p>At startup, all error output goes to stderr. After that, all error output goes to syslog.</p>
<h2>Files</h2>
<p>/etc/ipmi_lan.conf</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ipmi_ui/">ipmi_ui</a></code>(1) </p>
<h2>Known Problems</h2>
<p>Currently, <code>ipmilan</code> does not implement writing the config file. IPMI commands to change configuration options are accepted, but the permanent writing of the changes does not currently work.</p>
<h2>Author</h2>
<p>Corey Minyard &lt;cminyard [at] mvista.org&gt;</p>

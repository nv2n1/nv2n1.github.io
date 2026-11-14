---
title: "openipmi_conparms(7)"
name: "openipmi_conparms"
section: "7"
letter: "o"
url: "/docs/linux/man/7-openipmi_conparms/"
description: "openipmi_cmdparms – Connection parameters for OpenIPMI"
---

<p>openipmi_cmdparms &#8211; Connection parameters for OpenIPMI</p>
<h2>Synopsis</h2>
<p><code>smi</code> <i>smi-num</i> <code>lan</code> [<code>-U</code> <i>username</i>] [<code>-P</code> <i>password</i>] [<code>-p[2]</code> <i>port</i>] [<code>-A</code> <i>authtype</i>] [<code>-L</code> <i>privilege</i>] [<code>-s</code>] [<code>-Ra</code> <i>auth alg</i>] [<code>-Ri</code> <i>integ alg</i>] [<code>-Rc</code> <i>conf algo</i>] [<code>-Rl</code>] [<code>-Rk</code> <i>bmc key</i>] [<code>-H</code> <i>hackname</i>] <i>host</i> [ <i>host</i>] </p>
<h2>Description</h2>
<p>The connection parameters for OpenIPMI vary depending on the connection type. This document describes the standard connection types; others may be available from OEMs. </p>
<h2>Options</h2>
<dl>
<dt><i>smi-num</i></p>
<dd>The SMI interface for the local connection. There may be more than one BMC connection on a system and they are generally numbered, like <code>/dev/ipmi0</code>, <code>/dev/ipmi1</code>, etc. </p>
<dt><code>-U&nbsp;<wbr></code><i>username</i></p>
<dd>Use the given <i>username</i> for the LAN connection. If none is given, then no username is used. </p>
<dt><code>-P&nbsp;<wbr></code><i>password</i></p>
<dd>The <i>password</i> to use for the connection. If none is given, the user is assumed to have an empty password </p>
<dt><code>-p</code>[<code>2</code>] <i>port</i></p>
<dd>The UCP <i>port</i> to connect to. This defaults to the standard 623 port, so it is not necessary unless a special port is required. Note that since you can have two connections (hosts), <code>-p</code> is for the first host and <code>-p2</code> is for the second host. </p>
<dt><code>-A&nbsp;<wbr></code><i>authtype</i></p>
<dd>The <i>authentication type</i> to use, one of <code>rmcp+</code>, <code>md5</code>, <code>md2</code>, <code>straight</code>, or <code>none</code>. If you don&#8217;t supply this, the most secure one available is chosen, in the order given in the previous list. </p>
<dt><code>-L&nbsp;<wbr></code><i>privilege</i></p>
<dd>The <i>privilege</i> to use for the connection. Lower privileges cannot execute some commands. Privileges are: <code>callback</code>, <code>user</code>, <code>operator</code>, <code>admin</code>, and <code>oem</code>. The default is <code>admin</code>. </p>
<dt><code>-Ra&nbsp;<wbr></code><i>authentication algorithm</i></p>
<dd>Set the <i>RMCP+ authentication algorithm</i> to use. Options are: <code>bmcpick</code>, <code>rakp_none</code>, <code>rakp_hmac_sha1</code>, and <code>rakp_hmac_md5</code>. The <code>bmcpick</code> option is used by default, which means the BMC picks the algorithm it wants to use. </p>
<dt><code>-Ri&nbsp;<wbr></code><i>integrity algorithm</i></p>
<dd>The <i>RMCP+ integrity algorithm</i> to use. This ensures that the data has not be altered between the sender and receiver. Valid options are: <code>bmcpick</code>, <code>none</code>, <code>hmac_sha1</code>, <code>hmac_md5</code>, and <code>md5</code>. The <code>bmcpick</code> option is used by default, which means the BMC picks the algorithm it wants to use. </p>
<dt><code>-Rc&nbsp;<wbr></code><i>confidentiality algorithm</i></p>
<dd>The <i>RMCP+ confidentiality (encryption) algorithm</i> to use. This keeps eavesdroppers from seeing the data. Valid values are: <code>bmcpick</code>, <code>aes_cbc_128</code>, <code>xrc4_128</code>, and <code>xrc_40</code>. The <code>bmcpick</code> option is used by default, which means the BMC picks the algorithm it wants to use. </p>
<dt><code>-Rl</code></p>
<dd>If this is specified, the username is looked up using the privilege level along with the username. This allows the same name to have different passwords with different privilege levels. </p>
<dt><code>-Rk&nbsp;<wbr></code><i>BMC Key</i></p>
<dd>If the system requires two-key lookups, this specifies the <i>second key</i> (the BMC key) to use. This is ignored if two-key lookups are not enabled by the BMC. </p>
<dt><code>-H&nbsp;<wbr></code><i>hackname</i></p>
<dd>Well, it always happens. Things in the field don&#8217;t work quite like they are supposed to. There was some vagueness in the first IPMI specs and different vendors interpreted RMCP+ in different ways. This allows different options to be supported. Try different hacks if your RMCP+ systems don&#8217;t authenticate properly. These are: </p>
<dl>
<dd>
<dl>
<dt><code>rakp3_wrong_rolem</code></p>
<dd>Some systems use the incorrect Role(m) field in a specific authentication message (the RAKP3 message). This is a common problem. </p>
<dt><code>rmcpp_integ_sik</code></p>
<dd>The original IPMI 2.0 spec specified the incorrect key to use for the integrity key. This forces use of the Session Initiation Key. The default is to use <a href="/docs/linux/man/1-k/">K</a>(1)</dl>
</dl>
<dt><code>-s</code></p>
<dd>Make two connections to the BMC. This means the BMC has two different IP addresses/ports that are equivalent. If this is specified, a second host must be supplied. This is not the same as two connections to two different BMCs. This must be a connection to the same BMC. </p>
<dt><i>host</i></p>
<dd>The IP address (either by name lookup or specified directly) to connect to. If the <code>-s</code> is specified, two hosts must be supplied. </p>
</dl>
<p> The <code>-Ra</code>, <code>-Ri</code>, <code>-Rc</code>, <code>-Rk</code> and <code>-Rl</code> options only apply to RMCP+ connections and will be ignored if the connection does not support RMCP+ or if a non-RMCP+ authentication type is specified.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ipmish/">ipmish</a></code>(8), <code><a href="/docs/linux/man/8-openipmicmd/">openipmicmd</a></code>(8), <code><a href="/docs/linux/man/1-solterm/">solterm</a></code>(1) </p>
<h2>Known Problems</h2>
<p>This is excessively complicated, but the defaults should be good.</p>
<h2>Author</h2>
<p>Corey Minyard &lt;cminyard [at] mvista.org&gt;</p>

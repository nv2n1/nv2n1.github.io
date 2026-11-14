---
title: "isdnctrl_conf(8)"
name: "isdnctrl_conf"
section: "8"
letter: "i"
url: "/docs/linux/man/8-isdnctrl_conf/"
description: "isdnctrl_conf – isdnctrl configuration"
---

<p>isdnctrl_conf &#8211; isdnctrl configuration</p>
<dl>
<dt><code>writeconf</code><i> file</i></p>
<dd>Writes the configuration into a file. If <i>file</i> is omitted, the default file <code>/etc/isdn/isdn.conf</code> will be used.</p>
<dt><code>readconf</code><i> file</i></p>
<dd>Reads the configuration from a file. If <i>file</i> is omitted, the default file <code>/etc/isdn/isdn.conf</code> will be used.</dl>
<h3>Syntax of the configuration file</h3>
<p>This syntax will be used for the options <code>readconf</code> and <code>writeconf.</code> All entries are included in the section <code>[ISDNCTRL].</code> This section contains an entry <code>INTERFACES,</code> which describes the interfaces. Each subsection <code>[INTERFACE]</code> or <code>[SLAVE]</code> describes one interface. There are the following entries possible:</p>
<dl>
<dt><code>NAME = </code><i>name</i></p>
<dd>The name of the interface. This entry is required. <code>Example:</code> NAME = ippp0</p>
<dt><code>EAZ = </code><i>eaz</i></p>
<dd>Set the EAZ or the MSN. This entry is required. <code>Example:</code> EAZ = 4711</p>
<dt><code>PHONE_IN = </code><i>num</i><code> [</code><i>num</i><code>&#8230;]</code></p>
<dd>Set the incoming phone number(s). It requires at least one blank between the different numbers. <code>Example:</code> PHONE_IN = 08151234 08151235 08151236</p>
<dt><code>PHONE_OUT = </code><i>num</i><code> [</code><i>num</i><code>&#8230;]</code></p>
<dd>Set the outgoing phone number(s). It requires at least one blank between the different numbers. <code>Example:</code> PHONE_OUT = 08151237 08151238</p>
<dt><code>SECURE = on|off</code></p>
<dd>Turn on or off the security feature. <code>Example:</code> SECURE = on</p>
<dt><code>CALLBACK = off|in|out</code></p>
<dd>Selects callback mode. <code>Example:</code> CALLBACK = in</p>
<dt><code>CBHUP = on|off</code></p>
<dd>Turns on or off hangup before starting callback. <code>Example:</code> CBHUP = on</p>
<dt><code>CBDELAY = </code><i>seconds</i></p>
<dd>Set the callback delay to <i>seconds</i>. <code>Example:</code> CBDELAY = 5</p>
<dt><code>DIALMAX = </code><i>num</i></p>
<dd>Set the number of dial attempts to <i>num</i>. <code>Example:</code> DIALMAX = 1</p>
<dt><code>HUPTIMEOUT = </code><i>seconds</i></p>
<dd>Set the hangup time to <i>seconds</i>. <code>Example:</code> HUPTIMEOUT = 20</p>
<dt><code>IHUP = on|off</code></p>
<dd>Turns on or off the hangup timeout for incoming calls. <code>Example:</code> IHUP = on</p>
<dt><code>CHARGEHUP = on|off</code></p>
<dd>Turns on or off hangup before next charge info. <code>Example:</code> CHARGEHUP = on</p>
<dt><code>CHARGEINT = </code><i>seconds</i></p>
<dd>Sets the charge interval to <i>seconds</i>. <code>Example:</code> CHARGEINT = 1</p>
<dt><code>L2_PROT = </code><i>protocol</i></p>
<dd>Set the layer-2 protocol. Allowed values for <i>protocol</i> are<code> x75i</code>,<code> x75ui</code>,<code> x75bui </code>and<code> hdlc</code>. <code>Example:</code> L2_PROT = hdlc</p>
<dt><code>L3_PROT = </code><i>protocol</i></p>
<dd>Set the layer-3 protocol. Allowed value for <i>protocol</i> is only <code>trans</code>. <code>Example:</code> L3_PROT = trans</p>
<dt><code>ENCAP = </code><i>encapsulation</i></p>
<dd>Sets the encapsulation mode. Allowed values for <i>encapsulation</i> are<code> rawip</code>,<code> ip</code>,<code> cisco_h</code>,<code> cisco_hk</code>,<code> ethernet</code>,<code> syncppp </code>and<code> uihdlc</code>. <code>Example:</code> ENCAP = rawip</p>
<dt><code>ADDSLAVE = </code><i>slave</i></p>
<dd>Adds a slave interface for channel-bundling. <code>Example:</code> ADDSLAVE = s-ippp0</p>
<dt><code>SDELAY = </code><i>seconds</i></p>
<dd>Set the delay in seconds for the slave-dialing. <code>Example:</code> SDELAY = 10</p>
<dt><code>TRIGGER = </code><i>cps</i></p>
<dd>Set trigger level for slave-dialing. <code>Example:</code> TRIGGER = 4000</p>
<dt><code>BIND = </code><i>driverId</i><code>,</code><i>channel</i></p>
<dd>Binds the current interface to a specific physical channel. Before and after the comma may not be a blank. <code>Example:</code> BIND = teles1,0</p>
<dt><code>PPPBIND = </code><i>num</i></p>
<dd>Binds the current interface to the ippp device <code>/dev/ippp</code><i>X</i><code>.</code> This works only for synchronous PPP. The value must be a number. <code>Example:</code> PPPBIND = 0</p>
<dt><code>Example for a configuration file</code></p>
<dd>[ISDNCTRL]<br />
&nbsp;<wbr>&nbsp;<wbr>INTERFACES&nbsp;<wbr>=&nbsp;<wbr>{<br />
&nbsp;<wbr>[INTERFACE]<br />
&nbsp;<wbr>NAME&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>isdn0<br />
&nbsp;<wbr>EAZ&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>4711<br />
&nbsp;<wbr>PHONE_IN&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>08151234<br />
&nbsp;<wbr>PHONE_OUT&nbsp;<wbr>=&nbsp;<wbr>08151234<br />
&nbsp;<wbr>SECURE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>on<br />
&nbsp;<wbr>DIALMAX&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>1<br />
&nbsp;<wbr>HUPTIMEOUT=&nbsp;<wbr>20<br />
&nbsp;<wbr>IHUP&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>on<br />
&nbsp;<wbr>CHARGEHUP&nbsp;<wbr>=&nbsp;<wbr>on<br />
&nbsp;<wbr>L2_PROT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>hdlc<br />
&nbsp;<wbr>L3_PROT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>trans<br />
&nbsp;<wbr>ENCAP&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>rawip<br />
&nbsp;<wbr>ADDSLAVE&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>s-isdn0<br />
&nbsp;<wbr>SDELAY&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>10 </p>
<pre><code>[SLAVE]

NAME      = s-isdn0

EAZ       = 4711

PHONE_OUT = 08151234

SECURE    = on

DIALMAX   = 1

HUPTIMEOUT= 10

IHUP      = on

CHARGEHUP = on

L2_PROT   = hdlc

L3_PROT   = trans

ENCAP     = rawip
[INTERFACE]

NAME      = ippp0

EAZ       = 4712

PHONE_OUT = 08151235 08151236

SECURE    = on

DIALMAX   = 5

HUPTIMEOUT= 200

IHUP      = on

CHARGEHUP = on

L2_PROT   = hdlc

L3_PROT   = trans

ENCAP     = syncppp

PPPBIND   = 0
}
</code></pre>

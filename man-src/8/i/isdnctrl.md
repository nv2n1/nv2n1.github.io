---
title: "isdnctrl(8)"
name: "isdnctrl"
section: "8"
letter: "i"
url: "/docs/linux/man/8-isdnctrl/"
description: "isdnctrl – get/set ISDN device information"
---

<p>isdnctrl &#8211; get/set ISDN device information</p>
<h2>Synopsis</h2>
<p><code>isdnctrl</code><i> action device </i><code>&#8230;</code></p>
<h2>Description</h2>
<p><code>isdnctrl</code> is used to create and delete network interfaces for <font SIZE="-1">ISDN,</font> set up the various parameters and phone numbers for dial in and dial out. It is also used to list the current parameters of an already configured network interface. <code>isdnctrl</code> is <code>not</code> needed for configuration of <font SIZE="-1">ISDN</font> ttys! The use of <code>isdnctrl</code> is independent of the hardware driver. </p>
<h2>Options</h2>
<p>The following <code>actions</code> may be given to <code>isdnctrl</code>.</p>
<dl>
<dt><code>addif</code><i> name</i></p>
<dd>Adds a new <font SIZE="-1">ISDN</font> interface <i>name</i> to the kernel. If <i>name</i> is omitted, the kernel will use <code>ethX,</code> where X is an increasing number starting from 0. This is not ideal so providing a name such as <code>isdn0</code> (for raw ip interfaces) or <code>ippp0</code> (for synchronous PPP interfaces) is strongly recommended.</p>
<dt><code>delif</code><i> name </i><code>[force]</code></p>
<dd>Removes the <font SIZE="-1">ISDN</font> interface <i>name</i> from the kernel. If the optional keyword <code>force</code> is appended, <code>isdnctrl</code> executes <code>ifconfig</code><i> name </i><code>down</code> before removing it.</p>
<dt><code>reset [force]</code></p>
<dd>Removes all <font SIZE="-1">ISDN</font> interfaces from the kernel if possible. If the optional keyword <code>force</code> is appended, <code>isdnctrl</code> executes <code>ifconfig</code><i> name </i><code>down</code> before removing an interface.</p>
<dt><code>ifdefaults</code><i> name </i></p>
<dd>resets interface <i>name</i> to reasonable defaults.</p>
<dt><code>dialmode</code><i> name </i><code>[</code><i>off</i><code>|</code><i>manual</i><code>|</code><i>auto</i><code>]</code></p>
<dd>Sets the dial mode of the interface to one of:</dl>
<dl>
<dd><code>off</code><br />
 no connection can be made; an existing connection is terminated immediately. Also, incoming connections are not possible. </p>
<p> <code>manual</code><br />
 manual dialing / hangup; a connection will only be made after <code>isdnctrl dial</code> <i>name</i> but the line will be disconnected after the huptimeout value set if using kernel drivers updated since 1 Nov 1998; otherwise an explicit <code>isdnctrl hangup</code> <i>name</i> will be needed to cause the connection to be dropped.<br />
 Incoming connections are possible; however, if this interface is configured in <code>callback in</code> mode, the callback dial will not happen (as this is actually an outgoing connection, not an incoming one). </p>
<p> <code>auto</code><br />
 autodial mode; an outgoing packet will trigger a dialout, and a hangup will occur after the huptimeout value specified (see below).<br />
 An interface in <code>auto</code> dial mode will call another system back (if configured in <code>callback in</code> mode). </p>
<p> <code>auto</code> was the &quot;old&quot; behaviour (as it was before <code>dialmode</code> was implemented). </p>
<p> If no argument is given, the current dialmode value is displayed. </p>
<p> You can give <code>all</code> as the interface name; the command will then be executed for all interfaces.</dl>
<dl>
<dt><code>addphone</code><i> name </i><code>out</code><i> num</i></p>
<dd>Adds the phone number <i>num</i> to the list of outgoing numbers of the <font SIZE="-1">ISDN</font> interface <i>name</i>. Numbers in this list are used to dial the remote station if the connection is down and packets are to be sent via the interface (Dial on demand). More than one number can be set by calling <code>isdnctrl addphone</code> repeatedly. If more than one number is set, these will be tried one after another (the last added number is tried first, etc.). When using a German SPV-type connection, the number has to be prefixed by a capital S.</p>
<dt><code>addphone</code><i> name </i><code>in</code><i> num</i></p>
<dd>Adds the phone number <i>num</i> to the list of incoming numbers of the <font SIZE="-1">ISDN</font> interface <i>name</i>. Numbers in this list are used to verify access permission of the remote station if an incoming call is received. The verification can be disabled by setting the interface into insecure mode using <code>isdnctrl</code><i> name </i><code>secure</code><i> off.</i> If the list is empty, incoming calls are disabled. More than one number can be added by calling <code>isdnctrl addphone</code> repeatedly. Also wildcards can be used (see below).</p>
<dt><code>delphone</code><i> name </i><code>in|out</code><i> num</i></p>
<dd>Removes phone number <i>num</i> from the incoming or outgoing phone list.</p>
<dt><code>eaz</code><i> name </i><code>[</code><i>num</i><code>]</code></p>
<dd>Set the EAZ (German 1TR6 protocol) or MSN (Euro-ISDN E-DSS1) for <font SIZE="-1">ISDN</font> interface <i>name</i> to <i>num</i>. For an EAZ this is only one digit, while for an MSN <i>num</i> is the whole MSN (usually the local phone number). If <i>num</i> is omitted, <code>isdnctrl</code> prints the current setting for <font SIZE="-1">ISDN</font> interface <i>name</i>.</p>
<dt><code>huptimeout</code><i> name </i><code>[</code><i>seconds</i><code>]</code></p>
<dd>Set the hangup timeout for <font SIZE="-1">ISDN</font> interface <i>name</i> to <i>seconds</i>. If there is inactivity (i.e. no traffic on the interface) for the given time the driver automatically shuts down the connection. If <i>seconds</i> is omitted <code>isdnctrl</code> prints the current setting for interface <i>name</i>.</p>
<dt><code>cbdelay</code><i> name </i><code>[</code><i>seconds</i><code>]</code></p>
<dd>Set the callback delay for <font SIZE="-1">ISDN</font> interface <i>name</i> to <i>seconds</i>. If callback mode for this interface is <code>in</code>, dialing is delayed the given time. If the callback mode is <code>out</code>, after dialing out and waiting the given time, a hangup is issued to free the line for the incoming callback from the remote machine. This hangup-after-dial is disabled by setting <code>cbdelay</code> to 0. If <i>seconds</i> is omitted <code>isdnctrl</code> prints the current setting for interface <i>name</i>.</p>
<dt><code>dialmax</code><i> name </i><code>[</code><i>num</i><code>]</code></p>
<dd>Set the number of dial attempts for <font SIZE="-1">ISDN</font> interface <i>name</i> to <i>num</i>. If dialing, each phone number is tried this many times before giving up. If <i>num</i> is omitted <code>isdnctrl</code> prints the current setting for interface <i>name</i>.</p>
<dt><code>ihup</code><i> name </i><code>[on|off]</code></p>
<dd>Turn on or off the hangup timeout for incoming calls on interface <i>name</i>. If on or off is omitted the current setting is printed.</p>
<dt><code>chargehup</code><i> name </i><code>[on|off]</code></p>
<dd>Turn on or off hangup before next charge info for interface <i>name</i>. This can only be used if the <font SIZE="-1">ISDN</font> provider transmits charge info during and after the connection. If set to on, the driver will close the connection just before the next charge info will be received if the interface is inactive. If on or off is omitted the current setting is printed.</p>
<dt><code>chargeint</code><i> name </i><code>[</code><i>seconds</i><code>]</code></p>
<dd>If <i>seconds</i> are given, the charge interval for the given interface is set. This may be useful on <font SIZE="-1">ISDN</font> lines with no chargeinfo or no online chargeinfo. The connection will be closed 2 seconds before the end of the next estimated charge interval if <i>huptimeout</i> seconds of inactivity have been reached. If <i>ihup </i> is <code>on</code>, incoming connections are closed by this mechanism also. On lines with online charge info you also might ask by <code>chargeint</code><i> name</i> for the current charge interval as delivered from the telecom on a given interface.</p>
<dt><code>secure</code><i> name </i><code>[on|off]</code></p>
<dd>Turns on or off the security feature for interface <i>name</i>. If set to <code>on</code>, incoming calls will only be accepted if the calling number can be found in the incoming access list. See description of action <code>addphone</code> for information about how to add numbers to this list. If<code> on </code>or<code> off</code> is omitted, the current setting is printed.</p>
<dt><code>callback</code><i> name </i><code>[</code><i>mode</i><code>]</code></p>
<dd>Set callback mode for interface <i>name</i> to mode <i>mode</i>. If callback mode is <code>in</code>, then after getting an incoming call, a callback is triggered. If callback mode is <code>out</code>, then the local system does the initial call and then waits for callback of the remote machine. The option <code>on</code> is available only for compatibility with older versions. Its meaning is the same like <code>in</code>. If callback mode is <code>off</code>, calls are handled normally without special processing.</p>
<dt><code>cbhup</code><i> name </i><code>[on|off]</code></p>
<dd>Turns on or off Hangup (Reject) for interface <i>name</i> before starting callback. If cbhup is <code>on</code>, when receiving an incoming call, the interface first rejects that call before the callback sequence is started. If <code>on</code> or <code>off</code> is omitted, the current setting is printed.</p>
<dt><code>encap</code><i> name </i><code>[</code><i>encapsulation</i><code>]</code></p>
<dd>Set the encapsulation mode for interface <i>name</i>. Possible encapsulations are:</dl>
<dl>
<dd><code>rawip</code><br />
 raw ip encapsulation (default) </p>
<p> <code>ip</code><br />
 IP + typefield encapsulation </p>
<p> <code>cisco-h</code><br />
 Special mode for communicating with a Cisco in HDLC-mode with Cisco-keepalive switched off. </p>
<p> <code>ethernet</code><br />
 ethernet over <font SIZE="-1">ISDN</font> (MAC-header included) </p>
<p> <code>syncppp</code><br />
 Synchronous PPP over <font SIZE="-1">ISDN</font> </p>
<p> <code>uihdlc</code><br />
 raw ip with additional ui-header </p>
<p> <code>cisco-hk</code><br />
 Special mode for communicating with a Cisco in HDLC-mode with Cisco-keepalive switched on. </p>
<p> <code>x25iface</code><br />
 Provides an interface as required by the Linux X.25 PLP protocol implementation (requires Linux 2.1.x or newer).</dl>
<p> If <i>encapsulation</i> is omitted, the current setting is printed.</p>
<dl>
<dt><code>l2_prot</code><i> name </i><code>[protocol]</code></p>
<dd>Set the layer-2 protocol for interface <i>name</i>. Possible values for <i>protocol</i> are:<br />
 <code>x75i</code>, <code>x75ui</code>, <code>x75bui</code> and <code>hdlc</code>. If <i>protocol</i> is omitted the current setting is printed.</p>
<dt><code>l3_prot name [protocol]</code></p>
<dd>Set the layer-3 protocol for interface <i>name</i>. At the moment only <code>trans</code> is supported here. If <i>protocol</i> is omitted the current setting is printed.</p>
<dt><code>list</code><i> name</i></p>
<dd>List all parameters and the charge info for interface <i>name</i>. If <i>name</i> is <code>all</code>, all interfaces are listed.</p>
<dt><code>status</code><i> name</i></p>
<dd>Show the connection status for interface <i>name</i>. The output can be one of the following types:</p>
<dl>
<dd><code>ippp0 not connected</code><br />
 There is no connection </p>
<p> <code>ippp0 connected to 0123456789</code><br />
 There is an outgoing connection to phone number 0123456789 </p>
<p> <code>ippp0 connected from 0123456789</code><br />
 There is an incoming connection from phone number 0123456789</dl>
<p> If the interface is connected, the exit status of the command is true, else it is false.<br />
 If <i>name</i> is <code>all</code>, then the connection status for all interfaces is shown. The exit status is always true in this case.<br />
 If <i>name</i> is <code>active</code>, then only those interfaces that are currently connected are shown. The exit status is always true in this case.</p>
<dt><code>verbose</code><i> num</i></p>
<dd>Set verbosity level to <i>num</i>.</p>
<dt><code>hangup</code><i> name</i></p>
<dd>The connection of interface <i>name</i> is closed immediately.</p>
<dt><code>bind</code><i> name driverId</i><code>,</code><i>channel </i><code>[exclusive]</code></p>
<dd>Binds an interface <i>name</i> to a physical channel. The <i>driverId</i> identifies a specific S0-Port. The channels of a port start counting with zero. If <code>exclusive</code> is given, other interfaces cannot use that channel anymore. Otherwise, the channel may be used by other interfaces.</p>
<dt><code>unbind</code><i> name</i></p>
<dd>Unbinds a the previously bound interface <i>name</i>.</p>
<dt><code>pppbind</code><i> name </i><code>[</code><i>num</i><code>]</code></p>
<dd>Binds the interface <i>name</i> to an ippp device <code>/dev/ippp</code><i>num</i><code>.</code> This works only for synchronous ppp. The value must be a number. If <i>num</i> is omitted and <i>name</i> is called <code>ippp</code><i>X</i> , then the interface is bound to <code>/dev/ippp</code><i>X</i><code>.</code></p>
<dt><code>pppunbind</code><i> name</i></p>
<dd>Unbinds the previously bound interface <i>name</i>. </p>
<dt><code>busreject</code><i> driverId </i><code>[on|off]</code></p>
<dd>If switched <code>on</code>, instead of ignoring incoming calls not matching any interface, isdn4linux responds with a <code>REJECT</code> to those calls. If switched <code>off</code>, isdn4linux is passive, allowing other devices connected to the same S0-bus to answer the call. You normally should <code>not</code> enable this feature, if the <font SIZE="-1">ISDN</font> adaptor is not the only device connected to the S0-bus. Otherwise it could happen, that isdn4linux rejects an incoming call which belongs to another device on the bus. </p>
<dt><code>addslave</code><i> name slave</i></p>
<dd>Adds a slave interface named <i>slave</i> to interface <i>name</i> for raw channel-bundling. For bundling of more than two channels, any number of slaves can be added to an interface by using this command repeatedly. <i>name</i> must refer to an existing &quot;master&quot; interface (not a slave). Slave interfaces are not visible to the kernel, however all usual <font SIZE="-1">ISDN</font> settings can be configured. Because slave interfaces are not visible to the kernel, they are configured &quot;through&quot; their &quot;master&quot;, so <code>it is important</code> that slave interfaces are added <code>before</code> the corresponding &quot;master&quot; is started by <code>ifconfig</code>. If the &quot;master&quot; is already up, it has to be shutdown with <code>ifconfig down &#8230;</code> otherwise the <code>addslave</code> command will be rejected. </p>
<dt><code>sdelay</code><i> name num</i></p>
<dd>Set delay for slave-dialing. The master interface <i>name</i> has to have a load of more than <code>trigger</code> cps for at least <i>num</i> seconds, before its slave starts dialing.<br />
 Note that this only works for rawIP, not MPPP! </p>
<dt><code>trigger</code><i> name num</i></p>
<dd>Set trigger level for slave-dialing. The master interface <i>name</i> has to have a load of more than <i>num</i> cps for at least <code>sdelay</code> seconds, before its slave starts dialing.<br />
 Note that this only works for rawIP, not MPPP! </p>
<dt><code>addlink</code><i> name</i></p>
<dd>For MPPP, this adds a slave interface to the existing connection, i.e. connect the extra channel now. It is like a <code>dial</code> command for the extra channel.<br />
 This also means that <code>addlink</code> will only work if the master interface <i>name</i> must already be connected! Also, the <code>dialmode</code> for the slave interface must be <i>auto</i>. </p>
<dt><code>removelink</code><i> name</i></p>
<dd>For MPPP, this removes a slave interface from the existing connection, i.e. hangup the extra channel now. </p>
<dt><code>dial</code><i> name</i></p>
<dd>Force dialing of interface <i>name</i>.</p>
<dt><code>mapping</code><i> driverId MSN0</i><code>[,</code><i>MSN1</i><code>[,</code><i>MSN2</i><code>]] &#8230; [,</code><i>MSN9</i><code>]</code></p>
<dd>Installs a mapping-table for MSN&lt;-&gt;EAZ-mapping. See README for details.</dl>
<h2>Wildcards</h2>
<p>When using <code>isdnctrl addphone </code><i>name</i><code> in </code><i>num</i> to add phone numbers to the incoming-call accept-list of an interface, wildcards similar to shell wildcards can be used. The following wildcards are supported: </p>
<dl>
<dt><code>?</code></p>
<dd>one arbitrary digit</p>
<dt><code>*</code></p>
<dd>zero or arbitrary number of digits</p>
<dt><code>[</code><i>list</i><code>]</code></p>
<dd>one of the digits in <i>list</i></p>
<dt><code>[</code><i>1</i><code>&#8211;</code><i>5</i><code>]</code></p>
<dd>one digit in the range of (including) <i>1</i> and <i>5</i>.</p>
<dt><code>^</code></p>
<dd>if this appears as the first character in a list, inverts the list.</dl>
<h2>Bugs</h2>
<p>This man page is not complete. </p>
<h2>Author</h2>
<p>Fritz Elfert &lt;fritz [at] isdn4linux.de&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/4-ttyi/">ttyI</a></code>(4), <code><a href="/docs/linux/man/4-isdnctrl/">isdnctrl</a></code>(4), <code><a href="/docs/linux/man/4-isdninfo/">isdninfo</a></code>(4), <code><a href="/docs/linux/man/4-isdn_audio/">isdn_audio</a></code>(4), <code><a href="/docs/linux/man/7-isdn_cause/">isdn_cause</a></code>(7). </p>

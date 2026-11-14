---
title: "isdnctrl(4)"
name: "isdnctrl"
section: "4"
letter: "i"
url: "/docs/linux/man/4-isdnctrl/"
description: "isdnctrl – ISDN control device"
---

<p>isdnctrl &#8211; ISDN control device</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;linux/isdn.h&gt;</code></pre>
<h2>Description</h2>
<p><i>/dev/isdnctrl</i> is a character device with major number <code>45</code> and minor numbers <code>64</code> to <code>127</code>. It allows controlling functionality of the Linux <font SIZE="-1">ISDN</font> subsystem.</p>
<h2>Ioctl Functions</h2>
<p>Currently, the following ioctl calls are supported:</p>
<dl>
<dt><code>IIOCNETAIF</code></p>
<dd>Add an <font SIZE="-1">ISDN</font> network interface.</p>
<dl>
<dd>This function adds a network interface to the kernel&#8217;s device table. This interface can be used just like normal eth interfaces.</p>
<dl>
<dt>Argument:</p>
<dd><i>arg</i> should point to a zero terminated string of max. 10 characters. if <i>arg</i> is NULL, the kernel assigns a name.</p>
<dt>Return:</p>
<dd>On success, the name of the new interface is copied to <i>arg</i>. and the call returns 0. On failure, an error code is returned.</dl>
</dl>
<dt><code>IIOCNETASL</code></p>
<dd>Create a slave interface.</p>
<dl>
<dd>Creates a slave interface for RAW-device channel-bundling. These devices behave like network-interfaces, except they are invisible to user. Only <font SIZE="-1">ISDN</font> parameters can be controlled, not IP-parameters. IP-parameters are inherited from the corresponding master-device.</p>
<dl>
<dt>Argument:</p>
<dd><i>arg</i> should point to a zero terminated string of max. 21 characters containing two comma-separated names. The first part is the name of an existing <font SIZE="-1">ISDN</font> network device, which will be master. The second part will be the name of the new slave interface.</p>
<dt>Return:</p>
<dd>On success, the name of the new interface is copied to <i>arg</i>. and the call returns 0. On failure, an error code is returned.</dl>
</dl>
<dt><code>IIOCNETDIF</code></p>
<dd>Delete a network-interface.</p>
<dl>
<dd>This call deletes an existing <font SIZE="-1">ISDN</font> network interface.</p>
<dl>
<dt>Argument:</p>
<dd><i>arg</i> should point to a zero terminated string of max. 10 characters naming an existing interface which will be deleted. If the interface is a master interface, all its slave-interfaces will be deleted also.</p>
<dt>Return:</p>
<dd>On success, the call returns 0. On failure, an error code is returned.</dl>
</dl>
<dt><code>IIOCNETSCF</code></p>
<dd>Set configurable parameters of an <font SIZE="-1">ISDN</font> network interface.</p>
<dl>
<dd>This call replaces all <font SIZE="-1">ISDN</font> related parameters of an interface by the parameters given.</p>
<dl>
<dt>Argument:</p>
<dd><i>arg</i> should point to a <i>struct isdn_net_ioctl_cfg</i> (defined in linux/isdn.h)</p>
<dt>Return:</p>
<dd>On success, the call returns 0. On failure, an error code is returned.</dl>
</dl>
<dt><code>IIOCNETGCF</code></p>
<dd>Get configurable parameters of an <font SIZE="-1">ISDN</font> network interface.</p>
<dl>
<dd>This call returns all <font SIZE="-1">ISDN</font> related parameters of an interface.</p>
<dl>
<dt>Argument:</p>
<dd><i>arg</i> should point to a <i>struct isdn_net_ioctl_cfg</i> (defined in linux/isdn.h) which will be filled by the current setup.</p>
<dt>Return:</p>
<dd>On success, the call returns 0 and the interface-setup is copied to *arg. On failure, an error code is returned.</dl>
</dl>
<dt><code>IIOCNETANM</code></p>
<dd>Add a phone number to an <font SIZE="-1">ISDN</font> network interface.</p>
<dl>
<dd>This call adds a phone number to an existing network interface.</p>
<dl>
<dt>Argument:</p>
<dd><i>arg</i> should point to a <i>struct isdn_net_ioctl_phone</i> which contains necessary information.</p>
<dt>Return:</p>
<dd>On success, the call returns 0 and the phone number is added to either outgoing or incoming number list. On failure, an error code is returned.</dl>
</dl>
<dt><code>IIOCNETDNM</code></p>
<dd>Delete a phone number from an <font SIZE="-1">ISDN</font> network interface.</p>
<dl>
<dd>This call deletes a phone number from an existing network interface.</p>
<dl>
<dt>Argument:</p>
<dd><i>arg</i> should point to a <i>struct isdn_net_ioctl_phone</i> which contains necessary information.</p>
<dt>Return:</p>
<dd>On success, the call returns 0 and the phone number is deleted from either outgoing or incoming number list. On failure, an error code is returned.</dl>
</dl>
<dt><code>IIOCNETGNM</code></p>
<dd>Get list of phone numbers from an <font SIZE="-1">ISDN</font> network interface.</p>
<dl>
<dd>This call returns the list of phone numbers associated to an existing network interface.</p>
<dl>
<dt>Argument:</p>
<dd><i>arg</i> should point to a union of <i>struct isdn_net_ioctl_phone</i> and a buffer, large enough to hold a concatenated list of strings containing the phone numbers.</p>
<dt>Return:</p>
<dd>On success, the call returns 0 and the list of phone numbers is returned as a space-separated list of number-strings terminated by a NULL byte.</dl>
</dl>
<dt><code>IIOCNETDIL</code></p>
<dd>Trigger dialing of an <font SIZE="-1">ISDN</font> network interface.</p>
<dl>
<dd>This call initiates dialing of an <font SIZE="-1">ISDN</font> network interface, if it is not connected. Normally, this ioctl is not needed, because <font SIZE="-1">ISDN</font> network interface perform dial on demand by default.</p>
<dl>
<dt>Argument:</p>
<dd><i>arg</i> should point to a zero terminated string of max. 10 characters naming the desired interface.</p>
<dt>Return:</p>
<dd>On success, the call returns 0 and the interface starts dialing.</dl>
</dl>
<dt><code>IIOCNETHUP</code></p>
<dd>Hangup an <font SIZE="-1">ISDN</font> network interface.</p>
<dl>
<dd>This call initiates hangup of an <font SIZE="-1">ISDN</font> network interface, if it is connected.</p>
<dl>
<dt>Argument:</p>
<dd><i>arg</i> should point to a zero terminated string of max. 10 characters naming the desired interface.</p>
<dt>Return:</p>
<dd>On success, the call returns 0 and the interface hangs up.</dl>
</dl>
<dt><code>IIOCNETALN</code></p>
<dd>Add a link of an MPP-configured <font SIZE="-1">ISDN</font> network interface.</p>
<dl>
<dd>This call initiates dialing of a Multilink-PPP slave <font SIZE="-1">ISDN</font> network interface, if it is not connected.</p>
<dl>
<dt>Argument:</p>
<dd><i>arg</i> should point to a zero terminated string of max. 10 characters naming the desired interface.</p>
<dt>Return:</p>
<dd>On success, the call returns 0 and the interface starts dialing.</dl>
</dl>
<dt><code>IIOCNETDLN</code></p>
<dd>Hangup an MPP-configured <font SIZE="-1">ISDN</font> network interface.</p>
<dl>
<dd>This call initiates hangup of an Multilink-PPP <font SIZE="-1">ISDN</font> network interface, if it is connected.</p>
<dl>
<dt>Argument:</p>
<dd><i>arg</i> should point to a zero terminated string of max. 10 characters naming the desired interface.</p>
<dt>Return:</p>
<dd>On success, the call returns 0 and the interface hangs up.</dl>
</dl>
<dt><code>IIOCNETARU</code></p>
<dd>Add a timeout rule to an <font SIZE="-1">ISDN</font> network interface.</p>
<dl>
<dd>This call adds a timeout rule to an existing interface.</p>
<dl>
<dt>Argument:</p>
<dd><i>arg</i> should point to a <i>struct isdn_ioctl_timeout_rule</i> containing the necessary parameters.</p>
<dt>Return:</p>
<dd>On success, the call returns 0 and the rule is added to the rule list of the interface.</dl>
</dl>
<dt><code>IIOCNETDRU</code></p>
<dd>Delete a timeout rule from an <font SIZE="-1">ISDN</font> network interface.</p>
<dl>
<dd>This call deletes a timeout rule from an existing interface.</p>
<dl>
<dt>Argument:</p>
<dd><i>arg</i> should point to a <i>struct isdn_ioctl_timeout_rule</i> containing the necessary parameters.</p>
<dt>Return:</p>
<dd>On success, the call returns 0 and the rule is deleted from the rule list of the interface.</dl>
</dl>
<dt><code>IIOCNETGRU</code></p>
<dd>Get a timeout rule from an <font SIZE="-1">ISDN</font> network interface.</p>
<dl>
<dd>This call returns a timeout rule from an existing interface.</p>
<dl>
<dt>Argument:</p>
<dd><i>arg</i> should point to a <i>struct isdn_ioctl_timeout_rule</i> containing the necessary parameters.</p>
<dt>Return:</p>
<dd>On success, the call returns 0 and the struct is filled from the rule list of the interface.</dl>
</dl>
<dt><code>IIOCNETBUD</code></p>
<dd>Handle budget accounting of an <font SIZE="-1">ISDN</font> network interface.</p>
<dl>
<dd>
<dl>
<dt>Argument and Return:</p>
<dd>to be defined.</dl>
</dl>
<dt><code>IIOCSETVER</code></p>
<dd>Set verbosity of link level.</p>
<dl>
<dd>
<dl>
<dt>Argument:</p>
<dd><i>arg</i> is an integer, defining the new verbose value.</p>
<dt>Return:</p>
<dd>This call always returns 0.</dl>
</dl>
<dt><code>IIOCSETGST</code></p>
<dd>Set global stop flag of link level.</p>
<dl>
<dd>
<dl>
<dt>Argument:</p>
<dd><i>arg</i> is an integer, defining the new stop flag value (0 or !0).</p>
<dt>Return:</p>
<dd>This call always returns 0.</dl>
</dl>
<dt><code>IIOCSETBRJ</code></p>
<dd>Set busreject flag of a lowlevel driver.</p>
<dl>
<dd>
<dl>
<dt>Argument:</p>
<dd><i>arg</i> should point to an <i>struct isdn_ioctl_struct</i> containing the driver&#8217;s ID and the value of the busreject flag.</p>
<dt>Return:</p>
<dd>On success, the call returns 0 and the busreject flag of the selected driver is set according the given parameter.</dl>
</dl>
<dt><code>IIOCSIGPRF</code></p>
<dd>Enable signaling on change of modem profiles.</p>
<dl>
<dd>With this call, the calling process is registered to receive a SIGIO on every change of any register of any ttyI. Thus it can read register settings and save them to a file. The calling process has to keep the device open in order to receive notifications. As soon as it closes the device, registration is deleted.</p>
<dl>
<dt>Argument:</p>
<dd>none</p>
<dt>Return:</p>
<dd>This call always returns 0.</dl>
</dl>
<dt><code>IIOCGETPRF</code></p>
<dd>Get all modem register settings.</p>
<dl>
<dd>With this call, all modem registers of all ttyI devices can be read.</p>
<dl>
<dt>Argument:</p>
<dd><i>arg</i> should point to a buffer of length ( <code>ISDN_MODEM_ANZREG</code> + <code>ISDN_MSNLEN</code> ) * <code>ISDN_MAX_CHANNELS</code>.</p>
<dt>Return:</p>
<dd>On return, the provided buffer is filled with the register values.</dl>
</dl>
<dt><code>IIOCSETPRF</code></p>
<dd>Set all modem register settings.</p>
<dl>
<dd>With this call, all modem registers of all ttyI devices can be written.</p>
<dl>
<dt>Argument:</p>
<dd><i>arg</i> should point to a buffer of length ( <code>ISDN_MODEM_ANZREG</code> + <code>ISDN_MSNLEN</code> ) * <code>ISDN_MAX_CHANNELS</code>. filled with the values of all modem registers.</p>
<dt>Return:</p>
<dd>On return, the modem registers are set from the contents of the provided buffer.</dl>
</dl>
<dt><code>IIOCSETMAP</code></p>
<dd>Set Mapping table.</p>
<dl>
<dd>This call is used to set EAZ/MSN mapping of a lowlevel driver.</p>
<dl>
<dt>Argument:</p>
<dd><i>arg</i> should point to a <i>struct isdn_ioctl_struct</i> containing the necessary parameters.</p>
<dt>Return:</p>
<dd>On success, the mapping table is set from the given parameters an the call returns 0.</dl>
</dl>
<dt><code>IIOCGETMAP</code></p>
<dd>Get Mapping table.</p>
<dl>
<dd>This call is used to get EAZ/MSN mapping of a lowlevel driver.</p>
<dl>
<dt>Argument:</p>
<dd><i>arg</i> should point to a <i>struct isdn_ioctl_struct</i> containing the necessary parameters.</p>
<dt>Return:</p>
<dd>On success, the current mapping table of the given driver is returned and the call returns 0.</dl>
</dl>
<dt><code>IIOCDRVCTL</code></p>
<dd>Lowlevel driver ioctl.</p>
<dl>
<dd>This call is used for controlling various lowlevel drivers. The ioctl-code for this command is assembled by adding IIOCDRVCTL (128) and the desired driver ioctl-code. Therefore, a lowlevel driver can understand a maximum of 127 different ioctls.</p>
<dl>
<dt>Argument:</p>
<dd><i>arg</i> should point to a <i>struct isdn_ioctl_struct</i> containing the necessary parameters, especially the driver-Id must be filled correctly. The arg component inside isdn_ioctl_struct is handed down to the driver&#8217;s ioctl function. Its meaning is not defined here and depends on the lowlevel driver. See documentation for the various lowlevel drivers for information about driver- specific ioctl.</p>
<dt>Return:</p>
<dd>The return code depends on the driver&#8217;s ioctl function. Usually, 0 means no error.</dl>
</dl>
</dl>
<h2>Author</h2>
<p>Fritz Elfert &lt;fritz [at] isdn4linux.de&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/4-isdninfo/">isdninfo</a></code>(4), <code><a href="/docs/linux/man/4-icnctrl/">icnctrl</a></code>(4). </p>

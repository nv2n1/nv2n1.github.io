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
<p><i>/dev/isdnctrl</i> is a character device with major number <code>45</code> and minor numbers <code>64</code> to <code>127</code>. It allows controlling functionality of the Linux ISDN subsystem.</p>
<h2>Ioctl Functions</h2>
<p>Currently, the following ioctl calls are supported:</p>
<dl>
<dt><code>IIOCNETAIF</code></dt>
<dd>Add an ISDN network interface.</dd>
<dl>
<dd>This function adds a network interface to the kernel&#8217;s device table. This interface can be used just like normal eth interfaces.</dd>
<dl>
<dt>Argument:</dt>
<dd><i>arg</i> should point to a zero terminated string of max. 10 characters. if <i>arg</i> is NULL, the kernel assigns a name.</dd>
<dt>Return:</dt>
<dd>On success, the name of the new interface is copied to <i>arg</i>. and the call returns 0. On failure, an error code is returned.</dd></dl>
</dl>
<dt><code>IIOCNETASL</code></dt>
<dd>Create a slave interface.</dd>
<dl>
<dd>Creates a slave interface for RAW-device channel-bundling. These devices behave like network-interfaces, except they are invisible to user. Only ISDN parameters can be controlled, not IP-parameters. IP-parameters are inherited from the corresponding master-device.</dd>
<dl>
<dt>Argument:</dt>
<dd><i>arg</i> should point to a zero terminated string of max. 21 characters containing two comma-separated names. The first part is the name of an existing ISDN network device, which will be master. The second part will be the name of the new slave interface.</dd>
<dt>Return:</dt>
<dd>On success, the name of the new interface is copied to <i>arg</i>. and the call returns 0. On failure, an error code is returned.</dd></dl>
</dl>
<dt><code>IIOCNETDIF</code></dt>
<dd>Delete a network-interface.</dd>
<dl>
<dd>This call deletes an existing ISDN network interface.</dd>
<dl>
<dt>Argument:</dt>
<dd><i>arg</i> should point to a zero terminated string of max. 10 characters naming an existing interface which will be deleted. If the interface is a master interface, all its slave-interfaces will be deleted also.</dd>
<dt>Return:</dt>
<dd>On success, the call returns 0. On failure, an error code is returned.</dd></dl>
</dl>
<dt><code>IIOCNETSCF</code></dt>
<dd>Set configurable parameters of an ISDN network interface.</dd>
<dl>
<dd>This call replaces all ISDN related parameters of an interface by the parameters given.</dd>
<dl>
<dt>Argument:</dt>
<dd><i>arg</i> should point to a <i>struct isdn_net_ioctl_cfg</i> (defined in linux/isdn.h)</dd>
<dt>Return:</dt>
<dd>On success, the call returns 0. On failure, an error code is returned.</dd></dl>
</dl>
<dt><code>IIOCNETGCF</code></dt>
<dd>Get configurable parameters of an ISDN network interface.</dd>
<dl>
<dd>This call returns all ISDN related parameters of an interface.</dd>
<dl>
<dt>Argument:</dt>
<dd><i>arg</i> should point to a <i>struct isdn_net_ioctl_cfg</i> (defined in linux/isdn.h) which will be filled by the current setup.</dd>
<dt>Return:</dt>
<dd>On success, the call returns 0 and the interface-setup is copied to *arg. On failure, an error code is returned.</dd></dl>
</dl>
<dt><code>IIOCNETANM</code></dt>
<dd>Add a phone number to an ISDN network interface.</dd>
<dl>
<dd>This call adds a phone number to an existing network interface.</dd>
<dl>
<dt>Argument:</dt>
<dd><i>arg</i> should point to a <i>struct isdn_net_ioctl_phone</i> which contains necessary information.</dd>
<dt>Return:</dt>
<dd>On success, the call returns 0 and the phone number is added to either outgoing or incoming number list. On failure, an error code is returned.</dd></dl>
</dl>
<dt><code>IIOCNETDNM</code></dt>
<dd>Delete a phone number from an ISDN network interface.</dd>
<dl>
<dd>This call deletes a phone number from an existing network interface.</dd>
<dl>
<dt>Argument:</dt>
<dd><i>arg</i> should point to a <i>struct isdn_net_ioctl_phone</i> which contains necessary information.</dd>
<dt>Return:</dt>
<dd>On success, the call returns 0 and the phone number is deleted from either outgoing or incoming number list. On failure, an error code is returned.</dd></dl>
</dl>
<dt><code>IIOCNETGNM</code></dt>
<dd>Get list of phone numbers from an ISDN network interface.</dd>
<dl>
<dd>This call returns the list of phone numbers associated to an existing network interface.</dd>
<dl>
<dt>Argument:</dt>
<dd><i>arg</i> should point to a union of <i>struct isdn_net_ioctl_phone</i> and a buffer, large enough to hold a concatenated list of strings containing the phone numbers.</dd>
<dt>Return:</dt>
<dd>On success, the call returns 0 and the list of phone numbers is returned as a space-separated list of number-strings terminated by a NULL byte.</dd></dl>
</dl>
<dt><code>IIOCNETDIL</code></dt>
<dd>Trigger dialing of an ISDN network interface.</dd>
<dl>
<dd>This call initiates dialing of an ISDN network interface, if it is not connected. Normally, this ioctl is not needed, because ISDN network interface perform dial on demand by default.</dd>
<dl>
<dt>Argument:</dt>
<dd><i>arg</i> should point to a zero terminated string of max. 10 characters naming the desired interface.</dd>
<dt>Return:</dt>
<dd>On success, the call returns 0 and the interface starts dialing.</dd></dl>
</dl>
<dt><code>IIOCNETHUP</code></dt>
<dd>Hangup an ISDN network interface.</dd>
<dl>
<dd>This call initiates hangup of an ISDN network interface, if it is connected.</dd>
<dl>
<dt>Argument:</dt>
<dd><i>arg</i> should point to a zero terminated string of max. 10 characters naming the desired interface.</dd>
<dt>Return:</dt>
<dd>On success, the call returns 0 and the interface hangs up.</dd></dl>
</dl>
<dt><code>IIOCNETALN</code></dt>
<dd>Add a link of an MPP-configured ISDN network interface.</dd>
<dl>
<dd>This call initiates dialing of a Multilink-PPP slave ISDN network interface, if it is not connected.</dd>
<dl>
<dt>Argument:</dt>
<dd><i>arg</i> should point to a zero terminated string of max. 10 characters naming the desired interface.</dd>
<dt>Return:</dt>
<dd>On success, the call returns 0 and the interface starts dialing.</dd></dl>
</dl>
<dt><code>IIOCNETDLN</code></dt>
<dd>Hangup an MPP-configured ISDN network interface.</dd>
<dl>
<dd>This call initiates hangup of an Multilink-PPP ISDN network interface, if it is connected.</dd>
<dl>
<dt>Argument:</dt>
<dd><i>arg</i> should point to a zero terminated string of max. 10 characters naming the desired interface.</dd>
<dt>Return:</dt>
<dd>On success, the call returns 0 and the interface hangs up.</dd></dl>
</dl>
<dt><code>IIOCNETARU</code></dt>
<dd>Add a timeout rule to an ISDN network interface.</dd>
<dl>
<dd>This call adds a timeout rule to an existing interface.</dd>
<dl>
<dt>Argument:</dt>
<dd><i>arg</i> should point to a <i>struct isdn_ioctl_timeout_rule</i> containing the necessary parameters.</dd>
<dt>Return:</dt>
<dd>On success, the call returns 0 and the rule is added to the rule list of the interface.</dd></dl>
</dl>
<dt><code>IIOCNETDRU</code></dt>
<dd>Delete a timeout rule from an ISDN network interface.</dd>
<dl>
<dd>This call deletes a timeout rule from an existing interface.</dd>
<dl>
<dt>Argument:</dt>
<dd><i>arg</i> should point to a <i>struct isdn_ioctl_timeout_rule</i> containing the necessary parameters.</dd>
<dt>Return:</dt>
<dd>On success, the call returns 0 and the rule is deleted from the rule list of the interface.</dd></dl>
</dl>
<dt><code>IIOCNETGRU</code></dt>
<dd>Get a timeout rule from an ISDN network interface.</dd>
<dl>
<dd>This call returns a timeout rule from an existing interface.</dd>
<dl>
<dt>Argument:</dt>
<dd><i>arg</i> should point to a <i>struct isdn_ioctl_timeout_rule</i> containing the necessary parameters.</dd>
<dt>Return:</dt>
<dd>On success, the call returns 0 and the struct is filled from the rule list of the interface.</dd></dl>
</dl>
<dt><code>IIOCNETBUD</code></dt>
<dd>Handle budget accounting of an ISDN network interface.</dd>
<dl>
<dd>
</dd><dl>
<dt>Argument and Return:</dt>
<dd>to be defined.</dd></dl>
</dl>
<dt><code>IIOCSETVER</code></dt>
<dd>Set verbosity of link level.</dd>
<dl>
<dd>
</dd><dl>
<dt>Argument:</dt>
<dd><i>arg</i> is an integer, defining the new verbose value.</dd>
<dt>Return:</dt>
<dd>This call always returns 0.</dd></dl>
</dl>
<dt><code>IIOCSETGST</code></dt>
<dd>Set global stop flag of link level.</dd>
<dl>
<dd>
</dd><dl>
<dt>Argument:</dt>
<dd><i>arg</i> is an integer, defining the new stop flag value (0 or !0).</dd>
<dt>Return:</dt>
<dd>This call always returns 0.</dd></dl>
</dl>
<dt><code>IIOCSETBRJ</code></dt>
<dd>Set busreject flag of a lowlevel driver.</dd>
<dl>
<dd>
</dd><dl>
<dt>Argument:</dt>
<dd><i>arg</i> should point to an <i>struct isdn_ioctl_struct</i> containing the driver&#8217;s ID and the value of the busreject flag.</dd>
<dt>Return:</dt>
<dd>On success, the call returns 0 and the busreject flag of the selected driver is set according the given parameter.</dd></dl>
</dl>
<dt><code>IIOCSIGPRF</code></dt>
<dd>Enable signaling on change of modem profiles.</dd>
<dl>
<dd>With this call, the calling process is registered to receive a SIGIO on every change of any register of any ttyI. Thus it can read register settings and save them to a file. The calling process has to keep the device open in order to receive notifications. As soon as it closes the device, registration is deleted.</dd>
<dl>
<dt>Argument:</dt>
<dd>none</dd>
<dt>Return:</dt>
<dd>This call always returns 0.</dd></dl>
</dl>
<dt><code>IIOCGETPRF</code></dt>
<dd>Get all modem register settings.</dd>
<dl>
<dd>With this call, all modem registers of all ttyI devices can be read.</dd>
<dl>
<dt>Argument:</dt>
<dd><i>arg</i> should point to a buffer of length ( <code>ISDN_MODEM_ANZREG</code> + <code>ISDN_MSNLEN</code> ) * <code>ISDN_MAX_CHANNELS</code>.</dd>
<dt>Return:</dt>
<dd>On return, the provided buffer is filled with the register values.</dd></dl>
</dl>
<dt><code>IIOCSETPRF</code></dt>
<dd>Set all modem register settings.</dd>
<dl>
<dd>With this call, all modem registers of all ttyI devices can be written.</dd>
<dl>
<dt>Argument:</dt>
<dd><i>arg</i> should point to a buffer of length ( <code>ISDN_MODEM_ANZREG</code> + <code>ISDN_MSNLEN</code> ) * <code>ISDN_MAX_CHANNELS</code>. filled with the values of all modem registers.</dd>
<dt>Return:</dt>
<dd>On return, the modem registers are set from the contents of the provided buffer.</dd></dl>
</dl>
<dt><code>IIOCSETMAP</code></dt>
<dd>Set Mapping table.</dd>
<dl>
<dd>This call is used to set EAZ/MSN mapping of a lowlevel driver.</dd>
<dl>
<dt>Argument:</dt>
<dd><i>arg</i> should point to a <i>struct isdn_ioctl_struct</i> containing the necessary parameters.</dd>
<dt>Return:</dt>
<dd>On success, the mapping table is set from the given parameters an the call returns 0.</dd></dl>
</dl>
<dt><code>IIOCGETMAP</code></dt>
<dd>Get Mapping table.</dd>
<dl>
<dd>This call is used to get EAZ/MSN mapping of a lowlevel driver.</dd>
<dl>
<dt>Argument:</dt>
<dd><i>arg</i> should point to a <i>struct isdn_ioctl_struct</i> containing the necessary parameters.</dd>
<dt>Return:</dt>
<dd>On success, the current mapping table of the given driver is returned and the call returns 0.</dd></dl>
</dl>
<dt><code>IIOCDRVCTL</code></dt>
<dd>Lowlevel driver ioctl.</dd>
<dl>
<dd>This call is used for controlling various lowlevel drivers. The ioctl-code for this command is assembled by adding IIOCDRVCTL (128) and the desired driver ioctl-code. Therefore, a lowlevel driver can understand a maximum of 127 different ioctls.</dd>
<dl>
<dt>Argument:</dt>
<dd><i>arg</i> should point to a <i>struct isdn_ioctl_struct</i> containing the necessary parameters, especially the driver-Id must be filled correctly. The arg component inside isdn_ioctl_struct is handed down to the driver&#8217;s ioctl function. Its meaning is not defined here and depends on the lowlevel driver. See documentation for the various lowlevel drivers for information about driver- specific ioctl.</dd>
<dt>Return:</dt>
<dd>The return code depends on the driver&#8217;s ioctl function. Usually, 0 means no error.</dd></dl>
</dl>
</dl>
<h2>Author</h2>
<p>Fritz Elfert &lt;fritz [at] isdn4linux.de&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/4-isdninfo/">isdninfo</a></code>(4), <code>icnctrl</code>(4). </p>

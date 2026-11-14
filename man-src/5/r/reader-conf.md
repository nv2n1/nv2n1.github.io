---
title: "reader-conf(5)"
name: "reader-conf"
section: "5"
letter: "r"
url: "/docs/linux/man/5-reader-conf/"
description: "reader.conf – configuration file for pcscd readers’ drivers"
---

<p>reader.conf &#8211; configuration file for pcscd readers&#8217; drivers</p>
<h2>Description</h2>
<p>The <i>/etc/reader.conf.d/reader.conf</i> file contains configuration information for serial and (some) PCMCIA smart card readers. </p>
<p> USB readers SHALL NOT be configured using this file. <code>pcscd</code> uses another mechanism to automatically load USB drivers.</p>
<h2>Syntax</h2>
<p>The <i>/etc/reader.conf.d/reader.conf</i> is a regular text file. Each reader must be defined by four fields: </p>
<p>&nbsp;<wbr>FRIENDLYNAME&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TEXT_STRING<br />
&nbsp;<wbr>DEVICENAME&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>FILENAME<br />
&nbsp;<wbr>LIBPATH&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>FILENAME<br />
&nbsp;<wbr>CHANNELID&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>NUMBER </p>
<p> The &quot;FRIENDLYNAME&quot; field is an arbitrary text used to identify the reader. This text is displayed by commands like <code><a href="/docs/linux/man/1-pcsc_scan/">pcsc_scan</a></code>(1) that prints the names of all the connected and detected readers. </p>
<p> The &quot;DEVICENAME&quot; field was not used for old drivers (using the IFD handler version 2.0 or earlier). It is now (IFD handler version 3.0) used to identify the physical port on which the reader is connected. This is the device name of this port. It is dependent of the OS kernel. The first serial port device is called <i>/dev/ttyS0</i> under Linux and <i>/dev/cuaa0</i> under FreeBSD. </p>
<p> The &quot;LIBPATH&quot; field is the filename of the driver code. The driver is a dynamically loaded piece of code (generally a <i>drivername.so*</i>file). </p>
<p> The &quot;CHANNELID&quot; is no more used for recent drivers (IFD handler 3.0) and has been superseded by &quot;DEVICENAME&quot;. If you have an old driver this field is used to indicate the port to use. You should read your driver documentation to know what information is needed here. It should be the serial port number for a serial reader.</p>
<h2>Example</h2>
<p>&nbsp;<wbr>#&nbsp;<wbr>Gemplus GemPCTwin reader with serial communication<br />
&nbsp;<wbr>#&nbsp;<wbr>connected to the first serial port<br />
&nbsp;<wbr>FRIENDLYNAME&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&quot;GemPCTwin serial&quot;<br />
&nbsp;<wbr>DEVICENAME&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>/dev/ttyS0<br />
&nbsp;<wbr>LIBPATH&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>/usr/lib64/pcsc/drivers/serial/libccidtwin.so.0.4.1<br />
&nbsp;<wbr>CHANNELID&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1</p>
<h2>Debugging</h2>
<p>In order to set up your <i>/etc/reader.conf.d/reader.conf</i> file correctly you may want to have debug messages from <code>pcscd</code>. I recommend you to start <code>pscsd</code> in the foreground and debug mode using:<br />
&nbsp;<wbr>#&nbsp;<wbr>pcscd &#8211;foreground &#8211;debug </p>
<p> If everything seems OK you can use the <code>pcsc_scan</code> command to print the list of correctly detected readers and try to get the ATR of your smart cards.</p>
<h2>Author</h2>
<p>Ludovic Rousseau &lt;ludovic.rousseau [at] free.fr&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-pcscd/">pcscd</a></code>(8), <code><a href="/docs/linux/man/1-pcsc_scan/">pcsc_scan</a></code>(1) </p>

---
title: "gammurc(5)"
name: "gammurc"
section: "5"
letter: "g"
url: "/docs/linux/man/5-gammurc/"
description: "gammurc – gammu(1) configuration file"
---

<p>gammurc &#8211; <a href="/docs/linux/man/1-gammu/">gammu</a>(1) configuration file </p>
<h2>Synopsis</h2>
<p><i>/etc/gammurc</i> or <i>~/.gammurc</i></p>
<h2>Description</h2>
<p><a href="/docs/linux/man/1-gammu/">gammu</a>(1) reads configuration from a config file. It&#8217;s location is determined on runtime. On Unix systems, it first tries ~/.gammurc and then falls back to /etc/gammurc. On Windows, user configuration is tried at profile/Application Data/gammurc and then gammu falls back to current directory (./gammurc). This file use ini file syntax, with comments being marked with both ; and #. Sections of config file are identified in square brackets line [this]. All key values are case insensitive. Configuration file for gammu can contain several sections &#8211; [gammu], [gammu1], [gammuN], &#8230; Each section configures one connection setup and in default mode gammu tries all of them in numerical order. You can also specify which configuration section to use by giving it&#8217;s number ([gammu] has number 0) as a parameter to <a href="/docs/linux/man/1-gammu/">gammu</a>(1) and it will then use only this section.</p>
<dl>
<dt><code>Connection</code></p>
<dd>Protocol which will be used to talk to your phone. For Nokia cables you want to use one of following: <code>fbus</code> &#8211; serial FBUS connection<br />
 <code>fbususb</code> &#8211; FBUS over USB cable (experimental, for Nokia cables on Linux, including DKU-2)<br />
 <code>dlr3</code> &#8211; DLR-3 and compatible cables<br />
 <code>dku2</code> &#8211; DKU-2 and compatible cables<br />
 <code>dku5</code> &#8211; DKU-5 and compatible cables<br />
 <code>mbus</code> &#8211; serial MBUS connection If you use some non original cable, you might need to append -nodtr (eg. for ARK3116 based cables) or -nopower, but Gammu should be able to detect this automatically. For non-Nokia phones connected using cable you generally want: <code>at</code> &#8211; generic AT commands based connection You can optionally specify speed of the connection, eg. at19200, but it is not needed for modern USB cables. For IrDA connections use one of following: <code>irdaphonet</code> &#8211; Phonet connection for Nokia phones.<br />
 <code>irdaat</code> &#8211; AT commands connection for most of phones (this is not supported on Linux).<br />
 <code>irdaobex</code> &#8211; OBEX (IrMC or file transfer) connection for most of phones.<br />
 <code>irdagnapbus</code> &#8211; GNapplet based connection for Symbian phones For Bluetooth connection use one of following: <code>bluephonet</code> &#8211; Phonet connection for Nokia phones.<br />
 <code>blueat</code> &#8211; AT commands connection for most of phones.<br />
 <code>blueobex</code> &#8211; OBEX (IrMC or file transfer) connection for most of phones.<br />
 <code>bluerfgnapbus</code> &#8211; GNapplet based connection for Symbian phones</p>
<dt><code>Port</code></p>
<dd>Device node or address of phone. It depends on used connection. For cables or emulated serial ports, you enter device name (for example /dev/ttyS0, /dev/ttyACM0, /dev/ircomm0, /dev/rfcomm0 on Linux, /dev/cuad0 on FreeBSD or COM1: on Windows). The special exception are DKU-2 and DKU-5 cables on Windows, where the device is automatically detected from driver information and this parameters is ignored. For Bluetooth connection you have to enter Bluetooth address of your phone (you can list Bluetooth devices in range on Linux using &quot;hcitool scan&quot; command). Optionally you can also force Gammu to use specified channel by includig channel number after slash. Before using Gammu, your device should be paired with computer or you should have set up automatic pairing. For IrDA connections, this parameters is not used at all. If IrDA does not work on Linux, you might need to bring up the interface and enable discovery (you need to run these commands as root): </p>
<dt><code>Model</code></p>
<dd>Do not use this parameter unless really needed! The only use case for this is when Gammu does not know your phone and misdetects it&#8217;s features. The only special case for using model is to force special type of OBEX connection instead of letting Gammu try the best suited for selected operation: <code>obexfs</code> &#8211; force using of file browsing service (file system support)<br />
 <code>obexirmc</code> &#8211; force using of IrMC service (contacts, calendar and notes support)<br />
 <code>obexnone</code> &#8211; none service chosen, this has only limited use for sending file (<code>sendfile</code> command)</p>
<dt><code>SynchronizeTime</code></p>
<dd>If you want to set time from computer to phone during starting connection.</p>
<dt><code>StartInfo</code></p>
<dd>This option allow to set, that you want (setting &quot;yes&quot;) to see message on the phone screen or phone should enable light for a moment during starting connection. Phone will not beep during starting connection with this option. This works only with some Nokia phones.</p>
<dt><code>GammuCoding</code></p>
<dd>Forces using specified codepage (for example &quot;1250&quot; will force CP-1250 or &quot;utf8&quot; for UTF-8). This should not be needed in most cases, Gammu should detect it according to your locales.</p>
<dt><code>GammuLoc</code></p>
<dd>Path to directory with localisation files (the directory should contain LANG/LC_MESSAGES/gammu.mo). If gammu is properly installed it should find these files automatically.</p>
<dt><code>LogFile</code></p>
<dd>Path to file where information about communication will be stored.</p>
<dt><code>LogFormat</code></p>
<dd>Determines what all will be logged to LogFile. Possible values are: <code>nothing</code> &#8211; no debug level<br />
 <code>text</code> &#8211; transmission dump in text format<br />
 <code>textall</code> &#8211; all possible info in text format<br />
 <code>textalldate</code> &#8211; all possible info in text format, with time stamp<br />
 <code>errors</code> &#8211; errors in text format<br />
 <code>errorsdate</code> &#8211; errors in text format, with time stamp<br />
 <code>binary</code> &#8211; transmission dump in binary format For debugging use either <code>textalldate</code> or <code>textall</code>, it contains all needed information to diagnose problems.</p>
<dt><code>Features</code></p>
<dd>Custom features for phone. This can be used as override when values coded in common/gsmphones.c are bad or missing. Consult include/gammu-info.h for possible values (all GSM_Feature values without leading F_ prefix). Please report correct values to Gammu authors.</p>
<dt><code>Use_Locking</code></p>
<dd>On Posix systems, you might want to lock serial device when it is being used using UUCP-style lock files. Enabling this option (setting to yes) will make Gammu honor these locks and create it on startup. On most distributions you need additional privileges to use locking (eg. you need to be member of uucp group). This option has no meaning on Windows. </p>
<h2>Example</h2>
<p>There is more complete example available in Gammu documentation. Gammu configuration for Nokia phone using DLR-3 cable:  </p>
<pre>[gammu]
port = /dev/ttyACM0
connection = dlr3</pre>
<p> Gammu configuration for Sony-Ericsson phone (or any other AT compatible phone) connected using USB cable:  </p>
<pre>[gammu]
port = /dev/ttyACM0
connection = at</pre>
<p> Gammu configuration for Sony-Ericsson (or any other AT compatible phone) connected using bluetooth:  </p>
<pre>[gammu]
port = B0:0B:00:00:FA:CE
connection = blueat</pre>
<p> Gammu configuration for phone which needs to manually adjust Bluetooth channel to use channel 42:  </p>
<pre>[gammu]
port = B0:0B:00:00:FA:CE/42
connection = blueat</pre>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-gammu-smsd/">gammu-smsd</a>(1), <a href="/docs/linux/man/1-gammu/">gammu</a>(1), <a href="/docs/linux/man/5-gammurc/">gammurc</a>(5)</p>
<h2>Author</h2>
<p>gammu-smsd and this manual page were written by Michal Cihar &lt;michal [at] cihar.com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2009 Michal Cihar and other authors. License GPLv2: GNU GPL version 2 &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">http://www.gnu.org/licenses/old-licenses/gpl-2.0.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>Reporting Bugs</h2>
<p>Please report bugs to &lt;<a rel="nofollow" href="http://bugs.cihar.com">http://bugs.cihar.com</a>&gt;.</p>

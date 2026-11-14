---
title: "obexftp(1)"
name: "obexftp"
section: "1"
letter: "o"
url: "/docs/linux/man/1-obexftp/"
description: "obexftp – Mobile Equipment file transfer tool"
---

<h2>NAME</h2>
<p> obexftp &#8211; Mobile Equipment file transfer tool</p>
<h2>SYNOPSIS</h2>
<p> <code>obexftp</code> [<i>OPTION</i>] [<i>COMMANDS</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>obexftp</code> is used to access files on mobile equipment, i.e. cell phones. With <code>obexftpd</code> you can transfer files between any computers using <code>IrDA</code>, <code>Bluetooth</code> and <code>TCP/IP</code>. </p>
<p> This tool lets you access the <code>ObexFTP</code> library by the means of a command line interface. You might consider using the other means available. E.g. the <code>ObexFS</code> filesystem for Linux.</p>
<h2>OPTIONS</h2>
<p> The ordering of options is important. Every command will use the most recent device set. Every file without command switch will apply to the command given most recent. See <code>EXAMPLES</code></p>
<h3>TRANSPORT OPTIONS</h3>
<dl>
<dt><code>-i</code>, <code>&#8211;irda</code></p>
<dd> Connect using the IrDA protocol. This is the default.</p>
<dt><code>-b</code> <i>device</i>, <code>&#8211;bluetooth</code> <i>device</i></p>
<dd> Connect to this bluetooth device. If the device is not given the first device found will be used.</p>
<dt><code>-B</code> <i>number</i>, <code>&#8211;channel</code> <i>number</i></p>
<dd> Use this bluetooth channel when connecting. The channel will be discoverd automatically if this option is not used.</p>
<dt><code>-d</code> <i>no/address</i>, <code>&#8211;hci</code> <i>no/address</i></p>
<dd> Use the bluetooth device referenced by number or address as source device for the connection.</p>
<dt><code>-u</code> <i>intf no</i>, <code>&#8211;usb</code> <i>intf no</i></p>
<dd> Connect to this usb interface or list all available usb interfaces.</p>
<dt><code>-t</code> <i>device</i>, <code>&#8211;tty</code> <i>device</i></p>
<dd> Connect to this tty device.</p>
<dt><code>-n</code> <i>host</i>, <code>&#8211;network</code> <i>host</i></p>
<dd> Connect to this network host.</dl>
<h3>COMPATIBILITY OPTIONS</h3>
<dl>
<dt><code>-U</code> <i>uuid</i>, <code>&#8211;uuid</code> <i>uuid</i></p>
<dd> Select the UUID to connect with. Recognized values are currently &quot;none&quot; needed by some Nokia mobile devices, &quot;FBS&quot; (default) for the normal file browsing service, &quot;IRMC&quot; for IRMC synchronisation and &quot;S45&quot; when connecting to a Siemens Mobile phone via cable or &quot;SHARP&quot; for PCSOFTWARE UUID with Sharp devices.</p>
<dt><code>-H</code>, <code>&#8211;noconn</code></p>
<dd> Suppress connection IDs (i.e. send no connection header to the mobile).</p>
<dt><code>-S</code>, <code>&#8211;nopath</code></p>
<dd> Don&#8217;t use &quot;setpath&quot; commands (i.e. send the whole path as filename to the mobile). Can be used together with <code>&#8211;noconn</code> and <code>&#8211;uuid none</code> to send an OBEX-PUSH.</dl>
<h3>SETTING THE FILE PATH</h3>
<dl>
<dt><code>-c</code> <i>folder</i>, <code>&#8211;chdir</code> <i>folder</i></p>
<dd> Set the mobiles current working directory.</p>
<dt><code>-C</code> <i>folder</i>, <code>&#8211;mkdir</code> <i>folder</i></p>
<dd> Set the mobiles current working directory. The folder will be created if it doesn&#8217;t exist.</p>
<dt><code>-l</code> <i>folder</i>, <code>&#8211;list</code> <i>folder</i></p>
<dd> List a folder.</dl>
<h3>SENDING AND RETRIEVING FILES</h3>
<dl>
<dt><code>-o</code> <i>path</i>, <code>&#8211;output</code> <i>path</i></p>
<dd> Specify the target file name, overriding the implicit local name from <code>&#8211;get</code> or the implicit remote name from <code>&#8211;put</code></p>
<dt><code>-g</code> <i>source</i>, <code>&#8211;get</code> <i>source</i></p>
<dd> Retrieve files from mobile.</p>
<dt><code>-G</code> <i>source</i>, <code>&#8211;getdelete</code> <i>source</i></p>
<dd> Retrieve files from mobile and delete them on the mobile</p>
<dt><code>-p</code> <i>source</i>, <code>&#8211;put</code> <i>source</i></p>
<dd> Send files to the mobile.</p>
<dt><code>-k</code> <i>source</i>, <code>&#8211;delete</code> <i>source</i></p>
<dd> Delete files from the mobile.</dl>
<h3>EXPERIMENTAL EXTRAS</h3>
<dl>
<dt><code>-X</code>, <code>&#8211;capability</code></p>
<dd> Retrieve the capability object from the mobile (if available).</p>
<dt><code>-Y</code>, <code>&#8211;probe</code></p>
<dd> Probe and report device characteristics</p>
<dt><code>-x</code>, <code>&#8211;info</code></p>
<dd> Retrieve misc infos from mobile. I.e. memory size and free memory. Siemens specific for now.</p>
<dt><code>-m</code> <i>src</i> <i>dest</i>, <code>&#8211;move</code> <i>src</i> <i>dest</i></p>
<dd> Move (rename) files on the mobile. Siemens specific for now.</dl>
<h3>VERSION INFORMATION AND HELP</h3>
<dl>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Be verbose and give some additional infos.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print version string and exit.</p>
<dt><code>-h</code>, <code>&#8211;help</code>, <code>&#8211;usage</code></p>
<dd> Print short usage instructions.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>To get the directory listing from the first irda device</p>
<dd> <code>obexftp -i -l</code> or just <code>obexftp -l</code> as IrDA is the default.</p>
<dt>To get the file bar from directory foo from the first bluetooth device</p>
<dd> <code>obexftp -b -c foo -g bar</code></p>
<dt>To send the file bar to directory foo with device on first serial port</p>
<dd> <code>obexftp -t /dev/ttyS0 -c foo -p bar</code></p>
<dt>It is possible to use RfComm (serial port over bluetooth)</p>
<dd> <code>obexftp -t /dev/rfcomm0 -c foo -p bar</code></p>
<dt>And also IrComm (serial port over IrDA)</p>
<dd> <code>obexftp -t /dev/ircomm0 -c foo -p bar</code></p>
<dt>To send the file bar using plain OBEX PUSH</p>
<dd> <code>obexftp &#8211;bluetooth &#8211;nopath &#8211;noconn &#8211;uuid none &#8211;put bar</code></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-obexftpd/">obexftpd</a>(1), <a href="/docs/linux/man/3-openobex/">openobex</a>(3), <a href="/docs/linux/man/3-obexftp/">obexftp</a>(3), <a href="/docs/linux/man/3-multicobex/">multicobex</a>(3), <a href="/docs/linux/man/3-libbfb/">libbfb</a>(3).</p>
<h2>BUGS</h2>
<p> Bugs ? Features !</p>
<h2>NOTES</h2>
<p> The software has been tested and reported working on at least Siemens, Ericsson, and Nokia phones.</p>
<h2>AUTHOR</h2>
<p> Christian W. Zuckschwerdt &lt;zany [at] triq.net&gt; </p>
<h2>Index</h2>

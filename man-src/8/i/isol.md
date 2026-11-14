---
title: "isol(8)"
name: "isol"
section: "8"
letter: "i"
url: "/docs/linux/man/8-isol/"
description: "ipmiutil_sol – an IPMI Serial-Over-LAN Console application"
---

<p>ipmiutil_sol &#8211; an IPMI Serial-Over-LAN Console application </p>
<h2>Synopsis</h2>
<p><code>ipmiutil sol [-acdeilorsvwxz -NUPREFJTVY]</code> </p>
<h2>Description</h2>
<p>This utility starts an IPMI Serial-Over-LAN console session. A Serial-over-LAN console allows the client to see and modify functions before the OS boots, such as BIOS setup, grub, etc. This utility uses either the IPMI LAN 1.5 or 2.0 SOL interface. The 1.5 SOL interface is specific to Intel BMCs, while any IPMI 2.0 BMC should support 2.0 SOL. The target system/node must first have these parameters configured before SOL sessions can be started:<br />
 &#8211; [BIOS] serial console redirection parameters,<br />
 &#8211; [IPMI] lan and SOL parameters (see ipmiutil lan or ilan), and<br />
 &#8211; [OS] For Linux, edit grub.conf, inittab, and securetty parameters.<br />
 Be sure that the baud rate matches in all of the above places. See the ipmiutil UserGuide section 4.8 for details. </p>
<h2>Options</h2>
<dl>
<dt>-a</p>
<dd>Activate the SOL Console session, and enter console mode. Use the escape sequence (&#8216;~.&#8217;) to exit the session.</p>
<dt>-c &#8216;^&#8217;</p>
<dd>Set the escape Character to &#8216;^&#8217;, or another ANSI character. This changes the default two-character escape sequence (&#8216;~.&#8217;) to the specified single escape character, which will end the SOL session.</p>
<dt>-d</p>
<dd>Deactivate the SOL Console session. Use this if the previous session was aborted abnormally and starting a new session gives an error.</p>
<dt>-e</p>
<dd>Turn Encryption off in negotiation when activating a session. By default, encryption is on for Serial-Over-LAN console sessions.</p>
<dt>-l</p>
<dd>Use Legacy BIOS mapping for Enter key (CR+LF) instead of just LF. This is needed for BIOS Setup menus and DOS, but causes an extra LF to occur in Linux. So, only use this option if doing BIOS or DOS changes. This should be seldom be needed since now the default is to automatically detect these menus with colored backgrounds and change the mapping.</p>
<dt>-i input_file</p>
<dd>Use this file as an input script. The input_file will be read after the session is established. This can be used to automate certain tasks. The input_file is read one line at a time. If the input_file does not have an escape character (~) to end the session, then the input is returned to the keyboard when the file ends.</p>
<dt>-o output_file</p>
<dd>Use a Trace log. The output_file is created and all SOL screen output is written to the file, including VT100 escape sequences. If the output_file exists, the output is appended to it. This can be used to log what the user has done in an SOL session.</p>
<dt>-p</p>
<dd>Port to use. Defaults to RMCP port 623.</p>
<dt>-r</p>
<dd>Use Raw terminal I/O instead of custom VT100 to ANSI translation (in Windows). Use this option if the server is configured in BIOS and BMC for ANSI and the utility is being invoked from Windows.</p>
<dt>-s NNN</p>
<dd>For a slow link with high latency, this adds a delay of NNN microseconds between sending and receiving SOL packets. The default is 100 microseconds.</p>
<dt>-w</p>
<dd>(Windows only) Do not use the Windows Console buffer, but use Windows stdio instead. This does not handle cursor positioning correctly in some cases, however.</p>
<dt>-v log_file</p>
<dd>Causes debug messages to be displayed to the specified debug log_file. The default log_file is isoldbg.log in the current directory.</p>
<dt>-x</p>
<dd>Causes debug messages to be displayed to the debug log file.</p>
<dt>-z</p>
<dd>Causes more verbose debug messages to be displayed to the debug log file.</p>
<dt>-N nodename</p>
<dd>Nodename or IP address of the remote target system. If a nodename is specified, IPMI LAN interface is used. Otherwise the local system management interface is used.</p>
<dt>-U rmt_user</p>
<dd>Remote username for the nodename given. The default is a null username.</p>
<dt>-P/-R rmt_pswd</p>
<dd>Remote password for the nodename given. The default is a null password.</p>
<dt>-E</p>
<dd>Use the remote password from Environment variable IPMI_PASSWORD.</p>
<dt>-F drv_t</p>
<dd>Force the driver type to one of the followng: imb, va, open, gnu, landesk, lan, lan2, lan2i, kcs, smb. Note that lan2i means lan2 with intelplus. The default is to detect any supported driver type and use it.</p>
<dt>-J</p>
<dd>Use the specified LanPlus cipher suite (0 thru 17): 0=none/none/none, 1=sha1/none/none, 2=sha1/sha1/none, 3=sha1/sha1/cbc128, 4=sha1/sha1/xrc4_128, 5=sha1/sha1/xrc4_40, 6=md5/none/none, &#8230; 14=md5/md5/xrc4_40. Default is 3.</p>
<dt>-T</p>
<dd>Use a specified IPMI LAN Authentication Type: 0=None, 1=MD2, 2=MD5, 4=Straight Password, 5=OEM.</p>
<dt>-V</p>
<dd>Use a specified IPMI LAN privilege level. 1=Callback level, 2=User level, 3=Operator level, 4=Administrator level (default), 5=OEM level.</p>
<dt>-Y</p>
<dd>Yes, do prompt the user for the IPMI LAN remote password. Alternatives for the password are -E or -P. </p>
</dl>
<h2>Examples</h2>
<p>ipmiutil sol -a -N nodename -U username -P password<br />
 Starts an SOL console session to the nodename. Detect the lan protocol. ipmiutil sol -a -N nodename -U username -P password -Flan2<br />
 Starts an SOL console session to the nodename. Force lan protocol to 2.0. </p>
<h2>Platform Serial Port Configuration Examples</h2>
<p>First, enter BIOS Setup for Serial Console Redirection parameters: (these vary by platform) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Console Redirection&nbsp;<wbr>=&nbsp;<wbr>Serial Port B </p>
<p>&nbsp;<wbr>&nbsp;<wbr>ACPI Redirection&nbsp;<wbr>=&nbsp;<wbr>Disabled </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Baud Rate&nbsp;<wbr>=&nbsp;<wbr>115.2K </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Flow Control&nbsp;<wbr>=&nbsp;<wbr>CTS/RTS </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Terminal Type&nbsp;<wbr>=&nbsp;<wbr>VT100 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Legacy Redirection&nbsp;<wbr>=&nbsp;<wbr>Enabled<br />
 Note that the Baud Rate can vary, but it must match in all locations where it is used (BIOS, IPMI, and Linux).<br />
 For some non-Intel platforms, the serial console would be COM1 instead of COM2, but should be enabled in BIOS.<br />
 From Linux, run &quot;ipmiutil serial -c&quot; for Terminal Mode shared configuration.<br />
 Or, on older Intel TSRLT2 platforms: From Linux, run &quot;ipmiutil serial -s&quot; for Basic Mode Shared configuration.</p>
<h2>Linux Configuration For Serial Console</h2>
<p>If using lilo, in /etc/lilo.conf, add </p>
<p>&nbsp;<wbr>&nbsp;<wbr>append=&quot;console=ttyS1,19200n8 console=tty0&quot;<br />
 (and comment out the &quot;message=&quot; line because it includes graphics)<br />
 Note that the append line can be placed in the global section and removed from each kernel section if there are no other differences. </p>
<p> Or, if using grub, edit /boot/grub/grub.conf as follows: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#Omit the splashimage or gfxmenu </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>splashimage=(hd0,0)/grub/splash.xpm.gz </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#The serial and terminal lines are not usually needed </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>serial &#8211;unit=1 &#8211;speed=19200 &#8211;word=8 &#8211;parity=no &#8211;stop=1 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>terminal &#8211;timeout=10 serial console </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#Add the console=ttyS*&nbsp;<wbr>parameter to the kernel line </p>
<p>&nbsp;<wbr>kernel&nbsp;<wbr>(hd0,0)&nbsp;<wbr>/vmlinuz root=/dev/sda2 console=ttyS1,19200n8 </p>
<p> Add this line to /etc/initab, if ttyS1 is not already there: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>co:2345:respawn:/sbin/agetty ttyS1 19200 vt100 </p>
<p> Add this line to /etc/securetty, if ttyS1 is not already there: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>ttyS1</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ipmiutil/">ipmiutil</a>(8) <a href="/docs/linux/man/8-ialarms/">ialarms</a>(8) <a href="/docs/linux/man/8-iconfig/">iconfig</a>(8) <a href="/docs/linux/man/8-icmd/">icmd</a>(8) <a href="/docs/linux/man/8-idiscover/">idiscover</a>(8) <a href="/docs/linux/man/8-ievents/">ievents</a>(8) <a href="/docs/linux/man/8-ifru/">ifru</a>(8) <a href="/docs/linux/man/8-igetevent/">igetevent</a>(8) <a href="/docs/linux/man/8-ihealth/">ihealth</a>(8) <a href="/docs/linux/man/8-ilan/">ilan</a>(8) <a href="/docs/linux/man/8-ireset/">ireset</a>(8) <a href="/docs/linux/man/8-isel/">isel</a>(8) <a href="/docs/linux/man/8-isensor/">isensor</a>(8) <a href="/docs/linux/man/8-iserial/">iserial</a>(8) <a href="/docs/linux/man/8-iwdt/">iwdt</a>(8) </p>
<h2>Warnings</h2>
<p>See <a rel="nofollow" href="http://ipmiutil.sourceforge.net/">http://ipmiutil.sourceforge.net/</a> for the latest version of ipmiutil and any bug fix list.</p>
<h2>Copyright</h2>
<p>Copyright (C) 2009 Kontron America, Inc. </p>
<p> See the file COPYING in the distribution for more details regarding redistribution. </p>
<p> This utility is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY.</p>
<h2>Author</h2>
<p>Andy Cress &lt;arcress at users.sourceforge.net&gt;</p>

---
title: "iserial(8)"
name: "iserial"
section: "8"
letter: "i"
url: "/docs/linux/man/8-iserial/"
description: "ipmiutil_serial – configure a system for Serial/EMP management functions, such as Terminal Mode, and optionally share the port with the Serial Console."
---

<p>ipmiutil_serial &#8211; configure a system for Serial/EMP management functions, such as Terminal Mode, and optionally share the port with the Serial Console.</p>
<h2>Synopsis</h2>
<p><code>ipmiutil serial [-bcdeflq#rsvxB -m0 -m1 -n ser_chan -u user -p passwd -NUPREFJTVY]</code> </p>
<h2>Description</h2>
<p><i>ipmiutil serial</i> is a program that uses an IPMI driver to send IPMI commands which configure a system to enable EMP/serial Terminal Mode management functions within the firmware, so that an administrator can use command-line character commands via the serial port to power cycle the system and perform other functions, even if the system is not running an OS. This level of access needs to be protected by a username/password login, which can be specified with this utility. This utility can use either the /dev/ipmi0 driver from OpenIPMI, the /dev/imb driver from Intel, the /dev/ipmikcs driver from valinux, direct user-space IOs, or the IPMI LAN interface if -N. </p>
<h2>Options</h2>
<p>Command line options are described below.</p>
<dl>
<dt>-b</p>
<dd>Set up and enable the Serial Port EMP parameters for Basic Mode management functions. This does not set a username or password.</p>
<dt>-c</p>
<dd>Configure and enable the Serial Port EMP parameters for Terminal Mode management functions, shared with BIOS Console Redirection. Setting a new username and password for serial access via -u and -p is recommended for security.</p>
<dt>-d</p>
<dd>Disable the serial port access for IPMI commands. The serial port is then only available for BIOS console and OS functions. A side-effect of this option is that it sets the default user (1) back to admin access.</p>
<dt>-e</p>
<dd>Enable EMP Terminal Mode without shared BIOS console. The serial port is then only available for EMP Terminal Mode functions.</p>
<dt>-f</p>
<dd>Specifies the Flow Control for the Serial EMP. 0 means no flow control, and 1 means RTS/CTS flow control (default). This must match the BIOS Serial Console setting.</p>
<dt>-l</p>
<dd>Show LAN Parameters. This option reads and displays the LAN Parameter configuration also.</p>
<dt>-m0</p>
<dd>Switch the Serial Port MUX to Baseboard/BIOS Console operation. Set no other configuration parameters.</p>
<dt>-m1</p>
<dd>Switch the Serial Port MUX to Terminal Mode management. Set no other configuration parameters.</p>
<dt>-n ser_chan</p>
<dd>Sets the IPMI channel number to use for the EMP serial channel (often 4). Note that the IPMI channels for LAN, Serial, etc. are numbered differently on each platform type. The default is to detect the first available IPMI serial channel.</p>
<dt>-#</p>
<dd>Same as -q below.</p>
<dt>-q</p>
<dd>Specify an alternate user number for the EMP Username from the -u option. This is normally user number 2, 3, or 4, where 3 is the default. The maximum number of users is 15.</p>
<dt>-r</p>
<dd>Read Only. This option just reads the Serial Parameter configuration without writing any values.</p>
<dt>-s</p>
<dd>Set up and enable the Serial Port EMP parameters for Shared operation between Basic Mode management functions and Baseboard (BIOS) Remote Console. This option switches the Serial Port MUX to Baseboard Console operation.</p>
<dt>-t</p>
<dd>Configure and enable the Serial Port EMP parameters for Terminal Mode management functions, shared with BIOS Console Redirection. Same as -c, but easier to remember.</p>
<dt>-u username</p>
<dd>This specifies a username for the EMP Terminal Mode login. It can be any string, up to 15 characters. If -u is not used, the default user 1 (null) will be assumed. The username, if specified, will be set for user 3, unless option -q is specified.</p>
<dt>-p password</p>
<dd>This specifies a password for the EMP Terminal Mode login. It can be any string, up to 15 characters. A null password is used if none is specified. This password applies to user 3 if -u is used, to user 1 otherwise.</p>
<dt>-v priv</p>
<dd>Set a specific access priVilege for this user, where priv can be: 1=Callback, 2=User, 3=Operator, 4=Admin, 5=OEM, 15=NoAccess The default if not specified or specified in error, is to use 4=Admin.</p>
<dt>-x</p>
<dd>Causes extra debug messages to be displayed.</p>
<dt>-B</p>
<dd>Set the Baud rate of the serial port to one of the following: 9600, 19,2K, 38.4K, 57.6K, or 115.2K. The default is 19.2K bps. </p>
<dt>-N nodename</p>
<dd>Nodename or IP address of the remote target system. If a nodename is specified, IPMI LAN interface is used. Otherwise the local system management interface is used.</p>
<dt>-P/-R rmt_pswd</p>
<dd>Remote password for the nodename given. The default is a null password.</p>
<dt>-U rmt_user</p>
<dd>Remote username for the nodename given. The default is a null username.</p>
<dt>-E</p>
<dd>Use the remote password from Environment variable IPMI_PASSWORD.</p>
<dt>-F drv_t</p>
<dd>Force the driver type to one of the followng: imb, va, open, gnu, landesk, lan, lan2, lan2i, kcs, smb. Note that lan2i means lan2 with intelplus. The default is to detect any available driver type and use it.</p>
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
<dl>
<dt>ipmiutil serial -t (or -c)</p>
<dd>Enables Terminal Mode management functions, shared with BIOS Serial Console redirection. The user can switch between serial console operations and IPMI Terminal Mode commands by typing ESC &#8216;)&#8217; and ESC &#8216;Q&#8217;.</p>
<dt>ipmiutil serial -s</p>
<dd>Enables Basic Mode management functions shared with BIOS Serial Console redirection. The user can switch between serial console operations and IPMI Basic Mode management programs on the same serial port.</p>
<dt>ipmiutil serial -d</p>
<dd>Disables the serial port management functions. This would be used if only the BIOS Serial Console were used and no BMC serial management functions.  How to login to a Terminal Mode console:<br />
 ESC ( (switch to Terminal mode)<br />
 [SYS PWD -N ] (login for default user, null psw)<br />
 [SYS PWD -U ROOT -N PASSWORD] (syntax example for user 3)<br />
 [SYS 000157 ACTIVATE] (activate advanced commands)<br />
 [SYS HEALTH QUERY]<br />
 [SYS HELP]<br />
 [SYS PWD] (logoff)<br />
 ESC Q (switch to BIOS console)<br />
 See IPMI 1.5 Spec, Appendix E, and Intel TIGPR2U TPS for more information. </p>
<h2>Dependencies</h2>
<p>The ipmiutil serial utility is intended to configure the EMP serial port on the server for shared access between BMC/IPMI functions and BIOS Console Redirection. Some platforms only support only Basic Mode for BMC/IPMI functions. Basic Mode requires a remote client application to utilize it (Windows ISC Console/DPC, or a special modified Linux telnet). There are some platforms which implement Terminal Mode via IPMI v1.5 Appendix E to make remote management with character commands available on the serial port without a special remote client application. </p>
<p> For example, Intel TSRLT2 systems would use &quot;ipmiutil serial -s&quot; for Basic Mode shared functions, but Intel TIGPR2U systems could use &quot;ipmiutil serial -c&quot; to configure Terminal Mode functions. On your system, run &quot;ipmiutil serial -r&quot; to check whether Serial Param(29): &quot;Terminal Mode Config&quot; is supported. If not, configure Basic Mode via &quot;ipmiutil serial -s&quot;.</p>
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
<p><a href="/docs/linux/man/8-ipmiutil/">ipmiutil</a>(8) <a href="/docs/linux/man/8-ialarms/">ialarms</a>(8) <a href="/docs/linux/man/8-iconfig/">iconfig</a>(8) <a href="/docs/linux/man/8-icmd/">icmd</a>(8) <a href="/docs/linux/man/8-idiscover/">idiscover</a>(8) <a href="/docs/linux/man/8-ievents/">ievents</a>(8) <a href="/docs/linux/man/8-ifru/">ifru</a>(8) <a href="/docs/linux/man/8-igetevent/">igetevent</a>(8) <a href="/docs/linux/man/8-ihealth/">ihealth</a>(8) <a href="/docs/linux/man/8-ilan/">ilan</a>(8) <a href="/docs/linux/man/8-ireset/">ireset</a>(8) <a href="/docs/linux/man/8-isel/">isel</a>(8) <a href="/docs/linux/man/8-isensor/">isensor</a>(8) <a href="/docs/linux/man/8-isol/">isol</a>(8) <a href="/docs/linux/man/8-iwdt/">iwdt</a>(8) </p>
<h2>Warnings</h2>
<p>See <a rel="nofollow" href="http://ipmiutil.sourceforge.net/">http://ipmiutil.sourceforge.net/</a> for the latest version of ipmiutil and any bug fix list.</p>
<h2>Copyright</h2>
<p>Copyright (C) 2009 Kontron America, Inc. </p>
<p> See the file COPYING in the distribution for more details regarding redistribution. </p>
<p> This utility is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY.</p>
<h2>Author</h2>
<p>Andy Cress &lt;arcress at users.sourceforge.net&gt;</p>

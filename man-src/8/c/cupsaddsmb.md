---
title: "cupsaddsmb(8)"
name: "cupsaddsmb"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cupsaddsmb/"
description: "cupsaddsmb – export printers to samba for windows clients"
---

<p>cupsaddsmb &#8211; export printers to samba for windows clients</p>
<h2>Synopsis</h2>
<p><code>cupsaddsmb</code> [ <code>-H</code> <i>samba-server</i> ] [ <code>-U</code> <i>samba-user[%samba-password]</i> ] [ <code>-h</code> <i>cups-server[:port]</i> ] [ <code>-v</code> ] <code>-a</code><br />
 <code>cupsaddsmb</code> [ <code>-H</code> <i>samba-server</i> ] [ <code>-U</code> <i>samba-user[%samba-password]</i> ] [ <code>-h</code> <i>cups-server[:port]</i> ] [ <code>-v</code> ] <i>printer</i> [ &#8230; <i>printer</i> ]</p>
<h2>Description</h2>
<p>The <code>cupsaddsmb</code> program exports printers to the SAMBA software (version 2.2.0 or higher) for use with Windows clients. Depending on the SAMBA configuration, you may need to provide a password to export the printers. This program requires the Windows printer driver files described below.</p>
<h3>Samba Configuration</h3>
<p><code>cupsaddsmb</code> uses the RPC-based printing support in SAMBA to provide printer drivers and PPD files to Windows client machines. In order to use this functionality, you must first configure the SAMBA <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5) file to support printing through CUPS and provide a printer driver download share, as follows: </p>
<pre> [global]
 load printers = yes
 printing = cups
 printcap name = cups
 [printers]
 comment = All Printers
 path = /var/spool/samba
 browseable = no
 public = yes
 guest ok = yes
 writable = no
 printable = yes
 [print$]
 comment = Printer Drivers
 path = /etc/samba/drivers
 browseable = yes
 guest ok = no
 read only = yes
 write list = root</pre>
<p>This configuration assumes a FHS-compliant installation of SAMBA; adjust the [printers] and [print$] share paths accordingly on your system as needed.</p>
<h3>Microsoft Postscript Drivers For Windows</h3>
<p>The base driver for Windows 2000 and higher is the Microsoft PostScript driver, which is available on any system running Windows 2000 or higher in the %WINDIR%\SYSTEM32\SPOOL\DRIVERS\W32X86\3 folder for 32-bit drivers and %WINDIR%\SYSTEM32\SPOOL\DRIVERS\X64\3 folder for 64-bit drivers. </p>
<p> Copy the 32-bit drivers to the <i>/usr/share/cups/drivers</i> directory and the 64-bit drivers to the <i>/usr/share/cups/drivers/x64</i> directory exactly as named below: </p>
<pre> ps5ui.dll
 pscript.hlp
 pscript.ntf
 pscript5.dll</pre>
<p><code>Note:</code> Unlike Windows, case is significant &#8211; make sure that you use the lowercase filenames shown above, otherwise <code>cupsaddsmb</code> will fail to export the drivers.</p>
<h2>Options</h2>
<p><code>cupsaddsmb</code> supports the following options:</p>
<dl>
<dt><code>-H </code><i>samba-server</i></p>
<dd>Specifies the SAMBA server which defaults to the CUPS server.</p>
<dt><code>-U </code><i>samba-user</i>[<code>%</code><i>samba-password</i>]</p>
<dd>Specifies the SAMBA print admin username which defaults to your current username. If the username contains a percent (%) character, then the text following the percent is treated as the SAMBA password to use.</p>
<dt><code>-a</code></p>
<dd>Exports all known printers. Otherwise only the named printers are exported.</p>
<dt><code>-h </code><i>cups-server</i>[<code>:</code><i>port</i>]</p>
<dd>Specifies a different CUPS server to use.</p>
<dt><code>-v</code></p>
<dd>Specifies that verbose information should be shown. This is useful for debugging SAMBA configuration problems.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-rpcclient/">rpcclient</a></code>(1), <code><a href="/docs/linux/man/1-smbclient/">smbclient</a></code>(1), <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8), <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5), CUPS Online Help (<a rel="nofollow" href="http://localhost:631/help)">http://localhost:631/help)</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2007-2017 by Apple Inc.</p>

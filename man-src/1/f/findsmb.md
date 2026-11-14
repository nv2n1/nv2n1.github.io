---
title: "findsmb(1)"
name: "findsmb"
section: "1"
letter: "f"
url: "/docs/linux/man/1-findsmb/"
description: "findsmb – list info about machines that respond to SMB name queries on a subnet"
---

<h2 class="name">NAME</h2>
<p> findsmb &#8211; list info about machines that respond to SMB name queries on a subnet </p>
<h2>SYNOPSIS</h2>
<dl>
<dt>
<dd>findsmb [subnet broadcast address]</dl>
<h2>DESCRIPTION</h2>
<p> This perl script is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> findsmb is a perl script that prints out several pieces of information about machines on a subnet that respond to SMB name query requests. It uses <code><a href="/docs/linux/man/1-nmblookup/">nmblookup</a></code>(1) and <code><a href="/docs/linux/man/1-smbclient/">smbclient</a></code>(1) to obtain this information.</p>
<h2>OPTIONS</h2>
<p> -r</p>
<dl>
<dt>
<dd> Controls whether findsmb takes bugs in Windows95 into account when trying to find a Netbios name registered of the remote machine. This option is disabled by default because it is specific to Windows 95 and Windows 95 machines only. If set, <code><a href="/docs/linux/man/1-nmblookup/">nmblookup</a></code>(1) will be called with <code>-B</code> option.</dl>
<p> subnet broadcast address</p>
<dl>
<dt>
<dd> Without this option, findsmb will probe the subnet of the machine where <code><a href="/docs/linux/man/1-findsmb/">findsmb</a></code>(1) is run. This value is passed to <code><a href="/docs/linux/man/1-nmblookup/">nmblookup</a></code>(1) as part of the <code>-B</code> option.</dl>
<h2>EXAMPLES</h2>
<p> The output of findsmb lists the following information for all machines that respond to the initial nmblookup for any name: IP address, NetBIOS name, Workgroup name, operating system, and SMB server version. </p>
<p> There will be a &#8216;+&#8217; in front of the workgroup name for machines that are local master browsers for that workgroup. There will be an &#8216;*&#8217; in front of the workgroup name for machines that are the domain master browser for that workgroup. Machines that are running Windows for Workgroups, Windows 95 or Windows 98 will not show any information about the operating system or server version. </p>
<p> The command with <code>-r</code> option must be run on a system without <code><a href="/docs/linux/man/8-nmbd/">nmbd</a></code>(8) running. If nmbd is running on the system, you will only get the IP address and the DNS name of the machine. To get proper responses from Windows 95 and Windows 98 machines, the command must be run as root and with <code>-r</code> option on a machine without nmbd running. </p>
<p> For example, running findsmb without <code>-r</code> option set would yield output similar to the following </p>
<dl>
<dt>
<dd>
<pre><code>
IP ADDR         NETBIOS NAME   WORKGROUP/OS/VERSION 
--------------------------------------------------------------------- 
192.168.35.10   MINESET-TEST1  [DMVENGR]
192.168.35.55   LINUXBOX      *[MYGROUP] [Unix] [Samba 2.0.6]
192.168.35.56   HERBNT2        [HERB-NT]
192.168.35.63   GANDALF        [MVENGR] [Unix] [Samba 2.0.5a for IRIX]
192.168.35.65   SAUNA          [WORKGROUP] [Unix] [Samba 1.9.18p10]
192.168.35.71   FROGSTAR       [ENGR] [Unix] [Samba 2.0.0 for IRIX]
192.168.35.78   HERBDHCP1     +[HERB]
192.168.35.88   SCNT2         +[MVENGR] [Windows NT 4.0] [NT LAN Manager 4.0]
192.168.35.93   FROGSTAR-PC    [MVENGR] [Windows 5.0] [Windows 2000 LAN Manager]
192.168.35.97   HERBNT1       *[HERB-NT] [Windows NT 4.0] [NT LAN Manager 4.0]
</code></pre>
</dl>
<h2>VERSION</h2>
<p> This man page is part of version 4.11.6-Ubuntu of the Samba suite.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-nmbd/">nmbd</a></code>(8), <code><a href="/docs/linux/man/1-smbclient/">smbclient</a></code>(1), and <code><a href="/docs/linux/man/1-nmblookup/">nmblookup</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. </p>
<h2>Index</h2>

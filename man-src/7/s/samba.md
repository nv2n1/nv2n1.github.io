---
title: "samba(7)"
name: "samba"
section: "7"
letter: "s"
url: "/docs/linux/man/7-samba/"
description: "samba – A Windows AD and SMB/CIFS fileserver for UNIX"
---

<p>samba &#8211; A Windows AD and SMB/CIFS fileserver for UNIX</p>
<h2>Synopsis</h2>
<dl>
<dd>samba</dl>
<h2>Description</h2>
<p>The Samba software suite is a collection of programs that implements the Server Message Block (commonly abbreviated as SMB) protocol for UNIX systems and provides Active Directory services. The first version of the SMB protocol is sometimes also referred to as the Common Internet File System (CIFS). For a more thorough description, see <a rel="nofollow noopener" href="http://www.ubiqx.org/cifs/." target="_blank">http://www.ubiqx.org/cifs/.</a> Samba also implements the NetBIOS protocol in nmbd. </p>
<p> <code><a href="/docs/linux/man/8-samba/">samba</a></code>(8)</p>
<dl>
<dd>The samba daemon provides the Active Directory services and file and print services to SMB clients. The configuration file for this daemon is described in <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5).</dl>
<p> <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8)</p>
<dl>
<dd>The smbd daemon provides the file and print services to SMB clients. The configuration file for this daemon is described in <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5).</dl>
<p> <code><a href="/docs/linux/man/8-nmbd/">nmbd</a></code>(8)</p>
<dl>
<dd>The nmbd daemon provides NetBIOS nameservice and browsing support. The configuration file for this daemon is described in <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5).</dl>
<p> <code><a href="/docs/linux/man/8-winbindd/">winbindd</a></code>(8)</p>
<dl>
<dd>winbindd is a daemon that is used for integrating authentication and the user database into unix.</dl>
<p> <code><a href="/docs/linux/man/1-smbclient/">smbclient</a></code>(1)</p>
<dl>
<dd>The smbclient program implements a simple ftp-like client. This is useful for accessing SMB shares on other compatible SMB servers, and can also be used to allow a UNIX box to print to a printer attached to any SMB server.</dl>
<p> <code><a href="/docs/linux/man/8-samba-tool/">samba-tool</a></code>(8)</p>
<dl>
<dd>The samba-tool is the main Samba Administration tool regarding Active Directory services.</dl>
<p> <code><a href="/docs/linux/man/1-testparm/">testparm</a></code>(1)</p>
<dl>
<dd>The testparm utility is a simple syntax checker for Samba&#8217;s <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5) configuration file. In AD server mode samba-tool testparm should be used though.</dl>
<p> <code><a href="/docs/linux/man/1-smbstatus/">smbstatus</a></code>(1)</p>
<dl>
<dd>The smbstatus tool provides access to information about the current connections to smbd.</dl>
<p> <code><a href="/docs/linux/man/1-nmblookup/">nmblookup</a></code>(1)</p>
<dl>
<dd>The nmblookup tool allows NetBIOS name queries to be made.</dl>
<p> <code><a href="/docs/linux/man/8-smbpasswd/">smbpasswd</a></code>(8)</p>
<dl>
<dd>The smbpasswd command is a tool for setting passwords on local Samba but also on remote SMB servers.</dl>
<p> <code><a href="/docs/linux/man/1-smbcacls/">smbcacls</a></code>(1)</p>
<dl>
<dd>The smbcacls command is a tool to set ACL&#8217;s on remote SMB servers.</dl>
<p> <code><a href="/docs/linux/man/1-smbtree/">smbtree</a></code>(1)</p>
<dl>
<dd>The smbtree command is a text-based network neighborhood tool.</dl>
<p> <code><a href="/docs/linux/man/1-smbtar/">smbtar</a></code>(1)</p>
<dl>
<dd>The smbtar can make backups of data directly from SMB servers.</dl>
<p> <code><a href="/docs/linux/man/8-smbspool/">smbspool</a></code>(8)</p>
<dl>
<dd>smbspool is a helper utility for printing on printers connected to SMB servers.</dl>
<p> <code><a href="/docs/linux/man/1-smbcontrol/">smbcontrol</a></code>(1)</p>
<dl>
<dd>smbcontrol is a utility that can change the behaviour of running samba, smbd, nmbd and winbindd daemons.</dl>
<p> <code><a href="/docs/linux/man/1-rpcclient/">rpcclient</a></code>(1)</p>
<dl>
<dd>rpcclient is a utility that can be used to execute RPC commands on remote SMB servers.</dl>
<p> <code><a href="/docs/linux/man/8-pdbedit/">pdbedit</a></code>(8)</p>
<dl>
<dd>The pdbedit command can be used to maintain the local user database on a Samba server.</dl>
<p> <code><a href="/docs/linux/man/1-findsmb/">findsmb</a></code>(1)</p>
<dl>
<dd>The findsmb command can be used to find SMB servers on the local network.</dl>
<p> <code><a href="/docs/linux/man/8-net/">net</a></code>(8)</p>
<dl>
<dd>The net command is the main administration tool for Samba member and standalone servers.</dl>
<p> <code><a href="/docs/linux/man/1-wbinfo/">wbinfo</a></code>(1)</p>
<dl>
<dd>wbinfo is a utility that retrieves and stores information related to winbind.</dl>
<p> <code><a href="/docs/linux/man/1-profiles/">profiles</a></code>(1)</p>
<dl>
<dd>profiles is a command-line utility that can be used to replace all occurrences of a certain SID with another SID.</dl>
<p> <code><a href="/docs/linux/man/1-log2pcap/">log2pcap</a></code>(1)</p>
<dl>
<dd>log2pcap is a utility for generating pcap trace files from Samba log files.</dl>
<p> <code><a href="/docs/linux/man/1-vfstest/">vfstest</a></code>(1)</p>
<dl>
<dd>vfstest is a utility that can be used to test vfs modules.</dl>
<p> <code><a href="/docs/linux/man/1-ntlm_auth/">ntlm_auth</a></code>(1)</p>
<dl>
<dd>ntlm_auth is a helper-utility for external programs wanting to do NTLM-authentication.</dl>
<p> <code><a href="/docs/linux/man/1-smbcquotas/">smbcquotas</a></code>(1)</p>
<dl>
<dd>smbcquotas is a tool to manage quotas on remote SMB servers.</dl>
<h2>Components</h2>
<p>The Samba suite is made up of several components. Each component is described in a separate manual page. It is strongly recommended that you read the documentation that comes with Samba and the manual pages of those components that you use. If the manual pages and documents aren&#8217;t clear enough then please visit <a rel="nofollow noopener" href="https://devel.samba.org" target="_blank">https://devel.samba.org</a> for information on how to file a bug report or submit a patch. </p>
<p> If you require help, visit the Samba webpage at <a rel="nofollow noopener" href="https://www.samba.org/" target="_blank">https://www.samba.org/</a> and explore the many option available to you.</p>
<h2>Availability</h2>
<p>The Samba software suite is licensed under the GNU Public License(GPL). A copy of that license should have come with the package in the file COPYING. You are encouraged to distribute copies of the Samba suite, but please obey the terms of this license. </p>
<p> The latest version of the Samba suite can be obtained from <a rel="nofollow noopener" href="https://download.samba.org/pub/samba/." target="_blank">https://download.samba.org/pub/samba/.</a> </p>
<p> The Samba Wiki at <a rel="nofollow noopener" href="https://wiki.samba.org" target="_blank">https://wiki.samba.org</a> has also a lot of useful information. On the Samba mailing list at <a rel="nofollow noopener" href="https://lists.samba.org" target="_blank">https://lists.samba.org</a> you can find a lot of information in the archives and you can subscribe to the samba list and ask for help or discuss things.</p>
<h2>Version</h2>
<p>This man page is part of version 4.11.6-Ubuntu of the Samba suite.</p>
<h2>Contributions</h2>
<p>If you wish to contribute to the Samba project, then I suggest you join the Samba mailing list at <a rel="nofollow noopener" href="https://lists.samba.org." target="_blank">https://lists.samba.org.</a> </p>
<p> If you have patches to submit, visit <a rel="nofollow noopener" href="https://devel.samba.org/" target="_blank">https://devel.samba.org/</a> for information on how to do it properly. We prefer patches in git format-patch format.</p>
<h2>Contributors</h2>
<p>Contributors to the project are now too numerous to mention here but all deserve the thanks of all Samba users. To see a full list, look at the change-log in the source package for the pre-CVS changes and at <a rel="nofollow noopener" href="https://git.samba.org/" target="_blank">https://git.samba.org/</a> for the contributors to Samba post-GIT. GIT is the Open Source source code control system used by the Samba Team to develop Samba. The project would have been unmanageable without it.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>

---
title: "ftpusers(5)"
name: "ftpusers"
section: "5"
letter: "f"
url: "/docs/linux/man/5-ftpusers/"
description: "ftpusers – list of users that may not log in via the FTP daemon"
---

<p>ftpusers &#8211; list of users that may not log in via the FTP daemon</p>
<h2>Description</h2>
<p>The text file <code>ftpusers</code> contains a list of users that may not log in using the File Transfer Protocol (FTP) server daemon. This file is used not merely for system administration purposes but for improving security within a TCP/IP networked environment. It will typically contain a list of the users that either have no business using ftp or have too many privileges to be allowed to log in through the FTP server daemon. Such users usually include root, daemon, bin, uucp, and news. If your FTP server daemon doesn&#8217;t use <code>ftpusers</code> then it is suggested that you read its documentation to find out how to block access for certain users. Washington University FTP server Daemon (wuftpd) and Professional FTP Daemon (proftpd) are known to make use of <code>ftpusers</code>.</p>
<h3>Format</h3>
<p>The format of <code>ftpusers</code> is very simple. There is one account name (or username) per line. Lines starting with a # are ignored.</p>
<h2>Files</h2>
<p><i>/etc/ftpusers</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-passwd/">passwd</a></code>(5), <code><a href="/docs/linux/man/8-proftpd/">proftpd</a></code>(8), <code><a href="/docs/linux/man/8-wuftpd/">wuftpd</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 3.53 of the Linux <i>man-pages</i> project. A description of the project, and information about reporting bugs, can be found at <a rel="nofollow" href="http://www.kernel.org/doc/man-pages/.">http://www.kernel.org/doc/man-pages/.</a> </p>

---
title: "smbspool(8)"
name: "smbspool"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smbspool/"
description: "smbspool – send a print file to an SMB printer"
---

<p>smbspool &#8211; send a print file to an SMB printer</p>
<h2>Synopsis</h2>
<dl>
<dd>smbspool {job} {user} {title} {copies} {options} [filename]</dl>
<h2>Description</h2>
<p>This tool is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> smbspool is a very small print spooling program that sends a print file to an SMB printer. The command-line arguments are position-dependent for compatibility with the Common UNIX Printing System, but you can use smbspool with any printing system or from a program or script. </p>
<p> <i>DEVICE URI</i> </p>
<p> smbspool specifies the destination using a Uniform Resource Identifier (&quot;URI&quot;) with a method of &quot;smb&quot;. This string can take a number of forms: </p>
<dl>
<dd>&bull; <a href="smb://server[:port]/printer">smb://server[:port]/printer</a></dl>
<dl>
<dd>&bull; <a href="smb://workgroup/server[:port]/printer">smb://workgroup/server[:port]/printer</a></dl>
<dl>
<dd>&bull; <a href="smb://username:password@server[:port]/printer">smb://username:password@server[:port]/printer</a></dl>
<dl>
<dd>&bull; <a href="smb://username:password@workgroup/server[:port]/printer">smb://username:password@workgroup/server[:port]/printer</a></dl>
<p> smbspool tries to get the URI from the environment variable <code>DEVICE_URI</code>. If <code>DEVICE_URI</code> is not present, smbspool will use argv[0] if that starts with &#8220;smb://&#8221; or argv[1] if that is not the case. </p>
<p> Programs using the <a href="/docs/linux/man/2-exec/">exec</a>(2) functions can pass the URI in argv[0], while shell scripts must set the <code>DEVICE_URI</code> environment variable prior to running smbspool.</p>
<h2>Options</h2>
<dl>
<dd>&bull; The job argument (argv[1]) contains the job ID number and is presently not used by smbspool.</dl>
<dl>
<dd>&bull; The user argument (argv[2]) contains the print user&#8217;s name and is presently not used by smbspool.</dl>
<dl>
<dd>&bull; The title argument (argv[3]) contains the job title string and is passed as the remote file name when sending the print job.</dl>
<dl>
<dd>&bull; The copies argument (argv[4]) contains the number of copies to be printed of the named file. If no filename is provided then this argument is not used by smbspool.</dl>
<dl>
<dd>&bull; The options argument (argv[5]) contains the print options in a single string and is currently not used by smbspool.</dl>
<dl>
<dd>&bull; The filename argument (argv[6]) contains the name of the file to print. If this argument is not specified then the print file is read from the standard input.</dl>
<h2>Version</h2>
<p>This man page is correct for version 3 of the Samba suite.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) and <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7).</p>
<h2>Author</h2>
<p>smbspool was written by Michael Sweet at Easy Software Products. </p>
<p> The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. </p>
<p> The original Samba man pages were written by Karl Auer. The man page sources were converted to YODL format (another excellent piece of Open Source software, available at <a href="ftp://ftp.icce.rug.nl/pub/unix/)">ftp://ftp.icce.rug.nl/pub/unix/)</a> and updated for the Samba 2.0 release by Jeremy Allison. The conversion to DocBook for Samba 2.2 was done by Gerald Carter. The conversion to DocBook XML 4.2 for Samba 3.0 was done by Alexander Bokovoy.</p>

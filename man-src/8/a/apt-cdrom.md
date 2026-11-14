---
title: "apt-cdrom(8)"
name: "apt-cdrom"
section: "8"
letter: "a"
url: "/docs/linux/man/8-apt-cdrom/"
description: "apt-cdrom – APT CD-ROM management utility"
---

<p>apt-cdrom &#8211; APT CD-ROM management utility</p>
<h2>Synopsis</h2>
<pre><code>apt-cdrom [-rmfan] [-d=cdrom_mount_point] [-o=config_string] [-c=config_file] {add | ident | {-v | --version} | {-h | --help}}</code></pre>
<h2>Description</h2>
<p><code>apt-cdrom</code></p>
<dd>is used to add a new CD-ROM to APT&#8217;s list of available sources. <code>apt-cdrom</code> takes care of determining the structure of the disc as well as correcting for several possible mis-burns and verifying the index files. </p>
<p> It is necessary to use <code>apt-cdrom</code> to add CDs to the APT system; it cannot be done by hand. Furthermore each disc in a multi-CD set must be inserted and scanned separately to account for possible mis-burns. </p>
<p> Unless the <code>-h</code>, or <code>&#8211;help</code> option is given, one of the commands below must be present. </p>
<p> <code>add</code></p>
<dl>
<dd>add is used to add a new disc to the source list. It will unmount the CD-ROM device, prompt for a disc to be inserted and then proceed to scan it and copy the index files. If the disc does not have a proper .disk directory you will be prompted for a descriptive title. </p>
<p> APT uses a CD-ROM ID to track which disc is currently in the drive and maintains a database of these IDs in /var/lib/apt/cdroms.list</dl>
<p> <code>ident</code></p>
<dl>
<dd>A debugging tool to report the identity of the current disc as well as the stored file name</dl>
<h2>Options</h2>
<p>All command line options may be set using the configuration file, the descriptions indicate the configuration option to set. For boolean options you can override the config file by using something like <code>-f-</code>,<code>&#8211;no-f</code>, <code>-f=no</code> or several other variations. </p>
<p> <code>&#8211;no-auto-detect</code>, <code>&#8211;cdrom</code></p>
<dl>
<dd>Do not try to auto-detect the CD-ROM path. Usually combined with the <code>&#8211;cdrom</code> option. Configuration Item: Acquire::cdrom::AutoDetect.</dl>
<p> <code>-d</code>, <code>&#8211;cdrom</code></p>
<dl>
<dd>Mount point; specify the location to mount the CD-ROM. This mount point must be listed in /etc/fstab and properly configured. Configuration Item: Acquire::cdrom::mount.</dl>
<p> <code>-r</code>, <code>&#8211;rename</code></p>
<dl>
<dd>Rename a disc; change the label of a disc or override the disc&#8217;s given label. This option will cause <code>apt-cdrom</code> to prompt for a new label. Configuration Item: APT::CDROM::Rename.</dl>
<p> <code>-m</code>, <code>&#8211;no-mount</code></p>
<dl>
<dd>No mounting; prevent <code>apt-cdrom</code> from mounting and unmounting the mount point. Configuration Item: APT::CDROM::NoMount.</dl>
<p> <code>-f</code>, <code>&#8211;fast</code></p>
<dl>
<dd>Fast Copy; Assume the package files are valid and do not check every package. This option should be used only if <code>apt-cdrom</code> has been run on this disc before and did not detect any errors. Configuration Item: APT::CDROM::Fast.</dl>
<p> <code>-a</code>, <code>&#8211;thorough</code></p>
<dl>
<dd>Thorough Package Scan; This option may be needed with some old Debian 1.1/1.2 discs that have Package files in strange places. It takes much longer to scan the CD but will pick them all up.</dl>
<p> <code>-n</code>, <code>&#8211;just-print</code>, <code>&#8211;recon</code>, <code>&#8211;no-act</code></p>
<dl>
<dd>No Changes; Do not change the <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5) file and do not write index files. Everything is still checked however. Configuration Item: APT::CDROM::NoAct.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Show a short usage summary.</dl>
<p> <code>-v</code>, <code>&#8211;version</code></p>
<dl>
<dd>Show the program version.</dl>
<p> <code>-c</code>, <code>&#8211;config-file</code></p>
<dl>
<dd>Configuration File; Specify a configuration file to use. The program will read the default configuration file and then this configuration file. If configuration settings need to be set before the default configuration files are parsed specify a file with the <code>APT_CONFIG</code> environment variable. See <code><a href="/docs/linux/man/5-apt-conf/">apt.conf</a></code>(5) for syntax information.</dl>
<p> <code>-o</code>, <code>&#8211;option</code></p>
<dl>
<dd>Set a Configuration Option; This will set an arbitrary configuration option. The syntax is <code>-o Foo::Bar=bar</code>. <code>-o</code> and <code>&#8211;option</code> can be used multiple times to set different options.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-apt-conf/">apt.conf</a></code>(5), <code><a href="/docs/linux/man/8-apt-get/">apt-get</a></code>(8), <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5)</p>
<h2>Diagnostics</h2>
<p><code>apt-cdrom</code> returns zero on normal operation, decimal 100 on error.</p>
<h2>Bugs</h2>
<p>m[blue]<code>APT bug page</code>m[]<font SIZE="-2">[1]</font>. If you wish to report a bug in APT, please see /usr/share/doc/debian/bug-reporting.txt or the <code><a href="/docs/linux/man/1-reportbug/">reportbug</a></code>(1) command.</p>
<h2>Authors</h2>
<p><code>Jason Gunthorpe</code></p>
<dl>
<dd></dl>
<p> <code>APT team</code></p>
<dl>
<dd></dl>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>APT bug page</p>
<dl>
<dd><a rel="nofollow" href="http://bugs.debian.org/src:apt">http://bugs.debian.org/src:apt</a></dl>

---
title: "smbstatus(1)"
name: "smbstatus"
section: "1"
letter: "s"
url: "/docs/linux/man/1-smbstatus/"
description: "smbstatus – report on current Samba connections"
---

<h2 class="name">NAME</h2>
<p> smbstatus &#8211; report on current Samba connections </p>
<h2>SYNOPSIS</h2>
<dl>
<dt>
<dd>smbstatus [-P] [-b] [-d&nbsp;<wbr>&lt;debug level&gt;] [-v] [-L] [-B] [-p] [-S] [-N] [-f] [-s&nbsp;<wbr>&lt;configuration file&gt;] [-u&nbsp;<wbr>&lt;username&gt;] [-n|&#8211;numeric] [-R|&#8211;profile-rates]</dl>
<h2>DESCRIPTION</h2>
<p> This tool is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> smbstatus is a very simple program to list the current Samba connections.</p>
<h2>OPTIONS</h2>
<p> -P|&#8211;profile</p>
<dl>
<dt>
<dd> If samba has been compiled with the profiling option, print only the contents of the profiling shared memory area.</dl>
<p> -R|&#8211;profile-rates</p>
<dl>
<dt>
<dd> If samba has been compiled with the profiling option, print the contents of the profiling shared memory area and the call rates.</dl>
<p> -b|&#8211;brief</p>
<dl>
<dt>
<dd> gives brief output.</dl>
<p> -d|&#8211;debuglevel=level</p>
<dl>
<dt>
<dd> <i>level</i> is an integer from 0 to 10. The default value if this parameter is not specified is 0. </p>
<p> The higher this value, the more detail will be logged to the log files about the activities of the server. At level 0, only critical errors and serious warnings will be logged. Level 1 is a reasonable level for day-to-day running &#8211; it generates a small amount of information about operations carried out. </p>
<p> Levels above 1 will generate considerable amounts of log data, and should only be used when investigating a problem. Levels above 3 are designed for use only by developers and generate HUGE amounts of log data, most of which is extremely cryptic. </p>
<p> Note that specifying this parameter here will override the m[blue]<code>log level</code>m[] parameter in the smb.conf file.</dl>
<p> -V|&#8211;version</p>
<dl>
<dt>
<dd> Prints the program version number.</dl>
<p> -s|&#8211;configfile=&lt;configuration file&gt;</p>
<dl>
<dt>
<dd> The file specified contains the configuration details required by the server. The information in this file includes server-specific information such as what printcap file to use, as well as descriptions of all the services that the server is to provide. See smb.conf for more information. The default configuration file name is determined at compile time.</dl>
<p> -l|&#8211;log-basename=logdirectory</p>
<dl>
<dt>
<dd> Base directory name for log/debug files. The extension <code>&quot;.progname&quot;</code> will be appended (e.g. log.smbclient, log.smbd, etc&#8230;). The log file is never removed by the client.</dl>
<p> &#8211;option=&lt;name&gt;=&lt;value&gt;</p>
<dl>
<dt>
<dd> Set the <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5) option &quot;&lt;name&gt;&quot; to value &quot;&lt;value&gt;&quot; from the command line. This overrides compiled-in defaults and options read from the configuration file.</dl>
<p> -v|&#8211;verbose</p>
<dl>
<dt>
<dd> gives verbose output.</dl>
<p> -L|&#8211;locks</p>
<dl>
<dt>
<dd> causes smbstatus to only list locks.</dl>
<p> -B|&#8211;byterange</p>
<dl>
<dt>
<dd> causes smbstatus to include byte range locks.</dl>
<p> -p|&#8211;processes</p>
<dl>
<dt>
<dd> print a list of <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) processes and exit. Useful for scripting.</dl>
<p> -S|&#8211;shares</p>
<dl>
<dt>
<dd> causes smbstatus to only list shares.</dl>
<p> -N|&#8211;notify</p>
<dl>
<dt>
<dd> causes smbstatus to display registered file notifications</dl>
<p> -f|&#8211;fast</p>
<dl>
<dt>
<dd> causes smbstatus to not check if the status data is valid by checking if the processes that the status data refer to all still exist. This speeds up execution on busy systems and clusters but might display stale data of processes that died without cleaning up properly.</dl>
<p> -?|&#8211;help</p>
<dl>
<dt>
<dd> Print a summary of command line options.</dl>
<p> -u|&#8211;user=&lt;username&gt;</p>
<dl>
<dt>
<dd> selects information relevant to <i>username</i> only.</dl>
<p> -n|&#8211;numeric</p>
<dl>
<dt>
<dd> causes smbstatus to display numeric UIDs and GIDs instead of resolving them to names.</dl>
<h2>VERSION</h2>
<p> This man page is correct for version 3 of the Samba suite.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) and <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5).</p>
<h2>AUTHOR</h2>
<p> The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. </p>
<p> The original Samba man pages were written by Karl Auer. The man page sources were converted to YODL format (another excellent piece of Open Source software, available at <a href="ftp://ftp.icce.rug.nl/pub/unix/)">ftp://ftp.icce.rug.nl/pub/unix/)</a> and updated for the Samba 2.0 release by Jeremy Allison. The conversion to DocBook for Samba 2.2 was done by Gerald Carter. The conversion to DocBook XML 4.2 for Samba 3.0 was done by Alexander Bokovoy. </p>
<h2>Index</h2>

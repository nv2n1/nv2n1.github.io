---
title: "profiles(1)"
name: "profiles"
section: "1"
letter: "p"
url: "/docs/linux/man/1-profiles/"
description: "profiles – A utility to report and change SIDs in registry files"
---

<h2 class="name">NAME</h2>
<p> profiles &#8211; A utility to report and change SIDs in registry files </p>
<h2>SYNOPSIS</h2>
<dl>
<dt>
<dd>profiles [-v] [-c|&#8211;change-sid SID] [-n|&#8211;new-sid SID] {file}</dl>
<h2>DESCRIPTION</h2>
<p> This tool is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> profiles is a utility that reports and changes SIDs in windows registry files. It currently only supports NT.</p>
<h2>OPTIONS</h2>
<p> file</p>
<dl>
<dt>
<dd> Registry file to view or edit.</dl>
<p> -v,&#8211;verbose</p>
<dl>
<dt>
<dd> Increases verbosity of messages.</dl>
<p> -c SID1 -n SID2, &#8211;change-sid SID1 &#8211;new-sid SID2</p>
<dl>
<dt>
<dd> Change all occurrences of SID1 in file by SID2.</dl>
<p> -d|&#8211;debuglevel=level</p>
<dl>
<dt>
<dd> <i>level</i> is an integer from 0 to 10. The default value if this parameter is not specified is 1. </p>
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
<p> -?|&#8211;help</p>
<dl>
<dt>
<dd> Print a summary of command line options.</dl>
<p> &#8211;usage</p>
<dl>
<dt>
<dd> Display brief usage message.</dl>
<h2>VERSION</h2>
<p> This man page is correct for version 3 of the Samba suite.</p>
<h2>AUTHOR</h2>
<p> The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. </p>
<p> The profiles man page was written by Jelmer Vernooij. </p>
<h2>Index</h2>

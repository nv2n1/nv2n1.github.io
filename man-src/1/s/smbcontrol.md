---
title: "smbcontrol(1)"
name: "smbcontrol"
section: "1"
letter: "s"
url: "/docs/linux/man/1-smbcontrol/"
description: "smbcontrol – send messages to smbd, nmbd or winbindd processes"
---

<h2 class="name">NAME</h2>
<p> smbcontrol &#8211; send messages to smbd, nmbd or winbindd processes </p>
<h2>SYNOPSIS</h2>
<dl>
<dt>
<dd>smbcontrol [-s] [-t|&#8211;timeout]</p>
<dt>
<dd>smbcontrol [destination] [message-type] [parameter]</dl>
<h2>DESCRIPTION</h2>
<p> This tool is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> smbcontrol is a very small program, which sends messages to a <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8), a <code><a href="/docs/linux/man/8-nmbd/">nmbd</a></code>(8), or a <code><a href="/docs/linux/man/8-winbindd/">winbindd</a></code>(8) daemon running on the system.</p>
<h2>OPTIONS</h2>
<p> -?|&#8211;help</p>
<dl>
<dt>
<dd> Print a summary of command line options.</dl>
<p> &#8211;usage</p>
<dl>
<dt>
<dd> Display brief usage message.</dl>
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
<p> -t|&#8211;timeout</p>
<dl>
<dt>
<dd> Set timeout to seconds.</dl>
<p> destination</p>
<dl>
<dt>
<dd> One of <i>nmbd</i>, <i>smbd</i>, <i>winbindd</i> or a process ID. </p>
<p> The <i>all</i> destination causes the message to &quot;broadcast&quot; to all running daemons including nmbd and winbind. This is a change for Samba 3.3, prior to this the parameter smbd used to do this. </p>
<p> The <i>smbd</i> destination causes the message to be sent to the smbd daemon specified in the smbd.pid file. </p>
<p> The <i>nmbd</i> destination causes the message to be sent to the nmbd daemon specified in the nmbd.pid file. </p>
<p> The <i>winbindd</i> destination causes the message to be sent to the winbind daemon specified in the winbindd.pid file. </p>
<p> If a single process ID is given, the message is sent to only that process.</dl>
<p> message-type</p>
<dl>
<dt>
<dd> Type of message to send. See the section <code>MESSAGE-TYPES</code> for details.</dl>
<p> parameters</p>
<dl>
<dt>
<dd> any parameters required for the message-type</dl>
<h2>MESSAGE-TYPES</h2>
<p> Available message types are: </p>
<p> close-share</p>
<dl>
<dt>
<dd> Order smbd to close the client connections to the named share. Note that this doesn&#8217;t affect client connections to any other shares. This message-type takes an argument of the share name for which client connections will be closed, or the &quot;*&quot; character which will close all currently open shares. This may be useful if you made changes to the access controls on the share. This message can only be sent to <code>smbd</code>.</dl>
<p> debug</p>
<dl>
<dt>
<dd> Set debug level to the value specified by the parameter. This can be sent to any of the destinations. If this message is sent to either the smbd or winbindd daemons, the parent process will rebroadcast the message to all child processes changing the debug level in each one.</dl>
<p> kill-client-ip</p>
<dl>
<dt>
<dd> Order smbd to close the client connections from a given IP address. This message-type takes an argument of the IP address from which client connections will be closed. This message can only be sent to <code>smbd</code>.</dl>
<p> force-election</p>
<dl>
<dt>
<dd> This message causes the nmbd daemon to force a new browse master election.</dl>
<p> ping</p>
<dl>
<dt>
<dd> Send specified number of &quot;ping&quot; messages and wait for the same number of reply &quot;pong&quot; messages. This can be sent to any of the destinations.</dl>
<p> profile</p>
<dl>
<dt>
<dd> Change profile settings of a daemon, based on the parameter. The parameter can be &quot;on&quot; to turn on profile stats collection, &quot;off&quot; to turn off profile stats collection, &quot;count&quot; to enable only collection of count stats (time stats are disabled), and &quot;flush&quot; to zero the current profile stats. This can be sent to any smbd or nmbd destinations.</dl>
<p> debuglevel</p>
<dl>
<dt>
<dd> Request debuglevel of a certain daemon and write it to stdout. This can be sent to any of the destinations.</dl>
<p> profilelevel</p>
<dl>
<dt>
<dd> Request profilelevel of a certain daemon and write it to stdout. This can be sent to any smbd or nmbd destinations.</dl>
<p> printnotify</p>
<dl>
<dt>
<dd> Order smbd to send a printer notify message to any Windows NT clients connected to a printer. This message-type takes the following arguments: </p>
<p> queuepause printername</p>
<dl>
<dt>
<dd> Send a queue pause change notify message to the printer specified.</dl>
<p> queueresume printername</p>
<dl>
<dt>
<dd> Send a queue resume change notify message for the printer specified.</dl>
<p> jobpause printername unixjobid</p>
<dl>
<dt>
<dd> Send a job pause change notify message for the printer and unix jobid specified.</dl>
<p> jobresume printername unixjobid</p>
<dl>
<dt>
<dd> Send a job resume change notify message for the printer and unix jobid specified.</dl>
<p> jobdelete printername unixjobid</p>
<dl>
<dt>
<dd> Send a job delete change notify message for the printer and unix jobid specified.</dl>
<p> Note that this message only sends notification that an event has occurred. It doesn&#8217;t actually cause the event to happen. </p>
<p> This message can only be sent to <code>smbd</code>.</dl>
<p> dmalloc-mark</p>
<dl>
<dt>
<dd> Set a mark for dmalloc. Can be sent to both smbd and nmbd. Only available if samba is built with dmalloc support.</dl>
<p> dmalloc-log-changed</p>
<dl>
<dt>
<dd> Dump the pointers that have changed since the mark set by dmalloc-mark. Can be sent to both smbd and nmbd. Only available if samba is built with dmalloc support.</dl>
<p> shutdown</p>
<dl>
<dt>
<dd> Shut down specified daemon. Can be sent to both smbd and nmbd.</dl>
<p> pool-usage</p>
<dl>
<dt>
<dd> Print a human-readable description of all talloc(pool) memory usage by the specified daemon/process. Available for both smbd and nmbd.</dl>
<p> drvupgrade</p>
<dl>
<dt>
<dd> Force clients of printers using specified driver to update their local version of the driver. Can only be sent to smbd.</dl>
<p> reload-config</p>
<dl>
<dt>
<dd> Force daemon to reload smb.conf configuration file. Can be sent to <code>smbd</code>, <code>nmbd</code>, or <code>winbindd</code>.</dl>
<p> reload-printers</p>
<dl>
<dt>
<dd> Force smbd to reload printers. Can only be sent to <code>smbd</code>.</dl>
<p> idmap</p>
<dl>
<dt>
<dd> Notify about changes of id mapping. Can be sent to <code>smbd</code> or (not implemented yet) <code>winbindd</code>. </p>
<p> flush [uid|gid]</p>
<dl>
<dt>
<dd> Flush caches for sid &lt;-&gt; gid and/or sid &lt;-&gt; uid mapping.</dl>
<p> delete &lt;ID&gt;</p>
<dl>
<dt>
<dd> Remove a mapping from cache. The mapping is given by &lt;ID&gt; which may either be a sid: S-x-&#8230;, a gid: &quot;GID number&quot; or a uid: &quot;UID number&quot;.</dl>
<p> kill &lt;ID&gt;</p>
<dl>
<dt>
<dd> Remove a mapping from cache. Terminate <code>smbd</code> if the id is currently in use.</dl>
</dl>
<p> num-children</p>
<dl>
<dt>
<dd> Query the number of smbd child processes. This message can only be sent to <code>smbd</code>.</dl>
<h2>VERSION</h2>
<p> This man page is correct for version 3 of the Samba suite.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-nmbd/">nmbd</a></code>(8) and <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8).</p>
<h2>AUTHOR</h2>
<p> The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. </p>
<p> The original Samba man pages were written by Karl Auer. The man page sources were converted to YODL format (another excellent piece of Open Source software, available at <a href="ftp://ftp.icce.rug.nl/pub/unix/)">ftp://ftp.icce.rug.nl/pub/unix/)</a> and updated for the Samba 2.0 release by Jeremy Allison. The conversion to DocBook for Samba 2.2 was done by Gerald Carter. The conversion to DocBook XML 4.2 for Samba 3.0 was done by Alexander Bokovoy. </p>
<h2>Index</h2>

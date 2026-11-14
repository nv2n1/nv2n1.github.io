---
title: "nmblookup(1)"
name: "nmblookup"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nmblookup/"
description: "nmblookup – NetBIOS over TCP/IP client used to lookup NetBIOS names"
---

<h2 class="name">NAME</h2>
<p> nmblookup &#8211; NetBIOS over TCP/IP client used to lookup NetBIOS names </p>
<h2>SYNOPSIS</h2>
<dl>
<dt>
<dd>nmblookup [-M|&#8211;master-browser] [-R|&#8211;recursion] [-S|&#8211;status] [-r|&#8211;root-port] [-A|&#8211;lookup-by-ip] [-B|&#8211;broadcast&nbsp;&lt;broadcast address&gt;] [-U|&#8211;unicast&nbsp;&lt;unicast address&gt;] [-d&nbsp;&lt;debug level&gt;] [-s&nbsp;&lt;smb config file&gt;] [-i&nbsp;&lt;NetBIOS scope&gt;] [-T|&#8211;translate] [-f|&#8211;flags] {name}</dl>
<h2>DESCRIPTION</h2>
<p> This tool is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> nmblookup is used to query NetBIOS names and map them to IP addresses in a network using NetBIOS over TCP/IP queries. The options allow the name queries to be directed at a particular IP broadcast area or to a particular machine. All queries are done over UDP.</p>
<h2>OPTIONS</h2>
<p> -M|&#8211;master-browser</p>
<dl>
<dt>
<dd> Searches for a master browser by looking up the NetBIOS <i>name</i> with a type of <code>0x1d</code>. If <i> name</i> is &quot;-&quot; then it does a lookup on the special name <code>__MSBROWSE__</code>. Please note that in order to use the name &quot;-&quot;, you need to make sure &quot;-&quot; isn&#8217;t parsed as an argument, e.g. use : <code>nmblookup -M &#8212; &#8211;</code>.</dl>
<p> -R|&#8211;recursion</p>
<dl>
<dt>
<dd> Set the recursion desired bit in the packet to do a recursive lookup. This is used when sending a name query to a machine running a WINS server and the user wishes to query the names in the WINS server. If this bit is unset the normal (broadcast responding) NetBIOS processing code on a machine is used instead. See RFC1001, RFC1002 for details.</dl>
<p> -S|&#8211;status</p>
<dl>
<dt>
<dd> Once the name query has returned an IP address then do a node status query as well. A node status query returns the NetBIOS names registered by a host.</dl>
<p> -r|&#8211;root-port</p>
<dl>
<dt>
<dd> Try and bind to UDP port 137 to send and receive UDP datagrams. The reason for this option is a bug in Windows 95 where it ignores the source port of the requesting packet and only replies to UDP port 137. Unfortunately, on most UNIX systems root privilege is needed to bind to this port, and in addition, if the <code><a href="/docs/linux/man/8-nmbd/">nmbd</a></code>(8) daemon is running on this machine it also binds to this port.</dl>
<p> -A|&#8211;lookup-by-ip</p>
<dl>
<dt>
<dd> Interpret <i>name</i> as an IP Address and do a node status query on this address.</dl>
<p> -n|&#8211;netbiosname &lt;primary NetBIOS name&gt;</p>
<dl>
<dt>
<dd> This option allows you to override the NetBIOS name that Samba uses for itself. This is identical to setting the m[blue]<code>netbios name</code>m[] parameter in the smb.conf file. However, a command line setting will take precedence over settings in smb.conf.</dl>
<p> -i|&#8211;scope &lt;scope&gt;</p>
<dl>
<dt>
<dd> This specifies a NetBIOS scope that nmblookup will use to communicate with when generating NetBIOS names. For details on the use of NetBIOS scopes, see rfc1001.txt and rfc1002.txt. NetBIOS scopes are <i>very</i> rarely used, only set this parameter if you are the system administrator in charge of all the NetBIOS systems you communicate with.</dl>
<p> -W|&#8211;workgroup=domain</p>
<dl>
<dt>
<dd> Set the SMB domain of the username. This overrides the default domain which is the domain defined in smb.conf. If the domain specified is the same as the servers NetBIOS name, it causes the client to log on using the servers local SAM (as opposed to the Domain SAM).</dl>
<p> -O|&#8211;socket-options socket options</p>
<dl>
<dt>
<dd> TCP socket options to set on the client socket. See the socket options parameter in the smb.conf manual page for the list of valid options.</dl>
<p> -?|&#8211;help</p>
<dl>
<dt>
<dd> Print a summary of command line options.</dl>
<p> &#8211;usage</p>
<dl>
<dt>
<dd> Display brief usage message.</dl>
<p> -B|&#8211;broadcast &lt;broadcast address&gt;</p>
<dl>
<dt>
<dd> Send the query to the given broadcast address. Without this option the default behavior of nmblookup is to send the query to the broadcast address of the network interfaces as either auto-detected or defined in the <i>interfaces</i> parameter of the <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5) file.</dl>
<p> -U|&#8211;unicast &lt;unicast address&gt;</p>
<dl>
<dt>
<dd> Do a unicast query to the specified address or host <i>unicast address</i>. This option (along with the <i>-R</i> option) is needed to query a WINS server.</dl>
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
<p> -T|&#8211;translate</p>
<dl>
<dt>
<dd> This causes any IP addresses found in the lookup to be looked up via a reverse DNS lookup into a DNS name, and printed out before each </p>
<p> <i>IP address &#8230;. NetBIOS name</i> </p>
<p> pair that is the normal output.</dl>
<p> -f|&#8211;flags</p>
<dl>
<dt>
<dd> Show which flags apply to the name that has been looked up. Possible answers are zero or more of: Response, Authoritative, Truncated, Recursion_Desired, Recursion_Available, Broadcast.</dl>
<p> name</p>
<dl>
<dt>
<dd> This is the NetBIOS name being queried. Depending upon the previous options this may be a NetBIOS name or IP address. If a NetBIOS name then the different name types may be specified by appending &#8216;#&lt;type&gt;&#8217; to the name. This name may also be &#8216;*&#8217;, which will return all registered names within a broadcast area.</dl>
<h2>EXAMPLES</h2>
<p> nmblookup can be used to query a WINS server (in the same way nslookup is used to query DNS servers). To query a WINS server, nmblookup must be called like this: </p>
<p> nmblookup -U server -R &#8216;name&#8217; </p>
<p> For example, running : </p>
<p> nmblookup -U samba.org -R &#8216;IRIX#1B&#8217; </p>
<p> would query the WINS server samba.org for the domain master browser (1B name type) for the IRIX workgroup.</p>
<h2>VERSION</h2>
<p> This man page is part of version 4.11.6-Ubuntu of the Samba suite.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-nmbd/">nmbd</a></code>(8), <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7), and <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5).</p>
<h2>AUTHOR</h2>
<p> The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. </p>
<h2>Index</h2>

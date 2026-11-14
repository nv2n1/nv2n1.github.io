---
title: "dbwrap_tool(1)"
name: "dbwrap_tool"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbwrap_tool/"
description: "dbwrap_tool – low level TDB/CTDB manipulation tool using the dbwrap interface"
---

<h2 class="name">NAME</h2>
<p> dbwrap_tool &#8211; low level TDB/CTDB manipulation tool using the dbwrap interface </p>
<h2>SYNOPSIS</h2>
<dl>
<dt>
<dd>dbwrap_tool [&#8211;persistent] [&#8211;non-persistent] [-d&nbsp;&lt;debug level&gt;] [-s&nbsp;&lt;config file&gt;] [-l&nbsp;&lt;log file base&gt;] [-V] [&#8211;option=&lt;name&gt;=&lt;value&gt;] {&lt;database&gt;} {&lt;operation&gt;} [&lt;key&gt;&nbsp;[&lt;type&gt;&nbsp;[&lt;value&gt;]]]</dl>
<h2>DESCRIPTION</h2>
<p> This tool is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> The dbwrap_tool program is used to read and manipulate TDB/CTDB databases using the dbwrap interface. </p>
<p> The following database operations are available:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; fetch: fetch a record</dl>
<dl>
<dt>
<dd> &bull; store: create or modify a record</dl>
<dl>
<dt>
<dd> &bull; delete: remove a record</dl>
<dl>
<dt>
<dd> &bull; exists: test for existence of a record</dl>
<dl>
<dt>
<dd> &bull; erase: remove all records</dl>
<dl>
<dt>
<dd> &bull; listkeys: list all available records</dl>
<dl>
<dt>
<dd> &bull; listwatchers: list processes, which are waiting for changes in a record</dl>
</dl>
<p> The following types are available:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; int32: signed 32bit integer</dl>
<dl>
<dt>
<dd> &bull; uint32: unsigned 32bit integer</dl>
<dl>
<dt>
<dd> &bull; string: &quot;hello world&quot;</dl>
<dl>
<dt>
<dd> &bull; hex: hex strings like &quot;68656C6C6F20776F726C6400&quot; (&quot;hello world&quot;)</dl>
</dl>
<h2>OPTIONS</h2>
<p> &#8211;persistent</p>
<dl>
<dt>
<dd> Open the database as a persistent database. </p>
<p> Exactly one of &#8211;persistent and &#8211;non-persistent must be specified.</dl>
<p> &#8211;non-persistent</p>
<dl>
<dt>
<dd> Open the database as a non-persistent database. </p>
<p> Caveat: opening a database as non-persistent when there is currently no other opener will wipe the database. </p>
<p> Exactly one of &#8211;persistent and &#8211;non-persistent must be specified.</dl>
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
<h2>COMMANDS</h2>
<h3>fetch</h3>
<dl>
<dt>
<dd>dbwrap_tool &lt;database&gt; fetch &lt;key&gt; &lt;type&gt; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>
</dl>
<h3>store</h3>
<dl>
<dt>
<dd>dbwrap_tool &lt;database&gt; store &lt;key&gt; &lt;type&gt; &lt;value&gt; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>
</dl>
<h3>delete</h3>
<dl>
<dt>
<dd>dbwrap_tool &lt;database&gt; delete &lt;key&gt; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>
</dl>
<h3>exists</h3>
<dl>
<dt>
<dd>dbwrap_tool &lt;database&gt; exists &lt;key&gt; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>
</dl>
<h3>erase</h3>
<dl>
<dt>
<dd>dbwrap_tool &lt;database&gt; erase</dl>
<h3>listkeys</h3>
<dl>
<dt>
<dd>dbwrap_tool &lt;database&gt; listkeys <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>
</dl>
<h3>listwatchers</h3>
<dl>
<dt>
<dd>dbwrap_tool &lt;database&gt; listwatchers <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>
</dl>
<h2>EXAMPLES</h2>
<p> List all keys from winbindd_idmap.tdb</p>
<dl>
<dt>
<dd> dbwrap_tool &#8211;persistent winbindd_idmap.tdb listkeys</dl>
<p> Fetch record with key &quot;USER HWM&quot; as uint32</p>
<dl>
<dt>
<dd> dbwrap_tool &#8211;persistent winbindd_idmap.tdb fetch &quot;USER HWM&quot; uint32</dl>
<p> Remove record with key &quot;USER HWM&quot;</p>
<dl>
<dt>
<dd> dbwrap_tool &#8211;persistent winbindd_idmap.tdb remove &quot;USER HWM&quot;</dl>
<p> Store and overwrite record &quot;USER HWM&quot; with value 214</p>
<dl>
<dt>
<dd> uint32: dbwrap_tool &#8211;persistent winbindd_idmap.tdb store &quot;USER HWM&quot; uint32 214 hex: dbwrap_tool &#8211;persistent winbindd_idmap.tdb store &quot;USER HWM&quot; hex D6000000</dl>
<h2>NOTES</h2>
<p> Use with caution!</p>
<h2>VERSION</h2>
<p> This man page is part of version 4.11.6-Ubuntu of the Samba suite.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8), <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7)</p>
<h2>AUTHOR</h2>
<p> The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. </p>
<p> The dbwrap_tool manpage was written by Bjoern Baumbach. </p>
<h2>Index</h2>

---
title: "freetds-conf(5)"
name: "freetds-conf"
section: "5"
letter: "f"
url: "/docs/linux/man/5-freetds-conf/"
description: "freetds.conf – configuration file for FreeTDS"
---

<p><code>freetds.conf</code> &#8211; configuration file for FreeTDS</p>
<h2>Synopsis</h2>
<p>The freetds.conf file describes Sybase and Microsoft database servers to the FreeTDS library. It comprises sections headed by a servername, followed by a list of connection properties denoted as name-value pairs. Defaults are defined via a Bq global section. This file supersedes the interfaces file that Sybase defines for the same purpose, although the latter is still supported.</p>
<h2>Description</h2>
<p>A section begins with a servername &#8212; the name of the server &#8212; in square brackets. The servername is chosen at the client&#8217;s descretion. (One exception: with Sybase ASA the servername must match the database name to be used.) </p>
<p> Sections contain properties, one per line, in the form </p>
<blockquote><p><tt>name = value</tt></p></blockquote>
<p> where <i>name</i> is the connection property to be described. Servernames and properties are not case sensitive. Values are case-preserving i.e., copied literally. Comments begin with either a semicolon (So ; Sc or pound sign ) (So # Sc and continue to end of line. Blank lines are ignored. Whitespace surrounding the ) So = Sc is ignored.</p>
<h2>Properties</h2>
<dl>
<dt><code>client charset</code></p>
<dd>encoding of client data; overrides <a href="/docs/linux/man/1-locale/">locale</a>(1) settings</p>
<dl>
<dt><code>Domain:</code></p>
<dd>iconv character set names</p>
<dt><code>Default:</code></p>
<dd>ISO-8859-1</dl>
<dt><code>connect timeout</code></p>
<dd>seconds to wait for response from connect request</p>
<dl>
<dt><code>Domain:</code></p>
<dd>0 to MAX_INT</p>
<dt><code>Default:</code></p>
<dd>none</dl>
<dt><code>debug flags</code></p>
<dd>logging granularity</p>
<dl>
<dt><code>Domain:</code></p>
<dd>32-bit integer</p>
<dt><code>Default:</code></p>
<dd>0x4fff</dl>
<dt><code>dump file</code></p>
<dd>specifies location of a logfile and turns on logging</p>
<dl>
<dt><code>Domain:</code></p>
<dd>valid file name</p>
<dt><code>Default:</code></p>
<dd>none</dl>
<dt><code>dump file append</code></p>
<dd>log data appended to file instead of re-writing for each connection</p>
<dl>
<dt><code>Domain:</code></p>
<dd>yes/no</p>
<dt><code>Default:</code></p>
<dd>no</dl>
<dt><code>emulate little endian</code></p>
<dd>forces big endian machines to act as little endian to communicate with Microsoft Servers</p>
<dl>
<dt><code>Domain:</code></p>
<dd>yes/no</p>
<dt><code>Default:</code></p>
<dd>no</dl>
<dt><code>encryption</code></p>
<dd>
<dl>
<dt><i>off</i></p>
<dd>disables encryption (default)</p>
<dt><i>request</i></p>
<dd>use if available</p>
<dt><i>required</i></p>
<dd>allow encrypted connections only</dl>
<dt><code>host</code></p>
<dd>Name of the host the server is running on.</p>
<dl>
<dt><code>Domain:</code></p>
<dd>host name or IP address</p>
<dt><code>Default:</code></p>
<dd>SYBASE</dl>
<dt><code>initial block size</code></p>
<dd>maximum size of a protocol block</p>
<dl>
<dt><code>Domain:</code></p>
<dd>multiple of 512</p>
<dt><code>Default:</code></p>
<dd>512</dl>
<dt><code>instance</code></p>
<dd>name of Microsoft SQL Server instance to connect to (supersedes <i>port</i></p>
<dl>
<dt><code>Domain:</code></p>
<dd>instance name</p>
<dt><code>Default:</code></p>
<dd>none</dl>
<dt><code>port</code></p>
<dd>port number that the server is listening to</p>
<dl>
<dt><code>Domain:</code></p>
<dd>any valid port</p>
<dt><code>Default:</code></p>
<dd>TDS 5.0, 5000; TDS 7.0 and up, 1433</dl>
<dt><code>tds version</code></p>
<dd>TDS protocol version to use</p>
<dl>
<dt><code>Domain:</code></p>
<dd>4.2, 5.0, 7.0, 7.1, 7.2</p>
<dt><code>Default:</code></p>
<dd>&#8211;<code>-with-tdsver</code> value (5.0 if unspecified)</dl>
<dt><code>text size</code></p>
<dd>default value of TEXTSIZE, in bytes</p>
<dl>
<dt><code>Domain:</code></p>
<dd>0 to 4,294,967,295</p>
<dt><code>Default:</code></p>
<dd>4,294,967,295</dl>
<dt><code>timeout</code></p>
<dd>seconds to wait for response to a query</p>
<dl>
<dt><code>Domain:</code></p>
<dd>0 to MAX_INT</p>
<dt><code>Default:</code></p>
<dd>none (wait forever)</dl>
</dl>
<p> Do not define both Fa port and Fa instance Ns . One implies the other. </p>
<p> Boolean property values may be denoted as on/off, true/false, or 1/0.</p>
<h3>Debug Flags</h3>
<p>The log&#8217;s granularity can be controlled with the <i>debug flags</i> property.</p>
<dl>
<dt><code>Value Ta </code><code>Meaning</code></p>
<dd>
<dt><code>&nbsp;<wbr>&nbsp;<wbr>0x02<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>severe error</code></p>
<dd>
<dt><code>&nbsp;<wbr>&nbsp;<wbr>0x04<tt>&nbsp;<wbr>&nbsp;<wbr></tt>error</code></p>
<dd>
<dt><code>&nbsp;<wbr>&nbsp;<wbr>0x08<tt>&nbsp;<wbr></tt>warning</code></p>
<dd>
<dt><code>&nbsp;<wbr>&nbsp;<wbr>0x10<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>network</code></p>
<dd>
<dt><code>&nbsp;<wbr>&nbsp;<wbr>0x20information level 1</code></p>
<dd>
<dt><code>&nbsp;<wbr>&nbsp;<wbr>0x40information level 2</code></p>
<dd>
<dt><code>&nbsp;<wbr>&nbsp;<wbr>0x80function trace and info</code></p>
<dd>
<dt><code>0x1000show pid</code></p>
<dd>
<dt><code>0x2000show time</code></p>
<dd>
<dt><code>0x4000show source level info (source file and line)</code></p>
<dd>
<dt><code>0x8000thread id (not implemented).</code></p>
<dd></dl>
<h2>Names And Locations</h2>
<p>The file is normally named<br />
 /etc/freetds.conf or ${HOME}/.freetds.conf That name can be overridden with the FREETDSCONF environment variable. </p>
<p> FreeTDS will search conf files for a servername in the following order: </p>
<ol>
<li> a filename set programatically via dbsetifile() that is in .conf format
<li> a filename in the environment variable FREETDSCONF that is in .conf format
<li> ${HOME}/.freetds.conf if extant
<li> /etc/freetds.conf </ol>
<p> The search stops with the first file containing the servername. </p>
<p> If no conf file is found, FreeTDS searches for an interfaces file in the following order: </p>
<ol>
<li> a filename set programatically via dbsetifile() that is in interfaces format
<li> ${HOME}/.interfaces
<li> $SYBASE/interfaces (where <code>$SYBASE is an environment variable)</code> </ol>
<p> If the requested servername is not found in any configuration file, the fallback mechanism is: </p>
<ol>
<li> attempt to convert the name to an IP address with <a href="/docs/linux/man/3-inet_addr/">inet_addr</a>(3), else
<li> attempt to convert the name to an IP address with <a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a>(3), else
<li> attempt to look up the literal name &#8220;SYBASE&#8221; </ol>
<h2>Environment</h2>
<dl>
<dt><code>FREETDSCONF</code></p>
<dd>overrides name and location of the system-wide conf file</p>
<dt><code>TDSDUMP</code></p>
<dd>overrides the name and location of the FreeTDS log file</p>
<dt><code>TDSDUMPCONFIG</code></p>
<dd>specifies a name and location of a file that logs the search of configuration files</p>
<dt><code>TDSHOST</code></p>
<dd>overrides the host property</p>
<dt><code>TDSPORT</code></p>
<dd>overrides the port property</p>
<dt><code>TDSQUERY</code></p>
<dd>synonym for DSQUERY, the default servername</p>
<dt><code>TDSVER</code></p>
<dd>overrides the version specified in the freetds.conf</dl>
<p> The environment variables <code>TDSVER, TDSDUMP, TDSPORT, TDSQUERY, and TDSHOST</code> override values set by a .conf or interfaces file.</p>
<h2>Files</h2>
<p>/etc/freetds.conf , ${HOME}/.freetds.conf</p>
<h2>See Also</h2>
<p><i>FreeTDS User Guide</i></p>
<h2>History</h2>
<p>.conf files first appeared with version 0.53 of FreeTDS.</p>

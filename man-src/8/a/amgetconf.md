---
title: "amgetconf(8)"
name: "amgetconf"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amgetconf/"
description: "amgetconf – look up configuration parameters and manipulate debug logs"
---

<p>amgetconf &#8211; look up configuration parameters and manipulate debug logs</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>amgetconf</code> [<i>-l|&#8211;list</i>] [<i>&#8211;client</i>] [<i>&#8211;execute-where client|server</i>] [<code>-o</code>&nbsp;<wbr><i>configoption</i>&#8230;] [<i>config</i>] <i>parameter</i></dl>
<h2>Description</h2>
<p><code>Amgetconf</code></p>
<dd>has three main jobs: to fetch configuration information from the Amanda configuration; to fetch build-time configuration values; and to open and close debug logs for shell scripts. Each is treated in its own subsection, below. If <i>config</i> is not specified, <code>amgetconf</code> assumes it is being run from the configuration directory and that <i>amanda.conf</i> is present. The order of options and arguments does not matter. <i>parameter</i> is always case-insensitive, and &#8216;-&#8216; and &#8216;_&#8217; are treated as identical, just as in <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5). See the &quot;<code>CONFIGURATION OVERRIDE</code>&quot; section in <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8) for information on the -o option.</p>
<h3>Amanda Configuration</h3>
<p>If <i>parameter</i> is a configuration keyword (from <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5)), then amgetconf will return the corresponding value. For keywords which can take multiple values, amgetconf will return all values, one on each line. Values in configuration subsections are specified with parameters of the form TYPE:NAME:PARAMETER, where TYPE is the subsection type (one of dumptype, tapetype, interface, holdingdisk, application-tool, or script-tool; NAME is the name of the subsection (e.g., user-tar), and PARAMETER is the name of the disired parameter within that subsection. The &#8211;list option lists the subsections of a certain type, where the type is givein as the parameter. The &#8211;client option is equivalent to &#8211;execute-where server (below). The &#8211;execute-where option tells amgetconf whether to operate on the client or the server; the server is the default.</p>
<h3>Build Configuration</h3>
<p>If <i>parameter</i> begins with build., then the following name is a build environment variable. Variables without a value (e.g. XFSDUMP on a system that does not support that type of file system) will not report an error and will return an empty string as the value. Some boolean variables (e.g. <i>USE_AMANDAHOSTS</i>) will return 1 if the flag is set or an empty string if it is not, while others return yes or no, as indicated below (the difference is historical). Combining the &#8211;list option with the parameter build will enumerate all available build parameters. <code>Build Parameters</code> bindir, sbindir, libexecdir, mandir</p>
<dl>
<dd>Install directories</dl>
<p> AMANDA_TMPDIR, CONFIG_DIR, AMANDA_DBGDIR, GNUTAR_LISTED_INCREMENTAL_DIR</p>
<dl>
<dd>Runtime directories</dl>
<p> listed_inc_dir</p>
<dl>
<dd>Same as GNUTAR_LISTED_INCREMENTAL_DIR</dl>
<p> CC, VERSION, ASSERTIONS, LOCKING</p>
<dl>
<dd>Build information. ASSERTIONS is 1 or empty.</dl>
<p> DUMP, RESTORE, VDUMP, VRESTORE, XFSDUMP, XFSRESTORE, VXDUMP, VXRESTORE, SAMBA_CLIENT, GNUTAR, STAR, COMPRESS_PATH, UNCOMPRESS_PATH</p>
<dl>
<dd>Paths to various utility progarms (empty if they are not found or not used)</dl>
<p> AIX_BACKUP</p>
<dl>
<dd>Is DUMP the AIX backup program? (empty or 1)</dl>
<p> DUMP_RETURNS_1</p>
<dl>
<dd>Does DUMP return 1 on success? (empty or 1)</dl>
<p> BSD_SECURITY, BSDUDP_SECURITY, BSDTCP_SECURITY, KRB5_SECURITY, SSH_SECURITY, RSH_SECURITY</p>
<dl>
<dd>Indicate which authentication mechanisms are available (yes or no).</dl>
<p> USE_AMANDAHOSTS</p>
<dl>
<dd>Should the &quot;bsd&quot; authentication mechanism use amandahosts? (yes or no).</dl>
<p> AMANDA_DEBUG_DAYS</p>
<dl>
<dd>Number of days after which debug logs are deleted.</dl>
<p> DEFAULT_SERVER, DEFAULT_CONFIG, DEFAULT_TAPE_SERVER, DEFAULT_TAPE_DEVICE</p>
<dl>
<dd>Default values for configuration parameters</dl>
<p> CLIENT_LOGIN</p>
<dl>
<dd>Userid under which the client runs (from &#8211;with-user).</dl>
<p> USE_RUNDUMP</p>
<dl>
<dd>Should Amanda use the rundump wrapper? (empty or 1)</dl>
<p> CHECK_USERID</p>
<dl>
<dd>Does Amanda check that userids are correct? (empty or 1)</dl>
<p> COMPRESS_SUFFIX, COMPRESS_FAST_OPT, COMPRESS_BEST_OPT, UNCOMPRESS_OPT</p>
<dl>
<dd>Command-line options for the compression program.</dl>
<p> TICKET_LIFETIME, SERVER_HOST_PRINCIPAL, SERVER_HOST_INSTANCE, SERVER_HOST_KEY_FILE, CLIENT_HOST_PRINCIPAL, CLIENT_HOST_INSTANCE, CLIENT_HOST_KEY_FILE</p>
<dl>
<dd>Kerberos parameters.</dl>
<h3>Debug Log Management</h3>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 That this application is responsible for debug logs is a historical quirk, but the functionality is widely used.  If <i>parameter</i> begins with <i>dbopen.</i>, the string following the period is a program name and an Amanda debug file will be created for the caller. The name of the logfile is returned. If <i>parameter</i> begins with <i>dbclose.</i>, the string following the period is a program name previously used with <i>dbopen.</i>, followed by a colon (:) and the previously opened file name. The name of the logfile is returned.</p>
<h2>Examples</h2>
<p>Find out the path to the log file directory: </p>
<pre>% amgetconf daily logdir
/usr/local/etc/amanda/daily/logs</pre>
<p>Find out the current tape type: </p>
<pre>% amgetconf daily tapetype
DLT4000-IV</pre>
<p>Find out that tape type&#8217;s length: </p>
<pre>% amgetconf daily tapetype:DLT4000-IV:length
1024000</pre>
<p>List the other available tapetype: </p>
<pre>% amgetconf daily --list tapetype
DISK
QIC-60
DEC-DLT2000
...</pre>
<p>Find out the configuration directory: </p>
<pre>% amgetconf build.CONFIG_DIR
/usr/local/etc/amanda/</pre>
<p>List all build-time parameters </p>
<pre>% amgetconf --list build
AIX_BACKUP
AMANDA_DBGDIR
AMANDA_DEBUG_DAYS
...</pre>
<p>Create, use and close a debug file in a script: </p>
<pre>% debug_file=`amgetconf daily dbopen.myscript`
% echo debug information &gt;&gt; $debug_file
% amgetconf daily dbclose.myscript:$debug_file</pre>
<h2>Messages</h2>
<p>amgetconf: no such parameter <i>param</i></p>
<dl>
<dd>Parameter <i>param</i> is not a known keyword (e.g. not a valid <i>amanda.conf</i> keyword).</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5), <code><a href="/docs/linux/man/5-amanda-client-conf/">amanda-client.conf</a></code>(5) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Author</h2>
<p><code>Jean-Louis Martineau</code> &lt;martineau [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>

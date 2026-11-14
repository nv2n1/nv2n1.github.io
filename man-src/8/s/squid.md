---
title: "squid(8)"
name: "squid"
section: "8"
letter: "s"
url: "/docs/linux/man/8-squid/"
description: "squid – HTTP web proxy caching server"
---

<p>squid &#8211; HTTP web proxy caching server</p>
<h2>Synopsis</h2>
<p><code>squid</code> <code>[-dhisrvzCFNRSVYX]</code> <code>[-l</code> facility <code>] [-f</code> config-file <code>] [-[au]</code> port <code>] [-k</code> signal <code>] [-n</code> service-name <code>] [-O</code> command-line <code>]</code></p>
<h2>Description</h2>
<p><code>squid</code> is a high-performance proxy caching server for web clients, supporting FTP, gopher, ICAP, ICP, HTCP and HTTP data objects. Unlike traditional caching software, Squid handles all requests in a single, non-blocking process. </p>
<p> Squid keeps meta data and especially hot objects cached in RAM, caches DNS lookups, supports non-blocking DNS lookups, and implements negative caching of failed requests. </p>
<p> Squid supports SSL, extensive access controls, and full request logging. By using the lightweight Internet Cache Protocols ICP, HTCP or CARP, Squid caches can be arranged in a hierarchy or mesh for additional bandwidth savings. </p>
<p> Squid consists of a main server program <code>squid</code> , some optional programs for custom processing and authentication, and some management and client tools. When squid starts up, it spawns a configurable number of helper processes, each of which can perform parallel lookups. This reduces the amount of time the cache waits for results. </p>
<p> Squid is derived from the ARPA-funded Harvest Project. </p>
<p> This manual page only lists the command line arguments. For details on how to configure Squid see the file <code>/etc/squid/squid.conf.documented,</code> the Squid wiki FAQ and examples at <a rel="nofollow" href="http://wiki.squid-cache.org/">http://wiki.squid-cache.org/</a> , or the configuration manual on the Squid home page <a rel="nofollow" href="http://www.squid-cache.org/Doc/config/">http://www.squid-cache.org/Doc/config/</a></p>
<h2>Options</h2>
<dl>
<dt><code>-a port</code></p>
<dd>Specify HTTP port number where Squid should listen for requests, in addition to any <code>http_port</code> specifications in <code>squid.conf</code></p>
<dt><code>-C</code></p>
<dd>Do not catch fatal signals.</p>
<dt><code>-d level</code></p>
<dd>Write debugging to stderr also.</p>
<dt><code>-f file</code></p>
<dd>Use the given config-file instead of <code>/etc/squid/squid.conf .</code> If the file name starts with a <code>!</code> or <code>|</code> then it is assumed to be an external command or command line. Can for example be used to pre-process the configuration before it is being read by Squid. To facilitate this Squid also understands the common #line notion to indicate the real source file.</p>
<dt><code>-F</code></p>
<dd>Don&#8217;t serve any requests until store is rebuilt.</p>
<dt><code>-h</code></p>
<dd>Print help message.</p>
<dt><code>-i</code></p>
<dd>Install as a Windows Service (see <code>-n</code> option).</p>
<dt><code>-k reconfigure | rotate | shutdown | interrupt | kill | debug | check | parse</code></p>
<dd>Parse configuration file, then send signal to running copy (except <code>-k parse</code> ) and exit.</p>
<dt><code>-l facility</code></p>
<dd>Use specified syslog facility. Implies <code>-s</code></p>
<dt><code>-n name</code></p>
<dd>Specify Windows Service name to use for service operations, default is: <code>Squid</code></p>
<dt><code>-N</code></p>
<dd>No daemon mode.</p>
<dt><code>-O options</code></p>
<dd>Set Windows Service Command line options in Registry.</p>
<dt><code>-r</code></p>
<dd>Remove a Windows Service (see <code>-n</code> option).</p>
<dt><code>-R</code></p>
<dd>Do not set <code>REUSEADDR</code> on port.</p>
<dt><code>-s</code></p>
<dd>Enable logging to syslog. Also configurable in <code>/etc/squid/squid.conf</code></p>
<dt><code>-S</code></p>
<dd>Double-check swap during rebuild.</p>
<dt><code>-u port</code></p>
<dd>Specify ICP port number (default: 3130), disable with 0.</p>
<dt><code>-v</code></p>
<dd>Print version and build details.</p>
<dt><code>-X</code></p>
<dd>Force full debugging.</p>
<dt><code>-Y</code></p>
<dd>Only return <code>UDP_HIT</code> or <code>UDP_MISS_NOFETCH</code> during fast reload.</p>
<dt><code>-z</code></p>
<dd>Create missing swap directories and other missing cache_dir structures, then exit. All cache_dir types create the configured top-level directory if it is missing. Other actions are type-specific. For example, ufs-based storage systems create missing L1 and L2 directories while Rock creates the missing database file.</p>
<dd>This option does not enable validation of any present swap structures. Its focus is on creation of missing pieces. If nothing is missing, squid -z just exits. If you suspect cache_dir corruption, you must delete the top-level cache_dir directory before running squid -z.</p>
<dd>By default, squid -z runs in daemon mode (so that configuration macros and other SMP features work as expected). Use <code>-N</code> option to overwrite this.</dl>
<h2>Files</h2>
<p>Squid configuration files located in /etc/squid/:</p>
<dl>
<dt>squid.conf</p>
<dd>The main configuration file. You must initially make changes to this file for <code>squid</code> to work. For example, the default configuration only allows access from RFC private LAN networks. Some packaging distributions block even that.</p>
<dt>squid.conf.default</p>
<dd>Reference copy of the configuration file. Always kept up to date with the version of Squid you are using.</p>
<dd>Use this to look up the default configuration settings and syntax after upgrading.</p>
<dt>squid.conf.documented</p>
<dd>Reference copy of the configuration file. Always kept up to date with the version of Squid you are using.</p>
<dd>Use this to read the documentation for configuration options available in your build of Squid. The online configuration manual is also available for a full reference of options. <code>see</code><a rel="nofollow" href="http://www.squid-cache.org/Doc/config/">http://www.squid-cache.org/Doc/config/</a></p>
<dt>cachemgr.conf</p>
<dd>The main configuration file for the web <code>cachemgr.cgi</code> tools.</p>
<dt>msntauth.conf</p>
<dd>The main configuration file for the Sample MSNT authenticator.</p>
<dt>errorpage.css</p>
<dd>CSS Stylesheet to control the display of generated error pages. Use this to set any company branding you need, it will apply to every language Squid provides error pages for.</dl>
<p> Some files also located elsewhere:</p>
<dl>
<dt>/etc/squid/mime.conf (mime_table)</p>
<dd>MIME type mappings for FTP gatewaying</p>
<dt>/usr/share/squid/errors</p>
<dd>Location of Squid error pages and templates.</dl>
<h2>Author</h2>
<p>Squid was written over many years by a changing team of developers and maintained in turn by <i>Duane Wessels &lt;duane [at] squid-cache.org&gt;</i> <i>Henrik Nordstrom &lt;hno [at] squid-cache.org&gt;</i> <i>Amos Jeffries &lt;amosjeffries [at] squid-cache.org&gt;</i> </p>
<p> With contributions from many others in the Squid community. see CONTRIBUTORS for a full list of individuals who contributed code. see CREDITS for a list of major code contributing copyright holders.</p>
<h2>Copyright</h2>
<p>&nbsp;<wbr>*&nbsp;<wbr>Copyright&nbsp;<wbr>(C)&nbsp;<wbr>1996-2016 The Squid Software Foundation and contributors<br />
&nbsp;<wbr>*<br />
&nbsp;<wbr>*&nbsp;<wbr>Squid software is distributed under GPLv2+&nbsp;<wbr>license and includes<br />
&nbsp;<wbr>*&nbsp;<wbr>contributions from numerous individuals and organizations.<br />
&nbsp;<wbr>*&nbsp;<wbr>Please see the COPYING and CONTRIBUTORS files for details.</p>
<h2>Questions</h2>
<p>Questions on the usage of this program can be sent to the <i>Squid Users mailing list</i> &lt;squid-users [at] squid-cache.org&gt;</p>
<h2>Reporting Bugs</h2>
<p>Bug reports need to be made in English. See <a rel="nofollow" href="http://wiki.squid-cache.org/SquidFaq/BugReporting">http://wiki.squid-cache.org/SquidFaq/BugReporting</a> for details of what you need to include with your bug report. </p>
<p> Report bugs or bug fixes using <a rel="nofollow" href="http://bugs.squid-cache.org/">http://bugs.squid-cache.org/</a> </p>
<p> Report serious security bugs to <i>Squid Bugs &lt;squid-bugs [at] squid-cache.org&gt;</i> </p>
<p> Report ideas for new improvements to the <i>Squid Developers mailing list</i> &lt;squid-dev [at] squid-cache.org&gt;</p>
<h2>See Also</h2>
<p><code>cachemgr.cgi (8), </code> <code>squidclient (1), </code> <code>pam_auth (8), </code> <code>squid_ldap_auth (8), </code> <code>squid_ldap_group (8), </code> <code>ext_session_acl (8), </code> <code>squid_unix_group (8), </code><br />
 The Squid FAQ wiki <a rel="nofollow" href="http://wiki.squid-cache.org/SquidFaq">http://wiki.squid-cache.org/SquidFaq</a><br />
 The Squid Configuration Manual <a rel="nofollow" href="http://www.squid-cache.org/Doc/config/">http://www.squid-cache.org/Doc/config/</a> </p>

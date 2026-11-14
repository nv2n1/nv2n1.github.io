---
title: "boa(8)"
name: "boa"
section: "8"
letter: "b"
url: "/docs/linux/man/8-boa/"
description: "boa – a single-tasking high performance http server"
---

<p><code>boa &#8211; a single-tasking high performance http server</code></p>
<h2>Synopsis</h2>
<p><code>boa</code> [<code>-c</code> <i>server_root</i>] [<code>-r</code> <i>chroot</i>] [<code>-d</code>]</p>
<h2>Description</h2>
<p>Boa is a single-tasking HTTP server. That means that unlike traditional web servers, it does not fork for each incoming connection, nor does it fork many copies of itself to handle multiple connections. It internally multiplexes all of the ongoing HTTP connections, and forks only for CGI programs (which must be separate processes.) Preliminary tests show Boa is more than twice as fast as Apache. </p>
<p> The primary design goals of Boa are speed and security. Security, in the sense of &quot;can&#8217;t be subverted by a malicious user&quot;, not &quot;fine grained access control and encrypted communications&quot;. Boa is not intended as a feature-packed server; if you want one of those, check out WN from John Franks. Modifications to Boa that improve its speed, security, robustness, and portability, are eagerly sought. Other features may be added if they can be achieved without hurting the primary goals.</p>
<h2>Options</h2>
<dl>
<dt><code>-d</code></p>
<dd>instruct Boa not to fork itself (non-daemonize). </p>
<dt><code>-c </code><i>server_root</i></p>
<dd>choose a server root overriding the default SERVER_ROOT #define in <i>defines.h</i> </p>
<p> The server root must hold your local copy of the configuration file </p>
<dt><code>-r </code><i>chroot</i></p>
<dd>instruct Boa where to chdir and chroot to. The chdir/chroot is done before the configuration file is read, or any log files are opened. </p>
</dl>
<h2>Files</h2>
<dl>
<dt><code>boa.conf</code> &#8211; the sole configuration file for Boa.</p>
<dd>The directives in this file are defined in the <code>DIRECTIVES</code> section. </p>
<dt><code>mime.types</code> &#8211; the</p>
<dd>MimeTypes &lt;filename&gt; defines what Content-Type Boa will send in an HTTP/1.0 or better transaction.</dl>
<h2>Directives</h2>
<p>The Boa configuration file is parsed with a lex/yacc or flex/bison generated parser. If it reports an error, the line number will be provided; it should be easy to spot. The syntax of each of these rules is very simple, and they can occur in any order. Where possible, these directives mimic those of NCSA httpd 1.3; We saw no reason to introduce gratuitous differences. </p>
<p> Note: the &quot;ServerRoot&quot; is not in this configuration file. It can be compiled into the server (see <i>defines.h</i> ) or specified on the command line with the <code>-c </code> option. </p>
<p> The following directives are contained in the <i>boa.conf</i> file, and most, but not all, are required.</p>
<dl>
<dt>Port &lt;integer&gt;</p>
<dd>This is the port that Boa runs on. The default port for http servers is 80. If it is less than 1024, the server must be started as root.</p>
<dt>User &lt;user name or UID&gt;</p>
<dd>The name or UID the server should run as. For Boa to attempt this, the server must be started as root.</p>
<dt>Group &lt;group name or GID&gt;</p>
<dd>The group name or GID the server should run as. For Boa to attempt this, the server must be started as root.</p>
<dt>ServerAdmin &lt;email address&gt;</p>
<dd>The email address where server problems should be sent. Note: this is not currently used.</p>
<dt>PidFile &lt;filename&gt;</p>
<dd>Where to put the pid of the process. Comment out to write no pid file. Note: Because Boa drops privileges at startup, and the pid file is written by the UID/GID before doing so, Boa does not attempt removal of the pid file.</p>
<dt>ErrorLog &lt;filename&gt;</p>
<dd>The location of the error log file. If this does not start with /, it is considered relative to the server root. Set to /dev/null if you don&#8217;t want errors logged.</p>
<dt>AccessLog &lt;filename&gt;</p>
<dd>The location of the access log file. If this does not start with /, it is considered relative to the server root. Comment out or set to /dev/null (less effective) to disable access logging.</p>
<dt>VerboseCGILogs</p>
<dd>This is a logical switch and does not take any parameters. Comment out to disable.</p>
<dt>CGILog &lt;filename&gt;</p>
<dd>The location of the CGI error log file. If this does not start with /, it is considered relative to the server root. If specified, this is the file that the stderr of CGIs is tied to, *instead* of to the ErrorLog.</p>
<dt>CGIumask &lt;umask&gt;</p>
<dd>The CGIumask is set immediately before execution of the CGI. The default value is 027. The number must be interpretable unambiguously by the C function strtol. No base is specified, so one may use a hexadecimal, decimal, or octal number if it is prefixed accordingly.</p>
<dt>ServerName &lt;server_name&gt;</p>
<dd>The name of this server that should be sent back to clients if different than that returned by gethostname.</p>
<dt>VirtualHost</p>
<dd>This is a logical switch and does not take any parameters. Comment out to disable. Given DocumentRoot /var/www, requests on interface &#8216;A&#8217; or IP &#8216;IP-A&#8217; become /var/www/IP-A. Example: <a rel="nofollow" href="http://localhost/">http://localhost/</a> becomes /var/www/127.0.0.1</p>
<dt>VHostRoot &lt;directory&gt;</p>
<dd>The root location for all virtually hosted data Comment out to disable. Incompatible with &#8216;Virtualhost&#8217; and &#8216;DocumentRoot&#8217;!! Given VHostRoot /var/www, requests to host foo.bar.com, where foo.bar.com is ip a.b.c.d, become /var/www/a.b.c.d/foo.bar.com Hostnames are &quot;cleaned&quot;, and must conform to the rules specified in rfc1034, which are be summarized here: </p>
<p> Hostnames must start with a letter, end with a letter or digit, and have as interior characters only letters, digits, and hyphen. Hostnames must not exceed 63 characters in length.</p>
<dt>DefaultVHost &lt;hostname&gt;</p>
<dd>Define this in order to have a default hostname when the client does not specify one, if using VirtualHostName. If not specified, the word &quot;default&quot; will be used for compatibility with older clients.</p>
<dt>DocumentRoot &lt;directory&gt;</p>
<dd>The root directory of the HTML documents. If this does not start with /, it is considered relative to the server root.</p>
<dt>UserDir &lt;directory&gt;</p>
<dd>The name of the directory which is appended onto a user&#8217;s home directory if a ~user request is received.</p>
<dt>DirectoryIndex &lt;filename&gt;</p>
<dd>Name of the file to use as a pre-written HTML directory index. Please make and use these files. On the fly creation of directory indexes can be slow.</p>
<dt>DirectoryMaker &lt;directory&gt;</p>
<dd>Name of the program used to generate on-the-fly directory listings. The program must take one or two command-line arguments, the first being the directory to index (absolute), and the second, which is optional, contains what Boa would have the &quot;title&quot; of the document be. Comment out if you don&#8217;t want on the fly directory listings. If this does not start with /, it is considered relative to the server root.</p>
<dt>KeepAliveMax &lt;integer&gt;</p>
<dd>Number of KeepAlive requests to allow per connection. Comment out, or set to 0 to disable keepalive processing.</p>
<dt>KeepAliveTimeout &lt;integer&gt;</p>
<dd>Number of seconds to wait before keepalive connections time out.</p>
<dt>MimeTypes &lt;file&gt;</p>
<dd>The location of the <i>mime.types</i> file. If this does not start with /, it is considered relative to the server root. Set to /dev/null if you do not want to load a mime types file. Do *not* comment out (better use AddType!)</p>
<dt>DefaultType &lt;mime type&gt;</p>
<dd>MIME type used if the file extension is unknown, or there is no file extension.</p>
<dt>AddType &lt;mime type&gt; &lt;extension&gt; [extension&#8230;]</p>
<dd>Associates a MIME type with an extension or extensions.</p>
<dt>Redirect, Alias, and ScriptAlias &lt;path1&gt; &lt;path2&gt;</p>
<dd>Redirect, Alias, and ScriptAlias all have the same semantics &#8212; they match the beginning of a request and take appropriate action. Use Redirect for other servers, Alias for the same server, and ScriptAlias to enable directories for script execution. </p>
<p> Redirect allows you to tell clients about documents which used to exist in your server&#8217;s namespace, but do not anymore. This allows you tell the clients where to look for the relocated document. </p>
<p> Alias aliases one path to another. Of course, symbolic links in the file system work fine too. </p>
<p> ScriptAlias maps a virtual path to a directory for serving scripts.</dl>
<p> Please see the included <i>boa.conf </i> for defaults and examples.</p>
<h2>History</h2>
<p>Like the Linux kernel, even numbered versions are &quot;stable&quot;, and odd numbered versions are &quot;unstable&quot;, or rather, &quot;development&quot;. Versions 0.91 and 0.91beta of Boa were released by Paul Phillips &lt;paulp [at] go2net.com&gt; </p>
<p> Version 0.92 was released by Larry Doolittle on December 12, 1996. </p>
<p> Version 0.93 was the development version of 0.94. </p>
<p> Version 0.94 was released 22 Jan 2000.</p>
<h2>Bugs</h2>
<p>There are probably bugs, but we are not aware of any at this time.</p>
<h2>Author</h2>
<p>Boa was created by Paul Phillips &lt;paulp [at] go2net.com&gt;. It is now being maintained and enhanced by Larry Doolittle &lt;ldoolitt [at] boa.org&gt; and Jon Nelson &lt;jnelson [at] boa.org&gt;. </p>
<p> Linux is the development platform at the moment, other OS&#8217;s are known to work. If you&#8217;d like to contribute to this effort, contact Larry or Jon via e-mail.</p>
<h2>License</h2>
<p>This program is distributed under the GNU General Public License, as noted in each source file.</p>

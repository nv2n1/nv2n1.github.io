---
title: "cups-files-conf(5)"
name: "cups-files-conf"
section: "5"
letter: "c"
url: "/docs/linux/man/5-cups-files-conf/"
description: "cups-files.conf – file and directory configuration file for cups"
---

<p>cups-files.conf &#8211; file and directory configuration file for cups</p>
<h2>Description</h2>
<p>The <code>cups-files.conf</code> file configures the files and directories used by the CUPS scheduler, <code><a href="/docs/linux/man/8-cupsd/">cupsd</a></code>(8). It is normally located in the <i>/etc/cups</i> directory. </p>
<p> Each line in the file can be a configuration directive, a blank line, or a comment. Configuration directives typically consist of a name and zero or more values separated by whitespace. The configuration directive name and values are case-insensitive. Comment lines start with the # character.</p>
<h3>Directives</h3>
<p>The following directives are understood by <code><a href="/docs/linux/man/8-cupsd/">cupsd</a></code>(8):</p>
<dl>
<dt><code>AccessLog</code></p>
<dd>
<dt><code>AccessLog </code><i>filename</i></p>
<dd>
<dt><code>AccessLog stderr</code></p>
<dd>
<dt><code>AccessLog syslog</code></p>
<dd>Defines the access log filename. Specifying a blank filename disables access log generation. The value &quot;stderr&quot; causes log entries to be sent to the standard error file when the scheduler is running in the foreground, or to the system log daemon when run in the background. The value &quot;syslog&quot; causes log entries to be sent to the system log daemon. The server name may be included in filenames using the string &quot;%s&quot;, for example: </p>
<pre> AccessLog /var/log/cups/%s-access_log</pre>
<p>The default is &quot;/var/log/cups/access_log&quot;.</p>
<dt><code>CacheDir </code><i>directory</i></p>
<dd>Specifies the directory to use for long-lived temporary (cache) files. The default is &quot;/var/spool/cups/cache&quot; or &quot;/var/cache/cups&quot; depending on the platform.</p>
<dt><code>ConfigFilePerm </code><i>mode</i></p>
<dd>Specifies the permissions for all configuration files that the scheduler writes. The default is &quot;0644&quot; on macOS and &quot;0640&quot; on all other operating systems.</dl>
<p> <code>Note:</code> The permissions for the <i>printers.conf</i> file are currently masked to only allow access from the scheduler user (typically root). This is done because printer device URIs sometimes contain sensitive authentication information that should not be generally known on the system. There is no way to disable this security feature.</p>
<dl>
<dt><code>CreateSelfSignedCerts yes</code></p>
<dd>
<dt><code>CreateSelfSignedCerts no</code></p>
<dd>Specifies whether the scheduler automatically creates self-signed certificates for client connections using TLS. The default is yes.</p>
<dt><code>DataDir </code><i>path</i></p>
<dd>Specifies the directory where data files can be found. The default is usually &quot;/usr/share/cups&quot;.</p>
<dt><code>DocumentRoot </code><i>directory</i></p>
<dd>Specifies the root directory for the CUPS web interface content. The default is usually &quot;/usr/share/doc/cups&quot;.</p>
<dt><code>ErrorLog</code></p>
<dd>
<dt><code>ErrorLog </code><i>filename</i></p>
<dd>
<dt><code>ErrorLog stderr</code></p>
<dd>
<dt><code>ErrorLog syslog</code></p>
<dd>Defines the error log filename. Specifying a blank filename disables error log generation. The value &quot;stderr&quot; causes log entries to be sent to the standard error file when the scheduler is running in the foreground, or to the system log daemon when run in the background. The value &quot;syslog&quot; causes log entries to be sent to the system log daemon. The server name may be included in filenames using the string &quot;%s&quot;, for example: </p>
<pre> ErrorLog /var/log/cups/%s-error_log</pre>
<p>The default is &quot;/var/log/cups/error_log&quot;.</p>
<dt><code>FatalErrors none</code></p>
<dd>
<dt><code>FatalErrors all </code><i>-kind </i>[ &#8230; <i>-kind </i>]</p>
<dd>
<dt><code>FatalErrors </code><i>kind </i>[ &#8230; <i>kind </i>]</p>
<dd>Specifies which errors are fatal, causing the scheduler to exit. The default is &quot;config&quot;. The <i>kind</i> strings are:</p>
<dl>
<dd>
<dl>
<dt><code>none</code></p>
<dd>No errors are fatal.</p>
<dt><code>all</code></p>
<dd>All of the errors below are fatal.</p>
<dt><code>browse</code></p>
<dd>Browsing initialization errors are fatal, for example failed connections to the DNS-SD daemon.</p>
<dt><code>config</code></p>
<dd>Configuration file syntax errors are fatal.</p>
<dt><code>listen</code></p>
<dd>Listen or Port errors are fatal, except for IPv6 failures on the loopback or &quot;any&quot; addresses.</p>
<dt><code>log</code></p>
<dd>Log file creation or write errors are fatal.</p>
<dt><code>permissions</code></p>
<dd>Bad startup file permissions are fatal, for example shared TLS certificate and key files with world-read permissions.</dl>
</dl>
<dt><code>Group </code><i>group-name-or-number</i></p>
<dd>Specifies the group name or ID that will be used when executing external programs. The default group is operating system specific but is usually &quot;lp&quot; or &quot;nobody&quot;.</p>
<dt><code>LogFileGroup </code><i>group-name-or-number</i></p>
<dd>Specifies the group name or ID that will be used for log files. The default group is operating system specific but is usually &quot;lp&quot; or &quot;nobody&quot;.</p>
<dt><code>LogFilePerm </code><i>mode</i></p>
<dd>Specifies the permissions of all log files that the scheduler writes. The default is &quot;0644&quot;.</p>
<dt><code>PageLog </code>[ <i>filename</i> ]</p>
<dd>
<dt><code>PageLog stderr</code></p>
<dd>
<dt><code>PageLog syslog</code></p>
<dd>Defines the page log filename. The value &quot;stderr&quot; causes log entries to be sent to the standard error file when the scheduler is running in the foreground, or to the system log daemon when run in the background. The value &quot;syslog&quot; causes log entries to be sent to the system log daemon. Specifying a blank filename disables page log generation. The server name may be included in filenames using the string &quot;%s&quot;, for example: </p>
<pre> PageLog /var/log/cups/%s-page_log</pre>
<p>The default is &quot;/var/log/cups/page_log&quot;.</p>
<dt><code>PassEnv </code><i>variable </i>[ &#8230; <i>variable </i>]</p>
<dd>Passes the specified environment variable(s) to child processes. Note: the standard CUPS filter and backend environment variables cannot be overridden using this directive.</p>
<dt><code>RemoteRoot </code><i>username</i></p>
<dd>Specifies the username that is associated with unauthenticated accesses by clients claiming to be the root user. The default is &quot;remroot&quot;.</p>
<dt><code>RequestRoot </code><i>directory</i></p>
<dd>Specifies the directory that contains print jobs and other HTTP request data. The default is &quot;/var/spool/cups&quot;.</p>
<dt><code>Sandboxing relaxed</code></p>
<dd>
<dt><code>Sandboxing strict</code></p>
<dd>Specifies the level of security sandboxing that is applied to print filters, backends, and other child processes of the scheduler. The default is &quot;strict&quot;. This directive is currently only used/supported on macOS.</p>
<dt><code>ServerBin </code><i>directory</i></p>
<dd>Specifies the directory containing the backends, CGI programs, filters, helper programs, notifiers, and port monitors. The default is &quot;/usr/lib/cups&quot; or &quot;/usr/libexec/cups&quot; depending on the platform.</p>
<dt><code>ServerKeychain </code><i>path</i></p>
<dd>Specifies the location of TLS certificates and private keys. The default is &quot;/Library/Keychains/System.keychain&quot; on macOS and &quot;/etc/cups/ssl&quot; on all other operating systems. macOS uses its keychain database to store certificates and keys while other platforms use separate files in the specified directory, *.crt for PEM-encoded certificates and *.key for PEM-encoded private keys.</p>
<dt><code>ServerRoot </code><i>directory</i></p>
<dd>Specifies the directory containing the server configuration files. The default is &quot;/etc/cups&quot;.</p>
<dt><code>SetEnv </code><i>variable value</i></p>
<dd>Set the specified environment variable to be passed to child processes. Note: the standard CUPS filter and backend environment variables cannot be overridden using this directive.</p>
<dt><code>StateDir </code><i>directory</i></p>
<dd>Specifies the directory to use for PID and local certificate files. The default is &quot;/var/run/cups&quot; or &quot;/etc/cups&quot; depending on the platform.</p>
<dt><code>SyncOnClose Yes</code></p>
<dd>
<dt><code>SyncOnClose No</code></p>
<dd>Specifies whether the scheduler calls <code><a href="/docs/linux/man/2-fsync/">fsync</a></code>(2) after writing configuration or state files.</p>
<dt><code>SystemGroup </code><i>group-name </i>[ &#8230; <i>group-name</i> ]</p>
<dd>Specifies the group(s) to use for <i>@SYSTEM</i> group authentication. The default contains &quot;admin&quot;, &quot;lpadmin&quot;, &quot;root&quot;, &quot;sys&quot;, and/or &quot;system&quot;.</p>
<dt><code>TempDir </code><i>directory</i></p>
<dd>Specifies the directory where short-term temporary files are stored. The default is &quot;/var/spool/cups/tmp&quot;.</p>
<dt><code>User </code><i>username</i></p>
<dd>Specifies the user name or ID that is used when running external programs. The default is &quot;lp&quot;.</dl>
<h3>Deprecated Directives</h3>
<p>The following directives are deprecated and will be removed from a future version of CUPS:</p>
<dl>
<dt><code>FileDevice Yes</code></p>
<dd>
<dt><code>FileDevice No</code></p>
<dd>Specifies whether the file pseudo-device can be used for new printer queues. The URI &quot;file:///dev/null&quot; is always allowed. File devices cannot be used with &quot;raw&quot; print queues &#8211; a PPD file is required. The specified file is overwritten for every print job. Writing to directories is not supported.</p>
<dt><code>Printcap </code><i>filename</i></p>
<dd>Specifies a file that is filled with a list of local print queues.</p>
<dt><code>PrintcapFormat bsd</code></p>
<dd>
<dt><code>PrintcapFormat plist</code></p>
<dd>
<dt><code>PrintcapFormat solaris</code></p>
<dd>Specifies the format to use for the Printcap file. &quot;bsd&quot; is the historical LPD printcap file format. &quot;plist&quot; is the Apple plist file format. &quot;solaris&quot; is the historical Solaris LPD printcap file format.</dl>
<h2>Notes</h2>
<p>The scheduler MUST be restarted manually after making changes to the <code>cups-files.conf</code> file. On Linux this is typically done using the <code><a href="/docs/linux/man/8-systemctl/">systemctl</a></code>(8) command, while on macOS the <code><a href="/docs/linux/man/8-launchctl/">launchctl</a></code>(8) command is used instead.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-classes-conf/">classes.conf</a></code>(5), <code><a href="/docs/linux/man/1-cups/">cups</a></code>(1), <code><a href="/docs/linux/man/8-cupsd/">cupsd</a></code>(8), <code><a href="/docs/linux/man/5-cupsd-conf/">cupsd.conf</a></code>(5), <code><a href="/docs/linux/man/5-mime-convs/">mime.convs</a></code>(5), <code><a href="/docs/linux/man/5-mime-types/">mime.types</a></code>(5), <code><a href="/docs/linux/man/5-printers-conf/">printers.conf</a></code>(5), <code><a href="/docs/linux/man/5-subscriptions-conf/">subscriptions.conf</a></code>(5), CUPS Online Help (<a rel="nofollow" href="http://localhost:631/help)">http://localhost:631/help)</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2020-2022 by OpenPrinting.</p>

---
title: "cupsd(5)"
name: "cupsd"
section: "5"
letter: "c"
url: "/docs/linux/man/5-cupsd/"
description: "cupsd.conf – server configuration file for cups"
---

<p>cupsd.conf &#8211; server configuration file for cups</p>
<h2>Description</h2>
<p>The <i>cupsd.conf</i> file configures the CUPS scheduler, <i><a href="/docs/linux/man/8-cupsd/">cupsd</a>(8)</i>. It is normally located in the <i>/etc/cups</i> directory. <code>Note:</code> File, directory, and user configuration directives that used to be allowed in the <i>cupsd.conf</i> file are now stored in the <i><a href="/docs/linux/man/5-cups-files-conf/">cups-files.conf</a>(5)</i> instead in order to prevent certain types of privilege escalation attacks. </p>
<p> Each line in the file can be a configuration directive, a blank line, or a comment. Comment lines start with the # character. The configuration directives are intentionally similar to those used by the popular Apache web server software and are described below.</p>
<h2>Directives</h2>
<p>The following directives are understood by <i><a href="/docs/linux/man/8-cupsd/">cupsd</a>(8)</i>. Consult the on-line help for detailed descriptions:</p>
<dl>
<dt>AccessLogLevel config</dt>
<dd>
</dd><dt>AccessLogLevel actions</dt>
<dd>
</dd><dt>AccessLogLevel all</dt>
<dd>Specifies the logging level for the AccessLog file.</dd>
<dt>Allow all</dt>
<dd>
</dd><dt>Allow none</dt>
<dd>
</dd><dt>Allow host.domain.com</dt>
<dd>
</dd><dt>Allow *.domain.com</dt>
<dd>
</dd><dt>Allow ip-address</dt>
<dd>
</dd><dt>Allow ip-address/netmask</dt>
<dd>
</dd><dt>Allow ip-address/mm</dt>
<dd>
</dd><dt>Allow @IF(name)</dt>
<dd>
</dd><dt>Allow @LOCAL</dt>
<dd>Allows access from the named hosts or addresses.</dd>
<dt>AuthType None</dt>
<dd>
</dd><dt>AuthType Basic</dt>
<dd>
</dd><dt>AuthType BasicDigest</dt>
<dd>
</dd><dt>AuthType Digest</dt>
<dd>
</dd><dt>AuthType Negotiate</dt>
<dd>Specifies the authentication type (None, Basic, BasicDigest, Digest, Negotiate)</dd>
<dt>AutoPurgeJobs Yes</dt>
<dd>
</dd><dt>AutoPurgeJobs No</dt>
<dd>Specifies whether to purge job history data automatically when it is no longer required for quotas.</dd>
<dt>BrowseLocalProtocols [All] [DNSSD]</dt>
<dd>Specifies the protocols to use for local printer sharing.</dd>
<dt>BrowseWebIF Yes</dt>
<dd>
</dd><dt>BrowseWebIF No</dt>
<dd>Specifies whether the CUPS web interface is advertised via DNS-SD.</dd>
<dt>Browsing Yes</dt>
<dd>
</dd><dt>Browsing No</dt>
<dd>Specifies whether or not shared printers should be advertised.</dd>
<dt>Classification banner</dt>
<dd>Specifies the security classification of the server.</dd>
<dt>ClassifyOverride Yes</dt>
<dd>
</dd><dt>ClassifyOverride No</dt>
<dd>Specifies whether to allow users to override the classification of individual print jobs.</dd>
<dt>DefaultAuthType Basic</dt>
<dd>
</dd><dt>DefaultAuthType BasicDigest</dt>
<dd>
</dd><dt>DefaultAuthType Digest</dt>
<dd>
</dd><dt>DefaultAuthType Negotiate</dt>
<dd>Specifies the default type of authentication to use.</dd>
<dt>DefaultEncryption Never</dt>
<dd>
</dd><dt>DefaultEncryption IfRequested</dt>
<dd>
</dd><dt>DefaultEncryption Required</dt>
<dd>Specifies the type of encryption to use for authenticated requests.</dd>
<dt>DefaultLanguage locale</dt>
<dd>Specifies the default language to use for text and web content.</dd>
<dt>DefaultPaperSize Auto</dt>
<dd>
</dd><dt>DefaultPaperSize None</dt>
<dd>
</dd><dt>DefaultPaperSize sizename</dt>
<dd>Specifies the default paper size for new print queues. &quot;Auto&quot; uses a locale- specific default, while &quot;None&quot; specifies there is no default paper size.</dd>
<dt>DefaultPolicy policy-name</dt>
<dd>Specifies the default access policy to use.</dd>
<dt>DefaultShared Yes</dt>
<dd>
</dd><dt>DefaultShared No</dt>
<dd>Specifies whether local printers are shared by default.</dd>
<dt>Deny all</dt>
<dd>
</dd><dt>Deny none</dt>
<dd>
</dd><dt>Deny host.domain.com</dt>
<dd>
</dd><dt>Deny *.domain.com</dt>
<dd>
</dd><dt>Deny ip-address</dt>
<dd>
</dd><dt>Deny ip-address/netmask</dt>
<dd>
</dd><dt>Deny ip-address/mm</dt>
<dd>
</dd><dt>Deny @IF(name)</dt>
<dd>
</dd><dt>Deny @LOCAL</dt>
<dd>Denies access to the named host or address.</dd>
<dt>DirtyCleanInterval seconds</dt>
<dd>Specifies the delay for updating of configuration and state files. A value of 0 causes the update to happen as soon as possible, typically within a few milliseconds.</dd>
<dt>Encryption IfRequested</dt>
<dd>
</dd><dt>Encryption Never</dt>
<dd>
</dd><dt>Encryption Required</dt>
<dd>Specifies the level of encryption that is required for a particular location.</dd>
<dt>ErrorPolicy abort-job</dt>
<dd>Specifies that a failed print job should be aborted (discarded) unless otherwise specified for the printer.</dd>
<dt>ErrorPolicy retry-job</dt>
<dd>Specifies that a failed print job should be retried at a later time unless otherwise specified for the printer.</dd>
<dt>ErrorPolicy retry-this-job</dt>
<dd>Specifies that a failed print job should be retried immediately unless otherwise specified for the printer.</dd>
<dt>ErrorPolicy stop-printer</dt>
<dd>Specifies that a failed print job should stop the printer unless otherwise specified for the printer. The &#8216;stop-printer&#8217; error policy is the default.</dd>
<dt>FilterLimit limit</dt>
<dd>Specifies the maximum cost of filters that are run concurrently.</dd>
<dt>FilterNice nice-value</dt>
<dd>Specifies the scheduling priority (&quot;nice&quot; value) of filters that are run to print a job.</dd>
<dt>GSSServiceName name</dt>
<dd>Specifies the service name when using Kerberos authentication. The default service name is &quot;http&quot;.</dd>
<dt>HostNameLookups On</dt>
<dd>
</dd><dt>HostNameLookups Off</dt>
<dd>
</dd><dt>HostNameLookups Double</dt>
<dd>Specifies whether or not to do reverse lookups on client addresses.</dd>
<dt>Include filename</dt>
<dd>Includes the named file.</dd>
<dt>JobKillDelay seconds</dt>
<dd>Specifies the number of seconds to wait before killing the filters and backend associated with a canceled or held job.</dd>
<dt>JobPrivateAccess all</dt>
<dd>
</dd><dt>JobPrivateAccess default</dt>
<dd>
</dd><dt>JobPrivateAccess {user|@group|@ACL|@OWNER|@SYSTEM}+</dt>
<dd>Specifies an access list for a job&#8217;s private values. The &quot;default&quot; access list is &quot;@OWNER @SYSTEM&quot;. &quot;@ACL&quot; maps to the printer&#8217;s requesting-user-name-allowed or requesting-user-name-denied values.</dd>
<dt>JobPrivateValues all</dt>
<dd>
</dd><dt>JobPrivateValues default</dt>
<dd>
</dd><dt>JobPrivateValues none</dt>
<dd>
</dd><dt>JobPrivateValues attribute-name-1 [ &#8230; attribute-name-N ]</dt>
<dd>Specifies the list of job values to make private. The &quot;default&quot; values are &quot;job-name&quot;, &quot;job-originating-host-name&quot;, and &quot;job-originating-user-name&quot;.</dd>
<dt>JobRetryInterval seconds</dt>
<dd>Specifies the interval between retries of jobs in seconds.</dd>
<dt>JobRetryLimit count</dt>
<dd>Specifies the number of retries that are done for jobs.</dd>
<dt>KeepAlive Yes</dt>
<dd>
</dd><dt>KeepAlive No</dt>
<dd>Specifies whether to support HTTP keep-alive connections.</dd>
<dt>KeepAliveTimeout seconds</dt>
<dd>Specifies the amount of time that connections are kept alive.</dd>
<dt>&lt;Limit operations&gt; &#8230; &lt;/Limit&gt;</dt>
<dd>Specifies the IPP operations that are being limited inside a policy.</dd>
<dt>&lt;Limit methods&gt; &#8230; &lt;/Limit&gt;</dt>
<dd>
</dd><dt>&lt;LimitExcept methods&gt; &#8230; &lt;/LimitExcept&gt;</dt>
<dd>Specifies the HTTP methods that are being limited inside a location.</dd>
<dt>LimitRequestBody</dt>
<dd>Specifies the maximum size of any print job request.</dd>
<dt>Listen ip-address:port</dt>
<dd>
</dd><dt>Listen *:port</dt>
<dd>
</dd><dt>Listen /path/to/domain/socket</dt>
<dd>Listens to the specified address and port or domain socket path.</dd>
<dt>&lt;Location /path&gt; &#8230; &lt;/Location&gt;</dt>
<dd>Specifies access control for the named location.</dd>
<dt>LogDebugHistory #-messages</dt>
<dd>Specifies the number of debugging messages that are logged when an error occurs in a print job.</dd>
<dt>LogLevel alert</dt>
<dd>
</dd><dt>LogLevel crit</dt>
<dd>
</dd><dt>LogLevel debug2</dt>
<dd>
</dd><dt>LogLevel debug</dt>
<dd>
</dd><dt>LogLevel emerg</dt>
<dd>
</dd><dt>LogLevel error</dt>
<dd>
</dd><dt>LogLevel info</dt>
<dd>
</dd><dt>LogLevel none</dt>
<dd>
</dd><dt>LogLevel notice</dt>
<dd>
</dd><dt>LogLevel warn</dt>
<dd>Specifies the logging level for the ErrorLog file.</dd>
<dt>LogTimeFormat standard</dt>
<dd>
</dd><dt>LogTimeFormat usecs</dt>
<dd>Specifies the format of the date and time in the log files.</dd>
<dt>MaxClients number</dt>
<dd>Specifies the maximum number of simultaneous clients to support.</dd>
<dt>MaxClientsPerHost number</dt>
<dd>Specifies the maximum number of simultaneous clients to support from a single address.</dd>
<dt>MaxCopies number</dt>
<dd>Specifies the maximum number of copies that a user can print of each job.</dd>
<dt>MaxHoldTime seconds</dt>
<dd>Specifies the maximum time a job may remain in the &quot;indefinite&quot; hold state before it is canceled. Set to 0 to disable cancellation of held jobs.</dd>
<dt>MaxJobs number</dt>
<dd>Specifies the maximum number of simultaneous jobs to support.</dd>
<dt>MaxJobsPerPrinter number</dt>
<dd>Specifies the maximum number of simultaneous jobs per printer to support.</dd>
<dt>MaxJobsPerUser number</dt>
<dd>Specifies the maximum number of simultaneous jobs per user to support.</dd>
<dt>MaxJobTime seconds</dt>
<dd>Specifies the maximum time a job may take to print before it is canceled. The default is 10800 seconds (3 hours). Set to 0 to disable cancellation of &quot;stuck&quot; jobs.</dd>
<dt>MaxLogSize number-bytes</dt>
<dd>Specifies the maximum size of the log files before they are rotated (0 to disable rotation)</dd>
<dt>MaxRequestSize number-bytes</dt>
<dd>Specifies the maximum request/file size in bytes (0 for no limit)</dd>
<dt>MultipleOperationTimeout seconds</dt>
<dd>Specifies the maximum amount of time to allow between files in a multiple file print job.</dd>
<dt>Order allow,deny</dt>
<dd>
</dd><dt>Order deny,allow</dt>
<dd>Specifies the order of HTTP access control (allow,deny or deny,allow)</dd>
<dt>PageLogFormat format string</dt>
<dd>Specifies the format of page log lines.</dd>
<dt>PassEnv variable [&#8230; variable]</dt>
<dd>Passes the specified environment variable(s) to child processes.</dd>
<dt>&lt;Policy name&gt; &#8230; &lt;/Policy&gt;</dt>
<dd>Specifies access control for the named policy.</dd>
<dt>Port number</dt>
<dd>Specifies a port number to listen to for HTTP requests.</dd>
<dt>PreserveJobFiles Yes</dt>
<dd>
</dd><dt>PreserveJobFiles No</dt>
<dd>Specifies whether or not to preserve job files after they are printed.</dd>
<dt>PreserveJobHistory Yes</dt>
<dd>
</dd><dt>PreserveJobHistory No</dt>
<dd>Specifies whether or not to preserve the job history after they are printed.</dd>
<dt>PrintcapFormat bsd</dt>
<dd>
</dd><dt>PrintcapFormat plist</dt>
<dd>
</dd><dt>PrintcapFormat solaris</dt>
<dd>Specifies the format of the printcap file.</dd>
<dt>ReloadTimeout seconds</dt>
<dd>Specifies the amount of time to wait for job completion before restarting the scheduler.</dd>
<dt>Require group group-name-list</dt>
<dd>
</dd><dt>Require user user-name-list</dt>
<dd>
</dd><dt>Require valid-user</dt>
<dd>Specifies that user or group authentication is required.</dd>
<dt>RIPCache bytes</dt>
<dd>Specifies the maximum amount of memory to use when converting images and PostScript files to bitmaps for a printer.</dd>
<dt>Satisfy all</dt>
<dd>
</dd><dt>Satisfy any</dt>
<dd>Specifies whether all or any limits set for a Location must be satisfied to allow access.</dd>
<dt>ServerAdmin user [at] domain.com</dt>
<dd>Specifies the email address of the server administrator.</dd>
<dt>ServerAlias hostname [&#8230; hostname]</dt>
<dd>
</dd><dt>ServerAlias *</dt>
<dd>Specifies an alternate name that the server is known by. The special name &quot;*&quot; allows any name to be used.</dd>
<dt>ServerName hostname-or-ip-address</dt>
<dd>Specifies the fully-qualified hostname of the server.</dd>
<dt>ServerTokens Full</dt>
<dd>
</dd><dt>ServerTokens Major</dt>
<dd>
</dd><dt>ServerTokens Minimal</dt>
<dd>
</dd><dt>ServerTokens Minor</dt>
<dd>
</dd><dt>ServerTokens None</dt>
<dd>
</dd><dt>ServerTokens OS</dt>
<dd>
</dd><dt>ServerTokens ProductOnly</dt>
<dd>Specifies what information is included in the Server header of HTTP responses.</dd>
<dt>SetEnv variable value</dt>
<dd>Set the specified environment variable to be passed to child processes.</dd>
<dt>SSLListen</dt>
<dd>Listens on the specified address and port for encrypted connections.</dd>
<dt>SSLOptions None</dt>
<dd>
</dd><dt>SSLOptions NoEmptyFragments</dt>
<dd>Sets SSL/TLS protocol options for encrypted connections.</dd>
<dt>SSLPort</dt>
<dd>Listens on the specified port for encrypted connections.</dd>
<dt>StrictConformance Yes</dt>
<dd>
</dd><dt>StrictConformance No</dt>
<dd>Specifies whether the scheduler requires clients to strictly adhere to the IPP specifications. The default is No.</dd>
<dt>SubscriptionPrivateAccess all</dt>
<dd>
</dd><dt>SubscriptionPrivateAccess default</dt>
<dd>
</dd><dt>SubscriptionPrivateAccess {user|@group|@ACL|@OWNER|@SYSTEM}+</dt>
<dd>Specifies an access list for a subscription&#8217;s private values. The &quot;default&quot; access list is &quot;@OWNER @SYSTEM&quot;. &quot;@ACL&quot; maps to the printer&#8217;s requesting-user-name-allowed or requesting-user-name-denied values.</dd>
<dt>SubscriptionPrivateValues all</dt>
<dd>
</dd><dt>SubscriptionPrivateValues default</dt>
<dd>
</dd><dt>SubscriptionPrivateValues none</dt>
<dd>
</dd><dt>SubscriptionPrivateValues attribute-name-1 [ &#8230; attribute-name-N ]</dt>
<dd>Specifies the list of job values to make private. The &quot;default&quot; values are &quot;notify-events&quot;, &quot;notify-pull-method&quot;, &quot;notify-recipient-uri&quot;, &quot;notify-subscriber-user-name&quot;, and &quot;notify-user-data&quot;.</dd>
<dt>Timeout seconds</dt>
<dd>Specifies the HTTP request timeout in seconds.</dd>
<dt>WebInterface yes</dt>
<dd>
</dd><dt>WebInterface no</dt>
<dd>Specifies whether the web interface is enabled.</dd></dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-classes-conf/">classes.conf</a>(5)</i>, <i><a href="/docs/linux/man/5-cups-files-conf/">cups-files.conf</a>(5)</i>, <i><a href="/docs/linux/man/8-cupsd/">cupsd</a>(8)</i>, <i><a href="/docs/linux/man/5-mime-convs/">mime.convs</a>(5)</i>, <i><a href="/docs/linux/man/5-mime-types/">mime.types</a>(5)</i>, <i><a href="/docs/linux/man/5-printers-conf/">printers.conf</a>(5)</i>, <i><a href="/docs/linux/man/5-subscriptions-conf/">subscriptions.conf</a>(5)</i>,<br/>
 <a rel="nofollow" href="http://localhost:631/help">http://localhost:631/help</a></p>
<h2>Copyright</h2>
<p>Copyright 2007-2013 by Apple Inc.</p>

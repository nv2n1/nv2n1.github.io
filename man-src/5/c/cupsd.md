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
<dt>AccessLogLevel config</p>
<dd>
<dt>AccessLogLevel actions</p>
<dd>
<dt>AccessLogLevel all</p>
<dd>Specifies the logging level for the AccessLog file.</p>
<dt>Allow all</p>
<dd>
<dt>Allow none</p>
<dd>
<dt>Allow host.domain.com</p>
<dd>
<dt>Allow *.domain.com</p>
<dd>
<dt>Allow ip-address</p>
<dd>
<dt>Allow ip-address/netmask</p>
<dd>
<dt>Allow ip-address/mm</p>
<dd>
<dt>Allow @IF(name)</p>
<dd>
<dt>Allow @LOCAL</p>
<dd>Allows access from the named hosts or addresses.</p>
<dt>AuthType None</p>
<dd>
<dt>AuthType Basic</p>
<dd>
<dt>AuthType BasicDigest</p>
<dd>
<dt>AuthType Digest</p>
<dd>
<dt>AuthType Negotiate</p>
<dd>Specifies the authentication type (None, Basic, BasicDigest, Digest, Negotiate)</p>
<dt>AutoPurgeJobs Yes</p>
<dd>
<dt>AutoPurgeJobs No</p>
<dd>Specifies whether to purge job history data automatically when it is no longer required for quotas.</p>
<dt>BrowseLocalProtocols [All] [DNSSD]</p>
<dd>Specifies the protocols to use for local printer sharing.</p>
<dt>BrowseWebIF Yes</p>
<dd>
<dt>BrowseWebIF No</p>
<dd>Specifies whether the CUPS web interface is advertised via DNS-SD.</p>
<dt>Browsing Yes</p>
<dd>
<dt>Browsing No</p>
<dd>Specifies whether or not shared printers should be advertised.</p>
<dt>Classification banner</p>
<dd>Specifies the security classification of the server.</p>
<dt>ClassifyOverride Yes</p>
<dd>
<dt>ClassifyOverride No</p>
<dd>Specifies whether to allow users to override the classification of individual print jobs.</p>
<dt>DefaultAuthType Basic</p>
<dd>
<dt>DefaultAuthType BasicDigest</p>
<dd>
<dt>DefaultAuthType Digest</p>
<dd>
<dt>DefaultAuthType Negotiate</p>
<dd>Specifies the default type of authentication to use.</p>
<dt>DefaultEncryption Never</p>
<dd>
<dt>DefaultEncryption IfRequested</p>
<dd>
<dt>DefaultEncryption Required</p>
<dd>Specifies the type of encryption to use for authenticated requests.</p>
<dt>DefaultLanguage locale</p>
<dd>Specifies the default language to use for text and web content.</p>
<dt>DefaultPaperSize Auto</p>
<dd>
<dt>DefaultPaperSize None</p>
<dd>
<dt>DefaultPaperSize sizename</p>
<dd>Specifies the default paper size for new print queues. &quot;Auto&quot; uses a locale- specific default, while &quot;None&quot; specifies there is no default paper size.</p>
<dt>DefaultPolicy policy-name</p>
<dd>Specifies the default access policy to use.</p>
<dt>DefaultShared Yes</p>
<dd>
<dt>DefaultShared No</p>
<dd>Specifies whether local printers are shared by default.</p>
<dt>Deny all</p>
<dd>
<dt>Deny none</p>
<dd>
<dt>Deny host.domain.com</p>
<dd>
<dt>Deny *.domain.com</p>
<dd>
<dt>Deny ip-address</p>
<dd>
<dt>Deny ip-address/netmask</p>
<dd>
<dt>Deny ip-address/mm</p>
<dd>
<dt>Deny @IF(name)</p>
<dd>
<dt>Deny @LOCAL</p>
<dd>Denies access to the named host or address.</p>
<dt>DirtyCleanInterval seconds</p>
<dd>Specifies the delay for updating of configuration and state files. A value of 0 causes the update to happen as soon as possible, typically within a few milliseconds.</p>
<dt>Encryption IfRequested</p>
<dd>
<dt>Encryption Never</p>
<dd>
<dt>Encryption Required</p>
<dd>Specifies the level of encryption that is required for a particular location.</p>
<dt>ErrorPolicy abort-job</p>
<dd>Specifies that a failed print job should be aborted (discarded) unless otherwise specified for the printer.</p>
<dt>ErrorPolicy retry-job</p>
<dd>Specifies that a failed print job should be retried at a later time unless otherwise specified for the printer.</p>
<dt>ErrorPolicy retry-this-job</p>
<dd>Specifies that a failed print job should be retried immediately unless otherwise specified for the printer.</p>
<dt>ErrorPolicy stop-printer</p>
<dd>Specifies that a failed print job should stop the printer unless otherwise specified for the printer. The &#8216;stop-printer&#8217; error policy is the default.</p>
<dt>FilterLimit limit</p>
<dd>Specifies the maximum cost of filters that are run concurrently.</p>
<dt>FilterNice nice-value</p>
<dd>Specifies the scheduling priority (&quot;nice&quot; value) of filters that are run to print a job.</p>
<dt>GSSServiceName name</p>
<dd>Specifies the service name when using Kerberos authentication. The default service name is &quot;http&quot;.</p>
<dt>HostNameLookups On</p>
<dd>
<dt>HostNameLookups Off</p>
<dd>
<dt>HostNameLookups Double</p>
<dd>Specifies whether or not to do reverse lookups on client addresses.</p>
<dt>Include filename</p>
<dd>Includes the named file.</p>
<dt>JobKillDelay seconds</p>
<dd>Specifies the number of seconds to wait before killing the filters and backend associated with a canceled or held job.</p>
<dt>JobPrivateAccess all</p>
<dd>
<dt>JobPrivateAccess default</p>
<dd>
<dt>JobPrivateAccess {user|@group|@ACL|@OWNER|@SYSTEM}+</p>
<dd>Specifies an access list for a job&#8217;s private values. The &quot;default&quot; access list is &quot;@OWNER @SYSTEM&quot;. &quot;@ACL&quot; maps to the printer&#8217;s requesting-user-name-allowed or requesting-user-name-denied values.</p>
<dt>JobPrivateValues all</p>
<dd>
<dt>JobPrivateValues default</p>
<dd>
<dt>JobPrivateValues none</p>
<dd>
<dt>JobPrivateValues attribute-name-1 [ &#8230; attribute-name-N ]</p>
<dd>Specifies the list of job values to make private. The &quot;default&quot; values are &quot;job-name&quot;, &quot;job-originating-host-name&quot;, and &quot;job-originating-user-name&quot;.</p>
<dt>JobRetryInterval seconds</p>
<dd>Specifies the interval between retries of jobs in seconds.</p>
<dt>JobRetryLimit count</p>
<dd>Specifies the number of retries that are done for jobs.</p>
<dt>KeepAlive Yes</p>
<dd>
<dt>KeepAlive No</p>
<dd>Specifies whether to support HTTP keep-alive connections.</p>
<dt>KeepAliveTimeout seconds</p>
<dd>Specifies the amount of time that connections are kept alive.</p>
<dt>&lt;Limit operations&gt; &#8230; &lt;/Limit&gt;</p>
<dd>Specifies the IPP operations that are being limited inside a policy.</p>
<dt>&lt;Limit methods&gt; &#8230; &lt;/Limit&gt;</p>
<dd>
<dt>&lt;LimitExcept methods&gt; &#8230; &lt;/LimitExcept&gt;</p>
<dd>Specifies the HTTP methods that are being limited inside a location.</p>
<dt>LimitRequestBody</p>
<dd>Specifies the maximum size of any print job request.</p>
<dt>Listen ip-address:port</p>
<dd>
<dt>Listen *:port</p>
<dd>
<dt>Listen /path/to/domain/socket</p>
<dd>Listens to the specified address and port or domain socket path.</p>
<dt>&lt;Location /path&gt; &#8230; &lt;/Location&gt;</p>
<dd>Specifies access control for the named location.</p>
<dt>LogDebugHistory #-messages</p>
<dd>Specifies the number of debugging messages that are logged when an error occurs in a print job.</p>
<dt>LogLevel alert</p>
<dd>
<dt>LogLevel crit</p>
<dd>
<dt>LogLevel debug2</p>
<dd>
<dt>LogLevel debug</p>
<dd>
<dt>LogLevel emerg</p>
<dd>
<dt>LogLevel error</p>
<dd>
<dt>LogLevel info</p>
<dd>
<dt>LogLevel none</p>
<dd>
<dt>LogLevel notice</p>
<dd>
<dt>LogLevel warn</p>
<dd>Specifies the logging level for the ErrorLog file.</p>
<dt>LogTimeFormat standard</p>
<dd>
<dt>LogTimeFormat usecs</p>
<dd>Specifies the format of the date and time in the log files.</p>
<dt>MaxClients number</p>
<dd>Specifies the maximum number of simultaneous clients to support.</p>
<dt>MaxClientsPerHost number</p>
<dd>Specifies the maximum number of simultaneous clients to support from a single address.</p>
<dt>MaxCopies number</p>
<dd>Specifies the maximum number of copies that a user can print of each job.</p>
<dt>MaxHoldTime seconds</p>
<dd>Specifies the maximum time a job may remain in the &quot;indefinite&quot; hold state before it is canceled. Set to 0 to disable cancellation of held jobs.</p>
<dt>MaxJobs number</p>
<dd>Specifies the maximum number of simultaneous jobs to support.</p>
<dt>MaxJobsPerPrinter number</p>
<dd>Specifies the maximum number of simultaneous jobs per printer to support.</p>
<dt>MaxJobsPerUser number</p>
<dd>Specifies the maximum number of simultaneous jobs per user to support.</p>
<dt>MaxJobTime seconds</p>
<dd>Specifies the maximum time a job may take to print before it is canceled. The default is 10800 seconds (3 hours). Set to 0 to disable cancellation of &quot;stuck&quot; jobs.</p>
<dt>MaxLogSize number-bytes</p>
<dd>Specifies the maximum size of the log files before they are rotated (0 to disable rotation)</p>
<dt>MaxRequestSize number-bytes</p>
<dd>Specifies the maximum request/file size in bytes (0 for no limit)</p>
<dt>MultipleOperationTimeout seconds</p>
<dd>Specifies the maximum amount of time to allow between files in a multiple file print job.</p>
<dt>Order allow,deny</p>
<dd>
<dt>Order deny,allow</p>
<dd>Specifies the order of HTTP access control (allow,deny or deny,allow)</p>
<dt>PageLogFormat format string</p>
<dd>Specifies the format of page log lines.</p>
<dt>PassEnv variable [&#8230; variable]</p>
<dd>Passes the specified environment variable(s) to child processes.</p>
<dt>&lt;Policy name&gt; &#8230; &lt;/Policy&gt;</p>
<dd>Specifies access control for the named policy.</p>
<dt>Port number</p>
<dd>Specifies a port number to listen to for HTTP requests.</p>
<dt>PreserveJobFiles Yes</p>
<dd>
<dt>PreserveJobFiles No</p>
<dd>Specifies whether or not to preserve job files after they are printed.</p>
<dt>PreserveJobHistory Yes</p>
<dd>
<dt>PreserveJobHistory No</p>
<dd>Specifies whether or not to preserve the job history after they are printed.</p>
<dt>PrintcapFormat bsd</p>
<dd>
<dt>PrintcapFormat plist</p>
<dd>
<dt>PrintcapFormat solaris</p>
<dd>Specifies the format of the printcap file.</p>
<dt>ReloadTimeout seconds</p>
<dd>Specifies the amount of time to wait for job completion before restarting the scheduler.</p>
<dt>Require group group-name-list</p>
<dd>
<dt>Require user user-name-list</p>
<dd>
<dt>Require valid-user</p>
<dd>Specifies that user or group authentication is required.</p>
<dt>RIPCache bytes</p>
<dd>Specifies the maximum amount of memory to use when converting images and PostScript files to bitmaps for a printer.</p>
<dt>Satisfy all</p>
<dd>
<dt>Satisfy any</p>
<dd>Specifies whether all or any limits set for a Location must be satisfied to allow access.</p>
<dt>ServerAdmin user [at] domain.com</p>
<dd>Specifies the email address of the server administrator.</p>
<dt>ServerAlias hostname [&#8230; hostname]</p>
<dd>
<dt>ServerAlias *</p>
<dd>Specifies an alternate name that the server is known by. The special name &quot;*&quot; allows any name to be used.</p>
<dt>ServerName hostname-or-ip-address</p>
<dd>Specifies the fully-qualified hostname of the server.</p>
<dt>ServerTokens Full</p>
<dd>
<dt>ServerTokens Major</p>
<dd>
<dt>ServerTokens Minimal</p>
<dd>
<dt>ServerTokens Minor</p>
<dd>
<dt>ServerTokens None</p>
<dd>
<dt>ServerTokens OS</p>
<dd>
<dt>ServerTokens ProductOnly</p>
<dd>Specifies what information is included in the Server header of HTTP responses.</p>
<dt>SetEnv variable value</p>
<dd>Set the specified environment variable to be passed to child processes.</p>
<dt>SSLListen</p>
<dd>Listens on the specified address and port for encrypted connections.</p>
<dt>SSLOptions None</p>
<dd>
<dt>SSLOptions NoEmptyFragments</p>
<dd>Sets SSL/TLS protocol options for encrypted connections.</p>
<dt>SSLPort</p>
<dd>Listens on the specified port for encrypted connections.</p>
<dt>StrictConformance Yes</p>
<dd>
<dt>StrictConformance No</p>
<dd>Specifies whether the scheduler requires clients to strictly adhere to the IPP specifications. The default is No.</p>
<dt>SubscriptionPrivateAccess all</p>
<dd>
<dt>SubscriptionPrivateAccess default</p>
<dd>
<dt>SubscriptionPrivateAccess {user|@group|@ACL|@OWNER|@SYSTEM}+</p>
<dd>Specifies an access list for a subscription&#8217;s private values. The &quot;default&quot; access list is &quot;@OWNER @SYSTEM&quot;. &quot;@ACL&quot; maps to the printer&#8217;s requesting-user-name-allowed or requesting-user-name-denied values.</p>
<dt>SubscriptionPrivateValues all</p>
<dd>
<dt>SubscriptionPrivateValues default</p>
<dd>
<dt>SubscriptionPrivateValues none</p>
<dd>
<dt>SubscriptionPrivateValues attribute-name-1 [ &#8230; attribute-name-N ]</p>
<dd>Specifies the list of job values to make private. The &quot;default&quot; values are &quot;notify-events&quot;, &quot;notify-pull-method&quot;, &quot;notify-recipient-uri&quot;, &quot;notify-subscriber-user-name&quot;, and &quot;notify-user-data&quot;.</p>
<dt>Timeout seconds</p>
<dd>Specifies the HTTP request timeout in seconds.</p>
<dt>WebInterface yes</p>
<dd>
<dt>WebInterface no</p>
<dd>Specifies whether the web interface is enabled.</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-classes-conf/">classes.conf</a>(5)</i>, <i><a href="/docs/linux/man/5-cups-files-conf/">cups-files.conf</a>(5)</i>, <i><a href="/docs/linux/man/8-cupsd/">cupsd</a>(8)</i>, <i><a href="/docs/linux/man/5-mime-convs/">mime.convs</a>(5)</i>, <i><a href="/docs/linux/man/5-mime-types/">mime.types</a>(5)</i>, <i><a href="/docs/linux/man/5-printers-conf/">printers.conf</a>(5)</i>, <i><a href="/docs/linux/man/5-subscriptions-conf/">subscriptions.conf</a>(5)</i>,<br />
 <a rel="nofollow" href="http://localhost:631/help">http://localhost:631/help</a></p>
<h2>Copyright</h2>
<p>Copyright 2007-2013 by Apple Inc.</p>

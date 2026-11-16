---
title: "cupsd-conf(5)"
name: "cupsd-conf"
section: "5"
letter: "c"
url: "/docs/linux/man/5-cupsd-conf/"
description: "cupsd.conf – server configuration file for cups"
---

<p>cupsd.conf &#8211; server configuration file for cups</p>
<h2>Description</h2>
<p>The <i>cupsd.conf</i> file configures the CUPS scheduler, <code><a href="/docs/linux/man/8-cupsd/">cupsd</a></code>(8). It is normally located in the <i>/etc/cups</i> directory. Each line in the file can be a configuration directive, a blank line, or a comment. Configuration directives typically consist of a name and zero or more values separated by whitespace. The configuration directive name and values are case-insensitive. Comment lines start with the # character.</p>
<h3>Top-Level Directives</h3>
<p>The following top-level directives are understood by <code><a href="/docs/linux/man/8-cupsd/">cupsd</a></code>(8):</p>
<dl>
<dt><code>AccessLogLevel config</code></dt>
<dd>
</dd><dt><code>AccessLogLevel actions</code></dt>
<dd>
</dd><dt><code>AccessLogLevel all</code></dt>
<dd>Specifies the logging level for the AccessLog file. The &quot;config&quot; level logs when printers and classes are added, deleted, or modified and when configuration files are accessed or updated. The &quot;actions&quot; level logs when print jobs are submitted, held, released, modified, or canceled, and any of the conditions for &quot;config&quot;. The &quot;all&quot; level logs all requests. The default access log level is &quot;actions&quot;.</dd>
<dt><code>AutoPurgeJobs Yes</code></dt>
<dd>
</dd><dt><code>AutoPurgeJobs No</code></dt>
<dd>Specifies whether to purge job history data automatically when it is no longer required for quotas. The default is &quot;No&quot;.</dd>
<dt><code>BrowseDNSSDSubTypes</code><i>_subtype[,&#8230;]</i></dt>
<dd>Specifies a list of Bonjour sub-types to advertise for each shared printer. For example, &quot;BrowseDNSSDSubTypes _cups,_print&quot; will tell network clients that both CUPS sharing and IPP Everywhere are supported. The default is &quot;_cups&quot; which is necessary for printer sharing to work between systems using CUPS.</dd>
<dt><code>BrowseLocalProtocols all</code></dt>
<dd>
</dd><dt><code>BrowseLocalProtocols dnssd</code></dt>
<dd>
</dd><dt><code>BrowseLocalProtocols none</code></dt>
<dd>Specifies which protocols to use for local printer sharing. The default is &quot;dnssd&quot; on systems that support Bonjour and &quot;none&quot; otherwise.</dd>
<dt><code>BrowseWebIF Yes</code></dt>
<dd>
</dd><dt><code>BrowseWebIF No</code></dt>
<dd>Specifies whether the CUPS web interface is advertised. The default is &quot;No&quot;.</dd>
<dt><code>Browsing Yes</code></dt>
<dd>
</dd><dt><code>Browsing No</code></dt>
<dd>Specifies whether shared printers are advertised. The default is &quot;No&quot;.</dd>
<dt><code>DefaultAuthType Basic</code></dt>
<dd>Specifies the default type of authentication to use. The default is &quot;Basic&quot;.</dd>
<dt><code>DefaultEncryption Never</code></dt>
<dd>
</dd><dt><code>DefaultEncryption IfRequested</code></dt>
<dd>
</dd><dt><code>DefaultEncryption Required</code></dt>
<dd>Specifies whether encryption will be used for authenticated requests. The default is &quot;Required&quot;.</dd>
<dt><code>DefaultLanguage </code><i>locale</i></dt>
<dd>Specifies the default language to use for text and web content. The default is &quot;en&quot;.</dd>
<dt><code>DefaultPaperSize Auto</code></dt>
<dd>
</dd><dt><code>DefaultPaperSize None</code></dt>
<dd>
</dd><dt><code>DefaultPaperSize </code><i>sizename</i></dt>
<dd>Specifies the default paper size for new print queues. &quot;Auto&quot; uses a locale-specific default, while &quot;None&quot; specifies there is no default paper size. Specific size names are typically &quot;Letter&quot; or &quot;A4&quot;. The default is &quot;Auto&quot;. Note: The default paper size must use a size name from the PPD file and not a PWG self-describing media size name.</dd>
<dt><code>DefaultPolicy </code><i>policy-name</i></dt>
<dd>Specifies the default access policy to use. The default access policy is &quot;default&quot;.</dd>
<dt><code>DefaultShared Yes</code></dt>
<dd>
</dd><dt><code>DefaultShared No</code></dt>
<dd>Specifies whether local printers are shared by default. The default is &quot;Yes&quot;.</dd>
<dt><code>DirtyCleanInterval </code><i>seconds</i></dt>
<dd>Specifies the delay for updating of configuration and state files. A value of 0 causes the update to happen as soon as possible, typically within a few milliseconds. The default value is &quot;30&quot;.</dd>
<dt><code>DNSSDHostName</code><i>hostname.example.com</i></dt>
<dd>Specifies the fully-qualified domain name for the server that is used for Bonjour sharing. The default is typically the server&#8217;s &quot;.local&quot; hostname.</dd>
<dt><code>ErrorPolicy abort-job</code></dt>
<dd>Specifies that a failed print job should be aborted (discarded) unless otherwise specified for the printer.</dd>
<dt><code>ErrorPolicy retry-current-job</code></dt>
<dd>Specifies that a failed print job should be retried immediately unless otherwise specified for the printer.</dd>
<dt><code>ErrorPolicy retry-job</code></dt>
<dd>Specifies that a failed print job should be retried at a later time unless otherwise specified for the printer.</dd>
<dt><code>ErrorPolicy stop-printer</code></dt>
<dd>Specifies that a failed print job should stop the printer unless otherwise specified for the printer. The &#8216;stop-printer&#8217; error policy is the default.</dd>
<dt><code>FilterLimit </code><i>limit</i></dt>
<dd>Specifies the maximum cost of filters that are run concurrently, which can be used to minimize disk, memory, and CPU resource problems. A limit of 0 disables filter limiting. An average print to a non-PostScript printer needs a filter limit of about 200. A PostScript printer needs about half that (100). Setting the limit below these thresholds will effectively limit the scheduler to printing a single job at any time. The default limit is &quot;0&quot;.</dd>
<dt><code>FilterNice </code><i>nice-value</i></dt>
<dd>Specifies the scheduling priority ( <code>nice</code>(8) value) of filters that are run to print a job. The nice value ranges from 0, the highest priority, to 19, the lowest priority. The default is 0.</dd>
<dd><code>HostNameLookups On</code></dd>
<dt><code>HostNameLookups Off</code></dt>
<dd>
</dd><dt><code>HostNameLookups Double</code></dt>
<dd>Specifies whether to do reverse lookups on connecting clients. The &quot;Double&quot; setting causes <code><a href="/docs/linux/man/8-cupsd/">cupsd</a></code>(8) to verify that the hostname resolved from the address matches one of the addresses returned for that hostname. Double lookups also prevent clients with unregistered addresses from connecting to your server. The default is &quot;Off&quot; to avoid the potential server performance problems with hostname lookups. Only set this option to &quot;On&quot; or &quot;Double&quot; if absolutely required.</dd>
<dt><code>IdleExitTimeout </code><i>seconds</i></dt>
<dd>Specifies the length of time to wait before shutting down due to inactivity. The default is &quot;60&quot; seconds. Note: Only applicable when <code><a href="/docs/linux/man/8-cupsd/">cupsd</a></code>(8) is run on-demand (e.g., with <code>-l</code>).</dd>
<dt><code>JobKillDelay </code><i>seconds</i></dt>
<dd>Specifies the number of seconds to wait before killing the filters and backend associated with a canceled or held job. The default is &quot;30&quot;.</dd>
<dt><code>JobRetryInterval </code><i>seconds</i></dt>
<dd>Specifies the interval between retries of jobs in seconds. This is typically used for fax queues but can also be used with normal print queues whose error policy is &quot;retry-job&quot; or &quot;retry-current-job&quot;. The default is &quot;30&quot;.</dd>
<dt><code>JobRetryLimit </code><i>count</i></dt>
<dd>Specifies the number of retries that are done for jobs. This is typically used for fax queues but can also be used with normal print queues whose error policy is &quot;retry-job&quot; or &quot;retry-current-job&quot;. The default is &quot;5&quot;.</dd>
<dt><code>KeepAlive Yes</code></dt>
<dd>
</dd><dt><code>KeepAlive No</code></dt>
<dd>Specifies whether to support HTTP keep-alive connections. The default is &quot;Yes&quot;.</dd>
<dt><code>&lt;Limit </code><i>operation </i>&#8230;<code>&gt; </code>&#8230; <code>&lt;/Limit&gt;</code></dt>
<dd>Specifies the IPP operations that are being limited inside a Policy section. IPP operation names are listed below in the section &quot;IPP OPERATION NAMES&quot;.</dd>
<dt><code>&lt;Limit </code><i>method </i>&#8230;<code>&gt; </code>&#8230; <code>&lt;/Limit&gt;</code></dt>
<dd>
</dd><dt><code>&lt;LimitExcept </code><i>method </i>&#8230;<code>&gt; </code>&#8230; <code>&lt;/LimitExcept&gt;</code></dt>
<dd>Specifies the HTTP methods that are being limited inside a Location section. HTTP method names are listed below in the section &quot;HTTP METHOD NAMES&quot;.</dd>
<dt><code>LimitRequestBody </code><i>size</i></dt>
<dd>Specifies the maximum size of print files, IPP requests, and HTML form data. The default is &quot;0&quot; which disables the limit check.</dd>
<dt><code>Listen </code><i>ipv4-address</i><code>:</code><i>port</i></dt>
<dd>
</dd><dt><code>Listen [</code><i>ipv6-address</i><code>]:</code><i>port</i></dt>
<dd>
</dd><dt><code>Listen *:</code><i>port</i></dt>
<dd>
</dd><dt><code>Listen </code><i>/path/to/domain/socket</i></dt>
<dd>Listens to the specified address and port or domain socket path for connections. Multiple Listen directives can be provided to listen on multiple addresses. The Listen directive is similar to the Port directive but allows you to restrict access to specific interfaces or networks. Note: &quot;Listen *:<i>port</i>&quot; and &quot;Port <i>port</i>&quot; effectively listen on all IP addresses, so you cannot combine them with Listen directives for explicit IPv4 or IPv6 addresses on the same port.</dd>
<dt><code>&lt;Location </code><i>/path</i><code>&gt; </code>&#8230; <code>&lt;/Location&gt;</code></dt>
<dd>Specifies access control for the named location. Paths are documented below in the section &quot;LOCATION PATHS&quot;.</dd>
<dt><code>LogDebugHistory </code><i>number</i></dt>
<dd>Specifies the number of debugging messages that are retained for logging if an error occurs in a print job. Debug messages are logged regardless of the LogLevel setting.</dd>
<dt><code>LogLevel </code>none</dt>
<dd>
</dd><dt><code>LogLevel </code>emerg</dt>
<dd>
</dd><dt><code>LogLevel </code>alert</dt>
<dd>
</dd><dt><code>LogLevel </code>crit</dt>
<dd>
</dd><dt><code>LogLevel </code>error</dt>
<dd>
</dd><dt><code>LogLevel </code>warn</dt>
<dd>
</dd><dt><code>LogLevel </code>notice</dt>
<dd>
</dd><dt><code>LogLevel </code>info</dt>
<dd>
</dd><dt><code>LogLevel </code>debug</dt>
<dd>
</dd><dt><code>LogLevel </code>debug2</dt>
<dd>Specifies the level of logging for the ErrorLog file. The value &quot;none&quot; stops all logging while &quot;debug2&quot; logs everything. The default is &quot;warn&quot;.</dd>
<dt><code>LogTimeFormat </code>standard</dt>
<dd>
</dd><dt><code>LogTimeFormat </code>usecs</dt>
<dd>Specifies the format of the date and time in the log files. The value &quot;standard&quot; is the default and logs whole seconds while &quot;usecs&quot; logs microseconds.</dd>
<dt><code>MaxClients </code><i>number</i></dt>
<dd>Specifies the maximum number of simultaneous clients that are allowed by the scheduler. The default is &quot;100&quot;.</dd>
<dt><code>MaxClientsPerHost </code><i>number</i></dt>
<dd>Specifies the maximum number of simultaneous clients that are allowed from a single address. The default is the MaxClients value.</dd>
<dt><code>MaxCopies </code><i>number</i></dt>
<dd>Specifies the maximum number of copies that a user can print of each job. The default is &quot;9999&quot;.</dd>
<dt><code>MaxHoldTime </code><i>seconds</i></dt>
<dd>Specifies the maximum time a job may remain in the &quot;indefinite&quot; hold state before it is canceled. The default is &quot;0&quot; which disables cancellation of held jobs.</dd>
<dt><code>MaxJobs </code><i>number</i></dt>
<dd>Specifies the maximum number of simultaneous jobs that are allowed. Set to &quot;0&quot; to allow an unlimited number of jobs. The default is &quot;500&quot;.</dd>
<dt><code>MaxJobsPerPrinter </code><i>number</i></dt>
<dd>Specifies the maximum number of simultaneous jobs that are allowed per printer. The default is &quot;0&quot; which allows up to MaxJobs jobs per printer.</dd>
<dt><code>MaxJobsPerUser </code><i>number</i></dt>
<dd>Specifies the maximum number of simultaneous jobs that are allowed per user. The default is &quot;0&quot; which allows up to MaxJobs jobs per user.</dd>
<dt><code>MaxJobTime </code><i>seconds</i></dt>
<dd>Specifies the maximum time a job may take to print before it is canceled. Set to &quot;0&quot; to disable cancellation of &quot;stuck&quot; jobs. The default is &quot;10800&quot; (3 hours).</dd>
<dt><code>MaxLogSize </code><i>size</i></dt>
<dd>Specifies the maximum size of the log files before they are rotated. The value &quot;0&quot; disables log rotation. The default is &quot;1048576&quot; (1MB).</dd>
<dt><code>MaxSubscriptions </code><i>number</i></dt>
<dd>Specifies the maximum number of simultaneous event subscriptions that are allowed. Set to &quot;0&quot; to allow an unlimited number of subscriptions. The default is &quot;100&quot;.</dd>
<dt><code>MaxSubscriptionsPerJob </code><i>number</i></dt>
<dd>Specifies the maximum number of simultaneous event subscriptions that are allowed per job. The default is &quot;0&quot; which allows up to MaxSubscriptions subscriptions per job.</dd>
<dt><code>MaxSubscriptionsPerPrinter </code><i>number</i></dt>
<dd>Specifies the maximum number of simultaneous event subscriptions that are allowed per printer. The default is &quot;0&quot; which allows up to MaxSubscriptions subscriptions per printer.</dd>
<dt><code>MaxSubscriptionsPerUser </code><i>number</i></dt>
<dd>Specifies the maximum number of simultaneous event subscriptions that are allowed per user. The default is &quot;0&quot; which allows up to MaxSubscriptions subscriptions per user.</dd>
<dt><code>MultipleOperationTimeout </code><i>seconds</i></dt>
<dd>Specifies the maximum amount of time to allow between files in a multiple file print job. The default is &quot;900&quot; (15 minutes).</dd>
<dt><code>&lt;Policy </code><i>name</i><code>&gt; </code>&#8230; <code>&lt;/Policy&gt;</code></dt>
<dd>Specifies access control for the named policy.</dd>
<dt><code>Port </code><i>number</i></dt>
<dd>Listens to the specified port number for connections.</dd>
<dt><code>PreserveJobFiles Yes</code></dt>
<dd>
</dd><dt><code>PreserveJobFiles No</code></dt>
<dd>
</dd><dt><code>PreserveJobFiles </code><i>seconds</i></dt>
<dd>Specifies whether job files (documents) are preserved after a job is printed. If a numeric value is specified, job files are preserved for the indicated number of seconds after printing. The default is &quot;86400&quot; (preserve 1 day).</dd>
<dt><code>PreserveJobHistory Yes</code></dt>
<dd>
</dd><dt><code>PreserveJobHistory No</code></dt>
<dd>
</dd><dt><code>PreserveJobHistory </code><i>seconds</i></dt>
<dd>Specifies whether the job history is preserved after a job is printed. If a numeric value is specified, the job history is preserved for the indicated number of seconds after printing. If &quot;Yes&quot;, the job history is preserved until the MaxJobs limit is reached. The default is &quot;Yes&quot;.</dd>
<dt><code>ReadyPaperSizes </code><i>sizename[,&#8230;]</i></dt>
<dd>Specifies a list of potential paper sizes that are reported as &quot;ready&quot; (loaded). The actual list will only contain sizes that each printer supports. The default is &quot;Letter,Legal,Tabloid,4&#215;6,Env10&quot; when the default paper size is &quot;Letter&quot; and &quot;A3,A4,A5,A6,EnvDL&quot; otherwise. Note: Paper sizes must use the size names from the PPD file and not PWG self-describing media size names.</dd>
<dt><code>ReloadTimeout </code><i>seconds</i></dt>
<dd>Specifies the amount of time to wait for job completion before restarting the scheduler. The default is &quot;30&quot;.</dd>
<dt><code>ServerAdmin </code><i>email-address</i></dt>
<dd>Specifies the email address of the server administrator. The default value is &quot;root [at] ServerName&quot;.</dd>
<dt><code>ServerAlias </code><i>hostname </i>[ &#8230; <i>hostname </i>]</dt>
<dd>
</dd><dt><code>ServerAlias *</code></dt>
<dd>The ServerAlias directive is used for HTTP Host header validation when clients connect to the scheduler from external interfaces. Using the special name &quot;*&quot; can expose your system to known browser-based DNS rebinding attacks, even when accessing sites through a firewall. If the auto-discovery of alternate names does not work, we recommend listing each alternate name with a ServerAlias directive instead of using &quot;*&quot;.</dd>
<dt><code>ServerName </code><i>hostname</i></dt>
<dd>Specifies the fully-qualified hostname of the server. The default is the value reported by the <code><a href="/docs/linux/man/1-hostname/">hostname</a></code>(1) command.</dd>
<dt><code>ServerTokens None</code></dt>
<dd>
</dd><dt><code>ServerTokens ProductOnly</code></dt>
<dd>
</dd><dt><code>ServerTokens Major</code></dt>
<dd>
</dd><dt><code>ServerTokens Minor</code></dt>
<dd>
</dd><dt><code>ServerTokens Minimal</code></dt>
<dd>
</dd><dt><code>ServerTokens OS</code></dt>
<dd>
</dd><dt><code>ServerTokens Full</code></dt>
<dd>Specifies what information is included in the Server header of HTTP responses. &quot;None&quot; disables the Server header. &quot;ProductOnly&quot; reports &quot;CUPS&quot;. &quot;Major&quot; reports &quot;CUPS/major IPP/2&quot;. &quot;Minor&quot; reports &quot;CUPS/major.minor IPP/2.1&quot;. &quot;Minimal&quot; reports &quot;CUPS/major.minor.patch IPP/2.1&quot;. &quot;OS&quot; reports &quot;CUPS/major.minor.path (osname osversion) IPP/2.1&quot;. &quot;Full&quot; reports &quot;CUPS/major.minor.path (osname osversion; architecture) IPP/2.1&quot;. The default is &quot;Minimal&quot;.</dd>
<dt><code>SSLListen </code><i>ipv4-address</i><code>:</code><i>port</i></dt>
<dd>
</dd><dt><code>SSLListen [</code><i>ipv6-address</i><code>]:</code><i>port</i></dt>
<dd>
</dd><dt><code>SSLListen *:</code><i>port</i></dt>
<dd>Listens on the specified address and port for encrypted connections.</dd>
<dt>
</dt><dt><code>SSLOptions </code>[<i>AllowDH</i>] [<i>AllowRC4</i>] [<i>AllowSSL3</i>] [<i>DenyCBC</i>] [<i>DenyTLS1.0</i>] [<i>MaxTLS1.0</i>] [<i>MaxTLS1.1</i>] [<i>MaxTLS1.2</i>] [<i>MaxTLS1.3</i>] [<i>MinTLS1.0</i>] [<i>MinTLS1.1</i>] [<i>MinTLS1.2</i>] [<i>MinTLS1.3</i>]</dt>
<dd>
</dd><dd>
</dd><dt><code>SSLOptions None</code></dt>
<dd>Sets encryption options (only in /etc/cups/client.conf). By default, CUPS only supports encryption using TLS v1.0 or higher using known secure cipher suites. Security is reduced when <i>Allow</i> options are used. Security is enhanced when <i>Deny</i> options are used. The <i>AllowDH</i> option enables cipher suites using plain Diffie-Hellman key negotiation (not supported on systems using GNU TLS). The <i>AllowRC4</i> option enables the 128-bit RC4 cipher suites, which are required for some older clients. The <i>AllowSSL3</i> option enables SSL v3.0, which is required for some older clients that do not support TLS v1.0. The <i>DenyCBC</i> option disables all CBC cipher suites. The <i>DenyTLS1.0</i> option disables TLS v1.0 support &#8211; this sets the minimum protocol version to TLS v1.1. The <i>MinTLS</i> options set the minimum TLS version to support. The <i>MaxTLS</i> options set the maximum TLS version to support. Not all operating systems support TLS 1.3 at this time.</dd>
<dt><code>SSLPort </code><i>port</i></dt>
<dd>Listens on the specified port for encrypted connections.</dd>
<dt><code>StrictConformance Yes</code></dt>
<dd>
</dd><dt><code>StrictConformance No</code></dt>
<dd>Specifies whether the scheduler requires clients to strictly adhere to the IPP specifications. The default is &quot;No&quot;.</dd>
<dt><code>Timeout </code><i>seconds</i></dt>
<dd>Specifies the HTTP request timeout. The default is &quot;900&quot; (15 minutes).</dd>
<dt><code>WebInterface yes</code></dt>
<dd>
</dd><dt><code>WebInterface no</code></dt>
<dd>Specifies whether the web interface is enabled. The default is &quot;No&quot;.</dd></dl>
<h3>Http Method Names</h3>
<p>The following HTTP methods are supported by <code><a href="/docs/linux/man/8-cupsd/">cupsd</a></code>(8):</p>
<dl>
<dt>GET</dt>
<dd>Used by a client to download icons and other printer resources and to access the CUPS web interface.</dd>
<dt>HEAD</dt>
<dd>Used by a client to get the type, size, and modification date of resources.</dd>
<dt>OPTIONS</dt>
<dd>Used by a client to establish a secure (SSL/TLS) connection.</dd>
<dt>POST</dt>
<dd>Used by a client to submit IPP requests and HTML forms from the CUPS web interface.</dd>
<dt>PUT</dt>
<dd>Used by a client to upload configuration files.</dd></dl>
<h3>Ipp Operation Names</h3>
<p>The following IPP operations are supported by <code><a href="/docs/linux/man/8-cupsd/">cupsd</a></code>(8):</p>
<dl>
<dt>CUPS-Accept-Jobs</dt>
<dd>Allows a printer to accept new jobs.</dd>
<dt>CUPS-Add-Modify-Class</dt>
<dd>Adds or modifies a printer class.</dd>
<dt>CUPS-Add-Modify-Printer</dt>
<dd>Adds or modifies a printer.</dd>
<dt>CUPS-Authenticate-Job</dt>
<dd>Releases a job that is held for authentication.</dd>
<dt>CUPS-Delete-Class</dt>
<dd>Deletes a printer class.</dd>
<dt>CUPS-Delete-Printer</dt>
<dd>Deletes a printer.</dd>
<dt>CUPS-Get-Classes</dt>
<dd>Gets a list of printer classes.</dd>
<dt>CUPS-Get-Default</dt>
<dd>Gets the server default printer or printer class.</dd>
<dt>CUPS-Get-Devices</dt>
<dd>Gets a list of devices that are currently available.</dd>
<dt>CUPS-Get-Document</dt>
<dd>Gets a document file for a job.</dd>
<dt>CUPS-Get-PPD</dt>
<dd>Gets a PPD file.</dd>
<dt>CUPS-Get-PPDs</dt>
<dd>Gets a list of installed PPD files.</dd>
<dt>CUPS-Get-Printers</dt>
<dd>Gets a list of printers.</dd>
<dt>CUPS-Move-Job</dt>
<dd>Moves a job.</dd>
<dt>CUPS-Reject-Jobs</dt>
<dd>Prevents a printer from accepting new jobs.</dd>
<dt>CUPS-Set-Default</dt>
<dd>Sets the server default printer or printer class.</dd>
<dt>Cancel-Job</dt>
<dd>Cancels a job.</dd>
<dt>Cancel-Jobs</dt>
<dd>Cancels one or more jobs.</dd>
<dt>Cancel-My-Jobs</dt>
<dd>Cancels one or more jobs creates by a user.</dd>
<dt>Cancel-Subscription</dt>
<dd>Cancels a subscription.</dd>
<dt>Close-Job</dt>
<dd>Closes a job that is waiting for more documents.</dd>
<dt>Create-Job</dt>
<dd>Creates a new job with no documents.</dd>
<dt>Create-Job-Subscriptions</dt>
<dd>Creates a subscription for job events.</dd>
<dt>Create-Printer-Subscriptions</dt>
<dd>Creates a subscription for printer events.</dd>
<dt>Get-Job-Attributes</dt>
<dd>Gets information about a job.</dd>
<dt>Get-Jobs</dt>
<dd>Gets a list of jobs.</dd>
<dt>Get-Notifications</dt>
<dd>Gets a list of event notifications for a subscription.</dd>
<dt>Get-Printer-Attributes</dt>
<dd>Gets information about a printer or printer class.</dd>
<dt>Get-Subscription-Attributes</dt>
<dd>Gets information about a subscription.</dd>
<dt>Get-Subscriptions</dt>
<dd>Gets a list of subscriptions.</dd>
<dt>Hold-Job</dt>
<dd>Holds a job from printing.</dd>
<dt>Hold-New-Jobs</dt>
<dd>Holds all new jobs from printing.</dd>
<dt>Pause-Printer</dt>
<dd>Stops processing of jobs by a printer or printer class.</dd>
<dt>Pause-Printer-After-Current-Job</dt>
<dd>Stops processing of jobs by a printer or printer class after the current job is finished.</dd>
<dt>Print-Job</dt>
<dd>Creates a new job with a single document.</dd>
<dt>Purge-Jobs</dt>
<dd>Cancels one or more jobs and deletes the job history.</dd>
<dt>Release-Held-New-Jobs</dt>
<dd>Allows previously held jobs to print.</dd>
<dt>Release-Job</dt>
<dd>Allows a job to print.</dd>
<dt>Renew-Subscription</dt>
<dd>Renews a subscription.</dd>
<dt>Restart-Job</dt>
<dd>Reprints a job, if possible.</dd>
<dt>Send-Document</dt>
<dd>Adds a document to a job.</dd>
<dt>Set-Job-Attributes</dt>
<dd>Changes job information.</dd>
<dt>Set-Printer-Attributes</dt>
<dd>Changes printer or printer class information.</dd>
<dt>Validate-Job</dt>
<dd>Validates options for a new job.</dd></dl>
<h3>Location Paths</h3>
<p>The following paths are commonly used when configuring <code><a href="/docs/linux/man/8-cupsd/">cupsd</a></code>(8):</p>
<dl>
<dt>/</dt>
<dd>The path for all get operations (get-printers, get-jobs, etc.)</dd>
<dt>/admin</dt>
<dd>The path for all administration operations (add-printer, delete-printer, start-printer, etc.)</dd>
<dt>/admin/conf</dt>
<dd>The path for access to the CUPS configuration files (cupsd.conf, client.conf, etc.)</dd>
<dt>/admin/log</dt>
<dd>The path for access to the CUPS log files (access_log, error_log, page_log)</dd>
<dt>/classes</dt>
<dd>The path for all printer classes</dd>
<dt>/classes/name</dt>
<dd>The resource for the named printer class</dd>
<dt>/jobs</dt>
<dd>The path for all jobs (hold-job, release-job, etc.)</dd>
<dt>/jobs/id</dt>
<dd>The path for the specified job</dd>
<dt>/printers</dt>
<dd>The path for all printers</dd>
<dt>/printers/name</dt>
<dd>The path for the named printer</dd>
<dt>/printers/name.png</dt>
<dd>The icon file path for the named printer</dd>
<dt>/printers/name.ppd</dt>
<dd>The PPD file path for the named printer</dd></dl>
<h3>Directives Valid Within Location And Limit Sections</h3>
<p>The following directives may be placed inside Location and Limit sections in the <code>cupsd.conf</code> file:</p>
<dl>
<dt><code>Allow all</code></dt>
<dd>
</dd><dt><code>Allow none</code></dt>
<dd>
</dd><dt><code>Allow </code><i>host.domain.com</i></dt>
<dd>
</dd><dt><code>Allow *.</code><i>domain.com</i></dt>
<dd>
</dd><dt><code>Allow </code><i>ipv4-address</i></dt>
<dd>
</dd><dt><code>Allow </code><i>ipv4-address</i><code>/</code><i>netmask</i></dt>
<dd>
</dd><dt><code>Allow </code><i>ipv4-address</i><code>/</code><i>mm</i></dt>
<dd>
</dd><dt><code>Allow [</code><i>ipv6-address</i><code>]</code></dt>
<dd>
</dd><dt><code>Allow [</code><i>ipv6-address</i><code>]/</code><i>mm</i></dt>
<dd>
</dd><dt><code>Allow @IF(</code><i>name</i><code>)</code></dt>
<dd>
</dd><dt><code>Allow @LOCAL</code></dt>
<dd>Allows access from the named hosts, domains, addresses, or interfaces. The @IF(name) form uses the current subnets configured for the named interface. The @LOCAL form uses the current subnets configured for all interfaces that are not point-to-point, for example Ethernet and Wi-Fi interfaces are used but DSL and VPN interfaces are not. The Order directive controls whether Allow lines are evaluated before or after Deny lines.</dd>
<dt><code>AuthType None</code></dt>
<dd>
</dd><dt><code>AuthType Basic</code></dt>
<dd>
</dd><dt><code>AuthType Default</code></dt>
<dd>Specifies the type of authentication required. The value &quot;Default&quot; corresponds to the DefaultAuthType value.</dd>
<dt><code>Deny all</code></dt>
<dd>
</dd><dt><code>Deny none</code></dt>
<dd>
</dd><dt><code>Deny </code><i>host.domain.com</i></dt>
<dd>
</dd><dt><code>Deny *.</code><i>domain.com</i></dt>
<dd>
</dd><dt><code>Deny </code><i>ipv4-address</i></dt>
<dd>
</dd><dt><code>Deny </code><i>ipv4-address</i><code>/</code><i>netmask</i></dt>
<dd>
</dd><dt><code>Deny </code><i>ipv4-address</i><code>/</code><i>mm</i></dt>
<dd>
</dd><dt><code>Deny [</code><i>ipv6-address</i><code>]</code></dt>
<dd>
</dd><dt><code>Deny [</code><i>ipv6-address</i><code>]/</code><i>mm</i></dt>
<dd>
</dd><dt><code>Deny @IF(</code><i>name</i><code>)</code></dt>
<dd>
</dd><dt><code>Deny @LOCAL</code></dt>
<dd>Denies access from the named hosts, domains, addresses, or interfaces. The @IF(name) form uses the current subnets configured for the named interface. The @LOCAL form uses the current subnets configured for all interfaces that are not point-to-point, for example Ethernet and Wi-Fi interfaces are used but DSL and VPN interfaces are not. The Order directive controls whether Deny lines are evaluated before or after Allow lines.</dd>
<dt><code>Encryption IfRequested</code></dt>
<dd>
</dd><dt><code>Encryption Never</code></dt>
<dd>
</dd><dt><code>Encryption Required</code></dt>
<dd>Specifies the level of encryption that is required for a particular location. The default value is &quot;IfRequested&quot;.</dd>
<dt><code>Order allow,deny</code></dt>
<dd>Specifies that access is denied by default. Allow lines are then processed followed by Deny lines to determine whether a client may access a particular resource.</dd>
<dt><code>Order deny,allow</code></dt>
<dd>Specifies that access is allowed by default. Deny lines are then processed followed by Allow lines to determine whether a client may access a particular resource.</dd>
<dt><code>Require group </code><i>group-name </i>[ <i>group-name </i>&#8230; ]</dt>
<dd>Specifies that an authenticated user must be a member of one of the named groups.</dd>
<dt><code>Require user {</code><i>user-name</i>|<code>@</code><i>group-name</i>} &#8230;</dt>
<dd>Specifies that an authenticated user must match one of the named users or be a member of one of the named groups. The group name &quot;@SYSTEM&quot; corresponds to the list of groups defined by the SystemGroup directive in the <code><a href="/docs/linux/man/5-cups-files-conf/">cups-files.conf</a></code>(5) file. The group name &quot;@OWNER&quot; corresponds to the owner of the resource, for example the person that submitted a print job. Note: The &#8216;root&#8217; user is not special and must be granted privileges like any other user account.</dd>
<dt><code>Require valid-user</code></dt>
<dd>Specifies that any authenticated user is acceptable.</dd>
<dt><code>Satisfy all</code></dt>
<dd>Specifies that all Allow, AuthType, Deny, Order, and Require conditions must be satisfied to allow access.</dd>
<dt><code>Satisfy any</code></dt>
<dd>Specifies that any a client may access a resource if either the authentication (AuthType/Require) or address (Allow/Deny/Order) conditions are satisfied. For example, this can be used to require authentication only for remote accesses.</dd></dl>
<h3>Directives Valid Within Policy Sections</h3>
<p>The following directives may be placed inside Policy sections in the <code>cupsd.conf</code> file:</p>
<dl>
<dt><code>JobPrivateAccess all</code></dt>
<dd>
</dd><dt><code>JobPrivateAccess default</code></dt>
<dd>
</dd><dt><code>JobPrivateAccess </code>{<i>user</i>|<code>@</code><i>group</i>|<code>@ACL</code>|<code>@OWNER</code>|<code>@SYSTEM</code>} &#8230;</dt>
<dd>Specifies an access list for a job&#8217;s private values. The &quot;default&quot; access list is &quot;@OWNER @SYSTEM&quot;. &quot;@ACL&quot; maps to the printer&#8217;s requesting-user-name-allowed or requesting-user-name-denied values. &quot;@OWNER&quot; maps to the job&#8217;s owner. &quot;@SYSTEM&quot; maps to the groups listed for the SystemGroup directive in the <code><a href="/docs/linux/man/5-cups-files-conf/">cups-files.conf</a></code>(5) file.</dd>
<dt><code>JobPrivateValues all</code></dt>
<dd>
</dd><dt><code>JobPrivateValues default</code></dt>
<dd>
</dd><dt><code>JobPrivateValues none</code></dt>
<dd>
</dd><dt><code>JobPrivateValues </code><i>attribute-name </i>[ &#8230; <i>attribute-name </i>]</dt>
<dd>Specifies the list of job values to make private. The &quot;default&quot; values are &quot;job-name&quot;, &quot;job-originating-host-name&quot;, &quot;job-originating-user-name&quot;, and &quot;phone&quot;.</dd>
<dt><code>SubscriptionPrivateAccess all</code></dt>
<dd>
</dd><dt><code>SubscriptionPrivateAccess default</code></dt>
<dd>
</dd><dt><code>SubscriptionPrivateAccess </code>{<i>user</i>|<code>@</code><i>group</i>|<code>@ACL</code>|<code>@OWNER</code>|<code>@SYSTEM</code>} &#8230;</dt>
<dd>Specifies an access list for a subscription&#8217;s private values. The &quot;default&quot; access list is &quot;@OWNER @SYSTEM&quot;. &quot;@ACL&quot; maps to the printer&#8217;s requesting-user-name-allowed or requesting-user-name-denied values. &quot;@OWNER&quot; maps to the job&#8217;s owner. &quot;@SYSTEM&quot; maps to the groups listed for the SystemGroup directive in the <code><a href="/docs/linux/man/5-cups-files-conf/">cups-files.conf</a></code>(5) file.</dd>
<dt><code>SubscriptionPrivateValues all</code></dt>
<dd>
</dd><dt><code>SubscriptionPrivateValues default</code></dt>
<dd>
</dd><dt><code>SubscriptionPrivateValues none</code></dt>
<dd>
</dd><dt><code>SubscriptionPrivateValues </code><i>attribute-name </i>[ &#8230; <i>attribute-name </i>]</dt>
<dd>Specifies the list of subscription values to make private. The &quot;default&quot; values are &quot;notify-events&quot;, &quot;notify-pull-method&quot;, &quot;notify-recipient-uri&quot;, &quot;notify-subscriber-user-name&quot;, and &quot;notify-user-data&quot;.</dd></dl>
<h3>Deprecated Directives</h3>
<p>The following directives are deprecated and will be removed in a future release of CUPS:</p>
<dl>
<dt><code>AuthType Negotiate</code></dt>
<dd>Specifies Kerberos authentication is required.</dd>
<dt><code>Classification </code><i>banner</i></dt>
<dd>Specifies the security classification of the server. Any valid banner name can be used, including &quot;classified&quot;, &quot;confidential&quot;, &quot;secret&quot;, &quot;topsecret&quot;, and &quot;unclassified&quot;, or the banner can be omitted to disable secure printing functions. The default is no classification banner.</dd>
<dt><code>ClassifyOverride Yes</code></dt>
<dd>
</dd><dt><code>ClassifyOverride No</code></dt>
<dd>Specifies whether users may override the classification (cover page) of individual print jobs using the &quot;job-sheets&quot; option. The default is &quot;No&quot;.</dd>
<dt><code>DefaultAuthType Negotiate</code></dt>
<dd>Specifies that Kerberos authentication is required by default.</dd>
<dt><code>GSSServiceName </code><i>name</i></dt>
<dd>Specifies the service name when using Kerberos authentication. The default service name is &quot;http.&quot;</dd>
<dt><code>PageLogFormat </code><i>format-string</i></dt>
<dd>Specifies the format of PageLog lines. Sequences beginning with percent (%) characters are replaced with the corresponding information, while all other characters are copied literally. The following percent sequences are recognized: </dd>
<pre> &quot;%%&quot; inserts a single percent character.
 &quot;%{name}&quot; inserts the value of the specified IPP attribute.
 &quot;%C&quot; inserts the number of copies for the current page.
 &quot;%P&quot; inserts the current page number.
 &quot;%T&quot; inserts the current date and time in common log format.
 &quot;%j&quot; inserts the job ID.
 &quot;%p&quot; inserts the printer name.
 &quot;%u&quot; inserts the username.</pre>
<p>The default is the empty string, which disables page logging. The string &quot;%p %u %j %T %P %C %{job-billing} %{job-originating-host-name} %{job-name} %{media} %{sides}&quot; creates a page log with the standard items. Use &quot;%{job-impressions-completed}&quot; to insert the number of pages (sides) that were printed, or &quot;%{job-media-sheets-completed}&quot; to insert the number of sheets that were printed.</dl>
<h2>Notes</h2>
<p>File, directory, and user configuration directives that used to be allowed in the <code>cupsd.conf</code> file are now stored in the <code><a href="/docs/linux/man/5-cups-files-conf/">cups-files.conf</a></code>(5) file instead in order to prevent certain types of privilege escalation attacks. </p>
<p> The scheduler MUST be restarted manually after making changes to the <code>cupsd.conf</code> file. On Linux this is typically done using the <code>systemctl</code>(8) command, while on macOS the <code>launchctl</code>(8) command is used instead. </p>
<p> The @LOCAL macro name can be confusing since the system running <code>cupsd</code> often belongs to a different set of subnets from its clients.</p>
<h2>Conforming To</h2>
<p>The <code>cupsd.conf</code> file format is based on the Apache HTTP Server configuration file format.</p>
<h2>Examples</h2>
<p>Log everything with a maximum log file size of 32 megabytes: </p>
<pre> AccessLogLevel all
 LogLevel debug2
 MaxLogSize 32m</pre>
<p>Require authentication for accesses from outside the 10. network: </p>
<pre> &lt;Location /&gt;
 Order allow,deny
 Allow from 10./8
 AuthType Basic
 Require valid-user
 Satisfy any
 &lt;/Location&gt;</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-classes-conf/">classes.conf</a></code>(5), <code><a href="/docs/linux/man/5-cups-files-conf/">cups-files.conf</a></code>(5), <code><a href="/docs/linux/man/8-cupsd/">cupsd</a></code>(8), <code><a href="/docs/linux/man/5-mime-convs/">mime.convs</a></code>(5), <code><a href="/docs/linux/man/5-mime-types/">mime.types</a></code>(5), <code><a href="/docs/linux/man/5-printers-conf/">printers.conf</a></code>(5), <code><a href="/docs/linux/man/5-subscriptions-conf/">subscriptions.conf</a></code>(5), CUPS Online Help (<a rel="nofollow" href="http://localhost:631/help)">http://localhost:631/help)</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2020-2022 by OpenPrinting.</p>
</p>
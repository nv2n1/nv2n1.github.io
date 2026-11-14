---
title: "cupsd-logs(8)"
name: "cupsd-logs"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cupsd-logs/"
description: "cupsd-logs – cupsd log files (access_log, error_log, and page_log)"
---

<p>cupsd-logs &#8211; cupsd log files (access_log, error_log, and page_log)</p>
<h2>Description</h2>
<p><code><a href="/docs/linux/man/8-cupsd/">cupsd</a></code>(8) normally maintains three log files: <i>access_log</i> to track requests that are submitted to the scheduler, <i>error_log</i> to track progress and errors, and <i>page_log</i> to track pages that are printed. Configuration directives in <code><a href="/docs/linux/man/5-cupsd-conf/">cupsd.conf</a></code>(5) and <code><a href="/docs/linux/man/5-cups-files-conf/">cups-files.conf</a></code>(5) control what information is logged and where it is stored.</p>
<h3>Access Log File Format</h3>
<p>The <i>access_log</i> file lists each HTTP resource that is accessed by a web browser or client. Each line is in an extended version of the so-called &quot;Common Log Format&quot; used by many web servers and web reporting tools: </p>
<pre> <i>host group user date-time </i>&quot;<i>method resource version</i>&quot; <i>status bytes
 ipp-operation ipp-status</i></pre>
<p>For example: </p>
<pre> 10.0.1.2 - - [01/Dec/2005:21:50:28 +0000] &quot;POST / HTTP/1.1&quot; 200 317
 CUPS-Get-Printers successful-ok-ignored-or-substituted-attributes
 localhost - - [01/Dec/2005:21:50:32 +0000] &quot;GET /admin HTTP/1.1&quot;
 200 0 - -
 localhost - - [01/Dec/2005:21:50:32 +0000] &quot;POST / HTTP/1.1&quot;
 200 157 CUPS-Get-Printers
 successful-ok-ignored-or-substituted-attributes
 localhost - - [01/Dec/2005:21:50:32 +0000] &quot;POST / HTTP/1.1&quot;
 200 1411 CUPS-Get-Devices -
 localhost - - [01/Dec/2005:21:50:32 +0000] &quot;GET /admin HTTP/1.1&quot;
 200 6667 - -</pre>
<p>The <i>host</i> field will normally only be an IP address unless you have enabled the HostNameLookups directive in the <i>cupsd.conf</i> file or if the IP address corresponds to your local machine. </p>
<p> The <i>group</i> field always contains &quot;-&quot;. </p>
<p> The <i>user</i> field is the authenticated username of the requesting user. If no username and password is supplied for the request then this field contains &quot;-&quot;. </p>
<p> The <i>date-time</i> field is the date and time of the request in local time and is in the format &quot;[DD/MON/YYYY:HH:MM:SS +ZZZZ]&quot;. </p>
<p> The <i>method</i> field is the HTTP method used: &quot;GET&quot;, &quot;HEAD&quot;, &quot;OPTIONS&quot;, &quot;POST&quot;, or &quot;PUT&quot;. &quot;GET&quot; requests are used to get files from the server, both for the web interface and to get configuration and log files. &quot;HEAD&quot; requests are used to get information about a resource prior to a &quot;GET&quot;. &quot;OPTIONS&quot; requests are used to upgrade connections to TLS encryption. &quot;POST&quot; requests are used for web interface forms and IPP requests. &quot;PUT&quot; requests are used to upload configuration files. </p>
<p> The <i>resource</i> field is the filename of the requested resource. </p>
<p> The <i>version</i> field is the HTTP specification version used by the client. For CUPS clients this will always be &quot;HTTP/1.1&quot;. </p>
<p> The <i>status</i> field contains the HTTP result status of the request, as follows:</p>
<dl>
<dd>
<dl>
<dt>200</p>
<dd>Successful operation.</p>
<dt>201</p>
<dd>File created/modified successfully.</p>
<dt>304</p>
<dd>The requested file has not changed.</p>
<dt>400</p>
<dd>Bad HTTP request; typically this means that you have a malicious program trying to access your server.</p>
<dt>401</p>
<dd>Unauthorized, authentication (username + password) is required.</p>
<dt>403</p>
<dd>Access is forbidden; typically this means that a client tried to access a file or resource they do not have permission to access.</p>
<dt>404</p>
<dd>The file or resource does not exist.</p>
<dt>405</p>
<dd>URL access method is not allowed; typically this means you have a web browser using your server as a proxy.</p>
<dt>413</p>
<dd>Request too large; typically this means that a client tried to print a file larger than the MaxRequestSize allows.</p>
<dt>426</p>
<dd>Upgrading to TLS-encrypted connection.</p>
<dt>500</p>
<dd>Server error; typically this happens when the server is unable to open/create a file &#8211; consult the error_log file for details.</p>
<dt>501</p>
<dd>The client requested encryption but encryption support is not enabled/compiled in.</p>
<dt>505</p>
<dd>HTTP version number not supported; typically this means that you have a malicious program trying to access your server.</dl>
</dl>
<p> The <i>bytes</i> field contains the number of bytes in the request. For POST requests the bytes field contains the number of bytes of non-IPP data that is received from the client. </p>
<p> The <i>ipp-operation</i> field contains either &quot;-&quot; for non-IPP requests or the IPP operation name for POST requests containing an IPP request. </p>
<p> The <i>ipp-status</i> field contains either &quot;-&quot; for non-IPP requests or the IPP status code name for POST requests containing an IPP response.</p>
<h3>Error Log File Format</h3>
<p>The <i>error_log</i> file lists messages from the scheduler &#8211; errors, warnings, etc. The LogLevel directive in the <code><a href="/docs/linux/man/5-cupsd-conf/">cupsd.conf</a></code>(5) file controls which messages are logged: </p>
<pre> level date-time message</pre>
<p>For example: </p>
<pre> I [20/May/1999:19:18:28 +0000] [Job 1] Queued on 'DeskJet' by 'mike'.
 D [20/May/1999:19:18:28 +0000] [Job 1] argv[0]=&quot;DeskJet&quot;
 D [20/May/1999:19:18:28 +0000] [Job 1] argv[1]=&quot;1&quot;
 D [20/May/1999:19:18:28 +0000] [Job 1] argv[2]=&quot;mike&quot;
 D [20/May/1999:19:18:28 +0000] [Job 1] argv[3]=&quot;myjob&quot;
 D [20/May/1999:19:18:28 +0000] [Job 1] argv[4]=&quot;1&quot;
 D [20/May/1999:19:18:28 +0000] [Job 1] argv[5]=&quot;media=
 na_letter_8.5x11in sides=one-sided&quot;
 D [20/May/1999:19:18:28 +0000] [Job 1] argv[6]=&quot;/var/spool/cups/
 d000001-001&quot;
 I [20/May/1999:19:21:02 +0000] [Job 2] Queued on 'DeskJet' by 'mike'.
 I [20/May/1999:19:22:24 +0000] [Job 2] Canceled by 'mike'.</pre>
<p>The <i>level</i> field contains the type of message:</p>
<dl>
<dt>A</p>
<dd>Alert message (LogLevel alert)</p>
<dt>C</p>
<dd>Critical error message (LogLevel crit)</p>
<dt>D</p>
<dd>Debugging message (LogLevel debug)</p>
<dt>d</p>
<dd>Detailed debugging message (LogLevel debug2)</p>
<dt>E</p>
<dd>Normal error message (LogLevel error)</p>
<dt>I</p>
<dd>Informational message (LogLevel info)</p>
<dt>N</p>
<dd>Notice message (LogLevel notice)</p>
<dt>W</p>
<dd>Warning message (LogLevel warn)</p>
<dt>X</p>
<dd>Emergency error message (LogLevel emerg)</dl>
<p> The <i>date-time</i> field contains the date and time of when the page started printing. The format of this field is identical to the data-time field in the <i>access_log</i> file. </p>
<p> The <i>message</i> field contains a free-form textual message. Messages from job filters are prefixed with &quot;[Job NNN]&quot; where &quot;NNN&quot; is the job ID.</p>
<h3>Page Log File Format</h3>
<p>The <i>page_log</i> file lists each page or group of pages that are sent to a printer. By default, each line contains the following information: </p>
<pre> <i>printer user job-id date-time page-number num-copies job-billing
 job-originating-host-name job-name media sides</i>
 <i>printer user job-id date-time </i><code>total </code><i>num-impressions job-billing
 job-originating-host-name job-name media sides</i></pre>
<p>For example the entries for a two page job called &quot;myjob&quot; might look like: </p>
<pre> DeskJet root 1 [20/May/1999:19:21:05 +0000] 1 1 acme-123
 localhost myjob na_letter_8.5x11in one-sided
 DeskJet root 1 [20/May/1999:19:21:05 +0000] 2 1 acme-123
 localhost myjob na_letter_8.5x11in one-sided
 DeskJet root 1 [20/May/1999:19:21:06 +0000] total 2 acme-123
 localhost myjob na_letter_8.5x11in one-sided</pre>
<p>The PageLogFormat directive in the <code><a href="/docs/linux/man/5-cupsd-conf/">cupsd.conf</a></code>(5) file can be used to change this information. </p>
<p> The <i>printer</i> field contains the name of the printer that printed the page. If you send a job to a printer class, this field will contain the name of the printer that was assigned the job. </p>
<p> The <i>user</i> field contains the name of the user (the IPP requesting-user-name attribute) that submitted this file for printing. </p>
<p> The <i>job-id</i> field contains the job number of the page being printed. </p>
<p> The <i>date-time</i> field contains the date and time of when the page started printing. The format of this field is identical to the data-time field in the <i>access_log</i> file. </p>
<p> The <i>page-number</i> and <i>num-copies</i> fields contain the page number and number of copies being printed of that page. For printers that cannot produce copies on their own, the num-copies field will always be 1. </p>
<p> Lines containing the keyword &quot;total&quot; have a <i>num-impressions</i> field instead which provides the total number of impressions (sides) that have been printed on for the job. </p>
<p> The <i>job-billing</i> field contains a copy of the job-billing or job-account-id attributes provided with the IPP Create-Job or Print-Job requests or &quot;-&quot; if neither was provided. </p>
<p> The <i>job-originating-host-name</i> field contains the hostname or IP address of the client that printed the job. </p>
<p> The <i>job-name</i> field contains a copy of the job-name attribute provided with the IPP Create-Job or Print-Job requests or &quot;-&quot; if none was provided. </p>
<p> The <i>media</i> field contains a copy of the media or media-col/media-size attribute provided with the IPP Create-Job or Print-Job requests or &quot;-&quot; if none was provided. </p>
<p> The <i>sides</i> field contains a copy of the sides attribute provided with the IPP Create-Job or Print-Job requests or &quot;-&quot; if none was provided.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-cupsd/">cupsd</a></code>(8), <code><a href="/docs/linux/man/5-cupsd-conf/">cupsd.conf</a></code>(5), <code><a href="/docs/linux/man/5-cups-files-conf/">cups-files.conf</a></code>(5), CUPS Online Help (<a rel="nofollow" href="http://localhost:631/help)">http://localhost:631/help)</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2007-2014 by Apple Inc.</p>

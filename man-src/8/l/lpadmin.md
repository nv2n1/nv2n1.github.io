---
title: "lpadmin(8)"
name: "lpadmin"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lpadmin/"
description: "lpadmin – configure cups printers and classes"
---

<p>lpadmin &#8211; configure cups printers and classes</p>
<h2>Synopsis</h2>
<p><code>lpadmin</code> [ <code>-E</code> ] [ <code>-U</code> <i>username</i> ] [ <code>-h </code><i>server</i>[<code>:</code><i>port</i>] ] <code>-d</code> <i>destination</i><br />
 <code>lpadmin</code> [ <code>-E</code> ] [ <code>-U</code> <i>username</i> ] [ <code>-h </code><i>server</i>[<code>:</code><i>port</i>] ] <code>-p</code> <i>destination</i> [ <code>-R</code> <i>name-default</i> ] <i>option(s)</i><br />
 <code>lpadmin</code> [ <code>-E</code> ] [ <code>-U</code> <i>username</i> ] [ <code>-h </code><i>server</i>[<code>:</code><i>port</i>] ] <code>-x</code> <i>destination</i></p>
<h2>Description</h2>
<p><code>lpadmin</code> configures printer and class queues provided by CUPS. It can also be used to set the server default printer or class. </p>
<p> When specified before the <i>-d</i>, <i>-p</i>, or <i>-x</i> options, the <i>-E</i> option forces encryption when connecting to the server. </p>
<p> The first form of the command (<i>-d</i>) sets the default printer or class to <i>destination</i>. Subsequent print jobs submitted via the <code><a href="/docs/linux/man/1-lp/">lp</a></code>(1) or <code><a href="/docs/linux/man/1-lpr/">lpr</a></code>(1) commands will use this destination unless the user specifies otherwise with the <code><a href="/docs/linux/man/1-lpoptions/">lpoptions</a></code>(1) command. </p>
<p> The second form of the command (<i>-p</i>) configures the named printer or class. The additional options are described below. </p>
<p> The third form of the command (<i>-x</i>) deletes the printer or class <i>destination</i>. Any jobs that are pending for the destination will be removed and any job that is currently printed will be aborted.</p>
<h2>Options</h2>
<p>The following options are recognized when configuring a printer queue:</p>
<dl>
<dt><code>-c </code><i>class</i></p>
<dd>Adds the named <i>printer</i> to <i>class</i>. If <i>class</i> does not exist it is created automatically.</p>
<dt><code>-m </code><i>model</i></p>
<dd>Sets a standard PPD file for the printer from the <i>model</i> directory or using one of the driver interfaces. Use the <i>-m</i> option with the <code><a href="/docs/linux/man/8-lpinfo/">lpinfo</a></code>(8) command to get a list of supported models. The model &quot;raw&quot; clears any existing PPD file and the model &quot;everywhere&quot; queries the printer referred to by the specified IPP <i>device-uri</i>. Note: Models other than &quot;everywhere&quot; are deprecated and will not be supported in a future version of CUPS.</p>
<dt><code>-o cupsIPPSupplies=true</code></p>
<dd>
<dt><code>-o cupsIPPSupplies=false</code></p>
<dd>Specifies whether IPP supply level values should be reported.</p>
<dt><code>-o cupsSNMPSupplies=true</code></p>
<dd>
<dt><code>-o cupsSNMPSupplies=false</code></p>
<dd>Specifies whether SNMP supply level (RFC 3805) values should be reported.</p>
<dt><code>-o job-k-limit=</code><i>value</i></p>
<dd>Sets the kilobyte limit for per-user quotas. The value is an integer number of kilobytes; one kilobyte is 1024 bytes.</p>
<dt><code>-o job-page-limit=</code><i>value</i></p>
<dd>Sets the page limit for per-user quotas. The value is the integer number of pages that can be printed; double-sided pages are counted as two pages.</p>
<dt><code>-o job-quota-period=</code><i>value</i></p>
<dd>Sets the accounting period for per-user quotas. The value is an integer number of seconds; 86,400 seconds are in one day.</p>
<dt><code>-o job-sheets-default=</code><i>banner</i></p>
<dd>
<dt><code>-o job-sheets-default=</code><i>banner</i><code>,</code><i>banner</i></p>
<dd>Sets the default banner page(s) to use for print jobs.</p>
<dt><code>-o </code><i>name</i><code>=</code><i>value</i></p>
<dd>Sets a PPD option for the printer. PPD options can be listed using the <i>-l</i> option with the <code><a href="/docs/linux/man/1-lpoptions/">lpoptions</a></code>(1) command.</p>
<dt><code>-o </code><i>name</i><code>-default=</code><i>value</i></p>
<dd>Sets a default server-side option for the destination. Any print-time option can be defaulted, e.g., &quot;-o number-up-default=2&quot; to set the default &quot;number-up&quot; option value to 2.</p>
<dt><code>-o port-monitor=</code><i>name</i></p>
<dd>Sets the binary communications program to use when printing, &quot;none&quot;, &quot;bcp&quot;, or &quot;tbcp&quot;. The default program is &quot;none&quot;. The specified port monitor must be listed in the printer&#8217;s PPD file.</p>
<dt><code>-o printer-error-policy=</code><i>name</i></p>
<dd>Sets the policy for errors such as printers that cannot be found or accessed, don&#8217;t support the format being printed, fail during submission of the print data, or cause one or more filters to crash. The name must be one of &quot;abort-job&quot; (abort the job on error), &quot;retry-job&quot; (retry the job at a future time), &quot;retry-current-job&quot; (retry the current job immediately), or &quot;stop-printer&quot; (stop the printer on error). The default error policy is &quot;stop-printer&quot; for printers and &quot;retry-current-job&quot; for classes.</p>
<dt><code>-o printer-is-shared=true</code></p>
<dd>
<dt><code>-o printer-is-shared=false</code></p>
<dd>Sets the destination to shared/published or unshared/unpublished. Shared/published destinations are publicly announced by the server on the LAN based on the browsing configuration in <i>cupsd.conf</i>, while unshared/unpublished destinations are not announced. The default value is &quot;true&quot;.</p>
<dt><code>-o printer-op-policy=</code><i>name</i></p>
<dd>Sets the IPP operation policy associated with the destination. The name must be defined in the <i>cupsd.conf</i> in a Policy section. The default operation policy is &quot;default&quot;.</p>
<dt><code>-R </code><i>name</i><code>-default</code></p>
<dd>Deletes the named option from <i>printer</i>.</p>
<dt><code>-r </code><i>class</i></p>
<dd>Removes the named <i>printer</i> from <i>class</i>. If the resulting class becomes empty it is removed.</p>
<dt><code>-u allow:</code>{<i>user</i>|<code>@</code><i>group</i>}{<code>,</code><i>user</i>|<code>,@</code><i>group</i>}*</p>
<dd>
<dt><code>-u deny:</code>{<i>user</i>|<code>@</code><i>group</i>}{<code>,</code><i>user</i>|<code>,@</code><i>group</i>}*</p>
<dd>
<dt><code>-u allow:all</code></p>
<dd>
<dt><code>-u deny:none</code></p>
<dd>Sets user-level access control on a destination. Names starting with &quot;@&quot; are interpreted as UNIX groups. The latter two forms turn user-level access control off. Note: The user &#8216;root&#8217; is not granted special access &#8211; using &quot;-u allow:foo,bar&quot; will allow users &#8216;foo&#8217; and &#8216;bar&#8217; to access the printer but NOT &#8216;root&#8217;.</p>
<dt><code>-v &quot;</code><i>device-uri</i><code>&quot;</code></p>
<dd>Sets the <i>device-uri</i> attribute of the printer queue. Use the <i>-v</i> option with the <code><a href="/docs/linux/man/8-lpinfo/">lpinfo</a></code>(8) command to get a list of supported device URIs and schemes.</p>
<dt><code>-D &quot;</code><i>info</i><code>&quot;</code></p>
<dd>Provides a textual description of the destination.</p>
<dt><code>-E</code></p>
<dd>When specified before the <code>-d</code>, <code>-p</code>, or <code>-x</code> options, forces the use of TLS encryption on the connection to the scheduler. Otherwise, enables the destination and accepts jobs; this is the same as running the <code><a href="/docs/linux/man/8-cupsaccept/">cupsaccept</a></code>(8) and <code><a href="/docs/linux/man/8-cupsenable/">cupsenable</a></code>(8) programs on the destination.</p>
<dt><code>-L &quot;</code><i>location</i><code>&quot;</code></p>
<dd>Provides a textual location of the destination.</dl>
<h2>Deprecated Options</h2>
<p>The following <code>lpadmin</code> options are deprecated:</p>
<dl>
<dt><code>-i </code><i>filename</i></p>
<dd>This option historically has been used to provide either a System V interface script or (as an implementation side-effect) a PPD file. Note: Interface scripts are not supported by CUPS. PPD files and printer drivers are deprecated and will not be supported in a future version of CUPS.</p>
<dt><code>-P </code><i>ppd-file</i></p>
<dd>Specifies a PostScript Printer Description (PPD) file to use with the printer. Note: PPD files and printer drivers are deprecated and will not be supported in a future version of CUPS.</dl>
<h2>Conforming To</h2>
<p>Unlike the System V printing system, CUPS allows printer names to contain any printable character except SPACE, TAB, &quot;/&quot;, or &quot;#&quot;. Also, printer and class names are <i>not</i> case-sensitive. </p>
<p> Finally, the CUPS version of <code>lpadmin</code> may ask the user for an access password depending on the printing system configuration. This differs from the System V version which requires the root user to execute this command.</p>
<h2>Notes</h2>
<p>CUPS printer drivers and backends are deprecated and will no longer be supported in a future feature release of CUPS. Printers that do not support IPP can be supported using applications such as <code><a href="/docs/linux/man/1-ippeveprinter/">ippeveprinter</a></code>(1). </p>
<p> The CUPS version of <code>lpadmin</code> does not support all of the System V or Solaris printing system configuration options. </p>
<p> Interface scripts are not supported for security reasons. </p>
<p> The double meaning of the <code>-E</code> option is an unfortunate historical oddity. </p>
<p> The <code>lpadmin</code> command communicates with the scheduler (<code>cupsd</code>) to make changes to the printing system configuration. This configuration information is stored in several files including <i>printers.conf</i> and <i>classes.conf</i>. These files should not be edited directly and are an implementation detail of CUPS that is subject to change at any time.</p>
<h2>Example</h2>
<p>Create an IPP Everywhere print queue: </p>
<pre> lpadmin -p myprinter -E -v <a href="ipp://myprinter.local/ipp/print">ipp://myprinter.local/ipp/print</a> -m everywhere</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-cupsaccept/">cupsaccept</a></code>(8), <code><a href="/docs/linux/man/8-cupsenable/">cupsenable</a></code>(8), <code><a href="/docs/linux/man/8-lpinfo/">lpinfo</a></code>(8), <code><a href="/docs/linux/man/1-lpoptions/">lpoptions</a></code>(1), CUPS Online Help (<a rel="nofollow" href="http://localhost:631/help)">http://localhost:631/help)</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2021-2022 by OpenPrinting.</p>

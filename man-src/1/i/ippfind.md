---
title: "ippfind(1)"
name: "ippfind"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ippfind/"
description: "ippfind – find internet printing protocol printers"
---

<h2 class="name">NAME</h2>
<p> ippfind &#8211; find internet printing protocol printers </p>
<h2>SYNOPSIS</h2>
<p> <code>ippfind</code> [ <i>options</i> ] <i>regtype</i>[<code>,</code><i>subtype</i>][<code>.</code><i>domain</i><code>.</code>] &#8230; [ <i>expression</i><br />
&nbsp;&#8230;&nbsp;]<br />
 <code>ippfind</code> [ <i>options</i> ] <i>name</i>[<code>.</code><i>regtype</i>[<code>.</code><i>domain</i><code>.</code>]] &#8230; [ <i>expression</i><br />
&nbsp;&#8230;&nbsp;]<br />
 <code>ippfind</code> <code>&#8211;help</code><br />
 <code>ippfind</code> <code>&#8211;version</code></p>
<h2>DESCRIPTION</h2>
<p> <code>ippfind</code> finds services registered with a DNS server or available through local devices. Its primary purpose is to find IPP printers and show their URIs, show their current status, or run commands.</p>
<h3>REGISTRATION TYPES</h3>
<p> <code>ippfind</code> supports the following registration types:</p>
<dl>
<dt>_http._tcp</p>
<dd> HyperText Transport Protocol (HTTP, RFC 2616)</p>
<dt>_https._tcp</p>
<dd> Secure HyperText Transport Protocol (HTTPS, RFC 2818)</p>
<dt>_ipp._tcp</p>
<dd> Internet Printing Protocol (IPP, RFC 2911)</p>
<dt>_ipps._tcp</p>
<dd> Secure Internet Printing Protocol (IPPS, draft)</p>
<dt>_printer._tcp</p>
<dd> Line Printer Daemon (LPD, RFC 1179)</dl>
<h3>EXPRESSIONS</h3>
<p> <code>ippfind</code> supports expressions much like the <code><a href="/docs/linux/man/1-find/">find</a></code>(1) utility. However, unlike <code><a href="/docs/linux/man/1-find/">find</a></code>(1), <code>ippfind</code> uses POSIX regular expressions instead of shell filename matching patterns. If <i>&#8211;exec</i>, <i>-l</i>, <i>&#8211;ls</i>, <i>-p</i>, <i>&#8211;print</i>, <i>&#8211;print-name</i>, <i>-q</i>, <i>&#8211;quiet</i>, <i>-s</i>, or <i>-x</i> is not specified, <code>ippfind</code> adds <i>&#8211;print</i> to print the service URI of anything it finds. The following expressions are supported:</p>
<dl>
<dt><code>-d </code><i>regex</i></p>
<dd>
<dt><code>&#8211;domain </code><i>regex</i></p>
<dd> True if the domain matches the given regular expression.</p>
<dt><code>&#8211;false</code></p>
<dd> Always false.</p>
<dt><code>-h </code><i>regex</i></p>
<dd>
<dt><code>&#8211;host </code><i>regex</i></p>
<dd> True is the hostname matches the given regular expression.</p>
<dt><code>-l</code></p>
<dd>
<dt><code>&#8211;ls</code></p>
<dd> Lists attributes returned by Get-Printer-Attributes for IPP printers and traditional <i>find</i> &quot;-ls&quot; output for HTTP URLs. The result is true if the URI is accessible, false otherwise.</p>
<dt><code>&#8211;local</code></p>
<dd> True if the service is local to this computer.</p>
<dt><code>-N </code><i>name</i></p>
<dd>
<dt><code>&#8211;literal-name </code><i>name</i></p>
<dd> True if the service instance name matches the given name.</p>
<dt><code>-n </code><i>regex</i></p>
<dd>
<dt><code>&#8211;name </code><i>regex</i></p>
<dd> True if the service instance name matches the given regular expression.</p>
<dt><code>&#8211;path </code><i>regex</i></p>
<dd> True if the URI resource path matches the given regular expression.</p>
<dt><code>-P </code><i>number</i>[<code>&#8211;</code><i>number</i>]</p>
<dd>
<dt><code>&#8211;port </code><i>number</i>[<code>&#8211;</code><i>number</i>]</p>
<dd> True if the port matches the given number or range.</p>
<dt><code>-p</code></p>
<dd>
<dt><code>&#8211;print</code></p>
<dd> Prints the URI if the result of previous expressions is true. The result is always true.</p>
<dt><code>-q</code></p>
<dd>
<dt><code>&#8211;quiet</code></p>
<dd> Quiet mode &#8211; just returns the exit codes below.</p>
<dt><code>-r</code></p>
<dd>
<dt><code>&#8211;remote</code></p>
<dd> True if the service is not local to this computer.</p>
<dt><code>-s</code></p>
<dd>
<dt><code>&#8211;print-name</code></p>
<dd> Prints the service instance name if the result of previous expressions is true. The result is always true.</p>
<dt><code>&#8211;true</code></p>
<dd> Always true.</p>
<dt><code>-t </code><i>key</i></p>
<dd>
<dt><code>&#8211;txt </code><i>key</i></p>
<dd> True if the TXT record contains the named key.</p>
<dt><code>&#8211;txt-</code><i>key regex</i></p>
<dd> True if the TXT record contains the named key and matches the given regular expression.</p>
<dt><code>-u </code><i>regex</i></p>
<dd>
<dt><code>&#8211;uri </code><i>regex</i></p>
<dd> True if the URI matches the given regular expression.</p>
<dt><code>-x </code><i>utility </i>[ <i>argument </i>&#8230; ] <code>;</code></p>
<dd>
<dt><code>&#8211;exec </code><i>utility </i>[ <i>argument </i>&#8230; ] <code>;</code></p>
<dd> Executes the specified program if the current result is true. &quot;{foo}&quot; arguments are replaced with the corresponding value &#8211; see SUBSTITUTIONS below.</dl>
<p> Expressions may also contain modifiers:</p>
<dl>
<dt><code>( </code><i>expression </i><code>)</code></p>
<dd> Group the result of expressions.</p>
<dt><code>! </code><i>expression</i></p>
<dd>
<dt><code>&#8211;not </code><i>expression</i></p>
<dd> Unary NOT of the expression.</p>
<dt><i>expression expression</i></p>
<dd>
<dt><i>expression </i><code>&#8211;and </code><i>expression</i></p>
<dd> Logical AND of expressions.</p>
<dt><i>expression </i><code>&#8211;or </code><i>expression</i></p>
<dd> Logical OR of expressions.</dl>
<h3>SUBSTITUTIONS</h3>
<p> The substitutions for &quot;{foo}&quot; in <i>-e</i> and <i>&#8211;exec</i> are:</p>
<dl>
<dt><code>{service_domain}</code></p>
<dd> Domain name, e.g., &quot;example.com.&quot;, &quot;local.&quot;, etc.</p>
<dt><code>{service_hostname}</code></p>
<dd> Fully-qualified domain name, e.g., &quot;printer.example.com.&quot;, &quot;printer.local.&quot;, etc.</p>
<dt><code>{service_name}</code></p>
<dd> Service instance name, e.g., &quot;My Fine Printer&quot;.</p>
<dt><code>{service_port}</code></p>
<dd> Port number for server, typically 631 for IPP and 80 for HTTP.</p>
<dt><code>{service_regtype}</code></p>
<dd> DNS-SD registration type, e.g., &quot;_ipp._tcp&quot;, &quot;_http._tcp&quot;, etc.</p>
<dt><code>{service_scheme}</code></p>
<dd> URI scheme for DNS-SD registration type, e.g., &quot;ipp&quot;, &quot;http&quot;, etc.</p>
<dt><code>{}</code></p>
<dd>
<dt><code>{service_uri}</code></p>
<dd> URI for service, e.g., &quot;<a href="ipp://printer.local./ipp/print">ipp://printer.local./ipp/print</a>&quot;, &quot;<a rel="nofollow" href="http://printer.local./">http://printer.local./</a>&quot;, etc.</p>
<dt><code>{txt_</code><i>key</i><code>}</code></p>
<dd> Value of TXT record <i>key</i> (lowercase).</dl>
<h2>OPTIONS</h2>
<p> <code>ippfind</code> supports the following options:</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Show program help.</p>
<dt><code>&#8211;version</code></p>
<dd> Show program version.</p>
<dt><code>-4</code></p>
<dd> Use IPv4 when listing.</p>
<dt><code>-6</code></p>
<dd> Use IPv6 when listing.</p>
<dt><code>-T </code><i>seconds</i></p>
<dd> Specify find timeout in seconds. If 1 or less, <code>ippfind</code> stops as soon as it thinks it has found everything. The default timeout is 1 second.</p>
<dt><code>-V </code><i>version</i></p>
<dd> Specifies the IPP version when listing. Supported values are &quot;1.1&quot;, &quot;2.0&quot;, &quot;2.1&quot;, and &quot;2.2&quot;.</dl>
<h2>EXIT STATUS</h2>
<p> <code>ippfind</code> returns 0 if the result for all processed expressions is true, 1 if the result of any processed expression is false, 2 if browsing or any query or resolution failed, 3 if an undefined option or invalid expression was specified, and 4 if it ran out of memory.</p>
<h2>ENVIRONMENT</h2>
<p> When executing a program, <code>ippfind</code> sets the following environment variables for the matching service registration:</p>
<dl>
<dt><code>IPPFIND_SERVICE_DOMAIN</code></p>
<dd> Domain name, e.g., &quot;example.com.&quot;, &quot;local.&quot;, etc.</p>
<dt><code>IPPFIND_SERVICE_HOSTNAME</code></p>
<dd> Fully-qualified domain name, e.g., &quot;printer.example.com.&quot;, &quot;printer.local.&quot;, etc.</p>
<dt><code>IPPFIND_SERVICE_NAME</code></p>
<dd> Service instance name, e.g., &quot;My Fine Printer&quot;.</p>
<dt><code>IPPFIND_SERVICE_PORT</code></p>
<dd> Port number for server, typically 631 for IPP and 80 for HTTP.</p>
<dt><code>IPPFIND_SERVICE_REGTYPE</code></p>
<dd> DNS-SD registration type, e.g., &quot;_ipp._tcp&quot;, &quot;_http._tcp&quot;, etc.</p>
<dt><code>IPPFIND_SERVICE_SCHEME</code></p>
<dd> URI scheme for DNS-SD registration type, e.g., &quot;ipp&quot;, &quot;http&quot;, etc.</p>
<dt><code>IPPFIND_SERVICE_URI</code></p>
<dd> URI for service, e.g., &quot;<a href="ipp://printer.local./ipp/print">ipp://printer.local./ipp/print</a>&quot;, &quot;<a rel="nofollow" href="http://printer.local./">http://printer.local./</a>&quot;, etc.</p>
<dt><code>IPPFIND_TXT_</code><i>KEY</i></p>
<dd> Values of TXT record <i>KEY</i> (uppercase).</dl>
<h2>EXAMPLES</h2>
<p> To show the status of all registered IPP printers on your network, run: </p>
<pre>
    ippfind --ls
</pre>
<p> Similarly, to send a PostScript test page to every PostScript printer, run: </p>
<pre><code>
ippfind-- txt - pdl application / postscript-- exec ipptool - f onepage - letter.ps '{}' print - job.test \;
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ipptool/">ipptool</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2021-2022 by OpenPrinting. </p>
<h2>Index</h2>

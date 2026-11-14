---
title: "ipptool(1)"
name: "ipptool"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipptool/"
description: "ipptool – perform internet printing protocol requests"
---

<h2 class="name">NAME</h2>
<p> ipptool &#8211; perform internet printing protocol requests </p>
<h2>SYNOPSIS</h2>
<p> <code>ipptool</code> [ <code>&#8211;help</code> ] [ <code>&#8211;ippserver</code> <i>filename</i> ] [ <code>&#8211;stop-after-include-error</code> ] [ <code>&#8211;version</code> ] [ <code>-4</code> ] [ <code>-6</code> ] [ <code>-C</code> ] [ <code>-E</code> ] [ <code>-I</code> ] [ <code>-L</code> ] [ <code>-P</code> <i>filename.plist</i> ] [ <code>-S</code> ] [ <code>-T</code> <i>seconds</i> ] [ <code>-V</code> <i>version</i> ] [ <code>-X</code> ] [ <code>-c</code> ] [ <code>-d</code> <i>name=value</i> ] [ <code>-f</code> <i>filename</i> ] [ <code>-h</code> ] [ <code>-i</code> <i>seconds</i> ] [ <code>-j</code> ] [ <code>-n</code> <i>repeat-count</i> ] [ <code>-q</code> ] [ <code>-t</code> ] [ <code>-v ]</code> <i>printer-uri</i> <i>testfile</i> [ &#8230; <i>testfile</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>ipptool</code> sends IPP requests to the specified <i>printer-uri</i> and tests and/or displays the results. Each named <i>testfile</i> defines one or more requests, including the expected response status, attributes, and values. Output is either a plain text, formatted text, CSV, or XML report on the standard output, with a non-zero exit status indicating that one or more tests have failed. The <i>testfile</i> format is described in <code><a href="/docs/linux/man/5-ipptoolfile/">ipptoolfile</a></code>(5).</p>
<h2>OPTIONS</h2>
<p> The following options are recognized by <code>ipptool:</code></p>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Shows program help.</p>
<dt><code>&#8211;ippserver </code><i>filename</i></p>
<dd> Specifies that the test results should be written to the named <code>ippserver</code> attributes file.</p>
<dt><code>&#8211;stop-after-include-error</code></p>
<dd> Tells <code>ipptool</code> to stop if an error occurs in an included file. Normally <code>ipptool</code> will continue with subsequent tests after the INCLUDE directive.</p>
<dt><code>&#8211;version</code></p>
<dd> Shows the version of <code>ipptool</code> being used.</p>
<dt><code>-4</code></p>
<dd> Specifies that <code>ipptool</code> must connect to the printer or server using IPv4.</p>
<dt><code>-6</code></p>
<dd> Specifies that <code>ipptool</code> must connect to the printer or server using IPv6.</p>
<dt><code>-C</code></p>
<dd> Specifies that requests should be sent using the HTTP/1.1 &quot;Transfer-Encoding: chunked&quot; header, which is required for conformance by all versions of IPP. The default is to use &quot;Transfer-Encoding: chunked&quot; for requests with attached files and &quot;Content-Length:&quot; for requests without attached files.</p>
<dt><code>-E</code></p>
<dd> Forces TLS encryption when connecting to the server using the HTTP &quot;Upgrade&quot; header.</p>
<dt><code>-I</code></p>
<dd> Specifies that <code>ipptool</code> will continue past errors.</p>
<dt><code>-L</code></p>
<dd> Specifies that requests should be sent using the HTTP/1.0 &quot;Content-Length:&quot; header, which is required for conformance by all versions of IPP. The default is to use &quot;Transfer-Encoding: chunked&quot; for requests with attached files and &quot;Content-Length:&quot; for requests without attached files.</p>
<dt><code>-P</code><i>&nbsp;filename.plist</i></p>
<dd> Specifies that the test results should be written to the named XML (Apple plist) file in addition to the regular test report (<code>-t</code>). This option is incompatible with the <code>-i</code> (interval) and <code>-n</code> (repeat-count) options.</p>
<dt><code>-S</code></p>
<dd> Forces (dedicated) TLS encryption when connecting to the server.</p>
<dt><code>-T</code><i>&nbsp;seconds</i></p>
<dd> Specifies a timeout for IPP requests in seconds.</p>
<dt><code>-V</code><i>&nbsp;version</i></p>
<dd> Specifies the default IPP version to use: 1.0, 1.1, 2.0, 2.1, or 2.2. If not specified, version 1.1 is used.</p>
<dt><code>-X</code></p>
<dd> Specifies that XML (Apple plist) output is desired instead of the plain text report. This option is incompatible with the <code>-i</code> (interval) and <code>-n</code> (repeat-count) options.</p>
<dt><code>-c</code></p>
<dd> Specifies that CSV (comma-separated values) output is desired instead of the plain text output.</p>
<dt><code>-d</code><i>&nbsp;name=value</i></p>
<dd> Defines the named variable.</p>
<dt><code>-f</code><i>&nbsp;filename</i></p>
<dd> Defines the default request filename for tests.</p>
<dt><code>-h</code></p>
<dd> Validate HTTP response headers.</p>
<dt><code>-i</code><i>&nbsp;seconds</i></p>
<dd> Specifies that the (last) <i>testfile</i> should be repeated at the specified interval. This option is incompatible with the <code>-X</code> (XML plist output) option.</p>
<dt><code>-j</code></p>
<dd> Specifies that <code>ipptool</code> will produce JSON output.</p>
<dt><code>-l</code></p>
<dd> Specifies that plain text output is desired.</p>
<dt><code>-n</code><i>&nbsp;repeat-count</i></p>
<dd> Specifies that the (last) <i>testfile</i> should be repeated the specified number of times. This option is incompatible with the <i>-X</i> (XML plist output) option.</p>
<dt><code>-q</code></p>
<dd> Be quiet and produce no output.</p>
<dt><code>-t</code></p>
<dd> Specifies that CUPS test report output is desired instead of the plain text output.</p>
<dt><code>-v</code></p>
<dd> Specifies that all request and response attributes should be output in CUPS test mode (<code>-t</code>). This is the default for XML output.</dl>
<h2>EXIT STATUS</h2>
<p> The <code>ipptool</code> program returns 0 if all tests were successful and 1 otherwise.</p>
<h2>FILES</h2>
<p> The following standard files are available: </p>
<pre>
    color.jpg
    create-printer-subscription.test
    document-a4.pdf
    document-a4.ps
    document-letter.pdf
    document-letter.ps
    get-completed-jobs.test
    get-jobs.test
    get-notifications.test
    get-printer-attributes.test
    get-subscriptions.test
    gray.jpg
    ipp-1.1.test
    ipp-2.0.test
    ipp-2.1.test
    ipp-2.2.test
    ipp-everywhere.test
    onepage-a4.pdf
    onepage-a4.ps
    onepage-letter.pdf
    onepage-letter.ps
    print-job.test
    print-job-deflate.test
    print-job-gzip.test
    testfile.jpg
    testfile.pcl
    testfile.pdf
    testfile.ps
    testfile.txt
    validate-job.test
</pre>
<h2>CONFORMING TO</h2>
<p> The <code>ipptool</code> program is unique to CUPS and conforms to the Internet Printing Protocol up to version 2.2.</p>
<h2>EXAMPLES</h2>
<p> Get a list of completed jobs for &quot;myprinter&quot;: </p>
<pre>
    ipptool <a href="ipp://localhost/printers/myprinter">ipp://localhost/printers/myprinter</a> get-completed-jobs.test
</pre>
<p> Send email notifications to &quot;user [at] example.com&quot; when &quot;myprinter&quot; changes: </p>
<pre>
    ipptool -d recipient=mailto:user [at] example.com \
        <a href="ipp://localhost/printers/myprinter">ipp://localhost/printers/myprinter</a> create-printer-subscription.test
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-ipptoolfile/">ipptoolfile</a></code>(5), IANA IPP Registry (<a rel="nofollow" href="https://www.iana.org/assignments/ipp-registrations">https://www.iana.org/assignments/ipp-registrations</a>), PWG Internet Printing Protocol Workgroup (<a rel="nofollow" href="https://www.pwg.org/ipp)">https://www.pwg.org/ipp)</a> RFC 8011 (<a rel="nofollow" href="https://datatracker.ietf.org/doc/html/rfc8011">https://datatracker.ietf.org/doc/html/rfc8011</a>),</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2021-2022 by OpenPrinting. </p>
<h2>Index</h2>

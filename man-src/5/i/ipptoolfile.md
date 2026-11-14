---
title: "ipptoolfile(5)"
name: "ipptoolfile"
section: "5"
letter: "i"
url: "/docs/linux/man/5-ipptoolfile/"
description: "ipptoolfile – ipptool file format"
---

<p>ipptoolfile &#8211; ipptool file format</p>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/1-ipptool/">ipptool</a></code>(1) program accepts free-form plain text files that describe one or more IPP requests. Comments start with the &quot;#&quot; character and continue to the end of the line. Each request is enclosed by curly braces, for example: </p>
<pre> # This is a comment
 {
 # The name of the test
 NAME &quot;Print PDF File&quot;
 # The request to send
 OPERATION Print-Job
 GROUP operation-attributes-tag
 ATTR charset attributes-charset utf-8
 ATTR language attributes-natural-language en
 ATTR uri printer-uri $uri
 ATTR name requesting-user-name $user
 ATTR mimeMediaType document-format application/pdf
 GROUP job-attributes-tag
 ATTR collection media-col {
 # US Letter plain paper from the &quot;main&quot; tray
 MEMBER collection media-size {
 MEMBER integer x-dimension 21590
 MEMBER integer y-dimension 27940
 }
 MEMBER integer media-top-margin 423
 MEMBER integer media-bottom-margin 423
 MEMBER integer media-left-margin 423
 MEMBER integer media-right-margin 423
 MEMBER keyword media-source &quot;main&quot;
 MEMBER keyword media-type &quot;stationery&quot;
 }
 FILE testfile.pdf
 # The response to expect
 STATUS successful-ok
 EXPECT job-id OF-TYPE integer WITH-VALUE &gt;0
 EXPECT job-uri OF-TYPE uri
 }
 {
 # The name of the test
 NAME &quot;Wait for Job to Complete&quot;
 # The request to send
 OPERATION Get-Job-Attributes
 GROUP operation-attributes-tag
 ATTR charset attributes-charset utf-8
 ATTR language attributes-natural-language en
 ATTR uri printer-uri $uri
 ATTR integer job-id $job-id
 ATTR name requesting-user-name $user
 # The response to expect
 STATUS successful-ok
 EXPECT job-id OF-TYPE integer WITH-VALUE $job-id
 EXPECT job-uri OF-TYPE uri
 EXPECT job-state OF-TYPE enum WITH-VALUE &gt;5 REPEAT-NO-MATCH
 EXPECT job-originating-user-name OF-TYPE name WITH-VALUE &quot;$user&quot;
 # Show the job state until completed...
 DISPLAY job-state
 DISPLAY job-state-reasons
 }</pre>
<h3>Top-Level Directives</h3>
<p>The following directives can be used outside of a <i>test</i>:</p>
<dl>
<dt><code>{ </code><i>test </i><code>}</code></p>
<dd>Defines a test.</p>
<dt><code>DEFINE </code><i>variable-name value</i></p>
<dd>Defines the named variable to the given value. This is equivalent to specifying <i>-d variable-name=value</i> on the <code><a href="/docs/linux/man/8-ipptool/">ipptool</a></code>(8) command-line.</p>
<dt><code>DEFINE-DEFAULT </code><i>variable-name value</i></p>
<dd>Defines the named variable to the given value if it does not already have a value.</p>
<dt><code>FILE-ID &quot;</code><i>identifier</i><code>&quot;</code></p>
<dd>Specifies an identifier string for the current file.</p>
<dt><code>IGNORE-ERRORS yes</code></p>
<dd>
<dt><code>IGNORE-ERRORS no</code></p>
<dd>Specifies whether, by default, <code><a href="/docs/linux/man/8-ipptool/">ipptool</a></code>(8) will ignore errors and continue with subsequent tests.</p>
<dt><code>INCLUDE &quot;</code><i>filename</i><code>&quot;</code></p>
<dd>
<dt><code>INCLUDE &lt;</code><i>filename</i><code>&gt;</code></p>
<dd>Includes another test file. The first form includes a file relative to the current test file, while the second form includes a file from the <code><a href="/docs/linux/man/8-ipptool/">ipptool</a></code>(8) include directory.</p>
<dt><code>INCLUDE-IF-DEFINED </code><i>name </i><code>&quot;</code><i>filename</i><code>&quot;</code></p>
<dd>
<dt><code>INCLUDE-IF-DEFINED </code><i>name </i><code>&lt;</code><i>filename</i><code>&gt;</code></p>
<dd>Includes another test file if the named variable is defined. The first form includes a file relative to the current test file, while the second form includes a file from the <code><a href="/docs/linux/man/8-ipptool/">ipptool</a></code>(8) include directory.</p>
<dt><code>INCLUDE-IF-NOT-DEFINED </code><i>name </i><code>&quot;</code><i>filename</i><code>&quot;</code></p>
<dd>
<dt><code>INCLUDE-IF-NOT-DEFINED </code><i>name </i><code>&lt;</code><i>filename</i><code>&gt;</code></p>
<dd>Includes another test file if the named variable is not defined. The first form includes a file relative to the current test file, while the second form includes a file from the <code><a href="/docs/linux/man/8-ipptool/">ipptool</a></code>(8) include directory.</p>
<dt><code>SKIP-IF-DEFINED </code><i>variable-name</i></p>
<dd>
<dt><code>SKIP-IF-NOT-DEFINED </code><i>variable-name</i></p>
<dd>Specifies that the remainder of the test file should be skipped when the variable is or is not defined.</p>
<dt><code>STOP-AFTER-INCLUDE-ERROR no</code></p>
<dd>
<dt><code>STOP-AFTER-INCLUDE-ERROR yes</code></p>
<dd>Specifies whether tests will be stopped after an error in an included file.</p>
<dt><code>TRANSFER auto</code></p>
<dd>Specifies that tests will, by default, use &quot;Transfer-Encoding: chunked&quot; for requests with attached files and &quot;Content-Length:&quot; for requests without attached files.</p>
<dt><code>TRANSFER chunked</code></p>
<dd>Specifies that tests will, by default, use the HTTP/1.1 &quot;Transfer-Encoding: chunked&quot; header. This is the default and is equivalent to specifying <i>-c</i> on the <code><a href="/docs/linux/man/8-ipptool/">ipptool</a></code>(8) command-line. Support for chunked requests is required for conformance with all versions of IPP.</p>
<dt><code>TRANSFER length</code></p>
<dd>Specifies that tests will, by default, use the HTTP/1.0 &quot;Content-Length:&quot; header. This is equivalent to specifying <i>-l</i> on the <code><a href="/docs/linux/man/8-ipptool/">ipptool</a></code>(8) command-line. Support for content length requests is required for conformance with all versions of IPP.</p>
<dt><code>VERSION 1.0</code></p>
<dd>
<dt><code>VERSION 1.1</code></p>
<dd>
<dt><code>VERSION 2.0</code></p>
<dd>
<dt><code>VERSION 2.1</code></p>
<dd>
<dt><code>VERSION 2.2</code></p>
<dd>Specifies the default IPP version number to use for the tests that follow.</dl>
<h3>Test Directives</h3>
<p>The following directives are understood within a <i>test</i>:</p>
<dl>
<dt><code>ATTR </code><i>out-of-band-tag attribute-name</i></p>
<dd>
<dt><code>ATTR </code><i>tag attribute-name value(s)</i></p>
<dd>Adds an attribute to the test request. Out-of-band tags (admin-define, delete-attribute, no-value, not-settable, unknown, unsupported) have no value. Values for other tags are delimited by the comma (&quot;,&quot;) character &#8211; escape commas using the &quot;\&quot; character. Common attributes and values are listed in the IANA IPP registry &#8211; see references below.</p>
<dt><code>ATTR collection </code><i>attribute-name </i><code>{ MEMBER </code><i>tag member-name value(s) &#8230; </i><code>}</code> [ <i>&#8230; </i><code>,{ </code><i>&#8230; </i><code>} </code>]</p>
<dd>Adds a collection attribute to the test request. Member attributes follow the same syntax as regular attributes and can themselves be nested collections. Multiple collection values can be supplied as needed, separated by commas.</p>
<dt><code>COMPRESSION deflate</code></p>
<dd>
<dt><code>COMPRESSION gzip</code></p>
<dd>
<dt><code>COMPRESSION none</code></p>
<dd>Uses the specified compression on the document data following the attributes in a Print-Job or Send-Document request.</p>
<dt><code>DELAY </code><i>seconds</i>[<i>,repeat-seconds</i>]</p>
<dd>Specifies a delay in seconds before this test will be run. If two values are specified, the second value is used as the delay between repeated tests.</p>
<dt><code>DISPLAY </code><i>attribute-name</i></p>
<dd>Specifies that value of the named attribute should be output as part of the test report.</p>
<dt><code>EXPECT </code><i>attribute-name </i>[ <i>predicate(s) </i>]</p>
<dd>
<dt><code>EXPECT ?</code><i>attribute-name predicate(s)</i></p>
<dd>
<dt><code>EXPECT !</code><i>attribute-name</i></p>
<dd>Specifies that the response must/may/must not include the named attribute. Additional requirements can be added as predicates &#8211; see the &quot;EXPECT PREDICATES&quot; section for more information on predicates. Attribute names can specify member attributes by separating the attribute and member names with the forward slash, for example &quot;media-col/media-size/x-dimension&quot;.</p>
<dt><code>EXPECT-ALL </code><i>attribute-name </i>[ <i>predicate(s) </i>]</p>
<dd>
<dt><code>EXPECT-ALL ?</code><i>attribute-name predicate(s)</i></p>
<dd>Specifies that the response must/may include the named attribute and that all occurrences of that attribute must match the given predicates.</p>
<dt><code>FILE filename</code></p>
<dd>Specifies a file to include at the end of the request. This is typically used when sending a test print file.</p>
<dt><code>GROUP tag</code></p>
<dd>Specifies the group tag for subsequent attributes in the request.</p>
<dt><code>IGNORE-ERRORS yes</code></p>
<dd>
<dt><code>IGNORE-ERRORS no</code></p>
<dd>Specifies whether <code><a href="/docs/linux/man/8-ipptool/">ipptool</a></code>(8) will ignore errors and continue with subsequent tests.</p>
<dt><code>MONITOR-PRINTER-STATE </code>[ <i>printer-uri </i>] <code>{ EXPECT </code><i>attribute-name </i>[ <i>predicate(s) </i>] <code>}</code></p>
<dd>Specifies printer state monitoring tests to run in parallel with the test operation. The monitoring tests will run until all of the <code>EXPECT</code> conditions are satisfied or the primary test operation has completed, whichever occurs first.</p>
<dt><code>NAME &quot;</code><i>literal string</i><code>&quot;</code></p>
<dd>Specifies the human-readable name of the test.</p>
<dt><code>OPERATION </code><i>operation-code</i></p>
<dd>Specifies the operation to be performed.</p>
<dt><code>PASS-IF-DEFINED </code><i>variable-name</i></p>
<dd>
<dt><code>PASS-IF-NOT-DEFINED </code><i>variable-name</i></p>
<dd>Specifies that the current test should be passed automatically when the variable is or is not defined.</p>
<dt><code>PAUSE &quot;</code><i>message</i><code>&quot;</code></p>
<dd>Displays the provided message and waits for the user to press a key to continue.</p>
<dt><code>REQUEST-ID </code><i>number</i></p>
<dd>
<dt><code>REQUEST-ID random</code></p>
<dd>Specifies the request-id value to use in the request, either an integer or the word &quot;random&quot; to use a randomly generated value (the default).</p>
<dt><code>RESOURCE </code><i>path</i></p>
<dd>Specifies an alternate resource path that is used for the HTTP POST request. The default is the resource from the URI provided to the <code><a href="/docs/linux/man/8-ipptool/">ipptool</a></code>(8) program.</p>
<dt><code>SKIP-IF-DEFINED </code><i>variable-name</i></p>
<dd>
<dt><code>SKIP-IF-NOT-DEFINED </code><i>variable-name</i></p>
<dd>Specifies that the current test should be skipped when the variable is or is not defined.</p>
<dt><code>SKIP-PREVIOUS-ERROR yes</code></p>
<dd>
<dt><code>SKIP-PREVIOUS-ERROR no</code></p>
<dd>Specifies whether <code><a href="/docs/linux/man/8-ipptool/">ipptool</a></code>(8) will skip the current test if the previous test resulted in an error/failure.</p>
<dt><code>STATUS </code><i>status-code </i>[ <i>predicate</i> ]</p>
<dd>Specifies an expected response status-code value. Additional requirements can be added as predicates &#8211; see the &quot;STATUS PREDICATES&quot; section for more information on predicates.</p>
<dt><code>TEST-ID &quot;</code><i>identifier</i>&quot;</p>
<dd>Specifies an identifier string for the current test.</p>
<dt><code>TRANSFER auto</code></p>
<dd>Specifies that this test will use &quot;Transfer-Encoding: chunked&quot; if it has an attached file or &quot;Content-Length:&quot; otherwise.</p>
<dt><code>TRANSFER chunked</code></p>
<dd>Specifies that this test will use the HTTP/1.1 &quot;Transfer-Encoding: chunked&quot; header.</p>
<dt><code>TRANSFER length</code></p>
<dd>Specifies that this test will use the HTTP/1.0 &quot;Content-Length:&quot; header.</p>
<dt><code>VERSION 1.0</code></p>
<dd>
<dt><code>VERSION 1.1</code></p>
<dd>
<dt><code>VERSION 2.0</code></p>
<dd>
<dt><code>VERSION 2.1</code></p>
<dd>
<dt><code>VERSION 2.2</code></p>
<dd>Specifies the IPP version number to use for this test.</dl>
<h3>Expect Predicates</h3>
<p>The following predicates are understood following the <code>EXPECT</code> test directive:</p>
<dl>
<dt><code>COUNT </code><i>number</i></p>
<dd>Requires the <code>EXPECT</code> attribute to have the specified number of values.</p>
<dt><code>DEFINE-MATCH </code><i>variable-name</i></p>
<dd>Defines the variable to &quot;1&quot; when the <code>EXPECT</code> condition matches. A side-effect of this predicate is that this <code>EXPECT</code> will never fail a test.</p>
<dt><code>DEFINE-NO-MATCH </code><i>variable-name</i></p>
<dd>Defines the variable to &quot;1&quot; when the <code>EXPECT</code> condition does not match. A side-effect of this predicate is that this <code>EXPECT</code> will never fail a test.</p>
<dt><code>DEFINE-VALUE </code><i>variable-name</i></p>
<dd>Defines the variable to the value of the attribute when the <code>EXPECT</code> condition matches. A side-effect of this predicate is that this <code>EXPECT</code> will never fail a test.</p>
<dt><code>DISPLAY-MATCH </code><i>&quot;message&quot;</i></p>
<dd>Displays the specified message when the <code>EXPECT</code> condition matches.</p>
<dt><code>IF-DEFINED </code><i>variable-name</i></p>
<dd>Makes the <code>EXPECT</code> conditions apply only if the specified variable is defined.</p>
<dt><code>IF-NOT-DEFINED </code><i>variable-name</i></p>
<dd>Makes the <code>EXPECT</code> conditions apply only if the specified variable is not defined.</p>
<dt><code>IN-GROUP </code><i>tag</i></p>
<dd>Requires the <code>EXPECT</code> attribute to be in the specified group tag.</p>
<dt><code>OF-TYPE </code><i>tag[(limits)|tag|&#8230;]</i></p>
<dd>Requires the <code>EXPECT</code> attribute to use one of the specified value tag(s). Most value tags also support the specification of limits in parenthesis, for example &quot;name(42)&quot; would allow nameWith/WithoutLanguage strings up to 42 octets in length, &quot;name(4:MAX)&quot; would allow nameWith/WithoutLanguage strings between 4 and 255 octets in length, and &quot;integer(-273:MAX)&quot; would allow integers between -273 and 2147483647.</p>
<dt><code>REPEAT-LIMIT </code><i>number</i></p>
<dd>Specifies the maximum number of times to repeat if the <code>REPEAT-MATCH</code> or <code>REPEAT-NO-MATCH</code> predicate is specified. The default value is 1000.</p>
<dt><code>REPEAT-MATCH</code></p>
<dd>
<dt><code>REPEAT-NO-MATCH</code></p>
<dd>Specifies that the current test should be repeated when the <code>EXPECT</code> condition matches or does not match.</p>
<dt><code>SAME-COUNT-AS </code><i>attribute-name</i></p>
<dd>Requires the <code>EXPECT</code> attribute to have the same number of values as the specified parallel attribute.</p>
<dt><code>WITH-ALL-HOSTNAMES &quot;</code><i>literal string</i><code>&quot;</code></p>
<dd>
<dt><code>WITH-ALL-HOSTNAMES &quot;/</code><i>regular expression</i><code>/&quot;</code></p>
<dd>Requires that all URI values contain a matching hostname.</p>
<dt><code>WITH-ALL-RESOURCES &quot;</code><i>literal string</i><code>&quot;</code></p>
<dd>
<dt><code>WITH-ALL-RESOURCES &quot;/</code><i>regular expression</i><code>/&quot;</code></p>
<dd>Requires that all URI values contain a matching resource (including leading /).</p>
<dt><code>WITH-ALL-SCHEMES &quot;</code><i>literal string</i><code>&quot;</code></p>
<dd>
<dt><code>WITH-ALL-SCHEMES &quot;/</code><i>regular expression</i><code>/&quot;</code></p>
<dd>Requires that all URI values contain a matching scheme.</p>
<dt><code>WITH-ALL-VALUES &quot;</code><i>literal string</i><code>&quot;</code></p>
<dd>Requires that all values of the <code>EXPECT</code> attribute match the literal string. Comparisons are case-sensitive.</p>
<dt><code>WITH-ALL-VALUES &lt;</code><i>number</i></p>
<dd>
<dt><code>WITH-ALL-VALUES =</code><i>number</i></p>
<dd>
<dt><code>WITH-ALL-VALUES &gt;</code><i>number</i></p>
<dd>
<dt><code>WITH-ALL-VALUES </code><i>number</i>[<i>,&#8230;,number</i>]</p>
<dd>Requires that all values of the <code>EXPECT</code> attribute match the number(s) or numeric comparison. When comparing rangeOfInteger values, the &quot;&lt;&quot; and &quot;&gt;&quot; operators only check the upper bound of the range.</p>
<dt><code>WITH-ALL-VALUES &quot;false&quot;</code></p>
<dd>
<dt><code>WITH-ALL-VALUES &quot;true&quot;</code></p>
<dd>Requires that all values of the <code>EXPECT</code> attribute match the boolean value given.</p>
<dt><code>WITH-ALL-VALUES &quot;/</code><i>regular expression</i><code>/&quot;</code></p>
<dd>Requires that all values of the <code>EXPECT</code> attribute match the regular expression, which must conform to the POSIX regular expression syntax. Comparisons are case-sensitive.</p>
<dt><code>WITH-DISTINCT-VALUES</code></p>
<dd>Requires that all values of the <code>EXPECT</code> attribute are unique. Comparisons are case-sensitive. Only charset, collection, enum, integer, keyword, mimeMediaType, naturalLanguage, rangeOfInteger, resolution, uriScheme attributes support this predicate.</p>
<dt><code>WITH-HOSTNAME &quot;</code><i>literal string</i><code>&quot;</code></p>
<dd>
<dt><code>WITH-HOSTNAME &quot;/</code><i>regular expression</i><code>/&quot;</code></p>
<dd>Requires that at least one URI value contains a matching hostname.</p>
<dt><code>WITH-RESOURCE &quot;</code><i>literal string</i><code>&quot;</code></p>
<dd>
<dt><code>WITH-RESOURCE &quot;/</code><i>regular expression</i><code>/&quot;</code></p>
<dd>Requires that at least one URI value contains a matching resource (including leading /).</p>
<dt><code>WITH-SCHEME &quot;</code><i>literal string</i><code>&quot;</code></p>
<dd>
<dt><code>WITH-SCHEME &quot;/</code><i>regular expression</i><code>/&quot;</code></p>
<dd>Requires that at least one URI value contains a matching scheme.</p>
<dt><code>WITH-VALUE &quot;</code><i>literal string</i><code>&quot;</code></p>
<dd>Requires that at least one value of the <code>EXPECT</code> attribute matches the literal string. Comparisons are case-sensitive.</p>
<dt><code>WITH-VALUE &lt;</code><i>number</i></p>
<dd>
<dt><code>WITH-VALUE =</code><i>number</i></p>
<dd>
<dt><code>WITH-VALUE &gt;</code><i>number</i></p>
<dd>
<dt><code>WITH-VALUE </code><i>number</i>[<i>,&#8230;,number</i>]</p>
<dd>Requires that at least one value of the <code>EXPECT</code> attribute matches the number(s) or numeric comparison. When comparing rangeOfInteger values, the &quot;&lt;&quot; and &quot;&gt;&quot; operators only check the upper bound of the range.</p>
<dt><code>WITH-VALUE &quot;false&quot;</code></p>
<dd>
<dt><code>WITH-VALUE &quot;true&quot;</code></p>
<dd>Requires that at least one value of the <code>EXPECT</code> attribute matches the boolean value given.</p>
<dt><code>WITH-VALUE &quot;/</code><i>regular expression</i><code>/&quot;</code></p>
<dd>Requires that at least one value of the <code>EXPECT</code> attribute matches the regular expression, which must conform to the POSIX regular expression syntax. Comparisons are case-sensitive.</p>
<dt><code>WITH-VALUE-FROM </code><i>attribute-name</i></p>
<dd>Requires that the value(s) of the <code>EXPECT</code> attribute matches the value(s) in the specified attribute. For example, &quot;EXPECT job-sheets WITH-VALUE-FROM job-sheets-supported&quot; requires that the &quot;job-sheets&quot; value is listed as a value of the &quot;job-sheets-supported&quot; attribute.</dl>
<h3>Status Predicates</h3>
<p>The following predicates are understood following the <code>STATUS</code> test directive:</p>
<dl>
<dt><code>DEFINE-MATCH </code><i>variable-name</i></p>
<dd>Defines the variable to &quot;1&quot; when the <code>STATUS</code> matches. A side-effect of this predicate is that this <code>STATUS</code> will never fail a test.</p>
<dt><code>DEFINE-NO-MATCH </code><i>variable-name</i></p>
<dd>Defines the variable to &quot;1&quot; when the <code>STATUS</code> does not match. A side-effect of this predicate is that this <code>STATUS</code> will never fail a test.</p>
<dt><code>IF-DEFINED </code><i>variable-name</i></p>
<dd>Makes the <code>STATUS</code> apply only if the specified variable is defined.</p>
<dt><code>IF-NOT-DEFINED </code><i>variable-name</i></p>
<dd>Makes the <code>STATUS</code> apply only if the specified variable is not defined.</p>
<dt><code>REPEAT-LIMIT </code><i>number</i></p>
<dd>Specifies the maximum number of times to repeat. The default value is 1000.</p>
<dt><code>REPEAT-MATCH</code></p>
<dd>
<dt><code>REPEAT-NO-MATCH</code></p>
<dd>Specifies that the current test should be repeated when the response status-code matches or does not match the value specified by the STATUS directive.</dl>
<h3>Operation Codes</h3>
<p>Operation codes correspond to the hexadecimal numbers (0xHHHH) and names from RFC 8011 and other IPP extension specifications. Here is a complete list of names supported by <code><a href="/docs/linux/man/8-ipptool/">ipptool</a></code>(8): </p>
<pre> Acknowledge-Document
 Acknowledge-Identify-Printer
 Acknowledge-Job
 Activate-Printer
 Add-Document-Images
 Allocate-Printer-Resources
 Cancel-Current-Job
 Cancel-Job
 Cancel-Jobs
 Cancel-My-Jobs
 Cancel-Resource
 Cancel-Subscription
 Close-Job
 Create-Job
 Create-Job-Subscriptions
 Create-Printer
 Create-Printer-Subscriptions
 Create-Resource
 Create-Resource-Subscriptions
 Create-System-Subscriptions
 CUPS-Accept-Jobs
 CUPS-Accept-Jobs
 CUPS-Add-Modify-Class
 CUPS-Add-Modify-Printer
 CUPS-Authenticate-Job
 CUPS-Create-Local-Printer
 CUPS-Delete-Class
 CUPS-Delete-Printer
 CUPS-Get-Classes
 CUPS-Get-Default
 CUPS-Get-Devices
 CUPS-Get-Document
 CUPS-Get-PPD
 CUPS-Get-PPDs
 CUPS-Get-Printers
 CUPS-Move-Job
 CUPS-Reject-Jobs
 CUPS-Set-Default
 Deactivate-Printer
 Deallocate-Printer-Resources
 Delete-Printer
 Deregister-Output-Device
 Disable-All-Printers
 Disable-Printer
 Enable-All-Printers
 Enable-Printer
 Fetch-Document
 Fetch-Job
 Get-Job-Attributes
 Get-Jobs
 Get-Next-Document-Data
 Get-Notifications
 Get-Output-Device-Attributes
 Get-Printer-Attributes
 Get-Printer-Support-Files
 Get-Printer-Supported-Values
 Get-Printers
 Get-Subscription-Attributes
 Get-Subscriptions
 Get-System-Attributes
 Get-System-Supported-Values
 Hold-Job
 Hold-New-Jobs
 Identify-Printer
 Install-Resource
 Pause-All-Printers
 Pause-All-Printers-After-Current-Job
 Pause-Printer
 Pause-Printer-After-Current-Job
 Print-Job
 Print-URI
 Promote-Job
 Purge-Jobs
 Register-Output-Device
 Release-Held-New-Jobs
 Release-Job
 Renew-Subscription
 Reprocess-Job
 Restart-Job
 Restart-Printer
 Restart-System
 Resubmit-Job
 Resume-All-Printers
 Resume-Job
 Resume-Printer
 Schedule-Job-After
 Send-Document
 Send-Hardcopy-Document
 Send-Notifications
 Send-Resource-Data
 Send-URI
 Set-Job-Attributes
 Set-Printer-Attributes
 Set-Resource-Attributes
 Set-System-Attributes
 Shutdown-All-Printers
 Shutdown-One-Printer
 Shutdown-Printer
 Startup-All-Printers
 Startup-One-Printer
 Startup-Printer
 Suspend-Current-Job
 Update-Active-Jobs
 Update-Document-Status
 Update-Job-Status
 Update-Output-Device-Attributes
 Validate-Document
 Validate-Job</pre>
<h3>Status Codes</h3>
<p>Status codes correspond to the hexadecimal numbers (0xHHHH) and names from RFC 8011 and other IPP extension specifications. Here is a complete list of the names supported by <code><a href="/docs/linux/man/8-ipptool/">ipptool</a></code>(8): </p>
<pre> client-error-account-authorization-failed
 client-error-account-closed
 client-error-account-info-needed
 client-error-account-limit-reached
 client-error-attributes-not-settable
 client-error-attributes-or-values-not-supported
 client-error-bad-request
 client-error-charset-not-supported
 client-error-compression-error
 client-error-compression-not-supported
 client-error-conflicting-attributes
 client-error-document-access-error
 client-error-document-format-error
 client-error-document-format-not-supported
 client-error-document-password-error
 client-error-document-permission-error
 client-error-document-security-error
 client-error-document-unprintable-error
 client-error-forbidden
 client-error-gone
 client-error-ignored-all-notifications
 client-error-ignored-all-subscriptions
 client-error-not-authenticated
 client-error-not-authorized
 client-error-not-fetchable
 client-error-not-found
 client-error-not-possible
 client-error-print-support-file-not-found
 client-error-request-entity-too-large
 client-error-request-value-too-long
 client-error-timeout
 client-error-too-many-subscriptions
 client-error-uri-scheme-not-supported
 cups-error-account-authorization-failed
 cups-error-account-closed
 cups-error-account-info-needed
 cups-error-account-limit-reached
 cups-see-other
 redirection-other-site
 server-error-busy
 server-error-device-error
 server-error-internal-error
 server-error-job-canceled
 server-error-multiple-document-jobs-not-supported
 server-error-not-accepting-jobs
 server-error-operation-not-supported
 server-error-printer-is-deactivated
 server-error-service-unavailable
 server-error-temporary-error
 server-error-version-not-supported
 successful-ok
 successful-ok-but-cancel-subscription
 successful-ok-conflicting-attributes
 successful-ok-events-complete
 successful-ok-ignored-notifications
 successful-ok-ignored-or-substituted-attributes
 successful-ok-ignored-subscriptions
 successful-ok-too-many-events</pre>
<h3>Tags</h3>
<p>Value and group tags correspond to the names from RFC 8011 and other IPP extension specifications. Here are the group tags: </p>
<pre> document-attributes-tag
 event-notification-attributes-tag
 job | job-attributes-tag
 operation | operation-attributes-tag
 printer | printer-attributes-tag
 resource-attributes-tag
 subscription-attributes-tag
 system-attributes-tag
 unsupported-attributes-tag</pre>
<p>Here are the value tags: </p>
<pre> admin-define
 boolean
 charset
 collection | begCollection
 dateTime
 default
 delete-attribute
 enum
 integer
 keyword
 language | naturalLanguage
 mimetype | mimeMediaType
 name | nameWithLanguage | nameWithoutLanguage
 no-value
 not-settable
 octetString
 rangeOfInteger
 resolution
 text | textWithLanguage | textWithoutLanguage
 unknown
 unsupported
 uri
 uriScheme</pre>
<h3>Variables</h3>
<p>The <code><a href="/docs/linux/man/8-ipptool/">ipptool</a></code>(8) program maintains a list of variables that can be used in any literal string or attribute value by specifying &quot;<i>$variable-name</i>&quot;. Aside from variables defined using the <i>-d</i> option or <code>DEFINE</code> directive, the following pre-defined variables are available:</p>
<dl>
<dt><code>$$</code></p>
<dd>Inserts a single &quot;$&quot; character.</p>
<dt><code>$ENV[</code><i>name</i><code>]</code></p>
<dd>Inserts the value of the named environment variable, or an empty string if the environment variable is not defined.</p>
<dt><code>$date-current</code></p>
<dd>Inserts the current date and time using the ISO-8601 format (&quot;yyyy-mm-ddThh:mm:ssZ&quot;).</p>
<dt><code>$date-start</code></p>
<dd>Inserts the starting date and time using the ISO-8601 format (&quot;yyyy-mm-ddThh:mm:ssZ&quot;).</p>
<dt><code>$filename</code></p>
<dd>Inserts the filename provided to <code><a href="/docs/linux/man/8-ipptool/">ipptool</a></code>(8) with the <i>-f</i> option.</p>
<dt><code>$filetype</code></p>
<dd>Inserts the MIME media type for the filename provided to <code><a href="/docs/linux/man/8-ipptool/">ipptool</a></code>(8) with the <i>-f</i> option.</p>
<dt><code>$hostname</code></p>
<dd>Inserts the hostname from the URI provided to <code><a href="/docs/linux/man/8-ipptool/">ipptool</a></code>(8).</p>
<dt><code>$job-id</code></p>
<dd>Inserts the last &quot;job-id&quot; attribute value returned in a test response or 0 if no &quot;job-id&quot; attribute has been seen.</p>
<dt><code>$job-uri</code></p>
<dd>Inserts the last &quot;job-uri&quot; attribute value returned in a test response or an empty string if no &quot;job-uri&quot; attribute has been seen.</p>
<dt><code>$notify-subscription-id</code></p>
<dd>Inserts the last &quot;notify-subscription-id&quot; attribute value returned in a test response or 0 if no &quot;notify-subscription-id&quot; attribute has been seen.</p>
<dt><code>$port</code></p>
<dd>Inserts the port number from the URI provided to <code><a href="/docs/linux/man/8-ipptool/">ipptool</a></code>(8).</p>
<dt><code>$resource</code></p>
<dd>Inserts the resource path from the URI provided to <code><a href="/docs/linux/man/8-ipptool/">ipptool</a></code>(8).</p>
<dt><code>$scheme</code></p>
<dd>Inserts the scheme from the URI provided to <code><a href="/docs/linux/man/8-ipptool/">ipptool</a></code>(8).</p>
<dt><code>$uri</code></p>
<dd>Inserts the URI provided to <code><a href="/docs/linux/man/8-ipptool/">ipptool</a></code>(8).</p>
<dt><code>$uriuser</code></p>
<dd>Inserts the username from the URI provided to <code><a href="/docs/linux/man/8-ipptool/">ipptool</a></code>(8), if any.</p>
<dt><code>$user</code></p>
<dd>Inserts the current user&#8217;s login name.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ipptool/">ipptool</a></code>(1), IANA IPP Registry (<a rel="nofollow" href="https://www.iana.org/assignments/ipp-registrations">https://www.iana.org/assignments/ipp-registrations</a>), PWG Internet Printing Protocol Workgroup (<a rel="nofollow" href="https://www.pwg.org/ipp">https://www.pwg.org/ipp</a>), RFC 8011 (<a rel="nofollow" href="https://datatracker.ietf.org/doc/html/rfc8011)">https://datatracker.ietf.org/doc/html/rfc8011)</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2021-2022 by OpenPrinting.</p>

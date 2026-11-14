---
title: "osinfo(1)"
name: "osinfo"
section: "1"
letter: "o"
url: "/docs/linux/man/1-osinfo/"
description: "osinfo – gather information regarding the running operating system"
---

<h2>NAME</h2>
<p> osinfo &#8211; gather information regarding the running operating system</p>
<h2>SYNOPSIS</h2>
<p> <code>osinfo</code> [ <code>-s</code> ] [ <code>-h</code> hostname ] [ <code>-p</code> portnumber ]<br />
&nbsp;<wbr>[&nbsp;<wbr><code>-u</code>&nbsp;<wbr>username&nbsp;<wbr>]&nbsp;<wbr>[&nbsp;<wbr><code>-w</code>&nbsp;<wbr>password&nbsp;<wbr>]&nbsp;<wbr>[&nbsp;<wbr><code>-t</code>&nbsp;<wbr>timeout&nbsp;<wbr>]<br />
&nbsp;<wbr>[&nbsp;<wbr><code>-c</code>&nbsp;<wbr>]&nbsp;<wbr>[&nbsp;<wbr><code>&#8211;help</code>&nbsp;<wbr>]&nbsp;<wbr>[&nbsp;<wbr><code>&#8211;version</code>&nbsp;<wbr>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>osinfo </code> command displays information regarding the operating system, gathered via WBEM using the PG_OperatingSystem class supported by the OperatingSystem Provider (bundled with OpenPegasus). <code>osinfo</code> requires the CIM Server to be installed and running. </p>
<p> By default, the information is formatted for display, converting CIMDateTime strings into a more user-readable format (see Examples), and converting the total number of seconds of uptime into the appropriate number of days, hours, minutes, and seconds. </p>
<p> If a property value is unavailable, it will be shown as &quot;Unknown&quot;</p>
<h3>Options</h3>
<p> <code>osinfo</code> recognizes the following options:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-c</code></p>
<dd> Use the CIM formats for DateTime and SystemUpTime values (not the formatting done by default). As specified by the DMTF, the CIMDateTime format is yyyymmddhhmmss.mmmmmmsutc, where yyyy is a 4-digit year, mm is the month, dd is the day, hh is the hour on a 24-hour clock, mm is the minute, ss is the second, mmmmmm is the number of microseconds, s is a &quot;+&quot; or &quot;-&quot; indicating the sign of the UTC (Universal Time Code) correction field (since the DateTime is returned in the local time zone of the system), and utc is the offset from UTC in minutes.</p>
<dt><code>-h</code> hostname</p>
<dd> Connect to the CIM Server on the specified host. If this option is not specified, <code>osinfo </code> connects to the localhost.</p>
<dt><code>&#8211;help</code></p>
<dd> Display command usage information.</p>
<dt><code>-p</code> portnumber</p>
<dd> Connect to the CIM Server on the specified port number. If this option is not specified, <code>osinfo</code> connects to the default port for the wbem-http service, or if the <code>-s</code> option is specified, to the default port for the wbem-https service.</p>
<dt><code>-s</code></p>
<dd> Enable the use of the SSL protocol between <code>osinfo </code> and the CIM server. The <code>-s</code> option should be specified if the CIM Server on the specified hostname/portnumber expects clients to connect using HTTPS.</p>
<dt><code>-t</code> timeout</p>
<dd> Wait the specified number of milliseconds on sending a request, before timing out if no response has been received. The <i>timeout </i> value must be an integer value greater than 0.</p>
<dt><code>-u</code> username</p>
<dd> Connect as the specified <i>R username . </i> If <i>username </i> is not specified, the current logged in user is used for authentication. This option is ignored if neither <i>hostname </i> nor <i>portnumber </i> is specified.</p>
<dt><code>&#8211;version</code></p>
<dd> Display CIM Server version.</p>
<dt><code>-w</code> password</p>
<dd> Authenticate the connection using the specified <i>password .</i> This option is ignored if neither <i>hostname </i> nor <i>portnumber </i> is specified. WARNING: A password should not be specified on the command line on a multi-user system, since command-line options are typically world-readable for a short window of time. If the remote host requests authentication and this option is not specified, <code>osinfo </code> will prompt for the password.</dl>
</dl>
<h2>EXIT STATUS</h2>
<p> When an error occurs, an error message is written to stderr and an appropriate value is returned. The following values are returned:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>0 </code></p>
<dd> Success</p>
<dt><code>1</code></p>
<dd> Error</dl>
</dl>
<h2>USAGE NOTE</h2>
<p> The <code>osinfo </code> command requires that the CIM Server is running.</p>
<h2>DIAGNOSTICS</h2>
<p> <code>osinfo error: Cannot connect</code></p>
<dl>
<dt>
<dd> The CIMOM is not running. Start the CIMOM with the <code>cimserver</code> command and re-run <code>osinfo .</code></dl>
<h2>EXAMPLES</h2>
<p> Run the default <code>osinfo </code> command.</p>
<dl>
<dt>
<dd>
<dt><code>OperatingSystem Information</code></p>
<dd>
<dt><code> Host: myserver.hp.com </code></p>
<dd>
<dt><code> Name: HP-UX </code></p>
<dd>
<dt><code> Version: B.11.00 </code></p>
<dd>
<dt><code> UserLicense: Unlimited user license </code></p>
<dd>
<dt><code> OSCapability: 32 bit </code></p>
<dd>
<dt><code> LastBootTime: Sep 24, 2001 9:16:18 (-0700) </code></p>
<dd>
<dt><code> LocalDateTime: May 23, 2002 10:55:54 (-0700) </code></p>
<dd>
<dt><code> SystemUpTime: 20828377 seconds = 241 days, 1 hr, 39 mins, 37 secs </code></p>
<dd></dl>
<p> The system myserver.hp.com is running version B.11.00 of HP-UX, has an unlimited user license, and is 32-bit capable. The Operating System was last booted on Sept 24, 2001 and the local date and time are given. All time values are offset from GMT by -7 hours. </p>
<p> Run <code>osinfo ,</code> with the values displayed in their CIM format</p>
<dl>
<dt>
<dd> <code>osinfo -c</code> </p>
<dt><code>OperatingSystem Information</code></p>
<dd>
<dt><code> Host: rushmore.cup.hp.com</code></p>
<dd>
<dt><code> Name: HP-UX</code></p>
<dd>
<dt><code> Version: B.11.00</code></p>
<dd>
<dt><code> UserLicense: Unlimited user license</code></p>
<dd>
<dt><code> OSCapability: 32 bit</code></p>
<dd>
<dt><code> LastBootTime: 20010924091618.000000-420</code></p>
<dd>
<dt><code> LocalDateTime: 20020523105801.000000-420</code></p>
<dd>
<dt><code> SystemUpTime: 20828504</code></p>
<dd></dl>
<p> The same rushmore.cup.hp.com system is displayed, but in this output the LastBootTime and LocalDateTime values are in the CIM format. The SystemUpTime value is in total seconds (as specified by CIM). Other fields do not change, as their CIM specification is the strings themselves.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cimserver/">cimserver</a>(1).</p>
<h2>STANDARDS CONFORMANCE</h2>
<p> <code>osinfo</code> : DMTF WBEM (Web-Based Enterprise Management) and CIM (Common Information Model) </p>
<h2>Index</h2>

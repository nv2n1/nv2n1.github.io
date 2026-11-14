---
title: "ippeveprinter(1)"
name: "ippeveprinter"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ippeveprinter/"
description: "ippeveprinter – an ipp everywhere printer application for cups"
---

<h2 class="name">NAME</h2>
<p> ippeveprinter &#8211; an ipp everywhere printer application for cups </p>
<h2>SYNOPSIS</h2>
<p> <code>ippeveprinter</code> [ <code>&#8211;help</code> ] [ <code>&#8211;no-web-forms</code> ] [ <code>&#8211;pam-service</code> <i>service</i> ] [ <code>&#8211;version</code> ] [ <code>-2</code> ] [ <code>-A</code> ] [ <code>-D</code> <i>device-uri</i> ] [ <code>-F</code> <i>output-type/subtype</i> ] [ <code>-K</code> <i>keypath</i> ] [ <code>-M</code> <i>manufacturer</i> ] [ <code>-P</code> <i>filename.ppd</i> ] [ <code>-V</code> <i>ipp-version</i> ] [ <code>-a</code> <i>filename.conf</i> ] [ <code>-c</code> <i>command</i> ] [ <code>-d</code> <i>spool-directory</i> ] [ <code>-f</code> <i>type/subtype[,&#8230;]</i> ] [ <code>-i</code> <i>iconfile.png</i> ] [ <code>-k</code> ] [ <code>-l</code> <i>location</i> ] [ <code>-m</code> <i>model</i> ] [ <code>-n</code> <i>hostname</i> ] [ <code>-p</code> <i>port</i> ] [ <code>-r</code> <i>subtype[,subtype]</i> ] [ <code>-s</code> <i>speed[,color-speed]</i> ] [ <code>-v[vvv]</code> ] <i>service-name</i></p>
<h2>DESCRIPTION</h2>
<p> <code>ippeveprinter</code> is a simple Internet Printing Protocol (IPP) server conforming to the IPP Everywhere (PWG 5100.14) specification. It can be used to test client software or act as a very basic print server that runs a command for every job that is printed.</p>
<h2>OPTIONS</h2>
<p> The following options are recognized by <code>ippeveprinter:</code></p>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Show program usage.</p>
<dt><code>&#8211;no-web-forms</code></p>
<dd> Disable the web interface forms used to update the media and supply levels.</p>
<dt><code>&#8211;pam-service </code><i>service</i></p>
<dd> Set the PAM service name. The default service is &quot;cups&quot;.</p>
<dt><code>&#8211;version</code></p>
<dd> Show the CUPS version.</p>
<dt><code>-2</code></p>
<dd> Report support for two-sided (duplex) printing.</p>
<dt><code>-A</code></p>
<dd> Enable authentication for the created printer. <code>ippeveprinter</code> uses PAM to authenticate HTTP Basic credentials.</p>
<dt><code>-D </code><i>device-uri</i></p>
<dd> Set the device URI for print output. The URI can be a filename, directory, or a network socket URI of the form &quot;<a href="socket://ADDRESS[:PORT]">socket://ADDRESS[:PORT]</a>&quot; (where the default port number is 9100). When specifying a directory, <code>ippeveprinter</code> will create an output file using the job ID and name.</p>
<dt><code>-F </code><i>output-type/subtype[,&#8230;]</i></p>
<dd> Specifies the output MIME media type. The default is &quot;application/postscript&quot; when the <code>-P</code> option is specified.</p>
<dt><code>-M </code><i>manufacturer</i></p>
<dd> Set the manufacturer of the printer. The default is &quot;Example&quot;.</p>
<dt><code>-P </code><i>filename.ppd</i></p>
<dd> Load printer attributes from the specified PPD file. This option is typically used in conjunction with the <code><a href="/docs/linux/man/7-ippeveps/">ippeveps</a></code>(7) printer command (&quot;-c ippeveps&quot;).</p>
<dt><code>-V 1.1</code></p>
<dd>
<dt><code>-V 2.0</code></p>
<dd> Specifies the maximum IPP version to report. 2.0 is the default.</p>
<dt><code>-c </code><i>command</i></p>
<dd> Run the specified command for each document that is printed. If &quot;command&quot; is not an absolute path (&quot;/path/to/command&quot;), <code>ippeveprinter</code> looks for the command in the &quot;command&quot; subdirectory of the CUPS binary directory, typically /usr/lib/cups/command or /usr/libexec/cups/command. The <code><a href="/docs/linux/man/1-cups-config/">cups-config</a></code>(1) command can be used to discover the correct binary directory (&quot;cups-config &#8211;serverbin&quot;). In addition, the CUPS_SERVERBIN environment variable can be used to override the default location of this directory &#8211; see the <code><a href="/docs/linux/man/1-cups/">cups</a></code>(1) man page for more details.</p>
<dt><code>-d </code><i>spool-directory</i></p>
<dd> Specifies the directory that will hold the print files. The default is a directory under the user&#8217;s current temporary directory.</p>
<dt><code>-f </code><i>type/subtype[,&#8230;]</i></p>
<dd> Specifies a list of MIME media types that the server will accept. The default depends on the type of printer created.</p>
<dt><code>-i </code><i>iconfile.png</i></p>
<dd> Specifies the printer icon file for the server. The file must be a PNG format image. The default is an internally-provided PNG image.</p>
<dt><code>-k</code></p>
<dd> Keeps the print documents in the spool directory rather than deleting them.</p>
<dt><code>-l </code><i>location</i></p>
<dd> Specifies the human-readable location string that is reported by the server. The default is the empty string.</p>
<dt><code>-m </code><i>model</i></p>
<dd> Specifies the model name of the printer. The default is &quot;Printer&quot;.</p>
<dt><code>-n </code><i>hostname</i></p>
<dd> Specifies the hostname that is reported by the server. The default is the name returned by the <code><a href="/docs/linux/man/1-hostname/">hostname</a></code>(1) command.</p>
<dt><code>-p </code><i>port</i></p>
<dd> Specifies the port number to listen on. The default is a user-specific number from 8000 to 8999.</p>
<dt><code>-r off</code></p>
<dd> Turns off DNS-SD service advertisements entirely.</p>
<dt><code>-r </code><i>subtype[,subtype]</i></p>
<dd> Specifies the DNS-SD subtype(s) to advertise. Separate multiple subtypes with a comma. The default is &quot;_print&quot;.</p>
<dt><code>-s </code><i>speed[,color-speed]</i></p>
<dd> Specifies the printer speed in pages per minute. If two numbers are specified and the second number is greater than zero, the server will report support for color printing. The default is &quot;10,0&quot;.</p>
<dt><code>-v[vvv]</code></p>
<dd> Be (very) verbose when logging activity to standard error.</dl>
<h2>EXIT STATUS</h2>
<p> The <code>ippeveprinter</code> program returns 1 if it is unable to process the command-line arguments or register the IPP service. Otherwise <code>ippeveprinter</code> will run continuously until terminated.</p>
<h2>CONFORMING TO</h2>
<p> The <code>ippeveprinter</code> program is unique to CUPS and conforms to the IPP Everywhere (PWG 5100.14) specification.</p>
<h2>ENVIRONMENT</h2>
<p> <code>ippeveprinter</code> adds environment variables starting with &quot;IPP_&quot; for all IPP Job attributes in the print request. For example, when executing a command for an IPP Job containing the &quot;media&quot; Job Template attribute, the &quot;IPP_MEDIA&quot; environment variable will be set to the value of that attribute. </p>
<p> In addition, all IPP &quot;xxx-default&quot; and &quot;pwg-xxx&quot; Printer Description attributes are added to the environment. For example, the &quot;IPP_MEDIA_DEFAULT&quot; environment variable will be set to the default value for the &quot;media&quot; Job Template attribute. </p>
<p> Enumerated values are converted to their keyword equivalents. For example, a &quot;print-quality&quot; Job Template attribute with a enum value of 3 will become the &quot;IPP_PRINT_QUALITY&quot; environment variable with a value of &quot;draft&quot;. This string conversion only happens for standard Job Template attributes, currently &quot;finishings&quot;, &quot;orientation-requested&quot;, and &quot;print-quality&quot;. </p>
<p> Finally, the &quot;CONTENT_TYPE&quot; environment variable contains the MIME media type of the document being printed, the &quot;DEVICE_URI&quot; environment variable contains the device URI as specified with the &quot;-D&quot; option, the &quot;OUTPUT_FORMAT&quot; environment variable contains the output MIME media type, and the &quot;PPD&quot; environment variable contains the PPD filename as specified with the &quot;-P&quot; option.</p>
<h2>COMMAND OUTPUT</h2>
<p> Unless they communicate directly with a printer, print commands send printer-ready data to the standard output. </p>
<p> Print commands can send messages back to <code>ippeveprinter</code> on the standard error with one of the following prefixes:</p>
<dl>
<dt><code>ATTR: </code><i>attribute=value[ attribute=value]</i></p>
<dd> Sets the named attribute(s) to the given values. Currently only the &quot;job-impressions&quot; and &quot;job-impressions-completed&quot; Job Status attributes and the &quot;marker-xxx&quot;, &quot;printer-alert&quot;, &quot;printer-alert-description&quot;, &quot;printer-supply&quot;, and &quot;printer-supply-description&quot; Printer Status attributes can be set.</p>
<dt><code>DEBUG: </code><i>Debugging message</i></p>
<dd> Logs a debugging message if at least two -v&#8217;s have been specified.</p>
<dt><code>ERROR: </code><i>Error message</i></p>
<dd> Logs an error message and copies the message to the &quot;job-state-message&quot; attribute.</p>
<dt><code>INFO: </code><i>Informational message</i></p>
<dd> Logs an informational/progress message if -v has been specified and copies the message to the &quot;job-state-message&quot; attribute unless an error has been reported.</p>
<dt><code>STATE: </code><i>keyword[,keyword,&#8230;]</i></p>
<dd> Sets the printer&#8217;s &quot;printer-state-reasons&quot; attribute to the listed keywords.</p>
<dt><code>STATE: &#8211;</code><i>keyword[,keyword,&#8230;]</i></p>
<dd> Removes the listed keywords from the printer&#8217;s &quot;printer-state-reasons&quot; attribute.</p>
<dt><code>STATE: +</code><i>keyword[,keyword,&#8230;]</i></p>
<dd> Adds the listed keywords to the printer&#8217;s &quot;printer-state-reasons&quot; attribute.</dl>
<h2>EXAMPLES</h2>
<p> Run <code>ippeveprinter</code> with a service name of My Cool Printer: </p>
<pre>
    ippeveprinter &quot;My Cool Printer&quot;
</pre>
<p> Run the <code><a href="/docs/linux/man/1-file/">file</a></code>(1) command whenever a job is sent to the server: </p>
<pre>
    ippeveprinter -c /usr/bin/file &quot;My Cool Printer&quot;
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-ippevepcl/">ippevepcl</a></code>(7), <code><a href="/docs/linux/man/7-ippeveps/">ippeveps</a></code>(7), PWG Internet Printing Protocol Workgroup (<a rel="nofollow" href="http://www.pwg.org/ipp)">http://www.pwg.org/ipp)</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2021-2022 by OpenPrinting. </p>
<h2>Index</h2>

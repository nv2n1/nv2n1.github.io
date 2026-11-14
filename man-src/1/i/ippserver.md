---
title: "ippserver(1)"
name: "ippserver"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ippserver/"
description: "ippserver – a simple internet printing protocol server"
---

<h2 class="name">NAME</h2>
<p> ippserver &#8211; a simple internet printing protocol server </p>
<h2>SYNOPSIS</h2>
<p> <code>ippserver</code> [ <code>-2</code> ] [ <code>-M</code> <i>manufacturer</i> ] [ <code>-P</code> ] [ <code>-c</code> <i>command</i> ] [ <code>-d</code> <i>spool-directory</i> ] [ <code>-f</code> <i>type/subtype[,&#8230;]</i> ] [ <code>-h</code> ] [ <code>-i</code> <i>iconfile.png</i> ] [ <code>-k</code> ] [ <code>-l</code> <i>location</i> ] [ <code>-m</code> <i>model</i> ] [ <code>-n</code> <i>hostname</i> ] [ <code>-p</code> <i>port</i> ] [ <code>-r</code> <i>subtype</i> ] [ <code>-s</code> <i>speed[,color-speed]</i> ] [ <code>-v[vvv]</code> ] <i>service-name</i></p>
<h2>DESCRIPTION</h2>
<p> <code>ippserver</code> is a simple Internet Printing Protocol (IPP) server conforming to the IPP Everywhere (PWG 5100.14) specification. It can be used to test client software or act as a very basic print server that runs a command for every job that is printed.</p>
<h2>OPTIONS</h2>
<p> The following options are recognized by <code>ippserver:</code></p>
<dl>
<dt><code>-2</code></p>
<dd> Report support for two-sided (duplex) printing.</p>
<dt><code>-M </code><i>manufacturer</i></p>
<dd> Set the manufacturer of the printer. The default is &quot;Test&quot;.</p>
<dt><code>-P</code></p>
<dd> Report support for PIN printing.</p>
<dt><code>-c </code><i>command</i></p>
<dd> Run the specified command for each document that is printed.</p>
<dt><code>-d </code><i>spool-directory</i></p>
<dd> Specifies the directory that will hold the print files. The default is a directory under the user&#8217;s current temporary directory.</p>
<dt><code>-f </code><i>type/subtype[,&#8230;]</i></p>
<dd> Specifies a list of MIME media types that the server will accept. The default is &quot;application/pdf,image/jpeg,image/pwg-raster&quot;.</p>
<dt><code>-h</code></p>
<dd> Shows program help.</p>
<dt><code>-i </code><i>iconfile.png</i></p>
<dd> Specifies the printer icon file for the server. The default is &quot;printer.png&quot;.</p>
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
<dt><code>-r </code><i>subtype</i></p>
<dd> Specifies the Bonjour subtype(s) to advertise. Separate multiple subtypes with a comma. The default is &quot;_print&quot;.</p>
<dt><code>-s </code><i>speed[,color-speed]</i></p>
<dd> Specifies the printer speed in pages per minute. If two numbers are specified and the second number is greater than zero, the server will report support for color printing. The default is &quot;10,0&quot;.</p>
<dt><code>-v[vvv]</code></p>
<dd> Be (very) verbose when logging activity to the standard output.</dl>
<h2>EXIT STATUS</h2>
<p> The <code>ippserver</code> program returns 1 if it is unable to process the command-line arguments or register the IPP service. Otherwise <code>ippserver</code> will run continuously until terminated.</p>
<h2>CONFORMING TO</h2>
<p> The <code>ippserver</code> program is unique to CUPS and conforms to the IPP Everywhere (PWG 5100.14) specification.</p>
<h2>ENVIRONMENT</h2>
<p> <code>ippserver</code> adds environment variables starting with &quot;IPP_&quot; for all IPP Job attributes in the print request. For example, when executing a command for an IPP Job containing the &quot;media&quot; Job Template attribute, the &quot;IPP_MEDIA&quot; environment variable will be set to the value of that attribute. </p>
<p> Enumerated values are converted to their keyword equivalents. For example, a &quot;print-quality&quot; Job Template attribute with a enum value of 3 will become the &quot;IPP_PRINT_QUALITY&quot; environment variable with a value of &quot;draft&quot;.</p>
<h2>EXAMPLES</h2>
<p> Run <code>ippserver</code> with a service name of My Cool Printer: </p>
<pre>
    ippserver &quot;My Cool Printer&quot;
</pre>
<p> Run the <code><a href="/docs/linux/man/1-file/">file</a></code>(1) command whenever a job is sent to the server: </p>
<pre>
    ippserver -c file &quot;My Cool Printer&quot;
</pre>
<h2>SEE ALSO</h2>
<p> PWG Internet Printing Protocol Workgroup (<a rel="nofollow" href="http://www.pwg.org/ipp)">http://www.pwg.org/ipp)</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2007-2014 by Apple Inc. </p>
<h2>Index</h2>

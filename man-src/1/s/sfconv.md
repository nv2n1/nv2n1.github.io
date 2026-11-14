---
title: "sfconv(1)"
name: "sfconv"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sfconv/"
description: "sfconv – A tool for converting the encoding of Standard Format (SF) files"
---

<h2 class="name">NAME</h2>
<p> sfconv &#8211; A tool for converting the encoding of Standard Format (SF) files </p>
<h2>SYNOPSIS</h2>
<h3>8-bit to Unicode:</h3>
<dl>
<dt>sfconv <code>-8u</code> [-utf8|-be|-le] [-bom] <code>-c</code> ControlFile [-d MappingDirectory] <code>-i</code> InFile <code>-o</code> OutFile</p>
<dd></dl>
<h3>Unicode to 8-bit:</h3>
<dl>
<dt>sfconv <code>-u8</code> [-utf8|-be|-le] <code>-c</code> ControlFile [-d MappingDirectory] <code>-i</code> InFile <code>-o</code> OutFile</p>
<dd></dl>
<h2>DESCRIPTION</h2>
<p> A tool for converting Standard Format (SF) files is included in the current TECkit package. This is <code>sfconv</code> , a command-line tool that uses an XML “control file” to specify the mappings associated with the various markers in an SF file. Note that the current SFconv tool should be considered a prototype rather than a full solution to the issue of SF conversions. A more complete tool with an improved user interface would be desirable.</p>
<h2>OPTIONS</h2>
<p> The SFconv utility uses command-line options to specify the conversion direction, control file, and input and output files. The required arguments are:</p>
<dl>
<dt><code>-8u</code>|<code>-u8</code></p>
<dd> conversion direction: 8-bit to Unicode or vice versa</p>
<dt><code>-c</code>controlFile</p>
<dd> specifies XML control file</p>
<dt><code>-i</code>inFile</p>
<dd> specifies filename of input SF file</p>
<dt><code>-o</code>outFile</p>
<dd> specifies filename for converted output </p>
<p> In addition, the following optional arguments may be used if appropriate:</p>
<dt><code>-d</code>mappingDir</p>
<dd> directory where mapping files ( .tec files) are to be found</p>
<dt><code>-utf8</code>|<code>-be</code>|<code>-le</code></p>
<dd> Unicode encoding form: UTF-8, UTF-16BE, or UTF16-LE (default is UTF8 for output, or detected from input file if BOM is present)</p>
<dt><code>-bom</code></p>
<dd> (only when mapping to Unicode) write initial BOM to the output file</p>
<dt><code>-nfc</code>|<code>-nfd</code></p>
<dd> (only when mapping to Unicode) normalize to NFC or NFD</dl>
<h2>Further Information</h2>
<p> For further information see the document TECkit_Tools.pdf. On a Debian system, this can be found in /usr/share/doc/teckit. </p>
<h2>Index</h2>

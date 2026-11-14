---
title: "zipdetails(1)"
name: "zipdetails"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zipdetails/"
---

<h2 class="name">NAME</h2>
 

 zipdetails - display the internal structure of zip files 

<h2>SYNOPSIS</h2>

 <pre><code>
zipdetails[-v][--scan] zipfile.zip
        zipdetails -
    h
        zipdetails-- version
</code></pre>

<h2>DESCRIPTION</h2>

 Zipdetails displays information about the internal record structure of zip files. It is not concerned with displaying any details of the compressed data stored in the zip file. 

 The program assumes prior understanding of the internal structure of a Zip file. You should have a copy of the Zip <font SIZE="-1">APPNOTE</font> file at hand to help understand the output from this program (``<font SIZE="-1">SEE ALSO''</font> for details).

<h3>Default Behaviour</h3>

 By default the program expects to be given a well-formed zip file. It will navigate the Zip file by first parsing the zip central directory at the end of the file. If that is found, it will then walk through the zip records starting at the beginning of the file. Any badly formed zip data structures encountered are likely to terminate the program. 

 If the program finds any structural problems with the zip file it will print a summary at the end of the output report. The set of error cases reported is very much a work in progress, so don't rely on this feature to find all the possible errors in a zip file. If you have suggestions for use-cases where this could be enhanced please consider creating an enhancement request (see ``<font SIZE="-1">SUPPORT''</font>).

<h3>Scan-Mode</h3>

 If you do have a potentially corrupt zip file, particulatly where the central directory at the end of the file is absent/incomplete, you can try usng the <tt>&quot;--scan&quot;</tt> option to search for zip records that are still present. 

 When Scan-mode is enabled, the program will walk the zip file from the start blindly looking for the 4-byte signatures that preceed each of the zip data structures. If it finds any of the recognised signatures it will attempt to dump the associated zip record. For very large zip files, this operation can take a long time to run. 

 Note that the 4-byte signatures used in zip files can sometimes match with random data stored in the zip file, so care is needed interpreting the results.

<h3><font SIZE="-1">OPTIONS</font></h3>

<dl>
<dt>-h
<dd> Display help
<dt>--scan
<dd> Walk the zip file loking for possible zip records. Can be error-prone. See ``Scan-Mode''
<dt>-v
<dd> Enable Verbose mode. See ``Verbose Output''.
<dt>--version
<dd> Display version number of the program and exit.</dl>

<h3>Default Output</h3>

 By default zipdetails will output the details of the zip file in three columns.
<dl>
<dt>Column 1
<dd> This contains the offset from the start of the file in hex.
<dt>Column 2
<dd> This contains a textual description of the field.
<dt>Column 3
<dd> If the field contains a numeric value it will be displayed in hex. Zip stores most numbers in little-endian format - the value displayed will have the little-endian encoding removed. 

 Next, is an optional description of what the value means.</dl>

<h3>Verbose Output</h3>

 If the <tt>&quot;-v&quot;</tt> option is present, column 1 is expanded to include
<dl>
<dt>&bull;
<dd> The offset from the start of the file in hex.
<dt>&bull;
<dd> The length of the field in hex.
<dt>&bull;
<dd> A hex dump of the bytes in field in the order they are stored in the zip file.</dl>

<h2>LIMITATIONS</h2>

 The following zip file features are not supported by this program:
<dl>
<dt>&bull;
<dd> Multi-part archives.
<dt>&bull;
<dd> The strong encryption features defined in the ``<font SIZE="-1">APPNOTE''</font> document.</dl>

<h2>TODO</h2>

 Error handling is a work in progress. If the program encounters a problem reading a zip file it is likely to terminate with an unhelpful error message.

<h2>SUPPORT</h2>

 General feedback/questions/bug reports should be sent to &lt;<a rel="nofollow" HREF="https://github.com/pmqs/IO-Compress/issues">https://github.com/pmqs/IO-Compress/issues</a>&gt; (preferred) or &lt;<a rel="nofollow" HREF="https://rt.cpan.org/Public/Dist/Display.html?Name=IO-Compress">https://rt.cpan.org/Public/Dist/Display.html?Name=IO-Compress</a>&gt;.

<h2>SEE ALSO</h2>

 The primary reference for Zip files is the ``<font SIZE="-1">APPNOTE''</font> document available at &lt;<a rel="nofollow" HREF="http://www.pkware.com/documents/casestudies/APPNOTE.TXT">http://www.pkware.com/documents/casestudies/APPNOTE.TXT</a>&gt;. 

 An alternative reference is the Info-Zip appnote. This is available from &lt;<a HREF="ftp://ftp.info-zip.org/pub/infozip/doc/">ftp://ftp.info-zip.org/pub/infozip/doc/</a>&gt; 

 The <tt>&quot;zipinfo&quot;</tt> program that comes with the info-zip distribution (&lt;<a rel="nofollow" HREF="http://www.info-zip.org/">http://www.info-zip.org/</a>&gt;) can also display details of the structure of a zip file. 

 See also Archive::Zip::SimpleZip, IO::Compress::Zip, IO::Uncompress::Unzip.

<h2>AUTHOR</h2>

 Paul Marquess <i>pmqs [at] cpan.org</i>.

<h2>COPYRIGHT</h2>

 Copyright (c) 2011-2021 Paul Marquess. All rights reserved. 

 This program is free software; you can redistribute it and/or modify it under the same terms as Perl itself. 

<h2>Index</h2>



<dt><a HREF="#lbAJ">LIMITATIONS</a>
<dd>
<dt><a HREF="#lbAK">TODO</a>
<dd>
<dt><a HREF="#lbAL">SUPPORT</a>
<dd>
<dt><a HREF="#lbAM">SEE ALSO</a>
<dd>
<dt><a HREF="#lbAN">AUTHOR</a>
<dd>
<dt><a HREF="#lbAO">COPYRIGHT</a>
<dd></dl>

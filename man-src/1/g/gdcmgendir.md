---
title: "gdcmgendir(1)"
name: "gdcmgendir"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdcmgendir/"
description: "gdcmgendir – .TH \"gdcmgendir\" 1 \"Fri Oct 29 2010\" \"Version 2.0.16\" \"GDCM\""
---

<h2 class="name">NAME</h2>
<p> gdcmgendir &#8211; .TH &quot;gdcmgendir&quot; 1 &quot;Fri Oct 29 2010&quot; &quot;Version 2.0.16&quot; &quot;GDCM&quot; </p>
<h2 class="name">NAME</h2>
<p> gdcmgendir &#8211; .SH &quot;SYNOPSIS&quot; </p>
<pre>
gdcmgendir [options] file-in file-out
</pre>
<h2>DESCRIPTION</h2>
<h2>PARAMETERS</h2>
<pre>
file-in   DICOM input filename
file-out  DICOM output filename
</pre>
<h2>OPTIONS</h2>
<h3>Parameters</h3>
<h3>OPTIONS</h3>
<pre><code>
- i-- input DICOM filename or directory - o-- output DICOM filename or directory - r-- recursive recursive.--descriptor descriptor.--root - uid Root UID.--resources - path Resources path.
</code></pre>
<h3>general options</h3>
<p>&#8211; h&#8211; help<br />
        print this help text and exit &#8211;<br />
    v&#8211; version<br />
        print version information and exit &#8211;<br />
    V&#8211; verbose<br />
        verbose<br />
        mode(warning + error)<br />
            .-<br />
    W&#8211; warning<br />
    warning mode,<br />
    print warning information<br />
        &#8211; E&#8211; error<br />
        error mode,<br />
    print error information<br />
        &#8211; D&#8211; debug<br />
        debug mode,<br />
    print debug information</p>
<h3>environment variable</h3>
<pre>
  GDCM_ROOT_UID Root UID
  GDCM_RESOURCES_PATH path pointing to resources files (Part3.xml, ...)
</pre>
<h2>Typical usage</h2>
<h2>NOTE</h2>
<p> One may have to run some preliminary steps in order to get gdcmgendir to generate the DICOMDIR file. Namely two steps: </p>
<dl>
<dt>*</p>
<dd> Batch renaming of the DICOM filename into something compatible with ISO 9660 filename convention</p>
<dt>*</p>
<dd> Convert all DICOM file into the Explicit VR Little Endian Uncompressed (1.2.840.10008.1.2.1)</dl>
<p> Step 1. can be solved in a numerous way. Eg. on UNIX environment this could either be solved using the mkisofs command line tool. filename should not contains any extension since the VR CS does not allow for the &#8216;.&#8217; character. Only upper case, digit 0-9, the space &#8216; &#8216; and the underscore &#8216;_&#8217; character are valid in VR CS, with a maximum of 8 bytes. Another simple tool that can be handy is &#8216;rename&#8217; in conjunction with &#8216;basename&#8217;. </p>
<p> Step 2. can simply be achieved using the gdcmconv command line tool: </p>
<pre><code>
  $ for i in `ls IMG*`;
  do
      gdcmconv-- raw-- force $i / tmp / out / $i;
  done
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gdcmconv/">gdcmconv</a></code>(1), <code><a href="/docs/linux/man/1-gdcmanon/">gdcmanon</a></code>(1), <code><a href="/docs/linux/man/1-rename/">rename</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2006-2010 Mathieu Malaterre </p>
<h2>Index</h2>

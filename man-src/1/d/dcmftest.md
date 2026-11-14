---
title: "dcmftest(1)"
name: "dcmftest"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dcmftest/"
description: "dcmftest – Test if file uses DICOM part 10 format"
---

<h2 class="name">NAME</h2>
<p> dcmftest &#8211; Test if file uses DICOM part 10 format </p>
<h2>SYNOPSIS</h2>
<pre>
dcmftest file...
</pre>
<h2>DESCRIPTION</h2>
<p> The <code>dcmftest</code> utility checks whether the files specified on the command line are DICOM files in part 10 format (with meta-header).</p>
<h2>PARAMETERS</h2>
<pre>
dcmfile-in  DICOM input filename to be dumped
</pre>
<h2>NOTES</h2>
<p> All files specified on the command line are checked for the presence of the DICOM &#8216;magic word&#8217; &#8216;DICM&#8217; at byte position 128. No attempt is made to parse the complete data set. For each file the test result is printed to <i>stdout</i> in the form &#8216;yes: &lt;filename&gt;
&#8217; or &#8216;no: &lt;filename&gt;
&#8217;. The utility terminates with a return code corresponding to the number of files found to be non-DICOM, i.e. if all files pass as DICOM files, the return value is 0. This behaviour is intended for use in shell script programming.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dcmgpdir/">dcmgpdir</a></code>(1), <code><a href="/docs/linux/man/1-dcmmkdir/">dcmmkdir</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1997-2010 by OFFIS e.V., Escherweg 2, 26121 Oldenburg, Germany. </p>
<h2>Index</h2>

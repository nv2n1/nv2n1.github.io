---
title: "gdcmscanner(1)"
name: "gdcmscanner"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdcmscanner/"
description: "gdcmscanner – .TH \"gdcmscanner\" 1 \"Fri Oct 29 2010\" \"Version 2.0.16\" \"GDCM\""
---

<h2 class="name">NAME</h2>
<p> gdcmscanner &#8211; .TH &quot;gdcmscanner&quot; 1 &quot;Fri Oct 29 2010&quot; &quot;Version 2.0.16&quot; &quot;GDCM&quot; </p>
<h2 class="name">NAME</h2>
<p> gdcmscanner &#8211; .SH &quot;SYNOPSIS&quot; </p>
<pre>
gdcmscanner [options] directory
</pre>
<h2>DESCRIPTION</h2>
<p> The <code>gdcmscanner</code> is a command line tool to quickly extract value from a set of DICOM attribute in a DICOM File-Set.</p>
<h3>PARAMETERS</h3>
<pre>
  -d --dir       DICOM directory
  -t --tag %d,%d DICOM tag(s) to look for
</pre>
<h3>OPTIONS</h3>
<pre>
  -p --print      Print output.
  -r --recursive  Recusively descend directory.
</pre>
<h3>general options</h3>
<pre><code>
- h-- help
        print this help text and exit -
    v-- version
        print version information and exit -
    V-- verbose
        verbose
        mode(warning + error)
            .-
    W-- warning
    warning mode,
    print warning information
        - E-- error
        error mode,
    print error information
        - D-- debug
        debug mode,
    print debug information
</code></pre>
<h2>Typical usage</h2>
<h2>Simple usage</h2>
<p> In order to display all the value for Patient Name (0010,0010) in the directory name <code>gdcmData</code>, simply do: </p>
<pre>
$ gdcmscanner -t 10,10 -d gdcmData -p
</pre>
<h2>Complex usage</h2>
<p> Because gdcmscanner does not support progress, you have to wait until all files are traversed to see any results. This is quite cumbersome, on linux this can be worked around with the following trick: </p>
<pre>
$ find gdcmData -type d -exec gdcmscanner -t 10,10 -d {} -p ; 
</pre>
<p> So all directory are locally traversed (no child directory are recursively traversed), which means results comes out much faster.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gdcmdump/">gdcmdump</a></code>(1), <code><a href="/docs/linux/man/1-gdcmraw/">gdcmraw</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2006-2010 Mathieu Malaterre </p>
<h2>Index</h2>

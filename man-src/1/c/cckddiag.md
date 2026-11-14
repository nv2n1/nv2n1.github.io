---
title: "cckddiag(1)"
name: "cckddiag"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cckddiag/"
description: "cckddiag – Hercules CCKD DASD diagnostic tool"
---

<h2>NAME</h2>
<p> <code>cckddiag</code> &#8211; Hercules CCKD DASD diagnostic tool </p>
<h2>SYNOPSIS</h2>
<p> <code>cckddiag</code> [options&#8230;] <code>filename</code> </p>
<h2>DESCRIPTION</h2>
<p> Hercules support tool used to assist in the diagnosis of CCKD DASD problems. Operates on Hercules CCKD DASD volumes in read-only mode, and displays various information contained in CCKD DASD files. Effective usage requires internal knowledge of Hercules CCKD DASD files. </p>
<h2>OPTIONS</h2>
<p> The following options are used to specify which portions of the CCKD DASD file are to be displayed. Options may not be combined; for example, -cd1 is not a valid option. Surround each option by blank(s). </p>
<p> Argument numbers may be specified either in decimal or hexadecimal. If the number begins with the characters 0x the number is presumed to be hexadecimal; else the number is presumed to be decimal. No numeric overflow checking is done, the user is assumed (!) to know what they&#8217;re doing. </p>
<p> Options are divided into three categories: <code>global options</code>, <code>track-related options</code>, and <code>the offset option</code>. </p>
<h2>Global options</h2>
<h3>filename</h3>
<p> specifies the Hercules CCKD DASD filename (sometimes referred to as the DASD image file)</p>
<h3>-v</h3>
<p> display version and exit</p>
<h3>-d</h3>
<p> display DEVHDR</p>
<h3>-c</h3>
<p> display CDEVHDR</p>
<h3>-1</h3>
<p> display L1TAB (note this option is a numeric one)</p>
<h3>-g</h3>
<p> enable debug output </p>
<h2>Track-related options</h2>
<p> To direct cckddiag to a specific track, two options are provided: -a and -r. The remaining track-related options describe the kind of output desired. The TRKHDR for the track is displayed for all track-related options.</p>
<h3>-a cc hh</h3>
<p> display <code>absolute</code> CCHH data &#8211; where <code>cc</code> and <code>hh</code> are respectively the cylinder number (relative zero), and the head number (relative zero).</p>
<h3>-r tt</h3>
<p> display <code>relative</code> track data &#8211; where <code>tt</code> is the track number (relative zero).</p>
<h3>-2</h3>
<p> display L2TAB &#8211; requires a corresponding -a or -r specification to direct cckddiag to a specific track.</p>
<h3>-t</h3>
<p> display track data &#8211; displays the COUNT, KEY, and DATA record summaries for the data residing on the indicated track.</p>
<h3>-x</h3>
<p> hex display track key/data &#8211; displays the KEY and DATA records&#8217; contents in hexadecimal display format for the indicated track. Some repetitive data may be omitted from the hex display output. </p>
<h2>Offset option</h2>
<p> This option provides the ability to examine any portion of the CCKD file, as an alternative to track specification.</p>
<h3>-o oo ll</h3>
<p> hex display data at offset <code>oo</code> of length <code>ll</code>. </p>
<h2>SEE ALSO</h2>
<dl>
<dt><a href="/docs/linux/man/4-cckd/">cckd</a>(4)</p>
<dd>
<dt><a rel="nofollow" href="http://www.hercules-390.org/">http://www.hercules-390.org/</a> the Hercules emulator homepage.</p>
<dd>
<dt><a rel="nofollow" href="http://www.hercules-390.org/cckddasd.html">http://www.hercules-390.org/cckddasd.html</a> which describes</p>
<dd> the Hercules CCKD DASD facility. </p>
</dl>
<h2>HISTORY</h2>
<p> 2003-02-07 originally written by James M. Morrison </p>
<h2>Index</h2>

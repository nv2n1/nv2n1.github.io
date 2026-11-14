---
title: "esdmon(1)"
name: "esdmon"
section: "1"
letter: "e"
url: "/docs/linux/man/1-esdmon/"
---

<h2 class="name">NAME</h2>
 

 esdmon - The Enlightened Sound Daemon 

<h2>DESCRIPTION</h2>

 EsounD monitor. Opens the esd socket and duplicates the stream being sent to the sound device.

<h2>USAGE</h2>

 esdmon [<font SIZE="-1">OPTIONS</font>] [<font SIZE="-1">FILE</font>] 

 Options: 

 <tt>&quot;-s&quot;</tt>, --server=HOSTNAME set EsounD server <tt>&quot;-b&quot;</tt>, output file should be 8-bit <tt>&quot;-m&quot;</tt>, output file should be mono <tt>&quot;-r&quot;</tt> <font SIZE="-1">RATE</font>, set output rate to <font SIZE="-1">RATE</font> 

 <font SIZE="-1">FILE</font> is the file to write the output stream to. Default is stdout.

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/1-esd/">esd</a></i>(1), <i><a HREF="/docs/linux/man/1-esdcat/">esdcat</a></i>(1), <i><a HREF="/docs/linux/man/1-esddsp/">esddsp</a></i>(1), <i><a HREF="/docs/linux/man/1-esdloop/">esdloop</a></i>(1), <i><a HREF="/docs/linux/man/1-esdplay/">esdplay</a></i>(1), <i><a HREF="/docs/linux/man/1-esdsample/">esdsample</a></i>(1), <i><a HREF="/docs/linux/man/1-esd-config/">esd-config</a></i>(1), <i><a HREF="/docs/linux/man/1-esdctl/">esdctl</a></i>(1), <i><a HREF="/docs/linux/man/1-esdfilt/">esdfilt</a></i>(1), <i><a HREF="/docs/linux/man/1-esdrec/">esdrec</a></i>(1) 

<h2>Index</h2>



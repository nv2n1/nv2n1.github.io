---
title: "esdfilt(1)"
name: "esdfilt"
section: "1"
letter: "e"
url: "/docs/linux/man/1-esdfilt/"
---

<h2 class="name">NAME</h2>
 

 esdfilt - The Enlightened Sound Daemon 

<h2>DESCRIPTION</h2>

 EsounD filter. Sample esd filter program that implements halving and doubling, Optionally writing the new data to a seperate file.

<h2>USAGE</h2>

 esdfilt [<font SIZE="-1">OPTIONS</font>] [<font SIZE="-1">FILE</font>] 

 <tt>&quot;-s&quot;</tt>, --server=HOSTNAME set EsounD server <tt>&quot;-b&quot;</tt>, output file should be 8-bit <tt>&quot;-m&quot;</tt>, output file should be mono <tt>&quot;-r&quot;</tt> <font SIZE="-1">RATE</font>, set output rate to <font SIZE="-1">RATE</font> <tt>&quot;-half&quot;</tt> halve each sample <tt>&quot;-double&quot;</tt> double each sample 

 If <font SIZE="-1">FILE</font> is specified, the filtered output will be written there. Otherwise it will be written back to esound to change the output to the sound device.

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/1-esd/">esd</a></i>(1), <i><a HREF="/docs/linux/man/1-esdcat/">esdcat</a></i>(1), <i><a HREF="/docs/linux/man/1-esddsp/">esddsp</a></i>(1), <i><a HREF="/docs/linux/man/1-esdloop/">esdloop</a></i>(1), <i><a HREF="/docs/linux/man/1-esdplay/">esdplay</a></i>(1), <i><a HREF="/docs/linux/man/1-esdsample/">esdsample</a></i>(1), <i><a HREF="/docs/linux/man/1-esd-config/">esd-config</a></i>(1), <i><a HREF="/docs/linux/man/1-esdctl/">esdctl</a></i>(1), <i><a HREF="/docs/linux/man/1-esdmon/">esdmon</a></i>(1), <i><a HREF="/docs/linux/man/1-esdrec/">esdrec</a></i>(1) 

<h2>Index</h2>



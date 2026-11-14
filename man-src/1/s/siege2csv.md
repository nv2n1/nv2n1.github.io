---
title: "siege2csv(1)"
name: "siege2csv"
section: "1"
letter: "s"
url: "/docs/linux/man/1-siege2csv/"
---

<h2 class="name">NAME</h2>
 

 bombardment - Run siege with an ever-increasing number of users 

<h3><font SIZE="-1">SYNOPSIS</font></h3>

 bombardment [urlfile] [clients] [increment] [trials] [delay] bombardment urls.txt 5 10 20 1

<h2>DESCRIPTION</h2>

 bombardment is part of the <tt>siege</tt> distribution. It calls <tt>siege</tt> with an initial number of clients. When that run finishes, it immediately calls siege again with that number of clients plus the increment. It does this the number of times specified in the fourth argument.

<h2>OPTIONS</h2>

 urlfile 
&nbsp;<wbr>The name of the file containing one or more URLs for siege to test. 

 clients 
&nbsp;<wbr>The initial number of clients to be used on the first run. 

 increment 
&nbsp;<wbr>The number of clients to add to each ensuing run. 

 trials 
&nbsp;<wbr>The number of times to run siege. 

 delay 
&nbsp;<wbr>The is the amount of time, in seconds, that each client will wait 
&nbsp;<wbr>between requests.&nbsp;<wbr>&nbsp;<wbr>The&nbsp;<wbr><tt>siege</tt>&nbsp;<wbr>default is overridden by bombardment

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/1-siege/">siege</a></i>(1), <i><a HREF="/docs/linux/man/1-siege2csv/">siege2csv</a></i>(1)

<h2>AUTHOR</h2>

 Written by Peter Hutnick, et al. 

<h2>Index</h2>



<dt><a HREF="#lbAD">DESCRIPTION</a>
<dd>
<dt><a HREF="#lbAE">OPTIONS</a>
<dd>
<dt><a HREF="#lbAF">SEE ALSO</a>
<dd>
<dt><a HREF="#lbAG">AUTHOR</a>
<dd></dl>

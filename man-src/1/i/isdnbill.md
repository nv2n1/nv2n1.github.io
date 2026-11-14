---
title: "isdnbill(1)"
name: "isdnbill"
section: "1"
letter: "i"
url: "/docs/linux/man/1-isdnbill/"
description: "isdnbill – report isdn costs"
---

<h2 class="name">NAME</h2>
<p> isdnbill &#8211; report isdn costs</p>
<h2>DESCRIPTION</h2>
<p> isdnbill is a simple and imperfect utility to show the bill for ISDN calls. Note that it is only for indicative purposes! It works best in Germany, and even then there are no guarantees. Consider its use for educational purposes only&#8230; </p>
<p> For better results, use isdnrep. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-V</code></p>
<dd> show version </p>
<dt><code>-a</code></p>
<dd> show all connections </p>
<dt><code>-e</code></p>
<dd> show incomplete calls </p>
<dt><code>-f</code></p>
<dd> recalculate costs _always_ </p>
<dt><code>-i</code></p>
<dd> show incoming calls </p>
<dt><code>-m</code></p>
<dd> prices without VAT </p>
<dt><code>-n</code></p>
<dd> do _not_ replace numbers with aliases </p>
<dt><code>-o</code></p>
<dd> show outgoing calls </p>
<dt><code>-t</code></p>
<dd> show only current connections </p>
<dt><code>-vn</code></p>
<dd> verbose level n </p>
<dt><code>-Nnnn</code></p>
<dd> show only calls with the specified number </p>
<dt><code>-I</code></p>
<dd> show only calls on the internal S0 bus </p>
<dt><code>-E</code></p>
<dd> show only calls on the external S0 bus </p>
</dl>
<h2>FILES</h2>
<dl>
<dt><code>/var/log/isdn.log</code> or <code>/var/lib/isdn/calls</code></p>
<dd> isdnlog log file with information about all calls. </p>
<dt><code>/etc/isdn/isdn.conf</code></p>
<dd> general configuration </p>
<dt><code>/etc/isdn/callerid.conf</code></p>
<dd> aliases for telephone numbers </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-isdnlog/">isdnlog</a>(5) <a href="/docs/linux/man/8-isdnlog/">isdnlog</a>(8) <a href="/docs/linux/man/1-isdnrep/">isdnrep</a>(1)</code> </p>
<h2>AUTHOR</h2>
<p> This manual page was written by Paul Slootman &lt;paul [at] debian.org&gt;, for Debian GNU/Linux. </p>
<h2>Index</h2>

---

title: "isdnbill(1)"
name: "isdnbill"
section: "1"
letter: "i"
url: "/docs/linux/man/1-isdnbill/"
description: "isdnbill – report isdn costs"
---

<p> isdnbill is a simple and imperfect utility to show the bill for ISDN calls. Note that it is only for indicative purposes! It works best in Germany, and even then there are no guarantees. Consider its use for educational purposes only&#8230; </p>
<p> For better results, use isdnrep. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-V</code></dt>
<dd> show version </dd>
<dt><code>-a</code></dt>
<dd> show all connections </dd>
<dt><code>-e</code></dt>
<dd> show incomplete calls </dd>
<dt><code>-f</code></dt>
<dd> recalculate costs _always_ </dd>
<dt><code>-i</code></dt>
<dd> show incoming calls </dd>
<dt><code>-m</code></dt>
<dd> prices without VAT </dd>
<dt><code>-n</code></dt>
<dd> do _not_ replace numbers with aliases </dd>
<dt><code>-o</code></dt>
<dd> show outgoing calls </dd>
<dt><code>-t</code></dt>
<dd> show only current connections </dd>
<dt><code>-vn</code></dt>
<dd> verbose level n </dd>
<dt><code>-Nnnn</code></dt>
<dd> show only calls with the specified number </dd>
<dt><code>-I</code></dt>
<dd> show only calls on the internal S0 bus </dd>
<dt><code>-E</code></dt>
<dd> show only calls on the external S0 bus </dd>
</dl>
<h2>FILES</h2>
<dl>
<dt><code>/var/log/isdn.log</code> or <code>/var/lib/isdn/calls</code></dt>
<dd> isdnlog log file with information about all calls. </dd>
<dt><code>/etc/isdn/isdn.conf</code></dt>
<dd> general configuration </dd>
<dt><code>/etc/isdn/callerid.conf</code></dt>
<dd> aliases for telephone numbers </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-isdnlog/">isdnlog</a>(5) <a href="/docs/linux/man/8-isdnlog/">isdnlog</a>(8) <a href="/docs/linux/man/1-isdnrep/">isdnrep</a>(1)</code> </p>
<h2>AUTHOR</h2>
<p> This manual page was written by Paul Slootman &lt;paul [at] debian.org&gt;, for Debian GNU/Linux. </p>

---

title: "vboxtoau(1)"
name: "vboxtoau"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vboxtoau/"
description: "vboxtoau – isdn voice box (sound converter)"
---

<h2>NAME</h2>
<p> vboxtoau &#8211; isdn voice box (sound converter)</p>
<p> <code>vboxtoau</code> <i>[OPTION] [OPTION] [&#8230;] &lt; INFILE &gt; OUTFILE</i></p>
<p> With vboxtoau you can convert files with vbox audio header to .au files (sun audio format). vboxtoau is a link to vboxcnvt.</p>
<h2>OPTIONS</h2>
<p> Vboxtoau reads from stdin and writes to stdout.</p>
<dl>
<dt><code>-r, &#8211;samplerate RATE</code></dt>
<dd> Samplerate to write into the header of the output file. There is no sound conversion! Default is 8000.</dd>
<dt><code>-u, &#8211;ulaw</code></dt>
<dd> Convert to 8-bit ulaw.</dd>
<dt><code>-1, &#8211;linear8</code></dt>
<dd> Convert to 8-bit linear.</dd>
<dt><code>-2, &#8211;linear16</code></dt>
<dd> Convert to 16-bit linear. (Default)</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> Show summary of options.</dd>
<dt><code>-v, &#8211;version</code></dt>
<dd> Show version of program.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-autovbox/">autovbox</a>(1), <a href="/docs/linux/man/1-rmdtovbox/">rmdtovbox</a>(1), <a href="/docs/linux/man/1-vboxmode/">vboxmode</a>(1), <a href="/docs/linux/man/1-vboxcnvt/">vboxcnvt</a>(1), <a href="/docs/linux/man/5-vbox/">vbox</a>(5)</code></p>
<h2>AUTHOR</h2>
<p> This manual page was written by Andreas Jellinghaus &lt;aj [at] dungeon.inka.de&gt;, for Debian GNU/Linux and isdn4linux. </p>

---
title: "sendfax(8)"
name: "sendfax"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sendfax/"
description: "sendfax – send group 3 fax files (G3 files) with a class 2 faxmodem"
---

<p>sendfax &#8211; send group 3 fax files (G3 files) with a class 2 faxmodem</p>
<h2>Synopsis</h2>
<p><code>sendfax</code> [<code>-p</code>] [<code>-x</code>&lt;debug<code>level&gt;</code>] [<code>-v</code>] [<code>-l</code>&lt;modem<code>lines&gt;</code>] [<code>-m</code>&lt;initstring&gt;<code>]</code> [<code>-d</code>&lt;poll<code>directory&gt;</code>] [<code>-C</code>&lt;modem<code>class&gt;</code>] [<code>-S</code>] [<code>-n</code>] [<code>-r</code>] [<code>-D</code>&lt;dial<code>prefix&gt;</code>] phone-number [<i>g3file(s)</i>]</p>
<h2>Description</h2>
<p>Send the named g3 fax files to the fax machine at &quot;phone number&quot;. The g3 files can be created with <a href="/docs/linux/man/1-pbm2g3/">pbm2g3</a>(1) or GNU&#8217;s GhostScript with the &quot;digifax&quot; driver.</p>
<h2>Options</h2>
<dl>
<dt><code>-p</code></p>
<dd>Tells <i>sendfax</i> to try fax polling, that is, get any documents queued in the remote fax machine for you (used for weather maps and the like)</p>
<dt><code>-x &lt;debug level&gt;</code></p>
<dd>Use the given level of verbosity for logging &#8211; 0 means no logging, 5 is really noisy.</p>
<dt><code>-v</code></p>
<dd>Give some progress report on stdout.</p>
<dt><code>-l &lt;modem lines&gt;</code></p>
<dd>Use the given modem lines. Multiple lines can be separated by &quot;:&quot;. Example: sendfax -l tty1a:tty2a</p>
<dt><code>-m &lt;initstring&gt;</code></p>
<dd>Send an additional init string. This string is sent right after initializing the modem and setting it into class 2 mode. You can use this to set the speaker value, some special registers, whatsoever. The modem must return &quot;OK&quot;. If it returns &quot;ERROR&quot;, sendfax prints an error message and aborts. You do not have to prepend the &quot;AT&quot; prefix, but it won&#8217;t do harm either.</p>
<dt><code>-d &lt;directory&gt;</code></p>
<dd>Specify the directory where polled fax files should go to. Defaults to &quot;.&quot; for the current directory. Unused if not polling a fax.</p>
<dt><code>-C &lt;class&gt;</code></p>
<dd>Tells <i>sendfax</i> how to treat the modem. Possible values for &lt;class&gt; are &quot;auto&quot; (default, try to find out which fax command set the modem supports), &quot;cls2&quot; (use the class 2 fax command set, even if the modem claims to support class 2.0) and &quot;c2.0&quot; (use the class 2.0 fax command set). Obviously, &quot;data&quot; (which is valid for &quot;mgetty -C &#8230;&quot;) is not of much use here.</p>
<dt><code>-S</code></p>
<dd>Assume modem connection on stdin, do not try to lock or initialize anything. To take over existing connection (for interworking with vgetty et.al.) use with a dial string of &quot;T1&quot; (just a short beep, no phone number at all would confuse many modems, a pulse dialed number may confuse the telco switch) and &quot;-m ATX1&quot; (do not wait for dial tone).</p>
<dt><code>-n</code></p>
<dd>Tells <i>sendfax</i> to send the fax pages in &#8220;normal&#8221; (204&#215;98 dpi) mode. Default is &#8220;fine&#8221; mode (204&#215;196 dpi).</p>
<dt><code>-r</code></p>
<dd>If this option is given, <i>sendfax</i> will rename all the fax G3 files to &#8220;&lt;filename&gt;.done&#8221; after successfully sending this. This is intended to be used from &#8220;faxrunq&#8221;, to make sure that a partially-sended fax isn&#8217;t retransmitted as a whole every time. </p>
<p> If this option is set, sendfax will not (!) complain if not all files named on the command line exist.</p>
<dt><code>-D &lt;dial prefix&gt;</code></p>
<dd>Override the default (set by sendfax.config or in policy.h) for the &#8216;ATxxx&#8217; command to dial the remote number. This is rarely used from the command line, but you might want to use it in combination with faxrunqd&#8217;s policy routing option (see example in <a href="/docs/linux/man/5-faxrunqd-policy/">faxrunqd.policy</a>(5)).</p>
<dt><code>-M &lt;max speed&gt;</code></p>
<dd>Sets the maximum transmission (modem to modem) speed. This is only needed in very rare cases, because normally the modems negotiate the correct speed automatically. Example: &quot;-M 7200&quot;.</p>
<dt><code>-R &lt;max tries&gt;</code></p>
<dd>Sets the maximum number of attempts to transmit a given page, before <i>sendfax</i> gives up on this page. Normally it&#8217;s not needed to change this &#8211; the default is &quot;(up to) 3 tries&quot; and that works quite well for most environments. </p>
</dl>
<h2>Config File</h2>
<p>If compiled accordingly, <i>sendfax</i> can read all its configuration from at run-time from a file, usually called /etc/mgetty+sendfax/sendfax.config. See the documentation in the mgetty.info manual for details.</p>
<h2>Diagnostics</h2>
<p><i>sendfax</i> returns an error code, according to the reason why the program terminated. If everything went OK, <i>sendfax</i> returns 0. If &#8220;harmless&#8221; errors (didn&#8217;t cost money) occured, an error code below 10 is returned. If a dial attempt failed after the remote end picked up (it will cost money), a return code of 10 or higher is returned. </p>
<p> In Detail, the return codes are as follows:</p>
<dl>
<dd>
<dl>
<dt>0</p>
<dd>all pages have been transmitted successfully</p>
<dt>1</p>
<dd>error on the sendfax command line</p>
<dt>2</p>
<dd>cannot open fax device (e.g. due to locked modem)</p>
<dt>3</p>
<dd>cannot initialize modem (e.g. modem switched off)</p>
<dt>4</p>
<dd>dialup failed with BUSY</p>
<dt>5</p>
<dd>dialup failed with NO DIALTONE</p>
<dt>10</p>
<dd>dialup failed with ERROR or NO CARRIER (modem handshake failed)</p>
<dt>11</p>
<dd>waiting for XON failed (rarely seen)</p>
<dt>12</p>
<dd>transmitting or polling page(s) failed (connection dropped)</dl>
</dl>
<p> Very detailed debug information is written to the log file. It can be found in &quot;/var/log/sendfax.log&quot;. If it doesn&#8217;t contain enough details, enhance the log level with the &quot;-x&quot; option to sendfax, e.g. &quot;-x 5&quot;. </p>
<p> Many of the common problems and solutions are discussed in the mgetty manual and the FAQ. Please see the WWW page at <a rel="nofollow" href="http://alpha.greenie.net/mgetty/">http://alpha.greenie.net/mgetty/</a> for both.</p>
<h2>References</h2>
<p>The standard for Group 3 fax is defined in CCITT Recommendation T.4.</p>
<h2>Bugs</h2>
<p><i>sendfax</i> should be able to put a header on the page. <i>sendfax</i> should be able to read TIFF g3 input files. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-g3cat/">g3cat</a>(1), <a href="/docs/linux/man/1-pbm2g3/">pbm2g3</a>(1), <a href="/docs/linux/man/1-mgetty/">mgetty</a>(1), <a href="/docs/linux/man/1-faxspool/">faxspool</a>(1), <a href="/docs/linux/man/1-faxrunq/">faxrunq</a>(1), <a href="/docs/linux/man/8-faxrunqd/">faxrunqd</a>(8)</p>
<h2>Author</h2>
<p><i>sendfax</i> is Copyright (C) 1993 by Gert Doering, &lt;gert [at] greenie.muc.de&gt;.</p>

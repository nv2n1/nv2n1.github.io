---
title: "mgetty(8)"
name: "mgetty"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mgetty/"
description: "mgetty – smart modem getty"
---

<p>mgetty &#8211; smart modem getty</p>
<h2>Synopsis</h2>
<p><code>mgetty</code> [<code>options</code>] ttydevice [<i>gettydefs</i>]</p>
<h2>Description</h2>
<p>Mgetty is a &#8220;smart&#8221; getty replacement, designed for use with Hayes compatible data and data/fax modems. Mgetty knows about modem initialization, manual modem answering (so your modem doesn&#8217;t answer if the machine isn&#8217;t ready), UUCP locking (so you can use the same device for dial-in and dial-out). Mgetty provides very extensive logging facilities. This manpage doesn&#8217;t try to detail mgetty setup in detail, it just lists the most important options. For detailed instructions, see the info file mgetty.info (mgetty.texi). </p>
<h2>Options</h2>
<dl>
<dt><code>-k &lt;space&gt;</code></p>
<dd>Tells <i>mgetty</i> to leave &lt;space&gt; kbytes free on disk when receiving a fax.</p>
<dt><code>-x &lt;debug level&gt;</code></p>
<dd>Use the given level of verbosity for logging &#8211; 0 means no logging, 9 is really noisy. The log file is usually /tmp/log_mg.&lt;device&gt;</p>
<dt><code>-s &lt;speed&gt;</code></p>
<dd>Set the port speed to use, e.g. &quot;-s 19200&quot;.</p>
<dt><code>-r</code></p>
<dd>Tells <i>mgetty</i> that it is running on a direct line. UUCP locking is done, but no modem initialization whatsoever.</p>
<dt><code>-p &lt;login prompt&gt;</code></p>
<dd>Use the given string to prompt users for their login names. Various tokens are allowed in this string. These tokens are: @ for the system name, 
, \g, , for newline, bell, and form feed, respectively.  and  will expand to the OS version and release. \P, \l and \L will expand to the tty name (&quot;ttyS0&quot;). \Y will give the Caller ID, \I the &quot;CONNECT foobar&quot; string returned by the modem, and \S or  will output the port speed. \N and 

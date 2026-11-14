---
title: "ascii-xfr(1)"
name: "ascii-xfr"
section: "1"
letter: "a"
url: "/docs/linux/man/1-ascii-xfr/"
description: "ascii-xfr – upload/download files using the ASCII protocol"
---

<h2>NAME</h2>
<p> ascii-xfr &#8211; upload/download files using the ASCII protocol</p>
<h2>SYNOPSIS</h2>
<p> <code>ascii-xfr</code> <code>-s|-r</code> [<code>-ednv</code>] [<code>-l</code> <i>linedelay</i>] [<code>-c</code> <i>characterdelay</i>] <i>filename</i></p>
<h2>DESCRIPTION</h2>
<p> <code>Ascii-xfr</code> Transfers files in ASCII mode. This means no flow control, no checksumming and no file-name negotiation. It should <i>only</i> be used if the remote system doesn&#8217;t understand anything else. </p>
<p> The ASCII protocol transfers files line-by-line. The EOL (End-Of-Line) character is transmitted as CRLF. When receiving, the CR character is stripped from the incoming file. The Control-Z (ASCII 26) character signals End-Of-File, if option -e is specified (unless you change it to Control-D (ASCII 4) with -d). </p>
<p> <code>Ascii-xfr</code> reads from <i>stdin</i> when receiving, and sends data on <i>stdout</i> when sending. Some form of input or output redirection to the modem device is thus needed when downloading or uploading, respectively.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-s</code></p>
<dd> Send a file.</p>
<dt><code>-r</code></p>
<dd> Receive a file. One of <code>-s</code> or <code>-r</code> <i>must</i> be present.</p>
<dt><code>-e</code></p>
<dd> Send the End-Of-File character (Control-Z, ASCII 26 by default) when uploading has finished.</p>
<dt><code>-d</code></p>
<dd> Use the Control-D (ASCII 4) as End-Of-File character.</p>
<dt><code>-n</code></p>
<dd> Do not translate CR to CRLF and vice versa.</p>
<dt><code>-v</code></p>
<dd> Verbose: show transfer statistics on the stderr output.</p>
<dt><code>-l</code> <i>milliseconds</i></p>
<dd> When transmitting, pause for this delay after each line.</p>
<dt><code>-c</code> <i>milliseconds</i></p>
<dd> When transmitting, pause for this delay after each character.</p>
<dt><i>file</i></p>
<dd> Name of the file to send or receive. When receiving, any existing file by this name will be truncated.</dl>
<h2>USAGE WITH MINICOM</h2>
<p> If you want to call this program from <code><a href="/docs/linux/man/1-minicom/">minicom</a>(1)</code>, start minicom and go to the <code>O</code>ptions menu. Select <i>File transfer protocols</i>. Add the following lines, for example as protocols <code>I</code> and <code>J</code>. </p>
<pre>
I  Ascii    /usr/bin/ascii-xfr -sv   Y   U   N   Y
J  Ascii    /usr/bin/ascii-xfr -rv   Y   D   N   Y
</pre>
<h2>AUTHOR</h2>
<p> Miquel van Smoorenburg, miquels [at] cistron.nl<br />
 Jukka Lahtinen, walker [at] netsonic.fi</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-minicom/">minicom</a>(1) </p>
<h2>Index</h2>

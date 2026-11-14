---
title: "axgetput(1)"
name: "axgetput"
section: "1"
letter: "a"
url: "/docs/linux/man/1-axgetput/"
description: "axgetput – upload or download files via AX.25 / axspawn Linux login session."
---

<h2>NAME</h2>
<p> axgetput &#8211; upload or download files via AX.25 / axspawn Linux login session.</p>
<h2>SYNOPSIS</h2>
<p> <code>axgetput</code> [-b <i>blocksize</i>] [-i] [-v] [-h] [?] <i>filename</i><br />
 <code>axgetput</code> [-b <i>blocksize</i>] [-i] -s [-v] [-h] [?] [<i>filename</i>] </p>
<h2>DESCRIPTION</h2>
<dl>
<dt><code>-b blocksize</code></p>
<dd> Set the blocksize (frame length) of transmitted data. Defaults to 256 bytes which matches typical AX.25 network confurations best.</p>
<dt><code>-i</code></p>
<dd> Compute CRC checksum only.</p>
<dt><code>.B -s</code></p>
<dd> Indicates input from a stream. This option is available only if STDIN is a pipe. The filename argument may be omitted if -s is given. The length of the file need not to be known.</p>
<dt><code>-v</code></p>
<dd> print version and exit.</p>
<dt><code>-h, ?</code></p>
<dd> print usage and exit.</dl>
<p> <code>axgetput</code> is the actual name of the program. You execute for e.g. <code>bget</code> or <code>bput</code> while axgetput is the common program to which bget and bput are linked to. axgetput autodetermines which operation mode the user desires. </p>
<p> axgetput sets the pty to be 8bit clean (thus enables binary mode for the file transfer). It requires that the user is logged in through <a href="/docs/linux/man/8-axspawn/">axspawn</a>(8). </p>
<p> <code>I. #BIN Protocol</code> </p>
<p> <code>bget</code> is used for downloading a file on this system from the unix login shell via his ax25 session to his packet-radio terminal program. The download &quot;protocol&quot; is the &quot;#BIN&quot; standard known from packet radio mailboxes. </p>
<p> <code>bput</code> does it the other way round: with this comand, the user may upload a file to this computer. </p>
<p> The #BIN protocol provides a CRC consistency check after the file is transfered. The transfer of the file modification time is part of the #BIN protocol. </p>
<p> <code>II. YAPP Protocol</code> </p>
<p> <code>yget</code> or <code>yput</code> is reserverd for the yapp protocol, which is not supported in this version. </p>
<p> <code>II. DIDADIT Protocol</code> </p>
<p> <code>rget</code> or <code>rput</code> is reserverd for the didadit protocol, which is not supported in this version. </p>
<p> Anyone like to implement yapp and didadit protcols? </p>
<h2>AUTHOR</h2>
<p> Thomas Osterried DL9SAU &lt;thomas [at] x-berg.in-berlin.de&gt; Ralf Baechle DL5RB &lt;ralf [at] linux-mips.org&gt; </p>
<h2>Index</h2>

---
title: "pamexec(1)"
name: "pamexec"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamexec/"
description: "pamexec – Execute a shell command on each image in a Netpbm image stream"
---

<h2 class="name">NAME</h2>
<p> pamexec &#8211; Execute a shell command on each image in a Netpbm image stream</p>
<h2>SYNOPSIS</h2>
<p> <code>pamexec</code> </p>
<p> [&#8216;<i>command</i>&#8216;] </p>
<p> [<i>netpbmfile</i>] </p>
<p> [<code>-check</code>] </p>
<p> Minimum unique abbreviation of option is acceptable. You may use double hyphens instead of single hyphen to denote options. You may use white space in place of the equals sign to separate an option name from its value. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamexec</code> reads a Netpbm image stream as input. For each image, it runs a specified shell command and supplies the image to it as Standard Input (with a pipe). </p>
<p> <i>netpbmfile</i> is the file name of the input file, or <code>&#8211;</code> to indicate Standard Input. The default is Standard Input. </p>
<p> Many Netpbm programs understand multimage Netpbm streams themselves, so you don&#8217;t need to use <code>pamexec</code> to run the program on the images in the stream. Ideally, all Netpbm programs would have that capability, but multi-image streams are a relatively recent invention, so older Netpbm programs just process the first image in the stream and then stop. Even recently written Netpbm programs work that way, since the authors aren&#8217;t aware of the multi-image possibility. </p>
<p> Another way to process a multi-image stream is to use <code>pamsplit</code> to explode it into multiple files, one image per file. You can then process those files. </p>
<p> To run your command on a subset of the images in the stream, use <code>pampick</code> to select the desired images from the input stream and pipe the result to <code>pamexec</code>. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-check</code></p>
<dd> This causes <code>pamexec</code> to exit without processing any further images if the command has a nonzero exit status. </p>
</dl>
<h2>APPLICATIONS</h2>
<p> To make an animated GIF movie: </p>
<pre>
<tt>
    pamexec pamtogif myvideo.ppm | gifsicle --multifile &gt;myvideo.gif
</tt>
</pre>
<h2>LIMITATIONS</h2>
<p> <code>pamexec</code> assumes all commands consume all of Standard Input. If yours doesn&#8217;t (perhaps it just exits when it&#8217;s seen enough), you can buffer through a temporary file like this: </p>
<pre>
<tt>
    pamexec 'cat &gt;/tmp/x; head -3 x' myvideo.ppm  
</tt>
</pre>
<h2>HISTORY</h2>
<p> <code>pamexec</code> was new in Netpbm 10.56 (September 2011). </p>
<p> Michael Pot wrote it, borrowing from <code>pamsplit</code>. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pamfile/">pamfile</a></code>(1) , <code><a href="/docs/linux/man/1-pampick/">pampick</a></code>(1) , <code><a href="/docs/linux/man/1-pampick/">pampick</a></code>(1) , <code><a href="/docs/linux/man/1-pnm/">pnm</a></code>(1) , <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) , <code>cat</code> man page </p>
<h2>Index</h2>

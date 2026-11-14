---
title: "pamchannel(1)"
name: "pamchannel"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamchannel/"
description: "pamchannel – extract channels from a PAM image"
---

<h2 class="name">NAME</h2>
<p> pamchannel &#8211; extract channels from a PAM image</p>
<h2>SYNOPSIS</h2>
<p> <code>pamchannel</code> [<code>-infile </code><i>infile</i>] [<code>-tupletype </code><i>tupletype</i>] [<i>channum</i> &#8230;] </p>
<p> Minimum unique abbreviation of option is acceptable. You may use double hyphens instead of single hyphen to denote options. You may use white space in place of the equals sign to separate an option name from its value. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamchannel</code> reads a PAM or PNM image as input and produces a PAM image as output, consisting of the indicated channels (planes) of the input. </p>
<p> Each <i>channum</i> argument is the number of a channel of the input, with the first channel being zero. The channels in the output are in the order of these arguments. </p>
<p> The output is the same dimensions as the input, except that the depth is the number of <i>channum</i> arguments you supply. The tuple type is a null string unless you specify the <code>-tupletype</code> option. </p>
<p> This program works on multi-image streams, producing a corresponding output stream. But before Netpbm 10.32 (February 2006), it ignored every image after the first. </p>
<p> <code>pamstack</code> does the opposite of <code>pamchannel</code>: It takes multiple PAM or PNM images as input and stacks their planes (channels) on top of one another to yield a single PAM. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-infile</code> <i>infile</i></p>
<dd> This specifies the input file, which defaults to Standard Input. You may specify <code>&#8211;</code> to select Standard Input explicitly. </p>
<p> This is a little unconventional for Netpbm programs, which usually have the input file specification as an argument. For <code>pamchannel</code>, the arguments are channel numbers. </p>
<dt><code>-tupletype</code> <i>tupletype</i></p>
<dd> This specified the tuple type name to be recorded in the output. You may use any string up to 255 characters. Some programs recognize some names. If you omit this option, the default tuple type name is null. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) </p>
<p> <code><a href="/docs/linux/man/1-pamstack/">pamstack</a></code>(1) </p>
<h2>HISTORY</h2>
<p> <code>pamchannel</code> was new, along with the PAM format, in Netpbm 9.7 (August 2000). </p>
<h2>Index</h2>

---
title: "gpscat(1)"
name: "gpscat"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gpscat/"
description: "gpscat – dump the output from a GPS"
---

<h2 class="name">NAME</h2>
<p> gpscat &#8211; dump the output from a GPS </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>gpscat</code> [-s&nbsp;<wbr><i>speed</i>] [-p] [-t] [-D&nbsp;<wbr><i>debuglevel</i>] <i>file-or-serial-port</i></dl>
<h2>DESCRIPTION</h2>
<dd>gpscat is a simple program for logging and packetizing GPS data streams. It takes input from a specified file or serial device (presumed to have a GPS attached) and reports to standard output. The program runs until end of input or it is interrupted by ^C or other means. It does not terminate on a bad backet; this is intentional. </p>
<p> In raw mode (the default) gpscat simply dumps its input to standard output. Nonprintable characters other than ASCII whitespace are rendered as hexadecimal string escapes. </p>
<p> In packetizing mode, gpscat uses the same code as <code><a href="/docs/linux/man/8-gpsd/">gpsd</a></code>(8)&#8217;s packet sniffer to break the input into packets. Packets are reported one per line; line breaks in the packets themselves are escaped. </p>
<p> This program is useful as a sanity checker when examining a new device. It can be used as a primitive NMEA logger, but beware that (a) interrupting it likely to cut off output in mid-sentence, and (b) to avoid displaying incomplete NMEA sentences right up next to shell prompts that often contain a $, raw mode always emits an extra final linefeed. </p>
<p> Also, be aware that packetizing mode will produce useless results &#8212; probably consuming the entirety of input and appearing to hang &#8212; if it is fed data that is not a sequence of packets of one of the known types. </p>
<p> The program accepts the following options: </p>
<p> -p</p>
<dl>
<dt>
<dd> Invoke packetizer mode.</dl>
<p> -s</p>
<dl>
<dt>
<dd> Set the port&#8217;s baud rate (and optionally its parity and stop bits) before reading. Argument should begin with one of the normal integer baud rates (300, 1200, 4800, 9600, 19200, 38400, etc.). It may be followed by an optional suffix [NOE][12] to set parity (None, Even, Odd) and stop bits (1 or 2).</dl>
<p> -t</p>
<dl>
<dt>
<dd> Invoke packetizer mode, with the packet type and length (in parentheses) reported before a colon and space on each line.</dl>
<p> -D</p>
<dl>
<dt>
<dd> In packetizer mode, enable progress messages from the packet getter. Probably only of interest to developers testing packet getter changes.</dl>
<p> -h</p>
<dl>
<dt>
<dd> Display program usage and exit.</dl>
<p> Specifying -s 4800N1 is frequently helpful with unknown devices.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-gpsd/">gpsd</a></code>(8), <code><a href="/docs/linux/man/1-gps/">gps</a></code>(1), <code><a href="/docs/linux/man/3-libgps/">libgps</a></code>(3), <code><a href="/docs/linux/man/3-libgpsd/">libgpsd</a></code>(3), <code><a href="/docs/linux/man/1-gpsfake/">gpsfake</a></code>(1). <code><a href="/docs/linux/man/1-gpsprof/">gpsprof</a></code>(1), <code><a href="/docs/linux/man/1-gpsctl/">gpsctl</a></code>(1), <code><a href="/docs/linux/man/8-gpsdctl/">gpsdctl</a></code>(8), <code><a href="/docs/linux/man/1-gpsmon/">gpsmon</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> Eric S. Raymond &lt;esr [at] thyrsus.com&gt;. </p>
<h2>Index</h2>

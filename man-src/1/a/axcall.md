---
title: "axcall(1)"
name: "axcall"
section: "1"
letter: "a"
url: "/docs/linux/man/1-axcall/"
description: "axcall – make an AX.25, NET/ROM or Rose connection."
---

<h2>NAME</h2>
<p> axcall &#8211; make an AX.25, NET/ROM or Rose connection.</p>
<h2>SYNOPSIS</h2>
<p> For AX.25<br />
 <code>axcall [-b l|e] [-d] [-h] [-m s|e] [-p paclen] [-r] [-t] [-v] [-w window] port callsign [[via] digipeaters&#8230;..]</code> </p>
<p> For NET/ROM<br />
 <code>axcall [-d] [-h] [-p paclen] [-r] [-t] [-v] port callsign</code> </p>
<p> For Rose<br />
 <code>axcall [-d] [-h] [-r] [-t] [-v] port callsign address [[via] digipeater]</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>Axcall</code> is the general purpose AX.25, NET/ROM and Rose connection program. As is normal in AX.25 it runs entirely in line mode. All CR/LF translation is done transparently. The program provides ASCII, YAPP, YAPP-C and 7+ file transfer facilities. Some of the options are only valid in AX.25 mode, the program will quietly ignore them if given in NET/ROM mode or in Rose mode. </p>
<p> This version of <code>axcall</code> incorporates many changes that include a much improved user interface. The port name is mandatory and is the name of the port which the connection will be made on. The port name may be either an AX.25, a NET/ROM port or a Rose port, <code>axcall</code> will determine which automatically. </p>
<p> When using NET/ROM the use of digipeaters is meaningless and is not supported. However when using Rose up to one digipeater may be specified, as well as the Rose address of the distant node and the callsign of the remote station. The Rose address must be ten digits long and it must exist in the Rose node tables. For Rose connects to work <code>axparms</code> must have been used to set a callsign/uid mapping for the userid in use.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b l|e</code></p>
<dd> Sets the method of backoff to use with AX.25 connections. The default is taken from the port specification, but can be overridden by this option. Valid values are <code>l</code> for linear backoff, and <code>e</code> for exponential backoff.</p>
<dt><code>-d</code></p>
<dd> Turn on socket level debugging.</p>
<dt><code>-h</code></p>
<dd> Selects Slave mode.</p>
<dt><code>-m s|e</code></p>
<dd> Sets the AX.25 mode to use. The default is taken from the port specification, but can be overridden by this option. Valid values are <code>s</code> for normal (modulus 8) AX.25 operation, or <code>e</code> for extended (modulus 128) AX.25 operation.</p>
<dt><code>-p paclen</code></p>
<dd> Specify a specific maximum amount of data to be sent in each AX.25 packet.</p>
<dt><code>-r</code></p>
<dd> Selects Raw mode.</p>
<dt><code>-t</code></p>
<dd> Selects Talk mode.</p>
<dt><code>-v</code></p>
<dd> Display the version.</p>
<dt><code>-w window</code></p>
<dd> Specify a specific AX.25 window for this connection. Only valid in AX.25 mode.</dl>
<p> The axcall program interprets lines beginning with a &#8216;~&#8217; specially. The following &#8216;~&#8217; escapes are available.</p>
<dl>
<dt><code>~?</code></p>
<dd> List escapes</p>
<dt><code>~~</code></p>
<dd> A ~ symbol</p>
<dt><code>~.</code></p>
<dd> Close connection</p>
<dt><code>~! [command]</code></p>
<dd> Run a command</p>
<dt><code>~0</code></p>
<dd> Change to Raw mode</p>
<dt><code>~1</code></p>
<dd> Change to Slave mode</p>
<dt><code>~2</code></p>
<dd> Change to Talk mode</p>
<dt><code>~a</code></p>
<dd> Start a file transfer (Autobin)</p>
<dt><code>~b</code></p>
<dd> Start a file transfer (Binary)</p>
<dt><code>~c</code></p>
<dd> Close the logfile</p>
<dt><code>~h</code></p>
<dd> List escapes</p>
<dt><code>~o [filename]</code></p>
<dd> Open a logfile (default &#8216;logfile.txt&#8217;)</p>
<dt><code>~r</code></p>
<dd> Reconnect to remote station</p>
<dt><code>~s</code></p>
<dd> Stop an upload</p>
<dt><code>~u [filename]</code></p>
<dd> Upload a file (ASCII upload)</p>
<dt><code>~yu [filename]</code></p>
<dd> Upload a file (YAPP upload)</p>
<dt><code>~yd [filename]</code></p>
<dd> Download a file (YAPP download)</p>
<dt><code>~z</code></p>
<dd> Suspend program</dl>
<p> The program provides no terminal emulation features. These are left up to the console facilities of the terminal in use. The program is however &#8216;8 bit clean&#8217;.</p>
<h2>FILES</h2>
<pre>
/proc/net/nr_nodes
<br>
/proc/net/rose_nodes
<br>
/etc/ax25/axports
<br>
/etc/ax25/nrports
<br>
/etc/ax25/rsports
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-axlisten/">axlisten</a></code>(1), <code><a href="/docs/linux/man/1-mheard/">mheard</a></code>(1), <code><a href="/docs/linux/man/4-ax25/">ax25</a></code>(4), <code><a href="/docs/linux/man/4-netrom/">netrom</a></code>(4), <code><a href="/docs/linux/man/4-rose/">rose</a></code>(4), <code><a href="/docs/linux/man/5-axports/">axports</a></code>(5), <code><a href="/docs/linux/man/5-nrports/">nrports</a></code>(5), <code><a href="/docs/linux/man/5-rsports/">rsports</a></code>(5), <code><a href="/docs/linux/man/8-axparms/">axparms</a></code>(8), <code><a href="/docs/linux/man/8-nrparms/">nrparms</a></code>(8), <code><a href="/docs/linux/man/8-rsparms/">rsparms</a></code>(8).</p>
<h2>AUTHORS</h2>
<pre><code>
Alexander Tietzel DG6XA&lt;TIETZE_A[at] etech.fh - hamburg.de&gt;

    Joerg Reuter DL1BKE&lt;jreuter[at] poboxes.com&gt;

        Alan Cox GW4PTS&lt;alan[at] cymru.net&gt;

            Jonathan Naylor G4KLX&lt;g4klx[at] g4klx.demon.co.uk&gt;

                Steve Henson G6IXS&lt;shenson[at] nyx.cs.du.edu&gt;
</code></pre>
<h2>Index</h2>

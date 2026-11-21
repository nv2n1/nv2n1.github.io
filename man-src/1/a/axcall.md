---

title: "axcall(1)"
name: "axcall"
section: "1"
letter: "a"
url: "/docs/linux/man/1-axcall/"
description: "axcall – make an AX.25, NET/ROM or Rose connection."
---

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
<dt><code>-b l|e</code></dt>
<dd> Sets the method of backoff to use with AX.25 connections. The default is taken from the port specification, but can be overridden by this option. Valid values are <code>l</code> for linear backoff, and <code>e</code> for exponential backoff.</dd>
<dt><code>-d</code></dt>
<dd> Turn on socket level debugging.</dd>
<dt><code>-h</code></dt>
<dd> Selects Slave mode.</dd>
<dt><code>-m s|e</code></dt>
<dd> Sets the AX.25 mode to use. The default is taken from the port specification, but can be overridden by this option. Valid values are <code>s</code> for normal (modulus 8) AX.25 operation, or <code>e</code> for extended (modulus 128) AX.25 operation.</dd>
<dt><code>-p paclen</code></dt>
<dd> Specify a specific maximum amount of data to be sent in each AX.25 packet.</dd>
<dt><code>-r</code></dt>
<dd> Selects Raw mode.</dd>
<dt><code>-t</code></dt>
<dd> Selects Talk mode.</dd>
<dt><code>-v</code></dt>
<dd> Display the version.</dd>
<dt><code>-w window</code></dt>
<dd> Specify a specific AX.25 window for this connection. Only valid in AX.25 mode.</dd></dl>
<p> The axcall program interprets lines beginning with a &#8216;~&#8217; specially. The following &#8216;~&#8217; escapes are available.</p>
<dl>
<dt><code>~?</code></dt>
<dd> List escapes</dd>
<dt><code>~~</code></dt>
<dd> A ~ symbol</dd>
<dt><code>~.</code></dt>
<dd> Close connection</dd>
<dt><code>~! [command]</code></dt>
<dd> Run a command</dd>
<dt><code>~0</code></dt>
<dd> Change to Raw mode</dd>
<dt><code>~1</code></dt>
<dd> Change to Slave mode</dd>
<dt><code>~2</code></dt>
<dd> Change to Talk mode</dd>
<dt><code>~a</code></dt>
<dd> Start a file transfer (Autobin)</dd>
<dt><code>~b</code></dt>
<dd> Start a file transfer (Binary)</dd>
<dt><code>~c</code></dt>
<dd> Close the logfile</dd>
<dt><code>~h</code></dt>
<dd> List escapes</dd>
<dt><code>~o [filename]</code></dt>
<dd> Open a logfile (default &#8216;logfile.txt&#8217;)</dd>
<dt><code>~r</code></dt>
<dd> Reconnect to remote station</dd>
<dt><code>~s</code></dt>
<dd> Stop an upload</dd>
<dt><code>~u [filename]</code></dt>
<dd> Upload a file (ASCII upload)</dd>
<dt><code>~yu [filename]</code></dt>
<dd> Upload a file (YAPP upload)</dd>
<dt><code>~yd [filename]</code></dt>
<dd> Download a file (YAPP download)</dd>
<dt><code>~z</code></dt>
<dd> Suspend program</dd></dl>
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

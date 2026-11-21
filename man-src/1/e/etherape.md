---

title: "etherape(1)"
name: "etherape"
section: "1"
letter: "e"
url: "/docs/linux/man/1-etherape/"
description: "etherape – graphical network traffic browser"
---

<p> etherape &#8211; graphical network traffic browser</p>
<h2>SYNOPSIS</h2>
<p> <code>etherape</code> [ <code>-m</code> operating mode ] [ <code>-i</code> interface ] [ <code>-f</code> filter ] [ <code>-r</code> inputfile ] [ <code>-n</code> ] [ <code>-d</code> ] [ <code>-F</code> ] [ <code>-N</code> color ] [ <code>-L</code> color ] [ <code>-T</code> color ] <code>-z ]</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>etherape</code> is a network traffic browser. It displays network activity graphically. It uses GNOME libraries as its user interface, and libpcap, a packet capture and filtering library.</p>
<h2>OPTIONS</h2>
<p> These options can be supplied to the command:</p>
<dl>
<dt><code>-m, &#8211;mode </code>&lt;ethernet|fddi|ip|tcp&gt;</dt>
<dd> set mode of operation (default is lowest level for current device)</dd>
<dt><code>-i, &#8211;interface </code>&lt;interface name&gt;</dt>
<dd> set interface to listen to</dd>
<dt><code>-f, &#8211;filter </code>&lt;capture filter&gt;</dt>
<dd> set capture filter</dd>
<dt><code>-r, &#8211;infile </code>&lt;file name&gt;</dt>
<dd> set input file</dd>
<dt><code>-n, &#8211;numeric</code></dt>
<dd> don&#8217;t convert addresses to names</dd>
<dt><code>-d, &#8211;diagram-only</code></dt>
<dd> don&#8217;t display any node text identification</dd>
<dt><code>-F, &#8211;no-fade</code></dt>
<dd> do not fade old links</dd>
<dt><code>-N, &#8211;node-color </code>&lt;color&gt;</dt>
<dd> set the node color</dd>
<dt><code>-L, &#8211;link-color </code>&lt;color&gt;</dt>
<dd> set the link color</dd>
<dt><code>-T, &#8211;text-color </code>&lt;color&gt;</dt>
<dd> set the text color</dd>
<dt><code>-z, &#8211;zero-delay </code></dt>
<dd> ignores timestamps when replaying a capture file.</dd>
<dt><code>-?, &#8211;help</code></dt>
<dd> show a brief help message</dd></dl>
<h2>FILES</h2>
<p> Etherape will use <i>/etc/ethers</i> if there is one. If not, it will try to reverse lookup the ip address. </p>
<p> <code>IMPORTANT!</code> It is particularly important when running in ethernet mode to have the ethernet address of your router in /etc/ethers. If not, your router will have as name whatever IP address it was forwarding traffic from when it was first heard. </p>
<h2>SEE ALSO</h2>
<p> The etherape webpage is at <a rel="nofollow" href="http://etherape.sourceforge.net/">http://etherape.sourceforge.net/</a> </p>
<h2>AUTHOR</h2>
<p> Juan Toledo &lt;toledo [at] users.sourceforge.net&gt; </p>

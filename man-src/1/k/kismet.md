---
title: "kismet(1)"
name: "kismet"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kismet/"
description: "kismet – Wireless sniffing and monitoring"
---

<h2 class="name">NAME</h2>
<p> <code>kismet</code> &#8211; Wireless sniffing and monitoring </p>
<h2>SYNOPSIS</h2>
<p> <i>kismet</i> [server-options] [- ] [client-options] </p>
<p> <i>kismet_server</i> [-<code>nqs</code> ] [-<code>t </code><i>title</i> ] [-<code>f </code><i>config-file</i> ] [-<code>c </code><i>capture-source</i> ] [-<code>C </code><i>enable-capture-sources</i> ] [-<code>l </code><i>log-types</i> ] [-<code>d </code><i>dump-type</i> ] [-<code>m </code><i>max-packets-per-file</i> ] [-<code>g </code><i>gpshost:port</i> ] [-<code>p </code><i>listen-port</i> ] [-<code>a </code><i>allowed-hosts</i> ] [-<code>N </code><i>server-name</i> ] </p>
<p> <i>kismet_client</i> [-<code>qr</code> ] [-<code>f </code><i>config-file</i> ] [-<code>s </code><i>serverhost:port</i> ] [-<code>g </code><i>gui-type</i> ] [-<code>c </code><i>display-columns</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>Kismet</code> is an 802.11 layer2 wireless network detector, sniffer, and intrusion detection system. Kismet will work with any wireless card which supports raw monitoring (rfmon) mode, and can sniff 802.11b, 802.11a, and 802.11g traffic. </p>
<p> Kismet identifies networks by passively collecting packets and detecting standard named networks, detecting (and given time, decloaking) hidden networks, and inferring the presence of nonbeaconing networks via data traffic.<br />
 <code>kismet</code> supports logging to the wtapfile packet format (readable by tcpdump and ethereal) and saves detected network informat as plaintext, CSV, and XML. <code>kismet</code> is capable of using any GPS supported by <code>gpsd</code> and logs and plots network data. </p>
<p> <code>kismet</code> is divided into three basic programs, <code>kismet_server</code> <code>kismet_client</code> and <code>gpsmap</code></p>
<h2>USAGE</h2>
<p> <code>kismet</code> handles automatically starting kismet_server and kismet_client.<br />
 <code>kismet</code> is installed as suid-root by default. It will drop privs to the user specified in <code>kismet.conf</code> immediately after binding and configuring the capture source. </p>
<h2>KISMET_SERVER</h2>
<p> <code>kismet_server</code> captures, dissects, and logs packets and GPS data. It is capable of running in `headless&#8217; mode with no display. Multiple clients (on multiple computers) can be connected to a single server.</p>
<dl>
<dt><code>-I</code></p>
<dd> Set the initial channel for a channel source (source:channel)</p>
<dt><code>-x</code></p>
<dd> Forcibly enable the channel hopper</p>
<dt><code>-X</code></p>
<dd> Forcibly disable the channel hopper</p>
<dt><code>-t</code></p>
<dd> Set the title used for the %t field of the logfile template (Default: Kismet)</p>
<dt><code>-n</code></p>
<dd> Disable all logging</p>
<dt><code>-f</code></p>
<dd> Use an alternate config file</p>
<dt><code>-c</code></p>
<dd> Override capture source lines (type,interface,name). Refer to <a href="/docs/linux/man/5-kismet-conf/">kismet.conf</a>(5) for more information. Multiple capture source options can be specified for multiple sources. All sources provided here are automatically enabled unless an enable list is also supplied.</p>
<dt><code>-C</code></p>
<dd> Comma-separated list to override what capture sources are enabled.</p>
<dt><code>-l</code></p>
<dd> Override logging types, comma separated (dump, cisco, weak, csv, xml, gps)</p>
<dt><code>-m</code></p>
<dd> Override maximum packets logged per file</p>
<dt><code>-q</code></p>
<dd> Override sound option and run in quiet mode</p>
<dt><code>-g</code></p>
<dd> Override GPS host:port</p>
<dt><code>-p</code></p>
<dd> Override port to listen on for clients</p>
<dt><code>-a</code></p>
<dd> Override list of client IPs or network/mask blocks (comma separated) allowed to connect</p>
<dt><code>-s</code></p>
<dd> Run in silent mode (no console status information)</p>
<dt><code>-N</code></p>
<dd> Override server name for this instance of Kismet</p>
<dt><code>-v</code></p>
<dd> Print version</p>
<dt><code>-h</code></p>
<dd> Help</dl>
<h2>KISMET_CLIENT</h2>
<p> <code>kismet_client</code> is a ncurses and panels interface which connects to the server and displays detected networks, statistics, network details, etc.</p>
<dl>
<dt><code>-f</code></p>
<dd> Use an alternate config file</p>
<dt><code>-u</code></p>
<dd> Use an alternate UI config file</p>
<dt><code>-q</code></p>
<dd> Override sound option and run in quiet mode</p>
<dt><code>-s</code></p>
<dd> Override server host:port</p>
<dt><code>-r</code></p>
<dd> Attempt to automatically restablish the connection if the server terminates</p>
<dt><code>-g</code></p>
<dd> Override UI type (curses, panel)</p>
<dt><code>-c</code></p>
<dd> Override list of columns to display (comma seperated)</p>
<dt><code>-v</code></p>
<dd> Print version</p>
<dt><code>-h</code></p>
<dd> Help</dl>
<h2>GPSMAP</h2>
<p> <code>gpsmap</code> reads GPS and Network XML datafiles and plots networks on downloaded maps or user-supplied images (such as satellite photos).</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-kismet_drone/">kismet_drone</a>(1), <a href="/docs/linux/man/1-gpsmap/">gpsmap</a>(1), <a href="/docs/linux/man/5-kismet-conf/">kismet.conf</a>(5), <a href="/docs/linux/man/5-kismet_ui-conf/">kismet_ui.conf</a>(5), <a href="/docs/linux/man/5-kismet_drone-conf/">kismet_drone.conf</a>(5) </p>
<h2>Index</h2>

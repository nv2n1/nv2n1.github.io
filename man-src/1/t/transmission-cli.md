---

title: "transmission-cli(1)"
name: "transmission-cli"
section: "1"
letter: "t"
url: "/docs/linux/man/1-transmission-cli/"
description: "transmission-cli – a bittorrent client"
---

<p> <code>transmission-cli</code> &#8211; a bittorrent client</p>
<h2>SYNOPSIS</h2>
<p> <code>transmission-cli</code> -words &#8211;<code>h</code><br/>
<code>transmission-cli</code> [-<code>b | B</code> ] [-<code>d </code><i>number | &#8211;</i><code>D</code> ] [-<code>er | ep | et</code> ] [-<code>f </code><i>script</i> ] [-<code>g </code><i>directory</i> ] [-<code>h</code> ] [-<code>m | M</code> ] [-<code>p </code><i>port</i> ] [-<code>t </code><i>tos</i> ] [-<code>u </code><i>number | &#8211;</i><code>U</code> ] [-<code>v</code> ] [-<code>w </code><i>directory</i> ] <i>torrent-file</i></p>
<h2>DESCRIPTION</h2>
<p> The <code>transmission-cli</code> program is a lightweight, command-line BitTorrent client with scripting capabilities. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-b &#8211;blocklist</code></dt>
<dd> Enable peer blocklists. Transmission understands the bluetack blocklist file format. New blocklists can be added by copying them into the config-dir&#8217;s &quot;blocklists&quot; subdirectory.</dd>
<dt><code>-B &#8211;no-blocklist</code></dt>
<dd> Disble blocklists.</dd>
<dt><code>-d, -downlimit </code><i>number</i></dt>
<dd> Set the maximum download speed in KB/s</dd>
<dt><code>-D, -no-downlimit</code></dt>
<dd> Don&#8217;t limit the download speed</dd>
<dt><code>-er &#8211;encryption-required</code></dt>
<dd> Encrypt all peer connections.</dd>
<dt><code>-ep &#8211;encryption-preferred </code></dt>
<dd> Prefer encrypted peer connections.</dd>
<dt><code>-et &#8211;encryption-tolerated</code></dt>
<dd> Prefer unencrypted peer connections.</dd>
<dt><code>-f, -finish </code><i>script</i></dt>
<dd> Set a script to run when the torrent finishes</dd>
<dt><code>-g, &#8211;config-dir </code><i>directory</i></dt>
<dd> Where to look for configuration files. This can be used to swap between using the cli, daemon, gtk, and qt clients. See <a rel="nofollow" href="http://trac.transmissionbt.com/wiki/ConfigFiles">http://trac.transmissionbt.com/wiki/ConfigFiles</a> for more information.</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> Prints a short usage summary.</dd>
<dt><code>-m, &#8211;portmap</code></dt>
<dd> Enable portmapping via NAT-PMP or UPnP</dd>
<dt><code>-M, &#8211;no-portmap</code></dt>
<dd> Disable portmapping</dd>
<dt><code>-n, &#8211;new </code><i>sourcefile</i></dt>
<dd> Create torrent from the specified file or directory</dd>
<dt><code>-p, -port </code><i>port</i></dt>
<dd> Set the port to listen for incoming peers. (Default: 51413)</dd>
<dt><code>-t, -tos </code><i>tos</i></dt>
<dd> Set the peer socket TOS for local router-based traffic shaping. Valid values are </dd>
<p> &#8220;default&#8221; &#8220;lowcost&#8221; &#8220;throughput&#8221; &#8220;reliability&#8221; &#8220;lowdelay&#8221; </p>
<p> a decimal value 0-255 or a hexidecimal value 0x00-0xff)</p>
<dt><code>-u, -uplimit </code><i>number</i></dt>
<dd> Set the maximum upload speed in KB/s</dd>
<dt><code>-U, -no-uplimit</code></dt>
<dd> Don&#8217;t limit the upload speed</dd>
<dt><code>-v, &#8211;verify</code></dt>
<dd> Verify the torrent&#8217;s downloaded data.</dd>
<dt><code>-w, &#8211;download-dir </code><i>directory</i></dt>
<dd> Where to save downloaded data.</dd></dl>
<h2>SIGNALS</h2>
<p> In addition to these options, sending <code>transmission-cli</code> a SIGHUP signal will contact the tracker for more peers.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>TRANSMISSION_HOME</code></dt>
<dd> Sets the default config-dir.</dd>
<dt><code>http_proxy</code></dt>
<dd> libcurl uses this environment variable when performing tracker announces.</dd></dl>
<h2>FILES</h2>
<dl>
<dt><code>~/.config/transmission</code></dt>
<dd> Directory where <code>transmission-cli</code> keeps torrent information for future seeding and resume operations.</dd></dl>
<h2>AUTHORS</h2>
<p> The <code>transmission-cli</code> program was written by An -nosplit An Eric Petit , An Josh Elsasser , An Jordan Lee , and An Mitchell Livingston .</p>
<h2>SEE ALSO</h2>
<p> transmission-create1, transmission-daemon1, transmission-edit1, transmission-gtk1, transmission-qt1, transmission-remote1, transmission-show1 </p>
<p> <a rel="nofollow" href="http://www.transmissionbt.com/">http://www.transmissionbt.com/</a> </p>

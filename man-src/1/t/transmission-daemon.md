---
title: "transmission-daemon(1)"
name: "transmission-daemon"
section: "1"
letter: "t"
url: "/docs/linux/man/1-transmission-daemon/"
description: "transmission-daemon – a bittorrent client"
---

<h2>NAME</h2>
<p> <code>transmission-daemon</code> &#8211; a bittorrent client</p>
<h2>SYNOPSIS</h2>
<p> -words <code>transmission-daemon</code> &#8211;<code>h</code><br />
<code>transmission-daemon</code> [-<code>a </code><i>x.x.x.x,&#8230;</i> ] [-<code>b | B</code> ] [-<code>c </code><i>directory</i> ] [-<code>C</code> ] [-<code>d</code> ] [-<code>f</code> ] [-<code>g </code><i>directory</i> ] [-<code>h</code> ] [-<code>p </code><i>port</i> ] [-<code>t | T</code> ] [-<code>u </code><i>username</i> ] [-<code>v </code><i>password</i> ] [-<code>P </code><i>port</i> ] [-<code>m | M</code> ] [-<code>l </code><i>limit</i> ] [-<code>L </code><i>limit</i> ] [-<code>er | ep | et</code> ] [-<code>utp | no-utp</code> ] [-<code>V</code> ] [-<code>w </code><i>download-dir</i> ] [-<code>e </code><i>logfile</i> ] [-<code>log-error | log-info | log-debug</code> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>transmission-daemon</code> is a daemon-based Transmission session that can be controlled via RPC commands from transmission&#8217;s web interface or transmission-remote1.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a &#8211;allowed </code><i>x.x.x.x,&#8230;</i></p>
<dd> Allow RPC access to a comma-delimited whitelist of IP addresses. Wildcards can be specified in an address by using &#8216;*&#8217;. Default: &quot;127.0.0.1&quot; Example: &quot;127.0.0.*,192.168.1.*&quot;</p>
<dt><code>-b &#8211;blocklist</code></p>
<dd> Enable peer blocklists. Transmission understands the bluetack blocklist file format. New blocklists can be added by copying them into the config-dir&#8217;s &quot;blocklists&quot; subdirectory.</p>
<dt><code>-c </code><i>directory</i></p>
<dd> Directory to watch for new .torrent files to be added. As they are added to this directory, the daemon will load them into Transmission.</p>
<dt><code>-C</code></p>
<dd> Do not watch for new .torrent files.</p>
<dt><code>-B &#8211;no-blocklist</code></p>
<dd> Disble blocklists.</p>
<dt><code>-d</code></p>
<dd> Dump transmission-daemon&#8217;s settings to stderr.</p>
<dt><code>-f &#8211;foreground</code></p>
<dd> Run in the foreground and print errors to stderr.</p>
<dt><code>-g &#8211;config-dir </code><i>directory</i></p>
<dd> Where to look for configuration files. This can be used to swap between using the cli, daemon, gtk, and qt clients. See <a rel="nofollow" href="http://trac.transmissionbt.com/wiki/ConfigFiles">http://trac.transmissionbt.com/wiki/ConfigFiles</a> for more information.</p>
<dt><code>-er &#8211;encryption-required</code></p>
<dd> Encrypt all peer connections.</p>
<dt><code>-ep &#8211;encryption-preferred</code></p>
<dd> Prefer encrypted peer connections.</p>
<dt><code>-et &#8211;encryption-tolerated</code></p>
<dd> Prefer unencrypted peer connections.</p>
<dt><code>-gsr &#8211;global-seedratio </code><i>ratio</i></p>
<dd> All torrents, unless overridden by a per-torrent setting, should seed until a specific <i>ratio</i></p>
<dt><code>-GSR &#8211;no-global-seedratio</code></p>
<dd> All torrents, unless overridden by a per-torrent setting, should seed regardless of ratio</p>
<dt><code>-h &#8211;help</code></p>
<dd> Print command-line option descriptions.</p>
<dt><code>&#8211;incomplete-dir </code><i>dir</i></p>
<dd> When adding new torrents, store their contents in <i>directory</i> until the torrent is done.</p>
<dt><code>&#8211;no-incomplete-dir</code></p>
<dd> Don&#8217;t store incomplete torrents in a different directory.</p>
<dt><code>-i &#8211;bind-address-ipv4</code></p>
<dd> Listen for IPv4 BitTorrent connections on a specific address. Only one IPv4 listening address is allowed. Default: 0.0.0.0 (All addresses)</p>
<dt><code>-I &#8211;bind-address-ipv6</code></p>
<dd> Listen for IPv6 BitTorrent connections on a specific address. Only one IPv6 listening address is allowed. Default: :: (All addresses)</p>
<dt><code>-r &#8211;rpc-bind-address</code></p>
<dd> Listen for RPC connections on a specific address. This must be an IPv4 address. Only one RPC listening address is allowed. Default: 0.0.0.0 (All addresses)</p>
<dt><code>&#8211;paused</code></p>
<dd> Pause all torrents on startup</p>
<dt><code>-L &#8211;peerlimit-global </code><i>limit</i></p>
<dd> Overall peer limit. Useful on embedded systems where the default might be unsuitable. Default: 240</p>
<dt><code>-l &#8211;peerlimit-torrent </code><i>limit</i></p>
<dd> Peer limit per torrent. Useful on embedded systems where the default might be unsuitable. Default: 60</p>
<dt><code>-m &#8211;portmap</code></p>
<dd> Enable portmapping via NAT-PMP or UPnP</p>
<dt><code>-M &#8211;no-portmap</code></p>
<dd> Disable portmapping</p>
<dt><code>-o &#8211;dht</code></p>
<dd> Enable distributed hash table (DHT).</p>
<dt><code>-O &#8211;no-dht</code></p>
<dd> Disable distribued hash table (DHT).</p>
<dt><code>-p &#8211;port </code><i>port</i></p>
<dd> Port to open and listen for RPC requests on. Default: 9091</p>
<dt><code>-P, -peerport </code><i>port</i></p>
<dd> Port to listen for incoming peers on. Default: 51413</p>
<dt><code>-t &#8211;auth</code></p>
<dd> Require clients to authenticate themselves. This doesn&#8217;t do much good unless <i>username</i> and <i>password</i> are also set.</p>
<dt><code>-T &#8211;no-auth</code></p>
<dd> Don&#8217;t require authentication from clients.</p>
<dt><code>-u &#8211;username </code><i>username</i></p>
<dd> Used for client authentication.</p>
<dt><code>-v &#8211;password </code><i>password</i></p>
<dd> Used for client authentication.</p>
<dt><code>-V &#8211;version</code></p>
<dd> Show version number and exit</p>
<dt><code>&#8211;utp</code></p>
<dd> Enable uTP for peer connections.</p>
<dt><code>&#8211;no-utp</code></p>
<dd> Disable uTP for peer connections.</p>
<dt><code>-w &#8211;download-dir</code></p>
<dd> Where to store downloaded data.</p>
<dt><code>-e &#8211;logfile</code></p>
<dd> Where to store transmission&#8217;s log messages.</p>
<dt><code>&#8211;log-error</code></p>
<dd> Show error messages</p>
<dt><code>&#8211;log-info</code></p>
<dd> Show error and info messages</p>
<dt><code>&#8211;log-debug</code></p>
<dd> Show error, info, and debug messages</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>http_proxy</code></p>
<dd> libcurl uses this environment variable when performing tracker announces.</p>
<dt><code>TRANSMISSION_HOME</code></p>
<dd> Sets the default config-dir.</dl>
<h2>FILES</h2>
<dl>
<dt><code>~/.config/transmission-daemon</code></p>
<dd> The config-dir used when neither [<code>TRANSMISSION_HOME</code> ] nor [-<code>g</code> ] is specified. See <a rel="nofollow" href="http://trac.transmissionbt.com/wiki/ConfigFiles">http://trac.transmissionbt.com/wiki/ConfigFiles</a> for more information.</dl>
<h2>AUTHORS</h2>
<p> An -nosplit An Jordan Lee , An Josh Elsasser , An Eric Petit , and An Mitchell Livingston .</p>
<h2>SEE ALSO</h2>
<p> transmission-create1, transmission-daemon1, transmission-edit1, transmission-gtk1, transmission-qt1, transmission-remote1, transmission-show1 </p>
<p> <a rel="nofollow" href="http://www.transmissionbt.com/">http://www.transmissionbt.com/</a> </p>
<h2>Index</h2>

---

title: "transmission-qt(1)"
name: "transmission-qt"
section: "1"
letter: "t"
url: "/docs/linux/man/1-transmission-qt/"
description: "transmission-qt – a bittorrent client"
---

<p> <code>transmission-qt</code> &#8211; a bittorrent client</p>
<h2>SYNOPSIS</h2>
<p> <code>transmission-qt</code> &#8211;<code>h</code><br/>
<code>transmission-qt</code> [<br/>
<code>options</code> ] [<i>torrent-file &#8230;</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>transmission-qt</code> is a fast and easy BitTorrent client. </p>
<p> BitTorrent is a peer-to-peer file transfer protocol which uses a metainfo file (usually with the .torrent file extension) and a central tracker to distribute file data amongst a group of peers. For more information on the BitTorrent protocol see <a rel="nofollow" href="http://www.bittorrent.org/">http://www.bittorrent.org/</a></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h &#8211;help</code></dt>
<dd> Show help options</dd>
<dt><code>-g, &#8211;config-dir </code><i>directory</i></dt>
<dd> Where to look for configuration files. This can be used to swap between using the cli, daemon, gtk, and qt clients. See <a rel="nofollow" href="http://trac.transmissionbt.com/wiki/ConfigFiles">http://trac.transmissionbt.com/wiki/ConfigFiles</a> for more information.</dd>
<dt><code>-m &#8211;minimized</code></dt>
<dd> Start minimized in notification area</dd>
<dt><code>-p, &#8211;port </code><i>port</i></dt>
<dd> Port to use when connecting to an existing session</dd>
<dt><code>-r, &#8211;remote </code><i>host</i></dt>
<dd> Connect to an existing session at the specified hostname</dd>
<dt><code>-u, &#8211;username </code><i>username</i></dt>
<dd> Username to use when connecting to an existing session</dd>
<dt><code>-v, &#8211;version</code></dt>
<dd> Show version number and exit</dd>
<dt><code>-w, &#8211;password </code><i>password</i></dt>
<dd> Password to use when connecting to an existing session</dd></dl>
<p> Multiple .torrent files may be added at startup by appending them on the command line. If <code>transmission-qt</code> is already running, the torrents will be added to the running instance.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>TRANSMISSION_HOME</code></dt>
<dd> Sets the default config-dir.</dd></dl>
<h2>FILES</h2>
<dl>
<dt><code>~/.config/transmission</code></dt>
<dd> The config-dir used when neither [<code>TRANSMISSION_HOME</code> ] nor [-<code>g</code> ] is specified.</dd></dl>
<h2>AUTHORS</h2>
<p> An -nosplit <code>transmission-qt</code> was written by An Jordan Lee , An Josh Elsasser , An Eric Petit , and An Mitchell Livingston .</p>
<h2>SEE ALSO</h2>
<p> transmission-create1, transmission-daemon1, transmission-edit1, transmission-gtk1, transmission-qt1, transmission-remote1, transmission-show1 </p>
<p> <a rel="nofollow" href="http://www.transmissionbt.com/">http://www.transmissionbt.com/</a> </p>

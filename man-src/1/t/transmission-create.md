---
title: "transmission-create(1)"
name: "transmission-create"
section: "1"
letter: "t"
url: "/docs/linux/man/1-transmission-create/"
description: "transmission-create – command-line utility to create .torrent files"
---

<h2>NAME</h2>
<p> <code>transmission-create</code> &#8211; command-line utility to create .torrent files</p>
<h2>SYNOPSIS</h2>
<p> -words [-<code>h </code> ] [-<code>p </code> ] [-<code>o </code><i>file</i> ] [-<code>c </code><i>comment</i> ] [-<code>t </code><i>tracker</i> ] [-<code>s </code><i>piece-size-KiB</i> ] [<i>source file or directory</i> ]</p>
<h2>DESCRIPTION</h2>
<p> creates BitTorrent .torrent files from the command line</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h &#8211;help</code></dt>
<dd> Show a short help page and exit.</dd>
<dt><code>-o &#8211;outfile</code></dt>
<dd> Save the generated .torrent to this filename.</dd>
<dt><code>-p &#8211;private</code></dt>
<dd> Flag the torrent as intended for use on private trackers.</dd>
<dt><code>-c &#8211;comment</code></dt>
<dd> Add a comment to the torrent file.</dd>
<dt><code>-s &#8211;piecesize</code></dt>
<dd> Set how many KiB each piece should be, overriding the preferred default</dd>
<dt><code>-t &#8211;tracker</code></dt>
<dd> Add a tracker&#8217;s <i>announce URL</i> to the .torrent. Most torrents will have at least one <i>announce URL.</i> To add more than one, use this option multiple times.</dd></dl>
<h2>AUTHORS</h2>
<p> An -nosplit An Jordan Lee</p>
<h2>SEE ALSO</h2>
<p> transmission-create1, transmission-daemon1, transmission-edit1, transmission-gtk1, transmission-qt1, transmission-remote1, transmission-show1 </p>
<p> <a rel="nofollow" href="http://www.transmissionbt.com/">http://www.transmissionbt.com/</a> </p>

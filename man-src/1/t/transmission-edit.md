---
title: "transmission-edit(1)"
name: "transmission-edit"
section: "1"
letter: "t"
url: "/docs/linux/man/1-transmission-edit/"
description: "transmission-edit – command-line utility to modify .torrent files’ announce URLs"
---

<h2>NAME</h2>
<p> <code>transmission-edit</code> &#8211; command-line utility to modify .torrent files&#8217; announce URLs</p>
<h2>SYNOPSIS</h2>
<p> -words [-<code>h </code> ] [-<code>a </code><i>url</i> ] [-<code>d </code><i>url</i> ] [-<code>r </code><i>search replace</i> ] <i>torrentfile(s)</i></p>
<h2>DESCRIPTION</h2>
<p> command-line utility to modify .torrent files&#8217; announce URLs</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h &#8211;help</code></dt>
<dd> Show a short help page and exit.</dd>
<dt><code>-a &#8211;add </code><i>URL</i></dt>
<dd> Add an announce URL to the torrent&#8217;s announce-list if it&#8217;s not already in the list</dd>
<dt><code>-d &#8211;delete </code><i>URL</i></dt>
<dd> Remove an announce URL from the torrent&#8217;s announce-list</dd>
<dt><code>-r &#8211;replace </code><i>search replace</i></dt>
<dd> Substring search-and-replace inside a torrent&#8217;s announce URLs. This can be used to change an announce URL when the tracker moves or your passcode changes.</dd></dl>
<h2>EXAMPLES</h2>
<p> Update a tracker passcode in all your torrents: </p>
<blockquote>
<pre>
$ transmission-edit -r old-passcode new-passcode ~/.config/transmission/torrents/*\.torrent
</pre>
</blockquote>
<h2>AUTHORS</h2>
<p> An -nosplit An Jordan Lee</p>
<h2>SEE ALSO</h2>
<p> transmission-create1, transmission-daemon1, transmission-edit1, transmission-gtk1, transmission-qt1, transmission-remote1, transmission-show1 </p>
<p> <a rel="nofollow" href="http://www.transmissionbt.com/">http://www.transmissionbt.com/</a> </p>
<h2>Index</h2>

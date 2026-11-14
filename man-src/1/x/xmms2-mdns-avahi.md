---
title: "xmms2-mdns-avahi(1)"
name: "xmms2-mdns-avahi"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xmms2-mdns-avahi/"
description: "xmms2-mdns-avahi – announces XMMS2 via mDNS"
---

<h2>NAME</h2>
<p> xmms2-mdns-avahi &#8211; announces XMMS2 via mDNS</p>
<h2>SYNOPSIS</h2>
<p> <i>xmms2-mdns-avahi</i></p>
<h2>DESCRIPTION</h2>
<p> <code>XMMS2 </code> is a redesign of the XMMS (<a rel="nofollow" href="http://www.xmms.org)">http://www.xmms.org)</a> music player. It features a client-server model, allowing multiple (even simultaneous!) user interfaces, both textual and graphical. All common audio formats are supported using plugins. On top of this, there is a flexible media library to organize your music. </p>
<p> <i>xmms2-mdns-avahi</i> is the Avahi mDNS announcing client for <code>XMMS2.</code> <i>xmms2-mdns-avahi</i> is designed to announce the presence of an accessible <code>XMMS2</code> TCP socket if one is available. <i>xmms2-mdns-avahi</i> offers a _xmms2._tcp service if, and only if, the <i>XMMS_PATH_FULL</i> enviornmental variable contains a TCP socket. This allows clients that support mDNS discovery to easily locate and connect to this <i><a href="/docs/linux/man/1-xmms2d/">xmms2d</a>(1) </i> instance.</p>
<h2>ENVIRONMENTAL VARIABLES</h2>
<dl>
<dt><i>XMMS_PATH_FULL</i></p>
<dd> A complete list of URL paths seperated by &#8216;;&#8217; pointed to the <i><a href="/docs/linux/man/1-xmms2d/">xmms2d</a>(1).</i> See <code>IPC SOCKET</code> in <i><a href="/docs/linux/man/1-xmms2d/">xmms2d</a>(1)</i> for details of possible values for this variable </p>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-xmms2/">xmms2</a>(1), <a href="/docs/linux/man/1-xmms2d/">xmms2d</a>(1), <a rel="nofollow" href="http://xmms2.xmms.org">http://xmms2.xmms.org</a></p>
<h2>HISTORY</h2>
<p> The <code>XMMS2</code> Project was started by Tobias Rundström and Anders Gustafsson. It is developed with their lead by a small group of contributers from all over the world.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Alexander Botero-Lowry &lt;alex [at] foxybanana.com&gt; </p>
<h2>Index</h2>

---
title: "gajim(1)"
name: "gajim"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gajim/"
description: "gajim – a Jabber/XMPP client"
---

<h2 class="name">NAME</h2>
<p> <code>gajim</code> &#8211; a Jabber/XMPP client </p>
<h2>SYNOPSIS</h2>
<p> &#8211;<code>h</code><br />
 [-<code>q</code> ] [-<code>v</code> ] [-<code>l </code><i>subsystem=level</i> ] [-<code>p </code><i>name</i> ] [-<code>c </code><i>directory</i> ]</p>
<h2>DESCRIPTION</h2>
<p> is a Jabber/XMPP client written in Python and GTK+. works nicely with GNOME, yet it does not require it to run. is designed for novice and advanced users as one, as well for XMPP server admins. </p>
<p> XMPP is the Extensible Messaging and Presence Protocol, a set of open technologies for instant messaging, presence, multi-party chat, voice and video calls, collaboration, lightweight middleware, content syndication, and generalized routing of XML data. For more information on the XMPP protocol see &lt;<a rel="nofollow" href="https://xmpp.org/about-xmpp/">https://xmpp.org/about-xmpp/</a>&gt;.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h &#8211;help</code></p>
<dd> Show help options</p>
<dt><code>-q &#8211;quiet</code></p>
<dd> Show only critical errors</p>
<dt><code>-v &#8211;verbose</code></p>
<dd> Print xml stanzas and other debug information</p>
<dt><code>-l &#8211;loglevel </code><i>subsystem=level Bq </i>, <i>subsystem=level Bq </i><i>&#8230;</i></p>
<dd> Configure logging system. Subsystem can be <i>gajim.interface</i> <i>gajim.c.connection</i> <i>.nbxmpp.client_nb</i> etc. Level can be <i>DEBUG</i> <i>INFO</i> <i>WARNING</i> <i>ERROR</i> or <i>CRITICAL</i></p>
<dt><code>-p &#8211;profile </code><i>name</i></p>
<dd> Run using config.name in configuration directory</p>
<dt><code>-c &#8211;config-path </code><i>directory</i></p>
<dd> Where to look for configuration files</dl>
<h2>FILES</h2>
<dl>
<dt><code>$XDG_CACHE_DIR/gajim/cache.db</code></p>
<dd> Cache database file of transports, caps, roster entry, and roster group.</p>
<dt><code>$XDG_CACHE_DIR/gajim/avatars/</code></p>
<dd> Cache directory of avatars.</p>
<dt><code>$XDG_CACHE_DIR/gajim/vcards/</code></p>
<dd> Cache directory of vCards (virtual cards).</p>
<dt><code>$XDG_CONFIG_DIR/gajim/</code></p>
<dd> The config-path used when [-<code>c</code> ] is not specified.</p>
<dt><code>$XDG_DATA_DIR/gajim/certs/</code></p>
<dd> Directory where certificates are stored.</p>
<dt><code>$XDG_DATA_DIR/gajim/logs.db</code></p>
<dd> The history database log file. For more information on database logs see &lt;<a rel="nofollow" href="https://trac.gajim.org/wiki/LogsDatabase">https://trac.gajim.org/wiki/LogsDatabase</a>&gt;.</dl>
<h2>AUTHORS</h2>
<p> An -nosplit is written and maintained by An Yann Leboulanger , and An Denis Fomin , with contributions and patches merged from many individuals around the world. See files AUTHORS and THANKS for a complete list.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2003-2015 Gajim Team </p>
<p> is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; version 3 only. </p>
<p> is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with <code>.</code> If not, see &lt;<a rel="nofollow" href="https://www.gnu.org/licenses/">https://www.gnu.org/licenses/</a>&gt;.</p>
<h2>FEEDBACK</h2>
<p> You can report bugs or feature requests in our bug tracker at <i>trac.gajim.org</i> or in the <i>gajim-devel</i> mailing list; if you want to send us a patch, please do so in our bug tracker. You can also find us in our chat room.</p>
<h2>WWW</h2>
<p> <a rel="nofollow" href="https://www.gajim.org/">https://www.gajim.org/</a></p>
<h2>XMPP</h2>
<p> You are welcome to join us at gajim [at] conference.gajim.org</p>
<h2>MAILING LIST</h2>
<p> Below are public mailing lists on lists.gajim.org </p>
<blockquote>
<pre>
<a rel="nofollow" href="https://lists.gajim.org/cgi-bin/listinfo/gajim-devel">https://lists.gajim.org/cgi-bin/listinfo/gajim-devel</a>
<a rel="nofollow" href="https://lists.gajim.org/cgi-bin/listinfo/translators">https://lists.gajim.org/cgi-bin/listinfo/translators</a>
</pre>
</blockquote>
<p> More mailing lists at </p>
<blockquote>
<pre>
<a rel="nofollow" href="https://lists.gajim.org/cgi-bin/listinfo">https://lists.gajim.org/cgi-bin/listinfo</a>
</pre>
</blockquote>
<h2>BUGS</h2>
<p> Please submit bugs at </p>
<blockquote>
<pre>
<a rel="nofollow" href="https://trac.gajim.org/">https://trac.gajim.org/</a>
<a rel="nofollow" href="https://trac-plugins.gajim.org/">https://trac-plugins.gajim.org/</a>
<a rel="nofollow" href="https://python-nbxmpp.gajim.org/">https://python-nbxmpp.gajim.org/</a>
</pre>
</blockquote>
<h2>SEE ALSO</h2>
<p> gajim-remote1 gajim-history-manager1 </p>
<h2>Index</h2>

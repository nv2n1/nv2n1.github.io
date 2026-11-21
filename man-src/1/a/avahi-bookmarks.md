---

title: "avahi-bookmarks(1)"
name: "avahi-bookmarks"
section: "1"
letter: "a"
url: "/docs/linux/man/1-avahi-bookmarks/"
description: "avahi-bookmarks – Web service showing mDNS/DNS-SD announced HTTP services using the Avahi daemon"
---

<h2>NAME</h2>
<p> avahi-bookmarks &#8211; Web service showing mDNS/DNS-SD announced HTTP services using the Avahi daemon</p>
<p> <code>avahi-bookmarks </code></p>
<p> A web service for listing HTTP services that are announced via mDNS/DNS-SD using the Avahi daemon. avahi-bookmarks opens a TCP socket on port 8080 and waits for incoming HTTP connections returning a dynamic web site containing links to all services of type _http._tcp on the LAN. Point your browser to <a rel="nofollow" href="http://localhost:8080/">http://localhost:8080/</a> to make use of avahi-bookmarks.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-p | &#8211;port=</code> <i>PORT</i></dt>
<dd> Specify a TCP port number to listen on. If omitted defaults to 8080.</dd>
<dt><code>-a | &#8211;address=</code> <i>address</i></dt>
<dd> Specify an IP address to listen on. If omitted defaults to 127.0.0.1. Specify 0.0.0.0 if you want to allow remote access.</dd>
<dt><code>-H | &#8211;host-names</code></dt>
<dd> Create links pointing to mDNS host names instead of resolved IP addreses. This is only compatible with your browser if you run some kind of local NSS module to resolve mDNS host names (e.g. nss-mdns). If both -A and -H are ommited avahi-bookmarks detects whether NSS support is available locally. This option conflicts with -A.</dd>
<dt><code>-A | &#8211;addresses</code></dt>
<dd> Create links pointing to numeric IP addresses instead of mDNS host names. This will break access to hosts running virtual servers. If both -A and -H are ommited avahi-bookmarks detects whether NSS support is available locally. This option conflicts with -H.</dd>
<dt><code>-d | &#8211;domain</code>=<i>DOMAIN</i></dt>
<dd> The domain to browse for services in.</dd>
<dt><code>-h | &#8211;help</code></dt>
<dd> Show help</dd></dl>
<h2>AUTHORS</h2>
<p> The Avahi Developers &lt;avahi (at) lists (dot) freedesktop (dot) org&gt;; Avahi is available from <code><a rel="nofollow" href="http://avahi.org/">http://avahi.org/</a></code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-avahi-browse/">avahi-browse</a>(1)</code>, <code><a href="/docs/linux/man/8-avahi-daemon/">avahi-daemon</a>(8)</code></p>
<h2>COMMENTS</h2>
<p> This man page was written using <code>xml2man(1)</code> by Oliver Kurth. </p>

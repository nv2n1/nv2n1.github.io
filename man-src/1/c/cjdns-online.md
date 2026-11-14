---
title: "cjdns-online(1)"
name: "cjdns-online"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cjdns-online/"
description: "cjdns-online — check whether cjdns tunnel devices are available"
---

<h2>NAME</h2>
<p> <code>cjdns-online</code> &#8212; check whether cjdns tunnel devices are available</p>
<h2>SYNOPSIS</h2>
<p> <code>cjdns-online</code> [&lt;options&gt;&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> Cjdns-online waits for cjdns to make its tunnel device available so that services that listen on the cjdns IP can start. If you have configured services to listen on the cjdns IP, then you can use:</p>
<dl>
<dt>
<dd>
<pre>
systemctl enable cjdns-wait-online
</pre>
<dt>
<dd></dl>
<p> to wait until this IP is available before starting network services. This will increase your boot time somewhat, but is needed to launch thttpd at boot, for example.</p>
<h2>OPTIONS</h2>
<dl>
<dt>&bull;</p>
<dd> <code>-t</code>, <code>&#8211;timeout</code> &lt;timeout_value&gt;:<tt>&nbsp;<wbr></tt><br />
 time to wait in seconds, default 30</p>
<dt>&bull;</p>
<dd> <code>-x</code>, <code>&#8211;exit</code>:<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><br />
 Exit immediately if cjdns is not online</p>
<dt>&bull;</p>
<dd> <code>-q</code>, <code>&#8211;quiet</code>: Don&#8217;t print anything</p>
<dt>&bull;</p>
<dd> <code>-s</code>, <code>&#8211;wait-for-startup</code>: Wait for full startup instead of just tun dev. This is not implemented.</p>
<dt>
<dd></dl>
<h2 class="name">NAME</h2>
<p> <code>cjdns-online</code> &#8212; check whether cjdns tunnel devices are available </p>
<h2>SYNOPSIS</h2>
<p> <code>cjdns-online</code> [&lt;options&gt;&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> Cjdns-online waits for cjdns to make its tunnel device available so that services that listen on the cjdns IP can start. If you have configured services to listen on the cjdns IP, then you can use:</p>
<dl>
<dt>
<dd>
<pre>
systemctl enable cjdns-wait-online
</pre>
<dt>
<dd></dl>
<p> to wait until this IP is available before starting network services. This will increase your boot time somewhat, but is needed to launch thttpd at boot, for example.</p>
<h2>OPTIONS</h2>
<dl>
<dt>&bull;</p>
<dd> <code>-t</code>, <code>&#8211;timeout</code> &lt;timeout_value&gt;:<tt>&nbsp;<wbr></tt><br />
 time to wait in seconds, default 30</p>
<dt>&bull;</p>
<dd> <code>-x</code>, <code>&#8211;exit</code>:<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><br />
 Exit immediately if cjdns is not online</p>
<dt>&bull;</p>
<dd> <code>-q</code>, <code>&#8211;quiet</code>: Don&#8217;t print anything</p>
<dt>&bull;</p>
<dd> <code>-s</code>, <code>&#8211;wait-for-startup</code>: Wait for full startup instead of just tun dev. This is not implemented.</p>
<dt>
<dd>
</dl>
<h2>Index</h2>

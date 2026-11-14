---
title: "cjdroute(1)"
name: "cjdroute"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cjdroute/"
description: "cjdroute — Cjdns packet switch"
---

<h2>NAME</h2>
<p> <code>cjdroute</code> &#8212; Cjdns packet switch</p>
<h2>SYNOPSIS</h2>
<p> <code>/usr/sbin/cjdroute</code> [&lt;options&gt;&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> Cjdns implements an encrypted IPv6 network using public-key cryptography for address allocation and a distributed hash table for routing. This provides near-zero-configuration networking, and prevents many of the security and scalability issues that plague existing networks. </p>
<p> cjdroute runs in the background and either decrypts packets addressed to this node, or sends them on to the next node in the route.</p>
<h2>OPTIONS</h2>
<dl>
<dt>&bull;</p>
<dd> <code>&#8211;help</code>: Print usage summary.</p>
<dt>&bull;</p>
<dd> <code>&#8211;genconf</code> [&#8211;no-eth]: Generate a configuration file, write it to stdout. If &#8211;no-eth is specified then ethernet beaconing will be disabled.</p>
<dt>&bull;</p>
<dd> <code>&#8211;bench</code>: Run some cryptography performance benchmarks.</p>
<dt>&bull;</p>
<dd> <code>&#8211;version</code>:<br />
 Print cjdroute version and the protocol version which this node speaks.</p>
<dt>&bull;</p>
<dd> <code>&#8211;cleanconf</code> &lt; conf: Print a clean (valid json) version of the config.</p>
<dt>&bull;</p>
<dd> <code>&#8211;nobg</code><br />
 Never fork to the background no matter the config.</p>
<dt>
<dd></dl>
<h2>USAGE</h2>
<p> To get the router up and running:</p>
<dl>
<dt>&bull;</p>
<dd> Step 1: Generate a new configuration file if one doesn&#8217;t already exist.</p>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>cjdroute &#8211;genconf&nbsp;<wbr>&gt;&nbsp;<wbr>/etc/cjdroute.conf</p>
<dt>
<dd> You can also simply:</p>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>systemctl start cjdns</p>
<dt>
<dd> which will tell cjdroute to generate a new config if needed.</p>
<dt>&bull;</p>
<dd> Step 2: Find somebody to connect to. Check out the IRC channel or <a rel="nofollow" href="http://hyperboria.net/">http://hyperboria.net/</a> for information about how to meet new people and make connect to them. Read more here: <a rel="nofollow" href="https://github.com/cjdelisle/cjdns/#2-find-a-friend">https://github.com/cjdelisle/cjdns/#2-find-a-friend</a></p>
<dt>
<dd> By default, cjdroute will find any cjdns nodes on your local LAN without any configuration.</p>
<dt>&bull;</p>
<dd> Step 3: Add that somebody&#8217;s node to your cjdroute.conf file. <a rel="nofollow" href="https://github.com/cjdelisle/cjdns/#3-connect-your-node-to-your-friends-node">https://github.com/cjdelisle/cjdns/#3-connect-your-node-to-your-friends-node</a></p>
<dt>&bull;</p>
<dd> Step 4: Fire it up!</p>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>systemctl start cjdns</p>
<dt>
<dd> Or if you had already started cjdns:</p>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>systemctl restart cjdns</p>
<dt>
<dd></dl>
<p> For more information about other functions and non-standard setups, see README.md <a href="/docs/linux/man/1-cjdroute/">cjdroute</a>(1) &#8212; Cjdns packet switch =============================================</p>
<h2>SYNOPSIS</h2>
<p> <code>/usr/sbin/cjdroute</code> [&lt;options&gt;&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> Cjdns implements an encrypted IPv6 network using public-key cryptography for address allocation and a distributed hash table for routing. This provides near-zero-configuration networking, and prevents many of the security and scalability issues that plague existing networks. </p>
<p> cjdroute runs in the background and either decrypts packets addressed to this node, or sends them on to the next node in the route.</p>
<h2>OPTIONS</h2>
<dl>
<dt>&bull;</p>
<dd> <code>&#8211;help</code>: Print usage summary.</p>
<dt>&bull;</p>
<dd> <code>&#8211;genconf</code> [&#8211;no-eth]: Generate a configuration file, write it to stdout. If &#8211;no-eth is specified then ethernet beaconing will be disabled.</p>
<dt>&bull;</p>
<dd> <code>&#8211;bench</code>: Run some cryptography performance benchmarks.</p>
<dt>&bull;</p>
<dd> <code>&#8211;version</code>:<br />
 Print cjdroute version and the protocol version which this node speaks.</p>
<dt>&bull;</p>
<dd> <code>&#8211;cleanconf</code> &lt; conf: Print a clean (valid json) version of the config.</p>
<dt>&bull;</p>
<dd> <code>&#8211;nobg</code><br />
 Never fork to the background no matter the config.</p>
<dt>
<dd></dl>
<h2>USAGE</h2>
<p> To get the router up and running:</p>
<dl>
<dt>&bull;</p>
<dd> Step 1: Generate a new configuration file if one doesn&#8217;t already exist.</p>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>cjdroute &#8211;genconf&nbsp;<wbr>&gt;&nbsp;<wbr>/etc/cjdroute.conf</p>
<dt>
<dd> You can also simply:</p>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>systemctl start cjdns</p>
<dt>
<dd> which will tell cjdroute to generate a new config if needed.</p>
<dt>&bull;</p>
<dd> Step 2: Find somebody to connect to. Check out the IRC channel or <a rel="nofollow" href="http://hyperboria.net/">http://hyperboria.net/</a> for information about how to meet new people and make connect to them. Read more here: <a rel="nofollow" href="https://github.com/cjdelisle/cjdns/#2-find-a-friend">https://github.com/cjdelisle/cjdns/#2-find-a-friend</a></p>
<dt>
<dd> By default, cjdroute will find any cjdns nodes on your local LAN without any configuration.</p>
<dt>&bull;</p>
<dd> Step 3: Add that somebody&#8217;s node to your cjdroute.conf file. <a rel="nofollow" href="https://github.com/cjdelisle/cjdns/#3-connect-your-node-to-your-friends-node">https://github.com/cjdelisle/cjdns/#3-connect-your-node-to-your-friends-node</a></p>
<dt>&bull;</p>
<dd> Step 4: Fire it up!</p>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>systemctl start cjdns</p>
<dt>
<dd> Or if you had already started cjdns:</p>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>systemctl restart cjdns</p>
<dt>
<dd></dl>
<p> For more information about other functions and non-standard setups, see README.md </p>
<h2>Index</h2>

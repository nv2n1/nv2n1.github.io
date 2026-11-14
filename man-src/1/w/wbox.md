---
title: "wbox(1)"
name: "wbox"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wbox/"
description: "wbox – HTTP testing tool and configuration-less HTTP server"
---

<h2>NAME</h2>
<p> wbox &#8211; HTTP testing tool and configuration-less HTTP server</p>
<h2>SYNOPSIS</h2>
<p> <code>wbox</code> &lt;url&gt; [ options ]<br />
 <code>wbox</code> servermode webroot &lt;path&gt; [serverport &lt;portnumber&gt; (def 8081)] </p>
<h2>DESCRIPTION</h2>
<p> <i>wbox</i> aims to help you having fun while testing HTTP related stuff. You can use it to perform many tasks, including the following: </p>
<p> &#8211; Benchmarking how much time it takes to generate content for your web application. </p>
<p> &#8211; Web server and web application stressing. </p>
<p> &#8211; Testing virtual domains configuration without the need to alter your local resolver. </p>
<p> &#8211; Use it as a <code>configuration-less HTTP server</code> to share files!</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>&lt;number&gt;</i></p>
<dd> Stop after &lt;number&gt; requests</p>
<dt><i>compr</i></p>
<dd> Send Accept-Encoding: gzip,deflate in request</p>
<dt><i>showhdr </i></p>
<dd> Show the HTTP reply header</p>
<dt><i>dump</i></p>
<dd> Show the HTTP reply header + body</p>
<dt><i>silent</i></p>
<dd> Don&#8217;t show status lines</p>
<dt><i>head</i></p>
<dd> Use the HEAD method instead of GET</p>
<dt><i>http10</i></p>
<dd> Use HTTP/1.0 instead of HTTP/1.1</p>
<dt><i>close</i></p>
<dd> Close the connection after reading few bytes</p>
<dt><i>host<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;hostname&gt;</i></p>
<dd> Use &lt;hostname&gt; as Host: field in HTTP request</p>
<dt><i>timesplit</i></p>
<dd> Show transfer times for different data chunks</p>
<dt><i>wait<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;number&gt; </i></p>
<dd> Wait &lt;number&gt; seconds between requests. Default 1.</p>
<dt><i>clients &lt;number&gt;</i></p>
<dd> Spawn &lt;number&gt; concurrent clients (via fork()).</p>
<dt><i>referer &lt;url&gt;</i></p>
<dd> Send the specified referer header.</p>
<dt><i>cookie &lt;name&gt; &lt;val&gt;</i></p>
<dd> Set cookie name=val, can be used multiple times.</p>
<dt><i>maxclients &lt;number&gt;</i></p>
<dd> Max concurrent clients in <code>server mode</code><i> (default 20).</p>
<dt>-h or &#8211;help</i></p>
<dd> Show this help.</p>
<dt><i>-v</i></p>
<dd> Show version.</dl>
<h2>USAGE EXAMPLES</h2>
<p> wbox wikipedia.org (simplest, basic usage) </p>
<p> wbox wikipedia.org 3 compr wait 0 (three requests, compression, no delay) </p>
<p> wbox wikipedia.org 1 showhdr silent (just show the HTTP reply header) </p>
<p> wbox wikipedia.org timesplit (show splitted time information) </p>
<p> wbox 1.2.3.4 host example.domain (test a virtual domain at 1.2.3.4) </p>
<p> wbox servermode webroot /tmp/mydocuments (Try it with <a rel="nofollow" href="http://127.0.0.1:8081)">http://127.0.0.1:8081)</a></p>
<h2>TUTORIAL</h2>
<p> Wbox is trivial to use but, in order to understand better what wbox is and how to use it, you may want to read the TUTORIAL inside the /usr/share/doc/wbox/ directory.</p>
<h2>AUTHOR</h2>
<p> wbox was written by Salvatore &#8216;antirez&#8217; Sanfilippo &lt;antirez [at] gmail.com&gt;. </p>
<p> This manual page was written by Alberto Furia &lt;straluna [at] email.it&gt;, for the Debian project (and may be used by others). </p>
<h2>Index</h2>

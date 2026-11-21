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
<dt><i>&lt;number&gt;</i></dt>
<dd> Stop after &lt;number&gt; requests</dd>
<dt><i>compr</i></dt>
<dd> Send Accept-Encoding: gzip,deflate in request</dd>
<dt><i>showhdr </i></dt>
<dd> Show the HTTP reply header</dd>
<dt><i>dump</i></dt>
<dd> Show the HTTP reply header + body</dd>
<dt><i>silent</i></dt>
<dd> Don&#8217;t show status lines</dd>
<dt><i>head</i></dt>
<dd> Use the HEAD method instead of GET</dd>
<dt><i>http10</i></dt>
<dd> Use HTTP/1.0 instead of HTTP/1.1</dd>
<dt><i>close</i></dt>
<dd> Close the connection after reading few bytes</dd>
<dt><i>host<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;hostname&gt;</i></dt>
<dd> Use &lt;hostname&gt; as Host: field in HTTP request</dd>
<dt><i>timesplit</i></dt>
<dd> Show transfer times for different data chunks</dd>
<dt><i>wait<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;number&gt; </i></dt>
<dd> Wait &lt;number&gt; seconds between requests. Default 1.</dd>
<dt><i>clients &lt;number&gt;</i></dt>
<dd> Spawn &lt;number&gt; concurrent clients (via fork()).</dd>
<dt><i>referer &lt;url&gt;</i></dt>
<dd> Send the specified referer header.</dd>
<dt><i>cookie &lt;name&gt; &lt;val&gt;</i></dt>
<dd> Set cookie name=val, can be used multiple times.</dd>
<dt><i>maxclients &lt;number&gt;</i></dt>
<dd> Max concurrent clients in <code>server mode</code><i> (default 20).</dd>
<dt>-h or &#8211;help</i></dt>
<dd> Show this help.</dd>
<dt><i>-v</i></dt>
<dd> Show version.</dd></dl>
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

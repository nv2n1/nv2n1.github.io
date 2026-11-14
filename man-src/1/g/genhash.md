---
title: "genhash(1)"
name: "genhash"
section: "1"
letter: "g"
url: "/docs/linux/man/1-genhash/"
description: "genhash – md5 hash generation tool for remote web pages"
---

<h2>NAME</h2>
<p> genhash &#8211; md5 hash generation tool for remote web pages</p>
<h2>SYNOPSIS</h2>
<p> <code>genhash [options] [-s server-address] [-p port] [-u url]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>genhash</code> is a tool used for generating md5sum hashes of remote web pages. <code>genhash</code> can use HTTP or HTTPS to connect to the web page. The output by this utility includes the HTTP header, page data, and the md5sum of the data. This md5sum can then be used within the <code><a href="/docs/linux/man/8-keepalived/">keepalived</a>(8)</code> program, for monitoring HTTP and HTTPS services.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;use-ssl, -S</code></p>
<dd> Use SSL to connect to the server.</p>
<dt><code>&#8211;server &lt;host&gt;, -s</code></p>
<dd> Specify the ip address to connect to.</p>
<dt><code>&#8211;port &lt;port&gt;, -p</code></p>
<dd> Specify the port to connect to.</p>
<dt><code>&#8211;url &lt;url&gt;, -u</code></p>
<dd> Specify the path to the file you want to generate the hash of.</p>
<dt><code>&#8211;use-virtualhost &lt;host&gt;, -V</code></p>
<dd> Specify the virtual host to send along with the HTTP headers.</p>
<dt><code>&#8211;hash &lt;alg&gt;, -H</code></p>
<dd> Specify the hash algorithm to make a digest of the target page. Consult the help screen for list of available ones with a mark of the default one.</p>
<dt><code>&#8211;verbose, -v</code></p>
<dd> Be verbose with the output.</p>
<dt><code>&#8211;help, -h</code></p>
<dd> Display the program help screen and exit.</p>
<dt><code>&#8211;release, -r</code></p>
<dd> Display the release number (version) and exit.</p>
<dt>
<dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-keepalived/">keepalived</a></code>(8), <code><a href="/docs/linux/man/5-keepalived-conf/">keepalived.conf</a></code>(5)</p>
<h2>AUTHOR</h2>
<p> <code>genhash</code> was written by Alexandre Cassen &lt;acassen [at] linux-vs.org&gt;. </p>
<p> This man page was contributed by Andres Salomon &lt;dilinger [at] voxel.net&gt; for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>

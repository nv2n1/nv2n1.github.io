---
title: "unbound-streamtcp(1)"
name: "unbound-streamtcp"
section: "1"
letter: "u"
url: "/docs/linux/man/1-unbound-streamtcp/"
description: "unbound-streamtcp – unbound DNS lookup utility"
---

<h2 class="name">NAME</h2>
<p> <code>unbound-streamtcp</code> &#8211; unbound DNS lookup utility </p>
<h2>SYNOPSIS</h2>
<p> <code>unbound-streamtcp</code> [<code>-unsh</code>] [<code>-f</code> <i>ipaddr[@port]</i>] <i>name</i> <i>type</i> <i>class</i></p>
<h2>DESCRIPTION</h2>
<p> <code>unbound-streamtcp</code> sends a DNS Query of the given <code>type</code> and <code>class</code> for the given <code>name</code> to the DNS server over TCP and displays the response. </p>
<p> If the server to query is not given using the <code>-f</code> option then localhost (127.0.0.1) is used. More queries can be given on one commandline, they are resolved in sequence. </p>
<p> The available options are:</p>
<dl>
<dt><i>name</i></p>
<dd> This name is resolved (looked up in the DNS).</p>
<dt><i>type</i></p>
<dd> Specify the type of data to lookup.</p>
<dt><i>class</i></p>
<dd> Specify the class to lookup for.</p>
<dt><code>-u</code></p>
<dd> Use UDP instead of TCP. No retries are attempted.</p>
<dt><code>-n</code></p>
<dd> Do not wait for the answer.</p>
<dt><code>-s</code></p>
<dd> Use SSL.</p>
<dt><code>-h</code></p>
<dd> Print program usage.</p>
<dt><code>-f </code><i>ipaddr[@port]</i></p>
<dd> Specify the server to send the queries to. If not specified localhost (127.0.0.1) is used.</dl>
<h2>EXAMPLES</h2>
<p> Some examples of use. </p>
<p> $ unbound-streamtcp <a rel="nofollow" href="http://www.example.com">www.example.com</a> A IN </p>
<p> $ unbound-streamtcp -f 192.168.1.1 <a rel="nofollow" href="http://www.example.com">www.example.com</a> SOA IN </p>
<p> $ unbound-streamtcp -f 192.168.1.1 [at] 1234 153.1.168.192.in-addr.arpa. PTR IN</p>
<h2>EXIT CODE</h2>
<p> The unbound-streamtcp program exits with status code 1 on error, 0 on no error.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Tomas Hozza &lt;thozza [at] redhat.com&gt;. </p>
<h2>Index</h2>

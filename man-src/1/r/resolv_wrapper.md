---
title: "resolv_wrapper(1)"
name: "resolv_wrapper"
section: "1"
letter: "r"
url: "/docs/linux/man/1-resolv_wrapper/"
description: "resolv_wrapper – A wrapper for dns name resolving or dns faking."
---

<h2 class="name">NAME</h2>
<p> resolv_wrapper &#8211; A wrapper for dns name resolving or dns faking. </p>
<h2>SYNOPSIS</h2>
<p> LD_PRELOAD=libresolv_wrapper.so RESOLV_WRAPPER_CONF=&quot;/path/to/resolv.conf&quot; <code>./myapplication</code></p>
<h2>DESCRIPTION</h2>
<p> resolv_wrapper makes it possible on most UNIX platforms to contact your own DNS implementation in your test environment. It requires socket_wrapper to be able to contact it. If it doesn&#8217;t work on a special platform the wrapper is able to fake DNS queries and return valid responses to your application. </p>
<dl>
<dt>
<dd> &bull; Redirects name queries to the nameservers specified in your resolv.conf</dl>
<dl>
<dt>
<dd> &bull; Can fake DNS queries using a simple formatted DNS hosts file.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> <code>RESOLV_WRAPPER_CONF</code></p>
<dl>
<dt>
<dd> This is used to specify the resolv.conf to use. The format of the resolv.conf file is defined in the manpage <i><a href="/docs/linux/man/5-resolv-conf/">resolv.conf</a>(5)</i>. Currently only the <code>namserver</code> directive is supported.</dl>
<p> <code>RESOLV_WRAPPER_HOSTS</code></p>
<dl>
<dt>
<dd> This environment variable is used for faking DNS queries. It must point to a hosts-like text file that specifies fake records for custom queries. The format of the file looks like this: </p>
<dl>
<dt>
<dd>
<pre>
TYPE    RECORD_NAME RECORD_VALUE
</pre>
</dl>
</dl>
<p> For example: </p>
<dl>
<dt>
<dd>
<pre>
A       dc.cwrap.org 127.0.0.10
AAAA    dc.cwrap.org fd00::5357:5f0a
CNAME   kerberos.cwrap.org dc.cwrap.org
SRV     _kerberos._tcp.cwrap.org kerberos.cwrap.org 88
</pre>
</dl>
<p> <code>RESOLV_WRAPPER_DEBUGLEVEL</code></p>
<dl>
<dt>
<dd> If you need to see what is going on in resolv_wrapper itself or try to find a bug, you can enable logging support in resolv_wrapper if you built it with debug symbols. </p>
<dl>
<dt>
<dd> &bull; 0 = ERROR</dl>
<dl>
<dt>
<dd> &bull; 1 = WARNING</dl>
<dl>
<dt>
<dd> &bull; 2 = DEBUG</dl>
<dl>
<dt>
<dd> &bull; 3 = TRACE</dl>
</dl>
<h2>EXAMPLE</h2>
<p> The following command would trick <i><a href="/docs/linux/man/1-kinit/">kinit</a>(1)</i> into using DNS servers from &quot;./resolv.conf&quot; for Kerberos service resolution: </p>
<dl>
<dt>
<dd>
<pre>
$ LD_PRELOAD=libresolv_wrapper.so RESOLV_WRAPPER_CONF=&quot;./resolv.conf&quot; kinit user [at] EXAMPLE.COM
</pre>
</dl>
<h2>Index</h2>

---
title: "sniproxy(8)"
name: "sniproxy"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sniproxy/"
description: "SNIProxy – transparent session based TLS and HTTP proxy"
---

<p>SNIProxy &#8211; transparent session based TLS and HTTP proxy</p>
<h2>Synopsis</h2>
<p><code>sniproxy</code> [ &#8211;<code>c</code> <i>config</i> ] [ &#8211;<code>f</code> ] [ &#8211;<code>n</code> <i>file-descriptor-limit</i> ] [ &#8211;<code>V</code> ] </p>
<h2>Description</h2>
<p>Proxies incoming HTTP and TLS connections based on the hostname contained in the initial request of the TCP session. This enables HTTPS name-based virtual hosting to separate backend servers without installing the private key on the proxy machine. </p>
<h2>Options</h2>
<dl>
<dt>-c <i>config</i></p>
<dd>Specify configuration file to use. The default is /etc/sniproxy.conf. </p>
<dt>-f</p>
<dd>Run in foreground. Do not daemonize or drop privileges. </p>
<dt>-n <i>file-descriptor-limit</i></p>
<dd>Specify the maximum file descriptor resource limit. SNIProxy will attempt to set the maximum file descriptor limit to the value specified. </p>
<dt>-V</p>
<dd>Print the version of SNIProxy and exit. </p>
</dl>

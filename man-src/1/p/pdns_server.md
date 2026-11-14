---
title: "pdns_server(1)"
name: "pdns_server"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdns_server/"
description: "pdns_server – The PowerDNS nameserver"
---

<h2>NAME</h2>
<p> pdns_server &#8211; The PowerDNS nameserver</p>
<h2>SYNOPSIS</h2>
<p> <code>pdns_server [options]</code></p>
<h2>DESCRIPTION</h2>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;daemon=</code><i>yes|no</i></p>
<dd> Indicate if the server should run in the background as a real daemon, or in the foreground.</p>
<dt><code>&#8211;guardian=</code><i>yes|no</i></p>
<dd> Run <code>pdns_server</code> inside a guardian. This guardian monitors the performance of the inner <code>pdns_server</code> instance. It is also this guardian that <code>pdns_control</code> talks to.</p>
<dt><code>&#8211;control-console</code></p>
<dd> Run the server in a special monitor mode. This enables detailed logging and exposes the raw control socket.</p>
<dt><code>&#8211;loglevel=</code><i>&lt;level&gt;</i></p>
<dd> Set the logging level.</p>
<dt><code>&#8211;help</code></p>
<dd> To view more options that are available use this option.</dl>
<h2>FILES</h2>
<dl>
<dt><i>&lt;socket&gt;</i></p>
<dd> Control socket used to communicate with <code>pdns_server</code>.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-pdns_control/">pdns_control</a></code>(8) </p>
<h2>Index</h2>

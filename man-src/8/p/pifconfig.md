---
title: "pifconfig(8)"
name: "pifconfig"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pifconfig/"
---

pifconfig - display information about a network interface

<h2>Synopsis</h2>

pifconfig [INTERFACE [INTERFACE [INTERFACE] ...]]

<h2>Description</h2>

This script mimic ifconfig behavior, but is written purely in python and python module ethtool.

<h2>Options</h2>

INTERFACE
<dl><dd>Display information about only the listed interfaces. If no interface is given all interfaces are displayed.</dl>
 

 -h, --help
<dl><dd>Show help message and exit.</dl>

<h2>See Also</h2>

<a HREF="/docs/linux/man/8-ifconfig/">ifconfig</a>(8)

<h2>Authors</h2>

Arnaldo Carvalho de Melo &lt;acme [at] redhat.com&gt; 

 Man page written by Miroslav Suchý &lt;msuchy [at] redhat.com&gt;, David Sommerseth &lt;davids [at] redhat.com&gt;

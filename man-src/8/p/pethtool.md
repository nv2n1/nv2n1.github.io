---
title: "pethtool(8)"
name: "pethtool"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pethtool/"
---

pethtool - Display or change ethernet card settings

<h2>Synopsis</h2>

pethtool [OPTIONS] [&lt;INTERFACE&gt;]

<h2>Description</h2>

This script mimic ethtool behavior, but is written purely in python and python module ethtool.

<h2>Options</h2>

INTERFACE
<dl><dd>Is the name of the ethernet device on which pethtool should operate.</dl>
 

 -h, --help
<dl><dd>Show help message and exit.</dl>
 

 -c|--show-coalesce
<dl><dd>Show coalesce options</dl>
 

 -C|--coalesce
<dl><dd>Set coalesce options 

<dl><dd><pre>adaptive-rx on|off
adaptive-tx on|off
rx-usecs N
rx-frames N
rx-usecs-irq N
rx-frames-irq N
tx-usecs N
tx-frames N
tx-usecs-irq N
tx-frames-irq N
stats-block-usecs N
pkt-rate-low N
rx-usecs-low N
rx-frames-low N
tx-usecs-low N
tx-frames-low N
pkt-rate-high N
rx-usecs-high N
rx-frames-high N
tx-usecs-high N
tx-frames-high N
sample-interval N</pre></dl></dl>
 

 -i|--driver
<dl><dd>Show driver information</dl>
 

 -k|--show-offload
<dl><dd>Get protocol offload information</dl>
 

 -K|--offload
<dl><dd>Set protocol offload
<dl><dd>[ tso on|off ]</dl></dl>

<h2>See Also</h2>

<a HREF="/docs/linux/man/8-ethtool/">ethtool</a>(8)

<h2>Authors</h2>

Arnaldo Carvalho de Melo &lt;acme [at] redhat.com&gt; 

 Man page written by Miroslav Suchý &lt;msuchy [at] redhat.com&gt;

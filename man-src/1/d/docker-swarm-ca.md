---
title: "docker-swarm-ca(1)"
name: "docker-swarm-ca"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-swarm-ca/"
description: "docker-swarm-ca – Display and rotate the root CA"
---

<h2 class="name">NAME</h2>
<p> docker-swarm-ca &#8211; Display and rotate the root CA </p>
<h2>SYNOPSIS</h2>
<p> <code>docker swarm ca [OPTIONS]</code> </p>
<h2>DESCRIPTION</h2>
<p> Display and rotate the root CA </p>
<h2>OPTIONS</h2>
<p> <code>&#8211;ca-cert</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Path to the PEM-formatted root CA certificate to use for the new cluster</p>
<p> <code>&#8211;ca-key</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Path to the PEM-formatted root CA key to use for the new cluster</p>
<p> <code>&#8211;cert-expiry</code>=2160h0m0s <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Validity period for node certificates (ns|us|ms|s|m|h)</p>
<p> <code>-d</code>, <code>&#8211;detach</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Exit immediately instead of waiting for the root rotation to converge</p>
<p> <code>&#8211;external-ca</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Specifications of one or more certificate signing endpoints</p>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for ca</p>
<p> <code>-q</code>, <code>&#8211;quiet</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Suppress progress output</p>
<p> <code>&#8211;rotate</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Rotate the swarm CA &#8211; if no certificate or key are provided, new ones will be generated</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-swarm/">docker-swarm</a>(1)</code> </p>
<h2>Index</h2>

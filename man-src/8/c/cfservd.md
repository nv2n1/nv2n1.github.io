---
title: "cfservd(8)"
name: "cfservd"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cfservd/"
description: "cfservd – cfengine server daemon"
---

<p>cfservd &#8211; cfengine server daemon</p>
<h2>Synopsis</h2>
<p>/usr/local/sbin/cfservd [options] </p>
<h2>Description</h2>
<p><code>cfengine</code> is a language based system specifically designed for testing and configuring unix-like systems attached to a TCP/IP network. Cfservd is a file server and protective wrapper for starting cfengine remotely. It performs access control based on RSA authentication and IP address. The daemon looks for a configuration file cfservd.conf by default. Cfservd gives little information when it fails to serve. This is by design. More information can be obtained using the debug option -d2 on both client and server ends.</p>
<dl>
<dt>-d (&#8211;debug)</p>
<dd>Enable debugging output. (parsing -d1,run, -d2, lite -d3)</p>
<dt>-h (&#8211;help)</p>
<dd>
<h2>Author</h2>
<p>Mark Burgess, Oslo University College</p>
<h2>Information</h2>
<p><a rel="nofollow" href="http://www.cfengine.org">http://www.cfengine.org</a></p>

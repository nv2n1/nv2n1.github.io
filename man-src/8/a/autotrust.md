---
title: "autotrust(8)"
name: "autotrust"
section: "8"
letter: "a"
url: "/docs/linux/man/8-autotrust/"
description: "autotrust – automated updates of DNSSEC trust anchors."
---

<p><code>autotrust</code> &#8211; automated updates of DNSSEC trust anchors.</p>
<h2>Synopsis</h2>
<p><code>autotrust</code> [<code>-c</code> <i>configfile</i>] [<code>-d</code>] [<code>-h</code>] [<code>-v</code> <i>verbosity</i>]</p>
<h2>Description</h2>
<p><code>autotrust</code> is a standalone application that automatically updates DNSSEC trust anchors. These can be used for DNSSEC aware resolvers like Unbound or BIND9. It is compliant with RFC 5011, with the exception of query intervals and retry times. In order to follow these time recommendations, autotrust should run as a daemon. It is to be called from the commandline once in a while, or from a cron job.</p>
<h2>Options</h2>
<p>All the configurations need to be set in the configuration file. For more information, see the autotrust.conf.sample. </p>
<dl>
<dt><code>-c</code><i> configfile</i></p>
<dd>Use this configfile.</p>
<dt><code>-d</code></p>
<dd>Run as daemon.</p>
<dt><code>-h</code></p>
<dd>Print help information and exit.</p>
<dt><code>-v</code><i> verbosity</i></p>
<dd>Specify a verbosity level. Setting it to zero will produce no output. Default verbosity level is 1. If verbosity is given in the configfile, the commandline value will be overrided.</dl>
<h2>Files</h2>
<dl>
<dt>/etc/autotrust/autotrust.conf</p>
<dd>default configuration file. /var/lib/autotrust/autotrust.state default file to store trust anchor state.</dl>
<h2>Diagnostics</h2>
<p><code>autotrust</code> will log all notifications and problems to the specified logfile. If no logfile was specified, output is directed to stderr. If autotrust is not daemonized, it will perform a single active refresh and will return zero code if the refresh was successfull, 1 otherwise.</p>
<h2>Authors</h2>
<p><code>autotrust</code> was written by NLnet Labs.</p>
<h2>Bugs</h2>
<p>Bugreports can be send to autotrust-users [at] nlnetlabs.nl. See TODO for more information. </p>

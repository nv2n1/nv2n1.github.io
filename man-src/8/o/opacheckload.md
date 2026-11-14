---
title: "opacheckload(8)"
name: "opacheckload"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opacheckload/"
description: "opacheckload"
---

<p>opacheckload </p>
<p> Returns load information on hosts in the fabric.</p>
<h2>Syntax</h2>
<p>opacheckload [-f <i>hostfile</i>] [-h &#8216;<i>hosts</i>&#8216;] [-r] [-a|-n numprocs] [-d uploaddir]</p>
<h2>Options</h2>
<dl>
<dt>&#8211;help</p>
<dd>Produces full help text. </p>
<dt>-f <i>hostfile</i></p>
<dd>File with hosts to check. Default = /etc/sysconfig/opa/hosts </p>
<dt>-h <i>hosts</i></p>
<dd>List of hosts to check. </p>
<dt>-r</p>
<dd>Reverses output to show the least busy hosts. Default is busiest hosts.</p>
<dt>-n <i>numprocs</i></p>
<dd>Shows top <i>numprocs</i> hosts. Default is 10.</p>
<dt>-a</p>
<dd>Shows all hosts. Default is 10. </p>
<dt>-d <i>upload_dir</i></p>
<dd>Directory to upload loadavg to. Default is uploads. </p>
</dl>
<h2>Examples</h2>
<p>opacheckload opacheckload -h &#8216;arwen elrond&#8217; HOSTS=&#8217;arwen elrond&#8217; opacheckload</p>
<h2>Environment Variables</h2>
<dl>
<dt><code>HOSTS</code></p>
<dd>List of hosts, used if -h option not supplied. </p>
<dt><code>HOSTS_FILE</code></p>
<dd>File containing list of hosts, used in absence of -f and -h. </p>
<dt><code>UPLOADS_DIR</code></p>
<dd>Directory to upload loadavg, used in absence of -d. </p>
<dt><code>FF_MAX_PARALLEL</code></p>
<dd>Maximum concurrent operations. </p>
</dl>

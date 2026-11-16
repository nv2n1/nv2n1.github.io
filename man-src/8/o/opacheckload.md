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
<dt>&#8211;help</dt>
<dd>Produces full help text. </dd>
<dt>-f <i>hostfile</i></dt>
<dd>File with hosts to check. Default = /etc/sysconfig/opa/hosts </dd>
<dt>-h <i>hosts</i></dt>
<dd>List of hosts to check. </dd>
<dt>-r</dt>
<dd>Reverses output to show the least busy hosts. Default is busiest hosts.</dd>
<dt>-n <i>numprocs</i></dt>
<dd>Shows top <i>numprocs</i> hosts. Default is 10.</dd>
<dt>-a</dt>
<dd>Shows all hosts. Default is 10. </dd>
<dt>-d <i>upload_dir</i></dt>
<dd>Directory to upload loadavg to. Default is uploads. </dd>
</dl>
<h2>Examples</h2>
<p>opacheckload opacheckload -h &#8216;arwen elrond&#8217; HOSTS=&#8217;arwen elrond&#8217; opacheckload</p>
<h2>Environment Variables</h2>
<dl>
<dt><code>HOSTS</code></dt>
<dd>List of hosts, used if -h option not supplied. </dd>
<dt><code>HOSTS_FILE</code></dt>
<dd>File containing list of hosts, used in absence of -f and -h. </dd>
<dt><code>UPLOADS_DIR</code></dt>
<dd>Directory to upload loadavg, used in absence of -d. </dd>
<dt><code>FF_MAX_PARALLEL</code></dt>
<dd>Maximum concurrent operations. </dd>
</dl>

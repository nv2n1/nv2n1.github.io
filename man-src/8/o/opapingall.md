---
title: "opapingall(8)"
name: "opapingall"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opapingall/"
description: "opapingall"
---

<p>opapingall </p>
<p> <code>(All)</code> Pings a group of hosts or chassis to verify that they are powered on and accessible through TCP/IP ping.</p>
<h2>Syntax</h2>
<p>opapingall [-C -p] [-f <i>hostfile</i>] [-F <i>chassisfile</i>] [-h &#8216;hosts&#8217;] [-H &#8216;chassis&#8217;]</p>
<h2>Options</h2>
<dl>
<dt>&#8211;help</p>
<dd>Produces full help text. </p>
<dt>-C</p>
<dd>Performs a ping against a chassis. The default is hosts. </p>
<dt>-p</p>
<dd>Pings all hosts/chassis in parallel. </p>
<dt>-f <i>hostfile</i></p>
<dd>File with hosts in cluster, default is /etc/sysconfig/opa/hosts. </p>
<dt>-F <i>chassisfile</i></p>
<dd>File with chassis in cluster default is /etc/sysconfig/opa/chassis. </p>
<dt>-h hosts</p>
<dd>List of hosts to ping. </p>
<dt>-H chassis</p>
<dd>List of chassis to ping. </p>
</dl>
<h2>Example</h2>
<p>opapingall<br />
 opapingall -h &#8216;arwen elrond&#8217;<br />
 HOSTS=&#8217;arwen elrond&#8217; opapingall<br />
 opapingall -C <code>NOTE:</code> This command pings all hosts/chassis found in the specified host/chassis file. The use of -C option merely selects the default file and/or environment variable to use. For this command, it is valid to use a file that lists both hosts and chassis. </p>
<pre><code>opapingall -C -H 'chassis1 chassis2'

CHASSIS='chassis1 chassis2' opapingall -C</code></pre>
<h2>Environment Variables</h2>
<dl>
<dt><code>HOSTS</code></p>
<dd>List of hosts, used if -h option not supplied. </p>
<dt><code>CHASSIS</code></p>
<dd>List of chassis, used if -H option not supplied. </p>
<dt><code>HOSTS_FILE</code></p>
<dd>File containing list of hosts, used in absence of -f and -h. </p>
<dt><code>CHASSIS_FILE</code></p>
<dd>File containing list of chassis, used in absence of -F and -H. </p>
<dt><code>FF_MAX_PARALLEL</code></p>
<dd>When -p option is used, maximum concurrent operations are performed. </p>
</dl>

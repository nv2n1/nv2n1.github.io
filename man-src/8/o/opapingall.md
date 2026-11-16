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
<dt>&#8211;help</dt>
<dd>Produces full help text. </dd>
<dt>-C</dt>
<dd>Performs a ping against a chassis. The default is hosts. </dd>
<dt>-p</dt>
<dd>Pings all hosts/chassis in parallel. </dd>
<dt>-f <i>hostfile</i></dt>
<dd>File with hosts in cluster, default is /etc/sysconfig/opa/hosts. </dd>
<dt>-F <i>chassisfile</i></dt>
<dd>File with chassis in cluster default is /etc/sysconfig/opa/chassis. </dd>
<dt>-h hosts</dt>
<dd>List of hosts to ping. </dd>
<dt>-H chassis</dt>
<dd>List of chassis to ping. </dd>
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
<dt><code>HOSTS</code></dt>
<dd>List of hosts, used if -h option not supplied. </dd>
<dt><code>CHASSIS</code></dt>
<dd>List of chassis, used if -H option not supplied. </dd>
<dt><code>HOSTS_FILE</code></dt>
<dd>File containing list of hosts, used in absence of -f and -h. </dd>
<dt><code>CHASSIS_FILE</code></dt>
<dd>File containing list of chassis, used in absence of -F and -H. </dd>
<dt><code>FF_MAX_PARALLEL</code></dt>
<dd>When -p option is used, maximum concurrent operations are performed. </dd>
</dl>

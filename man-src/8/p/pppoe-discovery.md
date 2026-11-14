---
title: "pppoe-discovery(8)"
name: "pppoe-discovery"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pppoe-discovery/"
description: "pppoe-discovery – perform PPPoE discovery"
---

<p>pppoe-discovery &#8211; perform PPPoE discovery</p>
<h2>Synopsis</h2>
<p><code>pppoe-discovery</code> [ <i>options</i> ]<br />
 <code>pppoe-discovery</code> { <code>-V</code> | <code>-h</code> }</p>
<h2>Description</h2>
<p><code>pppoe-discovery</code> performs the same discovery process as <code>pppoe</code>, but does not initiate a session. It sends a PADI packet and then prints the names of access concentrators in each PADO packet it receives.</p>
<h2>Options</h2>
<dl>
<dt><code>-I</code><i> interface</i></p>
<dd>
<dl>
<dd>The <code>-I</code> option specifies the Ethernet interface to use. Under Linux, it is typically eth0 or eth1. The interface should be &#8220;up&#8221; before you start <code>pppoe-discovery</code>, but should <i>not</i> be configured to have an IP address. The default interface is eth0.</dl>
<dt><code>-D</code><i> file_name</i></p>
<dd>
<dl>
<dd>The <code>-D</code> option causes every packet to be dumped to the specified <i>file_name</i>. This is intended for debugging only.</dl>
<dt><code>-U</code></p>
<dd>
<dl>
<dd>Causes <code>pppoe-discovery</code> to use the Host-Uniq tag in its discovery packets. The value of the tag is derived from the process&#8217;s PID number. This lets you run multiple instances of <code>pppoe-discovery</code> and/or <code>pppd</code> without having their discovery packets interfere with one another. You must supply this option to <i>all</i> instances that you intend to run simultaneously. This option is mutually exclusive with <code>-W</code>.</dl>
<dt><code>-W</code><i> value</i></p>
<dd>
<dl>
<dd>Causes <code>pppoe-discovery</code> to use the Host-Uniq tag in its discovery packets. The value of the tag is taken from the option argument, encoded as a string of hexadecimal digits. This lets you run multiple instances of <code>pppoe-discovery</code> and/or <code>pppd</code> without having their discovery packets interfere with one another. You must supply this option to <i>all</i> instances that you intend to run simultaneously. This option is mutually exclusive with <code>-U</code>.</dl>
<dt><code>-S</code><i> service_name</i></p>
<dd>
<dl>
<dd>Specifies the desired service name. <code>pppoe-discovery</code> will only accept access concentrators which can provide the specified service. In most cases, you should <i>not</i> specify this option. Use it only if you know that there are multiple access concentrators or know that you need a specific service name.</dl>
<dt><code>-C</code><i> ac_name</i></p>
<dd>
<dl>
<dd>Specifies the desired access concentrator name. <code>pppoe-discovery</code> will only accept the specified access concentrator. In most cases, you should <i>not</i> specify this option. Use it only if you know that there are multiple access concentrators. If both the <code>-S</code> and <code>-C</code> options are specified, they must <i>both</i> match.</dl>
<dt><code>-Q</code></p>
<dd>
<dl>
<dd>Causes <code>pppoe-discovery</code> to avoid printing discovered access concentrator names. This can be useful in scripts, which can use the exit code of the program to determine whether any matching access concentrators were discovered.</dl>
<dt><code>-t</code><i> timeout</i></p>
<dd>
<dl>
<dd>Changes the discovery timeout for PADI requests, in seconds. The default value is 5 seconds.</dl>
<dt><code>-a</code><i> attempts</i></p>
<dd>
<dl>
<dd>Changes the number of PADI discovery attempts made. By default, 3 attempts are made to discover access concentrators before giving up.</dl>
<dt><code>-V</code> | <code>-h</code></p>
<dd>
<dl>
<dd>Either of these options causes <code>pppoe-discovery</code> to print its version number and usage information, then exit.</dl>
</dl>
<h2>Authors</h2>
<p><code>pppoe-discovery</code> was written by Marco d&#8217;Itri &lt;md [at] linux.it&gt;, based on <code>pppoe</code> by David F. Skoll &lt;dfs [at] roaringpenguin.com&gt;.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-pppoe/">pppoe</a>(8), <a href="/docs/linux/man/8-pppoe-sniff/">pppoe-sniff</a>(8) </p>

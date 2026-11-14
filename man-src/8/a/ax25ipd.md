---
title: "ax25ipd(8)"
name: "ax25ipd"
section: "8"
letter: "a"
url: "/docs/linux/man/8-ax25ipd/"
description: "ax25ipd – AX.25 into IP Encapsulator"
---

<p>ax25ipd &#8211; AX.25 into IP Encapsulator</p>
<h2>Synopsis</h2>
<p><code>ax25ipd [options]</code></p>
<h2>Description</h2>
<p><code>ax25ipd</code> is an RFC1226 compliant daemon capable of providing the encapsualtion neccessary to send and receive AX.25 traffic across an IP transport. Normally invoked as part of the boot order network initialisation, <code>ax25ipd</code> is capable of talking directly to a serial port connected tnc, or over a pipe to a linux AX.25 port. KAM DE Dual Port Kiss is also supported. <code>ax25ipd</code> can be run as a pure encapsulator, or as a digital repeater with a functional callsign. Destination IP addresses are determined from a hardcoded map of callsign/IP Address pairs. <code>ax25ipd</code> defaults to using <code>/etc/ax25/ax25ipd.conf</code> as its config file. </p>
<h2>Options</h2>
<dl>
<dt><code>-v,&#8211;version</code></p>
<dd>Display the version.</p>
<dt><code>-h,&#8211;help</code></p>
<dd>Display a summary of the command line options.</p>
<dt><code>-l,&#8211;loglevel</code><i>NUM</i></p>
<dd>Set the logging level to NUM.</p>
<dt><code>-c,&#8211;configfile</code><i>FILE</i></p>
<dd>Use the configuration file named by FILE instead of the default.</dl>
<h2>Files</h2>
<p>/etc/ax25/ax25ipd.conf</p>
<h2>See Also</h2>
<p><code>ax25ipd.conf</code> <code><a href="/docs/linux/man/1-beacon/">beacon</a></code>(1), <code><a href="/docs/linux/man/4-ax25/">ax25</a></code>(4), <code><a href="/docs/linux/man/4-netrom/">netrom</a></code>(4), <code><a href="/docs/linux/man/4-rose/">rose</a></code>(4), <code><a href="/docs/linux/man/8-kissattach/">kissattach</a></code>(8). </p>
<h2>Bugs</h2>
<p>Routing needs to be looked at seriously, the method of routing is a real hack, and improvements to it have only added to the hack. </p>
<p> Logging needs to be properly implemented. </p>
<p> Command line parsing needs to be properly implemented. </p>
<p> <code>ax25ipd</code> should be part of the Linux AX.25 kernel support probably :-)</p>
<h2>Authors</h2>
<pre>Michael Westerhof &lt;Mike.Westerhof [at] Central.Sun.COM&gt; &lt;invalid address&gt;
<br>
Michael Durrant &lt;&gt;
<br>
D. Jeff Dionne VE3DJF &lt;Jeff [at] lnx_rpi.ee.ryerson.ca&gt;
<br>
Rob Mayfield VK5XXX/VK5ZEU &lt;mayfieldrob [at] mail.dec.com&gt;
<br>
Terry Dawson VK2KTJ &lt;terry [at] animats.net&gt;
<br></pre>

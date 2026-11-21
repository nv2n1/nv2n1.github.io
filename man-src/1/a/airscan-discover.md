---

title: "airscan-discover(1)"
name: "airscan-discover"
section: "1"
letter: "a"
url: "/docs/linux/man/1-airscan-discover/"
description: "airscan-discover – Discover sane-airscan compatible scanners"
---

<p> <code>airscan-discover</code> &#8211; Discover sane-airscan compatible scanners </p>
<p> <code>airscan-discover [-h] [-d] [-t]</code></p>
<p> <code>airscan-discover</code> is a command-line tool to find eSCL and WSD scanners on a local network </p>
<p> It uses Avahi to discover DNS-SD devices and its own implementation of WS-Discovery to discover WSD devices. </p>
<p> On success, it outputs a fragment of sane-airscan configuration file, that can be directly added to <code>/etc/sane.d/airscan.conf</code></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></dt>
<dd> Print help screen</dd>
<dt><code>-d</code></dt>
<dd> Print debug messages to console</dd>
<dt><code>-t</code></dt>
<dd> Write a very detailed protocol trace to <code>airscan-discover-zeroconf.log</code> and <code>airscan-discover-zeroconf.tar</code></dd></dl>
<h2>FILES</h2>
<dl>
<dt><code>airscan-discover-zeroconf.log</code></dt>
<dd> Protocol trace</dd>
<dt><code>airscan-discover-zeroconf.tar</code></dt>
<dd> Non-textual messages, if any, saved here. Textual (i.e., XML) messages included directly into the .log file</dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-sane/">sane</a>(7), <a href="/docs/linux/man/5-sane-airscan/">sane-airscan</a>(5)</p>
<h2>AUTHOR</h2>
<p> Alexander Pevzner &lt;pzz [at] apevzner.com&gt; </p>

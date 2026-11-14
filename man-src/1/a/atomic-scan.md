---
title: "atomic-scan(1)"
name: "atomic-scan"
section: "1"
letter: "a"
url: "/docs/linux/man/1-atomic-scan/"
description: "atomic-scan – Scan for CVEs in a container or image"
---

<h2 class="name">NAME</h2>
<p> atomic-scan &#8211; Scan for CVEs in a container or image </p>
<h2>SYNOPSIS</h2>
<p> <code>atomic scan</code> [<code>-h</code>|<code>&#8211;help</code>] [<code>&#8211;list</code>] [<code>&#8211;scanner</code>] [<code>&#8211;scan_type</code>] [<code>&#8211;verbose</code>] [<code>&#8211;all</code> | <code>&#8211;images</code> | <code>&#8211;containers</code> | <code>&#8211;rootfs</code> rootfs path to scan| IMAGE or CONTAINER names &#8230;] </p>
<h2>DESCRIPTION</h2>
<p> <code>atomic scan</code> will scan the a container or image looking for known Common Vulnerabilities and Exposures(CVEs) by default. It can also scan paths on the host filesystem as well using the <i>&#8211;rootfs</i> option. </p>
<p> The architecture for <i>atomic scan</i> is very plug-in friendly. You can define additional scanners to use via the plug-in interface. To list the available scanners setup on your system, you can use <i>&#8211;list</i>. To use a different scanner, you simple pass its name with the <i>&#8211;scanner</i> switch. You can also select a different scan type using the <i>&#8211;scan_type</i> switch. </p>
<h2>OPTIONS</h2>
<p> <code>-h</code> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<p> <code>&#8211;verbose</code> Show more verbose output. Specifically the stdout from the image scanner itself. </p>
<p> <code>&#8211;list</code> Show all scanners configured for atomic and their scan types. </p>
<p> <code>&#8211;scanner</code> Select as scanner other than the default. </p>
<p> <code>&#8211;scan_type</code> Select a scan_type other than the default. </p>
<p> <code>&#8211;all</code><br />
&nbsp;<wbr>&nbsp;<wbr>Instead of providing image or container names, scan all images&nbsp;<wbr>(excluding intermediate image layers)&nbsp;<wbr>and containers </p>
<p> <code>&#8211;images</code><br />
&nbsp;<wbr>&nbsp;<wbr>Scan all images&nbsp;<wbr>(excluding intermediate layers).&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Similar to the results of docker images. </p>
<p> <code>&#8211;containers</code><br />
&nbsp;<wbr>&nbsp;<wbr>Scan all containers.&nbsp;<wbr>&nbsp;<wbr>Similar to the results of docker ps -a </p>
<p> <code>&#8211;rootfs</code><br />
&nbsp;<wbr>&nbsp;<wbr>Rootfs path to scan.&nbsp;<wbr>&nbsp;<wbr>Can provide&nbsp;<wbr><i>&#8211;rootfs</i>&nbsp;<wbr>multiple times.<br />
&nbsp;<wbr>&nbsp;<wbr>Note: SELinux separation will be disabled for &#8211;rootfs scans, but all other container<br />
&nbsp;<wbr>&nbsp;<wbr>separation will still be in place. </p>
<h2>EXAMPLES</h2>
<p> List all the scanners atomic knows about and display their default scan types. </p>
<dl>
<dt>
<dd>
<pre>
atomic scan --list
</pre>
</dl>
<p> Scan an image named &#8216;foo1&#8217;. </p>
<dl>
<dt>
<dd>
<pre>
atomic scan foo1
</pre>
</dl>
<p> Scan images named &#8216;foo1&#8217; and &#8216;foo2&#8217; and produce a detailed report. </p>
<dl>
<dt>
<dd>
<pre>
atomic scan foo1 foo2
</pre>
</dl>
<p> Scan all containers. </p>
<dl>
<dt>
<dd>
<pre>
atomic scan --containers
</pre>
</dl>
<p> Scan all containers and images and create a detailed report. </p>
<dl>
<dt>
<dd>
<pre>
atomic scan --all
</pre>
</dl>
<p> Scan a rootfs mounted at /tmp/chroot </p>
<dl>
<dt>
<dd>
<pre>
atomic scan --rootfs /tmp/chroot
</pre>
</dl>
<p> Scan an image called &#8216;foo1&#8217; with a scanner called &#8216;custom_scanner&#8217; and its default scan_type </p>
<dl>
<dt>
<dd>
<pre>
atomic scan --scanner custom_scanner foo1
</pre>
</dl>
<p> Scan an image called &#8216;foo1&#8217; with a scanner called &#8216;custom_scanner&#8217; and a scan type of &#8216;list_rpms&#8217; </p>
<dl>
<dt>
<dd>
<pre>
atomic scan --scanner custom_scanner --scan_type list_rpms foo1
</pre>
</dl>
<h2>HISTORY</h2>
<p> Initial revision by Brent Baude (bbaude at redhat dot com) September 2015 Updated for new atomic scan architecture by Brent Baude (bbaude at redhat dot com) May 2016 </p>
<h2>Index</h2>

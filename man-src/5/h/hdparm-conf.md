---
title: "hdparm-conf(5)"
name: "hdparm-conf"
section: "5"
letter: "h"
url: "/docs/linux/man/5-hdparm-conf/"
description: "hdparm.conf – Debian configuration file for hdparm"
---

<p>hdparm.conf &#8211; Debian configuration file for hdparm</p>
<h2>Description</h2>
<p>This is the default configuration for hdparm for Debian. It is a rather simple script, so please follow the following guidelines :) Any line that begins with a comment is ignored &#8211; add as many as you like. </p>
<p> Since hdparm doesn&#8217;t use init script anymore, this configuration is mainly used by udev. Still one can re-apply settings from the config file by calling either </p>
<p> <code>/usr/lib/pm-utils/power.d/95hdparm-apm resume</code> </p>
<p> or by calling </p>
<p> <code>DEVNAME=/dev/&lt;disk&gt; /lib/udev/hdparm</code> </p>
<p> Note that an in-line comment is not supported. If a line consists of whitespace only (tabs, spaces, carriage return), it will be ignored, so you can space control fields as you like. ANYTHING ELSE IS PARSED!! </p>
<p> This means that lines with stray characters or lines that use non # comment characters will be interpreted by the initscript. This has probably minor, but potentially serious, side effects for your hard drives, so please follow the guidelines. Patches to improve flexibilty welcome. </p>
<p> Note that if the init script causes boot problems, you can pass &#8216;nohdparm&#8217; on the kernel command line, and the script will not be run. </p>
<p> Setting an option outside of one of the stanzas enables it for all drives. </p>
<p> If an option is listed twice, the second instance replaces the first. </p>
<p> /sbin/hdparm is not run unless a block of the form: </p>
<p> <code>DEV {</code></p>
<dl>
<dt>option</p>
<dd>
<dt>option</p>
<dd>
<dt>}</p>
<dd></dl>
<p> exists. This blocks will cause /sbin/hdparm OPTIONS DEV to be run. Where OPTIONS is the concatenation of all options previously defined outside of a block and all options defined with in the block.</p>
<h2>Options</h2>
<p>See <code>man 8 hdparm</code></p>
<h2>Author</h2>
<p>hdparm was written by Mark Lord &lt;mlord [at] pobox.com&gt;. The initial manual page was created by Stephen Gran &lt;sgran [at] debian.org&gt; for the Debian GNU/Linux system (but may be used by others).</p>

---
title: "fido(1)"
name: "fido"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fido/"
description: "fido is a realish-time log watchdog and alert daemon."
---

<h2>NAME</h2>
<p> fido is a realish-time log watchdog and alert daemon.</p>
<h2>SYNOPSIS</h2>
<p> fido [<i>option</i>]</p>
<h2>DESCRIPTION</h2>
<p> fido is a multi-threaded daemon that can watch several files at once. It looks for patterns that you configure and executes scripts or programs in the event of a match. <tt>fido</tt> works in &#8220;realish-time&#8221; in that it is about a second or so behind the clock.</p>
<h2>OPTIONS</h2>
<p> <code>Option Syntax</code> </p>
<p> Since <tt>fido</tt> uses <font SIZE="-1">GNU</font> getopt to process command-line arguments, every option has a long form along with the short one. Long options are more convenient to remember, but take time to type. You may freely mix different option styles, i.e., </p>
<pre>
  $ fido -d --pid=/var/run/fido.pid
</pre>
<p> <code>Startup Options</code> </p>
<dl>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Display the version of <tt>fido</tt> and exit.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print a help message describing all of <tt>fido</tt>&#8216;s command-line options and exit.</p>
<dt><code>-C</code>, <code>&#8211;config</code></p>
<dd> Prints the default values for all configurable settings. Values are read from the active resource file and command line arguements.</p>
<dt><code>-f /path/file</code>, <code>&#8211;file=/path/file</code></p>
<dd> This option can be used to specify a <tt>fido</tt> config file. If none is selected it will attempt to load <font SIZE="-1">FIDORC</font> as an <font SIZE="-1">ENV</font> variable. If <font SIZE="-1">FIDORC</font> is not set, then it will attempt the following files in this order: </p>
<pre>
  /etc/fido/fido.conf
  /etc/fido.conf 
  /usr/local/etc/fido.conf 
  /usr/local/etc/fido/fido.conf
</pre>
<p> At this point, if fido hasn&#8217;t found a config file, it will try to run off command line arguments. <font SIZE="-1">NOTE:</font> Command line arguments take precedent over config file settings.</p>
<dt><code>-d</code>, <code>&#8211;daemon</code></p>
<dd> This options tells fido to run in the background as a daemon. This is a default option so select this to override the config file. </p>
<p> Sets the network protocol to <font SIZE="-1">ICMP</font>. During a netscan, <tt>fido</tt> can use either <font SIZE="-1">ICMP</font> echo (default) or <font SIZE="-1">TCP/IP</font> connect for discovery. This option sets the protocol to <font SIZE="-1">ICMP</font>. This option is like pinging hosts on a network with the ping utility. <font SIZE="-1">ICMP</font> requires raw sockets. Therefore, <tt>fido</tt> must either be run as root or setuid root. (see <font SIZE="-1">ERRORS</font> below).</p>
<dt><code>-p /path/file</code>, <code>&#8211;pid=/path/file</code></p>
<dd> By default, <tt>fido</tt> writes a pid file to /var/run/fido.pid You may override that location with this option, <tt>fido</tt> &#8211;pid=/var/lib/run/fido.pid</p>
<dt><code>-l </code><font SIZE="-1"><code>VAL</code></font>, <code>&#8211;log=VAL</code></p>
<dd> Use this option to specify a logging method. The values can be &#8220;/path/to/file&#8221; or &#8220;syslog&#8221; <tt>fido</tt> can either log its messages to syslog or it can use its own internal logging mechanism to write to a specified file.</dl>
<h2>CONFIG FILE</h2>
<dl>
<dt>
<dd> fido&#8217;s configurable options can be set and stored in config files. All stored settings can be overridden with command line arguments. If a logging mechanism is set in config file, it can be overridden with &#8211;log. <tt>fido</tt> reads config files in a priortized fashion. The <font SIZE="-1">ENV</font> variable <font SIZE="-1">FIDORC</font> is the highest. That is followed by &#8216;-f /path/file&#8217; and by the system defaults: </p>
<pre>
  /etc/fido/fido.conf
  /etc/fido.conf
  /usr/local/etc/fido.conf
  /usr/local/etc/fido/fido.conf
</pre>
<p> Here is an example that sets an <font SIZE="-1">ENV</font> variable and invokes the program: </p>
<pre>
  $ FIDORC=/home/jeff/haha fido -d
</pre>
</dl>
<h2>AUTHOR</h2>
<dl>
<dt>
<dd> Jeffrey Fulmer, et al. &lt;jeff [at] joedog.org&gt;</dl>
<h2>SEE ALSO</h2>
<dl>
<dt>
<dd> <i><a href="/docs/linux/man/5-fido-conf/">fido.conf</a></i>(5)</dl>
<h2>COPYRIGHT</h2>
<dl>
<dt>
<dd> Copyright (C) <tt>2000-2014</tt> by <tt>Jeffrey Fulmer, et al.</tt> </p>
<p> This is free software; see the source for copying conditions. There is <font SIZE="-1">NO</font> warranty; not even for <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS</font> <font SIZE="-1">FOR</font> A <font SIZE="-1">PARTICULAR</font> <font SIZE="-1">PURPOSE</font>. </p>
</dl>
<h2>Index</h2>

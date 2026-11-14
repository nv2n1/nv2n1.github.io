---
title: "vidalia(1)"
name: "vidalia"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vidalia/"
description: "vidalia – Controller GUI for tor"
---

<h2 class="name">NAME</h2>
<p> vidalia &#8211; Controller GUI for tor</p>
<h2>SYNOPSIS</h2>
<p> <code>vidalia</code> [<i>options</i>] </p>
<h2>DESCRIPTION</h2>
<p> Vidalia allows you to start and stop Tor, view the status of Tor at a glance, and monitor Tor&#8217;s bandwidth usage. Vidalia also makes it easy to contribute to the Tor network by helping you setup a Tor server, if you wish. To find more information about what Tor is and how to use it, see the Tor homepage: <a rel="nofollow" href="https://www.torproject.org/">https://www.torproject.org/</a></p>
<h2>OPTIONS</h2>
<p> <code>-help</code> Displays this usage message and exits.</p>
<dl>
<dt><code>-reset</code></p>
<dd> Resets ALL stored Vidalia settings.</p>
<dt><code>-datadir </code><i>&lt;directory&gt;</i></p>
<dd> Sets Vidalia&#8217;s datadir to <i>&lt;directory&gt;</i></p>
<dt><code>-pidfile </code><i>&lt;directory/pidfile&gt;</i></p>
<dd> Sets Vidalia&#8217;s pidfile to <i>&lt;directory/pidfile&gt;</i></p>
<dt><code>-logfile </code><i>&lt;file&gt;</i></p>
<dd> Sets the name and location of Vidalia&#8217;s log file. If this option is specified without a <i>loglevel</i>, the default level of &#8216;notice&#8217; will be used.</p>
<dt><code>-loglevel </code><i>[debug|info|notice|warn|error]</i></p>
<dd> Sets the verbosity of Vidalia&#8217;s logging. If this option is specified without a <i>logfile</i>, the log messages will be printed to stdout.</p>
<dt><code>-style </code><i>&lt;directory&gt;</i></p>
<dd> Sets Vidalia&#8217;s interface style. [Windows|Motif|CDE|Plastique]</p>
<dt><code>-lang </code><i>&lt;langcode&gt;</i></p>
<dd> Sets Vidalia&#8217;s language. Run Vidalia with the <i>-help</i> option to see a list of available language codes. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tor/">tor</a></code>(1) </p>
<p> <code><a rel="nofollow" href="http://www.vidalia-project.net/">http://www.vidalia-project.net/</a></code> </p>
<h2>AUTHORS</h2>
<p> Matt Edman &lt;edmanm [at] vidalia-project.net&gt;<br />
 Justin Hipple &lt;hipplej [at] vidalia-project.net&gt; </p>
<p> This manpage was written by Alexander Wirt &lt;formorer [at] debian.org&gt; for the Debian Distribution (but may be used by others). </p>
<h2>Index</h2>

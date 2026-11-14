---
title: "colorize(1)"
name: "colorize"
section: "1"
letter: "c"
url: "/docs/linux/man/1-colorize/"
description: "colorize – A robust log colorizer"
---

<h2 class="name">NAME</h2>
<p> colorize &#8211; A robust log colorizer </p>
<h2>SYNOPSIS</h2>
<p> <code>colorize</code> [<i>options</i>]<i>&lt;</i>logfile</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>colorize</code> utility. </p>
<p> <code>colorize</code> is a short (no, it&#8217;s not short anymore :) perl script to colorize your logs. You can even use syslog-ng to redirect all logs to the script and colorize them on the fly!</p>
<h2>OPTIONS</h2>
<p> These programs follow the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>-f, &#8211;file </code><i>output</i></p>
<dd> Print output to <i>output</i> instead of standard output.</p>
<dt><code>-F, &#8211;rcfile </code><i>rcfile</i></p>
<dd> Specify an initialization file to read instead of /etc/colorizerc and ~/.colorizerc</p>
<dt><code>-h, &#8211;html</code></p>
<dd> Generate output in HTML format.</p>
<dt><code>&#8211;nocss</code></p>
<dd> Don&#8217;t use cascanding style sheets for HTML output. This can be used when the program you want to use to view the output doesn&#8217;t support cascading stylesheets (like some mailers).</p>
<dt><code>-b, &#8211;bgcolor </code><i>color</i></p>
<dd> Set the color <i>color</i> as the background color for HTML output. The given value should be a valid HTML color reference, like &quot;#ff0000&quot; or &quot;red&quot;.</p>
<dt><code>-C, &#8211;convert-date</code></p>
<dd> Convert unix timestamp to readable date format (in oops and squid log example).</p>
<dt><code>-r, &#8211;remove-facility</code></p>
<dd> syslog-ng paste the facility level before log messages, with this switch you can cut these strings off.</p>
<dt><code>&#8211;help</code></p>
<dd> Show summary of options and exit.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Show version of program.</dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Gergely Nagy &lt;8@free.bsd.hu&gt;, for the Debian GNU/Linux system (but may be used by others). Modified by Istvan Karaszi &lt;colorize [at] spam.raszi.hu&gt;. </p>
<h2>Index</h2>

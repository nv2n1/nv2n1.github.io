---
title: "statgrab-make-mrtg-config(1)"
name: "statgrab-make-mrtg-config"
section: "1"
letter: "s"
url: "/docs/linux/man/1-statgrab-make-mrtg-config/"
description: "statgrab-make-mrtg-config – generates MRTG configuration"
---

<h2>NAME</h2>
<p> statgrab-make-mrtg-config &#8211; generates MRTG configuration</p>
<h2>SYNOPSIS</h2>
<p> <code>statgrab-make-mrtg-config</code> [OPTION]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>statgrab-make-mrtg-config</code> generates MRTG configuration from statgrab output and writes it to stdout.</p>
<h2>OPTIONS</h2>
<p> The following options are supported.</p>
<dl>
<dt><code>&#8211;no-header</code></p>
<dd> Don&#8217;t print MRTG global options; useful if you want to include the output of this script in another MRTG config file</p>
<dt><code>&#8211;workdir</code> <i>PATH</i></p>
<dd> Use PATH for MRTG&#8217;s WorkDir option</p>
<dt><code>&#8211;statgrab</code> <i>PATH</i></p>
<dd> Specify location of statgrab binary (default &quot;statgrab&quot;)</p>
<dt><code>&#8211;help</code></p>
<dd> Display help and exit</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-statgrab/">statgrab</a></code>(1) <code><a href="/docs/linux/man/1-statgrab-make-mrtg-index/">statgrab-make-mrtg-index</a></code>(1)</p>
<h2>AUTHORS</h2>
<p> This man page was derived from the man page written by Bartosz Fenski for the Debian GNU/Linux distribution.</p>
<h2>WEBSITE</h2>
<p> &lt;<a rel="nofollow" href="http://www.i-scream.org/libstatgrab/">http://www.i-scream.org/libstatgrab/</a>&gt; </p>
<h2>Index</h2>

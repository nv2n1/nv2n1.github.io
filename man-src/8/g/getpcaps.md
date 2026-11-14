---
title: "getpcaps(8)"
name: "getpcaps"
section: "8"
letter: "g"
url: "/docs/linux/man/8-getpcaps/"
description: "getpcaps – display process capabilities"
---

<p>getpcaps &#8211; display process capabilities</p>
<h2>Synopsis</h2>
<p><code>getpcaps</code> [optional args] <i>pid</i>&#8230;</p>
<h2>Description</h2>
<p><code>getpcaps</code> displays the capabilities on the processes indicated by the <i>pid</i> value(s) given on the command line. A <i>pid</i> of 0 displays the capabilities of the process that is running <code>getpcaps</code> itself. </p>
<p> The capabilities are displayed in the <code><a href="/docs/linux/man/3-cap_from_text/">cap_from_text</a></code>(3) format. </p>
<p> Optional arguments:</p>
<dl>
<dt><code>&#8211;help</code> or <code>&#8211;usage</code></p>
<dd>Displays usage information and exits.</p>
<dt><code>&#8211;ugly</code> or <code>&#8211;legacy</code></p>
<dd>Displays output in a somewhat ugly legacy format.</p>
<dt><code>&#8211;verbose</code></p>
<dd>Displays usage in a legacy-like format but not quite so ugly in modern default terminal fonts.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-capsh/">capsh</a></code>(1), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/8-getcap/">getcap</a></code>(8), <code><a href="/docs/linux/man/8-setcap/">setcap</a></code>(8)</p>
<h2>Author</h2>
<p>This manual page was originally written by Robert Bihlmeyer &lt;robbe [at] debian.org&gt;, for the Debian GNU/Linux system (but may be used by others).</p>

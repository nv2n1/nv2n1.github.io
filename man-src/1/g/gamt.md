---
title: "gamt(1)"
name: "gamt"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gamt/"
description: "gamt – Intel AMT serial-over-lan (sol) client."
---

<h2>NAME</h2>
<p> gamt &#8211; Intel AMT serial-over-lan (sol) client.</p>
<h2>SYNOPSIS</h2>
<p> <code>gamt [ options ] [ host ]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>gamt</code> provides access to the serial-over-lan port of Intel AMT managed machines. <code>host</code> is the hostname or IP address of the machine gamt should connect to. </p>
<p> For more inforamtions on Intel AMT check <a href="/docs/linux/man/7-amt-howto/">amt-howto</a>(7).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> Display help text.</p>
<dt><code>-u &lt;user&gt;</code></p>
<dd> Specify username, defaults to &quot;admin&quot;.</p>
<dt><code>-p &lt;pass&gt;</code></p>
<dd> Specify password. <code>gamt</code> will prompt you if unspecified.</p>
<dt><code>-f &lt;font&gt;</code></p>
<dd> Specify terminal font, defaults to &quot;monospace 12&quot;.</p>
<dt><code>-c &lt;color&gt;</code></p>
<dd> Specify terminal text color, defaults to &quot;gray&quot;.</p>
<dt><code>-b &lt;color&gt;</code></p>
<dd> Specify terminal background color, defaults to &quot;black&quot;.</dl>
<p> Font, colors can also be changed using menu options. These settings are also written to the <code>~/.gamtrc</code> config file, so they persistent.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>AMT_PASSWORD</code></p>
<dd> Default value for the password.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-amtterm/">amtterm</a>(1), <a href="/docs/linux/man/1-amttool/">amttool</a>(1), <a href="/docs/linux/man/7-amt-howto/">amt-howto</a>(7)</p>
<h2>AUTHOR</h2>
<p> (c) 2007 Gerd Hoffmann &lt;kraxel [at] redhat.com&gt; </p>
<h2>Index</h2>

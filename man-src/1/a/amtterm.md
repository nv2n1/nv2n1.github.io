---
title: "amtterm(1)"
name: "amtterm"
section: "1"
letter: "a"
url: "/docs/linux/man/1-amtterm/"
description: "amtterm – Intel AMT serial-over-lan (sol) client."
---

<h2>NAME</h2>
<p> amtterm &#8211; Intel AMT serial-over-lan (sol) client.</p>
<h2>SYNOPSIS</h2>
<p> <code>amtterm [ options ] host [ port ]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>amtterm</code> provides access to the serial-over-lan port of Intel AMT managed machines. <code>host</code> is the hostname or IP address of the machine amtterm should connect to. <code>port</code> is the tcp port to use and defaults to 16994 (standard AMT redirection port) if unspecified. </p>
<p> For more inforamtions on Intel AMT check <a href="/docs/linux/man/7-amt-howto/">amt-howto</a>(7).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> Display help text.</p>
<dt><code>-v</code></p>
<dd> Be verbose (default).</p>
<dt><code>-q</code></p>
<dd> Be quiet.</p>
<dt><code>-u &lt;user&gt;</code></p>
<dd> Specify username, defaults to &quot;admin&quot;.</p>
<dt><code>-p &lt;pass&gt;</code></p>
<dd> Specify password. <code>amtterm</code> will prompt on the terminal if unspecified.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>AMT_PASSWORD</code></p>
<dd> Default value for the password.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gamt/">gamt</a>(1), <a href="/docs/linux/man/1-amttool/">amttool</a>(1), <a href="/docs/linux/man/7-amt-howto/">amt-howto</a>(7)</p>
<h2>AUTHOR</h2>
<p> (c) 2007 Gerd Hoffmann &lt;kraxel [at] redhat.com&gt; </p>
<h2>Index</h2>

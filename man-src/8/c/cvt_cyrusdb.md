---
title: "cvt_cyrusdb(8)"
name: "cvt_cyrusdb"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cvt_cyrusdb/"
description: "cvt_cyrusdb – convert a database file between cyrus database formats"
---

<p>&nbsp;<wbr>*</p>
<h2>Name</h2>
<p>cvt_cyrusdb &#8211; convert a database file between cyrus database formats</p>
<h2>Synopsis</h2>
<p><code>cvt_cyrusdb</code> [ <code>-C</code> <i>config-file</i> ] &lt;old-file&gt; &lt;old-fileformat&gt; &lt;new-file&gt; &lt;new-file-format&gt;</p>
<h2>Description</h2>
<p><i>cvt_cyrusdb</i> is used to convert a cyrusdb file between different database backends. Note that you should not attempt to use the same file for input and output. </p>
<p> Running without any options will list the available database backends. </p>
<p> <i>cvt_cyrusdb</i> reads any applicable configuration options out of the <i><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a></i>(5) file unless specified otherwise by <code>-C</code>. note that the file locations are NOT read out of the configuration file, and must be supplied on the command line.</p>
<h2>Options</h2>
<dl>
<dt><code>-C</code><i> config-file</i></p>
<dd>Read configuration options from <i>config-file</i>.</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/imapd.conf</code></p>
<dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a>(5)</code> </p>

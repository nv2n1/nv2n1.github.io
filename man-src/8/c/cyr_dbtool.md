---
title: "cyr_dbtool(8)"
name: "cyr_dbtool"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cyr_dbtool/"
description: "cyr_dbtool – manage Cyrus databases"
---

<p>&nbsp;<wbr>*</p>
<h2>Name</h2>
<p>cyr_dbtool &#8211; manage Cyrus databases</p>
<h2>Synopsis</h2>
<p><code>cyr_dbtool</code> [ <code>-C</code> <i>config-file</i> ] [ <code>-n</code> ] &lt;db file&gt; &lt;db backend&gt; &lt;action&gt; [ &lt;key&gt; ] [ &lt;value&gt; ]</p>
<h2>Description</h2>
<p><i>cyr_dbtool</i> is used to manage a cyrusdb file. The usable actions are: </p>
<p> <code>show</code><i> [&lt;prefix&gt;]</i> </p>
<p> <code>get</code><i> &lt;key&gt;</i> </p>
<p> <code>set</code><i> &lt;key&gt; &lt;value&gt;</i> </p>
<p> <code>delete</code><i> &lt;key&gt;</i> </p>
<p> <code>consistency</code> </p>
<p> You may omit key or key/value and specify one per line on stdin. Keys are terminated by tab or newline, values are terminated by newline. </p>
<p> Running without any options will list the available database backends and usable actions. </p>
<p> The &#8216;consistency&#8217; command runs a consistency check on the DB by calling </p>
<p> <i>cyr_dbtool</i> reads any applicable configuration options out of the <i><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a></i>(5) file unless specified otherwise by <code>-C</code>. note that the file locations are NOT read out of the configuration file, and must be supplied on the command line.</p>
<h2>Options</h2>
<dl>
<dt><code>-C</code><i> config-file</i></p>
<dd>Read configuration options from <i>config-file</i>.</p>
<dt><code>-n</code></p>
<dd>Create the database file if it doesn&#8217;t already exist.</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/imapd.conf</code></p>
<dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a>(5)</code> </p>

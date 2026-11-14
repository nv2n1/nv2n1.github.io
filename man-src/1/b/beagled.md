---
title: "beagled(1)"
name: "beagled"
section: "1"
letter: "b"
url: "/docs/linux/man/1-beagled/"
description: "beagled – the Beagle desktop search daemon"
---

<h2>NAME</h2>
<p> beagled &#8211; the Beagle desktop search daemon</p>
<h2>SYNOPSIS</h2>
<p> <code>beagled</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>beagled,</code> the Beagle daemon, is the heart of Beagle, a system for searching and managing your personal information space. The Beagle daemon should normally be started as part of user&#8217;s desktop startup process. </p>
<p> Running <code>beagled</code> by hand is of use for those wishing to customize the Beagle daemon&#8217;s execution via command-line options, developers testing Beagle, or those who use Beagle only infrequently.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;foreground|&#8211;fg</code></p>
<dd> If specified, execute the Beagle daemon in the foreground.</p>
<dt><code>&#8211;background|&#8211;bg</code></p>
<dd> If specified, execute the Beagle daemon in the background (default).</p>
<dt><code>&#8211;replace</code></p>
<dd> If specified, the daemon tries to shutdown and replace any other Beagle daemon already running.</p>
<dt><code>&#8211;backend </code></p>
<dd> Configure which backends to use.</p>
<dt><code>&#8211;backend &lt;name&gt; </code></p>
<dd> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Only start backend &#8216;name&#8217;</p>
<dt><code>&#8211;backend +&lt;name&gt;</code></p>
<dd> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Additionally start backend &#8216;name&#8217;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>&#8211;backend -&lt;name&gt;</code></p>
<dd> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Disable backend &#8216;name&#8217;<tt>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>&#8211;list-backends</code></p>
<dd> Retrieve a list of all known backends. This list of backends can then be used with with the &#8211;allow/deny-backend options. Using this argument will print out the list of backends and then exit.</p>
<dt><code>&#8211;add-static-backend</code></p>
<dd> Add a static backend by path.</p>
<dt><code>&#8211;version</code></p>
<dd> Show version of daemon, Mono, and Sqlite.</dl>
<h2>ADVANCE OPTIONS</h2>
<p> <code>These</code> options are mainly for debugging and fine-tuning execution and are thus not required for standard use.</p>
<dl>
<dt><code>&#8211;debug</code></p>
<dd> Enable extensive logging suited for general debugging purposes.</p>
<dt><code>&#8211;debug-memory</code></p>
<dd> Enable mono debugging suited for extensive debugging purposes.</p>
<dt><code>&#8211;indexing-test-mode</code></p>
<dd>
&nbsp;<wbr>Run in foreground, and exit when fully indexed.</p>
<dt><code>&#8211;indexing-delay </code></p>
<dd> Time to wait before indexing. (Default 60 seconds)</p>
<dt><code>&#8211;disable-scheduler</code></p>
<dd> Disable the internal scheduler and thus refrain the Beagle daemon from performing any crawling or indexing. Search facilities will remain enabled.</p>
<dt><code>&#8211;disable-text-cache</code></p>
<dd> Dont&#8217;t cache text content of the indexed data. This option only affects data that is indexed in the current session of beagled.</dl>
<h2>AUTHOR</h2>
<p> Novell, Inc.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to <a rel="nofollow" href="http://bugzilla.gnome.org">http://bugzilla.gnome.org</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2005-2007 Novell, Inc. </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-beagle-query/">beagle-query</a></code>(1), <code><a href="/docs/linux/man/1-beagle-status/">beagle-status</a></code>(1), <code><a href="/docs/linux/man/1-beagle-shutdown/">beagle-shutdown</a></code>(1), </p>
<h2>Index</h2>

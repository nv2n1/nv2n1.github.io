---
title: "update-smart-drivedb(8)"
name: "update-smart-drivedb"
section: "8"
letter: "u"
url: "/docs/linux/man/8-update-smart-drivedb/"
description: "update-smart-drivedb – update smartmontools drive database"
---

<p>update-smart-drivedb &#8211; update smartmontools drive database</p>
<h2>Synopsis</h2>
<p><code>update-smart-drivedb</code> [<i>OPTIONS</i>] [<i>DESTFILE</i>] </p>
<h2>Description</h2>
<p>[This man page is generated for the Linux version of smartmontools. It does not contain info specific to other platforms.] <code>update-smart-drivedb</code> updates <code>/var/lib/smartmontools/drivedb/drivedb.h</code> or <i>DESTFILE</i> from smartmontools SVN repository. It tries to download first from the current branch and then from trunk. The tools used for downloading are either <code><a href="/docs/linux/man/1-curl/">curl</a></code>(1), <code><a href="/docs/linux/man/1-wget/">wget</a></code>(1), <code><a href="/docs/linux/man/1-lynx/">lynx</a></code>(1), or <code><a href="/docs/linux/man/1-svn/">svn</a></code>(1). The old file is kept if the downloaded file is identical (ignoring the differences in Id string) otherwise it is moved to <code>drivedb.h.old</code>. </p>
<h2>Options</h2>
<dl>
<dt><code>-s SMARTCTL</code></p>
<dd>Use the <code><a href="/docs/linux/man/8-smartctl/">smartctl</a></code>(8) executable at path SMARTCTL for drive database syntax check. The form &#8216;-s -&#8216; disables the syntax check. The default is <code>/usr/sbin/smartctl</code>.</p>
<dt><code>-t TOOL</code></p>
<dd>Use TOOL for download. TOOL is one of: <i>curl wget lynx</i> <i>svn</i>. The default is the first one found in PATH.</p>
<dt><code>-u LOCATION</code></p>
<dd>Use URL of LOCATION for download. LOCATION is one of:<br />
 <i>sf</i> (Sourceforge code browser via HTTPS),<br />
 <i>svn</i> (SVN repository via HTTPS),<br />
 <i>svni</i> (SVN repository via HTTP),<br />
 <i>trac</i> (Trac code browser via HTTPS).<br />
 The default is <i>svn</i>.</p>
<dt><code>&#8211;cacert FILE</code></p>
<dd>Use CA certificates from FILE to verify the peer.</p>
<dt><code>&#8211;capath DIR</code></p>
<dd>Use CA certificate files from DIR to verify the peer.</p>
<dt><code>&#8211;insecure</code></p>
<dd>Don&#8217;t abort download if certificate verification fails. This option is also required if a HTTP URL is selected with &#8216;-u&#8217; option.</p>
<dt><code>&#8211;dryrun</code></p>
<dd>Print download commands only.</p>
<dt><code>-v</code></p>
<dd>Verbose output. </p>
</dl>
<h2>Examples</h2>
<pre># update-smart-drivedb
/var/lib/smartmontools/drivedb/drivedb.h updated from branches/RELEASE_6_6_DRIVEDB</pre>
<h2>Exit Status</h2>
<p>The exit status is 0 if the database has been successfully updated. If an error occurs the exit status is 1.</p>
<h2>Files</h2>
<dl>
<dt><code>/usr/sbin/update-smart-drivedb</code></p>
<dd>full path of this script.</p>
<dt><code>/usr/sbin/smartctl</code></p>
<dd>used to check syntax of new drive database.</p>
<dt><code>/var/lib/smartmontools/drivedb/drivedb.h</code></p>
<dd>current drive database.</p>
<dt><code>/var/lib/smartmontools/drivedb/drivedb.h.old</code></p>
<dd>previous drive database.</p>
<dt><code>/var/lib/smartmontools/drivedb/drivedb.h.error</code></p>
<dd>new drive database if rejected due to syntax errors.</p>
<dt><code>/var/lib/smartmontools/drivedb/drivedb.h.lastcheck</code></p>
<dd>empty file created if downloaded file was identical. </p>
</dl>
<h2>Authors</h2>
<p><code>Christian Franke</code>.<br />
 This manual page was originally written by <code>Hannes von Haugwitz &lt;hannes [at] vonhaugwitz.com&gt;</code>.</p>
<h2>Reporting Bugs</h2>
<p>To submit a bug report, create a ticket in smartmontools wiki:<br />
 &lt;<code><a rel="nofollow" href="http://www.smartmontools.org/">http://www.smartmontools.org/</a></code>&gt;.<br />
 Alternatively send the info to the smartmontools support mailing list:<br />
 &lt;<code><a rel="nofollow" href="https://lists.sourceforge.net/lists/listinfo/smartmontools-support">https://lists.sourceforge.net/lists/listinfo/smartmontools-support</a>&gt;. </p>
<p> </code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-smartctl/">smartctl</a></code>(8), <code><a href="/docs/linux/man/8-smartd/">smartd</a></code>(8). </p>
<h2>Package Version</h2>
<p>smartmontools-6.6 2016-05-31 r4324<br />
 $Id: update-smart-drivedb.8.in 4223 2016-02-26 20:18:40Z chrfranke $</p>

---
title: "bacula-sd(8)"
name: "bacula-sd"
section: "8"
letter: "b"
url: "/docs/linux/man/8-bacula-sd/"
description: "bacula-sd – Bacula’s Storage Daemon"
---

<p><code>bacula-sd</code> &#8211; Bacula&#8217;s Storage Daemon</p>
<h2>Synopsis</h2>
<p><code>bacula-sd</code> [<i>options</i>]</p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>bacula-sd</code> command.<br />
 Bacula&#8217;s Storage Daemon acts as the interface between the Bacula network backup system and a tape drive/autochanger or filesystem where the backups will be stored.</p>
<h2>Options</h2>
<dl>
<dt><code>-c&nbsp;<wbr></code><i>file</i></p>
<dd>Specify the configuration file to use.</p>
<dt><code>-d&nbsp;<wbr></code><i>nn</i></p>
<dd>Set debug level to <i>nn</i>.</p>
<dt><code>-dt</code></p>
<dd>Print timestamp in debug output.</p>
<dt><code>-f</code></p>
<dd>Run in foreground (for debugging).</p>
<dt><code>-g&nbsp;<wbr></code><i>group</i></p>
<dd>Set the group/gid to run as.</p>
<dt><code>-p</code></p>
<dd>Proceed in spite of I/O errors</p>
<dt><code>-m</code></p>
<dd>Print kaboom output (for debugging)</p>
<dt><code>-s</code></p>
<dd>No signals (for debugging).</p>
<dt><code>-t</code></p>
<dd>Test the configuration file and report errors.</p>
<dt><code>-u&nbsp;<wbr></code><i>user</i></p>
<dd>Set the username/uid to run as.</p>
<dt><code>-v</code></p>
<dd>Set verbose mode.</p>
<dt><code>-?</code></p>
<dd>Show version and usage of program.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-bacula-dir/">bacula-dir</a></code>(8), <code><a href="/docs/linux/man/8-bacula-fd/">bacula-fd</a></code>(8).</p>
<h2>Author</h2>
<p>This manual page was written by Jose Luis Tallon &lt;jltallon [at] adv-solutions.net&gt;.</p>

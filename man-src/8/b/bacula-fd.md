---
title: "bacula-fd(8)"
name: "bacula-fd"
section: "8"
letter: "b"
url: "/docs/linux/man/8-bacula-fd/"
description: "bacula-fd – Bacula’s File Daemon"
---

<p><code>bacula-fd</code> &#8211; Bacula&#8217;s File Daemon</p>
<h2>Synopsis</h2>
<p><code>bacula-fd</code> [<i>options</i>]</p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>bacula</code> command.<br />
 Bacula&#8217;s File Daemon acts as the interface between the Bacula network backup system and the filesystems to be backed up: it is responsible for reading/writing/verifying the files to be backup&#8217;d/verified/restored. Network transfer can optionally be compressed.</p>
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
<dt><code>-k</code></p>
<dd>Keep readall permission when dropping privileges.</p>
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
<p><code><a href="/docs/linux/man/8-bacula-dir/">bacula-dir</a></code>(8), <code><a href="/docs/linux/man/8-bacula-sd/">bacula-sd</a></code>(8).</p>
<h2>Author</h2>
<p>This manual page was written by Jose Luis Tallon &lt;jltallon [at] adv-solutions.net&gt;.</p>

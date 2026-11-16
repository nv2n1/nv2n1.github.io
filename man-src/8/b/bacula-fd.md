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
<dt><code>-c&nbsp;<wbr></code><i>file</i></dt>
<dd>Specify the configuration file to use.</dd>
<dt><code>-d&nbsp;<wbr></code><i>nn</i></dt>
<dd>Set debug level to <i>nn</i>.</dd>
<dt><code>-dt</code></dt>
<dd>Print timestamp in debug output.</dd>
<dt><code>-f</code></dt>
<dd>Run in foreground (for debugging).</dd>
<dt><code>-g&nbsp;<wbr></code><i>group</i></dt>
<dd>Set the group/gid to run as.</dd>
<dt><code>-k</code></dt>
<dd>Keep readall permission when dropping privileges.</dd>
<dt><code>-m</code></dt>
<dd>Print kaboom output (for debugging)</dd>
<dt><code>-s</code></dt>
<dd>No signals (for debugging).</dd>
<dt><code>-t</code></dt>
<dd>Test the configuration file and report errors.</dd>
<dt><code>-u&nbsp;<wbr></code><i>user</i></dt>
<dd>Set the username/uid to run as.</dd>
<dt><code>-v</code></dt>
<dd>Set verbose mode.</dd>
<dt><code>-?</code></dt>
<dd>Show version and usage of program.</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-bacula-dir/">bacula-dir</a></code>(8), <code><a href="/docs/linux/man/8-bacula-sd/">bacula-sd</a></code>(8).</p>
<h2>Author</h2>
<p>This manual page was written by Jose Luis Tallon &lt;jltallon [at] adv-solutions.net&gt;.</p>

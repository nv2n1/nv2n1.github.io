---
title: "checksec(7)"
name: "checksec"
section: "7"
letter: "c"
url: "/docs/linux/man/7-checksec/"
description: "checksec – check executables and kernel properties"
---

<p>checksec &#8211; check executables and kernel properties</p>
<h2>Synopsis</h2>
<p><code>checksec [options] [file]</code></p>
<h2>Description</h2>
<p><code>checksec</code> is a bash script used to check the properties of executables (like PIE, RELRO, PaX, Canaries, ASLR, Fortify Source) and kernel security options (like GRSecurity and SELinux).</p>
<h2>Options</h2>
<dl>
<dt><code>-o</code> or <code>&#8211;output</code> or <code>&#8211;format</code> <code>{cli|csv|xml|json}</code></p>
<dd>Output the results in different formats for ingestion to other applications. NOTE: This option must go before any other options currently</p>
<dt><code>-h</code> or <code>&#8211;help</code></p>
<dd>Displays the help text</p>
<dt><code>-f</code> or <code>&#8211;file</code></p>
<dd>Checks individual files for security features compiled into the executable</p>
<dt><code>-d</code> or <code>&#8211;dir</code></p>
<dd>Recursively checks all executable files in the directory for security features compiled into the executables</p>
<dt><code>-p</code> or <code>&#8211;proc</code></p>
<dd>Checks the security features of a running process by name</p>
<dt><code>-pa</code> or <code>&#8211;proc-all</code></p>
<dd>Checks the security features of all running processes</p>
<dt><code>-pl</code> or <code>&#8211;proc-libs</code></p>
<dd>Checks the security features of the all libraries of a running process ID</p>
<dt><code>-k</code> or <code>&#8211;kernel</code></p>
<dd>Checks the security features of the running kernel or a specified kernel config</p>
<dt><code>-ff</code> or <code>&#8211;fortify-file</code></p>
<dd>Checks the fortifiability of a file and if any of the fortifiable features have already been compiled into the file</p>
<dt><code>-fp</code> or <code>&#8211;fortify-proc</code></p>
<dd>Checks the fortifiability of a running process and if any of the fortifiable features have already been compiled in</p>
<dt><code>&#8211;version</code></p>
<dd>Shows the current version of the running software</p>
<dt><code>-u</code> or <code>&#8211;update</code> or <code>&#8211;upgrade</code></p>
<dd>Checks source for a signed update and updates the application if available </p>
</dl>
<h2>Diagnostics</h2>
<p>The following diagnostics may be issued on stderr:<br />
&nbsp;<wbr> Permission Denied.</p>
<dl>
<dd>For most of the checks you must be root..</dl>
<p> Debugging</p>
<dl>
<dd><code>&#8211;debug</code> option can be specified for debug level output</dl>
<h2>Authors</h2>
<p>Brian Davis &lt;slimm609 at gmail dot com&gt; Checksec was originally written by Tobias Klein</p>

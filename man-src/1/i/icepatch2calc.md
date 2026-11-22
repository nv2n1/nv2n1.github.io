---

title: "icepatch2calc(1)"
name: "icepatch2calc"
section: "1"
letter: "i"
url: "/docs/linux/man/1-icepatch2calc/"
description: "icepatch2calc – IcePatch2 tool to compress files and calculate checksums."
---

<p> icepatch2calc &#8211; IcePatch2 tool to compress files and calculate checksums.</p>
<h2>SYNOPSIS</h2>
<p> icepatch2calc [options] data_dir [file&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> IcePatch2 tool to compress files and calculate checksums. Full documentation for icepatch2calc is available online at:<br/>
 &quot;<a rel="nofollow" href="http://doc.zeroc.com/display/Ice/Using+icepatch2calc">http://doc.zeroc.com/display/Ice/Using+icepatch2calc</a>&quot;. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd>
 Displays a help message. </dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd> Displays the Ice version. </dd>
<dt><code>-z</code>, <code>&#8211;compress</code></dt>
<dd>
 Normally, icepatch2calc scans the data directory and compresses a file only if no compressed version exists, or if the compressed version of a file has a modification time that predates that of the uncompressed version. If you specify -z, the tool re-scans and recompresses the entire data directory, regardless of the time stamps on files. This option is useful if you suspect that time stamps in the data directory may be incorrect. </dd>
<dt><code>-Z</code>, <code>&#8211;no-compress</code></dt>
<dd>
 This option allows you to create a client-side checksum file. Do not use this option when creating the checksum file for the server — the option is for creating a client-side IcePatch2.sum file for updates of software on distribution media. </dd>
<dt><code>-i</code>, <code>&#8211;case-insensitive</code></dt>
<dd>
 This option disallows file names that differ only in case. (An error message will be printed if icepatch2calc encounters any files that differ in case only.) This is particularly useful for Unix servers with Windows clients, since Windows folds the case of file names, and therefore such files would override each other on the Windows client. </dd>
<dt><code>-V</code>, <code>&#8211;verbose</code></dt>
<dd>
 This option prints a progress message for each file that is compressed and for each checksum that is computed. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-icepatch2client/">icepatch2client</a></code>(1), <code><a href="/docs/linux/man/1-icepatch2server/">icepatch2server</a></code>(1) </p>

---
title: "reged(8)"
name: "reged"
section: "8"
letter: "r"
url: "/docs/linux/man/8-reged/"
description: "reged – utility to export/import and edit a Windows registry hives"
---

<p>reged &#8211; utility to export/import and edit a Windows registry hives</p>
<h2>Synopsis</h2>
<p><code>reged</code> [<i>options</i>] -x<i>&lt;registryhivefile&gt;</i>&lt;prefixstring&gt;<i>&lt;key&gt;</i>&lt;output.reg&gt; <code>reged</code> [<i>options</i>] -I<i>&lt;registryhivefile&gt;</i>&lt;prefixstring&gt;<i>&lt;input.reg&gt;</i> <code>reged</code> [<i>options</i>] -e<i>&lt;registryhivefile&gt;</i> </p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>reged</code> command. This manual page was written for the Debian distribution because the original program does not have a manual page. <code>reged</code> is the an interactive command line utility that can be used to export, import or edit a Microsoft Windows registry hive. </p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></p>
<dd>Show summary of options.</p>
<dt><code>-x &lt;registryhivefile&gt; &lt;prefixstring&gt; &lt;key&gt; &lt;output.reg&gt;</code></p>
<dd>Export parts of a hive file to a text registry (.reg) file. Prefixstring indicates the part of the registry hive to dump (for example HKEY_LOCAL_MACHINE\SOFTWARE). The &lt;key&gt; parameter defines the key to dump (recursively). You can use \ or \ to list all the keys in the hive file. </p>
<p> Only one hive file and one .reg file can be defined. </p>
<dt><code>-I &lt;registryhivefile&gt; &lt;prefixstring&gt; &lt;input.reg&gt;</code></p>
<dd>Import the content of the input.reg file into the registry file. The value &lt;prefixstring&gt; can be any valid prefix, for example is HKEY_LOCAL_MACHINE\SOFTWARE. </p>
<p> Only one .reg and one hive file supported at the same time </p>
<dt><code>-e &lt;registryhive&gt; &#8230;</code></p>
<dd>Interactive edit one or more registry files. </p>
<dt><code>-L</code></p>
<dd>Log all changed filenames to /tmp/changed. When this option is set the program automatically saves the changes in the hive files without prompting the user. </p>
<p> Be careful when using the <code>-L</code> option as a root user in a multiuser system. The filename is fixed and this can be used by malicious users (dropping a symlink with the same name) to overwrite system files. </p>
<dt><code>-C</code></p>
<dd>Automatically save all changes. Do not prompt the user. </p>
<dt><code>-N</code></p>
<dd>Do not allocate more information, only allow the editing of existing values with same size. </p>
<dt><code>-E</code></p>
<dd>Do not expand the hive file (safe mode). </p>
<dt><code>-t</code></p>
<dd>Print debug information of allocated blocks. </p>
<dt><code>-v</code></p>
<dd>Print verbose information and debug messages. </p>
</dl>
<h2>Known Bugs</h2>
<p>There are many <code>unknown</code> bugs. If you find bugs please report them to the author.</p>
<h2>See Also</h2>
<p><code>chntpwd, samusrgrp, sampasswd</code><br />
 You will find more information available on how this program works, in the text files <i>/usr/share/doc/chntpw/README.txt</i> and <i>/usr/share/doc/chntpw/MANUAL.txt</i> </p>
<h2>Author</h2>
<p>This program was written by Petter N Hagen. </p>
<p> This manual page was written by Javier Fernandez-Sanguino &lt;jfs [at] debian.org&gt;, for the Debian GNU/Linux system (but may be used by others).</p>

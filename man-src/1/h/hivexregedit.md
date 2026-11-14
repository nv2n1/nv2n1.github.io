---
title: "hivexregedit(1)"
name: "hivexregedit"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hivexregedit/"
description: "hivexregedit – Merge and export Registry changes from regedit-format files."
---

<h2 class="name">NAME</h2>
<p> hivexregedit &#8211; Merge and export Registry changes from regedit-format files. </p>
<h2>SYNOPSIS</h2>
<pre><code>
hivexregedit-- merge[--prefix prefix][--encoding enc] hivefile[regfile] hivexregedit-- export[--prefix prefix] hivefile key &gt; regfile
</code></pre>
<h2>DESCRIPTION</h2>
<p> Please note hivexregedit is a low-level tool for manipulating hive files directly. To merge or export registry changes to Windows virtual machines it&#8217;s better to use <i><a href="/docs/linux/man/1-virt-win-reg/">virt-win-reg</a></i>(1). </p>
<p> Given a local binary (&#8220;hive&#8221;) file, there are two modes. <tt>&quot;--merge&quot;</tt> imports (merges) changes from a regedit-format file into the hive. It is similar to using the <tt>&quot;/s&quot;</tt> switch in Windows regedit.exe. </p>
<p> <tt>&quot;--export&quot;</tt> exports a Registry key (recursively) into the regedit format.</p>
<h3><font SIZE="-1">ENCODING</font></h3>
<p> <tt>&quot;hivexregedit&quot;</tt> expects that regedit files have already been re-encoded in the local encoding. Usually on Linux hosts, this means <font SIZE="-1">UTF-8</font> with Unix-style line endings. Since Windows regedit files are often in <font SIZE="-1">UTF-16LE</font> with Windows-style line endings, you may need to re-encode the whole file before or after processing. </p>
<p> To re-encode a file from Windows format to Linux (before processing it with the <tt>&quot;--merge&quot;</tt> option), you would do something like this: </p>
<pre>
 iconv -f utf-16le -t utf-8 &lt; win.reg | dos2unix &gt; linux.reg
</pre>
<p> To go in the opposite direction, after using <tt>&quot;--export&quot;</tt> and before sending the file to a Windows user, do something like this: </p>
<pre>
 unix2dos &lt; linux.reg | iconv -f utf-8 -t utf-16le &gt; win.reg
</pre>
<p> For more information about encoding, see <i><a href="/docs/linux/man/3-win--hivex--regedit/">Win::Hivex::Regedit</a></i>(3). </p>
<p> If you are unsure about the current encoding, use the <i><a href="/docs/linux/man/1-file/">file</a></i>(1) command. Recent versions of Windows regedit.exe produce a <font SIZE="-1">UTF-16LE</font> file with Windows-style (<font SIZE="-1">CRLF</font>) line endings, like this: </p>
<pre>
 $ file software.reg
 software.reg: Little-endian UTF-16 Unicode text, with very long lines,
 with CRLF line terminators
</pre>
<p> This file would need conversion before you could <tt>&quot;--merge&quot;</tt> it.</p>
<h3><font SIZE="-1">SHELL QUOTING</font></h3>
<p> Be careful when passing parameters containing <tt>&quot;\&quot;</tt> (backslash) in the shell. Usually you will have to use &#8216;single quotes&#8217; or double backslashes (but not both) to protect them from the shell.</p>
<h3>CurrentControlSet etc.</h3>
<p> Registry keys like <tt>&quot;CurrentControlSet&quot;</tt> don&#8217;t really exist in the Windows Registry at the level of the hive file, and therefore you cannot modify these. </p>
<p> <tt>&quot;CurrentControlSet&quot;</tt> is usually an alias for <tt>&quot;ControlSet001&quot;</tt>. In some circumstances it might refer to another control set. The way to find out is to look at the <tt>&quot;HKLM\SYSTEM\Select&quot;</tt> key: </p>
<pre>
 $ hivexregedit --export SYSTEM '\Select'
 [\Select]
 &quot;Current&quot;=dword:00000001
 &quot;Default&quot;=dword:00000001
 &quot;Failed&quot;=dword:00000000
 &quot;LastKnownGood&quot;=dword:00000002
</pre>
<p> &#8220;Current&#8221; is the one which Windows will choose when it boots. </p>
<p> Similarly, other <tt>&quot;Current...&quot;</tt> keys in the path may need to be replaced.</p>
<h2>EXAMPLE</h2>
<p>$ virt &#8211; cat WindowsGuest / Windows / System32 / config / software &gt; software.hive<br />
                                                                         $ hivexregedit&#8211; export &#8211;prefix &#8216;HKEY_LOCAL_MACHINE\SOFTWARE&#8217; software.hive &#8216;\Microsoft&#8217; &gt; ms &#8211; keys.reg<br />
                                                                                                                                                                              $ hivexregedit&#8211; merge system.hive&#8211; prefix &#8216;HKEY_LOCAL_MACHINE\SYSTEM&#8217; additions.reg</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Display help.</p>
<dt><code>&#8211;debug</code></p>
<dd> Enable debugging in the hivex library. This is useful for diagnosing bugs and also malformed hive files.</p>
<dt><code>&#8211;merge</code></p>
<dd>
hivexregedit&#8211; merge[&#8211;prefix prefix][&#8211;encoding enc] hivefile[regfile]</p>
<p> Merge <tt>&quot;regfile&quot;</tt> (a regedit-format text file) into the hive <tt>&quot;hivefile&quot;</tt>. If <tt>&quot;regfile&quot;</tt> is omitted, then the program reads from standard input. (Also you can give multiple input files). </p>
<p> <tt>&quot;--prefix&quot;</tt> specifies the Windows Registry prefix. It is almost always necessary to use this when dealing with real hive files. </p>
<p> <tt>&quot;--encoding&quot;</tt> specifies the encoding for unmarked strings in the input. It defaults to <tt>&quot;UTF-16LE&quot;</tt> which should work for recent versions of Windows. Another possibility is to use <tt>&quot;ASCII&quot;</tt>.</p>
<dt><code>&#8211;export</code></p>
<dd>
<pre><code>
hivexregedit-- export[--prefix prefix] hivefile key &gt; regfile
</code></pre>
<p> <tt>&quot;key&quot;</tt> is a path within the hive <tt>&quot;hivefile&quot;</tt>. (The key should not contain any prefix and should be quoted to defend backslashes from the shell). The key is exported, recursively, to standard output in the textual regedit format. </p>
<p> <tt>&quot;--prefix&quot;</tt> specifies the Windows Registry prefix. It is almost always necessary to use this when dealing with real hive files.</p>
<dt><code>&#8211;prefix</code> prefix</p>
<dd> Hive files and Windows Registry key names are indirectly related. For example, inside the software hive, all keys are stored relative to <tt>&quot;HKEY_LOCAL_MACHINE\SOFTWARE&quot;</tt>. Thus <tt>&quot;HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft&quot;</tt> appears in the hive file as <tt>&quot;\Microsoft&quot;</tt>. </p>
<p> The hive format itself does not store this prefix, so you have to supply it based on outside knowledge. (<i><a href="/docs/linux/man/1-virt-win-reg/">virt-win-reg</a></i>(1), amongst other things, already knows about this). </p>
<p> Usually it is sufficient to pass the parameter <tt>&quot;--prefix 'HKEY_LOCAL_MACHINE\SOFTWARE'&quot;</tt> or similar when doing merges and exports.</p>
<dt><code>&#8211;encoding</code> UTF-16LE|ASCII</p>
<dd> When merging (only), you may need to specify the encoding for strings to be used in the hive file. This is explained in detail in &#8220;<font SIZE="-1">ENCODING STRINGS&#8221;</font> in <i><a href="/docs/linux/man/3-win--hivex--regedit/">Win::Hivex::Regedit</a></i>(3). </p>
<p> The default is to use <font SIZE="-1">UTF-16LE,</font> which should work with recent versions of Windows.</p>
<dt><code>&#8211;unsafe-printable-strings</code></p>
<dd> When exporting (only), assume strings are <font SIZE="-1">UTF-16LE</font> and print them as strings instead of hex sequences. Remove the final zero codepoint from strings if present. </p>
<p> This is unsafe and does not preserve the fidelity of strings in the original hive for various reasons:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Assumes the original encoding is <font SIZE="-1">UTF-16LE. ASCII</font> strings and strings in other encodings will be corrupted by this transformation.</p>
<dt>&bull;</p>
<dd> Assumes that everything which has type 1 or 2 is really a string and that everything else is not a string, but the type field in real hives is not reliable.</p>
<dt>&bull;</p>
<dd> Loses information about whether a zero codepoint followed the string in the hive or not.</dl>
</dl>
<dl>
<dt>
<dd>
<p> This all happens because the hive itself contains no information about how strings are encoded (see &#8220;<font SIZE="-1">ENCODING STRINGS&#8221;</font> in <i><a href="/docs/linux/man/3-win--hivex--regedit/">Win::Hivex::Regedit</a></i>(3)). </p>
<p> You should only use this option for quick hacking and debugging of the hive contents, and <i>never</i> use it if the output is going to be passed into another program or stored in another hive.</dl>
</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-virt-win-reg/">virt-win-reg</a></i>(1), <i><a href="/docs/linux/man/3-win--hivex--regedit/">Win::Hivex::Regedit</a></i>(3), <i><a href="/docs/linux/man/3-win--hivex/">Win::Hivex</a></i>(3), <i><a href="/docs/linux/man/1-hivexsh/">hivexsh</a></i>(1), <i><a href="/docs/linux/man/1-dos2unix/">dos2unix</a></i>(1), <i><a href="/docs/linux/man/1-unix2dos/">unix2dos</a></i>(1), <i><a href="/docs/linux/man/1-iconv/">iconv</a></i>(1), &lt;<a rel="nofollow" href="http://libguestfs.org/">http://libguestfs.org/</a>&gt;.</p>
<h2>AUTHOR</h2>
<p> Richard W.M. Jones &lt;<a rel="nofollow" href="http://people.redhat.com/~rjones/">http://people.redhat.com/~rjones/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2010 Red Hat Inc. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, <font SIZE="-1">MA 02139, USA.</font> </p>
<h2>Index</h2>
<dt><a href="#lbAH">EXAMPLE</a></p>
<dd>
<dt><a href="#lbAI">OPTIONS</a></p>
<dd>
<dt><a href="#lbAJ">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAK">AUTHOR</a></p>
<dd>
<dt><a href="#lbAL">COPYRIGHT</a></p>
<dd></dl>

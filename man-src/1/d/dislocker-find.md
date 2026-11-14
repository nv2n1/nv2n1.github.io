---
title: "dislocker-find(1)"
name: "dislocker-find"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dislocker-find/"
description: "Dislocker find – Find BitLocker-encrypted volumes."
---

<h2>NAME</h2>
<p> Dislocker find &#8211; Find BitLocker-encrypted volumes.</p>
<h2>SYNOPSIS</h2>
<p> dislocker-find [-h] [files&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> The program try to find BitLocker-encrypted volumes or check that provided files are BitLocker-encrypted. </p>
<p> It will print every file it find to be BitLocker-encrypted, one per line. Each file/line can be passed to the dislocker suite to be decrypted (`-V&#8217; option).</p>
<h2>OPTIONS</h2>
<p> Program&#8217;s options are described below: </p>
<dl>
<dt><code>-h</code></p>
<dd> print the help and exit</dl>
<dl>
<dt><code>files</code></p>
<dd> check for BitLocker-encrypted partitions among these files instead of trying to find them alone</dl>
<h2>RETURN VALUES</h2>
<p> -1 means an error occurred, other numbers are the number of BitLocker-encrypted volumes found. For example, 0 means no volume has been found, 42 means 42 volumes have been found.</p>
<h2>EXAMPLES</h2>
<p> No volume is found automatically, the program returns 0 volume found (the last line comes from the echo):</p>
<dl>
<dt>
<dd>
<pre>
# dislocker-find.rb ; echo $?
No BitLocker volume found.
0
</pre>
</dl>
<p> Two volumes are found, the program returns this number (the last line comes from the echo):</p>
<dl>
<dt>
<dd>
<pre>
# dislocker-find.rb ; echo $?
/dev/sda3
/dev/sda7
2
</pre>
</dl>
<h2>AUTHOR</h2>
<p> This tool is developed by Romain Coltel on behalf of HSC (<code><a rel="nofollow" href="http://www.hsc.fr/">http://www.hsc.fr/</a></code>) </p>
<p> Feel free to send bugs report to &lt;dislocker __AT__ hsc __DOT__ fr&gt; </p>
<h2>Index</h2>

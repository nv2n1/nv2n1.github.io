---
title: "amarchiver(8)"
name: "amarchiver"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amarchiver/"
description: "amarchiver – Create, extract or list amanda archive"
---

<p>amarchiver &#8211; Create, extract or list amanda archive</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>amarchiver</code> &#8211;version|&#8211;create|&#8211;extract|&#8211;list [&#8211;verbose] [&#8211;file&nbsp;<wbr><i>file</i>] [<i>filename</i>]&#8230;</dl>
<h2>Description</h2>
<p><code>Amarchiver</code></p>
<dd>manipulates amanda archive file. On creation, amarchiver doesn&#8217;t recurse into directories. If a filename specifies a directory, it will be ignored. If it specifies a character device, amarchiver reads the device and archives the data. If a filename specifies a named pipe, amarchiver reads the named pipe and archives the data. </p>
<p> Note that this tool is more limited than the Amanda archive library, and may not be appropriate for some archive files &#8212; particularly those which use non-strings in their filenames.</p>
<h2>Options</h2>
<p><code>&#8211;version</code></p>
<dl>
<dd>print the amarchiver version</dl>
<p> <code>&#8211;create</code></p>
<dl>
<dd>Create an amanda archive. Only the supplied filenames are included. With one <code>&#8211;verbose</code>, lists the filenames. With two, lists the filenames and sizes.</dl>
<p> <code>&#8211;list</code></p>
<dl>
<dd>List the filenames in an amanda archive. No additional filenames are allowed on the command line.</dl>
<p> <code>&#8211;extract</code></p>
<dl>
<dd>Extract an amanda archive. If filenames are supplied, only those files are extracted. Files are created in the current directory, suffixed with a dot (&#8216;.&#8217;) and the attribute ID.</dl>
<p> <code>&#8211;verbose</code></p>
<dl>
<dd>Give more information.</dl>
<p> <code>&#8211;file</code> file</p>
<dl>
<dd>Create, list or extract from the given file instead of stdin/stdout.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/5-amanda-archive-format/">amanda-archive-format</a></code>(5) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Authors</h2>
<p><code>Dustin J. Mitchell</code> &lt;dustin [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
<p> <code>Jean-Louis Martineau</code> &lt;martineau [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>

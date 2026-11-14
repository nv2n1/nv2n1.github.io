---
title: "update-cracklib(8)"
name: "update-cracklib"
section: "8"
letter: "u"
url: "/docs/linux/man/8-update-cracklib/"
description: "update-cracklib – Regenerate cracklib dictionary"
---

<p>update-cracklib &#8211; Regenerate cracklib dictionary</p>
<h2>Synopsis</h2>
<p><code>update-cracklib</code> </p>
<h2>Description</h2>
<p><code>update-cracklib</code> builds a compressed and accumulated version of wordlists stored in the directories given in cracklib&#8217;s configuration file /etc/cracklib/cracklib.conf. Programs using cracklib2 need this database to be of any use. By default this script is called by cron every day. </p>
<h2>Result</h2>
<p><code>update-cracklib</code> prints out two numbers: the number of words read from the ASCII dictionaries and the number of words eventually written into the cracklib database; if no error occurred, these should be equal. </p>
<p> 0 is returned on success, otherwise an error message is printed to standard error and -1 is returned.</p>
<h2>Files</h2>
<dl>
<dt><code>/etc/cracklib/cracklib.conf</code></p>
<dd>shell script that sets <code>cracklib_dictpath_src</code> which must be a space separated list of source dictionary files. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-cracklib/">cracklib</a></code>(3), <code><a href="/docs/linux/man/8-crack_mkdict/">crack_mkdict</a></code>(8) </p>
<h2>Author</h2>
<p>This program and manual page was written by Martin Pitt &lt;martin [at] piware.de&gt; for the Debian GNU/Linux System (but may be used by others).</p>

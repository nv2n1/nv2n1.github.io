---
title: "amraw(8)"
name: "amraw"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amraw/"
description: "amraw – Amanda Application open and read data"
---

<p>amraw &#8211; Amanda Application open and read data</p>
<h2>Description</h2>
<p>Amraw is an Amanda Application API script. It should not be run by users directly. It uses dd to backup and restore data. </p>
<p> Amraw can backup only one directory entry, it can be a single file, a raw device, anything that amanda can open and read. </p>
<p> The <code>diskdevice</code> in the disklist (DLE) must be the filename amraw open and read. </p>
<p> Restore is done in place, an open is done and the data is written to it. A file owned by root and permission 0600 is create if the directory entry doesn&#8217;t exist before the restore. </p>
<p> Only full backup is allowed</p>
<h2>Properties</h2>
<p>This section lists the properties that control amgtar&#8217;s functionality. See <code><a href="/docs/linux/man/7-amanda-applications/">amanda-applications</a></code>(7) for information on application properties and how they are configured. </p>
<p> DIRECTORY</p>
<dl>
<dd>Used only for restore command, can be a device name or file, the data will be restored to it.</dl>
<h2>Example</h2>
<pre> define application-tool app_amraw {
 plugin &quot;amraw&quot;
 }</pre>
<p>A dumptype using this application might look like: </p>
<pre> define dumptype amraw {
 global
 program &quot;APPLICATION&quot;
 application &quot;app_amraw&quot;
 }</pre>
<p>Note that the <i>program</i> parameter must be set to <i>&quot;APPLICATION&quot;</i> to use the <i>application</i> parameter.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5), <code><a href="/docs/linux/man/7-amanda-applications/">amanda-applications</a></code>(7) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Author</h2>
<p><code>Jean-Louis Martineau</code> &lt;martineau [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>

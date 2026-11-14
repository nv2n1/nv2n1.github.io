---
title: "perf-buildid-cache(1)"
name: "perf-buildid-cache"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perf-buildid-cache/"
description: "perf-buildid-cache – Manage build-id cache."
---

<h2 class="name">NAME</h2>
<p> perf-buildid-cache &#8211; Manage build-id cache. </p>
<h2>SYNOPSIS</h2>
<pre>
<i>perf buildid-cache &lt;options&gt;</i>
</pre>
<h2>DESCRIPTION</h2>
<p> This command manages the build-id cache. It can add and remove files to/from the cache. In the future it should as well purge older entries, set upper limits for the space used by the cache, etc.</p>
<h2>OPTIONS</h2>
<p> -a, &#8211;add=</p>
<dl>
<dt>
<dd> Add specified file to the cache.</dl>
<p> -k, &#8211;kcore</p>
<dl>
<dt>
<dd> Add specified kcore file to the cache. For the current host that is /proc/kcore which requires root permissions to read. Be aware that running <i>perf buildid-cache</i> as root may update root&#8217;s build-id cache not the user&#8217;s. Use the -v option to see where the file is created. Note that the copied file contains only code sections not the whole core image. Note also that files &quot;kallsyms&quot; and &quot;modules&quot; must also be in the same directory and are also copied. All 3 files are created with read permissions for root only. kcore will not be added if there is already a kcore in the cache (with the same build-id) that has the same modules at the same addresses. Use the -v option to see if a copy of kcore is actually made.</dl>
<p> -r, &#8211;remove=</p>
<dl>
<dt>
<dd> Remove specified file from the cache.</dl>
<p> -M, &#8211;missing=</p>
<dl>
<dt>
<dd> List missing build ids in the cache for the specified file.</dl>
<p> -u, &#8211;update</p>
<dl>
<dt>
<dd> Update specified file of the cache. It can be used to update kallsyms kernel dso to vmlinux in order to support annotation.</dl>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
<dd> Be more verbose.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-perf-record/">perf-record</a></code>(1), <code><a href="/docs/linux/man/1-perf-report/">perf-report</a></code>(1), <code><a href="/docs/linux/man/1-perf-buildid-list/">perf-buildid-list</a></code>(1) </p>
<h2>Index</h2>

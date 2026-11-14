---
title: "htcacheclean(8)"
name: "htcacheclean"
section: "8"
letter: "h"
url: "/docs/linux/man/8-htcacheclean/"
description: "htcacheclean – Clean up the disk cache"
---

<p>htcacheclean &#8211; Clean up the disk cache</p>
<h2>Synopsis</h2>
<p> <code>htcacheclean</code> [ &#8211;<code>D</code> ] [ &#8211;<code>v</code> ] [ &#8211;<code>t</code> ] [ &#8211;<code>r</code> ] [ &#8211;<code>n</code> ] [ &#8211;<code>R</code><i>round</i> ] &#8211;<code>p</code><i>path</i> [ &#8211;<code>l</code><i>limit</i> ] [ &#8211;<code>L</code><i>limit</i> ]<br />
&nbsp; <code>htcacheclean</code> [ &#8211;<code>n</code> ] [ &#8211;<code>t</code> ] [ &#8211;<code>i</code> ] [ &#8211;<code>P</code><i>pidfile</i> ] [ &#8211;<code>R</code><i>round</i> ] &#8211;<code>d</code><i>interval</i> &#8211;<code>p</code><i>path</i> [ &#8211;<code>l</code><i>limit</i> ] [ &#8211;<code>L</code><i>limit</i> ]<br />
&nbsp; <code>htcacheclean</code> [ &#8211;<code>v</code> ] [ &#8211;<code>R</code><i>round</i> ] &#8211;<code>p</code><i>path</i> [ &#8211;<code>a</code> ] [ &#8211;<code>A</code> ]<br />
&nbsp; <code>htcacheclean</code> [ &#8211;<code>D</code> ] [ &#8211;<code>v</code> ] [ &#8211;<code>t</code> ] [ &#8211;<code>R</code><i>round</i> ] &#8211;<code>p</code><i>path</i> <i>url</i><br />
&nbsp; </p>
<h2>Summary</h2>
<p>&nbsp; </p>
<p> <code>htcacheclean</code> is used to keep the size of mod_cache_disk&#8217;s storage within a given size limit, or limit on inodes in use. This tool can run either manually or in daemon mode. When running in daemon mode, it sleeps in the background and checks the cache directory at regular intervals for cached content to be removed. You can stop the daemon cleanly by sending it a TERM or INT signal. When run manually, a once off check of the cache directory is made for cached content to be removed. If one or more URLs are specified, each URL will be deleted from the cache, if present.<br />
&nbsp;</p>
<h2>Options</h2>
<p>&nbsp;<br />
&nbsp;</p>
<dl>
<dt><code>-d</code><i>interval</i></p>
<dd>Daemonize and repeat cache cleaning every <i>interval</i> minutes. This option is mutually exclusive with the <code>-D</code>, <code>-v</code> and <code>-r</code> options. To shutdown the daemon cleanly, just send it a <code>SIGTERM</code> or <code>SIGINT</code>.</p>
<dt><code>-D</code></p>
<dd>Do a dry run and don&#8217;t delete anything. This option is mutually exclusive with the <code>-d</code> option. When doing a dry run and deleting directories with <code>-t</code>, the inodes reported deleted in the stats cannot take into account the directories deleted, and will be marked as an estimate.</p>
<dt><code>-v</code></p>
<dd>Be verbose and print statistics. This option is mutually exclusive with the <code>-d</code> option.</p>
<dt><code>-r</code></p>
<dd>Clean thoroughly. This assumes that the Apache web server is not running (otherwise you may get garbage in the cache). This option is mutually exclusive with the <code>-d</code> option and implies the <code>-t</code> option.</p>
<dt><code>-n</code></p>
<dd>Be nice. This causes slower processing in favour of other processes. <code>htcacheclean</code> will sleep from time to time so that (a) the disk IO will be delayed and (b) the kernel can schedule other processes in the meantime.</p>
<dt><code>-t</code></p>
<dd>Delete all empty directories. By default only cache files are removed, however with some configurations the large number of directories created may require attention. If your configuration requires a very large number of directories, to the point that inode or file allocation table exhaustion may become an issue, use of this option is advised.</p>
<dt><code>-p</code><i>path</i></p>
<dd>Specify <i>path</i> as the root directory of the disk cache. This should be the same value as specified with the CacheRoot directive.</p>
<dt><code>-P</code><i>pidfile</i></p>
<dd>Specify <i>pidfile</i> as the name of the file to write the process ID to when daemonized.</p>
<dt><code>-R</code><i>round</i></p>
<dd>Specify <i>round</i> as the amount to round sizes up to, to compensate for disk block sizes. Set to the block size of the cache partition.</p>
<dt><code>-l</code><i>limit</i></p>
<dd>Specify <i>limit</i> as the total disk cache size limit. The value is expressed in bytes by default (or attaching <code>B</code> to the number). Attach <code>K</code> for Kbytes, <code>M</code> for MBytes or <code>G</code> for Gbytes.</p>
<dt><code>-L</code><i>limit</i></p>
<dd>Specify <i>limit</i> as the total disk cache inode limit. <code>K</code>, <code>M</code> or <code>G</code> suffix can also be used.</p>
<dt><code>-i</code></p>
<dd>Be intelligent and run only when there was a modification of the disk cache. This option is only possible together with the <code>-d</code> option.</p>
<dt><code>-a</code></p>
<dd>List the URLs currently stored in the cache. Variants of the same URL will be listed once for each variant.</p>
<dt><code>-A</code></p>
<dd>List the URLs currently stored in the cache, along with their attributes in the following order: url, header size, body size, status, entity version, date, expiry, request time, response time, body present, head request.<br />
&nbsp;</dl>
<h2>Deleting A Specific Url</h2>
<p>&nbsp; </p>
<p> If <code>htcacheclean</code> is passed one or more URLs, each URL will be deleted from the cache. If multiple variants of an URL exists, all variants would be deleted.<br />
&nbsp; </p>
<p> When a reverse proxied URL is to be deleted, the effective URL is constructed from the <code>Host</code> header, the <code>port</code>, the <code>path</code> and the <code>query</code>. Note the &#8216;?&#8217; in the URL must always be specified explicitly, whether a query string is present or not. For example, an attempt to delete the path <code>/</code> from the server <code>localhost</code>, the URL to delete would be <code><a rel="nofollow" href="http://localhost:80/?">http://localhost:80/?</a></code>.<br />
&nbsp;</p>
<h2>Listing Urls In The Cache</h2>
<p>&nbsp; </p>
<p> By passing the <code>-a</code> or <code>-A</code> options to <code>htcacheclean</code>, the URLs within the cache will be listed as they are found, one URL per line. The <code>-A</code> option dumps the full cache entry after the URL, with fields in the following order:<br />
&nbsp;<br />
&nbsp;</p>
<dl>
<dt>url</p>
<dd>The URL of the entry.</p>
<dt>header size</p>
<dd>The size of the header in bytes.</p>
<dt>body size</p>
<dd>The size of the body in bytes.</p>
<dt>status</p>
<dd>Status of the cached response.</p>
<dt>entity version</p>
<dd>The number of times this entry has been revalidated without being deleted.</p>
<dt>date</p>
<dd>Date of the response.</p>
<dt>expiry</p>
<dd>Expiry date of the response.</p>
<dt>request time</p>
<dd>Time of the start of the request.</p>
<dt>response time</p>
<dd>Time of the end of the request.</p>
<dt>body present</p>
<dd>If 0, no body is stored with this request, 1 otherwise.</p>
<dt>head request</p>
<dd>If 1, the entry contains a cached HEAD request with no body, 0 otherwise.<br />
&nbsp;</dl>
<h2>Exit Status</h2>
<p>&nbsp; </p>
<p> <code>htcacheclean</code> returns a zero status (&quot;true&quot;) if all operations were successful, <code>1</code> otherwise. If an URL is specified, and the URL was cached and successfully removed, <code>0</code> is returned, <code>2</code> otherwise. If an error occurred during URL removal, <code>1</code> is returned.<br />
&nbsp;</p>

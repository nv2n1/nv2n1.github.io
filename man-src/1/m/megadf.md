---
title: "megadf(1)"
name: "megadf"
section: "1"
letter: "m"
url: "/docs/linux/man/1-megadf/"
description: "megadf – Show total available, used, or free space in the cloud"
---

<h2 class="name">NAME</h2>
<p> megadf &#8211; Show total available, used, or free space in the cloud </p>
<h2>SYNOPSIS</h2>
<pre><code>
megadf[--free | --total | --used][--mb | --gb | -h]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Shows available, used and free space in the cloud in machine or human readable formats.</p>
<h2>OPTIONS</h2>
<p> &#8211;total</p>
<dl>
<dt>
</dt><dd> Show only total available space (free + used).</dd></dl>
<p> &#8211;free</p>
<dl>
<dt>
</dt><dd> Show only free space.</dd></dl>
<p> &#8211;used</p>
<dl>
<dt>
</dt><dd> Show only used space.</dd></dl>
<p> &#8211;human, -h</p>
<dl>
<dt>
</dt><dd> Display file sizes in a human readable format.</dd></dl>
<p> &#8211;mb</p>
<dl>
<dt>
</dt><dd> Show in MiB units.</dd></dl>
<p> &#8211;gb</p>
<dl>
<dt>
</dt><dd> Show in GiB units.</dd></dl>
<p> -u &lt;email&gt;, &#8211;username &lt;email&gt;</p>
<dl>
<dt>
</dt><dd> Account username (email)</dd></dl>
<p> -p &lt;password&gt;, &#8211;password &lt;password&gt;</p>
<dl>
<dt>
</dt><dd> Account password</dd></dl>
<p> &#8211;config &lt;path&gt;</p>
<dl>
<dt>
</dt><dd> Load configuration from a file</dd></dl>
<p> &#8211;ignore-config-file</p>
<dl>
<dt>
</dt><dd> Disable loading .megarc</dd></dl>
<p> &#8211;no-ask-password</p>
<dl>
<dt>
</dt><dd> Never ask interactively for a password</dd></dl>
<p> &#8211;reload</p>
<dl>
<dt>
</dt><dd> Reload filesystem cache</dd></dl>
<p> &#8211;debug [&lt;options&gt;]</p>
<dl>
<dt>
</dt><dd> Enable debugging of various aspects of the megatools operation. You may enable multiple debugging options separated by commas. (eg. &#8211;debug api,fs) </dd>
<p> Available options are: </p>
<dl>
<dt>
</dt><dd> &bull; </dd>
<p> api: Dump Mega.co.nz API calls</dl>
<dl>
<dt>
</dt><dd> &bull; </dd>
<p> fs: Dump Mega.co.nz filesystem (may require &#8211;reload to actually print something)</dl>
<dl>
<dt>
</dt><dd> &bull; </dd>
<p> cache: Dump cache contents</dl>
</dl>
<p> &#8211;version</p>
<dl>
<dt>
</dt><dd> Show version information</dd></dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
</dt><dd> &bull; Show overall human readable space usage information: </dd>
<dl>
<dt>
</dt><dd>
<pre>
$ megadf -h
Total: 50.0 GiB
Used:  6.4 GiB
Free:  43.6 GiB
</pre>
</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> &bull; Check free space from a script: </dd>
<dl>
<dt>
</dt><dd>
<pre>
$ test `megadf --free --gb` -lt 1 &amp;&amp; \
  echo &quot;You have less than 1 GiB of available free space&quot;
</pre>
</dd></dl>
</dl>
<h2>KNOWN BUGS</h2>
<p> Megadf can&#8217;t determine available space for premium accounts.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-megatools/">megatools</a></code>(7), <code><a href="/docs/linux/man/5-megarc/">megarc</a></code>(5), <code><a href="/docs/linux/man/1-megadf/">megadf</a></code>(1), <code><a href="/docs/linux/man/1-megadl/">megadl</a></code>(1), <code><a href="/docs/linux/man/1-megaget/">megaget</a></code>(1), <code><a href="/docs/linux/man/1-megals/">megals</a></code>(1), <code><a href="/docs/linux/man/1-megamkdir/">megamkdir</a></code>(1), <code><a href="/docs/linux/man/1-megaput/">megaput</a></code>(1), <code><a href="/docs/linux/man/1-megareg/">megareg</a></code>(1), <code><a href="/docs/linux/man/1-megarm/">megarm</a></code>(1), <code><a href="/docs/linux/man/1-megamv/">megamv</a></code>(1), <code><a href="/docs/linux/man/1-megasync/">megasync</a></code>(1), <code><a href="/docs/linux/man/1-megafs/">megafs</a></code>(1).</p>
<h2>MEGATOOLS</h2>
<p> Part of the <code><a href="/docs/linux/man/7-megatools/">megatools</a></code>(7) suite.</p>
<h2>BUGS</h2>
<p> Report bugs at <a rel="nofollow" href="https://github.com/megous/megatools">https://github.com/megous/megatools</a> or megous [at] megous.com.</p>
<h2>AUTHOR</h2>
<p> Megatools was written by Ondrej Jirman &lt;megous [at] megous.com&gt;, 2013. </p>
<p> Official website is <a rel="nofollow" href="http://megatools.megous.com.">http://megatools.megous.com.</a> </p>

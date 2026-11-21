---

title: "grok-pull(1)"
name: "grok-pull"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grok-pull/"
description: "GROK-PULL – Clone or update local git repositories"
---

<h2>NAME</h2>
<p> GROK-PULL &#8211; Clone or update local git repositories</p>
<p> grok-pull -c /path/to/repos.conf</p>
<p> This utility runs from a cronjob and downloads the latest manifest from the grokmirror master. If there are new repositories or changes in the existing repositories, grok-pull will perform the necessary git commands to clone or fetch the required data from the master. </p>
<p> At the end of its run, grok-pull will generate its own manifest file, which can then be used for further mirroring.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></dt>
<dd> show program&#8217;s version number and exit</dd>
<dt><code>-h</code>,<code> &#8211;help</code></dt>
<dd> show this help message and exit</dd>
<dt><code>-v</code>,<code> &#8211;verbose</code></dt>
<dd> Be verbose and tell us what you are doing</dd>
<dt><code>-n</code>,<code> &#8211;no-mtime-check</code></dt>
<dd> Run without checking manifest mtime.</dd>
<dt><code>-f</code>,<code> &#8211;force</code></dt>
<dd> Force full git update regardless of last-modified times. Also useful when repos.conf has changed.</dd>
<dt><code>-p</code>,<code> &#8211;purge</code></dt>
<dd> Remove any git trees that are no longer in manifest.</dd>
<dt><code>-y</code>,<code> &#8211;pretty</code></dt>
<dd> Pretty-print the generated manifest (sort repos and add indentation). This is much slower, so should be used with caution on large collections.</dd>
<dt><code>-r</code>,<code> &#8211;no-reuse-existing-repos</code></dt>
<dd> If any existing repositories are found on disk, do NOT set new remote origin and reuse, just skip them entirely</dd>
<dt><code>-m</code>,<code> &#8211;verify-mirror</code></dt>
<dd> Do not perform any updates, just verify that mirror matches upstream manifest.</dd>
<dt><code>-s</code><i>&nbsp;<wbr>SUBPATH</i>,<code>&nbsp;<wbr>&#8211;verify-subpath=</code><i>SUBPATH</i></dt>
<dd> Only verify a subpath (accepts shell globbing)</dd>
<dt><code>-c</code><i>&nbsp;<wbr>CONFIG</i>,<code>&nbsp;<wbr>&#8211;config=</code><i>CONFIG</i></dt>
<dd> Location of repos.conf</dd></dl>
<h2>EXAMPLES</h2>
<p> Locate repos.conf and modify it to reflect your needs. The default configuration file is heavily commented. </p>
<p> Add a cronjob to run as frequently as you like. For example, add the following to <code>/etc/cron.d/grokmirror.cron</code>: </p>
<pre>
# Run grok-pull every minute as user &quot;mirror&quot;
* * * * * mirror /usr/bin/grok-pull -p -c /etc/grokmirror/repos.conf
</pre>
<p> Make sure the user &quot;mirror&quot; (or whichever user you specified) is able to write to the toplevel, log and lock locations specified in repos.conf.</p>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</dt>
<dd> <a href="/docs/linux/man/1-grok-manifest/">grok-manifest</a>(1)</dd>
<dt>&bull;</dt>
<dd> <a href="/docs/linux/man/1-grok-fsck/">grok-fsck</a>(1)</dd>
<dt>&bull;</dt>
<dd> <a href="/docs/linux/man/1-git/">git</a>(1)</dd></dl>
<h2>SUPPORT</h2>
<p> Please send support requests to the mailing list: </p>
<pre>
<a rel="nofollow" href="http://lists.kernel.org/mailman/listinfo/grokmirror">http://lists.kernel.org/mailman/listinfo/grokmirror</a>
</pre>
<h2>AUTHOR</h2>
<p> mricon [at] kernel.org </p>
<p> License: GPLv3+</p>
<h2>COPYRIGHT</h2>
<p> The Linux Foundation and contributors </p>

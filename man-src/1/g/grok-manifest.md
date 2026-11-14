---
title: "grok-manifest(1)"
name: "grok-manifest"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grok-manifest/"
description: "GROK-MANIFEST – Create manifest for use with grokmirror"
---

<h2>NAME</h2>
<p> GROK-MANIFEST &#8211; Create manifest for use with grokmirror</p>
<h2>SYNOPSIS</h2>
<p> grok-manifest [opts] -m manifest.js[.gz] -t /path [/path/to/bare.git]</p>
<h2>DESCRIPTION</h2>
<p> Call grok-manifest from a git post-update or post-receive hook to create the latest repository manifest. This manifest file is downloaded by mirror slaves (if newer than what they already have) and used to only clone/pull the repositories that have changed since the mirror&#8217;s last run.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd> show program&#8217;s version number and exit</p>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd> show this help message and exit</p>
<dt><code>-m</code><i>&nbsp;<wbr>MANIFILE</i>,<code>&nbsp;<wbr>&#8211;manifest=</code><i>MANIFILE</i></p>
<dd> Location of manifest.js or manifest.js.gz</p>
<dt><code>-t</code><i>&nbsp;<wbr>TOPLEVEL</i>,<code>&nbsp;<wbr>&#8211;toplevel=</code><i>TOPLEVEL</i></p>
<dd> Top dir where all repositories reside</p>
<dt><code>-l</code><i>&nbsp;<wbr>LOGFILE</i>,<code>&nbsp;<wbr>&#8211;logfile=</code><i>LOGFILE</i></p>
<dd> When specified, will put debug logs in this location</p>
<dt><code>-c</code>,<code> &#8211;check-export-ok</code></p>
<dd> Honor the git-daemon-export-ok magic file and do not export repositories not marked as such</p>
<dt><code>-n</code>,<code> &#8211;use-now</code></p>
<dd> Use current timestamp instead of parsing commits</p>
<dt><code>-p</code>,<code> &#8211;purge</code></p>
<dd> Purge deleted git repositories from manifest</p>
<dt><code>-x</code>,<code> &#8211;remove</code></p>
<dd> Remove repositories passed as arguments from the manifest file</p>
<dt><code>-y</code>,<code> &#8211;pretty</code></p>
<dd> Pretty-print the generated manifest (sort repos and add indentation). This is much slower, so should be used with caution on large collections.</p>
<dt><code>-w</code>,<code> &#8211;wait-for-manifest</code></p>
<dd> When running with arguments, wait if manifest is not there (can be useful when multiple writers are writing to the manifest file via NFS)</p>
<dt><code>-i</code><i>&nbsp;<wbr>IGNORE</i>,<code>&nbsp;<wbr>&#8211;ignore-paths=</code><i>IGNORE</i></p>
<dd> When finding git dirs, ignore these paths (can be used multiple times, accepts shell-style globbing)</p>
<dt><code>-v</code>,<code> &#8211;verbose</code></p>
<dd> Be verbose and tell us what you are doing</dl>
<h2>EXAMPLES</h2>
<p> The examples assume that the repositories are located in /repos. If your repositories are in <code>/var/lib/git</code>, adjust both <code>-m</code> and <code>-t</code> flags accordingly. </p>
<p> Initial manifest generation: </p>
<pre>
/usr/bin/grok-manifest -m /repos/manifest.js.gz -t /repos
</pre>
<p> Inside the git hook: </p>
<pre>
/usr/bin/grok-manifest -m /repos/manifest.js.gz -t /repos -n `pwd`
</pre>
<p> To purge deleted repositories, use the <code>-p</code> flag when running from cron: </p>
<pre>
/usr/bin/grok-manifest -m /repos/manifest.js.gz -t /repos -p
</pre>
<p> You can also add it to the gitolite&#8217;s &quot;rm&quot; ADC using the <code>-x</code> flag: </p>
<pre>
/usr/bin/grok-manifest -m /repos/manifest.js.gz -t /repos -x $repo.git
</pre>
<p> To troubleshoot potential problems, you can pass <code>-l</code> parameter to grok-manifest, just make sure the user executing the hook command (user git or gitolite, for example) is able to write to that location: </p>
<pre>
/usr/bin/grok-manifest -m /repos/manifest.js.gz -t /repos \
    -l /var/log/git/grok-manifest-hook.log -n `pwd`
</pre>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/1-grok-pull/">grok-pull</a>(1)</p>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/1-git/">git</a>(1)</dl>
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
<h2>Index</h2>

---

title: "grok-fsck(1)"
name: "grok-fsck"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grok-fsck/"
description: "GROK-FSCK – Check mirrored repositories for corruption"
---

<h2>NAME</h2>
<p> GROK-FSCK &#8211; Check mirrored repositories for corruption</p>
<p> grok-fsck -c /path/to/fsck.conf</p>
<p> Git repositories can get corrupted whether they are frequently updated or not, which is why it is useful to routinely check them using &quot;git fsck&quot;. Grokmirror ships with a &quot;grok-fsck&quot; utility that will run &quot;git fsck&quot; on all mirrored git repositories. It is supposed to be run nightly from cron, and will do its best to randomly stagger the checks so only a subset of repositories is checked each night. Any errors will be sent to the user set in MAILTO.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></dt>
<dd> show program&#8217;s version number and exit</dd>
<dt><code>-h</code>,<code> &#8211;help</code></dt>
<dd> show this help message and exit</dd>
<dt><code>-v</code>,<code> &#8211;verbose</code></dt>
<dd> Be verbose and tell us what you are doing</dd>
<dt><code>-f</code>,<code> &#8211;force</code></dt>
<dd> Force immediate run on all repositories.</dd>
<dt><code>-c</code><i>&nbsp;<wbr>CONFIG</i>,<code>&nbsp;<wbr>&#8211;config=</code><i>CONFIG</i></dt>
<dd> Location of fsck.conf</dd></dl>
<h2>EXAMPLES</h2>
<p> Locate fsck.conf and modify it to reflect your needs. The default configuration file is heavily commented. </p>
<p> Set up a cron job to run nightly and to email any discovered errors to root: </p>
<pre>
# Make sure MAILTO is set, for error reports
MAILTO=root
# Run nightly, at 2AM
00 02 * * * mirror /usr/bin/grok-fsck -c /etc/grokmirror/fsck.conf
</pre>
<p> You can force a full run using the <code>-f</code> flag, but unless you only have a few smallish git repositories, it&#8217;s not recommended, as it may take several hours to complete.</p>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</dt>
<dd> <a href="/docs/linux/man/1-grok-manifest/">grok-manifest</a>(1)</dd>
<dt>&bull;</dt>
<dd> <a href="/docs/linux/man/1-grok-pull/">grok-pull</a>(1)</dd>
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

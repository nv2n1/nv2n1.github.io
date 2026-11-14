---
title: "grok-dumb-pull(1)"
name: "grok-dumb-pull"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grok-dumb-pull/"
description: "GROK-DUMB-PULL – Update git repositories not managed by grokmirror"
---

<h2>NAME</h2>
<p> GROK-DUMB-PULL &#8211; Update git repositories not managed by grokmirror</p>
<h2>SYNOPSIS</h2>
<p> grok-dumb-pull [options] /path/to/repos</p>
<h2>DESCRIPTION</h2>
<p> This is a satellite utility that updates repositories not exported via grokmirror manifest. You will need to manually clone these repositories using &quot;git clone &#8211;mirror&quot; and then define a cronjob to update them as frequently as you require. Grok-dumb-pull will bluntly execute &quot;git remote update&quot; in each of them.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd> show program&#8217;s version number and exit</p>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd> show this help message and exit</p>
<dt><code>-v</code>,<code> &#8211;verbose</code></p>
<dd> Be verbose and tell us what you are doing</p>
<dt><code>-s</code>,<code> &#8211;svn</code></p>
<dd> The remotes for these repositories are Subversion</p>
<dt><code>-r</code><i>&nbsp;<wbr>REMOTES</i>,<code>&nbsp;<wbr>&#8211;remote-names=</code><i>REMOTES</i></p>
<dd> Only fetch remotes matching this name (accepts globbing, can be passed multiple times)</p>
<dt><code>-u</code><i>&nbsp;<wbr>POSTHOOK</i>,<code>&nbsp;<wbr>&#8211;post-update-hook=</code><i>POSTHOOK</i></p>
<dd> Run this hook after each repository is updated. Passes full path to the repository as the sole argument.</p>
<dt><code>-l</code><i>&nbsp;<wbr>LOGFILE</i>,<code>&nbsp;<wbr>&#8211;logfile=</code><i>LOGFILE</i></p>
<dd> Put debug logs into this file</dl>
<h2>EXAMPLES</h2>
<p> The following will update all bare git repositories found in /path/to/repos hourly, and /path/to/special/repo.git daily, fetching only the &quot;github&quot; remote: </p>
<pre>
MAILTO=root
# Update all repositories found in /path/to/repos hourly
0 * * * * mirror /usr/bin/grok-dumb-pull /path/to/repos
# Update /path/to/special/repo.git daily, fetching &quot;github&quot; remote
0 0 * * * mirror /usr/bin/grok-dumb-pull -r github /path/to/special/repo.git
</pre>
<p> Make sure the user &quot;mirror&quot; (or whichever user you specified) is able to write to the repos specified.</p>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/1-grok-pull/">grok-pull</a>(1)</p>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/1-grok-manifest/">grok-manifest</a>(1)</p>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/1-grok-fsck/">grok-fsck</a>(1)</p>
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

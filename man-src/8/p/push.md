---
title: "push(8)"
name: "push"
section: "8"
letter: "p"
url: "/docs/linux/man/8-push/"
description: "push – fetch mail via POP"
---

<p><code>push</code> &#8211; fetch mail via POP</p>
<h2>Synopsis</h2>
<p>[-<code>5 | &#8211;krb5</code> ] [-<code>v | &#8211;verbose</code> ] [-<code>f | &#8211;fork</code> ] [-<code>l | -leave</code> ] [-<code>-from</code> ] [-<code>c | -count</code> ] [-<code>-headers = </code><i>headers</i> ] [-<code>p </code><i>port-spec | </i> &#8211;<code>-port = </code><i>port-spec</i> ] <i>po-box</i> filename</p>
<h2>Description</h2>
<p>retrieves mail from the post office box <i>po-box</i> and stores the mail in mbox format in filename The <i>po-box</i> can have any of the following formats:</p>
<dl>
<dt><code>`hostname:username&#8217; </code></p>
<dd>
<dt><code>`po:hostname:username&#8217; </code></p>
<dd>
<dt><code>`username [at] hostname&#8217; </code></p>
<dd>
<dt><code>`po:username [at] hostname&#8217; </code></p>
<dd>
<dt><code>`hostname&#8217; </code></p>
<dd>
<dt><code>`po:username&#8217; </code></p>
<dd></dl>
<p> If no username is specified, assumes that it&#8217;s the same as on the local machine; <i>hostname</i> defaults to the value of the <code>MAILHOST</code> environment variable. </p>
<p> Supported options:</p>
<dl>
<dt> &#8211;<code>5</code> &#8211;<code>-krb5</code></p>
<dd>
<dd>use Kerberos 5 (if compiled with support for Kerberos 5)</p>
<dt> &#8211;<code>f</code> &#8211;<code>-fork</code></p>
<dd>
<dd>fork before starting to delete messages</p>
<dt> &#8211;<code>l</code> &#8211;<code>-leave</code></p>
<dd>
<dd>don&#8217;t delete fetched mail</p>
<dt> &#8211;<code>-from</code></p>
<dd>
<dd>behave like from.</p>
<dt> &#8211;<code>c</code> &#8211;<code>-count</code></p>
<dd>
<dd>first print how many messages and bytes there are.</p>
<dt> &#8211;<code>-headers = </code><i>headers</i></p>
<dd>
<dd>a list of comma-separated headers that should get printed.</p>
<dt> &#8211;<code>p </code><i>port-spec</i> &#8211;<code>-port = </code><i>port-spec</i></p>
<dd>
<dd>use this port instead of the default `kpop&#8217; or `1109&#8242;</dl>
<p> The default is to first try Kerberos 5 authentication and then, if that fails, Kerberos 4.</p>
<h2>Environment</h2>
<dl>
<dt><code>MAILHOST</code></p>
<dd>points to the post office, if no other hostname is specified.</dl>
<h2>Examples</h2>
<blockquote>
<pre>$ push cornfield:roosta ~/.emacs-mail-crash-box</pre>
</blockquote>
<p> tries to fetch mail for the user <i>roosta</i> from the post office at &#8220;cornfield&#8221; and stores the mail in ~/.emacs-mail-crash-box (you are using Gnus, aren&#8217;t you?) </p>
<blockquote>
<pre>$ push --from -5 havregryn</pre>
</blockquote>
<p> tries to fetch <code>From:</code> lines for current user at post office &#8220;havregryn&#8221; using Kerberos 5.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-from/">from</a>(1), <a href="/docs/linux/man/1-pfrom/">pfrom</a>(1), <a href="/docs/linux/man/8-movemail/">movemail</a>(8), <a href="/docs/linux/man/8-popper/">popper</a>(8)</p>
<h2>History</h2>
<p>was written while waiting for <code>movemail</code> to finish getting the mail.</p>

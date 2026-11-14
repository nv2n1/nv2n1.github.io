---
title: "megareg(1)"
name: "megareg"
section: "1"
letter: "m"
url: "/docs/linux/man/1-megareg/"
description: "megareg – Register new Mega.co.nz account"
---

<h2 class="name">NAME</h2>
<p> megareg &#8211; Register new Mega.co.nz account </p>
<h2>SYNOPSIS</h2>
<pre><code>
megareg[--scripted]-- register --email&lt;email&gt; --name&lt;realname&gt; --password&lt;password&gt;
    megareg[--scripted]-- verify&lt;state&gt;&lt;link&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<p> Registers new Mega.co.nz account. Registration is split into two steps: </p>
<dl>
<dt>
<dd> 1. </p>
<p> &#8211;register: Creates a new non-verified account</dl>
<dl>
<dt>
<dd> 2. </p>
<p> &#8211;verify: Verifies account with the link that was sent to &lt;email&gt;</dl>
<p> See example of registration below.</p>
<h2>OPTIONS</h2>
<p> &#8211;register</p>
<dl>
<dt>
<dd> Create new non-verified account.</dl>
<p> &#8211;verify &lt;state&gt; &lt;link&gt;</p>
<dl>
<dt>
<dd> Verify account previously created by megareg &#8211;register. You need to pass &lt;state&gt; that was returned from megareg &#8211;register and a verification link from the email that was sent to &lt;email&gt;.</dl>
<p> &#8211;email &lt;email&gt;</p>
<dl>
<dt>
<dd> Email serves as your new account username, that you&#8217;ll be using to sign in. </p>
<p> <code>NOTES</code>: Beware that ATM, email format is not validated by megatools.</dl>
<p> &#8211;name &lt;realname&gt;</p>
<dl>
<dt>
<dd> Your real (or fake) name.</dl>
<p> &#8211;password &lt;password&gt;</p>
<dl>
<dt>
<dd> Plaintext password. No strength checking is done, so make sure you pick a strong password yourself.</dl>
<p> &#8211;scripted</p>
<dl>
<dt>
<dd> After registration, print the command that can be used to finish the registration in a format suitable for scripting purposes.</dl>
<p> &#8211;debug [&lt;options&gt;]</p>
<dl>
<dt>
<dd> Enable debugging of various aspects of the megatools operation. You may enable multiple debugging options separated by commas. (eg. &#8211;debug api,fs) </p>
<p> Available options are: </p>
<dl>
<dt>
<dd> &bull; </p>
<p> api: Dump Mega.co.nz API calls</dl>
<dl>
<dt>
<dd> &bull; </p>
<p> fs: Dump Mega.co.nz filesystem (may require &#8211;reload to actually print something)</dl>
<dl>
<dt>
<dd> &bull; </p>
<p> cache: Dump cache contents</dl>
</dl>
<p> &#8211;version</p>
<dl>
<dt>
<dd> Show version information</dl>
<h2>EXAMPLE</h2>
<p> First create an non-verified account: </p>
<dl>
<dt>
<dd>
<pre><code>
$ megareg-- register --email your[at] email.com-- name "Your Name" --password "Your Password" Registration email was sent to test[at] megous.com.To complete registration, you must run : megareg-- verify vbFFFv7AFM25etzkFXLs9A == : Z7FFbgAAAAAAAAAArL33eA == : inEONh3tmwY @LINK @(Where @LINK @is registration link from the 'MEGA Signup' email)
</code></pre>
</dl>
<p> Now wait for a verification mail and run the command as asked: </p>
<dl>
<dt>
<dd>
<pre>
$ megareg --verify vbFFFv7AFM25etzkFXLs9A==:Z7FFbgAAAAAAAAAArL33eA==:inEONh3tmwY \
    '<a rel="nofollow" href="https://mega.co.nz/#confirmciyfWXRGFNcM...'">https://mega.co.nz/#confirmciyfWXRGFNcM...'</a>
Account registered successfully!
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-megatools/">megatools</a></code>(7), <code><a href="/docs/linux/man/5-megarc/">megarc</a></code>(5), <code><a href="/docs/linux/man/1-megadf/">megadf</a></code>(1), <code><a href="/docs/linux/man/1-megadl/">megadl</a></code>(1), <code><a href="/docs/linux/man/1-megaget/">megaget</a></code>(1), <code><a href="/docs/linux/man/1-megals/">megals</a></code>(1), <code><a href="/docs/linux/man/1-megamkdir/">megamkdir</a></code>(1), <code><a href="/docs/linux/man/1-megaput/">megaput</a></code>(1), <code><a href="/docs/linux/man/1-megareg/">megareg</a></code>(1), <code><a href="/docs/linux/man/1-megarm/">megarm</a></code>(1), <code><a href="/docs/linux/man/1-megamv/">megamv</a></code>(1), <code><a href="/docs/linux/man/1-megasync/">megasync</a></code>(1), <code><a href="/docs/linux/man/1-megafs/">megafs</a></code>(1).</p>
<h2>MEGATOOLS</h2>
<p> Part of the <code><a href="/docs/linux/man/7-megatools/">megatools</a></code>(7) suite.</p>
<h2>BUGS</h2>
<p> Report bugs at <a rel="nofollow" href="https://github.com/megous/megatools">https://github.com/megous/megatools</a> or megous [at] megous.com.</p>
<h2>AUTHOR</h2>
<p> Megatools was written by Ondrej Jirman &lt;megous [at] megous.com&gt;, 2013. </p>
<p> Official website is <a rel="nofollow" href="http://megatools.megous.com.">http://megatools.megous.com.</a> </p>
<h2>Index</h2>

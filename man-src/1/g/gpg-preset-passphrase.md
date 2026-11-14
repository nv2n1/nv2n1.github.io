---
title: "gpg-preset-passphrase(1)"
name: "gpg-preset-passphrase"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gpg-preset-passphrase/"
description: "gpg-preset-passphrase – Put a passphrase into gpg-agent’s cache"
---

<h2 class="name">NAME</h2>
<p> <code>gpg-preset-passphrase</code> &#8211; Put a passphrase into gpg-agent&#8217;s cache </p>
<h2>SYNOPSIS</h2>
<p> <code>gpg-preset-passphrase</code> [<i>options</i>] [<i>command</i>] <i>cache-id</i> </p>
<h2>DESCRIPTION</h2>
<p> The <code>gpg-preset-passphrase</code> is a utility to seed the internal cache of a running <code>gpg-agent</code> with passphrases. It is mainly useful for unattended machines, where the usual <code>pinentry</code> tool may not be used and the passphrases for the to be used keys are given at machine startup. </p>
<p> This program works with GnuPG 2 and later. GnuPG 1.x is not supported. </p>
<p> Passphrases set with this utility don&#8217;t expire unless the <code>&#8211;forget</code> option is used to explicitly clear them from the cache &#8212; or <code>gpg-agent</code> is either restarted or reloaded (by sending a SIGHUP to it). Note that the maximum cache time as set with <code>&#8211;max-cache-ttl</code> is still honored. It is necessary to allow this passphrase presetting by starting <code>gpg-agent</code> with the <code>&#8211;allow-preset-passphrase</code>. </p>
<p> <code>gpg-preset-passphrase</code> is invoked this way: </p>
<dl>
<dt>
<dd>
<pre><code>
gpg - preset - passphrase[options][command] cacheid
</code></pre>
</dl>
<p> <i>cacheid</i> is either a 40 character keygrip of hexadecimal characters identifying the key for which the passphrase should be set or cleared. The keygrip is listed along with the key when running the command: <code>gpgsm &#8211;with-keygrip &#8211;list-secret-keys</code>. Alternatively an arbitrary string may be used to identify a passphrase; it is suggested that such a string is prefixed with the name of the application (e.g <code>foo:12346</code>). Scripts should always use the option <code>&#8211;with-colons</code>, which provides the keygrip in a &quot;grp&quot; line (cf. &#8216;<i>doc/DETAILS</i>&#8216;)/ </p>
<p> One of the following command options must be given: </p>
<dl>
<dt><code>&#8211;preset</code></p>
<dd> Preset a passphrase. This is what you usually will use. <code>gpg-preset-passphrase</code> will then read the passphrase from <code>stdin</code>. </p>
<dt><code>&#8211;forget</code></p>
<dd> Flush the passphrase for the given cache ID from the cache. </p>
</dl>
<p> The following additional options may be used: </p>
<dl>
<dt><code>-v</code></p>
<dd> <code>&#8211;verbose</code> Output additional information while running. </p>
<dt><code>-P </code><i>string</i></p>
<dd> <code>&#8211;passphrase </code><i>string</i> Instead of reading the passphrase from <code>stdin</code>, use the supplied <i>string</i> as passphrase. Note that this makes the passphrase visible for other users.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gpg/">gpg</a></code>(1), <code><a href="/docs/linux/man/1-gpgsm/">gpgsm</a></code>(1), <code><a href="/docs/linux/man/1-gpg-agent/">gpg-agent</a></code>(1), <code><a href="/docs/linux/man/1-scdaemon/">scdaemon</a></code>(1) </p>
<p> The full documentation for this tool is maintained as a Texinfo manual. If GnuPG and the info program are properly installed at your site, the command </p>
<dl>
<dt>
<dd>
<pre>
info gnupg
</pre>
</dl>
<p> should give you access to the complete manual including a menu structure and an index. </p>
<h2>Index</h2>

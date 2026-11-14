---
title: "plowshare-conf(5)"
name: "plowshare-conf"
section: "5"
letter: "p"
url: "/docs/linux/man/5-plowshare-conf/"
description: "plowshare.conf – Configuration file for Plowshare"
---

<p>plowshare.conf &#8211; Configuration file for Plowshare</p>
<h2>Description</h2>
<p><code>Plowshare</code> (plowdown, plowup, plowdel, plowlist or plowprobe) uses a configuration file called <i>plowshare.conf</i> for its initial setup. This configuration file is searched for in the following places when plowshare is started:</p>
<dl>
<dd>
<pre><i>~/.config/plowshare/plowshare.conf</i>
<i>/etc/plowshare.conf</i></pre>
</dl>
<p> Note: Usage of configuration file can be disabled using <code>&#8211;no-plowsharerc</code> command-line option. There is also <code>&#8211;plowsharerc=</code><i>FILE</i> option to specify an alternate configuration file. </p>
<h2>File Format</h2>
<p><i>plowshare.conf</i> file uses an INI-style format. It is composed of six sections which may be present in any order. Each section may contain lines of the form: </p>
<dl>
<dd>
<pre><code>[General]</code>
 <i>token</i> <i>=</i> <i>value</i>
 ...
<code>[Plowdown]</code>
 <i>token</i> <i>=</i> <i>value</i>
 ...
<code>[Plowup]</code>
 <i>token</i> <i>=</i> <i>value</i>
 ...
<code>[Plowdel]</code>
 <i>token</i> <i>=</i> <i>value</i>
 ...
<code>[Plowlist]</code>
 <i>token</i> <i>=</i> <i>value</i>
 ...
<code>[Plowprobe]</code>
 <i>token</i> <i>=</i> <i>value</i>
 ...
<code># this is a comment</code></pre>
</dl>
<p> Notes:</p>
<dl>
<dt>&bull;</p>
<dd>Sections are unordered.</p>
<dt>&bull;</p>
<dd>Blank lines or lines beginning with a hash character (&#8216;#&#8217;) are treated as comments and ignored.</p>
<dt>&bull;</p>
<dd>Whitespace before and after a <i>token</i> or <i>value</i> is ignored (although a <i>value</i> can contain whitespace within).</p>
<dt>&bull;</p>
<dd>Double quoting <i>value</i> is optional. Use them to preserve leading and trailing whitespace.</dl>
<p> Valid tokens are always lowercase. Names are long-option command-line arguments of plowshare. For example: <i>temp-directory</i> for plowdown. For modules options, tokens are prepended by module name and a slash character. For example: <i>rapidgator/auth</i> (short-option are also possible here). </p>
<p> For values, no backslash interpretation is made. &quot;	&quot; is a regular string with two characters, it is not a tab character. </p>
<p> Options in general section prevail over Plow* section. Options given on the command line prevail over configuration file options.</p>
<h2>Example</h2>
<p>### ### Plowshare configuration file ###  [Plowdown] deathbycaptcha=matt:blablabla timeout=3600 [Plowup] max-retries=2 printf=Download URL: %u%nDelete URL: %d%n mirrorcreator/auth-free = foo:bar mirrorcreator/mediafire = yes [Plowlist] verbose = 3 </p>
<h2>Authors</h2>
<p>Plowshare was initially written by Arnau Sanchez. See the AUTHORS file for a list of some of the many other contributors. </p>
<p> Plowshare is (C) 2010-2014 The Plowshare Team</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-plowdown/">plowdown</a></code>(1), <code><a href="/docs/linux/man/1-plowup/">plowup</a></code>(1), <code><a href="/docs/linux/man/1-plowdel/">plowdel</a></code>(1), <code><a href="/docs/linux/man/1-plowlist/">plowlist</a></code>(1), <code><a href="/docs/linux/man/1-plowprobe/">plowprobe</a></code>(1). </p>

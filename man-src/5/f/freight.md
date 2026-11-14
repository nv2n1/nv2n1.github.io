---
title: "freight(5)"
name: "freight"
section: "5"
letter: "f"
url: "/docs/linux/man/5-freight/"
description: "freight – Freight configuration"
---

<p><code>freight</code> &#8211; Freight configuration</p>
<h2>Description</h2>
<p>The Freight configuration is a <code>source</code>d shell script that defines a few important variables.</p>
<h2>Options</h2>
<dl>
<dt><code>VARLIB</code></p>
<dd>The Freight library directory. Typically <i>/var/lib/freight</i>.</p>
<dt><code>VARCACHE</code></p>
<dd>The Freight cache directory. Typically <i>/var/cache/freight</i>. This should be the document root of the web server.</p>
<dt><code>ARCHS</code></p>
<dd>The architectures to support. Typically <i>i386 amd64</i>.</p>
<dt><code>ORIGIN</code></p>
<dd>The <code>Origin</code> field in the Debian archive.</p>
<dt><code>LABEL</code></p>
<dd>The <code>Label</code> field in the Debian archive.</p>
<dt><code>CACHE</code></p>
<dd><i>on</i> to cache package control files or <i>off</i> to read them from the packages on each <code><a href="/docs/linux/man/1-freight-cache/">freight-cache</a></code>(1) run.</p>
<dt><code>GPG</code></p>
<dd>The GPG key(s) to use. This value must be set either in a configuration file or by using the <code>-g</code> option to <code><a href="/docs/linux/man/1-freight-cache/">freight-cache</a></code>(1). Multiple keys can be given to sign the repository with more signatures.</p>
<dt><code>GPG_PASSPHRASE_FILE</code></p>
<dd>Pathname of a file containing the GPGP private key&#8217;s passphrase. This sets the <code>&#8211;passphrase-fd</code> and <code>&#8211;passphrase-file</code> options to <code><a href="/docs/linux/man/1-gpg/">gpg</a></code>(1). The passphrase file can be set either in a configuration file or by using the <code>-p</code> option to <code><a href="/docs/linux/man/1-freight-cache/">freight-cache</a></code>(1).</p>
<dt><code>GPG_DIGEST_ALGO</code></p>
<dd>Message digest algorithm that GPG should use to sign the repository. Apt is phasing out SHA1 so it is recommended to use SHA512 for most use-cases. This sets the <code>&#8211;personal-digest-preferences</code> option to <code><a href="/docs/linux/man/1-gpg/">gpg</a></code>(1). The digest algorithm can be set either in a configuration file or by using the <code>-a</code> option to <code><a href="/docs/linux/man/1-freight-cache/">freight-cache</a></code>(1).</p>
<dt><code>SYMLINKS</code></p>
<dd><i>on</i> to follow symbolic links in <code>VARLIB</code> to produce extra components in the cache directory or <i>off</i> to offer no special treatment.</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/freight.conf</i></p>
<dd>The default configuration file.</p>
<dt><i>~/.freight.conf</i></p>
<dd>User-specific configuration file.</p>
<dt><i>etc/freight.conf</i>, <i>.freight.conf</i></p>
<dd>Directory-specific configuration files.</dl>
<h2>Environment Variables</h2>
<dl>
<dt><code>FREIGHT_CONF</code></p>
<dd>The pathname of an alternate configuration file.</dl>
<h2>Theme Song</h2>
<p>The New Pornographers &#8211; &quot;All the Old Showstoppers&quot;</p>
<h2>Author</h2>
<p>Richard Crowley <i>r@rcrowley.org</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-freight-add/">freight-add</a></code>(1) adds packages to the intermediate &quot;Freight library&quot; that is used by <code><a href="/docs/linux/man/1-freight-cache/">freight-cache</a></code>(1) to build the actual repositories. <code><a href="/docs/linux/man/1-reprepro/">reprepro</a></code>(1) manages Debian archives, too, if Freight isn&#8217;t your thing. </p>

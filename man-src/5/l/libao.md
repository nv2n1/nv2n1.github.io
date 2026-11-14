---
title: "libao(5)"
name: "libao"
section: "5"
letter: "l"
url: "/docs/linux/man/5-libao/"
description: "libao.conf – configuration for libao."
---

<p>libao.conf &#8211; configuration for libao.</p>
<h2>Synopsis</h2>
<p><code>/etc/libao.conf</code> <code>~/.libao</code> </p>
<h2>Description</h2>
<p><code>libao.conf</code> and <code>.libao</code> are configuration files for libao, the audio output library. They specify various options to libao, as described below. <code>libao.conf</code> sets system-wide options, whereas <code>~/.libao</code> sets user-specific options. When an option is set in both places, the option in <code>~/.libao</code> takes precedence. </p>
<h2>File Format</h2>
<p>The file consists of comments and key-value pairs. Comments are on separate lines that start with a <code>#</code> symbol. The key-value pairs are of the form:</p>
<dl>
<dd><code>key=value</code></dl>
<p> where <code>key</code> contains no whitespace and no equal signs. <code>value</code> will be all of the text after the equal sign until (but not including) the ending newline. Beware of extra spaces at the end of the line! They will probably be interpreted as part of the option value. </p>
<p> The following is a list of valid global option keys. Any driver specific option may be used as well as those keys.</p>
<dl>
<dd>
<dl>
<dt>default_driver</p>
<dd>The short name of the driver libao should use by default. Valid values include (not all are available on every platform): oss, esd, arts, alsa, nas, irix, sun, roar and sndio. Note that &quot;sun&quot; is used on many BSD systems as well as Solaris.</p>
<dt>debug (Value optional/ignored)</p>
<dd>Sets all the drivers as well as AO itself into debugging output mode. Unlike passing the debug option to a driver, debug will also print debugging information from driver loading and testing.</p>
<dt>quiet (Value optional/ignored)</p>
<dd>Sets all the drivers as well as AO itself into silent mode. Errors will return only error codes; neither ao nor the drivers will print any output whatsoever to stderr.</p>
<dt>verbose (Value optional/ignored)</p>
<dd>Sets all the drivers as well as AO itself into verbose mode.</dl>
</dl>
<h2>Example</h2>
<p>Here is an example <code>libao.conf</code> that forces the OSS driver to be used by default: </p>
<pre><code># This is a comment.

default_driver=oss
</code></pre>
<h2>Bugs</h2>
<p><code>libao.conf</code> is missing a number of potentially useful options. </p>
<h2>Authors</h2>
<p>Stan Seibert &lt;volsung [at] xiph.org&gt;</p>

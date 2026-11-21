---

title: "freight-init(1)"
name: "freight-init"
section: "1"
letter: "f"
url: "/docs/linux/man/1-freight-init/"
description: "freight-init – initialize a Freight directory"
---

<h2>NAME</h2>
<p> <code>freight-init</code> &#8211; initialize a Freight directory</p>
<p> <code>freight init</code> [<code>&#8211;libdir</code> <i>varlib</i>] [<code>&#8211;cachedir</code> <i>varcache</i>] [<code>&#8211;archs</code> <i>archs</i>] [<code>&#8211;origin</code> <i>origin</i>] [<code>&#8211;label</code> <i>label</i>] [<code>-v</code>] [<code>-h</code>] <code>-g</code> <i>gpg</i> <i>dirname</i></p>
<p> <code>freight-init</code> will setup a directory to be used by Freight. It will generate small wrappers around the original Freight commands. Use <code><a href="/docs/linux/man/1-freight-add/">freight-add</a></code>(1) and <code><a href="/docs/linux/man/1-freight-cache/">freight-cache</a></code>(1) to work against the <code>VARLIB</code> and <code>VARCACHE</code> given to <code>freight init</code>. </p>
<p> The benefit of using <code>freight-init</code> is to automate the setup of Freight and to configure all data to be stored in one directory. </p>
<p> Configuration is stored in <i>dirname</i><code>/etc/freight.conf</code>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-g</code> <i>gpg</i>, <code>&#8211;gpg=</code><i>gpg</i></dt>
<dd> GPG key. May be given multiple times.</dd>
<dt><code>&#8211;libdir=</code><i>varlib</i></dt>
<dd> VARLIB directory to use. Defaults to <i>dirname</i><code>/var/lib</code></dd>
<dt><code>&#8211;cachedir=</code><i>varcache</i></dt>
<dd> VARCACHE directory to use. Defaults to <i>dirname</i><code>/var/cache</code></dd>
<dt><code>&#8211;archs=</code><i>archs</i></dt>
<dd> Architectures to generate archives for. Defaults to <code>i386 amd64</code></dd>
<dt><code>&#8211;origin=</code><i>origin</i></dt>
<dd> Debian archive Origin field value. Defaults to <code>Freight</code></dd>
<dt><code>&#8211;label=</code><i>label</i></dt>
<dd> Debian archive Label field value. Defaults to <code>Freight</code></dd>
<dt><code>&#8211;suite=</code><i>suite</i></dt>
<dd> Debian archive Suite field value.</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> Verbose mode.</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Show a help message.</dd></dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/freight.conf</i>, <i>~/.freight.conf</i>, <i>etc/freight.conf</i>, <i>.freight.conf</i></dt>
<dd> The default configuration files. See <code><a href="/docs/linux/man/5-freight/">freight</a></code>(5).</dd></dl>
<h2>THEME SONG</h2>
<p> The New Pornographers &#8211; &quot;All the Old Showstoppers&quot;</p>
<h2>AUTHOR</h2>
<p> Jens Braeuer <i>braeuer.jens [at] googlemail.com</i></p>
<h2>SEE ALSO</h2>
<p> Part of <code><a href="/docs/linux/man/1-freight/">freight</a></code>(1). </p>

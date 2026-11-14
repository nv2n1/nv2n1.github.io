---
title: "pungi(8)"
name: "pungi"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pungi/"
description: "pungi – anaconda-based installation spin tool"
---

<p>pungi &#8211; anaconda-based installation spin tool</p>
<h2>Synopsis</h2>
<p><code>pungi</code> [options]</p>
<h2>Description</h2>
<p><code>pungi</code> is a tool to create anaconda-based installation trees or media images given a set of RPM packages. </p>
<h2>Options</h2>
<p><code>pungi</code> is entirely command line oriented. All input to the program is given by command line options. </p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd>Display a help message and then quit.</p>
<dt><code>&#8211;version</code></p>
<dd>Display program&#8217;s version number and then quit.</p>
<dt><code>&#8211;name=string</code></p>
<dd>Set the name for your distribution (defaults to &quot;Fedora&quot;).</p>
<dt><code>&#8211;ver=string</code></p>
<dd>Set the version for your distribution (defaults to datestamp, used for $releasever in yum).</p>
<dt><code>&#8211;flavor=string</code></p>
<dd>Set the flavor of your spin (optional).</p>
<dt><code>&#8211;destdir=pathspec</code></p>
<dd>Path specifying the destination directory (defaults to current directory).</p>
<dt><code>&#8211;cachedir=pathspec</code></p>
<dd>Package cache directory (defaults to /var/cache/pungi).</p>
<dt><code>&#8211;bugurl=urlspec</code></p>
<dd>The URL for your bug reporting system (defaults to <a rel="nofollow" href="http://bugzilla.redhat.com">http://bugzilla.redhat.com</a>).</p>
<dt><code>&#8211;discs=integer</code></p>
<dd>The number of discs you want to create (defaults to 1).</p>
<dt><code>&#8211;nosource</code></p>
<dd>Disable gathering of source packages (optional).</p>
<dt><code>&#8211;sourceisos</code></p>
<dd>Create the source media images (other arch runs must be done).</p>
<dt><code>&#8211;force</code></p>
<dd>Force reuse of an existing destination directory (will overwrite files).</p>
<dt><code>-c ksfile, &#8211;config=ksfile</code></p>
<dd>Path to kickstart configuration file.</p>
<dt><code>&#8211;all-stages</code></p>
<dd>Enable ALL stages.</p>
<dt><code>-G</code></p>
<dd>Enable the Gather stage.</p>
<dt><code>-C</code></p>
<dd>Enable the Createrepo stage.</p>
<dt><code>-B</code></p>
<dd>Enable the BuildInstall stage.</p>
<dt><code>-I</code></p>
<dd>Enable the CreateISO stage. </p>
</dl>
<h2>Examples</h2>
<pre>pungi -c /usr/share/pungi/f8-fedora.ks --destdir=/data/Fedora8 --name Fedora --ver 8</pre>
<h2>See Also</h2>
<pre><a rel="nofollow" href="http://fedoraproject.org/wiki/Releases/FeatureUsePungi">http://fedoraproject.org/wiki/Releases/FeatureUsePungi</a>
<a rel="nofollow" href="https://hosted.fedoraproject.org/projects/pungi/">https://hosted.fedoraproject.org/projects/pungi/</a></pre>
<h2>Authors</h2>
<pre>See the Authors file included with this program.</pre>
<h2>Bugs</h2>
<p>No bugs were harmed in the making of this software. </p>

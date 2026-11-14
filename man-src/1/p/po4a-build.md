---
title: "po4a-build(1)"
name: "po4a-build"
section: "1"
letter: "p"
url: "/docs/linux/man/1-po4a-build/"
description: "po4a-build – build translated documentation"
---

<h2 class="name">NAME</h2>
<p> po4a-build &#8211; build translated documentation </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>po4a-build</code> [<code>-f</code> | <code>&#8211;file</code><i> FILE</i>] [<code>&#8211;pot-only</code>]</p>
<dt> <code>po4a-build</code> [<code>-?</code> | <code>-h</code> | <code>&#8211;help</code> | <code>&#8211;version</code>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>po4a-build</code></p>
<dd>is intended to make it as easy to produce translated documentation as it can be to produce the current untranslated content. </p>
<p> When <code>po4a</code> prepares the translated content as POD or DocBook XML, the final documentation can then be built using <code>po4a-build</code>. Both the untranslated and translated content is built as a single process, updating the POT files at the same time. </p>
<p> Existing build instructions are replaced by a single call to <code>po4a-build</code> and a simple configuration file is used to tell <code>po4a-build</code> how to build each element and which binary packages will include the translated and untranslated content. </p>
<p> Once built, the content will be in package-specific directories beneath the <code>BASEDIR</code> specified in the configuration file. For a binary package foo, with translations into German and French, this would result in: </p>
<dl>
<dt>
<dd>
<pre>
BASEDIR/foo/man/man1/foo.1
BASEDIR/foo/man/de/man1/foo.1
BASEDIR/foo/man/fr/man1/foo.1
    
</pre>
</dl>
<p> This makes it easy to include all the generated content into the binary package with a single install location: </p>
<dl>
<dt>
<dd>
<pre>
doc/foo/man/* ./usr/share/man/
doc/foo/html/* ./usr/share/doc/foo/
    
</pre>
</dl>
<p> This rule will not need to be updated when new translations are added and adding a second binary package (bar) allows the content for that package to kept separate.</p>
<h3>Supported formats</h3>
<p> Currently, <code>po4a-build</code> supports the following combinations: </p>
<dl>
<dt>
<dd> 1. DocBook XML for section 1.</dl>
<dl>
<dt>
<dd> 2. DocBook XML for section 3.</dl>
<dl>
<dt>
<dd> 3. DocBook XML for HTML.</dl>
<dl>
<dt>
<dd> 4. POD for section 1.</dl>
<dl>
<dt>
<dd> 5. POD for section 3.</dl>
<dl>
<dt>
<dd> 6. POD for section 5.</dl>
<dl>
<dt>
<dd> 7. POD for section 7.</dl>
<p> All supported formats, in all supported combinations, can be handled in a single po4a-build.conf configuration file and in a single call to <code>po4a-build</code>. See <code><a href="/docs/linux/man/5-po4a-build-conf/">po4a-build.conf</a></code>(5).</p>
<h2>CONFIGURATION</h2>
<p> <code>po4a-build</code> uses a default configuration file, po4a-build.conf which should be in the top level directory of your package VCS. (Use the <code>-f</code> option to specify a different file.) See <code><a href="/docs/linux/man/5-po4a-build-conf/">po4a-build.conf</a></code>(5). </p>
<p> <code>Example 1. example configuration file</code> </p>
<p> An example configuration file is available at: </p>
<dl>
<dt>
<dd>
<pre>
/usr/share/doc/po4a/examples/po4a-build.conf.example
    
</pre>
</dl>
<h3>configuration file layout</h3>
<p> The configuration file consists of several sections, general, XML/XSL support, POD support and HTML support. </p>
<p> General includes the name and location of the po4a config file (probably best to leave this as po4a.config), the po directory containing the documentation PO files (often doc/po), the full name of the POT file used to create the translations, the BASEDIR for the generated output, whether the package contains manpages in section 3 rather than just section 1 and the names of the binary packages which are to contain the generated output. </p>
<p> XML/XSL support includes specifying which of the binary packages use XSL support in the XMLPACKAGES variable, the top level DocBook file to pass to <code>xsltproc</code> and the location of the XML or DocBook files. The XSLFILE can be overridden, if necessary. </p>
<p> POD support includes specifying which of the binary packages use POD support in the PODPACKAGES variable and the full name of the POD file. </p>
<p> HTML support specifies the subdirectory to create below BASEDIR for the untranslated and translated HTML content and the DocBook file to generate the HTML. The HTMLXSL file can be overridden, if necessary.</p>
<h2>COMMANDS</h2>
<p> <code>&#8211;pot-only</code></p>
<dl>
<dt>
<dd> Only updates the POT file(s). <code>&#8211;pot-only</code> is intended to support packages including all POT files in the package source. Packages using Autotools can easily add the POT file via EXTRA_DIST but packages just using a Makefile or certain VCS build helpers can find it awkward to add the POT file (which is a generated file) without putting the POT file into the VCS. To avoid this ugly and unnecessary work, <code>po4a-build</code> can update the POT file(s) at the start of the build, so that <code>dpkg-source</code> includes them into the source tarball. </p>
<p> <code>Example 2. svn-buildpackage example</code> </p>
<p> <code>svn-buildpackage</code> has explicit support for this kind of addition, using the <code>useNativeDist</code> SVN property and the <code>native-dist</code> Make target. </p>
<dl>
<dt>
<dd>
<pre>
# adds the POT file to the source tarball
native-dist: Makefile
        po4a-build --pot-only
            
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
$ svn propset useNativeDist 1 debian
            
</pre>
</dl>
</dl>
<p> <code>-h</code>|<code>&#8211;help</code></p>
<dl>
<dt>
<dd> print the usage message and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> print the usage message and exit.</dl>
<h2>OPTIONS</h2>
<p> <code>-f</code>|<code>&#8211;file</code><i> FILE</i></p>
<dl>
<dt>
<dd> Override the <code>po4a-build</code> default configuration file (po4a-build.conf) and supply your own.</dl>
<h2>AUTHOR</h2>
<p> <code>po4a-build</code> was written by Neil Williams &lt;codehelp [at] debian.org&gt;. </p>
<p> This manual page was written by Neil Williams &lt;codehelp [at] debian.org&gt; </p>
<h2>Index</h2>

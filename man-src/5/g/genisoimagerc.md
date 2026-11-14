---
title: "genisoimagerc(5)"
name: "genisoimagerc"
section: "5"
letter: "g"
url: "/docs/linux/man/5-genisoimagerc/"
description: "genisoimagerc – startup configuration file for genisoimage"
---

<p>genisoimagerc &#8211; startup configuration file for genisoimage</p>
<h2>Description</h2>
<p><code><a href="/docs/linux/man/1-genisoimage/">genisoimage</a></code>(1) searches for a configuration file in several places; it uses the first one it is able to open. First, if the <code>GENISOIMAGERC</code> environment variable is set, its value is used as the filename; likewise for the <code>MKISOFSRC</code> environment variable. Next, <code>genisoimage</code> looks for files named <i>.genisoimagerc</i> or <i>.mkisofsrc</i>, first in the current working directory, then in the user&#8217;s home directory. Next, it looks for <i>/etc/genisoimagerc</i>. Finally, it looks for a <i>.genisoimagerc</i> in the same directory as <code>genisoimage</code> itself is stored. </p>
<p> The <i>.genisoimagerc</i> file contains lines of the form</p>
<dl>
<dd><code>TAG=</code><i>value</i></dl>
<p> where <code>TAG</code> is one of the settings defined below. The case of the tag is not significant. All settings have command-line equivalents; if the command-line parameter is specified, it takes priority over the configuration file. </p>
<p> Blank lines and lines beginning with `#&#8217; are ignored.</p>
<h2>Configuration Settings</h2>
<dl>
<dt>ABST</p>
<dd>The abstract information, typically the name of a file on the disc containing an abstract. There is space for 37 characters. Equivalent to the <code>-abstract</code> command-line option.</p>
<dt>APPI</p>
<dd>The application identifier should describe the application that will be on the disc. There is space for 128 characters. Equivalent to the <code>-A</code> command-line option.</p>
<dt>BIBL</p>
<dd>The bibliographic information, often the name of a file on the disc containing a bibliography. There is space for 37 characters. Equivalent to the <code>-biblio</code> command-line option.</p>
<dt>COPY</p>
<dd>The copyright information, typically the name of a file on the disc containing the copyright notice. There is space for 37 characters. Equivalent to the <code>-copyright</code> command-line option.</p>
<dt>HFS_TYPE</p>
<dd>The default <code>TYPE</code> for Macintosh files. Must be exactly 4 characters. Equivalent to the <code>-hfs-type</code> command-line option. The default value is <i>TEXT</i>.</p>
<dt>HFS_CREATOR</p>
<dd>The default <code>CREATOR</code> for Macintosh files. Must be exactly 4 characters. Equivalent to the <code>-hfs-creator</code> command-line option. The default value is <i>Unix</i>.</p>
<dt>PREP</p>
<dd>This should describe the preparer of the CD-ROM, usually with a mailing address and phone number. There is space for 128 characters. Equivalent to the <code>-p</code> command-line option.</p>
<dt>PUBL</p>
<dd>This should describe the publisher of the CD-ROM, usually with a mailing address and phone number. There is space for 128 characters. Equivalent to the <code>-publisher</code> command-line option.</p>
<dt>SYSI</p>
<dd>The System Identifier. There is space for 32 characters. Equivalent to the <code>-sysid</code> command-line option.</p>
<dt>VOLI</p>
<dd>The Volume Identifier. There is space for 32 characters. Equivalent to the <code>-V</code> command-line option.</p>
<dt>VOLS</p>
<dd>The Volume Set Name. There is space for 128 characters. Equivalent to the <code>-volset</code> command-line option.</dl>
<p> <code>genisoimage</code> can also be configured at compile time with defaults for many of these fields. See the file <i>defaults.h</i>.</p>
<h2>Examples</h2>
<p>The following file</p>
<dl>
<dd>
<pre>COPY=src/COPYING
SYSI=Multics 75</pre>
</dl>
<p> is equivalent to the <code>genisoimage</code> command-line parameters</p>
<dl>
<dd><i>-copyright src/COPYING -sysid &quot;Multics 75&quot;</i></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-genisoimage/">genisoimage</a></code>(1).</p>
<h2>Authors</h2>
<p>See the <code><a href="/docs/linux/man/1-genisoimage/">genisoimage</a></code>(1) manual page for credits for the <code>genisoimage</code> program and documentation.</p>

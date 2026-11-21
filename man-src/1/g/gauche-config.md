---

title: "gauche-config(1)"
name: "gauche-config"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gauche-config/"
description: "gauche-config – retrieve configuration parameters of Gauche"
---

<p> <code>gauche-config</code> <i>option</i> </p>
<p> <i>Gauche-config </i> displays various parameters specified at the configuration time of the Gauche Scheme implementation. It can be used in Makefile and other configuration scripts that uses Gauche. </p>
<h2>OPTIONS</h2>
<h3>General parameters</h3>
<dl>
<dt><code>-V</code></dt>
<dd> Gauche version.</dd>
<dt><code>&#8211;reconfigure</code></dt>
<dd> Prints the command line used to configure the current Gauche installation. </dd>
</dl>
<h3>Parameters to compile an application using Gauche</h3>
<dl>
<dt><code>-I, -L, -l</code></dt>
<dd> List of &quot;-I&quot; options (include directories), &quot;-L&quot; options (library directories), and &quot;-l&quot; options (libraries) for the compiler which are required to compile applications that links Gauche library.</dd>
<dt><code>&#8211;cc</code></dt>
<dd> Name of the compiler used to compile the current installation.</dd>
<dt><code>&#8211;ac</code></dt>
<dd> Directory name that contains Gauche specific autoconf macro.</dd>
<dt><code>&#8211;arch</code></dt>
<dd> The architecture signature, which is used in the pathname of architecture-dependent files, e.g. &quot;i686-pc-linux-gnu&quot;. </dd>
</dl>
<h3>Parameters to install files</h3>
<dl>
<dt><code>&#8211;syslibdir, &#8211;sitelibdir</code></dt>
<dd> Directories where system/site scheme files go.</dd>
<dt><code>&#8211;sysarchdir, &#8211;sitearchdir</code></dt>
<dd> Directories where architecture-dependent system/site files go.</dd>
<dt><code>&#8211;sysincdir, &#8211;siteincdir</code></dt>
<dd> Directories where system/site header files of extensions go.</dd>
<dt><code>&#8211;mandir, &#8211;infodir</code></dt>
<dd> Directories where gauche manpage and info docs are installed. </dd>
</dl>
<h2>Parameters to compile Gauche extention</h2>
<dl>
<dt><code>&#8211;so-suffix</code></dt>
<dd> Object file suffix of the gauche extension.</dd>
<dt><code>&#8211;so-cflags</code></dt>
<dd> Flags required to compile shared object.</dd>
<dt><code>&#8211;so-ldflags</code></dt>
<dd> Flags required to link a gauche extension.</dd>
<dt><code>&#8211;so-libs</code></dt>
<dd> Libraries to be linked with a gauche extension.</dd>
<dt><code>&#8211;dylib-suffix</code></dt>
<dd> Dynamic/shared library file suffix of the system.</dd>
<dt><code>&#8211;dylib-ldflags</code></dt>
<dd> Flags required to link dynamic/shared library file.</dd>
<dt><code>&#8211;libgauche-so</code></dt>
<dd> The name of shared library of libgauche. </dd>
</dl>
<h2>AUTHORS</h2>
<p> Shiro Kawai (shiro @ acm . org) </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gosh/">gosh</a>(1) </p>
<p> Gauche Scheme interpreter:<br />
 <a rel="nofollow" href="http://practical-scheme.net/gauche/">http://practical-scheme.net/gauche/</a> </p>

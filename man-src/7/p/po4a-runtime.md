---
title: "po4a-runtime(7)"
name: "po4a-runtime"
section: "7"
letter: "p"
url: "/docs/linux/man/7-po4a-runtime/"
---

po4a-runtime - po4a and runtime gettext translation without Autotools

<h2>Introduction</h2>

With <i>po4a-build</i>, <i>po4a</i> also includes support for adding translation of runtime script output messages using gettext but without requiring the package to adopt Autotools and the typical <i>./configure</i> process. 

 Using example <i>Makefile</i> snippets, packages can harness <i>intltool</i> with minimal effort.

<h2>Layout</h2>

Documentation translation should <font SIZE="-1">NOT</font> use the same <i>po/</i> directory as the runtime translation. Whilst runtime translation can use directories other than <i>po/</i>, it is usually easiest to go with the convention.

<h2>Multiple languages</h2>

Just a word on packages that use scripts in multiple programming languages. A common mix is Perl and shell. Note bene: gettext <font SIZE="-1">WILL</font> get confused and omit strings from one or other language unless file extensions are used for whichever is the least problematic language. 

 When using multiple languages, experiment with various settings in <i>po/Makevars</i> until you get all the strings you need in the <font SIZE="-1">POT</font> file. 

 In particular, specifying two languages in <i>po/Makevars</i> can be problematic. Instead of: 

 <pre> # Don't do this:
 XGETTEXT_OPTIONS = -L Perl -L Shell --from-code=iso-8859-1</pre>Consider renaming (or providing symlink(s) for) all files for one of the languages involved and omitting the explicit -L options. The file extension only needs to exist during the time that <i>po/POTFILES.in</i> is being processed. 

 The --keywords option can also be useful - see the xgettext documentation.

<h2>Populating po/</h2>

So, create your top level <i>po/</i> directory and then use the example files in <i>/usr/share/doc/po4a/examples/</i> to populate it.
<dl><dt><font SIZE="-1">LINGUAS</font>
<dd>Must exist, even if empty. Consists of a list of translations - each line not starting with a '#' must match an existing <font SIZE="-1">PO</font> file. e.g. if <i></i><font SIZE="-1"><i>LINGUAS</i></font><i></i> contains a single line, 'fr', an <i>fr.po</i> file must exist alongside the <i></i><font SIZE="-1"><i>LINGUAS</i></font><i></i> file. 

 <pre> $ cat po/LINGUAS
 cs
 de
 fr
 $</pre>By convention, the <i></i><font SIZE="-1"><i>LINGUAS</i></font><i></i> file is sorted alphabetically but that is a manual process.
<dt><font SIZE="-1">POTFILES</font>.in
<dd>The list of files containing the messages that need to be translated at runtime - i.e. your scripts. If you've used the top level <i>po/</i> directory, the paths should be relative to the top level directory, not the <i>po/</i> directory itself. 

 <pre> $ ls -l
 myscript.pl
 another.pl
 foo/support.pl
 po/
 po/POTFILES.in
 $ cat po/POTFILES.in
 myscript.pl
 another.pl
 foo/support.pl
 $</pre>Note that it is explicitly supported that the scripts themselves can contain strings for both runtime and documentation translation, e.g. using gettext functions for runtime and embedded <font SIZE="-1">POD</font> content for documentation. So it is not a problem to have the same file listed in <i>po/POTFILES.in</i> and <i>doc/po4a-build.conf</i>
<dt>Makevars-perl.example
<dd>If your scripts are in Perl, copy this example file as <i>po/Makevars</i> and edit it to suit.
<dt>Makevars-shell.example
<dd>If your scripts are in shell, copy this example file as <i>po/Makevars</i> and edit it to suit.
<dt>po4a-build.make
<dd>Copy this example file as <i>po/Makefile</i> - it shouldn't need editing but you may want to keep it updated against <i>/usr/share/doc/po4a/examples/po4a-build.make</i> as it may need to be updated within po4a releases as the underlying intltool support changes. (The file itself was generated from another project using Autotools and intltool.)</dl>

<h2>Building</h2>

These snippets need to be added to your top level Makefile or whatever other method you use to prepare your sources for distribution. 

 <pre> clean:
 $(MAKE) -C po/ clean
 install:
 $(MAKE) -C po/ install DESTDIR=$(DESTDIR)
 dist:
 $(MAKE) -C po/ pot</pre>(In an Autotools project, this would happen automatically by simply adding <i>po</i> to the <tt>&quot;SUBDIRS&quot;</tt> value in <i>Makefile.am</i>.)

<h2>Maintenance</h2>

Runtime translation isn't quite as easy as <i>po4a-build</i> in that adding a new translation does require editing <i>po/LINGUAS</i>, but apart from that, updating translations is merely a case of replacing the relevant <font SIZE="-1">PO</font> file with the new version. 

 Depending on how you prepare your source tarball, you may also need to list new <font SIZE="-1">PO</font> files in the <i></i><font SIZE="-1"><i>MANIFEST</i></font><i></i> file or add to the script(s) that prepare the tarball. (That also applies to <i>po4a-build</i>.) 

 Any <i>*.mo</i> or <i>*.gmo</i> files in <i>po/</i> can be deleted / cleaned up.

<h2>Copyright</h2>

Whilst the example files are part of the po4a project, you are free to use, modify and distribute them in your own projects without needing to refer back to po4a or list the po4a team in your own copyright notices, in the same manner as other build tools like Automake itself. If you want to mention po4a, that is fine too.

<h2>Authors</h2>

<pre> Neil Williams &lt;linux [at] codehelp.co.uk&gt;</pre>

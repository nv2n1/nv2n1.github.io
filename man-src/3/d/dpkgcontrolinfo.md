---
title: "dpkgcontrolinfo(3)"
name: "dpkgcontrolinfo"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpkgcontrolinfo/"
---

Dpkg::Control::Info - parse files like debian/control 

<h2>Description</h2>It provides an object to access data of files that follow the same syntax as <i>debian/control</i>.
<h2>Functions</h2><dl COMPACT><dt>$c = Dpkg::Control::Info-&gt;new($file)
<dd>Create a new Dpkg::Control::Info object for <tt>$file</tt>. If <tt>$file</tt> is omitted, it loads <i>debian/control</i>. If file is ``-'', it parses the standard input.
<dt>$c-&gt;<i>reset()</i>
<dd>Resets what got read.
<dt>$c-&gt;load($file)
<dd>Load the content of <tt>$file</tt>. Exits in case of errors. If file is ``-'', it loads from the standard input.
<dt>$c-&gt;parse($fh, $description)
<dd>Parse a control file from the given filehandle. Exits in case of errors. <tt>$description</tt> is used to describe the filehandle, ideally it's a filename or a description of where the data comes from. It's used in error messages.
<dt>$c-&gt;[0]
<dd><dt>$c-&gt;<i>get_source()</i>
<dd>Returns a Dpkg::Control object containing the fields concerning the source package.
<dt>$c-&gt;get_pkg_by_idx($idx)
<dd>Returns a Dpkg::Control object containing the fields concerning the binary package numbered <tt>$idx</tt> (starting at 1).
<dt>$c-&gt;get_pkg_by_name($name)
<dd>Returns a Dpkg::Control object containing the fields concerning the binary package named <tt>$name</tt>.
<dt>$c-&gt;<i>get_packages()</i>
<dd>Returns a list containing the Dpkg::Control objects for all binary packages.
<dt>$c-&gt;output($filehandle)
<dd>Dump the content into a filehandle.
<dt>&quot;$c&quot;
<dd>Return a string representation of the content.
<dt>@{$c}
<dd>Return a list of Dpkg::Control objects, the first one is corresponding to source information and the following ones are the binary packages information.</dl><h2>Changes</h2><h3>Version 1.00</h3>Mark the module as public.
<h2>Author</h2>Raphaël Hertzog &lt;hertzog [at] debian.org&gt;.

---
title: "dpkgconf(3)"
name: "dpkgconf"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpkgconf/"
---

Dpkg::Conf - parse dpkg configuration files 

<h2>Description</h2>The Dpkg::Conf object can be used to read options from a configuration file. It can exports an array that can then be parsed exactly like <tt>@ARGV</tt>.
<h2>Functions</h2><dl COMPACT><dt>my $conf = Dpkg::Conf-&gt;new(%opts)
</dt><dd>Create a new Dpkg::Conf object. Some options can be set through <tt>%opts:</tt> if allow_short evaluates to true (it defaults to false), then short options are allowed in the configuration file, they should be prepended with a single hyphen.
</dd><dt>@$conf
</dt><dd></dd><dt>@options = $conf-&gt;<i>get_options()</i>
</dt><dd>Returns the list of options that can be parsed like <tt>@ARGV</tt>.
</dd><dt>$conf-&gt;load($file)
</dt><dd>Read options from a file. Return the number of options parsed.
</dd><dt>$conf-&gt;parse($fh)
</dt><dd>Parse options from a file handle. Return the number of options parsed.
</dd><dt>$conf-&gt;filter(remove =&gt; $rmfunc)
</dt><dd></dd><dt>$conf-&gt;filter(keep =&gt; $keepfunc)
</dt><dd>Filter the list of options, either removing or keeping all those that return true when &amp;$rmfunc($option) or &amp;keepfunc($option) is called.
</dd><dt>$string = $conf-&gt;output($fh)
</dt><dd>Write the options in the given filehandle (if defined) and return a string representation of the content (that would be) written.
</dd><dt>&quot;$conf&quot;
</dt><dd>Return a string representation of the content.
</dd><dt>$conf-&gt;save($file)
</dt><dd>Save the options in a file.</dd></dl><h2>Changes</h2><h3>Version 1.01</h3>New method: <tt>$conf</tt>-&gt;<i>filter()</i>
<h3>Version 1.00</h3>Mark the module as public.
<h2>Author</h2>Raphaël Hertzog &lt;hertzog [at] debian.org&gt;.

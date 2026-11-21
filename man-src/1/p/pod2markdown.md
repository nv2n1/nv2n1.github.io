---

title: "pod2markdown(1)"
name: "pod2markdown"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pod2markdown/"
---

pod2markdown - Convert POD text to Markdown 

<h2>VERSION</h2>

 version 2.002

<pre>
    # parse STDIN, print to STDOUT
    $ pod2markdown &lt; POD_File &gt; Markdown_File
    # parse file, print to STDOUT
    $ pod2markdown input.pod
    # parse file, print to file
    $ pod2markdown input.pod output.mkdn
    # parse STDIN, print to file
    $ pod2markdown - output.mkdn
</pre>

This program uses Pod::Markdown to convert <font SIZE="-1">POD</font> into Markdown sources. 

 It accepts two optional arguments:
<dl>
<dt>&bull;
</dt><dd> input pod file (defaults to <tt>&quot;STDIN&quot;</tt>)
</dd><dt>&bull;
</dt><dd> output markdown file (defaults to <tt>&quot;STDOUT&quot;</tt>)</dd></dl>

<h2>SEE ALSO</h2>

 This program is strongly based on <tt>&quot;pod2mdwn&quot;</tt> from Module::Build::IkiWiki.

<h2>AUTHORS</h2>

<dl>
<dt>&bull;
</dt><dd> Marcel Gruenauer &lt;marcel [at] cpan.org&gt;
</dd><dt>&bull;
</dt><dd> Victor Moral &lt;victor [at] taquiones.net&gt;
</dd><dt>&bull;
</dt><dd> Ryan C. Thompson &lt;rct at thompsonclan d0t org&gt;
</dd><dt>&bull;
</dt><dd> Aristotle Pagaltzis &lt;pagaltzis [at] gmx.de&gt;
</dd><dt>&bull;
</dt><dd> Randy Stauner &lt;rwstauner [at] cpan.org&gt;</dd></dl>

<h2>COPYRIGHT AND LICENSE</h2>

 This software is copyright (c) 2004 by Marcel Gruenauer. 

 This is free software; you can redistribute it and/or modify it under the same terms as the Perl 5 programming language system itself.

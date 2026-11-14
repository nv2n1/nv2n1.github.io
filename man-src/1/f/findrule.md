---
title: "findrule(1)"
name: "findrule"
section: "1"
letter: "f"
url: "/docs/linux/man/1-findrule/"
---

<h2 class="name">NAME</h2>
 

 findrule - command line wrapper to File::Find::Rule 

<h2>USAGE</h2>

 <pre><code>
findrule[path...][expression]
</code></pre>

<h2>DESCRIPTION</h2>

 <tt>&quot;findrule&quot;</tt> mostly borrows the interface from <font SIZE="-1">GNU</font> <i><a HREF="/docs/linux/man/1-find/">find</a></i>(1) to provide a command-line interface onto the File::Find::Rule heirarchy of modules. 

 The syntax for expressions is the rule name, preceded by a dash, followed by an optional argument. If the argument is an opening parenthesis it is taken as a list of arguments, terminated by a closing parenthesis. 

 Some examples: 

 <pre>
 find -file -name ( foo bar )
</pre> 

 files named <tt>&quot;foo&quot;</tt> or <tt>&quot;bar&quot;</tt>, below the current directory. 

 <pre>
 find -file -name foo -bar
</pre> 

 files named <tt>&quot;foo&quot;</tt>, that have pubs (for this is what our ficticious <tt>&quot;bar&quot;</tt> clause specifies), below the current directory. 

 <pre>
 find -file -name ( -bar )
</pre> 

 files named <tt>&quot;-bar&quot;</tt>, below the current directory. In this case if we'd have omitted the parenthesis it would have parsed as a call to name with no arguments, followed by a call to -bar.

<h3>Supported switches</h3>

 I'm very slack. Please consult the File::Find::Rule manpage for now, and prepend - to the commands that you want.

<h3>Extra bonus switches</h3>

 findrule automatically loads all of your installed File::Find::Rule::* extension modules, so check the documentation to see what those would be.

<h2>AUTHOR</h2>

 Richard Clamp &lt;richardc [at] unixbeard.net&gt; from a suggestion by Tatsuhiko Miyagawa

<h2>COPYRIGHT</h2>

 Copyright (C) 2002 Richard Clamp. All Rights Reserved. 

 This program is free software; you can redistribute it and/or modify it under the same terms as Perl itself.

<h2>SEE ALSO</h2>

 File::Find::Rule 

<h2>Index</h2>



---
title: "rpmextra(1)"
name: "rpmextra"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rpmextra/"
description: "rpmextra – display extra packages : not from distribution repositories"
---

<h2 class="name">NAME</h2>
<p> rpmextra &#8211; display extra packages : not from distribution repositories </p>
<h2>DESCRIPTION</h2>
<p> rpmextra search for extra packages : packages installed on the system that are not available in any repository listed in the config file </p>
<p> this packages are often installed manually and are not updated as others packages by distribution tools</p>
<h2>SYNOPSIS</h2>
<p> rpmextra [options] </p>
<p> options: </p>
<pre>
   -help                brief help message
   -man                 full documentation
   -V, --version        print version
   -verbose             verbose
</pre>
<h2>REQUIRED ARGUMENTS</h2>
<p> none</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-help</code></p>
<dd> Print a brief help message and exits.</p>
<dt><code>-man</code></p>
<dd> Print the manual page and exits.</p>
<dt><code>-version</code></p>
<dd> Print the program release and exit.</p>
<dt><code>-verbose</code></p>
<dd> The program works and print debugging messages.</dl>
<h2>USAGE</h2>
<p> rpmextra</p>
<h2>DIAGNOSTICS</h2>
<p> the verbose mode allow to see which functions are used</p>
<h2>EXIT STATUS</h2>
<p> O if all is ok </p>
<p> &gt;=1 if a problem</p>
<h2>CONFIGURATION</h2>
<p> nothing</p>
<h2>DEPENDENCIES</h2>
<p> rpmextra depends upon rpm package managers. it can use yum (Redhat), urpmi (Mandriva), zypper (Suse) tools</p>
<h2>INCOMPATIBILITIES</h2>
<p> not known</p>
<h2>BUGS AND LIMITATIONS</h2>
<p> the program does not work well on program installed with several versions</p>
<h2>NOTES</h2>
<p> this program can be used as &#8220;normal&#8221; user</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-rpm/">rpm</a></i>(1) for rpm call </p>
<p> <i><a href="/docs/linux/man/1-rpmorphan/">rpmorphan</a></i>(1) </p>
<p> <i><a href="/docs/linux/man/1-rpmusage/">rpmusage</a></i>(1) </p>
<p> <i><a href="/docs/linux/man/1-rpmduplicates/">rpmduplicates</a></i>(1) </p>
<p> <i><a href="/docs/linux/man/1-rpmdep/">rpmdep</a></i>(1)</p>
<h2>LICENSE AND COPYRIGHT</h2>
<p> Copyright (C) 2008 by Eric Gerbier This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.</p>
<h2>AUTHOR</h2>
<p> Eric Gerbier </p>
<p> you can report any bug or suggest to gerbier [at] users.sourceforge.net </p>
<h2>Index</h2>

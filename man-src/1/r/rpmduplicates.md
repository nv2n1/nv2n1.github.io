---
title: "rpmduplicates(1)"
name: "rpmduplicates"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rpmduplicates/"
description: "rpmduplicates – find program with several version installed"
---

<h2 class="name">NAME</h2>
<p> rpmduplicates &#8211; find program with several version installed </p>
<h2>DESCRIPTION</h2>
<p> sometimes, the upgrade of a system will install new packages, and &#8220;forget&#8221; to remove the older version. Rpmorphan do not work with this kind of unused packages. Rpmduplicates is the answer. I recommend to run it after each distribution upgrade (for example from fedora core 7 to 8).</p>
<h2>SYNOPSIS</h2>
<p> rpmduplicates.pl [options] </p>
<p> options: </p>
<pre>
   -help                brief help message
   -man                 full documentation
   -V, --version        print version
   -verbose             verbose
</pre>
<h2>REQUIRED ARGUMENTS</h2>
<p> nothing</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-help</code></p>
<dd> Print a brief help message and exits.</p>
<dt><code>-man</code></p>
<dd> Print the full manual page and exits.</p>
<dt><code>-version</code></p>
<dd> Print the program release and exit.</p>
<dt><code>-verbose</code></p>
<dd> The program works and print debugging messages.</dl>
<h2>USAGE</h2>
<p> rpmduplicates.pl</p>
<h2>FILES</h2>
<p> nothing</p>
<h2>DIAGNOSTICS</h2>
<p> it will show the duplicates with their version and build date </p>
<p> and suggest to remove the older one </p>
<p> example : </p>
<p> duplicate kernel-devel : 2.6.24.4-64.fc8 (Sat Mar 29 15:36:41 2008) / 2.6.24.3-50.fc8 (Thu Mar 20 20:43:47 2008) </p>
<p> suggest : rpm -e kernel-devel-2.6.24.3-50.fc8</p>
<h2>EXIT STATUS</h2>
<p> the number of duplicates packages found</p>
<h2>CONFIGURATION</h2>
<p> nothing</p>
<h2>DEPENDENCIES</h2>
<p> rpmorphan library</p>
<h2>INCOMPATIBILITIES</h2>
<p> not known</p>
<h2>BUGS AND LIMITATIONS</h2>
<p> not known</p>
<h2>NOTES</h2>
<p> this program can be used as &#8220;normal&#8221; user </p>
<p> the gpg-pubkey packages are excluded from the result</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-rpm/">rpm</a></i>(1) for rpm call </p>
<p> <i><a href="/docs/linux/man/1-rpmorphan/">rpmorphan</a></i>(1) </p>
<p> <i><a href="/docs/linux/man/1-rpmusage/">rpmusage</a></i>(1) </p>
<p> <i><a href="/docs/linux/man/1-rpmdep/">rpmdep</a></i>(1) </p>
<p> <i><a href="/docs/linux/man/1-rpmextra/">rpmextra</a></i>(1)</p>
<h2>LICENSE AND COPYRIGHT</h2>
<p> Copyright (C) 2008 by Eric Gerbier This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.</p>
<h2>AUTHOR</h2>
<p> Eric Gerbier </p>
<p> you can report any bug or suggest to gerbier [at] users.sourceforge.net </p>
<h2>Index</h2>

---
title: "rpmdep(1)"
name: "rpmdep"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rpmdep/"
description: "rpmdep – display the full dependency of an installed rpm package"
---

<h2 class="name">NAME</h2>
<p> rpmdep &#8211; display the full dependency of an installed rpm package </p>
<h2>DESCRIPTION</h2>
<p> rpmdep is an improved &#8216;rpm -qR&#8217; command : it search recursively for package dependencies, and resolvs all dependencies to package names. It can also prepare a file to build a graph of dependencies, with graphviz.</p>
<h2>SYNOPSIS</h2>
<p> rpmdep.pl [options] package </p>
<p> options: </p>
<pre>
   -help                brief help message
   -man                 full documentation
   -V, --version        print version
   -use-cache           use cache file instead rpm query
   -clear-cache         clear cache file
   -verbose             verbose
   -dot dotfile         build a dot file for graphviz
   -depending           instead of dependencies, display dependings
   -all                 works on all installed packages
</pre>
<h2>REQUIRED ARGUMENTS</h2>
<p> a package to analyse. Only one name may be given. It is not necessary if you are using the -all option.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-help</code></p>
<dd> Print a brief help message and exits.</p>
<dt><code>-man</code></p>
<dd> Print the manual page and exits.</p>
<dt><code>-version</code></p>
<dd> Print the program release and exit.</p>
<dt><code>-verbose</code></p>
<dd> The program works and print debugging messages.</p>
<dt><code>-dot</code></p>
<dd> create a dot file to be used by graphviz. in normal call, an arrow from a to b means that a package depends (uses) b package. in dependings call, an arrow from a to b means that a package is used by b package.</p>
<dt><code>-use-cache</code></p>
<dd> the rpm query may be long (10 to 30 s). If you will run an rpmorphan tool several time, this option will allow to gain a lot of time : it save the rpm query on a file cache (first call), then use this cache instead quering rpm (others calls).</p>
<dt><code>-clear-cache</code></p>
<dd> to remove cache file. Can be used with -use-cache to write a new cache.</p>
<dt><code>&#8211;depending</code></p>
<dd> instead of showing package dependencies (rpm -qR), display packages wich are depending upon the given argument : it then act as an improved &#8216;rpm -q &#8211;whatrequires&#8217; command</p>
<dt><code>&#8211;all</code></p>
<dd> rpmdep will then work on all installed packages, and display the results sorted by the number of depends (or dependings).</dl>
<h2>USAGE</h2>
<p> get the full list of dependencies for rpmrebuild package </p>
<pre>
  rpmdep.pl rpmrebuild
</pre>
<p> get the full list of dependencies for rpmrestore package and build the graph data file (rpmrestore.dot) </p>
<pre>
  rpmdep.pl -dot rpmrestore.dot rpmrestore
</pre>
<p> build a png graph image from the graph data </p>
<pre>
  dot -Tpng rpmrestore.dot -o rpmrestore.png
</pre>
<p> get depending package of perl </p>
<pre>
  rpmdep.pl --depending perl
</pre>
<p> check is a package is an orphan </p>
<pre>
  rpmdep.pl --depending afick-gui
</pre>
<p> list all package dependencies </p>
<pre>
  rpmdep.pl -a
</pre>
<p> list all packages dependings and prepare a graph </p>
<pre>
  rpmdep.pl -a --depending --dot alldep.dot
</pre>
<h2>FILES</h2>
<p> the program can use the /tmp/rpmorphan.cache file</p>
<h2>DIAGNOSTICS</h2>
<p> the verbose mode allow to see all the recursive work </p>
<p> others messages are</p>
<dl>
<dt><code>package &#8230; is not installed</code></p>
<dd> this is not a name of an installed package</p>
<dt><code>&#8230; has no dependencies</code></p>
<dd> this can comes for some admin tools (ash for example)</p>
<dt><code>&#8230; depends upon (list)</code></p>
<dd> return a list of sorted and comma separated packages</p>
<dt><code>&#8230; is needed by (list)</code></p>
<dd> return the depending package list</p>
<dt><code>no depending : &#8230; is an orphan</code></p>
<dd> the given package has no depending packages : it is an orphan</dl>
<h2>EXIT STATUS</h2>
<p> O if all is ok </p>
<p> &gt;=1 if a problem</p>
<h2>CONFIGURATION</h2>
<p> nothing</p>
<h2>DEPENDENCIES</h2>
<p> you should use graphviz to build graph from</p>
<h2>INCOMPATIBILITIES</h2>
<p> not known</p>
<h2>BUGS AND LIMITATIONS</h2>
<p> the program does not work well on program installed in several versions</p>
<h2>NOTES</h2>
<p> this program can be used as &#8220;normal&#8221; user</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-rpm/">rpm</a></i>(1) for rpm call </p>
<p> <i><a href="/docs/linux/man/1-rpmorphan/">rpmorphan</a></i>(1) </p>
<p> <i><a href="/docs/linux/man/1-rpmusage/">rpmusage</a></i>(1) </p>
<p> <i><a href="/docs/linux/man/1-rpmduplicates/">rpmduplicates</a></i>(1) </p>
<p> <i><a href="/docs/linux/man/1-rpmextra/">rpmextra</a></i>(1)</p>
<h2>LICENSE AND COPYRIGHT</h2>
<p> Copyright (C) 2008 by Eric Gerbier This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.</p>
<h2>AUTHOR</h2>
<p> Eric Gerbier </p>
<p> you can report any bug or suggest to gerbier [at] users.sourceforge.net </p>
<h2>Index</h2>

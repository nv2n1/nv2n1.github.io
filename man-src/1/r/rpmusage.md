---
title: "rpmusage(1)"
name: "rpmusage"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rpmusage/"
description: "rpmusage – display rpm packages last use"
---

<h2 class="name">NAME</h2>
<p> rpmusage &#8211; display rpm packages last use </p>
<h2>DESCRIPTION</h2>
<p> rpmusage will display for each package, the last date it was used (in days). It can be used to find unused packages. It use the atime field of all package&#8217;s files to do this job. Note : as it scan all files inodes, the run may be long &#8230;</p>
<h2>SYNOPSIS</h2>
<p> rpmusage.pl [options] [targets] </p>
<p> options: </p>
<pre>
   -help                brief help message
   -man                 full documentation
   -V, --version        print version
   -verbose             verbose
   -fullalgo            force full algorythm
   -use-cache           use cache to avoid rpm query
   -clear-cache         remove cache file
   -exclude pac         exclude pac from results
   -install-time +/-d   apply on packages which are installed before (after) d days
   -access-time d       apply on packages which are not been accessed for d days (slow)
</pre>
<p> targets: </p>
<pre>
   -package pac         search last access on pac package
   -all                 apply on all packages (this is the default)
   -guess-perl          apply on perl packages
   -guess-python        apply on python packages
   -guess-pike          apply on pike packages
   -guess-ruby          apply on ruby packages
   -guess-common        apply on common packages
   -guess-data          apply on data packages
   -guess-doc           apply on documentation packages
   -guess-dev           apply on development packages
   -guess-lib           apply on library packages
   -guess-all           apply all -guess-* options (perl, python ...)
   -guess-custom regex  apply the given regex to filter to package's names to filter the output
</pre>
<h2>REQUIRED ARGUMENTS</h2>
<p> it can be used without any argument, and then will apply on all packages</p>
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
<dt><code>-use-cache</code></p>
<dd> the rpm query may be long (10 to 30 s). If you will run an rpmorphan tool several time, this option will allow to gain a lot of time : it save the rpm query on a file cache (first call), then use this cache instead quering rpm (others calls).</p>
<dt><code>-clear-cache</code></p>
<dd> to remove cache file. Can be used with -use-cache to write a new cache.</p>
<dt><code>-exclude</code></p>
<dd> this option will specify the packages to exclude from the output. Can be used as &#8216;&#8211;exclude pac1 &#8211;exclude pac2&#8217; or &#8216;&#8211;exclude &#8220;pac1, pac2&#8221;&#8217;</p>
<dt><code>-install-time</code></p>
<dd> install-time is a filter on the period from the package installation date to now (in days). if set positive, it only allow packages installed before x days. if set negative, it only allow packages installed since x days.</p>
<dt><code>-access-time</code></p>
<dd> access-time is designed to filter packages which have not been used since x days. </p>
<p> be careful : this option will slow the program</p>
<dt><code>-fullalgo</code></p>
<dd> for a small list of packages, rpmusage use a different quicker methode : rpm -e &#8211;test </p>
<p> this option can be used to force the use of the full algo</p>
<dt><code>-package</code></p>
<dd> search if the given package(s) is(are) orphaned. Can be used as &#8216;&#8211;package pac1 &#8211;package pac2&#8217; or &#8216;&#8211;package &#8220;pac1, pac2&#8221;&#8217;</p>
<dt><code>-all</code></p>
<dd> apply on all installed packages. The output should be interpreted. For example lilo or grub are orphaned packages, but are necessary to boot &#8230; </p>
<p> the &#8220;-install-time&#8221; and &#8220;-access-time&#8221; options may be useful to filter the list</p>
<dt><code>-guess-perl</code></p>
<dd> This option tries to find perl modules. It tries to match &#8220;^perl&#8221;</p>
<dt><code>-guess-python</code></p>
<dd> This option tries to find python modules. It tries to match &#8220;^python&#8221;</p>
<dt><code>-guess-pike</code></p>
<dd> This option tries to find pike modules. It tries to match &#8220;^pike&#8221;</p>
<dt><code>-guess-ruby</code></p>
<dd> This option tries to find ruby modules. It tries to match &#8220;^ruby&#8221;</p>
<dt><code>-guess-common</code></p>
<dd> This option tries to find common packages. It tries to match &#8220;-common$&#8221;</p>
<dt><code>-guess-data</code></p>
<dd> This option tries to find data packages. It tries to match &#8220;-data$&#8221;</p>
<dt><code>-guess-doc</code></p>
<dd> This option tries to find documentation packages. It tries to match &#8220;-doc$&#8221;</p>
<dt><code>-guess-data</code></p>
<dd> This option tries to find data packages. It tries to match &#8220;-data$&#8221;</p>
<dt><code>-guess-dev</code></p>
<dd> This option tries to find development packages. It tries to match &#8220;-devel$&#8221;</p>
<dt><code>-guess-lib</code></p>
<dd> This option tries to find library packages. It tries to match &#8220;^lib&#8221;</p>
<dt><code>-guess-all</code></p>
<dd> This is a short to tell : Try all of the above (perl, python &#8230;)</p>
<dt><code>-guess-custom</code></p>
<dd> this will allow you to specify your own filter. for exemple &#8220;^wh&#8221; will match whois, whatsnewfm &#8230;</dl>
<h2>USAGE</h2>
<p> display all packages in access date order </p>
<p> rpmusage.pl | sort -k 2 -n </p>
<p> only ask for perl packages </p>
<p> rpmusage.pl &#8211;guess-perl | sort -k 2 -n </p>
<p> to read the output : &#8220;python-pexpect 97 on /usr/share/doc/python-pexpect&#8221; means the package was last used 97 days ago and the more recently used file was the /usr/share/doc/python-pexpect file</p>
<h2>FILES</h2>
<p> /tmp/rpmorphan.cache : cache file to store rpm query. The cache file is common to all rpmorphan tools</p>
<h2>DEPENDENCIES</h2>
<p> rpmusage uses only standard perl module. </p>
<p> but it needs the rpm command tool.</p>
<h2>BUGS AND LIMITATIONS</h2>
<p> the software can only work with one version of each software : we only treat the first version seen</p>
<h2>CONFIGURATION</h2>
<p> the program can read rcfile if some exists. it will load in order </p>
<p> /etc/rpmorphanrc </p>
<p> ~/.rpmorphanrc </p>
<p> .rpmorphanrc </p>
<p> In this file, </p>
<p> # are comments, </p>
<p> and parameters are stored in the following format : parameter = value </p>
<p> example : </p>
<p> all = 1 </p>
<p> curses = 1</p>
<h2>INCOMPATIBILITIES</h2>
<p> not known</p>
<h2>DIAGNOSTICS</h2>
<p> to be written</p>
<h2>NOTES</h2>
<p> this program should be used as root superuser, because it needs to access (in read mode) to all files</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-rpm/">rpm</a></i>(1) for rpm call </p>
<p> <i><a href="/docs/linux/man/1-rpmorphan/">rpmorphan</a></i>(1) </p>
<p> <i><a href="/docs/linux/man/1-rpmdep/">rpmdep</a></i>(1) </p>
<p> <i><a href="/docs/linux/man/1-rpmduplicates/">rpmduplicates</a></i>(1) </p>
<p> <i><a href="/docs/linux/man/1-rpmextra/">rpmextra</a></i>(1)</p>
<h2>EXIT STATUS</h2>
<p> should be allways 0</p>
<h2>LICENSE AND COPYRIGHT</h2>
<p> Copyright (C) 2006 by Eric Gerbier This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.</p>
<h2>AUTHOR</h2>
<p> Eric Gerbier </p>
<p> you can report any bug or suggest to gerbier [at] users.sourceforge.net </p>
<h2>Index</h2>

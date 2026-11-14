---
title: "rpmorphan(1)"
name: "rpmorphan"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rpmorphan/"
description: "rpmorphan – find orphaned packages"
---

<h2 class="name">NAME</h2>
<p> rpmorphan &#8211; find orphaned packages </p>
<h2>DESCRIPTION</h2>
<p> rpmorphan finds &#8220;orphaned&#8221; packages on your system. It determines which packages have no other packages depending on their installation, and shows you a list of these packages. It is clone of deborphan debian software for rpm packages. </p>
<p> It will try to help you to remove unused packages, for exemple : </p>
<p> &#8211; after a distribution upgrade </p>
<p> &#8211; when you want to suppress packages after some tests</p>
<h2>SYNOPSIS</h2>
<p> rpmorphan [options] [targets] </p>
<p> or </p>
<p> grpmorphan [options] [targets] </p>
<p> using grpmorphan is a short way to use &#8220;rpmorphan -gui&#8221; </p>
<p> options: </p>
<pre>
   -help                brief help message
   -man                 full documentation
   -V, --version        print version
   -verbose             verbose
   -dry-run             simulate package remove
   -fullalgo            force full algorythm
   -suggests            use suggested package as if required
   -arch                work and show on full name with version and architecture
   -use-cache           use cache to avoid rpm query
   -clear-cache         remove cache file
   -gui                 display the graphical interface
   -tk                  display the tk graphical interface
   -curses              display the curses graphical interface
   -exclude pac         exclude pac from results
   -install-time +/-d   apply on packages which are installed before (after) d days
   -access-time d       apply on packages which are not been accessed for d days (slow)
</pre>
<p> targets: </p>
<pre>
   -package pac         search if pac is an orphan package
   -all                 apply on all packages
   -guess-perl          apply on perl packages
   -guess-python        apply on python packages
   -guess-pike          apply on pike packages
   -guess-ruby          apply on ruby packages
   -guess-common        apply on common packages
   -guess-data          apply on data packages
   -guess-doc           apply on documentation packages
   -guess-dev           apply on development packages
   -guess-lib           apply on library packages (this is the default target if none is specified)
   -guess-all           apply all -guess-* options (perl, python ...)
   -guess-custom regex  apply the given regex to filter to package's names to filter the output
</pre>
<p> keep file management </p>
<pre>
   -keep-file file      define the keep file to be used
   -list-keep           list permanent exclude list
   -zero-keep           empty permanent exclude list
   -add-keep pac        add pac package to permanent exclude list
   -del-keep pac        remove pac package from permanent exclude list
</pre>
<h2>REQUIRED ARGUMENTS</h2>
<p> you should provide at least one target. this can be</p>
<dl>
<dt><code>-all</code></p>
<dd> all the installed rpm package</p>
<dt><code>-package</code></p>
<dd> one or several explicit package</p>
<dt><code>-guess-*</code></p>
<dd> pre-selected packages groups</p>
<dt><code>-guess-custom</code></p>
<dd> give a filter to select the packages you want study. you can use regular expressions.</dl>
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
<dt><code>-dry-run</code></p>
<dd> this is a simulation mode : rpmorphan will show you what is the result of package removing. The window&#8217;s title is modified to show this mode.</p>
<dt><code>-use-cache</code></p>
<dd> the rpm query may be long (10 to 30 s). If you will run an rpmorphan tool several time, this option will allow to gain a lot of time : it save the rpm query on a file cache (first call), then use this cache instead quering rpm (others calls).</p>
<dt><code>-clear-cache</code></p>
<dd> to remove cache file. Can be used with -use-cache to write a new cache.</p>
<dt><code>-gui</code></p>
<dd> display a graphical interface which allow to show informations, remove packages (an internal help is provided). This is currently the same as the -tk option</p>
<dt><code>-tk</code></p>
<dd> display a tk graphical interface which allow to show informations, remove packages (an internal help is provided). The Tk perl module is necessary to run the gui.</p>
<dt><code>-curses</code></p>
<dd> display a curses graphical interface which allow to show informations, remove packages (an internal help is provided). The Curses::UI perl module is necessary to run the gui.</p>
<dt><code>-exclude</code></p>
<dd> this option will specify the packages to exclude from the output. Can be used as &#8216;&#8211;exclude pac1 &#8211;exclude pac2&#8217; or &#8216;&#8211;exclude &#8220;pac1, pac2&#8221;&#8217;</p>
<dt><code>-install-time</code></p>
<dd> install-time is a filter on the period from the package installation date to now (in days). if set positive, it only allow packages installed before x days. if set negative, it only allow packages installed since x days.</p>
<dt><code>-access-time</code></p>
<dd> access-time is designed to filter packages which have not been used since x days. </p>
<p> be careful : this option will slow the program</p>
<dt><code>-fullalgo</code></p>
<dd> for a small list of packages, rpmorphan use a different quicker methode : rpm -e &#8211;test </p>
<p> this option can be used to force the use of the full algo</p>
<dt><code>-suggests</code></p>
<dd> some rpm version offers a meta-data dependency call suggests : it is for usefull but not necessary packages. if this option is set, the suggested packages are used in rpmorphan as required packages. The default value for this option is unset.</p>
<dt><code>-arch</code></p>
<dd> by default, rpmorphan works on package name. this option will rpmorphan work on full package name : name-version-release.arch. This may be usefull if you have several version or several archictectures installed.</p>
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
<dd> this will allow you to specify your own filter. for exemple &#8220;^wh&#8221; will match whois, whatsnewfm &#8230;</p>
<dt><code>-keep-file</code></p>
<dd> define the keep file to be used. If not set, the /var/lib/rpmorphan/keep will be used</p>
<dt><code>-list-keep</code></p>
<dd> list the permanent list of excluded packages and exit.</p>
<dt><code>-zero-keep</code></p>
<dd> empty the permanent list of excluded packages and exit.</p>
<dt><code>-add-keep</code></p>
<dd> add package(s) to the permanent list of excluded packages and exit. </p>
<p> Can be used as &#8216;&#8211;add-keep pac1 &#8211;add-keep pac2&#8217; or &#8216;&#8211;add-keep &#8220;pac1, pac2&#8221;&#8217;</p>
<dt><code>-del-keep</code></p>
<dd> remove package(s) from the permanent list of excluded packages and exit. </p>
<p> Can be used as &#8216;&#8211;add-keep pac1 &#8211;add-keep pac2&#8217; or &#8216;&#8211;add-keep &#8220;pac1, pac2&#8221;&#8217;</dl>
<h2>USAGE</h2>
<p> rpmorphan can be useful after a distribution upgrade, to remove packages forgotten by the upgrade tool. It is interesting to use the options &quot;-all -install-time +xx&#8217;. </p>
<p> If you want to remove some recent tested packages, my advice is &quot;-all -install-time -xx&#8217;. </p>
<p> if you just want to clean your disk, use &#8216;-all -access-time xxx&#8217;</p>
<h2>FILES</h2>
<p> /var/lib/rpmorphan/keep : the permanent exclude list </p>
<p> /tmp/rpmorphan.cache : cache file to store rpm query. The cache file is common to all rpmorphan tools </p>
<p> /var/log/rpmorphan.log : log of all deleted packages</p>
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
<h2>DEPENDENCIES</h2>
<p> rpmorphan uses standard perl module in console mode. </p>
<p> If you want to use the Tk graphical interface, you should install the Tk module (perl-Tk rpm package). </p>
<p> If you want to use the curses interface, you should install the Curses::UI perl module ( perl-Curses-UI rpm package). </p>
<p> If you want to speed up rpmorphan, you should install the <font SIZE="-1">RPM2</font> perl module ( perl-RPM2 rpm package). On mandriva, the <font SIZE="-1">URPM</font> perl module (dependency from urpmi) will be used instead.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>display orphaned libraries</p>
<dd> rpmorphan</p>
<dt>display all orphaned packages in a curses interface</p>
<dd> rpmorphan &#8211;all &#8211;curses</p>
<dt>display orphaned packages, not used since one year</p>
<dd> rpmorphan &#8211;all -access-time +365</p>
<dt>display all orphaned packages, installed in the last 10 days</p>
<dd> rpmorphan &#8211;all -install-time -10</p>
<dt>display all orphaned packages, installed one month ago (or more)</p>
<dd> rpmorphan &#8211;all -install-time +30</dl>
<h2>BUGS AND LIMITATIONS</h2>
<p> Virtuals packages are not well (for now) taken in account. Let&#8217;s see an example : lilo and grub provide &#8216;bootloader&#8217; virtual, which is necessary for system boot. if the 2 are installed, they will be shown all 2 as orphans (but you can not remove the 2). If you remove one of them, the other is now longer shown as orphan. </p>
<p> the software can only work with one version of each software : we only treat the first version seen</p>
<h2>INCOMPATIBILITIES</h2>
<p> not known</p>
<h2>DIAGNOSTICS</h2>
<p> to be written</p>
<h2>NOTES</h2>
<p> this program can be used as &#8220;normal&#8221; user to show orphans, but you need to run it as supersuser (root) to remove packages or apply changes in the permanent exclude list </p>
<p> access-time and install-time options are &#8220;new&#8221; features, not available in deborphan tool </p>
<p> For Fedora users : Yum offers a program called &#8216;package-cleanup&#8217; which, called with the &#8216;&#8211;leaves&#8217; option, can show quickly a list of unused library packages. </p>
<p> For Mandriva users : the &#8216;urpme &#8211;auto-orphans&#8217; command show quickly a a list of unused library packages.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><font SIZE="-1">RPMORPHAN_METHOD</font></p>
<dd> for experts only : allow to force the method used to get rpm data. It can be set to <font SIZE="-1">URPM, RPM2</font> or &#8216;basic&#8217; (for external rpm query)</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-rpm/">rpm</a></i>(1) for rpm call </p>
<p> <i><a href="/docs/linux/man/1-rpmusage/">rpmusage</a></i>(1) </p>
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

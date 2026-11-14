---
title: "helpztags(1)"
name: "helpztags"
section: "1"
letter: "h"
url: "/docs/linux/man/1-helpztags/"
---

<h2 class="name">NAME</h2>
 

 helpztags - generate the help tags file for directory 

<h2>SYNOPSIS</h2>

 helpztags <i></i><font SIZE="-1"><i>DIRS</i></font><i></i>...

<h2>DESCRIPTION</h2>

 <i>helpztags</i> scans given directories for <i>*.txt</i> and <i>*.txt.gz</i> files. Each file is scanned for tags used in <i>vim</i> help files. For each directory proper <i>tags</i> file is generated. 

 There should be at least one directory given. In other case program exits with error.

<h2>AUTHORS</h2>

 Written by Jakub Turski and Artur R. Czechowski based on idea contained in <tt> vim
 </tt> sources for its <tt> :helptags command
 </tt>.

<h2>REPORTING BUGS</h2>

 Please use a Debian <tt> reportbug
 </tt> command or procedure described at <tt> <a rel="nofollow" HREF="http://bugs.debian.org/">http://bugs.debian.org/</a>
 </tt>.

<h2>SEE ALSO</h2>

 Read <tt> :help helptags
 </tt> in <i>vim</i> for detailed information about helptags. 

<h2>Index</h2>



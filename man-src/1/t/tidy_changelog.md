---
title: "tidy_changelog(1)"
name: "tidy_changelog"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tidy_changelog/"
---

<h2 class="name">NAME</h2>
 

 tidy_changelog - command-line tool for CPAN::Changes 

<h2>SYNOPSIS</h2>

 <pre>
    $ tidy_changelog Changelog
</pre>

<h2>DESCRIPTION</h2>

 Takes a changelog file, parse it using CPAN::Changes and prints out the resulting output. If a file is not given, the program will see if there is one file in the current directory beginning by 'change' (case-insensitive) and, if so, assume it to be the changelog.

<h2>ARGUMENTS</h2>

<h3>--next</h3>

 If provided, assumes that there is a placeholder header for an upcoming next release. The placeholder token is given via <i>--token</i>.

<h3>--token</h3>

 Regular expression to use to detect the token for an upcoming release if <i>--next</i> is used. If not explicitly given, defaults to <tt>&quot;\{\{\$NEXT\}\}&quot;</tt>.

<h3>--headers</h3>

 If given, only print out the release header lines, without any of the changes.

<h3>--reverse</h3>

 Prints the releases in reverse order (from the oldest to latest). 

<h2>Index</h2>



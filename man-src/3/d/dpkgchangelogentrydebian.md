---
title: "dpkgchangelogentrydebian(3)"
name: "dpkgchangelogentrydebian"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpkgchangelogentrydebian/"
---

Dpkg::Changelog::Entry::Debian - represents a Debian changelog entry 

<h2>Description</h2>This object represents a Debian changelog entry. It implements the generic interface Dpkg::Changelog::Entry. Only functions specific to this implementation are described below.
<h2>Functions</h2><dl COMPACT><dt>my @items = $entry-&gt;<i>get_change_items()</i>
<dd>Return a list of change items. Each item contains at least one line. A change line starting with an asterisk denotes the start of a new item. Any change line like ``[ Raphaël Hertzog ]'' is treated like an item of its own even if it starts a set of items attributed to this person (the following line necessarily starts a new item).
<dt>my @errors = $entry-&gt;<i>check_header()</i>
<dd><dt>my @errors = $entry-&gt;<i>check_trailer()</i>
<dd>Return a list of errors. Each item in the list is an error message describing the problem. If the empty list is returned, no errors have been found.
<dt>$entry-&gt;<i>normalize()</i>
<dd>Normalize the content. Strip whitespaces at end of lines, use a single empty line to separate each part.</dl><h2>Utility Functions</h2><dl COMPACT><dt>my $bool = match_header($line)
<dd>Checks if the line matches a valid changelog header line.
<dt>my $bool = match_trailer($line)
<dd>Checks if the line matches a valid changelog trailing line.
<dt>my @closed_bugs = find_closes($changes)
<dd>Takes one string as argument and finds ``Closes: #123456, #654321'' statements as supported by the Debian Archive software in it. Returns all closed bug numbers in an array.</dl><h2>Changes</h2><h3>Version 1.01</h3>New functions: <i>match_header()</i>, <i>match_trailer()</i> 

 Deprecated variables: <tt>$regex_header</tt>, <tt>$regex_trailer</tt>
<h3>Version 1.00</h3>Mark the module as public.
<h2>Author</h2>Raphaël Hertzog &lt;hertzog [at] debian.org&gt;.

---
title: "testlintianconfigfile(3)"
name: "testlintianconfigfile"
section: "3"
letter: "t"
url: "/docs/linux/man/3-testlintianconfigfile/"
---

Test::Lintian::ConfigFile -- generic helper routines for colon-delimited configuration files 

<h2>Synopsis</h2>use Test::Lintian::ConfigFile qw(read_config); my <tt>$desc</tt> = read_config('t/tags/testname/desc');
<h2>Description</h2>Routines for dealing with colon-delimited configuration files.
<h2>Functions</h2><dl COMPACT><dt>read_config(<font SIZE="-1">PATH, HASHREF</font>)
<dd>Reads the configuration file located at <font SIZE="-1">PATH</font> into a hash and returns it. When also passed a <font SIZE="-1">HASHREF,</font> will fill that instead.
<dt>write_config(<font SIZE="-1">TEST_CASE, PATH</font>)
<dd>Write the config described by hash reference <font SIZE="-1">TEST_CASE</font> to the file named <font SIZE="-1">PATH.</font>
<dt>read_field_from_file(<font SIZE="-1">FIELD, FILE</font>)
<dd>Returns the list of lines from file <font SIZE="-1">FILE</font> which start with the string <font SIZE="-1">FIELD</font> followed by a colon. The string <font SIZE="-1">FIELD</font> and the colon are removed from each line. 

</dl>

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
<h2>Functions</h2><dl COMPACT><dt>read_config(PATH, HASHREF)
</dt><dd>Reads the configuration file located at PATH into a hash and returns it. When also passed a HASHREF, will fill that instead.
</dd><dt>write_config(TEST_CASE, PATH)
</dt><dd>Write the config described by hash reference TEST_CASE to the file named PATH.
</dd><dt>read_field_from_file(FIELD, FILE)
</dt><dd>Returns the list of lines from file FILE which start with the string FIELD followed by a colon. The string FIELD and the colon are removed from each line. 
</dd></dl>

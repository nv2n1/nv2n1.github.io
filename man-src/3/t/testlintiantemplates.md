---
title: "testlintiantemplates(3)"
name: "testlintiantemplates"
section: "3"
letter: "t"
url: "/docs/linux/man/3-testlintiantemplates/"
---

Test::Lintian::Templates -- Helper routines dealing with templates 

<h2>Synopsis</h2>use Test::Lintian::Templates qw(fill_template); 

 my <tt>$data</tt> = { 'placeholder' =&gt; 'value' }; my <tt>$file</tt> = '/path/to/generated/file'; 

 fill_template(``$file.in'', <tt>$file</tt>, <tt>$data</tt>);
<h2>Description</h2>Routines for dealing with templates in Lintian test specifications.
<h2>Functions</h2><dl COMPACT><dt>copy_skeleton_template_sets(<font SIZE="-1">INSTRUCTIONS, RUN_PATH, SUITE, TEST_SET</font>)
<dd>Copies template sets belonging to <font SIZE="-1">SUITE</font> into the test working directory <font SIZE="-1">RUN_PATH</font> according to <font SIZE="-1">INSTRUCTIONS.</font> The <font SIZE="-1">INSTRUCTIONS</font> are the target directory relative to <font SIZE="-1">RUN_PATH</font> followed by the name of the template set in parentheses. Multiple such instructions must be separated by commas.
<dt>remove_surplus_templates(<font SIZE="-1">SRC_DIR, TARGET_DIR</font>)
<dd>Removes from <font SIZE="-1">TARGET_DIR</font> any templates that have corresponding originals in <font SIZE="-1">SRC_DIR.</font>
<dt>fill_skeleton_templates(<font SIZE="-1">INSTRUCTIONS, HASH, EPOCH, RUN_PATH, TEST_SET</font>)
<dd>Fills the templates specified in <font SIZE="-1">INSTRUCTIONS</font> using the data in <font SIZE="-1">HASH.</font> Only fills templates when the generated files are not present or are older than either the file modification time of the template or the age of the data as evidenced by <font SIZE="-1">EPOCH.</font> The <font SIZE="-1">INSTRUCTIONS</font> are the target directory relative to <font SIZE="-1">RUN_PATH</font> followed by the name of the whitelist in parentheses. Multiple instructions must be separated by commas.
<dt>fill_whitelisted_templates(<font SIZE="-1">DIR, WHITE_LIST, HASH, HASH_EPOCH</font>)
<dd>Generates all files in array <font SIZE="-1">WHITE_LIST</font> relative to <font SIZE="-1">DIR</font> from their templates, which are assumed to have the same file name but with extension '.in', using data provided in <font SIZE="-1">HASH.</font> The optional argument <font SIZE="-1">HASH_EPOCH</font> can be used to preserve files when no generation is necessary.
<dt>fill_all_templates(<font SIZE="-1">HASH, DIR</font>)
<dd>Fills all templates in <font SIZE="-1">DIR</font> with data from <font SIZE="-1">HASH.</font>
<dt>fill_template(<font SIZE="-1">TEMPLATE, GENERATED, HASH, HASH_EPOCH, DELIMITERS</font>)
<dd>Fills template <font SIZE="-1">TEMPLATE</font> with data from <font SIZE="-1">HASH</font> and places the result in file <font SIZE="-1">GENERATED.</font> When given <font SIZE="-1">HASH_EPOCH,</font> will evaluate beforehand if a substitution is necessary based on file modification times. The optional parameter <font SIZE="-1">DELIMITERS</font> can be used to change the standard delimiters. 

</dl>

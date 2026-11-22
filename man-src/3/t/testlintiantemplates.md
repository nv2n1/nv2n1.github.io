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
<h2>Functions</h2><dl COMPACT><dt>copy_skeleton_template_sets(INSTRUCTIONS, RUN_PATH, SUITE, TEST_SET)
</dt><dd>Copies template sets belonging to SUITE into the test working directory RUN_PATH according to INSTRUCTIONS. The INSTRUCTIONS are the target directory relative to RUN_PATH followed by the name of the template set in parentheses. Multiple such instructions must be separated by commas.
</dd><dt>remove_surplus_templates(SRC_DIR, TARGET_DIR)
</dt><dd>Removes from TARGET_DIR any templates that have corresponding originals in SRC_DIR.
</dd><dt>fill_skeleton_templates(INSTRUCTIONS, HASH, EPOCH, RUN_PATH, TEST_SET)
</dt><dd>Fills the templates specified in INSTRUCTIONS using the data in HASH. Only fills templates when the generated files are not present or are older than either the file modification time of the template or the age of the data as evidenced by EPOCH. The INSTRUCTIONS are the target directory relative to RUN_PATH followed by the name of the whitelist in parentheses. Multiple instructions must be separated by commas.
</dd><dt>fill_whitelisted_templates(DIR, WHITE_LIST, HASH, HASH_EPOCH)
</dt><dd>Generates all files in array WHITE_LIST relative to DIR from their templates, which are assumed to have the same file name but with extension '.in', using data provided in HASH. The optional argument HASH_EPOCH can be used to preserve files when no generation is necessary.
</dd><dt>fill_all_templates(HASH, DIR)
</dt><dd>Fills all templates in DIR with data from HASH.
</dd><dt>fill_template(TEMPLATE, GENERATED, HASH, HASH_EPOCH, DELIMITERS)
</dt><dd>Fills template TEMPLATE with data from HASH and places the result in file GENERATED. When given HASH_EPOCH, will evaluate beforehand if a substitution is necessary based on file modification times. The optional parameter DELIMITERS can be used to change the standard delimiters. 
</dd></dl>

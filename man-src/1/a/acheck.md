---
title: "acheck(1)"
name: "acheck"
section: "1"
letter: "a"
url: "/docs/linux/man/1-acheck/"
description: "acheck – Check common localization mistakes"
---

<h2 class="name">NAME</h2>
<p> acheck &#8211; Check common localization mistakes </p>
<h2>SYNOPSIS</h2>
<p> acheck [<font SIZE="-1">OPTIONS</font>] [<font SIZE="-1">INPUT_FILE</font>]</p>
<h2>DESCRIPTION</h2>
<p> This program parses a file checking for syntax rules and optionally asking Aspell for checking word spelling. It makes fix suggestions and outputs a corrected file accordingly adding review comments if requested. </p>
<p> It tries to find the file type according to the extension or the first lines and loads rules accordingly. </p>
<p> It displays lines when they are parse. </p>
<p> When an error is found, a menu is displayed. Just press Enter if you don&#8217;t want to change anything. If a choice suits you, enter the corresponding number. If you want to fix it but no choice is correct, enter a space, then you will be asked for a string to replace the highlighted text. The script will replace the highlighted text with your choice and parse it again for new errors. </p>
<p> Here are all the available commands:</p>
<dl>
<dt><i>Enter</i>, ignore.</p>
<dd> Ignore.</p>
<dt><i>Ctrl+L</i>, redraw.</p>
<dd> Rewrite the last line, suggestions and hints.</p>
<dt><i>Space</i>, edit.</p>
<dd> Edit the highlighted text.</p>
<dt><i>E</i>, edit line.</p>
<dd> Edit the whole line.</p>
<dt><i>H</i>, add hint.</p>
<dd> Add the displayed hint as review comment. Use this if you want the translator to see the corresponding warning or error but you have no correction.</p>
<dt><i>N</i>, next line.</p>
<dd> Skip the rest of this line.</p>
<dt><i>X</i>, exit and discard all changes.</p>
<dd> Quit without saving modifications, the script ask you for confirmation, you have to enter `<code>yes</code>&#8216; to exit otherwise parsing starts again at the current mistake.</p>
<dt><i>a</i>, add in dictionary.</p>
<dd> Add the highlighted word to you personal dictionary, capitalized as it is.</p>
<dt><i>l</i>, add lowercase in dictionary.</p>
<dd> Lowercase the highlighted word to add it to your personal dictionary.</p>
<dt><i>i</i>, ignore word.</p>
<dd> Ignore the highlighted word, same as <i>Enter</i>.</p>
<dt><i>I</i>, ignore all.</p>
<dd> Ignore the highlighted word and add it to your session dictionary.</dl>
<h2>OPTIONS</h2>
<p> Verbosity level:</p>
<dl>
<dt><i>-q</i>, <i>&#8211;quiet</i></p>
<dd> quiet mode.</p>
<dt><i>-v</i></p>
<dd> verbose, start at level <i></i>$Debug<i> + 1</i>, add more for more verbosity (see below).</p>
<dt><i>&#8211;verbose n</i></p>
<dd> set verbosity level to <i>n</i> (see below).</dl>
<p> Files:</p>
<dl>
<dt><i>-i</i>, <i>&#8211;input</i></p>
<dd> input filename, can be &#8216;<i>&#8211;</i>&#8216; to read data from standard input.</p>
<dt><i>-o</i>, <i>&#8211;output</i></p>
<dd> output filename, can be &#8216;<i>&#8211;</i>&#8216; to write data to standard ouput. If no output filename is provided, input file is backed up with `<i>bak_ext</i>&#8216; extension and input filename is used.</dl>
<p> Spell check:</p>
<dl>
<dt><i>-s</i>, <i>&#8211;spell</i></p>
<dd> check spelling with Aspell.</p>
<dt><i>-d language</i>, <i>&#8211;dict language</i></p>
<dd> use <i>language</i> dictionary for Aspell.</p>
<dt><i>-n</i>, <i>&#8211;nospell</i></p>
<dd> don&#8217;t check spelling.</dl>
<p> Mode:</p>
<dl>
<dt><i>-r</i>, <i>&#8211;review</i></p>
<dd> review mode, add comments on lines beginning with <i></i>$Comment<i></i> after parsed line.</p>
<dt><i>-t</i>, <i>&#8211;trans</i></p>
<dd> translator mode, don&#8217;t add comments, just fix errors.</dl>
<p> others:</p>
<dl>
<dt><i>&#8211;rules ruleset</i></p>
<dd> use <i>ruleset</i> rules set.</p>
<dt><i>&#8211;type filetype</i></p>
<dd> use <i>filetype</i> whatever the file type is.</p>
<dt><i>&#8211;dump</i></p>
<dd> Dump the rules to check and exit, use this for debugging purposes.</p>
<dt><i>-V</i>, <i>&#8211;version</i></p>
<dd> print version and exit.</p>
<dt><i>-h</i>, <i>&#8211;help</i></p>
<dd> print a short usage message and exit.</dl>
<h2>Verbosity Level</h2>
<dl>
<dt><i>0</i> quiet, normal</p>
<dd> only warnings and errors</p>
<dt><i>1</i> debug</p>
<dd> names of subroutines</p>
<dt><i>2</i> debug verbose</p>
<dd> names and arguments of subroutines</p>
<dt><i>3</i> .. <i>5</i> debug very verbose</p>
<dd> output parsing and checking details</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/5-acheck/">acheck</a></i>(5), <i><a href="/docs/linux/man/5-acheck-rules/">acheck-rules</a></i>(5)</p>
<h2>AUTHOR</h2>
<p> Nicolas Bertolissio &lt;bertol [at] debian.org&gt;</p>
<h2>POD ERRORS</h2>
<p> Hey! <code>The above document had some coding errors, which are explained below:</code></p>
<dl>
<dt>Around line 196:</p>
<dd> You forgot a &#8216;=back&#8217; before &#8216;=head1&#8217; </p>
</dl>
<h2>Index</h2>

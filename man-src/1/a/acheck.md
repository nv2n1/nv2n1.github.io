---

title: "acheck(1)"
name: "acheck"
section: "1"
letter: "a"
url: "/docs/linux/man/1-acheck/"
description: "acheck – Check common localization mistakes"
---

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
<dt><i>Enter</i>, ignore.</dt>
<dd> Ignore.</dd>
<dt><i>Ctrl+L</i>, redraw.</dt>
<dd> Rewrite the last line, suggestions and hints.</dd>
<dt><i>Space</i>, edit.</dt>
<dd> Edit the highlighted text.</dd>
<dt><i>E</i>, edit line.</dt>
<dd> Edit the whole line.</dd>
<dt><i>H</i>, add hint.</dt>
<dd> Add the displayed hint as review comment. Use this if you want the translator to see the corresponding warning or error but you have no correction.</dd>
<dt><i>N</i>, next line.</dt>
<dd> Skip the rest of this line.</dd>
<dt><i>X</i>, exit and discard all changes.</dt>
<dd> Quit without saving modifications, the script ask you for confirmation, you have to enter `<code>yes</code>&#8216; to exit otherwise parsing starts again at the current mistake.</dd>
<dt><i>a</i>, add in dictionary.</dt>
<dd> Add the highlighted word to you personal dictionary, capitalized as it is.</dd>
<dt><i>l</i>, add lowercase in dictionary.</dt>
<dd> Lowercase the highlighted word to add it to your personal dictionary.</dd>
<dt><i>i</i>, ignore word.</dt>
<dd> Ignore the highlighted word, same as <i>Enter</i>.</dd>
<dt><i>I</i>, ignore all.</dt>
<dd> Ignore the highlighted word and add it to your session dictionary.</dd></dl>
<h2>OPTIONS</h2>
<p> Verbosity level:</p>
<dl>
<dt><i>-q</i>, <i>&#8211;quiet</i></dt>
<dd> quiet mode.</dd>
<dt><i>-v</i></dt>
<dd> verbose, start at level <i></i>$Debug<i> + 1</i>, add more for more verbosity (see below).</dd>
<dt><i>&#8211;verbose n</i></dt>
<dd> set verbosity level to <i>n</i> (see below).</dd></dl>
<p> Files:</p>
<dl>
<dt><i>-i</i>, <i>&#8211;input</i></dt>
<dd> input filename, can be &#8216;<i>&#8211;</i>&#8216; to read data from standard input.</dd>
<dt><i>-o</i>, <i>&#8211;output</i></dt>
<dd> output filename, can be &#8216;<i>&#8211;</i>&#8216; to write data to standard ouput. If no output filename is provided, input file is backed up with `<i>bak_ext</i>&#8216; extension and input filename is used.</dd></dl>
<p> Spell check:</p>
<dl>
<dt><i>-s</i>, <i>&#8211;spell</i></dt>
<dd> check spelling with Aspell.</dd>
<dt><i>-d language</i>, <i>&#8211;dict language</i></dt>
<dd> use <i>language</i> dictionary for Aspell.</dd>
<dt><i>-n</i>, <i>&#8211;nospell</i></dt>
<dd> don&#8217;t check spelling.</dd></dl>
<p> Mode:</p>
<dl>
<dt><i>-r</i>, <i>&#8211;review</i></dt>
<dd> review mode, add comments on lines beginning with <i></i>$Comment<i></i> after parsed line.</dd>
<dt><i>-t</i>, <i>&#8211;trans</i></dt>
<dd> translator mode, don&#8217;t add comments, just fix errors.</dd></dl>
<p> others:</p>
<dl>
<dt><i>&#8211;rules ruleset</i></dt>
<dd> use <i>ruleset</i> rules set.</dd>
<dt><i>&#8211;type filetype</i></dt>
<dd> use <i>filetype</i> whatever the file type is.</dd>
<dt><i>&#8211;dump</i></dt>
<dd> Dump the rules to check and exit, use this for debugging purposes.</dd>
<dt><i>-V</i>, <i>&#8211;version</i></dt>
<dd> print version and exit.</dd>
<dt><i>-h</i>, <i>&#8211;help</i></dt>
<dd> print a short usage message and exit.</dd></dl>
<h2>Verbosity Level</h2>
<dl>
<dt><i>0</i> quiet, normal</dt>
<dd> only warnings and errors</dd>
<dt><i>1</i> debug</dt>
<dd> names of subroutines</dd>
<dt><i>2</i> debug verbose</dt>
<dd> names and arguments of subroutines</dd>
<dt><i>3</i> .. <i>5</i> debug very verbose</dt>
<dd> output parsing and checking details</dd></dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/5-acheck/">acheck</a></i>(5), <i><a href="/docs/linux/man/5-acheck-rules/">acheck-rules</a></i>(5)</p>
<h2>AUTHOR</h2>
<p> Nicolas Bertolissio &lt;bertol [at] debian.org&gt;</p>
<h2>POD ERRORS</h2>
<p> Hey! <code>The above document had some coding errors, which are explained below:</code></p>
<dl>
<dt>Around line 196:</dt>
<dd> You forgot a &#8216;=back&#8217; before &#8216;=head1&#8217; </dd>
</dl>

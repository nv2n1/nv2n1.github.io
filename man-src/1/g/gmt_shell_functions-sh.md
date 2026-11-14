---
title: "gmt_shell_functions-sh(1)"
name: "gmt_shell_functions-sh"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gmt_shell_functions-sh/"
description: "gmt_shell_functions.sh – Practical functions to be used in GMT bourne shell scripts"
---

<p>gmt_shell_functions.sh &#8211; Practical functions to be used in GMT bourne shell scripts</p>
<h2>Synopsis</h2>
<p><code>gmt_init_tmpdir</code> </p>
<p> <code>gmt_remove_tmpdir</code> </p>
<p> <code>gmt_clean_up</code> [<i>prefix</i>] </p>
<p> <code>gmt_message</code> <i>message</i> </p>
<p> <code>gmt_abort</code> <i>message</i> </p>
<p> <code>gmt_get_nrecords</code> <i>file(s)</i> </p>
<p> <code>gmt_get_ndatarecords</code> <i>file(s)</i> </p>
<p> <code>gmt_get_nfields</code> <i>string</i> </p>
<p> <code>gmt_get_field</code> <i>string</i> </p>
<p> <code>gmt_get_region</code> <i>file(s)</i> [<i>options</i>] </p>
<p> <code>gmt_get_gridregion</code> <i>file</i> [<i>options</i>] </p>
<p> <code>gmt_get_map_width</code> <code>-R</code> <code>-J</code> </p>
<p> <code>gmt_get_map_height</code> <code>-R</code> <code>-J</code> </p>
<p> <code>gmt_set_psfile</code> <i>file</i> </p>
<p> <code>gmt_set_pdffile</code> <i>file</i> </p>
<p> <code>gmt_set_framename</code> <i>prefix framenumber</i> </p>
<p> <code>gmt_set_framenext</code> <i>framenumber</i></p>
<h2>Description</h2>
<p><code>gmt_shell_functions.sh</code> provides a set of functions to Bourne (again) shell scripts in support of GMT. The calling shell script should include the following line, before the functions can be used: </p>
<p> <code>. gmt_shell_functions.sh</code> </p>
<p> Once included in a shell script, <code>gmt_shell_functions.sh</code> allows GMT users to do some scripting more easily than otherwise. The functions made available are:</p>
<dl>
<dt><code>gmt_init_tmpdir</code></p>
<dd>Creates a temporary directory in <code>/tmp</code> or (when defined) in the directory specified by the environment variable <code>TMPDIR</code>. The name of the temporary directory is returned as environment variable <code>GMT_TMPDIR</code>. This function also causes GMT to run in &#8216;isolation mode&#8217;, i.e., all temporary files will be created in <code>GMT_TMPDIR</code> and the <code>gmt.conf</code> file will not be adjusted.</p>
<dt><code>gmt_remove_tmpdir</code></p>
<dd>Removes the temporary directory and unsets the <code>GMT_TMPDIR</code> environment variable.</p>
<dt><code>gmt_cleanup</code></p>
<dd>Remove all files and directories in which the current process number is part of the file name. If the optional <i>prefix</i> is given then we also delete all files and directories that begins with the given prefix.</p>
<dt><code>gmt_message</code></p>
<dd>Send a message to standard error.</p>
<dt><code>gmt_abort</code></p>
<dd>Send a message to standard error and exit the shell.</p>
<dt><code>gmt_get_nrecords</code></p>
<dd>Returns the total number of lines in <i>file(s)</i></p>
<dt><code>gmt_get_ndatarecords</code></p>
<dd>Returns the total number of data records in <i>file(s)</i>, i.e., not counting headers.</p>
<dt><code>gmt_get_nfields</code></p>
<dd>Returns the number of fields or words in <i>string</i></p>
<dt><code>gmt_get_field</code></p>
<dd>Returns the given <i>field</i> in a <i>string</i>. Must pass <i>string</i> between double quotes to preserve it as one item.</p>
<dt><code>gmt_get_region</code></p>
<dd>Returns the region in the form w/e/s/n based on the data in table <i>file(s)</i>. Optionally add -I*dx*/<i>dy</i> to round off the answer.</p>
<dt><code>gmt_get_gridregion</code></p>
<dd>Returns the region in the form w/e/s/n based on the header of a grid <i>file</i>. Optionally add -I*dx*/<i>dy</i> to round off the answer.</p>
<dt><code>gmt_get_map_width</code></p>
<dd>Expects the user to give the desired <code>-R</code> <code>-J</code> settings and returns the map width in the current measurement unit.</p>
<dt><code>gmt_get_map_height</code></p>
<dd>Expects the user to give the desired <code>-R</code> <code>-J</code> settings and returns the map height in the current measurement unit.</p>
<dt><code>gmt_set_psfile</code></p>
<dd>Create the output PostScript file name based on the base name of a given file (usually the script name <code>$0</code>).</p>
<dt><code>gmt_set_framename</code></p>
<dd>Returns a lexically ordered filename stem (i.e., no extension) given the file prefix and the current frame number, using a width of 6 for the integer including leading zeros. Useful when creating animations and lexically sorted filenames are required.</p>
<dt><code>gmt_set_framenext</code></p>
<dd>Accepts the current frame integer counter and returns the next integer counter.</dl>
<h2>Notes</h2>
<p>1. These functions only work in the Bourne shell (<code>sh</code>) and their derivatives (like <code>ash</code>, <code>bash</code>, <code>ksh</code> and <code>zsh</code>). These functions do not work in the C shell (<code>csh</code>) or their derivatives (like <code>tcsh</code>), and cannot be used in DOS batch scripts either. </p>
<p> 2. <code>gmt_shell_functions.sh</code> were first introduced in GMT version 4.2.2 and have since been regularly expanded with other practical scripting short-cuts. If you want to suggest other functions, please do so by adding a New Issue request on gmt.soest.hawaii.edu.</p>
<h2>See Also</h2>
<p><code>gmt</code> , <code>gmt.conf</code> , <code>gmtinfo</code> , <code>grdinfo</code></p>
<h2>Copyright</h2>
<p>2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe</p>

---
title: "testlintianhooks(3)"
name: "testlintianhooks"
section: "3"
letter: "t"
url: "/docs/linux/man/3-testlintianhooks/"
---

Test::Lintian::Hooks -- hook routines for the test runners 

<h2>Synopsis</h2><pre> use Test::Lintian::Hooks qw(sed_hook);
 sed_hook('script.sed', 'input.file');</pre><h2>Description</h2>Various hook routines for the test runners.
<h2>Functions</h2><dl COMPACT><dt>sed_hook(<font SIZE="-1">SCRIPT, SUBJECT, OUTPUT</font>)
<dd>Runs the parser sed on file <font SIZE="-1">SUBJECT</font> using the instructions in <font SIZE="-1">SCRIPT</font> and places the result in the file <font SIZE="-1">OUTPUT.</font>
<dt>sort_lines(<font SIZE="-1">UNSORTED, SORTED</font>)
<dd>Sorts the file <font SIZE="-1">UNSORTED</font> line by line and places the result into the file <font SIZE="-1">SORTED.</font>
<dt>calibrate(<font SIZE="-1">SCRIPT, ACTUAL, EXPECTED, CALIBRATED</font>)
<dd>Executes calibration script <font SIZE="-1">SCRIPT</font> with the three arguments <font SIZE="-1">EXPECTED, ACTUAL</font> and <font SIZE="-1">CALIBRATED,</font> all of which are file paths. Please note that the order of arguments in this function corresponds to the bookkeeping logic of <font SIZE="-1">ACTUAL</font> vs <font SIZE="-1">EXPECTED.</font> The order for the script is different.
<dt>find_missing_prerequisites(<font SIZE="-1">TEST_CASE</font>)
<dd>Returns a string with missing dependencies, if applicable, that would be necessary to run the test described by hash <font SIZE="-1">DESC.</font>
<dt>run_lintian(<font SIZE="-1">DESC, INPUT, INCLUDES, OUTPUT, DIR</font>)
<dd>Runs Lintian in directory <font SIZE="-1">DIR</font> on the input file <font SIZE="-1">INPUT</font> and a collects the output in file <font SIZE="-1">OUTPUT.</font> Any include directories in <font SIZE="-1">INCLUDES,</font> if present, are passed on. 

</dl>

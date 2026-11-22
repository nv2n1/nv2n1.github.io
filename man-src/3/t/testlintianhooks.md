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
<h2>Functions</h2><dl COMPACT><dt>sed_hook(SCRIPT, SUBJECT, OUTPUT)
</dt><dd>Runs the parser sed on file SUBJECT using the instructions in SCRIPT and places the result in the file OUTPUT.
</dd><dt>sort_lines(UNSORTED, SORTED)
</dt><dd>Sorts the file UNSORTED line by line and places the result into the file SORTED.
</dd><dt>calibrate(SCRIPT, ACTUAL, EXPECTED, CALIBRATED)
</dt><dd>Executes calibration script SCRIPT with the three arguments EXPECTED, ACTUAL and CALIBRATED, all of which are file paths. Please note that the order of arguments in this function corresponds to the bookkeeping logic of ACTUAL vs EXPECTED. The order for the script is different.
</dd><dt>find_missing_prerequisites(TEST_CASE)
</dt><dd>Returns a string with missing dependencies, if applicable, that would be necessary to run the test described by hash DESC.
</dd><dt>run_lintian(DESC, INPUT, INCLUDES, OUTPUT, DIR)
</dt><dd>Runs Lintian in directory DIR on the input file INPUT and a collects the output in file OUTPUT. Any include directories in INCLUDES, if present, are passed on. 
</dd></dl>

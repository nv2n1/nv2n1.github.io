---
title: "mathomatic(1)"
name: "mathomatic"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mathomatic/"
description: "mathomatic – a computer algebra system rmath – a computer algebra system with functions"
---

<h2 class="name">NAME</h2>
<p> mathomatic &#8211; a computer algebra system<br />
 rmath &#8211; a computer algebra system with functions</p>
<h2>SYNOPSIS</h2>
<p> <code>mathomatic</code> [ <code>-bchqrtuvwx</code> ] [ <code>-s</code> level ] [ <code>-m</code> number ] [ input_files ]<br />
 <code>rmath</code> [ input_files ] </p>
<h2>DESCRIPTION</h2>
<p> Mathomatic is a portable Computer Algebra System (CAS) that can solve, simplify, combine, and compare algebraic equations, perform general complex number and polynomial arithmetic, etc. It does some calculus and handles all elementary algebra, except logarithms. Plotting expressions with gnuplot is also supported. </p>
<p> <code>mathomatic</code> is the main Mathomatic application that does interactive symbolic-numeric mathematics through a console interface. The numerical arithmetic is double precision floating point with up to 14 decimal digits accuracy. Many results will be exact, because multiple combined floating point numbers can be used for a single mathematical value; for example: <code>2^(1/3),</code> which is the cubed root of 2 exactly. </p>
<p> <code>rmath</code> allows you to use Mathomatic with input of functions like <code>sin(x)</code> and <code>sqrt(x)</code> automatically expanded to equivalent algebraic expressions by the <code>m4</code> macro processor. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code></p>
<dd> Enable bold colors. Color mode will be turned on and colors will be brighter if this option is specified. Same as the &quot;set bold color&quot; command. </p>
<dt><code>-c</code></p>
<dd> Toggle color mode. This mode outputs ANSI terminal escape sequences to make each level of parentheses a different color, for easier reading. Requires a terminal emulator that supports ANSI color escape sequences. If the colors are too hard to see, use the <code>-b</code> option to increase the brightness. </p>
<dt><code>-h</code></p>
<dd> Display a brief help message listing all of these options and then exit. </p>
<dt><code>-m number</code></p>
<dd> Change the memory size of equation spaces. It is followed by a decimal floating point number which is a multiplier of the default equation space size. This allows larger equation spaces so that manipulating extremely large expressions will succeed without getting the &quot;Expression too large&quot; error. Specifying a number higher than 100 may make Mathomatic unresponsive. </p>
<dt><code>-q</code></p>
<dd> Set quiet mode. The startup message and prompts are not displayed. This is useful when piping or redirecting input into Mathomatic, because the input won&#8217;t be displayed, so prompt output should be turned off. This option does the same thing as the &quot;set no prompt&quot; command. </p>
<dt><code>-r</code></p>
<dd> Disable readline input processing. Readline allows using the cursor keys and outputs terminal control codes which can be turned off with this option. </p>
<dt><code>-s level</code></p>
<dd> Set the enforced security level for the Mathomatic session. Level 0 is the default with no security. Level 1 disallows shelling out. Level 2 disallows shelling out and writing files. Level 3 disallows shelling out and reading/writing files for complete security. This run-time option was created for use on open public servers that can&#8217;t use the SECURE compile-time define. </p>
<dt><code>-t</code></p>
<dd> Set test mode. Used when testing and comparing output. Bypasses loading startup file, turns off color mode and readline, sets wide output mode, ignores pause command, etc. </p>
<dt><code>-u</code></p>
<dd> Guarantee that standard output and standard error output are unbuffered. Useful when piping. </p>
<dt><code>-v</code></p>
<dd> Display version number, compilation options used, maximum possible memory usage, then exit. </p>
<dt><code>-w</code></p>
<dd> Set wide output mode for an unlimited width output device like the &quot;set wide&quot; command does. Sets infinite screen columns and rows so that 2D (two dimensional) expression output will always succeed and not be downgraded to 1D output when it doesn&#8217;t fit in the display area. Use when redirecting output or with a terminal emulator that doesn&#8217;t wrap lines. This mode only affects 2D output. </p>
<dt><code>-x</code></p>
<dd> Enable HTML output mode (which is also valid XHTML). This makes Mathomatic output suitable for inclusion in a web page. The color mode and bold colors flags affect this mode, allowing HTML color output. Wide output mode is also set by this option, meaning expressions will always be displayed in 2D. </p>
</dl>
<h2>GENERAL</h2>
<p> After any options, text files may be specified on the shell command line that will be automatically read in with the read command. </p>
<p> Mathomatic is best run from within a terminal emulator. It uses console line input and output for the user interface. First you type in your mathematical equations in standard infix notation, then you can solve them by typing in the variable name at the prompt, or perform operations on them with simple English commands. Type &quot;help&quot; or &quot;?&quot; for the help command. If the command is longer than 4 letters, you only need to type in the first 4 letters. Most commands operate on the current equation by default. </p>
<p> A command preceded by an exclamation point (such as &quot;!ls&quot;) is taken to be a shell command and is passed unchanged to the shell (/bin/sh). &quot;!&quot; by itself invokes the default shell, which is specified in the SHELL environment variable. &quot;!&quot; is also the factorial operator. </p>
<p> Complete documentation is available in HTML format; see the local documentation directory or online at &quot;<a rel="nofollow" href="http://mathomatic.org/math/doc/">http://mathomatic.org/math/doc/</a>&quot; for the latest Mathomatic documentation. </p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>EDITOR</code></p>
<dd> The EDITOR environment variable specifies which text editor to use for the edit command. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt><code>~/.mathomaticrc</code></p>
<dd> Optional startup file containing Mathomatic set command options. It should be a text file with one set option per line. Do not include the word &quot;set&quot;. For example, the line &quot;no color&quot; will make Mathomatic default to non-color mode, which is useful if you are not using a standard terminal emulator. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-matho-primes/">matho-primes</a></code>(1), <code><a href="/docs/linux/man/1-primorial/">primorial</a></code>(1), <code><a href="/docs/linux/man/1-matho-mult/">matho-mult</a></code>(1), <code><a href="/docs/linux/man/1-matho-sum/">matho-sum</a></code>(1), <code><a href="/docs/linux/man/1-matho-pascal/">matho-pascal</a></code>(1), <code><a href="/docs/linux/man/1-matho-sumsq/">matho-sumsq</a></code>(1) </p>
<h2>BUGS</h2>
<p> The command to take the limit of an expression is partially functional and experimental. All else should work perfectly; if not, report it as a bug on the Launchpad website: &quot;<a rel="nofollow" href="http://launchpad.net/mathomatic">http://launchpad.net/mathomatic</a>&quot;. Please include version information, which you can find by running <code>mathomatic -v</code> or by entering the version command. </p>
<h2>AUTHOR</h2>
<p> Mathomatic has been written by George Gesslein II (gesslein [at] linux.com) with help from John Blommers (<a rel="nofollow" href="http://www.blommers.org">www.blommers.org</a>). It is free software, available under the terms and conditions of the GNU Lesser General Public License from &quot;<a rel="nofollow" href="http://mathomatic.org">http://mathomatic.org</a>&quot;. </p>
<h2>Index</h2>

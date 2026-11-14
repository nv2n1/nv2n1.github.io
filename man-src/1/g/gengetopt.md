---
title: "gengetopt(1)"
name: "gengetopt"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gengetopt/"
description: "gengetopt – manual page for gengetopt 2.22.6"
---

<h2>NAME</h2>
<p> gengetopt &#8211; manual page for gengetopt 2.22.6</p>
<h2>SYNOPSIS</h2>
<p> <code>gengetopt</code> [<i>OPTIONS</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> GNU gengetopt 2.22.6 </p>
<p> This program generates a C function that uses getopt_long function to parse the command line options, validate them and fill a struct.</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print help and exit</p>
<dt><code>&#8211;detailed-help</code></p>
<dd> Print help, including all details and hidden options, and exit</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print version and exit</dl>
<p> Main options:</p>
<dl>
<dt><code>-i</code>, <code>&#8211;input</code>=<i>filename</i></p>
<dd> input file (default std input)</p>
<dt><code>-f</code>, <code>&#8211;func-name</code>=<i>name</i></p>
<dd> name of generated function (default=`cmdline_parser&#8217;)</p>
<dt><code>-a</code>, <code>&#8211;arg-struct-name</code>=<i>name</i></p>
<dd> name of generated args info struct (default=`gengetopt_args_info&#8217;)</p>
<dt><code>-F</code>, <code>&#8211;file-name</code>=<i>name</i></p>
<dd> name of generated file (default=`cmdline&#8217;)</p>
<dt><code>&#8211;output-dir</code>=<i>path</i></p>
<dd> output directory</p>
<dt>
<dd> if this option is not specified, the files are generated in the current directory.</p>
<dt><code>&#8211;header-output-dir</code>=<i>path</i></p>
<dd> header output directory</p>
<dt><code>&#8211;src-output-dir</code>=<i>path</i></p>
<dd> source output directory</p>
<dt><code>-c</code>, <code>&#8211;c-extension</code>=<i>ext</i></p>
<dd> extension of c file (default=`c&#8217;)</p>
<dt><code>-H</code>, <code>&#8211;header-extension</code>=<i>ext</i></p>
<dd> extension of header file (default=`h&#8217;)</p>
<dt><code>-l</code>, <code>&#8211;long-help</code></p>
<dd> long usage line in help</p>
<dt>
<dd> The usage line will print all the options, e.g.,</p>
<dt>
<dd> sample1 <code>-iINT</code>|&#8211;int-opt=INT [-h|&#8211;help]</p>
<dt><code>&#8211;default-optional</code></p>
<dd> by default, an option is considered optional if not specified otherwise</p>
<dt><code>-u</code>, <code>&#8211;unamed-opts</code>[=<i>STRING</i>]</p>
<dd> accept options without names (e.g., file names) (default=`FILES&#8217;)</dl>
<p> The parser generated is thought to be used to parse the command line arguments. However, you can also generate parsers for configuration files, or strings that contain the arguments to parse, by using the following two options.</p>
<dl>
<dt><code>-C</code>, <code>&#8211;conf-parser</code></p>
<dd> generate a config file parser</p>
<dt><code>-S</code>, <code>&#8211;string-parser</code></p>
<dd> generate a string parser (the string contains the command line)</dl>
<h3>Additional options:</h3>
<dl>
<dt><code>-G</code>, <code>&#8211;include-getopt</code></p>
<dd> adds the code for getopt_long in the generated C file</p>
<dt><code>-n</code>, <code>&#8211;no-handle-help</code></p>
<dd> do not handle <code>&#8211;help</code>|-h automatically</p>
<dt>
<dd> If <code>&#8211;no-handle-help</code> is specified, the command line option <code>&#8211;help</code>|-h will not be handled automatically, so the programmer will be able to print some other information; then the function for printing the standard help output can be used; this function is called &lt;parser-name&gt;_print_help.</p>
<dt>
<dd> Notice that, although the programmer can handle <code>&#8211;help</code>|-h manually, the parser will return after finding such option: the other command line options, if any, will be ignored. In case you want to have full control on <code>&#8211;help</code>|-h, you should use <code>&#8211;ho-help</code>.</p>
<dt><code>&#8211;no-help</code></p>
<dd> do not add <code>&#8211;help</code>|-h automatically</p>
<dt>
<dd> With this option you can disable the automatic addition of options <code>&#8211;help</code>|-h. The programmer will then be able to add this option in the input file and handle it as he sees fit. Notice that <code>&#8211;no-help</code> will also disable the automatic options <code>&#8211;detailed-help</code> and <code>&#8211;full-help</code>.</p>
<dt>
<dd> The programmer can still define options with short character h as he wants, but he cannot define options help, unless he specifies <code>&#8211;no-help</code> (otherwise an error will be printed).</p>
<dt><code>-N</code>, <code>&#8211;no-handle-version</code></p>
<dd> do not handle <code>&#8211;version</code>|-V automatically</p>
<dt><code>&#8211;no-version</code></p>
<dd> do not add <code>&#8211;version</code>|-V automatically</p>
<dt>
<dd> See above the details about <code>&#8211;no-handle-help</code> and <code>&#8211;no-help</code>, respectively.</p>
<dt><code>-e</code>, <code>&#8211;no-handle-error</code></p>
<dd> do not exit on errors</p>
<dt>
<dd> With this option, if the generated parser encounters an error (e.g., an unknown option) it does not make the main program exit; instead, the parser function returns a value different 0, and the main program can print a help message.</p>
<dt><code>&#8211;show-required</code>[=<i>STRING</i>]</p>
<dd> in the output of help will specify which options are mandatory, by using the optional passed string (default=`(mandatory)&#8217;)</p>
<dt><code>&#8211;strict-hidden</code></p>
<dd> completely hide hidden options</p>
<dt><code>-g</code>, <code>&#8211;gen-version</code></p>
<dd> put gengetopt version in the generated file (default=on)</p>
<dt><code>&#8211;set-package</code>=<i>STRING</i></p>
<dd> set the package name (override package defined in the .ggo file)</p>
<dt><code>&#8211;set-version</code>=<i>STRING</i></p>
<dd> set the version number (override version defined in the .ggo file)</p>
<dt><code>&#8211;show-help</code></p>
<dd> show the output of <code>&#8211;help</code> instead of generating code</p>
<dt><code>&#8211;show-full-help</code></p>
<dd> show the output of <code>&#8211;full-help</code> (i.e., including hidden options) instead of generating code</p>
<dt><code>&#8211;show-detailed-help</code></p>
<dd> show the output of <code>&#8211;detailed-help</code> (i.e., including details and hidden options) instead of generating code</p>
<dt><code>&#8211;show-version</code></p>
<dd> show the output of <code>&#8211;version</code> instead of generating code</dl>
<p> Please refer to the info manual for further explanations. </p>
<p> Maintained by Lorenzo Bettini &lt;<a rel="nofollow" href="http://www.lorenzobettini.it">http://www.lorenzobettini.it</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1999-2011 Free Software Foundation Inc. This program comes with ABSOLUTELY NO WARRANTY; for details please see the file &#8216;COPYING&#8217; supplied with the source code.<br />
 This is free software, and you are welcome to redistribute it under certain conditions; again, see &#8216;COPYING&#8217; for details. This program is released under the GNU General Public License.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>gengetopt</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>gengetopt</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info gengetopt</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>

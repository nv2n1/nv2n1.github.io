---
title: "source-highlight(1)"
name: "source-highlight"
section: "1"
letter: "s"
url: "/docs/linux/man/1-source-highlight/"
description: "Source-highlight – convert source code to syntax highlighted document"
---

<h2>NAME</h2>
<p> Source-highlight &#8211; convert source code to syntax highlighted document</p>
<h2>SYNOPSIS</h2>
<p> <code>source-highlight</code> [<i>OPTIONS</i>]&#8230; <i>&lt; input_file &gt; output_file</i></p>
<h2>DESCRIPTION</h2>
<p> GNU source-highlight 3.1.6 </p>
<p> Highlight the syntax of a source file (e.g. Java) into a specific format (e.g. HTML)</p>
<dl>
<dt>
<dd> source-highlight [OPTIONS]&#8230; <code>-i</code> input_file <code>-o</code> output_file source-highlight [OPTIONS]&#8230; [FILES]&#8230;</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print help and exit</p>
<dt><code>&#8211;detailed-help</code></p>
<dd> Print help, including all details and hidden options, and exit</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print version and exit</p>
<dt><code>-i</code>, <code>&#8211;input</code>=<i>filename</i></p>
<dd> input file. default std input</p>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>filename</i></p>
<dd> output file. default std output (when the third invocation form is used). If STDOUT is specified, the output is directed to standard output</dl>
<p> you can simply specify some files at the command line and also use regular expressions (for instance *.java). In this case the name for the output files will be formed using the name of the source file with a .&lt;ext&gt; appended, where &lt;ext&gt; is the extension chosen according to the output format specified (for instance .html).</p>
<dl>
<dt><code>-s</code>, <code>&#8211;src-lang</code>=<i>STRING</i></p>
<dd> source language (use <code>&#8211;lang-list</code> to get the complete list). If not specified, the source language will be guessed from the file extension.</p>
<dt><code>&#8211;lang-list</code></p>
<dd> list all the supported language and associated language definition file</p>
<dt><code>&#8211;outlang-list</code></p>
<dd> list all the supported output language and associated language definition file</p>
<dt><code>-f</code>, <code>&#8211;out-format</code>=<i>STRING</i></p>
<dd> output format (use <code>&#8211;outlang-list</code> to get the complete list) (default=`html&#8217;)</p>
<dt><code>-d</code>, <code>&#8211;doc</code></p>
<dd> create an output file that can be used as a stand alone document (e.g., not to be included in another one)</p>
<dt><code>&#8211;no-doc</code></p>
<dd> cancel the <code>&#8211;doc</code> option even if it is implied (e.g., when css is given)</p>
<dt><code>-c</code>, <code>&#8211;css</code>=<i>filename</i></p>
<dd> the external style sheet filename. Implies <code>&#8211;doc</code></p>
<dt><code>-T</code>, <code>&#8211;title</code>=<i>STRING</i></p>
<dd> give a title to the output document. Implies <code>&#8211;doc</code></p>
<dt><code>-t</code>, <code>&#8211;tab</code>=<i>INT</i></p>
<dd> specify tab length. (default=`8&#8242;)</p>
<dt><code>-H</code>, <code>&#8211;header</code>=<i>filename</i></p>
<dd> file to insert as header</p>
<dt><code>-F</code>, <code>&#8211;footer</code>=<i>filename</i></p>
<dd> file to insert as footer</p>
<dt><code>&#8211;style-file</code>=<i>filename</i></p>
<dd> specify the file containing format options (default=`default.style&#8217;)</p>
<dt><code>&#8211;style-css-file</code>=<i>filename</i> specify the file containing format options (in</p>
<dd> css syntax)</p>
<dt><code>&#8211;style-defaults</code>=<i>filename</i> specify the file containing defaults for format</p>
<dd> options (default=`style.defaults&#8217;)</p>
<dt><code>&#8211;outlang-def</code>=<i>filename</i></p>
<dd> output language definition file</p>
<dt><code>&#8211;outlang-map</code>=<i>filename</i></p>
<dd> output language map file (default=`outlang.map&#8217;)</p>
<dt><code>&#8211;data-dir</code>=<i>path</i></p>
<dd> directory where language definition files and language maps are searched for. If not specified these files are searched for in the current directory and in the data dir installation directory</p>
<dt><code>&#8211;output-dir</code>=<i>path</i></p>
<dd> output directory</p>
<dt><code>&#8211;lang-def</code>=<i>filename</i></p>
<dd> language definition file</p>
<dt><code>&#8211;lang-map</code>=<i>filename</i></p>
<dd> language map file (default=`lang.map&#8217;)</p>
<dt><code>&#8211;show-lang-elements</code>=<i>filename</i></p>
<dd> prints the language elements that are defined</p>
<dt>
<dd> in the language definition file</p>
<dt><code>&#8211;infer-lang</code></p>
<dd> force to infer source script language (overriding given language specification)</dl>
<h3>Lines:</h3>
<dl>
<dt><code>-n</code>, <code>&#8211;line-number</code>[=<i>padding</i>]</p>
<dd> number all output lines, using the specified padding character (default=`0&#8242;)</p>
<dt><code>&#8211;line-number-ref</code>[=<i>prefix</i>]</p>
<dd> number all output lines and generate an anchor,</p>
<dt>
<dd> made of the specified prefix + the line number (default=`line&#8217;)</dl>
<p> Filtering output:</p>
<dl>
<dt>
<dd> Mode: linerange</p>
<dt>
<dd> specifying line ranges</p>
<dt><code>&#8211;line-range</code>=<i>STRING</i></p>
<dd> generate only the lines in the specified range(s)</p>
<dt><code>&#8211;range-separator</code>=<i>STRING</i></p>
<dd> the optional separator to be printed among ranges (e.g., &quot;&#8230;&quot;)</p>
<dt><code>&#8211;range-context</code>=<i>INT</i></p>
<dd> number of (context) lines generated even if not in range</p>
<dt>
<dd> Mode: regexrange</p>
<dt>
<dd> specifying regular expression delimited ranges</p>
<dt><code>&#8211;regex-range</code>=<i>STRING</i></p>
<dd> generate only the lines within the specified regular expressions</dl>
<h3>reference generation:</h3>
<dl>
<dt><code>&#8211;gen-references</code>=<i>STRING</i></p>
<dd> generate references (possible values=&quot;inline&quot;, &quot;postline&quot;, &quot;postdoc&quot; default=`inline&#8217;)</p>
<dt><code>&#8211;ctags-file</code>=<i>filename</i></p>
<dd> specify the file generated by ctags that will be used to generate references (default=`tags&#8217;)</p>
<dt><code>&#8211;ctags</code>=<i>cmd</i></p>
<dd> how to run the ctags command. If this option is not specified, ctags will be executed with the default value. If it is specified with an empty string, ctags will not be executed at all (default=`ctags <code>&#8211;excmd</code>=<i>n</i> <code>&#8211;tag-relative</code>=<i>yes</i>&#8216;)</dl>
<h3>testing:</h3>
<dl>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> verbose mode on</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> print no progress information</p>
<dt><code>&#8211;binary-output</code></p>
<dd> write output files in binary mode</p>
<dt><code>&#8211;statistics</code></p>
<dd> print some statistics (i.e., elapsed time)</p>
<dt><code>&#8211;gen-version</code></p>
<dd> put source-highlight version in the generated file (default=on)</p>
<dt><code>&#8211;check-lang</code>=<i>filename</i></p>
<dd> only check the correctness of a language definition file</p>
<dt><code>&#8211;check-outlang</code>=<i>filename</i></p>
<dd> only check the correctness of an output language definition file</p>
<dt><code>&#8211;failsafe</code></p>
<dd> if no language definition is found for the input, it is simply copied to the output</p>
<dt><code>-g</code>, <code>&#8211;debug-langdef</code>[=<i>type</i>]</p>
<dd> debug a language definition. In dump mode just dumps all the steps; in interactive, at each step, waits for some input (press ENTER to step) (possible values=&quot;interactive&quot;, &quot;dump&quot; default=`dump&#8217;)</p>
<dt><code>&#8211;show-regex</code>=<i>filename</i></p>
<dd> show the regular expression automaton corresponding to a language definition file</dl>
<p> Maintained by Lorenzo Bettini &lt;<a rel="nofollow" href="http://www.lorenzobettini.it">http://www.lorenzobettini.it</a>&gt;</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-source-highlight at gnu.org&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1999-2008 Lorenzo Bettini &lt;<a rel="nofollow" href="http://www.lorenzobettini.it">http://www.lorenzobettini.it</a>&gt; This program comes with ABSOLUTELY NO WARRANTY.<br />
 This is free software; you may redistribute copies of the program under the terms of the GNU General Public License. For more information about these matters, see the file named COPYING.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>Source-highlight</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>Source-highlight</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info Source-highlight</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>

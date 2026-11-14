---
title: "states(1)"
name: "states"
section: "1"
letter: "s"
url: "/docs/linux/man/1-states/"
description: "states – awk alike text processing tool"
---

<h2 class="name">NAME</h2>
<p> states &#8211; awk alike text processing tool</p>
<h2>SYNOPSIS</h2>
<p> <code>states</code> [<code>-hvV</code>] [<code>-D </code><i>var</i><code>=</code><i>val</i>] [<code>-f </code><i>file</i>] [<code>-o </code><i>outputfile</i>] [<code>-p </code><i>path</i>] [<code>-s </code><i>startstate</i>] [<code>-W </code><i>level</i>] [<i>filename</i> &#8230;] </p>
<h2>DESCRIPTION</h2>
<p> <code>States</code> is an awk-alike text processing tool with some state machine extensions. It is designed for program source code highlighting and to similar tasks where state information helps input processing. </p>
<p> At a single point of time, <code>States</code> is in one state, each quite similar to awk&#8217;s work environment, they have regular expressions which are matched from the input and actions which are executed when a match is found. From the action blocks, <code>states</code> can perform state transitions; it can move to another state from which the processing is continued. State transitions are recorded so <code>states</code> can return to the calling state once the current state has finished. </p>
<p> The biggest difference between <code>states</code> and awk, besides state machine extensions, is that <code>states</code> is not line-oriented. It matches regular expression tokens from the input and once a match is processed, it continues processing from the current position, not from the beginning of the next input line. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-D </code><i>var</i><code>=</code><i>val</i><code>, &#8211;define=</code><i>var</i><code>=</code><i>val</i></p>
<dd> Define variable <i>var</i> to have string value <i>val</i>. Command line definitions overwrite variable definitions found from the config file.</p>
<dt><code>-f </code><i>file</i><code>, &#8211;file=</code><i>file</i></p>
<dd> Read state definitions from file <i>file</i>. As a default, <code>states</code> tries to read state definitions from file <code>states.st</code> in the current working directory.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Print short help message and exit.</p>
<dt><code>-o </code><i>file</i><code>, &#8211;output=</code><i>file</i></p>
<dd> Save output to file <i>file</i> instead of printing it to <code>stdout</code>.</p>
<dt><code>-p </code><i>path</i><code>, &#8211;path=</code><i>path</i></p>
<dd> Set the load path to <i>path</i>. The load path defaults to the directory, from which the state definitions file is loaded.</p>
<dt><code>-s </code><i>state</i><code>, &#8211;state=</code><i>state</i></p>
<dd> Start execution from state <code>state</code>. This definition overwrites start state resolved from the <code>start</code> block.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Increase the program verbosity.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Print <code>states</code> version and exit.</p>
<dt><code>-W </code><i>level</i><code>, &#8211;warning=</code><i>level</i></p>
<dd> Set the warning level to <i>level</i>. Possible values for <i>level</i> are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>light</code></p>
<dd> light warnings (default)</p>
<dt><code>all</code></p>
<dd> all warnings</dl>
</dl>
</dl>
<h2>STATES PROGRAM FILES</h2>
<p> <code>States</code> program files can contain on <i>start</i> block, <i>startrules</i> and <i>namerules</i> blocks to specify the initial state, <i>state</i> definitions and <i>expressions</i>. </p>
<p> The <i>start</i> block is the main() of the <code>states</code> program, it is executed on script startup for each input file and it can perform any initialization the script needs. It normally also calls the <code>check_startrules()</code> and <code>check_namerules()</code> primitives which resolve the initial state from the input file name or the data found from the beginning of the input file. Here is a sample start block which initializes two variables and does the standard start state resolving: </p>
<dl>
<dt>
<dd>
<pre><code>
start
{
    a = 1;
    msg = "Hello, world!";
    check_startrules();
    check_namerules();
}
</code></pre>
</dl>
<p> Once the start block is processed, the input processing is continued from the initial state. </p>
<p> The initial state is resolved by the information found from the <i>startrules</i> and <i>namerules</i> blocks. Both blocks contain regular expression &#8211; symbol pairs, when the regular expression is matched from the name of from the beginning of the input file, the initial state is named by the corresponding symbol. For example, the following start and name rules can distinguish C and Fortran files: </p>
<dl>
<dt>
<dd>
<pre><code>
namerules
{
    /\.(c | h) $ / c;
    /\.[fF] $ / fortran;
}
startrules
{
    / -\* -[cC] -\* - / c;
    / -\* -fortran -\* - / fortran;
}
</code></pre>
</dl>
<p> If these rules are used with the previously shown start block, <code>states</code> first check the beginning of input file. If it has string <code>-*- c -*-</code>, the file is assumed to contain C code and the processing is started from state called <code>c</code>. If the beginning of the input file has string <code>-*- fortran -*-</code>, the initial state is <code>fortran</code>. If none of the start rules matched, the name of the input file is matched with the namerules. If the name ends to suffix <code>c</code> or <code>C</code>, we go to state <code>c</code>. If the suffix is <code>f</code> or <code>F</code>, the initial state is fortran. </p>
<p> If both start and name rules failed to resolve the start state, <code>states</code> just copies its input to output unmodified. </p>
<p> The start state can also be specified from the command line with option <code>-s</code>, <code>&#8211;state</code>. </p>
<p> State definitions have the following syntax: </p>
<p> <code>state { </code><i>expr</i> {<i>statements</i>} &#8230; } </p>
<p> where <i>expr</i> is: a regular expression, special expression or symbol and <i>statements</i> is a list of statements. When the expression <i>expr</i> is matched from the input, the statement block is executed. The statement block can call <code>states</code>&#8216; primitives, user-defined subroutines, call other states, etc. Once the block is executed, the input processing is continued from the current intput position (which might have been changed if the statement block called other states). </p>
<p> Special expressions <code>BEGIN</code> and <code>END</code> can be used in the place of <i>expr</i>. Expression <code>BEGIN</code> matches the beginning of the state, its block is called when the state is entered. Expression <code>END</code> matches the end of the state, its block is executed when <code>states</code> leaves the state. </p>
<p> If <i>expr</i> is a symbol, its value is looked up from the global environment and if it is a regular expression, it is matched to the input, otherwise that rule is ignored. </p>
<p> The <code>states</code> program file can also have top-level expressions, they are evaluated after the program file is parsed but before any input files are processed or the <i>start</i> block is evaluated. </p>
<h2>PRIMITIVE FUNCTIONS</h2>
<dl>
<dt><code>call (</code><i>symbol</i><code>)</code></p>
<dd> Move to state <i>symbol</i> and continue input file processing from that state. Function returns whatever the <code>symbol</code> state&#8217;s terminating <code>return</code> statement returned.</p>
<dt><code>calln (</code><i>name</i><code>)</code></p>
<dd> Like <code>call</code> but the argument <i>name</i> is evaluated and its value must be string. For example, this function can be used to call a state which name is stored to a variable.</p>
<dt><code>check_namerules ()</code></p>
<dd> Try to resolve start state from <code>namerules</code> rules. Function returns <code>1</code> if start state was resolved or <code>0</code> otherwise.</p>
<dt><code>check_startrules ()</code></p>
<dd> Try to resolve start state from <code>startrules</code> rules. Function returns <code>1</code> if start state was resolved or <code>0</code> otherwise.</p>
<dt><code>concat (</code><i>str</i><code>, &#8230;)</code></p>
<dd> Concanate argument strings and return result as a new string.</p>
<dt><code>float (</code><i>any</i><code>)</code></p>
<dd> Convert argument to a floating point number.</p>
<dt><code>getenv (</code><i>str</i><code>)</code></p>
<dd> Get value of environment variable <i>str</i>. Returns an empty string if variable <i>var</i> is undefined.</p>
<dt><code>int (</code><i>any</i><code>)</code></p>
<dd> Convert argument to an integer number.</p>
<dt><code>length (</code><i>item</i><code>, &#8230;)</code></p>
<dd> Count the length of argument strings or lists.</p>
<dt><code>list (</code><i>any</i><code>, &#8230;)</code></p>
<dd> Create a new list which contains items <i>any</i>, &#8230;</p>
<dt><code>panic (</code><i>any</i><code>, &#8230;)</code></p>
<dd> Report a non-recoverable error and exit with status <code>1</code>. Function never returns.</p>
<dt><code>print (</code><i>any</i><code>, &#8230;)</code></p>
<dd> Convert arguments to strings and print them to the output.</p>
<dt><code>range (</code><i>source</i><code>, </code><i>start</i><code>, </code><i>end</i><code>)</code></p>
<dd> Return a sub-range of <i>source</i> starting from position <i>start</i> (inclusively) to <i>end</i> (exclusively). Argument <i>source</i> can be string or list.</p>
<dt><code>regexp (</code><i>string</i><code>)</code></p>
<dd> Convert string <i>string</i> to a new regular expression.</p>
<dt><code>regexp_syntax (</code><i>char</i><code>, </code><i>syntax</i><code>)</code></p>
<dd> Modify regular expression character syntaxes by assigning new syntax <i>syntax</i> for character <i>char</i>. Possible values for <i>syntax</i> are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8216;w&#8217;</code></p>
<dd> character is a word constituent</p>
<dt><code>&#8216; &#8216;</code></p>
<dd> character isn&#8217;t a word constituent</dl>
</dl>
<dt><code>regmatch (</code><i>string</i><code>, </code><i>regexp</i><code>)</code></p>
<dd> Check if string <i>string</i> matches regular expression <i>regexp</i>. Functions returns a boolean success status and sets sub-expression registers <code>$</code><i>n</i>.</p>
<dt><code>regsub (</code><i>string</i>, <i>regexp</i><code>, </code><i>subst</i><code>)</code></p>
<dd> Search regular expression <i>regexp</i> from string <i>string</i> and replace the matching substring with string <i>subst</i>. Returns the resulting string. The substitution string <i>subst</i> can contain <code>$</code><i>n</i> references to the <i>n</i>:th parenthesized sup-expression.</p>
<dt><code>regsuball (</code><i>string</i>, <i>regexp</i><code>, </code><i>subst</i><code>)</code></p>
<dd> Like <code>regsub</code> but replace all matches of regular expression <i>regexp</i> from string <i>string</i> with string <i>subst</i>.</p>
<dt><code>require_state (</code><i>symbol</i><code>)</code></p>
<dd> Check that the state <i>symbol</i> is defined. If the required state is undefined, the function tries to autoload it. If the loading fails, the program will terminate with an error message.</p>
<dt><code>split (</code><i>regexp</i><code>, </code><i>string</i><code>)</code></p>
<dd> Split string <i>string</i> to list considering matches of regular rexpression <i>regexp</i> as item separator.</p>
<dt><code>sprintf (</code><i>fmt</i>, &#8230;)</p>
<dd> Format arguments according to <i>fmt</i> and return result as a string.</p>
<dt><code>strcmp (</code><i>str1</i><code>, </code><i>str2</i><code>)</code></p>
<dd> Perform a case-sensitive comparision for strings <i>str1</i> and <i>str2</i>. Function returns a value that is:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-1</code></p>
<dd> string <i>str1</i> is less than <i>str2</i></p>
<dt><code>0</code></p>
<dd> strings are equal</p>
<dt><code>1</code></p>
<dd> string <i>str1</i> is greater than <i>str2</i></dl>
</dl>
<dt><code>string (</code><i>any</i><code>)</code></p>
<dd> Convert argument to string.</p>
<dt><code>strncmp (</code><i>str1</i><code>, </code><i>str2</i><code>, </code><i>num</i><code>)</code></p>
<dd> Perform a case-sensitive comparision for strings <i>str1</i> and <i>str2</i> comparing at maximum <i>num</i><code> characters.</p>
<dt>substring (</code><i>str</i><code>, </code><i>start</i><code>, </code><i>end</i><code>)</code></p>
<dd> Return a substring of string <i>str</i> starting from position <i>start</i> (inclusively) to <i>end</i> (exclusively). </p>
</dl>
<h2>BUILTIN VARIABLES</h2>
<dl>
<dt><code>$.</code></p>
<dd> current input line number</p>
<dt><code>$</code><i>n</i></p>
<dd> the <i>n</i>:th parenthesized regular expression sub-expression from the latest state regular expression or from the <code>regmatch</code> primitive</p>
<dt><code>$`</code></p>
<dd> everything before the matched regular rexpression. This is usable when used with the <code>regmatch</code> primitive; the contents of this variable is undefined when used in action blocks to refer the data before the block&#8217;s regular expression.</p>
<dt><code>$B</code></p>
<dd> an alias for <code>$`</code></p>
<dt><code>argv</code></p>
<dd> list of input file names</p>
<dt><code>filename</code></p>
<dd> name of the current input file</p>
<dt><code>program</code></p>
<dd> name of the program (usually <code>states</code>)</p>
<dt><code>version</code></p>
<dd> program version string </p>
</dl>
<h2>FILES</h2>
<pre>
/usr/share/enscript/hl/*.st             enscript's states definitions
</pre>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-awk/">awk</a>(1), <a href="/docs/linux/man/1-enscript/">enscript</a>(1) </p>
<h2>AUTHOR</h2>
<p> Markku Rossi &lt;mtr [at] iki.fi&gt; &lt;<a rel="nofollow" href="http://www.iki.fi/~mtr/">http://www.iki.fi/~mtr/</a>&gt; </p>
<p> GNU Enscript WWW home page: &lt;<a rel="nofollow" href="http://www.iki.fi/~mtr/genscript/">http://www.iki.fi/~mtr/genscript/</a>&gt; </p>
<h2>Index</h2>

---
title: "jq(1)"
name: "jq"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jq/"
description: "jq – Command-line JSON processor"
---

<h2 class="name">NAME</h2>
<p> <code>jq</code> &#8211; Command-line JSON processor </p>
<h2>SYNOPSIS</h2>
<p> <code>jq</code> [<i>options</i>&#8230;] <i>filter</i> [<i>files</i>&#8230;] </p>
<p> <code>jq</code> can transform JSON in various ways, by selecting, iterating, reducing and otherwise mangling JSON documents. For instance, running the command <code>jq &#8216;map(.price) | add&#8217;</code> will take an array of JSON objects as input and return the sum of their &quot;price&quot; fields. </p>
<p> <code>jq</code> can accept text input as well, but by default, <code>jq</code> reads a stream of JSON entities (including numbers and other literals) from <code>stdin</code>. Whitespace is only needed to separate entities such as 1 and 2, and true and false. One or more <i>files</i> may be specified, in which case <code>jq</code> will read input from those instead. </p>
<p> The <i>options</i> are described in the <i>INVOKING JQ</i> section; they mostly concern input and output formatting. The <i>filter</i> is written in the jq language and specifies how to transform the input file or document.</p>
<h2>FILTERS</h2>
<p> A jq program is a &quot;filter&quot;: it takes an input, and produces an output. There are a lot of builtin filters for extracting a particular field of an object, or converting a number to a string, or various other standard tasks. </p>
<p> Filters can be combined in various ways &#8211; you can pipe the output of one filter into another filter, or collect the output of a filter into an array. </p>
<p> Some filters produce multiple results, for instance there&#8217;s one that produces all the elements of its input array. Piping that filter into a second runs the second filter for each element of the array. Generally, things that would be done with loops and iteration in other languages are just done by gluing filters together in jq. </p>
<p> It&#8217;s important to remember that every filter has an input and an output. Even literals like &quot;hello&quot; or 42 are filters &#8211; they take an input but always produce the same literal as output. Operations that combine two filters, like addition, generally feed the same input to both and combine the results. So, you can implement an averaging filter as <code>add / length</code> &#8211; feeding the input array both to the <code>add</code> filter and the <code>length</code> filter and then performing the division. </p>
<p> But that&#8217;s getting ahead of ourselves. :) Let&#8217;s start with something simpler: ## INVOKING JQ </p>
<p> jq filters run on a stream of JSON data. The input to jq is parsed as a sequence of whitespace-separated JSON values which are passed through the provided filter one at a time. The output(s) of the filter are written to standard out, again as a sequence of whitespace-separated JSON data. </p>
<p> Note: it is important to mind the shell&#8217;s quoting rules. As a general rule it&#8217;s best to always quote (with single-quote characters) the jq program, as too many characters with special meaning to jq are also shell meta-characters. For example, <code>jq &quot;foo&quot;</code> will fail on most Unix shells because that will be the same as <code>jq foo</code>, which will generally fail because <code>foo is not defined</code>. When using the Windows command shell (cmd.exe) it&#8217;s best to use double quotes around your jq program when given on the command-line (instead of the <code>-f program-file</code> option), but then double-quotes in the jq program need backslash escaping. </p>
<p> You can affect how jq reads and writes its input and output using some command-line options:</p>
<dl>
<dt>&#x25cb;</p>
<dd> <code>&#8211;version</code>:</p>
<dt>
<dd> Output the jq version and exit with zero.</p>
<dt>&#x25cb;</p>
<dd> <code>&#8211;seq</code>:</p>
<dt>
<dd> Use the <code>application/json-seq</code> MIME type scheme for separating JSON texts in jq&#8217;s input and output. This means that an ASCII RS (record separator) character is printed before each value on output and an ASCII LF (line feed) is printed after every output. Input JSON texts that fail to parse are ignored (but warned about), discarding all subsequent input until the next RS. This mode also parses the output of jq without the <code>&#8211;seq</code> option.</p>
<dt>&#x25cb;</p>
<dd> <code>&#8211;stream</code>:</p>
<dt>
<dd> Parse the input in streaming fashion, outputing arrays of path and leaf values (scalars and empty arrays or empty objects). For example, <code>&quot;a&quot;</code> becomes <code>[[],&quot;a&quot;]</code>, and <code>[[],&quot;a&quot;,[&quot;b&quot;]]</code> becomes <code>[[0],[]]</code>, <code>[[1],&quot;a&quot;]</code>, and <code>[[1,0],&quot;b&quot;]</code>.</p>
<dt>
<dd> This is useful for processing very large inputs. Use this in conjunction with filtering and the <code>reduce</code> and <code>foreach</code> syntax to reduce large inputs incrementally.</p>
<dt>&#x25cb;</p>
<dd> <code>&#8211;slurp</code>/<code>-s</code>:</p>
<dt>
<dd> Instead of running the filter for each JSON object in the input, read the entire input stream into a large array and run the filter just once.</p>
<dt>&#x25cb;</p>
<dd> <code>&#8211;raw-input</code>/<code>-R</code>:</p>
<dt>
<dd> Don&#8217;t parse the input as JSON. Instead, each line of text is passed to the filter as a string. If combined with <code>&#8211;slurp</code>, then the entire input is passed to the filter as a single long string.</p>
<dt>&#x25cb;</p>
<dd> <code>&#8211;null-input</code>/<code>-n</code>:</p>
<dt>
<dd> Don&#8217;t read any input at all! Instead, the filter is run once using <code>null</code> as the input. This is useful when using jq as a simple calculator or to construct JSON data from scratch.</p>
<dt>&#x25cb;</p>
<dd> <code>&#8211;compact-output</code> / <code>-c</code>:</p>
<dt>
<dd> By default, jq pretty-prints JSON output. Using this option will result in more compact output by instead putting each JSON object on a single line.</p>
<dt>&#x25cb;</p>
<dd> <code>&#8211;tab</code>:</p>
<dt>
<dd> Use a tab for each indentation level instead of two spaces.</p>
<dt>&#x25cb;</p>
<dd> <code>&#8211;indent n</code>:</p>
<dt>
<dd> Use the given number of spaces (no more than 8) for indentation.</p>
<dt>&#x25cb;</p>
<dd> <code>&#8211;color-output</code> / <code>-C</code> and <code>&#8211;monochrome-output</code> / <code>-M</code>:</p>
<dt>
<dd> By default, jq outputs colored JSON if writing to a terminal. You can force it to produce color even if writing to a pipe or a file using <code>-C</code>, and disable color with <code>-M</code>.</p>
<dt>
<dd> Colors can be configured with the <code>JQ_COLORS</code> environment variable (see below).</p>
<dt>&#x25cb;</p>
<dd> <code>&#8211;ascii-output</code> / <code>-a</code>:</p>
<dt>
<dd> jq usually outputs non-ASCII Unicode codepoints as UTF-8, even if the input specified them as escape sequences (like &quot;μ&quot;). Using this option, you can force jq to produce pure ASCII output with every non-ASCII character replaced with the equivalent escape sequence.</p>
<dt>&#x25cb;</p>
<dd> <code>&#8211;unbuffered</code></p>
<dt>
<dd> Flush the output after each JSON object is printed (useful if you&#8217;re piping a slow data source into jq and piping jq&#8217;s output elsewhere).</p>
<dt>&#x25cb;</p>
<dd> <code>&#8211;sort-keys</code> / <code>-S</code>:</p>
<dt>
<dd> Output the fields of each object with the keys in sorted order.</p>
<dt>&#x25cb;</p>
<dd> <code>&#8211;raw-output</code> / <code>-r</code>:</p>
<dt>
<dd> With this option, if the filter&#8217;s result is a string then it will be written directly to standard output rather than being formatted as a JSON string with quotes. This can be useful for making jq filters talk to non-JSON-based systems.</p>
<dt>&#x25cb;</p>
<dd> <code>&#8211;join-output</code> / <code>-j</code>:</p>
<dt>
<dd> Like <code>-r</code> but jq won&#8217;t print a newline after each output.</p>
<dt>&#x25cb;</p>
<dd> <code>-f filename</code> / <code>&#8211;from-file filename</code>:</p>
<dt>
<dd> Read filter from the file rather than from a command line, like awk&#8217;s -f option. You can also use &#8216;#&#8217; to make comments.</p>
<dt>&#x25cb;</p>
<dd> <code>-Ldirectory</code> / <code>-L directory</code>:</p>
<dt>
<dd> Prepend <code>directory</code> to the search list for modules. If this option is used then no builtin search list is used. See the section on modules below.</p>
<dt>&#x25cb;</p>
<dd> <code>-e</code> / <code>&#8211;exit-status</code>:</p>
<dt>
<dd> Sets the exit status of jq to 0 if the last output values was neither <code>false</code> nor <code>null</code>, 1 if the last output value was either <code>false</code> or <code>null</code>, or 4 if no valid result was ever produced. Normally jq exits with 2 if there was any usage problem or system error, 3 if there was a jq program compile error, or 0 if the jq program ran.</p>
<dt>
<dd> Another way to set the exit status is with the <code>halt_error</code> builtin function.</p>
<dt>&#x25cb;</p>
<dd> <code>&#8211;arg name value</code>:</p>
<dt>
<dd> This option passes a value to the jq program as a predefined variable. If you run jq with <code>&#8211;arg foo bar</code>, then <code>$foo</code> is available in the program and has the value <code>&quot;bar&quot;</code>. Note that <code>value</code> will be treated as a string, so <code>&#8211;arg foo 123</code> will bind <code>$foo</code> to <code>&quot;123&quot;</code>.</p>
<dt>
<dd> Named arguments are also available to the jq program as <code>$ARGS.named</code>.</p>
<dt>&#x25cb;</p>
<dd> <code>&#8211;argjson name JSON-text</code>:</p>
<dt>
<dd> This option passes a JSON-encoded value to the jq program as a predefined variable. If you run jq with <code>&#8211;argjson foo 123</code>, then <code>$foo</code> is available in the program and has the value <code>123</code>.</p>
<dt>&#x25cb;</p>
<dd> <code>&#8211;slurpfile variable-name filename</code>:</p>
<dt>
<dd> This option reads all the JSON texts in the named file and binds an array of the parsed JSON values to the given global variable. If you run jq with <code>&#8211;slurpfile foo bar</code>, then <code>$foo</code> is available in the program and has an array whose elements correspond to the texts in the file named <code>bar</code>.</p>
<dt>&#x25cb;</p>
<dd> <code>&#8211;rawfile variable-name filename</code>:</p>
<dt>
<dd> This option reads in the named file and binds its contents to the given global variable. If you run jq with <code>&#8211;rawfile foo bar</code>, then <code>$foo</code> is available in the program and has a string whose contents are to the texs in the file named <code>bar</code>.</p>
<dt>&#x25cb;</p>
<dd> <code>&#8211;argfile variable-name filename</code>:</p>
<dt>
<dd> Do not use. Use <code>&#8211;slurpfile</code> instead.</p>
<dt>
<dd> (This option is like <code>&#8211;slurpfile</code>, but when the file has just one text, then that is used, else an array of texts is used as in <code>&#8211;slurpfile</code>.)</p>
<dt>&#x25cb;</p>
<dd> <code>&#8211;args</code>:</p>
<dt>
<dd> Remaining arguments are positional string arguments. These are available to the jq program as <code>$ARGS.positional[]</code>.</p>
<dt>&#x25cb;</p>
<dd> <code>&#8211;jsonargs</code>:</p>
<dt>
<dd> Remaining arguments are positional JSON text arguments. These are available to the jq program as <code>$ARGS.positional[]</code>.</p>
<dt>&#x25cb;</p>
<dd> <code>&#8211;run-tests [filename]</code>:</p>
<dt>
<dd> Runs the tests in the given file or standard input. This must be the last option given and does not honor all preceding options. The input consists of comment lines, empty lines, and program lines followed by one input line, as many lines of output as are expected (one per output), and a terminating empty line. Compilation failure tests start with a line containing only &quot;%%FAIL&quot;, then a line containing the program to compile, then a line containing an error message to compare to the actual.</p>
<dt>
<dd> Be warned that this option can change backwards-incompatibly.</p>
<dt>
<dd></dl>
<h2>BASIC FILTERS</h2>
<h3>Identity: .</h3>
<p> The absolute simplest filter is <code>.</code> . This is a filter that takes its input and produces it unchanged as output. That is, this is the identity operator. </p>
<p> Since jq by default pretty-prints all output, this trivial program can be a useful way of formatting JSON output from, say, <code>curl</code>.</p>
<dl>
<dt>
<dd>
<pre>
jq '.'
   &quot;Hello, world!&quot;
=&gt; &quot;Hello, world!&quot;
</pre>
<dt>
<dd></dl>
<h3>Object Identifier-Index: .foo, .foo.bar</h3>
<p> The simplest <i>useful</i> filter is <code>.foo</code>. When given a JSON object (aka dictionary or hash) as input, it produces the value at the key &quot;foo&quot;, or null if there&#8217;s none present. </p>
<p> A filter of the form <code>.foo.bar</code> is equivalent to <code>.foo|.bar</code>. </p>
<p> This syntax only works for simple, identifier-like keys, that is, keys that are all made of alphanumeric characters and underscore, and which do not start with a digit. </p>
<p> If the key contains special characters, you need to surround it with double quotes like this: <code>.&quot;foo$&quot;</code>, or else <code>.[&quot;foo$&quot;]</code>. </p>
<p> For example <code>.[&quot;foo::bar&quot;]</code> and <code>.[&quot;foo.bar&quot;]</code> work while <code>.foo::bar</code> does not, and <code>.foo.bar</code> means <code>.[&quot;foo&quot;].[&quot;bar&quot;]</code>.</p>
<dl>
<dt>
<dd>
<pre><code>
jq '.foo' {"foo" : 42, "bar" : "less interesting data"} = &gt; 42 jq '.foo' {"notfoo" : true, "alsonotfoo" : false} = &gt; null
                                                                                                                         jq '.["foo"]' {"foo" : 42} = &gt; 42
</code></pre>
<dt>
<dd></dl>
<h3>Optional Object Identifier-Index: .foo?</h3>
<p> Just like <code>.foo</code>, but does not output even an error when <code>.</code> is not an array or an object.</p>
<dl>
<dt>
<dd>
jq &#8216;.foo?&#8217; {&#8220;foo&#8221; : 42, &#8220;bar&#8221; : &#8220;less interesting data&#8221;} = &gt; 42 jq &#8216;.foo?&#8217; {&#8220;notfoo&#8221; : true, &#8220;alsonotfoo&#8221; : false} = &gt; null<br />
                                                                                                                           jq &#8216;.[&#8220;foo&#8221;]?&#8217; {&#8220;foo&#8221; : 42} = &gt; 42 jq &#8216;[.foo?]&#8217;<br />
                                                                                                                                                               [1, 2] = &gt; []</p>
<dt>
<dd></dl>
<h3>Generic Object Index: .[&lt;string&gt;]</h3>
<p> You can also look up fields of an object using syntax like <code>.[&quot;foo&quot;]</code> (.foo above is a shorthand version of this, but only for identifier-like strings).</p>
<h3>Array Index: .[2]</h3>
<p> When the index value is an integer, <code>.[&lt;value&gt;]</code> can index arrays. Arrays are zero-based, so <code>.[2]</code> returns the third element. </p>
<p> Negative indices are allowed, with -1 referring to the last element, -2 referring to the next to last element, and so on.</p>
<dl>
<dt>
<dd>
jq &#8216;.[0]&#8217;<br />
    [{&#8220;name&#8221; : &#8220;JSON&#8221;, &#8220;good&#8221; : true}, {&#8220;name&#8221; : &#8220;XML&#8221;, &#8220;good&#8221; : false}] = &gt; {&#8220;name&#8221; : &#8220;JSON&#8221;, &#8220;good&#8221; : true} jq &#8216;.[2]&#8217;<br />
                                                                                 [{&#8220;name&#8221; : &#8220;JSON&#8221;, &#8220;good&#8221; : true}, {&#8220;name&#8221; : &#8220;XML&#8221;, &#8220;good&#8221; : false}] = &gt; null<br />
                                                                                                                                                              jq &#8216;.[-2]&#8217;<br />
                                                                                                                                                                  [1, 2, 3] = &gt; 2</p>
<dt>
<dd></dl>
<h3>Array/String Slice: .[10:15]</h3>
<p> The <code>.[10:15]</code> syntax can be used to return a subarray of an array or substring of a string. The array returned by <code>.[10:15]</code> will be of length 5, containing the elements from index 10 (inclusive) to index 15 (exclusive). Either index may be negative (in which case it counts backwards from the end of the array), or omitted (in which case it refers to the start or end of the array).</p>
<dl>
<dt>
<dd>
jq &#8216;.[2:4]&#8217;<br />
    [&#8220;a&#8221;, &#8220;b&#8221;, &#8220;c&#8221;, &#8220;d&#8221;, &#8220;e&#8221;] = &gt; [ &#8220;c&#8221;, &#8220;d&#8221; ] jq &#8216;.[2:4]&#8217; &#8220;abcdefghi&#8221; = &gt; &#8220;cd&#8221; jq &#8216;.[:3]&#8217;<br />
                                                                               [&#8220;a&#8221;, &#8220;b&#8221;, &#8220;c&#8221;, &#8220;d&#8221;, &#8220;e&#8221;] = &gt; [ &#8220;a&#8221;, &#8220;b&#8221;, &#8220;c&#8221; ] jq &#8216;.[-2:]&#8217;<br />
                                                                                                                 [&#8220;a&#8221;, &#8220;b&#8221;, &#8220;c&#8221;, &#8220;d&#8221;, &#8220;e&#8221;] = &gt; [ &#8220;d&#8221;, &#8220;e&#8221; ]</p>
<dt>
<dd></dl>
<h3>Array/Object Value Iterator: .[]</h3>
<p> If you use the <code>.[index]</code> syntax, but omit the index entirely, it will return <i>all</i> of the elements of an array. Running <code>.[]</code> with the input <code>[1,2,3]</code> will produce the numbers as three separate results, rather than as a single array. </p>
<p> You can also use this on an object, and it will return all the values of the object.</p>
<dl>
<dt>
<dd>
jq &#8216;.[]&#8217;<br />
    [{&#8220;name&#8221; : &#8220;JSON&#8221;, &#8220;good&#8221; : true}, {&#8220;name&#8221; : &#8220;XML&#8221;, &#8220;good&#8221; : false}] = &gt; {&#8220;name&#8221; : &#8220;JSON&#8221;, &#8220;good&#8221; : true},<br />
                                                                 {&#8220;name&#8221; : &#8220;XML&#8221;, &#8220;good&#8221; : false} jq &#8216;.[]&#8217;<br />
                                                                     [] = &gt;<br />
                                                                          jq &#8216;.[]&#8217; {&#8220;a&#8221; : 1, &#8220;b&#8221; : 1} = &gt; 1,<br />
                                                                 1</p>
<dt>
<dd></dl>
<h3>.[]?</h3>
<p> Like <code>.[]</code>, but no errors will be output if . is not an array or object.</p>
<h3>Comma: ,</h3>
<p> If two filters are separated by a comma, then the same input will be fed into both and the two filters&#8217; output value streams will be concatenated in order: first, all of the outputs produced by the left expression, and then all of the outputs produced by the right. For instance, filter <code>.foo, .bar</code>, produces both the &quot;foo&quot; fields and &quot;bar&quot; fields as separate outputs.</p>
<dl>
<dt>
<dd>
jq &#8216;.foo, .bar&#8217; {&#8220;foo&#8221; : 42, &#8220;bar&#8221; : &#8220;something else&#8221;, &#8220;baz&#8221; : true} = &gt; 42, &#8220;something else&#8221; jq &#8216;.user, .projects[]&#8217; {&#8220;user&#8221; : &#8220;stedolan&#8221;, &#8220;projects&#8221; : [ &#8220;jq&#8221;, &#8220;wikiflow&#8221; ]} = &gt; &#8220;stedolan&#8221;, &#8220;jq&#8221;, &#8220;wikiflow&#8221; jq &#8216;.[4,2]'[&#8220;a&#8221;, &#8220;b&#8221;, &#8220;c&#8221;, &#8220;d&#8221;, &#8220;e&#8221;] = &gt; &#8220;e&#8221;, &#8220;c&#8221;</p>
<dt>
<dd></dl>
<h3>Pipe: |</h3>
<p> The | operator combines two filters by feeding the output(s) of the one on the left into the input of the one on the right. It&#8217;s pretty much the same as the Unix shell&#8217;s pipe, if you&#8217;re used to that. </p>
<p> If the one on the left produces multiple results, the one on the right will be run for each of those results. So, the expression <code>.[] | .foo</code> retrieves the &quot;foo&quot; field of each element of the input array. </p>
<p> Note that <code>.a.b.c</code> is the same as <code>.a | .b | .c</code>. </p>
<p> Note too that <code>.</code> is the input value at the particular stage in a &quot;pipeline&quot;, specifically: where the <code>.</code> expression appears. Thus <code>.a | . | .b</code> is the same as <code>.a.b</code>, as the <code>.</code> in the middle refers to whatever value <code>.a</code> produced.</p>
<dl>
<dt>
<dd>
jq &#8216;.[] | .name&#8217;<br />
    [{&#8220;name&#8221; : &#8220;JSON&#8221;, &#8220;good&#8221; : true}, {&#8220;name&#8221; : &#8220;XML&#8221;, &#8220;good&#8221; : false}] = &gt; &#8220;JSON&#8221;,<br />
                                                                 &#8220;XML&#8221;</p>
<dt>
<dd></dl>
<h3>Parenthesis</h3>
<p> Parenthesis work as a grouping operator just as in any typical programming language.</p>
<dl>
<dt>
<dd>
<pre>
jq '(. + 2) * 5'
   1
=&gt; 15
</pre>
<dt>
<dd></dl>
<h2>TYPES AND VALUES</h2>
<p> jq supports the same set of datatypes as JSON &#8211; numbers, strings, booleans, arrays, objects (which in JSON-speak are hashes with only string keys), and &quot;null&quot;. </p>
<p> Booleans, null, strings and numbers are written the same way as in javascript. Just like everything else in jq, these simple values take an input and produce an output &#8211; <code>42</code> is a valid jq expression that takes an input, ignores it, and returns 42 instead.</p>
<h3>Array construction: []</h3>
<p> As in JSON, <code>[]</code> is used to construct arrays, as in <code>[1,2,3]</code>. The elements of the arrays can be any jq expression, including a pipeline. All of the results produced by all of the expressions are collected into one big array. You can use it to construct an array out of a known quantity of values (as in <code>[.foo, .bar, .baz]</code>) or to &quot;collect&quot; all the results of a filter into an array (as in <code>[.items[].name]</code>) </p>
<p> Once you understand the &quot;,&quot; operator, you can look at jq&#8217;s array syntax in a different light: the expression <code>[1,2,3]</code> is not using a built-in syntax for comma-separated arrays, but is instead applying the <code>[]</code> operator (collect results) to the expression 1,2,3 (which produces three different results). </p>
<p> If you have a filter <code>X</code> that produces four results, then the expression <code>[X]</code> will produce a single result, an array of four elements.</p>
<dl>
<dt>
<dd>
jq &#8216;[.user, .projects[]]&#8217; {&#8220;user&#8221; : &#8220;stedolan&#8221;, &#8220;projects&#8221; : [ &#8220;jq&#8221;, &#8220;wikiflow&#8221; ]} = &gt; [ &#8220;stedolan&#8221;, &#8220;jq&#8221;, &#8220;wikiflow&#8221; ] jq &#8216;[ .[] | . * 2]&#8217;<br />
                                                                                           [1, 2, 3] = &gt; [ 2, 4, 6 ]</p>
<dt>
<dd></dl>
<h3>Object Construction: {}</h3>
<p> Like JSON, <code>{}</code> is for constructing objects (aka dictionaries or hashes), as in: <code>{&quot;a&quot;: 42, &quot;b&quot;: 17}</code>. </p>
<p> If the keys are &quot;identifier-like&quot;, then the quotes can be left off, as in <code>{a:42, b:17}</code>. Keys generated by expressions need to be parenthesized, e.g., <code>{(&quot;a&quot;+&quot;b&quot;):59}</code>. </p>
<p> The value can be any expression (although you may need to wrap it in parentheses if it&#8217;s a complicated one), which gets applied to the {} expression&#8217;s input (remember, all filters have an input and an output).</p>
<dl>
<dt>
<dd>
<pre>
{foo: .bar}
</pre>
<dt>
<dd></dl>
<p> will produce the JSON object <code>{&quot;foo&quot;: 42}</code> if given the JSON object <code>{&quot;bar&quot;:42, &quot;baz&quot;:43}</code> as its input. You can use this to select particular fields of an object: if the input is an object with &quot;user&quot;, &quot;title&quot;, &quot;id&quot;, and &quot;content&quot; fields and you just want &quot;user&quot; and &quot;title&quot;, you can write</p>
<dl>
<dt>
<dd>
<pre>
{user: .user, title: .title}
</pre>
<dt>
<dd></dl>
<p> Because that is so common, there&#8217;s a shortcut syntax for it: <code>{user, title}</code>. </p>
<p> If one of the expressions produces multiple results, multiple dictionaries will be produced. If the input&#8217;s</p>
<dl>
<dt>
<dd>
{<br />
    &#8220;user&#8221; : &#8220;stedolan&#8221;, &#8220;titles&#8221; : [ &#8220;JQ Primer&#8221;, &#8220;More JQ&#8221; ]<br />
}</p>
<dt>
<dd></dl>
<p> then the expression</p>
<dl>
<dt>
<dd>
{<br />
    user, title :.titles[]<br />
}</p>
<dt>
<dd></dl>
<p> will produce two outputs:</p>
<dl>
<dt>
<dd>
{&#8220;user&#8221; : &#8220;stedolan&#8221;, &#8220;title&#8221; : &#8220;JQ Primer&#8221;} {<br />
    &#8220;user&#8221; : &#8220;stedolan&#8221;, &#8220;title&#8221; : &#8220;More JQ&#8221;<br />
}</p>
<dt>
<dd></dl>
<p> Putting parentheses around the key means it will be evaluated as an expression. With the same input as above,</p>
<dl>
<dt>
<dd>
<pre>
{(.user): .titles}
</pre>
<dt>
<dd></dl>
<p> produces</p>
<dl>
<dt>
<dd>
{&#8220;stedolan&#8221; : [ &#8220;JQ Primer&#8221;, &#8220;More JQ&#8221; ]} jq &#8216;{user, title: .titles[]}&#8217; {&#8220;user&#8221; : &#8220;stedolan&#8221;, &#8220;titles&#8221; : [ &#8220;JQ Primer&#8221;, &#8220;More JQ&#8221; ]} = &gt; {&#8220;user&#8221; : &#8220;stedolan&#8221;, &#8220;title&#8221; : &#8220;JQ Primer&#8221;}, {&#8220;user&#8221; : &#8220;stedolan&#8221;, &#8220;title&#8221; : &#8220;More JQ&#8221;} jq &#8216;{(.user): .titles}&#8217; {&#8220;user&#8221; : &#8220;stedolan&#8221;, &#8220;titles&#8221; : [ &#8220;JQ Primer&#8221;, &#8220;More JQ&#8221; ]} = &gt;<br />
{<br />
    &#8220;stedolan&#8221; : [ &#8220;JQ Primer&#8221;, &#8220;More JQ&#8221; ]<br />
}</p>
<dt>
<dd></dl>
<h3>Recursive Descent: ..</h3>
<p> Recursively descends <code>.</code>, producing every value. This is the same as the zero-argument <code>recurse</code> builtin (see below). This is intended to resemble the XPath <code>//</code> operator. Note that <code>..a</code> does not work; use <code>..|.a</code> instead. In the example below we use <code>..|.a?</code> to find all the values of object keys &quot;a&quot; in any object found &quot;below&quot; <code>.</code>. </p>
<p> This is particularly useful in conjunction with <code>path(EXP)</code> (also see below) and the <code>?</code> operator.</p>
<dl>
<dt>
<dd>
jq &#8216;..|.a?&#8217;<br />
    [[ {&#8220;a&#8221; : 1} ]] = &gt; 1</p>
<dt>
<dd></dl>
<h2>BUILTIN OPERATORS AND FUNCTIONS</h2>
<p> Some jq operator (for instance, <code>+</code>) do different things depending on the type of their arguments (arrays, numbers, etc.). However, jq never does implicit type conversions. If you try to add a string to an object you&#8217;ll get an error message and no result.</p>
<h3>Addition: +</h3>
<p> The operator <code>+</code> takes two filters, applies them both to the same input, and adds the results together. What &quot;adding&quot; means depends on the types involved:</p>
<dl>
<dt>&#x25cb;</p>
<dd> <code>Numbers</code> are added by normal arithmetic.</p>
<dt>&#x25cb;</p>
<dd> <code>Arrays</code> are added by being concatenated into a larger array.</p>
<dt>&#x25cb;</p>
<dd> <code>Strings</code> are added by being joined into a larger string.</p>
<dt>&#x25cb;</p>
<dd> <code>Objects</code> are added by merging, that is, inserting all the key-value pairs from both objects into a single combined object. If both objects contain a value for the same key, the object on the right of the <code>+</code> wins. (For recursive merge use the <code>*</code> operator.)</p>
<dt>
<dd></dl>
<p> <code>null</code> can be added to any value, and returns the other value unchanged.</p>
<dl>
<dt>
<dd>
jq &#8216;.a + 1&#8217; {&#8220;a&#8221; : 7} = &gt; 8 jq &#8216;.a + .b&#8217; {&#8220;a&#8221; : [ 1, 2 ], &#8220;b&#8221; : [ 3, 4 ]} = &gt; [ 1, 2, 3, 4 ] jq &#8216;.a + null&#8217; {&#8220;a&#8221; : 1} = &gt; 1 jq &#8216;.a + 1&#8217; {} = &gt; 1 jq &#8216;{a: 1} + {b: 2} + {c: 3} + {a: 42}&#8217; null = &gt;<br />
{<br />
    &#8220;a&#8221; : 42, &#8220;b&#8221; : 2, &#8220;c&#8221; : 3<br />
}</p>
<dt>
<dd></dl>
<h3>Subtraction: &#8211;</h3>
<p> As well as normal arithmetic subtraction on numbers, the <code>&#8211;</code> operator can be used on arrays to remove all occurrences of the second array&#8217;s elements from the first array.</p>
<dl>
<dt>
<dd>
jq &#8216;4 &#8211; .a&#8217; {&#8220;a&#8221; : 3} = &gt; 1 jq &#8216;. &#8211; [&#8220;xml&#8221;, &#8220;yaml&#8221;]&#8217;<br />
                              [&#8220;xml&#8221;, &#8220;yaml&#8221;, &#8220;json&#8221;] = &gt; [&#8220;json&#8221;]</p>
<dt>
<dd></dl>
<h3>Multiplication, division, modulo: *, /, and %</h3>
<p> These infix operators behave as expected when given two numbers. Division by zero raises an error. <code>x % y</code> computes x modulo y. </p>
<p> Multiplying a string by a number produces the concatenation of that string that many times. <code>&quot;x&quot; * 0</code> produces <code>null</code>. </p>
<p> Dividing a string by another splits the first using the second as separators. </p>
<p> Multiplying two objects will merge them recursively: this works like addition but if both objects contain a value for the same key, and the values are objects, the two are merged with the same strategy.</p>
<dl>
<dt>
<dd>
jq &#8217;10 / . * 3&#8242; 5 = &gt; 6 jq &#8216;. / &#8220;, &#8220;&#8216; &#8220;a, b,c,d, e&#8221; = &gt; [ &#8220;a&#8221;, &#8220;b,c,d&#8221;, &#8220;e&#8221; ] jq &#8216;{&#8220;k&#8221;: {&#8220;a&#8221;: 1, &#8220;b&#8221;: 2}} * {&#8220;k&#8221;: {&#8220;a&#8221;: 0,&#8221;c&#8221;: 3}}&#8217; null = &gt;<br />
{<br />
    &#8220;k&#8221;:<br />
    {<br />
        &#8220;a&#8221; : 0, &#8220;b&#8221; : 2, &#8220;c&#8221; : 3<br />
    }<br />
}<br />
jq &#8216;.[] | (1 / .)?&#8217;<br />
    [1, 0, -1] = &gt; 1,<br />
           -1</p>
<dt>
<dd></dl>
<h3>length</h3>
<p> The builtin function <code>length</code> gets the length of various different types of value:</p>
<dl>
<dt>&#x25cb;</p>
<dd> The length of a <code>string</code> is the number of Unicode codepoints it contains (which will be the same as its JSON-encoded length in bytes if it&#8217;s pure ASCII).</p>
<dt>&#x25cb;</p>
<dd> The length of an <code>array</code> is the number of elements.</p>
<dt>&#x25cb;</p>
<dd> The length of an <code>object</code> is the number of key-value pairs.</p>
<dt>&#x25cb;</p>
<dd> The length of <code>null</code> is zero.</p>
<dt>
<dd> jq &#8216;.[] | length&#8217; [[1,2], &quot;string&quot;, {&quot;a&quot;:2}, null] =&gt; 2, 6, 1, 0</p>
<dt>
<dd></dl>
<h3>utf8bytelength</h3>
<p> The builtin function <code>utf8bytelength</code> outputs the number of bytes used to encode a string in UTF-8.</p>
<dl>
<dt>
<dd>
<pre>
jq 'utf8bytelength'
   &quot;μ&quot;
=&gt; 2
</pre>
<dt>
<dd></dl>
<h3>keys, keys_unsorted</h3>
<p> The builtin function <code>keys</code>, when given an object, returns its keys in an array. </p>
<p> The keys are sorted &quot;alphabetically&quot;, by unicode codepoint order. This is not an order that makes particular sense in any particular language, but you can count on it being the same for any two objects with the same set of keys, regardless of locale settings. </p>
<p> When <code>keys</code> is given an array, it returns the valid indices for that array: the integers from 0 to length-1. </p>
<p> The <code>keys_unsorted</code> function is just like <code>keys</code>, but if the input is an object then the keys will not be sorted, instead the keys will roughly be in insertion order.</p>
<dl>
<dt>
<dd>
jq &#8216;keys&#8217; {&#8220;abc&#8221; : 1, &#8220;abcd&#8221; : 2, &#8220;Foo&#8221; : 3} = &gt; [ &#8220;Foo&#8221;, &#8220;abc&#8221;, &#8220;abcd&#8221; ] jq &#8216;keys&#8217;<br />
                                                     [42, 3, 35] = &gt; [ 0, 1, 2 ]</p>
<dt>
<dd></dl>
<h3>has(key)</h3>
<p> The builtin function <code>has</code> returns whether the input object has the given key, or the input array has an element at the given index. </p>
<p> <code>has($key)</code> has the same effect as checking whether <code>$key</code> is a member of the array returned by <code>keys</code>, although <code>has</code> will be faster.</p>
<dl>
<dt>
<dd>
jq &#8216;map(has(&#8220;foo&#8221;))&#8217;<br />
    [{&#8220;foo&#8221; : 42}, {}] = &gt; [ true, false ] jq &#8216;map(has(2))&#8217;<br />
                               [[ 0, 1 ], [ &#8220;a&#8221;, &#8220;b&#8221;, &#8220;c&#8221; ]] = &gt; [ false, true ]</p>
<dt>
<dd></dl>
<h3>in</h3>
<p> The builtin function <code>in</code> returns whether or not the input key is in the given object, or the input index corresponds to an element in the given array. It is, essentially, an inversed version of <code>has</code>.</p>
<dl>
<dt>
<dd>
jq &#8216;.[] | in({&#8220;foo&#8221;: 42})&#8217;<br />
    [&#8220;foo&#8221;, &#8220;bar&#8221;] = &gt; true,<br />
            false jq &#8216;map(in([0,1]))&#8217;<br />
                [2, 0] = &gt; [ false, true ]</p>
<dt>
<dd></dl>
<h3>map(x), map_values(x)</h3>
<p> For any filter <code>x</code>, <code>map(x)</code> will run that filter for each element of the input array, and return the outputs in a new array. <code>map(.+1)</code> will increment each element of an array of numbers. </p>
<p> Similarly, <code>map_values(x)</code> will run that filter for each element, but it will return an object when an object is passed. </p>
<p> <code>map(x)</code> is equivalent to <code>[.[] | x]</code>. In fact, this is how it&#8217;s defined. Similarly, <code>map_values(x)</code> is defined as <code>.[] |= x</code>.</p>
<dl>
<dt>
<dd>
jq &#8216;map(.+1)&#8217;<br />
    [1, 2, 3] = &gt; [ 2, 3, 4 ] jq &#8216;map_values(.+1)&#8217; {&#8220;a&#8221; : 1, &#8220;b&#8221; : 2, &#8220;c&#8221; : 3} = &gt;<br />
{<br />
    &#8220;a&#8221; : 2, &#8220;b&#8221; : 3, &#8220;c&#8221; : 4<br />
}</p>
<dt>
<dd></dl>
<h3>path(path_expression)</h3>
<p> Outputs array representations of the given path expression in <code>.</code>. The outputs are arrays of strings (object keys) and/or numbers (array indices). </p>
<p> Path expressions are jq expressions like <code>.a</code>, but also <code>.[]</code>. There are two types of path expressions: ones that can match exactly, and ones that cannot. For example, <code>.a.b.c</code> is an exact match path expression, while <code>.a[].b</code> is not. </p>
<p> <code>path(exact_path_expression)</code> will produce the array representation of the path expression even if it does not exist in <code>.</code>, if <code>.</code> is <code>null</code> or an array or an object. </p>
<p> <code>path(pattern)</code> will produce array representations of the paths matching <code>pattern</code> if the paths exist in <code>.</code>. </p>
<p> Note that the path expressions are not different from normal expressions. The expression <code>path(..|select(type==&quot;boolean&quot;))</code> outputs all the paths to boolean values in <code>.</code>, and only those paths.</p>
<dl>
<dt>
<dd>
jq &#8216;path(.a[0].b)&#8217; null = &gt; [ &#8220;a&#8221;, 0, &#8220;b&#8221; ] jq &#8216;[path(..)]&#8217; {&#8220;a&#8221; : [ {&#8220;b&#8221; : 1} ]} = &gt; [ [], [&#8220;a&#8221;], [ &#8220;a&#8221;, 0 ], [ &#8220;a&#8221;, 0, &#8220;b&#8221; ] ]</p>
<dt>
<dd></dl>
<h3>del(path_expression)</h3>
<p> The builtin function <code>del</code> removes a key and its corresponding value from an object.</p>
<dl>
<dt>
<dd>
jq &#8216;del(.foo)&#8217; {&#8220;foo&#8221; : 42, &#8220;bar&#8221; : 9001, &#8220;baz&#8221; : 42} = &gt; {&#8220;bar&#8221; : 9001, &#8220;baz&#8221; : 42} jq &#8216;del(.[1, 2])&#8217;<br />
                                                              [&#8220;foo&#8221;, &#8220;bar&#8221;, &#8220;baz&#8221;] = &gt; [&#8220;foo&#8221;]</p>
<dt>
<dd></dl>
<h3>getpath(PATHS)</h3>
<p> The builtin function <code>getpath</code> outputs the values in <code>.</code> found at each path in <code>PATHS</code>.</p>
<dl>
<dt>
<dd>
jq &#8216;getpath([&#8220;a&#8221;,&#8221;b&#8221;])&#8217; null = &gt; null<br />
                                     jq &#8216;[getpath([&#8220;a&#8221;,&#8221;b&#8221;], [&#8220;a&#8221;,&#8221;c&#8221;])]&#8217; {&#8220;a&#8221; : {&#8220;b&#8221; : 0, &#8220;c&#8221; : 1}} = &gt; [ 0, 1 ]</p>
<dt>
<dd></dl>
<h3>setpath(PATHS; VALUE)</h3>
<p> The builtin function <code>setpath</code> sets the <code>PATHS</code> in <code>.</code> to <code>VALUE</code>.</p>
<dl>
<dt>
<dd>
jq &#8216;setpath([&#8220;a&#8221;,&#8221;b&#8221;]; 1)&#8217; null = &gt;<br />
{<br />
    &#8220;a&#8221;:<br />
    {<br />
        &#8220;b&#8221; : 1<br />
    }<br />
}<br />
jq &#8216;setpath([&#8220;a&#8221;,&#8221;b&#8221;]; 1)&#8217; {&#8220;a&#8221; : {&#8220;b&#8221; : 0}} = &gt;<br />
{<br />
    &#8220;a&#8221;:<br />
    {<br />
        &#8220;b&#8221; : 1<br />
    }<br />
}<br />
jq &#8216;setpath([0,&#8221;a&#8221;]; 1)&#8217; null = &gt; [ {&#8220;a&#8221; : 1} ]</p>
<dt>
<dd></dl>
<h3>delpaths(PATHS)</h3>
<p> The builtin function <code>delpaths</code> sets the <code>PATHS</code> in <code>.</code>. <code>PATHS</code> must be an array of paths, where each path is an array of strings and numbers.</p>
<dl>
<dt>
<dd>
jq &#8216;delpaths([[&#8220;a&#8221;,&#8221;b&#8221;]])&#8217; {&#8220;a&#8221; : {&#8220;b&#8221; : 1}, &#8220;x&#8221; : {&#8220;y&#8221; : 2}} = &gt;<br />
{<br />
    &#8220;a&#8221; : {}, &#8220;x&#8221;:<br />
    {<br />
        &#8220;y&#8221; : 2<br />
    }<br />
}</p>
<dt>
<dd></dl>
<h3>to_entries, from_entries, with_entries</h3>
<p> These functions convert between an object and an array of key-value pairs. If <code>to_entries</code> is passed an object, then for each <code>k: v</code> entry in the input, the output array includes <code>{&quot;key&quot;: k, &quot;value&quot;: v}</code>. </p>
<p> <code>from_entries</code> does the opposite conversion, and <code>with_entries(foo)</code> is a shorthand for <code>to_entries | map(foo) | from_entries</code>, useful for doing some operation to all keys and values of an object. <code>from_entries</code> accepts key, Key, name, Name, value and Value as keys.</p>
<dl>
<dt>
<dd>
jq &#8216;to_entries&#8217; {&#8220;a&#8221; : 1, &#8220;b&#8221; : 2} = &gt; [ {&#8220;key&#8221; : &#8220;a&#8221;, &#8220;value&#8221; : 1}, {&#8220;key&#8221; : &#8220;b&#8221;, &#8220;value&#8221; : 2} ] jq &#8216;from_entries&#8217;<br />
                                           [{&#8220;key&#8221; : &#8220;a&#8221;, &#8220;value&#8221; : 1}, {&#8220;key&#8221; : &#8220;b&#8221;, &#8220;value&#8221; : 2}] = &gt; {&#8220;a&#8221; : 1, &#8220;b&#8221; : 2} jq &#8216;with_entries(.key |= &#8220;KEY_&#8221; + .)&#8217; {&#8220;a&#8221; : 1, &#8220;b&#8221; : 2} = &gt;<br />
{<br />
    &#8220;KEY_a&#8221; : 1, &#8220;KEY_b&#8221; : 2<br />
}</p>
<dt>
<dd></dl>
<h3>select(boolean_expression)</h3>
<p> The function <code>select(foo)</code> produces its input unchanged if <code>foo</code> returns true for that input, and produces no output otherwise. </p>
<p> It&#8217;s useful for filtering lists: <code>[1,2,3] | map(select(. &gt;= 2))</code> will give you <code>[2,3]</code>.</p>
<dl>
<dt>
<dd>
jq &#8216;map(select(. &gt;= 2))&#8217;<br />
    [1, 5, 3, 0, 7] = &gt; [ 5, 3, 7 ] jq &#8216;.[] | select(.id == &#8220;second&#8221;)&#8217;<br />
                            [{&#8220;id&#8221; : &#8220;first&#8221;, &#8220;val&#8221; : 1}, {&#8220;id&#8221; : &#8220;second&#8221;, &#8220;val&#8221; : 2}] = &gt;<br />
{<br />
    &#8220;id&#8221; : &#8220;second&#8221;, &#8220;val&#8221; : 2<br />
}</p>
<dt>
<dd></dl>
<h3>arrays, objects, iterables, booleans, numbers, normals, finites, strings, nulls, values, scalars</h3>
<p> These built-ins select only inputs that are arrays, objects, iterables (arrays or objects), booleans, numbers, normal numbers, finite numbers, strings, null, non-null values, and non-iterables, respectively.</p>
<dl>
<dt>
<dd>
jq &#8216;.[]|numbers&#8217;<br />
    [[], {}, 1, &#8220;foo&#8221;, null, true, false] = &gt; 1</p>
<dt>
<dd></dl>
<h3>empty</h3>
<p> <code>empty</code> returns no results. None at all. Not even <code>null</code>. </p>
<p> It&#8217;s useful on occasion. You&#8217;ll know if you need it :)</p>
<dl>
<dt>
<dd>
jq &#8216;1, empty, 2&#8217; null = &gt; 1, 2 jq &#8216;[1,2,empty,3]&#8217; null = &gt; [ 1, 2, 3 ]</p>
<dt>
<dd></dl>
<h3>error(message)</h3>
<p> Produces an error, just like <code>.a</code> applied to values other than null and objects would, but with the given message as the error&#8217;s value. Errors can be caught with try/catch; see below.</p>
<h3>halt</h3>
<p> Stops the jq program with no further outputs. jq will exit with exit status <code>0</code>.</p>
<h3>halt_error, halt_error(exit_code)</h3>
<p> Stops the jq program with no further outputs. The input will be printed on <code>stderr</code> as raw output (i.e., strings will not have double quotes) with no decoration, not even a newline. </p>
<p> The given <code>exit_code</code> (defaulting to <code>5</code>) will be jq&#8217;s exit status. </p>
<p> For example, <code>&quot;Error: somthing went wrong
&quot;|<a href="/docs/linux/man/1-halt_error/">halt_error</a>(1)</code>.</p>
<h3>$__loc__</h3>
<p> Produces an object with a &quot;file&quot; key and a &quot;line&quot; key, with the filename and line number where <code>$__loc__</code> occurs, as values.</p>
<dl>
<dt>
<dd>
<pre>
jq 'try error(&quot;\($__loc__)&quot;) catch .'
   null
=&gt; &quot;{\&quot;file\&quot;:\&quot;&lt;top-level&gt;\&quot;,\&quot;line\&quot;:1}&quot;
</pre>
<dt>
<dd></dl>
<h3>paths, paths(node_filter), leaf_paths</h3>
<p> <code>paths</code> outputs the paths to all the elements in its input (except it does not output the empty list, representing . itself). </p>
<p> <code>paths(f)</code> outputs the paths to any values for which <code>f</code> is true. That is, <code>paths(numbers)</code> outputs the paths to all numeric values. </p>
<p> <code>leaf_paths</code> is an alias of <code>paths(scalars)</code>; <code>leaf_paths</code> is <i>deprecated</i> and will be removed in the next major release.</p>
<dl>
<dt>
<dd>
jq &#8216;[paths]&#8217;<br />
    [1, [ [], {&#8220;a&#8221; : 2} ]] = &gt; [ [0], [1], [ 1, 0 ], [ 1, 1 ], [ 1, 1, &#8220;a&#8221; ] ] jq &#8216;[paths(scalars)]&#8217;<br />
                                   [1, [ [], {&#8220;a&#8221; : 2} ]] = &gt; [ [0], [ 1, 1, &#8220;a&#8221; ] ]</p>
<dt>
<dd></dl>
<h3>add</h3>
<p> The filter <code>add</code> takes as input an array, and produces as output the elements of the array added together. This might mean summed, concatenated or merged depending on the types of the elements of the input array &#8211; the rules are the same as those for the <code>+</code> operator (described above). </p>
<p> If the input is an empty array, <code>add</code> returns <code>null</code>.</p>
<dl>
<dt>
<dd>
jq &#8216;add&#8217;<br />
    [&#8220;a&#8221;, &#8220;b&#8221;, &#8220;c&#8221;] = &gt; &#8220;abc&#8221; jq &#8216;add&#8217;<br />
                            [1, 2, 3] = &gt; 6 jq &#8216;add&#8217;<br />
                                              [] = &gt; null</p>
<dt>
<dd></dl>
<h3>any, any(condition), any(generator; condition)</h3>
<p> The filter <code>any</code> takes as input an array of boolean values, and produces <code>true</code> as output if any of the elements of the array are <code>true</code>. </p>
<p> If the input is an empty array, <code>any</code> returns <code>false</code>. </p>
<p> The <code>any(condition)</code> form applies the given condition to the elements of the input array. </p>
<p> The <code>any(generator; condition)</code> form applies the given condition to all the outputs of the given generator.</p>
<dl>
<dt>
<dd>
jq &#8216;any&#8217;<br />
    [true, false] = &gt; true jq &#8216;any&#8217;<br />
                          [false, false] = &gt; false jq &#8216;any&#8217;<br />
                                                 [] = &gt; false</p>
<dt>
<dd></dl>
<h3>all, all(condition), all(generator; condition)</h3>
<p> The filter <code>all</code> takes as input an array of boolean values, and produces <code>true</code> as output if all of the elements of the array are <code>true</code>. </p>
<p> The <code>all(condition)</code> form applies the given condition to the elements of the input array. </p>
<p> The <code>all(generator; condition)</code> form applies the given condition to all the outputs of the given generator. </p>
<p> If the input is an empty array, <code>all</code> returns <code>true</code>.</p>
<dl>
<dt>
<dd>
jq &#8216;all&#8217;<br />
    [true, false] = &gt; false jq &#8216;all&#8217;<br />
                          [true, true] = &gt; true jq &#8216;all&#8217;<br />
                                               [] = &gt; true</p>
<dt>
<dd></dl>
<h3>flatten, flatten(depth)</h3>
<p> The filter <code>flatten</code> takes as input an array of nested arrays, and produces a flat array in which all arrays inside the original array have been recursively replaced by their values. You can pass an argument to it to specify how many levels of nesting to flatten. </p>
<p> <code><a href="/docs/linux/man/2-flatten/">flatten</a>(2)</code> is like <code>flatten</code>, but going only up to two levels deep.</p>
<dl>
<dt>
<dd>
jq &#8216;flatten&#8217;<br />
    [1, [2], [[3]]] = &gt; [ 1, 2, 3 ] jq &#8216;flatten(1)&#8217;<br />
                            [1, [2], [[3]]] = &gt; [ 1, 2, [3] ] jq &#8216;flatten&#8217;<br />
                                                    [[]] = &gt; [] jq &#8216;flatten&#8217;<br />
                                                                 [{&#8220;foo&#8221; : &#8220;bar&#8221;}, [ {&#8220;foo&#8221; : &#8220;baz&#8221;} ]] = &gt; [ {&#8220;foo&#8221; : &#8220;bar&#8221;}, {&#8220;foo&#8221; : &#8220;baz&#8221;} ]</p>
<dt>
<dd></dl>
<h3>range(upto), range(from;upto) range(from;upto;by)</h3>
<p> The <code>range</code> function produces a range of numbers. <code>range(4;10)</code> produces 6 numbers, from 4 (inclusive) to 10 (exclusive). The numbers are produced as separate outputs. Use <code>[range(4;10)]</code> to get a range as an array. </p>
<p> The one argument form generates numbers from 0 to the given number, with an increment of 1. </p>
<p> The two argument form generates numbers from <code>from</code> to <code>upto</code> with an increment of 1. </p>
<p> The three argument form generates numbers <code>from</code> to <code>upto</code> with an increment of <code>by</code>.</p>
<dl>
<dt>
<dd>
jq &#8216;range(2;4)&#8217; null = &gt; 2, 3 jq &#8216;[range(2;4)]&#8217; null = &gt; [ 2, 3 ] jq &#8216;[range(4)]&#8217; null = &gt; [ 0, 1, 2, 3 ] jq &#8216;[range(0;10;3)]&#8217; null = &gt; [ 0, 3, 6, 9 ] jq &#8216;[range(0;10;-1)]&#8217; null = &gt; [] jq &#8216;[range(0;-5;-1)]&#8217; null = &gt; [ 0, -1, -2, -3, -4 ]</p>
<dt>
<dd></dl>
<h3>floor</h3>
<p> The <code>floor</code> function returns the floor of its numeric input.</p>
<dl>
<dt>
<dd>
<pre>
jq 'floor'
   3.14159
=&gt; 3
</pre>
<dt>
<dd></dl>
<h3>sqrt</h3>
<p> The <code>sqrt</code> function returns the square root of its numeric input.</p>
<dl>
<dt>
<dd>
<pre>
jq 'sqrt'
   9
=&gt; 3
</pre>
<dt>
<dd></dl>
<h3>tonumber</h3>
<p> The <code>tonumber</code> function parses its input as a number. It will convert correctly-formatted strings to their numeric equivalent, leave numbers alone, and give an error on all other input.</p>
<dl>
<dt>
<dd>
jq &#8216;.[] | tonumber&#8217;<br />
    [1, &#8220;1&#8221;] = &gt; 1,<br />
        1</p>
<dt>
<dd></dl>
<h3>tostring</h3>
<p> The <code>tostring</code> function prints its input as a string. Strings are left unchanged, and all other values are JSON-encoded.</p>
<dl>
<dt>
<dd>
jq &#8216;.[] | tostring&#8217;<br />
    [1, &#8220;1&#8221;, [1]] = &gt; &#8220;1&#8221;,<br />
             &#8220;1&#8221;, &#8220;[1]&#8221;</p>
<dt>
<dd></dl>
<h3>type</h3>
<p> The <code>type</code> function returns the type of its argument as a string, which is one of null, boolean, number, string, array or object.</p>
<dl>
<dt>
<dd>
jq &#8216;map(type)&#8217;<br />
    [0, false, [], {}, null, &#8220;hello&#8221;] = &gt; [ &#8220;number&#8221;, &#8220;boolean&#8221;, &#8220;array&#8221;, &#8220;object&#8221;, &#8220;null&#8221;, &#8220;string&#8221; ]</p>
<dt>
<dd></dl>
<h3>infinite, nan, isinfinite, isnan, isfinite, isnormal</h3>
<p> Some arithmetic operations can yield infinities and &quot;not a number&quot; (NaN) values. The <code>isinfinite</code> builtin returns <code>true</code> if its input is infinite. The <code>isnan</code> builtin returns <code>true</code> if its input is a NaN. The <code>infinite</code> builtin returns a positive infinite value. The <code>nan</code> builtin returns a NaN. The <code>isnormal</code> builtin returns true if its input is a normal number. </p>
<p> Note that division by zero raises an error. </p>
<p> Currently most arithmetic operations operating on infinities, NaNs, and sub-normals do not raise errors.</p>
<dl>
<dt>
<dd>
jq &#8216;.[] | (infinite * .) &lt; 0&#8217;<br />
    [-1, 1] = &gt; true,<br />
         false jq &#8216;infinite, nan | type&#8217; null = &gt; &#8220;number&#8221;, &#8220;number&#8221;</p>
<dt>
<dd></dl>
<h3>sort, sort_by(path_expression)</h3>
<p> The <code>sort</code> functions sorts its input, which must be an array. Values are sorted in the following order:</p>
<dl>
<dt>&#x25cb;</p>
<dd> <code>null</code></p>
<dt>&#x25cb;</p>
<dd> <code>false</code></p>
<dt>&#x25cb;</p>
<dd> <code>true</code></p>
<dt>&#x25cb;</p>
<dd> numbers</p>
<dt>&#x25cb;</p>
<dd> strings, in alphabetical order (by unicode codepoint value)</p>
<dt>&#x25cb;</p>
<dd> arrays, in lexical order</p>
<dt>&#x25cb;</p>
<dd> objects</p>
<dt>
<dd></dl>
<p> The ordering for objects is a little complex: first they&#8217;re compared by comparing their sets of keys (as arrays in sorted order), and if their keys are equal then the values are compared key by key. </p>
<p> <code>sort</code> may be used to sort by a particular field of an object, or by applying any jq filter. </p>
<p> <code>sort_by(foo)</code> compares two elements by comparing the result of <code>foo</code> on each element.</p>
<dl>
<dt>
<dd>
jq &#8216;sort&#8217;<br />
    [8, 3, null, 6] = &gt; [ null, 3, 6, 8 ] jq &#8216;sort_by(.foo)&#8217;<br />
                            [{&#8220;foo&#8221; : 4, &#8220;bar&#8221; : 10}, {&#8220;foo&#8221; : 3, &#8220;bar&#8221; : 100}, {&#8220;foo&#8221; : 2, &#8220;bar&#8221; : 1}] = &gt; [ {&#8220;foo&#8221; : 2, &#8220;bar&#8221; : 1}, {&#8220;foo&#8221; : 3, &#8220;bar&#8221; : 100}, {&#8220;foo&#8221; : 4, &#8220;bar&#8221; : 10} ]</p>
<dt>
<dd></dl>
<h3>group_by(path_expression)</h3>
<p> <code>group_by(.foo)</code> takes as input an array, groups the elements having the same <code>.foo</code> field into separate arrays, and produces all of these arrays as elements of a larger array, sorted by the value of the <code>.foo</code> field. </p>
<p> Any jq expression, not just a field access, may be used in place of <code>.foo</code>. The sorting order is the same as described in the <code>sort</code> function above.</p>
<dl>
<dt>
<dd>
jq &#8216;group_by(.foo)&#8217;<br />
    [{&#8220;foo&#8221; : 1, &#8220;bar&#8221; : 10}, {&#8220;foo&#8221; : 3, &#8220;bar&#8221; : 100}, {&#8220;foo&#8221; : 1, &#8220;bar&#8221; : 1}] = &gt; [ [ {&#8220;foo&#8221; : 1, &#8220;bar&#8221; : 10}, {&#8220;foo&#8221; : 1, &#8220;bar&#8221; : 1} ], [ {&#8220;foo&#8221; : 3, &#8220;bar&#8221; : 100} ] ]</p>
<dt>
<dd></dl>
<h3>min, max, min_by(path_exp), max_by(path_exp)</h3>
<p> Find the minimum or maximum element of the input array. </p>
<p> The <code>min_by(path_exp)</code> and <code>max_by(path_exp)</code> functions allow you to specify a particular field or property to examine, e.g. <code>min_by(.foo)</code> finds the object with the smallest <code>foo</code> field.</p>
<dl>
<dt>
<dd>
jq &#8216;min&#8217;<br />
    [5, 4, 2, 7] = &gt; 2 jq &#8216;max_by(.foo)&#8217;<br />
                         [{&#8220;foo&#8221; : 1, &#8220;bar&#8221; : 14}, {&#8220;foo&#8221; : 2, &#8220;bar&#8221; : 3}] = &gt;<br />
{<br />
    &#8220;foo&#8221; : 2, &#8220;bar&#8221; : 3<br />
}</p>
<dt>
<dd></dl>
<h3>unique, unique_by(path_exp)</h3>
<p> The <code>unique</code> function takes as input an array and produces an array of the same elements, in sorted order, with duplicates removed. </p>
<p> The <code>unique_by(path_exp)</code> function will keep only one element for each value obtained by applying the argument. Think of it as making an array by taking one element out of every group produced by <code>group</code>.</p>
<dl>
<dt>
<dd>
jq &#8216;unique&#8217;<br />
    [1, 2, 5, 3, 5, 3, 1, 3] = &gt; [ 1, 2, 3, 5 ] jq &#8216;unique_by(.foo)&#8217;<br />
                                     [{&#8220;foo&#8221; : 1, &#8220;bar&#8221; : 2}, {&#8220;foo&#8221; : 1, &#8220;bar&#8221; : 3}, {&#8220;foo&#8221; : 4, &#8220;bar&#8221; : 5}] = &gt; [ {&#8220;foo&#8221; : 1, &#8220;bar&#8221; : 2}, {&#8220;foo&#8221; : 4, &#8220;bar&#8221; : 5} ] jq &#8216;unique_by(length)&#8217;<br />
                                                                                                                      [&#8220;chunky&#8221;, &#8220;bacon&#8221;, &#8220;kitten&#8221;, &#8220;cicada&#8221;, &#8220;asparagus&#8221;] = &gt; [ &#8220;bacon&#8221;, &#8220;chunky&#8221;, &#8220;asparagus&#8221; ]</p>
<dt>
<dd></dl>
<h3>reverse</h3>
<p> This function reverses an array.</p>
<dl>
<dt>
<dd>
jq &#8216;reverse&#8217;<br />
    [1, 2, 3, 4] = &gt; [ 4, 3, 2, 1 ]</p>
<dt>
<dd></dl>
<h3>contains(element)</h3>
<p> The filter <code>contains(b)</code> will produce true if b is completely contained within the input. A string B is contained in a string A if B is a substring of A. An array B is contained in an array A if all elements in B are contained in any element in A. An object B is contained in object A if all of the values in B are contained in the value in A with the same key. All other types are assumed to be contained in each other if they are equal.</p>
<dl>
<dt>
<dd>
jq &#8216;contains(&#8220;bar&#8221;)&#8217; &#8220;foobar&#8221; = &gt; true jq &#8216;contains([&#8220;baz&#8221;, &#8220;bar&#8221;])&#8217;<br />
                                      [&#8220;foobar&#8221;, &#8220;foobaz&#8221;, &#8220;blarp&#8221;] = &gt; true jq &#8216;contains([&#8220;bazzzzz&#8221;, &#8220;bar&#8221;])&#8217;<br />
                                                                            [&#8220;foobar&#8221;, &#8220;foobaz&#8221;, &#8220;blarp&#8221;] = &gt; false jq &#8216;contains({foo: 12, bar: [{barp: 12}]})&#8217; {&#8220;foo&#8221; : 12, &#8220;bar&#8221; : [ 1, 2, {&#8220;barp&#8221; : 12, &#8220;blip&#8221; : 13} ]} = &gt; true jq &#8216;contains({foo: 12, bar: [{barp: 15}]})&#8217; {&#8220;foo&#8221; : 12, &#8220;bar&#8221; : [ 1, 2, {&#8220;barp&#8221; : 12, &#8220;blip&#8221; : 13} ]} = &gt; false</p>
<dt>
<dd></dl>
<h3>indices(s)</h3>
<p> Outputs an array containing the indices in <code>.</code> where <code>s</code> occurs. The input may be an array, in which case if <code>s</code> is an array then the indices output will be those where all elements in <code>.</code> match those of <code>s</code>.</p>
<dl>
<dt>
<dd>
jq &#8216;indices(&#8220;, &#8220;)&#8217; &#8220;a,b, cd, efg, hijk&#8221; = &gt; [ 3, 7, 12 ] jq &#8216;indices(1)&#8217;<br />
                                                [0, 1, 2, 1, 3, 1, 4] = &gt; [ 1, 3, 5 ] jq &#8216;indices([1,2])&#8217;<br />
                                                                              [0, 1, 2, 3, 1, 4, 2, 5, 1, 2, 6, 7] = &gt; [ 1, 8 ]</p>
<dt>
<dd></dl>
<h3>index(s), rindex(s)</h3>
<p> Outputs the index of the first (<code>index</code>) or last (<code>rindex</code>) occurrence of <code>s</code> in the input.</p>
<dl>
<dt>
<dd>
<pre>
jq 'index(&quot;, &quot;)'
   &quot;a,b, cd, efg, hijk&quot;
=&gt; 3
jq 'rindex(&quot;, &quot;)'
   &quot;a,b, cd, efg, hijk&quot;
=&gt; 12
</pre>
<dt>
<dd></dl>
<h3>inside</h3>
<p> The filter <code>inside(b)</code> will produce true if the input is completely contained within b. It is, essentially, an inversed version of <code>contains</code>.</p>
<dl>
<dt>
<dd>
jq &#8216;inside(&#8220;foobar&#8221;)&#8217; &#8220;bar&#8221; = &gt; true jq &#8216;inside([&#8220;foobar&#8221;, &#8220;foobaz&#8221;, &#8220;blarp&#8221;])&#8217;<br />
                                    [&#8220;baz&#8221;, &#8220;bar&#8221;] = &gt; true jq &#8216;inside([&#8220;foobar&#8221;, &#8220;foobaz&#8221;, &#8220;blarp&#8221;])&#8217;<br />
                                                           [&#8220;bazzzzz&#8221;, &#8220;bar&#8221;] = &gt; false jq &#8216;inside({&#8220;foo&#8221;: 12, &#8220;bar&#8221;:[1,2,{&#8220;barp&#8221;:12, &#8220;blip&#8221;:13}]})&#8217; {&#8220;foo&#8221; : 12, &#8220;bar&#8221; : [ {&#8220;barp&#8221; : 12} ]} = &gt; true jq &#8216;inside({&#8220;foo&#8221;: 12, &#8220;bar&#8221;:[1,2,{&#8220;barp&#8221;:12, &#8220;blip&#8221;:13}]})&#8217; {&#8220;foo&#8221; : 12, &#8220;bar&#8221; : [ {&#8220;barp&#8221; : 15} ]} = &gt; false</p>
<dt>
<dd></dl>
<h3>startswith(str)</h3>
<p> Outputs <code>true</code> if . starts with the given string argument.</p>
<dl>
<dt>
<dd>
jq &#8216;[.[]|startswith(&#8220;foo&#8221;)]&#8217;<br />
    [&#8220;fo&#8221;, &#8220;foo&#8221;, &#8220;barfoo&#8221;, &#8220;foobar&#8221;, &#8220;barfoob&#8221;] = &gt; [ false, true, false, true, false ]</p>
<dt>
<dd></dl>
<h3>endswith(str)</h3>
<p> Outputs <code>true</code> if . ends with the given string argument.</p>
<dl>
<dt>
<dd>
jq &#8216;[.[]|endswith(&#8220;foo&#8221;)]&#8217;<br />
    [&#8220;foobar&#8221;, &#8220;barfoo&#8221;] = &gt; [ false, true ]</p>
<dt>
<dd></dl>
<h3>combinations, <a href="/docs/linux/man/n-combinations/">combinations</a>(n)</h3>
<p> Outputs all combinations of the elements of the arrays in the input array. If given an argument <code>n</code>, it outputs all combinations of <code>n</code> repetitions of the input array.</p>
<dl>
<dt>
<dd>
jq &#8216;combinations&#8217;<br />
    [[ 1, 2 ], [ 3, 4 ]] = &gt; [ 1, 3 ],<br />
                      [ 1, 4 ], [ 2, 3 ], [ 2, 4 ] jq &#8216;combinations(2)'[0, 1] = &gt; [ 0, 0 ], [ 0, 1 ], [ 1, 0 ], [ 1, 1 ]</p>
<dt>
<dd></dl>
<h3>ltrimstr(str)</h3>
<p> Outputs its input with the given prefix string removed, if it starts with it.</p>
<dl>
<dt>
<dd>
jq &#8216;[.[]|ltrimstr(&#8220;foo&#8221;)]&#8217;<br />
    [&#8220;fo&#8221;, &#8220;foo&#8221;, &#8220;barfoo&#8221;, &#8220;foobar&#8221;, &#8220;afoo&#8221;] = &gt; [ &#8220;fo&#8221;, &#8220;&#8221;, &#8220;barfoo&#8221;, &#8220;bar&#8221;, &#8220;afoo&#8221; ]</p>
<dt>
<dd></dl>
<h3>rtrimstr(str)</h3>
<p> Outputs its input with the given suffix string removed, if it ends with it.</p>
<dl>
<dt>
<dd>
jq &#8216;[.[]|rtrimstr(&#8220;foo&#8221;)]&#8217;<br />
    [&#8220;fo&#8221;, &#8220;foo&#8221;, &#8220;barfoo&#8221;, &#8220;foobar&#8221;, &#8220;foob&#8221;] = &gt; [ &#8220;fo&#8221;, &#8220;&#8221;, &#8220;bar&#8221;, &#8220;foobar&#8221;, &#8220;foob&#8221; ]</p>
<dt>
<dd></dl>
<h3>explode</h3>
<p> Converts an input string into an array of the string&#8217;s codepoint numbers.</p>
<dl>
<dt>
<dd>
<pre>
jq 'explode'
   &quot;foobar&quot;
=&gt; [102,111,111,98,97,114]
</pre>
<dt>
<dd></dl>
<h3>implode</h3>
<p> The inverse of explode.</p>
<dl>
<dt>
<dd>
<pre>
jq 'implode'
   [65, 66, 67]
=&gt; &quot;ABC&quot;
</pre>
<dt>
<dd></dl>
<h3>split(str)</h3>
<p> Splits an input string on the separator argument.</p>
<dl>
<dt>
<dd>
<pre>
jq 'split(&quot;, &quot;)'
   &quot;a, b,c,d, e, &quot;
=&gt; [&quot;a&quot;,&quot;b,c,d&quot;,&quot;e&quot;,&quot;&quot;]
</pre>
<dt>
<dd></dl>
<h3>join(str)</h3>
<p> Joins the array of elements given as input, using the argument as separator. It is the inverse of <code>split</code>: that is, running <code>split(&quot;foo&quot;) | join(&quot;foo&quot;)</code> over any input string returns said input string. </p>
<p> Numbers and booleans in the input are converted to strings. Null values are treated as empty strings. Arrays and objects in the input are not supported.</p>
<dl>
<dt>
<dd>
jq &#8216;join(&#8220;, &#8220;)&#8217;<br />
    [&#8220;a&#8221;, &#8220;b,c,d&#8221;, &#8220;e&#8221;] = &gt; &#8220;a, b,c,d, e&#8221; jq &#8216;join(&#8221; &#8220;)&#8217;<br />
                                [&#8220;a&#8221;, 1, 2.3, true, null, false] = &gt; &#8220;a 1 2.3 true  false&#8221;</p>
<dt>
<dd></dl>
<h3>ascii_downcase, ascii_upcase</h3>
<p> Emit a copy of the input string with its alphabetic characters (a-z and A-Z) converted to the specified case.</p>
<h3>while(cond; update)</h3>
<p> The <code>while(cond; update)</code> function allows you to repeatedly apply an update to <code>.</code> until <code>cond</code> is false. </p>
<p> Note that <code>while(cond; update)</code> is internally defined as a recursive jq function. Recursive calls within <code>while</code> will not consume additional memory if <code>update</code> produces at most one output for each input. See advanced topics below.</p>
<dl>
<dt>
<dd>
jq &#8216;[while(.&lt;100; .*2)]&#8217; 1 = &gt; [ 1, 2, 4, 8, 16, 32, 64 ]</p>
<dt>
<dd></dl>
<h3>until(cond; next)</h3>
<p> The <code>until(cond; next)</code> function allows you to repeatedly apply the expression <code>next</code>, initially to <code>.</code> then to its own output, until <code>cond</code> is true. For example, this can be used to implement a factorial function (see below). </p>
<p> Note that <code>until(cond; next)</code> is internally defined as a recursive jq function. Recursive calls within <code>until()</code> will not consume additional memory if <code>next</code> produces at most one output for each input. See advanced topics below.</p>
<dl>
<dt>
<dd>
jq &#8216;[.,1]|until(.[0] &lt; 1; [.[0] &#8211; 1, .[1] * .[0]])|.[1]&#8217; 4 = &gt; 24</p>
<dt>
<dd></dl>
<h3>recurse(f), recurse, recurse(f; condition), recurse_down</h3>
<p> The <code>recurse(f)</code> function allows you to search through a recursive structure, and extract interesting data from all levels. Suppose your input represents a filesystem:</p>
<dl>
<dt>
<dd>
{<br />
    &#8220;name&#8221; : &#8220;/&#8221;, &#8220;children&#8221; : [<br />
        {&#8220;name&#8221; : &#8220;/bin&#8221;, &#8220;children&#8221; : [<br />
             {&#8220;name&#8221; : &#8220;/bin/ls&#8221;, &#8220;children&#8221; : []},<br />
             {&#8220;name&#8221; : &#8220;/bin/sh&#8221;, &#8220;children&#8221; : []}<br />
         ]},<br />
        {&#8220;name&#8221; : &#8220;/home&#8221;, &#8220;children&#8221; : [<br />
             {&#8220;name&#8221; : &#8220;/home/stephen&#8221;, &#8220;children&#8221; : [<br />
                  {&#8220;name&#8221; : &#8220;/home/stephen/jq&#8221;, &#8220;children&#8221; : []}<br />
              ]}<br />
         ]}<br />
    ]<br />
}</p>
<dt>
<dd></dl>
<p> Now suppose you want to extract all of the filenames present. You need to retrieve <code>.name</code>, <code>.children[].name</code>, <code>.children[].children[].name</code>, and so on. You can do this with:</p>
<dl>
<dt>
<dd>
<pre>
recurse(.children[]) | .name
</pre>
<dt>
<dd></dl>
<p> When called without an argument, <code>recurse</code> is equivalent to <code>recurse(.[]?)</code>. </p>
<p> <code>recurse(f)</code> is identical to <code>recurse(f; . != null)</code> and can be used without concerns about recursion depth. </p>
<p> <code>recurse(f; condition)</code> is a generator which begins by emitting . and then emits in turn .|f, .|f|f, .|f|f|f, &#8230; so long as the computed value satisfies the condition. For example, to generate all the integers, at least in principle, one could write <code>recurse(.+1; true)</code>. </p>
<p> For legacy reasons, <code>recurse_down</code> exists as an alias to calling <code>recurse</code> without arguments. This alias is considered <i>deprecated</i> and will be removed in the next major release. </p>
<p> The recursive calls in <code>recurse</code> will not consume additional memory whenever <code>f</code> produces at most a single output for each input.</p>
<dl>
<dt>
<dd>
jq &#8216;recurse(.foo[])&#8217; {&#8220;foo&#8221; : [ {&#8220;foo&#8221; : []}, {&#8220;foo&#8221; : [ {&#8220;foo&#8221; : []} ]} ]} = &gt; {&#8220;foo&#8221; : [ {&#8220;foo&#8221; : []}, {&#8220;foo&#8221; : [ {&#8220;foo&#8221; : []} ]} ]}, {&#8220;foo&#8221; : []}, {&#8220;foo&#8221; : [ {&#8220;foo&#8221; : []} ]}, {&#8220;foo&#8221; : []} jq &#8216;recurse&#8217; {&#8220;a&#8221; : 0, &#8220;b&#8221; : [1]} = &gt; {&#8220;a&#8221; : 0, &#8220;b&#8221; : [1]}, 0, [1], 1 jq &#8216;recurse(. * .; . &lt; 20)&#8217; 2 = &gt; 2, 4, 16</p>
<dt>
<dd></dl>
<h3>walk(f)</h3>
<p> The <code>walk(f)</code> function applies f recursively to every component of the input entity. When an array is encountered, f is first applied to its elements and then to the array itself; when an object is encountered, f is first applied to all the values and then to the object. In practice, f will usually test the type of its input, as illustrated in the following examples. The first example highlights the usefulness of processing the elements of an array of arrays before processing the array itself. The second example shows how all the keys of all the objects within the input can be considered for alteration.</p>
<dl>
<dt>
<dd>
jq &#8216;walk(if type == &#8220;array&#8221; then sort else . end)&#8217;<br />
    [[ 4, 1, 7 ], [ 8, 5, 2 ], [ 3, 6, 9 ]] = &gt; [ [ 1, 4, 7 ], [ 2, 5, 8 ], [ 3, 6, 9 ] ] jq &#8216;walk( if type == &#8220;object&#8221; then with_entries( .key |= sub( &#8220;^_+&#8221;; &#8220;&#8221;) ) else . end )&#8217;<br />
                                                    [{&#8220;_a&#8221; : {&#8220;__b&#8221; : 2}}] = &gt; [ {&#8220;a&#8221; : {&#8220;b&#8221; : 2}} ]</p>
<dt>
<dd></dl>
<h3>$ENV, env</h3>
<p> <code>$ENV</code> is an object representing the environment variables as set when the jq program started. </p>
<p> <code>env</code> outputs an object representing jq&#8217;s current environment. </p>
<p> At the moment there is no builtin for setting environment variables.</p>
<dl>
<dt>
<dd>
<pre>
jq '$ENV.PAGER'
   null
=&gt; &quot;less&quot;
jq 'env.PAGER'
   null
=&gt; &quot;less&quot;
</pre>
<dt>
<dd></dl>
<h3>transpose</h3>
<p> Transpose a possibly jagged matrix (an array of arrays). Rows are padded with nulls so the result is always rectangular.</p>
<dl>
<dt>
<dd>
jq &#8216;transpose&#8217;<br />
    [[1], [ 2, 3 ]] = &gt; [ [ 1, 2 ], [ null, 3 ] ]</p>
<dt>
<dd></dl>
<h3>bsearch(x)</h3>
<p> bsearch(x) conducts a binary search for x in the input array. If the input is sorted and contains x, then bsearch(x) will return its index in the array; otherwise, if the array is sorted, it will return (-1 &#8211; ix) where ix is an insertion point such that the array would still be sorted after the insertion of x at ix. If the array is not sorted, bsearch(x) will return an integer that is probably of no interest.</p>
<dl>
<dt>
<dd>
jq &#8216;bsearch(0)&#8217;<br />
    [0, 1] = &gt; 0 jq &#8216;bsearch(0)&#8217;<br />
                   [1, 2, 3] = &gt; -1 jq &#8216;bsearch(4) as $ix | if $ix &lt; 0 then .[-(1+$ix)] = 4 else . end&#8217;<br />
                                     [1, 2, 3] = &gt; [ 1, 2, 3, 4 ]</p>
<dt>
<dd></dl>
<h3>String interpolation &#8211; \(foo)</h3>
<p> Inside a string, you can put an expression inside parens after a backslash. Whatever the expression returns will be interpolated into the string.</p>
<dl>
<dt>
<dd>
<pre>
jq '&quot;The input was \(.), which is one less than \(.+1)&quot;'
   42
=&gt; &quot;The input was 42, which is one less than 43&quot;
</pre>
<dt>
<dd></dl>
<h3>Convert to/from JSON</h3>
<p> The <code>tojson</code> and <code>fromjson</code> builtins dump values as JSON texts or parse JSON texts into values, respectively. The tojson builtin differs from tostring in that tostring returns strings unmodified, while tojson encodes strings as JSON strings.</p>
<dl>
<dt>
<dd>
jq &#8216;[.[]|tostring]&#8217;<br />
    [1, &#8220;foo&#8221;, [&#8220;foo&#8221;]] = &gt; [ &#8220;1&#8221;, &#8220;foo&#8221;, &#8220;[\&#8221;foo\&#8221;]&#8221; ] jq &#8216;[.[]|tojson]&#8217;<br />
                                [1, &#8220;foo&#8221;, [&#8220;foo&#8221;]] = &gt; [ &#8220;1&#8221;, &#8220;\&#8221;foo\&#8221;&#8221;, &#8220;[\&#8221;foo\&#8221;]&#8221; ] jq &#8216;[.[]|tojson|fromjson]&#8217;<br />
                                                            [1, &#8220;foo&#8221;, [&#8220;foo&#8221;]] = &gt; [ 1, &#8220;foo&#8221;, [&#8220;foo&#8221;] ]</p>
<dt>
<dd></dl>
<h3>Format strings and escaping</h3>
<p> The <code>@foo</code> syntax is used to format and escape strings, which is useful for building URLs, documents in a language like HTML or XML, and so forth. <code>@foo</code> can be used as a filter on its own, the possible escapings are:</p>
<dl>
<dt><code>@text</code>:</p>
<dd>
<dt><code>@json</code>:</p>
<dd>
<dt><code>@html</code>:</p>
<dd>
<dt><code>@uri</code>:</p>
<dd>
<dt><code>@csv</code>:</p>
<dd>
<dt><code>@tsv</code>:</p>
<dd>
<dt><code>@sh</code>:</p>
<dd>
<dt><code>@base64</code>:</p>
<dd>
<dt><code>@base64d</code>:</p>
<dd>
</dl>
<p> This syntax can be combined with string interpolation in a useful way. You can follow a <code>@foo</code> token with a string literal. The contents of the string literal will <i>not</i> be escaped. However, all interpolations made inside that string literal will be escaped. For instance,</p>
<dl>
<dt>
<dd>
<pre>
@uri &quot;<a rel="nofollow" href="https://www.google.com/search?q=\(.search)">https://www.google.com/search?q=\(.search)</a>&quot;
</pre>
<dt>
<dd></dl>
<p> will produce the following output for the input <code>{&quot;search&quot;:&quot;what is jq?&quot;}</code>:</p>
<dl>
<dt>
<dd>
<pre>
&quot;<a rel="nofollow" href="https://www.google.com/search?q=what%20is%20jq%3F">https://www.google.com/search?q=what%20is%20jq%3F</a>&quot;
</pre>
<dt>
<dd></dl>
<p> Note that the slashes, question mark, etc. in the URL are not escaped, as they were part of the string literal.</p>
<dl>
<dt>
<dd>
<pre>
jq '@html'
   &quot;This works if x &lt; y&quot;
=&gt; &quot;This works if x &amp;lt; y&quot;
jq '@sh &quot;echo \(.)&quot;'
   &quot;O'Hara's Ale&quot;
=&gt; &quot;echo 'O'\''Hara'\''s Ale'&quot;
jq '@base64'
   &quot;This is a message&quot;
=&gt; &quot;VGhpcyBpcyBhIG1lc3NhZ2U=&quot;
jq '@base64d'
   &quot;VGhpcyBpcyBhIG1lc3NhZ2U=&quot;
=&gt; &quot;This is a message&quot;
</pre>
<dt>
<dd></dl>
<h3>Dates</h3>
<p> jq provides some basic date handling functionality, with some high-level and low-level builtins. In all cases these builtins deal exclusively with time in UTC. </p>
<p> The <code>fromdateiso8601</code> builtin parses datetimes in the ISO 8601 format to a number of seconds since the Unix epoch (1970-01-01T00:00:00Z). The <code>todateiso8601</code> builtin does the inverse. </p>
<p> The <code>fromdate</code> builtin parses datetime strings. Currently <code>fromdate</code> only supports ISO 8601 datetime strings, but in the future it will attempt to parse datetime strings in more formats. </p>
<p> The <code>todate</code> builtin is an alias for <code>todateiso8601</code>. </p>
<p> The <code>now</code> builtin outputs the current time, in seconds since the Unix epoch. </p>
<p> Low-level jq interfaces to the C-library time functions are also provided: <code>strptime</code>, <code>strftime</code>, <code>strflocaltime</code>, <code>mktime</code>, <code>gmtime</code>, and <code>localtime</code>. Refer to your host operating system&#8217;s documentation for the format strings used by <code>strptime</code> and <code>strftime</code>. Note: these are not necessarily stable interfaces in jq, particularly as to their localization functionality. </p>
<p> The <code>gmtime</code> builtin consumes a number of seconds since the Unix epoch and outputs a &quot;broken down time&quot; representation of Greenwhich Meridian time as an array of numbers representing (in this order): the year, the month (zero-based), the day of the month (one-based), the hour of the day, the minute of the hour, the second of the minute, the day of the week, and the day of the year &#8212; all one-based unless otherwise stated. The day of the week number may be wrong on some systems for dates before March 1st 1900, or after December 31 2099. </p>
<p> The <code>localtime</code> builtin works like the <code>gmtime</code> builtin, but using the local timezone setting. </p>
<p> The <code>mktime</code> builtin consumes &quot;broken down time&quot; representations of time output by <code>gmtime</code> and <code>strptime</code>. </p>
<p> The <code>strptime(fmt)</code> builtin parses input strings matching the <code>fmt</code> argument. The output is in the &quot;broken down time&quot; representation consumed by <code>gmtime</code> and output by <code>mktime</code>. </p>
<p> The <code>strftime(fmt)</code> builtin formats a time (GMT) with the given format. The <code>strflocaltime</code> does the same, but using the local timezone setting. </p>
<p> The format strings for <code>strptime</code> and <code>strftime</code> are described in typical C library documentation. The format string for ISO 8601 datetime is <code>&quot;%Y-%m-%dT%H:%M:%SZ&quot;</code>. </p>
<p> jq may not support some or all of this date functionality on some systems. In particular, the <code>%u</code> and <code>%j</code> specifiers for <code>strptime(fmt)</code> are not supported on macOS.</p>
<dl>
<dt>
<dd>
<pre>
jq 'fromdate'
   &quot;2015-03-05T23:51:47Z&quot;
=&gt; 1425599507
jq 'strptime(&quot;%Y-%m-%dT%H:%M:%SZ&quot;)'
   &quot;2015-03-05T23:51:47Z&quot;
=&gt; [2015,2,5,23,51,47,4,63]
jq 'strptime(&quot;%Y-%m-%dT%H:%M:%SZ&quot;)|mktime'
   &quot;2015-03-05T23:51:47Z&quot;
=&gt; 1425599507
</pre>
<dt>
<dd></dl>
<h3>SQL-Style Operators</h3>
<p> jq provides a few SQL-style operators.</p>
<dl>
<dt>INDEX(stream; index_expression):</p>
<dd>
<dt>JOIN($idx; stream; idx_expr; join_expr):</p>
<dd>
<dt>JOIN($idx; stream; idx_expr):</p>
<dd>
<dt>JOIN($idx; idx_expr):</p>
<dd>
<dt>IN(s):</p>
<dd>
<dt>IN(source; s):</p>
<dd>
</dl>
<h3>builtins</h3>
<p> Returns a list of all builtin functions in the format <code>name/arity</code>. Since functions with the same name but different arities are considered separate functions, <code>all/0</code>, <code>all/1</code>, and <code>all/2</code> would all be present in the list.</p>
<h2>CONDITIONALS AND COMPARISONS</h2>
<h3>==, !=</h3>
<p> The expression &#8216;a == b&#8217; will produce &#8216;true&#8217; if the result of a and b are equal (that is, if they represent equivalent JSON documents) and &#8216;false&#8217; otherwise. In particular, strings are never considered equal to numbers. If you&#8217;re coming from Javascript, jq&#8217;s == is like Javascript&#8217;s === &#8211; considering values equal only when they have the same type as well as the same value. </p>
<p> != is &quot;not equal&quot;, and &#8216;a != b&#8217; returns the opposite value of &#8216;a == b&#8217;</p>
<dl>
<dt>
<dd>
jq &#8216;.[] == 1&#8217;<br />
    [1, 1.0, &#8220;1&#8221;, &#8220;banana&#8221;] = &gt; true,<br />
                  true, false, false</p>
<dt>
<dd></dl>
<h3>if-then-else</h3>
<p> <code>if A then B else C end</code> will act the same as <code>B</code> if <code>A</code> produces a value other than false or null, but act the same as <code>C</code> otherwise. </p>
<p> Checking for false or null is a simpler notion of &quot;truthiness&quot; than is found in Javascript or Python, but it means that you&#8217;ll sometimes have to be more explicit about the condition you want: you can&#8217;t test whether, e.g. a string is empty using <code>if .name then A else B end</code>, you&#8217;ll need something more like <code>if (.name | length) &gt; 0 then A else B end</code> instead. </p>
<p> If the condition <code>A</code> produces multiple results, then <code>B</code> is evaluated once for each result that is not false or null, and <code>C</code> is evaluated once for each false or null. </p>
<p> More cases can be added to an if using <code>elif A then B</code> syntax.</p>
<dl>
<dt>
<dd>
jq &#8216;if . == 0 then   &#8220;zero&#8221; elif . == 1 then   &#8220;one&#8221; else   &#8220;many&#8221; end&#8217; 2 = &gt; &#8220;many&#8221;</p>
<dt>
<dd></dl>
<h3>&gt;, &gt;=, &lt;=, &lt;</h3>
<p> The comparison operators <code>&gt;</code>, <code>&gt;=</code>, <code>&lt;=</code>, <code>&lt;</code> return whether their left argument is greater than, greater than or equal to, less than or equal to or less than their right argument (respectively). </p>
<p> The ordering is the same as that described for <code>sort</code>, above.</p>
<dl>
<dt>
<dd>
<pre>
jq '. &lt; 5'
   2
=&gt; true
</pre>
<dt>
<dd></dl>
<h3>and/or/not</h3>
<p> jq supports the normal Boolean operators and/or/not. They have the same standard of truth as if expressions &#8211; false and null are considered &quot;false values&quot;, and anything else is a &quot;true value&quot;. </p>
<p> If an operand of one of these operators produces multiple results, the operator itself will produce a result for each input. </p>
<p> <code>not</code> is in fact a builtin function rather than an operator, so it is called as a filter to which things can be piped rather than with special syntax, as in <code>.foo and .bar | not</code>. </p>
<p> These three only produce the values &quot;true&quot; and &quot;false&quot;, and so are only useful for genuine Boolean operations, rather than the common Perl/Python/Ruby idiom of &quot;value_that_may_be_null or default&quot;. If you want to use this form of &quot;or&quot;, picking between two values rather than evaluating a condition, see the &quot;//&quot; operator below.</p>
<dl>
<dt>
<dd>
jq &#8217;42 and &#8220;a string&#8221;&#8216; null = &gt; true jq &#8216;(true, false) or false&#8217; null = &gt; true, false jq &#8216;(true, true) and (true, false)&#8217; null = &gt; true, false, true, false jq &#8216;[true, false | not]&#8217; null = &gt; [ false, true ]</p>
<dt>
<dd></dl>
<h3>Alternative operator: //</h3>
<p> A filter of the form <code>a // b</code> produces the same results as <code>a</code>, if <code>a</code> produces results other than <code>false</code> and <code>null</code>. Otherwise, <code>a // b</code> produces the same results as <code>b</code>. </p>
<p> This is useful for providing defaults: <code>.foo // 1</code> will evaluate to <code>1</code> if there&#8217;s no <code>.foo</code> element in the input. It&#8217;s similar to how <code>or</code> is sometimes used in Python (jq&#8217;s <code>or</code> operator is reserved for strictly Boolean operations).</p>
<dl>
<dt>
<dd>
jq &#8216;.foo // 42&#8217; {&#8220;foo&#8221; : 19} = &gt; 19 jq &#8216;.foo // 42&#8217; {} = &gt; 42</p>
<dt>
<dd></dl>
<h3>try-catch</h3>
<p> Errors can be caught by using <code>try EXP catch EXP</code>. The first expression is executed, and if it fails then the second is executed with the error message. The output of the handler, if any, is output as if it had been the output of the expression to try. </p>
<p> The <code>try EXP</code> form uses <code>empty</code> as the exception handler.</p>
<dl>
<dt>
<dd>
jq &#8216;try .a catch &#8220;. is not an object&#8221;&#8216; true = &gt; &#8220;. is not an object&#8221; jq &#8216;[.[]|try .a]&#8217;<br />
                                                    [{}, true, {&#8220;a&#8221; : 1}] = &gt; [ null, 1 ] jq &#8216;try error(&#8220;some exception&#8221;) catch .&#8217; true = &gt; &#8220;some exception&#8221;</p>
<dt>
<dd></dl>
<h3>Breaking out of control structures</h3>
<p> A convenient use of try/catch is to break out of control structures like <code>reduce</code>, <code>foreach</code>, <code>while</code>, and so on. </p>
<p> For example:</p>
<dl>
<dt>
<dd>
#Repeat an expression until it raises &#8220;break&#8221; as an<br />
#error, then stop repeating without re-raising the error.<br />
#But if the error caught is not &#8220;break&#8221; then re &#8211; raise it.<br />
try repeat(exp) catch.== &#8220;break&#8221; then empty else error;</p>
<dt>
<dd></dl>
<p> jq has a syntax for named lexical labels to &quot;break&quot; or &quot;go (back) to&quot;:</p>
<dl>
<dt>
<dd>
<pre>
label $out | ... break $out ...
</pre>
<dt>
<dd></dl>
<p> The <code>break $label_name</code> expression will cause the program to to act as though the nearest (to the left) <code>label $label_name</code> produced <code>empty</code>. </p>
<p> The relationship between the <code>break</code> and corresponding <code>label</code> is lexical: the label has to be &quot;visible&quot; from the break. </p>
<p> To break out of a <code>reduce</code>, for example:</p>
<dl>
<dt>
<dd>
label $out | reduce.[] as $item(null; if.== false then break $out else&#8230; end)</p>
<dt>
<dd></dl>
<p> The following jq program produces a syntax error:</p>
<dl>
<dt>
<dd>
<pre>
break $out
</pre>
<dt>
<dd></dl>
<p> because no label <code>$out</code> is visible.</p>
<h3>Error Suppression / Optional Operator: ?</h3>
<p> The <code>?</code> operator, used as <code>EXP?</code>, is shorthand for <code>try EXP</code>.</p>
<dl>
<dt>
<dd>
jq &#8216;[.[]|(.a)?]&#8217;<br />
    [{}, true, {&#8220;a&#8221; : 1}] = &gt; [ null, 1 ]</p>
<dt>
<dd></dl>
<h2>REGULAR EXPRESSIONS (PCRE)</h2>
<p> jq uses the Oniguruma regular expression library, as do php, ruby, TextMate, Sublime Text, etc, so the description here will focus on jq specifics. </p>
<p> The jq regex filters are defined so that they can be used using one of these patterns:</p>
<dl>
<dt>
<dd>
STRING | FILTER(REGEX) STRING | FILTER(REGEX; FLAGS) STRING | FILTER([REGEX]) STRING | FILTER([ REGEX, FLAGS ])</p>
<dt>
<dd></dl>
<p> where: * STRING, REGEX and FLAGS are jq strings and subject to jq string interpolation; * REGEX, after string interpolation, should be a valid PCRE regex; * FILTER is one of <code>test</code>, <code>match</code>, or <code>capture</code>, as described below. </p>
<p> FLAGS is a string consisting of one of more of the supported flags:</p>
<dl>
<dt>&#x25cb;</p>
<dd> <code>g</code> &#8211; Global search (find all matches, not just the first)</p>
<dt>&#x25cb;</p>
<dd> <code>i</code> &#8211; Case insensitive search</p>
<dt>&#x25cb;</p>
<dd> <code>m</code> &#8211; Multi line mode (&#8216;.&#8217; will match newlines)</p>
<dt>&#x25cb;</p>
<dd> <code>n</code> &#8211; Ignore empty matches</p>
<dt>&#x25cb;</p>
<dd> <code>p</code> &#8211; Both s and m modes are enabled</p>
<dt>&#x25cb;</p>
<dd> <code>s</code> &#8211; Single line mode (&#8216;^&#8217; -&gt; &#8216;\A&#8217;, &#8216;$&#8217; -&gt; &#8216;\Z&#8217;)</p>
<dt>&#x25cb;</p>
<dd> <code>l</code> &#8211; Find longest possible matches</p>
<dt>&#x25cb;</p>
<dd> <code>x</code> &#8211; Extended regex format (ignore whitespace and comments)</p>
<dt>
<dd></dl>
<p> To match whitespace in an x pattern use an escape such as \s, e.g.</p>
<dl>
<dt>&#x25cb;</p>
<dd> test( &quot;a\sb&quot;, &quot;x&quot; ).</p>
<dt>
<dd></dl>
<p> Note that certain flags may also be specified within REGEX, e.g.</p>
<dl>
<dt>&#x25cb;</p>
<dd>
<dt>
<dd></dl>
<p> evaluates to: true, true, false, false.</p>
<h3>test(val), test(regex; flags)</h3>
<p> Like <code>match</code>, but does not return match objects, only <code>true</code> or <code>false</code> for whether or not the regex matches the input.</p>
<dl>
<dt>
<dd>
jq &#8216;test(&#8220;foo&#8221;)&#8217; &#8220;foo&#8221; = &gt; true jq &#8216;.[] | test(&#8220;a b c # spaces are ignored&#8221;; &#8220;ix&#8221;)&#8217;<br />
                               [&#8220;xabcd&#8221;, &#8220;ABC&#8221;] = &gt; true,<br />
                 true</p>
<dt>
<dd></dl>
<h3>match(val), match(regex; flags)</h3>
<p> <code>match</code> outputs an object for each match it finds. Matches have the following fields:</p>
<dl>
<dt>&#x25cb;</p>
<dd> <code>offset</code> &#8211; offset in UTF-8 codepoints from the beginning of the input</p>
<dt>&#x25cb;</p>
<dd> <code>length</code> &#8211; length in UTF-8 codepoints of the match</p>
<dt>&#x25cb;</p>
<dd> <code>string</code> &#8211; the string that it matched</p>
<dt>&#x25cb;</p>
<dd> <code>captures</code> &#8211; an array of objects representing capturing groups.</p>
<dt>
<dd></dl>
<p> Capturing group objects have the following fields:</p>
<dl>
<dt>&#x25cb;</p>
<dd> <code>offset</code> &#8211; offset in UTF-8 codepoints from the beginning of the input</p>
<dt>&#x25cb;</p>
<dd> <code>length</code> &#8211; length in UTF-8 codepoints of this capturing group</p>
<dt>&#x25cb;</p>
<dd> <code>string</code> &#8211; the string that was captured</p>
<dt>&#x25cb;</p>
<dd> <code>name</code> &#8211; the name of the capturing group (or <code>null</code> if it was unnamed)</p>
<dt>
<dd></dl>
<p> Capturing groups that did not match anything return an offset of -1</p>
<dl>
<dt>
<dd>
jq &#8216;match(&#8220;(abc)+&#8221;; &#8220;g&#8221;)&#8217; &#8220;abc abc&#8221; = &gt; {&#8220;offset&#8221; : 0, &#8220;length&#8221; : 3, &#8220;string&#8221; : &#8220;abc&#8221;, &#8220;captures&#8221; : [ {&#8220;offset&#8221; : 0, &#8220;length&#8221; : 3, &#8220;string&#8221; : &#8220;abc&#8221;, &#8220;name&#8221; : null} ]}, {&#8220;offset&#8221; : 4, &#8220;length&#8221; : 3, &#8220;string&#8221; : &#8220;abc&#8221;, &#8220;captures&#8221; : [ {&#8220;offset&#8221; : 4, &#8220;length&#8221; : 3, &#8220;string&#8221; : &#8220;abc&#8221;, &#8220;name&#8221; : null} ]} jq &#8216;match(&#8220;foo&#8221;)&#8217; &#8220;foo bar foo&#8221; = &gt; {&#8220;offset&#8221; : 0, &#8220;length&#8221; : 3, &#8220;string&#8221; : &#8220;foo&#8221;, &#8220;captures&#8221; : []} jq &#8216;match([&#8220;foo&#8221;, &#8220;ig&#8221;])&#8217; &#8220;foo bar FOO&#8221; = &gt; {&#8220;offset&#8221; : 0, &#8220;length&#8221; : 3, &#8220;string&#8221; : &#8220;foo&#8221;, &#8220;captures&#8221; : []}, {&#8220;offset&#8221; : 8, &#8220;length&#8221; : 3, &#8220;string&#8221; : &#8220;FOO&#8221;, &#8220;captures&#8221; : []} jq &#8216;match(&#8220;foo (?&lt;bar123&gt;bar)? foo&#8221;; &#8220;ig&#8221;)&#8217; &#8220;foo bar foo foo  foo&#8221; = &gt; {&#8220;offset&#8221; : 0, &#8220;length&#8221; : 11, &#8220;string&#8221; : &#8220;foo bar foo&#8221;, &#8220;captures&#8221; : [ {&#8220;offset&#8221; : 4, &#8220;length&#8221; : 3, &#8220;string&#8221; : &#8220;bar&#8221;, &#8220;name&#8221; : &#8220;bar123&#8221;} ]}, {&#8220;offset&#8221; : 12, &#8220;length&#8221; : 8, &#8220;string&#8221; : &#8220;foo  foo&#8221;, &#8220;captures&#8221; : [ {&#8220;offset&#8221; : -1, &#8220;length&#8221; : 0, &#8220;string&#8221; : null, &#8220;name&#8221; : &#8220;bar123&#8221;} ]} jq &#8216;[ match(&#8220;.&#8221;; &#8220;g&#8221;)] | length&#8217; &#8220;abc&#8221; = &gt; 3</p>
<dt>
<dd></dl>
<h3>capture(val), capture(regex; flags)</h3>
<p> Collects the named captures in a JSON object, with the name of each capture as the key, and the matched string as the corresponding value.</p>
<dl>
<dt>
<dd>
jq &#8216;capture(&#8220;(?&lt;a&gt;[a-z]+)-(?&lt;n&gt;[0-9]+)&#8221;)&#8217; &#8220;xyzzy-14&#8221; = &gt;<br />
{<br />
    &#8220;a&#8221; : &#8220;xyzzy&#8221;, &#8220;n&#8221; : &#8220;14&#8221;<br />
}</p>
<dt>
<dd></dl>
<h3>scan(regex), scan(regex; flags)</h3>
<p> Emit a stream of the non-overlapping substrings of the input that match the regex in accordance with the flags, if any have been specified. If there is no match, the stream is empty. To capture all the matches for each input string, use the idiom <code>[ expr ]</code>, e.g. <code>[ scan(regex) ]</code>.</p>
<h3>split(regex; flags)</h3>
<p> For backwards compatibility, <code>split</code> splits on a string, not a regex.</p>
<h3>splits(regex), splits(regex; flags)</h3>
<p> These provide the same results as their <code>split</code> counterparts, but as a stream instead of an array.</p>
<h3>sub(regex; tostring) sub(regex; string; flags)</h3>
<p> Emit the string obtained by replacing the first match of regex in the input string with <code>tostring</code>, after interpolation. <code>tostring</code> should be a jq string, and may contain references to named captures. The named captures are, in effect, presented as a JSON object (as constructed by <code>capture</code>) to <code>tostring</code>, so a reference to a captured variable named &quot;x&quot; would take the form: &quot;(.x)&quot;.</p>
<h3>gsub(regex; string), gsub(regex; string; flags)</h3>
<p> <code>gsub</code> is like <code>sub</code> but all the non-overlapping occurrences of the regex are replaced by the string, after interpolation.</p>
<h2>ADVANCED FEATURES</h2>
<p> Variables are an absolute necessity in most programming languages, but they&#8217;re relegated to an &quot;advanced feature&quot; in jq. </p>
<p> In most languages, variables are the only means of passing around data. If you calculate a value, and you want to use it more than once, you&#8217;ll need to store it in a variable. To pass a value to another part of the program, you&#8217;ll need that part of the program to define a variable (as a function parameter, object member, or whatever) in which to place the data. </p>
<p> It is also possible to define functions in jq, although this is is a feature whose biggest use is defining jq&#8217;s standard library (many jq functions such as <code>map</code> and <code>find</code> are in fact written in jq). </p>
<p> jq has reduction operators, which are very powerful but a bit tricky. Again, these are mostly used internally, to define some useful bits of jq&#8217;s standard library. </p>
<p> It may not be obvious at first, but jq is all about generators (yes, as often found in other languages). Some utilities are provided to help deal with generators. </p>
<p> Some minimal I/O support (besides reading JSON from standard input, and writing JSON to standard output) is available. </p>
<p> Finally, there is a module/library system.</p>
<h3>Variable / Symbolic Binding Operator: &#8230; as $identifier | &#8230;</h3>
<p> In jq, all filters have an input and an output, so manual plumbing is not necessary to pass a value from one part of a program to the next. Many expressions, for instance <code>a + b</code>, pass their input to two distinct subexpressions (here <code>a</code> and <code>b</code> are both passed the same input), so variables aren&#8217;t usually necessary in order to use a value twice. </p>
<p> For instance, calculating the average value of an array of numbers requires a few variables in most languages &#8211; at least one to hold the array, perhaps one for each element or for a loop counter. In jq, it&#8217;s simply <code>add / length</code> &#8211; the <code>add</code> expression is given the array and produces its sum, and the <code>length</code> expression is given the array and produces its length. </p>
<p> So, there&#8217;s generally a cleaner way to solve most problems in jq than defining variables. Still, sometimes they do make things easier, so jq lets you define variables using <code>expression as $variable</code>. All variable names start with <code>$</code>. Here&#8217;s a slightly uglier version of the array-averaging example:</p>
<dl>
<dt>
<dd>
<pre>
length as $array_length | add / $array_length
</pre>
<dt>
<dd></dl>
<p> We&#8217;ll need a more complicated problem to find a situation where using variables actually makes our lives easier. </p>
<p> Suppose we have an array of blog posts, with &quot;author&quot; and &quot;title&quot; fields, and another object which is used to map author usernames to real names. Our input looks like:</p>
<dl>
<dt>
<dd>
{<br />
    &#8220;posts&#8221; : [ {&#8220;title&#8221; : &#8220;Frist psot&#8221;, &#8220;author&#8221; : &#8220;anon&#8221;},<br />
                {&#8220;title&#8221; : &#8220;A well-written article&#8221;, &#8220;author&#8221; : &#8220;person1&#8221;} ],<br />
              &#8220;realnames&#8221;:<br />
    {<br />
        &#8220;anon&#8221; : &#8220;Anonymous Coward&#8221;,<br />
                 &#8220;person1&#8221; : &#8220;Person McPherson&#8221;<br />
    }<br />
}</p>
<dt>
<dd></dl>
<p> We want to produce the posts with the author field containing a real name, as in:</p>
<dl>
<dt>
<dd>
{&#8220;title&#8221; : &#8220;Frist psot&#8221;, &#8220;author&#8221; : &#8220;Anonymous Coward&#8221;} {<br />
    &#8220;title&#8221; : &#8220;A well-written article&#8221;, &#8220;author&#8221; : &#8220;Person McPherson&#8221;<br />
}</p>
<dt>
<dd></dl>
<p> We use a variable, $names, to store the realnames object, so that we can refer to it later when looking up author usernames:</p>
<dl>
<dt>
<dd>
.realnames as $names |.posts[] |<br />
{<br />
    title, author : $names[.author]<br />
}</p>
<dt>
<dd></dl>
<p> The expression <code>exp as $x | &#8230;</code> means: for each value of expression <code>exp</code>, run the rest of the pipeline with the entire original input, and with <code>$x</code> set to that value. Thus <code>as</code> functions as something of a foreach loop. </p>
<p> Just as <code>{foo}</code> is a handy way of writing <code>{foo: .foo}</code>, so <code>{$foo}</code> is a handy way of writing <code>{foo:$foo}</code>. </p>
<p> Multiple variables may be declared using a single <code>as</code> expression by providing a pattern that matches the structure of the input (this is known as &quot;destructuring&quot;):</p>
<dl>
<dt>
<dd>
.as{realnames : $names, posts : [ $first, $second ]} | &#8230;</p>
<dt>
<dd></dl>
<p> The variable declarations in array patterns (e.g., <code>. as [$first, $second]</code>) bind to the elements of the array in from the element at index zero on up, in order. When there is no value at the index for an array pattern element, <code>null</code> is bound to that variable. </p>
<p> Variables are scoped over the rest of the expression that defines them, so</p>
<dl>
<dt>
<dd>
.realnames as $names | (.posts[] | {title, author : $names[.author]})</p>
<dt>
<dd></dl>
<p> will work, but</p>
<dl>
<dt>
<dd>
(.realnames as $names |.posts[]) |<br />
{<br />
    title, author : $names[.author]<br />
}</p>
<dt>
<dd></dl>
<p> won&#8217;t. </p>
<p> For programming language theorists, it&#8217;s more accurate to say that jq variables are lexically-scoped bindings. In particular there&#8217;s no way to change the value of a binding; one can only setup a new binding with the same name, but which will not be visible where the old one was.</p>
<dl>
<dt>
<dd>
jq &#8216;.bar as $x | .foo | . + $x&#8217; {&#8220;foo&#8221; : 10, &#8220;bar&#8221; : 200} = &gt; 210 jq &#8216;. as $i|[(.*2|. as $i| $i), $i]&#8217; 5 = &gt; [ 10, 5 ] jq &#8216;. as [$a, $b, {c: $c}] | $a + $b + $c&#8217;<br />
                                                                                                                 [2, 3, {&#8220;c&#8221; : 4, &#8220;d&#8221; : 5}] = &gt; 9 jq &#8216;.[] as [$a, $b] | {a: $a, b: $b}&#8217;<br />
                                                                                                                                                    [[0], [ 0, 1 ], [ 2, 1, 0 ]] = &gt; {&#8220;a&#8221; : 0, &#8220;b&#8221; : null},<br />
                                                     {&#8220;a&#8221; : 0, &#8220;b&#8221; : 1},<br />
{<br />
    &#8220;a&#8221; : 2, &#8220;b&#8221; : 1<br />
}</p>
<dt>
<dd></dl>
<h3>Destructuring Alternative Operator: ?//</h3>
<p> The destructuring alternative operator provides a concise mechanism for destructuring an input that can take one of several forms. </p>
<p> Suppose we have an API that returns a list of resources and events associated with them, and we want to get the user_id and timestamp of the first event for each resource. The API (having been clumsily converted from XML) will only wrap the events in an array if the resource has multiple events:</p>
<dl>
<dt>
<dd>
{<br />
    &#8220;resources&#8221; : [ {&#8220;id&#8221; : 1, &#8220;kind&#8221; : &#8220;widget&#8221;, &#8220;events&#8221; : {&#8220;action&#8221; : &#8220;create&#8221;, &#8220;user_id&#8221; : 1, &#8220;ts&#8221; : 13}},<br />
                    {&#8220;id&#8221; : 2, &#8220;kind&#8221; : &#8220;widget&#8221;, &#8220;events&#8221; : [ {&#8220;action&#8221; : &#8220;create&#8221;, &#8220;user_id&#8221; : 1, &#8220;ts&#8221; : 14}, {&#8220;action&#8221; : &#8220;destroy&#8221;, &#8220;user_id&#8221; : 1, &#8220;ts&#8221; : 15} ]} ]<br />
}</p>
<dt>
<dd></dl>
<p> We can use the destructuring alternative operator to handle this structural change simply:</p>
<dl>
<dt>
<dd>
.resources[] as{$id, $kind, events : {$user_id, $ts}} ? // {$id, $kind, events: [{$user_id, $ts}]} | {$user_id, $kind, $id, $ts}</p>
<dt>
<dd></dl>
<p> Or, if we aren&#8217;t sure if the input is an array of values or an object:</p>
<dl>
<dt>
<dd>
.[] as[$id, $kind, $user_id, $ts] ? // {$id, $kind, $user_id, $ts} | &#8230;</p>
<dt>
<dd></dl>
<p> Each alternative need not define all of the same variables, but all named variables will be available to the subsequent expression. Variables not matched in the alternative that succeeded will be <code>null</code>:</p>
<dl>
<dt>
<dd>
.resources[] as{$id, $kind, events : {$user_id, $ts}} ? // {$id, $kind, events: [{$first_user_id, $first_ts}]} | {$user_id, $first_user_id, $kind, $id, $ts, $first_ts}</p>
<dt>
<dd></dl>
<p> Additionally, if the subsequent expression returns an error, the alternative operator will attempt to try the next binding. Errors that occur during the final alternative are passed through.</p>
<dl>
<dt>
<dd>
[[3]] |.[] as[$a] ? // [$b] | if $a != null then error(&#8220;err: \($a)&#8221;) else {$a,$b} end<br />
    jq &#8216;.[] as {$a, $b, c: {$d, $e}} ?// {$a, $b, c: [{$d, $e}]} | {$a, $b, $d, $e}&#8217;<br />
        [{&#8220;a&#8221; : 1, &#8220;b&#8221; : 2, &#8220;c&#8221; : {&#8220;d&#8221; : 3, &#8220;e&#8221; : 4}}, {&#8220;a&#8221; : 1, &#8220;b&#8221; : 2, &#8220;c&#8221; : [ {&#8220;d&#8221; : 3, &#8220;e&#8221; : 4} ]}] = &gt; {&#8220;a&#8221; : 1, &#8220;b&#8221; : 2, &#8220;d&#8221; : 3, &#8220;e&#8221; : 4},<br />
                                                                                                     {&#8220;a&#8221; : 1, &#8220;b&#8221; : 2, &#8220;d&#8221; : 3, &#8220;e&#8221; : 4} jq &#8216;.[] as {$a, $b, c: {$d}} ?// {$a, $b, c: [{$e}]} | {$a, $b, $d, $e}&#8217;<br />
                                                                                                         [{&#8220;a&#8221; : 1, &#8220;b&#8221; : 2, &#8220;c&#8221; : {&#8220;d&#8221; : 3, &#8220;e&#8221; : 4}}, {&#8220;a&#8221; : 1, &#8220;b&#8221; : 2, &#8220;c&#8221; : [ {&#8220;d&#8221; : 3, &#8220;e&#8221; : 4} ]}] = &gt; {&#8220;a&#8221; : 1, &#8220;b&#8221; : 2, &#8220;d&#8221; : 3, &#8220;e&#8221; : null},<br />
                                                                                                     {&#8220;a&#8221; : 1, &#8220;b&#8221; : 2, &#8220;d&#8221; : null, &#8220;e&#8221; : 4} jq &#8216;.[] as [$a] ?// [$b] | if $a != null then error(&#8220;err: \($a)&#8221;) else {$a,$b} end&#8217;<br />
                                                                                                         [[3]] = &gt;<br />
{<br />
    &#8220;a&#8221; : null, &#8220;b&#8221; : 3<br />
}</p>
<dt>
<dd></dl>
<h3>Defining Functions</h3>
<p> You can give a filter a name using &quot;def&quot; syntax:</p>
<dl>
<dt>
<dd>
<pre>
def increment: . + 1;
</pre>
<dt>
<dd></dl>
<p> From then on, <code>increment</code> is usable as a filter just like a builtin function (in fact, this is how many of the builtins are defined). A function may take arguments:</p>
<dl>
<dt>
<dd>
<pre>
def map(f): [.[] | f];
</pre>
<dt>
<dd></dl>
<p> Arguments are passed as <i>filters</i> (functions with no arguments), <i>not</i> as values. The same argument may be referenced multiple times with different inputs (here <code>f</code> is run for each element of the input array). Arguments to a function work more like callbacks than like value arguments. This is important to understand. Consider:</p>
<dl>
<dt>
<dd>
<pre>
def foo(f): f|f;
5|foo(.*2)
</pre>
<dt>
<dd></dl>
<p> The result will be 20 because <code>f</code> is <code>.*2</code>, and during the first invocation of <code>f</code> <code>.</code> will be 5, and the second time it will be 10 (5 * 2), so the result will be 20. Function arguments are filters, and filters expect an input when invoked. </p>
<p> If you want the value-argument behaviour for defining simple functions, you can just use a variable:</p>
<dl>
<dt>
<dd>
<pre>
def addvalue(f): f as $f | map(. + $f);
</pre>
<dt>
<dd></dl>
<p> Or use the short-hand:</p>
<dl>
<dt>
<dd>
<pre>
def addvalue($f): ...;
</pre>
<dt>
<dd></dl>
<p> With either definition, <code>addvalue(.foo)</code> will add the current input&#8217;s <code>.foo</code> field to each element of the array. Do note that calling <code>addvalue(.[])</code> will cause the <code>map(. + $f)</code> part to be evaluated once per value in the value of <code>.</code> at the call site. </p>
<p> Multiple definitions using the same function name are allowed. Each re-definition replaces the previous one for the same number of function arguments, but only for references from functions (or main program) subsequent to the re-definition. See also the section below on scoping.</p>
<dl>
<dt>
<dd>
jq &#8216;def addvalue(f): . + [f]; map(addvalue(.[0]))&#8217;<br />
    [[ 1, 2 ], [ 10, 20 ]] = &gt; [ [ 1, 2, 1 ], [ 10, 20, 10 ] ] jq &#8216;def addvalue(f): f as $x | map(. + $x); addvalue(.[0])&#8217;<br />
                                   [[ 1, 2 ], [ 10, 20 ]] = &gt; [ [ 1, 2, 1, 2 ], [ 10, 20, 1, 2 ] ]</p>
<dt>
<dd></dl>
<h3>Scoping</h3>
<p> There are two types of symbols in jq: value bindings (a.k.a., &quot;variables&quot;), and functions. Both are scoped lexically, with expressions being able to refer only to symbols that have been defined &quot;to the left&quot; of them. The only exception to this rule is that functions can refer to themselves so as to be able to create recursive functions. </p>
<p> For example, in the following expression there is a binding which is visible &quot;to the right&quot; of it, <code>&#8230; | .*3 as $times_three | [. + $times_three] | &#8230;</code>, but not &quot;to the left&quot;. Consider this expression now, <code>&#8230; | (.*3 as $times_three | [.+ $times_three]) | &#8230;</code>: here the binding <code>$times_three</code> is <i>not</i> visible past the closing parenthesis.</p>
<h3>Reduce</h3>
<p> The <code>reduce</code> syntax in jq allows you to combine all of the results of an expression by accumulating them into a single answer. As an example, we&#8217;ll pass <code>[3,2,1]</code> to this expression:</p>
<dl>
<dt>
<dd>
<pre>
reduce .[] as $item (0; . + $item)
</pre>
<dt>
<dd></dl>
<p> For each result that <code>.[]</code> produces, <code>. + $item</code> is run to accumulate a running total, starting from 0. In this example, <code>.[]</code> produces the results 3, 2, and 1, so the effect is similar to running something like this:</p>
<dl>
<dt>
<dd>
0 | (3 as $item |.+ $item) |<br />
    (2 as $item |.+ $item) |<br />
    (1 as $item |.+ $item)<br />
        jq &#8216;reduce .[] as $item (0; . + $item)&#8217;<br />
            [10, 2, 5, 3] = &gt; 20</p>
<dt>
<dd></dl>
<h3>isempty(exp)</h3>
<p> Returns true if <code>exp</code> produces no outputs, false otherwise.</p>
<dl>
<dt>
<dd>
<pre>
jq 'isempty(empty)'
   null
=&gt; true
</pre>
<dt>
<dd></dl>
<h3>limit(n; exp)</h3>
<p> The <code>limit</code> function extracts up to <code>n</code> outputs from <code>exp</code>.</p>
<dl>
<dt>
<dd>
jq &#8216;[limit(3;.[])]&#8217;<br />
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] = &gt; [ 0, 1, 2 ]</p>
<dt>
<dd></dl>
<h3>first(expr), last(expr), nth(n; expr)</h3>
<p> The <code>first(expr)</code> and <code>last(expr)</code> functions extract the first and last values from <code>expr</code>, respectively. </p>
<p> The <code>nth(n; expr)</code> function extracts the nth value output by <code>expr</code>. This can be defined as <code>def nth(n; expr): last(limit(n + 1; expr));</code>. Note that <code>nth(n; expr)</code> doesn&#8217;t support negative values of <code>n</code>.</p>
<dl>
<dt>
<dd>
jq &#8216;[first(range(.)), last(range(.)), nth(./2; range(.))]&#8217; 10 = &gt; [ 0, 9, 5 ]</p>
<dt>
<dd></dl>
<h3>first, last, <a href="/docs/linux/man/n-nth/">nth</a>(n)</h3>
<p> The <code>first</code> and <code>last</code> functions extract the first and last values from any array at <code>.</code>. </p>
<p> The <code><a href="/docs/linux/man/n-nth/">nth</a>(n)</code> function extracts the nth value of any array at <code>.</code>.</p>
<dl>
<dt>
<dd>
jq &#8216;[range(.)]|[first, last, nth(5)]&#8217; 10 = &gt; [ 0, 9, 5 ]</p>
<dt>
<dd></dl>
<h3>foreach</h3>
<p> The <code>foreach</code> syntax is similar to <code>reduce</code>, but intended to allow the construction of <code>limit</code> and reducers that produce intermediate results (see example). </p>
<p> The form is <code>foreach EXP as $var (INIT; UPDATE; EXTRACT)</code>. Like <code>reduce</code>, <code>INIT</code> is evaluated once to produce a state value, then each output of <code>EXP</code> is bound to <code>$var</code>, <code>UPDATE</code> is evaluated for each output of <code>EXP</code> with the current state and with <code>$var</code> visible. Each value output by <code>UPDATE</code> replaces the previous state. Finally, <code>EXTRACT</code> is evaluated for each new state to extract an output of <code>foreach</code>. </p>
<p> This is mostly useful only for constructing <code>reduce</code>&#8211; and <code>limit</code>-like functions. But it is much more general, as it allows for partial reductions (see the example below).</p>
<dl>
<dt>
<dd>
jq &#8216;[foreach .[] as $item ([[],[]]; if $item == null then [[],.[0]] else [(.[0] + [$item]),[]] end; if $item == null then .[1] else empty end)]&#8217;<br />
    [1, 2, 3, 4, null, &#8220;a&#8221;, &#8220;b&#8221;, null] = &gt; [ [ 1, 2, 3, 4 ], [ &#8220;a&#8221;, &#8220;b&#8221; ] ]</p>
<dt>
<dd></dl>
<h3>Recursion</h3>
<p> As described above, <code>recurse</code> uses recursion, and any jq function can be recursive. The <code>while</code> builtin is also implemented in terms of recursion. </p>
<p> Tail calls are optimized whenever the expression to the left of the recursive call outputs its last value. In practice this means that the expression to the left of the recursive call should not produce more than one output for each input. </p>
<p> For example:</p>
<dl>
<dt>
<dd>
def recurse(f)<br />
    : def r :.,<br />
(f | select(.!= null) | r);<br />
r;<br />
def while (cond; update)<br />
    : def _while : if cond then.,<br />
(update | _while) else empty end;<br />
_while;<br />
def repeat(exp)<br />
    : def _repeat : exp, _repeat;<br />
_repeat;</p>
<dt>
<dd></dl>
<h3>Generators and iterators</h3>
<p> Some jq operators and functions are actually generators in that they can produce zero, one, or more values for each input, just as one might expect in other programming languages that have generators. For example, <code>.[]</code> generates all the values in its input (which must be an array or an object), <code>range(0; 10)</code> generates the integers between 0 and 10, and so on. </p>
<p> Even the comma operator is a generator, generating first the values generated by the expression to the left of the comma, then for each of those, the values generate by the expression on the right of the comma. </p>
<p> The <code>empty</code> builtin is the generator that produces zero outputs. The <code>empty</code> builtin backtracks to the preceding generator expression. </p>
<p> All jq functions can be generators just by using builtin generators. It is also possible to define new generators using only recursion and the comma operator. If the recursive call(s) is(are) &quot;in tail position&quot; then the generator will be efficient. In the example below the recursive call by <code>_range</code> to itself is in tail position. The example shows off three advanced topics: tail recursion, generator construction, and sub-functions.</p>
<dl>
<dt>
<dd>
jq &#8216;def range(init; upto; by): def _range: if (by &gt; 0 and . &lt; upto) or (by &lt; 0 and . &gt; upto) then ., ((.+by)|_range) else . end; if by == 0 then init else init|_range end | select((by &gt; 0 and . &lt; upto) or (by &lt; 0 and . &gt; upto)); range(0; 10; 3)&#8217; null = &gt; 0, 3, 6, 9 jq &#8216;def while(cond; update): def _while: if cond then ., (update | _while) else empty end; _while; [while(.&lt;100; .*2)]&#8217; 1 = &gt; [ 1, 2, 4, 8, 16, 32, 64 ]</p>
<dt>
<dd></dl>
<h2>MATH</h2>
<p> jq currently only has IEEE754 double-precision (64-bit) floating point number support. </p>
<p> Besides simple arithmetic operators such as <code>+</code>, jq also has most standard math functions from the C math library. C math functions that take a single input argument (e.g., <code>sin()</code>) are available as zero-argument jq functions. C math functions that take two input arguments (e.g., <code>pow()</code>) are available as two-argument jq functions that ignore <code>.</code>. C math functions that take three input arguments are available as three-argument jq functions that ignore <code>.</code>. </p>
<p> Availability of standard math functions depends on the availability of the corresponding math functions in your operating system and C math library. Unavailable math functions will be defined but will raise an error. </p>
<p> One-input C math functions: <code>acos</code> <code>acosh</code> <code>asin</code> <code>asinh</code> <code>atan</code> <code>atanh</code> <code>cbrt</code> <code>ceil</code> <code>cos</code> <code>cosh</code> <code>erf</code> <code>erfc</code> <code>exp</code> <code>exp10</code> <code>exp2</code> <code>expm1</code> <code>fabs</code> <code>floor</code> <code>gamma</code> <code>j0</code> <code>j1</code> <code>lgamma</code> <code>log</code> <code>log10</code> <code>log1p</code> <code>log2</code> <code>logb</code> <code>nearbyint</code> <code>pow10</code> <code>rint</code> <code>round</code> <code>significand</code> <code>sin</code> <code>sinh</code> <code>sqrt</code> <code>tan</code> <code>tanh</code> <code>tgamma</code> <code>trunc</code> <code>y0</code> <code>y1</code>. </p>
<p> Two-input C math functions: <code>atan2</code> <code>copysign</code> <code>drem</code> <code>fdim</code> <code>fmax</code> <code>fmin</code> <code>fmod</code> <code>frexp</code> <code>hypot</code> <code>jn</code> <code>ldexp</code> <code>modf</code> <code>nextafter</code> <code>nexttoward</code> <code>pow</code> <code>remainder</code> <code>scalb</code> <code>scalbln</code> <code>yn</code>. </p>
<p> Three-input C math functions: <code>fma</code>. </p>
<p> See your system&#8217;s manual for more information on each of these.</p>
<h2>I/O</h2>
<p> At this time jq has minimal support for I/O, mostly in the form of control over when inputs are read. Two builtins functions are provided for this, <code>input</code> and <code>inputs</code>, that read from the same sources (e.g., <code>stdin</code>, files named on the command-line) as jq itself. These two builtins, and jq&#8217;s own reading actions, can be interleaved with each other. </p>
<p> Two builtins provide minimal output capabilities, <code>debug</code>, and <code>stderr</code>. (Recall that a jq program&#8217;s output values are always output as JSON texts on <code>stdout</code>.) The <code>debug</code> builtin can have application-specific behavior, such as for executables that use the libjq C API but aren&#8217;t the jq executable itself. The <code>stderr</code> builtin outputs its input in raw mode to stder with no additional decoration, not even a newline. </p>
<p> Most jq builtins are referentially transparent, and yield constant and repeatable value streams when applied to constant inputs. This is not true of I/O builtins.</p>
<h3>input</h3>
<p> Outputs one new input.</p>
<h3>inputs</h3>
<p> Outputs all remaining inputs, one by one. </p>
<p> This is primarily useful for reductions over a program&#8217;s inputs.</p>
<h3>debug</h3>
<p> Causes a debug message based on the input value to be produced. The jq executable wraps the input value with <code>[&quot;DEBUG:&quot;, &lt;input-value&gt;]</code> and prints that and a newline on stderr, compactly. This may change in the future.</p>
<h3>stderr</h3>
<p> Prints its input in raw and compact mode to stderr with no additional decoration, not even a newline.</p>
<h3>input_filename</h3>
<p> Returns the name of the file whose input is currently being filtered. Note that this will not work well unless jq is running in a UTF-8 locale.</p>
<h3>input_line_number</h3>
<p> Returns the line number of the input currently being filtered.</p>
<h2>STREAMING</h2>
<p> With the <code>&#8211;stream</code> option jq can parse input texts in a streaming fashion, allowing jq programs to start processing large JSON texts immediately rather than after the parse completes. If you have a single JSON text that is 1GB in size, streaming it will allow you to process it much more quickly. </p>
<p> However, streaming isn&#8217;t easy to deal with as the jq program will have <code>[&lt;path&gt;, &lt;leaf-value&gt;]</code> (and a few other forms) as inputs. </p>
<p> Several builtins are provided to make handling streams easier. </p>
<p> The examples below use the streamed form of <code>[0,[1]]</code>, which is <code>[[0],0],[[1,0],1],[[1,0]],[[1]]</code>. </p>
<p> Streaming forms include <code>[&lt;path&gt;, &lt;leaf-value&gt;]</code> (to indicate any scalar value, empty array, or empty object), and <code>[&lt;path&gt;]</code> (to indicate the end of an array or object). Future versions of jq run with <code>&#8211;stream</code> and <code>-seq</code> may output additional forms such as <code>[&quot;error message&quot;]</code> when an input text fails to parse.</p>
<h3>truncate_stream(stream_expression)</h3>
<p> Consumes a number as input and truncates the corresponding number of path elements from the left of the outputs of the given streaming expression.</p>
<dl>
<dt>
<dd>
jq &#8216;[1|truncate_stream([[0],1],[[1,0],2],[[1,0]],[[1]])]&#8217; 1 = &gt; [ [ [0], 2 ], [[0]] ]</p>
<dt>
<dd></dl>
<h3>fromstream(stream_expression)</h3>
<p> Outputs values corresponding to the stream expression&#8217;s outputs.</p>
<dl>
<dt>
<dd>
jq &#8216;fromstream(1|truncate_stream([[0],1],[[1,0],2],[[1,0]],[[1]]))&#8217; null = &gt; [2]</p>
<dt>
<dd></dl>
<h3>tostream</h3>
<p> The <code>tostream</code> builtin outputs the streamed form of its input.</p>
<dl>
<dt>
<dd>
<pre><code>
jq '. as $dot|fromstream($dot|tostream)|.==$dot'
    [0, [ 1, {"a" : 1}, {"b" : 2} ]] = &gt; true
</code></pre>
<dt>
<dd></dl>
<h2>ASSIGNMENT</h2>
<p> Assignment works a little differently in jq than in most programming languages. jq doesn&#8217;t distinguish between references to and copies of something &#8211; two objects or arrays are either equal or not equal, without any further notion of being &quot;the same object&quot; or &quot;not the same object&quot;. </p>
<p> If an object has two fields which are arrays, <code>.foo</code> and <code>.bar</code>, and you append something to <code>.foo</code>, then <code>.bar</code> will not get bigger, even if you&#8217;ve previously set <code>.bar = .foo</code>. If you&#8217;re used to programming in languages like Python, Java, Ruby, Javascript, etc. then you can think of it as though jq does a full deep copy of every object before it does the assignment (for performance it doesn&#8217;t actually do that, but that&#8217;s the general idea). </p>
<p> This means that it&#8217;s impossible to build circular values in jq (such as an array whose first element is itself). This is quite intentional, and ensures that anything a jq program can produce can be represented in JSON. </p>
<p> All the assignment operators in jq have path expressions on the left-hand side (LHS). The right-hand side (RHS) provides values to set to the paths named by the LHS path expressions. </p>
<p> Values in jq are always immutable. Internally, assignment works by using a reduction to compute new, replacement values for <code>.</code> that have had all the desired assignments applied to <code>.</code>, then outputting the modified value. This might be made clear by this example: <code>{a:{b:{c:1}}} | (.a.b|=3), .</code>. This will output <code>{&quot;a&quot;:{&quot;b&quot;:3}}</code> and <code>{&quot;a&quot;:{&quot;b&quot;:{&quot;c&quot;:1}}}</code> because the last sub-expression, <code>.</code>, sees the original value, not the modified value. </p>
<p> Most users will want to use modification assignment operators, such as <code>|=</code> or <code>+=</code>, rather than <code>=</code>. </p>
<p> Note that the LHS of assignment operators refers to a value in <code>.</code>. Thus <code>$var.foo = 1</code> won&#8217;t work as expected (<code>$var.foo</code> is not a valid or useful path expression in <code>.</code>); use <code>$var | .foo = 1</code> instead.</p>

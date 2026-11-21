---

title: "mawk(1)"
name: "mawk"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mawk/"
description: "mawk – pattern scanning and text processing language"
---

<p> <code>mawk</code> [-<code>W </code><i>option</i>] [-<code>F </code><i>value</i>] [-<code>v </code><i>var=value</i>] [--] &#8216;program text&#8217; [file ...] <br />
 <code>mawk</code> [-<code>W </code><i>option</i>] [-<code>F </code><i>value</i>] [-<code>v </code><i>var=value</i>] [-<code>f </code><i>program-file</i>] [--] [file ...]  </p>
<p> <code>mawk</code> is an interpreter for the AWK Programming Language. The AWK language is useful for manipulation of data files, text retrieval and processing, and for prototyping and experimenting with algorithms. <code>mawk</code> is a <i>new awk</i> meaning it implements the AWK language as defined in Aho, Kernighan and Weinberger, <i>The AWK Programming Language,</i> Addison-Wesley Publishing, 1988 (hereafter referred to as the AWK book.) <code>mawk</code> conforms to the POSIX 1003.2 (draft 11.3) definition of the AWK language which contains a few features not described in the AWK book, and <code>mawk</code> provides a small number of extensions. </p>
<p> An AWK program is a sequence of <i>pattern {action}</i> pairs and function definitions. Short programs are entered on the command line usually enclosed in &#8216; &#8216; to avoid shell interpretation. Longer programs can be read in from a file with the -f option. Data input is read from the list of files on the command line or from standard input when the list is empty. The input is broken into records as determined by the record separator variable, <code>RS</code>. Initially, <code>RS</code> = ``\n&#8217;&#8216; and records are synonymous with lines. Each record is compared against each <i>pattern</i> and if it matches, the program text for <i>{action}</i> is executed.  </p>
<h2>OPTIONS</h2>
<dl>
<dt>-<code>F </code><i>value</i></dt>
<dd> <p> sets the field separator, <code>FS</code>, to <i>value</i>. </p>
 </dd>
<dt>-<code>f </code><i>file</dt>
<dd> <p> Program text is read from file</i> instead of from the command line. Multiple <code>-f</code> options are allowed. </p>
 </dd>
<dt>-<code>v </code><i>var=value</i></dt>
<dd> <p> assigns <i>value</i> to program variable <i>var</i>. </p>
 </dd>
<dt>--</dt>
<dd> <p> indicates the unambiguous end of options. </p>
 </dd></dl>
<p> The above options will be available with any POSIX compatible implementation of AWK. Implementation specific options are prefaced with <code>-W</code>. <code>mawk</code> provides these: </p>
<dl>
<dt>-<code>W </code>dump</dt>
<dd> <p> writes an assembler like listing of the internal representation of the program to stdout and exits 0 (on successful compilation). </p>
 </dd>
<dt>-<code>W </code>exec <i>file</dt>
<dd> <p> Program text is read from file</i> and this is the last option. </p>
 </dd>
<dd> <p> This is a useful alternative to -<code>f</code> on systems that support the <code>#!</code> ``magic number&#8217;&#8216; convention for executable scripts. Those implicitly pass the pathname of the script itself as the final parameter, and expect no more than one ``-&#8216;&#8216; option on the <code>#!</code> line. Because <code>mawk</code> can combine multiple -<code>W</code> options separated by commas, you can use this option when an additional -<code>W</code> option is needed. </p>
 </dd>
<dt>-<code>W </code>help</dt>
<dd> <p> prints a usage message to stderr and exits (same as ``-<code>W&nbsp;</code>usage&#8217;&#8216;). </p>
 </dd>
<dt>-<code>W </code>interactive</dt>
<dd> <p> sets unbuffered writes to stdout and line buffered reads from stdin. Records from stdin are lines regardless of the value of <code>RS</code>. </p>
 </dd>
<dt>-<code>W </code>posix_space</dt>
<dd> <p> forces <code>mawk</code> not to consider &#8216;\n&#8217; to be space. </p>
 </dd>
<dt>-<code>W </code>random=<i>num</i></dt>
<dd> <p> calls <code>srand</code> with the given parameter (and overrides the auto-seeding behavior). </p>
 </dd>
<dt>-<code>W </code>sprintf=<i>num</i></dt>
<dd> <p> adjusts the size of <code>mawk</code>&#8216;s internal sprintf buffer to <i>num</i> bytes. More than rare use of this option indicates <code>mawk</code> should be recompiled. </p>
 </dd>
<dt>-<code>W </code>usage</dt>
<dd> <p> prints a usage message to stderr and exits (same as ``-<code>W&nbsp;</code>help&#8217;&#8216;). </p>
 </dd>
<dt>-<code>W </code>version</dt>
<dd> <p> <code>mawk</code> writes its version and copyright to stdout and compiled limits to stderr and exits 0. </p>
 </dd></dl>
<p> <code>mawk</code> accepts abbreviations for any of these options, e.g., ``-<code>W&nbsp;</code>v&#8217;&#8216; and ``-<code>W</code>v&#8217;&#8216; both tell <code>mawk</code> to show its version. </p>
<p> <code>mawk</code> allows multiple <code>-W</code> options to be combined by separating the options with commas, e.g., -Wsprint=2000,posix. This is useful for executable <code>#!</code> ``magic number&#8217;&#8216; invocations in which only one argument is supported, e.g., -<code>Winteractive,exec</code>.  </p>
<h2>THE AWK LANGUAGE</h2>
<h3>1. Program structure</h3>
<p> An AWK program is a sequence of </code><i>pattern {action}</i> pairs and user function definitions. </p>
<p> A pattern can be: </p>
<pre><code>
<dl>
<dd>  BEGIN 
 END expression
expression , expression
 </dd></dl>

</code></pre>
<p> One, but not both, of <i>pattern {action}</i> can be omitted. If <i>{action}</i> is omitted it is implicitly { print }. If <i>pattern</i> is omitted, then it is implicitly matched. <code>BEGIN</code> and <code>END</code> patterns require an action. </p>
<p> Statements are terminated by newlines, semi-colons or both. Groups of statements such as actions or loop bodies are blocked via {&nbsp;...&nbsp;} as in C. The last statement in a block doesn&#8217;t need a terminator. Blank lines have no meaning; an empty statement is terminated with a semi-colon. Long statements can be continued with a backslash, \. A statement can be broken without a backslash after a comma, left brace, &amp;&amp;, ||, <code>do</code>, <code>else</code>, the right parenthesis of an <code>if</code>, <code>while</code> or <code>for</code> statement, and the right parenthesis of a function definition. A comment starts with # and extends to, but does not include the end of line. </p>
<p> The following statements control program flow inside blocks. </p>
<dl>
<dd> <p> <code>if</code> ( <i>expr</i> ) <i>statement</i> </p>
<p> <code>if</code> ( <i>expr</i> ) <i>statement</i> <code>else</code> <i>statement</i> </p>
<p> <code>while</code> ( <i>expr</i> ) <i>statement</i> </p>
<p> <code>do</code> <i>statement</i> <code>while</code> ( <i>expr</i> ) </p>
<p> <code>for</code> ( <i>opt_expr</i> ; <i>opt_expr</i> ; <i>opt_expr</i> ) <i>statement</i> </p>
<p> <code>for</code> ( <i>var </i><code>in </code><i>array</i> ) <i>statement</i> </p>
<p> <code>continue</code> </p>
<p> <code>break</code> </p>
 </dd></dl>
<h3>2. Data types, conversion and comparison</h3>
<p> There are two basic data types, numeric and string. Numeric constants can be integer like -2, decimal like 1.08, or in scientific notation like -1.1e4 or .28E-3. All numbers are represented internally and all computations are done in floating point arithmetic. So for example, the expression 0.2e2 == 20 is true and true is represented as 1.0. </p>
<p> String constants are enclosed in double quotes. </p>
<p> <center> &quot;This is a string with a newline at the end.\n&quot;<br />
 </center> </p>
<p> Strings can be continued across a line by escaping (\) the newline. The following escape sequences are recognized. </code> </p>
<pre><code>        \\ \
        \&quot; &quot;
        \a alert, ascii 7
        \b backspace, ascii 8
        \t tab, ascii 9
        \n newline, ascii 10
        \v vertical tab, ascii 11
        \f formfeed, ascii 12
        \r carriage return, ascii 13
        \ddd 1, 2 or 3 octal digits for ascii ddd
        \xhh 1 or 2 hex digits for ascii hh
</code></pre>
<p> If you escape any other character \c, you get \c, i.e., <code>mawk</code> ignores the escape. </p>
<p> There are really three basic data types; the third is <i>number and string</i> which has both a numeric value and a string value at the same time. User defined variables come into existence when first referenced and are initialized to <i>null</i>, a number and string value which has numeric value 0 and string value &quot;&quot;. Non-trivial number and string typed data come from input and are typically stored in fields. (See section 4). </p>
<p> The type of an expression is determined by its context and automatic type conversion occurs if needed. For example, to evaluate the statements </p>
<pre><code>        y = x + 2 ; z = x &quot;hello&quot;
</code></pre>
<p> The value stored in variable y will be typed numeric. If x is not numeric, the value read from x is converted to numeric before it is added to 2 and stored in y. The value stored in variable z will be typed string, and the value of x will be converted to string if necessary and concatenated with &quot;hello&quot;. (Of course, the value and type stored in x is not changed by any conversions.) A string expression is converted to numeric using its longest numeric prefix as with <code><a href="/docs/linux/man/3-atof/">atof</a></code>(3). A numeric expression is converted to string by replacing <i>expr</i> with <code>sprintf(CONVFMT</code>, <i>expr</i>), unless <i>expr</i> can be represented on the host machine as an exact integer then it is converted to <code>sprintf</code>(&quot;%d&quot;, <i>expr</i>). <code>Sprintf()</code> is an AWK built-in that duplicates the functionality of <code><a href="/docs/linux/man/3-sprintf/">sprintf</a></code>(3), and <code>CONVFMT</code> is a built-in variable used for internal conversion from number to string and initialized to &quot;%.6g&quot;. Explicit type conversions can be forced, <i>expr</i> &quot;&quot; is string and <i>expr</i>+0 is numeric. </p>
<p> To evaluate, <i>expr</i>1 <code>rel-op <i>expr</i>2, if both operands are numeric or number and string then the comparison is numeric; if both operands are string the comparison is string; if one operand is string, the non-string operand is converted and the comparison is string. The result is numeric, 1 or 0. </p>
<p> In boolean contexts such as, if</code> ( <i>expr</i> ) <i>statement</i>, a string expression evaluates true if and only if it is not the empty string &quot;&quot;; numeric values if and only if not numerically zero.  </p>
<h3>3. Regular expressions</h3>
<p> In the AWK language, records, fields and strings are often tested for matching a </code><i>regular expression</i>. Regular expressions are enclosed in slashes, and </p>
<pre><code> expr  ~ / r /
</code></pre>
<p> is an AWK expression that evaluates to 1 if <i>expr</i> ``matches&#8217;&#8216; <i>r</i>, which means a substring of <i>expr</i> is in the set of strings defined by <i>r</i>. With no match the expression evaluates to 0; replacing ~ with the ``not match&#8217;&#8216; operator, !~ , reverses the meaning. As pattern-action pairs, </p>
<pre><code>        / r / { action  } and $0  ~ / r / { action  }
</code></pre>
<p> are the same, and for each input record that matches <i>r</i>, <i>action</i> is executed. In fact, /<i>r</i>/ is an AWK expression that is equivalent to (<code>$0</code> ~ /<i>r</i>/) anywhere except when on the right side of a match operator or passed as an argument to a built-in function that expects a regular expression argument. </p>
<p> AWK uses extended regular expressions as with the <code>-E</code> option of <code><a href="/docs/linux/man/1-grep/">grep</a></code>(1). The regular expression metacharacters, i.e., those with special meaning in regular expressions are </p>
<pre><code>        \ ^ $ . [ ] | ( ) * + ?
</code></pre>
<p> Regular expressions are built up from characters as follows: </p>
<dl>
<dd>  </dd>
<dl>
<dt><i>c</i></dt>
<dd> <p> matches any non-metacharacter <i>c</i>. </p>
 </dd>
<dt>\<i>c</i></dt>
<dd> <p> matches a character defined by the same escape sequences used in string constants or the literal character <i>c</i> if \<i>c</i> is not an escape sequence. </p>
 </dd>
<dt>.</dt>
<dd> <p> matches any character (including newline). </p>
 </dd>
<dt>^</dt>
<dd> <p> matches the front of a string. </p>
 </dd>
<dt>$</dt>
<dd> <p> matches the back of a string. </p>
 </dd>
<dt>[c1c2c3...]</dt>
<dd> <p> matches any character in the class c1c2c3... . An interval of characters is denoted c1-c2 inside a class [...]. </p>
 </dd>
<dt>[^c1c2c3...]</dt>
<dd> <p> matches any character not in the class c1c2c3... </p>
 </dd></dl>
</dl>
<p> Regular expressions are built up from other regular expressions as follows: </p>
<dl>
<dd>  </dd>
<dl>
<dt><i>r</i>1 <i>r</i>2</dt>
<dd> <p> matches <i>r</i>1 followed immediately by <i>r</i>2 (concatenation). </p>
 </dd>
<dt><i>r</i>1 | <i>r</i>2</dt>
<dd> <p> matches <i>r</i>1 or <i>r</i>2 (alternation). </p>
 </dd>
<dt><i>r</i>*</dt>
<dd> <p> matches <i>r</i> repeated zero or more times. </p>
 </dd>
<dt><i>r</i>+</dt>
<dd> <p> matches <i>r</i> repeated one or more times. </p>
 </dd>
<dt><i>r</i>?</dt>
<dd> <p> matches <i>r</i> zero or once. </p>
 </dd>
<dt>(<i>r</i>)</dt>
<dd> <p> matches <i>r</i>, providing grouping. </p>
 </dd></dl>
</dl>
<p> The increasing precedence of operators is alternation, concatenation and unary (*, + or ?). </p>
<p> For example, </p>
<pre><code>        /^[_a-zA-Z][_a-zA-Z0-9]*$/ and
        /^[-+]?([0-9]+\.?|\.[0-9])[0-9]*([eE][-+]?[0-9]+)?$/
</code></pre>
<p> are matched by AWK identifiers and AWK numeric constants respectively. Note that ``.&#8216;&#8216; has to be escaped to be recognized as a decimal point, and that metacharacters are not special inside character classes. </p>
<p> Any expression can be used on the right hand side of the ~ or !~ operators or passed to a built-in that expects a regular expression. If needed, it is converted to string, and then interpreted as a regular expression. For example, </p>
<pre><code>        BEGIN { identifier = &quot;[_a-zA-Z][_a-zA-Z0-9]*&quot; }
        $0 ~ &quot;^&quot; identifier
</code></pre>
<p> prints all lines that start with an AWK identifier. </p>
<p> <code>mawk</code> recognizes the empty regular expression, //, which matches the empty string and hence is matched by any string at the front, back and between every character. For example, </p>
<pre><code>        echo abc | mawk { gsub(//, &quot;X&quot;) ; print }
        XaXbXcX
</code></pre>
<h3>4. Records and fields</h3>
<p> Records are read in one at a time, and stored in the </code><i>field</i> variable <code>$0</code>. The record is split into <i>fields</i> which are stored in <code>$1</code>, <code>$2</code>, ..., <code>$NF</code>. The built-in variable <code>NF</code> is set to the number of fields, and <code>NR</code> and <code>FNR</code> are incremented by 1. Fields above <code>$NF</code> are set to &quot;&quot;. </p>
<p> Assignment to <code>$0</code> causes the fields and <code>NF</code> to be recomputed. Assignment to <code>NF</code> or to a field causes <code>$0</code> to be reconstructed by concatenating the <code>$i&#8217;s</code> separated by <code>OFS</code>. Assignment to a field with index greater than <code>NF</code>, increases <code>NF</code> and causes <code>$0</code> to be reconstructed. </p>
<p> Data input stored in fields is string, unless the entire field has numeric form and then the type is number and string. For example, </p>
<pre><code>        echo 24 24E |
        mawk '{ print($1&gt;100, $1&gt;&quot;100&quot;, $2&gt;100, $2&gt;&quot;100&quot;) }'
        0 1 1 1
</code></pre>
<p> <code>$0</code> and <code>$2</code> are string and <code>$1</code> is number and string. The first comparison is numeric, the second is string, the third is string (100 is converted to &quot;100&quot;), and the last is string.  </p>
<h3>5. Expressions and operators</h3>
<p> The expression syntax is similar to C. Primary expressions are numeric constants, string constants, variables, fields, arrays and function calls. The identifier for a variable, array or function can be a sequence of letters, digits and underscores, that does not start with a digit. Variables are not declared; they exist when first referenced and are initialized to </code><i>null</i>. </p>
<p> New expressions are composed with the following operators in order of increasing precedence. </p>
<dl>
<dd> <pre><code>
 assignment               = += -= *= /= %= ^=
 conditional              ? :
 logical or               ||
 logical and              &amp;&amp;
 array membership  in
  matching                 ~ !~
 relational               &lt; &gt; &lt;= &gt;= == !=
 concatenation            (no explicit operator)
 add ops                  + -
 mul ops                  * / %
 unary                    + -
 logical not              !
 exponentiation           ^
 inc and dec              ++ -- (both post and pre)
 field                    $
 </dd></dl>

</code></pre>
<p> Assignment, conditional and exponentiation associate right to left; the other operators associate left to right. Any expression can be parenthesized.  </p>
<h3>6. Arrays</h3>
<p> Awk provides one-dimensional arrays. Array elements are expressed as </code><i>array</i>[<i>expr</i>]. <i>Expr</i> is internally converted to string type, so, for example, A[1] and A[&quot;1&quot;] are the same element and the actual index is &quot;1&quot;. Arrays indexed by strings are called associative arrays. Initially an array is empty; elements exist when first accessed. An expression, <i>expr</i><code> in</code><i> array</i> evaluates to 1 if </code><i>array</i>[<i>expr</i>] exists, else to 0. </p>
<p> There is a form of the <code>for</code> statement that loops over each index of an array. </p>
<pre><code> for  ( var   in  array ) statement 
</code></pre>
<p> sets <i>var</i> to each index of <i>array</i> and executes <i>statement</i>. The order that <i>var</i> transverses the indices of <i>array</i> is not defined. </p>
<p> The statement, <code>delete</code> </code><i>array</i>[<i>expr</i>], causes </code><i>array</i>[<i>expr</i>] not to exist. <code>mawk</code> supports an extension, <code>delete</code> <i>array</i>, which deletes all elements of <i>array</i>. </p>
<p> Multidimensional arrays are synthesized with concatenation using the built-in variable <code>SUBSEP</code>. <i>array</i>[<i>expr</i>1,<i>expr</i>2] is equivalent to <i>array</i>[<i>expr</i>1 <code>SUBSEP </code><i>expr</i>2]. Testing for a multidimensional element uses a parenthesized index, such as </p>
<pre><code>        if ( (i, j) in A ) print A[i, j]
</code></pre>
<code></code><h3>7. Builtin-variables</h3>
<p> The following variables are built-in and initialized before program execution. </p>
<dl>
<dd>  </dd>
<dl>
<dt><code>ARGC</code></dt>
<dd> <p> number of command line arguments. </p>
 </dd>
<dt><code>ARGV</code></dt>
<dd> <p> array of command line arguments, 0..ARGC-1. </p>
 </dd>
<dt><code>CONVFMT</code></dt>
<dd> <p> format for internal conversion of numbers to string, initially = &quot;%.6g&quot;. </p>
 </dd>
<dt><code>ENVIRON</code></dt>
<dd> <p> array indexed by environment variables. An environment string, <i>var=value</i> is stored as <code>ENVIRON</code>[<i>var</i>] = <i>value</i>. </p>
 </dd>
<dt><code>FILENAME</code></dt>
<dd> <p> name of the current input file. </p>
 </dd>
<dt><code>FNR</code></dt>
<dd> <p> current record number in <code>FILENAME</code>. </p>
 </dd>
<dt><code>FS</code></dt>
<dd> <p> splits records into fields as a regular expression. </p>
 </dd>
<dt><code>NF</code></dt>
<dd> <p> number of fields in the current record. </p>
 </dd>
<dt><code>NR</code></dt>
<dd> <p> current record number in the total input stream. </p>
 </dd>
<dt><code>OFMT</code></dt>
<dd> <p> format for printing numbers; initially = &quot;%.6g&quot;. </p>
 </dd>
<dt><code>OFS</code></dt>
<dd> <p> inserted between fields on output, initially = &quot; &quot;. </p>
 </dd>
<dt><code>ORS</code></dt>
<dd> <p> terminates each record on output, initially = &quot;\n&quot;. </p>
 </dd>
<dt><code>RLENGTH</code></dt>
<dd> <p> length set by the last call to the built-in function, <code>match()</code>. </p>
 </dd>
<dt><code>RS</code></dt>
<dd> <p> input record separator, initially = &quot;\n&quot;. </p>
 </dd>
<dt><code>RSTART</code></dt>
<dd> <p> index set by the last call to <code>match()</code>. </p>
 </dd>
<dt><code>SUBSEP</code></dt>
<dd> <p> used to build multiple array subscripts, initially = &quot;\034&quot;. </p>
 </dd></dl>
</dl>
<h3>8. Built-in functions</h3>
<p> String functions </p>
<dl>
<dd>  </dd>
<dl>
<dt>gsub(</code><i>r,s,t</i>) gsub(<i>r,s</i>)</dt>
<dd> <p> Global substitution, every match of regular expression <i>r</i> in variable <i>t</i> is replaced by string <i>s</i>. The number of replacements is returned. If <i>t</i> is omitted, <code>$0</code> is used. An &amp; in the replacement string <i>s</i> is replaced by the matched substring of <i>t</i>. \&amp; and \\ put literal &amp; and \, respectively, in the replacement string. </p>
 </dd>
<dt>index(<i>s,t</i>)</dt>
<dd> <p> If <i>t</i> is a substring of <i>s</i>, then the position where <i>t</i> starts is returned, else 0 is returned. The first character of <i>s</i> is in position 1. </p>
 </dd>
<dt>length(<i>s</i>)</dt>
<dd> <p> Returns the length of string or array. <i>s</i>. </p>
 </dd>
<dt>match(<i>s,r</i>)</dt>
<dd> <p> Returns the index of the first longest match of regular expression <i>r</i> in string <i>s</i>. Returns 0 if no match. As a side effect, <code>RSTART</code> is set to the return value. <code>RLENGTH</code> is set to the length of the match or -1 if no match. If the empty string is matched, <code>RLENGTH</code> is set to 0, and 1 is returned if the match is at the front, and length(<i>s</i>)+1 is returned if the match is at the back. </p>
 </dd>
<dt>split(<i>s,A,r</i>) split(<i>s,A</i>)</dt>
<dd> <p> String <i>s</i> is split into fields by regular expression <i>r</i> and the fields are loaded into array <i>A</i>. The number of fields is returned. See section 11 below for more detail. If <i>r</i> is omitted, <code>FS</code> is used. </p>
 </dd>
<dt>sprintf(<i>format,expr-list</i>)</dt>
<dd> <p> Returns a string constructed from <i>expr-list</i> according to <i>format</i>. See the description of printf() below. </p>
 </dd>
<dt>sub(<i>r,s,t</i>) sub(<i>r,s</i>)</dt>
<dd> <p> Single substitution, same as gsub() except at most one substitution. </p>
 </dd>
<dt>substr(<i>s,i,n</i>) substr(<i>s,i</i>)</dt>
<dd> <p> Returns the substring of string <i>s</i>, starting at index <i>i</i>, of length <i>n</i>. If <i>n</i> is omitted, the suffix of <i>s</i>, starting at <i>i</i> is returned. </p>
 </dd>
<dt>tolower(<i>s</i>)</dt>
<dd> <p> Returns a copy of <i>s</i> with all upper case characters converted to lower case. </p>
 </dd>
<dt>toupper(<i>s</i>)</dt>
<dd> <p> Returns a copy of <i>s</i> with all lower case characters converted to upper case. </p>
 </dd></dl>
</dl>
<p> Time functions </p>
<p> These are available on systems which support the corresponding C <code>mktime</code> and <code>strftime</code> functions: </p>
<dl>
<dd>  </dd>
<dl>
<dt>mktime(<i>specification</i>)</dt>
<dd> <p> converts a date specification to a timestamp with the same units as <code>systime</code>. The date specification is a string containing the components of the date as decimal integers: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>YYYY</dt>
<dd> <p> the year, e.g., 2012 </p>
 </dd>
<dt>MM</dt>
<dd> <p> the month of the year starting at 1 </p>
 </dd>
<dt>DD</dt>
<dd> <p> the day of the month starting at 1 </p>
 </dd>
<dt>HH</dt>
<dd> <p> hour (0-23) </p>
 </dd>
<dt>MM</dt>
<dd> <p> minute (0-59) </p>
 </dd>
<dt>SS</dt>
<dd> <p> seconds (0-59) </p>
 </dd>
<dt>DST</dt>
<dd> <p> tells how to treat timezone versus daylight savings time: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>positive</dt>
<dd> <p> DST is in effect </p>
 </dd>
<dt>zero (default)</dt>
<dd> <p> DST is not in effect </p>
 </dd>
<dt>negative</dt>
<dd> <p> mktime() should (use timezone information and system databases to) attempt to determine whether DST is in effect at the specified time. </p>
 </dd></dl>
</dl>
</dl>
</dl>
<dt>strftime([<i>format</i> [, <i>timestamp</i> [, <i>utc</i> ]]])</dt>
<dd> <p> formats the given timestamp using the format (passed to the C <code>strftime</code> function): </p>
 </dd>
<dl>
<dd> <p> <br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 If the <i>format</i> parameter is missing, &quot;%c&quot; is used. <br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 If the <i>timestamp</i> parameter is missing, the current value from <code>systime</code> is used. <br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 If the <i>utc</i> parameter is present and nonzero, the result is in UTC. Otherwise local time is used. </p>
 </dd></dl>
<dt>systime()</dt>
<dd> <p> returns the current time of day as the number of seconds since the Epoch (1970-01-01 00:00:00 UTC on POSIX systems). </p>
 </dd></dl>
</dl>
<p> Arithmetic functions </p>
<dl>
<dd> <pre><code>atan2( y,x ) Arctan of y / x  between -pi and pi.
cos( x ) Cosine function, x  in radians.
exp( x ) Exponential function.
int( x ) Returns x  truncated towards zero.
log( x ) Natural logarithm.
rand() Returns a random number between zero and one.
sin( x ) Sine function, x  in radians.
sqrt( x ) Returns square root of x .
</code></pre>
 </dd>
<dl>
<dt>srand(<i>expr</i>) srand()</dt>
<dd> <p> Seeds the random number generator, using the clock if <i>expr</i> is omitted, and returns the value of the previous seed. Srand(<i>expr</i>) is useful for repeating pseudo random sequences. </p>
 </dd>
<dd> <p> Note: <code>mawk</code> is normally configured to seed the random number generator from the clock at startup, making it unnecessary to call srand(). This feature can be suppressed via conditional compile, or overridden using the <code>-Wrandom</code> option. </p>
 </dd></dl>
</dl>
<h3>9. Input and output</h3>
<p> There are two output statements, print</code> and <code>printf</code>. </p>
<dl>
<dd>  </dd>
<dl>
<dt>print</dt>
<dd> <p> writes <code>$0 ORS</code> to standard output. </p>
 </dd>
<dt>print <i>expr</i>1, <i>expr</i>2, ..., <i>expr</i>n</dt>
<dd> <p> writes <i>expr</i>1 <code>OFS <i>expr</i>2 OFS</code> ... <i>expr</i>n <code>ORS</code> to standard output. Numeric expressions are converted to string with <code>OFMT</code>. </p>
 </dd>
<dt>printf <i>format, expr-list</i></dt>
<dd> <p> duplicates the printf C library function writing to standard output. The complete ANSI C format specifications are recognized with conversions %c, %d, %e, %E, %f, %g, %G, %i, %o, %s, %u, %x, %X and %%, and conversion qualifiers h and l. </p>
 </dd></dl>
</dl>
<p> The argument list to print or printf can optionally be enclosed in parentheses. Print formats numbers using <code>OFMT</code> or &quot;%d&quot; for exact integers. &quot;%c&quot; with a numeric argument prints the corresponding 8 bit character, with a string argument it prints the first character of the string. The output of print and printf can be redirected to a file or command by appending &gt; <i>file</i>, &gt;&gt; <i>file</i> or | <i>command</i> to the end of the print statement. Redirection opens <i>file</i> or <i>command</i> only once, subsequent redirections append to the already open stream. By convention, <code>mawk</code> associates the filename </p>
<dl>
<dd> <p> <br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 &quot;/dev/stderr&quot; with stderr, <br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 &quot;/dev/stdout&quot; with stdout, <br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 &quot;-&quot; and &quot;/dev/stdin&quot; with stdin. </p>
 </dd></dl>
<p> The association with stderr is especially useful because it allows print and printf to be redirected to stderr. These names can also be passed to functions. </p>
<p> The input function <code>getline</code> has the following variations. </p>
<dl>
<dd>  </dd>
<dl>
<dt>getline</dt>
<dd> <p> reads into <code>$0</code>, updates the fields, <code>NF</code>, <code>NR</code> and <code>FNR</code>. </p>
 </dd>
<dt>getline &lt; <i>file</i></dt>
<dd> <p> reads into <code>$0</code> from <i>file</i>, updates the fields and <code>NF</code>. </p>
 </dd>
<dt>getline <i>var</dt>
<dd> <p> reads the next record into var</i>, updates <code>NR</code> and <code>FNR</code>. </p>
 </dd>
<dt>getline <i>var</i> &lt; <i>file</dt>
<dd> <p> reads the next record of file</i> into <i>var</i>. </p>
 </dd>
<dt><i>command</i> | getline</dt>
<dd> <p> pipes a record from <i>command</i> into <code>$0</code> and updates the fields and <code>NF</code>. </p>
 </dd>
<dt><i>command</i> | getline <i>var</dt>
<dd> <p> pipes a record from command</i> into <i>var</i>. </p>
 </dd></dl>
</dl>
<p> Getline returns 0 on end-of-file, -1 on error, otherwise 1. </p>
<p> Commands on the end of pipes are executed by /bin/sh. </p>
<p> The function <code>close</code>(<i>expr</i>) closes the file or pipe associated with <i>expr</i>. Close returns 0 if <i>expr</i> is an open file, the exit status if <i>expr</i> is a piped command, and -1 otherwise. Close is used to reread a file or command, make sure the other end of an output pipe is finished or conserve file resources. </p>
<p> The function <code>fflush</code>(<i>expr</i>) flushes the output file or pipe associated with <i>expr</i>. Fflush returns 0 if <i>expr</i> is an open output stream else -1. Fflush without an argument flushes stdout. Fflush with an empty argument (&quot;&quot;) flushes all open output. </p>
<p> The function <code>system</code>(<i>expr</i>) uses the C runtime <code>system</code> call to execute <i>expr</i> and returns the corresponding wait status of the command as follows: <br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 if the <code>system</code> call failed, setting the status to -1, <i>mawk</i> returns that value. <br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 if the command exited normally, <i>mawk</i> returns its exit-status. <br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 if the command exited due to a signal such as <code>SIGHUP</code>, <i>mawk</i> returns the signal number plus 256. </p>
<p> Changes made to the <code>ENVIRON</code> array are not passed to commands executed with <code>system</code> or pipes.  </p>
<h3>10. User defined functions</h3>
<p> The syntax for a user defined function is </code> </p>
<pre><code> function  name( args  ) { statements  }
</code></pre>
<p> The function body can contain a return statement </p>
<pre><code> return   opt_expr 
</code></pre>
<p> A return statement is not required. Function calls may be nested or recursive. Functions are passed expressions by value and arrays by reference. Extra arguments serve as local variables and are initialized to <i>null</i>. For example, csplit(<i>s,A</i>) puts each character of <i>s</i> into array <i>A</i> and returns the length of <i>s</i>. </p>
<pre><code>        function csplit(s, A, n, i)
        {
          n = length(s)
          for( i = 1 ; i &lt;= n ; i++ ) A[i] = substr(s, i, 1)
          return n
        }
</code></pre>
<p> Putting extra space between passed arguments and local variables is conventional. Functions can be referenced before they are defined, but the function name and the &#8216;(&#8216; of the arguments must touch to avoid confusion with concatenation. </p>
<p> A function parameter is normally a scalar value (number or string). If there is a forward reference to a function using an array as a parameter, the function&#8217;s corresponding parameter will be treated as an array.  </p>
<h3>11. Splitting strings, records and files</h3>
<p> Awk programs use the same algorithm to split strings into arrays with split(), and records into fields on FS</code>. <code>mawk</code> uses essentially the same algorithm to split files into records on <code>RS</code>. </p>
<p> Split(<i>expr,A,sep</i>) works as follows: </p>
<dl>
<dd>  </dd>
<dl>
<dt>(1)</dt>
<dd> <p> If <i>sep</i> is omitted, it is replaced by <code>FS</code>. <i>Sep</i> can be an expression or regular expression. If it is an expression of non-string type, it is converted to string. </p>
 </dd>
<dt>(2)</dt>
<dd> <p> If <i>sep</i> = &quot; &quot; (a single space), then &lt;SPACE&gt; is trimmed from the front and back of <i>expr</i>, and <i>sep</i> becomes &lt;SPACE&gt;. <code>mawk</code> defines &lt;SPACE&gt; as the regular expression /[&nbsp;\t\n]+/. Otherwise <i>sep</i> is treated as a regular expression, except that meta-characters are ignored for a string of length 1, e.g., split(x, A, &quot;*&quot;) and split(x, A, /\*/) are the same. </p>
 </dd>
<dt>(3)</dt>
<dd> <p> If <i>expr</i> is not string, it is converted to string. If <i>expr</i> is then the empty string &quot;&quot;, split() returns 0 and <i>A</i> is set empty. Otherwise, all non-overlapping, non-null and longest matches of <i>sep</i> in <i>expr</i>, separate <i>expr</i> into fields which are loaded into <i>A</i>. The fields are placed in A[1], A[2], ..., A[n] and split() returns n, the number of fields which is the number of matches plus one. Data placed in <i>A</i> that looks numeric is typed number and string. </p>
 </dd></dl>
</dl>
<p> Splitting records into fields works the same except the pieces are loaded into <code>$1</code>, <code>$2</code>,..., <code>$NF</code>. If <code>$0</code> is empty, <code>NF</code> is set to 0 and all <code>$i</code> to &quot;&quot;. </p>
<p> <code>mawk</code> splits files into records by the same algorithm, but with the slight difference that <code>RS</code> is really a terminator instead of a separator. (<code>ORS</code> is really a terminator too). </p>
<dl>
<dd> <p> E.g., if <code>FS</code> = ``:+&#8216;&#8216; and <code>$0</code> = ``a::b:&#8216;&#8216; , then <code>NF</code> = 3 and <code>$1</code> = ``a&#8217;&#8216;, <code>$2</code> = ``b&#8217;&#8216; and <code>$3</code> = &quot;&quot;, but if ``a::b:&#8216;&#8216; is the contents of an input file and <code>RS</code> = ``:+&#8216;&#8216;, then there are two records ``a&#8217;&#8216; and ``b&#8217;&#8216;. </p>
 </dd></dl>
<p> <code>RS</code> = &quot; &quot; is not special. </p>
<p> If <code>FS</code> = &quot;&quot;, then <code>mawk</code> breaks the record into individual characters, and, similarly, split(<i>s,A,</i>&quot;&quot;) places the individual characters of <i>s</i> into <i>A</i>.  </p>
<h3>12. Multi-line records</h3>
<p> Since mawk</code> interprets <code>RS</code> as a regular expression, multi-line records are easy. Setting <code>RS</code> = &quot;\n\n+&quot;, makes one or more blank lines separate records. If <code>FS</code> = &quot; &quot; (the default), then single newlines, by the rules for &lt;SPACE&gt; above, become space and single newlines are field separators. </p>
<dl>
<dd> <p> For example, if <br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 a file is &quot;a b\nc\n\n&quot;, <br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>RS</code> = &quot;\n\n+&quot; and <br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>FS</code> = &quot;&nbsp;&quot;, </p>
<p> then there is one record ``a b\nc&#8217;&#8216; with three fields ``a&#8217;&#8216;, ``b&#8217;&#8216; and ``c&#8217;&#8216;: <br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 Changing <code>FS</code> = ``\n&#8217;&#8216;, gives two fields ``a b&#8217;&#8216; and ``c&#8217;&#8216;; <br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 changing <code>FS</code> = ``&#8216;&#8216;, gives one field identical to the record. </p>
 </dd></dl>
<p> If you want lines with spaces or tabs to be considered blank, set <code>RS</code> = ``\n([&nbsp;\t]*\n)+&#8216;&#8216;. For compatibility with other awks, setting <code>RS</code> = &quot;&quot; has the same effect as if blank lines are stripped from the front and back of files and then records are determined as if <code>RS</code> = ``\n\n+&#8216;&#8216;. POSIX requires that ``\n&#8217;&#8216; always separates records when <code>RS</code> = &quot;&quot; regardless of the value of <code>FS</code>. <code>mawk</code> does not support this convention, because defining ``\n&#8217;&#8216; as &lt;SPACE&gt; makes it unnecessary. </p>
<p> Most of the time when you change <code>RS</code> for multi-line records, you will also want to change <code>ORS</code> to ``\n\n&#8217;&#8216; so the record spacing is preserved on output.  </p>
<h3>13. Program execution</h3>
<p> This section describes the order of program execution. First ARGC</code> is set to the total number of command line arguments passed to the execution phase of the program. <code>ARGV[0]</code> is set the name of the AWK interpreter and <code>ARGV[1]</code> ... <code>ARGV[ARGC-1]</code> holds the remaining command line arguments exclusive of options and program source. For example with </p>
<pre><code>        mawk -f prog v=1 A t=hello B
</code></pre>
<p> <code>ARGC</code> = 5 with <code>ARGV[0]</code> = &quot;mawk&quot;, <code>ARGV[1]</code> = &quot;v=1&quot;, <code>ARGV[2]</code> = &quot;A&quot;, <code>ARGV[3]</code> = &quot;t=hello&quot; and <code>ARGV[4]</code> = &quot;B&quot;. </p>
<p> Next, each <code>BEGIN</code> block is executed in order. If the program consists entirely of <code>BEGIN</code> blocks, then execution terminates, else an input stream is opened and execution continues. If <code>ARGC</code> equals 1, the input stream is set to stdin, else the command line arguments <code>ARGV[1]</code> ... <code>ARGV[ARGC-1]</code> are examined for a file argument. </p>
<p> The command line arguments divide into three sets: file arguments, assignment arguments and empty strings &quot;&quot;. An assignment has the form <i>var</i>=<i>string</i>. When an <code>ARGV[i]</code> is examined as a possible file argument, if it is empty it is skipped; if it is an assignment argument, the assignment to <i>var</i> takes place and <code>i</code> skips to the next argument; else <code>ARGV[i]</code> is opened for input. If it fails to open, execution terminates with exit code 2. If no command line argument is a file argument, then input comes from stdin. Getline in a <code>BEGIN</code> action opens input. ``-&#8216;&#8216; as a file argument denotes stdin. </p>
<p> Once an input stream is open, each input record is tested against each <i>pattern</i>, and if it matches, the associated <i>action</i> is executed. An expression pattern matches if it is boolean true (see the end of section 2). A <code>BEGIN</code> pattern matches before any input has been read, and an <code>END</code> pattern matches after all input has been read. A range pattern, <i>expr</i>1,<i>expr</i>2 , matches every record between the match of <i>expr</i>1 and the match <i>expr</i>2 inclusively. </p>
<p> When end of file occurs on the input stream, the remaining command line arguments are examined for a file argument, and if there is one it is opened, else the <code>END</code> <i>pattern</i> is considered matched and all <code>END</code> <i>actions</i> are executed. </p>
<p> In the example, the assignment v=1 takes place after the <code>BEGIN</code> <i>actions</i> are executed, and the data placed in v is typed number and string. Input is then read from file A. On end of file A, t is set to the string &quot;hello&quot;, and B is opened for input. On end of file B, the <code>END</code> <i>actions</i> are executed. </p>
<p> Program flow at the <i>pattern</i> <i>{action}</i> level can be changed with the </p>
<pre><code> next
        nextfile
        exit  opt_expr 
</code></pre>
<p> statements: <br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 A <code>next</code> statement causes the next input record to be read and pattern testing to restart with the first <i>pattern {action}</i> pair in the program. <br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 A <code>nextfile</code> statement tells <code>mawk</code> to stop processing the current input file. It then updates FILENAME to the next file listed on the command line, and resets FNR to 1. <br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 An <code>exit</code> statement causes immediate execution of the <code>END</code> actions or program termination if there are none or if the <code>exit</code> occurs in an <code>END</code> action. The <i>opt_expr</i> sets the exit value of the program unless overridden by a later <code>exit</code> or subsequent error.  </p>
<h2>EXAMPLES</h2>
<pre><code>1. emulate cat.
        { print }
2. emulate wc.
        { chars += length($0) + 1 # add one for the \n
          words += NF
        }
        END{ print NR, words, chars }
3. count the number of unique ``real words''.
        BEGIN { FS = &quot;[^A-Za-z]+&quot; }
        { for(i = 1 ; i &lt;= NF ; i++) word[$i] = &quot;&quot; }
        END { delete word[&quot;&quot;]
              for ( i in word ) cnt++
              print cnt
        }
</code></pre>
<p> 4. sum the second field of every record based on the first field. </p>
<pre><code>        $1 ~ /credit|gain/ { sum += $2 }
        $1 ~ /debit|loss/ { sum -= $2 }
        END { print sum }
5. sort a file, comparing as string
        { line[NR] = $0 &quot;&quot; } # make sure of comparison type
                              # in case some lines look numeric
        END { isort(line, NR)
          for(i = 1 ; i &lt;= NR ; i++) print line[i]
        }
        #insertion sort of A[1..n]
        function isort( A, n, i, j, hold)
        {
          for( i = 2 ; i &lt;= n ; i++)
          {
            hold = A[j = i]
            while ( A[j-1] &gt; hold )
            { j-- ; A[j+1] = A[j] }
            A[j] = hold
          }
          # sentinel A[0] = &quot;&quot; will be created if needed
        }
</code></pre>
<h2>COMPATIBILITY ISSUES</h2>
<h3>MAWK 1.3.3 versus POSIX 1003.2 Draft 11.3</h3>
<p> The POSIX 1003.2(draft 11.3) definition of the AWK language is AWK as described in the AWK book with a few extensions that appeared in SystemVR4 nawk. The extensions are: </p>
<dl>
<dd> <p> <br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 New functions: toupper() and tolower(). <br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 New variables: ENVIRON[] and CONVFMT. <br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 ANSI C conversion specifications for printf() and sprintf(). <br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 New command options: -v var=value, multiple -f options and implementation options as arguments to -W. <br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 For systems (MS-DOS or Windows) which provide a <i>setmode</i> function, an environment variable MAWKBINMODE and a built-in variable BINMODE. The bits of the BINMODE value tell <i>mawk</i> how to modify the <code>RS</code> and <code>ORS</code> variables: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>0</dt>
<dd> <p> set standard input to binary mode, and if BIT-2 is unset, set <code>RS</code> to &quot;\r\n&quot; (CR/LF) rather than &quot;\n&quot; (LF). </p>
 </dd>
<dt>1</dt>
<dd> <p> set standard output to binary mode, and if BIT-2 is unset, set <code>ORS</code> to &quot;\r\n&quot; (CR/LF) rather than &quot;\n&quot; (LF). </p>
 </dd>
<dt>2</dt>
<dd> <p> suppress the assignment to <code>RS</code> and <code>ORS</code> of CR/LF, making it possible to run scripts and generate output compatible with Unix line-endings. </p>
 </dd></dl>
</dl>
</dl>
<p> POSIX AWK is oriented to operate on files a line at a time. <code>RS</code> can be changed from &quot;\n&quot; to another single character, but it is hard to find any use for this --- there are no examples in the AWK book. By convention, <code>RS</code> = &quot;&quot;, makes one or more blank lines separate records, allowing multi-line records. When <code>RS</code> = &quot;&quot;, &quot;\n&quot; is always a field separator regardless of the value in <code>FS</code>. </p>
<p> <code>mawk</code>, on the other hand, allows <code>RS</code> to be a regular expression. When &quot;\n&quot; appears in records, it is treated as space, and <code>FS</code> always determines fields. </p>
<p> Removing the line at a time paradigm can make some programs simpler and can often improve performance. For example, redoing example 3 from above, </p>
<pre><code>        BEGIN { RS = &quot;[^A-Za-z]+&quot; }
        { word[ $0 ] = &quot;&quot; }
        END { delete word[ &quot;&quot; ]
          for( i in word ) cnt++
          print cnt
        }
</code></pre>
<p> counts the number of unique words by making each word a record. On moderate size files, <code>mawk</code> executes twice as fast, because of the simplified inner loop. </p>
<p> The following program replaces each comment by a single space in a C program file, </p>
<pre><code>        BEGIN {
          RS = &quot;/\*([^*]|\*+[^/*])*\*+/&quot;
                # comment is record separator
          ORS = &quot; &quot;
          getline hold
       }
       { print hold ; hold = $0 }
       END { printf &quot;%s&quot; , hold }
</code></pre>
<p> Buffering one record is needed to avoid terminating the last record with a space. </p>
<p> With <code>mawk</code>, the following are all equivalent, </p>
<pre><code>        x ~ /a\+b/ x ~ &quot;a\+b&quot; x ~ &quot;a\\+b&quot;
</code></pre>
<p> The strings get scanned twice, once as string and once as regular expression. On the string scan, <code>mawk</code> ignores the escape on non-escape characters while the AWK book advocates <i>\c</i> be recognized as <i>c</i> which necessitates the double escaping of meta-characters in strings. POSIX explicitly declines to define the behavior which passively forces programs that must run under a variety of awks to use the more portable but less readable, double escape. </p>
<p> POSIX AWK does not recognize &quot;/dev/std{in,out,err}&quot;. Some systems provide an actual device for this, allowing AWKs which do not implement the feature directly to support it. </p>
<p> POSIX AWK does not recognize \x hex escape sequences in strings. Unlike ANSI C, <code>mawk</code> limits the number of digits that follows \x to two as the current implementation only supports 8 bit characters. The built-in <code>fflush</code> first appeared in a recent (1993) AT&amp;T awk released to netlib, and is not part of the POSIX standard. Aggregate deletion with <code>delete</code> <i>array</i> is not part of the POSIX standard. </p>
<p> POSIX explicitly leaves the behavior of <code>FS</code> = &quot;&quot; undefined, and mentions splitting the record into characters as a possible interpretation, but currently this use is not portable across implementations.  </p>
<h3>Random numbers</h3>
<p> POSIX does not prescribe a method for initializing random numbers at startup. </p>
<p> In practice, most implementations do nothing special, which makes <code>srand</code> and <code>rand</code> follow the C runtime library, making the initial seed value 1. Some implementations (Solaris XPG4 and Tru64) return 0 from the first call to <code>srand</code>, although the results from <code>rand</code> behave as if the initial seed is 1. Other implementations return 1. </p>
<p> While <code>mawk</code> can call <code>srand</code> at startup with no parameter (initializing random numbers from the clock), this feature may be suppressed using conditional compilation.  </p>
<h3>Extensions added for compatibility for GAWK and BWK</h3>
<p> <code>Nextfile</code> is a <code>gawk</code> extension (also implemented by BWK awk), is not yet part of the POSIX standard (as of October 2012), although it has been accepted for the next revision of the standard. </p>
<p> <code>Mktime</code>, <code>strftime</code>&nbsp;and <code>systime</code> are <code>gawk</code> extensions. </p>
<p> The &quot;/dev/stdin&quot; feature was added to <code>mawk</code> after 1.3.4, for compatibility with <code>gawk</code> and BWK awk. The corresponding &quot;-&quot; (alias for /dev/stdin) was present in mawk 1.3.3.  </p>
<h3>Subtle Differences not in POSIX or the AWK Book</h3>
<p> Finally, here is how <code>mawk</code> handles exceptional cases not discussed in the AWK book or the POSIX draft. It is unsafe to assume consistency across awks and safe to skip to the next section. </p>
<dl>
<dd> <p> <br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 substr(s, i, n) returns the characters of s in the intersection of the closed interval [1, length(s)] and the half-open interval [i, i+n). When this intersection is empty, the empty string is returned; so substr(&quot;ABC&quot;, 1, 0) = &quot;&quot; and substr(&quot;ABC&quot;, -4, 6) = &quot;A&quot;. <br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 Every string, including the empty string, matches the empty string at the front so, s ~ // and s ~ &quot;&quot;, are always 1 as is match(s, //) and match(s, &quot;&quot;). The last two set <code>RLENGTH</code> to 0. <br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 index(s, t) is always the same as match(s, t1) where t1 is the same as t with metacharacters escaped. Hence consistency with match requires that index(s, &quot;&quot;) always returns 1. Also the condition, index(s,t) != 0 if and only t is a substring of s, requires index(&quot;&quot;,&quot;&quot;) = 1. <br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 If getline encounters end of file, getline var, leaves var unchanged. Similarly, on entry to the <code>END</code> actions, <code>$0</code>, the fields and <code>NF</code> have their value unaltered from the last record. </p>
 </dd></dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> <code>Mawk</code> recognizes these variables: </p>
<dl>
<dd>  </dd>
<dl>
<dt>MAWKBINMODE</dt>
<dd> <p> (see <code>COMPATIBILITY ISSUES</code>) </p>
 </dd>
<dt>MAWK_LONG_OPTIONS</dt>
<dd> <p> If this is set, <code>mawk</code> uses its value to decide what to do with GNU-style long options: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>allow</dt>
<dd> <p> <code>Mawk</code> allows the option to be checked against the (small) set of long options it recognizes. </p>
 </dd>
<dt>error</dt>
<dd> <p> <code>Mawk</code> prints an error message and exits. This is the default. </p>
 </dd>
<dt>ignore</dt>
<dd> <p> <code>Mawk</code> ignores the option. </p>
 </dd>
<dt>warn</dt>
<dd> <p> Print an warning message and otherwise ignore the option. </p>
 </dd></dl>
</dl>
<dd> <p> If the variable is unset, <code>mawk</code> prints an error message and exits. </p>
 </dd>
<dt>WHINY_USERS</dt>
<dd> <p> This is an undocumented <code>gawk</code> feature. It tells <code>mawk</code> to sort array indices before it starts to iterate over the elements of an array. </p>
 </dd></dl>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-grep/">grep</a></code>(1) </p>
<p> Aho, Kernighan and Weinberger, <i>The AWK Programming Language</i>, Addison-Wesley Publishing, 1988, (the AWK book), defines the language, opening with a tutorial and advancing to many interesting programs that delve into issues of software design and analysis relevant to programming in any language. </p>
<p> <i>The GAWK Manual</i>, The Free Software Foundation, 1991, is a tutorial and language reference that does not attempt the depth of the AWK book and assumes the reader may be a novice programmer. The section on AWK arrays is excellent. It also discusses POSIX requirements for AWK.  </p>
<h2>BUGS</h2>
<p> <code>mawk</code> implements printf() and sprintf() using the C library functions, printf and sprintf, so full ANSI compatibility requires an ANSI C library. In practice this means the h conversion qualifier may not be available. Also <code>mawk</code> inherits any bugs or limitations of the library functions. </p>
<p> Implementors of the AWK language have shown a consistent lack of imagination when naming their programs.  </p>
<h2>AUTHOR</h2>
<p> Mike Brennan (brennan [at] whidbey.com). <br />
 Thomas E. Dickey &lt;dickey [at] invisible-island.net&gt;. </p>

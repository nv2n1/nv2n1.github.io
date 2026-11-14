---
title: "zshparam(1)"
name: "zshparam"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zshparam/"
description: "zshparam – zsh parameters"
---

<h2 class="name">NAME</h2>
<p> zshparam &#8211; zsh parameters </p>
<h2>DESCRIPTION</h2>
<p> A parameter has a name, a value, and a number of attributes. A name may be any sequence of alphanumeric characters and underscores, or the single characters `<code>*</code>&#8216;, `<code>@</code>&#8216;, `<code>#</code>&#8216;, `<code>?</code>&#8216;, `<code>&#8211;</code>&#8216;, `<code>$</code>&#8216;, or `<code>!</code>&#8216;. A parameter whose name begins with an alphanumeric or underscore is also referred to as a <i>variable</i>. </p>
<p> The attributes of a parameter determine the <i>type</i> of its value, often referred to as the parameter type or variable type, and also control other processing that may be applied to the value when it is referenced. The value type may be a <i>scalar</i> (a string, an integer, or a floating point number), an array (indexed numerically), or an <i>associative</i> array (an unordered set of name-value pairs, indexed by name, also referred to as a <i>hash</i>). </p>
<p> Named scalar parameters may have the <i>exported</i>, <code>-x</code>, attribute, to copy them into the process environment, which is then passed from the shell to any new processes that it starts. Exported parameters are called <i>environment variables</i>. The shell also <i>imports</i> environment variables at startup time and automatically marks the corresponding parameters as exported. Some environment variables are not imported for reasons of security or because they would interfere with the correct operation of other shell features. </p>
<p> Parameters may also be <i>special</i>, that is, they have a predetermined meaning to the shell. Special parameters cannot have their type changed or their readonly attribute turned off, and if a special parameter is unset, then later recreated, the special properties will be retained. </p>
<p> To declare the type of a parameter, or to assign a string or numeric value to a scalar parameter, use the <code>typeset</code> builtin. </p>
<p> The value of a scalar parameter may also be assigned by writing: </p>
<dl>
<dt>
<dd>
<pre>
<i>name</i><code>=</code><i>value</i>
</pre>
</dl>
<p> In scalar assignment, <i>value</i> is expanded as a single string, in which the elements of arrays are joined together; filename expansion is not performed unless the option <code>GLOB_ASSIGN</code> is set. </p>
<p> When the integer attribute, <code>-i</code>, or a floating point attribute, <code>-E</code> or <code>-F</code>, is set for <i>name</i>, the <i>value</i> is subject to arithmetic evaluation. Furthermore, by replacing `<code>=</code>&#8216; with `<code>+=</code>&#8216;, a parameter can be incremented or appended to. See the section `Array Parameters&#8217; and <i>Arithmetic Evaluation</i> (in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1)) for additional forms of assignment. </p>
<p> Note that assignment may implicitly change the attributes of a parameter. For example, assigning a number to a variable in arithmetic evaluation may change its type to integer or float, and with <code>GLOB_ASSIGN</code> assigning a pattern to a variable may change its type to an array. </p>
<p> To reference the value of a parameter, write `<code>$</code><i>name</i>&#8216; or `<code>${</code><i>name</i><code>}</code>&#8216;. See <i>Parameter Expansion</i> in <i><a href="/docs/linux/man/1-zshexpn/">zshexpn</a></i>(1) for complete details. That section also explains the effect of the difference between scalar and array assignment on parameter expansion.</p>
<h2>ARRAY PARAMETERS</h2>
<p> To assign an array value, write one of: </p>
<dl>
<dt>
<dd>
<pre>
<code>set -A</code> <i>name</i> <i>value</i> ...
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
<i>name</i><code>=(</code><i>value</i> ...<code>)</code>
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
<i>name</i><code>=(</code><code>[</code><i>key</i><code>]=</code><i>value</i> ...<code>)</code>
</pre>
</dl>
<p> If no parameter <i>name</i> exists, an ordinary array parameter is created. If the parameter <i>name</i> exists and is a scalar, it is replaced by a new array. </p>
<p> In the third form, <i>key</i> is an expression that will be evaluated in arithmetic context (in its simplest form, an integer) that gives the index of the element to be assigned with <i>value</i>. In this form any elements not explicitly mentioned that come before the largest index to which a value is assigned are assigned an empty string. The indices may be in any order. Note that this syntax is strict: <code>[</code> and <code>]=</code> must not be quoted, and <i>key</i> may not consist of the unquoted string <code>]=</code>, but is otherwise treated as a simple string. The enhanced forms of subscript expression that may be used when directly subscripting a variable name, described in the section Array Subscripts below, are not available. </p>
<p> The syntaxes with and without the explicit key may be mixed. An implicit <i>key</i> is deduced by incrementing the index from the previously assigned element. Note that it is not treated as an error if latter assignments in this form overwrite earlier assignments. </p>
<p> For example, assuming the option <code>KSH_ARRAYS</code> is not set, the following: </p>
<dl>
<dt>
<dd>
<pre>
<code>array=(one [3]=three four)</code>
</pre>
</dl>
<p> causes the array variable <code>array</code> to contain four elements <code>one</code>, an empty string, <code>three</code> and <code>four</code>, in that order. </p>
<p> In the forms where only <i>value</i> is specified, full command line expansion is performed. </p>
<p> In the <code>[</code><i>key</i><code>]=</code><i>value</i> form, both <i>key</i> and <i>value</i> undergo all forms of expansion allowed for single word shell expansions (this does not include filename generation); these are as performed by the parameter expansion flag <code>(e)</code> as described in <i><a href="/docs/linux/man/1-zshexpn/">zshexpn</a></i>(1). Nested parentheses may surround <i>value</i> and are included as part of the value, which is joined into a plain string; this differs from ksh which allows the values themselves to be arrays. A future version of zsh may support that. To cause the brackets to be interpreted as a character class for filename generation, and therefore to treat the resulting list of files as a set of values, quote the equal sign using any form of quoting. Example: </p>
<dl>
<dt>
<dd>
<pre>
<i>name</i><code>=(</code><code>[a-z]'='*)</code>
</pre>
</dl>
<p> To append to an array without changing the existing values, use one of the following: </p>
<dl>
<dt>
<dd>
<pre>
<i>name</i><code>+=(</code><i>value</i> ...<code>)</code>
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
<i>name</i><code>+=(</code><code>[</code><i>key</i><code>]=</code><i>value</i> ...<code>)</code>
</pre>
</dl>
<p> In the second form <i>key</i> may specify an existing index as well as an index off the end of the old array; any existing value is overwritten by <i>value</i>. Also, it is possible to use <code>[</code><i>key</i><code>]+=</code><i>value</i> to append to the existing value at that index. </p>
<p> Within the parentheses on the right hand side of either form of the assignment, newlines and semicolons are treated the same as white space, separating individual <i>value</i>s. Any consecutive sequence of such characters has the same effect. </p>
<p> Ordinary array parameters may also be explicitly declared with: </p>
<dl>
<dt>
<dd>
<pre>
<code>typeset -a</code> <i>name</i>
</pre>
</dl>
<p> Associative arrays <i>must</i> be declared before assignment, by using: </p>
<dl>
<dt>
<dd>
<pre>
<code>typeset -A</code> <i>name</i>
</pre>
</dl>
<p> When <i>name</i> refers to an associative array, the list in an assignment is interpreted as alternating keys and values: </p>
<dl>
<dt>
<dd>
<pre>
<code>set -A</code> <i>name</i> <i>key</i> <i>value</i> ...
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
<i>name</i><code>=(</code><i>key</i> <i>value</i> ...<code>)</code>
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
<i>name</i><code>=(</code><code>[</code><i>key</i><code>]=</code><i>value</i> ...<code>)</code>
</pre>
</dl>
<p> Note that only one of the two syntaxes above may be used in any given assignment; the forms may not be mixed. This is unlike the case of numerically indexed arrays. </p>
<p> Every <i>key</i> must have a <i>value</i> in this case. Note that this assigns to the entire array, deleting any elements that do not appear in the list. The append syntax may also be used with an associative array: </p>
<dl>
<dt>
<dd>
<pre>
<i>name</i><code>+=(</code><i>key</i> <i>value</i> ...<code>)</code>
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
<i>name</i><code>+=(</code><code>[</code><i>key</i><code>]=</code><i>value</i> ...<code>)</code>
</pre>
</dl>
<p> This adds a new key/value pair if the key is not already present, and replaces the value for the existing key if it is. In the second form it is also possible to use <code>[</code><i>key</i><code>]+=</code><i>value</i> to append to the existing value at that key. Expansion is performed identically to the corresponding forms for normal arrays, as described above. </p>
<p> To create an empty array (including associative arrays), use one of: </p>
<dl>
<dt>
<dd>
<pre>
<code>set -A</code> <i>name</i>
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
<i>name</i><code>=()</code>
</pre>
</dl>
<h3>Array Subscripts</h3>
<p> Individual elements of an array may be selected using a subscript. A subscript of the form `<code>[</code><i>exp</i><code>]</code>&#8216; selects the single element <i>exp</i>, where <i>exp</i> is an arithmetic expression which will be subject to arithmetic expansion as if it were surrounded by `<code>$((</code>&#8230;<code>))</code>&#8216;. The elements are numbered beginning with 1, unless the <code>KSH_ARRAYS</code> option is set in which case they are numbered from zero. </p>
<p> Subscripts may be used inside braces used to delimit a parameter name, thus `<code>${foo[2]}</code>&#8216; is equivalent to `<code>$foo[2]</code>&#8216;. If the <code>KSH_ARRAYS</code> option is set, the braced form is the only one that works, as bracketed expressions otherwise are not treated as subscripts. </p>
<p> If the <code>KSH_ARRAYS</code> option is not set, then by default accesses to an array element with a subscript that evaluates to zero return an empty string, while an attempt to write such an element is treated as an error. For backward compatibility the <code>KSH_ZERO_SUBSCRIPT</code> option can be set to cause subscript values 0 and 1 to be equivalent; see the description of the option in <i><a href="/docs/linux/man/1-zshoptions/">zshoptions</a></i>(1). </p>
<p> The same subscripting syntax is used for associative arrays, except that no arithmetic expansion is applied to <i>exp</i>. However, the parsing rules for arithmetic expressions still apply, which affects the way that certain special characters must be protected from interpretation. See <i>Subscript Parsing</i> below for details. </p>
<p> A subscript of the form `<code>[*]</code>&#8216; or `<code>[@]</code>&#8216; evaluates to all elements of an array; there is no difference between the two except when they appear within double quotes. `<code>&quot;$foo[*]&quot;</code>&#8216; evaluates to `<code>&quot;$foo[1] $foo[2] </code>&#8230;<code>&quot;</code>&#8216;, whereas `<code>&quot;$foo[@]&quot;</code>&#8216; evaluates to `<code>&quot;$foo[1]&quot; &quot;$foo[2]&quot; </code>&#8230;&#8217;. For associative arrays, `<code>[*]</code>&#8216; or `<code>[@]</code>&#8216; evaluate to all the values, in no particular order. Note that this does not substitute the keys; see the documentation for the `<code>k</code>&#8216; flag under <i>Parameter Expansion Flags</i> in <i><a href="/docs/linux/man/1-zshexpn/">zshexpn</a></i>(1) for complete details. When an array parameter is referenced as `<code>$</code><i>name</i>&#8216; (with no subscript) it evaluates to `<code>$</code><i>name</i><code>[*]</code>&#8216;, unless the <code>KSH_ARRAYS</code> option is set in which case it evaluates to `<code>${</code><i>name</i><code>[0]}</code>&#8216; (for an associative array, this means the value of the key `<code>0</code>&#8216;, which may not exist even if there are values for other keys). </p>
<p> A subscript of the form `<code>[</code><i>exp1</i><code>,</code><i>exp2</i><code>]</code>&#8216; selects all elements in the range <i>exp1</i> to <i>exp2</i>, inclusive. (Associative arrays are unordered, and so do not support ranges.) If one of the subscripts evaluates to a negative number, say <code>&#8211;</code><i>n</i>, then the <i>n</i>th element from the end of the array is used. Thus `<code>$foo[-3]</code>&#8216; is the third element from the end of the array <code>foo</code>, and `<code>$foo[1,-1]</code>&#8216; is the same as `<code>$foo[*]</code>&#8216;. </p>
<p> Subscripting may also be performed on non-array values, in which case the subscripts specify a substring to be extracted. For example, if <code>FOO</code> is set to `<code>foobar</code>&#8216;, then `<code>echo $FOO[2,5]</code>&#8216; prints `<code>ooba</code>&#8216;. Note that some forms of subscripting described below perform pattern matching, and in that case the substring extends from the start of the match of the first subscript to the end of the match of the second subscript. For example, </p>
<dl>
<dt>
<dd>
<pre><code>
string = "abcdefghijklm" print $
{string[(r)d?,(r)h?]
}
</code></pre>
</dl>
<p> prints `<code>defghi</code>&#8216;. This is an obvious generalisation of the rule for single-character matches. For a single subscript, only a single character is referenced (not the range of characters covered by the match). </p>
<p> Note that in substring operations the second subscript is handled differently by the <code>r</code> and <code>R</code> subscript flags: the former takes the shortest match as the length and the latter the longest match. Hence in the former case a <code>*</code> at the end is redundant while in the latter case it matches the whole remainder of the string. This does not affect the result of the single subscript case as here the length of the match is irrelevant. </p>
<h3>Array Element Assignment</h3>
<p> A subscript may be used on the left side of an assignment like so: </p>
<dl>
<dt>
<dd>
<pre>
<i>name</i><code>[</code><i>exp</i><code>]=</code><i>value</i>
</pre>
</dl>
<p> In this form of assignment the element or range specified by <i>exp</i> is replaced by the expression on the right side. An array (but not an associative array) may be created by assignment to a range or element. Arrays do not nest, so assigning a parenthesized list of values to an element or range changes the number of elements in the array, shifting the other elements to accommodate the new values. (This is not supported for associative arrays.) </p>
<p> This syntax also works as an argument to the <code>typeset</code> command: </p>
<dl>
<dt>
<dd>
<pre>
<code>typeset</code> <code>&quot;</code><i>name</i><code>[</code><i>exp</i><code>]&quot;=</code><i>value</i>
</pre>
</dl>
<p> The <i>value</i> may <i>not</i> be a parenthesized list in this case; only single-element assignments may be made with <code>typeset</code>. Note that quotes are necessary in this case to prevent the brackets from being interpreted as filename generation operators. The <code>noglob</code> precommand modifier could be used instead. </p>
<p> To delete an element of an ordinary array, assign `<code>()</code>&#8216; to that element. To delete an element of an associative array, use the <code>unset</code> command: </p>
<dl>
<dt>
<dd>
<pre>
<code>unset</code> <code>&quot;</code><i>name</i><code>[</code><i>exp</i><code>]&quot;</code>
</pre>
</dl>
<h3>Subscript Flags</h3>
<p> If the opening bracket, or the comma in a range, in any subscript expression is directly followed by an opening parenthesis, the string up to the matching closing one is considered to be a list of flags, as in `<i>name</i><code>[(</code><i>flags</i><code>)</code><i>exp</i><code>]</code>&#8216;. </p>
<p> The flags <code>s</code>, <code>n</code> and <code>b</code> take an argument; the delimiter is shown below as `<code>:</code>&#8216;, but any character, or the matching pairs `<code>(</code>&#8230;<code>)</code>&#8216;, `<code>{</code>&#8230;<code>}</code>&#8216;, `<code>[</code>&#8230;<code>]</code>&#8216;, or `<code>&lt;</code>&#8230;<code>&gt;</code>&#8216;, may be used, but note that `<code>&lt;</code>&#8230;<code>&gt;</code>&#8216; can only be used if the subscript is inside a double quoted expression or a parameter substitution enclosed in braces as otherwise the expression is interpreted as a redirection. </p>
<p> The flags currently understood are: </p>
<dl>
<dt>
<dd> <code>w</code> If the parameter subscripted is a scalar then this flag makes subscripting work on words instead of characters. The default word separator is whitespace. When combined with the <code>i</code> or <code>I</code> flag, the effect is to produce the index of the first character of the first/last word which matches the given pattern; note that a failed match in this case always yields 0.</p>
<dt><code>s:</code><i>string</i><code>:</code></p>
<dd> This gives the <i>string</i> that separates words (for use with the <code>w</code> flag). The delimiter character <code>:</code> is arbitrary; see above.</p>
<dt><code>p</code></p>
<dd> Recognize the same escape sequences as the <code>print</code> builtin in the string argument of a subsequent `<code>s</code>&#8216; flag.</p>
<dt><code>f</code></p>
<dd> If the parameter subscripted is a scalar then this flag makes subscripting work on lines instead of characters, i.e. with elements separated by newlines. This is a shorthand for `<code>pws:
:</code>&#8216;.</p>
<dt><code>r</code></p>
<dd> Reverse subscripting: if this flag is given, the <i>exp</i> is taken as a pattern and the result is the first matching array element, substring or word (if the parameter is an array, if it is a scalar, or if it is a scalar and the `<code>w</code>&#8216; flag is given, respectively). The subscript used is the number of the matching element, so that pairs of subscripts such as `<code>$foo[(r)??,3]</code>&#8216; and `<code>$foo[(r)??,(r)f*]</code>&#8216; are possible if the parameter is not an associative array. If the parameter is an associative array, only the value part of each pair is compared to the pattern, and the result is that value.</p>
<dl>
<dt>
<dd>
<p> If a search through an ordinary array failed, the search sets the subscript to one past the end of the array, and hence <code>${array[(r)</code><i>pattern</i><code>]}</code> will substitute the empty string. Thus the success of a search can be tested by using the <code>(i)</code> flag, for example (assuming the option <code>KSH_ARRAYS</code> is not in effect): </p>
<dl>
<dt>
<dd>
[[${array[(i)pattern]} &#8211; le ${#array}]]
</dl>
<p> If <code>KSH_ARRAYS</code> is in effect, the <code>-le</code> should be replaced by <code>-lt</code>.</dl>
<dt><code>R</code></p>
<dd> Like `<code>r</code>&#8216;, but gives the last match. For associative arrays, gives all possible matches. May be used for assigning to ordinary array elements, but not for assigning to associative arrays. On failure, for normal arrays this has the effect of returning the element corresponding to subscript 0; this is empty unless one of the options <code>KSH_ARRAYS</code> or <code>KSH_ZERO_SUBSCRIPT</code> is in effect.</p>
<dl>
<dt>
<dd>
<p> Note that in subscripts with both `<code>r</code>&#8216; and `<code>R</code>&#8216; pattern characters are active even if they were substituted for a parameter (regardless of the setting of <code>GLOB_SUBST</code> which controls this feature in normal pattern matching). The flag `<code>e</code>&#8216; can be added to inhibit pattern matching. As this flag does not inhibit other forms of substitution, care is still required; using a parameter to hold the key has the desired effect: </p>
<dl>
<dt>
<dd>
key2 = &#8216;original key&#8217; print $<br />
{<br />
    array[(Re)$key2]<br />
}
</dl>
</dl>
<dt><code>i</code></p>
<dd> Like `<code>r</code>&#8216;, but gives the index of the match instead; this may not be combined with a second argument. On the left side of an assignment, behaves like `<code>r</code>&#8216;. For associative arrays, the key part of each pair is compared to the pattern, and the first matching key found is the result. On failure substitutes the length of the array plus one, as discussed under the description of `<code>r</code>&#8216;, or the empty string for an associative array.</p>
<dt><code>I</code></p>
<dd> Like `<code>i</code>&#8216;, but gives the index of the last match, or all possible matching keys in an associative array. On failure substitutes 0, or the empty string for an associative array. This flag is best when testing for values or keys that do not exist.</p>
<dt><code>k</code></p>
<dd> If used in a subscript on an associative array, this flag causes the keys to be interpreted as patterns, and returns the value for the first key found where <i>exp</i> is matched by the key. Note this could be any such key as no ordering of associative arrays is defined. This flag does not work on the left side of an assignment to an associative array element. If used on another type of parameter, this behaves like `<code>r</code>&#8216;.</p>
<dt><code>K</code></p>
<dd> On an associative array this is like `<code>k</code>&#8216; but returns all values where <i>exp</i> is matched by the keys. On other types of parameters this has the same effect as `<code>R</code>&#8216;.</p>
<dt><code>n:</code><i>expr</i><code>:</code></p>
<dd> If combined with `<code>r</code>&#8216;, `<code>R</code>&#8216;, `<code>i</code>&#8216; or `<code>I</code>&#8216;, makes them give the <i>n</i>th or <i>n</i>th last match (if <i>expr</i> evaluates to <i>n</i>). This flag is ignored when the array is associative. The delimiter character <code>:</code> is arbitrary; see above.</p>
<dt><code>b:</code><i>expr</i><code>:</code></p>
<dd> If combined with `<code>r</code>&#8216;, `<code>R</code>&#8216;, `<code>i</code>&#8216; or `<code>I</code>&#8216;, makes them begin at the <i>n</i>th or <i>n</i>th last element, word, or character (if <i>expr</i> evaluates to <i>n</i>). This flag is ignored when the array is associative. The delimiter character <code>:</code> is arbitrary; see above.</p>
<dt><code>e</code></p>
<dd> This flag causes any pattern matching that would be performed on the subscript to use plain string matching instead. Hence `<code>${array[(re)*]}</code>&#8216; matches only the array element whose value is <code>*</code>. Note that other forms of substitution such as parameter substitution are not inhibited.</p>
<dl>
<dt>
<dd>
<p> This flag can also be used to force <code>*</code> or <code>@</code> to be interpreted as a single key rather than as a reference to all values. It may be used for either purpose on the left side of an assignment.</dl>
</dl>
<p> See <i>Parameter Expansion Flags</i> (<i><a href="/docs/linux/man/1-zshexpn/">zshexpn</a></i>(1)) for additional ways to manipulate the results of array subscripting. </p>
<h3>Subscript Parsing</h3>
<p> This discussion applies mainly to associative array key strings and to patterns used for reverse subscripting (the `<code>r</code>&#8216;, `<code>R</code>&#8216;, `<code>i</code>&#8216;, etc. flags), but it may also affect parameter substitutions that appear as part of an arithmetic expression in an ordinary subscript. </p>
<p> To avoid subscript parsing limitations in assignments to associative array elements, use the append syntax: </p>
<dl>
<dt>
<dd>
<pre>
<code>aa+=('key with &quot;*strange*&quot; characters' 'value string')</code>
</pre>
</dl>
<p> The basic rule to remember when writing a subscript expression is that all text between the opening `<code>[</code>&#8216; and the closing `<code>]</code>&#8216; is interpreted <i>as if</i> it were in double quotes (see <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1)). However, unlike double quotes which normally cannot nest, subscript expressions may appear inside double-quoted strings or inside other subscript expressions (or both!), so the rules have two important differences. </p>
<p> The first difference is that brackets (`<code>[</code>&#8216; and `<code>]</code>&#8216;) must appear as balanced pairs in a subscript expression unless they are preceded by a backslash (`<code>\</code>&#8216;). Therefore, within a subscript expression (and unlike true double-quoting) the sequence `<code>\[</code>&#8216; becomes `<code>[</code>&#8216;, and similarly `<code>\]</code>&#8216; becomes `<code>]</code>&#8216;. This applies even in cases where a backslash is not normally required; for example, the pattern `<code>[^[]</code>&#8216; (to match any character other than an open bracket) should be written `<code>[^\[]</code>&#8216; in a reverse-subscript pattern. However, note that `<code>\[^\[\]</code>&#8216; and even `<code>\[^[]</code>&#8216; mean the <i>same</i> thing, because backslashes are always stripped when they appear before brackets! </p>
<p> The same rule applies to parentheses (`<code>(</code>&#8216; and `<code>)</code>&#8216;) and braces (`<code>{</code>&#8216; and `<code>}</code>&#8216;): they must appear either in balanced pairs or preceded by a backslash, and backslashes that protect parentheses or braces are removed during parsing. This is because parameter expansions may be surrounded by balanced braces, and subscript flags are introduced by balanced parentheses. </p>
<p> The second difference is that a double-quote (`<code>&quot;</code>&#8216;) may appear as part of a subscript expression without being preceded by a backslash, and therefore that the two characters `<code>\&quot;</code>&#8216; remain as two characters in the subscript (in true double-quoting, `<code>\&quot;</code>&#8216; becomes `<code>&quot;</code>&#8216;). However, because of the standard shell quoting rules, any double-quotes that appear must occur in balanced pairs unless preceded by a backslash. This makes it more difficult to write a subscript expression that contains an odd number of double-quote characters, but the reason for this difference is so that when a subscript expression appears inside true double-quotes, one can still write `<code>\&quot;</code>&#8216; (rather than `<code>\\&quot;</code>&#8216;) for `<code>&quot;</code>&#8216;. </p>
<p> To use an odd number of double quotes as a key in an assignment, use the <code>typeset</code> builtin and an enclosing pair of double quotes; to refer to the value of that key, again use double quotes: </p>
<dl>
<dt>
<dd>
typeset &#8211; A aa<br />
              typeset &#8220;aa[one\&#8221;two\&#8221;three\&#8221;quotes]&#8221; = QQQ<br />
    print &#8220;$aa[one\&#8221;two\&#8221;three\&#8221;quotes]&#8221;
</dl>
<p> It is important to note that the quoting rules do not change when a parameter expansion with a subscript is nested inside another subscript expression. That is, it is not necessary to use additional backslashes within the inner subscript expression; they are removed only once, from the innermost subscript outwards. Parameters are also expanded from the innermost subscript first, as each expansion is encountered left to right in the outer expression. </p>
<p> A further complication arises from a way in which subscript parsing is <i>not</i> different from double quote parsing. As in true double-quoting, the sequences `<code>\*</code>&#8216;, and `<code>\@</code>&#8216; remain as two characters when they appear in a subscript expression. To use a literal `<code>*</code>&#8216; or `<code>@</code>&#8216; as an associative array key, the `<code>e</code>&#8216; flag must be used: </p>
<dl>
<dt>
<dd>
typeset &#8211; A aa<br />
              aa[(e) * ] = star<br />
    print $aa[(e) * ]
</dl>
<p> A last detail must be considered when reverse subscripting is performed. Parameters appearing in the subscript expression are first expanded and then the complete expression is interpreted as a pattern. This has two effects: first, parameters behave as if <code>GLOB_SUBST</code> were on (and it cannot be turned off); second, backslashes are interpreted twice, once when parsing the array subscript and again when parsing the pattern. In a reverse subscript, it&#8217;s necessary to use <i>four</i> backslashes to cause a single backslash to match literally in the pattern. For complex patterns, it is often easiest to assign the desired pattern to a parameter and then refer to that parameter in the subscript, because then the backslashes, brackets, parentheses, etc., are seen only when the complete expression is converted to a pattern. To match the value of a parameter literally in a reverse subscript, rather than as a pattern, use `<code>${(q</code><code>)</code><i>name</i><code>}</code>&#8216; (see <i><a href="/docs/linux/man/1-zshexpn/">zshexpn</a></i>(1)) to quote the expanded value. </p>
<p> Note that the `<code>k</code>&#8216; and `<code>K</code>&#8216; flags are reverse subscripting for an ordinary array, but are <i>not</i> reverse subscripting for an associative array! (For an associative array, the keys in the array itself are interpreted as patterns by those flags; the subscript is a plain string in that case.) </p>
<p> One final note, not directly related to subscripting: the numeric names of positional parameters (described below) are parsed specially, so for example `<code>$2foo</code>&#8216; is equivalent to `<code>${2}foo</code>&#8216;. Therefore, to use subscript syntax to extract a substring from a positional parameter, the expansion must be surrounded by braces; for example, `<code>${2[3,5]}</code>&#8216; evaluates to the third through fifth characters of the second positional parameter, but `<code>$2[3,5]</code>&#8216; is the entire second parameter concatenated with the filename generation pattern `<code>[3,5]</code>&#8216;. </p>
<h2>POSITIONAL PARAMETERS</h2>
<p> The positional parameters provide access to the command-line arguments of a shell function, shell script, or the shell itself; see the section `Invocation&#8217;, and also the section `Functions&#8217;. The parameter <i>n</i>, where <i>n</i> is a number, is the <i>n</i>th positional parameter. The parameter `<code>$0</code>&#8216; is a special case, see the section `Parameters Set By The Shell&#8217;. </p>
<p> The parameters <code>*</code>, <code>@</code> and <code>argv</code> are arrays containing all the positional parameters; thus `<code>$argv[</code><i>n</i><code>]</code>&#8216;, etc., is equivalent to simply `<code>$</code><i>n</i>&#8216;. Note that the options <code>KSH_ARRAYS</code> or <code>KSH_ZERO_SUBSCRIPT</code> apply to these arrays as well, so with either of those options set, `<code>${argv[0]}</code>&#8216; is equivalent to `<code>$1</code>&#8216; and so on. </p>
<p> Positional parameters may be changed after the shell or function starts by using the <code>set</code> builtin, by assigning to the <code>argv</code> array, or by direct assignment of the form `<i>n</i><code>=</code><i>value</i>&#8216; where <i>n</i> is the number of the positional parameter to be changed. This also creates (with empty values) any of the positions from 1 to <i>n</i> that do not already have values. Note that, because the positional parameters form an array, an array assignment of the form `<i>n</i><code>=(</code><i>value</i> &#8230;<code>)</code>&#8216; is allowed, and has the effect of shifting all the values at positions greater than <i>n</i> by as many positions as necessary to accommodate the new values. </p>
<h2>LOCAL PARAMETERS</h2>
<p> Shell function executions delimit scopes for shell parameters. (Parameters are dynamically scoped.) The <code>typeset</code> builtin, and its alternative forms <code>declare</code>, <code>integer</code>, <code>local</code> and <code>readonly</code> (but not <code>export</code>), can be used to declare a parameter as being local to the innermost scope. </p>
<p> When a parameter is read or assigned to, the innermost existing parameter of that name is used. (That is, the local parameter hides any less-local parameter.) However, assigning to a non-existent parameter, or declaring a new parameter with <code>export</code>, causes it to be created in the <i>outer</i>most scope. </p>
<p> Local parameters disappear when their scope ends. <code>unset</code> can be used to delete a parameter while it is still in scope; any outer parameter of the same name remains hidden. </p>
<p> Special parameters may also be made local; they retain their special attributes unless either the existing or the newly-created parameter has the <code>-h</code> (hide) attribute. This may have unexpected effects: there is no default value, so if there is no assignment at the point the variable is made local, it will be set to an empty value (or zero in the case of integers). The following: </p>
<dl>
<dt>
<dd>
<pre>
<code>typeset PATH=/new/directory:$PATH</code>
</pre>
</dl>
<p> is valid for temporarily allowing the shell or programmes called from it to find the programs in <code>/new/directory</code> inside a function. </p>
<p> Note that the restriction in older versions of zsh that local parameters were never exported has been removed. </p>
<h2>PARAMETERS SET BY THE SHELL</h2>
<p> In the parameter lists that follow, the mark `&lt;S&gt;&#8217; indicates that the parameter is special. `&lt;Z&gt;&#8217; indicates that the parameter does not exist when the shell initializes in <code>sh</code> or <code>ksh</code> emulation mode. </p>
<p> The following parameters are automatically set by the shell: </p>
<dl>
<dt>
<dd> <code>!</code> &lt;S&gt; The process ID of the last command started in the background with <code>&amp;</code>, put into the background with the <code>bg</code> builtin, or spawned with <code>coproc</code>.</p>
<dt><code>#</code> &lt;S&gt;</p>
<dd> The number of positional parameters in decimal. Note that some confusion may occur with the syntax <code>$#</code><i>param</i> which substitutes the length of <i>param</i>. Use <code>${#}</code> to resolve ambiguities. In particular, the sequence `<code>$#-</code><i>&#8230;</i>&#8216; in an arithmetic expression is interpreted as the length of the parameter <code>&#8211;</code>, q.v.</p>
<dt><code>ARGC</code> &lt;S&gt; &lt;Z&gt;</p>
<dd> Same as <code>#</code>.</p>
<dt><code>$</code> &lt;S&gt;</p>
<dd> The process ID of this shell. Note that this indicates the original shell started by invoking <code>zsh</code>; all processes forked from the shells without executing a new program, such as subshells started by <code>(</code><i>&#8230;</i><code>)</code>, substitute the same value.</p>
<dt><code>&#8211;</code> &lt;S&gt;</p>
<dd> Flags supplied to the shell on invocation or by the <code>set</code> or <code>setopt</code> commands.</p>
<dt><code>*</code> &lt;S&gt;</p>
<dd> An array containing the positional parameters.</p>
<dt><code>argv</code> &lt;S&gt; &lt;Z&gt;</p>
<dd> Same as <code>*</code>. Assigning to <code>argv</code> changes the local positional parameters, but <code>argv</code> is <i>not</i> itself a local parameter. Deleting <code>argv</code> with <code>unset</code> in any function deletes it everywhere, although only the innermost positional parameter array is deleted (so <code>*</code> and <code>@</code> in other scopes are not affected).</p>
<dt><code>@</code> &lt;S&gt;</p>
<dd> Same as <code>argv[@]</code>, even when <code>argv</code> is not set.</p>
<dt><code>?</code> &lt;S&gt;</p>
<dd> The exit status returned by the last command.</p>
<dt><code>0</code> &lt;S&gt;</p>
<dd> The name used to invoke the current shell, or as set by the <code>-c</code> command line option upon invocation. If the <code>FUNCTION_ARGZERO</code> option is set, <code>$0</code> is set upon entry to a shell function to the name of the function, and upon entry to a sourced script to the name of the script, and reset to its previous value when the function or script returns.</p>
<dt><code>status</code> &lt;S&gt; &lt;Z&gt;</p>
<dd> Same as <code>?</code>.</p>
<dt><code>pipestatus</code> &lt;S&gt; &lt;Z&gt;</p>
<dd> An array containing the exit statuses returned by all commands in the last pipeline.</p>
<dt><code>_</code> &lt;S&gt;</p>
<dd> The last argument of the previous command. Also, this parameter is set in the environment of every command executed to the full pathname of the command.</p>
<dt><code>CPUTYPE</code></p>
<dd> The machine type (microprocessor class or machine model), as determined at run time.</p>
<dt><code>EGID</code> &lt;S&gt;</p>
<dd> The effective group ID of the shell process. If you have sufficient privileges, you may change the effective group ID of the shell process by assigning to this parameter. Also (assuming sufficient privileges), you may start a single command with a different effective group ID by `<code>(EGID=</code><i>gid</i><code>; command)</code>&#8216;</p>
<dl>
<dt>
<dd>
<p> If this is made local, it is not implicitly set to 0, but may be explicitly set locally.</dl>
<dt><code>EUID</code> &lt;S&gt;</p>
<dd> The effective user ID of the shell process. If you have sufficient privileges, you may change the effective user ID of the shell process by assigning to this parameter. Also (assuming sufficient privileges), you may start a single command with a different effective user ID by `<code>(EUID=</code><i>uid</i><code>; command)</code>&#8216;</p>
<dl>
<dt>
<dd>
<p> If this is made local, it is not implicitly set to 0, but may be explicitly set locally.</dl>
<dt><code>ERRNO</code> &lt;S&gt;</p>
<dd> The value of errno (see <i><a href="/docs/linux/man/3-errno/">errno</a></i>(3)) as set by the most recently failed system call. This value is system dependent and is intended for debugging purposes. It is also useful with the <code>zsh/system</code> module which allows the number to be turned into a name or message.</p>
<dt><code>FUNCNEST</code> &lt;S&gt;</p>
<dd> Integer. If greater than or equal to zero, the maximum nesting depth of shell functions. When it is exceeded, an error is raised at the point where a function is called. The default value is determined when the shell is configured, but is typically 500. Increasing the value increases the danger of a runaway function recursion causing the shell to crash. Setting a negative value turns off the check.</p>
<dt><code>GID</code> &lt;S&gt;</p>
<dd> The real group ID of the shell process. If you have sufficient privileges, you may change the group ID of the shell process by assigning to this parameter. Also (assuming sufficient privileges), you may start a single command under a different group ID by `<code>(GID=</code><i>gid</i><code>; command)</code>&#8216;</p>
<dl>
<dt>
<dd>
<p> If this is made local, it is not implicitly set to 0, but may be explicitly set locally.</dl>
<dt><code>HISTCMD</code></p>
<dd> The current history event number in an interactive shell, in other words the event number for the command that caused <code>$HISTCMD</code> to be read. If the current history event modifies the history, <code>HISTCMD</code> changes to the new maximum history event number.</p>
<dt><code>HOST</code></p>
<dd> The current hostname.</p>
<dt><code>LINENO</code> &lt;S&gt;</p>
<dd> The line number of the current line within the current script, sourced file, or shell function being executed, whichever was started most recently. Note that in the case of shell functions the line number refers to the function as it appeared in the original definition, not necessarily as displayed by the <code>functions</code> builtin.</p>
<dt><code>LOGNAME</code></p>
<dd> If the corresponding variable is not set in the environment of the shell, it is initialized to the login name corresponding to the current login session. This parameter is exported by default but this can be disabled using the <code>typeset</code> builtin. The value is set to the string returned by the <i><a href="/docs/linux/man/3-getlogin/">getlogin</a></i>(3) system call if that is available.</p>
<dt><code>MACHTYPE</code></p>
<dd> The machine type (microprocessor class or machine model), as determined at compile time.</p>
<dt><code>OLDPWD</code></p>
<dd> The previous working directory. This is set when the shell initializes and whenever the directory changes.</p>
<dt><code>OPTARG</code> &lt;S&gt;</p>
<dd> The value of the last option argument processed by the <code>getopts</code> command.</p>
<dt><code>OPTIND</code> &lt;S&gt;</p>
<dd> The index of the last option argument processed by the <code>getopts</code> command.</p>
<dt><code>OSTYPE</code></p>
<dd> The operating system, as determined at compile time.</p>
<dt><code>PPID</code> &lt;S&gt;</p>
<dd> The process ID of the parent of the shell. As for <code>$$</code>, the value indicates the parent of the original shell and does not change in subshells.</p>
<dt><code>PWD</code></p>
<dd> The present working directory. This is set when the shell initializes and whenever the directory changes.</p>
<dt><code>RANDOM</code> &lt;S&gt;</p>
<dd> A pseudo-random integer from 0 to 32767, newly generated each time this parameter is referenced. The random number generator can be seeded by assigning a numeric value to <code>RANDOM</code>.</p>
<dl>
<dt>
<dd>
<p> The values of <code>RANDOM</code> form an intentionally-repeatable pseudo-random sequence; subshells that reference <code>RANDOM</code> will result in identical pseudo-random values unless the value of <code>RANDOM</code> is referenced or seeded in the parent shell in between subshell invocations.</dl>
<dt><code>SECONDS</code> &lt;S&gt;</p>
<dd> The number of seconds since shell invocation. If this parameter is assigned a value, then the value returned upon reference will be the value that was assigned plus the number of seconds since the assignment.</p>
<dl>
<dt>
<dd>
<p> Unlike other special parameters, the type of the <code>SECONDS</code> parameter can be changed using the <code>typeset</code> command. Only integer and one of the floating point types are allowed. For example, `<code>typeset -F SECONDS</code>&#8216; causes the value to be reported as a floating point number. The value is available to microsecond accuracy, although the shell may show more or fewer digits depending on the use of <code>typeset</code>. See the documentation for the builtin <code>typeset</code> in <i><a href="/docs/linux/man/1-zshbuiltins/">zshbuiltins</a></i>(1) for more details.</dl>
<dt><code>SHLVL</code> &lt;S&gt;</p>
<dd> Incremented by one each time a new shell is started.</p>
<dt><code>signals</code></p>
<dd> An array containing the names of the signals. Note that with the standard zsh numbering of array indices, where the first element has index 1, the signals are offset by 1 from the signal number used by the operating system. For example, on typical Unix-like systems <code>HUP</code> is signal number 1, but is referred to as <code>$signals[2]</code>. This is because of <code>EXIT</code> at position 1 in the array, which is used internally by zsh but is not known to the operating system.</p>
<dt><code>TRY_BLOCK_ERROR</code> &lt;S&gt;</p>
<dd> In an <code>always</code> block, indicates whether the preceding list of code caused an error. The value is 1 to indicate an error, 0 otherwise. It may be reset, clearing the error condition. See <i>Complex Commands</i> in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1)</p>
<dt><code>TRY_BLOCK_INTERRUPT</code> &lt;S&gt;</p>
<dd> This variable works in a similar way to <code>TRY_BLOCK_ERROR</code>, but represents the status of an interrupt from the signal SIGINT, which typically comes from the keyboard when the user types <code>^C</code>. If set to 0, any such interrupt will be reset; otherwise, the interrupt is propagated after the <code>always</code> block.</p>
<dl>
<dt>
<dd>
<p> Note that it is possible that an interrupt arrives during the execution of the <code>always</code> block; this interrupt is also propagated.</dl>
<dt><code>TTY</code></p>
<dd> The name of the tty associated with the shell, if any.</p>
<dt><code>TTYIDLE</code> &lt;S&gt;</p>
<dd> The idle time of the tty associated with the shell in seconds or -1 if there is no such tty.</p>
<dt><code>UID</code> &lt;S&gt;</p>
<dd> The real user ID of the shell process. If you have sufficient privileges, you may change the user ID of the shell by assigning to this parameter. Also (assuming sufficient privileges), you may start a single command under a different user ID by `<code>(UID=</code><i>uid</i><code>; command)</code>&#8216;</p>
<dl>
<dt>
<dd>
<p> If this is made local, it is not implicitly set to 0, but may be explicitly set locally.</dl>
<dt><code>USERNAME</code> &lt;S&gt;</p>
<dd> The username corresponding to the real user ID of the shell process. If you have sufficient privileges, you may change the username (and also the user ID and group ID) of the shell by assigning to this parameter. Also (assuming sufficient privileges), you may start a single command under a different username (and user ID and group ID) by `<code>(USERNAME=</code><i>username</i><code>; command)</code>&#8216;</p>
<dt><code>VENDOR</code></p>
<dd> The vendor, as determined at compile time.</p>
<dt><code>zsh_eval_context</code> &lt;S&gt; &lt;Z&gt; (<code>ZSH_EVAL_CONTEXT</code> &lt;S&gt;)</p>
<dd> An array (colon-separated list) indicating the context of shell code that is being run. Each time a piece of shell code that is stored within the shell is executed a string is temporarily appended to the array to indicate the type of operation that is being performed. Read in order the array gives an indication of the stack of operations being performed with the most immediate context last.</p>
<dl>
<dt>
<dd>
<p> Note that the variable does not give information on syntactic context such as pipelines or subshells. Use <code>$ZSH_SUBSHELL</code> to detect subshells. </p>
<p> The context is one of the following:</p>
<dl>
<dt>
<dd> <code>cmdarg</code> Code specified by the <code>-c</code> option to the command line that invoked the shell.</p>
<dt><code>cmdsubst</code></p>
<dd> Command substitution using the <code>`</code><i>&#8230;</i><code>`</code> or <code>$(</code><i>&#8230;</i><code>)</code> construct.</p>
<dt><code>equalsubst</code></p>
<dd> File substitution using the <code>=(</code><i>&#8230;</i><code>)</code> construct.</p>
<dt><code>eval</code></p>
<dd> Code executed by the <code>eval</code> builtin.</p>
<dt><code>evalautofunc</code></p>
<dd> Code executed with the <code>KSH_AUTOLOAD</code> mechanism in order to define an autoloaded function.</p>
<dt><code>fc</code></p>
<dd> Code from the shell history executed by the <code>-e</code> option to the <code>fc</code> builtin.</p>
<dt><code>file</code></p>
<dd> Lines of code being read directly from a file, for example by the <code>source</code> builtin.</p>
<dt><code>filecode</code></p>
<dd> Lines of code being read from a <code>.zwc</code> file instead of directly from the source file.</p>
<dt><code>globqual</code></p>
<dd> Code executed by the <code>e</code> or <code>+</code> glob qualifier.</p>
<dt><code>globsort</code></p>
<dd> Code executed to order files by the <code>o</code> glob qualifier.</p>
<dt><code>insubst</code></p>
<dd> File substitution using the <code>&lt;(</code><i>&#8230;</i><code>)</code> construct.</p>
<dt><code>loadautofunc</code></p>
<dd> Code read directly from a file to define an autoloaded function.</p>
<dt><code>outsubst</code></p>
<dd> File substitution using the <code>&gt;(</code><i>&#8230;</i><code>)</code> construct.</p>
<dt><code>sched</code></p>
<dd> Code executed by the <code>sched</code> builtin.</p>
<dt><code>shfunc</code></p>
<dd> A shell function.</p>
<dt><code>stty</code></p>
<dd> Code passed to <code>stty</code> by the <code>STTY</code> environment variable. Normally this is passed directly to the system&#8217;s <code>stty</code> command, so this value is unlikely to be seen in practice.</p>
<dt><code>style</code></p>
<dd> Code executed as part of a style retrieved by the <code>zstyle</code> builtin from the <code>zsh/zutil</code> module.</p>
<dt><code>toplevel</code></p>
<dd> The highest execution level of a script or interactive shell.</p>
<dt><code>trap</code></p>
<dd> Code executed as a trap defined by the <code>trap</code> builtin. Traps defined as functions have the context <code>shfunc</code>. As traps are asynchronous they may have a different hierarchy from other code.</p>
<dt><code>zpty</code></p>
<dd> Code executed by the <code>zpty</code> builtin from the <code>zsh/zpty</code> module.</p>
<dt><code>zregexparse-guard</code></p>
<dd> Code executed as a guard by the <code>zregexparse</code> command from the <code>zsh/zutil</code> module.</p>
<dt><code>zregexparse-action</code></p>
<dd> Code executed as an action by the <code>zregexparse</code> command from the <code>zsh/zutil</code> module.</dl>
</dl>
<dt><code>ZSH_ARGZERO</code></p>
<dd> If zsh was invoked to run a script, this is the name of the script. Otherwise, it is the name used to invoke the current shell. This is the same as the value of <code>$0</code> when the <code>POSIX_ARGZERO</code> option is set, but is always available.</p>
<dt><code>ZSH_EXECUTION_STRING</code></p>
<dd> If the shell was started with the option <code>-c</code>, this contains the argument passed to the option. Otherwise it is not set.</p>
<dt><code>ZSH_NAME</code></p>
<dd> Expands to the basename of the command used to invoke this instance of zsh.</p>
<dt><code>ZSH_PATCHLEVEL</code></p>
<dd> The output of `<code>git describe &#8211;tags &#8211;long</code>&#8216; for the zsh repository used to build the shell. This is most useful in order to keep track of versions of the shell during development between releases; hence most users should not use it and should instead rely on <code>$ZSH_VERSION</code>.</p>
<dt><code>zsh_scheduled_events</code></p>
<dd> See the section `The zsh/sched Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1).</p>
<dt><code>ZSH_SCRIPT</code></p>
<dd> If zsh was invoked to run a script, this is the name of the script, otherwise it is unset.</p>
<dt><code>ZSH_SUBSHELL</code></p>
<dd> Readonly integer. Initially zero, incremented each time the shell forks to create a subshell for executing code. Hence `<code>(print $ZSH_SUBSHELL)</code>&#8216; and `<code>print $(print $ZSH_SUBSHELL)</code>&#8216; output 1, while `<code>( (print $ZSH_SUBSHELL) )</code>&#8216; outputs 2.</p>
<dt><code>ZSH_VERSION</code></p>
<dd> The version number of the release of zsh.</dl>
<h2>PARAMETERS USED BY THE SHELL</h2>
<p> The following parameters are used by the shell. Again, `&lt;S&gt;&#8217; indicates that the parameter is special and `&lt;Z&gt;&#8217; indicates that the parameter does not exist when the shell initializes in <code>sh</code> or <code>ksh</code> emulation mode. </p>
<p> In cases where there are two parameters with an upper- and lowercase form of the same name, such as <code>path</code> and <code>PATH</code>, the lowercase form is an array and the uppercase form is a scalar with the elements of the array joined together by colons. These are similar to tied parameters created via `<code>typeset -T</code>&#8216;. The normal use for the colon-separated form is for exporting to the environment, while the array form is easier to manipulate within the shell. Note that unsetting either of the pair will unset the other; they retain their special properties when recreated, and recreating one of the pair will recreate the other. </p>
<dl>
<dt>
<dd> <code>ARGV0</code> If exported, its value is used as the <code>argv[0]</code> of external commands. Usually used in constructs like `<code>ARGV0=emacs nethack</code>&#8216;.</p>
<dt><code>BAUD</code></p>
<dd> The rate in bits per second at which data reaches the terminal. The line editor will use this value in order to compensate for a slow terminal by delaying updates to the display until necessary. If the parameter is unset or the value is zero the compensation mechanism is turned off. The parameter is not set by default.</p>
<dl>
<dt>
<dd>
<p> This parameter may be profitably set in some circumstances, e.g. for slow modems dialing into a communications server, or on a slow wide area network. It should be set to the baud rate of the slowest part of the link for best performance.</dl>
<dt><code>cdpath</code> &lt;S&gt; &lt;Z&gt; (<code>CDPATH</code> &lt;S&gt;)</p>
<dd> An array (colon-separated list) of directories specifying the search path for the <code>cd</code> command.</p>
<dt><code>COLUMNS</code> &lt;S&gt;</p>
<dd> The number of columns for this terminal session. Used for printing select lists and for the line editor.</p>
<dt><code>CORRECT_IGNORE</code></p>
<dd> If set, is treated as a pattern during spelling correction. Any potential correction that matches the pattern is ignored. For example, if the value is `<code>_*</code>&#8216; then completion functions (which, by convention, have names beginning with `<code>_</code>&#8216;) will never be offered as spelling corrections. The pattern does not apply to the correction of file names, as applied by the <code>CORRECT_ALL</code> option (so with the example just given files beginning with `<code>_</code>&#8216; in the current directory would still be completed).</p>
<dt><code>CORRECT_IGNORE_FILE</code></p>
<dd> If set, is treated as a pattern during spelling correction of file names. Any file name that matches the pattern is never offered as a correction. For example, if the value is `<code>.*</code>&#8216; then dot file names will never be offered as spelling corrections. This is useful with the <code>CORRECT_ALL</code> option.</p>
<dt><code>DIRSTACKSIZE</code></p>
<dd> The maximum size of the directory stack, by default there is no limit. If the stack gets larger than this, it will be truncated automatically. This is useful with the <code>AUTO_PUSHD</code> option.</p>
<dt><code>ENV</code></p>
<dd> If the <code>ENV</code> environment variable is set when zsh is invoked as <code>sh</code> or <code>ksh</code>, <code>$ENV</code> is sourced after the profile scripts. The value of <code>ENV</code> is subjected to parameter expansion, command substitution, and arithmetic expansion before being interpreted as a pathname. Note that <code>ENV</code> is <i>not</i> used unless the shell is interactive and zsh is emulating <code>sh</code> or <code>ksh</code>.</p>
<dt><code>FCEDIT</code></p>
<dd> The default editor for the <code>fc</code> builtin. If <code>FCEDIT</code> is not set, the parameter <code>EDITOR</code> is used; if that is not set either, a builtin default, usually <code>vi</code>, is used.</p>
<dt><code>fignore</code> &lt;S&gt; &lt;Z&gt; (<code>FIGNORE</code> &lt;S&gt;)</p>
<dd> An array (colon separated list) containing the suffixes of files to be ignored during filename completion. However, if completion only generates files with suffixes in this list, then these files are completed anyway.</p>
<dt><code>fpath</code> &lt;S&gt; &lt;Z&gt; (<code>FPATH</code> &lt;S&gt;)</p>
<dd> An array (colon separated list) of directories specifying the search path for function definitions. This path is searched when a function with the <code>-u</code> attribute is referenced. If an executable file is found, then it is read and executed in the current environment.</p>
<dt><code>histchars</code> &lt;S&gt;</p>
<dd> Three characters used by the shell&#8217;s history and lexical analysis mechanism. The first character signals the start of a history expansion (default `<code>!</code>&#8216;). The second character signals the start of a quick history substitution (default `<code>^</code>&#8216;). The third character is the comment character (default `<code>#</code>&#8216;).</p>
<dl>
<dt>
<dd>
<p> The characters must be in the ASCII character set; any attempt to set <code>histchars</code> to characters with a locale-dependent meaning will be rejected with an error message.</dl>
<dt><code>HISTCHARS</code> &lt;S&gt; &lt;Z&gt;</p>
<dd> Same as <code>histchars</code>. (Deprecated.)</p>
<dt><code>HISTFILE</code></p>
<dd> The file to save the history in when an interactive shell exits. If unset, the history is not saved.</p>
<dt><code>HISTORY_IGNORE</code></p>
<dd> If set, is treated as a pattern at the time history files are written. Any potential history entry that matches the pattern is skipped. For example, if the value is `<code>fc *</code>&#8216; then commands that invoke the interactive history editor are never written to the history file.</p>
<dl>
<dt>
<dd>
<p> Note that <code>HISTORY_IGNORE</code> defines a single pattern: to specify alternatives use the `<code>(</code><i>first</i><code>|</code><i>second</i><code>|</code><i>&#8230;</i><code>)</code>&#8216; syntax. </p>
<p> Compare the <code>HIST_NO_STORE</code> option or the <code>zshaddhistory</code> hook, either of which would prevent such commands from being added to the interactive history at all. If you wish to use <code>HISTORY_IGNORE</code> to stop history being added in the first place, you can define the following hook: </p>
<dl>
<dt>
<dd>
<pre><code>
zshaddhistory()
{
    emulate - L zsh##uncomment if HISTORY_IGNORE##should use EXTENDED_GLOB syntax
#setopt extendedglob
        [[$1 != ${~HISTORY_IGNORE}]]
}
</code></pre>
</dl>
</dl>
<dt><code>HISTSIZE</code> &lt;S&gt;</p>
<dd> The maximum number of events stored in the internal history list. If you use the <code>HIST_EXPIRE_DUPS_FIRST</code> option, setting this value larger than the <code>SAVEHIST</code> size will give you the difference as a cushion for saving duplicated history events.</p>
<dl>
<dt>
<dd>
<p> If this is made local, it is not implicitly set to 0, but may be explicitly set locally.</dl>
<dt><code>HOME</code> &lt;S&gt;</p>
<dd> The default argument for the <code>cd</code> command. This is not set automatically by the shell in <code>sh</code>, <code>ksh</code> or <code>csh</code> emulation, but it is typically present in the environment anyway, and if it becomes set it has its usual special behaviour.</p>
<dt><code>IFS</code> &lt;S&gt;</p>
<dd> Internal field separators (by default space, tab, newline and NUL), that are used to separate words which result from command or parameter expansion and words read by the <code>read</code> builtin. Any characters from the set space, tab and newline that appear in the IFS are called <i>IFS white space</i>. One or more IFS white space characters or one non-IFS white space character together with any adjacent IFS white space character delimit a field. If an IFS white space character appears twice consecutively in the IFS, this character is treated as if it were not an IFS white space character.</p>
<dl>
<dt>
<dd>
<p> If the parameter is unset, the default is used. Note this has a different effect from setting the parameter to an empty string.</dl>
<dt><code>KEYBOARD_HACK</code></p>
<dd> This variable defines a character to be removed from the end of the command line before interpreting it (interactive shells only). It is intended to fix the problem with keys placed annoyingly close to return and replaces the <code>SUNKEYBOARDHACK</code> option which did this for backquotes only. Should the chosen character be one of singlequote, doublequote or backquote, there must also be an odd number of them on the command line for the last one to be removed.</p>
<dl>
<dt>
<dd>
<p> For backward compatibility, if the <code>SUNKEYBOARDHACK</code> option is explicitly set, the value of <code>KEYBOARD_HACK</code> reverts to backquote. If the option is explicitly unset, this variable is set to empty.</dl>
<dt><code>KEYTIMEOUT</code></p>
<dd> The time the shell waits, in hundredths of seconds, for another key to be pressed when reading bound multi-character sequences.</p>
<dt><code>LANG</code> &lt;S&gt;</p>
<dd> This variable determines the locale category for any category not specifically selected via a variable starting with `<code>LC_</code>&#8216;.</p>
<dt><code>LC_ALL</code> &lt;S&gt;</p>
<dd> This variable overrides the value of the `<code>LANG</code>&#8216; variable and the value of any of the other variables starting with `<code>LC_</code>&#8216;.</p>
<dt><code>LC_COLLATE</code> &lt;S&gt;</p>
<dd> This variable determines the locale category for character collation information within ranges in glob brackets and for sorting.</p>
<dt><code>LC_CTYPE</code> &lt;S&gt;</p>
<dd> This variable determines the locale category for character handling functions. If the <code>MULTIBYTE</code> option is in effect this variable or <code>LANG</code> should contain a value that reflects the character set in use, even if it is a single-byte character set, unless only the 7-bit subset (ASCII) is used. For example, if the character set is ISO-8859-1, a suitable value might be <code>en_US.iso88591</code> (certain Linux distributions) or <code>en_US.ISO8859-1</code> (MacOS).</p>
<dt><code>LC_MESSAGES</code> &lt;S&gt;</p>
<dd> This variable determines the language in which messages should be written. Note that zsh does not use message catalogs.</p>
<dt><code>LC_NUMERIC</code> &lt;S&gt;</p>
<dd> This variable affects the decimal point character and thousands separator character for the formatted input/output functions and string conversion functions. Note that zsh ignores this setting when parsing floating point mathematical expressions.</p>
<dt><code>LC_TIME</code> &lt;S&gt;</p>
<dd> This variable determines the locale category for date and time formatting in prompt escape sequences.</p>
<dt><code>LINES</code> &lt;S&gt;</p>
<dd> The number of lines for this terminal session. Used for printing select lists and for the line editor.</p>
<dt><code>LISTMAX</code></p>
<dd> In the line editor, the number of matches to list without asking first. If the value is negative, the list will be shown if it spans at most as many lines as given by the absolute value. If set to zero, the shell asks only if the top of the listing would scroll off the screen.</p>
<dt><code>LOGCHECK</code></p>
<dd> The interval in seconds between checks for login/logout activity using the <code>watch</code> parameter.</p>
<dt><code>MAIL</code></p>
<dd> If this parameter is set and <code>mailpath</code> is not set, the shell looks for mail in the specified file.</p>
<dt><code>MAILCHECK</code></p>
<dd> The interval in seconds between checks for new mail.</p>
<dt><code>mailpath</code> &lt;S&gt; &lt;Z&gt; (<code>MAILPATH</code> &lt;S&gt;)</p>
<dd> An array (colon-separated list) of filenames to check for new mail. Each filename can be followed by a `<code>?</code>&#8216; and a message that will be printed. The message will undergo parameter expansion, command substitution and arithmetic expansion with the variable <code>$_</code> defined as the name of the file that has changed. The default message is `<code>You have new mail</code>&#8216;. If an element is a directory instead of a file the shell will recursively check every file in every subdirectory of the element.</p>
<dt><code>manpath</code> &lt;S&gt; &lt;Z&gt; (<code>MANPATH</code> &lt;S&gt; &lt;Z&gt;)</p>
<dd> An array (colon-separated list) whose value is not used by the shell. The <code>manpath</code> array can be useful, however, since setting it also sets <code>MANPATH</code>, and vice versa.</p>
<dt>
<dd> <code>match</code></p>
<dt>
<dd> <code>mbegin</code></p>
<dt>
<dd> <code>mend</code> Arrays set by the shell when the <code>b</code> globbing flag is used in pattern matches. See the subsection <i>Globbing flags</i> in the documentation for <i>Filename Generation</i> in <i><a href="/docs/linux/man/1-zshexpn/">zshexpn</a></i>(1).</p>
<dt>
<dd> <code>MATCH</code></p>
<dt>
<dd> <code>MBEGIN</code></p>
<dt>
<dd> <code>MEND</code> Set by the shell when the <code>m</code> globbing flag is used in pattern matches. See the subsection <i>Globbing flags</i> in the documentation for <i>Filename Generation</i> in <i><a href="/docs/linux/man/1-zshexpn/">zshexpn</a></i>(1).</p>
<dt><code>module_path</code> &lt;S&gt; &lt;Z&gt; (<code>MODULE_PATH</code> &lt;S&gt;)</p>
<dd> An array (colon-separated list) of directories that <code>zmodload</code> searches for dynamically loadable modules. This is initialized to a standard pathname, usually `<code>/usr/local/lib/zsh/$ZSH_VERSION</code>&#8216;. (The `<code>/usr/local/lib</code>&#8216; part varies from installation to installation.) For security reasons, any value set in the environment when the shell is started will be ignored.</p>
<dl>
<dt>
<dd>
<p> These parameters only exist if the installation supports dynamic module loading.</dl>
<dt><code>NULLCMD</code> &lt;S&gt;</p>
<dd> The command name to assume if a redirection is specified with no command. Defaults to <code>cat</code>. For <code>sh</code>/<code>ksh</code> behavior, change this to <code>:</code>. For <code>csh</code>-like behavior, unset this parameter; the shell will print an error message if null commands are entered.</p>
<dt><code>path</code> &lt;S&gt; &lt;Z&gt; (<code>PATH</code> &lt;S&gt;)</p>
<dd> An array (colon-separated list) of directories to search for commands. When this parameter is set, each directory is scanned and all files found are put in a hash table.</p>
<dt><code>POSTEDIT</code> &lt;S&gt;</p>
<dd> This string is output whenever the line editor exits. It usually contains termcap strings to reset the terminal.</p>
<dt>
<dd> <code>PROMPT</code> &lt;S&gt; &lt;Z&gt;</p>
<dt>
<dd> <code>PROMPT2</code> &lt;S&gt; &lt;Z&gt;</p>
<dt>
<dd> <code>PROMPT3</code> &lt;S&gt; &lt;Z&gt;</p>
<dt>
<dd> <code>PROMPT4</code> &lt;S&gt; &lt;Z&gt; Same as <code>PS1</code>, <code>PS2</code>, <code>PS3</code> and <code>PS4</code>, respectively.</p>
<dt><code>prompt</code> &lt;S&gt; &lt;Z&gt;</p>
<dd> Same as <code>PS1</code>.</p>
<dt><code>PROMPT_EOL_MARK</code></p>
<dd> When the <code>PROMPT_CR</code> and <code>PROMPT_SP</code> options are set, the <code>PROMPT_EOL_MARK</code> parameter can be used to customize how the end of partial lines are shown. This parameter undergoes prompt expansion, with the <code>PROMPT_PERCENT</code> option set. If not set, the default behavior is equivalent to the value `<code>%B%S%#%s%b</code>&#8216;.</p>
<dt><code>PS1</code> &lt;S&gt;</p>
<dd> The primary prompt string, printed before a command is read. It undergoes a special form of expansion before being displayed; see EXPANSION OF PROMPT SEQUENCES in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1). The default is `<code>%m%# </code>&#8216;.</p>
<dt><code>PS2</code> &lt;S&gt;</p>
<dd> The secondary prompt, printed when the shell needs more information to complete a command. It is expanded in the same way as <code>PS1</code>. The default is `<code>%_&gt; </code>&#8216;, which displays any shell constructs or quotation marks which are currently being processed.</p>
<dt><code>PS3</code> &lt;S&gt;</p>
<dd> Selection prompt used within a <code>select</code> loop. It is expanded in the same way as <code>PS1</code>. The default is `<code>?# </code>&#8216;.</p>
<dt><code>PS4</code> &lt;S&gt;</p>
<dd> The execution trace prompt. Default is `<code>+%N:%i&gt; </code>&#8216;, which displays the name of the current shell structure and the line number within it. In sh or ksh emulation, the default is `<code>+ </code>&#8216;.</p>
<dt><code>psvar</code> &lt;S&gt; &lt;Z&gt; (<code>PSVAR</code> &lt;S&gt;)</p>
<dd> An array (colon-separated list) whose elements can be used in <code>PROMPT</code> strings. Setting <code>psvar</code> also sets <code>PSVAR</code>, and vice versa.</p>
<dt><code>READNULLCMD</code> &lt;S&gt;</p>
<dd> The command name to assume if a single input redirection is specified with no command. Defaults to <code>more</code>.</p>
<dt><code>REPORTMEMORY</code></p>
<dd> If nonnegative, commands whose maximum resident set size (roughly speaking, main memory usage) in kilobytes is greater than this value have timing statistics reported. The format used to output statistics is the value of the <code>TIMEFMT</code> parameter, which is the same as for the <code>REPORTTIME</code> variable and the <code>time</code> builtin; note that by default this does not output memory usage. Appending <code>&quot; max RSS %M&quot;</code> to the value of <code>TIMEFMT</code> causes it to output the value that triggered the report. If <code>REPORTTIME</code> is also in use, at most a single report is printed for both triggers. This feature requires the <code>getrusage()</code> system call, commonly supported by modern Unix-like systems.</p>
<dt><code>REPORTTIME</code></p>
<dd> If nonnegative, commands whose combined user and system execution times (measured in seconds) are greater than this value have timing statistics printed for them. Output is suppressed for commands executed within the line editor, including completion; commands explicitly marked with the <code>time</code> keyword still cause the summary to be printed in this case.</p>
<dt><code>REPLY</code></p>
<dd> This parameter is reserved by convention to pass string values between shell scripts and shell builtins in situations where a function call or redirection are impossible or undesirable. The <code>read</code> builtin and the <code>select</code> complex command may set <code>REPLY</code>, and filename generation both sets and examines its value when evaluating certain expressions. Some modules also employ <code>REPLY</code> for similar purposes.</p>
<dt><code>reply</code></p>
<dd> As <code>REPLY</code>, but for array values rather than strings.</p>
<dt>
<dd> <code>RPROMPT</code> &lt;S&gt;</p>
<dt>
<dd> <code>RPS1</code> &lt;S&gt; This prompt is displayed on the right-hand side of the screen when the primary prompt is being displayed on the left. This does not work if the <code>SINGLE_LINE_ZLE</code> option is set. It is expanded in the same way as <code>PS1</code>.</p>
<dt>
<dd> <code>RPROMPT2</code> &lt;S&gt;</p>
<dt>
<dd> <code>RPS2</code> &lt;S&gt; This prompt is displayed on the right-hand side of the screen when the secondary prompt is being displayed on the left. This does not work if the <code>SINGLE_LINE_ZLE</code> option is set. It is expanded in the same way as <code>PS2</code>.</p>
<dt><code>SAVEHIST</code></p>
<dd> The maximum number of history events to save in the history file.</p>
<dl>
<dt>
<dd>
<p> If this is made local, it is not implicitly set to 0, but may be explicitly set locally.</dl>
<dt><code>SPROMPT</code> &lt;S&gt;</p>
<dd> The prompt used for spelling correction. The sequence `<code>%R</code>&#8216; expands to the string which presumably needs spelling correction, and `<code>%r</code>&#8216; expands to the proposed correction. All other prompt escapes are also allowed.</p>
<dl>
<dt>
<dd>
<p> The actions available at the prompt are <code>[nyae]</code>:</p>
<dl>
<dt><code>n</code> (`no&#8217;) (default)</p>
<dd> Discard the correction and run the command.</p>
<dt><code>y</code> (`yes&#8217;)</p>
<dd> Make the correction and run the command.</p>
<dt><code>a</code> (`abort&#8217;)</p>
<dd> Discard the entire command line without running it.</p>
<dt><code>e</code> (`edit&#8217;)</p>
<dd> Resume editing the command line.</dl>
</dl>
<dt><code>STTY</code></p>
<dd> If this parameter is set in a command&#8217;s environment, the shell runs the <code>stty</code> command with the value of this parameter as arguments in order to set up the terminal before executing the command. The modes apply only to the command, and are reset when it finishes or is suspended. If the command is suspended and continued later with the <code>fg</code> or <code>wait</code> builtins it will see the modes specified by <code>STTY</code>, as if it were not suspended. This (intentionally) does not apply if the command is continued via `<code>kill -CONT</code>&#8216;. <code>STTY</code> is ignored if the command is run in the background, or if it is in the environment of the shell but not explicitly assigned to in the input line. This avoids running stty at every external command by accidentally exporting it. Also note that <code>STTY</code> should not be used for window size specifications; these will not be local to the command.</p>
<dt><code>TERM</code> &lt;S&gt;</p>
<dd> The type of terminal in use. This is used when looking up termcap sequences. An assignment to <code>TERM</code> causes zsh to re-initialize the terminal, even if the value does not change (e.g., `<code>TERM=$TERM</code>&#8216;). It is necessary to make such an assignment upon any change to the terminal definition database or terminal type in order for the new settings to take effect.</p>
<dt><code>TERMINFO</code> &lt;S&gt;</p>
<dd> A reference to your terminfo database, used by the `terminfo&#8217; library when the system has it; see <i><a href="/docs/linux/man/5-terminfo/">terminfo</a></i>(5). If set, this causes the shell to reinitialise the terminal, making the workaround `<code>TERM=$TERM</code>&#8216; unnecessary.</p>
<dt><code>TERMINFO_DIRS</code> &lt;S&gt;</p>
<dd> A colon-seprarated list of terminfo databases, used by the `terminfo&#8217; library when the system has it; see <i><a href="/docs/linux/man/5-terminfo/">terminfo</a></i>(5). This variable is only used by certain terminal libraries, in particular ncurses; see <i><a href="/docs/linux/man/5-terminfo/">terminfo</a></i>(5) to check support on your system. If set, this causes the shell to reinitialise the terminal, making the workaround `<code>TERM=$TERM</code>&#8216; unnecessary. Note that unlike other colon-separated arrays this is not tied to a zsh array.</p>
<dt><code>TIMEFMT</code></p>
<dd> The format of process time reports with the <code>time</code> keyword. The default is `<code>%J %U user %S system %P cpu %*E total</code>&#8216;. Recognizes the following escape sequences, although not all may be available on all systems, and some that are available may not be useful:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>%%</code></p>
<dd> A `<code>%</code>&#8216;.</p>
<dt><code>%U</code></p>
<dd> CPU seconds spent in user mode.</p>
<dt><code>%S</code></p>
<dd> CPU seconds spent in kernel mode.</p>
<dt><code>%E</code></p>
<dd> Elapsed time in seconds.</p>
<dt><code>%P</code></p>
<dd> The CPU percentage, computed as 100*(<code>%U</code>+<code>%S</code>)/<code>%E</code>.</p>
<dt><code>%W</code></p>
<dd> Number of times the process was swapped.</p>
<dt><code>%X</code></p>
<dd> The average amount in (shared) text space used in kilobytes.</p>
<dt><code>%D</code></p>
<dd> The average amount in (unshared) data/stack space used in kilobytes.</p>
<dt><code>%K</code></p>
<dd> The total space used (<code>%X</code>+<code>%D</code>) in kilobytes.</p>
<dt><code>%M</code></p>
<dd> The maximum memory the process had in use at any time in kilobytes.</p>
<dt><code>%F</code></p>
<dd> The number of major page faults (page needed to be brought from disk).</p>
<dt><code>%R</code></p>
<dd> The number of minor page faults.</p>
<dt><code>%I</code></p>
<dd> The number of input operations.</p>
<dt><code>%O</code></p>
<dd> The number of output operations.</p>
<dt><code>%r</code></p>
<dd> The number of socket messages received.</p>
<dt><code>%s</code></p>
<dd> The number of socket messages sent.</p>
<dt><code>%k</code></p>
<dd> The number of signals received.</p>
<dt><code>%w</code></p>
<dd> Number of voluntary context switches (waits).</p>
<dt><code>%c</code></p>
<dd> Number of involuntary context switches.</p>
<dt><code>%J</code></p>
<dd> The name of this job.</dl>
<p> A star may be inserted between the percent sign and flags printing time (e.g., `<code>%*E</code>&#8216;); this causes the time to be printed in `<i>hh</i><code>:</code><i>mm</i><code>:</code><i>ss</i><code>.</code><i>ttt</i>&#8216; format (hours and minutes are only printed if they are not zero). Alternatively, `<code>m</code>&#8216; or `<code>u</code>&#8216; may be used (e.g., `<code>%mE</code>&#8216;) to produce time output in milliseconds or microseconds, respectively.</dl>
<dt><code>TMOUT</code></p>
<dd> If this parameter is nonzero, the shell will receive an <code>ALRM</code> signal if a command is not entered within the specified number of seconds after issuing a prompt. If there is a trap on <code>SIGALRM</code>, it will be executed and a new alarm is scheduled using the value of the <code>TMOUT</code> parameter after executing the trap. If no trap is set, and the idle time of the terminal is not less than the value of the <code>TMOUT</code> parameter, zsh terminates. Otherwise a new alarm is scheduled to <code>TMOUT</code> seconds after the last keypress.</p>
<dt><code>TMPPREFIX</code></p>
<dd> A pathname prefix which the shell will use for all temporary files. Note that this should include an initial part for the file name as well as any directory names. The default is `<code>/tmp/zsh</code>&#8216;.</p>
<dt><code>TMPSUFFIX</code></p>
<dd> A filename suffix which the shell will use for temporary files created by process substitutions (e.g., `<code>=(</code><i>list</i>)&#8217;). Note that the value should include a leading dot `<code>.</code>&#8216; if intended to be interpreted as a file extension. The default is not to append any suffix, thus this parameter should be assigned only when needed and then unset again.</p>
<dt><code>watch</code> &lt;S&gt; &lt;Z&gt; (<code>WATCH</code> &lt;S&gt;)</p>
<dd> An array (colon-separated list) of login/logout events to report.</p>
<dl>
<dt>
<dd>
<p> If it contains the single word `<code>all</code>&#8216;, then all login/logout events are reported. If it contains the single word `<code>notme</code>&#8216;, then all events are reported as with `<code>all</code>&#8216; except <code>$USERNAME</code>. </p>
<p> An entry in this list may consist of a username, an `<code>@</code>&#8216; followed by a remote hostname, and a `<code>%</code>&#8216; followed by a line (tty). Any of these may be a pattern (be sure to quote this during the assignment to <code>watch</code> so that it does not immediately perform file generation); the setting of the <code>EXTENDED_GLOB</code> option is respected. Any or all of these components may be present in an entry; if a login/logout event matches all of them, it is reported. </p>
<p> For example, with the <code>EXTENDED_GLOB</code> option set, the following: </p>
<dl>
<dt>
<dd>
<pre>
<code>watch=('^(pws|barts)')</code>
</pre>
</dl>
<p> causes reports for activity associated with any user other than <code>pws</code> or <code>barts</code>.</dl>
<dt><code>WATCHFMT</code></p>
<dd> The format of login/logout reports if the <code>watch</code> parameter is set. Default is `<code>%n has %a %l from %m</code>&#8216;. Recognizes the following escape sequences:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>%n</code> The name of the user that logged in/out.</p>
<dt><code>%a</code></p>
<dd> The observed action, i.e. &quot;logged on&quot; or &quot;logged off&quot;.</p>
<dt><code>%l</code></p>
<dd> The line (tty) the user is logged in on.</p>
<dt><code>%M</code></p>
<dd> The full hostname of the remote host.</p>
<dt><code>%m</code></p>
<dd> The hostname up to the first `<code>.</code>&#8216;. If only the IP address is available or the utmp field contains the name of an X-windows display, the whole name is printed.</p>
<dl>
<dt>
<dd>
<p> <i>NOTE:</i> The `<code>%m</code>&#8216; and `<code>%M</code>&#8216; escapes will work only if there is a host name field in the utmp on your machine. Otherwise they are treated as ordinary strings.</dl>
<dt><code>%S</code> (<code>%s</code>)</p>
<dd> Start (stop) standout mode.</p>
<dt><code>%U</code> (<code>%u</code>)</p>
<dd> Start (stop) underline mode.</p>
<dt><code>%B</code> (<code>%b</code>)</p>
<dd> Start (stop) boldface mode.</p>
<dt>
<dd> <code>%t</code></p>
<dt>
<dd> <code>%@</code> The time, in 12-hour, am/pm format.</p>
<dt><code>%T</code></p>
<dd> The time, in 24-hour format.</p>
<dt><code>%w</code></p>
<dd> The date in `<i>day</i><code>&#8211;</code><i>dd</i>&#8216; format.</p>
<dt><code>%W</code></p>
<dd> The date in `<i>mm</i><code>/</code><i>dd</i><code>/</code><i>yy</i>&#8216; format.</p>
<dt><code>%D</code></p>
<dd> The date in `<i>yy</i><code>&#8211;</code><i>mm</i><code>&#8211;</code><i>dd</i>&#8216; format.</p>
<dt><code>%D{</code><i>string</i><code>}</code></p>
<dd> The date formatted as <i>string</i> using the <code>strftime</code> function, with zsh extensions as described by EXPANSION OF PROMPT SEQUENCES in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1).</p>
<dt><code>%(</code><i>x</i><code>:</code><i>true-text</i><code>:</code><i>false-text</i><code>)</code></p>
<dd> Specifies a ternary expression. The character following the <i>x</i> is arbitrary; the same character is used to separate the text for the &quot;true&quot; result from that for the &quot;false&quot; result. Both the separator and the right parenthesis may be escaped with a backslash. Ternary expressions may be nested.</p>
<dl>
<dt>
<dd>
<p> The test character <i>x</i> may be any one of `<code>l</code>&#8216;, `<code>n</code>&#8216;, `<code>m</code>&#8216; or `<code>M</code>&#8216;, which indicate a `true&#8217; result if the corresponding escape sequence would return a non-empty value; or it may be `<code>a</code>&#8216;, which indicates a `true&#8217; result if the watched user has logged in, or `false&#8217; if he has logged out. Other characters evaluate to neither true nor false; the entire expression is omitted in this case. </p>
<p> If the result is `true&#8217;, then the <i>true-text</i> is formatted according to the rules above and printed, and the <i>false-text</i> is skipped. If `false&#8217;, the <i>true-text</i> is skipped and the <i>false-text</i> is formatted and printed. Either or both of the branches may be empty, but both separators must be present in any case.</dl>
</dl>
</dl>
<dt><code>WORDCHARS</code> &lt;S&gt;</p>
<dd> A list of non-alphanumeric characters considered part of a word by the line editor.</p>
<dt><code>ZBEEP</code></p>
<dd> If set, this gives a string of characters, which can use all the same codes as the <code>bindkey</code> command as described in the zsh/zle module entry in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1), that will be output to the terminal instead of beeping. This may have a visible instead of an audible effect; for example, the string `<code>[?5h[?5l</code>&#8216; on a vt100 or xterm will have the effect of flashing reverse video on and off (if you usually use reverse video, you should use the string `<code>[?5l[?5h</code>&#8216; instead). This takes precedence over the <code>NOBEEP</code> option.</p>
<dt><code>ZDOTDIR</code></p>
<dd> The directory to search for shell startup files (.zshrc, etc), if not <code>$HOME</code>.</p>
<dt><code>zle_bracketed_paste</code></p>
<dd> Many terminal emulators have a feature that allows applications to identify when text is pasted into the terminal rather than being typed normally. For ZLE, this means that special characters such as tabs and newlines can be inserted instead of invoking editor commands. Furthermore, pasted text forms a single undo event and if the region is active, pasted text will replace the region.</p>
<dl>
<dt>
<dd>
<p> This two-element array contains the terminal escape sequences for enabling and disabling the feature. These escape sequences are used to enable bracketed paste when ZLE is active and disable it at other times. Unsetting the parameter has the effect of ensuring that bracketed paste remains disabled.</dl>
<dt><code>zle_highlight</code></p>
<dd> An array describing contexts in which ZLE should highlight the input text. See <i>Character Highlighting</i> in <i><a href="/docs/linux/man/1-zshzle/">zshzle</a></i>(1).</p>
<dt><code>ZLE_LINE_ABORTED</code></p>
<dd> This parameter is set by the line editor when an error occurs. It contains the line that was being edited at the point of the error. `<code>print -zr &#8212; $ZLE_LINE_ABORTED</code>&#8216; can be used to recover the line. Only the most recent line of this kind is remembered.</p>
<dt>
<dd> <code>ZLE_REMOVE_SUFFIX_CHARS</code></p>
<dt>
<dd> <code>ZLE_SPACE_SUFFIX_CHARS</code> These parameters are used by the line editor. In certain circumstances suffixes (typically space or slash) added by the completion system will be removed automatically, either because the next editing command was not an insertable character, or because the character was marked as requiring the suffix to be removed.</p>
<dl>
<dt>
<dd>
<p> These variables can contain the sets of characters that will cause the suffix to be removed. If <code>ZLE_REMOVE_SUFFIX_CHARS</code> is set, those characters will cause the suffix to be removed; if <code>ZLE_SPACE_SUFFIX_CHARS</code> is set, those characters will cause the suffix to be removed and replaced by a space. </p>
<p> If <code>ZLE_REMOVE_SUFFIX_CHARS</code> is not set, the default behaviour is equivalent to: </p>
<dl>
<dt>
<dd>
<pre>
<code>ZLE_REMOVE_SUFFIX_CHARS=$' 	
;&amp;|'</code>
</pre>
</dl>
<p> If <code>ZLE_REMOVE_SUFFIX_CHARS</code> is set but is empty, no characters have this behaviour. <code>ZLE_SPACE_SUFFIX_CHARS</code> takes precedence, so that the following: </p>
<dl>
<dt>
<dd>
<pre>
<code>ZLE_SPACE_SUFFIX_CHARS=$'&amp;|'</code>
</pre>
</dl>
<p> causes the characters `<code>&amp;</code>&#8216; and `<code>|</code>&#8216; to remove the suffix but to replace it with a space. </p>
<p> To illustrate the difference, suppose that the option <code>AUTO_REMOVE_SLASH</code> is in effect and the directory <code>DIR</code> has just been completed, with an appended <code>/</code>, following which the user types `<code>&amp;</code>&#8216;. The default result is `<code>DIR&amp;</code>&#8216;. With <code>ZLE_REMOVE_SUFFIX_CHARS</code> set but without including `<code>&amp;</code>&#8216; the result is `<code>DIR/&amp;</code>&#8216;. With <code>ZLE_SPACE_SUFFIX_CHARS</code> set to include `<code>&amp;</code>&#8216; the result is `<code>DIR &amp;</code>&#8216;. </p>
<p> Note that certain completions may provide their own suffix removal or replacement behaviour which overrides the values described here. See the completion system documentation in <i><a href="/docs/linux/man/1-zshcompsys/">zshcompsys</a></i>(1).</dl>
<dt><code>ZLE_RPROMPT_INDENT</code> &lt;S&gt;</p>
<dd> If set, used to give the indentation between the right hand side of the right prompt in the line editor as given by <code>RPS1</code> or <code>RPROMPT</code> and the right hand side of the screen. If not set, the value 1 is used.</p>
<dl>
<dt>
<dd>
<p> Typically this will be used to set the value to 0 so that the prompt appears flush with the right hand side of the screen. This is not the default as many terminals do not handle this correctly, in particular when the prompt appears at the extreme bottom right of the screen. Recent virtual terminals are more likely to handle this case correctly. Some experimentation is necessary.</dl>
</dl>
<h2>Index</h2>

---
title: "perldata(1)"
name: "perldata"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perldata/"
description: "perldata – Perl data types"
---

<h2 class="name">NAME</h2>
<p> perldata &#8211; Perl data types </p>
<h2>DESCRIPTION</h2>
<h3>Variable names</h3>
<p> Perl has three built-in data types: scalars, arrays of scalars, and associative arrays of scalars, known as &#8220;hashes&#8221;. A scalar is a single string (of any size, limited only by the available memory), number, or a reference to something (which will be discussed in perlref). Normal arrays are ordered lists of scalars indexed by number, starting with 0. Hashes are unordered collections of scalar values indexed by their associated string key. </p>
<p> Values are usually referred to by name, or through a named reference. The first character of the name tells you to what sort of data structure it refers. The rest of the name tells you the particular value to which it refers. Usually this name is a single <i>identifier</i>, that is, a string beginning with a letter or underscore, and containing letters, underscores, and digits. In some cases, it may be a chain of identifiers, separated by <tt>&quot;::&quot;</tt> (or by the slightly archaic <tt>&quot;'&quot;</tt>); all but the last are interpreted as names of packages, to locate the namespace in which to look up the final identifier (see &#8220;Packages&#8221; in perlmod for details). For a more in-depth discussion on identifiers, see &#8220;Identifier parsing&#8221;. It&#8217;s possible to substitute for a simple identifier, an expression that produces a reference to the value at runtime. This is described in more detail below and in perlref. </p>
<p> Perl also has its own built-in variables whose names don&#8217;t follow these rules. They have strange names so they don&#8217;t accidentally collide with one of your normal variables. Strings that match parenthesized parts of a regular expression are saved under names containing only digits after the <tt>&quot;$&quot;</tt> (see perlop and perlre). In addition, several special variables that provide windows into the inner working of Perl have names containing punctuation characters. These are documented in perlvar. </p>
<p> Scalar values are always named with &#8216;$&#8217;, even when referring to a scalar that is part of an array or a hash. The &#8216;$&#8217; symbol works semantically like the English word &#8220;the&#8221; in that it indicates a single value is expected. </p>
<pre><code>
$days #the simple scalar value "days" $days[28] #the 29th element of array @days
        $days{'Feb'} #the 'Feb' value from hash %
    days
        $ #days #the last index of array @days
</code></pre>
<p> Entire arrays (and slices of arrays and hashes) are denoted by &#8216;@&#8217;, which works much as the word &#8220;these&#8221; or &#8220;those&#8221; does in English, in that it indicates multiple values are expected. </p>
<p>@days #($days[0], $days[1], &#8230; $days[n])<br />
    @days[3, 4, 5] #same as($days[3], $days[4], $days[5])<br />
        @days<br />
{<br />
    &#8216;a&#8217;, &#8216;c&#8217;<br />
}<br />
#same as($days{&#8216;a&#8217;}, $days{&#8216;c&#8217;})</p>
<p> Entire hashes are denoted by &#8216;%&#8217;: </p>
<pre>
    %days               # (key1, val1, key2, val2 ...)
</pre>
<p> In addition, subroutines are named with an initial &#8216;&amp;&#8217;, though this is optional when unambiguous, just as the word &#8220;do&#8221; is often redundant in English. Symbol table entries can be named with an initial &#8216;*&#8217;, but you don&#8217;t really care about that yet (if ever :-). </p>
<p> Every variable type has its own namespace, as do several non-variable identifiers. This means that you can, without fear of conflict, use the same name for a scalar variable, an array, or a hash&#8212;or, for that matter, for a filehandle, a directory handle, a subroutine name, a format name, or a label. This means that <tt>$foo</tt> and <tt>@foo</tt> are two different variables. It also means that <tt>$foo[1]</tt> is a part of <tt>@foo</tt>, not a part of <tt>$foo</tt>. This may seem a bit weird, but that&#8217;s okay, because it is weird. </p>
<p> Because variable references always start with &#8216;$&#8217;, &#8216;@&#8217;, or &#8216;%&#8217;, the &#8220;reserved&#8221; words aren&#8217;t in fact reserved with respect to variable names. They <i>are</i> reserved with respect to labels and filehandles, however, which don&#8217;t have an initial special character. You can&#8217;t have a filehandle named &#8220;log&#8221;, for instance. Hint: you could say <tt>&quot;open(LOG,'logfile')&quot;</tt> rather than <tt>&quot;open(log,'logfile')&quot;</tt>. Using uppercase filehandles also improves readability and protects you from conflict with future reserved words. Case <i>is</i> significant&#8211;&#8220;<font SIZE="-1">FOO&#8221;,</font> &#8220;Foo&#8221;, and &#8220;foo&#8221; are all different names. Names that start with a letter or underscore may also contain digits and underscores. </p>
<p> It is possible to replace such an alphanumeric name with an expression that returns a reference to the appropriate type. For a description of this, see perlref. </p>
<p> Names that start with a digit may contain only more digits. Names that do not start with a letter, underscore, digit or a caret are limited to one character, e.g., <tt>$%</tt> or <tt>$$</tt>. (Most of these one character names have a predefined significance to Perl. For instance, <tt>$$</tt> is the current process id. And all such names are reserved for Perl&#8217;s possible use.)</p>
<h3>Identifier parsing</h3>
<p> Up until Perl 5.18, the actual rules of what a valid identifier was were a bit fuzzy. However, in general, anything defined here should work on previous versions of Perl, while the opposite &#8212; edge cases that work in previous versions, but aren&#8217;t defined here &#8212; probably won&#8217;t work on newer versions. As an important side note, please note that the following only applies to bareword identifiers as found in Perl source code, not identifiers introduced through symbolic references, which have much fewer restrictions. If working under the effect of the <tt>&quot;use utf8;&quot;</tt> pragma, the following rules apply: </p>
<p>    / (?[ ( \p{Word} &amp; \p{XID_Start} ) + [_] ])<br />
      (?[ ( \p{Word} &amp; \p{XID_Continue} ) ]) *    /x</p>
<p> That is, a &#8220;start&#8221; character followed by any number of &#8220;continue&#8221; characters. Perl requires every character in an identifier to also match <tt>&quot;\w&quot;</tt> (this prevents some problematic cases); and Perl additionally accepts identfier names beginning with an underscore. </p>
<p> If not under <tt>&quot;use utf8&quot;</tt>, the source is treated as <font SIZE="-1">ASCII + 128</font> extra generic characters, and identifiers should match </p>
<pre>
    / (?aa) (?!\d) \w+ /x
</pre>
<p> That is, any word character in the <font SIZE="-1">ASCII</font> range, as long as the first character is not a digit. </p>
<p> There are two package separators in Perl: A double colon (<tt>&quot;::&quot;</tt>) and a single quote (<tt>&quot;'&quot;</tt>). Normal identifiers can start or end with a double colon, and can contain several parts delimited by double colons. Single quotes have similar rules, but with the exception that they are not legal at the end of an identifier: That is, <tt>&quot;$'foo&quot;</tt> and <tt>&quot;$foo'bar&quot;</tt> are legal, but <tt>&quot;$foo'bar'&quot;</tt> is not. </p>
<p> Additionally, if the identifier is preceded by a sigil &#8212; that is, if the identifier is part of a variable name &#8212; it may optionally be enclosed in braces. </p>
<p> While you can mix double colons with singles quotes, the quotes must come after the colons: <tt>&quot;$::::'foo&quot;</tt> and <tt>&quot;$foo::'bar&quot;</tt> are legal, but <tt>&quot;$::'::foo&quot;</tt> and <tt>&quot;$foo'::bar&quot;</tt> are not. </p>
<p> Put together, a grammar to match a basic identifier becomes </p>
<p> /<br />
  (?(DEFINE)<br />
      (?&lt;variable&gt;<br />
          (?&amp;sigil)<br />
          (?:<br />
                  (?&amp;normal_identifier)<br />
              |   \{ \s* (?&amp;normal_identifier) \s* \}<br />
          )<br />
      )<br />
      (?&lt;normal_identifier&gt;<br />
          (?: :: )* &#8216;?<br />
           (?&amp;basic_identifier)<br />
           (?: (?= (?: :: )+ &#8216;? | (?: :: )* &#8216; ) (?&amp;normal_identifier) )?<br />
          (?: :: )*<br />
      )<br />
      (?&lt;basic_identifier&gt;<br />
#is use utf8 on ?<br />
          (?(?{ (caller(0))[8] &amp; $utf8::hint_bits })<br />
              (?&amp;Perl_XIDS) (?&amp;Perl_XIDC)*<br />
            | (?aa) (?!\d) \w+<br />
          )<br />
      )<br />
      (?&lt;sigil&gt; [&amp;*\$\@\%])<br />
      (?&lt;Perl_XIDS&gt; (?[ ( \p{Word} &amp; \p{XID_Start} ) + [_] ]) )<br />
      (?&lt;Perl_XIDC&gt; (?[ \p{Word} &amp; \p{XID_Continue} ]) )<br />
  )<br />
 /x</p>
<p> Meanwhile, special identifiers don&#8217;t follow the above rules; For the most part, all of the identifiers in this category have a special meaning given by Perl. Because they have special parsing rules, these generally can&#8217;t be fully-qualified. They come in six forms (but don&#8217;t use forms 5 and 6):</p>
<dl>
<dt>1.</p>
<dd> A sigil, followed solely by digits matching <tt>&quot;\p{POSIX_Digit}&quot;</tt>, like <tt>$0</tt>, <tt>$1</tt>, or <tt>$10000</tt>.</p>
<dt>2.</p>
<dd> A sigil followed by a single character matching the <tt>&quot;\p{POSIX_Punct}&quot;</tt> property, like <tt>$!</tt> or <tt>&quot;%+&quot;</tt>, except the character <tt>&quot;{&quot;</tt> doesn&#8217;t work.</p>
<dt>3.</p>
<dd> A sigil, followed by a caret and any one of the characters <tt>&quot;[][A-Z^_?\]&quot;</tt>, like <tt>$^V</tt> or <tt>$^]</tt>.</p>
<dt>4.</p>
<dd> Similar to the above, a sigil, followed by bareword text in braces, where the first character is a caret. The next character is any one of the characters <tt>&quot;[][A-Z^_?\]&quot;</tt>, followed by <font SIZE="-1">ASCII</font> word characters. An example is <tt>&quot;${^GLOBAL_PHASE}&quot;</tt>.</p>
<dt>5.</p>
<dd> A sigil, followed by any single character in the range <tt>&quot;[�-��-�]&quot;</tt> when not under <tt>&quot;use utf8&quot;</tt>. (Under <tt>&quot;use utf8&quot;</tt>, the normal identifier rules given earlier in this section apply.) Use of non-graphic characters (the C1 controls, the NO-BREAK <font SIZE="-1">SPACE,</font> and the <font SIZE="-1">SOFT HYPHEN</font>) has been disallowed since v5.26.0. The use of the other characters is unwise, as these are all reserved to have special meaning to Perl, and none of them currently do have special meaning, though this could change without notice. </p>
<p> Note that an implication of this form is that there are identifiers only legal under <tt>&quot;use utf8&quot;</tt>, and vice-versa, for example the identifier <tt>&quot;$état&quot;</tt> is legal under <tt>&quot;use utf8&quot;</tt>, but is otherwise considered to be the single character variable <tt>$é</tt> followed by the bareword <tt>&quot;tat&quot;</tt>, the combination of which is a syntax error.</p>
<dt>6.</p>
<dd> This is a combination of the previous two forms. It is valid only when not under <tt>&quot;use utf8&quot;</tt> (normal identifier rules apply when under <tt>&quot;use utf8&quot;</tt>). The form is a sigil, followed by text in braces, where the first character is any one of the characters in the range <tt>&quot;[�-�]&quot;</tt> followed by <font SIZE="-1">ASCII</font> word characters up to the trailing brace. </p>
<p> The same caveats as the previous form apply: The non-graphic characters are no longer allowed with &#8220;use utf8&#8221;, it is unwise to use this form at all, and utf8ness makes a big difference.</dl>
<p> Prior to Perl v5.24, non-graphical <font SIZE="-1">ASCII</font> control characters were also allowed in some situations; this had been deprecated since v5.20.</p>
<h3>Context</h3>
<p> The interpretation of operations and values in Perl sometimes depends on the requirements of the context around the operation or value. There are two major contexts: list and scalar. Certain operations return list values in contexts wanting a list, and scalar values otherwise. If this is true of an operation it will be mentioned in the documentation for that operation. In other words, Perl overloads certain operations based on whether the expected return value is singular or plural. Some words in English work this way, like &#8220;fish&#8221; and &#8220;sheep&#8221;. </p>
<p> In a reciprocal fashion, an operation provides either a scalar or a list context to each of its arguments. For example, if you say </p>
<pre>
    int( &lt;STDIN&gt; )
</pre>
<p> the integer operation provides scalar context for the &lt;&gt; operator, which responds by reading one line from <font SIZE="-1">STDIN</font> and passing it back to the integer operation, which will then find the integer value of that line and return that. If, on the other hand, you say </p>
<pre>
    sort( &lt;STDIN&gt; )
</pre>
<p> then the sort operation provides list context for &lt;&gt;, which will proceed to read every line available up to the end of file, and pass that list of lines back to the sort routine, which will then sort those lines and return them as a list to whatever the context of the sort was. </p>
<p> Assignment is a little bit special in that it uses its left argument to determine the context for the right argument. Assignment to a scalar evaluates the right-hand side in scalar context, while assignment to an array or hash evaluates the righthand side in list context. Assignment to a list (or slice, which is just a list anyway) also evaluates the right-hand side in list context. </p>
<p> When you use the <tt>&quot;use warnings&quot;</tt> pragma or Perl&#8217;s <code>-w</code> command-line option, you may see warnings about useless uses of constants or functions in &#8220;void context&#8221;. Void context just means the value has been discarded, such as a statement containing only <tt>&quot;&quot;fred&quot;;&quot;</tt> or <tt>&quot;getpwuid(0);&quot;</tt>. It still counts as scalar context for functions that care whether or not they&#8217;re being called in list context. </p>
<p> User-defined subroutines may choose to care whether they are being called in a void, scalar, or list context. Most subroutines do not need to bother, though. That&#8217;s because both scalars and lists are automatically interpolated into lists. See &#8220;wantarray&#8221; in perlfunc for how you would dynamically discern your function&#8217;s calling context.</p>
<h3>Scalar values</h3>
<p> All data in Perl is a scalar, an array of scalars, or a hash of scalars. A scalar may contain one single value in any of three different flavors: a number, a string, or a reference. In general, conversion from one form to another is transparent. Although a scalar may not directly hold multiple values, it may contain a reference to an array or hash which in turn contains multiple values. </p>
<p> Scalars aren&#8217;t necessarily one thing or another. There&#8217;s no place to declare a scalar variable to be of type &#8220;string&#8221;, type &#8220;number&#8221;, type &#8220;reference&#8221;, or anything else. Because of the automatic conversion of scalars, operations that return scalars don&#8217;t need to care (and in fact, cannot care) whether their caller is looking for a string, a number, or a reference. Perl is a contextually polymorphic language whose scalars can be strings, numbers, or references (which includes objects). Although strings and numbers are considered pretty much the same thing for nearly all purposes, references are strongly-typed, uncastable pointers with builtin reference-counting and destructor invocation. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<br />
&nbsp; A scalar value is interpreted as <font SIZE="-1">FALSE</font> in the Boolean sense if it is undefined, the null string or the number 0 (or its string equivalent, &#8220;0&#8221;), and <font SIZE="-1">TRUE</font> if it is anything else. The Boolean context is just a special kind of scalar context where no conversion to a string or a number is ever performed. Negation of a true value by <tt>&quot;!&quot;</tt> or <tt>&quot;not&quot;</tt> returns a special false value. When evaluated as a string it is treated as <tt>&quot;&quot;</tt>, but as a number, it is treated as 0. Most Perl operators that return true or false behave this way. </p>
<p> There are actually two varieties of null strings (sometimes referred to as &#8220;empty&#8221; strings), a defined one and an undefined one. The defined version is just a string of length zero, such as <tt>&quot;&quot;</tt>. The undefined version is the value that indicates that there is no real value for something, such as when there was an error, or at end of file, or when you refer to an uninitialized variable or element of an array or hash. Although in early versions of Perl, an undefined scalar could become defined when first used in a place expecting a defined value, this no longer happens except for rare cases of autovivification as explained in perlref. You can use the <code>defined()</code> operator to determine whether a scalar value is defined (this has no meaning on arrays or hashes), and the <code>undef()</code> operator to produce an undefined value. </p>
<p> To find out whether a given string is a valid non-zero number, it&#8217;s sometimes enough to test it against both numeric 0 and also lexical &#8220;0&#8221; (although this will cause noises if warnings are on). That&#8217;s because strings that aren&#8217;t numbers count as 0, just as they do in <code>awk</code>: </p>
<p>if ($str == 0 &amp;&amp; $str ne &#8220;0&#8221;) {<br />
    warn &#8220;That doesn&#8217;t look like a number&#8221;;<br />
}</p>
<p> That method may be best because otherwise you won&#8217;t treat <font SIZE="-1">IEEE</font> notations like <tt>&quot;NaN&quot;</tt> or <tt>&quot;Infinity&quot;</tt> properly. At other times, you might prefer to determine whether string data can be used numerically by calling the <code>POSIX::strtod()</code> function or by inspecting your string with a regular expression (as documented in perlre). </p>
<p>warn &#8220;has nondigits&#8221; if /\D / ;<br />
warn &#8220;not a natural number&#8221; unless / ^\d + $ / ;<br />
#rejects &#8211; 3 warn &#8220;not an integer&#8221; unless / ^-    ?\d + $ / ;<br />
#rejects + 3 warn &#8220;not an integer&#8221; unless / ^[+-] ?\d + $ / ;<br />
warn &#8220;not a decimal number&#8221; unless / ^-?\d +\.     ?\d *$ / ;<br />
#rejects .2 warn &#8220;not a decimal number&#8221; unless / ^-? (?:\d + (?:\.\d *) ? |\.\d +) $ / ;<br />
    warn &#8220;not a C float&#8221;<br />
        unless /^([+-]?)(?=\d|\.\d)\d*(\.\d*)?([Ee]([+-]?\d+))?$/;</p>
<p> The length of an array is a scalar value. You may find the length of array <tt>@days</tt> by evaluating <tt>$#days</tt>, as in <code>csh</code>. However, this isn&#8217;t the length of the array; it&#8217;s the subscript of the last element, which is a different value since there is ordinarily a 0th element. Assigning to <tt>$#days</tt> actually changes the length of the array. Shortening an array this way destroys intervening values. Lengthening an array that was previously shortened does not recover values that were in those elements. </p>
<p> You can also gain some minuscule measure of efficiency by pre-extending an array that is going to get big. You can also extend an array by assigning to an element that is off the end of the array. You can truncate an array down to nothing by assigning the null list () to it. The following are equivalent: </p>
<pre>
    @whatever = ();
    $#whatever = -1;
</pre>
<p> If you evaluate an array in scalar context, it returns the length of the array. (Note that this is not true of lists, which return the last value, like the C comma operator, nor of built-in functions, which return whatever they feel like returning.) The following is always true: </p>
<pre>
    scalar(@whatever) == $#whatever + 1;
</pre>
<p> Some programmers choose to use an explicit conversion so as to leave nothing to doubt: </p>
<pre>
    $element_count = scalar(@whatever);
</pre>
<p> If you evaluate a hash in scalar context, it returns a false value if the hash is empty. If there are any key/value pairs, it returns a true value. A more precise definition is version dependent. </p>
<p> Prior to Perl 5.25 the value returned was a string consisting of the number of used buckets and the number of allocated buckets, separated by a slash. This is pretty much useful only to find out whether Perl&#8217;s internal hashing algorithm is performing poorly on your data set. For example, you stick 10,000 things in a hash, but evaluating <tt>%HASH</tt> in scalar context reveals <tt>&quot;1/16&quot;</tt>, which means only one out of sixteen buckets has been touched, and presumably contains all 10,000 of your items. This isn&#8217;t supposed to happen. </p>
<p> As of Perl 5.25 the return was changed to be the count of keys in the hash. If you need access to the old behavior you can use <tt>&quot;Hash::Util::bucket_ratio()&quot;</tt> instead. </p>
<p> If a tied hash is evaluated in scalar context, the <tt>&quot;SCALAR&quot;</tt> method is called (with a fallback to <tt>&quot;FIRSTKEY&quot;</tt>). </p>
<p> You can preallocate space for a hash by assigning to the <code>keys()</code> function. This rounds up the allocated buckets to the next power of two: </p>
<pre>
    keys(%users) = 1000;                # allocate 1024 buckets
</pre>
<h3>Scalar value constructors</h3>
<p> Numeric literals are specified in any of the following floating point or integer formats: </p>
<pre>
 12345
 12345.67
 .23E-10             # a very small number
 3.14_15_92          # a very important number
 4_294_967_296       # underscore for legibility
 0xff                # hex
 0xdead_beef         # more hex
 0377                # octal (only numbers, begins with 0)
 0b011011            # binary
 0x1.999ap-4         # hexadecimal floating point (the 'p' is required)
</pre>
<p> You are allowed to use underscores (underbars) in numeric literals between digits for legibility (but not multiple underscores in a row: <tt>&quot;23__500&quot;</tt> is not legal; <tt>&quot;23_500&quot;</tt> is). You could, for example, group binary digits by threes (as for a Unix-style mode argument such as 0b110_100_100) or by fours (to represent nibbles, as in 0b1010_0110) or in other groups. </p>
<p> String literals are usually delimited by either single or double quotes. They work much like quotes in the standard Unix shells: double-quoted string literals are subject to backslash and variable substitution; single-quoted strings are not (except for <tt>&quot;\'&quot;</tt> and <tt>&quot;\&quot;</tt>). The usual C-style backslash rules apply for making characters such as newline, tab, etc., as well as some more exotic forms. See &#8220;Quote and Quote-like Operators&#8221; in perlop for a list. </p>
<p> Hexadecimal, octal, or binary, representations in string literals (e.g. &#8216;0xff&#8217;) are not automatically converted to their integer representation. The <code>hex()</code> and <code>oct()</code> functions make these conversions for you. See &#8220;hex&#8221; in perlfunc and &#8220;oct&#8221; in perlfunc for more details. </p>
<p> Hexadecimal floating point can start just like a hexadecimal literal, and it can be followed by an optional fractional hexadecimal part, but it must be followed by <tt>&quot;p&quot;</tt>, an optional sign, and a power of two. The format is useful for accurately presenting floating point values, avoiding conversions to or from decimal floating point, and therefore avoiding possible loss in precision. Notice that while most current platforms use the 64-bit <font SIZE="-1">IEEE 754</font> floating point, not all do. Another potential source of (low-order) differences are the floating point rounding modes, which can differ between CPUs, operating systems, and compilers, and which Perl doesn&#8217;t control. </p>
<p> You can also embed newlines directly in your strings, i.e., they can end on a different line than they begin. This is nice, but if you forget your trailing quote, the error will not be reported until Perl finds another line containing the quote character, which may be much further on in the script. Variable substitution inside strings is limited to scalar variables, arrays, and array or hash slices. (In other words, names beginning with $ or @, followed by an optional bracketed expression as a subscript.) The following code segment prints out &#8220;The price is <tt>$100</tt>.&#8221; </p>
<pre>
    $Price = '$100';    # not interpolated
    print &quot;The price is $Price.
&quot;;     # interpolated
</pre>
<p> There is no double interpolation in Perl, so the <tt>$100</tt> is left as is. </p>
<p> By default floating point numbers substituted inside strings use the dot (&#8220;.&#8221;) as the decimal separator. If <tt>&quot;use locale&quot;</tt> is in effect, and <code>POSIX::setlocale()</code> has been called, the character used for the decimal separator is affected by the <font SIZE="-1">LC_NUMERIC</font> locale. See perllocale and <font SIZE="-1">POSIX</font>. </p>
<p> As in some shells, you can enclose the variable name in braces to disambiguate it from following alphanumerics (and underscores). You must also do this when interpolating a variable into a string to separate the variable name from a following double-colon or an apostrophe, since these would be otherwise treated as a package separator: </p>
<p>$who = &#8220;Larry&#8221;;<br />
print PASSWD &#8220;${who}::0:0:Superuser:/:/bin/perl
&#8221;;<br />
print &#8220;We use ${who}speak when ${who}&#8217;s here.
&#8221;;</p>
<p> Without the braces, Perl would have looked for a <tt>$whospeak</tt>, a <tt>$who::0</tt>, and a <tt>&quot;$who's&quot;</tt> variable. The last two would be the <tt>$0</tt> and the <tt>$s</tt> variables in the (presumably) non-existent package <tt>&quot;who&quot;</tt>. </p>
<p> In fact, a simple identifier within such curlies is forced to be a string, and likewise within a hash subscript. Neither need quoting. Our earlier example, <tt>$days{'Feb'}</tt> can be written as <tt>$days{Feb}</tt> and the quotes will be assumed automatically. But anything more complicated in the subscript will be interpreted as an expression. This means for example that <tt>&quot;$version{2.0}++&quot;</tt> is equivalent to <tt>&quot;$version{2}++&quot;</tt>, not to <tt>&quot;$version{'2.0'}++&quot;</tt>. </p>
<p> <i>Special floating point: infinity (Inf) and not-a-number (NaN)</i> </p>
<p> Floating point values include the special values <tt>&quot;Inf&quot;</tt> and <tt>&quot;NaN&quot;</tt>, for infinity and not-a-number. The infinity can be also negative. </p>
<p> The infinity is the result of certain math operations that overflow the floating point range, like 9**9**9. The not-a-number is the result when the result is undefined or unrepresentable. Though note that you cannot get <tt>&quot;NaN&quot;</tt> from some common &#8220;undefined&#8221; or &#8220;out-of-range&#8221; operations like dividing by zero, or square root of a negative number, since Perl generates fatal errors for those. </p>
<p> The infinity and not-a-number have their own special arithmetic rules. The general rule is that they are &#8220;contagious&#8221;: <tt>&quot;Inf&quot;</tt> plus one is <tt>&quot;Inf&quot;</tt>, and <tt>&quot;NaN&quot;</tt> plus one is <tt>&quot;NaN&quot;</tt>. Where things get interesting is when you combine infinities and not-a-numbers: <tt>&quot;Inf&quot;</tt> minus <tt>&quot;Inf&quot;</tt> and <tt>&quot;Inf&quot;</tt> divided by <tt>&quot;Inf&quot;</tt> are <tt>&quot;NaN&quot;</tt> (while <tt>&quot;Inf&quot;</tt> plus <tt>&quot;Inf&quot;</tt> is <tt>&quot;Inf&quot;</tt> and <tt>&quot;Inf&quot;</tt> times <tt>&quot;Inf&quot;</tt> is <tt>&quot;Inf&quot;</tt>). <tt>&quot;NaN&quot;</tt> is also curious in that it does not equal any number, <i>including</i> itself: <tt>&quot;NaN&quot;</tt> != <tt>&quot;NaN&quot;</tt>. </p>
<p> Perl doesn&#8217;t understand <tt>&quot;Inf&quot;</tt> and <tt>&quot;NaN&quot;</tt> as numeric literals, but you can have them as strings, and Perl will convert them as needed: &#8220;Inf&#8221; + 1. (You can, however, import them from the <font SIZE="-1">POSIX</font> extension; <tt>&quot;use POSIX qw(Inf NaN);&quot;</tt> and then use them as literals.) </p>
<p> Note that on input (string to number) Perl accepts <tt>&quot;Inf&quot;</tt> and <tt>&quot;NaN&quot;</tt> in many forms. Case is ignored, and the Win32-specific forms like <tt>&quot;1.#INF&quot;</tt> are understood, but on output the values are normalized to <tt>&quot;Inf&quot;</tt> and <tt>&quot;NaN&quot;</tt>. </p>
<p> <i>Version Strings</i> </p>
<p> A literal of the form <tt>&quot;v1.20.300.4000&quot;</tt> is parsed as a string composed of characters with the specified ordinals. This form, known as v-strings, provides an alternative, more readable way to construct strings, rather than use the somewhat less readable interpolation form <tt>&quot;

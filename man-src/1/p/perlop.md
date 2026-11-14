---
title: "perlop(1)"
name: "perlop"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlop/"
---

<h2 class="name">NAME</h2>
 

 perlop - Perl operators and precedence 

<h2>DESCRIPTION</h2>

 In Perl, the operator determines what operation is performed, independent of the type of the operands. For example <tt>&quot;$x + $y&quot;</tt> is always a numeric addition, and if <tt>$x</tt> or <tt>$y</tt> do not contain numbers, an attempt is made to convert them to numbers first. 

 This is in contrast to many other dynamic languages, where the operation is determined by the type of the first argument. It also means that Perl has two versions of some operators, one for numeric and one for string comparison. For example <tt>&quot;$x == $y&quot;</tt> compares two numbers for equality, and <tt>&quot;$x eq $y&quot;</tt> compares two strings. 

 There are a few exceptions though: <tt>&quot;x&quot;</tt> can be either string repetition or list repetition, depending on the type of the left operand, and <tt>&quot;&amp;&quot;</tt>, <tt>&quot;|&quot;</tt>, <tt>&quot;^&quot;</tt> and <tt>&quot;~&quot;</tt> can be either string or numeric bit operations.

<h3>Operator Precedence and Associativity</h3>

 Operator precedence and associativity work in Perl more or less like they do in mathematics. 

 <i>Operator precedence</i> means some operators group more tightly than others. For example, in <tt>&quot;2 + 4 * 5&quot;</tt>, the multiplication has higher precedence, so <tt>&quot;4 * 5&quot;</tt> is grouped together as the right-hand operand of the addition, rather than <tt>&quot;2 + 4&quot;</tt> being grouped together as the left-hand operand of the multiplication. It is as if the expression were written <tt>&quot;2 + (4 * 5)&quot;</tt>, not <tt>&quot;(2 + 4) * 5&quot;</tt>. So the expression yields <tt>&quot;2 + 20 == 22&quot;</tt>, rather than <tt>&quot;6 * 5 == 30&quot;</tt>. 

 <i>Operator associativity</i> defines what happens if a sequence of the same operators is used one after another: whether they will be grouped at the left or the right. For example, in <tt>&quot;9 - 3 - 2&quot;</tt>, subtraction is left associative, so <tt>&quot;9 - 3&quot;</tt> is grouped together as the left-hand operand of the second subtraction, rather than <tt>&quot;3 - 2&quot;</tt> being grouped together as the right-hand operand of the first subtraction. It is as if the expression were written <tt>&quot;(9 - 3) - 2&quot;</tt>, not <tt>&quot;9 - (3 - 2)&quot;</tt>. So the expression yields <tt>&quot;6 - 2 == 4&quot;</tt>, rather than <tt>&quot;9 - 1 == 8&quot;</tt>. 

 For simple operators that evaluate all their operands and then combine the values in some way, precedence and associativity (and parentheses) imply some ordering requirements on those combining operations. For example, in <tt>&quot;2 + 4 * 5&quot;</tt>, the grouping implied by precedence means that the multiplication of 4 and 5 must be performed before the addition of 2 and 20, simply because the result of that multiplication is required as one of the operands of the addition. But the order of operations is not fully determined by this: in <tt>&quot;2 * 2 + 4 * 5&quot;</tt> both multiplications must be performed before the addition, but the grouping does not say anything about the order in which the two multiplications are performed. In fact Perl has a general rule that the operands of an operator are evaluated in left-to-right order. A few operators such as <tt>&quot;&amp;&amp;=&quot;</tt> have special evaluation rules that can result in an operand not being evaluated at all; in general, the top-level operator in an expression has control of operand evaluation. 

 Perl operators have the following associativity and precedence, listed from highest precedence to lowest. Operators borrowed from C keep the same precedence relationship with each other, even where C's precedence is slightly screwy. (This makes learning Perl easier for C folks.) With very few exceptions, these all operate on scalar values only, not array values. 

 <pre><code>
left terms and list operators(leftward)
        left-&gt;nonassoc++ --right **right !~ \ and unary
    + and-left = ~!~left * / % x left + -.left &lt;&lt; &gt;&gt;
                                     nonassoc named unary operators
                                     nonassoc&lt;&gt; &lt;= &gt;=
                                     lt gt le ge
                                     nonassoc
                                 == != &lt;=&gt; eq ne cmp ~~left &amp;left
                             | ^left &amp;&amp;left
                         || //
                         nonassoc..... right
                     ?: right = += -= *= etc.goto last next redo dump
                                         left,
      = &gt;
        nonassoc list operators(rightward)
right not left and
        left or
    xor
</code></pre> 

 In the following sections, these operators are covered in detail, in the same order in which they appear in the table above. 

 Many operators can be overloaded for objects. See overload.

<h3>Terms and List Operators (Leftward)</h3>

 A <font SIZE="-1">TERM</font> has the highest precedence in Perl. They include variables, quote and quote-like operators, any expression in parentheses, and any function whose arguments are parenthesized. Actually, there aren't really functions in this sense, just list operators and unary operators behaving as functions because you put parentheses around the arguments. These are all documented in perlfunc. 

 If any list operator (<tt>&quot;print()&quot;</tt>, etc.) or any unary operator (<tt>&quot;chdir()&quot;</tt>, etc.) is followed by a left parenthesis as the next token, the operator and arguments within parentheses are taken to be of highest precedence, just like a normal function call. 

 In the absence of parentheses, the precedence of list operators such as <tt>&quot;print&quot;</tt>, <tt>&quot;sort&quot;</tt>, or <tt>&quot;chmod&quot;</tt> is either very high or very low depending on whether you are looking at the left side or the right side of the operator. For example, in 

 <pre>
    @ary = (1, 3, sort 4, 2);
    print @ary;         # prints 1324
</pre> 

 the commas on the right of the <tt>&quot;sort&quot;</tt> are evaluated before the <tt>&quot;sort&quot;</tt>, but the commas on the left are evaluated after. In other words, list operators tend to gobble up all arguments that follow, and then act like a simple <font SIZE="-1">TERM</font> with regard to the preceding expression. Be careful with parentheses: 

 
#These evaluate exit before doing the print:
print($foo, exit);
#Obviously not what you want.print $foo, exit;
#Nor is this.
#These do the print before evaluating exit:
    (print $foo),
    exit;
#This is what you want.print($foo), exit;
#Or this.print($foo), exit;
#Or even this.
 

 Also note that 

 <pre>
    print ($foo &amp; 255) + 1, &quot;\n&quot;;
</pre> 

 probably doesn't do what you expect at first glance. The parentheses enclose the argument list for <tt>&quot;print&quot;</tt> which is evaluated (printing the result of <tt>&quot;$foo &amp; 255&quot;</tt>). Then one is added to the return value of <tt>&quot;print&quot;</tt> (usually 1). The result is something like this: 

 <pre>
    1 + 1, &quot;\n&quot;;    # Obviously not what you meant.
</pre> 

 To do what you meant properly, you must write: 

 <pre>
    print(($foo &amp; 255) + 1, &quot;\n&quot;);
</pre> 

 See ``Named Unary Operators'' for more discussion of this. 

 Also parsed as terms are the <tt>&quot;do {}&quot;</tt> and <tt>&quot;eval {}&quot;</tt> constructs, as well as subroutine and method calls, and the anonymous constructors <tt>&quot;[]&quot;</tt> and <tt>&quot;{}&quot;</tt>. 

 See also ``Quote and Quote-like Operators'' toward the end of this section, as well as ``I/O Operators''.

<h3>The Arrow Operator</h3>

 &quot;<tt>&quot;-&gt;&quot;</tt>&quot; is an infix dereference operator, just as it is in C and C<font SIZE="-2">++</font>. If the right side is either a <tt>&quot;[...]&quot;</tt>, <tt>&quot;{...}&quot;</tt>, or a <tt>&quot;(...)&quot;</tt> subscript, then the left side must be either a hard or symbolic reference to an array, a hash, or a subroutine respectively. (Or technically speaking, a location capable of holding a hard reference, if it's an array or hash reference being used for assignment.) See perlreftut and perlref. 

 Otherwise, the right side is a method name or a simple scalar variable containing either the method name or a subroutine reference, and the left side must be either an object (a blessed reference) or a class name (that is, a package name). See perlobj. 

 The dereferencing cases (as opposed to method-calling cases) are somewhat extended by the <tt>&quot;postderef&quot;</tt> feature. For the details of that feature, consult ``Postfix Dereference Syntax'' in perlref.

<h3>Auto-increment and Auto-decrement</h3>

 <tt>&quot;++&quot;</tt> and <tt>&quot;--&quot;</tt> work as in C. That is, if placed before a variable, they increment or decrement the variable by one before returning the value, and if placed after, increment or decrement after returning the value. 

 
$i = 0;
$j = 0;
print $i++;
#prints 0 print++ $j;
#prints 1
 

 Note that just as in C, Perl doesn't define <b>when</b> the variable is incremented or decremented. You just know it will be done sometime before or after the value is returned. This also means that modifying a variable twice in the same statement will lead to undefined behavior. Avoid statements like: 

 
$i = $i++;
print++ $i + $i++;
 

 Perl will not guarantee what the result of the above statements is. 

 The auto-increment operator has a little extra builtin magic to it. If you increment a variable that is numeric, or that has ever been used in a numeric context, you get a normal increment. If, however, the variable has been used in only string contexts since it was set, and has a value that is not the empty string and matches the pattern <tt>&quot;/^[a-zA-Z]*[0-9]*\z/&quot;</tt>, the increment is done as a string, preserving each character within its range, with carry: 

 
print++($foo = "99");
#prints "100" print++($foo = "a0");
#prints "a1" print++($foo = "Az");
#prints "Ba" print++($foo = "zz");
#prints "aaa"
 

 <tt>&quot;undef&quot;</tt> is always treated as numeric, and in particular is changed to <tt>0</tt> before incrementing (so that a post-increment of an undef value will return <tt>0</tt> rather than <tt>&quot;undef&quot;</tt>). 

 The auto-decrement operator is not magical.

<h3>Exponentiation</h3>

 Binary <tt>&quot;**&quot;</tt> is the exponentiation operator. It binds even more tightly than unary minus, so <tt>&quot;-2**4&quot;</tt> is <tt>&quot;-(2**4)&quot;</tt>, not <tt>&quot;(-2)**4&quot;</tt>. (This is implemented using C's <tt><a HREF="/docs/linux/man/3-pow/">pow</a>(3)</tt> function, which actually works on doubles internally.) 

 Note that certain exponentiation expressions are ill-defined: these include <tt>&quot;0**0&quot;</tt>, <tt>&quot;1**Inf&quot;</tt>, and <tt>&quot;Inf**0&quot;</tt>. Do not expect any particular results from these special cases, the results are platform-dependent.

<h3>Symbolic Unary Operators</h3>

 Unary <tt>&quot;!&quot;</tt> performs logical negation, that is, ``not''. See also <tt>&quot;not&quot;</tt> for a lower precedence version of this. 

 Unary <tt>&quot;-&quot;</tt> performs arithmetic negation if the operand is numeric, including any string that looks like a number. If the operand is an identifier, a string consisting of a minus sign concatenated with the identifier is returned. Otherwise, if the string starts with a plus or minus, a string starting with the opposite sign is returned. One effect of these rules is that <tt>&quot;-bareword&quot;</tt> is equivalent to the string <tt>&quot;-bareword&quot;</tt>. If, however, the string begins with a non-alphabetic character (excluding <tt>&quot;+&quot;</tt> or <tt>&quot;-&quot;</tt>), Perl will attempt to convert the string to a numeric, and the arithmetic negation is performed. If the string cannot be cleanly converted to a numeric, Perl will give the warning <b>Argument ``the string'' isn't numeric in negation (-) at ...</b>. 

 Unary <tt>&quot;~&quot;</tt> performs bitwise negation, that is, 1's complement. For example, <tt>&quot;0666 &amp; ~027&quot;</tt> is 0640. (See also ``Integer Arithmetic'' and ``Bitwise String Operators''.) Note that the width of the result is platform-dependent: <tt>&quot;~0&quot;</tt> is 32 bits wide on a 32-bit platform, but 64 bits wide on a 64-bit platform, so if you are expecting a certain bit width, remember to use the <tt>&quot;&amp;&quot;</tt> operator to mask off the excess bits. 

 Starting in Perl 5.28, it is a fatal error to try to complement a string containing a character with an ordinal value above 255. 

 If the ``bitwise'' feature is enabled via <tt>&quot;use feature 'bitwise'&quot;</tt> or <tt>&quot;use v5.28&quot;</tt>, then unary <tt>&quot;~&quot;</tt> always treats its argument as a number, and an alternate form of the operator, <tt>&quot;~.&quot;</tt>, always treats its argument as a string. So <tt>&quot;~0&quot;</tt> and <tt>&quot;~&quot;0&quot;&quot;</tt> will both give 2**32-1 on 32-bit platforms, whereas <tt>&quot;~.0&quot;</tt> and <tt>&quot;~.&quot;0&quot;&quot;</tt> will both yield <tt>&quot;\xff&quot;</tt>. Until Perl 5.28, this feature produced a warning in the <tt>&quot;experimental::bitwise&quot;</tt> category. 

 Unary <tt>&quot;+&quot;</tt> has no effect whatsoever, even on strings. It is useful syntactically for separating a function name from a parenthesized expression that would otherwise be interpreted as the complete list of function arguments. (See examples above under ``Terms and List Operators (Leftward)''.) 

 Unary <tt>&quot;\&quot;</tt> creates references. If its operand is a single sigilled thing, it creates a reference to that object. If its operand is a parenthesised list, then it creates references to the things mentioned in the list. Otherwise it puts its operand in list context, and creates a list of references to the scalars in the list provided by the operand. See perlreftut and perlref. Do not confuse this behavior with the behavior of backslash within a string, although both forms do convey the notion of protecting the next thing from interpolation.

<h3>Binding Operators</h3>

 Binary <tt>&quot;=~&quot;</tt> binds a scalar expression to a pattern match. Certain operations search or modify the string <tt>$_</tt> by default. This operator makes that kind of operation work on some other string. The right argument is a search pattern, substitution, or transliteration. The left argument is what is supposed to be searched, substituted, or transliterated instead of the default <tt>$_</tt>. When used in scalar context, the return value generally indicates the success of the operation. The exceptions are substitution (<tt>&quot;s///&quot;</tt>) and transliteration (<tt>&quot;y///&quot;</tt>) with the <tt>&quot;/r&quot;</tt> (non-destructive) option, which cause the <b>r</b>eturn value to be the result of the substitution. Behavior in list context depends on the particular operator. See ``Regexp Quote-Like Operators'' for details and perlretut for examples using these operators. 

 If the right argument is an expression rather than a search pattern, substitution, or transliteration, it is interpreted as a search pattern at run time. Note that this means that its contents will be interpolated twice, so 

 <pre>
    '\\' =~ q'\\';
</pre> 

 is not ok, as the regex engine will end up trying to compile the pattern <tt>&quot;\&quot;</tt>, which it will consider a syntax error. 

 Binary <tt>&quot;!~&quot;</tt> is just like <tt>&quot;=~&quot;</tt> except the return value is negated in the logical sense. 

 Binary <tt>&quot;!~&quot;</tt> with a non-destructive substitution (<tt>&quot;s///r&quot;</tt>) or transliteration (<tt>&quot;y///r&quot;</tt>) is a syntax error.

<h3>Multiplicative Operators</h3>

 Binary <tt>&quot;*&quot;</tt> multiplies two numbers. 

 Binary <tt>&quot;/&quot;</tt> divides two numbers. 

 Binary <tt>&quot;%&quot;</tt> is the modulo operator, which computes the division remainder of its first argument with respect to its second argument. Given integer operands <tt>$m</tt> and <tt>$n</tt>: If <tt>$n</tt> is positive, then <tt>&quot;$m % $n&quot;</tt> is <tt>$m</tt> minus the largest multiple of <tt>$n</tt> less than or equal to <tt>$m</tt>. If <tt>$n</tt> is negative, then <tt>&quot;$m % $n&quot;</tt> is <tt>$m</tt> minus the smallest multiple of <tt>$n</tt> that is not less than <tt>$m</tt> (that is, the result will be less than or equal to zero). If the operands <tt>$m</tt> and <tt>$n</tt> are floating point values and the absolute value of <tt>$n</tt> (that is <tt>&quot;abs($n)&quot;</tt>) is less than <tt>&quot;(UV_MAX + 1)&quot;</tt>, only the integer portion of <tt>$m</tt> and <tt>$n</tt> will be used in the operation (Note: here <tt>&quot;UV_MAX&quot;</tt> means the maximum of the unsigned integer type). If the absolute value of the right operand (<tt>&quot;abs($n)&quot;</tt>) is greater than or equal to <tt>&quot;(UV_MAX + 1)&quot;</tt>, <tt>&quot;%&quot;</tt> computes the floating-point remainder <tt>$r</tt> in the equation <tt>&quot;($r = $m - $i*$n)&quot;</tt> where <tt>$i</tt> is a certain integer that makes <tt>$r</tt> have the same sign as the right operand <tt>$n</tt> (<b>not</b> as the left operand <tt>$m</tt> like C function <tt>&quot;fmod()&quot;</tt>) and the absolute value less than that of <tt>$n</tt>. Note that when <tt>&quot;use integer&quot;</tt> is in scope, <tt>&quot;%&quot;</tt> gives you direct access to the modulo operator as implemented by your C compiler. This operator is not as well defined for negative operands, but it will execute faster. 

 Binary <tt>&quot;x&quot;</tt> is the repetition operator. In scalar context, or if the left operand is neither enclosed in parentheses nor a <tt>&quot;qw//&quot;</tt> list, it performs a string repetition. In that case it supplies scalar context to the left operand, and returns a string consisting of the left operand string repeated the number of times specified by the right operand. If the <tt>&quot;x&quot;</tt> is in list context, and the left operand is either enclosed in parentheses or a <tt>&quot;qw//&quot;</tt> list, it performs a list repetition. In that case it supplies list context to the left operand, and returns a list consisting of the left operand list repeated the number of times specified by the right operand. If the right operand is zero or negative (raising a warning on negative), it returns an empty string or an empty list, depending on the context. 

 
print '-' x 80;
#print row of dashes
    print "\t" x($tab / 8),
    ' ' x($tab % 8);
#tab over
    @ones = (1)x 80;
#a list of 80 1's
    @ones = (5)x @ones;
#set all elements to 5


<h3>Additive Operators</h3>

 Binary <tt>&quot;+&quot;</tt> returns the sum of two numbers. 

 Binary <tt>&quot;-&quot;</tt> returns the difference of two numbers. 

 Binary <tt>&quot;.&quot;</tt> concatenates two strings.

<h3>Shift Operators</h3>

 Binary <tt>&quot;&lt;&lt;&quot;</tt> returns the value of its left argument shifted left by the number of bits specified by the right argument. Arguments should be integers. (See also ``Integer Arithmetic''.) 

 Binary <tt>&quot;&gt;&gt;&quot;</tt> returns the value of its left argument shifted right by the number of bits specified by the right argument. Arguments should be integers. (See also ``Integer Arithmetic''.) 

 If <tt>&quot;use integer&quot;</tt> (see ``Integer Arithmetic'') is in force then signed C integers are used (<i>arithmetic shift</i>), otherwise unsigned C integers are used (<i>logical shift</i>), even for negative shiftees. In arithmetic right shift the sign bit is replicated on the left, in logical shift zero bits come in from the left. 

 Either way, the implementation isn't going to generate results larger than the size of the integer type Perl was built with (32 bits or 64 bits). 

 Shifting by negative number of bits means the reverse shift: left shift becomes right shift, right shift becomes left shift. This is unlike in C, where negative shift is undefined. 

 Shifting by more bits than the size of the integers means most of the time zero (all bits fall off), except that under <tt>&quot;use integer&quot;</tt> right overshifting a negative shiftee results in -1. This is unlike in C, where shifting by too many bits is undefined. A common C behavior is ``shift by modulo wordbits'', so that for example 

 <pre>
    1 &gt;&gt; 64 == 1 &gt;&gt; (64 % 64) == 1 &gt;&gt; 0 == 1  # Common C behavior.
</pre> 

 but that is completely accidental. 

 If you get tired of being subject to your platform's native integers, the <tt>&quot;use bigint&quot;</tt> pragma neatly sidesteps the issue altogether: 

 
print 20 &lt;&lt; 20;
# 20971520 print 20 &lt;&lt; 40;
# 5120 on 32 - bit machines,
# 21990232555520 on 64 - bit machines
    use bigint;
print 20 &lt;&lt; 100;
# 25353012004564588029934064107520


<h3>Named Unary Operators</h3>

 The various named unary operators are treated as functions with one argument, with optional parentheses. 

 If any list operator (<tt>&quot;print()&quot;</tt>, etc.) or any unary operator (<tt>&quot;chdir()&quot;</tt>, etc.) is followed by a left parenthesis as the next token, the operator and arguments within parentheses are taken to be of highest precedence, just like a normal function call. For example, because named unary operators are higher precedence than <tt>&quot;||&quot;</tt>: 

 
chdir $foo || die;
#(chdir $foo) || die chdir($foo) || die;
#(chdir $foo) || die chdir($foo) || die;
#(chdir $foo) || die chdir +($foo) || die;
#(chdir $foo) || die
 

 but, because <tt>&quot;*&quot;</tt> is higher precedence than named operators: 

 
chdir $foo * 20;
#chdir($foo * 20)
        chdir($foo) *
    20;
#(chdir $foo) * 20 chdir($foo) * 20;
#(chdir $foo) * 20 chdir +($foo) * 20;
#chdir($foo * 20)
        rand 10 *
    20;
#rand(10 * 20)
        rand(10) *
    20;
#(rand 10) * 20 rand(10) * 20;
#(rand 10) * 20 rand +(10) * 20;
#rand(10 * 20)
 

 Regarding precedence, the filetest operators, like <tt>&quot;-f&quot;</tt>, <tt>&quot;-M&quot;</tt>, etc. are treated like named unary operators, but they don't follow this functional parenthesis rule. That means, for example, that <tt>&quot;-f($file).&quot;.bak&quot;&quot;</tt> is equivalent to <tt>&quot;-f &quot;$file.bak&quot;&quot;</tt>. 

 See also ``Terms and List Operators (Leftward)''.

<h3>Relational Operators</h3>

 Perl operators that return true or false generally return values that can be safely used as numbers. For example, the relational operators in this section and the equality operators in the next one return <tt>1</tt> for true and a special version of the defined empty string, <tt>&quot;&quot;</tt>, which counts as a zero but is exempt from warnings about improper numeric conversions, just as <tt>&quot;0 but true&quot;</tt> is. 

 Binary <tt>&quot;&lt;&quot;</tt> returns true if the left argument is numerically less than the right argument. 

 Binary <tt>&quot;&gt;&quot;</tt> returns true if the left argument is numerically greater than the right argument. 

 Binary <tt>&quot;&lt;=&quot;</tt> returns true if the left argument is numerically less than or equal to the right argument. 

 Binary <tt>&quot;&gt;=&quot;</tt> returns true if the left argument is numerically greater than or equal to the right argument. 

 Binary <tt>&quot;lt&quot;</tt> returns true if the left argument is stringwise less than the right argument. 

 Binary <tt>&quot;gt&quot;</tt> returns true if the left argument is stringwise greater than the right argument. 

 Binary <tt>&quot;le&quot;</tt> returns true if the left argument is stringwise less than or equal to the right argument. 

 Binary <tt>&quot;ge&quot;</tt> returns true if the left argument is stringwise greater than or equal to the right argument.

<h3>Equality Operators</h3>

 Binary <tt>&quot;==&quot;</tt> returns true if the left argument is numerically equal to the right argument. 

 Binary <tt>&quot;!=&quot;</tt> returns true if the left argument is numerically not equal to the right argument. 

 Binary <tt>&quot;&lt;=&gt;&quot;</tt> returns -1, 0, or 1 depending on whether the left argument is numerically less than, equal to, or greater than the right argument. If your platform supports <tt>&quot;NaN&quot;</tt>'s (not-a-numbers) as numeric values, using them with <tt>&quot;&lt;=&gt;&quot;</tt> returns undef. <tt>&quot;NaN&quot;</tt> is not <tt>&quot;&lt;&quot;</tt>, <tt>&quot;==&quot;</tt>, <tt>&quot;&gt;&quot;</tt>, <tt>&quot;&lt;=&quot;</tt> or <tt>&quot;&gt;=&quot;</tt> anything (even <tt>&quot;NaN&quot;</tt>), so those 5 return false. <tt>&quot;NaN != NaN&quot;</tt> returns true, as does <tt>&quot;NaN !=&quot;</tt> <i>anything else</i>. If your platform doesn't support <tt>&quot;NaN&quot;</tt>'s then <tt>&quot;NaN&quot;</tt> is just a string with numeric value 0. 

 
$ perl - le '$x = "NaN"; print "No NaN support here" if $x == $x' $ perl - le '$x = "NaN"; print "NaN support here" if $x != $x'
 

 (Note that the bigint, bigrat, and bignum pragmas all support <tt>&quot;NaN&quot;</tt>.) 

 Binary <tt>&quot;eq&quot;</tt> returns true if the left argument is stringwise equal to the right argument. 

 Binary <tt>&quot;ne&quot;</tt> returns true if the left argument is stringwise not equal to the right argument. 

 Binary <tt>&quot;cmp&quot;</tt> returns -1, 0, or 1 depending on whether the left argument is stringwise less than, equal to, or greater than the right argument. 

 Binary <tt>&quot;~~&quot;</tt> does a smartmatch between its arguments. Smart matching is described in the next section. 

 <tt>&quot;lt&quot;</tt>, <tt>&quot;le&quot;</tt>, <tt>&quot;ge&quot;</tt>, <tt>&quot;gt&quot;</tt> and <tt>&quot;cmp&quot;</tt> use the collation (sort) order specified by the current <tt>&quot;LC_COLLATE&quot;</tt> locale if a <tt>&quot;use locale&quot;</tt> form that includes collation is in effect. See perllocale. Do not mix these with Unicode, only use them with legacy 8-bit locale encodings. The standard <tt>&quot;Unicode::Collate&quot;</tt> and <tt>&quot;Unicode::Collate::Locale&quot;</tt> modules offer much more powerful solutions to collation issues. 

 For case-insensitive comparisons, look at the ``fc'' in perlfunc case-folding function, available in Perl v5.16 or later: 

 <pre>
    if ( fc($x) eq fc($y) ) { ... }
</pre>

<h3>Smartmatch Operator</h3>

 First available in Perl 5.10.1 (the 5.10.0 version behaved differently), binary <tt>&quot;~~&quot;</tt> does a ``smartmatch'' between its arguments. This is mostly used implicitly in the <tt>&quot;when&quot;</tt> construct described in perlsyn, although not all <tt>&quot;when&quot;</tt> clauses call the smartmatch operator. Unique among all of Perl's operators, the smartmatch operator can recurse. The smartmatch operator is experimental and its behavior is subject to change. 

 It is also unique in that all other Perl operators impose a context (usually string or numeric context) on their operands, autoconverting those operands to those imposed contexts. In contrast, smartmatch <i>infers</i> contexts from the actual types of its operands and uses that type information to select a suitable comparison mechanism. 

 The <tt>&quot;~~&quot;</tt> operator compares its operands ``polymorphically'', determining how to compare them according to their actual types (numeric, string, array, hash, etc.). Like the equality operators with which it shares the same precedence, <tt>&quot;~~&quot;</tt> returns 1 for true and <tt>&quot;&quot;</tt> for false. It is often best read aloud as ``in'', ``inside of'', or ``is contained in'', because the left operand is often looked for <i>inside</i> the right operand. That makes the order of the operands to the smartmatch operand often opposite that of the regular match operator. In other words, the ``smaller'' thing is usually placed in the left operand and the larger one in the right. 

 The behavior of a smartmatch depends on what type of things its arguments are, as determined by the following table. The first row of the table whose types apply determines the smartmatch behavior. Because what actually happens is mostly determined by the type of the second operand, the table is sorted on the right operand instead of on the left. 

 
Left Right Description and pseudocode == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
                                                                                                                                       Any undef check whether Any is undefined
                                                                                                                                           like : !defined Any
                                                                                                                                                      Any Object invoke ~~overloading on Object,
                                                                                                                                or die
                                                                                                                                            Right operand is an ARRAY : Left Right Description and pseudocode == ==
                                                                                                                                                                        == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
                                                                                                                                =
                                                                                                                                    ARRAY1 ARRAY2 recurse on paired elements of ARRAY1 and ARRAY2[2] like : (ARRAY1[0] ~~ARRAY2[0]) &amp;&amp; (ARRAY1[1] ~~ARRAY2[1]) &amp;&amp; ...HASH ARRAY any ARRAY elements exist as HASH keys like : grep
{
    exists HASH-&gt;
    {
        $_
    }
}
ARRAY
Regexp ARRAY any ARRAY elements pattern match Regexp
        like : grep{ / Regexp / } ARRAY
                   undef ARRAY undef in ARRAY
                       like : grep{!defined} ARRAY
                                  Any ARRAY smartmatch each ARRAY element[3] like : grep{Any ~~$_} ARRAY
                                                                                        Right operand is a HASH : Left Right Description and pseudocode == ==
                                                                                                                  == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
    =
        HASH1 HASH2 all same keys in both HASHes
            like : keys HASH1 ==
                   grep
{
    exists HASH2-&gt;
    {
        $_
    }
}
keys HASH1
    ARRAY HASH any ARRAY elements exist as HASH keys
        like : grep
{
    exists HASH-&gt;
    {
        $_
    }
}
ARRAY
 Regexp    HASH       any HASH keys pattern match Regexp
                like: grep { /Regexp/ } keys HASH
 undef     HASH       always false (undef can't be a key)
                like: 0 == 1
 Any       HASH       HASH key existence
                like: exists HASH-&gt;{Any}
 Right operand is CODE:
 Left      Right      Description and pseudocode
 ===============================================================
 ARRAY     CODE       sub returns true on all ARRAY elements[1]
                like: !grep { !CODE-&gt;($_) } ARRAY
 HASH      CODE       sub returns true on all HASH keys[1]
                like: !grep { !CODE-&gt;($_) } keys HASH
 Any       CODE       sub passed Any returns true
                like: CODE-&gt;(Any)
 

 Right operand is a Regexp: 

 
Left Right Description and pseudocode == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
                                                                                                                                       ARRAY Regexp any ARRAY elements match Regexp
                                                                                                                                           like : grep{ / Regexp / } ARRAY
                                                                                                                                                      HASH Regexp any HASH keys match Regexp
                                                                                                                                                          like : grep{ / Regexp / } keys HASH
                                                                                                                                                                     Any Regexp pattern match
                                                                                                                                                                         like : Any = ~ / Regexp /
                                                                                                                                                                                          Other : Left Right Description and pseudocode ==
                                                                                                                                                                                      == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
                                                                                                                                                                                =
                                                                                                                                                                                    Object Any invoke ~~overloading on Object,
                                                                                                                                or fall back to... Any Num numeric equality
                                                                                                                                            like : Any == Num Num nummy[4] numeric equality like : Num == nummy undef Any check whether undefined like : !defined(Any) Any Any string equality like : Any eq Any
 

 Notes:
<dl>
<dt>1. Empty hashes or arrays match.
<dd>
<dt>2. That is, each element smartmatches the element of the same index in the other array.[3]
<dd>
<dt>3. If a circular reference is found, fall back to referential equality.
<dd>
<dt>4. Either an actual number, or a string that looks like one.
<dd></dl>
 

 The smartmatch implicitly dereferences any non-blessed hash or array reference, so the <tt>&quot;</tt>HASH<tt>&quot;</tt> and <tt>&quot;</tt>ARRAY<tt>&quot;</tt> entries apply in those cases. For blessed references, the <tt>&quot;</tt>Object<tt>&quot;</tt> entries apply. Smartmatches involving hashes only consider hash keys, never hash values. 

 The ``like'' code entry is not always an exact rendition. For example, the smartmatch operator short-circuits whenever possible, but <tt>&quot;grep&quot;</tt> does not. Also, <tt>&quot;grep&quot;</tt> in scalar context returns the number of matches, but <tt>&quot;~~&quot;</tt> returns only true or false. 

 Unlike most operators, the smartmatch operator knows to treat <tt>&quot;undef&quot;</tt> specially: 

 
use v5 .10.1;
@array = (1, 2, 3, undef, 4, 5);
say "some elements undefined" if undef ~~@array;
 

 Each operand is considered in a modified scalar context, the modification being that array and hash variables are passed by reference to the operator, which implicitly dereferences them. Both elements of each pair are the same: 

 
use v5 .10.1;
my % hash = (red = &gt; 1, blue = &gt; 2, green = &gt; 3,
             orange = &gt; 4, yellow = &gt; 5, purple = &gt; 6,
             black = &gt; 7, grey = &gt; 8, white = &gt; 9);
my @array = qw(red blue green);
say "some array elements in hash keys" if @array ~~ % hash;
say "some array elements in hash keys" if \@array ~~ \% hash;
say "red in array" if "red" ~~@array;
say "red in array" if "red" ~~ \@array;
say "some keys end in e" if / e$ / ~~ % hash;
say "some keys end in e" if / e$ / ~~ \% hash;
 

 Two arrays smartmatch if each element in the first array smartmatches (that is, is ``in'') the corresponding element in the second array, recursively. 

 
use v5 .10.1;
my @little = qw(red blue green);
my @bigger = ("red", "blue", [ "orange", "green" ]);
if (@little ~~@bigger) {
#true !say "little is contained in bigger";
}
 

 Because the smartmatch operator recurses on nested arrays, this will still report that ``red'' is in the array. 

 
use v5 .10.1;
my @array = qw(red blue green);
my $nested_array = [[[[[[[@array]]]]]]];
say "red in array" if "red" ~~$nested_array;
 

 If two arrays smartmatch each other, then they are deep copies of each others' values, as this example reports: 

 
use v5 .12.0;
my @a = (0, 1, 2, [ 3, [ 4, 5 ], 6 ], 7);
my @b = (0, 1, 2, [ 3, [ 4, 5 ], 6 ], 7);
if (@a ~~@b &amp;&amp; @b ~~@a) {
    say "a and b are deep copies of each other";
}
elsif(@a ~~@b)
{
    say "a smartmatches in b";
}
elsif(@b ~~@a)
{
    say "b smartmatches in a";
}
else
{
    say "a and b don't smartmatch each other at all";
}
 

 If you were to set <tt>&quot;$b[3] = 4&quot;</tt>, then instead of reporting that ``a and b are deep copies of each other'', it now reports that <tt>&quot;b smartmatches in a&quot;</tt>. That's because the corresponding position in <tt>@a</tt> contains an array that (eventually) has a 4 in it. 

 Smartmatching one hash against another reports whether both contain the same keys, no more and no less. This could be used to see whether two records have the same field names, without caring what values those fields might have. For example: 

 
use v5 .10.1;
sub make_dogtag
{
    state $REQUIRED_FIELDS = {name = &gt; 1, rank = &gt; 1, serial_num = &gt; 1};
    my($class, $init_fields) = @_;
    die "Must supply (only) name, rank, and serial number" unless $init_fields ~~$REQUIRED_FIELDS;
    ...
}
 

 However, this only does what you mean if <tt>$init_fields</tt> is indeed a hash reference. The condition <tt>&quot;$init_fields ~~ $REQUIRED_FIELDS&quot;</tt> also allows the strings <tt>&quot;name&quot;</tt>, <tt>&quot;rank&quot;</tt>, <tt>&quot;serial_num&quot;</tt> as well as any array reference that contains <tt>&quot;name&quot;</tt> or <tt>&quot;rank&quot;</tt> or <tt>&quot;serial_num&quot;</tt> anywhere to pass through. 

 The smartmatch operator is most often used as the implicit operator of a <tt>&quot;when&quot;</tt> clause. See the section on ``Switch Statements'' in perlsyn. 

 <i>Smartmatching of Objects</i> 

 To avoid relying on an object's underlying representation, if the smartmatch's right operand is an object that doesn't overload <tt>&quot;~~&quot;</tt>, it raises the exception &quot;<tt>&quot;Smartmatching a non-overloaded object breaks encapsulation&quot;</tt>``. That's because one has no business digging around to see whether something is ''in&quot; an object. These are all illegal on objects without a <tt>&quot;~~&quot;</tt> overload: 

 <pre>
    %hash ~~ $object
       42 ~~ $object
   &quot;fred&quot; ~~ $object
</pre> 

 However, you can change the way an object is smartmatched by overloading the <tt>&quot;~~&quot;</tt> operator. This is allowed to extend the usual smartmatch semantics. For objects that do have an <tt>&quot;~~&quot;</tt> overload, see overload. 

 Using an object as the left operand is allowed, although not very useful. Smartmatching rules take precedence over overloading, so even if the object in the left operand has smartmatch overloading, this will be ignored. A left operand that is a non-overloaded object falls back on a string or numeric comparison of whatever the <tt>&quot;ref&quot;</tt> operator returns. That means that 

 <pre>
    $object ~~ X
</pre> 

 does <i>not</i> invoke the overload method with <tt>&quot;</tt>X<tt>&quot;</tt> as an argument. Instead the above table is consulted as normal, and based on the type of <tt>&quot;</tt>X<tt>&quot;</tt>, overloading may or may not be invoked. For simple strings or numbers, ``in'' becomes equivalent to this: 

 <pre>
    $object ~~ $number          ref($object) == $number
    $object ~~ $string          ref($object) eq $string
</pre> 

 For example, this reports that the handle smells IOish (but please don't really do this!): 

 
use IO::Handle;
my $fh = IO::Handle-&gt;new ();
if ($fh ~~ /\bIO\b /) {
    say "handle smells IOish";
}
 

 That's because it treats <tt>$fh</tt> as a string like <tt>&quot;IO::Handle=GLOB(0x8039e0)&quot;</tt>, then pattern matches against that.

<h3>Bitwise And</h3>

 Binary <tt>&quot;&amp;&quot;</tt> returns its operands ANDed together bit by bit. Although no warning is currently raised, the result is not well defined when this operation is performed on operands that aren't either numbers (see ``Integer Arithmetic'') nor bitstrings (see ``Bitwise String Operators''). 

 Note that <tt>&quot;&amp;&quot;</tt> has lower priority than relational operators, so for example the parentheses are essential in a test like 

 <pre>
    print &quot;Even\n&quot; if ($x &amp; 1) == 0;
</pre> 

 If the ``bitwise'' feature is enabled via <tt>&quot;use feature 'bitwise'&quot;</tt> or <tt>&quot;use v5.28&quot;</tt>, then this operator always treats its operands as numbers. Before Perl 5.28 this feature produced a warning in the <tt>&quot;experimental::bitwise&quot;</tt> category.

<h3>Bitwise Or and Exclusive Or</h3>

 Binary <tt>&quot;|&quot;</tt> returns its operands ORed together bit by bit. 

 Binary <tt>&quot;^&quot;</tt> returns its operands XORed together bit by bit. 

 Although no warning is currently raised, the results are not well defined when these operations are performed on operands that aren't either numbers (see ``Integer Arithmetic'') nor bitstrings (see ``Bitwise String Operators''). 

 Note that <tt>&quot;|&quot;</tt> and <tt>&quot;^&quot;</tt> have lower priority than relational operators, so for example the parentheses are essential in a test like 

 <pre>
    print &quot;false\n&quot; if (8 | 2) != 10;
</pre> 

 If the ``bitwise'' feature is enabled via <tt>&quot;use feature 'bitwise'&quot;</tt> or <tt>&quot;use v5.28&quot;</tt>, then this operator always treats its operands as numbers. Before Perl 5.28. this feature produced a warning in the <tt>&quot;experimental::bitwise&quot;</tt> category.

<h3>C-style Logical And</h3>

 Binary <tt>&quot;&amp;&amp;&quot;</tt> performs a short-circuit logical <font SIZE="-1">AND</font> operation. That is, if the left operand is false, the right operand is not even evaluated. Scalar or list context propagates down to the right operand if it is evaluated.

<h3>C-style Logical Or</h3>

 Binary <tt>&quot;||&quot;</tt> performs a short-circuit logical <font SIZE="-1">OR</font> operation. That is, if the left operand is true, the right operand is not even evaluated. Scalar or list context propagates down to the right operand if it is evaluated.

<h3>Logical Defined-Or</h3>

 Although it has no direct equivalent in C, Perl's <tt>&quot;//&quot;</tt> operator is related to its C-style ``or''. In fact, it's exactly the same as <tt>&quot;||&quot;</tt>, except that it tests the left hand side's definedness instead of its truth. Thus, <tt>&quot;EXPR1 // EXPR2&quot;</tt> returns the value of <tt>&quot;EXPR1&quot;</tt> if it's defined, otherwise, the value of <tt>&quot;EXPR2&quot;</tt> is returned. (<tt>&quot;EXPR1&quot;</tt> is evaluated in scalar context, <tt>&quot;EXPR2&quot;</tt> in the context of <tt>&quot;//&quot;</tt> itself). Usually, this is the same result as <tt>&quot;defined(EXPR1) ? EXPR1 : EXPR2&quot;</tt> (except that the ternary-operator form can be used as a lvalue, while <tt>&quot;EXPR1 // EXPR2&quot;</tt> cannot). This is very useful for providing default values for variables. If you actually want to test if at least one of <tt>$x</tt> and <tt>$y</tt> is defined, use <tt>&quot;defined($x // $y)&quot;</tt>. 

 The <tt>&quot;||&quot;</tt>, <tt>&quot;//&quot;</tt> and <tt>&quot;&amp;&amp;&quot;</tt> operators return the last value evaluated (unlike C's <tt>&quot;||&quot;</tt> and <tt>&quot;&amp;&amp;&quot;</tt>, which return 0 or 1). Thus, a reasonably portable way to find out the home directory might be: 

 
$home = $ENV
{
    HOME
}
// $ENV{LOGDIR}
// (getpwuid($&lt;))[7]
// die "You're homeless!\n";
 

 In particular, this means that you shouldn't use this for selecting between two aggregates for assignment: 

 
@a = @b || @c;
#This doesn't do the right thing
    @a = scalar(@b) || @c;
#because it really means this.
    @a = @b
    ? @b : @c;
#This works fine, though.
 

 As alternatives to <tt>&quot;&amp;&amp;&quot;</tt> and <tt>&quot;||&quot;</tt> when used for control flow, Perl provides the <tt>&quot;and&quot;</tt> and <tt>&quot;or&quot;</tt> operators (see below). The short-circuit behavior is identical. The precedence of <tt>&quot;and&quot;</tt> and <tt>&quot;or&quot;</tt> is much lower, however, so that you can safely use them after a list operator without the need for parentheses: 

 <pre>
    unlink &quot;alpha&quot;, &quot;beta&quot;, &quot;gamma&quot;
            or gripe(), next LINE;
</pre> 

 With the C-style operators that would have been written like this: 

 <pre>
    unlink(&quot;alpha&quot;, &quot;beta&quot;, &quot;gamma&quot;)
            || (gripe(), next LINE);
</pre> 

 It would be even more readable to write that this way: 

 
unless(unlink("alpha", "beta", "gamma"))
{
    gripe();
    next LINE;
}
 

 Using <tt>&quot;or&quot;</tt> for assignment is unlikely to do what you want; see below.

<h3>Range Operators</h3>

 Binary <tt>&quot;..&quot;</tt> is the range operator, which is really two different operators depending on the context. In list context, it returns a list of values counting (up by ones) from the left value to the right value. If the left value is greater than the right value then it returns the empty list. The range operator is useful for writing <tt>&quot;foreach (1..10)&quot;</tt> loops and for doing slice operations on arrays. In the current implementation, no temporary array is created when the range operator is used as the expression in <tt>&quot;foreach&quot;</tt> loops, but older versions of Perl might burn a lot of memory when you write something like this: 

 <pre>
    for (1 .. 1_000_000) {
        # code
    }
</pre> 

 The range operator also works on strings, using the magical auto-increment, see below. 

 In scalar context, <tt>&quot;..&quot;</tt> returns a boolean value. The operator is bistable, like a flip-flop, and emulates the line-range (comma) operator of <b>sed</b>, <b>awk</b>, and various editors. Each <tt>&quot;..&quot;</tt> operator maintains its own boolean state, even across calls to a subroutine that contains it. It is false as long as its left operand is false. Once the left operand is true, the range operator stays true until the right operand is true, <i></i><font SIZE="-1"><i>AFTER</i></font><i></i> which the range operator becomes false again. It doesn't become false till the next time the range operator is evaluated. It can test the right operand and become false on the same evaluation it became true (as in <b>awk</b>), but it still returns true once. If you don't want it to test the right operand until the next evaluation, as in <b>sed</b>, just use three dots (<tt>&quot;...&quot;</tt>) instead of two. In all other regards, <tt>&quot;...&quot;</tt> behaves just like <tt>&quot;..&quot;</tt> does. 

 The right operand is not evaluated while the operator is in the ``false'' state, and the left operand is not evaluated while the operator is in the ``true'' state. The precedence is a little lower than || and &amp;&amp;. The value returned is either the empty string for false, or a sequence number (beginning with 1) for true. The sequence number is reset for each range encountered. The final sequence number in a range has the string <tt>&quot;E0&quot;</tt> appended to it, which doesn't affect its numeric value, but gives you something to search for if you want to exclude the endpoint. You can exclude the beginning point by waiting for the sequence number to be greater than 1. 

 If either operand of scalar <tt>&quot;..&quot;</tt> is a constant expression, that operand is considered true if it is equal (<tt>&quot;==&quot;</tt>) to the current input line number (the <tt>$.</tt> variable). 

 To be pedantic, the comparison is actually <tt>&quot;int(EXPR) == int(EXPR)&quot;</tt>, but that is only an issue if you use a floating point expression; when implicitly using <tt>$.</tt> as described in the previous paragraph, the comparison is <tt>&quot;int(EXPR) == int($.)&quot;</tt> which is only an issue when <tt>$.</tt> is set to a floating point value and you are not reading from a file. Furthermore, <tt>&quot;span&quot; .. &quot;spat&quot;</tt> or <tt>&quot;2.18 .. 3.14&quot;</tt> will not do what you want in scalar context because each of the operands are evaluated using their integer representation. 

 Examples: 

 As a scalar operator: 

 
if (101..200) {
    print;
}
#print 2nd hundred lines, short for
#if ($.== 101..$.== 200){print;}
    next LINE if (1../ ^$ /);
#skip header lines, short for
#next LINE if ($.== 1../ ^$ /);
#(typically in a loop labeled LINE)
                        s /
                        ^ / &gt; / if (/ ^$ /..eof());
#quote body
#parse mail messages
    while (&lt;&gt;)
{
    $in_header = 1../ ^$ / ;
    $in_body = / ^$ /..eof;
    if ($in_header) {
#do something
    } else {
#in body
#do something else
    }
}
continue
{
    close ARGV if eof;
#reset $.each file
}
 

 Here's a simple example to illustrate the difference between the two range operators: 

 
@lines = ("   - Foo",
          "01 - Bar",
          "1  - Baz",
          "   - Quux");
foreach (@lines) {
    if (/ 0 /../ 1 /) {
        print "$_\n";
    }
}
 

 This program will print only the line containing ``Bar''. If the range operator is changed to <tt>&quot;...&quot;</tt>, it will also print the ``Baz'' line. 

 And now some examples as a list operator: 

 
for (101..200) {
    print
}
#print $_ 100 times
    @foo = @foo[0..$ #foo];
#an expensive no - op
    @foo = @foo[$ #foo - 4..$ #foo];
#slice last 5 items
 

 The range operator (in list context) makes use of the magical auto-increment algorithm if the operands are strings. You can say 

 <pre>
    @alphabet = (&quot;A&quot; .. &quot;Z&quot;);
</pre> 

 to get all normal letters of the English alphabet, or 

 <pre>
    $hexdigit = (0 .. 9, &quot;a&quot; .. &quot;f&quot;)[$num &amp; 15];
</pre> 

 to get a hexadecimal digit, or 

 
@z2 = ("01".."31");
print $z2[$mday];
 

 to get dates with leading zeros. 

 If the final value specified is not in the sequence that the magical increment would produce, the sequence goes until the next value would be longer than the final value specified. 

 As of Perl 5.26, the list-context range operator on strings works as expected in the scope of <tt>&quot;use feature 'unicode_strings&quot;</tt>. In previous versions, and outside the scope of that feature, it exhibits ``The ''Unicode Bug&quot;&quot; in perlunicode: its behavior depends on the internal encoding of the range endpoint. 

 If the initial value specified isn't part of a magical increment sequence (that is, a non-empty string matching <tt>&quot;/^[a-zA-Z]*[0-9]*\z/&quot;</tt>), only the initial value will be returned. So the following will only return an alpha: 

 <pre>
    use charnames &quot;greek&quot;;
    my @greek_small =  (&quot;\N{alpha}&quot; .. &quot;\N{omega}&quot;);
</pre> 

 To get the 25 traditional lowercase Greek letters, including both sigmas, you could use this instead: 

 
use charnames "greek";
my @greek_small = map{chr}(ord("\N{alpha}")
                               ..ord("\N{omega}"));
 

 However, because there are <i>many</i> other lowercase Greek characters than just those, to match lowercase Greek characters in a regular expression, you could use the pattern <tt>&quot;/(?:(?=\p{Greek})\p{Lower})+/&quot;</tt> (or the experimental feature <tt>&quot;/(?[ \p{Greek} &amp; \p{Lower} ])+/&quot;</tt>). 

 Because each operand is evaluated in integer form, <tt>&quot;2.18 .. 3.14&quot;</tt> will return two elements in list context. 

 <pre>
    @list = (2.18 .. 3.14); # same as @list = (2 .. 3);
</pre>

<h3>Conditional Operator</h3>

 Ternary <tt>&quot;?:&quot;</tt> is the conditional operator, just as in C. It works much like an if-then-else. If the argument before the <tt>&quot;?&quot;</tt> is true, the argument before the <tt>&quot;:&quot;</tt> is returned, otherwise the argument after the <tt>&quot;:&quot;</tt> is returned. For example: 

 <pre>
    printf &quot;I have %d dog%s.\n&quot;, $n,
            ($n == 1) ? &quot;&quot; : &quot;s&quot;;
</pre> 

 Scalar or list context propagates downward into the 2nd or 3rd argument, whichever is selected. 

 <pre>
    $x = $ok ? $y : $z;  # get a scalar
    @x = $ok ? @y : @z;  # get an array
    $x = $ok ? @y : @z;  # oops, that's just a count!
</pre> 

 The operator may be assigned to if both the 2nd and 3rd arguments are legal lvalues (meaning that you can assign to them): 

 <pre>
    ($x_or_y ? $x : $y) = $z;
</pre> 

 Because this operator produces an assignable result, using assignments without parentheses will get you in trouble. For example, this: 

 <pre>
    $x % 2 ? $x += 10 : $x += 2
</pre> 

 Really means this: 

 <pre>
    (($x % 2) ? ($x += 10) : $x) += 2
</pre> 

 Rather than this: 

 <pre>
    ($x % 2) ? ($x += 10) : ($x += 2)
</pre> 

 That should probably be written more simply as: 

 <pre>
    $x += ($x % 2) ? 10 : 2;
</pre>

<h3>Assignment Operators</h3>

 <tt>&quot;=&quot;</tt> is the ordinary assignment operator. 

 Assignment operators work as in C. That is, 

 <pre>
    $x += 2;
</pre> 

 is equivalent to 

 <pre>
    $x = $x + 2;
</pre> 

 although without duplicating any side effects that dereferencing the lvalue might trigger, such as from <tt>&quot;tie()&quot;</tt>. Other assignment operators work similarly. The following are recognized: 

 
* *= += *= &amp;= &amp;.= &lt;&lt;= &amp;&amp; =
    -= /= |= |.= &gt;&gt;= || =
                            .= %= ^= ^.= //=
    x =
 

 Although these are grouped by family, they all have the precedence of assignment. These combined assignment operators can only operate on scalars, whereas the ordinary assignment operator can assign to arrays, hashes, lists and even references. (See ``Context'' and ``List value constructors'' in perldata, and ``Assigning to References'' in perlref.) 

 Unlike in C, the scalar assignment operator produces a valid lvalue. Modifying an assignment is equivalent to doing the assignment and then modifying the variable that was assigned to. This is useful for modifying a copy of something, like this: 

 <pre>
    ($tmp = $global) =~ tr/13579/24680/;
</pre> 

 Although as of 5.14, that can be also be accomplished this way: 

 <pre>
    use v5.14;
    $tmp = ($global =~  tr/13579/24680/r);
</pre> 

 Likewise, 

 <pre>
    ($x += 2) *= 3;
</pre> 

 is equivalent to 

 
$x += 2;
$x *= 3;
 

 Similarly, a list assignment in list context produces the list of lvalues assigned to, and a list assignment in scalar context returns the number of elements produced by the expression on the right hand side of the assignment. 

 The three dotted bitwise assignment operators (<tt>&quot;&amp;.=&quot;</tt> <tt>&quot;|.=&quot;</tt> <tt>&quot;^.=&quot;</tt>) are new in Perl 5.22. See ``Bitwise String Operators''.

<h3>Comma Operator</h3>

 Binary <tt>&quot;,&quot;</tt> is the comma operator. In scalar context it evaluates its left argument, throws that value away, then evaluates its right argument and returns that value. This is just like C's comma operator. 

 In list context, it's just the list argument separator, and inserts both its arguments into the list. These arguments are also evaluated from left to right. 

 The <tt>&quot;=&gt;&quot;</tt> operator (sometimes pronounced ``fat comma'') is a synonym for the comma except that it causes a word on its left to be interpreted as a string if it begins with a letter or underscore and is composed only of letters, digits and underscores. This includes operands that might otherwise be interpreted as operators, constants, single number v-strings or function calls. If in doubt about this behavior, the left operand can be quoted explicitly. 

 Otherwise, the <tt>&quot;=&gt;&quot;</tt> operator behaves exactly as the comma operator or list argument separator, according to context. 

 For example: 

 <pre>
    use constant FOO =&gt; &quot;something&quot;;
    my %h = ( FOO =&gt; 23 );
</pre> 

 is equivalent to: 

 <pre>
    my %h = (&quot;FOO&quot;, 23);
</pre> 

 It is <i></i><font SIZE="-1"><i>NOT</i></font><i></i>: 

 <pre>
    my %h = (&quot;something&quot;, 23);
</pre> 

 The <tt>&quot;=&gt;&quot;</tt> operator is helpful in documenting the correspondence between keys and values in hashes, and other paired elements in lists. 

 
% hash = ($key = &gt; $value);
login($username = &gt; $password);
 

 The special quoting behavior ignores precedence, and hence may apply to <i>part</i> of the left operand: 

 <pre>
    print time.shift =&gt; &quot;bbb&quot;;
</pre> 

 That example prints something like <tt>&quot;1314363215shiftbbb&quot;</tt>, because the <tt>&quot;=&gt;&quot;</tt> implicitly quotes the <tt>&quot;shift&quot;</tt> immediately on its left, ignoring the fact that <tt>&quot;time.shift&quot;</tt> is the entire left operand.

<h3>List Operators (Rightward)</h3>

 On the right side of a list operator, the comma has very low precedence, such that it controls all comma-separated expressions found there. The only operators with lower precedence are the logical operators <tt>&quot;and&quot;</tt>, <tt>&quot;or&quot;</tt>, and <tt>&quot;not&quot;</tt>, which may be used to evaluate calls to list operators without the need for parentheses: 

 <pre>
    open HANDLE, &quot;&lt; :encoding(UTF-8)&quot;, &quot;filename&quot;
        or die &quot;Can't open: $!\n&quot;;
</pre> 

 However, some people find that code harder to read than writing it with parentheses: 

 <pre>
    open(HANDLE, &quot;&lt; :encoding(UTF-8)&quot;, &quot;filename&quot;)
        or die &quot;Can't open: $!\n&quot;;
</pre> 

 in which case you might as well just use the more customary <tt>&quot;||&quot;</tt> operator: 

 <pre>
    open(HANDLE, &quot;&lt; :encoding(UTF-8)&quot;, &quot;filename&quot;)
        || die &quot;Can't open: $!\n&quot;;
</pre> 

 See also discussion of list operators in ``Terms and List Operators (Leftward)''.

<h3>Logical Not</h3>

 Unary <tt>&quot;not&quot;</tt> returns the logical negation of the expression to its right. It's the equivalent of <tt>&quot;!&quot;</tt> except for the very low precedence.

<h3>Logical And</h3>

 Binary <tt>&quot;and&quot;</tt> returns the logical conjunction of the two surrounding expressions. It's equivalent to <tt>&quot;&amp;&amp;&quot;</tt> except for the very low precedence. This means that it short-circuits: the right expression is evaluated only if the left expression is true.

<h3>Logical or and Exclusive Or</h3>

 Binary <tt>&quot;or&quot;</tt> returns the logical disjunction of the two surrounding expressions. It's equivalent to <tt>&quot;||&quot;</tt> except for the very low precedence. This makes it useful for control flow: 

 <pre>
    print FH $data              or die &quot;Can't write to FH: $!&quot;;
</pre> 

 This means that it short-circuits: the right expression is evaluated only if the left expression is false. Due to its precedence, you must be careful to avoid using it as replacement for the <tt>&quot;||&quot;</tt> operator. It usually works out better for flow control than in assignments: 

 
$x = $y or $z;
#bug : this is wrong($x = $y) or $z;
#really means this $x = $y || $z;
#better written this way
 

 However, when it's a list-context assignment and you're trying to use <tt>&quot;||&quot;</tt> for control flow, you probably need <tt>&quot;or&quot;</tt> so that the assignment takes higher precedence. 

 
@info = stat($file) || die;
#oops, scalar sense of stat !@info = stat($file) or die;
#better, now @info gets its due
 

 Then again, you could always use parentheses. 

 Binary <tt>&quot;xor&quot;</tt> returns the exclusive-OR of the two surrounding expressions. It cannot short-circuit (of course). 

 There is no low precedence operator for defined-OR.

<h3>C Operators Missing From Perl</h3>

 Here is what C has that Perl doesn't:
<dl>
<dt>unary &amp;
<dd> Address-of operator. (But see the <tt>&quot;\&quot;</tt> operator for taking a reference.)
<dt>unary *
<dd> Dereference-address operator. (Perl's prefix dereferencing operators are typed: <tt>&quot;$&quot;</tt>, <tt>&quot;@&quot;</tt>, <tt>&quot;%&quot;</tt>, and <tt>&quot;&amp;&quot;</tt>.)
<dt>(<font SIZE="-1">TYPE</font>)
<dd> Type-casting operator.</dl>

<h3>Quote and Quote-like Operators</h3>

 While we usually think of quotes as literal values, in Perl they function as operators, providing various kinds of interpolating and pattern matching capabilities. Perl provides customary quote characters for these behaviors, but also provides a way for you to choose your quote character for any of them. In the following table, a <tt>&quot;{}&quot;</tt> represents any pair of delimiters you choose. 

 
Customary Generic Meaning Interpolates
        '' q
{
}
Literal no
    "" qq
{
}
Literal yes
        `` qx
{
}
Command yes *
    qw
{
}
Word list no
    //       m{}       Pattern match          yes*
    qr
{
}
Pattern yes *
    s{}
{
}
Substitution yes *
    tr{}
{
}
Transliteration no(but see below)
    y{}
{
}
Transliteration no(but see below)
    &lt;&lt; EOF here - doc yes *
                      *unless the delimiter is ''.
 

 Non-bracketing delimiters use the same character fore and aft, but the four sorts of <font SIZE="-1">ASCII</font> brackets (round, angle, square, curly) all nest, which means that 

 
q
{
    foo{bar} baz
}
 

 is the same as 

 <pre>
    'foo{bar}baz'
</pre> 

 Note, however, that this does not always work for quoting Perl code: 

 
$s = q
{
    if ($x eq "}")
        ...
};
#WRONG
 

 is a syntax error. The <tt>&quot;Text::Balanced&quot;</tt> module (standard as of v5.8, and from <font SIZE="-1">CPAN</font> before then) is able to do this properly. 

 There can (and in some cases, must) be whitespace between the operator and the quoting characters, except when <tt>&quot;#&quot;</tt> is being used as the quoting character. <tt>&quot;q#foo#&quot;</tt> is parsed as the string <tt>&quot;foo&quot;</tt>, while <tt>&quot;q #foo#&quot;</tt> is the operator <tt>&quot;q&quot;</tt> followed by a comment. Its argument will be taken from the next line. This allows you to write: 

 
s{foo} #Replace foo
{
    bar
}
#with bar.
 

 The cases where whitespace must be used are when the quoting character is a word character (meaning it matches <tt>&quot;/\w/&quot;</tt>): 

 <pre>
    q XfooX # Works: means the string 'foo'
    qXfooX  # WRONG!
</pre> 

 The following escape sequences are available in constructs that interpolate, and in transliterations whose delimiters aren't single quotes (<tt>&quot;'&quot;</tt>). 

 
    Sequence     Note  Description
    \t                  tab               (HT, TAB)
    \n                  newline           (NL)
    \r                  return            (CR)
    \f                  form feed         (FF)
    \b                  backspace         (BS)
    \a                  alarm (bell)      (BEL)
    \e                  escape            (ESC)
    \x{263A}     [1,8]  hex char          (example: SMILEY)
    \x1b         [2,8]  restricted range hex char (example: ESC)
    \N{name}     [3]    named Unicode character or character sequence
    \N{U+263D}   [4,8]  Unicode character (example: FIRST QUARTER MOON)
    \c[          [5]    control char      (example: chr(27))
    \o{23072}    [6,8]  octal char        (example: SMILEY)
    \033         [7,8]  restricted range octal char  (example: ESC)

<dl>
<dt>[1]
<dd> The result is the character specified by the hexadecimal number between the braces. See ``[8]'' below for details on which character. 

 Only hexadecimal digits are valid between the braces. If an invalid character is encountered, a warning will be issued and the invalid character and all subsequent characters (valid or invalid) within the braces will be discarded. 

 If there are no valid digits between the braces, the generated character is the <font SIZE="-1">NULL</font> character (<tt>&quot;\x{00}&quot;</tt>). However, an explicit empty brace (<tt>&quot;\x{}&quot;</tt>) will not cause a warning (currently).
<dt>[2]
<dd> The result is the character specified by the hexadecimal number in the range 0x00 to 0xFF. See ``[8]'' below for details on which character. 

 Only hexadecimal digits are valid following <tt>&quot;\x&quot;</tt>. When <tt>&quot;\x&quot;</tt> is followed by fewer than two valid digits, any valid digits will be zero-padded. This means that <tt>&quot;\x7&quot;</tt> will be interpreted as <tt>&quot;\x07&quot;</tt>, and a lone <tt>&quot;\x&quot;</tt> will be interpreted as <tt>&quot;\x00&quot;</tt>. Except at the end of a string, having fewer than two valid digits will result in a warning. Note that although the warning says the illegal character is ignored, it is only ignored as part of the escape and will still be used as the subsequent character in the string. For example: 

 <pre>
  Original    Result    Warns?
  &quot;\x7&quot;       &quot;\x07&quot;    no
  &quot;\x&quot;        &quot;\x00&quot;    no
  &quot;\x7q&quot;      &quot;\x07q&quot;   yes
  &quot;\xq&quot;       &quot;\x00q&quot;   yes
</pre>
<dt>[3]
<dd> The result is the Unicode character or character sequence given by <i>name</i>. See charnames.
<dt>[4]
<dd> <tt>&quot;\N{U+</tt>hexadecimal number<tt>}&quot;</tt> means the Unicode character whose Unicode code point is <i>hexadecimal number</i>.
<dt>[5]
<dd> The character following <tt>&quot;\c&quot;</tt> is mapped to some other character as shown in the table: 

 
Sequence Value
   \c @chr(0)
   \cA chr(1)
   \ca chr(1)
   \cB chr(2)
   \cb chr(2)...
   \cZ chr(26)
   \cz chr(26)
   \c[chr(27)
#See below for chr(28)
   \c] chr(29)
   \c ^ chr(30)
   \c_ chr(31)
   \c ? chr(127) #(on ASCII platforms; see below for link to
#EBCDIC discussion)
 

 In other words, it's the character whose code point has had 64 xor'd with its uppercase. <tt>&quot;\c?&quot;</tt> is <font SIZE="-1">DELETE</font> on <font SIZE="-1">ASCII</font> platforms because <tt>&quot;ord(&quot;?&quot;) ^ 64&quot;</tt> is 127, and <tt>&quot;\c@&quot;</tt> is <font SIZE="-1">NULL</font> because the ord of <tt>&quot;@&quot;</tt> is 64, so xor'ing 64 itself produces 0. 

 Also, <tt>&quot;\c\</tt>X<tt>&quot;</tt> yields <tt>&quot; chr(28) . &quot;</tt>X<tt>&quot;&quot;</tt> for any <i>X</i>, but cannot come at the end of a string, because the backslash would be parsed as escaping the end quote. 

 On <font SIZE="-1">ASCII</font> platforms, the resulting characters from the list above are the complete set of <font SIZE="-1">ASCII</font> controls. This isn't the case on <font SIZE="-1">EBCDIC</font> platforms; see ``<font SIZE="-1">OPERATOR DIFFERENCES''</font> in perlebcdic for a full discussion of the differences between these for <font SIZE="-1">ASCII</font> versus <font SIZE="-1">EBCDIC</font> platforms. 

 Use of any other character following the <tt>&quot;c&quot;</tt> besides those listed above is discouraged, and as of Perl v5.20, the only characters actually allowed are the printable <font SIZE="-1">ASCII</font> ones, minus the left brace <tt>&quot;{&quot;</tt>. What happens for any of the allowed other characters is that the value is derived by xor'ing with the seventh bit, which is 64, and a warning raised if enabled. Using the non-allowed characters generates a fatal error. 

 To get platform independent controls, you can use <tt>&quot;\N{...}&quot;</tt>.
<dt>[6]
<dd> The result is the character specified by the octal number between the braces. See ``[8]'' below for details on which character. 

 If a character that isn't an octal digit is encountered, a warning is raised, and the value is based on the octal digits before it, discarding it and all following characters up to the closing brace. It is a fatal error if there are no octal digits at all.
<dt>[7]
<dd> The result is the character specified by the three-digit octal number in the range 000 to 777 (but best to not use above 077, see next paragraph). See ``[8]'' below for details on which character. 

 Some contexts allow 2 or even 1 digit, but any usage without exactly three digits, the first being a zero, may give unintended results. (For example, in a regular expression it may be confused with a backreference; see ``Octal escapes'' in perlrebackslash.) Starting in Perl 5.14, you may use <tt>&quot;\o{}&quot;</tt> instead, which avoids all these problems. Otherwise, it is best to use this construct only for ordinals <tt>&quot;\077&quot;</tt> and below, remembering to pad to the left with zeros to make three digits. For larger ordinals, either use <tt>&quot;\o{}&quot;</tt>, or convert to something else, such as to hex and use <tt>&quot;\N{U+}&quot;</tt> (which is portable between platforms with different character sets) or <tt>&quot;\x{}&quot;</tt> instead.
<dt>[8]
<dd> Several constructs above specify a character by a number. That number gives the character's position in the character set encoding (indexed from 0). This is called synonymously its ordinal, code position, or code point. Perl works on platforms that have a native encoding currently of either ASCII/Latin1 or <font SIZE="-1">EBCDIC,</font> each of which allow specification of 256 characters. In general, if the number is 255 (0xFF, 0377) or below, Perl interprets this in the platform's native encoding. If the number is 256 (0x100, 0400) or above, Perl interprets it as a Unicode code point and the result is the corresponding Unicode character. For example <tt>&quot;\x{50}&quot;</tt> and <tt>&quot;\o{120}&quot;</tt> both are the number 80 in decimal, which is less than 256, so the number is interpreted in the native character set encoding. In <font SIZE="-1">ASCII</font> the character in the 80th position (indexed from 0) is the letter <tt>&quot;P&quot;</tt>, and in <font SIZE="-1">EBCDIC</font> it is the ampersand symbol <tt>&quot;&amp;&quot;</tt>. <tt>&quot;\x{100}&quot;</tt> and <tt>&quot;\o{400}&quot;</tt> are both 256 in decimal, so the number is interpreted as a Unicode code point no matter what the native encoding is. The name of the character in the 256th position (indexed by 0) in Unicode is <tt>&quot;LATIN CAPITAL LETTER A WITH MACRON&quot;</tt>. 

 An exception to the above rule is that <tt>&quot;\N{U+</tt>hex number<tt>}&quot;</tt> is always interpreted as a Unicode code point, so that <tt>&quot;\N{U+0050}&quot;</tt> is <tt>&quot;P&quot;</tt> even on <font SIZE="-1">EBCDIC</font> platforms.</dl>
 

 <font SIZE="-1"><b>NOTE</b></font>: Unlike C and other languages, Perl has no <tt>&quot;\v&quot;</tt> escape sequence for the vertical tab (<font SIZE="-1">VT,</font> which is 11 in both <font SIZE="-1">ASCII</font> and <font SIZE="-1">EBCDIC</font>), but you may use <tt>&quot;\N{VT}&quot;</tt>, <tt>&quot;\ck&quot;</tt>, <tt>&quot;\N{U+0b}&quot;</tt>, or <tt>&quot;\x0b&quot;</tt>. (<tt>&quot;\v&quot;</tt> does have meaning in regular expression patterns in Perl, see perlre.) 

 The following escape sequences are available in constructs that interpolate, but not in transliterations. 

 <pre>
    \l          lowercase next character only
    \u          titlecase (not uppercase!) next character only
    \L          lowercase all characters till \E or end of string
    \U          uppercase all characters till \E or end of string
    \F          foldcase all characters till \E or end of string
    \Q          quote (disable) pattern metacharacters till \E or
                end of string
    \E          end either case modification or quoted section
                (whichever was last seen)
</pre> 

 See ``quotemeta'' in perlfunc for the exact definition of characters that are quoted by <tt>&quot;\Q&quot;</tt>. 

 <tt>&quot;\L&quot;</tt>, <tt>&quot;\U&quot;</tt>, <tt>&quot;\F&quot;</tt>, and <tt>&quot;\Q&quot;</tt> can stack, in which case you need one <tt>&quot;\E&quot;</tt> for each. For example: 

 <pre>
 say&quot;This \Qquoting \ubusiness \Uhere isn't quite\E done yet,\E is it?&quot;;
 This quoting\ Business\ HERE\ ISN\'T\ QUITE\ done\ yet\, is it?
</pre> 

 If a <tt>&quot;use locale&quot;</tt> form that includes <tt>&quot;LC_CTYPE&quot;</tt> is in effect (see perllocale), the case map used by <tt>&quot;\l&quot;</tt>, <tt>&quot;\L&quot;</tt>, <tt>&quot;\u&quot;</tt>, and <tt>&quot;\U&quot;</tt> is taken from the current locale. If Unicode (for example, <tt>&quot;\N{}&quot;</tt> or code points of 0x100 or beyond) is being used, the case map used by <tt>&quot;\l&quot;</tt>, <tt>&quot;\L&quot;</tt>, <tt>&quot;\u&quot;</tt>, and <tt>&quot;\U&quot;</tt> is as defined by Unicode. That means that case-mapping a single character can sometimes produce a sequence of several characters. Under <tt>&quot;use locale&quot;</tt>, <tt>&quot;\F&quot;</tt> produces the same results as <tt>&quot;\L&quot;</tt> for all locales but a <font SIZE="-1">UTF-8</font> one, where it instead uses the Unicode definition. 

 All systems use the virtual <tt>&quot;\n&quot;</tt> to represent a line terminator, called a ``newline''. There is no such thing as an unvarying, physical newline character. It is only an illusion that the operating system, device drivers, C libraries, and Perl all conspire to preserve. Not all systems read <tt>&quot;\r&quot;</tt> as <font SIZE="-1">ASCII CR</font> and <tt>&quot;\n&quot;</tt> as <font SIZE="-1">ASCII LF.</font> For example, on the ancient Macs (pre-MacOS X) of yesteryear, these used to be reversed, and on systems without a line terminator, printing <tt>&quot;\n&quot;</tt> might emit no actual data. In general, use <tt>&quot;\n&quot;</tt> when you mean a ``newline'' for your system, but use the literal <font SIZE="-1">ASCII</font> when you need an exact character. For example, most networking protocols expect and prefer a <font SIZE="-1">CR+LF</font> (<tt>&quot;\015\012&quot;</tt> or <tt>&quot;\cM\cJ&quot;</tt>) for line terminators, and although they often accept just <tt>&quot;\012&quot;</tt>, they seldom tolerate just <tt>&quot;\015&quot;</tt>. If you get in the habit of using <tt>&quot;\n&quot;</tt> for networking, you may be burned some day. 

 For constructs that do interpolate, variables beginning with &quot;<tt>&quot;$&quot;</tt>`` or ''<tt>&quot;@&quot;</tt>&quot; are interpolated. Subscripted variables such as <tt>$a[3]</tt> or <tt>&quot;$href-&gt;{key}[0]&quot;</tt> are also interpolated, as are array and hash slices. But method calls such as <tt>&quot;$obj-&gt;meth&quot;</tt> are not. 

 Interpolating an array or slice interpolates the elements in order, separated by the value of <tt>$&quot;</tt>, so is equivalent to interpolating <tt>&quot;join $&quot;, @array&quot;</tt>. ``Punctuation'' arrays such as <tt>&quot;@*&quot;</tt> are usually interpolated only if the name is enclosed in braces <tt>&quot;@{*}&quot;</tt>, but the arrays <tt>@_</tt>, <tt>&quot;@+&quot;</tt>, and <tt>&quot;@-&quot;</tt> are interpolated even without braces. 

 For double-quoted strings, the quoting from <tt>&quot;\Q&quot;</tt> is applied after interpolation and escapes are processed. 

 <pre>
    &quot;abc\Qfoo\tbar$s\Exyz&quot;
</pre> 

 is equivalent to 

 <pre>
    &quot;abc&quot; . quotemeta(&quot;foo\tbar$s&quot;) . &quot;xyz&quot;
</pre> 

 For the pattern of regex operators (<tt>&quot;qr//&quot;</tt>, <tt>&quot;m//&quot;</tt> and <tt>&quot;s///&quot;</tt>), the quoting from <tt>&quot;\Q&quot;</tt> is applied after interpolation is processed, but before escapes are processed. This allows the pattern to match literally (except for <tt>&quot;$&quot;</tt> and <tt>&quot;@&quot;</tt>). For example, the following matches: 

 <pre>
    '\s\t' =~ /\Q\s\t/
</pre> 

 Because <tt>&quot;$&quot;</tt> or <tt>&quot;@&quot;</tt> trigger interpolation, you'll need to use something like <tt>&quot;/\Quser\E\@\Qhost/&quot;</tt> to match them literally. 

 Patterns are subject to an additional level of interpretation as a regular expression. This is done as a second pass, after variables are interpolated, so that regular expressions may be incorporated into the pattern from the variables. If this is not what you want, use <tt>&quot;\Q&quot;</tt> to interpolate a variable literally. 

 Apart from the behavior described above, Perl does not expand multiple levels of interpolation. In particular, contrary to the expectations of shell programmers, back-quotes do <i></i><font SIZE="-1"><i>NOT</i></font><i></i> interpolate within double quotes, nor do single quotes impede evaluation of variables when used within double quotes.

<h3>Regexp Quote-Like Operators</h3>

 Here are the quote-like operators that apply to pattern matching and related activities.
<dl>
<dt>&quot;qr/<i>STRING</i>/msixpodualn&quot;
<dd> This operator quotes (and possibly compiles) its <i></i><font SIZE="-1"><i>STRING</i></font><i></i> as a regular expression. <i></i><font SIZE="-1"><i>STRING</i></font><i></i> is interpolated the same way as <i></i><font SIZE="-1"><i>PATTERN</i></font><i></i> in <tt>&quot;m/</tt>PATTERN<tt>/&quot;</tt>. If <tt>&quot;'&quot;</tt> is used as the delimiter, no variable interpolation is done. Returns a Perl value which may be used instead of the corresponding <tt>&quot;/</tt>STRING<tt>/msixpodualn&quot;</tt> expression. The returned value is a normalized version of the original pattern. It magically differs from a string containing the same characters: <tt>&quot;ref(qr/x/)&quot;</tt> returns ``Regexp''; however, dereferencing it is not well defined (you currently get the normalized version of the original pattern, but this may change). 

 For example, 

 <pre>
    $rex = qr/my.STRING/is;
    print $rex;                 # prints (?si-xm:my.STRING)
    s/$rex/foo/;
</pre> 

 is equivalent to 

 <pre>
    s/my.STRING/foo/is;
</pre> 

 The result may be used as a subpattern in a match: 

 
$re = qr / $pattern / ;
$string = ~ / foo${re} bar / ;
#can be interpolated in other
#patterns
    $string = ~$re;
# or used standalone
         $string = ~ / $re /
    ;
# or this way
 

 Since Perl may compile the pattern at the moment of execution of the <tt>&quot;qr()&quot;</tt> operator, using <tt>&quot;qr()&quot;</tt> may have speed advantages in some situations, notably if the result of <tt>&quot;qr()&quot;</tt> is used standalone: 

 
sub match
{
    my $patterns = shift;
    my @compiled = map qr / $_ / i, @$patterns;
    grep
    {
        my $success = 0;
        foreach
            my $pat(@compiled)
            {
                $success = 1, last if / $pat / ;
            }
        $success;
    }
    @_;
}
 

 Precompilation of the pattern into an internal representation at the moment of <tt>&quot;qr()&quot;</tt> avoids the need to recompile the pattern every time a match <tt>&quot;/$pat/&quot;</tt> is attempted. (Perl has many other internal optimizations, but none would be triggered in the above example if we did not use <tt>&quot;qr()&quot;</tt> operator.) 

 Options (specified by the following modifiers) are: 

 
m Treat string as multiple lines.s Treat string as single line.(Make.match a newline)
    i Do case -insensitive pattern matching.x Use extended regular expressions; specifying two
        x's means \t and the SPACE character are ignored within
        square-bracketed character classes
    p   When matching preserve a copy of the matched string so
        that ${^PREMATCH}, ${^MATCH}, ${^POSTMATCH} will be
        defined (ignored starting in v5.20) as these are always
        defined starting in that release
    o   Compile pattern only once.
    a   ASCII-restrict: Use ASCII for \d, \s, \w and [[:posix:]]
        character classes;
specifying two a's adds the further restriction that no ASCII character will match a
            non -
        ASCII one under / i.l Use the current run - time locale's rules. u Use Unicode rules.d Use Unicode or
    native charset,
    as in 5.12 and earlier.n Non - capture mode.Don't let () fill in $1, $2, etc...
 

 If a precompiled pattern is embedded in a larger pattern then the effect of <tt>&quot;msixpluadn&quot;</tt> will be propagated appropriately. The effect that the <tt>&quot;/o&quot;</tt> modifier has is not propagated, being restricted to those patterns explicitly using it. 

 The <tt>&quot;/a&quot;</tt>, <tt>&quot;/d&quot;</tt>, <tt>&quot;/l&quot;</tt>, and <tt>&quot;/u&quot;</tt> modifiers (added in Perl 5.14) control the character set rules, but <tt>&quot;/a&quot;</tt> is the only one you are likely to want to specify explicitly; the other three are selected automatically by various pragmas. 

 See perlre for additional information on valid syntax for <i></i><font SIZE="-1"><i>STRING</i></font><i></i>, and for a detailed look at the semantics of regular expressions. In particular, all modifiers except the largely obsolete <tt>&quot;/o&quot;</tt> are further explained in ``Modifiers'' in perlre. <tt>&quot;/o&quot;</tt> is described in the next section.
<dt>&quot;m/<i>PATTERN</i>/msixpodualngc&quot;
<dd>
<dt>&quot;/<i>PATTERN</i>/msixpodualngc&quot;
<dd> Searches a string for a pattern match, and in scalar context returns true if it succeeds, false if it fails. If no string is specified via the <tt>&quot;=~&quot;</tt> or <tt>&quot;!~&quot;</tt> operator, the <tt>$_</tt> string is searched. (The string specified with <tt>&quot;=~&quot;</tt> need not be an lvalue---it may be the result of an expression evaluation, but remember the <tt>&quot;=~&quot;</tt> binds rather tightly.) See also perlre. 

 Options are as described in <tt>&quot;qr//&quot;</tt> above; in addition, the following match process modifiers are available: 

 <pre>
 g  Match globally, i.e., find all occurrences.
 c  Do not reset search position on a failed match when /g is
    in effect.
</pre> 

 If <tt>&quot;/&quot;</tt> is the delimiter then the initial <tt>&quot;m&quot;</tt> is optional. With the <tt>&quot;m&quot;</tt> you can use any pair of non-whitespace (<font SIZE="-1">ASCII</font>) characters as delimiters. This is particularly useful for matching path names that contain <tt>&quot;/&quot;</tt>, to avoid <font SIZE="-1">LTS</font> (leaning toothpick syndrome). If <tt>&quot;?&quot;</tt> is the delimiter, then a match-only-once rule applies, described in <tt>&quot;m?</tt>PATTERN<tt>?&quot;</tt> below. If <tt>&quot;'&quot;</tt> (single quote) is the delimiter, no variable interpolation is performed on the <i></i><font SIZE="-1"><i>PATTERN</i></font><i></i>. When using a delimiter character valid in an identifier, whitespace is required after the <tt>&quot;m&quot;</tt>. 

 <i></i><font SIZE="-1"><i>PATTERN</i></font><i></i> may contain variables, which will be interpolated every time the pattern search is evaluated, except for when the delimiter is a single quote. (Note that <tt>$(</tt>, <tt>$)</tt>, and <tt>$|</tt> are not interpolated because they look like end-of-string tests.) Perl will not recompile the pattern unless an interpolated variable that it contains changes. You can force Perl to skip the test and never recompile by adding a <tt>&quot;/o&quot;</tt> (which stands for ``once'') after the trailing delimiter. Once upon a time, Perl would recompile regular expressions unnecessarily, and this modifier was useful to tell it not to do so, in the interests of speed. But now, the only reasons to use <tt>&quot;/o&quot;</tt> are one of:
<dl>
<dt>
<dd>
<dl>
<dt>1.
<dd> The variables are thousands of characters long and you know that they don't change, and you need to wring out the last little bit of speed by having Perl skip testing for that. (There is a maintenance penalty for doing this, as mentioning <tt>&quot;/o&quot;</tt> constitutes a promise that you won't change the variables in the pattern. If you do change them, Perl won't even notice.)
<dt>2.
<dd> you want the pattern to use the initial values of the variables regardless of whether they change or not. (But there are saner ways of accomplishing this than using <tt>&quot;/o&quot;</tt>.)
<dt>3.
<dd> If the pattern contains embedded code, such as 

 <pre>
    use re 'eval';
    $code = 'foo(?{ $x })';
    /$code/
</pre> 

 then perl will recompile each time, even though the pattern string hasn't changed, to ensure that the current value of <tt>$x</tt> is seen each time. Use <tt>&quot;/o&quot;</tt> if you want to avoid this.</dl>
</dl>

<dl>
<dt>
<dd> 

 The bottom line is that using <tt>&quot;/o&quot;</tt> is almost never a good idea.</dl>

<dt>The empty pattern &quot;//&quot;
<dd> If the <i></i><font SIZE="-1"><i>PATTERN</i></font><i></i> evaluates to the empty string, the last <i>successfully</i> matched regular expression is used instead. In this case, only the <tt>&quot;g&quot;</tt> and <tt>&quot;c&quot;</tt> flags on the empty pattern are honored; the other flags are taken from the original pattern. If no match has previously succeeded, this will (silently) act instead as a genuine empty pattern (which will always match). 

 Note that it's possible to confuse Perl into thinking <tt>&quot;//&quot;</tt> (the empty regex) is really <tt>&quot;//&quot;</tt> (the defined-or operator). Perl is usually pretty good about this, but some pathological cases might trigger this, such as <tt>&quot;$x///&quot;</tt> (is that <tt>&quot;($x) / (//)&quot;</tt> or <tt>&quot;$x // /&quot;</tt>?) and <tt>&quot;print $fh //&quot;</tt> (<tt>&quot;print $fh(//&quot;</tt> or <tt>&quot;print($fh //&quot;</tt>?). In all of these examples, Perl will assume you meant defined-or. If you meant the empty regex, just use parentheses or spaces to disambiguate, or even prefix the empty regex with an <tt>&quot;m&quot;</tt> (so <tt>&quot;//&quot;</tt> becomes <tt>&quot;m//&quot;</tt>).
<dt>Matching in list context
<dd> If the <tt>&quot;/g&quot;</tt> option is not used, <tt>&quot;m//&quot;</tt> in list context returns a list consisting of the subexpressions matched by the parentheses in the pattern, that is, (<tt>$1</tt>, <tt>$2</tt>, <tt>$3</tt>...) (Note that here <tt>$1</tt> etc. are also set). When there are no parentheses in the pattern, the return value is the list <tt>&quot;(1)&quot;</tt> for success. With or without parentheses, an empty list is returned upon failure. 

 Examples: 

 
open(TTY, "+&lt;/dev/tty") || die "can't access /dev/tty: $!";
&lt;TTY&gt; = ~ / ^y / i &amp;&amp;foo();
#do foo if desired if (/ Version
                       : *([0 - 9.] *) /)
{
    $version = $1;
}
next if m # ^ / usr / spool / uucp #;
#poor man's grep
$arg = shift;
while (&lt;&gt;) {
    print if / $arg / o;
#compile only once(no longer needed !)
}
if (($F1, $F2, $Etc) = ($foo = ~ / ^(\S +)\s + (\S +)\s *(.*) /))
 

 This last example splits <tt>$foo</tt> into the first two words and the remainder of the line, and assigns those three fields to <tt>$F1</tt>, <tt>$F2</tt>, and <tt>$Etc</tt>. The conditional is true if any variables were assigned; that is, if the pattern matched. 

 The <tt>&quot;/g&quot;</tt> modifier specifies global pattern matching---that is, matching as many times as possible within the string. How it behaves depends on the context. In list context, it returns a list of the substrings matched by any capturing parentheses in the regular expression. If there are no parentheses, it returns a list of all the matched strings, as if there were parentheses around the whole pattern. 

 In scalar context, each execution of <tt>&quot;m//g&quot;</tt> finds the next match, returning true if it matches, and false if there is no further match. The position after the last match can be read or set using the <tt>&quot;pos()&quot;</tt> function; see ``pos'' in perlfunc. A failed match normally resets the search position to the beginning of the string, but you can avoid that by adding the <tt>&quot;/c&quot;</tt> modifier (for example, <tt>&quot;m//gc&quot;</tt>). Modifying the target string also resets the search position.
<dt>&quot;\G <i>assertion</i>&quot;
<dd> You can intermix <tt>&quot;m//g&quot;</tt> matches with <tt>&quot;m/\G.../g&quot;</tt>, where <tt>&quot;\G&quot;</tt> is a zero-width assertion that matches the exact position where the previous <tt>&quot;m//g&quot;</tt>, if any, left off. Without the <tt>&quot;/g&quot;</tt> modifier, the <tt>&quot;\G&quot;</tt> assertion still anchors at <tt>&quot;pos()&quot;</tt> as it was at the start of the operation (see ``pos'' in perlfunc), but the match is of course only attempted once. Using <tt>&quot;\G&quot;</tt> without <tt>&quot;/g&quot;</tt> on a target string that has not previously had a <tt>&quot;/g&quot;</tt> match applied to it is the same as using the <tt>&quot;\A&quot;</tt> assertion to match the beginning of the string. Note also that, currently, <tt>&quot;\G&quot;</tt> is only properly supported when anchored at the very beginning of the pattern. 

 Examples: 

 
#list context
($one, $five, $fifteen) = (`uptime` = ~ / (\d +\.\d +) / g);
#scalar context
local $ / = "";
while ($paragraph = &lt;&gt;) {
        while ($paragraph =~ /\p{Ll}['")]*[.!?]+['")]*\s/g) {
            $sentences++;
}
}
say $sentences;
 

 Here's another way to check for sentences in a paragraph: 

 
 my $sentence_rx = qr{
    (?: (?&lt;= ^ ) | (?&lt;= \s ) )  # after start-of-string or
#whitespace
    \p{Lu}                      # capital letter
    .*?                         # a bunch of anything
    (?&lt;= \S )                   # that ends in non-
#whitespace
    (?&lt;! \b [DMS]r  )           # but isn't a common abbr.
    (?&lt;! \b Mrs )
    (?&lt;! \b Sra )
    (?&lt;! \b St  )
    [.?!]                       # followed by a sentence
#ender
    (?= $ | \s )                # in front of end-of-string
# or whitespace
 }sx;
 local $ / = "";
 while (my $paragraph = &lt;&gt;) {
     say "NEW PARAGRAPH";
     my $count = 0;
     while ($paragraph = ~ / ($sentence_rx) / g) {
         printf "\tgot sentence %d: &lt;%s&gt;\n", ++$count, $1;
     }
 }
 

 Here's how to use <tt>&quot;m//gc&quot;</tt> with <tt>&quot;\G&quot;</tt>: 

 
$_ = "ppooqppqq";
while ($i++ &lt; 2) {
    print "1: '";
    print $1 while / (o) / gc;
    print "', pos=", pos, "\n";
    print "2: '";
    print $1 if /\G(q) / gc;
    print "', pos=", pos, "\n";
    print "3: '";
    print $1 while / (p) / gc;
    print "', pos=", pos, "\n";
}
print "Final: '$1', pos=", pos, "\n" if /\G(.) / ;
 

 The last example should print: 

 <pre>
    1: 'oo', pos=4
    2: 'q', pos=5
    3: 'pp', pos=7
    1: '', pos=7
    2: 'q', pos=8
    3: '', pos=8
    Final: 'q', pos=8
</pre> 

 Notice that the final match matched <tt>&quot;q&quot;</tt> instead of <tt>&quot;p&quot;</tt>, which a match without the <tt>&quot;\G&quot;</tt> anchor would have done. Also note that the final match did not update <tt>&quot;pos&quot;</tt>. <tt>&quot;pos&quot;</tt> is only updated on a <tt>&quot;/g&quot;</tt> match. If the final match did indeed match <tt>&quot;p&quot;</tt>, it's a good bet that you're running an ancient (pre-5.6.0) version of Perl. 

 A useful idiom for <tt>&quot;lex&quot;</tt>-like scanners is <tt>&quot;/\G.../gc&quot;</tt>. You can combine several regexps like this to process a string part-by-part, doing different actions depending on which regexp matched. Each regexp tries to match where the previous one leaves off. 

 
$_ = &lt;&lt; 'EOL';
$url = URI::URL-&gt;new ("http://example.com/");
die if $url eq "xXx";
EOL
    LOOP:
{
    print(" digits"), redo LOOP if /\G\d +\b[, .;]        ?\s        */ gc;
    print(" lowercase"), redo LOOP if /\G\p{Ll} +\b[, .;] ?\s * / gc;
    print(" UPPERCASE"), redo LOOP if /\G\p{Lu} +\b[, .;] ?\s * / gc;
    print(" Capitalized"), redo LOOP if /\G\p
    {
        Lu
    }
    \p{Ll} +\b[, .;] ?\s * / gc;
    print(" MiXeD"), redo LOOP if /\G\pL +\b[, .;]                      ?\s                      */ gc;
    print(" alphanumeric"), redo LOOP if /\G[\p { Alpha }\pN] +\b[, .;] ?\s * / gc;
    print(" line-noise"), redo LOOP if /\G\W + / gc;
    print ". That's all!\n";
}
 

 Here is the output (split into several lines): 

 <pre>
 line-noise lowercase line-noise UPPERCASE line-noise UPPERCASE
 line-noise lowercase line-noise lowercase line-noise lowercase
 lowercase line-noise lowercase lowercase line-noise lowercase
 lowercase line-noise MiXeD line-noise. That's all!
</pre>
<dt>&quot;m?<i>PATTERN</i>?msixpodualngc&quot;
<dd> This is just like the <tt>&quot;m/</tt>PATTERN<tt>/&quot;</tt> search, except that it matches only once between calls to the <tt>&quot;reset()&quot;</tt> operator. This is a useful optimization when you want to see only the first occurrence of something in each file of a set of files, for instance. Only <tt>&quot;m??&quot;</tt> patterns local to the current package are reset. 

 
while (&lt;&gt;) {
        if (m?^$?) {
#blank line between header and body
        }
}
continue
{
    reset if eof;
#clear m ? ? status for next file
}
 

 Another example switched the first ``latin1'' encoding it finds to ``utf8'' in a pod file: 

 <pre>
    s//utf8/ if m? ^ =encoding \h+ \K latin1 ?x;
</pre> 

 The match-once behavior is controlled by the match delimiter being <tt>&quot;?&quot;</tt>; with any other delimiter this is the normal <tt>&quot;m//&quot;</tt> operator. 

 In the past, the leading <tt>&quot;m&quot;</tt> in <tt>&quot;m?</tt>PATTERN<tt>?&quot;</tt> was optional, but omitting it would produce a deprecation warning. As of v5.22.0, omitting it produces a syntax error. If you encounter this construct in older code, you can just add <tt>&quot;m&quot;</tt>.
<dt>&quot;s/<i>PATTERN</i>/<i>REPLACEMENT</i>/msixpodualngcer&quot;
<dd> Searches a string for a pattern, and if found, replaces that pattern with the replacement text and returns the number of substitutions made. Otherwise it returns false (a value that is both an empty string (<tt>&quot;&quot;</tt>) and numeric zero (<tt>0</tt>) as described in ``Relational Operators''). 

 If the <tt>&quot;/r&quot;</tt> (non-destructive) option is used then it runs the substitution on a copy of the string and instead of returning the number of substitutions, it returns the copy whether or not a substitution occurred. The original string is never changed when <tt>&quot;/r&quot;</tt> is used. The copy will always be a plain string, even if the input is an object or a tied variable. 

 If no string is specified via the <tt>&quot;=~&quot;</tt> or <tt>&quot;!~&quot;</tt> operator, the <tt>$_</tt> variable is searched and modified. Unless the <tt>&quot;/r&quot;</tt> option is used, the string specified must be a scalar variable, an array element, a hash element, or an assignment to one of those; that is, some sort of scalar lvalue. 

 If the delimiter chosen is a single quote, no variable interpolation is done on either the <i></i><font SIZE="-1"><i>PATTERN</i></font><i></i> or the <i></i><font SIZE="-1"><i>REPLACEMENT</i></font><i></i>. Otherwise, if the <i></i><font SIZE="-1"><i>PATTERN</i></font><i></i> contains a <tt>&quot;$&quot;</tt> that looks like a variable rather than an end-of-string test, the variable will be interpolated into the pattern at run-time. If you want the pattern compiled only once the first time the variable is interpolated, use the <tt>&quot;/o&quot;</tt> option. If the pattern evaluates to the empty string, the last successfully executed regular expression is used instead. See perlre for further explanation on these. 

 Options are as with <tt>&quot;m//&quot;</tt> with the addition of the following replacement specific options: 

 <pre>
    e   Evaluate the right side as an expression.
    ee  Evaluate the right side as a string then eval the
        result.
    r   Return substitution and leave the original string
        untouched.
</pre> 

 Any non-whitespace delimiter may replace the slashes. Add space after the <tt>&quot;s&quot;</tt> when using a character allowed in identifiers. If single quotes are used, no interpretation is done on the replacement string (the <tt>&quot;/e&quot;</tt> modifier overrides this, however). Note that Perl treats backticks as normal delimiters; the replacement text is not evaluated as a command. If the <i></i><font SIZE="-1"><i>PATTERN</i></font><i></i> is delimited by bracketing quotes, the <i></i><font SIZE="-1"><i>REPLACEMENT</i></font><i></i> has its own pair of quotes, which may or may not be bracketing quotes, for example, <tt>&quot;s(foo)(bar)&quot;</tt> or <tt>&quot;s&lt;foo&gt;/bar/&quot;</tt>. A <tt>&quot;/e&quot;</tt> will cause the replacement portion to be treated as a full-fledged Perl expression and evaluated right then and there. It is, however, syntax checked at compile-time. A second <tt>&quot;e&quot;</tt> modifier will cause the replacement portion to be <tt>&quot;eval&quot;</tt>ed before being run as a Perl expression. 

 Examples: 

 
s /\bgreen\b / mauve / g;
#don't change wintergreen $path = ~s | / usr / bin | / usr / local / bin | ;
s / Login : $foo / Login : $bar / ;
#run - time pattern($foo = $bar) = ~s / this / that / ;
#copy first, then
#change
             ($foo = "$bar") = ~s / this / that /
    ;
#convert to string,
#copy, then change
    $foo = $bar = ~s / this / that / r;
#Same as above using / r
                           $foo = $bar = ~s / this / that / r = ~s / that / the other / r;
#Chained substitutes
#using / r
    @foo = map
{
    s / this / that / r
}
@bar # / r is very useful in
#maps
             $count = ($paragraph = ~s / Mister\b / Mr./ g);
#get change - cnt
                  $_ = 'abc123xyz';
s /\d + / $ &amp; * 2 / e;
#yields 'abc246xyz' s /\d + / sprintf("%5d", $ &amp;) / e;
#yields 'abc  246xyz' s /\w / $ &amp;x 2 / eg;
#yields 'aabbcc  224466xxyyzz' s / % (.) / $percent{$1 } / g;
#change percent escapes;
no / e s / % (.) / $percent{$1} || $ &amp; / ge;
#expr now, so / e s / ^= (\w +) / pod($1) / ge;
#use function call
    $_ = 'abc123xyz';
$x = s / abc / def / r;
#$x is 'def123xyz' and
#$_ remains 'abc123xyz'.
#expand variables in $_, but dynamics only, using
#symbolic dereferencing
    s /\$(\w +) / ${$1 } / g;
#Add one to the value of any numbers in the string
s / (\d +) / 1 + $1 / eg;
#Titlecase words in the last 30 characters only
substr($str, -30) = ~s /\b(\p{Alpha} +)\b /\u\L$1 / g;
#This will expand any embedded scalar variable
#(including lexicals) in $_ : First $1 is interpolated
#to the variable name, and then evaluated
s / (\$\w +) / $1 / eeg;
#Delete(most) C comments.
$program = ~s{
    /\* #Match the opening delimiter..*? #Match a minimal number of characters.
        \* / #Match the closing delimiter.}[] gsx;
    s/^\s*(.*?)\s*$/$1/;
#trim whitespace in $_,
#expensively
        for ($variable){#trim whitespace in $variable,
#cheap
                        s / ^\s +     //;
                            s /\s + $ //;
    } s / ([^] *)*([^] *) / $2 $1 /
        ;
#reverse 1st two fields
            $foo !~s /
        A / a / g;
#Lowercase all A's in $foo; return
# 0 if any were found and changed;
#otherwise return 1
 

 Note the use of <tt>&quot;$&quot;</tt> instead of <tt>&quot;\&quot;</tt> in the last example. Unlike <b>sed</b>, we use the \&lt;<i>digit</i>&gt; form only in the left hand side. Anywhere else it's $&lt;<i>digit</i>&gt;. 

 Occasionally, you can't use just a <tt>&quot;/g&quot;</tt> to get all the changes to occur that you might want. Here are two common cases: 

 
#put commas in the right places in an integer
    1 while s/(\d)(\d\d\d)(?!\d)/$1,$2/g;
#expand tabs to 8 - column spacing
    1 while s /\t + / ' ' x(length($ &amp;) * 8 - length($`) % 8) / e;
</dl>

<h3>Quote-Like Operators</h3>

<dl>
<dt>&quot;q/<i>STRING</i>/&quot;
<dd>
<dt>'<i>STRING</i>'
<dd> A single-quoted, literal string. A backslash represents a backslash unless followed by the delimiter or another backslash, in which case the delimiter or backslash is interpolated. 

 
$foo = q !I said, "You said, 'She said it.'" !;
$bar = q('This is it.');
$baz = '\n';
#a two - character string

<dt>&quot;qq/<i>STRING</i>/&quot;
<dd>
<dt>&quot;<i></i><font SIZE="-1"><i>STRING</i></font><i></i>&quot;
<dd> A double-quoted, interpolated string. 

 
$_.= qq(***The previous line contains the naughty word "$1".\n) if /\b(tcl | java | python)\b / i;
# : -)
    $baz = "\n";
#a one - character string

<dt>&quot;qx/<i>STRING</i>/&quot;
<dd>
<dt>&quot;`<i>STRING</i>`&quot;
<dd> A string which is (possibly) interpolated and then executed as a system command with <i>/bin/sh</i> or its equivalent. Shell wildcards, pipes, and redirections will be honored. The collected standard output of the command is returned; standard error is unaffected. In scalar context, it comes back as a single (potentially multi-line) string, or <tt>&quot;undef&quot;</tt> if the command failed. In list context, returns a list of lines (however you've defined lines with <tt>$/</tt> or <tt>$INPUT_RECORD_SEPARATOR</tt>), or an empty list if the command failed. 

 Because backticks do not affect standard error, use shell file descriptor syntax (assuming the shell supports this) if you care to address this. To capture a command's <font SIZE="-1">STDERR</font> and <font SIZE="-1">STDOUT</font> together: 

 <pre>
    $output = `cmd 2&gt;&amp;1`;
</pre> 

 To capture a command's <font SIZE="-1">STDOUT</font> but discard its <font SIZE="-1">STDERR:</font> 

 <pre>
    $output = `cmd 2&gt;/dev/null`;
</pre> 

 To capture a command's <font SIZE="-1">STDERR</font> but discard its <font SIZE="-1">STDOUT</font> (ordering is important here): 

 <pre>
    $output = `cmd 2&gt;&amp;1 1&gt;/dev/null`;
</pre> 

 To exchange a command's <font SIZE="-1">STDOUT</font> and <font SIZE="-1">STDERR</font> in order to capture the <font SIZE="-1">STDERR</font> but leave its <font SIZE="-1">STDOUT</font> to come out the old <font SIZE="-1">STDERR:</font> 

 <pre>
    $output = `cmd 3&gt;&amp;1 1&gt;&amp;2 2&gt;&amp;3 3&gt;&amp;-`;
</pre> 

 To read both a command's <font SIZE="-1">STDOUT</font> and its <font SIZE="-1">STDERR</font> separately, it's easiest to redirect them separately to files, and then read from those files when the program is done: 

 <pre>
    system(&quot;program args 1&gt;program.stdout 2&gt;program.stderr&quot;);
</pre> 

 The <font SIZE="-1">STDIN</font> filehandle used by the command is inherited from Perl's <font SIZE="-1">STDIN.</font> For example: 

 
open(SPLAT, "stuff") || die "can't open stuff: $!";
open(STDIN, "&lt;&amp;SPLAT") || die "can't dupe SPLAT: $!";
print STDOUT `sort`;
 

 will print the sorted contents of the file named <i>``stuff''</i>. 

 Using single-quote as a delimiter protects the command from Perl's double-quote interpolation, passing it on to the shell instead: 

 
$perl_info = qx(ps $$);
#that 's Perl' s $$
    $shell_info = qx 'ps $$';
#that 's the new shell' s $$
 

 How that string gets evaluated is entirely subject to the command interpreter on your system. On most platforms, you will have to protect shell metacharacters if you want them treated literally. This is in practice difficult to do, as it's unclear how to escape which characters. See perlsec for a clean and safe example of a manual <tt>&quot;fork()&quot;</tt> and <tt>&quot;exec()&quot;</tt> to emulate backticks safely. 

 On some platforms (notably DOS-like ones), the shell may not be capable of dealing with multiline commands, so putting newlines in the string may not get you what you want. You may be able to evaluate multiple commands in a single line by separating them with the command separator character, if your shell supports that (for example, <tt>&quot;;&quot;</tt> on many Unix shells and <tt>&quot;&amp;&quot;</tt> on the Windows <font SIZE="-1">NT</font> <tt>&quot;cmd&quot;</tt> shell). 

 Perl will attempt to flush all files opened for output before starting the child process, but this may not be supported on some platforms (see perlport). To be safe, you may need to set <tt>$|</tt> (<tt>$AUTOFLUSH</tt> in <tt>&quot;English&quot;</tt>) or call the <tt>&quot;autoflush()&quot;</tt> method of <tt>&quot;IO::Handle&quot;</tt> on any open handles. 

 Beware that some command shells may place restrictions on the length of the command line. You must ensure your strings don't exceed this limit after any necessary interpolations. See the platform-specific release notes for more details about your particular environment. 

 Using this operator can lead to programs that are difficult to port, because the shell commands called vary between systems, and may in fact not be present at all. As one example, the <tt>&quot;type&quot;</tt> command under the <font SIZE="-1">POSIX</font> shell is very different from the <tt>&quot;type&quot;</tt> command under <font SIZE="-1">DOS.</font> That doesn't mean you should go out of your way to avoid backticks when they're the right way to get something done. Perl was made to be a glue language, and one of the things it glues together is commands. Just understand what you're getting yourself into. 

 Like <tt>&quot;system&quot;</tt>, backticks put the child process exit code in <tt>$?</tt>. If you'd like to manually inspect failure, you can check all possible failure modes by inspecting <tt>$?</tt> like this: 

 
    if ($? == -1) {
        print "failed to execute: $!\n";
    }
    elsif ($? &amp; 127)
    {
        printf "child died with signal %d, %s coredump\n",
            ($? &amp; 127),  ($? &amp; 128) ? 'with' : 'without';
    }
    else
    {
        printf "child exited with value %d\n", $ ? &gt;&gt; 8;
    }
 

 Use the open pragma to control the I/O layers used when reading the output of the command, for example: 

 <pre>
  use open IN =&gt; &quot;:encoding(UTF-8)&quot;;
  my $x = `cmd-producing-utf-8`;
</pre> 

 <tt>&quot;qx//&quot;</tt> can also be called like a function with ``readpipe'' in perlfunc. 

 See ``I/O Operators'' for more discussion.
<dt>&quot;qw/<i>STRING</i>/&quot;
<dd> Evaluates to a list of the words extracted out of <i></i><font SIZE="-1"><i>STRING</i></font><i></i>, using embedded whitespace as the word delimiters. It can be understood as being roughly equivalent to: 

 <pre>
    split(&quot; &quot;, q/STRING/);
</pre> 

 the differences being that it only splits on <font SIZE="-1">ASCII</font> whitespace, generates a real list at compile time, and in scalar context it returns the last element in the list. So this expression: 

 <pre>
    qw(foo bar baz)
</pre> 

 is semantically equivalent to the list: 

 <pre>
    &quot;foo&quot;, &quot;bar&quot;, &quot;baz&quot;
</pre> 

 Some frequently seen examples: 

 <pre>
    use POSIX qw( setlocale localeconv )
    @EXPORT = qw( foo bar baz );
</pre> 

 A common mistake is to try to separate the words with commas or to put comments into a multi-line <tt>&quot;qw&quot;</tt>-string. For this reason, the <tt>&quot;use warnings&quot;</tt> pragma and the <b>-w</b> switch (that is, the <tt>$^W</tt> variable) produces warnings if the <i></i><font SIZE="-1"><i>STRING</i></font><i></i> contains the <tt>&quot;,&quot;</tt> or the <tt>&quot;#&quot;</tt> character.
<dt>&quot;tr/<i>SEARCHLIST</i>/<i>REPLACEMENTLIST</i>/cdsr&quot;
<dd>
<dt>&quot;y/<i>SEARCHLIST</i>/<i>REPLACEMENTLIST</i>/cdsr&quot;
<dd> Transliterates all occurrences of the characters found (or not found if the <tt>&quot;/c&quot;</tt> modifier is specified) in the search list with the positionally corresponding character in the replacement list, possibly deleting some, depending on the modifiers specified. It returns the number of characters replaced or deleted. If no string is specified via the <tt>&quot;=~&quot;</tt> or <tt>&quot;!~&quot;</tt> operator, the <tt>$_</tt> string is transliterated. 

 For <b>sed</b> devotees, <tt>&quot;y&quot;</tt> is provided as a synonym for <tt>&quot;tr&quot;</tt>. 

 If the <tt>&quot;/r&quot;</tt> (non-destructive) option is present, a new copy of the string is made and its characters transliterated, and this copy is returned no matter whether it was modified or not: the original string is always left unchanged. The new copy is always a plain string, even if the input string is an object or a tied variable. 

 Unless the <tt>&quot;/r&quot;</tt> option is used, the string specified with <tt>&quot;=~&quot;</tt> must be a scalar variable, an array element, a hash element, or an assignment to one of those; in other words, an lvalue. 

 If the characters delimiting <i></i><font SIZE="-1"><i>SEARCHLIST</i></font><i></i> and <i></i><font SIZE="-1"><i>REPLACEMENTLIST</i></font><i></i> are single quotes (<tt>&quot;tr'</tt>SEARCHLIST<tt>'</tt>REPLACEMENTLIST<tt>'&quot;</tt>), the only interpolation is removal of <tt>&quot;\&quot;</tt> from pairs of <tt>&quot;\\&quot;</tt>. 

 Otherwise, a character range may be specified with a hyphen, so <tt>&quot;tr/A-J/0-9/&quot;</tt> does the same replacement as <tt>&quot;tr/ACEGIBDFHJ/0246813579/&quot;</tt>. 

 If the <i></i><font SIZE="-1"><i>SEARCHLIST</i></font><i></i> is delimited by bracketing quotes, the <i></i><font SIZE="-1"><i>REPLACEMENTLIST</i></font><i></i> must have its own pair of quotes, which may or may not be bracketing quotes; for example, <tt>&quot;tr[aeiouy][yuoiea]&quot;</tt> or <tt>&quot;tr(+\-*/)/ABCD/&quot;</tt>. 

 Characters may be literals, or (if the delimiters aren't single quotes) any of the escape sequences accepted in double-quoted strings. But there is never any variable interpolation, so <tt>&quot;$&quot;</tt> and <tt>&quot;@&quot;</tt> are always treated as literals. A hyphen at the beginning or end, or preceded by a backslash is also always considered a literal. Escape sequence details are in the table near the beginning of this section. 

 Note that <tt>&quot;tr&quot;</tt> does <b>not</b> do regular expression character classes such as <tt>&quot;\d&quot;</tt> or <tt>&quot;\pL&quot;</tt>. The <tt>&quot;tr&quot;</tt> operator is not equivalent to the <tt><a HREF="/docs/linux/man/1-tr/">tr</a>(1)</tt> utility. <tt>&quot;tr[a-z][A-Z]&quot;</tt> will uppercase the 26 letters ``a'' through ``z'', but for case changing not confined to <font SIZE="-1">ASCII,</font> use <tt>&quot;lc&quot;</tt>, <tt>&quot;uc&quot;</tt>, <tt>&quot;lcfirst&quot;</tt>, <tt>&quot;ucfirst&quot;</tt> (all documented in perlfunc), or the substitution operator <tt>&quot;s/</tt>PATTERN<tt>/</tt>REPLACEMENT<tt>/&quot;</tt> (with <tt>&quot;\U&quot;</tt>, <tt>&quot;\u&quot;</tt>, <tt>&quot;\L&quot;</tt>, and <tt>&quot;\l&quot;</tt> string-interpolation escapes in the <i></i><font SIZE="-1"><i>REPLACEMENT</i></font><i></i> portion). 

 Most ranges are unportable between character sets, but certain ones signal Perl to do special handling to make them portable. There are two classes of portable ranges. The first are any subsets of the ranges <tt>&quot;A-Z&quot;</tt>, <tt>&quot;a-z&quot;</tt>, and <tt>&quot;0-9&quot;</tt>, when expressed as literal characters. 

 <pre>
  tr/h-k/H-K/
</pre> 

 capitalizes the letters <tt>&quot;h&quot;</tt>, <tt>&quot;i&quot;</tt>, <tt>&quot;j&quot;</tt>, and <tt>&quot;k&quot;</tt> and nothing else, no matter what the platform's character set is. In contrast, all of 

 <pre>
  tr/\x68-\x6B/\x48-\x4B/
  tr/h-\x6B/H-\x4B/
  tr/\x68-k/\x48-K/
</pre> 

 do the same capitalizations as the previous example when run on <font SIZE="-1">ASCII</font> platforms, but something completely different on <font SIZE="-1">EBCDIC</font> ones. 

 The second class of portable ranges is invoked when one or both of the range's end points are expressed as <tt>&quot;\N{...}&quot;</tt> 

 
$string = ~tr /\N{U + 20} -\N
{
    U + 7E
} // d;
 

 removes from <tt>$string</tt> all the platform's characters which are equivalent to any of Unicode U+0020, U+0021, ... U+007D, U+007E. This is a portable range, and has the same effect on every platform it is run on. In this example, these are the <font SIZE="-1">ASCII</font> printable characters. So after this is run, <tt>$string</tt> has only controls and characters which have no <font SIZE="-1">ASCII</font> equivalents. 

 But, even for portable ranges, it is not generally obvious what is included without having to look things up in the manual. A sound principle is to use only ranges that both begin from, and end at, either <font SIZE="-1">ASCII</font> alphabetics of equal case (<tt>&quot;b-e&quot;</tt>, <tt>&quot;B-E&quot;</tt>), or digits (<tt>&quot;1-4&quot;</tt>). Anything else is unclear (and unportable unless <tt>&quot;\N{...}&quot;</tt> is used). If in doubt, spell out the character sets in full. 

 Options: 

 <pre>
    c   Complement the SEARCHLIST.
    d   Delete found but unreplaced characters.
    r   Return the modified string and leave the original string
        untouched.
    s   Squash duplicate replaced characters.
</pre> 

 If the <tt>&quot;/d&quot;</tt> modifier is specified, any characters specified by <i></i><font SIZE="-1"><i>SEARCHLIST</i></font><i></i> not found in <i></i><font SIZE="-1"><i>REPLACEMENTLIST</i></font><i></i> are deleted. (Note that this is slightly more flexible than the behavior of some <b>tr</b> programs, which delete anything they find in the <i></i><font SIZE="-1"><i>SEARCHLIST</i></font><i></i>, period.) 

 If the <tt>&quot;/s&quot;</tt> modifier is specified, sequences of characters, all in a row, that were transliterated to the same character are squashed down to a single instance of that character. 

 <pre>
 my $a = &quot;aaaba&quot;
 $a =~ tr/a/a/s     # $a now is &quot;aba&quot;
</pre> 

 If the <tt>&quot;/d&quot;</tt> modifier is used, the <i></i><font SIZE="-1"><i>REPLACEMENTLIST</i></font><i></i> is always interpreted exactly as specified. Otherwise, if the <i></i><font SIZE="-1"><i>REPLACEMENTLIST</i></font><i></i> is shorter than the <i></i><font SIZE="-1"><i>SEARCHLIST</i></font><i></i>, the final character, if any, is replicated until it is long enough. There won't be a final character if and only if the <i></i><font SIZE="-1"><i>REPLACEMENTLIST</i></font><i></i> is empty, in which case <i></i><font SIZE="-1"><i>REPLACEMENTLIST</i></font><i></i> is copied from <i></i><font SIZE="-1"><i>SEARCHLIST</i></font><i></i>. An empty <i></i><font SIZE="-1"><i>REPLACEMENTLIST</i></font><i></i> is useful for counting characters in a class, or for squashing character sequences in a class. 

 
    tr/abcd//            tr/abcd/abcd/
    tr/abcd/AB/          tr/abcd/ABBB/
    tr/abcd//d           s/[abcd]//g
    tr/abcd/AB/d         (tr/ab/AB/ + s/[cd]//g)  - but run together
 

 If the <tt>&quot;/c&quot;</tt> modifier is specified, the characters to be transliterated are the ones <font SIZE="-1">NOT</font> in <i></i><font SIZE="-1"><i>SEARCHLIST</i></font><i></i>, that is, it is complemented. If <tt>&quot;/d&quot;</tt> and/or <tt>&quot;/s&quot;</tt> are also specified, they apply to the complemented <i></i><font SIZE="-1"><i>SEARCHLIST</i></font><i></i>. Recall, that if <i></i><font SIZE="-1"><i>REPLACEMENTLIST</i></font><i></i> is empty (except under <tt>&quot;/d&quot;</tt>) a copy of <i></i><font SIZE="-1"><i>SEARCHLIST</i></font><i></i> is used instead. That copy is made after complementing under <tt>&quot;/c&quot;</tt>. <i></i><font SIZE="-1"><i>SEARCHLIST</i></font><i></i> is sorted by code point order after complementing, and any <i></i><font SIZE="-1"><i>REPLACEMENTLIST</i></font><i></i> is applied to that sorted result. This means that under <tt>&quot;/c&quot;</tt>, the order of the characters specified in <i></i><font SIZE="-1"><i>SEARCHLIST</i></font><i></i> is irrelevant. This can lead to different results on <font SIZE="-1">EBCDIC</font> systems if <i></i><font SIZE="-1"><i>REPLACEMENTLIST</i></font><i></i> contains more than one character, hence it is generally non-portable to use <tt>&quot;/c&quot;</tt> with such a <i></i><font SIZE="-1"><i>REPLACEMENTLIST</i></font><i></i>. 

 Another way of describing the operation is this: If <tt>&quot;/c&quot;</tt> is specified, the <i></i><font SIZE="-1"><i>SEARCHLIST</i></font><i></i> is sorted by code point order, then complemented. If <i></i><font SIZE="-1"><i>REPLACEMENTLIST</i></font><i></i> is empty and <tt>&quot;/d&quot;</tt> is not specified, <i></i><font SIZE="-1"><i>REPLACEMENTLIST</i></font><i></i> is replaced by a copy of <i></i><font SIZE="-1"><i>SEARCHLIST</i></font><i></i> (as modified under <tt>&quot;/c&quot;</tt>), and these potentially modified lists are used as the basis for what follows. Any character in the target string that isn't in <i></i><font SIZE="-1"><i>SEARCHLIST</i></font><i></i> is passed through unchanged. Every other character in the target string is replaced by the character in <i></i><font SIZE="-1"><i>REPLACEMENTLIST</i></font><i></i> that positionally corresponds to its mate in <i></i><font SIZE="-1"><i>SEARCHLIST</i></font><i></i>, except that under <tt>&quot;/s&quot;</tt>, the 2nd and following characters are squeezed out in a sequence of characters in a row that all translate to the same character. If <i></i><font SIZE="-1"><i>SEARCHLIST</i></font><i></i> is longer than <i></i><font SIZE="-1"><i>REPLACEMENTLIST</i></font><i></i>, characters in the target string that match a character in <i></i><font SIZE="-1"><i>SEARCHLIST</i></font><i></i> that doesn't have a correspondence in <i></i><font SIZE="-1"><i>REPLACEMENTLIST</i></font><i></i> are either deleted from the target string if <tt>&quot;/d&quot;</tt> is specified; or replaced by the final character in <i></i><font SIZE="-1"><i>REPLACEMENTLIST</i></font><i></i> if <tt>&quot;/d&quot;</tt> isn't specified. 

 Some examples: 

 
$ARGV[1] = ~tr / A - Z / a - z / ;
#canonicalize to lower case ASCII
    $cnt = tr /*/*/;
#count the stars in $_
    $cnt = tr /*//;             # same thing
     $cnt = $sky =~ tr/*/
           * /
    ;
#count the stars in $sky
    $cnt = $sky = ~tr /*//;     # same thing
     $cnt = $sky =~ tr/*/
                  / c;
#count all the non - stars in $sky
                         $cnt = $sky = ~tr /*/*/ c;
#same, but transliterate each non - star
#into a star, leaving the already - stars
#alone.Afterwards, everything in $sky
#is a star.
                                        $cnt = tr / 0 - 9 //;           # count the ASCII digits in $_
                                                            tr /
                                                            a -
                                               zA - Z // s;              # bookkeeper -&gt; bokeper
                                                            tr /
                                                        o / o / s;
#bookkeeper-&gt;bokkeeper
        tr /
    oe / oe / s;
#bookkeeper-&gt;bokkeper
        tr /
    oe // s;                  # bookkeeper -&gt; bokkeper
        tr /
    oe / o / s;
#bookkeeper-&gt;bokkopor($HOST = $host) = ~tr / a - z / A - Z / ;
$HOST = $host = ~tr / a - z / A - Z / r;
#same thing
    $HOST = $host = ~tr / a - z / A - Z / r #chained with s /// r
    = ~s / : / -p / r;
tr / a - zA - Z / / cs;
#change non - alphas to single space
    @stripped = map tr / a - zA - Z / / csr,
    @original;
#/ r with map
tr[\200 -\377]
  [\000 -\177];
#wickedly delete 8th bit
        $foo !~tr /
    A / a / #transliterate all the A 's in $foo to ' a',
#return 0 if any were found and changed.
#Otherwise return 1
 

 If multiple transliterations are given for a character, only the first one is used: 

 <pre>
 tr/AAA/XYZ/
</pre> 

 will transliterate any A to X. 

 Because the transliteration table is built at compile time, neither the <i></i><font SIZE="-1"><i>SEARCHLIST</i></font><i></i> nor the <i></i><font SIZE="-1"><i>REPLACEMENTLIST</i></font><i></i> are subjected to double quote interpolation. That means that if you want to use variables, you must use an <tt>&quot;eval()&quot;</tt>: 

 
eval "tr/$oldlist/$newlist/";
die $ @ if $ @;
eval "tr/$oldlist/$newlist/, 1" or die $ @;

<dt>&quot;&lt;&lt;<i>EOF</i>&quot;
<dd> A line-oriented form of quoting is based on the shell ``here-document'' syntax. Following a <tt>&quot;&lt;&lt;&quot;</tt> you specify a string to terminate the quoted material, and all lines following the current line down to the terminating string are the value of the item. 

 Prefixing the terminating string with a <tt>&quot;~&quot;</tt> specifies that you want to use ``Indented Here-docs'' (see below). 

 The terminating string may be either an identifier (a word), or some quoted text. An unquoted identifier works like double quotes. There may not be a space between the <tt>&quot;&lt;&lt;&quot;</tt> and the identifier, unless the identifier is explicitly quoted. The terminating string must appear by itself (unquoted and with no surrounding whitespace) on the terminating line. 

 If the terminating string is quoted, the type of quotes used determine the treatment of the text.
<dl>
<dt>
<dd>
<dl>
<dt>Double Quotes
<dd> Double quotes indicate that the text will be interpolated using exactly the same rules as normal double quoted strings. 

 <pre>
       print &lt;&lt;EOF;
    The price is $Price.
    EOF
       print &lt;&lt; &quot;EOF&quot;; # same as above
    The price is $Price.
    EOF
</pre>
<dt>Single Quotes
<dd> Single quotes indicate the text is to be treated literally with no interpolation of its content. This is similar to single quoted strings except that backslashes have no special meaning, with <tt>&quot;\\&quot;</tt> being treated as two backslashes and not one as they would in every other quoting construct. 

 Just as in the shell, a backslashed bareword following the <tt>&quot;&lt;&lt;&quot;</tt> means the same thing as a single-quoted string does: 

 <pre>
        $cost = &lt;&lt;'VISTA';  # hasta la ...
    That'll be $10 please, ma'am.
    VISTA
        $cost = &lt;&lt;\VISTA;   # Same thing!
    That'll be $10 please, ma'am.
    VISTA
</pre> 

 This is the only form of quoting in perl where there is no need to worry about escaping content, something that code generators can and do make good use of.
<dt>Backticks
<dd> The content of the here doc is treated just as it would be if the string were embedded in backticks. Thus the content is interpolated as though it were double quoted and then executed via the shell, with the results of the execution returned. 

 <pre>
       print &lt;&lt; `EOC`; # execute command and get results
    echo hi there
    EOC
</pre></dl>
</dl>

<dl>
<dt>
<dd>
<dl>
<dt>Indented Here-docs
<dd> The here-doc modifier <tt>&quot;~&quot;</tt> allows you to indent your here-docs to make the code more readable: 

 
if ($some_var) {
    print &lt;&lt; ~EOF;
    This is a here - doc
                         EOF
}
 

 This will print... 

 <pre>
    This is a here-doc
</pre> 

 ...with no leading whitespace. 

 The delimiter is used to determine the <b>exact</b> whitespace to remove from the beginning of each line. All lines <b>must</b> have at least the same starting whitespace (except lines only containing a newline) or perl will croak. Tabs and spaces can be mixed, but are matched exactly. One tab will not be equal to 8 spaces! 

 Additional beginning whitespace (beyond what preceded the delimiter) will be preserved: 

 <pre>
    print &lt;&lt;~EOF;
      This text is not indented
        This text is indented with two spaces
                This text is indented with two tabs
      EOF
</pre> 

 Finally, the modifier may be used with all of the forms mentioned above: 

 <pre>
    &lt;&lt;~\EOF;
    &lt;&lt;~'EOF'
    &lt;&lt;~&quot;EOF&quot;
    &lt;&lt;~`EOF`
</pre> 

 And whitespace may be used between the <tt>&quot;~&quot;</tt> and quoted delimiters: 

 <pre>
    &lt;&lt;~ 'EOF'; # ... &quot;EOF&quot;, `EOF`
</pre></dl>
</dl>

<dl>
<dt>
<dd> 

 It is possible to stack multiple here-docs in a row: 

 
print &lt;&lt; "foo", &lt;&lt; "bar";
#you can stack them
    I said foo.foo
        I said bar.bar
            myfunc(&lt;&lt; "THIS", 23, &lt;&lt; 'THAT');
Here's a line or two.THIS
                     and here's another. THAT
 

 Just don't forget that you have to put a semicolon on the end to finish the statement, as Perl doesn't know you're not going to try to do this: 

 <pre>
       print &lt;&lt;ABC
    179231
    ABC
       + 20;
</pre> 

 If you want to remove the line terminator from your here-docs, use <tt>&quot;chomp()&quot;</tt>. 

 <pre>
    chomp($string = &lt;&lt;'END');
    This is a string.
    END
</pre> 

 If you want your here-docs to be indented with the rest of the code, use the <tt>&quot;&lt;&lt;~FOO&quot;</tt> construct described under ``Indented Here-docs'': 

 <pre>
    $quote = &lt;&lt;~'FINIS';
       The Road goes ever on and on,
       down from the door where it began.
       FINIS
</pre> 

 If you use a here-doc within a delimited construct, such as in <tt>&quot;s///eg&quot;</tt>, the quoted material must still come on the line following the <tt>&quot;&lt;&lt;FOO&quot;</tt> marker, which means it may be inside the delimited construct: 

 <pre>
    s/this/&lt;&lt;E . 'that'
    the other
    E
     . 'more '/eg;
</pre> 

 It works this way as of Perl 5.18. Historically, it was inconsistent, and you would have to write 

 <pre>
    s/this/&lt;&lt;E . 'that'
     . 'more '/eg;
    the other
    E
</pre> 

 outside of string evals. 

 Additionally, quoting rules for the end-of-string identifier are unrelated to Perl's quoting rules. <tt>&quot;q()&quot;</tt>, <tt>&quot;qq()&quot;</tt>, and the like are not supported in place of <tt>''</tt> and <tt>&quot;&quot;</tt>, and the only interpolation is for backslashing the quoting character: 

 <pre>
    print &lt;&lt; &quot;abc\&quot;def&quot;;
    testing...
    abc&quot;def
</pre> 

 Finally, quoted strings cannot span multiple lines. The general rule is that the identifier must be a string literal. Stick with that, and you should be safe.</dl>
</dl>

<h3>Gory details of parsing quoted constructs</h3>

 When presented with something that might have several different interpretations, Perl uses the <font SIZE="-1"><b>DWIM</b></font> (that's ``Do What I Mean'') principle to pick the most probable interpretation. This strategy is so successful that Perl programmers often do not suspect the ambivalence of what they write. But from time to time, Perl's notions differ substantially from what the author honestly meant. 

 This section hopes to clarify how Perl handles quoted constructs. Although the most common reason to learn this is to unravel labyrinthine regular expressions, because the initial steps of parsing are the same for all quoting operators, they are all discussed together. 

 The most important Perl parsing rule is the first one discussed below: when processing a quoted construct, Perl first finds the end of that construct, then interprets its contents. If you understand this rule, you may skip the rest of this section on the first reading. The other rules are likely to contradict the user's expectations much less frequently than this first one. 

 Some passes discussed below are performed concurrently, but because their results are the same, we consider them individually. For different quoting constructs, Perl performs different numbers of passes, from one to four, but these passes are always performed in the same order.
<dl>
<dt>Finding the end
<dd> The first pass is finding the end of the quoted construct. This results in saving to a safe location a copy of the text (between the starting and ending delimiters), normalized as necessary to avoid needing to know what the original delimiters were. 

 If the construct is a here-doc, the ending delimiter is a line that has a terminating string as the content. Therefore <tt>&quot;&lt;&lt;EOF&quot;</tt> is terminated by <tt>&quot;EOF&quot;</tt> immediately followed by <tt>&quot;\n&quot;</tt> and starting from the first column of the terminating line. When searching for the terminating line of a here-doc, nothing is skipped. In other words, lines after the here-doc syntax are compared with the terminating string line by line. 

 For the constructs except here-docs, single characters are used as starting and ending delimiters. If the starting delimiter is an opening punctuation (that is <tt>&quot;(&quot;</tt>, <tt>&quot;[&quot;</tt>, <tt>&quot;{&quot;</tt>, or <tt>&quot;&lt;&quot;</tt>), the ending delimiter is the corresponding closing punctuation (that is <tt>&quot;)&quot;</tt>, <tt>&quot;]&quot;</tt>, <tt>&quot;}&quot;</tt>, or <tt>&quot;&gt;&quot;</tt>). If the starting delimiter is an unpaired character like <tt>&quot;/&quot;</tt> or a closing punctuation, the ending delimiter is the same as the starting delimiter. Therefore a <tt>&quot;/&quot;</tt> terminates a <tt>&quot;qq//&quot;</tt> construct, while a <tt>&quot;]&quot;</tt> terminates both <tt>&quot;qq[]&quot;</tt> and <tt>&quot;qq]]&quot;</tt> constructs. 

 When searching for single-character delimiters, escaped delimiters and <tt>&quot;\\&quot;</tt> are skipped. For example, while searching for terminating <tt>&quot;/&quot;</tt>, combinations of <tt>&quot;\\&quot;</tt> and <tt>&quot;\/&quot;</tt> are skipped. If the delimiters are bracketing, nested pairs are also skipped. For example, while searching for a closing <tt>&quot;]&quot;</tt> paired with the opening <tt>&quot;[&quot;</tt>, combinations of <tt>&quot;\\&quot;</tt>, <tt>&quot;\]&quot;</tt>, and <tt>&quot;\[&quot;</tt> are all skipped, and nested <tt>&quot;[&quot;</tt> and <tt>&quot;]&quot;</tt> are skipped as well. However, when backslashes are used as the delimiters (like <tt>&quot;qq\\&quot;</tt> and <tt>&quot;tr\\\&quot;</tt>), nothing is skipped. During the search for the end, backslashes that escape delimiters or other backslashes are removed (exactly speaking, they are not copied to the safe location). 

 For constructs with three-part delimiters (<tt>&quot;s///&quot;</tt>, <tt>&quot;y///&quot;</tt>, and <tt>&quot;tr///&quot;</tt>), the search is repeated once more. If the first delimiter is not an opening punctuation, the three delimiters must be the same, such as <tt>&quot;s!!!&quot;</tt> and <tt>&quot;tr)))&quot;</tt>, in which case the second delimiter terminates the left part and starts the right part at once. If the left part is delimited by bracketing punctuation (that is <tt>&quot;()&quot;</tt>, <tt>&quot;[]&quot;</tt>, <tt>&quot;{}&quot;</tt>, or <tt>&quot;&lt;&gt;&quot;</tt>), the right part needs another pair of delimiters such as <tt>&quot;s(){}&quot;</tt> and <tt>&quot;tr[]//&quot;</tt>. In these cases, whitespace and comments are allowed between the two parts, although the comment must follow at least one whitespace character; otherwise a character expected as the start of the comment may be regarded as the starting delimiter of the right part. 

 During this search no attention is paid to the semantics of the construct. Thus: 

 <pre>
    &quot;$hash{&quot;$foo/$bar&quot;}&quot;
</pre> 

 or: 

 <pre>
    m/
      bar       # NOT a comment, this slash / terminated m//!
     /x
</pre> 

 do not form legal quoted expressions. The quoted part ends on the first <tt>&quot;&quot;&quot;</tt> and <tt>&quot;/&quot;</tt>, and the rest happens to be a syntax error. Because the slash that terminated <tt>&quot;m//&quot;</tt> was followed by a <tt>&quot;SPACE&quot;</tt>, the example above is not <tt>&quot;m//x&quot;</tt>, but rather <tt>&quot;m//&quot;</tt> with no <tt>&quot;/x&quot;</tt> modifier. So the embedded <tt>&quot;#&quot;</tt> is interpreted as a literal <tt>&quot;#&quot;</tt>. 

 Also no attention is paid to <tt>&quot;\c\&quot;</tt> (multichar control char syntax) during this search. Thus the second <tt>&quot;\&quot;</tt> in <tt>&quot;qq/\c\/&quot;</tt> is interpreted as a part of <tt>&quot;\/&quot;</tt>, and the following <tt>&quot;/&quot;</tt> is not recognized as a delimiter. Instead, use <tt>&quot;\034&quot;</tt> or <tt>&quot;\x1c&quot;</tt> at the end of quoted constructs.
<dt>Interpolation
<dd> The next step is interpolation in the text obtained, which is now delimiter-independent. There are multiple cases.
<dl>
<dt>
<dd>
<dl>
<dt>&quot;&lt;&lt;'EOF'&quot;
<dd> No interpolation is performed. Note that the combination <tt>&quot;\\&quot;</tt> is left intact, since escaped delimiters are not available for here-docs.
<dt>&quot;m''&quot;, the pattern of &quot;s'''&quot;
<dd> No interpolation is performed at this stage. Any backslashed sequences including <tt>&quot;\\&quot;</tt> are treated at the stage to ``parsing regular expressions''.
<dt>'', &quot;q//&quot;, &quot;tr'''&quot;, &quot;y'''&quot;, the replacement of &quot;s'''&quot;
<dd> The only interpolation is removal of <tt>&quot;\&quot;</tt> from pairs of <tt>&quot;\\&quot;</tt>. Therefore <tt>&quot;-&quot;</tt> in <tt>&quot;tr'''&quot;</tt> and <tt>&quot;y'''&quot;</tt> is treated literally as a hyphen and no character range is available. <tt>&quot;\1&quot;</tt> in the replacement of <tt>&quot;s'''&quot;</tt> does not work as <tt>$1</tt>.
<dt>&quot;tr///&quot;, &quot;y///&quot;
<dd> No variable interpolation occurs. String modifying combinations for case and quoting such as <tt>&quot;\Q&quot;</tt>, <tt>&quot;\U&quot;</tt>, and <tt>&quot;\E&quot;</tt> are not recognized. The other escape sequences such as <tt>&quot;\200&quot;</tt> and <tt>&quot;\t&quot;</tt> and backslashed characters such as <tt>&quot;\\&quot;</tt> and <tt>&quot;\-&quot;</tt> are converted to appropriate literals. The character <tt>&quot;-&quot;</tt> is treated specially and therefore <tt>&quot;\-&quot;</tt> is treated as a literal <tt>&quot;-&quot;</tt>.
<dt>&quot;&quot;, &quot;``&quot;, &quot;qq//&quot;, &quot;qx//&quot;, &quot;&lt;file*glob&gt;&quot;, &quot;&lt;&lt;&quot;EOF&quot;&quot;
<dd> <tt>&quot;\Q&quot;</tt>, <tt>&quot;\U&quot;</tt>, <tt>&quot;\u&quot;</tt>, <tt>&quot;\L&quot;</tt>, <tt>&quot;\l&quot;</tt>, <tt>&quot;\F&quot;</tt> (possibly paired with <tt>&quot;\E&quot;</tt>) are converted to corresponding Perl constructs. Thus, <tt>&quot;$foo\Qbaz$bar&quot;</tt> is converted to <tt>&quot;$foo . (quotemeta(&quot;baz&quot; . $bar))&quot;</tt> internally. The other escape sequences such as <tt>&quot;\200&quot;</tt> and <tt>&quot;\t&quot;</tt> and backslashed characters such as <tt>&quot;\\&quot;</tt> and <tt>&quot;\-&quot;</tt> are replaced with appropriate expansions. 

 Let it be stressed that <i>whatever falls between </i>&quot;\Q&quot;<i> and </i>&quot;\E&quot;<i></i> is interpolated in the usual way. Something like <tt>&quot;\Q\\E&quot;</tt> has no <tt>&quot;\E&quot;</tt> inside. Instead, it has <tt>&quot;\Q&quot;</tt>, <tt>&quot;\\&quot;</tt>, and <tt>&quot;E&quot;</tt>, so the result is the same as for <tt>&quot;\\\\E&quot;</tt>. As a general rule, backslashes between <tt>&quot;\Q&quot;</tt> and <tt>&quot;\E&quot;</tt> may lead to counterintuitive results. So, <tt>&quot;\Q\t\E&quot;</tt> is converted to <tt>&quot;quotemeta(&quot;\t&quot;)&quot;</tt>, which is the same as <tt>&quot;\\\t&quot;</tt> (since <font SIZE="-1">TAB</font> is not alphanumeric). Note also that: 

 <pre>
  $str = '\t';
  return &quot;\Q$str&quot;;
</pre> 

 may be closer to the conjectural <i>intention</i> of the writer of <tt>&quot;\Q\t\E&quot;</tt>. 

 Interpolated scalars and arrays are converted internally to the <tt>&quot;join&quot;</tt> and <tt>&quot;.&quot;</tt> catenation operations. Thus, <tt>&quot;$foo XXX '@arr'&quot;</tt> becomes: 

 <pre>
  $foo . &quot; XXX '&quot; . (join $&quot;, @arr) . &quot;'&quot;;
</pre> 

 All operations above are performed simultaneously, left to right. 

 Because the result of <tt>&quot;\Q </tt>STRING<tt> \E&quot;</tt> has all metacharacters quoted, there is no way to insert a literal <tt>&quot;$&quot;</tt> or <tt>&quot;@&quot;</tt> inside a <tt>&quot;\Q\E&quot;</tt> pair. If protected by <tt>&quot;\&quot;</tt>, <tt>&quot;$&quot;</tt> will be quoted to become <tt>&quot;\\\$&quot;</tt>; if not, it is interpreted as the start of an interpolated scalar. 

 Note also that the interpolation code needs to make a decision on where the interpolated scalar ends. For instance, whether <tt>&quot;a $x -&gt; {c}&quot;</tt> really means: 

 
"a ".$x." -&gt; {c}";
 

 or: 

 
"a ".$x-&gt;{c};
 

 Most of the time, the longest possible text that does not include spaces between components and which contains matching braces or brackets. because the outcome may be determined by voting based on heuristic estimators, the result is not strictly predictable. Fortunately, it's usually correct for ambiguous cases.
<dt>the replacement of &quot;s///&quot;
<dd> Processing of <tt>&quot;\Q&quot;</tt>, <tt>&quot;\U&quot;</tt>, <tt>&quot;\u&quot;</tt>, <tt>&quot;\L&quot;</tt>, <tt>&quot;\l&quot;</tt>, <tt>&quot;\F&quot;</tt> and interpolation happens as with <tt>&quot;qq//&quot;</tt> constructs. 

 It is at this step that <tt>&quot;\1&quot;</tt> is begrudgingly converted to <tt>$1</tt> in the replacement text of <tt>&quot;s///&quot;</tt>, in order to correct the incorrigible <i>sed</i> hackers who haven't picked up the saner idiom yet. A warning is emitted if the <tt>&quot;use warnings&quot;</tt> pragma or the <b>-w</b> command-line flag (that is, the <tt>$^W</tt> variable) was set.
<dt>&quot;RE&quot; in &quot;m?RE?&quot;, &quot;/RE/&quot;, &quot;m/RE/&quot;, &quot;s/RE/foo/&quot;,
<dd> Processing of <tt>&quot;\Q&quot;</tt>, <tt>&quot;\U&quot;</tt>, <tt>&quot;\u&quot;</tt>, <tt>&quot;\L&quot;</tt>, <tt>&quot;\l&quot;</tt>, <tt>&quot;\F&quot;</tt>, <tt>&quot;\E&quot;</tt>, and interpolation happens (almost) as with <tt>&quot;qq//&quot;</tt> constructs. 

 Processing of <tt>&quot;\N{...}&quot;</tt> is also done here, and compiled into an intermediate form for the regex compiler. (This is because, as mentioned below, the regex compilation may be done at execution time, and <tt>&quot;\N{...}&quot;</tt> is a compile-time construct.) 

 However any other combinations of <tt>&quot;\&quot;</tt> followed by a character are not substituted but only skipped, in order to parse them as regular expressions at the following step. As <tt>&quot;\c&quot;</tt> is skipped at this step, <tt>&quot;@&quot;</tt> of <tt>&quot;\c@&quot;</tt> in <font SIZE="-1">RE</font> is possibly treated as an array symbol (for example <tt>@foo</tt>), even though the same text in <tt>&quot;qq//&quot;</tt> gives interpolation of <tt>&quot;\c@&quot;</tt>. 

 Code blocks such as <tt>&quot;(?{BLOCK})&quot;</tt> are handled by temporarily passing control back to the perl parser, in a similar way that an interpolated array subscript expression such as <tt>&quot;foo$array[1+f(&quot;[xyz&quot;)]bar&quot;</tt> would be. 

 Moreover, inside <tt>&quot;(?{BLOCK})&quot;</tt>, <tt>&quot;(?# comment )&quot;</tt>, and a <tt>&quot;#&quot;</tt>-comment in a <tt>&quot;/x&quot;</tt>-regular expression, no processing is performed whatsoever. This is the first step at which the presence of the <tt>&quot;/x&quot;</tt> modifier is relevant. 

 Interpolation in patterns has several quirks: <tt>$|</tt>, <tt>$(</tt>, <tt>$)</tt>, <tt>&quot;@+&quot;</tt> and <tt>&quot;@-&quot;</tt> are not interpolated, and constructs <tt>$var[SOMETHING]</tt> are voted (by several different estimators) to be either an array element or <tt>$var</tt> followed by an <font SIZE="-1">RE</font> alternative. This is where the notation <tt>&quot;${arr[$bar]}&quot;</tt> comes handy: <tt>&quot;/${arr[0-9]}/&quot;</tt> is interpreted as array element <tt>&quot;-9&quot;</tt>, not as a regular expression from the variable <tt>$arr</tt> followed by a digit, which would be the interpretation of <tt>&quot;/$arr[0-9]/&quot;</tt>. Since voting among different estimators may occur, the result is not predictable. 

 The lack of processing of <tt>&quot;\\&quot;</tt> creates specific restrictions on the post-processed text. If the delimiter is <tt>&quot;/&quot;</tt>, one cannot get the combination <tt>&quot;\/&quot;</tt> into the result of this step. <tt>&quot;/&quot;</tt> will finish the regular expression, <tt>&quot;\/&quot;</tt> will be stripped to <tt>&quot;/&quot;</tt> on the previous step, and <tt>&quot;\\/&quot;</tt> will be left as is. Because <tt>&quot;/&quot;</tt> is equivalent to <tt>&quot;\/&quot;</tt> inside a regular expression, this does not matter unless the delimiter happens to be character special to the <font SIZE="-1">RE</font> engine, such as in <tt>&quot;s*foo*bar*&quot;</tt>, <tt>&quot;m[foo]&quot;</tt>, or <tt>&quot;m?foo?&quot;</tt>; or an alphanumeric char, as in: 

 <pre>
  m m ^ a \s* b mmx;
</pre> 

 In the <font SIZE="-1">RE</font> above, which is intentionally obfuscated for illustration, the delimiter is <tt>&quot;m&quot;</tt>, the modifier is <tt>&quot;mx&quot;</tt>, and after delimiter-removal the <font SIZE="-1">RE</font> is the same as for <tt>&quot;m/ ^ a \s* b /mx&quot;</tt>. There's more than one reason you're encouraged to restrict your delimiters to non-alphanumeric, non-whitespace choices.</dl>
</dl>

<dl>
<dt>
<dd> 

 This step is the last one for all constructs except regular expressions, which are processed further.</dl>

<dt>parsing regular expressions
<dd> Previous steps were performed during the compilation of Perl code, but this one happens at run time, although it may be optimized to be calculated at compile time if appropriate. After preprocessing described above, and possibly after evaluation if concatenation, joining, casing translation, or metaquoting are involved, the resulting <i>string</i> is passed to the <font SIZE="-1">RE</font> engine for compilation. 

 Whatever happens in the <font SIZE="-1">RE</font> engine might be better discussed in perlre, but for the sake of continuity, we shall do so here. 

 This is another step where the presence of the <tt>&quot;/x&quot;</tt> modifier is relevant. The <font SIZE="-1">RE</font> engine scans the string from left to right and converts it into a finite automaton. 

 Backslashed characters are either replaced with corresponding literal strings (as with <tt>&quot;\{&quot;</tt>), or else they generate special nodes in the finite automaton (as with <tt>&quot;\b&quot;</tt>). Characters special to the <font SIZE="-1">RE</font> engine (such as <tt>&quot;|&quot;</tt>) generate corresponding nodes or groups of nodes. <tt>&quot;(?#...)&quot;</tt> comments are ignored. All the rest is either converted to literal strings to match, or else is ignored (as is whitespace and <tt>&quot;#&quot;</tt>-style comments if <tt>&quot;/x&quot;</tt> is present). 

 Parsing of the bracketed character class construct, <tt>&quot;[...]&quot;</tt>, is rather different than the rule used for the rest of the pattern. The terminator of this construct is found using the same rules as for finding the terminator of a <tt>&quot;{}&quot;</tt>-delimited construct, the only exception being that <tt>&quot;]&quot;</tt> immediately following <tt>&quot;[&quot;</tt> is treated as though preceded by a backslash. 

 The terminator of runtime <tt>&quot;(?{...})&quot;</tt> is found by temporarily switching control to the perl parser, which should stop at the point where the logically balancing terminating <tt>&quot;}&quot;</tt> is found. 

 It is possible to inspect both the string given to <font SIZE="-1">RE</font> engine and the resulting finite automaton. See the arguments <tt>&quot;debug&quot;</tt>/<tt>&quot;debugcolor&quot;</tt> in the <tt>&quot;use re&quot;</tt> pragma, as well as Perl's <b>-Dr</b> command-line switch documented in ``Command Switches'' in perlrun.
<dt>Optimization of regular expressions
<dd> This step is listed for completeness only. Since it does not change semantics, details of this step are not documented and are subject to change without notice. This step is performed over the finite automaton that was generated during the previous pass. 

 It is at this stage that <tt>&quot;split()&quot;</tt> silently optimizes <tt>&quot;/^/&quot;</tt> to mean <tt>&quot;/^/m&quot;</tt>.</dl>

<h3>I/O Operators</h3>

 There are several I/O operators you should know about. 

 A string enclosed by backticks (grave accents) first undergoes double-quote interpolation. It is then interpreted as an external command, and the output of that command is the value of the backtick string, like in a shell. In scalar context, a single string consisting of all output is returned. In list context, a list of values is returned, one per line of output. (You can set <tt>$/</tt> to use a different line terminator.) The command is executed each time the pseudo-literal is evaluated. The status value of the command is returned in <tt>$?</tt> (see perlvar for the interpretation of <tt>$?</tt>). Unlike in <b>csh</b>, no translation is done on the return data---newlines remain newlines. Unlike in any of the shells, single quotes do not hide variable names in the command from interpretation. To pass a literal dollar-sign through to the shell you need to hide it with a backslash. The generalized form of backticks is <tt>&quot;qx//&quot;</tt>, or you can call the ``readpipe'' in perlfunc function. (Because backticks always undergo shell expansion as well, see perlsec for security concerns.) 

 In scalar context, evaluating a filehandle in angle brackets yields the next line from that file (the newline, if any, included), or <tt>&quot;undef&quot;</tt> at end-of-file or on error. When <tt>$/</tt> is set to <tt>&quot;undef&quot;</tt> (sometimes known as file-slurp mode) and the file is empty, it returns <tt>''</tt> the first time, followed by <tt>&quot;undef&quot;</tt> subsequently. 

 Ordinarily you must assign the returned value to a variable, but there is one situation where an automatic assignment happens. If and only if the input symbol is the only thing inside the conditional of a <tt>&quot;while&quot;</tt> statement (even if disguised as a <tt>&quot;for(;;)&quot;</tt> loop), the value is automatically assigned to the global variable <tt>$_</tt>, destroying whatever was there previously. (This may seem like an odd thing to you, but you'll use the construct in almost every Perl script you write.) The <tt>$_</tt> variable is not implicitly localized. You'll have to put a <tt>&quot;local $_;&quot;</tt> before the loop if you want that to happen. Furthermore, if the input symbol or an explicit assignment of the input symbol to a scalar is used as a <tt>&quot;while&quot;</tt>/<tt>&quot;for&quot;</tt> condition, then the condition actually tests for definedness of the expression's value, not for its regular truth value. 

 Thus the following lines are equivalent: 

 
while (defined($_ = &lt;STDIN&gt;)) {
    print;
}
while ($_ = &lt;STDIN&gt;) {
    print;
}
while (&lt;STDIN&gt;) {
    print;
}
for (;&lt;STDIN&gt;;) {
    print;
}
print while defined($_ = &lt;STDIN&gt;);
print while ($_ = &lt;STDIN&gt;);
print while&lt;STDIN&gt;;
 

 This also behaves similarly, but assigns to a lexical variable instead of to <tt>$_</tt>: 

 <pre>
    while (my $line = &lt;STDIN&gt;) { print $line }
</pre> 

 In these loop constructs, the assigned value (whether assignment is automatic or explicit) is then tested to see whether it is defined. The defined test avoids problems where the line has a string value that would be treated as false by Perl; for example a &quot;&quot; or a <tt>&quot;0&quot;</tt> with no trailing newline. If you really mean for such values to terminate the loop, they should be tested for explicitly: 

 
while (($_ = &lt;STDIN&gt;)ne '0') {
    ...
}
while (&lt;STDIN&gt;) {
    last unless $_;
    ...
}
 

 In other boolean contexts, <tt>&quot;&lt;</tt>FILEHANDLE<tt>&gt;&quot;</tt> without an explicit <tt>&quot;defined&quot;</tt> test or comparison elicits a warning if the <tt>&quot;use warnings&quot;</tt> pragma or the <b>-w</b> command-line switch (the <tt>$^W</tt> variable) is in effect. 

 The filehandles <font SIZE="-1">STDIN, STDOUT,</font> and <font SIZE="-1">STDERR</font> are predefined. (The filehandles <tt>&quot;stdin&quot;</tt>, <tt>&quot;stdout&quot;</tt>, and <tt>&quot;stderr&quot;</tt> will also work except in packages, where they would be interpreted as local identifiers rather than global.) Additional filehandles may be created with the <tt>&quot;open()&quot;</tt> function, amongst others. See perlopentut and ``open'' in perlfunc for details on this. 

 If a <tt>&quot;&lt;</tt>FILEHANDLE<tt>&gt;&quot;</tt> is used in a context that is looking for a list, a list comprising all input lines is returned, one line per list element. It's easy to grow to a rather large data space this way, so use with care. 

 <tt>&quot;&lt;</tt>FILEHANDLE<tt>&gt;&quot;</tt> may also be spelled <tt>&quot;readline(*</tt>FILEHANDLE<tt>)&quot;</tt>. See ``readline'' in perlfunc. 

 The null filehandle <tt>&quot;&lt;&gt;&quot;</tt> is special: it can be used to emulate the behavior of <b>sed</b> and <b>awk</b>, and any other Unix filter program that takes a list of filenames, doing the same to each line of input from all of them. Input from <tt>&quot;&lt;&gt;&quot;</tt> comes either from standard input, or from each file listed on the command line. Here's how it works: the first time <tt>&quot;&lt;&gt;&quot;</tt> is evaluated, the <tt>@ARGV</tt> array is checked, and if it is empty, <tt>$ARGV[0]</tt> is set to <tt>&quot;-&quot;</tt>, which when opened gives you standard input. The <tt>@ARGV</tt> array is then processed as a list of filenames. The loop 

 
while (&lt;&gt;) {
        ...                     # code for each line
}
 

 is equivalent to the following Perl-like pseudo code: 

 
unshift(@ARGV, '-') unless @ARGV;
while ($ARGV = shift) {
    open(ARGV, $ARGV);
    while (&lt;ARGV&gt;) {
            ...         # code for each line
    }
}
 

 except that it isn't so cumbersome to say, and will actually work. It really does shift the <tt>@ARGV</tt> array and put the current filename into the <tt>$ARGV</tt> variable. It also uses filehandle <i></i><font SIZE="-1"><i>ARGV</i></font><i></i> internally. <tt>&quot;&lt;&gt;&quot;</tt> is just a synonym for <tt>&quot;&lt;ARGV&gt;&quot;</tt>, which is magical. (The pseudo code above doesn't work because it treats <tt>&quot;&lt;ARGV&gt;&quot;</tt> as non-magical.) 

 Since the null filehandle uses the two argument form of ``open'' in perlfunc it interprets special characters, so if you have a script like this: 

 
while (&lt;&gt;) {
    print;
}
 

 and call it with <tt>&quot;perl dangerous.pl 'rm -rfv *|'&quot;</tt>, it actually opens a pipe, executes the <tt>&quot;rm&quot;</tt> command and reads <tt>&quot;rm&quot;</tt>'s output from that pipe. If you want all items in <tt>@ARGV</tt> to be interpreted as file names, you can use the module <tt>&quot;ARGV::readonly&quot;</tt> from <font SIZE="-1">CPAN,</font> or use the double bracket: 

 
while (&lt;&lt; &gt;&gt;) {
    print;
}
 

 Using double angle brackets inside of a while causes the open to use the three argument form (with the second argument being <tt>&quot;&lt;&quot;</tt>), so all arguments in <tt>&quot;ARGV&quot;</tt> are treated as literal filenames (including <tt>&quot;-&quot;</tt>). (Note that for convenience, if you use <tt>&quot;&lt;&lt;&gt;&gt;&quot;</tt> and if <tt>@ARGV</tt> is empty, it will still read from the standard input.) 

 You can modify <tt>@ARGV</tt> before the first <tt>&quot;&lt;&gt;&quot;</tt> as long as the array ends up containing the list of filenames you really want. Line numbers (<tt>$.</tt>) continue as though the input were one big happy file. See the example in ``eof'' in perlfunc for how to reset line numbers on each file. 

 If you want to set <tt>@ARGV</tt> to your own list of files, go right ahead. This sets <tt>@ARGV</tt> to all plain text files if no <tt>@ARGV</tt> was given: 

 
@ARGV = grep{-f &amp;&amp; -T} glob('*') unless @ARGV;
 

 You can even set them to pipe commands. For example, this automatically filters compressed arguments through <b>gzip</b>: 

 <pre>
    @ARGV = map { /\.(gz|Z)$/ ? &quot;gzip -dc &lt; $_ |&quot; : $_ } @ARGV;
</pre> 

 If you want to pass switches into your script, you can use one of the <tt>&quot;Getopts&quot;</tt> modules or put a loop on the front like this: 

 
while ($_ = $ARGV[0], / ^- /) {
    shift;
    last if / ^--$ / ;
    if (/ ^-D(.*) /) {
        $debug = $1
    }
    if (/ ^-v /) {
        $verbose++
    }
#... #other switches
}
while (&lt;&gt;) {
#... #code for each line
}
 

 The <tt>&quot;&lt;&gt;&quot;</tt> symbol will return <tt>&quot;undef&quot;</tt> for end-of-file only once. If you call it again after this, it will assume you are processing another <tt>@ARGV</tt> list, and if you haven't set <tt>@ARGV</tt>, will read input from <font SIZE="-1">STDIN.</font> 

 If what the angle brackets contain is a simple scalar variable (for example, <tt>$foo</tt>), then that variable contains the name of the filehandle to input from, or its typeglob, or a reference to the same. For example: 

 <pre>
    $fh = \*STDIN;
    $line = &lt;$fh&gt;;
</pre> 

 If what's within the angle brackets is neither a filehandle nor a simple scalar variable containing a filehandle name, typeglob, or typeglob reference, it is interpreted as a filename pattern to be globbed, and either a list of filenames or the next filename in the list is returned, depending on context. This distinction is determined on syntactic grounds alone. That means <tt>&quot;&lt;$x&gt;&quot;</tt> is always a <tt>&quot;readline()&quot;</tt> from an indirect handle, but <tt>&quot;&lt;$hash{key}&gt;&quot;</tt> is always a <tt>&quot;glob()&quot;</tt>. That's because <tt>$x</tt> is a simple scalar variable, but <tt>$hash{key}</tt> is not---it's a hash element. Even <tt>&quot;&lt;$x &gt;&quot;</tt> (note the extra space) is treated as <tt>&quot;glob(&quot;$x &quot;)&quot;</tt>, not <tt>&quot;readline($x)&quot;</tt>. 

 One level of double-quote interpretation is done first, but you can't say <tt>&quot;&lt;$foo&gt;&quot;</tt> because that's an indirect filehandle as explained in the previous paragraph. (In older versions of Perl, programmers would insert curly brackets to force interpretation as a filename glob: <tt>&quot;&lt;${foo}&gt;&quot;</tt>. These days, it's considered cleaner to call the internal function directly as <tt>&quot;glob($foo)&quot;</tt>, which is probably the right way to have done it in the first place.) For example: 

 
while (&lt;*.c&gt;) {
    chmod 0644, $_;
}
 

 is roughly equivalent to: 

 
open(FOO, "echo *.c | tr -s ' \t\r\f' '\\012\\012\\012\\012'|");
while (&lt;FOO&gt;) {
    chomp;
    chmod 0644, $_;
}
 

 except that the globbing is actually done internally using the standard <tt>&quot;File::Glob&quot;</tt> extension. Of course, the shortest way to do the above is: 

 <pre>
    chmod 0644, &lt;*.c&gt;;
</pre> 

 A (file)glob evaluates its (embedded) argument only when it is starting a new list. All values must be read before it will start over. In list context, this isn't important because you automatically get them all anyway. However, in scalar context the operator returns the next value each time it's called, or <tt>&quot;undef&quot;</tt> when the list has run out. As with filehandle reads, an automatic <tt>&quot;defined&quot;</tt> is generated when the glob occurs in the test part of a <tt>&quot;while&quot;</tt>, because legal glob returns (for example, a file called <i>0</i>) would otherwise terminate the loop. Again, <tt>&quot;undef&quot;</tt> is returned only once. So if you're expecting a single value from a glob, it is much better to say 

 <pre>
    ($file) = &lt;blurch*&gt;;
</pre> 

 than 

 <pre>
    $file = &lt;blurch*&gt;;
</pre> 

 because the latter will alternate between returning a filename and returning false. 

 If you're trying to do variable interpolation, it's definitely better to use the <tt>&quot;glob()&quot;</tt> function, because the older notation can cause people to become confused with the indirect filehandle notation. 

 
@files = glob("$dir/*.[ch]");
@files = glob($files[$i]);
 

 If an angle-bracket-based globbing expression is used as the condition of a <tt>&quot;while&quot;</tt> or <tt>&quot;for&quot;</tt> loop, then it will be implicitly assigned to <tt>$_</tt>. If either a globbing expression or an explicit assignment of a globbing expression to a scalar is used as a <tt>&quot;while&quot;</tt>/<tt>&quot;for&quot;</tt> condition, then the condition actually tests for definedness of the expression's value, not for its regular truth value.

<h3>Constant Folding</h3>

 Like C, Perl does a certain amount of expression evaluation at compile time whenever it determines that all arguments to an operator are static and have no side effects. In particular, string concatenation happens at compile time between literals that don't do variable substitution. Backslash interpolation also happens at compile time. You can say 

 <pre>
      'Now is the time for all'
    . &quot;\n&quot;
    .  'good men to come to.'
</pre> 

 and this all reduces to one string internally. Likewise, if you say 

 
foreach
    $file(@filenames)
    {
        if (-s $file &gt; 5 + 100 * 2 * *16) {
        }
    }
 

 the compiler precomputes the number which that expression represents so that the interpreter won't have to.

<h3>No-ops</h3>

 Perl doesn't officially have a no-op operator, but the bare constants <tt>0</tt> and <tt>1</tt> are special-cased not to produce a warning in void context, so you can for example safely do 

 
1 while foo();


<h3>Bitwise String Operators</h3>

 Bitstrings of any size may be manipulated by the bitwise operators (<tt>&quot;~ | &amp; ^&quot;</tt>). 

 If the operands to a binary bitwise op are strings of different sizes, <b>|</b> and <b>^</b> ops act as though the shorter operand had additional zero bits on the right, while the <b>&amp;</b> op acts as though the longer operand were truncated to the length of the shorter. The granularity for such extension or truncation is one or more bytes. 

 
#ASCII - based examples
print "j p \n" ^ " a h";
#prints "JAPH\n" print "JA" | "  ph\n";
#prints "japh\n" print "japh\nJunk" &amp; '_____';
#prints "JAPH\n";
print 'p N$' ^ " E&lt;H\n";
#prints "Perl\n";
 

 If you are intending to manipulate bitstrings, be certain that you're supplying bitstrings: If an operand is a number, that will imply a <b>numeric</b> bitwise operation. You may explicitly show which type of operation you intend by using <tt>&quot;&quot;</tt> or <tt>&quot;0+&quot;</tt>, as in the examples below. 

 
$foo = 150 | 105;
#yields 255(0x96 | 0x69 is 0xFF)
    $foo = '150' | 105;
#yields 255 $foo = 150 | '105';
#yields 255 $foo = '150' | '105';
#yields string '155'(under ASCII)
    $baz = 0 + $foo &amp; 0 + $bar;
#both ops explicitly numeric
    $biz = "$foo" ^ "$bar";
#both ops explicitly stringy
 

 This somewhat unpredictable behavior can be avoided with the ``bitwise'' feature, new in Perl 5.22. You can enable it via <tt>&quot;use feature 'bitwise'&quot;</tt> or <tt>&quot;use v5.28&quot;</tt>. Before Perl 5.28, it used to emit a warning in the <tt>&quot;experimental::bitwise&quot;</tt> category. Under this feature, the four standard bitwise operators (<tt>&quot;~ | &amp; ^&quot;</tt>) are always numeric. Adding a dot after each operator (<tt>&quot;~. |. &amp;. ^.&quot;</tt>) forces it to treat its operands as strings: 

 
use feature "bitwise";
$foo = 150 | 105;
#yields 255(0x96 | 0x69 is 0xFF)
    $foo = '150' | 105;
#yields 255 $foo = 150 | '105';
#yields 255 $foo = '150' | '105';
#yields 255 $foo = 150 |.105;
#yields string '155' $foo = '150' |.105;
#yields string '155' $foo = 150 |.'105';
#yields string '155' $foo = '150' |.'105';
#yields string '155' $baz = $foo &amp; $bar;
#both operands numeric
    $biz = $foo ^.$bar;
#both operands stringy
 

 The assignment variants of these operators (<tt>&quot;&amp;= |= ^= &amp;.= |.= ^.=&quot;</tt>) behave likewise under the feature. 

 It is a fatal error if an operand contains a character whose ordinal value is above 0xFF, and hence not expressible except in <font SIZE="-1">UTF-8.</font> The operation is performed on a non-UTF-8 copy for other operands encoded in <font SIZE="-1">UTF-8.</font> See ``Byte and Character Semantics'' in perlunicode. 

 See ``vec'' in perlfunc for information on how to manipulate individual bits in a bit vector.

<h3>Integer Arithmetic</h3>

 By default, Perl assumes that it must do most of its arithmetic in floating point. But by saying 

 <pre>
    use integer;
</pre> 

 you may tell the compiler to use integer operations (see integer for a detailed explanation) from here to the end of the enclosing <font SIZE="-1">BLOCK.</font> An inner <font SIZE="-1">BLOCK</font> may countermand this by saying 

 <pre>
    no integer;
</pre> 

 which lasts until the end of that <font SIZE="-1">BLOCK.</font> Note that this doesn't mean everything is an integer, merely that Perl will use integer operations for arithmetic, comparison, and bitwise operators. For example, even under <tt>&quot;use integer&quot;</tt>, if you take the <tt><a HREF="/docs/linux/man/2-sqrt/">sqrt</a>(2)</tt>, you'll still get <tt>1.4142135623731</tt> or so. 

 Used on numbers, the bitwise operators (<tt>&quot;&amp;&quot;</tt> <tt>&quot;|&quot;</tt> <tt>&quot;^&quot;</tt> <tt>&quot;~&quot;</tt> <tt>&quot;&lt;&lt;&quot;</tt> <tt>&quot;&gt;&gt;&quot;</tt>) always produce integral results. (But see also ``Bitwise String Operators''.) However, <tt>&quot;use integer&quot;</tt> still has meaning for them. By default, their results are interpreted as unsigned integers, but if <tt>&quot;use integer&quot;</tt> is in effect, their results are interpreted as signed integers. For example, <tt>&quot;~0&quot;</tt> usually evaluates to a large integral value. However, <tt>&quot;use integer; ~0&quot;</tt> is <tt>&quot;-1&quot;</tt> on two's-complement machines.

<h3>Floating-point Arithmetic</h3>

 

 

 While <tt>&quot;use integer&quot;</tt> provides integer-only arithmetic, there is no analogous mechanism to provide automatic rounding or truncation to a certain number of decimal places. For rounding to a certain number of digits, <tt>&quot;sprintf()&quot;</tt> or <tt>&quot;printf()&quot;</tt> is usually the easiest route. See perlfaq4. 

 Floating-point numbers are only approximations to what a mathematician would call real numbers. There are infinitely more reals than floats, so some corners must be cut. For example: 

 <pre>
    printf &quot;%.20g\n&quot;, 123456789123456789;
    #        produces 123456789123456784
</pre> 

 Testing for exact floating-point equality or inequality is not a good idea. Here's a (relatively expensive) work-around to compare whether two floating-point numbers are equal to a particular number of decimal places. See Knuth, volume <font SIZE="-1">II,</font> for a more robust treatment of this topic. 

 
sub fp_equal
{
    my($X, $Y, $POINTS) = @_;
    my($tX, $tY);
    $tX = sprintf("%.${POINTS}g", $X);
    $tY = sprintf("%.${POINTS}g", $Y);
    return $tX eq $tY;
}
 

 The <font SIZE="-1">POSIX</font> module (part of the standard perl distribution) implements <tt>&quot;ceil()&quot;</tt>, <tt>&quot;floor()&quot;</tt>, and other mathematical and trigonometric functions. The <tt>&quot;Math::Complex&quot;</tt> module (part of the standard perl distribution) defines mathematical functions that work on both the reals and the imaginary numbers. <tt>&quot;Math::Complex&quot;</tt> is not as efficient as <font SIZE="-1">POSIX,</font> but <font SIZE="-1">POSIX</font> can't work with complex numbers. 

 Rounding in financial applications can have serious implications, and the rounding method used should be specified precisely. In these cases, it probably pays not to trust whichever system rounding is being used by Perl, but to instead implement the rounding function you need yourself.

<h3>Bigger Numbers</h3>

 The standard <tt>&quot;Math::BigInt&quot;</tt>, <tt>&quot;Math::BigRat&quot;</tt>, and <tt>&quot;Math::BigFloat&quot;</tt> modules, along with the <tt>&quot;bignum&quot;</tt>, <tt>&quot;bigint&quot;</tt>, and <tt>&quot;bigrat&quot;</tt> pragmas, provide variable-precision arithmetic and overloaded operators, although they're currently pretty slow. At the cost of some space and considerable speed, they avoid the normal pitfalls associated with limited-precision representations. 

 
use 5.010;
use bigint;
#easy interface to Math::BigInt
    $x = 123456789123456789;
say $x *$x;
+ 15241578780673678515622620750190521
 

 Or with rationals: 

 <pre><code>
use 5.010;
use bigrat;
$x = 3 / 22;
$y = 4 / 6;
say "x/y is ", $x / $y;
say "x*y is ", $x *$y;
x / y is 9 / 44 x *y is 1 / 11
</code></pre> 

 Several modules let you calculate with unlimited or fixed precision (bound only by memory and <font SIZE="-1">CPU</font> time). There are also some non-standard modules that provide faster implementations via external C libraries. 

 Here is a short, but incomplete summary: 

 <pre>
  Math::String           treat string sequences like numbers
  Math::FixedPrecision   calculate with a fixed precision
  Math::Currency         for currency calculations
  Bit::Vector            manipulate bit vectors fast (uses C)
  Math::BigIntFast       Bit::Vector wrapper for big numbers
  Math::Pari             provides access to the Pari C library
  Math::Cephes           uses the external Cephes C library (no
                         big numbers)
  Math::Cephes::Fraction fractions via the Cephes library
  Math::GMP              another one using an external C library
  Math::GMPz             an alternative interface to libgmp's big ints
  Math::GMPq             an interface to libgmp's fraction numbers
  Math::GMPf             an interface to libgmp's floating point numbers
</pre> 

 Choose wisely. 

<h2>Index</h2>



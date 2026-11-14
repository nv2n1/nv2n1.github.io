---
title: "bc(1)"
name: "bc"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bc/"
description: "bc – An arbitrary precision calculator language"
---

<h2 class="name">NAME</h2>
<p> bc &#8211; An arbitrary precision calculator language </p>
<h2>SYNTAX</h2>
<p> <code>bc</code> [ <code>-hlwsqv</code> ] [long-options] [ <i> file &#8230;</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>bc</code> is a language that supports arbitrary precision numbers with interactive execution of statements. There are some similarities in the syntax to the C programming language. A standard math library is available by command line option. If requested, the math library is defined before processing any files. <code>bc</code> starts by processing code from all the files listed on the command line in the order listed. After all files have been processed, <code>bc</code> reads from the standard input. All code is executed as it is read. (If a file contains a command to halt the processor, <code>bc</code> will never read from the standard input.) </p>
<p> This version of <code>bc</code> contains several extensions beyond traditional <code>bc</code> implementations and the POSIX draft standard. Command line options can cause these extensions to print a warning or to be rejected. This document describes the language accepted by this processor. Extensions will be identified as such.</p>
<h3>OPTIONS</h3>
<dl>
<dt>-h, &#8211;help</p>
<dd> Print the usage and exit.</p>
<dt>-i, &#8211;interactive</p>
<dd> Force interactive mode.</p>
<dt>-l, &#8211;mathlib</p>
<dd> Define the standard math library.</p>
<dt>-w, &#8211;warn</p>
<dd> Give warnings for extensions to POSIX <code>bc</code>.</p>
<dt>-s, &#8211;standard</p>
<dd> Process exactly the POSIX <code>bc</code> language.</p>
<dt>-q, &#8211;quiet</p>
<dd> Do not print the normal GNU bc welcome.</p>
<dt>-v, &#8211;version</p>
<dd> Print the version number and copyright and quit.</dl>
<h3>NUMBERS</h3>
<p> The most basic element in <code>bc</code> is the number. Numbers are arbitrary precision numbers. This precision is both in the integer part and the fractional part. All numbers are represented internally in decimal and all computation is done in decimal. (This version truncates results from divide and multiply operations.) There are two attributes of numbers, the length and the scale. The length is the total number of decimal digits used by <code>bc</code> to represent a number and the scale is the total number of decimal digits after the decimal point. For example: </p>
<pre>
<dl><dt><dd> .000001 has a length of 6 and scale of 6.
 1935.000 has a length of 7 and a scale of 3.
</dl>
</pre>
<h3>VARIABLES</h3>
<p> Numbers are stored in two types of variables, simple variables and arrays. Both simple variables and array variables are named. Names begin with a letter followed by any number of letters, digits and underscores. All letters must be lower case. (Full alpha-numeric names are an extension. In POSIX <code>bc</code> all names are a single lower case letter.) The type of variable is clear by the context because all array variable names will be followed by brackets ([]). </p>
<p> There are four special variables, <code>scale, ibase, obase,</code> and <code>last</code>. <code>scale</code> defines how some operations use digits after the decimal point. The default value of <code>scale</code> is 0. <code>ibase</code> and <code>obase</code> define the conversion base for input and output numbers. The default for both input and output is base 10. <code>last</code> (an extension) is a variable that has the value of the last printed number. These will be discussed in further detail where appropriate. All of these variables may have values assigned to them as well as used in expressions.</p>
<h3>COMMENTS</h3>
<p> Comments in <code>bc</code> start with the characters <code>/*</code> and end with the characters <code>*/</code>. Comments may start anywhere and appear as a single space in the input. (This causes comments to delimit other input items. For example, a comment can not be found in the middle of a variable name.) Comments include any newlines (end of line) between the start and the end of the comment. </p>
<p> To support the use of scripts for <code>bc</code>, a single line comment has been added as an extension. A single line comment starts at a <code>#</code> character and continues to the next end of the line. The end of line character is not part of the comment and is processed normally.</p>
<h3>EXPRESSIONS</h3>
<p> The numbers are manipulated by expressions and statements. Since the language was designed to be interactive, statements and expressions are executed as soon as possible. There is no &quot;main&quot; program. Instead, code is executed as it is encountered. (Functions, discussed in detail later, are defined when encountered.) </p>
<p> A simple expression is just a constant. <code>bc</code> converts constants into internal decimal numbers using the current input base, specified by the variable <code>ibase</code>. (There is an exception in functions.) The legal values of <code>ibase</code> are 2 through 36. (Bases greater than 16 are an extension.) Assigning a value outside this range to <code>ibase</code> will result in a value of 2 or 36. Input numbers may contain the characters 0-9 and A-Z. (Note: They must be capitals. Lower case letters are variable names.) Single digit numbers always have the value of the digit regardless of the value of <code>ibase</code>. (i.e. A = 10.) For multi-digit numbers, <code>bc</code> changes all input digits greater or equal to ibase to the value of <code>ibase</code>-1. This makes the number <code>ZZZ</code> always be the largest 3 digit number of the input base. </p>
<p> Full expressions are similar to many other high level languages. Since there is only one kind of number, there are no rules for mixing types. Instead, there are rules on the scale of expressions. Every expression has a scale. This is derived from the scale of original numbers, the operation performed and in many cases, the value of the variable <code>scale</code>. Legal values of the variable <code>scale</code> are 0 to the maximum number representable by a C integer. </p>
<p> In the following descriptions of legal expressions, &quot;expr&quot; refers to a complete expression and &quot;var&quot; refers to a simple or an array variable. A simple variable is just a</p>
<dl>
<dt>
<dd> <i>name</i></dl>
<p> and an array variable is specified as</p>
<dl>
<dt>
<dd> <i>name</i>[<i>expr</i>]</dl>
<p> Unless specifically mentioned the scale of the result is the maximum scale of the expressions involved.</p>
<dl>
<dt>&#8211; expr</p>
<dd> The result is the negation of the expression.</p>
<dt>++ var</p>
<dd> The variable is incremented by one and the new value is the result of the expression.</p>
<dt>&#8212; var</p>
<dd> The variable is decremented by one and the new value is the result of the expression.</p>
<dt>var ++</p>
<dd>
&nbsp;The result of the expression is the value of the variable and then the variable is incremented by one.</p>
<dt>var &#8212;</p>
<dd> The result of the expression is the value of the variable and then the variable is decremented by one.</p>
<dt>expr + expr</p>
<dd> The result of the expression is the sum of the two expressions.</p>
<dt>expr &#8211; expr</p>
<dd> The result of the expression is the difference of the two expressions.</p>
<dt>expr * expr</p>
<dd> The result of the expression is the product of the two expressions.</p>
<dt>expr / expr</p>
<dd> The result of the expression is the quotient of the two expressions. The scale of the result is the value of the variable <code>scale</code>.</p>
<dt>expr % expr</p>
<dd> The result of the expression is the &quot;remainder&quot; and it is computed in the following way. To compute a%b, first a/b is computed to <code>scale</code> digits. That result is used to compute a-(a/b)*b to the scale of the maximum of <code>scale</code>+scale(b) and scale(a). If <code>scale</code> is set to zero and both expressions are integers this expression is the integer remainder function.</p>
<dt>expr ^ expr</p>
<dd> The result of the expression is the value of the first raised to the second. The second expression must be an integer. (If the second expression is not an integer, a warning is generated and the expression is truncated to get an integer value.) The scale of the result is <code>scale</code> if the exponent is negative. If the exponent is positive the scale of the result is the minimum of the scale of the first expression times the value of the exponent and the maximum of <code>scale</code> and the scale of the first expression. (e.g. scale(a^b) = min(scale(a)*b, max( <code>scale,</code> scale(a))).) It should be noted that expr^0 will always return the value of 1.</p>
<dt>( expr )</p>
<dd> This alters the standard precedence to force the evaluation of the expression.</p>
<dt>var = expr</p>
<dd> The variable is assigned the value of the expression.</p>
<dt>var &lt;op&gt;= expr</p>
<dd> This is equivalent to &quot;var = var &lt;op&gt; expr&quot; with the exception that the &quot;var&quot; part is evaluated only once. This can make a difference if &quot;var&quot; is an array.</dl>
<p> Relational expressions are a special kind of expression that always evaluate to 0 or 1, 0 if the relation is false and 1 if the relation is true. These may appear in any legal expression. (POSIX bc requires that relational expressions are used only in if, while, and for statements and that only one relational test may be done in them.) The relational operators are</p>
<dl>
<dt>expr1 &lt; expr2</p>
<dd> The result is 1 if expr1 is strictly less than expr2.</p>
<dt>expr1 &lt;= expr2</p>
<dd> The result is 1 if expr1 is less than or equal to expr2.</p>
<dt>expr1 &gt; expr2</p>
<dd> The result is 1 if expr1 is strictly greater than expr2.</p>
<dt>expr1 &gt;= expr2</p>
<dd> The result is 1 if expr1 is greater than or equal to expr2.</p>
<dt>expr1 == expr2</p>
<dd> The result is 1 if expr1 is equal to expr2.</p>
<dt>expr1 != expr2</p>
<dd> The result is 1 if expr1 is not equal to expr2.</dl>
<p> Boolean operations are also legal. (POSIX <code>bc</code> does NOT have boolean operations). The result of all boolean operations are 0 and 1 (for false and true) as in relational expressions. The boolean operators are:</p>
<dl>
<dt>!expr</p>
<dd> The result is 1 if expr is 0.</p>
<dt>expr &amp;&amp; expr</p>
<dd> The result is 1 if both expressions are non-zero.</p>
<dt>expr || expr</p>
<dd> The result is 1 if either expression is non-zero.</dl>
<p> The expression precedence is as follows: (lowest to highest) </p>
<pre><code>
|| operator, left associative &amp;&amp; operator, left associative !operator, nonassociative
    Relational operators,
    left associative
        Assignment
        operator,
    right associative + and - operators, left associative *, / and % operators, left associative ^ operator, right associative
                                                                                    unary -
                                                                                    operator,
    nonassociative++ and -- operators, nonassociative
</code></pre>
<p> This precedence was chosen so that POSIX compliant <code>bc</code> programs will run correctly. This will cause the use of the relational and logical operators to have some unusual behavior when used with assignment expressions. Consider the expression:</p>
<dl>
<dt>
<dd> a = 3 &lt; 5</dl>
<p> Most C programmers would assume this would assign the result of &quot;3 &lt; 5&quot; (the value 1) to the variable &quot;a&quot;. What this does in <code>bc</code> is assign the value 3 to the variable &quot;a&quot; and then compare 3 to 5. It is best to use parenthesis when using relational and logical operators with the assignment operators. </p>
<p> There are a few more special expressions that are provided in <code>bc</code>. These have to do with user defined functions and standard functions. They all appear as &quot;,<i>name/</i><code>(,</code><i>parameters/</i><code>)</code>&quot;. See the section on functions for user defined functions. The standard functions are:</p>
<dl>
<dt>length ( expression )</p>
<dd> The value of the length function is the number of significant digits in the expression.</p>
<dt>read ( )</p>
<dd> The read function (an extension) will read a number from the standard input, regardless of where the function occurs. Beware, this can cause problems with the mixing of data and program in the standard input. The best use for this function is in a previously written program that needs input from the user, but never allows program code to be input from the user. The value of the read function is the number read from the standard input using the current value of the variable <code>ibase</code> for the conversion base.</p>
<dt>scale ( expression )</p>
<dd> The value of the scale function is the number of digits after the decimal point in the expression.</p>
<dt>sqrt ( expression )</p>
<dd> The value of the sqrt function is the square root of the expression. If the expression is negative, a run time error is generated.</dl>
<h3>STATEMENTS</h3>
<p> Statements (as in most algebraic languages) provide the sequencing of expression evaluation. In <code>bc</code> statements are executed &quot;as soon as possible.&quot; Execution happens when a newline in encountered and there is one or more complete statements. Due to this immediate execution, newlines are very important in <code>bc</code>. In fact, both a semicolon and a newline are used as statement separators. An improperly placed newline will cause a syntax error. Because newlines are statement separators, it is possible to hide a newline by using the backslash character. The sequence &quot;\&lt;nl&gt;&quot;, where &lt;nl&gt; is the newline appears to <code>bc</code> as whitespace instead of a newline. A statement list is a series of statements separated by semicolons and newlines. The following is a list of <code>bc</code> statements and what they do: (Things enclosed in brackets ([]) are optional parts of the statement.)</p>
<dl>
<dt>expression</p>
<dd> This statement does one of two things. If the expression starts with &quot;&lt;variable&gt; &lt;assignment&gt; &#8230;&quot;, it is considered to be an assignment statement. If the expression is not an assignment statement, the expression is evaluated and printed to the output. After the number is printed, a newline is printed. For example, &quot;a=1&quot; is an assignment statement and &quot;(a=1)&quot; is an expression that has an embedded assignment. All numbers that are printed are printed in the base specified by the variable <code>obase</code>. The legal values for <code> obase</code> are 2 through BC_BASE_MAX. (See the section LIMITS.) For bases 2 through 16, the usual method of writing numbers is used. For bases greater than 16, <code>bc</code> uses a multi-character digit method of printing the numbers where each higher base digit is printed as a base 10 number. The multi-character digits are separated by spaces. Each digit contains the number of characters required to represent the base ten value of &quot;obase-1&quot;. Since numbers are of arbitrary precision, some numbers may not be printable on a single output line. These long numbers will be split across lines using the &quot;\&quot; as the last character on a line. The maximum number of characters printed per line is 70. Due to the interactive nature of <code>bc</code>, printing a number causes the side effect of assigning the printed value to the special variable <code>last</code>. This allows the user to recover the last value printed without having to retype the expression that printed the number. Assigning to <code>last</code> is legal and will overwrite the last printed value with the assigned value. The newly assigned value will remain until the next number is printed or another value is assigned to <code>last</code>. (Some installations may allow the use of a single period (.) which is not part of a number as a short hand notation for for <code>last</code>.)</p>
<dt>string</p>
<dd> The string is printed to the output. Strings start with a double quote character and contain all characters until the next double quote character. All characters are take literally, including any newline. No newline character is printed after the string.</p>
<dt><code>print</code> list</p>
<dd> The print statement (an extension) provides another method of output. The &quot;list&quot; is a list of strings and expressions separated by commas. Each string or expression is printed in the order of the list. No terminating newline is printed. Expressions are evaluated and their value is printed and assigned to the variable <code>last</code>. Strings in the print statement are printed to the output and may contain special characters. Special characters start with the backslash character (\). The special characters recognized by <code>bc</code> are &quot;a&quot; (alert or bell), &quot;b&quot; (backspace), &quot;f&quot; (form feed), &quot;n&quot; (newline), &quot;r&quot; (carriage return), &quot;q&quot; (double quote), &quot;t&quot; (tab), and &quot;\&quot; (backslash). Any other character following the backslash will be ignored.</p>
<dt>{ statement_list }</p>
<dd> This is the compound statement. It allows multiple statements to be grouped together for execution.</p>
<dt><code>if</code> ( expression ) statement1 [<code>else</code> statement2]</p>
<dd> The if statement evaluates the expression and executes statement1 or statement2 depending on the value of the expression. If the expression is non-zero, statement1 is executed. If statement2 is present and the value of the expression is 0, then statement2 is executed. (The else clause is an extension.)</p>
<dt><code>while</code> ( expression ) statement</p>
<dd> The while statement will execute the statement while the expression is non-zero. It evaluates the expression before each execution of the statement. Termination of the loop is caused by a zero expression value or the execution of a break statement.</p>
<dt><code>for</code> ( [expression1] ; [expression2] ; [expression3] ) statement</p>
<dd> The for statement controls repeated execution of the statement. Expression1 is evaluated before the loop. Expression2 is evaluated before each execution of the statement. If it is non-zero, the statement is evaluated. If it is zero, the loop is terminated. After each execution of the statement, expression3 is evaluated before the reevaluation of expression2. If expression1 or expression3 are missing, nothing is evaluated at the point they would be evaluated. If expression2 is missing, it is the same as substituting the value 1 for expression2. (The optional expressions are an extension. POSIX <code>bc</code> requires all three expressions.) The following is equivalent code for the for statement:<br />
expression1;<br />
while (expression2) {<br />
    statement;<br />
    expression3;<br />
}</p>
<dt><code>break</code></p>
<dd> This statement causes a forced exit of the most recent enclosing while statement or for statement.</p>
<dt><code>continue</code></p>
<dd> The continue statement (an extension) causes the most recent enclosing for statement to start the next iteration.</p>
<dt><code>halt</code></p>
<dd> The halt statement (an extension) is an executed statement that causes the <code>bc</code> processor to quit only when it is executed. For example, &quot;if (0 == 1) halt&quot; will not cause <code>bc</code> to terminate because the halt is not executed.</p>
<dt><code>return</code></p>
<dd> Return the value 0 from a function. (See the section on functions.)</p>
<dt><code>return</code> ( expression )</p>
<dd> Return the value of the expression from a function. (See the section on functions.) As an extension, the parenthesis are not required.</dl>
<h3>PSEUDO STATEMENTS</h3>
<p> These statements are not statements in the traditional sense. They are not executed statements. Their function is performed at &quot;compile&quot; time.</p>
<dl>
<dt><code>limits</code></p>
<dd> Print the local limits enforced by the local version of <code>bc</code>. This is an extension.</p>
<dt><code>quit</code></p>
<dd> When the quit statement is read, the <code>bc</code> processor is terminated, regardless of where the quit statement is found. For example, &quot;if (0 == 1) quit&quot; will cause <code>bc</code> to terminate.</p>
<dt><code>warranty</code></p>
<dd> Print a longer warranty notice. This is an extension.</dl>
<h3>FUNCTIONS</h3>
<p> Functions provide a method of defining a computation that can be executed later. Functions in <code>bc</code> always compute a value and return it to the caller. Function definitions are &quot;dynamic&quot; in the sense that a function is undefined until a definition is encountered in the input. That definition is then used until another definition function for the same name is encountered. The new definition then replaces the older definition. A function is defined as follows: </p>
<pre>
<dl><dt><dd><code>define </code><i>name </i><code>( </code><i>parameters </i><code>) { </code><i>newline
    auto_list   statement_list </i><code>}</code>
</dl>
</pre>
<p> A function call is just an expression of the form &quot;,<i>name/</i><code>(,</code><i>parameters/</i><code>)</code>&quot;. </p>
<p> Parameters are numbers or arrays (an extension). In the function definition, zero or more parameters are defined by listing their names separated by commas. All parameters are call by value parameters. Arrays are specified in the parameter definition by the notation &quot;,<i>name/</i><code>[]</code>&quot;. In the function call, actual parameters are full expressions for number parameters. The same notation is used for passing arrays as for defining array parameters. The named array is passed by value to the function. Since function definitions are dynamic, parameter numbers and types are checked when a function is called. Any mismatch in number or types of parameters will cause a runtime error. A runtime error will also occur for the call to an undefined function. </p>
<p> The <i>auto_list</i> is an optional list of variables that are for &quot;local&quot; use. The syntax of the auto list (if present) is &quot;<code>auto </code><i>name</i>, &#8230; ;&quot;. (The semicolon is optional.) Each <i>name</i> is the name of an auto variable. Arrays may be specified by using the same notation as used in parameters. These variables have their values pushed onto a stack at the start of the function. The variables are then initialized to zero and used throughout the execution of the function. At function exit, these variables are popped so that the original value (at the time of the function call) of these variables are restored. The parameters are really auto variables that are initialized to a value provided in the function call. Auto variables are different than traditional local variables because if function A calls function B, B may access function A&#8217;s auto variables by just using the same name, unless function B has called them auto variables. Due to the fact that auto variables and parameters are pushed onto a stack, <code>bc</code> supports recursive functions. </p>
<p> The function body is a list of <code>bc</code> statements. Again, statements are separated by semicolons or newlines. Return statements cause the termination of a function and the return of a value. There are two versions of the return statement. The first form, &quot;<code>return</code>&quot;, returns the value 0 to the calling expression. The second form, &quot;<code>return ( </code><i>expression </i><code>)</code>&quot;, computes the value of the expression and returns that value to the calling expression. There is an implied &quot;<code>return (0)</code>&quot; at the end of every function. This allows a function to terminate and return 0 without an explicit return statement. </p>
<p> Functions also change the usage of the variable <code>ibase</code>. All constants in the function body will be converted using the value of <code>ibase</code> at the time of the function call. Changes of <code>ibase</code> will be ignored during the execution of the function except for the standard function <code>read</code>, which will always use the current value of <code>ibase</code> for conversion of numbers. </p>
<p> Several extensions have been added to functions. First, the format of the definition has been slightly relaxed. The standard requires the opening brace be on the same line as the <code>define</code> keyword and all other parts must be on following lines. This version of <code>bc</code> will allow any number of newlines before and after the opening brace of the function. For example, the following definitions are legal. </p>
<p>define d(n)<br />
{<br />
    return (2 * n);<br />
}<br />
define d(n)<br />
{<br />
    return (2 * n);<br />
}</p>
<p> Functions may be defined as <code>void</code>. A void function returns no value and thus may not be used in any place that needs a value. A void function does not produce any output when called by itself on an input line. The key word <code>void</code> is placed between the key word <code>define</code> and the function name. For example, consider the following session. </p>
<p>define py(y)<br />
{<br />
    print &#8220;&#8212;&gt;&#8221;, y, &#8220;&lt;&#8212;&#8220;, &#8220;
&#8221;;<br />
}<br />
define void px(x)<br />
{<br />
    print &#8220;&#8212;&gt;&#8221;, x, &#8220;&lt;&#8212;&#8220;, &#8220;
&#8221;;<br />
}<br />
py(1)&#8212;&gt;1 &lt; &#8212; -0 px(1)&#8212;&gt;1 &lt; &#8212; &#8211;<br />
 Since <code>py</code> is not a void function, the call of <code><a href="/docs/linux/man/1-py/">py</a>(1)</code> prints the desired output and then prints a second line that is the value of the function. Since the value of a function that is not given an explicit return statement is zero, the zero is printed. For <code><a href="/docs/linux/man/1-px/">px</a>(1)</code>, no zero is printed because the function is a void function. </p>
<p> Also, call by variable for arrays was added. To declare a call by variable array, the declaration of the array parameter in the function definition looks like &quot;,<i>*name/</i><code>[]</code>&quot;. The call to the function remains the same as call by value arrays.</p>
<h3>MATH LIBRARY</h3>
<p> If <code>bc</code> is invoked with the <code>-l</code> option, a math library is preloaded and the default scale is set to 20. The math functions will calculate their results to the scale set at the time of their call. The math library defines the following functions:</p>
<dl>
<dt>s (,<i>x/</i>)</p>
<dd> The sine of x, x is in radians.</p>
<dt>c (,<i>x/</i>)</p>
<dd> The cosine of x, x is in radians.</p>
<dt>a (,<i>x/</i>)</p>
<dd> The arctangent of x, arctangent returns radians.</p>
<dt>l (,<i>x/</i>)</p>
<dd> The natural logarithm of x.</p>
<dt>e (,<i>x/</i>)</p>
<dd> The exponential function of raising e to the value x.</p>
<dt>j (,<i>n,x/</i>)</p>
<dd> The Bessel function of integer order n of x.</dl>
<h3>EXAMPLES</h3>
<p> In /bin/sh, the following will assign the value of &quot;pi&quot; to the shell variable <code>pi</code>.</p>
<dl>
<dt>
<dd> <tt> pi=$(echo &quot;scale=10; 4*<a href="/docs/linux/man/1-a/">a</a>(1)&quot; | bc -l) </tt></dl>
<p> The following is the definition of the exponential function used in the math library. This function is written in POSIX <code>bc</code>. </p>
<p>scale = 20<br />
    /* Uses the fact that e^x = (e^(x/2))^2<br />
       When x is small enough, we use the series:<br />
         e^x = 1 + x + x^2/2! + x^3/3! + &#8230;<br />
    */<br />
    define<br />
    e(x)<br />
{<br />
    auto a, d, e, f, i, m, v, z<br />
                              /* Check the sign of x. */<br />
                              if (x &lt; 0){m = 1 x = -x} /* Precondition x. */<br />
                              z = scale;<br />
    scale = 4 + z + .44 * x;<br />
    while (x &gt; 1) {<br />
        f += 1;<br />
        x /= 2;<br />
    }<br />
    /* Initialize the variables. */<br />
    v = 1 + x<br />
                a = x<br />
            d = 1 for (i = 2; 1; i++)<br />
    {<br />
        e = (a *= x) / (d *= i) if (e == 0)<br />
        {<br />
            if (f &gt; 0)<br />
                while (f&#8211;)<br />
                    v = v * v;<br />
            scale = z if (m) return (1 / v);<br />
            return (v / 1);<br />
        }<br />
        v += e<br />
    }<br />
}</p>
<p> The following is code that uses the extended features of <code>bc</code> to implement a simple program for calculating checkbook balances. This program is best kept in a file so that it can be used many times without having to retype it at every use. </p>
<p>scale = 2 print &#8220;
Check book program!
&#8221; print &#8221;  Remember, deposits are negative transactions.
&#8221; print &#8221;  Exit by a 0 transaction.

&#8221; print &#8220;Initial balance? &#8220;;<br />
bal = read()<br />
    bal /= 1 print &#8220;
&#8221; while (1)<br />
{<br />
    &#8220;current balance = &#8220;;<br />
    bal<br />
        &#8220;transaction? &#8220;;<br />
    trans = read() if (trans == 0) break;<br />
    bal -= trans<br />
        bal /= 1<br />
}<br />
quit</p>
<p> The following is the definition of the recursive factorial function. </p>
<pre><code>

define f(x)
{
    if (x &lt;= 1)
        return (1);
    return (f(x - 1) * x);
}
</code></pre>
<h3>READLINE AND LIBEDIT OPTIONS</h3>
<p> GNU <code>bc</code> can be compiled (via a configure option) to use the GNU <code>readline</code> input editor library or the BSD <code>libedit</code> library. This allows the user to do editing of lines before sending them to <code>bc</code>. It also allows for a history of previous lines typed. When this option is selected, <code>bc</code> has one more special variable. This special variable, <code>history</code> is the number of lines of history retained. For <code>readline</code>, a value of -1 means that an unlimited number of history lines are retained. Setting the value of <code>history</code> to a positive number restricts the number of history lines to the number given. The value of 0 disables the history feature. The default value is 100. For more information, read the user manuals for the GNU <code>readline</code>, <code>history</code> and BSD <code>libedit</code> libraries. One can not enable both <code>readline</code> and <code>libedit</code> at the same time.</p>
<h3>DIFFERENCES</h3>
<p> This version of <code>bc</code> was implemented from the POSIX P1003.2/D11 draft and contains several differences and extensions relative to the draft and traditional implementations. It is not implemented in the traditional way using <i><a href="/docs/linux/man/1-dc/">dc</a>(1).</i> This version is a single process which parses and runs a byte code translation of the program. There is an &quot;undocumented&quot; option (-c) that causes the program to output the byte code to the standard output instead of running it. It was mainly used for debugging the parser and preparing the math library. </p>
<p> A major source of differences is extensions, where a feature is extended to add more functionality and additions, where new features are added. The following is the list of differences and extensions.</p>
<dl>
<dt>LANG environment</p>
<dd> This version does not conform to the POSIX standard in the processing of the LANG environment variable and all environment variables starting with LC_.</p>
<dt>names</p>
<dd> Traditional and POSIX <code>bc</code> have single letter names for functions, variables and arrays. They have been extended to be multi-character names that start with a letter and may contain letters, numbers and the underscore character.</p>
<dt>Strings</p>
<dd> Strings are not allowed to contain NUL characters. POSIX says all characters must be included in strings.</p>
<dt>last</p>
<dd> POSIX <code>bc</code> does not have a <code>last</code> variable. Some implementations of <code>bc</code> use the period (.) in a similar way.</p>
<dt>comparisons</p>
<dd> POSIX <code>bc</code> allows comparisons only in the if statement, the while statement, and the second expression of the for statement. Also, only one relational operation is allowed in each of those statements.</p>
<dt>if statement, else clause</p>
<dd> POSIX <code>bc</code> does not have an else clause.</p>
<dt>for statement</p>
<dd> POSIX <code>bc</code> requires all expressions to be present in the for statement.</p>
<dt>&amp;&amp;, ||, !</p>
<dd> POSIX <code>bc</code> does not have the logical operators.</p>
<dt>read function</p>
<dd> POSIX <code>bc</code> does not have a read function.</p>
<dt>print statement</p>
<dd> POSIX <code>bc</code> does not have a print statement.</p>
<dt>continue statement</p>
<dd> POSIX <code>bc</code> does not have a continue statement.</p>
<dt>return statement</p>
<dd> POSIX <code>bc</code> requires parentheses around the return expression.</p>
<dt>array parameters</p>
<dd> POSIX <code>bc</code> does not (currently) support array parameters in full. The POSIX grammar allows for arrays in function definitions, but does not provide a method to specify an array as an actual parameter. (This is most likely an oversight in the grammar.) Traditional implementations of <code>bc</code> have only call by value array parameters.</p>
<dt>function format</p>
<dd> POSIX <code>bc</code> requires the opening brace on the same line as the <code>define</code> key word and the <code>auto</code> statement on the next line.</p>
<dt>=+, =-, =*, =/, =%, =^</p>
<dd> POSIX <code>bc</code> does not require these &quot;old style&quot; assignment operators to be defined. This version may allow these &quot;old style&quot; assignments. Use the limits statement to see if the installed version supports them. If it does support the &quot;old style&quot; assignment operators, the statement &quot;a =- 1&quot; will decrement <code>a</code> by 1 instead of setting <code>a</code> to the value -1.</p>
<dt>spaces in numbers</p>
<dd> Other implementations of <code>bc</code> allow spaces in numbers. For example, &quot;x=1 3&quot; would assign the value 13 to the variable x. The same statement would cause a syntax error in this version of <code>bc</code>.</p>
<dt>errors and execution</p>
<dd> This implementation varies from other implementations in terms of what code will be executed when syntax and other errors are found in the program. If a syntax error is found in a function definition, error recovery tries to find the beginning of a statement and continue to parse the function. Once a syntax error is found in the function, the function will not be callable and becomes undefined. Syntax errors in the interactive execution code will invalidate the current execution block. The execution block is terminated by an end of line that appears after a complete sequence of statements. For example, </p>
<pre>
<dl><dt><dd>a = 1
b = 2
</dl>
</pre>
<p> has two execution blocks and </p>
<pre>
<dl><dt><dd>{ a = 1
  b = 2 }
</dl>
</pre>
<p> has one execution block. Any runtime error will terminate the execution of the current execution block. A runtime warning will not terminate the current execution block.</p>
<dt>Interrupts</p>
<dd> During an interactive session, the SIGINT signal (usually generated by the control-C character from the terminal) will cause execution of the current execution block to be interrupted. It will display a &quot;runtime&quot; error indicating which function was interrupted. After all runtime structures have been cleaned up, a message will be printed to notify the user that <code>bc</code> is ready for more input. All previously defined functions remain defined and the value of all non-auto variables are the value at the point of interruption. All auto variables and function parameters are removed during the clean up process. During a non-interactive session, the SIGINT signal will terminate the entire run of <code>bc</code>.</dl>
<h3>LIMITS</h3>
<p> The following are the limits currently in place for this <code>bc</code> processor. Some of them may have been changed by an installation. Use the limits statement to see the actual values.</p>
<dl>
<dt>BC_BASE_MAX</p>
<dd> The maximum output base is currently set at 999. The maximum input base is 16.</p>
<dt>BC_DIM_MAX</p>
<dd> This is currently an arbitrary limit of 65535 as distributed. Your installation may be different.</p>
<dt>BC_SCALE_MAX</p>
<dd> The number of digits after the decimal point is limited to INT_MAX digits. Also, the number of digits before the decimal point is limited to INT_MAX digits.</p>
<dt>BC_STRING_MAX</p>
<dd> The limit on the number of characters in a string is INT_MAX characters.</p>
<dt>exponent</p>
<dd> The value of the exponent in the raise operation (^) is limited to LONG_MAX.</p>
<dt>variable names</p>
<dd> The current limit on the number of unique names is 32767 for each of simple variables, arrays and functions.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The following environment variables are processed by <code>bc</code>:</p>
<dl>
<dt>POSIXLY_CORRECT</p>
<dd> This is the same as the <code>-s</code> option.</p>
<dt>BC_ENV_ARGS</p>
<dd> This is another mechanism to get arguments to <code>bc</code>. The format is the same as the command line arguments. These arguments are processed first, so any files listed in the environment arguments are processed before any command line argument files. This allows the user to set up &quot;standard&quot; options and files to be processed at every invocation of <code>bc</code>. The files in the environment variables would typically contain function definitions for functions the user wants defined every time <code>bc</code> is run.</p>
<dt>BC_LINE_LENGTH</p>
<dd> This should be an integer specifying the number of characters in an output line for numbers. This includes the backslash and newline characters for long numbers. As an extension, the value of zero disables the multi-line feature. Any other value of this variable that is less than 3 sets the line length to 70.</dl>
<h2>DIAGNOSTICS</h2>
<p> If any file on the command line can not be opened, <code>bc</code> will report that the file is unavailable and terminate. Also, there are compile and run time diagnostics that should be self-explanatory.</p>
<h2>BUGS</h2>
<p> Error recovery is not very good yet. </p>
<p> Email bug reports to <code>bug-bc [at] gnu.org</code>. Be sure to include the word &#8220;bc&#8221; somewhere in the &#8220;Subject:&#8221; field.</p>
<h2>AUTHOR</h2>
<pre>
Philip A. Nelson
philnelson [at] acm.org
</pre>
<h2>ACKNOWLEDGEMENTS</h2>
<p> The author would like to thank Steve Sommars (Steve.Sommars [at] att.com) for his extensive help in testing the implementation. Many great suggestions were given. This is a much better product due to his involvement. </p>
<h2>Index</h2>

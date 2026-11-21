---
title: "nickle(1)"
name: "nickle"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nickle/"
description: "nickle – a desk calculator language"
---

<h2>SYNOPSIS</h2>
<p> nickle [&#8211;help|&#8211;usage] [-f file] [-l library] [-e expr] [ script ] [&#8211;] [arg &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <i>Nickle</i> is a desk calculator language with powerful programming and scripting capabilities. Nickle supports a variety of datatypes, especially arbitrary precision integers, rationals, and imprecise reals. The input language vaguely resembles C. Some things in C which do not translate easily are different, some design choices have been made differently, and a very few features are simply missing.</p>
<h2>USAGE</h2>
<p> An un-flagged argument is treated as a Nickle script, and replaces standard input. Any remaining arguments following the script are placed in the Nickle string array argv for programmatic inspection. When invoked without an expression or script argument, Nickle reads from standard input, and writes to standard output. </p>
<p> Options are as follows:</p>
<dl>
<dt><code>&#8211;help,&#8211;usage</code></dt>
<dd> Print a help/usage message and exit. This is a built-in feature of Nickle&#8217;s ParseArgs module, and thus will also be true of Nickle scripts that use this library.</dd>
<dt><code>-f,&#8211;file </code><i>file</i></dt>
<dd> Load <i>file</i> into Nickle before beginning execution.</dd>
<dt><code>-l,&#8211;library </code><i>library</i></dt>
<dd> Load <i>library</i> into Nickle before beginning execution. See below for a description of the library facility.</dd>
<dt><code>-e,&#8211;expr </code><i>expr</i></dt>
<dd> Evaluate <i>expr</i> before beginning execution.</dd>
<dt><code>&#8212;</code></dt>
<dd> Quit parsing arguments and pass the remainder, unevaluated, to <i>argv</i>.</dd></dl>
<h2>SYNTAX</h2>
<p> To make the input language more useful in an interactive setting, <code>newline</code> only terminates statements at &#8220;reasonable&#8221; times. <code>Newline</code> terminates either expressions or single statements typed by the user (with the exception of a few statements which require lookahead: notably if() and twixt(), which have an optional else part). Inside compound statements or function definitions, only a <code>;</code> terminates statements. This approach is convenient and does not appear to cause problems in normal use. </p>
<p> The syntax of Nickle programs is as follows. In this description, <code>name</code> denotes any sequence of letters, digits and _ characters not starting with a digit; <code>E</code> denotes any expression; <code>S</code> denotes any statement; and <code>T</code> denotes any type. The syntax <code>X,X,&#8230;,X</code> denotes one or more comma-separated Xs, unless otherwise indicated. </p>
<p> <code>Comments:</code> </p>
<p> C-style comments are enclosed in /* and */, and shell-style comments are denoted by a leading # at the start of a line. </p>
<p> <code>Operands:</code></p>
<dl>
<dt>real number</dt>
<dd> Can include exponent, need not include decimal point or sign. Will be treated as exact rationals. If a trailing decimal part contains an opening curly brace, the brace is silently ignored; if it contains a curly-bracketed trailing portion, it is treated as a repeating decimal. `Floating point&#8221; constants are currently represented internally as rationals: for floating constants with a given precision (and an infinite-precision exponent), use the imprecise() builtin function described below.</dd>
<dt>octal number</dt>
<dd> Start with a 0 (e.g., 014 is the same as 12).</dd>
<dt>hexidecimal number</dt>
<dd> Start with &quot;0x&quot; (e.g., 0x1a is the same as 26).</dd>
<dt>string</dt>
<dd> As in C. String constants are surrounded by double-quotes. Backslashed characters (including double-quotes) stand for themselves, except &quot;
&quot; stands for newline, &quot;
&quot; for carriage return, &quot;&quot; for backspace, &quot;	&quot; for tab and &quot;&quot; for formfeed.</dd>
<dt>name</dt>
<dd> A variable reference.</dd>
<dt>name() name(E,E,&#8230;,E)</dt>
<dd> A function call with zero or more arguments. Functions are fully call-by-value: arrays and structures are copied rather than being referenced as in C.</dd>
<dt>desc name T name = value</dt>
<dd> Definition expressions: a new name is made available, with the value of the definition being the value of the initializer in the second form, and uninitialized in the first form. The descriptor desc is not optional: it consists of any combination of visibility, storage class or type (in that order). See QUALIFIERS immediately below for a description of these qualifiers. A structured value expression is also possible: see VALUES below.</dd>
<dt>
</dt><dd> In addition to being able to initialize a definition with a Nickle value, C-style array, structure, and union definitions are also allowed: For example, the following </dd>
<pre><code>
int[ *, *] name = &#123;&#123;0, 1}, {2, 3}} int[2, 2] name = &#123;&#123;0...}...}
</code></pre>
<p> are permitted with the obvious semantics. This is the context in which the dimensions in a type may be expressions: see the discussion of array types above. See the discussion of array and structure values for array and structure initializer syntax.</dl>
<h2>QUALIFIERS</h2>
<p> A declaration or definition may be qualified, as in C, to indicate details of programmatic behavior. Unlike in C, these qualifiers, while optional, must appear in the given order. </p>
<p> <code>Visibility:</code></p>
<dl>
<dt>public</dt>
<dd> Any definition expression (function definition, variable definition, type definition) can be qualified with public to indicate that the name being defined should be visible outside the current namespace, and should be automatically imported. See Namespaces below for further info.</dd>
<dt>protected</dt>
<dd> Any definition expression (function definition, variable definition, type definition) can be qualified with protected to indicate that the name being defined should be visible outside the current namespace, but should not be made available by import declarations. See Namespaces below for further info.</dd></dl>
<p> <code>Lifetime:</code></p>
<dl>
<dt>auto</dt>
<dd> An auto object is local to a particular block: its lifetime is at least the lifetime of that block. An auto object with an initializer will be re-initialized each time it is evaluated. This is the default lifetime for local objects.</dd>
<dt>static</dt>
<dd> A static object is local to a particular function definition: its lifetime is at least the lifetime of that definition. A new static object will be created each time its enclosing function definition is evaluated.</dd>
<dt>
</dt><dd> In Nickle, the keyword static has to do only with lifetime (like the use of static inside C functions), not with visibility (which is handled by separate qualifiers as described above, not like the use of static in global scope in C).</dd>
<dt>global</dt>
<dd> A global object is global to the entire program: its lifetime is the lifetime of the program. A global object will be created and initialized when its definition is first seen. This is the default lifetime for global objects.</dd>
<dt>
</dt><dd> The distinction between static and global lifetime in Nickle is not possible in C, because C functions are not first class objects with nested scope. When deciding which to use in a Nickle program, think about what should happen if a definition is re-evaluated.</dd></dl>
<h2>OPERATORS</h2>
<p> Here are the basic Nickle operators, grouped in order of decreasing precedence: </p>
<dl>
<dt>A[E,E,&#8230;,E]</dt>
<dd> Refers to the E&#8217;th element of the array expression A, or the E1&#8217;th/E2&#8217;th/etc element of a multi-dimensional array. Both arrays of arrays ala C and multidimensional arrays ala NAWK are possible.</dd>
<dt>struct.tag</dt>
<dd> Structure dereference.</dd>
<dt>struct-&gt;tag</dt>
<dd> Structure pointer dereference ala C.</dd>
<dt>=============</dt>
<dd>
</dd><dt>++ &#8212;</dt>
<dd> Unary increment/decrement. May be either postfix or prefix.</dd>
<dt>&#8211;</dt>
<dd> Unary negate</dd>
<dt>! E</dt>
<dd> Logical negation.</dd>
<dt>E !</dt>
<dd> Factorial. Requires a non-negative integer argument.</dd>
<dt>* E</dt>
<dd> Pointer dereference.</dd>
<dt>&amp; E</dt>
<dd> Reference construction.</dd>
<dt>=============</dt>
<dd>
</dd><dt>(U) E</dt>
<dd> Construct a value of union type with tag U and value E.</dd>
<dt>=============</dt>
<dd>
</dd><dt>**</dt>
<dd> Exponentiation. Both operands may be fractional. The left operand must be non-negative unless the right operand is integer. The result type is the type of the left operand if the right operand is integer, and real otherwise.</dd>
<dt>
</dt><dd> This is the only known type-unsound feature of Nickle: an expression like 2 ** -3 will statically be of type integer, but dynamically will generate a rational result. This may cause a runtime type error later on: consider </dd>
<p>&nbsp;<wbr>&nbsp;<wbr>int x&nbsp;<wbr>=&nbsp;<wbr>2&nbsp;<wbr>**&nbsp;<wbr>-3; </p>
<dt>=============</dt>
<dd>
</dd><dt>* / // %</dt>
<dd> Times, divide, integer divide, and remainder. The right operand of the last three operators must be nonzero. The result type of the division operator will always be at least rational: the result type of the integer division operator will always be int. This is a notable departure from C, where integer division is implied by integer operands. Integer division is defined by </dd>
<p>&nbsp;<wbr>&nbsp;<wbr>x&nbsp;<wbr>//&nbsp;<wbr>y&nbsp;<wbr>==&nbsp;<wbr>y&nbsp;<wbr>&gt;&nbsp;<wbr>0&nbsp;<wbr>?&nbsp;<wbr>floor&nbsp;<wbr>(x&nbsp;<wbr>/&nbsp;<wbr>y)&nbsp;<wbr>: ceil(x&nbsp;<wbr>/&nbsp;<wbr>y)<br />
 The remainder is always non-negative and is defined by: by </p>
<p>&nbsp;<wbr>&nbsp;<wbr>x&nbsp;<wbr>%&nbsp;<wbr>y&nbsp;<wbr>=&nbsp;<wbr>x &#8211;&nbsp;<wbr>(x&nbsp;<wbr>//&nbsp;<wbr>y)&nbsp;<wbr>*&nbsp;<wbr>y </p>
<dt>=============</dt>
<dd>
</dd><dt>+ &#8211;</dt>
<dd> Addition and subtraction.</dd>
<dt>=============</dt>
<dd>
</dd><dt>&lt;&lt; &gt;&gt;</dt>
<dd> Bitwise left and right shift with integer operands. Negative right operands work as expected. These operators are defined by </dd>
<p>&nbsp;<wbr>&nbsp;<wbr>x&nbsp;<wbr>&lt;&lt;&nbsp;<wbr>y&nbsp;<wbr>=&nbsp;<wbr>x&nbsp;<wbr>*&nbsp;<wbr>2&nbsp;<wbr>**&nbsp;<wbr>y </p>
<p>&nbsp;<wbr>&nbsp;<wbr>x&nbsp;<wbr>&gt;&gt;&nbsp;<wbr>y&nbsp;<wbr>=&nbsp;<wbr>x&nbsp;<wbr>//&nbsp;<wbr>2&nbsp;<wbr>**&nbsp;<wbr>y<br />
 Another way to look at this is that negative left operands are considered to be in an infinite twos-complement representation (i.e., sign-extended to infinity), with right shift sign-extending its left operand.</p>
<dt>=============</dt>
<dd>
</dd><dt>&lt;= &gt;= &lt; &gt;</dt>
<dd> Relational operators.</dd>
<dt>=============</dt>
<dd>
</dd><dt>== !=</dt>
<dd> Equality operators.</dd>
<dt>=============</dt>
<dd> Finally, in order of decreasing precedence:</dd>
<dt>&amp;</dt>
<dd> Bitwise AND. Negative operands are considered to be in an infinite twos-complement representation (i.e., sign-extended to infinity).</dd>
<dt>^</dt>
<dd> Bitwise XOR. Negative operands as in bitwise AND.</dd>
<dt>|</dt>
<dd> Bitwise OR. Negative operands as in bitwise AND.</dd>
<dt>&amp;&amp;</dt>
<dd> Short-circuit logical AND.</dd>
<dt>||</dt>
<dd> Short-circuit logical OR.</dd>
<dt>E ? E : E</dt>
<dd> Conditional expression: if first expression is logical true, value is second expression, else third.</dd>
<dt>fork E</dt>
<dd> Create (and return) a thread. See Thread below for details.</dd>
<dt>= += -= *= /= //= %= **= &lt;&lt;= &gt;&gt;= ^= &amp;= |=</dt>
<dd> Assignment operators. Left-hand-side must be assignable. <code>x </code><i>&lt;op&gt;=</i><code> y</code> is equivalent to <code>x </code><i>=</i><code> x </code><i>&lt;op&gt;</i><code> y</code></dd>
<dt>E , E</dt>
<dd> Returns right-hand expression.</dd></dl>
<h2>TYPES</h2>
<p> The type declaration syntax of Nickle more strongly resembles the &#8220;left&#8221; variant of the Java syntax than the C syntax. Essentially, a type consists of:</p>
<dl>
<dt>poly integer rational real string continuation void</dt>
<dd> A base type of the language. Type void is actually only usable in certain contexts, notably function returns. It is currently implemented as a &#8220;unit&#8221; type ala ML, and thus has slightly different behavior than in C. Type poly is the supertype of all other types (i.e., it can be used to inhibit static type checking), and is the default type in most situations where a type need not appear.</dd>
<dt>file semaphore thread</dt>
<dd> Also builtin base types, but integral to the File and Thread ADTs: see below.</dd></dl>
<p> <code>More About Types:</code> </p>
<p> <i>Nickle</i> supports polymorphic data: As an expresion is evaluated, a data type is chosen to fit the result. Any Nickle object may be statically typed, in which case bounds violations will be flagged as errors at compile time. Polymorphic variables and functions do not place restrictions on the assigned data type; this is the default type for all objects.</p>
<dl>
<dt>poly</dt>
<dd> This describes the union of all datatypes. A variable with this type can contain any data value.</dd>
<dt>int</dt>
<dd> Arbitrary precision integers.</dd>
<dt>rational</dt>
<dd> Arbitrary precision rational numbers.</dd>
<dt>real</dt>
<dd> Arbitrary exponent precision floating point numbers. As many computations cannot be carried out exactly as rational numbers, Nickle implements non-precise arithmetic using its own machine-independent representation for floating point numbers. The builtin function imprecise(n) generates a real number with 256 bits of precision from the number n, while imprecise(n,p) generates a real number with p bits of precision.</dd>
<dt>T[]</dt>
<dd> An array of type T, of one or more dimensions. There are no zero-dimensional arrays in Nickle.</dd>
<dt>T[*]</dt>
<dd> A one-dimensional array of type T. Unlike in C, the dimension of an array is never part of its type in Nickle. Further, arrays and pointers are unrelated types in Nickle.</dd>
<dt>T[*,*,&#8230;,*]</dt>
<dd> A two or more dimensional array of type T. The stars &#8220;*&#8221; are not optional. As the previous paragraphs make clear, &#8220;T[]&#8221; is not a zero-dimensional array.</dd>
<dt>T[E,E,&#8230;,E]</dt>
<dd> In definition contexts, integer values may be given for each dimension of an array context. These are strictly for value-creation purposes, and are not part of the type. An array type is determined only by the base type and number of dimensions of the array.</dd>
<dt>T0() T0(T,T,&#8230;,T)</dt>
<dd> A function returning type T0. A function accepts 0 or more arguments.</dd>
<dt>T0() T0(T,T,&#8230;,T <code>&#8230;</code>)</dt>
<dd> A function accepting zero or more required arguments, plus an arbitrary number of optional arguments. The second sequence of three dots (ellipsis) is syntax, not metasyntax: see the description of varargs functions for details.</dd>
<dt>*T</dt>
<dd> A pointer to a location of type T. Pointer arithmetic in Nickle operates only upon pointers to arrays: the pointer must be of the correct type, and may never stray out of bounds. A pointer may either point to some location or be null (0). As in C, the precedence of &#8220;*&#8221; is lower than the precedence of &#8220;[]&#8221; or &#8220;()&#8221;: use parenthesis as needed.</dd>
<dt>struct {T name; T name; &#8230;}</dt>
<dd> A structure with fields of the given name and type. The types T are optional: in their absence, the type of the field is poly.</dd>
<dt>union {T name; T name; &#8230;}</dt>
<dd> A &#8220;disjoint union&#8221; of the given types. This is more like the variant record type of Pascal or the datatype of ML than the C union type: the names are tags of the given type, exactly one of which applies to a given value at a given time.</dd>
<dt>(T)</dt>
<dd> Parentheses for grouping.</dd></dl>
<p> <code>Typedef:</code> </p>
<p> As in C, new type names may be created with the typedef statement. The syntax is </p>
<p>&nbsp;<wbr>&nbsp;<wbr>typedef T typename;<br />
 where T is a Nickle type. The resulting typename may be used anywhere a type is expected.</p>
<h2>VALUES</h2>
<p> Values of the base types of Nickle are as expected. See the syntax for constants above. Values of type file, semaphore, and continuation may currently be created only by calls to builtin functions: no Nickle constants of these types exist. </p>
<p> As noted in TYPES above, Nickle has several kinds of &#8220;structured value&#8221;: arrays, functions, pointers, structures and disjoint unions. All of these have some common properties. When created, all of the component values are uninitialized (unless otherwise specified). Attempts to use an uninitialized value will result in either a compile-time error or a runtime exception. </p>
<p> <code>Arrays:</code></p>
<dl>
<dt>[E]</dt>
<dd> creates a (zero-based) array with E elements. E must be non-negative.</dd>
<dt>[E]{V,V,&#8230;,V}</dt>
<dd> Creates an array with E elements, initialized to the Vs. If there are too few initializers, remaining elements will remain uninitialized.</dd>
<dt>[E]{V,V,&#8230;,V<i>&#8230;</i>}</dt>
<dd> The second ellipsis (three dots) is syntax, not metasyntax. Create an array with E elements. The first elements in the array will be initialized according to the Vs, with any remaining elements receiving the same value as the last V. This syntax may be used in the obvious fashion with any of the array initializers below.</dd>
<dt>[*]{V,V,&#8230;,V}</dt>
<dd> Creates an initialized array with exactly as many elements as initializers. There must be at least one initializer.</dd>
<dt>[E,E,&#8230;,E] [*,*,&#8230;,*]</dt>
<dd> Creates multidimensional arrays. Integer expressions and &quot;*&quot; cannot be mixed: an array&#8217;s dimensions are entirely either specified or unspecified by the definition. These arrays may also be created initialized: see next paragraph for initializer syntax.</dd>
<dt>(T[E]) (T[E,E,&#8230;,E]) (T[E]){E,E,&#8230;,E}</dt>
<dd>
</dd><dt>(T[E,E,&#8230;,E])&#123;&#123;E,&#8230;},&#8230;,{E,&#8230;}}</dt>
<dd> Alternate syntax for creating arrays of type T. The initializers, in curly braces, are optional. The number of initializers must be less than or equal to the given number of elements in each dimension. For multidimensional arrays, the extra curly braces per dimension in the initializer are required; this is unlike C, where they are optional.</dd>
<dt>(T[*]){E,E,&#8230;,E} (T[*,*,&#8230;,*])&#123;&#123;E,&#8230;},&#8230;,{E,&#8230;}}</dt>
<dd> Creates arrays of type T, with each dimension&#8217;s size given by the maximum number of initializers in any subarray in that dimension.</dd></dl>
<p> <code>Pointers:</code></p>
<dl>
<dt>0</dt>
<dd> The null pointer, in contexts where a pointer is required.</dd>
<dt>&amp;V &amp;A[E,E,&#8230;,E] &amp;S.N</dt>
<dd> Creates a pointer to the given variable, array element, or structure member. The type of the pointer will be *T, where T is the type of the object pointed to.</dd>
<dt>*P</dt>
<dd> The value pointed to by pointer P. This can be viewed or modified as in C.</dd></dl>
<p> <code>Functions:</code></p>
<dl>
<dt>(T func(){S;S;&#8230;S;}) (T func(T name,T name,&#8230;T name){S;S;&#8230;S;})</dt>
<dd> Function expression: denotes a function of zero or more formal parameters with the given types and names, returning the given result type. The function body is given by the curly-brace-enclosed statement list. All types are optional, and default to poly. As noted above, functions are strictly call-by-value: in particular, arrays and structures are copied rather than referenced.</dd>
<dt>T function name(T name,T name,&#8230;,T name){S;S;&#8230;S;}</dt>
<dd> Defines a function of zero or more arguments. Syntactic sugar for </dd>
<p>&nbsp;<wbr>&nbsp;<wbr>T(T,T,&#8230;T)&nbsp;<wbr>name&nbsp;<wbr>=&nbsp;<wbr>(T func(T name,T name,&#8230;T name){S;S;&#8230;S;}); </p>
<dt>T function name(T name, T name <code>&#8230;</code>)</dt>
<dd> The ellipsis here is syntax, not metasyntax: if the last formal argument to a function is followed by three dots, the function may be called with more actuals than formals. All &#8220;extra&#8221; actuals are packaged into the array formal of the given name, and typechecked against the optional type T of the last argument (default poly).</dd></dl>
<p> <code>Structures:</code></p>
<dl>
<dt>(struct { T name; T name; &#8230;T name; }){name = E; name = E; &#8230;name=E;}</dt>
<dd> Create a value of a structured type. The named fields are initialized to the given values, with the remainder uninitialized. As indicated, initialization is by label rather than positional as in C.</dd></dl>
<p> <code>Unions:</code></p>
<dl>
<dt>(union { T name; T name; &#8230;T name; }.name) E</dt>
<dd> Create a value of the given union type, the variant given by .name, and the value given by E. E must be type-compatible with name.</dd></dl>
<h2>STATEMENTS</h2>
<p> The statement syntax very closely resembles that of C. Some additional syntax has been added to support Nickle&#8217;s additional functionality.</p>
<dl>
<dt>E;</dt>
<dd> Evaluates the expression.</dd>
<dt>{S &#8230; S}</dt>
<dd> Executes the enclosed statements in order.</dd>
<dt>if (E) S</dt>
<dd> Basic conditional.</dd>
<dt>if (E) S</dt>
<dd> Conditional execution.</dd>
<dt>else S</dt>
<dd> Else is allowed, with the usual syntax and semantics. In particular, an else binds to the most recent applicable if() or twixt().</dd>
<dt>while (E) S</dt>
<dd> C-style while loop.</dd>
<dt>do S while (E);</dt>
<dd> C-style do loop.</dd>
<dt>for (opt-E; opt-E; opt-E) S</dt>
<dd> C-style for loop.</dd>
<dt>switch (E) { case E: S-list case E: S-list &#8230; default: S-list }</dt>
<dd> C-style case statement. The case expressions are not required to be constant expressions, but may be arbitrary. The first case evaluating to the switch argument is taken, else the default if present, else the switch body is skipped.</dd>
<dt>twixt(opt-E; opt-E) S</dt>
<dd>
</dd><dt>twixt(opt-E; opt-E) S else S</dt>
<dd> If first argument expression evaluates to true, the body of the twixt() and then the second argument expression will be evaluated. If the first argument expression evaluates to false, the else statement will be executed if present. Otherwise, the entire twixt() statement will be skipped.</dd></dl>
<p> The twixt() statement guarantees that all of these events will happen in the specified order regardless of the manner in which the twixt() is entered (from outside) or exited, including exceptions, continuations, and break. (Compare with Java&#8217;s &#8220;finally&#8221; clause.)</p>
<dl>
<dt>try S;</dt>
<dd>
</dd><dt>try S catch name (T name, &#8230;) { S; &#8230; };</dt>
<dd>
</dd><dt>try S catch name (T name, &#8230;) { S; &#8230; } &#8230; ;</dt>
<dd> Execute the first statement S. If an exception is raised during execution, and the name matches the name in a catch block, bind the formal parameters in the catch block to the actual parameters of the exception, and execute the body of the catch block. There may be multiple catch blocks per try. Zero catches, while legal, is relatively useless. After completion of a catch block, execution continues after the try clause. As with else, a catch binds to the most recent applicable try-catch block.</dd>
<dt>raise name(name, name, &#8230;, name)</dt>
<dd> Raise the named exception with zero or more arguments.</dd>
<dt>;</dt>
<dd> The null statement</dd>
<dt>break;</dt>
<dd> Discontinue execution of the nearest enclosing for/do/while/switch/twixt statement. The leave expression will be executed as the twixt statement is exited.</dd>
<dt>continue;</dt>
<dd> Branch directly to the conditional test of the nearest enclosing for/do/while statement.</dd>
<dt>return E;</dt>
<dd> Return value E from the nearest enclosing function.</dd></dl>
<p> <code>Namespaces:</code> </p>
<p> Like Java and C++ Nickle has a notion of <i>namespace</i>, a collection of names with partially restricted visibility. In Nickle, namespaces are created with the <i>namespace</i> command.</p>
<dl>
<dt>opt-P namespace N { S &#8230; }</dt>
<dd> Places all names defined in the statements S into a namespace named N. The optional qualifier P may be the keyword public, but beware: this merely indicates that the name N itself is visible elsewhere in the current scope, and has nothing to do with the visibility of items inside the namespace.</dd>
<dt>extend namespace N { S &#8230; }</dt>
<dd> Reopen the given namespace N, and extend it with the names defined as public in the given statements S.</dd>
<dt>
</dt><dd> Names defined inside the namespace are invisible outside the namespace unless they are qualified with the keyword public. Public names may be referred to using a path notation: </dd>
<p>&nbsp;<wbr>&nbsp;<wbr>namespace::namespace::&#8230;::namespace::name<br />
 refers to the given name as defined inside the given set of namespaces. The double-colon syntax is unfortunate, as it is slightly different in meaning than in C++, but all the good symbols were taken, and it is believed to be a feature that the namespace separator is syntactically different than the structure operator. In Java, for example, the phrase </p>
<p>&nbsp;<wbr>&nbsp;<wbr>name.name.name<br />
 is syntactically ambiguous: the middle name may be either a structure or a namespace.</p>
<dt>import N;</dt>
<dd> The name N must refer to a namespace: all public names in this namespace are brought into the current scope (scoping out conflicting names).</dd></dl>
<h2>BUILTINS</h2>
<p> <i>Nickle</i> has a collection of standard functions built in. Some of these are written in C, but many are written in Nickle. Several collections of functions have associated builtin datatypes: their namespaces, together with their types, should be viewed as ADTs. </p>
<p> <code>Top-Level Builtins:</code></p>
<dl>
<dt>int printf(string fmt, poly args&#8230;)</dt>
<dd> Calls File::fprintf(stdout, fmt, args &#8230;) and returns its result.</dd>
<dt>string function gets ()</dt>
<dd> Calls File::fgets(stdin) and returns its result.</dd>
<dt>string function scanf (string fmt, *poly args&#8230;)</dt>
<dd> Calls File::vfscanf(stdin, fmt, args) and returns its result.</dd>
<dt>string function vscanf (string fmt, (*poly)[*] args)</dt>
<dd> Calls File::vfscanf(stdin, fmt, args) and returns its result.</dd>
<dt>real imprecise(rational value)</dt>
<dd> See the discussion of type real above.</dd>
<dt>real imprecise(rational value, int prec)</dt>
<dd> See the discussion of type real above.</dd>
<dt>int string_to_integer(string s)</dt>
<dd>
</dd><dt>int atoi(string s)</dt>
<dd> The argument s is a signed digit string, and the result is the integer it represents. If the string s is syntactically a hexadecimal, octal, binary, or explicit base-10 constant, treat it as such.</dd>
<dt>int string_to_integer(string s, int base)</dt>
<dd>
</dd><dt>int atoi(string s, int base)</dt>
<dd> Treat s as a string of digits in the given base. A base of 0 acts as with no base argument. Otherwise, base specification syntax in the string is ignored.</dd>
<dt>int putchar(int c)</dt>
<dd> Place the given character on the standard output using File::putc(c, stdout), and return its result.</dd>
<dt>int sleep(int msecs)</dt>
<dd> Try to suspend the current thread for at least msecs milliseconds. Return 1 on early return, and 0 otherwise.</dd>
<dt>int exit(int status)</dt>
<dd> Exit Nickle with the given status code. Do not return anything.</dd>
<dt>int dim(poly[*] a)</dt>
<dd> Given a one-dimensional array a, dim() returns the number of elements of a.</dd>
<dt>int[] dims(poly[] a)</dt>
<dd> Given an arbitrary array a, dims() returns an array of integers giving the size of each dimension of a. Thus, dim(dims(a)) is the number of dimensions of a.</dd>
<dt>*poly reference(poly v)</dt>
<dd> Given an arbitrary value v, &#8220;box&#8221; that value into storage and return a pointer to the box.</dd>
<dt>rational string_to_real(string s)</dt>
<dd>
</dd><dt>rational atof(string s)</dt>
<dd> Convert the real constant string s into its associated real number.</dd>
<dt>number abs(real v)</dt>
<dd> Return the absolute value of v. The result type chosen will match the given context.</dd>
<dt>int floor(real v)</dt>
<dd> Return the largest integer less than or equal to v. This will fail if v is a real and the precision is too low.</dd>
<dt>int ceil(real v)</dt>
<dd> Return the smallest integer greater than or equal to v. This will fail if v is a real and the precision is too low.</dd>
<dt>int exponent(real v)</dt>
<dd> Return the exponent of the imprecise real v.</dd>
<dt>rational mantissa(real v)</dt>
<dd> Return the mantissa of the imprecise real v, as a rational m with 0 &lt;= m &lt;= 0.5 .</dd>
<dt>int numerator(rational v)</dt>
<dd> Return the numerator of the rational number v: i.e., if v = n/d in reduced form, return n.</dd>
<dt>int denominator(rational v)</dt>
<dd> Return the denominator of the rational number v: i.e., if v = n/d in reduced form, return d.</dd>
<dt>int precision(real v)</dt>
<dd> Return the number of bits of precision of the mantissa of the imprecise real number v.</dd>
<dt>int sign(real v)</dt>
<dd> Return -1 or 1 as v is negative or nonnegative.</dd>
<dt>int bit_width(int v)</dt>
<dd> Return the number of bits required to represent abs(v) internally.</dd>
<dt>int is_int(poly v)</dt>
<dd> Type predicate.</dd>
<dt>int is_rational(poly v)</dt>
<dd> Numeric type predicates are inclusive: e.g., is_rational(1) returns 1.</dd>
<dt>int is_number(poly v)</dt>
<dd> Type predicate.</dd>
<dt>int is_string(poly v)</dt>
<dd> Type predicate.</dd>
<dt>int is_file(poly v)</dt>
<dd> Type predicate.</dd>
<dt>int is_thread(poly v)</dt>
<dd> Type predicate.</dd>
<dt>int is_semaphore(poly v)</dt>
<dd> Type predicate.</dd>
<dt>int is_continuation(poly v)</dt>
<dd> Type predicate.</dd>
<dt>int is_array(poly v)</dt>
<dd> Type predicate.</dd>
<dt>int is_ref(poly v)</dt>
<dd> Type predicate: checks for pointer type. This is arguably a misfeature, and may change.</dd>
<dt>int is_struct(poly v)</dt>
<dd> Type predicate.</dd>
<dt>int is_func(poly v)</dt>
<dd> Type predicate.</dd>
<dt>int is_void(poly v)</dt>
<dd> Type predicate.</dd>
<dt>int gcd(int p, int q)</dt>
<dd> Return the GCD of p and q. The result is always positive.</dd>
<dt>int xor(int a, int b)</dt>
<dd> Return a ^ b . This is mostly a holdover from before Nickle had an xor operator.</dd>
<dt>poly setjmp(continuation *c, poly retval)</dt>
<dd> The setjmp() and longjmp() primitives together with the continuation type form an ADT useful for nearly arbitrary transfers of flow-of-control. The setjmp() and longjmp() builtins are like those of C, except that the restriction that longjmp() always jump upwards is removed(!): a continuation saved via setjmp() never becomes invalid during the program lifetime.</dd>
<dt>
</dt><dd> The setjmp() builtin saves the current location and context into its continuation pointer argument, and then returns its second argument.</dd>
<dt>void longjmp(continuation c, poly retval)</dt>
<dd> The longjmp() builtin never returns to the call site, but instead returns from the setjmp() that created the continuation, with return value equal to the second argument of longjmp().</dd>
<dt>string prompt</dt>
<dd> The prompt printed during interactive use when at top-level. Default &quot;&gt; &quot;. when waiting for the rest of a statement or expression, and when debugging, respectively. Default values are &quot;&gt; &quot;, &quot;+ &quot;, and &quot;- &quot;.</dd>
<dt>string prompt2</dt>
<dd> The prompt printed during interactive use when waiting for the rest of a statement or expression. Default &quot;+ &quot;.</dd>
<dt>string prompt3</dt>
<dd> The prompt printed during interactive use when debugging. Default &quot;- &quot;.</dd>
<dt>string format</dt>
<dd> The printf() format for printing top-level values. Default &quot;%g&quot;.</dd>
<dt>string version</dt>
<dd> The version number of the Nickle implementation currently being executed.</dd>
<dt>string build</dt>
<dd> The build date of the Nickle implementation currently being executed, in the form &quot;yyyy/mm/dd&quot;, or &quot;?&quot; if the build date is unknown for some reason.</dd>
<dt>file stdin</dt>
<dd> Bound to the standard input stream.</dd>
<dt>file stdout</dt>
<dd> Bound to the standard output stream.</dd>
<dt>file stderr</dt>
<dd> Bound to the standard error stream.</dd></dl>
<p> <code>Exceptions:</code> </p>
<p> A few standard exceptions are predeclared and used internally by Nickle.</p>
<dl>
<dt>exception uninitialized_value(string msg)</dt>
<dd> Attempt to use an uninitialized value.</dd>
<dt>exception invalid_argument(string msg, int arg, poly val)</dt>
<dd> The arg-th argument to a builtin function had invalid value val.</dd>
<dt>exception readonly_box(string msg, poly val)</dt>
<dd> Attempt to change the value of a read-only quantity to val.</dd>
<dt>exception invalid_array_bounds(string msg, poly a, poly i)</dt>
<dd> Attempt to access array a at index i is out of bounds.</dd>
<dt>exception divide_by_zero(string msg, real num, real den)</dt>
<dd> Attempt to divide num by den with den == 0.</dd>
<dt>exception invalid_struct_member(string msg, poly struct, string name)</dt>
<dd> Attempt to refer to member name of the object struct, which does not exist.</dd>
<dt>exception invalid_binop_values(string msg, poly arg1, poly arg2)</dt>
<dd> Attempt to evaluate a binary operator with args arg1 and arg2, where at least one of these values is invalid.</dd>
<dt>exception invalid_unop_values(string msg, poly arg)</dt>
<dd> Attempt to evaluate a unary operator with invalid argument arg.</dd></dl>
<p> <code>Builtin Namespaces:</code></p>
<dl>
<dt>Math</dt>
<dd> The math functions available in the Math namespace are implemented in a fashion intended to be compatible with the C library. Please consult the appropriate manuals for further details.</dd>
<dt>real pi</dt>
<dd> Imprecise constant giving the value of the circumference/diameter ratio of the circle to the default precision of 256 bits.</dd>
<dt>protected real e</dt>
<dd> Imprecise constant giving the value of the base of natural logarithms to the default precision of 256 bits. Since e is protected, it must be referenced via Math::e, in order to avoid problems with using the fifth letter of the alphabet at top level.</dd>
<dt>real function sqrt(real v)</dt>
<dd> Returns the square root of v.</dd>
<dt>real function cbrt(real v)</dt>
<dd> Returns the cube root of v.</dd>
<dt>real function exp(real v)</dt>
<dd> Returns e**v.</dd>
<dt>real function log(real a)</dt>
<dd> Returns v such that e**v == a. Throws an invalid_argument exception if a is non-positive.</dd>
<dt>real function log10(real a)</dt>
<dd> Returns v such that 10**v == a. Throws an invalid_argument exception if a is non-positive.</dd>
<dt>real function log2(real a)</dt>
<dd> Returns v such that 2**v == a. Throws an invalid_argument exception if a is non-positive.</dd>
<dt>real function pi_value(int prec)</dt>
<dd> Returns the ratio of the circumference of a circle to the diameter, with prec bits of precision.</dd>
<dt>real function sin(real a)</dt>
<dd> Returns the ratio of the opposite side to the hypotenuse of angle a of a right triangle, given in radians.</dd>
<dt>real function cos(real a)</dt>
<dd> Returns the ratio of the adjacent side to the hypotenuse of angle a of a right triangle, given in radians.</dd>
<dt>void function sin_cos(real a, *real sinp, *real cosp)</dt>
<dd> Returns with sin(a) and cos(a) stored in the locations pointed to by sinp and cosp respectively. If either pointer is 0, do not store into that location. May be slightly faster than calling both trig functions independently.</dd>
<dt>real function tan(real a)</dt>
<dd> Returns the ratio of the opposite side to the adjacent side of angle a of a right triangle, given in radians. Note that tan(pi/2) is not currently an error: it will return a very large number dependent on the precision of its input.</dd>
<dt>real function asin(real v)</dt>
<dd> Returns a such that sin(a) == v.</dd>
<dt>real function acos(real v)</dt>
<dd> Returns a such that cos(a) == v.</dd>
<dt>real function atan(real v)</dt>
<dd> Returns a such that tan(a) == v.</dd>
<dt>real function atan2(real x, y)</dt>
<dd> Returns a such that tan(a) == x / y. Deals correctly with y == 0.</dd>
<dt>real function pow(real a, real b)</dt>
<dd> The implementation of the ** operator.</dd></dl>
<dl>
<dt>File</dt>
<dd> The namespace File provides operations on file values.</dd>
<dt>int function fprintf(file f, string s, &#8230;.)</dt>
<dd> Print formatted values to a file, as with UNIX stdio library fprintf(). fprintf() and printf() accept a reasonable sub-set of the stdio library version: %c, %d, %e, %x, %o, %f, %s, %g work as expected, as does %v to smart-print a value. Format modifiers may be placed between the percent-sign and the format letter to modify formatting. There are a lot of known bugs with input and output formatting.</dd>
<dl>
<dt>
</dt><dd>
<p> <code>Format Letters:</code></p>
</dd><dl>
<dt>%c</dt>
<dd> Requires a small integer argument (0..255), and formats as an ASCII character.</dd>
<dt>%d</dt>
<dd> Requires an integer argument, and formats as an integer.</dd>
<dt>%x</dt>
<dd> Requires an integer argument, and formats as a base-16 (hexadecimal) integer.</dd>
<dt>%o</dt>
<dd> Requires an integer argument, and formats as a base-8 (octal) integer.</dd>
<dt>%e</dt>
<dd> Requires a number argument, and formats in scientific notation.</dd>
<dt>%f</dt>
<dd> Requires a number argument, and formats in fixed-point notation.</dd>
<dt>%s</dt>
<dd> Requires a string argument, and emits the string literally.</dd>
<dt>%g</dt>
<dd> Requires a number, and tries to pick a precise and readable representation to format it.</dd></dl>
<p> <code>Format Modifiers:</code></p>
<dl>
<dt>digits</dt>
<dd> All format characters will take an integer format modifier indicating the number of blanks in the format field for the data to be formatted. The value will be printed right-justified in this space.</dd>
<dt>digits.digits</dt>
<dd> The real formats will take a pair of integer format modifiers indicating the field width and precision (number of chars after decimal point) of the formatted value. Either integer may be omitted.</dd>
<dt>&#8211;</dt>
<dd> A precision value indicating infinite precision.</dd>
<dt>*</dt>
<dd> The next argument to fprintf() is an integer indicating the field width or precision of the formatted value.</dd></dl>
</dl>
<dt>file function string_write()</dt>
<dd> Return a file which collects written values into a string.</dd>
<dt>int function close(file f)</dt>
<dd> Close file f and return an indication of success.</dd>
<dt>int function flush(file f)</dt>
<dd> Flush the buffers of file f and return an indication of success.</dd>
<dt>int function getc(file f)</dt>
<dd> Get the next character from file f and return it.</dd>
<dt>int function end(file f)</dt>
<dd> Returns true if file f is at EOF, else false.</dd>
<dt>int function error(file f)</dt>
<dd> Returns true if an error is pending on file f, else false.</dd>
<dt>int function clear_error(file f)</dt>
<dd> Clears pending errors on file f, and returns an indication of success.</dd>
<dt>file function string_read(string s)</dt>
<dd> Returns a virtual file whose contents are the string s.</dd>
<dt>string function string_string(file f)</dt>
<dd> Return the string previously written into the file f, which should have been created by string_read() or string_write(). Behavior on other files is currently undefined.</dd>
<dt>file function open(string path, string mode)</dt>
<dd> Open the file at the given path with the given mode string, ala UNIX stdio fopen(). Permissible modes are as in stdio: &quot;r&quot;, &quot;w&quot;, &quot;x&quot;, &quot;r+&quot;, &quot;w+&quot; and &quot;x+&quot;.</dd>
<dt>integer function fputc(integer c, file f)</dt>
<dd> Output the character c to the output file f, and return an indication of success.</dd>
<dt>integer function ungetc(integer c, file f)</dt>
<dd> Push the character c back onto the input file f, and return an indication of success.</dd>
<dt>integer function setbuf(file f, integer n)</dt>
<dd> Set the size of the buffer associated with file f to n, and return n.</dd>
<dt>string function fgets (file f)</dt>
<dd> Get a line of input from file f, and return the resulting string.</dd>
<dt>file function pipe(string path, string[*] argv, string mode)</dt>
<dd> Start up the program at the given path, returning a file which is one end of a &quot;pipe&quot; to the given process. The mode argument can be &quot;r&quot; to read from the pipe or &quot;w&quot; to write to the pipe. The argv argument is an array of strings giving the arguments to be passed to the program, with argv[0] conventionally being the program name.</dd>
<dt>int function print (file f, poly v, string fmt, int base, int width, int prec, string fill)</dt>
<dd> Print value v to file f in format fmt with the given base, width, prec, and fill. Used internally by File::fprintf();</dd>
<dt>int function fscanf(file f, string fmt, *poly args&#8230;)</dt>
<dd> Fill the locations pointed to by the array args with values taken from file f according to string fmt. The format specifiers are much as in UNIX stdio scanf(): the &quot;%d&quot;, &quot;%e&quot;, &quot;%f&quot;, &quot;%c&quot; and &quot;%s&quot; specifiers are supported with the expected modifiers.</dd>
<dt>int function vfscanf (file f, string fmt, (*poly)[*] args)</dt>
<dd> Given the file f, the format fmt, and the array of arguments args, fscanf() appropriately.</dd></dl>
<dl>
<dt>Thread</dt>
<dd> The namespace Thread supports various operations useful for programming with <i>threads</i>, which provide concurrent flow of control in the shared address space. There is one piece of special syntax associated with threads.</dd>
<dl>
<dl>
<dt>fork(E)</dt>
<dd> Accepts an arbitrary expression, and evaluates it in a new child thread. The parent thread receives the thread as the value of the fork expression.</dd></dl>
</dl>
<dt>
</dt><dd> The remainder of the Thread functions are fairly standard.</dd>
<dt>int function kill(thread list&#8230;)</dt>
<dd> Kills every running thread in the array list. With no arguments, kills the currently running thread. Returns the number of threads killed.</dd>
<dt>int function trace(poly list&#8230;)</dt>
<dd> Shows the state of every running thread in the array list. With no arguments, traces the default continuation. Returns the number of threads traced.</dd>
<dt>int function cont()</dt>
<dd> Continues execution of any interrupted threads, and returns the number of continued threads.</dd>
<dt>thread function current()</dt>
<dd> Return the current thread.</dd>
<dt>int function list()</dt>
<dd> Reports the currently running thread to stdout.</dd>
<dt>int function get_priority(thread t)</dt>
<dd> Reports the priority of the given thread.</dd>
<dt>thread function id_to_thread(int id)</dt>
<dd> Returns the thread with the given id, if found, and 0 otherwise.</dd>
<dt>poly function join(thread t)</dt>
<dd> Waits for thread t to terminate, and returns whatever it returns.</dd>
<dt>int function set_priority(thread t, int i)</dt>
<dd> Attempts to set the priority of thread t to level i, and returns the new priority. Larger priorities mean more runtime: a task with higher priority will always run instead of a lower priority task. Threads of equal highest priority will be pre-emptively multitasked.</dd></dl>
<dl>
<dt>Semaphore</dt>
<dd> The Semaphore namespace encapsulates operations on the semaphore built-in ADT. A semaphore is used for thread synchronization. Each signal() operation on the semaphore awakens the least-recent thread to wait() on that semaphore. The &#8220;count&#8221; of waiting processes may be set at semaphore creation time.</dd>
<dt>semaphore function new(int c)</dt>
<dd> Create a new semaphore with an initial count c of waiting processes. If c is positive, it means that c threads may wait on the semaphore before one blocks. If c is negative, it sets a count of threads which must be waiting on the semaphore before further waits will not block.</dd>
<dt>semaphore function new()</dt>
<dd> Call semaphore(0) and return its result.</dd>
<dt>int signal(semaphore s)</dt>
<dd> Increment semaphore s. If s is non-positive, and some thread is blocked on s, release the least-recently-blocked thread. Return 1 on success.</dd>
<dt>int wait(semaphore s)</dt>
<dd> Decrement semaphore s. If s is negative, block until released. Return 1 on success.</dd>
<dt>int test(semaphore s)</dt>
<dd> Test whether wait() on semaphore s would cause the current thread to block. If so, return 0. Otherwise, attempt to decrement s, and return 1 if successful.</dd></dl>
<dl>
<dt>String</dt>
<dd> The String namespace contains a few basic operations on the string ADT.</dd>
<dt>int function length(string s)</dt>
<dd> Returns the number of characters in s.</dd>
<dt>string function new(int c)</dt>
<dd> Returns as a string the single character c.</dd>
<dt>string function new(int cv[*])</dt>
<dd> Returns a string comprised of the characters of cv.</dd>
<dt>int function index(string t, string p)</dt>
<dd> Returns the integer index of the pattern string p in the target string t, or -1 if p is not a substring of t.</dd>
<dt>string function substr(string s, int i, int l)</dt>
<dd> Returns the substring of string s starting with the character at offset i (zero-based) and continuing for a total of l characters. If l is negative, the substring will consist of characters preceding rather than succeeding i.</dd></dl>
<dl>
<dt>PRNG</dt>
<dd> The PRNG namespace provides pseudo-random number generation and manipulation. The core generator is the RC4 stream cipher generator, properly bootstrapped. This provide a stream of cryptographically-secure pseudo-random bits at reasonable amortized cost. (But beware, initialization is somewhat expensive.)</dd>
<dt>void function srandom(int s)</dt>
<dd> Initialize the generator, using the (arbitrarily-large) integer as a seed.</dd>
<dt>void function dev_srandom(int nbits)</dt>
<dd> Initialize the generator, using nbits bits of entropy obtained from some reasonable entropy source. On UNIX systems, this source is /dev/urandom. Asking for more initial entropy than the system has may lead either to bootstrapping (as on UNIX) or to hanging, so use cautiously.</dd>
<dt>int function randbits(int n)</dt>
<dd> Returns an n-<code>bit</code> pseudo-random number, in the range <i>0..(2**n)-1</i>. Useful for things like RSA.</dd>
<dt>int function randint(int n)</dt>
<dd> Returns a pseudo-random number in the range <i>0..n-1</i>.</dd>
<dt>void function shuffle(*(poly[*]) a)</dt>
<dd> Performs an efficient in-place true shuffle (c.f. Knuth) of the array a.</dd></dl>
<dl>
<dt>Command</dt>
<dd> The Command namespace is used by the top-level commands as described below. It is also occasionally useful in its own right.</dd>
<dt>string library_path</dt>
<dd> Contains the current library search path, a colon-separated list of directories to be searched for library files.</dd>
<dt>int function undefine(string name)</dt>
<dd> Implements the top-level undefine command. Remove the name denoted by string name from the namespace. This removes all visible definitions of the name.</dd>
<dt>int function undefine(string[*] names)</dt>
<dd> Remove each of the names in the array names from the namespace. This removes all visible definitions of each name.</dd>
<dt>int function delete(string name)</dt>
<dd> Attempt to remove the command with the given string name from the top-level command list, and return 1 if successful.</dd>
<dt>int function lex_file(string path)</dt>
<dd> Attempt to make the file at the given path the current source of Nickle code, and return 1 if successful. Note that this effectively &#8220;includes&#8221; the file by pushing it onto a stack of files to be processed.</dd>
<dt>int function lex_library(string filename)</dt>
<dd> Like lex_file(), but searches the directories given by the <i>library_path</i> variable for the first file with the given filename.</dd>
<dt>int function lex_string(string code)</dt>
<dd> Attempt to make the Nickle code contained in the string code be the next input.</dd>
<dt>int function edit(string[*] names)</dt>
<dd> Implements the top-level edit command. The names in the array are a path of namespace names leading to the symbol name, which is last.</dd>
<dt>int function new(string name, poly func)</dt>
<dd> Binds function func to the top-level command string name: i.e., makes it part of the top-level command vocabulary.</dd>
<dt>int function new_names(string name, poly func)</dt>
<dd> Binds function func to the top-level command string name: i.e., makes it part of the top-level command vocabulary. Unlike new(), the string names given to func at the top level are passed unevaluated as an array of string names or as a single string name.</dd>
<dt>int function pretty_print(file f, string[*] names)</dt>
<dd> Implements the top-level print command. Each of the passed name strings is looked up and the corresponding code printed to file f.</dd>
<dt>int function display(string fmt, poly val)</dt>
<dd> Uses printf() to display the value val in format fmt.</dd></dl>
<dl>
<dt>History</dt>
<dd> Nickle maintains a top-level value history, useful as an adjunct to command-line editing when calculating. The History namespace contains functions to access this history.</dd>
<dt>int function show(string fmt)</dt>
<dd> Implements the history top-level command with no arguments. Show the most recent history values with format fmt.</dd>
<dt>int function show(string fmt, int count)</dt>
<dd> Implements the history top-level command with one argument. Show the last count history values with format fmt.</dd>
<dt>int function show(string fmt, int first, int last)</dt>
<dd> Implements the history top-level command with two arguments.</dd>
<dt>poly function insert(poly val)</dt>
<dd> Insert val in the history list, and return it.</dd></dl>
<dl>
<dt>Environ</dt>
<dd> Many operating systems have some notion of &#8220;environment variables.&#8221; The Environ namespace contains functions to manipulate these.</dd>
<dt>int function check(string name)</dt>
<dd> Returns 1 if the variable with the given name is in the environment, and 0 otherwise.</dd>
<dt>string function get(string name)</dt>
<dd> Attempts to retrieve and return the value of the environment variable with the given name. Throws an invalid_argument exception if the variable is not available.</dd>
<dt>int function unset(string name)</dt>
<dd> Attempts to unset the environment variable with the given name, and returns an indication of success.</dd>
<dt>string function set(string name, string value)</dt>
<dd> Attempts to set the environment variable with the given name to the given value, and returns an indication of success.</dd></dl>
<h2>COMMANDS</h2>
<p> Nickle has a set of commands which may be given at the top level.</p>
<dl>
<dt>quit</dt>
<dd> Exit Nickle.</dd>
<dt>quit E</dt>
<dd> Exit Nickle with integer status code E.</dd>
<dt>undefine NAME {,NAME}</dt>
<dd> Remove these names from the system.</dd>
<dt>load E</dt>
<dd> Load a file given by the string name E.</dd>
<dt>library E</dt>
<dd> Load a library given by the string name E. See the discussion of the NICKLEPATH environment variable in ENVIRONMENT below, and the discussion of Command::library_path above.</dd>
<dt>E # E</dt>
<dd> Print expr1 in base expr2 .</dd>
<dt>print NAME</dt>
<dd> Display a formatted version of the object denoted by NAME. Comments and original formating are lost. If NAME is a variable, print the type as well as the value.</dd>
<dt>edit NAME</dt>
<dd> Invoke $EDITOR on the named object, and re-incorporate the results of the edit. This is most useful with functions.</dd>
<dt>history</dt>
<dd> Display the 10 most recently printed values. They can be accessed with <code>$</code><i>n</i> where <i>n</i> is the number displayed to the right of the value in this list.</dd>
<dt>history <i>E</i></dt>
<dd> Display the E most recent history values.</dd>
<dt>history <i>E</i>,<i>E</i></dt>
<dd> Display history values from the first integer E through the second.</dd></dl>
<h2>DEBUGGER</h2>
<p> When an unhandled exception reaches top level during execution, the user receives a dash prompt, indicating that debug mode is active. In this mode, the command-line environment is that in which the unhandled exception was raised. In addition a number of debugging commands are available to the user:</p>
<dl>
<dt>trace</dt>
<dd> Get a stack backtrace showing the current state, as with the GDB where command.</dd>
<dt>up</dt>
<dd> Move up the stack (i.e., toward the top-level expression) ala GDB.</dd>
<dt>down</dt>
<dd> Move down the stack (i.e., toward the current context) ala GDB.</dd>
<dt>done</dt>
<dd> Leave debugging mode, abandoning execution.</dd>
<dt>
</dt><dd> In addition, the Debug namespace is scoped in in debugging mode. This is primarily of use in debugging Nickle itself.</dd>
<dt>collect()</dt>
<dd> Run the garbage collector.</dd>
<dt>dump(function)</dt>
<dd> Print the compiled byte code for function.</dd></dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt>EDITOR</dt>
<dd> The editor used by the edit command, described in COMMANDS above.</dd>
<dt>NICKLERC</dt>
<dd> The location of the user&#8217;s .nicklerc file, which will be loaded at the beginning of nickle execution if possible.</dd>
<dt>HOME</dt>
<dd> Used to find the user&#8217;s .nicklerc if NICKLERC is not set.</dd>
<dt>NICKLEPATH</dt>
<dd> A colon-separated path whose elements are directories containing Nickle code. The library command and the -l flag, described above, search this path for a filename matching the given file. The default library path in the absence of this variable is /usr/share/nickle.</dd>
<dt>NICKLESTART</dt>
<dd> The filename of the file that should be loaded as a bootstrap on Nickle startup. The default in the absence of this variable is to load /usr/share/nickle/builtin.5c.</dd></dl>
<h2>EXAMPLES</h2>
<p> An example (taken from the <i>bc</i> manual:<br />
real function exponent(real x)<br />
{<br />
    real a = 1;<br />
    int b = 1;<br />
    real s = 1;<br />
    int i = 1;<br />
    while (1) {<br />
        a = a * x;<br />
        b = b * i;<br />
        real c = a / b;<br />
        if (abs(c) &lt; 1e-6)<br />
            return s;<br />
        s = s + c;<br />
        i++;<br />
    }<br />
}<br />
 defines a function to compute an approximate value of the exponential function e ** x and<br />
for (i = 1; i &lt; 10; i++)<br />
    printf(&#8220;%g
&#8221;, exponent(i));<br />
 prints approximate values of the exponential function of the first ten integers.</p>
<h2>VERSION</h2>
<p> This document describes version 1.99.2 of nickle, as well as some newer features. It was distributed with version 2.69 of nickle.</p>
<h2>BUGS</h2>
<p> See the discussion of the type of the exponentiation operator ** above. </p>
<p> Due to a difficult-to-remove grammar ambiguity, it is not possible to use a bare assignment expression in an array initializer: it is confused with a structure initializer. For example:<br />
&gt; int x = 0;<br />
&gt; (int[*])<br />
{<br />
    x = 1<br />
}<br />
-&gt; (int[*]){x = 1} Non array initializer<br />
 The workaround is to parenthesize the assignment expression: </p>
<pre><code>
&gt; (int[*]){(x = 1)}
        [1]
{
    1
}
</code></pre>
<p> Because this is so rare, so hard to fix, and so easy to work around, this bug is unlikely to be fixed anytime soon. </p>
<p> There are a lot of known bugs with input and output formatting. The obvious stuff works, other stuff does not. </p>
<p> The semantics of division are unfortunately different from those of C. This is arguably because C is broken in this area: we cannot currently see any obvious fix. C allows automatic implicit coercion of floating to integral types, but we consider this a misfeature. </p>
<p> The implementation has not been thoroughly tested.</p>
<h2>AUTHOR</h2>
<p> <i>Nickle</i> is the work of Keith Packard &lt;keithp [at] keithp.com&gt; and Bart Massey &lt;bart_massey [at] iname.com&gt;. </p>
<p> Nickle is<br />
 Copyright 1988-2006 Keith Packard and Bart Massey. All Rights Reserved. </p>
<p> Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the &quot;Software&quot;), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: </p>
<p> The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. </p>
<p> THE SOFTWARE IS PROVIDED &quot;AS IS&quot;, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. </p>
<p> Except as contained in this notice, the names of the authors or their institutions shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from the authors. </p>

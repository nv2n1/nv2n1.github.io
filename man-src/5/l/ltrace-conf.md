---
title: "ltrace-conf(5)"
name: "ltrace-conf"
section: "5"
letter: "l"
url: "/docs/linux/man/5-ltrace-conf/"
description: "ltrace.conf – Configuration file for"
---

<p><code>ltrace.conf</code> &#8211; Configuration file for <code></p>
<p> <a href="/docs/linux/man/1-ltrace/">ltrace</a>(1)</code>. </p>
<h2>Description</h2>
<p>This manual page describes <code>ltrace.conf</code>, a file that describes prototypes of functions in binaries for <code><a href="/docs/linux/man/1-ltrace/">ltrace</a>(1)</code> to use. Ltrace needs this information to display function call arguments. Each line of a configuration file describes at most a single item. Lines composed entirely of white space are ignored, as are lines starting with semicolon character (comment lines). Described items can be either function prototypes, or definitions of type aliases. </p>
<h2>Prototypes</h2>
<p>A prototype describes return type and parameter types of a single function. The syntax is as follows: </p>
<dl>
<dd><i>LENS</i> <i>NAME</i> <code>(</code>[<i>LENS</i>{,<i>LENS</i>}]<code>);</code></dl>
<p> <i>NAME</i> is the (mangled) name of a symbol. In the elementary case, <i>LENS</i> is simply a type. Both lenses and types are described below. For example, a simple function prototype might look like this: </p>
<dl>
<dd><code>int</code> kill<code>(int,int);</code></dl>
<p> Despite the apparent similarity with C, <code>ltrace.conf</code> is really its own language that&#8217;s only somewhat inspired by C.</p>
<h2>Types</h2>
<p>Ltrace understands a range of primitive types. Those are interpreted according to C convention native on a given architecture. E.g. <code>ulong</code> is interpreted as 4-byte unsigned integer on 32-bit GNU/Linux machine, but 8-byte unsigned integer on 64-bit GNU/Linux machine. </p>
<dl>
<dt><code>void</code></p>
<dd>Denotes that a function does not return anything. Can be also used to construct a generic pointer, i.e. pointer-sized number formatted in hexadecimal format.</p>
<dt><code>char</code></p>
<dd>8-bit quantity rendered as a character</p>
<dt><code>ushort,short</code></p>
<dd>Denotes unsigned or signed short integer.</p>
<dt><code>uint,int</code></p>
<dd>Denotes unsigned or signed integer.</p>
<dt><code>ulong,long</code></p>
<dd>Denotes unsigned or signed long integer.</p>
<dt><code>float</code></p>
<dd>Denotes floating point number with single precision.</p>
<dt><code>double</code></p>
<dd>Denotes floating point number with double precision.</dl>
<p> Besides primitive types, the following composed types are possible: </p>
<dl>
<dt><code>struct(</code>[<i>LENS</i>{,<i>LENS</i>}]<code>)</code></p>
<dd>Describes a structure with given types as fields, e.g. <code>struct(int,int,float)</code>. </p>
<p> Alignment is computed as customary on the architecture. Custom alignment (e.g. packed structs) and bit-fields are not supported. It&#8217;s also not possible to differentiate between structs and non-POD C++ classes, for arches where it makes a difference. </p>
<dt><code>array(</code><i>LENS</i><code>,</code><i>EXPR</i><code>)</code></p>
<dd>Describes array of length <i>EXPR</i>, which is composed of types described by <i>LENS</i>, e.g. <code>array(int, </code>6<code>)</code>. </p>
<p> Note that in C, arrays in role of function argument decay into pointers. Ltrace currently handles this automatically, but for full formal correctness, any such arguments should be described as pointers to arrays. </p>
<dt><i>LENS</i><code>*</code></p>
<dd>Describes a pointer to a given type, e.g. <code>char*</code> or <code>int***</code>. Note that the former example actually describes a pointer to a character, not a string. See below for <code>string</code> lens, which is applicable to these cases. </p>
</dl>
<h2>Lenses</h2>
<p>Lenses change the way that types are described. In the simplest case, a lens is directly a type. Otherwise a type is decorated by the lens. Ltrace understands the following lenses: </p>
<dl>
<dt><code>oct(</code><i>TYPE</i><code>)</code></p>
<dd>The argument, which should be an integer type, is formatted in base-8. </p>
<dt><code>hex(</code><i>TYPE</i><code>)</code></p>
<dd>The argument, which should be an integer or floating point type, is formatted in base-16. Floating point arguments are converted to double and then displayed using the <code>%a</code> fprintf modifier. </p>
<dt><code>hide(</code><i>TYPE</i><code>)</code></p>
<dd>The argument is not shown in argument list. </p>
<dt><code>bool(</code><i>TYPE</i><code>)</code></p>
<dd>Arguments with zero value are shown as &quot;false&quot;, others are shown as &quot;true&quot;. </p>
<dt><code>bitvec(</code><i>TYPE</i><code>)</code></p>
<dd>Underlying argument is interpreted as a bit vector and a summary of bits set in the vector is displayed. For example if bits 3,4,5 and 7 of the bit vector are set, ltrace shows &lt;3-5,7&gt;. Empty bit vector is displayed as &lt;&gt;. If there are more bits set than unset, inverse is shown instead: e.g. ~&lt;0&gt; when a number 0xfffffffe is displayed. Full set is thus displayed ~&lt;&gt;. </p>
<p> If the underlying type is integral, then bits are shown in their natural big-endian order, with LSB being bit 0. E.g. <code>bitvec(ushort)</code> with value 0x0102 would be displayed as &lt;1,8&gt;, irrespective of underlying byte order. </p>
<p> For other data types (notably structures and arrays), the underlying data is interpreted byte after byte. Bit 0 of first byte has number 0, bit 0 of second byte number 8, and so on. Thus <code>bitvec(struct(int))</code> is endian sensitive, and will show bytes comprising the integer in their memory order. Pointers are first dereferenced, thus <code>bitvec(array(char, </code>32<code>)*)</code> is actually a pointer to 256-bit bit vector. </p>
</dl>
<p> <code>string(</code><i>TYPE</i><code>)</code><br />
 <code>string[</code><i>EXPR</i><code>]</code><br />
 <code>string</code></p>
<dl>
<dd>The first form of the argument is canonical, the latter two are syntactic sugar. In the canonical form, the function argument is formatted as string. The <i>TYPE</i> shall be either a <code>char*</code>, or <code>array(char,</code><i>EXPR</i><code>)</code>, or <code>array(char,</code><i>EXPR</i><code>)*</code>. If an array is given, the length will typically be a <code>zero</code> expression (but doesn&#8217;t have to be). Using argument that is plain array (i.e. not a pointer to array) makes sense e.g. in C structs, in cases like <code>struct(string(array(char, </code>6<code>)))</code>, which describes the C type <code>struct {char </code>s<code>[</code>6<code>];}</code>. </p>
<p> Because simple C-like strings are pretty common, there are two shorthand forms. The first shorthand form (with brackets) means the same as <code>string(array(char, </code><i>EXPR</i><code>)*)</code>. Plain <code>string</code> without an argument is then taken to mean the same as <code>string[zero]</code>. </p>
<p> Note that <code>char*</code> by itself describes a pointer to a char. Ltrace will dereference the pointer, and read and display the single character that it points to.</dl>
<p> <code>enum(</code><i>NAME</i>[<code>=</code><i>VALUE</i>]{,<i>NAME</i>[<code>=</code><i>VALUE</i>]}<code>)</code><br />
 <code>enum[</code><i>TYPE</i><code>](</code><i>NAME</i>[<code>=</code><i>VALUE</i>]{,<i>NAME</i>[<code>=</code><i>VALUE</i>]}<code>)</code></p>
<dl>
<dd>This describes an enumeration lens. If an argument has any of the given values, it is instead shown as the corresponding <i>NAME</i>. If a <i>VALUE</i> is omitted, the next consecutive value following after the previous <i>VALUE</i> is taken instead. If the first <i>VALUE</i> is omitted, it&#8217;s <code>0</code> by default. </p>
<p> <i>TYPE</i>, if given, is the underlying type. It is thus possible to create enums over shorts or longs&#8212;arguments that are themselves plain, non-enum types in C, but whose values can be meaningfully described as enumerations. If omitted, <i>TYPE</i> is taken to be <code>int</code>.</dl>
<h2>Type Aliases</h2>
<p>A line in config file can, instead of describing a prototype, create a type alias. Instead of writing the same enum or struct on many places (and possibly updating when it changes), one can introduce a name for such type, and later just use that name: </p>
<dl>
<dd><code>typedef </code><i>NAME</i><code> = </code><i>LENS</i><code>;</code></dl>
<h2>Recursive Structures</h2>
<p>Ltrace allows you to express recursive structures. Such structures are expanded to the depth described by the parameter -A. To declare a recursive type, you first have to introduce the type to ltrace by using forward declaration. Then you can use the type in other type definitions in the usual way: </p>
<dl>
<dd><code>typedef </code><i>NAME</i><code> = struct;</code><br />
 <code>typedef </code><i>NAME</i><code> = struct(</code><i>NAME</i> can be used here<code>)</code></dl>
<p> For example, consider the following singy-linked structure and a function that takes such list as an argument: </p>
<dl>
<dd><code>typedef</code> int_list <code>= struct;</code><br />
 <code>typedef</code> int_list <code>= struct(int,</code> int_list<code>*);</code><br />
 <code>void</code> ll<code>(</code>int_list<code>*);</code></dl>
<p> Such declarations might lead to an output like the following: </p>
<dl>
<dd>ll({ 9, { 8, { 7, { 6, &#8230; } } } }) = &lt;void&gt;</dl>
<p> Ltrace detects recursion and will not expand already-expanded structures. Thus a doubly-linked list would look like the following: </p>
<dl>
<dd><code>typedef</code> int_list <code>= struct;</code><br />
 <code>typedef</code> int_list <code>= struct(int,</code> int_list<code>*,</code> int_list<code>*);</code></dl>
<p> With output e.g. like: </p>
<dl>
<dd>ll({ 9, { 8, { 7, { 6, &#8230;, &#8230; }, recurse^ }, recurse^ }, nil })</dl>
<p> The &quot;recurse^&quot; tokens mean that given pointer points to a structure that was expanded in the previous layer. Simple &quot;recurse&quot; would mean that it points back to this object. E.g. &quot;recurse^^^&quot; means it points to a structure three layers up. For doubly-linked list, the pointer to the previous element is of course the one that has been just expanded in the previous round, and therefore all of them are either recurse^, or nil. If the next and previous pointers are swapped, the output adjusts correspondingly: </p>
<dl>
<dd>ll({ 9, nil, { 8, recurse^, { 7, recurse^, { 6, &#8230;, &#8230; } } } })</dl>
<h2>Expressions</h2>
<p>Ltrace has support for some elementary expressions. Each expression can be either of the following: </p>
<dl>
<dt><i>NUM</i></p>
<dd>An integer number. </p>
<dt><code>arg</code><i>NUM</i></p>
<dd>Value of <i>NUM</i>-th argument. The expression has the same value as the corresponding argument. <code>arg1</code> refers to the first argument, <code>arg0</code> to the return value of the given function. </p>
<dt><code>retval</code></p>
<dd>Return value of function, same as <code>arg0</code>. </p>
<dt><code>elt</code><i>NUM</i></p>
<dd>Value of <i>NUM</i>-th element of the surrounding structure type. E.g. <code>struct(ulong,array(int,elt1))</code> describes a structure whose first element is a length, and second element an array of ints of that length. </p>
</dl>
<p> <code>zero</code><br />
 <code>zero(</code><i>EXPR</i><code>)</code></p>
<dl>
<dd>Describes array which extends until the first element, whose each byte is 0. If an expression is given, that is the maximum length of the array. If NUL terminator is not found earlier, that&#8217;s where the array ends.</dl>
<h2>Parameter Packs</h2>
<p>Sometimes the actual function prototype varies slightly depending on the exact parameters given. For example, the number and types of printf parameters are not known in advance, but ltrace might be able to determine them in runtime. This feature has wider applicability, but currently the only parameter pack that ltrace supports is printf-style format string itself: </p>
<dl>
<dt><code>format</code></p>
<dd>When <code>format</code> is seen in the parameter list, the underlying string argument is parsed, and GNU-style format specifiers are used to determine what the following actual arguments are. E.g. if the format string is &quot;%s %d
&quot;, it&#8217;s as if the <code>format</code> was replaced by <code>string, string, int</code>. </p>
</dl>
<h2>Return Arguments</h2>
<p>C functions often use one or more arguments for returning values back to the caller. The caller provides a pointer to storage, which the called function initializes. Ltrace has some support for this idiom. </p>
<p> When a traced binary hits a function call, ltrace first fetches all arguments. It then displays <i>left</i> portion of the argument list. Only when the function returns does ltrace display <i>right</i> portion as well. Typically, left portion takes up all the arguments, and right portion only contains return value. But ltrace allows you to configure where exactly to put the dividing line by means of a <code>+</code> operator placed in front of an argument: </p>
<dl>
<dd><code>int</code> asprintf<code>(+string*, format);</code></dl>
<p> Here, the first argument to asprintf is denoted as return argument, which means that displaying the whole argument list is delayed until the function returns: </p>
<dl>
<dd>a.out-&gt;asprintf( &lt;unfinished &#8230;&gt;<br />
 libc.so.6-&gt;malloc(100) = 0x245b010<br />
 [&#8230; more calls here &#8230;]<br />
 &lt;&#8230; asprintf resumed&gt; &quot;X=1&quot;, &quot;X=%d&quot;, 1) = 5</dl>
<p> It is currently not possible to have an &quot;inout&quot; argument that passes information in both directions.</p>
<h2>Examples</h2>
<p>In the following, the first is the C prototype, and following that is ltrace configuration line. </p>
<pre><code>void func_charp_string(char str[]);

void func_charp_string(string);

enum e_foo { RED,
             GREEN,
             BLUE };

void func_enum(enum e_foo bar);

void func_enum(enum(RED, GREEN, BLUE));

- or -

     typedef e_foo = enum(RED, GREEN, BLUE);

void func_enum(e_foo);
void func_arrayi(int arr[], int len);

void func_arrayi(array(int, arg2) *, int);

struct S1 {
    float f;
    char a;
    char b;
};

struct S2 {
    char str[6];
    float f;
};

struct S1 func_struct(int a, struct S2, double d);

struct(float, char, char) func_struct_2(int, struct(string(array(char, 6)), float), double);
</code></pre>
<h2>Author</h2>
<p>Petr Machata &lt;pmachata [at] redhat.com&gt;</p>

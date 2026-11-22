---

title: "perlglossary(1)"
name: "perlglossary"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlglossary/"
description: "perlglossary – Perl Glossary"
---

<p> perlglossary &#8211; Perl Glossary </p>
<h2>VERSION</h2>
<p> version 5.20190126</p>
<h2>DESCRIPTION</h2>
<p> A glossary of terms (technical and otherwise) used in the Perl documentation, derived from the Glossary of <i>Programming Perl</i>, Fourth Edition. Words or phrases in bold are defined elsewhere in this glossary. </p>
<p> Other useful sources include the Unicode Glossary &lt;<a rel="nofollow" href="http://unicode.org/glossary/">http://unicode.org/glossary/</a>&gt;, the Free On-Line Dictionary of Computing &lt;<a rel="nofollow" href="http://foldoc.org/">http://foldoc.org/</a>&gt;, the Jargon File &lt;<a rel="nofollow" href="http://catb.org/~esr/jargon/">http://catb.org/~esr/jargon/</a>&gt;, and Wikipedia &lt;<a rel="nofollow" href="http://www.wikipedia.org/">http://www.wikipedia.org/</a>&gt;.</p>
<h3>A</h3>
<dl>
<dt>accessor methods</dt>
<dd> A <code>method</code> used to indirectly inspect or update an <code>object</code>’s state (its <code>instance variables</code>).</dd>
<dt>actual arguments</dt>
<dd> The <code>scalar values</code> that you supply to a <code>function</code> or <code>subroutine</code> when you call it. For instance, when you call <tt>&quot;power(&quot;puff&quot;)&quot;</tt>, the string <tt>&quot;puff&quot;</tt> is the actual argument. See also <code>argument</code> and <code>formal arguments</code>.</dd>
<dt>address operator</dt>
<dd> Some languages work directly with the memory addresses of values, but this can be like playing with fire. Perl provides a set of asbestos gloves for handling all memory management. The closest to an address operator in Perl is the backslash operator, but it gives you a <code>hard reference</code>, which is much safer than a memory address.</dd>
<dt>algorithm</dt>
<dd> A well-defined sequence of steps, explained clearly enough that even a computer could do them.</dd>
<dt>alias</dt>
<dd> A nickname for something, which behaves in all ways as though you’d used the original name instead of the nickname. Temporary aliases are implicitly created in the loop variable for <tt>&quot;foreach&quot;</tt> loops, in the <tt>$_</tt> variable for <tt>&quot;map&quot;</tt> or <tt>&quot;grep&quot;</tt> operators, in <tt>$a</tt> and <tt>$b</tt> during <tt>&quot;sort&quot;</tt>’s comparison function, and in each element of <tt>@_</tt> for the <code>actual arguments</code> of a subroutine call. Permanent aliases are explicitly created in <code>packages</code> by <code>importing</code> symbols or by assignment to <code>typeglobs</code>. Lexically scoped aliases for package variables are explicitly created by the <tt>&quot;our&quot;</tt> declaration.</dd>
<dt>alphabetic</dt>
<dd> The sort of characters we put into words. In Unicode, this is all letters including all ideographs and certain diacritics, letter numbers like Roman numerals, and various combining marks.</dd>
<dt>alternatives</dt>
<dd> A list of possible choices from which you may select only one, as in, “Would you like door A, B, or C?” Alternatives in regular expressions are separated with a single vertical bar: <tt>&quot;|&quot;</tt>. Alternatives in normal Perl expressions are separated with a double vertical bar: <tt>&quot;||&quot;</tt>. Logical alternatives in <code>Boolean</code> expressions are separated with either <tt>&quot;||&quot;</tt> or <tt>&quot;or&quot;</tt>.</dd>
<dt>anonymous</dt>
<dd> Used to describe a <code>referent</code> that is not directly accessible through a named <code>variable</code>. Such a referent must be indirectly accessible through at least one <code>hard reference</code>. When the last hard reference goes away, the anonymous referent is destroyed without pity.</dd>
<dt>application</dt>
<dd> A bigger, fancier sort of <code>program</code> with a fancier name so people don’t realize they are using a program.</dd>
<dt>architecture</dt>
<dd> The kind of computer you’re working on, where one “kind of computer” means all those computers sharing a compatible machine language. Since Perl programs are (typically) simple text files, not executable images, a Perl program is much less sensitive to the architecture it’s running on than programs in other languages, such as C, that are <code>compiled</code> into machine code. See also <code>platform</code> and <code>operating system</code>.</dd>
<dt>argument</dt>
<dd> A piece of data supplied to a <code>program</code>, <code>subroutine</code>, <code>function</code>, or <code>method</code> to tell it what it’s supposed to do. Also called a “parameter”.</dd>
<dt>ARGV</dt>
<dd> The name of the array containing the <code>argument</code> <code>vector</code> from the command line. If you use the empty <tt>&quot;&lt;&gt;&quot;</tt> operator, <tt>&quot;ARGV&quot;</tt> is the name of both the <code>filehandle</code> used to traverse the arguments and the <code>scalar</code> containing the name of the current input file.</dd>
<dt>arithmetical operator</dt>
<dd> A <code>symbol</code> such as <tt>&quot;+&quot;</tt> or <tt>&quot;/&quot;</tt> that tells Perl to do the arithmetic you were supposed to learn in grade school.</dd>
<dt>array</dt>
<dd> An ordered sequence of <code>values</code>, stored such that you can easily access any of the values using an <i>integer subscript</i> that specifies the value’s <code>offset</code> in the sequence.</dd>
<dt>array context</dt>
<dd> An archaic expression for what is more correctly referred to as <code>list context</code>.</dd>
<dt>Artistic License</dt>
<dd> The open source license that Larry Wall created for Perl, maximizing Perl’s usefulness, availability, and modifiability. The current version is 2. (&lt;<a rel="nofollow" href="http://www.opensource.org/licenses/artistic-license.php">http://www.opensource.org/licenses/artistic-license.php</a>&gt;).</dd>
<dt>ASCII</dt>
<dd> The American Standard Code for Information Interchange (a 7-bit character set adequate only for poorly representing English text). Often used loosely to describe the lowest 128 values of the various ISO-8859-X character sets, a bunch of mutually incompatible 8-bit codes best described as half ASCII. See also <code>Unicode</code>.</dd>
<dt>assertion</dt>
<dd> A component of a <code>regular expression</code> that must be true for the pattern to match but does not necessarily match any characters itself. Often used specifically to mean a <code>zero-width</code> assertion.</dd>
<dt>assignment</dt>
<dd> An <code>operator</code> whose assigned mission in life is to change the value of a <code>variable</code>.</dd>
<dt>assignment operator</dt>
<dd> Either a regular <code>assignment</code> or a compound <code>operator</code> composed of an ordinary assignment and some other operator, that changes the value of a variable in place; that is, relative to its old value. For example, <tt>&quot;$a += 2&quot;</tt> adds <tt>2</tt> to <tt>$a</tt>.</dd>
<dt>associative array</dt>
<dd> See <code>hash</code>. Please. The term associative array is the old Perl 4 term for a <code>hash</code>. Some languages call it a dictionary.</dd>
<dt>associativity</dt>
<dd> Determines whether you do the left <code>operator</code> first or the right <code>operator</code> first when you have “A <code>operator</code> B <code>operator</code> C”, and the two operators are of the same precedence. Operators like <tt>&quot;+&quot;</tt> are left associative, while operators like <tt>&quot;**&quot;</tt> are right associative. See Camel chapter 3, “Unary and Binary Operators” for a list of operators and their associativity.</dd>
<dt>asynchronous</dt>
<dd> Said of events or activities whose relative temporal ordering is indeterminate because too many things are going on at once. Hence, an asynchronous event is one you didn’t know when to expect.</dd>
<dt>atom</dt>
<dd> A <code>regular expression</code> component potentially matching a <code>substring</code> containing one or more characters and treated as an indivisible syntactic unit by any following <code>quantifier</code>. (Contrast with an <code>assertion</code> that matches something of <code>zero width</code> and may not be quantified.)</dd>
<dt>atomic operation</dt>
<dd> When Democritus gave the word “atom” to the indivisible bits of matter, he meant literally something that could not be cut: <i>ἀ-</i> (not) + <i>-τομος</i> (cuttable). An atomic operation is an action that can’t be interrupted, not one forbidden in a nuclear-free zone.</dd>
<dt>attribute</dt>
<dd> A new feature that allows the declaration of <code>variables</code> and <code>subroutines</code> with modifiers, as in <tt>&quot;sub foo : locked method&quot;</tt>. Also another name for an <code>instance variable</code> of an <code>object</code>.</dd>
<dt>autogeneration</dt>
<dd> A feature of <code>operator overloading</code> of <code>objects</code>, whereby the behavior of certain <code>operators</code> can be reasonably deduced using more fundamental operators. This assumes that the overloaded operators will often have the same relationships as the regular operators. See Camel chapter 13, “Overloading”.</dd>
<dt>autoincrement</dt>
<dd> To add one to something automatically, hence the name of the <tt>&quot;++&quot;</tt> operator. To instead subtract one from something automatically is known as an “autodecrement”.</dd>
<dt>autoload</dt>
<dd> To load on demand. (Also called “lazy” loading.) Specifically, to call an <tt>&quot;AUTOLOAD&quot;</tt> subroutine on behalf of an undefined subroutine.</dd>
<dt>autosplit</dt>
<dd> To split a string automatically, as the <i>–a</i> <code>switch</code> does when running under <i>–p</i> or <i>–n</i> in order to emulate <code>awk</code>. (See also the <tt>&quot;AutoSplit&quot;</tt> module, which has nothing to do with the <tt>&quot;–a&quot;</tt> switch but a lot to do with autoloading.)</dd>
<dt>autovivification</dt>
<dd> A Graeco-Roman word meaning “to bring oneself to life”. In Perl, storage locations (<code>lvalues</code>) spontaneously generate themselves as needed, including the creation of any <code>hard reference</code> values to point to the next level of storage. The assignment <tt>&quot;$a[5][5][5][5][5] = &quot;quintet&quot;&quot;</tt> potentially creates five scalar storage locations, plus four references (in the first four scalar locations) pointing to four new anonymous arrays (to hold the last four scalar locations). But the point of autovivification is that you don’t have to worry about it.</dd>
<dt>AV</dt>
<dd> Short for “array value”, which refers to one of Perl’s internal data types that holds an <code>array</code>. The <tt>&quot;AV&quot;</tt> type is a subclass of <code>SV</code>.</dd>
<dt>awk</dt>
<dd> Descriptive editing term—short for “awkward”. Also coincidentally refers to a venerable text-processing language from which Perl derived some of its high-level ideas.</dd></dl>
<h3>B</h3>
<dl>
<dt>backreference</dt>
<dd> A substring <code>captured</code> by a subpattern within unadorned parentheses in a <code>regex</code>. Backslashed decimal numbers (<tt>&quot;\1&quot;</tt>, <tt>&quot;\2&quot;</tt>, etc.) later in the same pattern refer back to the corresponding subpattern in the current match. Outside the pattern, the numbered variables (<tt>$1</tt>, <tt>$2</tt>, etc.) continue to refer to these same values, as long as the pattern was the last successful match of the current <code>dynamic scope</code>.</dd>
<dt>backtracking</dt>
<dd> The practice of saying, “If I had to do it all over, I’d do it differently,” and then actually going back and doing it all over differently. Mathematically speaking, it’s returning from an unsuccessful recursion on a tree of possibilities. Perl backtracks when it attempts to match patterns with a <code>regular expression</code>, and its earlier attempts don’t pan out. See the section “The Little Engine That /Couldn(n’t)” in Camel chapter 5, “Pattern Matching”.</dd>
<dt>backward compatibility</dt>
<dd> Means you can still run your old program because we didn’t break any of the features or bugs it was relying on.</dd>
<dt>bareword</dt>
<dd> A word sufficiently ambiguous to be deemed illegal under <tt>&quot;use strict 'subs'&quot;</tt>. In the absence of that stricture, a bareword is treated as if quotes were around it.</dd>
<dt>base class</dt>
<dd> A generic <code>object</code> type; that is, a <code>class</code> from which other, more specific classes are derived genetically by <code>inheritance</code>. Also called a “superclass” by people who respect their ancestors.</dd>
<dt>big-endian</dt>
<dd> From Swift: someone who eats eggs big end first. Also used of computers that store the most significant <code>byte</code> of a word at a lower byte address than the least significant byte. Often considered superior to little-endian machines. See also <code>little-endian</code>.</dd>
<dt>binary</dt>
<dd> Having to do with numbers represented in base 2. That means there’s basically two numbers: 0 and 1. Also used to describe a file of “nontext”, presumably because such a file makes full use of all the binary bits in its bytes. With the advent of <code>Unicode</code>, this distinction, already suspect, loses even more of its meaning.</dd>
<dt>binary operator</dt>
<dd> An <code>operator</code> that takes two <code>operands</code>.</dd>
<dt>bind</dt>
<dd> To assign a specific <code>network address</code> to a <code>socket</code>.</dd>
<dt>bit</dt>
<dd> An integer in the range from 0 to 1, inclusive. The smallest possible unit of information storage. An eighth of a <code>byte</code> or of a dollar. (The term “Pieces of Eight” comes from being able to split the old Spanish dollar into 8 bits, each of which still counted for money. That’s why a 25- cent piece today is still “two bits”.)</dd>
<dt>bit shift</dt>
<dd> The movement of bits left or right in a computer word, which has the effect of multiplying or dividing by a power of 2.</dd>
<dt>bit string</dt>
<dd> A sequence of <code>bits</code> that is actually being thought of as a sequence of bits, for once.</dd>
<dt>bless</dt>
<dd> In corporate life, to grant official approval to a thing, as in, “The VP of Engineering has blessed our WebCruncher project.” Similarly, in Perl, to grant official approval to a <code>referent</code> so that it can function as an <code>object</code>, such as a WebCruncher object. See the <tt>&quot;bless&quot;</tt> function in Camel chapter 27, “Functions”.</dd>
<dt>block</dt>
<dd> What a <code>process</code> does when it has to wait for something: “My process blocked waiting for the disk.” As an unrelated noun, it refers to a large chunk of data, of a size that the <code>operating system</code> likes to deal with (normally a power of 2 such as 512 or 8192). Typically refers to a chunk of data that’s coming from or going to a disk file.</dd>
<dt>BLOCK</dt>
<dd> A syntactic construct consisting of a sequence of Perl <code>statements</code> that is delimited by braces. The <tt>&quot;if&quot;</tt> and <tt>&quot;while&quot;</tt> statements are defined in terms of <i></i>&quot;BLOCK&quot;<i></i>s, for instance. Sometimes we also say “block” to mean a lexical scope; that is, a sequence of statements that acts like a <i></i>&quot;BLOCK&quot;<i></i>, such as within an <tt>&quot;eval&quot;</tt> or a file, even though the statements aren’t delimited by braces.</dd>
<dt>block buffering</dt>
<dd> A method of making input and output efficient by passing one <code>block</code> at a time. By default, Perl does block buffering to disk files. See <code>buffer</code> and <code>command buffering</code>.</dd>
<dt>Boolean</dt>
<dd> A value that is either <code>true</code> or <code>false</code>.</dd>
<dt>Boolean context</dt>
<dd> A special kind of <code>scalar context</code> used in conditionals to decide whether the <code>scalar value</code> returned by an expression is <code>true</code> or <code>false</code>. Does not evaluate as either a string or a number. See <code>context</code>.</dd>
<dt>breakpoint</dt>
<dd> A spot in your program where you’ve told the debugger to stop <code>execution</code> so you can poke around and see whether anything is wrong yet.</dd>
<dt>broadcast</dt>
<dd> To send a <code>datagram</code> to multiple destinations simultaneously.</dd>
<dt>BSD</dt>
<dd> A psychoactive drug, popular in the ’80s, probably developed at UC Berkeley or thereabouts. Similar in many ways to the prescription-only medication called “System V”, but infinitely more useful. (Or, at least, more fun.) The full chemical name is “Berkeley Standard Distribution”.</dd>
<dt>bucket</dt>
<dd> A location in a <code>hash table</code> containing (potentially) multiple entries whose keys “hash” to the same hash value according to its hash function. (As internal policy, you don’t have to worry about it unless you’re into internals, or policy.)</dd>
<dt>buffer</dt>
<dd> A temporary holding location for data. Data that are <code>Block buffering</code> means that the data is passed on to its destination whenever the buffer is full. <code>Line buffering</code> means that it’s passed on whenever a complete line is received. <code>Command buffering</code> means that it’s passed every time you do a <tt>&quot;print&quot;</tt> command (or equivalent). If your output is unbuffered, the system processes it one byte at a time without the use of a holding area. This can be rather inefficient.</dd>
<dt>built-in</dt>
<dd> A <code>function</code> that is predefined in the language. Even when hidden by <code>overriding</code>, you can always get at a built- in function by <code>qualifying</code> its name with the <tt>&quot;CORE::&quot;</tt> pseudopackage.</dd>
<dt>bundle</dt>
<dd> A group of related modules on <code>CPAN</code>. (Also sometimes refers to a group of command-line switches grouped into one <code>switch cluster</code>.)</dd>
<dt>byte</dt>
<dd> A piece of data worth eight <code>bits</code> in most places.</dd>
<dt>bytecode</dt>
<dd> A pidgin-like lingo spoken among ’droids when they don’t wish to reveal their orientation (see <code>endian</code>). Named after some similar languages spoken (for similar reasons) between compilers and interpreters in the late 20ᵗʰ century. These languages are characterized by representing everything as a nonarchitecture-dependent sequence of bytes.</dd></dl>
<h3>C</h3>
<dl>
<dt>C</dt>
<dd> A language beloved by many for its inside-out <code>type</code> definitions, inscrutable <code>precedence</code> rules, and heavy <code>overloading</code> of the function-call mechanism. (Well, actually, people first switched to C because they found lowercase identifiers easier to read than upper.) Perl is written in C, so it’s not surprising that Perl borrowed a few ideas from it.</dd>
<dt>cache</dt>
<dd> A data repository. Instead of computing expensive answers several times, compute it once and save the result.</dd>
<dt>callback</dt>
<dd> A <code>handler</code> that you register with some other part of your program in the hope that the other part of your program will <code>trigger</code> your handler when some event of interest transpires.</dd>
<dt>call by reference</dt>
<dd> An <code>argument</code>-passing mechanism in which the <code>formal arguments</code> refer directly to the <code>actual arguments</code>, and the <code>subroutine</code> can change the actual arguments by changing the formal arguments. That is, the formal argument is an <code>alias</code> for the actual argument. See also <code>call by value</code>.</dd>
<dt>call by value</dt>
<dd> An <code>argument</code>-passing mechanism in which the <code>formal arguments</code> refer to a copy of the <code>actual arguments</code>, and the <code>subroutine</code> cannot change the actual arguments by changing the formal arguments. See also <code>call by reference</code>.</dd>
<dt>canonical</dt>
<dd> Reduced to a standard form to facilitate comparison.</dd>
<dt>capture variables</dt>
<dd> The variables—such as <tt>$1</tt> and <tt>$2</tt>, and <tt>&quot;%+&quot;</tt> and <tt>&quot;%– &quot;</tt>—that hold the text remembered in a pattern match. See Camel chapter 5, “Pattern Matching”.</dd>
<dt>capturing</dt>
<dd> The use of parentheses around a <code>subpattern</code> in a <code>regular expression</code> to store the matched <code>substring</code> as a <code>backreference</code>. (Captured strings are also returned as a list in <code>list context</code>.) See Camel chapter 5, “Pattern Matching”.</dd>
<dt>cargo cult</dt>
<dd> Copying and pasting code without understanding it, while superstitiously believing in its value. This term originated from preindustrial cultures dealing with the detritus of explorers and colonizers of technologically advanced cultures. See <i>The Gods Must Be Crazy</i>.</dd>
<dt>case</dt>
<dd> A property of certain characters. Originally, typesetter stored capital letters in the upper of two cases and small letters in the lower one. Unicode recognizes three cases: <code>lowercase</code> (<code>character property</code> <tt>&quot;\p{lower}&quot;</tt>), <code>titlecase</code> (<tt>&quot;\p{title}&quot;</tt>), and <code>uppercase</code> (<tt>&quot;\p{upper}&quot;</tt>). A fourth casemapping called <code>foldcase</code> is not itself a distinct case, but it is used internally to implement <code>casefolding</code>. Not all letters have case, and some nonletters have case.</dd>
<dt>casefolding</dt>
<dd> Comparing or matching a string case-insensitively. In Perl, it is implemented with the <tt>&quot;/i&quot;</tt> pattern modifier, the <tt>&quot;fc&quot;</tt> function, and the <tt>&quot;\F&quot;</tt> double-quote translation escape.</dd>
<dt>casemapping</dt>
<dd> The process of converting a string to one of the four Unicode <code>casemaps</code>; in Perl, it is implemented with the <tt>&quot;fc&quot;</tt>, <tt>&quot;lc&quot;</tt>, <tt>&quot;ucfirst&quot;</tt>, and <tt>&quot;uc&quot;</tt> functions.</dd>
<dt>character</dt>
<dd> The smallest individual element of a string. Computers store characters as integers, but Perl lets you operate on them as text. The integer used to represent a particular character is called that character’s <code>codepoint</code>.</dd>
<dt>character class</dt>
<dd> A square-bracketed list of characters used in a <code>regular expression</code> to indicate that any character of the set may occur at a given point. Loosely, any predefined set of characters so used.</dd>
<dt>character property</dt>
<dd> A predefined <code>character class</code> matchable by the <tt>&quot;\p&quot;</tt> or <tt>&quot;\P&quot;</tt> <code>metasymbol</code>. <code>Unicode</code> defines hundreds of standard properties for every possible codepoint, and Perl defines a few of its own, too.</dd>
<dt>circumfix operator</dt>
<dd> An <code>operator</code> that surrounds its <code>operand</code>, like the angle operator, or parentheses, or a hug.</dd>
<dt>class</dt>
<dd> A user-defined <code>type</code>, implemented in Perl via a <code>package</code> that provides (either directly or by inheritance) <code>methods</code> (that is, <code>subroutines</code>) to handle <code>instances</code> of the class (its <code>objects</code>). See also <code>inheritance</code>.</dd>
<dt>class method</dt>
<dd> A <code>method</code> whose <code>invocant</code> is a <code>package</code> name, not an <code>object</code> reference. A method associated with the class as a whole. Also see <code>instance method</code>.</dd>
<dt>client</dt>
<dd> In networking, a <code>process</code> that initiates contact with a <code>server</code> process in order to exchange data and perhaps receive a service.</dd>
<dt>closure</dt>
<dd> An <code>anonymous</code> subroutine that, when a reference to it is generated at runtime, keeps track of the identities of externally visible <code>lexical variables</code>, even after those lexical variables have supposedly gone out of <code>scope</code>. They’re called “closures” because this sort of behavior gives mathematicians a sense of closure.</dd>
<dt>cluster</dt>
<dd> A parenthesized <code>subpattern</code> used to group parts of a <code>regular expression</code> into a single <code>atom</code>.</dd>
<dt>CODE</dt>
<dd> The word returned by the <tt>&quot;ref&quot;</tt> function when you apply it to a reference to a subroutine. See also <code>CV</code>.</dd>
<dt>code generator</dt>
<dd> A system that writes code for you in a low-level language, such as code to implement the backend of a compiler. See <code>program generator</code>.</dd>
<dt>codepoint</dt>
<dd> The integer a computer uses to represent a given character. ASCII codepoints are in the range 0 to 127; Unicode codepoints are in the range 0 to 0x1F_FFFF; and Perl codepoints are in the range 0 to 2³²−1 or 0 to 2⁶⁴−1, depending on your native integer size. In Perl Culture, sometimes called <code>ordinals</code>.</dd>
<dt>code subpattern</dt>
<dd> A <code>regular expression</code> subpattern whose real purpose is to execute some Perl code—for example, the <tt>&quot;(?{...})&quot;</tt> and <tt>&quot;(??{...})&quot;</tt> subpatterns.</dd>
<dt>collating sequence</dt>
<dd> The order into which <code>characters</code> sort. This is used by <code>string</code> comparison routines to decide, for example, where in this glossary to put “collating sequence”.</dd>
<dt>co-maintainer</dt>
<dd> A person with permissions to index a <code>namespace</code> in <code>PAUSE</code>. Anyone can upload any namespace, but only primary and co-maintainers get their contributions indexed.</dd>
<dt>combining character</dt>
<dd> Any character with the General Category of Combining Mark (<tt>&quot;\p{GC=M}&quot;</tt>), which may be spacing or nonspacing. Some are even invisible. A sequence of combining characters following a grapheme base character together make up a single user-visible character called a <code>grapheme</code>. Most but not all diacritics are combining characters, and vice versa.</dd>
<dt>command</dt>
<dd> In <code>shell</code> programming, the syntactic combination of a program name and its arguments. More loosely, anything you type to a shell (a command interpreter) that starts it doing something. Even more loosely, a Perl <code>statement</code>, which might start with a <code>label</code> and typically ends with a semicolon.</dd>
<dt>command buffering</dt>
<dd> A mechanism in Perl that lets you store up the output of each Perl <code>command</code> and then flush it out as a single request to the <code>operating system</code>. It’s enabled by setting the <tt>$|</tt> (<tt>$AUTOFLUSH</tt>) variable to a true value. It’s used when you don’t want data sitting around, not going where it’s supposed to, which may happen because the default on a <code>file</code> or <code>pipe</code> is to use <code>block buffering</code>.</dd>
<dt>command-line arguments</dt>
<dd> The <code>values</code> you supply along with a program name when you tell a <code>shell</code> to execute a <code>command</code>. These values are passed to a Perl program through <tt>@ARGV</tt>.</dd>
<dt>command name</dt>
<dd> The name of the program currently executing, as typed on the command line. In C, the <code>command</code> name is passed to the program as the first command-line argument. In Perl, it comes in separately as <tt>$0</tt>.</dd>
<dt>comment</dt>
<dd> A remark that doesn’t affect the meaning of the program. In Perl, a comment is introduced by a <tt>&quot;#&quot;</tt> character and continues to the end of the line.</dd>
<dt>compilation unit</dt>
<dd> The <code>file</code> (or <code>string</code>, in the case of <tt>&quot;eval&quot;</tt>) that is currently being <code>compiled</code>.</dd>
<dt>compile</dt>
<dd> The process of turning source code into a machine-usable form. See <code>compile phase</code>.</dd>
<dt>compile phase</dt>
<dd> Any time before Perl starts running your main program. See also <code>run phase</code>. Compile phase is mostly spent in <code>compile time</code>, but may also be spent in <code>runtime</code> when <tt>&quot;BEGIN&quot;</tt> blocks, <tt>&quot;use&quot;</tt> or <tt>&quot;no&quot;</tt> declarations, or constant subexpressions are being evaluated. The startup and import code of any <tt>&quot;use&quot;</tt> declaration is also run during compile phase.</dd>
<dt>compiler</dt>
<dd> Strictly speaking, a program that munches up another program and spits out yet another file containing the program in a “more executable” form, typically containing native machine instructions. The <i>perl</i> program is not a compiler by this definition, but it does contain a kind of compiler that takes a program and turns it into a more executable form (<code>syntax trees</code>) within the <i>perl</i> process itself, which the <code>interpreter</code> then interprets. There are, however, extension <code>modules</code> to get Perl to act more like a “real” compiler. See Camel chapter 16, “Compiling”.</dd>
<dt>compile time</dt>
<dd> The time when Perl is trying to make sense of your code, as opposed to when it thinks it knows what your code means and is merely trying to do what it thinks your code says to do, which is <code>runtime</code>.</dd>
<dt>composer</dt>
<dd> A “constructor” for a <code>referent</code> that isn’t really an <code>object</code>, like an anonymous array or a hash (or a sonata, for that matter). For example, a pair of braces acts as a composer for a hash, and a pair of brackets acts as a composer for an array. See the section “Creating References” in Camel chapter 8, “References”.</dd>
<dt>concatenation</dt>
<dd> The process of gluing one cat’s nose to another cat’s tail. Also a similar operation on two <code>strings</code>.</dd>
<dt>conditional</dt>
<dd> Something “iffy”. See <code>Boolean context</code>.</dd>
<dt>connection</dt>
<dd> In telephony, the temporary electrical circuit between the caller’s and the callee’s phone. In networking, the same kind of temporary circuit between a <code>client</code> and a <code>server</code>.</dd>
<dt>construct</dt>
<dd> As a noun, a piece of syntax made up of smaller pieces. As a transitive verb, to create an <code>object</code> using a <code>constructor</code>.</dd>
<dt>constructor</dt>
<dd> Any <code>class method</code>, <code>instance</code>, or <code>subroutine</code> that composes, initializes, blesses, and returns an <code>object</code>. Sometimes we use the term loosely to mean a <code>composer</code>.</dd>
<dt>context</dt>
<dd> The surroundings or environment. The context given by the surrounding code determines what kind of data a particular <code>expression</code> is expected to return. The three primary contexts are <code>list context</code>, <code>scalar</code>, and <code>void context</code>. Scalar context is sometimes subdivided into <code>Boolean context</code>, <code>numeric context</code>, <code>string context</code>, and <code>void context</code>. There’s also a “don’t care” context (which is dealt with in Camel chapter 2, “Bits and Pieces”, if you care).</dd>
<dt>continuation</dt>
<dd> The treatment of more than one physical <code>line</code> as a single logical line. <code>Makefile</code> lines are continued by putting a backslash before the <code>newline</code>. Mail headers, as defined by RFC 822, are continued by putting a space or tab <i>after</i> the newline. In general, lines in Perl do not need any form of continuation mark, because <code>whitespace</code> (including newlines) is gleefully ignored. Usually.</dd>
<dt>core dump</dt>
<dd> The corpse of a <code>process</code>, in the form of a file left in the <code>working directory</code> of the process, usually as a result of certain kinds of fatal errors.</dd>
<dt>CPAN</dt>
<dd> The Comprehensive Perl Archive Network. (See the Camel Preface and Camel chapter 19, “CPAN” for details.)</dd>
<dt>C preprocessor</dt>
<dd> The typical C compiler’s first pass, which processes lines beginning with <tt>&quot;#&quot;</tt> for conditional compilation and macro definition, and does various manipulations of the program text based on the current definitions. Also known as <i><a href="/docs/linux/man/1-cpp/">cpp</a></i>(1).</dd>
<dt>cracker</dt>
<dd> Someone who breaks security on computer systems. A cracker may be a true <code>hacker</code> or only a <code>script kiddie</code>.</dd>
<dt>currently selected output channel</dt>
<dd> The last <code>filehandle</code> that was designated with <tt>&quot;select(FILEHANDLE)&quot;</tt>; <tt>&quot;STDOUT&quot;</tt>, if no filehandle has been selected.</dd>
<dt>current package</dt>
<dd> The <code>package</code> in which the current statement is <code>compiled</code>. Scan backward in the text of your program through the current <code>lexical scope</code> or any enclosing lexical scopes until you find a package declaration. That’s your current package name.</dd>
<dt>current working directory</dt>
<dd> See <code>working directory</code>.</dd>
<dt>CV</dt>
<dd> In academia, a curriculum vitæ, a fancy kind of résumé. In Perl, an internal “code value” typedef holding a <code>subroutine</code>. The <tt>&quot;CV&quot;</tt> type is a subclass of <code>SV</code>.</dd></dl>
<h3>D</h3>
<dl>
<dt>dangling statement</dt>
<dd> A bare, single <code>statement</code>, without any braces, hanging off an <tt>&quot;if&quot;</tt> or <tt>&quot;while&quot;</tt> conditional. C allows them. Perl doesn’t.</dd>
<dt>datagram</dt>
<dd> A packet of data, such as a <code>UDP</code> message, that (from the viewpoint of the programs involved) can be sent independently over the network. (In fact, all packets are sent independently at the <code>IP</code> level, but <code>stream</code> protocols such as <code>TCP</code> hide this from your program.)</dd>
<dt>data structure</dt>
<dd> How your various pieces of data relate to each other and what shape they make when you put them all together, as in a rectangular table or a triangular tree.</dd>
<dt>data type</dt>
<dd> A set of possible values, together with all the operations that know how to deal with those values. For example, a numeric data type has a certain set of numbers that you can work with, as well as various mathematical operations that you can do on the numbers, but would make little sense on, say, a string such as <tt>&quot;Kilroy&quot;</tt>. Strings have their own operations, such as <code>concatenation</code>. Compound types made of a number of smaller pieces generally have operations to compose and decompose them, and perhaps to rearrange them. <code>Objects</code> that model things in the real world often have operations that correspond to real activities. For instance, if you model an elevator, your elevator object might have an <tt>&quot;open_door&quot;</tt> <code>method</code>.</dd>
<dt>DBM</dt>
<dd> Stands for “Database Management” routines, a set of routines that emulate an <code>associative array</code> using disk files. The routines use a dynamic hashing scheme to locate any entry with only two disk accesses. DBM files allow a Perl program to keep a persistent <code>hash</code> across multiple invocations. You can <tt>&quot;tie&quot;</tt> your hash variables to various DBM implementations.</dd>
<dt>declaration</dt>
<dd> An <code>assertion</code> that states something exists and perhaps describes what it’s like, without giving any commitment as to how or where you’ll use it. A declaration is like the part of your recipe that says, “two cups flour, one large egg, four or five tadpoles…” See <code>statement</code> for its opposite. Note that some declarations also function as statements. Subroutine declarations also act as definitions if a body is supplied.</dd>
<dt>declarator</dt>
<dd> Something that tells your program what sort of variable you’d like. Perl doesn’t require you to declare variables, but you can use <tt>&quot;my&quot;</tt>, <tt>&quot;our&quot;</tt>, or <tt>&quot;state&quot;</tt> to denote that you want something other than the default.</dd>
<dt>decrement</dt>
<dd> To subtract a value from a variable, as in “decrement <tt>$x</tt>” (meaning to remove 1 from its value) or “decrement <tt>$x</tt> by 3”.</dd>
<dt>default</dt>
<dd> A <code>value</code> chosen for you if you don’t supply a value of your own.</dd>
<dt>defined</dt>
<dd> Having a meaning. Perl thinks that some of the things people try to do are devoid of meaning; in particular, making use of variables that have never been given a <code>value</code> and performing certain operations on data that isn’t there. For example, if you try to read data past the end of a file, Perl will hand you back an undefined value. See also <code>false</code> and the <tt>&quot;defined&quot;</tt> entry in Camel chapter 27, “Functions”.</dd>
<dt>delimiter</dt>
<dd> A <code>character</code> or <code>string</code> that sets bounds to an arbitrarily sized textual object, not to be confused with a <code>separator</code> or <code>terminator</code>. “To delimit” really just means “to surround” or “to enclose” (like these parentheses are doing).</dd>
<dt>dereference</dt>
<dd> A fancy computer science term meaning “to follow a <code>reference</code> to what it points to”. The “de” part of it refers to the fact that you’re taking away one level of <code>indirection</code>.</dd>
<dt>derived class</dt>
<dd> A <code>class</code> that defines some of its <code>methods</code> in terms of a more generic class, called a <code>base class</code>. Note that classes aren’t classified exclusively into base classes or derived classes: a class can function as both a derived class and a base class simultaneously, which is kind of classy.</dd>
<dt>descriptor</dt>
<dd> See <code>file descriptor</code>.</dd>
<dt>destroy</dt>
<dd> To deallocate the memory of a <code>referent</code> (first triggering its <tt>&quot;DESTROY&quot;</tt> method, if it has one).</dd>
<dt>destructor</dt>
<dd> A special <code>method</code> that is called when an <code>object</code> is thinking about <code>destroying</code> itself. A Perl program’s <tt>&quot;DESTROY&quot;</tt> method doesn’t do the actual destruction; Perl just <code>triggers</code> the method in case the <code>class</code> wants to do any associated cleanup.</dd>
<dt>device</dt>
<dd> A whiz-bang hardware gizmo (like a disk or tape drive or a modem or a joystick or a mouse) attached to your computer, which the <code>operating system</code> tries to make look like a <code>file</code> (or a bunch of files). Under Unix, these fake files tend to live in the <i>/dev</i> directory.</dd>
<dt>directive</dt>
<dd> A <code>pod</code> directive. See Camel chapter 23, “Plain Old Documentation”.</dd>
<dt>directory</dt>
<dd> A special file that contains other files. Some <code>operating systems</code> call these “folders”, “drawers”, “catalogues”, or “catalogs”.</dd>
<dt>directory handle</dt>
<dd> A name that represents a particular instance of opening a directory to read it, until you close it. See the <tt>&quot;opendir&quot;</tt> function.</dd>
<dt>discipline</dt>
<dd> Some people need this and some people avoid it. For Perl, it’s an old way to say <code>I/O layer</code>.</dd>
<dt>dispatch</dt>
<dd> To send something to its correct destination. Often used metaphorically to indicate a transfer of programmatic control to a destination selected algorithmically, often by lookup in a table of function <code>references</code> or, in the case of object <code>methods</code>, by traversing the inheritance tree looking for the most specific definition for the method.</dd>
<dt>distribution</dt>
<dd> A standard, bundled release of a system of software. The default usage implies source code is included. If that is not the case, it will be called a “binary-only” distribution.</dd>
<dt>dual-lived</dt>
<dd> Some modules live both in the <code>Standard Library</code> and on <code>CPAN</code>. These modules might be developed on two tracks as people modify either version. The trend currently is to untangle these situations.</dd>
<dt>dweomer</dt>
<dd> An enchantment, illusion, phantasm, or jugglery. Said when Perl’s magical <code>dwimmer</code> effects don’t do what you expect, but rather seem to be the product of arcane <i>dweomercraft</i>, sorcery, or wonder working. [From Middle English.]</dd>
<dt>dwimmer</dt>
<dd> DWIM is an acronym for “Do What I Mean”, the principle that something should just do what you want it to do without an undue amount of fuss. A bit of code that does “dwimming” is a “dwimmer”. Dwimming can require a great deal of behind-the-scenes magic, which (if it doesn’t stay properly behind the scenes) is called a <code>dweomer</code> instead.</dd>
<dt>dynamic scoping</dt>
<dd> Dynamic scoping works over a <code>dynamic scope</code>, making variables visible throughout the rest of the <code>block</code> in which they are first used and in any <code>subroutines</code> that are called by the rest of the block. Dynamically scoped variables can have their values temporarily changed (and implicitly restored later) by a <tt>&quot;local&quot;</tt> operator. (Compare <code>lexical scoping</code>.) Used more loosely to mean how a subroutine that is in the middle of calling another subroutine “contains” that subroutine at <code>runtime</code>.</dd></dl>
<h3>E</h3>
<dl>
<dt>eclectic</dt>
<dd> Derived from many sources. Some would say <i>too</i> many.</dd>
<dt>element</dt>
<dd> A basic building block. When you’re talking about an <code>array</code>, it’s one of the items that make up the array.</dd>
<dt>embedding</dt>
<dd> When something is contained in something else, particularly when that might be considered surprising: “I’ve embedded a complete Perl interpreter in my editor!”</dd>
<dt>empty subclass test</dt>
<dd> The notion that an empty <code>derived class</code> should behave exactly like its <code>base class</code>.</dd>
<dt>encapsulation</dt>
<dd> The veil of abstraction separating the <code>interface</code> from the <code>implementation</code> (whether enforced or not), which mandates that all access to an <code>object</code>’s state be through <code>methods</code> alone.</dd>
<dt>endian</dt>
<dd> See <code>little-endian</code> and <code>big-endian</code>.</dd>
<dt>en passant</dt>
<dd> When you change a <code>value</code> as it is being copied. [From French “in passing”, as in the exotic pawn-capturing maneuver in chess.]</dd>
<dt>environment</dt>
<dd> The collective set of <code>environment variables</code> your <code>process</code> inherits from its parent. Accessed via <tt>%ENV</tt>.</dd>
<dt>environment variable</dt>
<dd> A mechanism by which some high-level agent such as a user can pass its preferences down to its future offspring (child <code>processes</code>, grandchild processes, great-grandchild processes, and so on). Each environment variable is a <code>key</code>/<code>value</code> pair, like one entry in a <code>hash</code>.</dd>
<dt>EOF</dt>
<dd> End of File. Sometimes used metaphorically as the terminating string of a <code>here document</code>.</dd>
<dt>errno</dt>
<dd> The error number returned by a <code>syscall</code> when it fails. Perl refers to the error by the name <tt>$!</tt> (or <tt>$OS_ERROR</tt> if you use the English module).</dd>
<dt>error</dt>
<dd> See <code>exception</code> or <code>fatal error</code>.</dd>
<dt>escape sequence</dt>
<dd> See <code>metasymbol</code>.</dd>
<dt>exception</dt>
<dd> A fancy term for an error. See <code>fatal error</code>.</dd>
<dt>exception handling</dt>
<dd> The way a program responds to an error. The exception-handling mechanism in Perl is the <tt>&quot;eval&quot;</tt> operator.</dd>
<dt>exec</dt>
<dd> To throw away the current <code>process</code>’s program and replace it with another, without exiting the process or relinquishing any resources held (apart from the old memory image).</dd>
<dt>executable file</dt>
<dd> A <code>file</code> that is specially marked to tell the <code>operating system</code> that it’s okay to run this file as a program. Usually shortened to “executable”.</dd>
<dt>execute</dt>
<dd> To run a <code>program</code> or <code>subroutine</code>. (Has nothing to do with the <tt>&quot;kill&quot;</tt> built-in, unless you’re trying to run a <code>signal handler</code>.)</dd>
<dt>execute bit</dt>
<dd> The special mark that tells the operating system it can run this program. There are actually three execute bits under Unix, and which bit gets used depends on whether you own the file singularly, collectively, or not at all.</dd>
<dt>exit status</dt>
<dd> See <code>status</code>.</dd>
<dt>exploit</dt>
<dd> Used as a noun in this case, this refers to a known way to compromise a program to get it to do something the author didn’t intend. Your task is to write unexploitable programs.</dd>
<dt>export</dt>
<dd> To make symbols from a <code>module</code> available for <code>import</code> by other modules.</dd>
<dt>expression</dt>
<dd> Anything you can legally say in a spot where a <code>value</code> is required. Typically composed of <code>literals</code>, <code>variables</code>, <code>operators</code>, <code>functions</code>, and <code>subroutine</code> calls, not necessarily in that order.</dd>
<dt>extension</dt>
<dd> A Perl module that also pulls in <code>compiled</code> C or C++ code. More generally, any experimental option that can be <code>compiled</code> into Perl, such as multithreading.</dd></dl>
<h3>F</h3>
<dl>
<dt>false</dt>
<dd> In Perl, any value that would look like <tt>&quot;&quot;</tt> or <tt>&quot;0&quot;</tt> if evaluated in a string context. Since undefined values evaluate to <tt>&quot;&quot;</tt>, all undefined values are false, but not all false values are undefined.</dd>
<dt>FAQ</dt>
<dd> Frequently Asked Question (although not necessarily frequently answered, especially if the answer appears in the Perl FAQ shipped standard with Perl).</dd>
<dt>fatal error</dt>
<dd> An uncaught <code>exception</code>, which causes termination of the <code>process</code> after printing a message on your <code>standard error</code> stream. Errors that happen inside an <tt>&quot;eval&quot;</tt> are not fatal. Instead, the <tt>&quot;eval&quot;</tt> terminates after placing the exception message in the <tt>$@</tt> (<tt>$EVAL_ERROR</tt>) variable. You can try to provoke a fatal error with the <tt>&quot;die&quot;</tt> operator (known as throwing or raising an exception), but this may be caught by a dynamically enclosing <tt>&quot;eval&quot;</tt>. If not caught, the <tt>&quot;die&quot;</tt> becomes a fatal error.</dd>
<dt>feeping creaturism</dt>
<dd> A spoonerism of “creeping featurism”, noting the biological urge to add just one more feature to a program.</dd>
<dt>field</dt>
<dd> A single piece of numeric or string data that is part of a longer <code>string</code>, <code>record</code>, or <code>line</code>. Variable-width fields are usually split up by <code>separators</code> (so use <tt>&quot;split&quot;</tt> to extract the fields), while fixed-width fields are usually at fixed positions (so use <tt>&quot;unpack&quot;</tt>). <code>Instance variables</code> are also known as “fields”.</dd>
<dt>FIFO</dt>
<dd> First In, First Out. See also <code>LIFO</code>. Also a nickname for a <code>named pipe</code>.</dd>
<dt>file</dt>
<dd> A named collection of data, usually stored on disk in a <code>directory</code> in a <code>filesystem</code>. Roughly like a document, if you’re into office metaphors. In modern filesystems, you can actually give a file more than one name. Some files have special properties, like directories and devices.</dd>
<dt>file descriptor</dt>
<dd> The little number the <code>operating system</code> uses to keep track of which opened <code>file</code> you’re talking about. Perl hides the file descriptor inside a <code>standard I/O</code> stream and then attaches the stream to a <code>filehandle</code>.</dd>
<dt>fileglob</dt>
<dd> A “wildcard” match on <code>filenames</code>. See the <tt>&quot;glob&quot;</tt> function.</dd>
<dt>filehandle</dt>
<dd> An identifier (not necessarily related to the real name of a file) that represents a particular instance of opening a file, until you close it. If you’re going to open and close several different files in succession, it’s fine to open each of them with the same filehandle, so you don’t have to write out separate code to process each file.</dd>
<dt>filename</dt>
<dd> One name for a file. This name is listed in a <code>directory</code>. You can use it in an <tt>&quot;open&quot;</tt> to tell the <code>operating system</code> exactly which file you want to open, and associate the file with a <code>filehandle</code>, which will carry the subsequent identity of that file in your program, until you close it.</dd>
<dt>filesystem</dt>
<dd> A set of <code>directories</code> and <code>files</code> residing on a partition of the disk. Sometimes known as a “partition”. You can change the file’s name or even move a file around from directory to directory within a filesystem without actually moving the file itself, at least under Unix.</dd>
<dt>file test operator</dt>
<dd> A built-in unary operator that you use to determine whether something is <code>true</code> about a file, such as <tt>&quot;–o $filename&quot;</tt> to test whether you’re the owner of the file.</dd>
<dt>filter</dt>
<dd> A program designed to take a <code>stream</code> of input and transform it into a stream of output.</dd>
<dt>first-come</dt>
<dd> The first <code>PAUSE</code> author to upload a <code>namespace</code> automatically becomes the <code>primary maintainer</code> for that namespace. The “first come” permissions distinguish a <code>primary maintainer</code> who was assigned that role from one who received it automatically.</dd>
<dt>flag</dt>
<dd> We tend to avoid this term because it means so many things. It may mean a command-line <code>switch</code> that takes no argument itself (such as Perl’s <tt>&quot;–n&quot;</tt> and <tt>&quot;–p&quot;</tt> flags) or, less frequently, a single-bit indicator (such as the <tt>&quot;O_CREAT&quot;</tt> and <tt>&quot;O_EXCL&quot;</tt> flags used in <tt>&quot;sysopen&quot;</tt>). Sometimes informally used to refer to certain regex modifiers.</dd>
<dt>floating point</dt>
<dd> A method of storing numbers in “scientific notation”, such that the precision of the number is independent of its magnitude (the decimal point “floats”). Perl does its numeric work with floating-point numbers (sometimes called “floats”) when it can’t get away with using <code>integers</code>. Floating-point numbers are mere approximations of real numbers.</dd>
<dt>flush</dt>
<dd> The act of emptying a <code>buffer</code>, often before it’s full.</dd>
<dt>FMTEYEWTK</dt>
<dd> Far More Than Everything You Ever Wanted To Know. An exhaustive treatise on one narrow topic, something of a super-<code>FAQ</code>. See Tom for far more.</dd>
<dt>foldcase</dt>
<dd> The casemap used in Unicode when comparing or matching without regard to case. Comparing lower-, title-, or uppercase are all unreliable due to Unicode’s complex, one-to-many case mappings. Foldcase is a <code>lowercase</code> variant (using a partially decomposed <code>normalization</code> form for certain codepoints) created specifically to resolve this.</dd>
<dt>fork</dt>
<dd> To create a child <code>process</code> identical to the parent process at its moment of conception, at least until it gets ideas of its own. A thread with protected memory.</dd>
<dt>formal arguments</dt>
<dd> The generic names by which a <code>subroutine</code> knows its <code>arguments</code>. In many languages, formal arguments are always given individual names; in Perl, the formal arguments are just the elements of an array. The formal arguments to a Perl program are <tt>$ARGV[0]</tt>, <tt>$ARGV[1]</tt>, and so on. Similarly, the formal arguments to a Perl subroutine are <tt>$_[0]</tt>, <tt>$_[1]</tt>, and so on. You may give the arguments individual names by assigning the values to a <tt>&quot;my&quot;</tt> list. See also <code>actual arguments</code>.</dd>
<dt>format</dt>
<dd> A specification of how many spaces and digits and things to put somewhere so that whatever you’re printing comes out nice and pretty.</dd>
<dt>freely available</dt>
<dd> Means you don’t have to pay money to get it, but the copyright on it may still belong to someone else (like Larry).</dd>
<dt>freely redistributable</dt>
<dd> Means you’re not in legal trouble if you give a bootleg copy of it to your friends and we find out about it. In fact, we’d rather you gave a copy to all your friends.</dd>
<dt>freeware</dt>
<dd> Historically, any software that you give away, particularly if you make the source code available as well. Now often called <code>open source software</code>. Recently there has been a trend to use the term in contradistinction to <code>open source software</code>, to refer only to free software released under the Free Software Foundation’s GPL (General Public License), but this is difficult to justify etymologically.</dd>
<dt>function</dt>
<dd> Mathematically, a mapping of each of a set of input values to a particular output value. In computers, refers to a <code>subroutine</code> or <code>operator</code> that returns a <code>value</code>. It may or may not have input values (called <code>arguments</code>).</dd>
<dt>funny character</dt>
<dd> Someone like Larry, or one of his peculiar friends. Also refers to the strange prefixes that Perl requires as noun markers on its variables.</dd></dl>
<h3>G</h3>
<dl>
<dt>garbage collection</dt>
<dd> A misnamed feature—it should be called, “expecting your mother to pick up after you”. Strictly speaking, Perl doesn’t do this, but it relies on a reference-counting mechanism to keep things tidy. However, we rarely speak strictly and will often refer to the reference-counting scheme as a form of garbage collection. (If it’s any comfort, when your interpreter exits, a “real” garbage collector runs to make sure everything is cleaned up if you’ve been messy with circular references and such.)</dd>
<dt>GID</dt>
<dd> Group ID—in Unix, the numeric group ID that the <code>operating system</code> uses to identify you and members of your <code>group</code>.</dd>
<dt>glob</dt>
<dd> Strictly, the shell’s <tt>&quot;*&quot;</tt> character, which will match a “glob” of characters when you’re trying to generate a list of filenames. Loosely, the act of using globs and similar symbols to do pattern matching. See also <code>fileglob</code> and <code>typeglob</code>.</dd>
<dt>global</dt>
<dd> Something you can see from anywhere, usually used of <code>variables</code> and <code>subroutines</code> that are visible everywhere in your program. In Perl, only certain special variables are truly global—most variables (and all subroutines) exist only in the current <code>package</code>. Global variables can be declared with <tt>&quot;our&quot;</tt>. See “Global Declarations” in Camel chapter 4, “Statements and Declarations”.</dd>
<dt>global destruction</dt>
<dd> The <code>garbage collection</code> of globals (and the running of any associated object destructors) that takes place when a Perl <code>interpreter</code> is being shut down. Global destruction should not be confused with the Apocalypse, except perhaps when it should.</dd>
<dt>glue language</dt>
<dd> A language such as Perl that is good at hooking things together that weren’t intended to be hooked together.</dd>
<dt>granularity</dt>
<dd> The size of the pieces you’re dealing with, mentally speaking.</dd>
<dt>grapheme</dt>
<dd> A graphene is an allotrope of carbon arranged in a hexagonal crystal lattice one atom thick. A <code>grapheme</code>, or more fully, a <i>grapheme cluster string</i> is a single user-visible <code>character</code>, which may in turn be several characters (<code>codepoints</code>) long. For example, a carriage return plus a line feed is a single grapheme but two characters, while a “ȫ” is a single grapheme but one, two, or even three characters, depending on <code>normalization</code>.</dd>
<dt>greedy</dt>
<dd> A <code>subpattern</code> whose <code>quantifier</code> wants to match as many things as possible.</dd>
<dt>grep</dt>
<dd> Originally from the old Unix editor command for “Globally search for a Regular Expression and Print it”, now used in the general sense of any kind of search, especially text searches. Perl has a built-in <tt>&quot;grep&quot;</tt> function that searches a list for elements matching any given criterion, whereas the <code><a href="/docs/linux/man/1-grep/">grep</a></code>(1) program searches for lines matching a <code>regular expression</code> in one or more files.</dd>
<dt>group</dt>
<dd> A set of users of which you are a member. In some operating systems (like Unix), you can give certain file access permissions to other members of your group.</dd>
<dt>GV</dt>
<dd> An internal “glob value” typedef, holding a <code>typeglob</code>. The <tt>&quot;GV&quot;</tt> type is a subclass of <code>SV</code>.</dd></dl>
<h3>H</h3>
<dl>
<dt>hacker</dt>
<dd> Someone who is brilliantly persistent in solving technical problems, whether these involve golfing, fighting orcs, or programming. Hacker is a neutral term, morally speaking. Good hackers are not to be confused with evil <code>crackers</code> or clueless <code>script kiddies</code>. If you confuse them, we will presume that you are either evil or clueless.</dd>
<dt>handler</dt>
<dd> A <code>subroutine</code> or <code>method</code> that Perl calls when your program needs to respond to some internal event, such as a <code>signal</code>, or an encounter with an operator subject to <code>operator overloading</code>. See also <code>callback</code>.</dd>
<dt>hard reference</dt>
<dd> A <code>scalar</code> <code>value</code> containing the actual address of a <code>referent</code>, such that the referent’s <code>reference</code> count accounts for it. (Some hard references are held internally, such as the implicit reference from one of a <code>typeglob</code>’s variable slots to its corresponding referent.) A hard reference is different from a <code>symbolic reference</code>.</dd>
<dt>hash</dt>
<dd> An unordered association of <code>key</code>/<code>value</code> pairs, stored such that you can easily use a string <code>key</code> to look up its associated data <code>value</code>. This glossary is like a hash, where the word to be defined is the key and the definition is the value. A hash is also sometimes septisyllabically called an “associative array”, which is a pretty good reason for simply calling it a “hash” instead.</dd>
<dt>hash table</dt>
<dd> A data structure used internally by Perl for implementing associative arrays (hashes) efficiently. See also <code>bucket</code>.</dd>
<dt>header file</dt>
<dd> A file containing certain required definitions that you must include “ahead” of the rest of your program to do certain obscure operations. A C header file has a <i>.h</i> extension. Perl doesn’t really have header files, though historically Perl has sometimes used translated <i>.h</i> files with a <i>.ph</i> extension. See <tt>&quot;require&quot;</tt> in Camel chapter 27, “Functions”. (Header files have been superseded by the <code>module</code> mechanism.)</dd>
<dt>here document</dt>
<dd> So called because of a similar construct in <code>shells</code> that pretends that the <code>lines</code> following the <code>command</code> are a separate <code>file</code> to be fed to the command, up to some terminating string. In Perl, however, it’s just a fancy form of quoting.</dd>
<dt>hexadecimal</dt>
<dd> A number in base 16, “hex” for short. The digits for 10 through 15 are customarily represented by the letters <tt>&quot;a&quot;</tt> through <tt>&quot;f&quot;</tt>. Hexadecimal constants in Perl start with <tt>&quot;0x&quot;</tt>. See also the <tt>&quot;hex&quot;</tt> function in Camel chapter 27, “Functions”.</dd>
<dt>home directory</dt>
<dd> The directory you are put into when you log in. On a Unix system, the name is often placed into <tt>$ENV{HOME}</tt> or <tt>$ENV{LOGDIR}</tt> by <i>login</i>, but you can also find it with <tt>&quot;(get&quot;</tt><tt>&quot;pwuid($&lt;))[7]&quot;</tt>. (Some platforms do not have a concept of a home directory.)</dd>
<dt>host</dt>
<dd> The computer on which a program or other data resides.</dd>
<dt>hubris</dt>
<dd> Excessive pride, the sort of thing for which Zeus zaps you. Also the quality that makes you write (and maintain) programs that other people won’t want to say bad things about. Hence, the third great virtue of a programmer. See also <code>laziness</code> and <code>impatience</code>.</dd>
<dt>HV</dt>
<dd> Short for a “hash value” typedef, which holds Perl’s internal representation of a hash. The <tt>&quot;HV&quot;</tt> type is a subclass of <code>SV</code>.</dd></dl>
<h3>I</h3>
<dl>
<dt>identifier</dt>
<dd> A legally formed name for most anything in which a computer program might be interested. Many languages (including Perl) allow identifiers to start with an alphabetic character, and then contain alphabetics and digits. Perl also allows connector punctuation like the underscore character wherever it allows alphabetics. (Perl also has more complicated names, like <code>qualified</code> names.)</dd>
<dt>impatience</dt>
<dd> The anger you feel when the computer is being lazy. This makes you write programs that don’t just react to your needs, but actually anticipate them. Or at least that pretend to. Hence, the second great virtue of a programmer. See also <code>laziness</code> and <code>hubris</code>.</dd>
<dt>implementation</dt>
<dd> How a piece of code actually goes about doing its job. Users of the code should not count on implementation details staying the same unless they are part of the published <code>interface</code>.</dd>
<dt>import</dt>
<dd> To gain access to symbols that are exported from another module. See <tt>&quot;use&quot;</tt> in Camel chapter 27, “Functions”.</dd>
<dt>increment</dt>
<dd> To increase the value of something by 1 (or by some other number, if so specified).</dd>
<dt>indexing</dt>
<dd> In olden days, the act of looking up a <code>key</code> in an actual index (such as a phone book). But now it&#8217;s merely the act of using any kind of key or position to find the corresponding <code>value</code>, even if no index is involved. Things have degenerated to the point that Perl’s <tt>&quot;index&quot;</tt> function merely locates the position (index) of one string in another.</dd>
<dt>indirect filehandle</dt>
<dd> An <code>expression</code> that evaluates to something that can be used as a <code>filehandle</code>: a <code>string</code> (filehandle name), a <code>typeglob</code>, a typeglob <code>reference</code>, or a low-level <code>IO</code> object.</dd>
<dt>indirection</dt>
<dd> If something in a program isn’t the value you’re looking for but indicates where the value is, that’s indirection. This can be done with either <code>symbolic references</code> or <code>hard</code>.</dd>
<dt>indirect object</dt>
<dd> In English grammar, a short noun phrase between a verb and its direct object indicating the beneficiary or recipient of the action. In Perl, <tt>&quot;print STDOUT &quot;$foo
&quot;;&quot;</tt> can be understood as “verb indirect-object object”, where <tt>&quot;STDOUT&quot;</tt> is the recipient of the <tt>&quot;print&quot;</tt> action, and <tt>&quot;$foo&quot;</tt> is the object being printed. Similarly, when invoking a <code>method</code>, you might place the invocant in the dative slot between the method and its arguments: </dd>
<pre>
    $gollum = new Pathetic::Creature &quot;Sméagol&quot;;
    give $gollum &quot;Fisssssh!&quot;;
    give $gollum &quot;Precious!&quot;;
</pre>
<dt>indirect object slot</dt>
<dd> The syntactic position falling between a method call and its arguments when using the indirect object invocation syntax. (The slot is distinguished by the absence of a comma between it and the next argument.) <tt>&quot;STDERR&quot;</tt> is in the indirect object slot here: </dd>
<pre>
    print STDERR &quot;Awake! Awake! Fear, Fire, Foes! Awake!
&quot;;
</pre>
<dt>infix</dt>
<dd> An <code>operator</code> that comes in between its <code>operands</code>, such as multiplication in <tt>&quot;24 * 7&quot;</tt>.</dd>
<dt>inheritance</dt>
<dd> What you get from your ancestors, genetically or otherwise. If you happen to be a <code>class</code>, your ancestors are called <code>base classes</code> and your descendants are called <code>derived classes</code>. See <code>single inheritance</code> and <code>multiple inheritance</code>.</dd>
<dt>instance</dt>
<dd> Short for “an instance of a class”, meaning an <code>object</code> of that <code>class</code>.</dd>
<dt>instance data</dt>
<dd> See <code>instance variable</code>.</dd>
<dt>instance method</dt>
<dd> A <code>method</code> of an <code>object</code>, as opposed to a <code>class method</code>. </dd>
<p> A <code>method</code> whose <code>invocant</code> is an <code>object</code>, not a <code>package</code> name. Every object of a class shares all the methods of that class, so an instance method applies to all instances of the class, rather than applying to a particular instance. Also see <code>class method</code>.</p>
<dt>instance variable</dt>
<dd> An <code>attribute</code> of an <code>object</code>; data stored with the particular object rather than with the class as a whole.</dd>
<dt>integer</dt>
<dd> A number with no fractional (decimal) part. A counting number, like 1, 2, 3, and so on, but including 0 and the negatives.</dd>
<dt>interface</dt>
<dd> The services a piece of code promises to provide forever, in contrast to its <code>implementation</code>, which it should feel free to change whenever it likes.</dd>
<dt>interpolation</dt>
<dd> The insertion of a scalar or list value somewhere in the middle of another value, such that it appears to have been there all along. In Perl, variable interpolation happens in double-quoted strings and patterns, and list interpolation occurs when constructing the list of values to pass to a list operator or other such construct that takes a <i></i>&quot;LIST&quot;<i></i>.</dd>
<dt>interpreter</dt>
<dd> Strictly speaking, a program that reads a second program and does what the second program says directly without turning the program into a different form first, which is what <code>compilers</code> do. Perl is not an interpreter by this definition, because it contains a kind of compiler that takes a program and turns it into a more executable form (<code>syntax trees</code>) within the <i>perl</i> process itself, which the Perl <code>runtime</code> system then interprets.</dd>
<dt>invocant</dt>
<dd> The agent on whose behalf a <code>method</code> is invoked. In a <code>class</code> method, the invocant is a package name. In an <code>instance</code> method, the invocant is an object reference.</dd>
<dt>invocation</dt>
<dd> The act of calling up a deity, daemon, program, method, subroutine, or function to get it to do what you think it’s supposed to do. We usually “call” subroutines but “invoke” methods, since it sounds cooler.</dd>
<dt>I/O</dt>
<dd> Input from, or output to, a <code>file</code> or <code>device</code>.</dd>
<dt>IO</dt>
<dd> An internal I/O object. Can also mean <code>indirect object</code>.</dd>
<dt>I/O layer</dt>
<dd> One of the filters between the data and what you get as input or what you end up with as output.</dd>
<dt>IPA</dt>
<dd> India Pale Ale. Also the International Phonetic Alphabet, the standard alphabet used for phonetic notation worldwide. Draws heavily on Unicode, including many combining characters.</dd>
<dt>IP</dt>
<dd> Internet Protocol, or Intellectual Property.</dd>
<dt>IPC</dt>
<dd> Interprocess Communication.</dd>
<dt>is-a</dt>
<dd> A relationship between two <code>objects</code> in which one object is considered to be a more specific version of the other, generic object: “A camel is a mammal.” Since the generic object really only exists in a Platonic sense, we usually add a little abstraction to the notion of objects and think of the relationship as being between a generic <code>base class</code> and a specific <code>derived class</code>. Oddly enough, Platonic classes don’t always have Platonic relationships—see <code>inheritance</code>.</dd>
<dt>iteration</dt>
<dd> Doing something repeatedly.</dd>
<dt>iterator</dt>
<dd> A special programming gizmo that keeps track of where you are in something that you’re trying to iterate over. The <tt>&quot;foreach&quot;</tt> loop in Perl contains an iterator; so does a hash, allowing you to <tt>&quot;each&quot;</tt> through it.</dd>
<dt>IV</dt>
<dd> The integer four, not to be confused with six, Tom’s favorite editor. IV also means an internal Integer Value of the type a <code>scalar</code> can hold, not to be confused with an <code>NV</code>.</dd></dl>
<h3>J</h3>
<dl>
<dt>JAPH</dt>
<dd> “Just Another Perl Hacker”, a clever but cryptic bit of Perl code that, when executed, evaluates to that string. Often used to illustrate a particular Perl feature, and something of an ongoing Obfuscated Perl Contest seen in USENET signatures.</dd></dl>
<h3>K</h3>
<dl>
<dt>key</dt>
<dd> The string index to a <code>hash</code>, used to look up the <code>value</code> associated with that key.</dd>
<dt>keyword</dt>
<dd> See <code>reserved words</code>.</dd></dl>
<h3>L</h3>
<dl>
<dt>label</dt>
<dd> A name you give to a <code>statement</code> so that you can talk about that statement elsewhere in the program.</dd>
<dt>laziness</dt>
<dd> The quality that makes you go to great effort to reduce overall energy expenditure. It makes you write labor-saving programs that other people will find useful, and then document what you wrote so you don’t have to answer so many questions about it. Hence, the first great virtue of a programmer. Also hence, this book. See also <code>impatience</code> and <code>hubris</code>.</dd>
<dt>leftmost longest</dt>
<dd> The preference of the <code>regular expression</code> engine to match the leftmost occurrence of a <code>pattern</code>, then given a position at which a match will occur, the preference for the longest match (presuming the use of a <code>greedy</code> quantifier). See Camel chapter 5, “Pattern Matching” for <i>much</i> more on this subject.</dd>
<dt>left shift</dt>
<dd> A <code>bit shift</code> that multiplies the number by some power of 2.</dd>
<dt>lexeme</dt>
<dd> Fancy term for a <code>token</code>.</dd>
<dt>lexer</dt>
<dd> Fancy term for a <code>tokener</code>.</dd>
<dt>lexical analysis</dt>
<dd> Fancy term for <code>tokenizing</code>.</dd>
<dt>lexical scoping</dt>
<dd> Looking at your <i>Oxford English Dictionary</i> through a microscope. (Also known as <code>static scoping</code>, because dictionaries don’t change very fast.) Similarly, looking at variables stored in a private dictionary (namespace) for each scope, which are visible only from their point of declaration down to the end of the lexical scope in which they are declared. —Syn. <code>static scoping</code>. —Ant. <code>dynamic scoping</code>.</dd>
<dt>lexical variable</dt>
<dd> A <code>variable</code> subject to <code>lexical scoping</code>, declared by <tt>&quot;my&quot;</tt>. Often just called a “lexical”. (The <tt>&quot;our&quot;</tt> declaration declares a lexically scoped name for a global variable, which is not itself a lexical variable.)</dd>
<dt>library</dt>
<dd> Generally, a collection of procedures. In ancient days, referred to a collection of subroutines in a <i>.pl</i> file. In modern times, refers more often to the entire collection of Perl <code>modules</code> on your system.</dd>
<dt>LIFO</dt>
<dd> Last In, First Out. See also <code>FIFO</code>. A LIFO is usually called a <code>stack</code>.</dd>
<dt>line</dt>
<dd> In Unix, a sequence of zero or more nonnewline characters terminated with a <code>newline</code> character. On non-Unix machines, this is emulated by the C library even if the underlying <code>operating system</code> has different ideas.</dd>
<dt>linebreak</dt>
<dd> A <code>grapheme</code> consisting of either a carriage return followed by a line feed or any character with the Unicode Vertical Space <code>character property</code>.</dd>
<dt>line buffering</dt>
<dd> Used by a <code>standard I/O</code> output stream that flushes its <code>buffer</code> after every <code>newline</code>. Many standard I/O libraries automatically set up line buffering on output that is going to the terminal.</dd>
<dt>line number</dt>
<dd> The number of lines read previous to this one, plus 1. Perl keeps a separate line number for each source or input file it opens. The current source file’s line number is represented by <tt>&quot;__LINE__&quot;</tt>. The current input line number (for the file that was most recently read via <tt>&quot;&lt;FH&gt;&quot;</tt>) is represented by the <tt>$.</tt> (<tt>$INPUT_LINE_NUMBER</tt>) variable. Many error messages report both values, if available.</dd>
<dt>link</dt>
<dd> Used as a noun, a name in a <code>directory</code> that represents a <code>file</code>. A given file can have multiple links to it. It’s like having the same phone number listed in the phone directory under different names. As a verb, to resolve a partially <code>compiled</code> file’s unresolved symbols into a (nearly) executable image. Linking can generally be static or dynamic, which has nothing to do with static or dynamic scoping.</dd>
<dt>LIST</dt>
<dd> A syntactic construct representing a comma- separated list of expressions, evaluated to produce a <code>list value</code>. Each <code>expression</code> in a <i></i>&quot;LIST&quot;<i></i> is evaluated in <code>list context</code> and interpolated into the list value.</dd>
<dt>list</dt>
<dd> An ordered set of scalar values.</dd>
<dt>list context</dt>
<dd> The situation in which an <code>expression</code> is expected by its surroundings (the code calling it) to return a list of values rather than a single value. Functions that want a <i></i>&quot;LIST&quot;<i></i> of arguments tell those arguments that they should produce a list value. See also <code>context</code>.</dd>
<dt>list operator</dt>
<dd> An <code>operator</code> that does something with a list of values, such as <tt>&quot;join&quot;</tt> or <tt>&quot;grep&quot;</tt>. Usually used for named built-in operators (such as <tt>&quot;print&quot;</tt>, <tt>&quot;unlink&quot;</tt>, and <tt>&quot;system&quot;</tt>) that do not require parentheses around their <code>argument</code> list.</dd>
<dt>list value</dt>
<dd> An unnamed list of temporary scalar values that may be passed around within a program from any list-generating function to any function or construct that provides a <code>list context</code>.</dd>
<dt>literal</dt>
<dd> A token in a programming language, such as a number or <code>string</code>, that gives you an actual <code>value</code> instead of merely representing possible values as a <code>variable</code> does.</dd>
<dt>little-endian</dt>
<dd> From Swift: someone who eats eggs little end first. Also used of computers that store the least significant <code>byte</code> of a word at a lower byte address than the most significant byte. Often considered superior to big-endian machines. See also <code>big-endian</code>.</dd>
<dt>local</dt>
<dd> Not meaning the same thing everywhere. A global variable in Perl can be localized inside a <code>dynamic scope</code> via the <tt>&quot;local&quot;</tt> operator.</dd>
<dt>logical operator</dt>
<dd> Symbols representing the concepts “and”, “or”, “xor”, and “not”.</dd>
<dt>lookahead</dt>
<dd> An <code>assertion</code> that peeks at the string to the right of the current match location.</dd>
<dt>lookbehind</dt>
<dd> An <code>assertion</code> that peeks at the string to the left of the current match location.</dd>
<dt>loop</dt>
<dd> A construct that performs something repeatedly, like a roller coaster.</dd>
<dt>loop control statement</dt>
<dd> Any statement within the body of a loop that can make a loop prematurely stop looping or skip an <code>iteration</code>. Generally, you shouldn’t try this on roller coasters.</dd>
<dt>loop label</dt>
<dd> A kind of key or name attached to a loop (or roller coaster) so that loop control statements can talk about which loop they want to control.</dd>
<dt>lowercase</dt>
<dd> In Unicode, not just characters with the General Category of Lowercase Letter, but any character with the Lowercase property, including Modifier Letters, Letter Numbers, some Other Symbols, and one Combining Mark.</dd>
<dt>lvaluable</dt>
<dd> Able to serve as an <code>lvalue</code>.</dd>
<dt>lvalue</dt>
<dd> Term used by language lawyers for a storage location you can assign a new <code>value</code> to, such as a <code>variable</code> or an element of an <code>array</code>. The “l” is short for “left”, as in the left side of an assignment, a typical place for lvalues. An <code>lvaluable</code> function or expression is one to which a value may be assigned, as in <tt>&quot;pos($x) = 10&quot;</tt>.</dd>
<dt>lvalue modifier</dt>
<dd> An adjectival pseudofunction that warps the meaning of an <code>lvalue</code> in some declarative fashion. Currently there are three lvalue modifiers: <tt>&quot;my&quot;</tt>, <tt>&quot;our&quot;</tt>, and <tt>&quot;local&quot;</tt>.</dd></dl>
<h3>M</h3>
<dl>
<dt>magic</dt>
<dd> Technically speaking, any extra semantics attached to a variable such as <tt>$!</tt>, <tt>$0</tt>, <tt>%ENV</tt>, or <tt>%SIG</tt>, or to any tied variable. Magical things happen when you diddle those variables.</dd>
<dt>magical increment</dt>
<dd> An <code>increment</code> operator that knows how to bump up ASCII alphabetics as well as numbers.</dd>
<dt>magical variables</dt>
<dd> Special variables that have side effects when you access them or assign to them. For example, in Perl, changing elements of the <tt>%ENV</tt> array also changes the corresponding environment variables that subprocesses will use. Reading the <tt>$!</tt> variable gives you the current system error number or message.</dd>
<dt>Makefile</dt>
<dd> A file that controls the compilation of a program. Perl programs don’t usually need a <code>Makefile</code> because the Perl compiler has plenty of self-control.</dd>
<dt>man</dt>
<dd> The Unix program that displays online documentation (manual pages) for you.</dd>
<dt>manpage</dt>
<dd> A “page” from the manuals, typically accessed via the <i><a href="/docs/linux/man/1-man/">man</a></i>(1) command. A manpage contains a SYNOPSIS, a DESCRIPTION, a list of BUGS, and so on, and is typically longer than a page. There are manpages documenting <code>commands</code>, <code>syscalls</code>, <code>library</code> <code>functions</code>, <code>devices</code>, <code>protocols</code>, <code>files</code>, and such. In this book, we call any piece of standard Perl documentation (like perlop or perldelta) a manpage, no matter what format it’s installed in on your system.</dd>
<dt>matching</dt>
<dd> See <code>pattern matching</code>.</dd>
<dt>member data</dt>
<dd> See <code>instance variable</code>.</dd>
<dt>memory</dt>
<dd> This always means your main memory, not your disk. Clouding the issue is the fact that your machine may implement <code>virtual</code> memory; that is, it will pretend that it has more memory than it really does, and it’ll use disk space to hold inactive bits. This can make it seem like you have a little more memory than you really do, but it’s not a substitute for real memory. The best thing that can be said about virtual memory is that it lets your performance degrade gradually rather than suddenly when you run out of real memory. But your program can die when you run out of virtual memory, too—if you haven’t thrashed your disk to death first.</dd>
<dt>metacharacter</dt>
<dd> A <code>character</code> that is <i>not</i> supposed to be treated normally. Which characters are to be treated specially as metacharacters varies greatly from context to context. Your <code>shell</code> will have certain metacharacters, double-quoted Perl <code>strings</code> have other metacharacters, and <code>regular expression</code> patterns have all the double-quote metacharacters plus some extra ones of their own.</dd>
<dt>metasymbol</dt>
<dd> Something we’d call a <code>metacharacter</code> except that it’s a sequence of more than one character. Generally, the first character in the sequence must be a true metacharacter to get the other characters in the metasymbol to misbehave along with it.</dd>
<dt>method</dt>
<dd> A kind of action that an <code>object</code> can take if you tell it to. See Camel chapter 12, “Objects”.</dd>
<dt>method resolution order</dt>
<dd> The path Perl takes through <tt>@INC</tt>. By default, this is a double depth first search, once looking for defined methods and once for <tt>&quot;AUTOLOAD&quot;</tt>. However, Perl lets you configure this with <tt>&quot;mro&quot;</tt>.</dd>
<dt>minicpan</dt>
<dd> A CPAN mirror that includes just the latest versions for each distribution, probably created with <tt>&quot;CPAN::Mini&quot;</tt>. See Camel chapter 19, “CPAN”.</dd>
<dt>minimalism</dt>
<dd> The belief that “small is beautiful”. Paradoxically, if you say something in a small language, it turns out big, and if you say it in a big language, it turns out small. Go figure.</dd>
<dt>mode</dt>
<dd> In the context of the <i><a href="/docs/linux/man/2-stat/">stat</a></i>(2) syscall, refers to the field holding the <code>permission bits</code> and the type of the <code>file</code>.</dd>
<dt>modifier</dt>
<dd> See <code>statement modifier</code>, <code>regular expression</code>, and <code>lvalue</code>, not necessarily in that order.</dd>
<dt>module</dt>
<dd> A <code>file</code> that defines a <code>package</code> of (almost) the same name, which can either <code>export</code> symbols or function as an <code>object</code> class. (A module’s main <i>.pm</i> file may also load in other files in support of the module.) See the <tt>&quot;use&quot;</tt> built-in.</dd>
<dt>modulus</dt>
<dd> An integer divisor when you’re interested in the remainder instead of the quotient.</dd>
<dt>mojibake</dt>
<dd> When you speak one language and the computer thinks you’re speaking another. You’ll see odd translations when you send UTF‑8, for instance, but the computer thinks you sent Latin-1, showing all sorts of weird characters instead. The term is written 「文字化け」in Japanese and means “character rot”, an apt description. Pronounced [<tt>&quot;modʑibake&quot;</tt>] in standard <code>IPA</code> phonetics, or approximately “moh-jee-bah-keh”.</dd>
<dt>monger</dt>
<dd> Short for one member of <code>Perl mongers</code>, a purveyor of Perl.</dd>
<dt>mortal</dt>
<dd> A temporary value scheduled to die when the current statement finishes.</dd>
<dt>mro</dt>
<dd> See <code>method resolution order</code>.</dd>
<dt>multidimensional array</dt>
<dd> An array with multiple subscripts for finding a single element. Perl implements these using <code>references</code>—see Camel chapter 9, “Data Structures”.</dd>
<dt>multiple inheritance</dt>
<dd> The features you got from your mother and father, mixed together unpredictably. (See also <code>inheritance</code> and <code>single inheritance</code>.) In computer languages (including Perl), it is the notion that a given class may have multiple direct ancestors or <code>base classes</code>.</dd></dl>
<h3>N</h3>
<dl>
<dt>named pipe</dt>
<dd> A <code>pipe</code> with a name embedded in the <code>filesystem</code> so that it can be accessed by two unrelated <code>processes</code>.</dd>
<dt>namespace</dt>
<dd> A domain of names. You needn’t worry about whether the names in one such domain have been used in another. See <code>package</code>.</dd>
<dt>NaN</dt>
<dd> Not a number. The value Perl uses for certain invalid or inexpressible floating-point operations.</dd>
<dt>network address</dt>
<dd> The most important attribute of a socket, like your telephone’s telephone number. Typically an IP address. See also <code>port</code>.</dd>
<dt>newline</dt>
<dd> A single character that represents the end of a line, with the ASCII value of 012 octal under Unix (but 015 on a Mac), and represented by <tt>&quot;
&quot;</tt> in Perl strings. For Windows machines writing text files, and for certain physical devices like terminals, the single newline gets automatically translated by your C library into a line feed and a carriage return, but normally, no translation is done.</dd>
<dt>NFS</dt>
<dd> Network File System, which allows you to mount a remote filesystem as if it were local.</dd>
<dt>normalization</dt>
<dd> Converting a text string into an alternate but equivalent <code>canonical</code> (or compatible) representation that can then be compared for equivalence. Unicode recognizes four different normalization forms: NFD, NFC, NFKD, and NFKC.</dd>
<dt>null character</dt>
<dd> A character with the numeric value of zero. It’s used by C to terminate strings, but Perl allows strings to contain a null.</dd>
<dt>null list</dt>
<dd> A <code>list value</code> with zero elements, represented in Perl by <tt>&quot;()&quot;</tt>.</dd>
<dt>null string</dt>
<dd> A <code>string</code> containing no characters, not to be confused with a string containing a <code>null character</code>, which has a positive length and is <code>true</code>.</dd>
<dt>numeric context</dt>
<dd> The situation in which an expression is expected by its surroundings (the code calling it) to return a number. See also <code>context</code> and <code>string context</code>.</dd>
<dt>numification</dt>
<dd> (Sometimes spelled <i>nummification</i> and <i>nummify</i>.) Perl lingo for implicit conversion into a number; the related verb is <i>numify</i>. <i>Numification</i> is intended to rhyme with <i>mummification</i>, and <i>numify</i> with <i>mummify</i>. It is unrelated to English <i>numen</i>, <i>numina</i>, <i>numinous</i>. We originally forgot the extra <i>m</i> a long time ago, and some people got used to our funny spelling, and so just as with <tt>&quot;HTTP_REFERER&quot;</tt>’s own missing letter, our weird spelling has stuck around.</dd>
<dt>NV</dt>
<dd> Short for Nevada, no part of which will ever be confused with civilization. NV also means an internal floating- point Numeric Value of the type a <code>scalar</code> can hold, not to be confused with an <code>IV</code>.</dd>
<dt>nybble</dt>
<dd> Half a <code>byte</code>, equivalent to one <code>hexadecimal</code> digit, and worth four <code>bits</code>.</dd></dl>
<h3>O</h3>
<dl>
<dt>object</dt>
<dd> An <code>instance</code> of a <code>class</code>. Something that “knows” what user-defined type (class) it is, and what it can do because of what class it is. Your program can request an object to do things, but the object gets to decide whether it wants to do them or not. Some objects are more accommodating than others.</dd>
<dt>octal</dt>
<dd> A number in base 8. Only the digits 0 through 7 are allowed. Octal constants in Perl start with 0, as in 013. See also the <tt>&quot;oct&quot;</tt> function.</dd>
<dt>offset</dt>
<dd> How many things you have to skip over when moving from the beginning of a string or array to a specific position within it. Thus, the minimum offset is zero, not one, because you don’t skip anything to get to the first item.</dd>
<dt>one-liner</dt>
<dd> An entire computer program crammed into one line of text.</dd>
<dt>open source software</dt>
<dd> Programs for which the source code is freely available and freely redistributable, with no commercial strings attached. For a more detailed definition, see &lt;<a rel="nofollow" href="http://www.opensource.org/osd.html">http://www.opensource.org/osd.html</a>&gt;.</dd>
<dt>operand</dt>
<dd> An <code>expression</code> that yields a <code>value</code> that an <code>operator</code> operates on. See also <code>precedence</code>.</dd>
<dt>operating system</dt>
<dd> A special program that runs on the bare machine and hides the gory details of managing <code>processes</code> and <code>devices</code>. Usually used in a looser sense to indicate a particular culture of programming. The loose sense can be used at varying levels of specificity. At one extreme, you might say that all versions of Unix and Unix-lookalikes are the same operating system (upsetting many people, especially lawyers and other advocates). At the other extreme, you could say this particular version of this particular vendor’s operating system is different from any other version of this or any other vendor’s operating system. Perl is much more portable across operating systems than many other languages. See also <code>architecture</code> and <code>platform</code>.</dd>
<dt>operator</dt>
<dd> A gizmo that transforms some number of input values to some number of output values, often built into a language with a special syntax or symbol. A given operator may have specific expectations about what <code>types</code> of data you give as its arguments (<code>operands</code>) and what type of data you want back from it.</dd>
<dt>operator overloading</dt>
<dd> A kind of <code>overloading</code> that you can do on built-in <code>operators</code> to make them work on <code>objects</code> as if the objects were ordinary scalar values, but with the actual semantics supplied by the object class. This is set up with the overload <code>pragma</code>—see Camel chapter 13, “Overloading”.</dd>
<dt>options</dt>
<dd> See either <code>switches</code> or <code>regular expression modifiers</code>.</dd>
<dt>ordinal</dt>
<dd> An abstract character’s integer value. Same thing as <code>codepoint</code>.</dd>
<dt>overloading</dt>
<dd> Giving additional meanings to a symbol or construct. Actually, all languages do overloading to one extent or another, since people are good at figuring out things from <code>context</code>.</dd>
<dt>overriding</dt>
<dd> Hiding or invalidating some other definition of the same name. (Not to be confused with <code>overloading</code>, which adds definitions that must be disambiguated some other way.) To confuse the issue further, we use the word with two overloaded definitions: to describe how you can define your own <code>subroutine</code> to hide a built-in <code>function</code> of the same name (see the section “Overriding Built-in Functions” in Camel chapter 11, “Modules”), and to describe how you can define a replacement <code>method</code> in a <code>derived class</code> to hide a <code>base class</code>’s method of the same name (see Camel chapter 12, “Objects”).</dd>
<dt>owner</dt>
<dd> The one user (apart from the superuser) who has absolute control over a <code>file</code>. A file may also have a <code>group</code> of users who may exercise joint ownership if the real owner permits it. See <code>permission bits</code>.</dd></dl>
<h3>P</h3>
<dl>
<dt>package</dt>
<dd> A <code>namespace</code> for global <code>variables</code>, <code>subroutines</code>, and the like, such that they can be kept separate from like-named <code>symbols</code> in other namespaces. In a sense, only the package is global, since the symbols in the package’s symbol table are only accessible from code <code>compiled</code> outside the package by naming the package. But in another sense, all package symbols are also globals—they’re just well-organized globals.</dd>
<dt>pad</dt>
<dd> Short for <code>scratchpad</code>.</dd>
<dt>parameter</dt>
<dd> See <code>argument</code>.</dd>
<dt>parent class</dt>
<dd> See <code>base class</code>.</dd>
<dt>parse tree</dt>
<dd> See <code>syntax tree</code>.</dd>
<dt>parsing</dt>
<dd> The subtle but sometimes brutal art of attempting to turn your possibly malformed program into a valid <code>syntax tree</code>.</dd>
<dt>patch</dt>
<dd> To fix by applying one, as it were. In the realm of hackerdom, a listing of the differences between two versions of a program as might be applied by the <code><a href="/docs/linux/man/1-patch/">patch</a></code>(1) program when you want to fix a bug or upgrade your old version.</dd>
<dt>PATH</dt>
<dd> The list of <code>directories</code> the system searches to find a program you want to <code>execute</code>. The list is stored as one of your <code>environment variables</code>, accessible in Perl as <tt>$ENV{PATH}</tt>.</dd>
<dt>pathname</dt>
<dd> A fully qualified filename such as <i>/usr/bin/perl</i>. Sometimes confused with <tt>&quot;PATH&quot;</tt>.</dd>
<dt>pattern</dt>
<dd> A template used in <code>pattern matching</code>.</dd>
<dt>pattern matching</dt>
<dd> Taking a pattern, usually a <code>regular expression</code>, and trying the pattern various ways on a string to see whether there’s any way to make it fit. Often used to pick interesting tidbits out of a file.</dd>
<dt>PAUSE</dt>
<dd> The Perl Authors Upload SErver (&lt;<a rel="nofollow" href="http://pause.perl.org">http://pause.perl.org</a>&gt;), the gateway for <code>modules</code> on their way to <code>CPAN</code>.</dd>
<dt>Perl mongers</dt>
<dd> A Perl user group, taking the form of its name from the New York Perl mongers, the first Perl user group. Find one near you at &lt;<a rel="nofollow" href="http://www.pm.org">http://www.pm.org</a>&gt;.</dd>
<dt>permission bits</dt>
<dd> Bits that the <code>owner</code> of a file sets or unsets to allow or disallow access to other people. These flag bits are part of the <code>mode</code> word returned by the <tt>&quot;stat&quot;</tt> built-in when you ask about a file. On Unix systems, you can check the <i><a href="/docs/linux/man/1-ls/">ls</a></i>(1) manpage for more information.</dd>
<dt>Pern</dt>
<dd> What you get when you do <tt>&quot;Perl++&quot;</tt> twice. Doing it only once will curl your hair. You have to increment it eight times to shampoo your hair. Lather, rinse, iterate.</dd>
<dt>pipe</dt>
<dd> A direct <code>connection</code> that carries the output of one <code>process</code> to the input of another without an intermediate temporary file. Once the pipe is set up, the two processes in question can read and write as if they were talking to a normal file, with some caveats.</dd>
<dt>pipeline</dt>
<dd> A series of <code>processes</code> all in a row, linked by <code>pipes</code>, where each passes its output stream to the next.</dd>
<dt>platform</dt>
<dd> The entire hardware and software context in which a program runs. A program written in a platform-dependent language might break if you change any of the following: machine, operating system, libraries, compiler, or system configuration. The <i>perl</i> interpreter has to be <code>compiled</code> differently for each platform because it is implemented in C, but programs written in the Perl language are largely platform independent.</dd>
<dt>pod</dt>
<dd> The markup used to embed documentation into your Perl code. Pod stands for “Plain old documentation”. See Camel chapter 23, “Plain Old Documentation”.</dd>
<dt>pod command</dt>
<dd> A sequence, such as <tt>&quot;=head1&quot;</tt>, that denotes the start of a <code>pod</code> section.</dd>
<dt>pointer</dt>
<dd> A <code>variable</code> in a language like C that contains the exact memory location of some other item. Perl handles pointers internally so you don’t have to worry about them. Instead, you just use symbolic pointers in the form of <code>keys</code> and <code>variable</code> names, or <code>hard references</code>, which aren’t pointers (but act like pointers and do in fact contain pointers).</dd>
<dt>polymorphism</dt>
<dd> The notion that you can tell an <code>object</code> to do something generic, and the object will interpret the command in different ways depending on its type. [&lt; Greek πολυ- + μορϕή, many forms.]</dd>
<dt>port</dt>
<dd> The part of the address of a TCP or UDP socket that directs packets to the correct process after finding the right machine, something like the phone extension you give when you reach the company operator. Also the result of converting code to run on a different platform than originally intended, or the verb denoting this conversion.</dd>
<dt>portable</dt>
<dd> Once upon a time, C code compilable under both BSD and SysV. In general, code that can be easily converted to run on another <code>platform</code>, where “easily” can be defined however you like, and usually is. Anything may be considered portable if you try hard enough, such as a mobile home or London Bridge.</dd>
<dt>porter</dt>
<dd> Someone who “carries” software from one <code>platform</code> to another. Porting programs written in platform-dependent languages such as C can be difficult work, but porting programs like Perl is very much worth the agony.</dd>
<dt>possessive</dt>
<dd> Said of quantifiers and groups in patterns that refuse to give up anything once they’ve gotten their mitts on it. Catchier and easier to say than the even more formal <i>nonbacktrackable</i>.</dd>
<dt>POSIX</dt>
<dd> The Portable Operating System Interface specification.</dd>
<dt>postfix</dt>
<dd> An <code>operator</code> that follows its <code>operand</code>, as in <tt>&quot;$x++&quot;</tt>.</dd>
<dt>pp</dt>
<dd> An internal shorthand for a “push- pop” code; that is, C code implementing Perl’s stack machine.</dd>
<dt>pragma</dt>
<dd> A standard module whose practical hints and suggestions are received (and possibly ignored) at compile time. Pragmas are named in all lowercase.</dd>
<dt>precedence</dt>
<dd> The rules of conduct that, in the absence of other guidance, determine what should happen first. For example, in the absence of parentheses, you always do multiplication before addition.</dd>
<dt>prefix</dt>
<dd> An <code>operator</code> that precedes its <code>operand</code>, as in <tt>&quot;++$x&quot;</tt>.</dd>
<dt>preprocessing</dt>
<dd> What some helper <code>process</code> did to transform the incoming data into a form more suitable for the current process. Often done with an incoming <code>pipe</code>. See also <code>C preprocessor</code>.</dd>
<dt>primary maintainer</dt>
<dd> The author that PAUSE allows to assign <code>co-maintainer</code> permissions to a <code>namespace</code>. A primary maintainer can give up this distinction by assigning it to another PAUSE author. See Camel chapter 19, “CPAN”.</dd>
<dt>procedure</dt>
<dd> A <code>subroutine</code>.</dd>
<dt>process</dt>
<dd> An instance of a running program. Under multitasking systems like Unix, two or more separate processes could be running the same program independently at the same time—in fact, the <tt>&quot;fork&quot;</tt> function is designed to bring about this happy state of affairs. Under other operating systems, processes are sometimes called “threads”, “tasks”, or “jobs”, often with slight nuances in meaning.</dd>
<dt>program</dt>
<dd> See <code>script</code>.</dd>
<dt>program generator</dt>
<dd> A system that algorithmically writes code for you in a high-level language. See also <code>code generator</code>.</dd>
<dt>progressive matching</dt>
<dd> <code>Pattern matching</code> matching&gt;that picks up where it left off before.</dd>
<dt>property</dt>
<dd> See either <code>instance variable</code> or <code>character property</code>.</dd>
<dt>protocol</dt>
<dd> In networking, an agreed-upon way of sending messages back and forth so that neither correspondent will get too confused.</dd>
<dt>prototype</dt>
<dd> An optional part of a <code>subroutine</code> declaration telling the Perl compiler how many and what flavor of arguments may be passed as <code>actual arguments</code>, so you can write subroutine calls that parse much like built-in functions. (Or don’t parse, as the case may be.)</dd>
<dt>pseudofunction</dt>
<dd> A construct that sometimes looks like a function but really isn’t. Usually reserved for <code>lvalue</code> modifiers like <tt>&quot;my&quot;</tt>, for <code>context</code> modifiers like <tt>&quot;scalar&quot;</tt>, and for the pick-your-own-quotes constructs, <tt>&quot;q//&quot;</tt>, <tt>&quot;qq//&quot;</tt>, <tt>&quot;qx//&quot;</tt>, <tt>&quot;qw//&quot;</tt>, <tt>&quot;qr//&quot;</tt>, <tt>&quot;m//&quot;</tt>, <tt>&quot;s///&quot;</tt>, <tt>&quot;y///&quot;</tt>, and <tt>&quot;tr///&quot;</tt>.</dd>
<dt>pseudohash</dt>
<dd> Formerly, a reference to an array whose initial element happens to hold a reference to a hash. You used to be able to treat a pseudohash reference as either an array reference or a hash reference. Pseduohashes are no longer supported.</dd>
<dt>pseudoliteral</dt>
<dd> An <code>operator</code> X<tt>&quot;that looks something like a </tt>literal<tt>, such as the output-grabbing operator, &lt;literal moreinfo=&quot;none&quot;&quot;</tt>`&gt;<i></i>&quot;command&quot;<i></i><tt>&quot;`&quot;</tt>.</dd>
<dt>public domain</dt>
<dd> Something not owned by anybody. Perl is copyrighted and is thus <i>not</i> in the public domain—it’s just <code>freely available</code> and <code>freely redistributable</code>.</dd>
<dt>pumpkin</dt>
<dd> A notional “baton” handed around the Perl community indicating who is the lead integrator in some arena of development.</dd>
<dt>pumpking</dt>
<dd> A <code>pumpkin</code> holder, the person in charge of pumping the pump, or at least priming it. Must be willing to play the part of the Great Pumpkin now and then.</dd>
<dt>PV</dt>
<dd> A “pointer value”, which is Perl Internals Talk for a <tt>&quot;char*&quot;</tt>.</dd></dl>
<h3>Q</h3>
<dl>
<dt>qualified</dt>
<dd> Possessing a complete name. The symbol <tt>$Ent::moot</tt> is qualified; <tt>$moot</tt> is unqualified. A fully qualified filename is specified from the top-level directory.</dd>
<dt>quantifier</dt>
<dd> A component of a <code>regular expression</code> specifying how many times the foregoing <code>atom</code> may occur.</dd></dl>
<h3>R</h3>
<dl>
<dt>race condition</dt>
<dd> A race condition exists when the result of several interrelated events depends on the ordering of those events, but that order cannot be guaranteed due to nondeterministic timing effects. If two or more programs, or parts of the same program, try to go through the same series of events, one might interrupt the work of the other. This is a good way to find an <code>exploit</code>.</dd>
<dt>readable</dt>
<dd> With respect to files, one that has the proper permission bit set to let you access the file. With respect to computer programs, one that’s written well enough that someone has a chance of figuring out what it’s trying to do.</dd>
<dt>reaping</dt>
<dd> The last rites performed by a parent <code>process</code> on behalf of a deceased child process so that it doesn’t remain a <code>zombie</code>. See the <tt>&quot;wait&quot;</tt> and <tt>&quot;waitpid&quot;</tt> function calls.</dd>
<dt>record</dt>
<dd> A set of related data values in a <code>file</code> or <code>stream</code>, often associated with a unique <code>key</code> field. In Unix, often commensurate with a <code>line</code>, or a blank-line–terminated set of lines (a “paragraph”). Each line of the <i>/etc/passwd</i> file is a record, keyed on login name, containing information about that user.</dd>
<dt>recursion</dt>
<dd> The art of defining something (at least partly) in terms of itself, which is a naughty no-no in dictionaries but often works out okay in computer programs if you’re careful not to recurse forever (which is like an infinite loop with more spectacular failure modes).</dd>
<dt>reference</dt>
<dd> Where you look to find a pointer to information somewhere else. (See <code>indirection</code>.) References come in two flavors: <code>symbolic references</code> and <code>hard references</code>.</dd>
<dt>referent</dt>
<dd> Whatever a reference refers to, which may or may not have a name. Common types of referents include scalars, arrays, hashes, and subroutines.</dd>
<dt>regex</dt>
<dd> See <code>regular expression</code>.</dd>
<dt>regular expression</dt>
<dd> A single entity with various interpretations, like an elephant. To a computer scientist, it’s a grammar for a little language in which some strings are legal and others aren’t. To normal people, it’s a pattern you can use to find what you’re looking for when it varies from case to case. Perl’s regular expressions are far from regular in the theoretical sense, but in regular use they work quite well. Here’s a regular expression: <tt>&quot;/Oh s.*t./&quot;</tt>. This will match strings like “<tt>&quot;Oh say can you see by the dawn's early light&quot;</tt>” and “<tt>&quot;Oh sit!&quot;</tt>”. See Camel chapter 5, “Pattern Matching”.</dd>
<dt>regular expression modifier</dt>
<dd> An option on a pattern or substitution, such as <tt>&quot;/i&quot;</tt> to render the pattern case- insensitive.</dd>
<dt>regular file</dt>
<dd> A <code>file</code> that’s not a <code>directory</code>, a <code>device</code>, a named <code>pipe</code> or <code>socket</code>, or a <code>symbolic link</code>. Perl uses the <tt>&quot;–f&quot;</tt> file test operator to identify regular files. Sometimes called a “plain” file.</dd>
<dt>relational operator</dt>
<dd> An <code>operator</code> that says whether a particular ordering relationship is <code>true</code> about a pair of <code>operands</code>. Perl has both numeric and string relational operators. See <code>collating sequence</code>.</dd>
<dt>reserved words</dt>
<dd> A word with a specific, built-in meaning to a <code>compiler</code>, such as <tt>&quot;if&quot;</tt> or <tt>&quot;delete&quot;</tt>. In many languages (not Perl), it’s illegal to use reserved words to name anything else. (Which is why they’re reserved, after all.) In Perl, you just can’t use them to name <code>labels</code> or <code>filehandles</code>. Also called “keywords”.</dd>
<dt>return value</dt>
<dd> The <code>value</code> produced by a <code>subroutine</code> or <code>expression</code> when evaluated. In Perl, a return value may be either a <code>list</code> or a <code>scalar</code>.</dd>
<dt>RFC</dt>
<dd> Request For Comment, which despite the timid connotations is the name of a series of important standards documents.</dd>
<dt>right shift</dt>
<dd> A <code>bit shift</code> that divides a number by some power of 2.</dd>
<dt>role</dt>
<dd> A name for a concrete set of behaviors. A role is a way to add behavior to a class without inheritance.</dd>
<dt>root</dt>
<dd> The superuser (<tt>&quot;UID&quot;</tt> == 0). Also the top-level directory of the filesystem.</dd>
<dt>RTFM</dt>
<dd> What you are told when someone thinks you should Read The Fine Manual.</dd>
<dt>run phase</dt>
<dd> Any time after Perl starts running your main program. See also <code>compile phase</code>. Run phase is mostly spent in <code>runtime</code> but may also be spent in <code>compile time</code> when <tt>&quot;require&quot;</tt>, <tt>&quot;do&quot;</tt> <i></i>&quot;FILE&quot;<i></i>, or <tt>&quot;eval&quot;</tt> <i></i>&quot;STRING&quot;<i></i> operators are executed, or when a substitution uses the <tt>&quot;/ee&quot;</tt> modifier.</dd>
<dt>runtime</dt>
<dd> The time when Perl is actually doing what your code says to do, as opposed to the earlier period of time when it was trying to figure out whether what you said made any sense whatsoever, which is <code>compile time</code>.</dd>
<dt>runtime pattern</dt>
<dd> A pattern that contains one or more variables to be interpolated before parsing the pattern as a <code>regular expression</code>, and that therefore cannot be analyzed at compile time, but must be reanalyzed each time the pattern match operator is evaluated. Runtime patterns are useful but expensive.</dd>
<dt>RV</dt>
<dd> A recreational vehicle, not to be confused with vehicular recreation. RV also means an internal Reference Value of the type a <code>scalar</code> can hold. See also <code>IV</code> and <code>NV</code> if you’re not confused yet.</dd>
<dt>rvalue</dt>
<dd> A <code>value</code> that you might find on the right side of an <code>assignment</code>. See also <code>lvalue</code>.</dd></dl>
<h3>S</h3>
<dl>
<dt>sandbox</dt>
<dd> A walled off area that’s not supposed to affect beyond its walls. You let kids play in the sandbox instead of running in the road. See Camel chapter 20, “Security”.</dd>
<dt>scalar</dt>
<dd> A simple, singular value; a number, <code>string</code>, or <code>reference</code>.</dd>
<dt>scalar context</dt>
<dd> The situation in which an <code>expression</code> is expected by its surroundings (the code calling it) to return a single <code>value</code> rather than a <code>list</code> of values. See also <code>context</code> and <code>list context</code>. A scalar context sometimes imposes additional constraints on the return value—see <code>string context</code> and <code>numeric context</code>. Sometimes we talk about a <code>Boolean context</code> inside conditionals, but this imposes no additional constraints, since any scalar value, whether numeric or <code>string</code>, is already true or false.</dd>
<dt>scalar literal</dt>
<dd> A number or quoted <code>string</code>—an actual <code>value</code> in the text of your program, as opposed to a <code>variable</code>.</dd>
<dt>scalar value</dt>
<dd> A value that happens to be a <code>scalar</code> as opposed to a <code>list</code>.</dd>
<dt>scalar variable</dt>
<dd> A <code>variable</code> prefixed with <tt>&quot;$&quot;</tt> that holds a single value.</dd>
<dt>scope</dt>
<dd> From how far away you can see a variable, looking through one. Perl has two visibility mechanisms. It does <code>dynamic scoping</code> of <tt>&quot;local&quot;</tt> <code>variables</code>, meaning that the rest of the <code>block</code>, and any <code>subroutines</code> that are called by the rest of the block, can see the variables that are local to the block. Perl does <code>lexical scoping</code> of <tt>&quot;my&quot;</tt> variables, meaning that the rest of the block can see the variable, but other subroutines called by the block <i>cannot</i> see the variable.</dd>
<dt>scratchpad</dt>
<dd> The area in which a particular invocation of a particular file or subroutine keeps some of its temporary values, including any lexically scoped variables.</dd>
<dt>script</dt>
<dd> A text <code>file</code> that is a program intended to be <code>executed</code> directly rather than <code>compiled</code> to another form of file before <code>execution</code>. </dd>
<p> Also, in the context of <code>Unicode</code>, a writing system for a particular language or group of languages, such as Greek, Bengali, or Tengwar.</p>
<dt>script kiddie</dt>
<dd> A <code>cracker</code> who is not a <code>hacker</code> but knows just enough to run canned scripts. A <code>cargo-cult</code> programmer.</dd>
<dt>sed</dt>
<dd> A venerable Stream EDitor from which Perl derives some of its ideas.</dd>
<dt>semaphore</dt>
<dd> A fancy kind of interlock that prevents multiple <code>threads</code> or <code>processes</code> from using up the same resources simultaneously.</dd>
<dt>separator</dt>
<dd> A <code>character</code> or <code>string</code> that keeps two surrounding strings from being confused with each other. The <tt>&quot;split&quot;</tt> function works on separators. Not to be confused with <code>delimiters</code> or <code>terminators</code>. The “or” in the previous sentence separated the two alternatives.</dd>
<dt>serialization</dt>
<dd> Putting a fancy <code>data structure</code> into linear order so that it can be stored as a <code>string</code> in a disk file or database, or sent through a <code>pipe</code>. Also called marshalling.</dd>
<dt>server</dt>
<dd> In networking, a <code>process</code> that either advertises a <code>service</code> or just hangs around at a known location and waits for <code>clients</code> who need service to get in touch with it.</dd>
<dt>service</dt>
<dd> Something you do for someone else to make them happy, like giving them the time of day (or of their life). On some machines, well-known services are listed by the <tt>&quot;getservent&quot;</tt> function.</dd>
<dt>setgid</dt>
<dd> Same as <code>setuid</code>, only having to do with giving away <code>group</code> privileges.</dd>
<dt>setuid</dt>
<dd> Said of a program that runs with the privileges of its <code>owner</code> rather than (as is usually the case) the privileges of whoever is running it. Also describes the bit in the mode word (<code>permission bits</code>) that controls the feature. This bit must be explicitly set by the owner to enable this feature, and the program must be carefully written not to give away more privileges than it ought to.</dd>
<dt>shared memory</dt>
<dd> A piece of <code>memory</code> accessible by two different <code>processes</code> who otherwise would not see each other’s memory.</dd>
<dt>shebang</dt>
<dd> Irish for the whole McGillicuddy. In Perl culture, a portmanteau of “sharp” and “bang”, meaning the <tt>&quot;#!&quot;</tt> sequence that tells the system where to find the interpreter.</dd>
<dt>shell</dt>
<dd> A <code>command</code>-line <code>interpreter</code>. The program that interactively gives you a prompt, accepts one or more <code>lines</code> of input, and executes the programs you mentioned, feeding each of them their proper <code>arguments</code> and input data. Shells can also execute scripts containing such commands. Under Unix, typical shells include the Bourne shell (<i>/bin/sh</i>), the C shell (<i>/bin/csh</i>), and the Korn shell (<i>/bin/ksh</i>). Perl is not strictly a shell because it’s not interactive (although Perl programs can be interactive).</dd>
<dt>side effects</dt>
<dd> Something extra that happens when you evaluate an <code>expression</code>. Nowadays it can refer to almost anything. For example, evaluating a simple assignment statement typically has the “side effect” of assigning a value to a variable. (And you thought assigning the value was your primary intent in the first place!) Likewise, assigning a value to the special variable <tt>$|</tt> (<tt>$AUTOFLUSH</tt>) has the side effect of forcing a flush after every <tt>&quot;write&quot;</tt> or <tt>&quot;print&quot;</tt> on the currently selected filehandle.</dd>
<dt>sigil</dt>
<dd> A glyph used in magic. Or, for Perl, the symbol in front of a variable name, such as <tt>&quot;$&quot;</tt>, <tt>&quot;@&quot;</tt>, and <tt>&quot;%&quot;</tt>.</dd>
<dt>signal</dt>
<dd> A bolt out of the blue; that is, an event triggered by the <code>operating system</code>, probably when you’re least expecting it.</dd>
<dt>signal handler</dt>
<dd> A <code>subroutine</code> that, instead of being content to be called in the normal fashion, sits around waiting for a bolt out of the blue before it will deign to <code>execute</code>. Under Perl, bolts out of the blue are called signals, and you send them with the <tt>&quot;kill&quot;</tt> built-in. See the <tt>%SIG</tt> hash in Camel chapter 25, “Special Names” and the section “Signals” in Camel chapter 15, “Interprocess Communication”.</dd>
<dt>single inheritance</dt>
<dd> The features you got from your mother, if she told you that you don’t have a father. (See also <code>inheritance</code> and <code>multiple inheritance</code>.) In computer languages, the idea that <code>classes</code> reproduce asexually so that a given class can only have one direct ancestor or <code>base class</code>. Perl supplies no such restriction, though you may certainly program Perl that way if you like.</dd>
<dt>slice</dt>
<dd> A selection of any number of <code>elements</code> from a <code>list</code>, <code>array</code>, or <code>hash</code>.</dd>
<dt>slurp</dt>
<dd> To read an entire <code>file</code> into a <code>string</code> in one operation.</dd>
<dt>socket</dt>
<dd> An endpoint for network communication among multiple <code>processes</code> that works much like a telephone or a post office box. The most important thing about a socket is its <code>network address</code> (like a phone number). Different kinds of sockets have different kinds of addresses—some look like filenames, and some don’t.</dd>
<dt>soft reference</dt>
<dd> See <code>symbolic reference</code>.</dd>
<dt>source filter</dt>
<dd> A special kind of <code>module</code> that does <code>preprocessing</code> on your script just before it gets to the <code>tokener</code>.</dd>
<dt>stack</dt>
<dd> A device you can put things on the top of, and later take them back off in the opposite order in which you put them on. See <code>LIFO</code>.</dd>
<dt>standard</dt>
<dd> Included in the official Perl distribution, as in a standard module, a standard tool, or a standard Perl <code>manpage</code>.</dd>
<dt>standard error</dt>
<dd> The default output <code>stream</code> for nasty remarks that don’t belong in <code>standard output</code>. Represented within a Perl program by the output&gt; <code>filehandle</code> <tt>&quot;STDERR&quot;</tt>. You can use this stream explicitly, but the <tt>&quot;die&quot;</tt> and <tt>&quot;warn&quot;</tt> built-ins write to your standard error stream automatically (unless trapped or otherwise intercepted).</dd>
<dt>standard input</dt>
<dd> The default input <code>stream</code> for your program, which if possible shouldn’t care where its data is coming from. Represented within a Perl program by the <code>filehandle</code> <tt>&quot;STDIN&quot;</tt>.</dd>
<dt>standard I/O</dt>
<dd> A standard C library for doing <code>buffered</code> input and output to the <code>operating system</code>. (The “standard” of standard I/O is at most marginally related to the “standard” of standard input and output.) In general, Perl relies on whatever implementation of standard I/O a given operating system supplies, so the buffering characteristics of a Perl program on one machine may not exactly match those on another machine. Normally this only influences efficiency, not semantics. If your standard I/O package is doing block buffering and you want it to <code>flush</code> the buffer more often, just set the <tt>$|</tt> variable to a true value.</dd>
<dt>Standard Library</dt>
<dd> Everything that comes with the official <i>perl</i> distribution. Some vendor versions of <i>perl</i> change their distributions, leaving out some parts or including extras. See also <code>dual-lived</code>.</dd>
<dt>standard output</dt>
<dd> The default output <code>stream</code> for your program, which if possible shouldn’t care where its data is going. Represented within a Perl program by the <code>filehandle</code> <tt>&quot;STDOUT&quot;</tt>.</dd>
<dt>statement</dt>
<dd> A <code>command</code> to the computer about what to do next, like a step in a recipe: “Add marmalade to batter and mix until mixed.” A statement is distinguished from a <code>declaration</code>, which doesn’t tell the computer to do anything, but just to learn something.</dd>
<dt>statement modifier</dt>
<dd> A <code>conditional</code> or <code>loop</code> that you put after the <code>statement</code> instead of before, if you know what we mean.</dd>
<dt>static</dt>
<dd> Varying slowly compared to something else. (Unfortunately, everything is relatively stable compared to something else, except for certain elementary particles, and we’re not so sure about them.) In computers, where things are supposed to vary rapidly, “static” has a derogatory connotation, indicating a slightly dysfunctional <code>variable</code>, <code>subroutine</code>, or <code>method</code>. In Perl culture, the word is politely avoided. </dd>
<p> If you’re a C or C++ programmer, you might be looking for Perl’s <tt>&quot;state&quot;</tt> keyword.</p>
<dt>static method</dt>
<dd> No such thing. See <code>class method</code>.</dd>
<dt>static scoping</dt>
<dd> No such thing. See <code>lexical scoping</code>.</dd>
<dt>static variable</dt>
<dd> No such thing. Just use a <code>lexical variable</code> in a scope larger than your <code>subroutine</code>, or declare it with <tt>&quot;state&quot;</tt> instead of with <tt>&quot;my&quot;</tt>.</dd>
<dt>stat structure</dt>
<dd> A special internal spot in which Perl keeps the information about the last <code>file</code> on which you requested information.</dd>
<dt>status</dt>
<dd> The <code>value</code> returned to the parent <code>process</code> when one of its child processes dies. This value is placed in the special variable <tt>$?</tt>. Its upper eight <code>bits</code> are the exit status of the defunct process, and its lower eight bits identify the signal (if any) that the process died from. On Unix systems, this status value is the same as the status word returned by <i><a href="/docs/linux/man/2-wait/">wait</a></i>(2). See <tt>&quot;system&quot;</tt> in Camel chapter 27, “Functions”.</dd>
<dt>STDERR</dt>
<dd> See <code>standard error</code>.</dd>
<dt>STDIN</dt>
<dd> See <code>standard input</code>.</dd>
<dt>STDIO</dt>
<dd> See <code>standard I/O</code>.</dd>
<dt>STDOUT</dt>
<dd> See <code>standard output</code>.</dd>
<dt>stream</dt>
<dd> A flow of data into or out of a process as a steady sequence of bytes or characters, without the appearance of being broken up into packets. This is a kind of <code>interface</code>—the underlying <code>implementation</code> may well break your data up into separate packets for delivery, but this is hidden from you.</dd>
<dt>string</dt>
<dd> A sequence of characters such as “He said !@#*&amp;%@#*?!”. A string does not have to be entirely printable.</dd>
<dt>string context</dt>
<dd> The situation in which an expression is expected by its surroundings (the code calling it) to return a <code>string</code>. See also <code>context</code> and <code>numeric context</code>.</dd>
<dt>stringification</dt>
<dd> The process of producing a <code>string</code> representation of an abstract object.</dd>
<dt>struct</dt>
<dd> C keyword introducing a structure definition or name.</dd>
<dt>structure</dt>
<dd> See <code>data structure</code>.</dd>
<dt>subclass</dt>
<dd> See <code>derived class</code>.</dd>
<dt>subpattern</dt>
<dd> A component of a <code>regular expression</code> pattern.</dd>
<dt>subroutine</dt>
<dd> A named or otherwise accessible piece of program that can be invoked from elsewhere in the program in order to accomplish some subgoal of the program. A subroutine is often parameterized to accomplish different but related things depending on its input <code>arguments</code>. If the subroutine returns a meaningful <code>value</code>, it is also called a <code>function</code>.</dd>
<dt>subscript</dt>
<dd> A <code>value</code> that indicates the position of a particular <code>array</code> <code>element</code> in an array.</dd>
<dt>substitution</dt>
<dd> Changing parts of a string via the <tt>&quot;s///&quot;</tt> operator. (We avoid use of this term to mean <code>variable interpolation</code>.)</dd>
<dt>substring</dt>
<dd> A portion of a <code>string</code>, starting at a certain <code>character</code> position (<code>offset</code>) and proceeding for a certain number of characters.</dd>
<dt>superclass</dt>
<dd> See <code>base class</code>.</dd>
<dt>superuser</dt>
<dd> The person whom the <code>operating system</code> will let do almost anything. Typically your system administrator or someone pretending to be your system administrator. On Unix systems, the <code>root</code> user. On Windows systems, usually the Administrator user.</dd>
<dt>SV</dt>
<dd> Short for “scalar value”. But within the Perl interpreter, every <code>referent</code> is treated as a member of a class derived from SV, in an object-oriented sort of way. Every <code>value</code> inside Perl is passed around as a C language <tt>&quot;SV*&quot;</tt> pointer. The SV <code>struct</code> knows its own “referent type”, and the code is smart enough (we hope) not to try to call a <code>hash</code> function on a <code>subroutine</code>.</dd>
<dt>switch</dt>
<dd> An option you give on a command line to influence the way your program works, usually introduced with a minus sign. The word is also used as a nickname for a <code>switch statement</code>.</dd>
<dt>switch cluster</dt>
<dd> The combination of multiple command- line switches (<i>e.g.</i>, <tt>&quot;–a –b –c&quot;</tt>) into one switch (<i>e.g.</i>, <tt>&quot;–abc&quot;</tt>). Any switch with an additional <code>argument</code> must be the last switch in a cluster.</dd>
<dt>switch statement</dt>
<dd> A program technique that lets you evaluate an <code>expression</code> and then, based on the value of the expression, do a multiway branch to the appropriate piece of code for that value. Also called a “case structure”, named after the similar Pascal construct. Most switch statements in Perl are spelled <tt>&quot;given&quot;</tt>. See “The <tt>&quot;given&quot;</tt> statement” in Camel chapter 4, “Statements and Declarations”.</dd>
<dt>symbol</dt>
<dd> Generally, any <code>token</code> or <code>metasymbol</code>. Often used more specifically to mean the sort of name you might find in a <code>symbol table</code>.</dd>
<dt>symbolic debugger</dt>
<dd> A program that lets you step through the <code>execution</code> of your program, stopping or printing things out here and there to see whether anything has gone wrong, and, if so, what. The “symbolic” part just means that you can talk to the debugger using the same symbols with which your program is written.</dd>
<dt>symbolic link</dt>
<dd> An alternate filename that points to the real <code>filename</code>, which in turn points to the real <code>file</code>. Whenever the <code>operating system</code> is trying to parse a <code>pathname</code> containing a symbolic link, it merely substitutes the new name and continues parsing.</dd>
<dt>symbolic reference</dt>
<dd> A variable whose value is the name of another variable or subroutine. By <code>dereferencing</code> the first variable, you can get at the second one. Symbolic references are illegal under <tt>&quot;use strict &quot;refs&quot;&quot;</tt>.</dd>
<dt>symbol table</dt>
<dd> Where a <code>compiler</code> remembers symbols. A program like Perl must somehow remember all the names of all the <code>variables</code>, <code>filehandles</code>, and <code>subroutines</code> you’ve used. It does this by placing the names in a symbol table, which is implemented in Perl using a <code>hash table</code>. There is a separate symbol table for each <code>package</code> to give each package its own <code>namespace</code>.</dd>
<dt>synchronous</dt>
<dd> Programming in which the orderly sequence of events can be determined; that is, when things happen one after the other, not at the same time.</dd>
<dt>syntactic sugar</dt>
<dd> An alternative way of writing something more easily; a shortcut.</dd>
<dt>syntax</dt>
<dd> From Greek σύνταξις, “with-arrangement”. How things (particularly symbols) are put together with each other.</dd>
<dt>syntax tree</dt>
<dd> An internal representation of your program wherein lower-level <code>constructs</code> dangle off the higher-level constructs enclosing them.</dd>
<dt>syscall</dt>
<dd> A <code>function</code> call directly to the <code>operating system</code>. Many of the important subroutines and functions you use aren’t direct system calls, but are built up in one or more layers above the system call level. In general, Perl programmers don’t need to worry about the distinction. However, if you do happen to know which Perl functions are really syscalls, you can predict which of these will set the <tt>$!</tt> (<tt>$ERRNO</tt>) variable on failure. Unfortunately, beginning programmers often confusingly employ the term “system call” to mean what happens when you call the Perl <tt>&quot;system&quot;</tt> function, which actually involves many syscalls. To avoid any confusion, we nearly always say “syscall” for something you could call indirectly via Perl’s <tt>&quot;syscall&quot;</tt> function, and never for something you would call with Perl’s <tt>&quot;system&quot;</tt> function.</dd></dl>
<h3>T</h3>
<dl>
<dt>taint checks</dt>
<dd> The special bookkeeping Perl does to track the flow of external data through your program and disallow their use in system commands.</dd>
<dt>tainted</dt>
<dd> Said of data derived from the grubby hands of a user, and thus unsafe for a secure program to rely on. Perl does taint checks if you run a <code>setuid</code> (or <code>setgid</code>) program, or if you use the <tt>&quot;–T&quot;</tt> switch.</dd>
<dt>taint mode</dt>
<dd> Running under the <tt>&quot;–T&quot;</tt> switch, marking all external data as suspect and refusing to use it with system commands. See Camel chapter 20, “Security”.</dd>
<dt>TCP</dt>
<dd> Short for Transmission Control Protocol. A protocol wrapped around the Internet Protocol to make an unreliable packet transmission mechanism appear to the application program to be a reliable <code>stream</code> of bytes. (Usually.)</dd>
<dt>term</dt>
<dd> Short for a “terminal”—that is, a leaf node of a <code>syntax tree</code>. A thing that functions grammatically as an <code>operand</code> for the operators in an expression.</dd>
<dt>terminator</dt>
<dd> A <code>character</code> or <code>string</code> that marks the end of another string. The <tt>$/</tt> variable contains the string that terminates a <tt>&quot;readline&quot;</tt> operation, which <tt>&quot;chomp&quot;</tt> deletes from the end. Not to be confused with <code>delimiters</code> or <code>separators</code>. The period at the end of this sentence is a terminator.</dd>
<dt>ternary</dt>
<dd> An <code>operator</code> taking three <code>operands</code>. Sometimes pronounced <code>trinary</code>.</dd>
<dt>text</dt>
<dd> A <code>string</code> or <code>file</code> containing primarily printable characters.</dd>
<dt>thread</dt>
<dd> Like a forked process, but without <code>fork</code>’s inherent memory protection. A thread is lighter weight than a full process, in that a process could have multiple threads running around in it, all fighting over the same process’s memory space unless steps are taken to protect threads from one another.</dd>
<dt>tie</dt>
<dd> The bond between a magical variable and its implementation class. See the <tt>&quot;tie&quot;</tt> function in Camel chapter 27, “Functions” and Camel chapter 14, “Tied Variables”.</dd>
<dt>titlecase</dt>
<dd> The case used for capitals that are followed by lowercase characters instead of by more capitals. Sometimes called sentence case or headline case. English doesn’t use Unicode titlecase, but casing rules for English titles are more complicated than simply capitalizing each word’s first character.</dd>
<dt>TMTOWTDI</dt>
<dd> There’s More Than One Way To Do It, the Perl Motto. The notion that there can be more than one valid path to solving a programming problem in context. (This doesn’t mean that more ways are always better or that all possible paths are equally desirable—just that there need not be One True Way.)</dd>
<dt>token</dt>
<dd> A morpheme in a programming language, the smallest unit of text with semantic significance.</dd>
<dt>tokener</dt>
<dd> A module that breaks a program text into a sequence of <code>tokens</code> for later analysis by a parser.</dd>
<dt>tokenizing</dt>
<dd> Splitting up a program text into <code>tokens</code>. Also known as “lexing”, in which case you get “lexemes” instead of tokens.</dd>
<dt>toolbox approach</dt>
<dd> The notion that, with a complete set of simple tools that work well together, you can build almost anything you want. Which is fine if you’re assembling a tricycle, but if you’re building a defranishizing comboflux regurgalator, you really want your own machine shop in which to build special tools. Perl is sort of a machine shop.</dd>
<dt>topic</dt>
<dd> The thing you’re working on. Structures like <tt>&quot;while(&lt;&gt;)&quot;</tt>, <tt>&quot;for&quot;</tt>, <tt>&quot;foreach&quot;</tt>, and <tt>&quot;given&quot;</tt> set the topic for you by assigning to <tt>$_</tt>, the default (<i>topic</i>) variable.</dd>
<dt>transliterate</dt>
<dd> To turn one string representation into another by mapping each character of the source string to its corresponding character in the result string. Not to be confused with translation: for example, Greek <i>πολύχρωμος</i> transliterates into <i>polychromos</i> but translates into <i>many-colored</i>. See the <tt>&quot;tr///&quot;</tt> operator in Camel chapter 5, “Pattern Matching”.</dd>
<dt>trigger</dt>
<dd> An event that causes a <code>handler</code> to be run.</dd>
<dt>trinary</dt>
<dd> Not a stellar system with three stars, but an <code>operator</code> taking three <code>operands</code>. Sometimes pronounced <code>ternary</code>.</dd>
<dt>troff</dt>
<dd> A venerable typesetting language from which Perl derives the name of its <tt>$%</tt> variable and which is secretly used in the production of Camel books.</dd>
<dt>true</dt>
<dd> Any scalar value that doesn’t evaluate to 0 or <tt>&quot;&quot;</tt>.</dd>
<dt>truncating</dt>
<dd> Emptying a file of existing contents, either automatically when opening a file for writing or explicitly via the <tt>&quot;truncate&quot;</tt> function.</dd>
<dt>type</dt>
<dd> See <code>data type</code> and <code>class</code>.</dd>
<dt>type casting</dt>
<dd> Converting data from one type to another. C permits this. Perl does not need it. Nor want it.</dd>
<dt>typedef</dt>
<dd> A type definition in the C and C++ languages.</dd>
<dt>typed lexical</dt>
<dd> A <code>lexical variable</code> lexical&gt;that is declared with a <code>class</code> type: <tt>&quot;my Pony $bill&quot;</tt>.</dd>
<dt>typeglob</dt>
<dd> Use of a single identifier, prefixed with <tt>&quot;*&quot;</tt>. For example, <tt>*name</tt> stands for any or all of <tt>$name</tt>, <tt>@name</tt>, <tt>%name</tt>, <tt>&amp;name</tt>, or just <tt>&quot;name&quot;</tt>. How you use it determines whether it is interpreted as all or only one of them. See “Typeglobs and Filehandles” in Camel chapter 2, “Bits and Pieces”.</dd>
<dt>typemap</dt>
<dd> A description of how C types may be transformed to and from Perl types within an <code>extension</code> module written in <code>XS</code>.</dd></dl>
<h3>U</h3>
<dl>
<dt>UDP</dt>
<dd> User Datagram Protocol, the typical way to send <code>datagrams</code> over the Internet.</dd>
<dt>UID</dt>
<dd> A user ID. Often used in the context of <code>file</code> or <code>process</code> ownership.</dd>
<dt>umask</dt>
<dd> A mask of those <code>permission bits</code> that should be forced off when creating files or directories, in order to establish a policy of whom you’ll ordinarily deny access to. See the <tt>&quot;umask&quot;</tt> function.</dd>
<dt>unary operator</dt>
<dd> An operator with only one <code>operand</code>, like <tt>&quot;!&quot;</tt> or <tt>&quot;chdir&quot;</tt>. Unary operators are usually prefix operators; that is, they precede their operand. The <tt>&quot;++&quot;</tt> and <tt>&quot;––&quot;</tt> operators can be either prefix or postfix. (Their position <i>does</i> change their meanings.)</dd>
<dt>Unicode</dt>
<dd> A character set comprising all the major character sets of the world, more or less. See &lt;<a rel="nofollow" href="http://www.unicode.org">http://www.unicode.org</a>&gt;.</dd>
<dt>Unix</dt>
<dd> A very large and constantly evolving language with several alternative and largely incompatible syntaxes, in which anyone can define anything any way they choose, and usually do. Speakers of this language think it’s easy to learn because it’s so easily twisted to one’s own ends, but dialectical differences make tribal intercommunication nearly impossible, and travelers are often reduced to a pidgin-like subset of the language. To be universally understood, a Unix shell programmer must spend years of study in the art. Many have abandoned this discipline and now communicate via an Esperanto-like language called Perl. </dd>
<p> In ancient times, Unix was also used to refer to some code that a couple of people at Bell Labs wrote to make use of a PDP-7 computer that wasn’t doing much of anything else at the time.</p>
<dt>uppercase</dt>
<dd> In Unicode, not just characters with the General Category of Uppercase Letter, but any character with the Uppercase property, including some Letter Numbers and Symbols. Not to be confused with <code>titlecase</code>.</dd></dl>
<h3>V</h3>
<dl>
<dt>value</dt>
<dd> An actual piece of data, in contrast to all the variables, references, keys, indices, operators, and whatnot that you need to access the value.</dd>
<dt>variable</dt>
<dd> A named storage location that can hold any of various kinds of <code>value</code>, as your program sees fit.</dd>
<dt>variable interpolation</dt>
<dd> The <code>interpolation</code> of a scalar or array variable into a string.</dd>
<dt>variadic</dt>
<dd> Said of a <code>function</code> that happily receives an indeterminate number of <code>actual arguments</code>.</dd>
<dt>vector</dt>
<dd> Mathematical jargon for a list of <code>scalar values</code>.</dd>
<dt>virtual</dt>
<dd> Providing the appearance of something without the reality, as in: virtual memory is not real memory. (See also <code>memory</code>.) The opposite of “virtual” is “transparent”, which means providing the reality of something without the appearance, as in: Perl handles the variable-length UTF‑8 character encoding transparently.</dd>
<dt>void context</dt>
<dd> A form of <code>scalar context</code> in which an <code>expression</code> is not expected to return any <code>value</code> at all and is evaluated for its <code>side effects</code> alone.</dd>
<dt>v-string</dt>
<dd> A “version” or “vector” <code>string</code> specified with a <tt>&quot;v&quot;</tt> followed by a series of decimal integers in dot notation, for instance, <tt>&quot;v1.20.300.4000&quot;</tt>. Each number turns into a <code>character</code> with the specified ordinal value. (The <tt>&quot;v&quot;</tt> is optional when there are at least three integers.)</dd></dl>
<h3>W</h3>
<dl>
<dt>warning</dt>
<dd> A message printed to the <tt>&quot;STDERR&quot;</tt> stream to the effect that something might be wrong but isn’t worth blowing up over. See <tt>&quot;warn&quot;</tt> in Camel chapter 27, “Functions” and the <tt>&quot;warnings&quot;</tt> pragma in Camel chapter 28, “Pragmantic Modules”.</dd>
<dt>watch expression</dt>
<dd> An expression which, when its value changes, causes a breakpoint in the Perl debugger.</dd>
<dt>weak reference</dt>
<dd> A reference that doesn’t get counted normally. When all the normal references to data disappear, the data disappears. These are useful for circular references that would never disappear otherwise.</dd>
<dt>whitespace</dt>
<dd> A <code>character</code> that moves your cursor but doesn’t otherwise put anything on your screen. Typically refers to any of: space, tab, line feed, carriage return, or form feed. In Unicode, matches many other characters that Unicode considers whitespace, including the ɴ-ʙʀ .</dd>
<dt>word</dt>
<dd> In normal “computerese”, the piece of data of the size most efficiently handled by your computer, typically 32 bits or so, give or take a few powers of 2. In Perl culture, it more often refers to an alphanumeric <code>identifier</code> (including underscores), or to a string of nonwhitespace <code>characters</code> bounded by whitespace or string boundaries.</dd>
<dt>working directory</dt>
<dd> Your current <code>directory</code>, from which relative pathnames are interpreted by the <code>operating system</code>. The operating system knows your current directory because you told it with a <tt>&quot;chdir&quot;</tt>, or because you started out in the place where your parent <code>process</code> was when you were born.</dd>
<dt>wrapper</dt>
<dd> A program or subroutine that runs some other program or subroutine for you, modifying some of its input or output to better suit your purposes.</dd>
<dt>WYSIWYG</dt>
<dd> What You See Is What You Get. Usually used when something that appears on the screen matches how it will eventually look, like Perl’s <tt>&quot;format&quot;</tt> declarations. Also used to mean the opposite of magic because everything works exactly as it appears, as in the three- argument form of <tt>&quot;open&quot;</tt>.</dd></dl>
<h3>X</h3>
<dl>
<dt>XS</dt>
<dd> An extraordinarily exported, expeditiously excellent, expressly eXternal Subroutine, executed in existing C or C++ or in an exciting extension language called (exasperatingly) XS.</dd>
<dt>XSUB</dt>
<dd> An external <code>subroutine</code> defined in <code>XS</code>.</dd></dl>
<h3>Y</h3>
<dl>
<dt>yacc</dt>
<dd> Yet Another Compiler Compiler. A parser generator without which Perl probably would not have existed. See the file <i>perly.y</i> in the Perl source distribution.</dd></dl>
<h3>Z</h3>
<dl>
<dt>zero width</dt>
<dd> A subpattern <code>assertion</code> matching the <code>null string</code> between <code>characters</code>.</dd>
<dt>zombie</dt>
<dd> A process that has died (exited) but whose parent has not yet received proper notification of its demise by virtue of having called <tt>&quot;wait&quot;</tt> or <tt>&quot;waitpid&quot;</tt>. If you <tt>&quot;fork&quot;</tt>, you must clean up after your child processes when they exit; otherwise, the process table will fill up and your system administrator will Not Be Happy with you.</dd></dl>
<h2>AUTHOR AND COPYRIGHT</h2>
<p> Based on the Glossary of <i>Programming Perl</i>, Fourth Edition, by Tom Christiansen, brian d foy, Larry Wall, &amp; Jon Orwant. Copyright (c) 2000, 1996, 1991, 2012 O&#8217;Reilly Media, Inc. This document may be distributed under the same terms as Perl itself. </p>

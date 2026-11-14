---
title: "perlintro(1)"
name: "perlintro"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlintro/"
---

<h2 class="name">NAME</h2>
 

 perlintro -- a brief introduction and overview of Perl 

<h2>DESCRIPTION</h2>

 This document is intended to give you a quick overview of the Perl programming language, along with pointers to further documentation. It is intended as a ``bootstrap'' guide for those who are new to the language, and provides just enough information for you to be able to read other peoples' Perl and understand roughly what it's doing, or write your own simple scripts. 

 This introductory document does not aim to be complete. It does not even aim to be entirely accurate. In some cases perfection has been sacrificed in the goal of getting the general idea across. You are <i>strongly</i> advised to follow this introduction with more information from the full Perl manual, the table of contents to which can be found in perltoc. 

 Throughout this document you'll see references to other parts of the Perl documentation. You can read that documentation using the <tt>&quot;perldoc&quot;</tt> command or whatever method you're using to read this document. 

 Throughout Perl's documentation, you'll find numerous examples intended to help explain the discussed features. Please keep in mind that many of them are code fragments rather than complete programs. 

 These examples often reflect the style and preference of the author of that piece of the documentation, and may be briefer than a corresponding line of code in a real program. Except where otherwise noted, you should assume that <tt>&quot;use strict&quot;</tt> and <tt>&quot;use warnings&quot;</tt> statements appear earlier in the ``program'', and that any variables used have already been declared, even if those declarations have been omitted to make the example easier to read. 

 Do note that the examples have been written by many different authors over a period of several decades. Styles and techniques will therefore differ, although some effort has been made to not vary styles too widely in the same sections. Do not consider one style to be better than others - ``There's More Than One Way To Do It'' is one of Perl's mottos. After all, in your journey as a programmer, you are likely to encounter different styles.

<h3>What is Perl?</h3>

 Perl is a general-purpose programming language originally developed for text manipulation and now used for a wide range of tasks including system administration, web development, network programming, <font SIZE="-1">GUI</font> development, and more. 

 The language is intended to be practical (easy to use, efficient, complete) rather than beautiful (tiny, elegant, minimal). Its major features are that it's easy to use, supports both procedural and object-oriented (<font SIZE="-1">OO</font>) programming, has powerful built-in support for text processing, and has one of the world's most impressive collections of third-party modules. 

 Different definitions of Perl are given in perl, perlfaq1 and no doubt other places. From this we can determine that Perl is different things to different people, but that lots of people think it's at least worth writing about.

<h3>Running Perl programs</h3>

 To run a Perl program from the Unix command line: 

 <pre>
 perl progname.pl
</pre> 

 Alternatively, put this as the first line of your script: 

 <pre>
 #!/usr/bin/env perl
</pre> 

 ... and run the script as <i>/path/to/script.pl</i>. Of course, it'll need to be executable first, so <tt>&quot;chmod 755 script.pl&quot;</tt> (under Unix). 

 (This start line assumes you have the <b>env</b> program. You can also put directly the path to your perl executable, like in <tt>&quot;#!/usr/bin/perl&quot;</tt>). 

 For more information, including instructions for other platforms such as Windows and Mac <font SIZE="-1">OS,</font> read perlrun.

<h3>Safety net</h3>

 Perl by default is very forgiving. In order to make it more robust it is recommended to start every program with the following lines: 

 <pre>
 #!/usr/bin/perl
 use strict;
 use warnings;
</pre> 

 The two additional lines request from perl to catch various common problems in your code. They check different things so you need both. A potential problem caught by <tt>&quot;use strict;&quot;</tt> will cause your code to stop immediately when it is encountered, while <tt>&quot;use warnings;&quot;</tt> will merely give a warning (like the command-line switch <b>-w</b>) and let your code run. To read more about them check their respective manual pages at strict and warnings.

<h3>Basic syntax overview</h3>

 A Perl script or program consists of one or more statements. These statements are simply written in the script in a straightforward fashion. There is no need to have a <tt>&quot;main()&quot;</tt> function or anything of that kind. 

 Perl statements end in a semi-colon: 

 <pre>
 print &quot;Hello, world&quot;;
</pre> 

 Comments start with a hash symbol and run to the end of the line 

 <pre>
 # This is a comment
</pre> 

 Whitespace is irrelevant: 

 <pre>
 print
     &quot;Hello, world&quot;
     ;
</pre> 

 ... except inside quoted strings: 

 <pre>
 # this would print with a linebreak in the middle
 print &quot;Hello
 world&quot;;
</pre> 

 Double quotes or single quotes may be used around literal strings: 

 <pre>
 print &quot;Hello, world&quot;;
 print 'Hello, world';
</pre> 

 However, only double quotes ``interpolate'' variables and special characters such as newlines (<tt>&quot;\n&quot;</tt>): 

 <pre>
 print &quot;Hello, $name\n&quot;;     # works fine
 print 'Hello, $name\n';     # prints $name\n literally
</pre> 

 Numbers don't need quotes around them: 

 <pre>
 print 42;
</pre> 

 You can use parentheses for functions' arguments or omit them according to your personal taste. They are only required occasionally to clarify issues of precedence. 

 <pre><code>
print("Hello, world\n");
print "Hello, world\n";
</code></pre> 

 More detailed information about Perl syntax can be found in perlsyn.

<h3>Perl variable types</h3>

 Perl has three main variable types: scalars, arrays, and hashes.
<dl>
<dt>Scalars
<dd> A scalar represents a single value: 

 <pre>
 my $animal = &quot;camel&quot;;
 my $answer = 42;
</pre> 

 Scalar values can be strings, integers or floating point numbers, and Perl will automatically convert between them as required. There is no need to pre-declare your variable types, but you have to declare them using the <tt>&quot;my&quot;</tt> keyword the first time you use them. (This is one of the requirements of <tt>&quot;use strict;&quot;</tt>.) 

 Scalar values can be used in various ways: 

 <pre>
 print $animal;
 print &quot;The animal is $animal\n&quot;;
 print &quot;The square of $answer is &quot;, $answer * $answer, &quot;\n&quot;;
</pre> 

 There are a number of ``magic'' scalars with names that look like punctuation or line noise. These special variables are used for all kinds of purposes, and are documented in perlvar. The only one you need to know about for now is <tt>$_</tt> which is the ``default variable''. It's used as the default argument to a number of functions in Perl, and it's set implicitly by certain looping constructs. 

 <pre>
 print;          # prints contents of $_ by default
</pre>
<dt>Arrays
<dd> An array represents a list of values: 

 
my @animals = ("camel", "llama", "owl");
my @numbers = (23, 42, 69);
my @mixed = ("camel", 42, 1.23);
 

 Arrays are zero-indexed. Here's how you get at elements in an array: 

 
print $animals[0];
#prints "camel" print $animals[1];
#prints "llama"
 

 The special variable <tt>$#array</tt> tells you the index of the last element of an array: 

 <pre>
 print $mixed[$#mixed];       # last element, prints 1.23
</pre> 

 You might be tempted to use <tt>&quot;$#array + 1&quot;</tt> to tell you how many items there are in an array. Don't bother. As it happens, using <tt>@array</tt> where Perl expects to find a scalar value (``in scalar context'') will give you the number of elements in the array: 

 <pre>
 if (@animals &lt; 5) { ... }
</pre> 

 The elements we're getting from the array start with a <tt>&quot;$&quot;</tt> because we're getting just a single value out of the array; you ask for a scalar, you get a scalar. 

 To get multiple values from an array: 

 
@animals[0, 1];
#gives("camel", "llama");
@animals[0..2];
#gives("camel", "llama", "owl");
@animals[1.. $ #animals];
#gives all except the first element
 

 This is called an ``array slice''. 

 You can do various useful things to lists: 

 <pre>
 my @sorted    = sort @animals;
 my @backwards = reverse @numbers;
</pre> 

 There are a couple of special arrays too, such as <tt>@ARGV</tt> (the command line arguments to your script) and <tt>@_</tt> (the arguments passed to a subroutine). These are documented in perlvar.
<dt>Hashes
<dd> A hash represents a set of key/value pairs: 

 <pre>
 my %fruit_color = (&quot;apple&quot;, &quot;red&quot;, &quot;banana&quot;, &quot;yellow&quot;);
</pre> 

 You can use whitespace and the <tt>&quot;=&gt;&quot;</tt> operator to lay them out more nicely: 

 <pre>
 my %fruit_color = (
     apple  =&gt; &quot;red&quot;,
     banana =&gt; &quot;yellow&quot;,
 );
</pre> 

 To get at hash elements: 

 <pre>
 $fruit_color{&quot;apple&quot;};           # gives &quot;red&quot;
</pre> 

 You can get at lists of keys and values with <tt>&quot;keys()&quot;</tt> and <tt>&quot;values()&quot;</tt>. 

 <pre>
 my @fruits = keys %fruit_colors;
 my @colors = values %fruit_colors;
</pre> 

 Hashes have no particular internal order, though you can sort the keys and loop through them. 

 Just like special scalars and arrays, there are also special hashes. The most well known of these is <tt>%ENV</tt> which contains environment variables. Read all about it (and other special variables) in perlvar.</dl>
 

 Scalars, arrays and hashes are documented more fully in perldata. 

 More complex data types can be constructed using references, which allow you to build lists and hashes within lists and hashes. 

 A reference is a scalar value and can refer to any other Perl data type. So by storing a reference as the value of an array or hash element, you can easily create lists and hashes within lists and hashes. The following example shows a 2 level hash of hash structure using anonymous hash references. 

 
my $variables = {
    scalar = &gt; {
                   description = &gt; "single item",
                   sigil = &gt; '$',
               },
    array = &gt; {
                  description = &gt; "ordered list of items",
                  sigil = &gt; '@',
              },
    hash = &gt; {
                 description = &gt; "key/value pairs",
                 sigil = &gt; '%',
             },
};
print "Scalars begin with a $variables-&gt;{'scalar'}-&gt;{'sigil'}\n";
 

 Exhaustive information on the topic of references can be found in perlreftut, perllol, perlref and perldsc.

<h3>Variable scoping</h3>

 Throughout the previous section all the examples have used the syntax: 

 <pre>
 my $var = &quot;value&quot;;
</pre> 

 The <tt>&quot;my&quot;</tt> is actually not required; you could just use: 

 <pre>
 $var = &quot;value&quot;;
</pre> 

 However, the above usage will create global variables throughout your program, which is bad programming practice. <tt>&quot;my&quot;</tt> creates lexically scoped variables instead. The variables are scoped to the block (i.e. a bunch of statements surrounded by curly-braces) in which they are defined. 

 
my $x = "foo";
my $some_condition = 1;
if ($some_condition) {
    my $y = "bar";
    print $x;
#prints "foo" print $y;
#prints "bar"
}
print $x;
#prints "foo" print $y;
#prints nothing;
$y has fallen out of scope
 

 Using <tt>&quot;my&quot;</tt> in combination with a <tt>&quot;use strict;&quot;</tt> at the top of your Perl scripts means that the interpreter will pick up certain common programming errors. For instance, in the example above, the final <tt>&quot;print $y&quot;</tt> would cause a compile-time error and prevent you from running the program. Using <tt>&quot;strict&quot;</tt> is highly recommended.

<h3>Conditional and looping constructs</h3>

 Perl has most of the usual conditional and looping constructs. As of Perl 5.10, it even has a case/switch statement (spelled <tt>&quot;given&quot;</tt>/<tt>&quot;when&quot;</tt>). See ``Switch Statements'' in perlsyn for more details. 

 The conditions can be any Perl expression. See the list of operators in the next section for information on comparison and boolean logic operators, which are commonly used in conditional statements.
<dl>
<dt>if
<dd> 
if (condition) {
    ...
}
elsif(other condition)
{
    ...
}
else
{
    ...
}
 

 There's also a negated version of it: 

 <pre>
 unless ( condition ) {
     ...
 }
</pre> 

 This is provided as a more readable version of <tt>&quot;if (!</tt>condition<tt>)&quot;</tt>. 

 Note that the braces are required in Perl, even if you've only got one line in the block. However, there is a clever way of making your one-line conditional blocks more English like: 

 
#the traditional way
if ($zippy) {
    print "Yow!";
}
#the Perlish post - condition way
print "Yow!" if $zippy;
print "We have no bananas" unless $bananas;

<dt>while
<dd> <pre>
 while ( condition ) {
     ...
 }
</pre> 

 There's also a negated version, for the same reason we have <tt>&quot;unless&quot;</tt>: 

 <pre>
 until ( condition ) {
     ...
 }
</pre> 

 You can also use <tt>&quot;while&quot;</tt> in a post-condition: 

 <pre>
 print &quot;LA LA LA\n&quot; while 1;          # loops forever
</pre>
<dt>for
<dd> Exactly like C: 

 
for ($i = 0; $i &lt;= $max; $i++) {
    ...
}
 

 The C style for loop is rarely needed in Perl since Perl provides the more friendly list scanning <tt>&quot;foreach&quot;</tt> loop.
<dt>foreach
<dd> 
foreach (@array) {
    print "This element is $_\n";
}
print $list[$_] foreach 0..$max;
#you don't have to use the default $_ either...
foreach
    my $key(keys % hash)
    {
        print "The value of $key is $hash{$key}\n";
    }
 

 The <tt>&quot;foreach&quot;</tt> keyword is actually a synonym for the <tt>&quot;for&quot;</tt> keyword. See <tt>&quot;&quot;Foreach Loops&quot; in perlsyn&quot;</tt>.</dl>
 

 For more detail on looping constructs (and some that weren't mentioned in this overview) see perlsyn.

<h3>Builtin operators and functions</h3>

 Perl comes with a wide selection of builtin functions. Some of the ones we've already seen include <tt>&quot;print&quot;</tt>, <tt>&quot;sort&quot;</tt> and <tt>&quot;reverse&quot;</tt>. A list of them is given at the start of perlfunc and you can easily read about any given function by using <tt>&quot;perldoc -f </tt>functionname<tt>&quot;</tt>. 

 Perl operators are documented in full in perlop, but here are a few of the most common ones:
<dl>
<dt>Arithmetic
<dd> <pre>
 +   addition
 -   subtraction
 *   multiplication
 /   division
</pre>
<dt>Numeric comparison
<dd> 
== equality != inequality&lt;less than&gt; greater than &lt;= less than or equal &gt;= greater than or equal

<dt>String comparison
<dd> <pre>
 eq  equality
 ne  inequality
 lt  less than
 gt  greater than
 le  less than or equal
 ge  greater than or equal
</pre> 

 (Why do we have separate numeric and string comparisons? Because we don't have special variable types, and Perl needs to know whether to sort numerically (where 99 is less than 100) or alphabetically (where 100 comes before 99).
<dt>Boolean logic
<dd> <pre>
 &amp;&amp;  and
 ||  or
 !   not
</pre> 

 (<tt>&quot;and&quot;</tt>, <tt>&quot;or&quot;</tt> and <tt>&quot;not&quot;</tt> aren't just in the above table as descriptions of the operators. They're also supported as operators in their own right. They're more readable than the C-style operators, but have different precedence to <tt>&quot;&amp;&amp;&quot;</tt> and friends. Check perlop for more detail.)
<dt>Miscellaneous
<dd> <pre>
 =   assignment
 .   string concatenation
 x   string multiplication
 ..  range operator (creates a list of numbers or strings)
</pre></dl>
 

 Many operators can be combined with a <tt>&quot;=&quot;</tt> as follows: 

 
$a += 1;
#same as $a = $a + 1 $a -= 1;
#same as $a = $a - 1 $a.= "\n";
#same as $a = $a."\n";


<h3>Files and I/O</h3>

 You can open a file for input or output using the <tt>&quot;open()&quot;</tt> function. It's documented in extravagant detail in perlfunc and perlopentut, but in short: 

 
open(my $in, "&lt;", "input.txt") or die "Can't open input.txt: $!";
open(my $out, "&gt;", "output.txt") or die "Can't open output.txt: $!";
open(my $log, "&gt;&gt;", "my.log") or die "Can't open my.log: $!";
 

 You can read from an open filehandle using the <tt>&quot;&lt;&gt;&quot;</tt> operator. In scalar context it reads a single line from the filehandle, and in list context it reads the whole file in, assigning each line to an element of the list: 

 <pre>
 my $line  = &lt;$in&gt;;
 my @lines = &lt;$in&gt;;
</pre> 

 Reading in the whole file at one time is called slurping. It can be useful but it may be a memory hog. Most text file processing can be done a line at a time with Perl's looping constructs. 

 The <tt>&quot;&lt;&gt;&quot;</tt> operator is most often seen in a <tt>&quot;while&quot;</tt> loop: 

 
while (&lt;$in&gt;) {
#assigns each line in turn to $_
        print "Just read in this line: $_";
}
 

 We've already seen how to print to standard output using <tt>&quot;print()&quot;</tt>. However, <tt>&quot;print()&quot;</tt> can also take an optional first argument specifying which filehandle to print to: 

 <pre>
 print STDERR &quot;This is your final warning.\n&quot;;
 print $out $record;
 print $log $logmessage;
</pre> 

 When you're done with your filehandles, you should <tt>&quot;close()&quot;</tt> them (though to be honest, Perl will clean up after you if you forget): 

 <pre>
 close $in or die &quot;$in: $!&quot;;
</pre>

<h3>Regular expressions</h3>

 Perl's regular expression support is both broad and deep, and is the subject of lengthy documentation in perlrequick, perlretut, and elsewhere. However, in short:
<dl>
<dt>Simple matching
<dd> 
if (/ foo /) {
    ...
}
#true if $_ contains "foo" if ($a = ~ / foo /)
{
    ...
}
#true if $a contains "foo"
 

 The <tt>&quot;//&quot;</tt> matching operator is documented in perlop. It operates on <tt>$_</tt> by default, or can be bound to another variable using the <tt>&quot;=~&quot;</tt> binding operator (also documented in perlop).
<dt>Simple substitution
<dd> <pre>
 s/foo/bar/;               # replaces foo with bar in $_
 $a =~ s/foo/bar/;         # replaces foo with bar in $a
 $a =~ s/foo/bar/g;        # replaces ALL INSTANCES of foo with bar
                           # in $a
</pre> 

 The <tt>&quot;s///&quot;</tt> substitution operator is documented in perlop.
<dt>More complex regular expressions
<dd> You don't just have to match on fixed strings. In fact, you can match on just about anything you could dream of by using more complex regular expressions. These are documented at great length in perlre, but for the meantime, here's a quick cheat sheet: 

 
.a single character
 \s a whitespace character(space, tab, newline,
                            ...)
 \S non -
        whitespace character
 \d a digit(0 - 9)
 \D a non - digit
 \w a word character(a - z, A - Z, 0 - 9, _)
 \W a non - word character[aeiou] matches a single character in the given set[^aeiou] matches a single character outside the given set(foo | bar | baz) matches any of the alternatives specified
    ^ start of string
    $ end of string
 

 Quantifiers can be used to specify how many of the previous thing you want to match on, where ``thing'' means either a literal character, one of the metacharacters listed above, or a group of characters or metacharacters in parentheses. 

 <pre>
 *                   zero or more of the previous thing
 +                   one or more of the previous thing
 ?                   zero or one of the previous thing
 {3}                 matches exactly 3 of the previous thing
 {3,6}               matches between 3 and 6 of the previous thing
 {3,}                matches 3 or more of the previous thing
</pre> 

 Some brief examples: 

 
/ ^\d + / string starts with one or more digits / ^$ / nothing in the string(start and end are adjacent) / (\d\s){
                                                                                                               3} /
                                        three digits,
    each followed by a whitespace character(eg "3 4 5 ") / (a.) + / matches a string in which every odd - numbered letter is a(eg "abacadaf")
#This loop reads from STDIN, and prints non - blank lines:
                                                                                                              while (&lt;&gt;)
{
    next if / ^$ / ;
    print;
}

<dt>Parentheses for capturing
<dd> As well as grouping, parentheses serve a second purpose. They can be used to capture the results of parts of the regexp match for later use. The results end up in <tt>$1</tt>, <tt>$2</tt> and so on. 

 
#a cheap and nasty way to break an email address up into parts
if ($email = ~ / ([^@] +) @(.+) /) {
    print "Username is $1\n";
    print "Hostname is $2\n";
}

<dt>Other regexp features
<dd> Perl regexps also support backreferences, lookaheads, and all kinds of other complex details. Read all about them in perlrequick, perlretut, and perlre.</dl>

<h3>Writing subroutines</h3>

 Writing subroutines is easy: 

 
sub logger
{
    my $logmessage = shift;
    open my $logfile, "&gt;&gt;", "my.log" or die "Could not open my.log: $!";
    print $logfile $logmessage;
}
 

 Now we can use the subroutine just as any other built-in function: 

 <pre>
 logger(&quot;We have a logger subroutine!&quot;);
</pre> 

 What's that <tt>&quot;shift&quot;</tt>? Well, the arguments to a subroutine are available to us as a special array called <tt>@_</tt> (see perlvar for more on that). The default argument to the <tt>&quot;shift&quot;</tt> function just happens to be <tt>@_</tt>. So <tt>&quot;my $logmessage = shift;&quot;</tt> shifts the first item off the list of arguments and assigns it to <tt>$logmessage</tt>. 

 We can manipulate <tt>@_</tt> in other ways too: 

 
my($logmessage, $priority) = @_;
#common my $logmessage = $_[0];
#uncommon, and ugly
 

 Subroutines can also return values: 

 <pre><code>
sub square
{
    my $num = shift;
    my $result = $num * $num;
    return $result;
}
</code></pre> 

 Then use it like: 

 <pre>
 $sq = <a HREF="//www.systutorials.com/docs/linux/man/8-square/">square</a>(8);
</pre> 

 For more information on writing subroutines, see perlsub.

<h3><font SIZE="-1">OO</font> Perl</h3>

 <font SIZE="-1">OO</font> Perl is relatively simple and is implemented using references which know what sort of object they are based on Perl's concept of packages. However, <font SIZE="-1">OO</font> Perl is largely beyond the scope of this document. Read perlootut and perlobj. 

 As a beginning Perl programmer, your most common use of <font SIZE="-1">OO</font> Perl will be in using third-party modules, which are documented below.

<h3>Using Perl modules</h3>

 Perl modules provide a range of features to help you avoid reinventing the wheel, and can be downloaded from <font SIZE="-1">CPAN</font> ( &lt;<a rel="nofollow" HREF="http://www.cpan.org/">http://www.cpan.org/</a>&gt; ). A number of popular modules are included with the Perl distribution itself. 

 Categories of modules range from text manipulation to network protocols to database integration to graphics. A categorized list of modules is also available from <font SIZE="-1">CPAN.</font> 

 To learn how to install modules you download from <font SIZE="-1">CPAN,</font> read perlmodinstall. 

 To learn how to use a particular module, use <tt>&quot;perldoc </tt>Module::Name<tt>&quot;</tt>. Typically you will want to <tt>&quot;use </tt>Module::Name<tt>&quot;</tt>, which will then give you access to exported functions or an <font SIZE="-1">OO</font> interface to the module. 

 perlfaq contains questions and answers related to many common tasks, and often provides suggestions for good <font SIZE="-1">CPAN</font> modules to use. 

 perlmod describes Perl modules in general. perlmodlib lists the modules which came with your Perl installation. 

 If you feel the urge to write Perl modules, perlnewmod will give you good advice.

<h2>AUTHOR</h2>

 Kirrily ``Skud'' Robert &lt;skud [at] cpan.org&gt; 

<h2>Index</h2>



<dt><a HREF="#lbAQ">AUTHOR</a>
<dd></dl>

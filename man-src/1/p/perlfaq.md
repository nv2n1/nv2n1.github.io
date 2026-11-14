---
title: "perlfaq(1)"
name: "perlfaq"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlfaq/"
description: "perlfaq – Frequently asked questions about Perl"
---

<h2 class="name">NAME</h2>
<p> perlfaq &#8211; Frequently asked questions about Perl </p>
<h2>VERSION</h2>
<p> version 5.20190126</p>
<h2>DESCRIPTION</h2>
<p> The perlfaq comprises several documents that answer the most commonly asked questions about Perl and Perl programming. It&#8217;s divided by topic into nine major sections outlined in this document.</p>
<h3>Where to find the perlfaq</h3>
<p> The perlfaq is an evolving document. Read the latest version at &lt;<a rel="nofollow" href="http://learn.perl.org/faq/">http://learn.perl.org/faq/</a>&gt;. It is also included in the standard Perl distribution.</p>
<h3>How to use the perlfaq</h3>
<p> The <tt>&quot;perldoc&quot;</tt> command line tool is part of the standard Perl distribution. To read the perlfaq: </p>
<pre>
    $ perldoc perlfaq
</pre>
<p> To search the perlfaq question headings: </p>
<pre>
    $ perldoc -q open
</pre>
<h3>How to contribute to the perlfaq</h3>
<p> Review &lt;<a rel="nofollow" href="https://github.com/perl-doc-cats/perlfaq/wiki">https://github.com/perl-doc-cats/perlfaq/wiki</a>&gt;. If you don&#8217;t find your suggestion create an issue or pull request against &lt;<a rel="nofollow" href="https://github.com/perl-doc-cats/perlfaq">https://github.com/perl-doc-cats/perlfaq</a>&gt;. </p>
<p> Once approved, changes are merged into &lt;<a rel="nofollow" href="https://github.com/tpf/perlfaq">https://github.com/tpf/perlfaq</a>&gt;, the repository which drives &lt;<a rel="nofollow" href="http://learn.perl.org/faq/">http://learn.perl.org/faq/</a>&gt;, and they are distributed with the next Perl 5 release.</p>
<h3>What if my question isn&#8217;t answered in the <font SIZE="-1">FAQ</font>?</h3>
<p> Try the resources in perlfaq2.</p>
<h2>TABLE OF CONTENTS</h2>
<dl>
<dt>perlfaq1 &#8211; General Questions About Perl</p>
<dd>
<dt>perlfaq2 &#8211; Obtaining and Learning about Perl</p>
<dd>
<dt>perlfaq3 &#8211; Programming Tools</p>
<dd>
<dt>perlfaq4 &#8211; Data Manipulation</p>
<dd>
<dt>perlfaq5 &#8211; Files and Formats</p>
<dd>
<dt>perlfaq6 &#8211; Regular Expressions</p>
<dd>
<dt>perlfaq7 &#8211; General Perl Language Issues</p>
<dd>
<dt>perlfaq8 &#8211; System Interaction</p>
<dd>
<dt>perlfaq9 &#8211; Web, Email and Networking</p>
<dd></dl>
<h2>THE QUESTIONS</h2>
<h3>perlfaq1: General Questions About Perl</h3>
<p> This section of the <font SIZE="-1">FAQ</font> answers very general, high-level questions about Perl.</p>
<dl>
<dt>&bull;</p>
<dd> What is Perl?</p>
<dt>&bull;</p>
<dd> Who supports Perl? Who develops it? Why is it free?</p>
<dt>&bull;</p>
<dd> Which version of Perl should I use?</p>
<dt>&bull;</p>
<dd> What are Perl 4, Perl 5, or Perl 6?</p>
<dt>&bull;</p>
<dd> What is Perl 6?</p>
<dt>&bull;</p>
<dd> How stable is Perl?</p>
<dt>&bull;</p>
<dd> How often are new versions of Perl released?</p>
<dt>&bull;</p>
<dd> Is Perl difficult to learn?</p>
<dt>&bull;</p>
<dd> How does Perl compare with other languages like Java, Python, <font SIZE="-1">REXX,</font> Scheme, or Tcl?</p>
<dt>&bull;</p>
<dd> Can I do [task] in Perl?</p>
<dt>&bull;</p>
<dd> When shouldn&#8217;t I program in Perl?</p>
<dt>&bull;</p>
<dd> What&#8217;s the difference between &#8220;perl&#8221; and &#8220;Perl&#8221;?</p>
<dt>&bull;</p>
<dd> What is a <font SIZE="-1">JAPH</font>?</p>
<dt>&bull;</p>
<dd> How can I convince others to use Perl?</dl>
<h3>perlfaq2: Obtaining and Learning about Perl</h3>
<p> This section of the <font SIZE="-1">FAQ</font> answers questions about where to find source and documentation for Perl, support, and related matters.</p>
<dl>
<dt>&bull;</p>
<dd> What machines support Perl? Where do I get it?</p>
<dt>&bull;</p>
<dd> How can I get a binary version of Perl?</p>
<dt>&bull;</p>
<dd> I don&#8217;t have a C compiler. How can I build my own Perl interpreter?</p>
<dt>&bull;</p>
<dd> I copied the Perl binary from one machine to another, but scripts don&#8217;t work.</p>
<dt>&bull;</p>
<dd> I grabbed the sources and tried to compile but gdbm/dynamic loading/malloc/linking/&#8230; failed. How do I make it work?</p>
<dt>&bull;</p>
<dd> What modules and extensions are available for Perl? What is <font SIZE="-1">CPAN</font>?</p>
<dt>&bull;</p>
<dd> Where can I get information on Perl?</p>
<dt>&bull;</p>
<dd> What is perl.com? Perl Mongers? pm.org? perl.org? cpan.org?</p>
<dt>&bull;</p>
<dd> Where can I post questions?</p>
<dt>&bull;</p>
<dd> Perl Books</p>
<dt>&bull;</p>
<dd> Which magazines have Perl content?</p>
<dt>&bull;</p>
<dd> Which Perl blogs should I read?</p>
<dt>&bull;</p>
<dd> What mailing lists are there for Perl?</p>
<dt>&bull;</p>
<dd> Where can I buy a commercial version of Perl?</p>
<dt>&bull;</p>
<dd> Where do I send bug reports?</dl>
<h3>perlfaq3: Programming Tools</h3>
<p> This section of the <font SIZE="-1">FAQ</font> answers questions related to programmer tools and programming support.</p>
<dl>
<dt>&bull;</p>
<dd> How do I do (anything)?</p>
<dt>&bull;</p>
<dd> How can I use Perl interactively?</p>
<dt>&bull;</p>
<dd> How do I find which modules are installed on my system?</p>
<dt>&bull;</p>
<dd> How do I debug my Perl programs?</p>
<dt>&bull;</p>
<dd> How do I profile my Perl programs?</p>
<dt>&bull;</p>
<dd> How do I cross-reference my Perl programs?</p>
<dt>&bull;</p>
<dd> Is there a pretty-printer (formatter) for Perl?</p>
<dt>&bull;</p>
<dd> Is there an <font SIZE="-1">IDE</font> or Windows Perl Editor?</p>
<dt>&bull;</p>
<dd> Where can I get Perl macros for vi?</p>
<dt>&bull;</p>
<dd> Where can I get perl-mode or cperl-mode for emacs?</p>
<dt>&bull;</p>
<dd> How can I use curses with Perl?</p>
<dt>&bull;</p>
<dd> How can I write a <font SIZE="-1">GUI</font> (X, Tk, Gtk, etc.) in Perl?</p>
<dt>&bull;</p>
<dd> How can I make my Perl program run faster?</p>
<dt>&bull;</p>
<dd> How can I make my Perl program take less memory?</p>
<dt>&bull;</p>
<dd> Is it safe to return a reference to local or lexical data?</p>
<dt>&bull;</p>
<dd> How can I free an array or hash so my program shrinks?</p>
<dt>&bull;</p>
<dd> How can I make my <font SIZE="-1">CGI</font> script more efficient?</p>
<dt>&bull;</p>
<dd> How can I hide the source for my Perl program?</p>
<dt>&bull;</p>
<dd> How can I compile my Perl program into byte code or C?</p>
<dt>&bull;</p>
<dd> How can I get <tt>&quot;#!perl&quot;</tt> to work on [<font SIZE="-1">MS-DOS,NT,&#8230;</font>]?</p>
<dt>&bull;</p>
<dd> Can I write useful Perl programs on the command line?</p>
<dt>&bull;</p>
<dd> Why don&#8217;t Perl one-liners work on my DOS/Mac/VMS system?</p>
<dt>&bull;</p>
<dd> Where can I learn about <font SIZE="-1">CGI</font> or Web programming in Perl?</p>
<dt>&bull;</p>
<dd> Where can I learn about object-oriented Perl programming?</p>
<dt>&bull;</p>
<dd> Where can I learn about linking C with Perl?</p>
<dt>&bull;</p>
<dd> I&#8217;ve read perlembed, perlguts, etc., but I can&#8217;t embed perl in my C program; what am I doing wrong?</p>
<dt>&bull;</p>
<dd> When I tried to run my script, I got this message. What does it mean?</p>
<dt>&bull;</p>
<dd> What&#8217;s MakeMaker?</dl>
<h3>perlfaq4: Data Manipulation</h3>
<p> This section of the <font SIZE="-1">FAQ</font> answers questions related to manipulating numbers, dates, strings, arrays, hashes, and miscellaneous data issues.</p>
<dl>
<dt>&bull;</p>
<dd> Why am I getting long decimals (eg, 19.9499999999999) instead of the numbers I should be getting (eg, 19.95)?</p>
<dt>&bull;</p>
<dd> Why is <code>int()</code> broken?</p>
<dt>&bull;</p>
<dd> Why isn&#8217;t my octal data interpreted correctly?</p>
<dt>&bull;</p>
<dd> Does Perl have a <code>round()</code> function? What about <code>ceil()</code> and <code>floor()</code>? Trig functions?</p>
<dt>&bull;</p>
<dd> How do I convert between numeric representations/bases/radixes?</p>
<dt>&bull;</p>
<dd> Why doesn&#8217;t &amp; work the way I want it to?</p>
<dt>&bull;</p>
<dd> How do I multiply matrices?</p>
<dt>&bull;</p>
<dd> How do I perform an operation on a series of integers?</p>
<dt>&bull;</p>
<dd> How can I output Roman numerals?</p>
<dt>&bull;</p>
<dd> Why aren&#8217;t my random numbers random?</p>
<dt>&bull;</p>
<dd> How do I get a random number between X and Y?</p>
<dt>&bull;</p>
<dd> How do I find the day or week of the year?</p>
<dt>&bull;</p>
<dd> How do I find the current century or millennium?</p>
<dt>&bull;</p>
<dd> How can I compare two dates and find the difference?</p>
<dt>&bull;</p>
<dd> How can I take a string and turn it into epoch seconds?</p>
<dt>&bull;</p>
<dd> How can I find the Julian Day?</p>
<dt>&bull;</p>
<dd> How do I find yesterday&#8217;s date?</p>
<dt>&bull;</p>
<dd> Does Perl have a Year 2000 or 2038 problem? Is Perl Y2K compliant?</p>
<dt>&bull;</p>
<dd> How do I validate input?</p>
<dt>&bull;</p>
<dd> How do I unescape a string?</p>
<dt>&bull;</p>
<dd> How do I remove consecutive pairs of characters?</p>
<dt>&bull;</p>
<dd> How do I expand function calls in a string?</p>
<dt>&bull;</p>
<dd> How do I find matching/nesting anything?</p>
<dt>&bull;</p>
<dd> How do I reverse a string?</p>
<dt>&bull;</p>
<dd> How do I expand tabs in a string?</p>
<dt>&bull;</p>
<dd> How do I reformat a paragraph?</p>
<dt>&bull;</p>
<dd> How can I access or change N characters of a string?</p>
<dt>&bull;</p>
<dd> How do I change the Nth occurrence of something?</p>
<dt>&bull;</p>
<dd> How can I count the number of occurrences of a substring within a string?</p>
<dt>&bull;</p>
<dd> How do I capitalize all the words on one line?</p>
<dt>&bull;</p>
<dd> How can I split a [character]-delimited string except when inside [character]?</p>
<dt>&bull;</p>
<dd> How do I strip blank space from the beginning/end of a string?</p>
<dt>&bull;</p>
<dd> How do I pad a string with blanks or pad a number with zeroes?</p>
<dt>&bull;</p>
<dd> How do I extract selected columns from a string?</p>
<dt>&bull;</p>
<dd> How do I find the soundex value of a string?</p>
<dt>&bull;</p>
<dd> How can I expand variables in text strings?</p>
<dt>&bull;</p>
<dd> What&#8217;s wrong with always quoting &#8220;$vars&#8221;?</p>
<dt>&bull;</p>
<dd> Why don&#8217;t my &lt;&lt;<font SIZE="-1">HERE</font> documents work?</p>
<dt>&bull;</p>
<dd> What is the difference between a list and an array?</p>
<dt>&bull;</p>
<dd> What is the difference between <tt>$array</tt>[1] and <tt>@array</tt>[1]?</p>
<dt>&bull;</p>
<dd> How can I remove duplicate elements from a list or array?</p>
<dt>&bull;</p>
<dd> How can I tell whether a certain element is contained in a list or array?</p>
<dt>&bull;</p>
<dd> How do I compute the difference of two arrays? How do I compute the intersection of two arrays?</p>
<dt>&bull;</p>
<dd> How do I test whether two arrays or hashes are equal?</p>
<dt>&bull;</p>
<dd> How do I find the first array element for which a condition is true?</p>
<dt>&bull;</p>
<dd> How do I handle linked lists?</p>
<dt>&bull;</p>
<dd> How do I handle circular lists?</p>
<dt>&bull;</p>
<dd> How do I shuffle an array randomly?</p>
<dt>&bull;</p>
<dd> How do I process/modify each element of an array?</p>
<dt>&bull;</p>
<dd> How do I select a random element from an array?</p>
<dt>&bull;</p>
<dd> How do I permute N elements of a list?</p>
<dt>&bull;</p>
<dd> How do I sort an array by (anything)?</p>
<dt>&bull;</p>
<dd> How do I manipulate arrays of bits?</p>
<dt>&bull;</p>
<dd> Why does <code>defined()</code> return true on empty arrays and hashes?</p>
<dt>&bull;</p>
<dd> How do I process an entire hash?</p>
<dt>&bull;</p>
<dd> How do I merge two hashes?</p>
<dt>&bull;</p>
<dd> What happens if I add or remove keys from a hash while iterating over it?</p>
<dt>&bull;</p>
<dd> How do I look up a hash element by value?</p>
<dt>&bull;</p>
<dd> How can I know how many entries are in a hash?</p>
<dt>&bull;</p>
<dd> How do I sort a hash (optionally by value instead of key)?</p>
<dt>&bull;</p>
<dd> How can I always keep my hash sorted?</p>
<dt>&bull;</p>
<dd> What&#8217;s the difference between &#8220;delete&#8221; and &#8220;undef&#8221; with hashes?</p>
<dt>&bull;</p>
<dd> Why don&#8217;t my tied hashes make the defined/exists distinction?</p>
<dt>&bull;</p>
<dd> How do I reset an <code>each()</code> operation part-way through?</p>
<dt>&bull;</p>
<dd> How can I get the unique keys from two hashes?</p>
<dt>&bull;</p>
<dd> How can I store a multidimensional array in a <font SIZE="-1">DBM</font> file?</p>
<dt>&bull;</p>
<dd> How can I make my hash remember the order I put elements into it?</p>
<dt>&bull;</p>
<dd> Why does passing a subroutine an undefined element in a hash create it?</p>
<dt>&bull;</p>
<dd> How can I make the Perl equivalent of a C structure/C<font SIZE="-2">++</font> class/hash or array of hashes or arrays?</p>
<dt>&bull;</p>
<dd> How can I use a reference as a hash key?</p>
<dt>&bull;</p>
<dd> How can I check if a key exists in a multilevel hash?</p>
<dt>&bull;</p>
<dd> How can I prevent addition of unwanted keys into a hash?</p>
<dt>&bull;</p>
<dd> How do I handle binary data correctly?</p>
<dt>&bull;</p>
<dd> How do I determine whether a scalar is a number/whole/integer/float?</p>
<dt>&bull;</p>
<dd> How do I keep persistent data across program calls?</p>
<dt>&bull;</p>
<dd> How do I print out or copy a recursive data structure?</p>
<dt>&bull;</p>
<dd> How do I define methods for every class/object?</p>
<dt>&bull;</p>
<dd> How do I verify a credit card checksum?</p>
<dt>&bull;</p>
<dd> How do I pack arrays of doubles or floats for <font SIZE="-1">XS</font> code?</dl>
<h3>perlfaq5: Files and Formats</h3>
<p> This section deals with I/O and the &#8220;f&#8221; issues: filehandles, flushing, formats, and footers.</p>
<dl>
<dt>&bull;</p>
<dd> How do I flush/unbuffer an output filehandle? Why must I do this?</p>
<dt>&bull;</p>
<dd> How do I change, delete, or insert a line in a file, or append to the beginning of a file?</p>
<dt>&bull;</p>
<dd> How do I count the number of lines in a file?</p>
<dt>&bull;</p>
<dd> How do I delete the last N lines from a file?</p>
<dt>&bull;</p>
<dd> How can I use Perl&#8217;s <tt>&quot;-i&quot;</tt> option from within a program?</p>
<dt>&bull;</p>
<dd> How can I copy a file?</p>
<dt>&bull;</p>
<dd> How do I make a temporary file name?</p>
<dt>&bull;</p>
<dd> How can I manipulate fixed-record-length files?</p>
<dt>&bull;</p>
<dd> How can I make a filehandle local to a subroutine? How do I pass filehandles between subroutines? How do I make an array of filehandles?</p>
<dt>&bull;</p>
<dd> How can I use a filehandle indirectly?</p>
<dt>&bull;</p>
<dd> How can I open a filehandle to a string?</p>
<dt>&bull;</p>
<dd> How can I set up a footer format to be used with <code>write()</code>?</p>
<dt>&bull;</p>
<dd> How can I <code>write()</code> into a string?</p>
<dt>&bull;</p>
<dd> How can I output my numbers with commas added?</p>
<dt>&bull;</p>
<dd> How can I translate tildes (~) in a filename?</p>
<dt>&bull;</p>
<dd> How come when I open a file read-write it wipes it out?</p>
<dt>&bull;</p>
<dd> Why do I sometimes get an &#8220;Argument list too long&#8221; when I use &lt;*&gt;?</p>
<dt>&bull;</p>
<dd> How can I open a file named with a leading &#8220;&gt;&#8221; or trailing blanks?</p>
<dt>&bull;</p>
<dd> How can I reliably rename a file?</p>
<dt>&bull;</p>
<dd> How can I lock a file?</p>
<dt>&bull;</p>
<dd> Why can&#8217;t I just open(<font SIZE="-1">FH, &#8220;</font>&gt;file.lock&#8221;)?</p>
<dt>&bull;</p>
<dd> I still don&#8217;t get locking. I just want to increment the number in the file. How can I do this?</p>
<dt>&bull;</p>
<dd> All I want to do is append a small amount of text to the end of a file. Do I still have to use locking?</p>
<dt>&bull;</p>
<dd> How do I randomly update a binary file?</p>
<dt>&bull;</p>
<dd> How do I get a file&#8217;s timestamp in perl?</p>
<dt>&bull;</p>
<dd> How do I set a file&#8217;s timestamp in perl?</p>
<dt>&bull;</p>
<dd> How do I print to more than one file at once?</p>
<dt>&bull;</p>
<dd> How can I read in an entire file all at once?</p>
<dt>&bull;</p>
<dd> How can I read in a file by paragraphs?</p>
<dt>&bull;</p>
<dd> How can I read a single character from a file? From the keyboard?</p>
<dt>&bull;</p>
<dd> How can I tell whether there&#8217;s a character waiting on a filehandle?</p>
<dt>&bull;</p>
<dd> How do I do a <tt>&quot;tail -f&quot;</tt> in perl?</p>
<dt>&bull;</p>
<dd> How do I <code>dup()</code> a filehandle in Perl?</p>
<dt>&bull;</p>
<dd> How do I close a file descriptor by number?</p>
<dt>&bull;</p>
<dd> Why can&#8217;t I use &#8220;C:	empoo&#8221; in <font SIZE="-1">DOS</font> paths? Why doesn&#8217;t `C:	empoo.exe` work?</p>
<dt>&bull;</p>
<dd> Why doesn&#8217;t glob(&#8220;*.*&#8221;) get all the files?</p>
<dt>&bull;</p>
<dd> Why does Perl let me delete read-only files? Why does <tt>&quot;-i&quot;</tt> clobber protected files? Isn&#8217;t this a bug in Perl?</p>
<dt>&bull;</p>
<dd> How do I select a random line from a file?</p>
<dt>&bull;</p>
<dd> Why do I get weird spaces when I print an array of lines?</p>
<dt>&bull;</p>
<dd> How do I traverse a directory tree?</p>
<dt>&bull;</p>
<dd> How do I delete a directory tree?</p>
<dt>&bull;</p>
<dd> How do I copy an entire directory?</dl>
<h3>perlfaq6: Regular Expressions</h3>
<p> This section is surprisingly small because the rest of the <font SIZE="-1">FAQ</font> is littered with answers involving regular expressions. For example, decoding a <font SIZE="-1">URL</font> and checking whether something is a number can be handled with regular expressions, but those answers are found elsewhere in this document (in perlfaq9 : &#8220;How do I decode or create those %-encodings on the web&#8221; and perlfaq4 : &#8220;How do I determine whether a scalar is a number/whole/integer/float&#8221;, to be precise).</p>
<dl>
<dt>&bull;</p>
<dd> How can I hope to use regular expressions without creating illegible and unmaintainable code?</p>
<dt>&bull;</p>
<dd> I&#8217;m having trouble matching over more than one line. What&#8217;s wrong?</p>
<dt>&bull;</p>
<dd> How can I pull out lines between two patterns that are themselves on different lines?</p>
<dt>&bull;</p>
<dd> How do I match <font SIZE="-1">XML, HTML,</font> or other nasty, ugly things with a regex?</p>
<dt>&bull;</p>
<dd> I put a regular expression into $/ but it didn&#8217;t work. What&#8217;s wrong?</p>
<dt>&bull;</p>
<dd> How do I substitute case-insensitively on the <font SIZE="-1">LHS</font> while preserving case on the <font SIZE="-1">RHS</font>?</p>
<dt>&bull;</p>
<dd> How can I make <tt>&quot;\w&quot;</tt> match national character sets?</p>
<dt>&bull;</p>
<dd> How can I match a locale-smart version of <tt>&quot;/[a-zA-Z]/&quot;</tt> ?</p>
<dt>&bull;</p>
<dd> How can I quote a variable to use in a regex?</p>
<dt>&bull;</p>
<dd> What is <tt>&quot;/o&quot;</tt> really for?</p>
<dt>&bull;</p>
<dd> How do I use a regular expression to strip C-style comments from a file?</p>
<dt>&bull;</p>
<dd> Can I use Perl regular expressions to match balanced text?</p>
<dt>&bull;</p>
<dd> What does it mean that regexes are greedy? How can I get around it?</p>
<dt>&bull;</p>
<dd> How do I process each word on each line?</p>
<dt>&bull;</p>
<dd> How can I print out a word-frequency or line-frequency summary?</p>
<dt>&bull;</p>
<dd> How can I do approximate matching?</p>
<dt>&bull;</p>
<dd> How do I efficiently match many regular expressions at once?</p>
<dt>&bull;</p>
<dd> Why don&#8217;t word-boundary searches with <tt>&quot;&quot;</tt> work for me?</p>
<dt>&bull;</p>
<dd> Why does using $&amp;, $`, or $&#8217; slow my program down?</p>
<dt>&bull;</p>
<dd> What good is <tt>&quot;\G&quot;</tt> in a regular expression?</p>
<dt>&bull;</p>
<dd> Are Perl regexes DFAs or NFAs? Are they <font SIZE="-1">POSIX</font> compliant?</p>
<dt>&bull;</p>
<dd> What&#8217;s wrong with using grep in a void context?</p>
<dt>&bull;</p>
<dd> How can I match strings with multibyte characters?</p>
<dt>&bull;</p>
<dd> How do I match a regular expression that&#8217;s in a variable?</dl>
<h3>perlfaq7: General Perl Language Issues</h3>
<p> This section deals with general Perl language issues that don&#8217;t clearly fit into any of the other sections.</p>
<dl>
<dt>&bull;</p>
<dd> Can I get a BNF/yacc/RE for the Perl language?</p>
<dt>&bull;</p>
<dd> What are all these $@%&amp;* punctuation signs, and how do I know when to use them?</p>
<dt>&bull;</p>
<dd> Do I always/never have to quote my strings or use semicolons and commas?</p>
<dt>&bull;</p>
<dd> How do I skip some return values?</p>
<dt>&bull;</p>
<dd> How do I temporarily block warnings?</p>
<dt>&bull;</p>
<dd> What&#8217;s an extension?</p>
<dt>&bull;</p>
<dd> Why do Perl operators have different precedence than C operators?</p>
<dt>&bull;</p>
<dd> How do I declare/create a structure?</p>
<dt>&bull;</p>
<dd> How do I create a module?</p>
<dt>&bull;</p>
<dd> How do I adopt or take over a module already on <font SIZE="-1">CPAN</font>?</p>
<dt>&bull;</p>
<dd> How do I create a class?</p>
<dt>&bull;</p>
<dd> How can I tell if a variable is tainted?</p>
<dt>&bull;</p>
<dd> What&#8217;s a closure?</p>
<dt>&bull;</p>
<dd> What is variable suicide and how can I prevent it?</p>
<dt>&bull;</p>
<dd> How can I pass/return a {Function, FileHandle, Array, Hash, Method, Regex}?</p>
<dt>&bull;</p>
<dd> How do I create a static variable?</p>
<dt>&bull;</p>
<dd> What&#8217;s the difference between dynamic and lexical (static) scoping? Between <code>local()</code> and <code>my()</code>?</p>
<dt>&bull;</p>
<dd> How can I access a dynamic variable while a similarly named lexical is in scope?</p>
<dt>&bull;</p>
<dd> What&#8217;s the difference between deep and shallow binding?</p>
<dt>&bull;</p>
<dd> Why doesn&#8217;t &#8220;my($foo) = &lt;$fh&gt;;&#8221; work right?</p>
<dt>&bull;</p>
<dd> How do I redefine a builtin function, operator, or method?</p>
<dt>&bull;</p>
<dd> What&#8217;s the difference between calling a function as &amp;foo and <code>foo()</code>?</p>
<dt>&bull;</p>
<dd> How do I create a switch or case statement?</p>
<dt>&bull;</p>
<dd> How can I catch accesses to undefined variables, functions, or methods?</p>
<dt>&bull;</p>
<dd> Why can&#8217;t a method included in this same file be found?</p>
<dt>&bull;</p>
<dd> How can I find out my current or calling package?</p>
<dt>&bull;</p>
<dd> How can I comment out a large block of Perl code?</p>
<dt>&bull;</p>
<dd> How do I clear a package?</p>
<dt>&bull;</p>
<dd> How can I use a variable as a variable name?</p>
<dt>&bull;</p>
<dd> What does &#8220;bad interpreter&#8221; mean?</p>
<dt>&bull;</p>
<dd> Do I need to recompile <font SIZE="-1">XS</font> modules when there is a change in the C library?</dl>
<h3>perlfaq8: System Interaction</h3>
<p> This section of the Perl <font SIZE="-1">FAQ</font> covers questions involving operating system interaction. Topics include interprocess communication (<font SIZE="-1">IPC</font>), control over the user-interface (keyboard, screen and pointing devices), and most anything else not related to data manipulation.</p>
<dl>
<dt>&bull;</p>
<dd> How do I find out which operating system I&#8217;m running under?</p>
<dt>&bull;</p>
<dd> How come <code>exec()</code> doesn&#8217;t return?</p>
<dt>&bull;</p>
<dd> How do I do fancy stuff with the keyboard/screen/mouse?</p>
<dt>&bull;</p>
<dd> How do I print something out in color?</p>
<dt>&bull;</p>
<dd> How do I read just one key without waiting for a return key?</p>
<dt>&bull;</p>
<dd> How do I check whether input is ready on the keyboard?</p>
<dt>&bull;</p>
<dd> How do I clear the screen?</p>
<dt>&bull;</p>
<dd> How do I get the screen size?</p>
<dt>&bull;</p>
<dd> How do I ask the user for a password?</p>
<dt>&bull;</p>
<dd> How do I read and write the serial port?</p>
<dt>&bull;</p>
<dd> How do I decode encrypted password files?</p>
<dt>&bull;</p>
<dd> How do I start a process in the background?</p>
<dt>&bull;</p>
<dd> How do I trap control characters/signals?</p>
<dt>&bull;</p>
<dd> How do I modify the shadow password file on a Unix system?</p>
<dt>&bull;</p>
<dd> How do I set the time and date?</p>
<dt>&bull;</p>
<dd> How can I <code>sleep()</code> or <code>alarm()</code> for under a second?</p>
<dt>&bull;</p>
<dd> How can I measure time under a second?</p>
<dt>&bull;</p>
<dd> How can I do an <code>atexit()</code> or <code>setjmp()</code>/<code>longjmp()</code>? (Exception handling)</p>
<dt>&bull;</p>
<dd> Why doesn&#8217;t my sockets program work under System V (Solaris)? What does the error message &#8220;Protocol not supported&#8221; mean?</p>
<dt>&bull;</p>
<dd> How can I call my system&#8217;s unique C functions from Perl?</p>
<dt>&bull;</p>
<dd> Where do I get the include files to do <code>ioctl()</code> or <code>syscall()</code>?</p>
<dt>&bull;</p>
<dd> Why do setuid perl scripts complain about kernel problems?</p>
<dt>&bull;</p>
<dd> How can I open a pipe both to and from a command?</p>
<dt>&bull;</p>
<dd> Why can&#8217;t I get the output of a command with <code>system()</code>?</p>
<dt>&bull;</p>
<dd> How can I capture <font SIZE="-1">STDERR</font> from an external command?</p>
<dt>&bull;</p>
<dd> Why doesn&#8217;t <code>open()</code> return an error when a pipe open fails?</p>
<dt>&bull;</p>
<dd> What&#8217;s wrong with using backticks in a void context?</p>
<dt>&bull;</p>
<dd> How can I call backticks without shell processing?</p>
<dt>&bull;</p>
<dd> Why can&#8217;t my script read from <font SIZE="-1">STDIN</font> after I gave it <font SIZE="-1">EOF</font> (^D on Unix, ^Z on MS-DOS)?</p>
<dt>&bull;</p>
<dd> How can I convert my shell script to perl?</p>
<dt>&bull;</p>
<dd> Can I use perl to run a telnet or ftp session?</p>
<dt>&bull;</p>
<dd> How can I write expect in Perl?</p>
<dt>&bull;</p>
<dd> Is there a way to hide perl&#8217;s command line from programs such as &#8220;ps&#8221;?</p>
<dt>&bull;</p>
<dd> I {changed directory, modified my environment} in a perl script. How come the change disappeared when I exited the script? How do I get my changes to be visible?</p>
<dt>&bull;</p>
<dd> How do I close a process&#8217;s filehandle without waiting for it to complete?</p>
<dt>&bull;</p>
<dd> How do I fork a daemon process?</p>
<dt>&bull;</p>
<dd> How do I find out if I&#8217;m running interactively or not?</p>
<dt>&bull;</p>
<dd> How do I timeout a slow event?</p>
<dt>&bull;</p>
<dd> How do I set <font SIZE="-1">CPU</font> limits?</p>
<dt>&bull;</p>
<dd> How do I avoid zombies on a Unix system?</p>
<dt>&bull;</p>
<dd> How do I use an <font SIZE="-1">SQL</font> database?</p>
<dt>&bull;</p>
<dd> How do I make a <code>system()</code> exit on control-C?</p>
<dt>&bull;</p>
<dd> How do I open a file without blocking?</p>
<dt>&bull;</p>
<dd> How do I tell the difference between errors from the shell and perl?</p>
<dt>&bull;</p>
<dd> How do I install a module from <font SIZE="-1">CPAN</font>?</p>
<dt>&bull;</p>
<dd> What&#8217;s the difference between require and use?</p>
<dt>&bull;</p>
<dd> How do I keep my own module/library directory?</p>
<dt>&bull;</p>
<dd> How do I add the directory my program lives in to the module/library search path?</p>
<dt>&bull;</p>
<dd> How do I add a directory to my include path (@INC) at runtime?</p>
<dt>&bull;</p>
<dd> Where are modules installed?</p>
<dt>&bull;</p>
<dd> What is socket.ph and where do I get it?</dl>
<h3>perlfaq9: Web, Email and Networking</h3>
<p> This section deals with questions related to running web sites, sending and receiving email as well as general networking.</p>
<dl>
<dt>&bull;</p>
<dd> Should I use a web framework?</p>
<dt>&bull;</p>
<dd> Which web framework should I use?</p>
<dt>&bull;</p>
<dd> What is Plack and <font SIZE="-1">PSGI</font>?</p>
<dt>&bull;</p>
<dd> How do I remove <font SIZE="-1">HTML</font> from a string?</p>
<dt>&bull;</p>
<dd> How do I extract URLs?</p>
<dt>&bull;</p>
<dd> How do I fetch an <font SIZE="-1">HTML</font> file?</p>
<dt>&bull;</p>
<dd> How do I automate an <font SIZE="-1">HTML</font> form submission?</p>
<dt>&bull;</p>
<dd> How do I decode or create those %-encodings on the web?</p>
<dt>&bull;</p>
<dd> How do I redirect to another page?</p>
<dt>&bull;</p>
<dd> How do I put a password on my web pages?</p>
<dt>&bull;</p>
<dd> How do I make sure users can&#8217;t enter values into a form that causes my <font SIZE="-1">CGI</font> script to do bad things?</p>
<dt>&bull;</p>
<dd> How do I parse a mail header?</p>
<dt>&bull;</p>
<dd> How do I check a valid mail address?</p>
<dt>&bull;</p>
<dd> How do I decode a <font SIZE="-1">MIME/BASE64</font> string?</p>
<dt>&bull;</p>
<dd> How do I find the user&#8217;s mail address?</p>
<dt>&bull;</p>
<dd> How do I send email?</p>
<dt>&bull;</p>
<dd> How do I use <font SIZE="-1">MIME</font> to make an attachment to a mail message?</p>
<dt>&bull;</p>
<dd> How do I read email?</p>
<dt>&bull;</p>
<dd> How do I find out my hostname, domainname, or <font SIZE="-1">IP</font> address?</p>
<dt>&bull;</p>
<dd> How do I fetch/put an (S)FTP file?</p>
<dt>&bull;</p>
<dd> How can I do <font SIZE="-1">RPC</font> in Perl?</dl>
<h2>CREDITS</h2>
<p> Tom Christiansen wrote the original perlfaq then expanded it with the help of Nat Torkington. brian d foy substantially edited and expanded the perlfaq. perlfaq-workers and others have also supplied feedback, patches and corrections over the years.</p>
<h2>AUTHOR AND COPYRIGHT</h2>
<p> Tom Christiansen wrote the original version of this document. brian d foy <tt>&quot;&lt;bdfoy [at] cpan.org&gt;&quot;</tt> wrote this version. See the individual perlfaq documents for additional copyright information. </p>
<p> This document is available under the same terms as Perl itself. Code examples in all the perlfaq documents are in the public domain. Use them as you see fit (and at your own risk with no warranty from anyone). </p>
<h2>Index</h2>
<dt><a href="#lbAI">TABLE OF CONTENTS</a></p>
<dd>
<dt><a href="#lbAJ">THE QUESTIONS</a></p>
<dd>
<dt><a href="#lbAT">CREDITS</a></p>
<dd>
<dt><a href="#lbAU">AUTHOR AND COPYRIGHT</a></p>
<dd></dl>

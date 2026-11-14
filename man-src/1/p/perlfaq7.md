---
title: "perlfaq7(1)"
name: "perlfaq7"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlfaq7/"
description: "perlfaq7 – General Perl Language Issues"
---

<h2 class="name">NAME</h2>
<p> perlfaq7 &#8211; General Perl Language Issues </p>
<h2>VERSION</h2>
<p> version 5.20190126</p>
<h2>DESCRIPTION</h2>
<p> This section deals with general Perl language issues that don&#8217;t clearly fit into any of the other sections.</p>
<h3>Can I get a BNF/yacc/RE for the Perl language?</h3>
<p> There is no <font SIZE="-1">BNF,</font> but you can paw your way through the yacc grammar in perly.y in the source distribution if you&#8217;re particularly brave. The grammar relies on very smart tokenizing code, so be prepared to venture into toke.c as well. </p>
<p> In the words of Chaim Frenkel: &#8220;Perl&#8217;s grammar can not be reduced to <font SIZE="-1">BNF.</font> The work of parsing perl is distributed between yacc, the lexer, smoke and mirrors.&#8221;</p>
<h3>What are all these $@%&amp;* punctuation signs, and how do I know when to use them?</h3>
<p> They are type specifiers, as detailed in perldata: </p>
<pre><code>
    $ for scalar values (number, string or reference)
    @ for arrays
    % for hashes (associative arrays)
    &amp; for subroutines (aka functions, procedures, methods)
    * for all types of that symbol name. In version 4 you used them like
      pointers, but in modern perls you can just use references.
</code></pre>
<p> There are a couple of other symbols that you&#8217;re likely to encounter that aren&#8217;t really type specifiers: </p>
<pre>
    &lt;&gt; are used for inputting a record from a filehandle.
    \  takes a reference to something.
</pre>
<p> Note that &lt;<font SIZE="-1">FILE</font>&gt; is <i>neither</i> the type specifier for files nor the name of the handle. It is the <tt>&quot;&lt;&gt;&quot;</tt> operator applied to the handle <font SIZE="-1">FILE.</font> It reads one line (well, record&#8212;see &#8220;$/&#8221; in perlvar) from the handle <font SIZE="-1">FILE</font> in scalar context, or <i>all</i> lines in list context. When performing open, close, or any other operation besides <tt>&quot;&lt;&gt;&quot;</tt> on files, or even when talking about the handle, do <i>not</i> use the brackets. These are correct: <tt>&quot;eof(FH)&quot;</tt>, <tt>&quot;seek(FH, 0, 2)&quot;</tt> and &#8220;copying from <font SIZE="-1">STDIN</font> to <font SIZE="-1">FILE&#8221;.</font></p>
<h3>Do I always/never have to quote my strings or use semicolons and commas?</h3>
<p> Normally, a bareword doesn&#8217;t need to be quoted, but in most cases probably should be (and must be under <tt>&quot;use strict&quot;</tt>). But a hash key consisting of a simple word and the left-hand operand to the <tt>&quot;=&gt;&quot;</tt> operator both count as though they were quoted: </p>
<p>This is like this &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -$foo{line} $foo{&#8216;line&#8217;} bar = &gt; stuff &#8216;bar&#8217; = &gt; stuff</p>
<p> The final semicolon in a block is optional, as is the final comma in a list. Good style (see perlstyle) says to put them in except for one-liners: </p>
<p>if ($whoops) {<br />
    exit 1<br />
}<br />
my @nums = (1, 2, 3);<br />
if ($whoops) {<br />
    exit 1;<br />
}<br />
my @lines = (&#8220;There Beren came from mountains cold&#8221;,<br />
             &#8220;And lost he wandered under leaves&#8221;, );</p>
<h3>How do I skip some return values?</h3>
<p> One way is to treat the return values as a list and index into it: </p>
<pre>
    $dir = (getpwnam($user))[7];
</pre>
<p> Another way is to use undef as an element on the left-hand-side: </p>
<pre>
    ($dev, $ino, undef, undef, $uid, $gid) = stat($file);
</pre>
<p> You can also use a list slice to select only the elements that you need: </p>
<pre>
    ($dev, $ino, $uid, $gid) = ( stat($file) )[0,1,4,5];
</pre>
<h3>How do I temporarily block warnings?</h3>
<p> If you are running Perl 5.6.0 or better, the <tt>&quot;use warnings&quot;</tt> pragma allows fine control of what warnings are produced. See perllexwarn for more details. </p>
<p>{<br />
    no warnings;<br />
#temporarily turn off warnings<br />
        $x = $y + $z;<br />
#I know these might be undef<br />
}</p>
<p> Additionally, you can enable and disable categories of warnings. You turn off the categories you want to ignore and you can still get other categories of warnings. See perllexwarn for the complete details, including the category names and hierarchy. </p>
<p>{<br />
    no warnings &#8216;uninitialized&#8217;;<br />
    $x = $y + $z;<br />
}</p>
<p> If you have an older version of Perl, the <tt>$^W</tt> variable (documented in perlvar) controls runtime warnings for a block: </p>
<p>{<br />
    local $ ^ W = 0;<br />
#temporarily turn off warnings<br />
        $x = $y + $z;<br />
#I know these might be undef<br />
}</p>
<p> Note that like all the punctuation variables, you cannot currently use <code>my()</code> on <tt>$^W</tt>, only <code>local()</code>.</p>
<h3>What&#8217;s an extension?</h3>
<p> An extension is a way of calling compiled C code from Perl. Reading perlxstut is a good place to learn more about extensions.</p>
<h3>Why do Perl operators have different precedence than C operators?</h3>
<p> Actually, they don&#8217;t. All C operators that Perl copies have the same precedence in Perl as they do in C. The problem is with operators that C doesn&#8217;t have, especially functions that give a list context to everything on their right, eg. print, chmod, exec, and so on. Such functions are called &#8220;list operators&#8221; and appear as such in the precedence table in perlop. </p>
<p> A common mistake is to write: </p>
<pre>
    unlink $file || die &quot;snafu&quot;;
</pre>
<p> This gets interpreted as: </p>
<pre>
    unlink ($file || die &quot;snafu&quot;);
</pre>
<p> To avoid this problem, either put in extra parentheses or use the super low precedence <tt>&quot;or&quot;</tt> operator: </p>
<pre>
    (unlink $file) || die &quot;snafu&quot;;
    unlink $file or die &quot;snafu&quot;;
</pre>
<p> The &#8220;English&#8221; operators (<tt>&quot;and&quot;</tt>, <tt>&quot;or&quot;</tt>, <tt>&quot;xor&quot;</tt>, and <tt>&quot;not&quot;</tt>) deliberately have precedence lower than that of list operators for just such situations as the one above. </p>
<p> Another operator with surprising precedence is exponentiation. It binds more tightly even than unary minus, making <tt>&quot;-2**2&quot;</tt> produce a negative four and not a positive one. It is also right-associating, meaning that <tt>&quot;2**3**2&quot;</tt> is two raised to the ninth power, not eight squared. </p>
<p> Although it has the same precedence as in C, Perl&#8217;s <tt>&quot;?:&quot;</tt> operator produces an lvalue. This assigns <tt>$x</tt> to either <tt>$if_true</tt> or <tt>$if_false</tt>, depending on the trueness of <tt>$maybe:</tt> </p>
<pre>
    ($maybe ? $if_true : $if_false) = $x;
</pre>
<h3>How do I declare/create a structure?</h3>
<p> In general, you don&#8217;t &#8220;declare&#8221; a structure. Just use a (probably anonymous) hash reference. See perlref and perldsc for details. Here&#8217;s an example: </p>
<p>$person = {};<br />
#new anonymous hash<br />
    $person-&gt;{AGE } = 24;<br />
#set field AGE to 24 $person-&gt;{NAME } = &#8220;Nat&#8221;;<br />
#set field NAME to &#8220;Nat&#8221;</p>
<p> If you&#8217;re looking for something a bit more rigorous, try perlootut.</p>
<h3>How do I create a module?</h3>
<p> perlnewmod is a good place to start, ignore the bits about uploading to <font SIZE="-1">CPAN</font> if you don&#8217;t want to make your module publicly available. </p>
<p> ExtUtils::ModuleMaker and Module::Starter are also good places to start. Many <font SIZE="-1">CPAN</font> authors now use Dist::Zilla to automate as much as possible. </p>
<p> Detailed documentation about modules can be found at: perlmod, perlmodlib, perlmodstyle. </p>
<p> If you need to include C code or C library interfaces use h2xs. h2xs will create the module distribution structure and the initial interface files. perlxs and perlxstut explain the details.</p>
<h3>How do I adopt or take over a module already on <font SIZE="-1">CPAN</font>?</h3>
<p> Ask the current maintainer to make you a co-maintainer or transfer the module to you. </p>
<p> If you can not reach the author for some reason contact the <font SIZE="-1">PAUSE</font> admins at modules [at] perl.org who may be able to help, but each case is treated separately.</p>
<dl>
<dt>&bull;</p>
<dd> Get a login for the Perl Authors Upload Server (<font SIZE="-1">PAUSE</font>) if you don&#8217;t already have one: &lt;<a rel="nofollow" href="http://pause.perl.org">http://pause.perl.org</a>&gt;</p>
<dt>&bull;</p>
<dd> Write to modules [at] perl.org explaining what you did to contact the current maintainer. The <font SIZE="-1">PAUSE</font> admins will also try to reach the maintainer.</p>
<dt>&bull;</p>
<dd> Post a public message in a heavily trafficked site announcing your intention to take over the module.</p>
<dt>&bull;</p>
<dd> Wait a bit. The <font SIZE="-1">PAUSE</font> admins don&#8217;t want to act too quickly in case the current maintainer is on holiday. If there&#8217;s no response to private communication or the public post, a <font SIZE="-1">PAUSE</font> admin can transfer it to you.</dl>
<h3>How do I create a class?</h3>
<p> (contributed by brian d foy) </p>
<p> In Perl, a class is just a package, and methods are just subroutines. Perl doesn&#8217;t get more formal than that and lets you set up the package just the way that you like it (that is, it doesn&#8217;t set up anything for you). </p>
<p> See also perlootut, a tutorial that covers class creation, and perlobj.</p>
<h3>How can I tell if a variable is tainted?</h3>
<p> You can use the <code>tainted()</code> function of the Scalar::Util module, available from <font SIZE="-1">CPAN</font> (or included with Perl since release 5.8.0). See also &#8220;Laundering and Detecting Tainted Data&#8221; in perlsec.</p>
<h3>What&#8217;s a closure?</h3>
<p> Closures are documented in perlref. </p>
<p> <i>Closure</i> is a computer science term with a precise but hard-to-explain meaning. Usually, closures are implemented in Perl as anonymous subroutines with lasting references to lexical variables outside their own scopes. These lexicals magically refer to the variables that were around when the subroutine was defined (deep binding). </p>
<p> Closures are most often used in programming languages where you can have the return value of a function be itself a function, as you can in Perl. Note that some languages provide anonymous functions but are not capable of providing proper closures: the Python language, for example. For more information on closures, check out any textbook on functional programming. Scheme is a language that not only supports but encourages closures. </p>
<p> Here&#8217;s a classic non-closure function-generating function: </p>
<p>sub add_function_generator<br />
{<br />
    return sub{shift() + shift()};<br />
}<br />
my $add_sub = add_function_generator();<br />
my $sum = $add_sub-&gt;(4, 5);<br />
#$sum is 9 now.</p>
<p> The anonymous subroutine returned by <code>add_function_generator()</code> isn&#8217;t technically a closure because it refers to no lexicals outside its own scope. Using a closure gives you a <i>function template</i> with some customization slots left out to be filled later. </p>
<p> Contrast this with the following <code>make_adder()</code> function, in which the returned anonymous function contains a reference to a lexical variable outside the scope of that function itself. Such a reference requires that Perl return a proper closure, thus locking in for all time the value that the lexical had when the function was created. </p>
<p>sub make_adder<br />
{<br />
    my $addpiece = shift;<br />
    return sub{shift() + $addpiece};<br />
}<br />
my $f1 = make_adder(20);<br />
my $f2 = make_adder(555);</p>
<p> Now <tt>&quot;$f1-&gt;($n)&quot;</tt> is always 20 plus whatever <tt>$n</tt> you pass in, whereas <tt>&quot;$f2-&gt;($n)&quot;</tt> is always 555 plus whatever <tt>$n</tt> you pass in. The <tt>$addpiece</tt> in the closure sticks around. </p>
<p> Closures are often used for less esoteric purposes. For example, when you want to pass in a bit of code into a function: </p>
<p>my $line;<br />
timeout(30, sub{$line = &lt;STDIN&gt;});</p>
<p> If the code to execute had been passed in as a string, <tt>'$line = &lt;STDIN&gt;'</tt>, there would have been no way for the hypothetical <code>timeout()</code> function to access the lexical variable <tt>$line</tt> back in its caller&#8217;s scope. </p>
<p> Another use for a closure is to make a variable <i>private</i> to a named subroutine, e.g. a counter that gets initialized at creation time of the sub and can only be modified from within the sub. This is sometimes used with a <font SIZE="-1">BEGIN</font> block in package files to make sure a variable doesn&#8217;t get meddled with during the lifetime of the package: </p>
<p>BEGIN<br />
{<br />
    my $id = 0;<br />
    sub next_id<br />
    {<br />
        ++$id<br />
    }<br />
}</p>
<p> This is discussed in more detail in perlsub; see the entry on <i>Persistent Private Variables</i>.</p>
<h3>What is variable suicide and how can I prevent it?</h3>
<p> This problem was fixed in perl 5.004_05, so preventing it means upgrading your version of perl. ;) </p>
<p> Variable suicide is when you (temporarily or permanently) lose the value of a variable. It is caused by scoping through <code>my()</code> and <code>local()</code> interacting with either closures or aliased <code>foreach()</code> iterator variables and subroutine arguments. It used to be easy to inadvertently lose a variable&#8217;s value this way, but now it&#8217;s much harder. Take this code: </p>
<p>my $f = &#8216;foo&#8217;;<br />
sub T<br />
{<br />
    while ($i++ &lt; 3) {<br />
        my $f = $f;<br />
        $f.= &#8220;bar&#8221;;<br />
        print $f, &#8220;
&#8221;<br />
    }<br />
}<br />
T;<br />
print &#8220;Finally $f
&#8221;;</p>
<p> If you are experiencing variable suicide, that <tt>&quot;my $f&quot;</tt> in the subroutine doesn&#8217;t pick up a fresh copy of the <tt>$f</tt> whose value is <tt>'foo'</tt>. The output shows that inside the subroutine the value of <tt>$f</tt> leaks through when it shouldn&#8217;t, as in this output: </p>
<pre>
    foobar
    foobarbar
    foobarbarbar
    Finally foo
</pre>
<p> The <tt>$f</tt> that has &#8220;bar&#8221; added to it three times should be a new <tt>$f</tt> <tt>&quot;my $f&quot;</tt> should create a new lexical variable each time through the loop. The expected output is: </p>
<pre>
    foobar
    foobar
    foobar
    Finally foo
</pre>
<h3>How can I pass/return a {Function, FileHandle, Array, Hash, Method, Regex}?</h3>
<p> You need to pass references to these objects. See &#8220;Pass by Reference&#8221; in perlsub for this particular question, and perlref for information on references.</p>
<dl>
<dt>Passing Variables and Functions</p>
<dd> Regular variables and functions are quite easy to pass: just pass in a reference to an existing or anonymous variable or function: </p>
<p>func( \$some_scalar);<br />
func( \@some_array);<br />
func([1..10]);<br />
func( \% some_hash);<br />
func({this = &gt; 10, that = &gt; 20});<br />
func( \&amp;some_func);<br />
func(sub{$_[0] * *$_[1]});</p>
<dt>Passing Filehandles</p>
<dd> As of Perl 5.6, you can represent filehandles with scalar variables which you treat as any other scalar. </p>
<p>open my $fh, $filename or die &#8220;Cannot open $filename! $!&#8221;;<br />
func($fh);<br />
sub func<br />
{<br />
    my $passed_fh = shift;<br />
    my $line = &lt;$passed_fh&gt;;<br />
}</p>
<p> Before Perl 5.6, you had to use the <tt>*FH</tt> or <tt>&quot;\*FH&quot;</tt> notations. These are &#8220;typeglobs&#8221;&#8211;see &#8220;Typeglobs and Filehandles&#8221; in perldata and especially &#8220;Pass by Reference&#8221; in perlsub for more information.</p>
<dt>Passing Regexes</p>
<dd> Here&#8217;s an example of how to pass in a string and a regular expression for it to match against. You construct the pattern with the <tt>&quot;qr//&quot;</tt> operator: </p>
<p>sub compare<br />
{<br />
    my($val1, $regex) = @_;<br />
    my $retval = $val1 = ~ / $regex / ;<br />
    return $retval;<br />
}<br />
$match = compare(&#8220;old McDonald&#8221;, qr / d.*D / i);</p>
<dt>Passing Methods</p>
<dd> To pass an object method into a subroutine, you can do this: </p>
<p>call_a_lot(10, $some_obj, &#8220;methname&#8221;)<br />
    sub call_a_lot<br />
{<br />
    my($count, $widget, $trick) = @_;<br />
    for (my $i = 0; $i &lt; $count; $i++) {<br />
        $widget-&gt;$trick();<br />
    }<br />
}</p>
<p> Or, you can use a closure to bundle up the object, its method call, and arguments: </p>
<p>my $whatnot = sub<br />
{<br />
    $some_obj-&gt;obfuscate(@args)<br />
};<br />
func($whatnot);<br />
sub func<br />
{<br />
    my $code = shift;<br />
    &amp;$code();<br />
}</p>
<p> You could also investigate the <code>can()</code> method in the <font SIZE="-1">UNIVERSAL</font> class (part of the standard perl distribution).</dl>
<h3>How do I create a static variable?</h3>
<p> (contributed by brian d foy) </p>
<p> In Perl 5.10, declare the variable with <tt>&quot;state&quot;</tt>. The <tt>&quot;state&quot;</tt> declaration creates the lexical variable that persists between calls to the subroutine: </p>
<p>sub counter<br />
{<br />
    state $count = 1;<br />
    $count++<br />
}</p>
<p> You can fake a static variable by using a lexical variable which goes out of scope. In this example, you define the subroutine <tt>&quot;counter&quot;</tt>, and it uses the lexical variable <tt>$count</tt>. Since you wrap this in a <font SIZE="-1">BEGIN</font> block, <tt>$count</tt> is defined at compile-time, but also goes out of scope at the end of the <font SIZE="-1">BEGIN</font> block. The <font SIZE="-1">BEGIN</font> block also ensures that the subroutine and the value it uses is defined at compile-time so the subroutine is ready to use just like any other subroutine, and you can put this code in the same place as other subroutines in the program text (i.e. at the end of the code, typically). The subroutine <tt>&quot;counter&quot;</tt> still has a reference to the data, and is the only way you can access the value (and each time you do, you increment the value). The data in chunk of memory defined by <tt>$count</tt> is private to <tt>&quot;counter&quot;</tt>. </p>
<p>BEGIN<br />
{<br />
    my $count = 1;<br />
    sub counter<br />
    {<br />
        $count++<br />
    }<br />
}<br />
my $start = counter();<br />
&#8230;.#code that calls counter();<br />
my $end = counter();</p>
<p> In the previous example, you created a function-private variable because only one function remembered its reference. You could define multiple functions while the variable is in scope, and each function can share the &#8220;private&#8221; variable. It&#8217;s not really &#8220;static&#8221; because you can access it outside the function while the lexical variable is in scope, and even create references to it. In this example, <tt>&quot;increment_count&quot;</tt> and <tt>&quot;return_count&quot;</tt> share the variable. One function adds to the value and the other simply returns the value. They can both access <tt>$count</tt>, and since it has gone out of scope, there is no other way to access it. </p>
<p>BEGIN<br />
{<br />
    my $count = 1;<br />
    sub increment_count{$count++} sub return_count<br />
    {<br />
        $count<br />
    }<br />
}</p>
<p> To declare a file-private variable, you still use a lexical variable. A file is also a scope, so a lexical variable defined in the file cannot be seen from any other file. </p>
<p> See &#8220;Persistent Private Variables&#8221; in perlsub for more information. The discussion of closures in perlref may help you even though we did not use anonymous subroutines in this answer. See &#8220;Persistent Private Variables&#8221; in perlsub for details.</p>
<h3>What&#8217;s the difference between dynamic and lexical (static) scoping? Between <code>local()</code> and <code>my()</code>?</h3>
<p> <tt>&quot;local($x)&quot;</tt> saves away the old value of the global variable <tt>$x</tt> and assigns a new value for the duration of the subroutine <i>which is visible in other functions called from that subroutine</i>. This is done at run-time, so is called dynamic scoping. <code>local()</code> always affects global variables, also called package variables or dynamic variables. </p>
<p> <tt>&quot;my($x)&quot;</tt> creates a new variable that is only visible in the current subroutine. This is done at compile-time, so it is called lexical or static scoping. <code>my()</code> always affects private variables, also called lexical variables or (improperly) static(ly scoped) variables. </p>
<p> For instance: </p>
<p>sub visible<br />
{<br />
    print &#8220;var has value $var
&#8221;;<br />
}<br />
sub dynamic<br />
{<br />
    local $var = &#8216;local&#8217;;<br />
#new temporary value for the still &#8211; global<br />
                                         visible();<br />
#variable called $var<br />
}<br />
sub lexical<br />
{<br />
    my $var = &#8216;private&#8217;;<br />
#new private variable, $var<br />
                           visible();<br />
#(invisible outside of sub scope)<br />
}<br />
$var = &#8216;global&#8217;;<br />
visible();<br />
#prints global<br />
dynamic();<br />
#prints local<br />
lexical();<br />
#prints global</p>
<p> Notice how at no point does the value &#8220;private&#8221; get printed. That&#8217;s because <tt>$var</tt> only has that value within the block of the <code>lexical()</code> function, and it is hidden from the called subroutine. </p>
<p> In summary, <code>local()</code> doesn&#8217;t make what you think of as private, local variables. It gives a global variable a temporary value. <code>my()</code> is what you&#8217;re looking for if you want private variables. </p>
<p> See &#8220;Private Variables via <code>my()</code>&#8221; in perlsub and &#8220;Temporary Values via <code>local()</code>&#8221; in perlsub for excruciating details.</p>
<h3>How can I access a dynamic variable while a similarly named lexical is in scope?</h3>
<p> If you know your package, you can just mention it explicitly, as in <tt>$Some_Pack::var</tt>. Note that the notation <tt>$::var</tt> is <code>not</code> the dynamic <tt>$var</tt> in the current package, but rather the one in the &#8220;main&#8221; package, as though you had written <tt>$main::var</tt>. </p>
<p>use vars &#8216;$var&#8217;;<br />
local $var = &#8220;global&#8221;;<br />
my $var = &#8220;lexical&#8221;;<br />
print &#8220;lexical is $var
&#8221;;<br />
print &#8220;global  is $main::var
&#8221;;</p>
<p> Alternatively you can use the compiler directive <code>our()</code> to bring a dynamic variable into the current lexical scope. </p>
<p>require 5.006;<br />
#our() did not exist before 5.6 use vars &#8216;$var&#8217;;<br />
local $var = &#8220;global&#8221;;<br />
my $var = &#8220;lexical&#8221;;<br />
print &#8220;lexical is $var
&#8221;;<br />
{<br />
    our $var;<br />
    print &#8220;global  is $var
&#8221;;<br />
}</p>
<h3>What&#8217;s the difference between deep and shallow binding?</h3>
<p> In deep binding, lexical variables mentioned in anonymous subroutines are the same ones that were in scope when the subroutine was created. In shallow binding, they are whichever variables with the same names happen to be in scope when the subroutine is called. Perl always uses deep binding of lexical variables (i.e., those created with <code>my()</code>). However, dynamic variables (aka global, local, or package variables) are effectively shallowly bound. Consider this just one more reason not to use them. See the answer to &#8220;What&#8217;s a closure?&#8221;.</p>
<h3>Why doesn&#8217;t my($foo) = &lt;$fh&gt;; work right?</h3>
<p> <tt>&quot;my()&quot;</tt> and <tt>&quot;local()&quot;</tt> give list context to the right hand side of <tt>&quot;=&quot;</tt>. The &lt;$fh&gt; read operation, like so many of Perl&#8217;s functions and operators, can tell which context it was called in and behaves appropriately. In general, the <code>scalar()</code> function can help. This function does nothing to the data itself (contrary to popular myth) but rather tells its argument to behave in whatever its scalar fashion is. If that function doesn&#8217;t have a defined scalar behavior, this of course doesn&#8217;t help you (such as with <code>sort()</code>). </p>
<p> To enforce scalar context in this particular case, however, you need merely omit the parentheses: </p>
<p>local($foo) = &lt;$fh&gt;;<br />
#WRONG local($foo) = scalar(&lt;$fh&gt;);<br />
#ok local $foo = &lt; $fh&gt;;<br />
#right</p>
<p> You should probably be using lexical variables anyway, although the issue is the same here: </p>
<pre>
    my($foo) = &lt;$fh&gt;;    # WRONG
    my $foo  = &lt;$fh&gt;;    # right
</pre>
<h3>How do I redefine a builtin function, operator, or method?</h3>
<p> Why do you want to do that? :-) </p>
<p> If you want to override a predefined function, such as <code>open()</code>, then you&#8217;ll have to import the new definition from a different module. See &#8220;Overriding Built-in Functions&#8221; in perlsub. </p>
<p> If you want to overload a Perl operator, such as <tt>&quot;+&quot;</tt> or <tt>&quot;**&quot;</tt>, then you&#8217;ll want to use the <tt>&quot;use overload&quot;</tt> pragma, documented in overload. </p>
<p> If you&#8217;re talking about obscuring method calls in parent classes, see &#8220;Overriding methods and method resolution&#8221; in perlootut.</p>
<h3>What&#8217;s the difference between calling a function as &amp;foo and <code>foo()</code>?</h3>
<p> (contributed by brian d foy) </p>
<p> Calling a subroutine as <tt>&amp;foo</tt> with no trailing parentheses ignores the prototype of <tt>&quot;foo&quot;</tt> and passes it the current value of the argument list, <tt>@_</tt>. Here&#8217;s an example; the <tt>&quot;bar&quot;</tt> subroutine calls <tt>&amp;foo</tt>, which prints its arguments list: </p>
<p>sub foo<br />
{<br />
    print &#8220;Args in foo are: @_
&#8221;;<br />
}<br />
sub bar<br />
{<br />
    &amp;foo;<br />
}<br />
bar(&#8220;a&#8221;, &#8220;b&#8221;, &#8220;c&#8221;);</p>
<p> When you call <tt>&quot;bar&quot;</tt> with arguments, you see that <tt>&quot;foo&quot;</tt> got the same <tt>@_</tt>: </p>
<pre>
    Args in foo are: a b c
</pre>
<p> Calling the subroutine with trailing parentheses, with or without arguments, does not use the current <tt>@_</tt>. Changing the example to put parentheses after the call to <tt>&quot;foo&quot;</tt> changes the program: </p>
<p>sub foo<br />
{<br />
    print &#8220;Args in foo are: @_
&#8221;;<br />
}<br />
sub bar<br />
{<br />
    &amp;foo();<br />
}<br />
bar(&#8220;a&#8221;, &#8220;b&#8221;, &#8220;c&#8221;);</p>
<p> Now the output shows that <tt>&quot;foo&quot;</tt> doesn&#8217;t get the <tt>@_</tt> from its caller. </p>
<pre>
    Args in foo are:
</pre>
<p> However, using <tt>&quot;&amp;&quot;</tt> in the call still overrides the prototype of <tt>&quot;foo&quot;</tt> if present: </p>
<p>sub foo($$$)<br />
{<br />
    print &#8220;Args infoo are: @_
&#8221;;<br />
}<br />
sub bar_1<br />
{<br />
    &amp;foo;<br />
}<br />
sub bar_2<br />
{<br />
    &amp;foo();<br />
}<br />
sub bar_3<br />
{<br />
    foo($_[0], $_[1], $_[2]);<br />
}<br />
#sub bar_4{foo(); }<br />
#bar_4 doesn&#8217;t compile: &#8220;Not enough arguments for main::foo at &#8230;&#8221;<br />
bar_1(&#8220;a&#8221;, &#8220;b&#8221;, &#8220;c&#8221;);<br />
#Args in foo are : a b c<br />
bar_2(&#8220;a&#8221;, &#8220;b&#8221;, &#8220;c&#8221;);<br />
#Args in foo are:<br />
bar_3(&#8220;a&#8221;, &#8220;b&#8221;, &#8220;c&#8221;);<br />
#Args in foo are : a b c</p>
<p> The main use of the <tt>@_</tt> pass-through feature is to write subroutines whose main job it is to call other subroutines for you. For further details, see perlsub.</p>
<h3>How do I create a switch or case statement?</h3>
<p> There is a given/when statement in Perl, but it is experimental and likely to change in future. See perlsyn for more details. </p>
<p> The general answer is to use a <font SIZE="-1">CPAN</font> module such as Switch::Plain: </p>
<p>use Switch::Plain;<br />
sswitch($variable_holding_a_string)<br />
{<br />
case &#8216;first&#8217;: {<br />
}<br />
case &#8216;second&#8217;: {<br />
}<br />
default: {<br />
}<br />
}</p>
<p> or for more complicated comparisons, <tt>&quot;if-elsif-else&quot;</tt>: </p>
<p>for ($variable_to_test) {<br />
    if (/ pat1 /) {<br />
    }<br />
#do something<br />
        elsif(/ pat2 /)<br />
    {<br />
    }<br />
#do something else elsif(/ pat3 /)<br />
    {<br />
    }<br />
#do something else else<br />
    {<br />
    }<br />
#default<br />
}</p>
<p> Here&#8217;s a simple example of a switch based on pattern matching, lined up in a way to make it look more like a switch statement. We&#8217;ll do a multiway conditional based on the type of reference stored in <tt>$whatchamacallit:</tt> </p>
<p>SWITCH : for (ref $whatchamacallit)<br />
{<br />
    / ^$ / &amp;&amp;die &#8220;not a reference&#8221;;<br />
    / SCALAR / &amp;&amp;do<br />
    {<br />
        print_scalar($$ref);<br />
        last SWITCH;<br />
    };<br />
    / ARRAY / &amp;&amp;do<br />
    {<br />
        print_array(@$ref);<br />
        last SWITCH;<br />
    };<br />
    / HASH / &amp;&amp;do<br />
    {<br />
        print_hash(% $ref);<br />
        last SWITCH;<br />
    };<br />
    / CODE / &amp;&amp;do<br />
    {<br />
        warn &#8220;can&#8217;t print function ref&#8221;;<br />
        last SWITCH;<br />
    };<br />
#DEFAULT<br />
    warn &#8220;User defined type skipped&#8221;;<br />
}</p>
<p> See perlsyn for other examples in this style. </p>
<p> Sometimes you should change the positions of the constant and the variable. For example, let&#8217;s say you wanted to test which of many answers you were given, but in a case-insensitive way that also allows abbreviations. You can use the following technique if the strings all start with different characters or if you want to arrange the matches so that one takes precedence over another, as <tt>&quot;SEND&quot;</tt> has precedence over <tt>&quot;STOP&quot;</tt> here: </p>
<p>chomp($answer = &lt;&gt;);<br />
if (&#8220;SEND&#8221; = ~ / ^\Q$answer / i) {<br />
    print &#8220;Action is send
&#8221;<br />
}<br />
elsif(&#8220;STOP&#8221; = ~ / ^\Q$answer / i){print &#8220;Action is stop
&#8221;} elsif(&#8220;ABORT&#8221; = ~ / ^\Q$answer / i){print &#8220;Action is abort
&#8221;} elsif(&#8220;LIST&#8221; = ~ / ^\Q$answer / i){print &#8220;Action is list
&#8221;} elsif(&#8220;EDIT&#8221; = ~ / ^\Q$answer / i)<br />
{<br />
    print &#8220;Action is edit
&#8221;<br />
}</p>
<p> A totally different approach is to create a hash of function references. </p>
<p>my % commands = (&#8220;happy&#8221; = &gt; \&amp; joy,<br />
                 &#8220;sad&#8221;, = &gt; \&amp; sullen,<br />
                 &#8220;done&#8221; = &gt; sub{die &#8220;See ya!&#8221;},<br />
                 &#8220;mad&#8221; = &gt; \&amp; angry, );<br />
print &#8220;How are you? &#8220;;<br />
chomp($string = &lt;STDIN&gt;);<br />
if ($commands{$string}) {<br />
    $commands<br />
    {<br />
        $string<br />
        } -&gt; ();<br />
} else {<br />
    print &#8220;No such command: $string
&#8221;;<br />
}</p>
<p> Starting from Perl 5.8, a source filter module, <tt>&quot;Switch&quot;</tt>, can also be used to get switch and case. Its use is now discouraged, because it&#8217;s not fully compatible with the native switch of Perl 5.10, and because, as it&#8217;s implemented as a source filter, it doesn&#8217;t always work as intended when complex syntax is involved.</p>
<h3>How can I catch accesses to undefined variables, functions, or methods?</h3>
<p> The <font SIZE="-1">AUTOLOAD</font> method, discussed in &#8220;Autoloading&#8221; in perlsub lets you capture calls to undefined functions and methods. </p>
<p> When it comes to undefined variables that would trigger a warning under <tt>&quot;use warnings&quot;</tt>, you can promote the warning to an error. </p>
<pre>
    use warnings FATAL =&gt; qw(uninitialized);
</pre>
<h3>Why can&#8217;t a method included in this same file be found?</h3>
<p> Some possible reasons: your inheritance is getting confused, you&#8217;ve misspelled the method name, or the object is of the wrong type. Check out perlootut for details about any of the above cases. You may also use <tt>&quot;print ref($object)&quot;</tt> to find out the class <tt>$object</tt> was blessed into. </p>
<p> Another possible reason for problems is that you&#8217;ve used the indirect object syntax (eg, <tt>&quot;find Guru &quot;Samy&quot;&quot;</tt>) on a class name before Perl has seen that such a package exists. It&#8217;s wisest to make sure your packages are all defined before you start using them, which will be taken care of if you use the <tt>&quot;use&quot;</tt> statement instead of <tt>&quot;require&quot;</tt>. If not, make sure to use arrow notation (eg., <tt>&quot;Guru-&gt;find(&quot;Samy&quot;)&quot;</tt>) instead. Object notation is explained in perlobj. </p>
<p> Make sure to read about creating modules in perlmod and the perils of indirect objects in &#8220;Method Invocation&#8221; in perlobj.</p>
<h3>How can I find out my current or calling package?</h3>
<p> (contributed by brian d foy) </p>
<p> To find the package you are currently in, use the special literal <tt>&quot;__PACKAGE__&quot;</tt>, as documented in perldata. You can only use the special literals as separate tokens, so you can&#8217;t interpolate them into strings like you can with variables: </p>
<pre>
    my $current_package = __PACKAGE__;
    print &quot;I am in package $current_package
&quot;;
</pre>
<p> If you want to find the package calling your code, perhaps to give better diagnostics as Carp does, use the <tt>&quot;caller&quot;</tt> built-in: </p>
<p>sub foo<br />
{<br />
    my @args = &#8230;;<br />
    my($package, $filename, $line) = caller;<br />
    print &#8220;I was called from package $package
&#8221;;<br />
        );</p>
<p> By default, your program starts in package <tt>&quot;main&quot;</tt>, so you will always be in some package. </p>
<p> This is different from finding out the package an object is blessed into, which might not be the current package. For that, use <tt>&quot;blessed&quot;</tt> from Scalar::Util, part of the Standard Library since Perl 5.8: </p>
<p>use Scalar::Util qw(blessed);<br />
my $object_package = blessed($object);</p>
<p> Most of the time, you shouldn&#8217;t care what package an object is blessed into, however, as long as it claims to inherit from that class: </p>
<p>my $is_right_class = eval{$object-&gt;isa($package)};<br />
#true or false</p>
<p> And, with Perl 5.10 and later, you don&#8217;t have to check for an inheritance to see if the object can handle a role. For that, you can use <tt>&quot;DOES&quot;</tt>, which comes from <tt>&quot;UNIVERSAL&quot;</tt>: </p>
<p>my $class_does_it = eval{$object-&gt;DOES($role)};<br />
#true or false</p>
<p> You can safely replace <tt>&quot;isa&quot;</tt> with <tt>&quot;DOES&quot;</tt> (although the converse is not true).</p>
<h3>How can I comment out a large block of Perl code?</h3>
<p> (contributed by brian d foy) </p>
<p> The quick-and-dirty way to comment out more than one line of Perl is to surround those lines with Pod directives. You have to put these directives at the beginning of the line and somewhere where Perl expects a new statement (so not in the middle of statements like the <tt>&quot;#&quot;</tt> comments). You end the comment with <tt>&quot;=cut&quot;</tt>, ending the Pod section: </p>
<p>= pod<br />
    my $object = NotGonnaHappen-&gt;new ();<br />
ignored_sub();<br />
$wont_be_assigned = 37;<br />
= cut</p>
<p> The quick-and-dirty method only works well when you don&#8217;t plan to leave the commented code in the source. If a Pod parser comes along, your multiline comment is going to show up in the Pod translation. A better way hides it from Pod parsers as well. </p>
<p> The <tt>&quot;=begin&quot;</tt> directive can mark a section for a particular purpose. If the Pod parser doesn&#8217;t want to handle it, it just ignores it. Label the comments with <tt>&quot;comment&quot;</tt>. End the comment using <tt>&quot;=end&quot;</tt> with the same label. You still need the <tt>&quot;=cut&quot;</tt> to go back to Perl code from the Pod comment: </p>
<p>= begin comment<br />
    my $object = NotGonnaHappen-&gt;new ();<br />
ignored_sub();<br />
$wont_be_assigned = 37;<br />
= end comment = cut</p>
<p> For more information on Pod, check out perlpod and perlpodspec.</p>
<h3>How do I clear a package?</h3>
<p> Use this code, provided by Mark-Jason Dominus: </p>
<p>sub scrub_package<br />
{<br />
    no strict &#8216;refs&#8217;;<br />
    my $pack = shift;<br />
    die &#8220;Shouldn&#8217;t delete main package&#8221; if $pack eq &#8220;&#8221; || $pack eq &#8220;main&#8221;;<br />
    my $stash = *{$pack.&#8217;::&#8217;} {HASH};<br />
    my $name;<br />
    foreach<br />
        $name(keys % $stash)<br />
        {<br />
            my $fullname = $pack.&#8217;::&#8217;.$name;<br />
#Get rid of everything with that name.<br />
            undef $$fullname;<br />
            undef @$fullname;<br />
            undef % $fullname;<br />
            undef &amp;$fullname;<br />
            undef *$fullname;<br />
        }<br />
}</p>
<p> Or, if you&#8217;re using a recent release of Perl, you can just use the <code>Symbol::delete_package()</code> function instead.</p>
<h3>How can I use a variable as a variable name?</h3>
<p> Beginners often think they want to have a variable contain the name of a variable. </p>
<p>$fred = 23;<br />
$varname = &#8220;fred&#8221;;<br />
++$$varname;<br />
#$fred now 24</p>
<p> This works <i>sometimes</i>, but it is a very bad idea for two reasons. </p>
<p> The first reason is that this technique <i>only works on global variables</i>. That means that if <tt>$fred</tt> is a lexical variable created with <code>my()</code> in the above example, the code wouldn&#8217;t work at all: you&#8217;d accidentally access the global and skip right over the private lexical altogether. Global variables are bad because they can easily collide accidentally and in general make for non-scalable and confusing code. </p>
<p> Symbolic references are forbidden under the <tt>&quot;use strict&quot;</tt> pragma. They are not true references and consequently are not reference-counted or garbage-collected. </p>
<p> The other reason why using a variable to hold the name of another variable is a bad idea is that the question often stems from a lack of understanding of Perl data structures, particularly hashes. By using symbolic references, you are just using the package&#8217;s symbol-table hash (like <tt>%main::</tt>) instead of a user-defined hash. The solution is to use your own hash or a real reference instead. </p>
<p>$USER_VARS{&#8220;fred&#8221;} = 23;<br />
my $varname = &#8220;fred&#8221;;<br />
$USER_VARS<br />
{<br />
    $varname<br />
}<br />
++;<br />
#not $$varname++</p>
<p> There we&#8217;re using the <tt>%USER_VARS</tt> hash instead of symbolic references. Sometimes this comes up in reading strings from the user with variable references and wanting to expand them to the values of your perl program&#8217;s variables. This is also a bad idea because it conflates the program-addressable namespace and the user-addressable one. Instead of reading a string and expanding it to the actual contents of your program&#8217;s own variables: </p>
<p>$str = &#8216;this has a $fred and $barney in it&#8217;;<br />
$str = ~s / (\$\w +) / $1 / eeg;<br />
#need double eval</p>
<p> it would be better to keep a hash around like <tt>%USER_VARS</tt> and have variable references actually refer to entries in that hash: </p>
<pre>
    $str =~ s/\$(\w+)/$USER_VARS{$1}/g;   # no /e here at all
</pre>
<p> That&#8217;s faster, cleaner, and safer than the previous approach. Of course, you don&#8217;t need to use a dollar sign. You could use your own scheme to make it less confusing, like bracketed percent symbols, etc. </p>
<pre>
    $str = 'this has a %fred% and %barney% in it';
    $str =~ s/%(\w+)%/$USER_VARS{$1}/g;   # no /e here at all
</pre>
<p> Another reason that folks sometimes think they want a variable to contain the name of a variable is that they don&#8217;t know how to build proper data structures using hashes. For example, let&#8217;s say they wanted two hashes in their program: <tt>%fred</tt> and <tt>%barney</tt>, and that they wanted to use another scalar variable to refer to those by name. </p>
<p>$name = &#8220;fred&#8221;;<br />
$$name{WIFE} = &#8220;wilma&#8221;;<br />
#set % fred<br />
           $name = &#8220;barney&#8221;;<br />
$$name{WIFE} = &#8220;betty&#8221;;<br />
#set % barney</p>
<p> This is still a symbolic reference, and is still saddled with the problems enumerated above. It would be far better to write: </p>
<p>$folks{&#8220;fred&#8221;} {WIFE} = &#8220;wilma&#8221;;<br />
$folks{&#8220;barney&#8221;} {WIFE} = &#8220;betty&#8221;;</p>
<p> And just use a multilevel hash to start with. </p>
<p> The only times that you absolutely <i>must</i> use symbolic references are when you really must refer to the symbol table. This may be because it&#8217;s something that one can&#8217;t take a real reference to, such as a format name. Doing so may also be important for method calls, since these always go through the symbol table for resolution. </p>
<p> In those cases, you would turn off <tt>&quot;strict 'refs'&quot;</tt> temporarily so you can play around with the symbol table. For example: </p>
<pre><code>
@colors = qw(red blue green yellow orange purple violet);
    for
        my $name(@colors)
        {
            no strict 'refs';
#renege for the block
                *$name = sub{"&lt;FONT COLOR='$name'&gt;@_&lt;/FONT&gt;" };
        }
</code></pre>
<p> All those functions (<code>red()</code>, <code>blue()</code>, <code>green()</code>, etc.) appear to be separate, but the real code in the closure actually was compiled only once. </p>
<p> So, sometimes you might want to use symbolic references to manipulate the symbol table directly. This doesn&#8217;t matter for formats, handles, and subroutines, because they are always global&#8212;you can&#8217;t use <code>my()</code> on them. For scalars, arrays, and hashes, though&#8212;and usually for subroutines&#8212; you probably only want to use hard references.</p>
<h3>What does bad interpreter mean?</h3>
<p> (contributed by brian d foy) </p>
<p> The &#8220;bad interpreter&#8221; message comes from the shell, not perl. The actual message may vary depending on your platform, shell, and locale settings. </p>
<p> If you see &#8220;bad interpreter &#8211; no such file or directory&#8221;, the first line in your perl script (the &#8220;shebang&#8221; line) does not contain the right path to perl (or any other program capable of running scripts). Sometimes this happens when you move the script from one machine to another and each machine has a different path to perl&#8211;/usr/bin/perl versus /usr/local/bin/perl for instance. It may also indicate that the source machine has <font SIZE="-1">CRLF</font> line terminators and the destination machine has <font SIZE="-1">LF</font> only: the shell tries to find /usr/bin/perl&lt;<font SIZE="-1">CR</font>&gt;, but can&#8217;t. </p>
<p> If you see &#8220;bad interpreter: Permission denied&#8221;, you need to make your script executable. </p>
<p> In either case, you should still be able to run the scripts with perl explicitly: </p>
<pre>
    % perl script.pl
</pre>
<p> If you get a message like &#8220;perl: command not found&#8221;, perl is not in your <font SIZE="-1">PATH,</font> which might also mean that the location of perl is not where you expect it so you need to adjust your shebang line.</p>
<h3>Do I need to recompile <font SIZE="-1">XS</font> modules when there is a change in the C library?</h3>
<p> (contributed by Alex Beamish) </p>
<p> If the new version of the C library is ABI-compatible (that&#8217;s Application Binary Interface compatible) with the version you&#8217;re upgrading from, and if the shared library version didn&#8217;t change, no re-compilation should be necessary.</p>
<h2>AUTHOR AND COPYRIGHT</h2>
<p> Copyright (c) 1997-2013 Tom Christiansen, Nathan Torkington, and other authors as noted. All rights reserved. </p>
<p> This documentation is free; you can redistribute it and/or modify it under the same terms as Perl itself. </p>
<p> Irrespective of its distribution, all code examples in this file are hereby placed into the public domain. You are permitted and encouraged to use this code in your own programs for fun or for profit as you see fit. A simple comment in the code giving credit would be courteous but is not required. </p>
<h2>Index</h2>
<dt><a href="#lbBJ">AUTHOR AND COPYRIGHT</a></p>
<dd></dl>

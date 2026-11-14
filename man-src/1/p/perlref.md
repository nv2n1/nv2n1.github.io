---
title: "perlref(1)"
name: "perlref"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlref/"
description: "perlref – Perl references and nested data structures"
---

<h2 class="name">NAME</h2>
<p> perlref &#8211; Perl references and nested data structures </p>
<h2>NOTE</h2>
<p> This is complete documentation about all aspects of references. For a shorter, tutorial introduction to just the essential features, see perlreftut.</p>
<h2>DESCRIPTION</h2>
<p> Before release 5 of Perl it was difficult to represent complex data structures, because all references had to be symbolic&#8212;and even then it was difficult to refer to a variable instead of a symbol table entry. Perl now not only makes it easier to use symbolic references to variables, but also lets you have &#8220;hard&#8221; references to any piece of data or code. Any scalar may hold a hard reference. Because arrays and hashes contain scalars, you can now easily build arrays of arrays, arrays of hashes, hashes of arrays, arrays of hashes of functions, and so on. </p>
<p> Hard references are smart&#8212;they keep track of reference counts for you, automatically freeing the thing referred to when its reference count goes to zero. (Reference counts for values in self-referential or cyclic data structures may not go to zero without a little help; see &#8220;Circular References&#8221; for a detailed explanation.) If that thing happens to be an object, the object is destructed. See perlobj for more about objects. (In a sense, everything in Perl is an object, but we usually reserve the word for references to objects that have been officially &#8220;blessed&#8221; into a class package.) </p>
<p> Symbolic references are names of variables or other objects, just as a symbolic link in a Unix filesystem contains merely the name of a file. The <tt>*glob</tt> notation is something of a symbolic reference. (Symbolic references are sometimes called &#8220;soft references&#8221;, but please don&#8217;t call them that; references are confusing enough without useless synonyms.) </p>
<p> In contrast, hard references are more like hard links in a Unix file system: They are used to access an underlying object without concern for what its (other) name is. When the word &#8220;reference&#8221; is used without an adjective, as in the following paragraph, it is usually talking about a hard reference. </p>
<p> References are easy to use in Perl. There is just one overriding principle: in general, Perl does no implicit referencing or dereferencing. When a scalar is holding a reference, it always behaves as a simple scalar. It doesn&#8217;t magically start being an array or hash or subroutine; you have to tell it explicitly to do so, by dereferencing it.</p>
<h3>Making References</h3>
<p> References can be created in several ways.</p>
<dl>
<dt>1.</p>
<dd> By using the backslash operator on a variable, subroutine, or value. (This works much like the &amp; (address-of) operator in C.) This typically creates <i>another</i> reference to a variable, because there&#8217;s already a reference to the variable in the symbol table. But the symbol table reference might go away, and you&#8217;ll still have the reference that the backslash returned. Here are some examples: </p>
<pre><code>
$scalarref = \$foo;
$arrayref = \@ARGV;
$hashref = \% ENV;
$coderef = \&amp; handler;
$globref = \* foo;
</code></pre>
<p> It isn&#8217;t possible to create a true reference to an <font SIZE="-1">IO</font> handle (filehandle or dirhandle) using the backslash operator. The most you can get is a reference to a typeglob, which is actually a complete symbol table entry. But see the explanation of the <tt>*foo{THING}</tt> syntax below. However, you can still use type globs and globrefs as though they were <font SIZE="-1">IO</font> handles.</p>
<dt>2.</p>
<dd> A reference to an anonymous array can be created using square brackets: </p>
<p>$arrayref = [ 1, 2, [ &#8216;a&#8217;, &#8216;b&#8217;, &#8216;c&#8217; ] ];</p>
<p> Here we&#8217;ve created a reference to an anonymous array of three elements whose final element is itself a reference to another anonymous array of three elements. (The multidimensional syntax described later can be used to access this. For example, after the above, <tt>&quot;$arrayref-&gt;[2][1]&quot;</tt> would have the value &#8220;b&#8221;.) </p>
<p> Taking a reference to an enumerated list is not the same as using square brackets&#8212;instead it&#8217;s the same as creating a list of references! </p>
<p>@list = (\$a, \@b, \% c);<br />
@list = \($a, @b, % c);<br />
#same thing !</p>
<p> As a special case, <tt>&quot;\(@foo)&quot;</tt> returns a list of references to the contents of <tt>@foo</tt>, not a reference to <tt>@foo</tt> itself. Likewise for <tt>%foo</tt>, except that the key references are to copies (since the keys are just strings rather than full-fledged scalars).</p>
<dt>3.</p>
<dd> A reference to an anonymous hash can be created using curly brackets: </p>
<pre>
    $hashref = {
        'Adam'  =&gt; 'Eve',
        'Clyde' =&gt; 'Bonnie',
    };
</pre>
<p> Anonymous hash and array composers like these can be intermixed freely to produce as complicated a structure as you want. The multidimensional syntax described below works for these too. The values above are literals, but variables and expressions would work just as well, because assignment operators in Perl (even within <code>local()</code> or <code>my()</code>) are executable statements, not compile-time declarations. </p>
<p> Because curly brackets (braces) are used for several other things including BLOCKs, you may occasionally have to disambiguate braces at the beginning of a statement by putting a <tt>&quot;+&quot;</tt> or a <tt>&quot;return&quot;</tt> in front so that Perl realizes the opening brace isn&#8217;t starting a <font SIZE="-1">BLOCK.</font> The economy and mnemonic value of using curlies is deemed worth this occasional extra hassle. </p>
<p> For example, if you wanted a function to make a new hash and return a reference to it, you have these options: </p>
<p>sub hashem<br />
{<br />
    {<br />
        @_<br />
    }<br />
}<br />
#silently wrong<br />
    sub hashem<br />
{<br />
    +<br />
    {<br />
        @_<br />
    }<br />
}<br />
#ok sub hashem<br />
{<br />
    return<br />
    {<br />
        @_<br />
    }<br />
}<br />
#ok</p>
<p> On the other hand, if you want the other meaning, you can do this: </p>
<p>sub showem<br />
{<br />
    {<br />
        @_<br />
    }<br />
}<br />
#ambiguous(<br />
    currently ok,<br />
#but may change)<br />
    sub showem {       {; @_ } } #ok sub showem { { return @_ } } #ok</p>
<p> The leading <tt>&quot;+{&quot;</tt> and <tt>&quot;{;&quot;</tt> always serve to disambiguate the expression to mean either the <font SIZE="-1">HASH</font> reference, or the <font SIZE="-1">BLOCK.</font></p>
<dt>4.</p>
<dd> A reference to an anonymous subroutine can be created by using <tt>&quot;sub&quot;</tt> without a subname: </p>
<pre>
    $coderef = sub { print &quot;Boink!
&quot; };
</pre>
<p> Note the semicolon. Except for the code inside not being immediately executed, a <tt>&quot;sub {}&quot;</tt> is not so much a declaration as it is an operator, like <tt>&quot;do{}&quot;</tt> or <tt>&quot;eval{}&quot;</tt>. (However, no matter how many times you execute that particular line (unless you&#8217;re in an <tt>&quot;eval(&quot;...&quot;)&quot;</tt>), <tt>$coderef</tt> will still have a reference to the <i>same</i> anonymous subroutine.) </p>
<p> Anonymous subroutines act as closures with respect to <code>my()</code> variables, that is, variables lexically visible within the current scope. Closure is a notion out of the Lisp world that says if you define an anonymous function in a particular lexical context, it pretends to run in that context even when it&#8217;s called outside the context. </p>
<p> In human terms, it&#8217;s a funny way of passing arguments to a subroutine when you define it as well as when you call it. It&#8217;s useful for setting up little bits of code to run later, such as callbacks. You can even do object-oriented stuff with it, though Perl already provides a different mechanism to do that&#8212;see perlobj. </p>
<p> You might also think of closure as a way to write a subroutine template without using <code>eval()</code>. Here&#8217;s a small example of how closures work: </p>
<p>sub newprint<br />
{<br />
    my $x = shift;<br />
    return sub<br />
    {<br />
        my $y = shift;<br />
        print &#8220;$x, $y!
&#8221;;<br />
    };<br />
}<br />
$h = newprint(&#8220;Howdy&#8221;);<br />
$g = newprint(&#8220;Greetings&#8221;);<br />
#Time passes&#8230;<br />
&amp;$h(&#8220;world&#8221;);<br />
&amp;$g(&#8220;earthlings&#8221;);</p>
<p> This prints </p>
<pre>
    Howdy, world!
    Greetings, earthlings!
</pre>
<p> Note particularly that <tt>$x</tt> continues to refer to the value passed into <code>newprint()</code> <i>despite</i> &#8220;my <tt>$x</tt>&#8221; having gone out of scope by the time the anonymous subroutine runs. That&#8217;s what a closure is all about. </p>
<p> This applies only to lexical variables, by the way. Dynamic variables continue to work as they have always worked. Closure is not something that most Perl programmers need trouble themselves about to begin with.</p>
<dt>5.</p>
<dd> References are often returned by special subroutines called constructors. Perl objects are just references to a special type of object that happens to know which package it&#8217;s associated with. Constructors are just special subroutines that know how to create that association. They do so by starting with an ordinary reference, and it remains an ordinary reference even while it&#8217;s also being an object. Constructors are often named <tt>&quot;new()&quot;</tt>. You <i>can</i> call them indirectly: </p>
<p>$objref = new Doggie(Tail = &gt; &#8216;short&#8217;, Ears = &gt; &#8216;long&#8217;);</p>
<p> But that can produce ambiguous syntax in certain cases, so it&#8217;s often better to use the direct method invocation approach: </p>
<p>$objref = Doggie-&gt;new (Tail = &gt; &#8216;short&#8217;, Ears = &gt; &#8216;long&#8217;);<br />
use Term::Cap;<br />
$terminal = Term::Cap-&gt;Tgetent({OSPEED = &gt; 9600});<br />
use Tk;<br />
$main = MainWindow-&gt;new ();<br />
$menubar = $main-&gt;Frame(-relief = &gt; &#8220;raised&#8221;,<br />
                        -borderwidth = &gt; 2)</p>
<dt>6.</p>
<dd> References of the appropriate type can spring into existence if you dereference them in a context that assumes they exist. Because we haven&#8217;t talked about dereferencing yet, we can&#8217;t show you any examples yet.</p>
<dt>7.</p>
<dd> A reference can be created by using a special syntax, lovingly known as the *foo{<font SIZE="-1">THING</font>} syntax. *foo{<font SIZE="-1">THING</font>} returns a reference to the <font SIZE="-1">THING</font> slot in *foo (which is the symbol table entry which holds everything known as foo). </p>
<p>$scalarref = *foo{SCALAR};<br />
$arrayref = *ARGV{ARRAY};<br />
$hashref = *ENV{HASH};<br />
$coderef = *handler{CODE};<br />
$ioref = *STDIN{IO};<br />
$globref = *foo{GLOB};<br />
$formatref = *foo{FORMAT};<br />
$globname = *foo{NAME};<br />
#&#8221;foo&#8221; $pkgname = * foo{PACKAGE };<br />
#&#8221;main&#8221;</p>
<p> Most of these are self-explanatory, but <tt>*foo{IO}</tt> deserves special attention. It returns the <font SIZE="-1">IO</font> handle, used for file handles (&#8220;open&#8221; in perlfunc), sockets (&#8220;socket&#8221; in perlfunc and &#8220;socketpair&#8221; in perlfunc), and directory handles (&#8220;opendir&#8221; in perlfunc). For compatibility with previous versions of Perl, <tt>*foo{FILEHANDLE}</tt> is a synonym for <tt>*foo{IO}</tt>, though it is discouraged, to encourage a consistent use of one name: <font SIZE="-1">IO.</font> On perls between v5.8 and v5.22, it will issue a deprecation warning, but this deprecation has since been rescinded. </p>
<p> <tt>*foo{THING}</tt> returns undef if that particular <font SIZE="-1">THING</font> hasn&#8217;t been used yet, except in the case of scalars. <tt>*foo{SCALAR}</tt> returns a reference to an anonymous scalar if <tt>$foo</tt> hasn&#8217;t been used yet. This might change in a future release. </p>
<p> <tt>*foo{NAME}</tt> and <tt>*foo{PACKAGE}</tt> are the exception, in that they return strings, rather than references. These return the package and name of the typeglob itself, rather than one that has been assigned to it. So, after <tt>&quot;*foo=*Foo::bar&quot;</tt>, <tt>*foo</tt> will become &#8220;*Foo::bar&#8221; when used as a string, but <tt>*foo{PACKAGE}</tt> and <tt>*foo{NAME}</tt> will continue to produce &#8220;main&#8221; and &#8220;foo&#8221;, respectively. </p>
<p> <tt>*foo{IO}</tt> is an alternative to the <tt>*HANDLE</tt> mechanism given in &#8220;Typeglobs and Filehandles&#8221; in perldata for passing filehandles into or out of subroutines, or storing into larger data structures. Its disadvantage is that it won&#8217;t create a new filehandle for you. Its advantage is that you have less risk of clobbering more than you want to with a typeglob assignment. (It still conflates file and directory handles, though.) However, if you assign the incoming value to a scalar instead of a typeglob as we do in the examples below, there&#8217;s no risk of that happening. </p>
<p>splutter(*STDOUT);<br />
#pass the whole glob<br />
    splutter(*STDOUT{IO});<br />
#pass both file and dir handles<br />
    sub splutter<br />
{<br />
    my $fh = shift;<br />
    print $fh &#8220;her um well a hmmm
&#8221;;<br />
}<br />
$rec = get_rec(*STDIN);<br />
#pass the whole glob<br />
    $rec = get_rec(*STDIN{IO});<br />
#pass both file and dir handles<br />
    sub get_rec<br />
{<br />
    my $fh = shift;<br />
    return scalar&lt;$fh&gt;;<br />
}
</dl>
<h3>Using References</h3>
<p> That&#8217;s it for creating references. By now you&#8217;re probably dying to know how to use references to get back to your long-lost data. There are several basic methods.</p>
<dl>
<dt>1.</p>
<dd> Anywhere you&#8217;d put an identifier (or chain of identifiers) as part of a variable or subroutine name, you can replace the identifier with a simple scalar variable containing a reference of the correct type: </p>
<p>$bar = $$scalarref;<br />
push(@$arrayref, $filename);<br />
$$arrayref[0] = &#8220;January&#8221;;<br />
$$hashref{&#8220;KEY&#8221;} = &#8220;VALUE&#8221;;<br />
&amp;$coderef(1, 2, 3);<br />
print $globref &#8220;output
&#8221;;</p>
<p> It&#8217;s important to understand that we are specifically <i>not</i> dereferencing <tt>$arrayref[0]</tt> or <tt>$hashref{&quot;KEY&quot;}</tt> there. The dereference of the scalar variable happens <i>before</i> it does any key lookups. Anything more complicated than a simple scalar variable must use methods 2 or 3 below. However, a &#8220;simple scalar&#8221; includes an identifier that itself uses method 1 recursively. Therefore, the following prints &#8220;howdy&#8221;. </p>
<pre>
    $refrefref = \\&quot;howdy&quot;;
    print $$$$refrefref;
</pre>
<dt>2.</p>
<dd> Anywhere you&#8217;d put an identifier (or chain of identifiers) as part of a variable or subroutine name, you can replace the identifier with a <font SIZE="-1">BLOCK</font> returning a reference of the correct type. In other words, the previous examples could be written like this: </p>
<p>$bar = ${$scalarref};<br />
push(@{$arrayref}, $filename);<br />
${$arrayref}[0] = &#8220;January&#8221;;<br />
${$hashref} {&#8220;KEY&#8221;} = &#8220;VALUE&#8221;;<br />
&amp;{$coderef}(1, 2, 3);<br />
$globref-&gt;print(&#8220;output
&#8221;);<br />
#iff IO::Handle is loaded</p>
<p> Admittedly, it&#8217;s a little silly to use the curlies in this case, but the <font SIZE="-1">BLOCK</font> can contain any arbitrary expression, in particular, subscripted expressions: </p>
<p>&amp;{$dispatch{$index}}(1, 2, 3);<br />
#call correct routine</p>
<p> Because of being able to omit the curlies for the simple case of <tt>$$x</tt>, people often make the mistake of viewing the dereferencing symbols as proper operators, and wonder about their precedence. If they were, though, you could use parentheses instead of braces. That&#8217;s not the case. Consider the difference below; case 0 is a short-hand version of case 1, <i>not</i> case 2: </p>
<p>$$hashref{&#8220;KEY&#8221;} = &#8220;VALUE&#8221;;<br />
#CASE 0 ${$hashref } {&#8220;KEY&#8221; } = &#8220;VALUE&#8221;;<br />
#CASE 1 ${$hashref{&#8220;KEY&#8221; } } = &#8220;VALUE&#8221;;<br />
#CASE 2 ${$hashref-&gt;{&#8220;KEY&#8221; } } = &#8220;VALUE&#8221;;<br />
#CASE 3</p>
<p> Case 2 is also deceptive in that you&#8217;re accessing a variable called <tt>%hashref</tt>, not dereferencing through <tt>$hashref</tt> to the hash it&#8217;s presumably referencing. That would be case 3.</p>
<dt>3.</p>
<dd> Subroutine calls and lookups of individual array elements arise often enough that it gets cumbersome to use method 2. As a form of syntactic sugar, the examples for method 2 may be written: </p>
<p>$arrayref-&gt;[0] = &#8220;January&#8221;;<br />
#Array element<br />
    $hashref-&gt;{&#8220;KEY&#8221; } = &#8220;VALUE&#8221;;<br />
#Hash element<br />
    $coderef-&gt;(1, 2, 3);<br />
#Subroutine call</p>
<p> The left side of the arrow can be any expression returning a reference, including a previous dereference. Note that <tt>$array[$x]</tt> is <i>not</i> the same thing as <tt>&quot;$array-&gt;[$x]&quot;</tt> here: </p>
<p>$array[$x]-&gt;<br />
{<br />
    &#8220;foo&#8221;<br />
    } -&gt; [0] = &#8220;January&#8221;;</p>
<p> This is one of the cases we mentioned earlier in which references could spring into existence when in an lvalue context. Before this statement, <tt>$array[$x]</tt> may have been undefined. If so, it&#8217;s automatically defined with a hash reference so that we can look up <tt>&quot;{&quot;foo&quot;}&quot;</tt> in it. Likewise <tt>&quot;$array[$x]-&gt;{&quot;foo&quot;}&quot;</tt> will automatically get defined with an array reference so that we can look up <tt>&quot;[0]&quot;</tt> in it. This process is called <i>autovivification</i>. </p>
<p> One more thing here. The arrow is optional <i>between</i> brackets subscripts, so you can shrink the above down to </p>
<p>$array[$x]{&#8220;foo&#8221;}[0] = &#8220;January&#8221;;</p>
<p> Which, in the degenerate case of using only ordinary arrays, gives you multidimensional arrays just like C&#8217;s: </p>
<p>$score[$x][$y][$z] += 42;</p>
<p> Well, okay, not entirely like C&#8217;s arrays, actually. C doesn&#8217;t know how to grow its arrays on demand. Perl does.</p>
<dt>4.</p>
<dd> If a reference happens to be a reference to an object, then there are probably methods to access the things referred to, and you should probably stick to those methods unless you&#8217;re in the class package that defines the object&#8217;s methods. In other words, be nice, and don&#8217;t violate the object&#8217;s encapsulation without a very good reason. Perl does not enforce encapsulation. We are not totalitarians here. We do expect some basic civility though.</dl>
<p> Using a string or number as a reference produces a symbolic reference, as explained above. Using a reference as a number produces an integer representing its storage location in memory. The only useful thing to be done with this is to compare two references numerically to see whether they refer to the same location. </p>
<p>if ($ref1 == $ref2) {<br />
#cheap numeric compare of references<br />
        print &#8220;refs 1 and 2 refer to the same thing
&#8221;;<br />
}</p>
<p> Using a reference as a string produces both its referent&#8217;s type, including any package blessing as described in perlobj, as well as the numeric address expressed in hex. The <code>ref()</code> operator returns just the type of thing the reference is pointing to, without the address. See &#8220;ref&#8221; in perlfunc for details and examples of its use. </p>
<p> The <code>bless()</code> operator may be used to associate the object a reference points to with a package functioning as an object class. See perlobj. </p>
<p> A typeglob may be dereferenced the same way a reference can, because the dereference syntax always indicates the type of reference desired. So <tt>&quot;${*foo}&quot;</tt> and <tt>&quot;${\$foo}&quot;</tt> both indicate the same scalar variable. </p>
<p> Here&#8217;s a trick for interpolating a subroutine call into a string: </p>
<p>print &#8220;My sub returned @{[mysub(1,2,3)]} that time.
&#8221;;</p>
<p> The way it works is that when the <tt>&quot;@{...}&quot;</tt> is seen in the double-quoted string, it&#8217;s evaluated as a block. The block creates a reference to an anonymous array containing the results of the call to <tt>&quot;mysub(1,2,3)&quot;</tt>. So the whole block returns a reference to an array, which is then dereferenced by <tt>&quot;@{...}&quot;</tt> and stuck into the double-quoted string. This chicanery is also useful for arbitrary expressions: </p>
<p>print &#8220;That yields @{[$n + 5]} widgets
&#8221;;</p>
<p> Similarly, an expression that returns a reference to a scalar can be dereferenced via <tt>&quot;${...}&quot;</tt>. Thus, the above expression may be written as: </p>
<pre>
    print &quot;That yields ${\($n + 5)} widgets
&quot;;
</pre>
<h3>Circular References</h3>
<p> It is possible to create a &#8220;circular reference&#8221; in Perl, which can lead to memory leaks. A circular reference occurs when two references contain a reference to each other, like this: </p>
<p>my $foo = {};<br />
my $bar = {foo = &gt; $foo};<br />
$foo-&gt;{bar} = $bar;</p>
<p> You can also create a circular reference with a single variable: </p>
<pre>
    my $foo;
    $foo = \$foo;
</pre>
<p> In this case, the reference count for the variables will never reach 0, and the references will never be garbage-collected. This can lead to memory leaks. </p>
<p> Because objects in Perl are implemented as references, it&#8217;s possible to have circular references with objects as well. Imagine a TreeNode class where each node references its parent and child nodes. Any node with a parent will be part of a circular reference. </p>
<p> You can break circular references by creating a &#8220;weak reference&#8221;. A weak reference does not increment the reference count for a variable, which means that the object can go out of scope and be destroyed. You can weaken a reference with the <tt>&quot;weaken&quot;</tt> function exported by the Scalar::Util module. </p>
<p> Here&#8217;s how we can make the first example safer: </p>
<p>use Scalar::Util &#8216;weaken&#8217;;<br />
my $foo = {};<br />
my $bar = {foo = &gt; $foo};<br />
$foo-&gt;{bar} = $bar;<br />
weaken $foo-&gt;{bar};</p>
<p> The reference from <tt>$foo</tt> to <tt>$bar</tt> has been weakened. When the <tt>$bar</tt> variable goes out of scope, it will be garbage-collected. The next time you look at the value of the <tt>&quot;$foo-&gt;{bar}&quot;</tt> key, it will be <tt>&quot;undef&quot;</tt>. </p>
<p> This action at a distance can be confusing, so you should be careful with your use of weaken. You should weaken the reference in the variable that will go out of scope <i>first</i>. That way, the longer-lived variable will contain the expected reference until it goes out of scope.</p>
<h3>Symbolic references</h3>
<p> We said that references spring into existence as necessary if they are undefined, but we didn&#8217;t say what happens if a value used as a reference is already defined, but <i>isn&#8217;t</i> a hard reference. If you use it as a reference, it&#8217;ll be treated as a symbolic reference. That is, the value of the scalar is taken to be the <i>name</i> of a variable, rather than a direct link to a (possibly) anonymous value. </p>
<p> People frequently expect it to work like this. So it does. </p>
<p>$name = &#8220;foo&#8221;;<br />
$$name = 1;<br />
#Sets $foo<br />
    ${$name } = 2;<br />
#Sets $foo<br />
    ${$name x 2 } = 3;<br />
#Sets $foofoo<br />
    $name-&gt;[0] = 4;<br />
#Sets $foo[0]<br />
           @$name = ();<br />
#Clears @foo<br />
    &amp;<br />
    $name();<br />
#Calls &amp;foo()<br />
    $pack = &#8220;THAT&#8221;;<br />
${&#8220;${pack}::$name&#8221;} = 5;<br />
#Sets $THAT::foo without eval</p>
<p> This is powerful, and slightly dangerous, in that it&#8217;s possible to intend (with the utmost sincerity) to use a hard reference, and accidentally use a symbolic reference instead. To protect against that, you can say </p>
<pre>
    use strict 'refs';
</pre>
<p> and then only hard references will be allowed for the rest of the enclosing block. An inner block may countermand that with </p>
<pre>
    no strict 'refs';
</pre>
<p> Only package variables (globals, even if localized) are visible to symbolic references. Lexical variables (declared with <code>my()</code>) aren&#8217;t in a symbol table, and thus are invisible to this mechanism. For example: </p>
<p>local $value = 10;<br />
$ref = &#8220;value&#8221;;<br />
{<br />
    my $value = 20;<br />
    print $$ref;<br />
}</p>
<p> This will still print 10, not 20. Remember that <code>local()</code> affects package variables, which are all &#8220;global&#8221; to the package.</p>
<h3>Not-so-symbolic references</h3>
<p> Brackets around a symbolic reference can simply serve to isolate an identifier or variable name from the rest of an expression, just as they always have within a string. For example, </p>
<p>$push = &#8220;pop on &#8220;;<br />
print &#8220;${push}over&#8221;;</p>
<p> has always meant to print &#8220;pop on over&#8221;, even though push is a reserved word. This is generalized to work the same without the enclosing double quotes, so that </p>
<pre>
    print ${push} . &quot;over&quot;;
</pre>
<p> and even </p>
<pre>
    print ${ push } . &quot;over&quot;;
</pre>
<p> will have the same effect. This construct is <i>not</i> considered to be a symbolic reference when you&#8217;re using strict refs: </p>
<p>use strict &#8216;refs&#8217;;<br />
${bareword};<br />
#Okay, means $bareword.${&#8220;bareword&#8221; };<br />
#Error, symbolic reference.</p>
<p> Similarly, because of all the subscripting that is done using single words, the same rule applies to any bareword that is used for subscripting a hash. So now, instead of writing </p>
<p>$hash{&#8220;aaa&#8221;} {&#8220;bbb&#8221;}<br />
{<br />
    &#8220;ccc&#8221;<br />
}</p>
<p> you can write just </p>
<p>$hash{aaa} {bbb}<br />
{<br />
    ccc<br />
}</p>
<p> and not worry about whether the subscripts are reserved words. In the rare event that you do wish to do something like </p>
<pre>
    $hash{ shift }
</pre>
<p> you can force interpretation as a reserved word by adding anything that makes it more than a bareword: </p>
<p>$hash{shift()} $hash{+shift} $hash<br />
{<br />
    shift @_<br />
}</p>
<p> The <tt>&quot;use warnings&quot;</tt> pragma or the <code>-w</code> switch will warn you if it interprets a reserved word as a string. But it will no longer warn you about using lowercase words, because the string is effectively quoted.</p>
<h3>Pseudo-hashes: Using an array as a hash</h3>
<p> Pseudo-hashes have been removed from Perl. The &#8216;fields&#8217; pragma remains available.</p>
<h3>Function Templates</h3>
<p> As explained above, an anonymous function with access to the lexical variables visible when that function was compiled, creates a closure. It retains access to those variables even though it doesn&#8217;t get run until later, such as in a signal handler or a Tk callback. </p>
<p> Using a closure as a function template allows us to generate many functions that act similarly. Suppose you wanted functions named after the colors that generated <font SIZE="-1">HTML</font> font changes for the various colors: </p>
<pre>
    print &quot;Be &quot;, red(&quot;careful&quot;), &quot;with that &quot;, green(&quot;light&quot;);
</pre>
<p> The <code>red()</code> and <code>green()</code> functions would be similar. To create these, we&#8217;ll assign a closure to a typeglob of the name of the function we&#8217;re trying to build. </p>
<p>@colors = qw(red blue green yellow orange purple violet);<br />
    for<br />
        my $name(@colors)<br />
        {<br />
            no strict &#8216;refs&#8217;;<br />
#allow symbol table manipulation<br />
                *$name = *{uc $name } = sub{&#8220;&lt;FONT COLOR=&#8217;$name&#8217;&gt;@_&lt;/FONT&gt;&#8221; };<br />
        }</p>
<p> Now all those different functions appear to exist independently. You can call <code>red()</code>, <font SIZE="-1"><code>RED</code></font><code>()</code>, <code>blue()</code>, <font SIZE="-1"><code>BLUE</code></font><code>()</code>, <code>green()</code>, etc. This technique saves on both compile time and memory use, and is less error-prone as well, since syntax checks happen at compile time. It&#8217;s critical that any variables in the anonymous subroutine be lexicals in order to create a proper closure. That&#8217;s the reasons for the <tt>&quot;my&quot;</tt> on the loop iteration variable. </p>
<p> This is one of the only places where giving a prototype to a closure makes much sense. If you wanted to impose scalar context on the arguments of these functions (probably not a wise idea for this particular example), you could have written it this way instead: </p>
<pre>
    *$name = sub ($) { &quot;&lt;FONT COLOR='$name'&gt;$_[0]&lt;/FONT&gt;&quot; };
</pre>
<p> However, since prototype checking happens at compile time, the assignment above happens too late to be of much use. You could address this by putting the whole loop of assignments within a <font SIZE="-1">BEGIN</font> block, forcing it to occur during compilation. </p>
<p> Access to lexicals that change over time&#8212;like those in the <tt>&quot;for&quot;</tt> loop above, basically aliases to elements from the surrounding lexical scopes&#8212; only works with anonymous subs, not with named subroutines. Generally said, named subroutines do not nest properly and should only be declared in the main package scope. </p>
<p> This is because named subroutines are created at compile time so their lexical variables get assigned to the parent lexicals from the first execution of the parent block. If a parent scope is entered a second time, its lexicals are created again, while the nested subs still reference the old ones. </p>
<p> Anonymous subroutines get to capture each time you execute the <tt>&quot;sub&quot;</tt> operator, as they are created on the fly. If you are accustomed to using nested subroutines in other programming languages with their own private variables, you&#8217;ll have to work at it a bit in Perl. The intuitive coding of this type of thing incurs mysterious warnings about &#8220;will not stay shared&#8221; due to the reasons explained above. For example, this won&#8217;t work: </p>
<p>sub outer<br />
{<br />
    my $x = $_[0] + 35;<br />
    sub inner<br />
    {<br />
        return $x * 19<br />
    }<br />
#WRONG return $x + inner();<br />
}</p>
<p> A work-around is the following: </p>
<p>sub outer<br />
{<br />
    my $x = $_[0] + 35;<br />
    local *inner = sub{return $x * 19};<br />
    return $x + inner();<br />
}</p>
<p> Now <code>inner()</code> can only be called from within <code>outer()</code>, because of the temporary assignments of the anonymous subroutine. But when it does, it has normal access to the lexical variable <tt>$x</tt> from the scope of <code>outer()</code> at the time outer is invoked. </p>
<p> This has the interesting effect of creating a function local to another function, something not normally supported in Perl.</p>
<h2>WARNING: Don&#8217;t use references as hash keys</h2>
<p> You may not (usefully) use a reference as the key to a hash. It will be converted into a string: </p>
<pre>
    $x{ \$a } = $a;
</pre>
<p> If you try to dereference the key, it won&#8217;t do a hard dereference, and you won&#8217;t accomplish what you&#8217;re attempting. You might want to do something more like </p>
<p>$r = \@a;<br />
$x{$r} = $r;</p>
<p> And then at least you can use the <code>values()</code>, which will be real refs, instead of the <code>keys()</code>, which won&#8217;t. </p>
<p> The standard Tie::RefHash module provides a convenient workaround to this.</p>
<h3>Postfix Dereference Syntax</h3>
<p> Beginning in v5.20.0, a postfix syntax for using references is available. It behaves as described in &#8220;Using References&#8221;, but instead of a prefixed sigil, a postfixed sigil-and-star is used. </p>
<p> For example: </p>
<p>$r = \@a;<br />
@b = $r-&gt;@ *;<br />
#equivalent to @$r or @{$r } $r = [1, [2, 3], 4];<br />
$r-&gt;[1] -&gt; @ *;<br />
#equivalent to @{$r-&gt;[1] }</p>
<p> In Perl 5.20 and 5.22, this syntax must be enabled with <tt>&quot;use feature 'postderef'&quot;</tt>. As of Perl 5.24, no feature declarations are required to make it available. </p>
<p> Postfix dereference should work in all circumstances where block (circumfix) dereference worked, and should be entirely equivalent. This syntax allows dereferencing to be written and read entirely left-to-right. The following equivalencies are defined: </p>
<p>$sref-&gt;$ *;<br />
#same as ${$sref } $aref-&gt;@ *;<br />
#same as @{$aref } $aref-&gt;$ #*;<br />
#same as $ #{$aref } $href-&gt;% *;<br />
#same as % {$href } $cref-&gt;&amp;*;<br />
#same as &amp;{$cref } $gref-&gt;**;<br />
#same as *<br />
{<br />
    $gref<br />
}</p>
<p> Note especially that <tt>&quot;$cref-&gt;&amp;*&quot;</tt> is <i>not</i> equivalent to <tt>&quot;$cref-&gt;()&quot;</tt>, and can serve different purposes. </p>
<p> Glob elements can be extracted through the postfix dereferencing feature: </p>
<p>$gref-&gt;*{SCALAR};<br />
#same as *{$gref }<br />
{<br />
    SCALAR<br />
}</p>
<p> Postfix array and scalar dereferencing <i>can</i> be used in interpolating strings (double quotes or the <tt>&quot;qq&quot;</tt> operator), but only if the <tt>&quot;postderef_qq&quot;</tt> feature is enabled.</p>
<h3>Postfix Reference Slicing</h3>
<p> Value slices of arrays and hashes may also be taken with postfix dereferencing notation, with the following equivalencies: </p>
<p>$aref-&gt;@[&#8230; ];<br />
#same as @$aref[&#8230;] $href-&gt;@{&#8230; };<br />
#same as @$href<br />
{<br />
    &#8230;<br />
}</p>
<p> Postfix key/value pair slicing, added in 5.20.0 and documented in the Key/Value Hash Slices section of perldata, also behaves as expected: </p>
<p>$aref-&gt;% [&#8230;];<br />
#same as % $aref[&#8230;] $href-&gt;% {&#8230; };<br />
#same as % $href<br />
{<br />
    &#8230;<br />
}</p>
<p> As with postfix array, postfix value slice dereferencing <i>can</i> be used in interpolating strings (double quotes or the <tt>&quot;qq&quot;</tt> operator), but only if the <tt>&quot;postderef_qq&quot;</tt> feature is enabled.</p>
<h3>Assigning to References</h3>
<p> Beginning in v5.22.0, the referencing operator can be assigned to. It performs an aliasing operation, so that the variable name referenced on the left-hand side becomes an alias for the thing referenced on the right-hand side: </p>
<pre>
    \$a = \$b; # $a and $b now point to the same scalar
    \&amp;foo = \&amp;bar; # foo() now means bar()
</pre>
<p> This syntax must be enabled with <tt>&quot;use feature 'refaliasing'&quot;</tt>. It is experimental, and will warn by default unless <tt>&quot;no warnings 'experimental::refaliasing'&quot;</tt> is in effect. </p>
<p> These forms may be assigned to, and cause the right-hand side to be evaluated in scalar context: </p>
<p>\$scalar<br />
    \@array<br />
    \% hash<br />
    \&amp;sub<br />
    \my $scalar<br />
    \my @array<br />
    \my % hash<br />
    \state $scalar # or @array, etc.<br />
    \our $scalar #etc.<br />
    \local $scalar #etc.<br />
    \local our $scalar #etc.<br />
    \$some_array[$index]<br />
    \$some_hash<br />
{<br />
    $key<br />
}<br />
\local $some_array[$index]<br />
    \local $some_hash{$key} condition ? \$this : \$that[0] #etc.</p>
<p> Slicing operations and parentheses cause the right-hand side to be evaluated in list context: </p>
<p>\@array[5..7](\@array[5..7])<br />
    \(@array[5..7])<br />
    \@hash{&#8216;foo&#8217;, &#8216;bar&#8217;}(\@hash{&#8216;foo&#8217;, &#8216;bar&#8217;})<br />
    \(@hash{&#8216;foo&#8217;, &#8216;bar&#8217;})(\$scalar)<br />
    \($scalar)<br />
    \(my $scalar)<br />
    \my($scalar)(\@array)(\% hash)(\&amp;sub)<br />
    \(&amp;sub)<br />
    \($foo, @bar, % baz)(\$foo, \@bar, \% baz)</p>
<p> Each element on the right-hand side must be a reference to a datum of the right type. Parentheses immediately surrounding an array (and possibly also <tt>&quot;my&quot;</tt>/<tt>&quot;state&quot;</tt>/<tt>&quot;our&quot;</tt>/<tt>&quot;local&quot;</tt>) will make each element of the array an alias to the corresponding scalar referenced on the right-hand side: </p>
<p>\(@a) = \(@b);<br />
#@a and @b now have the same elements<br />
    \my(@a) = \(@b);<br />
#likewise<br />
    \(my @a) = \(@b);<br />
#likewise push @a, 3;<br />
#but now @a has an extra element that @b lacks<br />
    \(@a) = (\$a, \$b, \$c);<br />
#@a now contains $a, $b, and $c</p>
<p> Combining that form with <tt>&quot;local&quot;</tt> and putting parentheses immediately around a hash are forbidden (because it is not clear what they should do): </p>
<p>\local(@array) = foo();<br />
#WRONG<br />
    \(% hash) = bar();<br />
#WRONG</p>
<p> Assignment to references and non-references may be combined in lists and conditional ternary expressions, as long as the values on the right-hand side are the right type for each element on the left, though this may make for obfuscated code: </p>
<p>(my $tom, \my $dick, \my @harry) = (\1, \2, [1..3]);<br />
#$tom is now \1<br />
#$dick is now 2(read &#8211; only)<br />
#@harry is(1, 2, 3)<br />
my $type = ref $thingy;<br />
($type ? $type eq &#8216;ARRAY&#8217; ? \@foo : \$bar : $baz) = $thingy;</p>
<p> The <tt>&quot;foreach&quot;</tt> loop can also take a reference constructor for its loop variable, though the syntax is limited to one of the following, with an optional <tt>&quot;my&quot;</tt>, <tt>&quot;state&quot;</tt>, or <tt>&quot;our&quot;</tt> after the backslash: </p>
<pre>
    \$s
    \@a
    \%h
    \&amp;c
</pre>
<p> No parentheses are permitted. This feature is particularly useful for arrays-of-arrays, or arrays-of-hashes: </p>
<p>foreach<br />
    \my @a(@array_of_arrays)<br />
    {<br />
        frobnicate($a[0], $a[-1]);<br />
    }<br />
foreach<br />
    \my % h(@array_of_hashes)<br />
    {<br />
        $h<br />
        {<br />
            gelastic<br />
        }<br />
        ++if $h{type} eq &#8216;funny&#8217;;<br />
    }</p>
<p> <font SIZE="-1"><code>CAVEAT:</code></font> Aliasing does not work correctly with closures. If you try to alias lexical variables from an inner subroutine or <tt>&quot;eval&quot;</tt>, the aliasing will only be visible within that inner sub, and will not affect the outer subroutine where the variables are declared. This bizarre behavior is subject to change.</p>
<h2>Declaring a Reference to a Variable</h2>
<p> Beginning in v5.26.0, the referencing operator can come after <tt>&quot;my&quot;</tt>, <tt>&quot;state&quot;</tt>, <tt>&quot;our&quot;</tt>, or <tt>&quot;local&quot;</tt>. This syntax must be enabled with <tt>&quot;use feature 'declared_refs'&quot;</tt>. It is experimental, and will warn by default unless <tt>&quot;no warnings 'experimental::refaliasing'&quot;</tt> is in effect. </p>
<p> This feature makes these: </p>
<pre>
    my \$x;
    our \$y;
</pre>
<p> equivalent to: </p>
<pre>
    \my $x;
    \our $x;
</pre>
<p> It is intended mainly for use in assignments to references (see &#8220;Assigning to References&#8221;, above). It also allows the backslash to be used on just some items in a list of declared variables: </p>
<pre><code>
my($foo, \@bar, \% baz);
#equivalent to : my $foo, \my(@bar, % baz);
</code></pre>
<h2>SEE ALSO</h2>
<p> Besides the obvious documents, source code can be instructive. Some pathological examples of the use of references can be found in the <i>t/op/ref.t</i> regression test in the Perl source directory. </p>
<p> See also perldsc and perllol for how to use references to create complex data structures, and perlootut and perlobj for how to use them to create objects. </p>
<h2>Index</h2>

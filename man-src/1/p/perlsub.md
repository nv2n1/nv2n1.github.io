---
title: "perlsub(1)"
name: "perlsub"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlsub/"
description: "perlsub – Perl subroutines"
---

<h2 class="name">NAME</h2>
<p> perlsub &#8211; Perl subroutines </p>
<h2>SYNOPSIS</h2>
<p> To declare subroutines: </p>
<pre><code>
sub NAME;
#A "forward" declaration.sub NAME(PROTO);
#ditto, but with prototypes
            sub NAME : ATTRS;
#with attributes
    sub NAME(PROTO) : ATTRS;
#with attributes and prototypes
    sub NAME BLOCK #A declaration and a definition.sub NAME(PROTO) BLOCK #ditto,
    but with prototypes
        sub NAME : ATTRS BLOCK #with attributes
            sub NAME(PROTO) : ATTRS BLOCK #with prototypes and attributes
                use feature 'signatures';
sub NAME(SIG) BLOCK #with signature
    sub NAME : ATTRS(SIG) BLOCK #with signature,
               attributes
               sub NAME : prototype(PROTO)(SIG) BLOCK #with signature,
                          prototype
</code></pre>
<p> To define an anonymous subroutine at runtime: </p>
<p>$subref = sub BLOCK;<br />
#no proto<br />
    $subref = sub(PROTO) BLOCK;<br />
#with proto<br />
    $subref = sub : ATTRS BLOCK;<br />
#with attributes<br />
    $subref = sub(PROTO) : ATTRS BLOCK;<br />
#with proto and attributes<br />
    use feature &#8216;signatures&#8217;;<br />
$subref = sub(SIG) BLOCK;<br />
#with signature<br />
    $subref = sub : ATTRS(SIG) BLOCK;<br />
#with signature, attributes</p>
<p> To import subroutines: </p>
<pre>
    use MODULE qw(NAME1 NAME2 NAME3);
</pre>
<p> To call subroutines: </p>
<p>NAME(LIST);<br />
#&amp; is optional with parentheses.NAME LIST;<br />
#Parentheses optional if predeclared / imported.<br />
                                           &amp;NAME(LIST);<br />
#Circumvent prototypes.<br />
    &amp;NAME;<br />
#Makes current @_ visible to called subroutine.</p>
<h2>DESCRIPTION</h2>
<p> Like many languages, Perl provides for user-defined subroutines. These may be located anywhere in the main program, loaded in from other files via the <tt>&quot;do&quot;</tt>, <tt>&quot;require&quot;</tt>, or <tt>&quot;use&quot;</tt> keywords, or generated on the fly using <tt>&quot;eval&quot;</tt> or anonymous subroutines. You can even call a function indirectly using a variable containing its name or a <font SIZE="-1">CODE</font> reference. </p>
<p> The Perl model for function call and return values is simple: all functions are passed as parameters one single flat list of scalars, and all functions likewise return to their caller one single flat list of scalars. Any arrays or hashes in these call and return lists will collapse, losing their identities&#8212;but you may always use pass-by-reference instead to avoid this. Both call and return lists may contain as many or as few scalar elements as you&#8217;d like. (Often a function without an explicit return statement is called a subroutine, but there&#8217;s really no difference from Perl&#8217;s perspective.) </p>
<p> Any arguments passed in show up in the array <tt>@_</tt>. (They may also show up in lexical variables introduced by a signature; see &#8220;Signatures&#8221; below.) Therefore, if you called a function with two arguments, those would be stored in <tt>$_[0]</tt> and <tt>$_[1]</tt>. The array <tt>@_</tt> is a local array, but its elements are aliases for the actual scalar parameters. In particular, if an element <tt>$_[0]</tt> is updated, the corresponding argument is updated (or an error occurs if it is not updatable). If an argument is an array or hash element which did not exist when the function was called, that element is created only when (and if) it is modified or a reference to it is taken. (Some earlier versions of Perl created the element whether or not the element was assigned to.) Assigning to the whole array <tt>@_</tt> removes that aliasing, and does not update any arguments. </p>
<p> A <tt>&quot;return&quot;</tt> statement may be used to exit a subroutine, optionally specifying the returned value, which will be evaluated in the appropriate context (list, scalar, or void) depending on the context of the subroutine call. If you specify no return value, the subroutine returns an empty list in list context, the undefined value in scalar context, or nothing in void context. If you return one or more aggregates (arrays and hashes), these will be flattened together into one large indistinguishable list. </p>
<p> If no <tt>&quot;return&quot;</tt> is found and if the last statement is an expression, its value is returned. If the last statement is a loop control structure like a <tt>&quot;foreach&quot;</tt> or a <tt>&quot;while&quot;</tt>, the returned value is unspecified. The empty sub returns the empty list. </p>
<p> Aside from an experimental facility (see &#8220;Signatures&#8221; below), Perl does not have named formal parameters. In practice all you do is assign to a <tt>&quot;my()&quot;</tt> list of these. Variables that aren&#8217;t declared to be private are global variables. For gory details on creating private variables, see &#8220;Private Variables via <code>my()</code>&#8221; and &#8220;Temporary Values via <code>local()</code>&#8221;. To create protected environments for a set of functions in a separate package (and probably a separate file), see &#8220;Packages&#8221; in perlmod. </p>
<p> Example: </p>
<p>sub max<br />
{<br />
    my $max = shift(@_);<br />
    foreach<br />
        $foo(@_)<br />
        {<br />
            $max = $foo if $max &lt; $foo;<br />
        }<br />
    return $max;<br />
}<br />
$bestday = max($mon, $tue, $wed, $thu, $fri);</p>
<p> Example: </p>
<p>#get a line, combining continuation lines<br />
#that start with whitespace<br />
sub get_line<br />
{<br />
    $thisline = $lookahead;<br />
#global variables !LINE : while (defined($lookahead = &lt;STDIN&gt;))<br />
    {<br />
        if ($lookahead = ~ / ^[ 	] /) {<br />
            $thisline.= $lookahead;<br />
        } else {<br />
            last LINE;<br />
        }<br />
    }<br />
    return $thisline;<br />
}<br />
$lookahead = &lt;STDIN&gt;;<br />
#get first line while (defined($line = get_line()))<br />
{<br />
    &#8230;<br />
}</p>
<p> Assigning to a list of private variables to name your arguments: </p>
<p>sub maybeset<br />
{<br />
    my($key, $value) = @_;<br />
    $Foo{$key} = $value unless $Foo{$key};<br />
}</p>
<p> Because the assignment copies the values, this also has the effect of turning call-by-reference into call-by-value. Otherwise a function is free to do in-place modifications of <tt>@_</tt> and change its caller&#8217;s values. </p>
<p>upcase_in($v1, $v2);<br />
#this changes $v1 and $v2<br />
    sub upcase_in<br />
{<br />
    for (@_) {<br />
        tr / a &#8211; z / A &#8211; Z /<br />
    }<br />
}</p>
<p> You aren&#8217;t allowed to modify constants in this way, of course. If an argument were actually literal and you tried to change it, you&#8217;d take a (presumably fatal) exception. For example, this won&#8217;t work: </p>
<pre>
    upcase_in(&quot;frederick&quot;);
</pre>
<p> It would be much safer if the <tt>&quot;upcase_in()&quot;</tt> function were written to return a copy of its parameters instead of changing them in place: </p>
<p>($v3, $v4) = upcase($v1, $v2);<br />
#this doesn&#8217;t change $v1 and $v2 sub upcase<br />
{<br />
    return unless defined wantarray;<br />
#void context, do nothing<br />
                       my @parms = @_;<br />
    for (@parms) {<br />
        tr / a &#8211; z / A &#8211; Z /<br />
    }<br />
    return wantarray ? @parms : $parms[0];<br />
}</p>
<p> Notice how this (unprototyped) function doesn&#8217;t care whether it was passed real scalars or arrays. Perl sees all arguments as one big, long, flat parameter list in <tt>@_</tt>. This is one area where Perl&#8217;s simple argument-passing style shines. The <tt>&quot;upcase()&quot;</tt> function would work perfectly well without changing the <tt>&quot;upcase()&quot;</tt> definition even if we fed it things like this: </p>
<p>@newlist = upcase(@list1, @list2);<br />
@newlist = upcase(split /<br />
                  : /, $var);</p>
<p> Do not, however, be tempted to do this: </p>
<pre>
    (@a, @b)   = upcase(@list1, @list2);
</pre>
<p> Like the flattened incoming parameter list, the return list is also flattened on return. So all you have managed to do here is stored everything in <tt>@a</tt> and made <tt>@b</tt> empty. See &#8220;Pass by Reference&#8221; for alternatives. </p>
<p> A subroutine may be called using an explicit <tt>&quot;&amp;&quot;</tt> prefix. The <tt>&quot;&amp;&quot;</tt> is optional in modern Perl, as are parentheses if the subroutine has been predeclared. The <tt>&quot;&amp;&quot;</tt> is <i>not</i> optional when just naming the subroutine, such as when it&#8217;s used as an argument to <code>defined()</code> or <code>undef()</code>. Nor is it optional when you want to do an indirect subroutine call with a subroutine name or reference using the <tt>&quot;&amp;$subref()&quot;</tt> or <tt>&quot;&amp;{$subref}()&quot;</tt> constructs, although the <tt>&quot;$subref-&gt;()&quot;</tt> notation solves that problem. See perlref for more about all that. </p>
<p> Subroutines may be called recursively. If a subroutine is called using the <tt>&quot;&amp;&quot;</tt> form, the argument list is optional, and if omitted, no <tt>@_</tt> array is set up for the subroutine: the <tt>@_</tt> array at the time of the call is visible to subroutine instead. This is an efficiency mechanism that new users may wish to avoid. </p>
<p>&amp;foo(1, 2, 3);<br />
#pass three arguments<br />
    foo(1, 2, 3);<br />
#the same<br />
foo();<br />
#pass a null list<br />
    &amp;<br />
    foo();<br />
#the same<br />
    &amp;foo;<br />
#foo() get current args, like foo(@_) !!foo;<br />
#like foo() IFF sub foo predeclared, else &#8220;foo&#8221;</p>
<p> Not only does the <tt>&quot;&amp;&quot;</tt> form make the argument list optional, it also disables any prototype checking on arguments you do provide. This is partly for historical reasons, and partly for having a convenient way to cheat if you know what you&#8217;re doing. See &#8220;Prototypes&#8221; below. </p>
<p> Since Perl 5.16.0, the <tt>&quot;__SUB__&quot;</tt> token is available under <tt>&quot;use feature 'current_sub'&quot;</tt> and <tt>&quot;use 5.16.0&quot;</tt>. It will evaluate to a reference to the currently-running sub, which allows for recursive calls without knowing your subroutine&#8217;s name. </p>
<p>use 5.16.0;<br />
my $factorial = sub<br />
{<br />
    my($x) = @_;<br />
    return 1 if $x == 1;<br />
    return ($x * __SUB__-&gt;($x &#8211; 1));<br />
};</p>
<p> The behavior of <tt>&quot;__SUB__&quot;</tt> within a regex code block (such as <tt>&quot;/(?{...})/&quot;</tt>) is subject to change. </p>
<p> Subroutines whose names are in all upper case are reserved to the Perl core, as are modules whose names are in all lower case. A subroutine in all capitals is a loosely-held convention meaning it will be called indirectly by the run-time system itself, usually due to a triggered event. Subroutines whose name start with a left parenthesis are also reserved the same way. The following is a list of some subroutines that currently do special, pre-defined things.</p>
<dl>
<dt>documented later in this document</p>
<dd> <tt>&quot;AUTOLOAD&quot;</tt></p>
<dt>documented in perlmod</p>
<dd> <tt>&quot;CLONE&quot;</tt>, <tt>&quot;CLONE_SKIP&quot;</tt></p>
<dt>documented in perlobj</p>
<dd> <tt>&quot;DESTROY&quot;</tt>, <tt>&quot;DOES&quot;</tt></p>
<dt>documented in perltie</p>
<dd> <tt>&quot;BINMODE&quot;</tt>, <tt>&quot;CLEAR&quot;</tt>, <tt>&quot;CLOSE&quot;</tt>, <tt>&quot;DELETE&quot;</tt>, <tt>&quot;DESTROY&quot;</tt>, <tt>&quot;EOF&quot;</tt>, <tt>&quot;EXISTS&quot;</tt>, <tt>&quot;EXTEND&quot;</tt>, <tt>&quot;FETCH&quot;</tt>, <tt>&quot;FETCHSIZE&quot;</tt>, <tt>&quot;FILENO&quot;</tt>, <tt>&quot;FIRSTKEY&quot;</tt>, <tt>&quot;GETC&quot;</tt>, <tt>&quot;NEXTKEY&quot;</tt>, <tt>&quot;OPEN&quot;</tt>, <tt>&quot;POP&quot;</tt>, <tt>&quot;PRINT&quot;</tt>, <tt>&quot;PRINTF&quot;</tt>, <tt>&quot;PUSH&quot;</tt>, <tt>&quot;READ&quot;</tt>, <tt>&quot;READLINE&quot;</tt>, <tt>&quot;SCALAR&quot;</tt>, <tt>&quot;SEEK&quot;</tt>, <tt>&quot;SHIFT&quot;</tt>, <tt>&quot;SPLICE&quot;</tt>, <tt>&quot;STORE&quot;</tt>, <tt>&quot;STORESIZE&quot;</tt>, <tt>&quot;TELL&quot;</tt>, <tt>&quot;TIEARRAY&quot;</tt>, <tt>&quot;TIEHANDLE&quot;</tt>, <tt>&quot;TIEHASH&quot;</tt>, <tt>&quot;TIESCALAR&quot;</tt>, <tt>&quot;UNSHIFT&quot;</tt>, <tt>&quot;UNTIE&quot;</tt>, <tt>&quot;WRITE&quot;</tt></p>
<dt>documented in PerlIO::via</p>
<dd> <tt>&quot;BINMODE&quot;</tt>, <tt>&quot;CLEARERR&quot;</tt>, <tt>&quot;CLOSE&quot;</tt>, <tt>&quot;EOF&quot;</tt>, <tt>&quot;ERROR&quot;</tt>, <tt>&quot;FDOPEN&quot;</tt>, <tt>&quot;FILENO&quot;</tt>, <tt>&quot;FILL&quot;</tt>, <tt>&quot;FLUSH&quot;</tt>, <tt>&quot;OPEN&quot;</tt>, <tt>&quot;POPPED&quot;</tt>, <tt>&quot;PUSHED&quot;</tt>, <tt>&quot;READ&quot;</tt>, <tt>&quot;SEEK&quot;</tt>, <tt>&quot;SETLINEBUF&quot;</tt>, <tt>&quot;SYSOPEN&quot;</tt>, <tt>&quot;TELL&quot;</tt>, <tt>&quot;UNREAD&quot;</tt>, <tt>&quot;UTF8&quot;</tt>, <tt>&quot;WRITE&quot;</tt></p>
<dt>documented in perlfunc</p>
<dd> <tt>&quot;import&quot;</tt> , <tt>&quot;unimport&quot;</tt> , <tt>&quot;INC&quot;</tt></p>
<dt>documented in <font SIZE="-1">UNIVERSAL</font></p>
<dd> <tt>&quot;VERSION&quot;</tt></p>
<dt>documented in perldebguts</p>
<dd> <tt>&quot;DB::DB&quot;</tt>, <tt>&quot;DB::sub&quot;</tt>, <tt>&quot;DB::lsub&quot;</tt>, <tt>&quot;DB::goto&quot;</tt>, <tt>&quot;DB::postponed&quot;</tt></p>
<dt>undocumented, used internally by the overload feature</p>
<dd> any starting with <tt>&quot;(&quot;</tt></dl>
<p> The <tt>&quot;BEGIN&quot;</tt>, <tt>&quot;UNITCHECK&quot;</tt>, <tt>&quot;CHECK&quot;</tt>, <tt>&quot;INIT&quot;</tt> and <tt>&quot;END&quot;</tt> subroutines are not so much subroutines as named special code blocks, of which you can have more than one in a package, and which you can <code>not</code> call explicitly. See &#8220;<font SIZE="-1">BEGIN, UNITCHECK, CHECK, INIT</font> and <font SIZE="-1">END&#8221;</font> in perlmod</p>
<h3>Signatures</h3>
<p> <font SIZE="-1"><code>WARNING</code></font>: Subroutine signatures are experimental. The feature may be modified or removed in future versions of Perl. </p>
<p> Perl has an experimental facility to allow a subroutine&#8217;s formal parameters to be introduced by special syntax, separate from the procedural code of the subroutine body. The formal parameter list is known as a <i>signature</i>. The facility must be enabled first by a pragmatic declaration, <tt>&quot;use feature 'signatures'&quot;</tt>, and it will produce a warning unless the &#8220;experimental::signatures&#8221; warnings category is disabled. </p>
<p> The signature is part of a subroutine&#8217;s body. Normally the body of a subroutine is simply a braced block of code, but when using a signature, the signature is a parenthesised list that goes immediately before the block, after any name or attributes. </p>
<p> For example, </p>
<pre>
    sub foo :lvalue ($a, $b = 1, @c) { .... }
</pre>
<p> The signature declares lexical variables that are in scope for the block. When the subroutine is called, the signature takes control first. It populates the signature variables from the list of arguments that were passed. If the argument list doesn&#8217;t meet the requirements of the signature, then it will throw an exception. When the signature processing is complete, control passes to the block. </p>
<p> Positional parameters are handled by simply naming scalar variables in the signature. For example, </p>
<p>sub foo($left, $right)<br />
{<br />
    return $left + $right;<br />
}</p>
<p> takes two positional parameters, which must be filled at runtime by two arguments. By default the parameters are mandatory, and it is not permitted to pass more arguments than expected. So the above is equivalent to </p>
<p>sub foo<br />
{<br />
    die &#8220;Too many arguments for subroutine&#8221; unless @_ &lt;= 2;<br />
    die &#8220;Too few arguments for subroutine&#8221; unless @_ &gt;= 2;<br />
    my $left = $_[0];<br />
    my $right = $_[1];<br />
    return $left + $right;<br />
}</p>
<p> An argument can be ignored by omitting the main part of the name from a parameter declaration, leaving just a bare <tt>&quot;$&quot;</tt> sigil. For example, </p>
<p>sub foo($first, $, $third)<br />
{<br />
    return &#8220;first=$first, third=$third&#8221;;<br />
}</p>
<p> Although the ignored argument doesn&#8217;t go into a variable, it is still mandatory for the caller to pass it. </p>
<p> A positional parameter is made optional by giving a default value, separated from the parameter name by <tt>&quot;=&quot;</tt>: </p>
<p>sub foo($left, $right = 0)<br />
{<br />
    return $left + $right;<br />
}</p>
<p> The above subroutine may be called with either one or two arguments. The default value expression is evaluated when the subroutine is called, so it may provide different default values for different calls. It is only evaluated if the argument was actually omitted from the call. For example, </p>
<p>my $auto_id = 0;<br />
sub foo($thing, $id = $auto_id++)<br />
{<br />
    print &#8220;$thing has ID $id&#8221;;<br />
}</p>
<p> automatically assigns distinct sequential IDs to things for which no <font SIZE="-1">ID</font> was supplied by the caller. A default value expression may also refer to parameters earlier in the signature, making the default for one parameter vary according to the earlier parameters. For example, </p>
<pre>
    sub foo ($first_name, $surname, $nickname = $first_name) {
        print &quot;$first_name $surname is known as \&quot;$nickname\&quot;&quot;;
    }
</pre>
<p> An optional parameter can be nameless just like a mandatory parameter. For example, </p>
<pre>
    sub foo ($thing, $ = 1) {
        print $thing;
    }
</pre>
<p> The parameter&#8217;s default value will still be evaluated if the corresponding argument isn&#8217;t supplied, even though the value won&#8217;t be stored anywhere. This is in case evaluating it has important side effects. However, it will be evaluated in void context, so if it doesn&#8217;t have side effects and is not trivial it will generate a warning if the &#8220;void&#8221; warning category is enabled. If a nameless optional parameter&#8217;s default value is not important, it may be omitted just as the parameter&#8217;s name was: </p>
<pre>
    sub foo ($thing, $=) {
        print $thing;
    }
</pre>
<p> Optional positional parameters must come after all mandatory positional parameters. (If there are no mandatory positional parameters then an optional positional parameters can be the first thing in the signature.) If there are multiple optional positional parameters and not enough arguments are supplied to fill them all, they will be filled from left to right. </p>
<p> After positional parameters, additional arguments may be captured in a slurpy parameter. The simplest form of this is just an array variable: </p>
<p>sub foo($filter, @inputs)<br />
{<br />
    print $filter-&gt;($_)foreach @inputs;<br />
}</p>
<p> With a slurpy parameter in the signature, there is no upper limit on how many arguments may be passed. A slurpy array parameter may be nameless just like a positional parameter, in which case its only effect is to turn off the argument limit that would otherwise apply: </p>
<pre>
    sub foo ($thing, @) {
        print $thing;
    }
</pre>
<p> A slurpy parameter may instead be a hash, in which case the arguments available to it are interpreted as alternating keys and values. There must be as many keys as values: if there is an odd argument then an exception will be thrown. Keys will be stringified, and if there are duplicates then the later instance takes precedence over the earlier, as with standard hash construction. </p>
<p>sub foo($filter, % inputs)<br />
{<br />
    print $filter-&gt;($_, $inputs{$_})foreach sort keys % inputs;<br />
}</p>
<p> A slurpy hash parameter may be nameless just like other kinds of parameter. It still insists that the number of arguments available to it be even, even though they&#8217;re not being put into a variable. </p>
<pre>
    sub foo ($thing, %) {
        print $thing;
    }
</pre>
<p> A slurpy parameter, either array or hash, must be the last thing in the signature. It may follow mandatory and optional positional parameters; it may also be the only thing in the signature. Slurpy parameters cannot have default values: if no arguments are supplied for them then you get an empty array or empty hash. </p>
<p> A signature may be entirely empty, in which case all it does is check that the caller passed no arguments: </p>
<p>sub foo()<br />
{<br />
    return 123;<br />
}</p>
<p> When using a signature, the arguments are still available in the special array variable <tt>@_</tt>, in addition to the lexical variables of the signature. There is a difference between the two ways of accessing the arguments: <tt>@_</tt> <i>aliases</i> the arguments, but the signature variables get <i>copies</i> of the arguments. So writing to a signature variable only changes that variable, and has no effect on the caller&#8217;s variables, but writing to an element of <tt>@_</tt> modifies whatever the caller used to supply that argument. </p>
<p> There is a potential syntactic ambiguity between signatures and prototypes (see &#8220;Prototypes&#8221;), because both start with an opening parenthesis and both can appear in some of the same places, such as just after the name in a subroutine declaration. For historical reasons, when signatures are not enabled, any opening parenthesis in such a context will trigger very forgiving prototype parsing. Most signatures will be interpreted as prototypes in those circumstances, but won&#8217;t be valid prototypes. (A valid prototype cannot contain any alphabetic character.) This will lead to somewhat confusing error messages. </p>
<p> To avoid ambiguity, when signatures are enabled the special syntax for prototypes is disabled. There is no attempt to guess whether a parenthesised group was intended to be a prototype or a signature. To give a subroutine a prototype under these circumstances, use a prototype attribute. For example, </p>
<p>sub foo : prototype($)<br />
{<br />
    $_[0]<br />
}</p>
<p> It is entirely possible for a subroutine to have both a prototype and a signature. They do different jobs: the prototype affects compilation of calls to the subroutine, and the signature puts argument values into lexical variables at runtime. You can therefore write </p>
<p>sub foo : prototype($$)($left, $right)<br />
{<br />
    return $left + $right;<br />
}</p>
<p> The prototype attribute, and any other attributes, must come before the signature. The signature always immediately precedes the block of the subroutine&#8217;s body.</p>
<h3>Private Variables via <code>my()</code></h3>
<p> Synopsis: </p>
<p>my $foo;<br />
#declare $foo lexically local<br />
    my(@wid, % get);<br />
#declare list of variables local<br />
    my $foo = &#8220;flurp&#8221;;<br />
#declare $foo lexical, and init it<br />
                           my @oof = @bar;<br />
#declare @oof lexical, and init it<br />
                           my $x : Foo = $y;<br />
#similar, with an attribute applied</p>
<p> <font SIZE="-1"><code>WARNING</code></font>: The use of attribute lists on <tt>&quot;my&quot;</tt> declarations is still evolving. The current semantics and interface are subject to change. See attributes and Attribute::Handlers. </p>
<p> The <tt>&quot;my&quot;</tt> operator declares the listed variables to be lexically confined to the enclosing block, conditional (<tt>&quot;if&quot;</tt>/<tt>&quot;unless&quot;</tt>/<tt>&quot;elsif&quot;</tt>/<tt>&quot;else&quot;</tt>), loop (<tt>&quot;for&quot;</tt>/<tt>&quot;foreach&quot;</tt>/<tt>&quot;while&quot;</tt>/<tt>&quot;until&quot;</tt>/<tt>&quot;continue&quot;</tt>), subroutine, <tt>&quot;eval&quot;</tt>, or <tt>&quot;do&quot;</tt>/<tt>&quot;require&quot;</tt>/<tt>&quot;use&quot;</tt>&#8216;d file. If more than one value is listed, the list must be placed in parentheses. All listed elements must be legal lvalues. Only alphanumeric identifiers may be lexically scoped&#8212;magical built-ins like <tt>$/</tt> must currently be <tt>&quot;local&quot;</tt>ized with <tt>&quot;local&quot;</tt> instead. </p>
<p> Unlike dynamic variables created by the <tt>&quot;local&quot;</tt> operator, lexical variables declared with <tt>&quot;my&quot;</tt> are totally hidden from the outside world, including any called subroutines. This is true if it&#8217;s the same subroutine called from itself or elsewhere&#8212;every call gets its own copy. </p>
<p> This doesn&#8217;t mean that a <tt>&quot;my&quot;</tt> variable declared in a statically enclosing lexical scope would be invisible. Only dynamic scopes are cut off. For example, the <tt>&quot;bumpx()&quot;</tt> function below has access to the lexical <tt>$x</tt> variable because both the <tt>&quot;my&quot;</tt> and the <tt>&quot;sub&quot;</tt> occurred at the same scope, presumably file scope. </p>
<p>my $x = 10;<br />
sub bumpx<br />
{<br />
    $x++<br />
}</p>
<p> An <tt>&quot;eval()&quot;</tt>, however, can see lexical variables of the scope it is being evaluated in, so long as the names aren&#8217;t hidden by declarations within the <tt>&quot;eval()&quot;</tt> itself. See perlref. </p>
<p> The parameter list to <code>my()</code> may be assigned to if desired, which allows you to initialize your variables. (If no initializer is given for a particular variable, it is created with the undefined value.) Commonly this is used to name input parameters to a subroutine. Examples: </p>
<p>$arg = &#8220;fred&#8221;;<br />
#&#8221;global&#8221; variable $n = cube_root(27);<br />
print &#8220;$arg thinks the root is $n
&#8221;;<br />
fred thinks the root is 3 sub cube_root<br />
{<br />
    my $arg = shift;<br />
#name doesn&#8217;t matter $arg * *= 1 / 3;<br />
    return $arg;<br />
}</p>
<p> The <tt>&quot;my&quot;</tt> is simply a modifier on something you might assign to. So when you do assign to variables in its argument list, <tt>&quot;my&quot;</tt> doesn&#8217;t change whether those variables are viewed as a scalar or an array. So </p>
<pre>
    my ($foo) = &lt;STDIN&gt;;                # WRONG?
    my @FOO = &lt;STDIN&gt;;
</pre>
<p> both supply a list context to the right-hand side, while </p>
<pre>
    my $foo = &lt;STDIN&gt;;
</pre>
<p> supplies a scalar context. But the following declares only one variable: </p>
<pre>
    my $foo, $bar = 1;                  # WRONG
</pre>
<p> That has the same effect as </p>
<pre>
    my $foo;
    $bar = 1;
</pre>
<p> The declared variable is not introduced (is not visible) until after the current statement. Thus, </p>
<pre>
    my $x = $x;
</pre>
<p> can be used to initialize a new <tt>$x</tt> with the value of the old <tt>$x</tt>, and the expression </p>
<pre>
    my $x = 123 and $x == 123
</pre>
<p> is false unless the old <tt>$x</tt> happened to have the value <tt>123</tt>. </p>
<p> Lexical scopes of control structures are not bounded precisely by the braces that delimit their controlled blocks; control expressions are part of that scope, too. Thus in the loop </p>
<p>while (my $line = &lt;&gt;) {<br />
    $line = lc $line;<br />
}<br />
continue<br />
{<br />
    print $line;<br />
}</p>
<p> the scope of <tt>$line</tt> extends from its declaration throughout the rest of the loop construct (including the <tt>&quot;continue&quot;</tt> clause), but not beyond it. Similarly, in the conditional </p>
<p>if ((my $answer = &lt;STDIN&gt;) = ~ / ^yes$ / i) {<br />
    user_agrees();<br />
}<br />
elsif($answer = ~ / ^no$ / i)<br />
{<br />
    user_disagrees();<br />
}<br />
else<br />
{<br />
    chomp $answer;<br />
    die &#8220;&#8216;$answer&#8217; is neither &#8216;yes&#8217; nor &#8216;no'&#8221;;<br />
}</p>
<p> the scope of <tt>$answer</tt> extends from its declaration through the rest of that conditional, including any <tt>&quot;elsif&quot;</tt> and <tt>&quot;else&quot;</tt> clauses, but not beyond it. See &#8220;Simple Statements&#8221; in perlsyn for information on the scope of variables in statements with modifiers. </p>
<p> The <tt>&quot;foreach&quot;</tt> loop defaults to scoping its index variable dynamically in the manner of <tt>&quot;local&quot;</tt>. However, if the index variable is prefixed with the keyword <tt>&quot;my&quot;</tt>, or if there is already a lexical by that name in scope, then a new lexical is created instead. Thus in the loop </p>
<p>    for<br />
        my $i(1, 2, 3)<br />
        {<br />
            some_function();<br />
        }</p>
<p> the scope of <tt>$i</tt> extends to the end of the loop, but not beyond it, rendering the value of <tt>$i</tt> inaccessible within <tt>&quot;some_function()&quot;</tt>. </p>
<p> Some users may wish to encourage the use of lexically scoped variables. As an aid to catching implicit uses to package variables, which are always global, if you say </p>
<pre>
    use strict 'vars';
</pre>
<p> then any variable mentioned from there to the end of the enclosing block must either refer to a lexical variable, be predeclared via <tt>&quot;our&quot;</tt> or <tt>&quot;use vars&quot;</tt>, or else must be fully qualified with the package name. A compilation error results otherwise. An inner block may countermand this with <tt>&quot;no strict 'vars'&quot;</tt>. </p>
<p> A <tt>&quot;my&quot;</tt> has both a compile-time and a run-time effect. At compile time, the compiler takes notice of it. The principal usefulness of this is to quiet <tt>&quot;use strict 'vars'&quot;</tt>, but it is also essential for generation of closures as detailed in perlref. Actual initialization is delayed until run time, though, so it gets executed at the appropriate time, such as each time through a loop, for example. </p>
<p> Variables declared with <tt>&quot;my&quot;</tt> are not part of any package and are therefore never fully qualified with the package name. In particular, you&#8217;re not allowed to try to make a package variable (or other global) lexical: </p>
<pre>
    my $pack::var;      # ERROR!  Illegal syntax
</pre>
<p> In fact, a dynamic variable (also known as package or global variables) are still accessible using the fully qualified <tt>&quot;::&quot;</tt> notation even while a lexical of the same name is also visible: </p>
<p>package main;<br />
local $x = 10;<br />
my $x = 20;<br />
print &#8220;$x and $::x
&#8221;;</p>
<p> That will print out <tt>20</tt> and <tt>10</tt>. </p>
<p> You may declare <tt>&quot;my&quot;</tt> variables at the outermost scope of a file to hide any such identifiers from the world outside that file. This is similar in spirit to C&#8217;s static variables when they are used at the file level. To do this with a subroutine requires the use of a closure (an anonymous function that accesses enclosing lexicals). If you want to create a private subroutine that cannot be called from outside that block, it can declare a lexical variable containing an anonymous sub reference: </p>
<p>my $secret_version = &#8216;1.001-beta&#8217;;<br />
my $secret_sub = sub{print $secret_version};<br />
&amp;$secret_sub();</p>
<p> As long as the reference is never returned by any function within the module, no outside module can see the subroutine, because its name is not in any package&#8217;s symbol table. Remember that it&#8217;s not <i></i><font SIZE="-1"><i>REALLY</i></font><i></i> called <tt>$some_pack::secret_version</tt> or anything; it&#8217;s just <tt>$secret_version</tt>, unqualified and unqualifiable. </p>
<p> This does not work with object methods, however; all object methods have to be in the symbol table of some package to be found. See &#8220;Function Templates&#8221; in perlref for something of a work-around to this.</p>
<h3>Persistent Private Variables</h3>
<p> There are two ways to build persistent private variables in Perl 5.10. First, you can simply use the <tt>&quot;state&quot;</tt> feature. Or, you can use closures, if you want to stay compatible with releases older than 5.10. </p>
<p> <i>Persistent variables via </i>state()<i></i> </p>
<p> Beginning with Perl 5.10.0, you can declare variables with the <tt>&quot;state&quot;</tt> keyword in place of <tt>&quot;my&quot;</tt>. For that to work, though, you must have enabled that feature beforehand, either by using the <tt>&quot;feature&quot;</tt> pragma, or by using <tt>&quot;-E&quot;</tt> on one-liners (see feature). Beginning with Perl 5.16, the <tt>&quot;CORE::state&quot;</tt> form does not require the <tt>&quot;feature&quot;</tt> pragma. </p>
<p> The <tt>&quot;state&quot;</tt> keyword creates a lexical variable (following the same scoping rules as <tt>&quot;my&quot;</tt>) that persists from one subroutine call to the next. If a state variable resides inside an anonymous subroutine, then each copy of the subroutine has its own copy of the state variable. However, the value of the state variable will still persist between calls to the same copy of the anonymous subroutine. (Don&#8217;t forget that <tt>&quot;sub { ... }&quot;</tt> creates a new subroutine each time it is executed.) </p>
<p> For example, the following code maintains a private counter, incremented each time the <code>gimme_another()</code> function is called: </p>
<p>use feature &#8216;state&#8217;;<br />
sub gimme_another<br />
{<br />
    state $x;<br />
    return ++$x<br />
}</p>
<p> And this example uses anonymous subroutines to create separate counters: </p>
<p>use feature &#8216;state&#8217;;<br />
sub create_counter<br />
{<br />
    return sub<br />
    {<br />
        state $x;<br />
        return ++$x<br />
    }<br />
}</p>
<p> Also, since <tt>$x</tt> is lexical, it can&#8217;t be reached or modified by any Perl code outside. </p>
<p> When combined with variable declaration, simple assignment to <tt>&quot;state&quot;</tt> variables (as in <tt>&quot;state $x = 42&quot;</tt>) is executed only the first time. When such statements are evaluated subsequent times, the assignment is ignored. The behavior of assignment to <tt>&quot;state&quot;</tt> declarations where the left hand side of the assignment involves any parentheses is currently undefined. </p>
<p> <i>Persistent variables with closures</i> </p>
<p> Just because a lexical variable is lexically (also called statically) scoped to its enclosing block, <tt>&quot;eval&quot;</tt>, or <tt>&quot;do&quot;</tt> <font SIZE="-1">FILE,</font> this doesn&#8217;t mean that within a function it works like a C static. It normally works more like a C auto, but with implicit garbage collection. </p>
<p> Unlike local variables in C or C<font SIZE="-2">++</font>, Perl&#8217;s lexical variables don&#8217;t necessarily get recycled just because their scope has exited. If something more permanent is still aware of the lexical, it will stick around. So long as something else references a lexical, that lexical won&#8217;t be freed&#8212;which is as it should be. You wouldn&#8217;t want memory being free until you were done using it, or kept around once you were done. Automatic garbage collection takes care of this for you. </p>
<p> This means that you can pass back or save away references to lexical variables, whereas to return a pointer to a C auto is a grave error. It also gives us a way to simulate C&#8217;s function statics. Here&#8217;s a mechanism for giving a function private variables with both lexical scoping and a static lifetime. If you do want to create something like C&#8217;s static variables, just enclose the whole function in an extra block, and put the static variable outside the function but in the block. </p>
<p>{<br />
    my $secret_val = 0;<br />
    sub gimme_another<br />
    {<br />
        return ++$secret_val;<br />
    }<br />
}<br />
#$secret_val now becomes unreachable by the outside<br />
#world, but retains its value between calls to gimme_another</p>
<p> If this function is being sourced in from a separate file via <tt>&quot;require&quot;</tt> or <tt>&quot;use&quot;</tt>, then this is probably just fine. If it&#8217;s all in the main program, you&#8217;ll need to arrange for the <tt>&quot;my&quot;</tt> to be executed early, either by putting the whole block above your main program, or more likely, placing merely a <tt>&quot;BEGIN&quot;</tt> code block around it to make sure it gets executed before your program starts to run: </p>
<p>BEGIN<br />
{<br />
    my $secret_val = 0;<br />
    sub gimme_another<br />
    {<br />
        return ++$secret_val;<br />
    }<br />
}</p>
<p> See &#8220;<font SIZE="-1">BEGIN, UNITCHECK, CHECK, INIT</font> and <font SIZE="-1">END&#8221;</font> in perlmod about the special triggered code blocks, <tt>&quot;BEGIN&quot;</tt>, <tt>&quot;UNITCHECK&quot;</tt>, <tt>&quot;CHECK&quot;</tt>, <tt>&quot;INIT&quot;</tt> and <tt>&quot;END&quot;</tt>. </p>
<p> If declared at the outermost scope (the file scope), then lexicals work somewhat like C&#8217;s file statics. They are available to all functions in that same file declared below them, but are inaccessible from outside that file. This strategy is sometimes used in modules to create private variables that the whole module can see.</p>
<h3>Temporary Values via <code>local()</code></h3>
<p> <font SIZE="-1"><code>WARNING</code></font>: In general, you should be using <tt>&quot;my&quot;</tt> instead of <tt>&quot;local&quot;</tt>, because it&#8217;s faster and safer. Exceptions to this include the global punctuation variables, global filehandles and formats, and direct manipulation of the Perl symbol table itself. <tt>&quot;local&quot;</tt> is mostly used when the current value of a variable must be visible to called subroutines. </p>
<p> Synopsis: </p>
<p>#localization of values<br />
local $foo;<br />
#make $foo dynamically local<br />
    local(@wid, % get);<br />
#make list of variables local<br />
    local $foo = &#8220;flurp&#8221;;<br />
#make $foo dynamic, and init it<br />
                        local @oof = @bar;<br />
#make @oof dynamic, and init it<br />
                        local $hash{key } = &#8220;val&#8221;;<br />
#sets a local value for this hash entry delete local $hash{key };<br />
#delete this entry for the current block<br />
    local($cond ? $v1 : $v2);<br />
#several types of lvalues support<br />
#localization<br />
#localization of symbols<br />
    local *FH;<br />
#localize $FH, @FH, % FH, &amp;FH&#8230; local *merlyn = *randal;<br />
#now $merlyn is really $randal, plus<br />
#@merlyn is really @randal, etc<br />
                                    local *merlyn = &#8216;randal&#8217;;<br />
#SAME THING : promote &#8216;randal&#8217; to *randal<br />
    local *merlyn = \$randal;<br />
#just alias $merlyn, not @merlyn etc</p>
<p> A <tt>&quot;local&quot;</tt> modifies its listed variables to be &#8220;local&#8221; to the enclosing block, <tt>&quot;eval&quot;</tt>, or <tt>&quot;do FILE&quot;</tt>&#8211;and to <i>any subroutine called from within that block</i>. A <tt>&quot;local&quot;</tt> just gives temporary values to global (meaning package) variables. It does <i>not</i> create a local variable. This is known as dynamic scoping. Lexical scoping is done with <tt>&quot;my&quot;</tt>, which works more like C&#8217;s auto declarations. </p>
<p> Some types of lvalues can be localized as well: hash and array elements and slices, conditionals (provided that their result is always localizable), and symbolic references. As for simple variables, this creates new, dynamically scoped values. </p>
<p> If more than one variable or expression is given to <tt>&quot;local&quot;</tt>, they must be placed in parentheses. This operator works by saving the current values of those variables in its argument list on a hidden stack and restoring them upon exiting the block, subroutine, or eval. This means that called subroutines can also reference the local variable, but not the global one. The argument list may be assigned to if desired, which allows you to initialize your local variables. (If no initializer is given for a particular variable, it is created with an undefined value.) </p>
<p> Because <tt>&quot;local&quot;</tt> is a run-time operator, it gets executed each time through a loop. Consequently, it&#8217;s more efficient to localize your variables outside the loop. </p>
<p> <i>Grammatical note on </i>local()<i></i> </p>
<p> A <tt>&quot;local&quot;</tt> is simply a modifier on an lvalue expression. When you assign to a <tt>&quot;local&quot;</tt>ized variable, the <tt>&quot;local&quot;</tt> doesn&#8217;t change whether its list is viewed as a scalar or an array. So </p>
<pre>
    local($foo) = &lt;STDIN&gt;;
    local @FOO = &lt;STDIN&gt;;
</pre>
<p> both supply a list context to the right-hand side, while </p>
<pre>
    local $foo = &lt;STDIN&gt;;
</pre>
<p> supplies a scalar context. </p>
<p> <i>Localization of special variables</i> </p>
<p> If you localize a special variable, you&#8217;ll be giving a new value to it, but its magic won&#8217;t go away. That means that all side-effects related to this magic still work with the localized value. </p>
<p> This feature allows code like this to work : </p>
<p>#Read the whole contents of FILE in $slurp<br />
{<br />
    local $ / = undef;<br />
    $slurp = &lt;FILE&gt;;<br />
}</p>
<p> Note, however, that this restricts localization of some values ; for example, the following statement dies, as of perl 5.10.0, with an error <i>Modification of a read-only value attempted</i>, because the <tt>$1</tt> variable is magical and read-only : </p>
<pre>
    local $1 = 2;
</pre>
<p> One exception is the default scalar variable: starting with perl 5.14 <tt>&quot;local($_)&quot;</tt> will always strip all magic from <tt>$_</tt>, to make it possible to safely reuse <tt>$_</tt> in a subroutine. </p>
<p> <font SIZE="-1"><code>WARNING</code></font>: Localization of tied arrays and hashes does not currently work as described. This will be fixed in a future release of Perl; in the meantime, avoid code that relies on any particular behavior of localising tied arrays or hashes (localising individual elements is still okay). See &#8220;Localising Tied Arrays and Hashes Is Broken&#8221; in perl58delta for more details. </p>
<p> <i>Localization of globs</i> </p>
<p> The construct </p>
<pre>
    local *name;
</pre>
<p> creates a whole new symbol table entry for the glob <tt>&quot;name&quot;</tt> in the current package. That means that all variables in its glob slot ($name, <tt>@name</tt>, <tt>%name</tt>, &amp;name, and the <tt>&quot;name&quot;</tt> filehandle) are dynamically reset. </p>
<p> This implies, among other things, that any magic eventually carried by those variables is locally lost. In other words, saying <tt>&quot;local */&quot;</tt> will not have any effect on the internal value of the input record separator. </p>
<p> <i>Localization of elements of composite types</i> </p>
<p> It&#8217;s also worth taking a moment to explain what happens when you <tt>&quot;local&quot;</tt>ize a member of a composite type (i.e. an array or hash element). In this case, the element is <tt>&quot;local&quot;</tt>ized <i>by name</i>. This means that when the scope of the <tt>&quot;local()&quot;</tt> ends, the saved value will be restored to the hash element whose key was named in the <tt>&quot;local()&quot;</tt>, or the array element whose index was named in the <tt>&quot;local()&quot;</tt>. If that element was deleted while the <tt>&quot;local()&quot;</tt> was in effect (e.g. by a <tt>&quot;delete()&quot;</tt> from a hash or a <tt>&quot;shift()&quot;</tt> of an array), it will spring back into existence, possibly extending an array and filling in the skipped elements with <tt>&quot;undef&quot;</tt>. For instance, if you say </p>
<p>% hash = (&#8216;This&#8217; = &gt; &#8216;is&#8217;, &#8216;a&#8217; = &gt; &#8216;test&#8217;);<br />
@ary = (0..5);<br />
{<br />
    local($ary[5]) = 6;<br />
    local($hash{&#8216;a&#8217;}) = &#8216;drill&#8217;;<br />
    while (my $e = pop(@ary)) {<br />
        print &#8220;$e . . .
&#8221;;<br />
        last unless $e &gt; 3;<br />
    }<br />
    if (@ary) {<br />
        $hash{&#8216;only a&#8217;} = &#8216;test&#8217;;<br />
        delete $hash{&#8216;a&#8217;};<br />
    }<br />
}<br />
print join(&#8216; &#8216;, map{&#8220;$_ $hash{$_}&#8221;} sort keys % hash), &#8220;.
&#8221;;<br />
print &#8220;The array has &#8220;, scalar(@ary), &#8221; elements: &#8220;,<br />
    join(<br />
        &#8216;, &#8216;, map { defined $_ ? $_ : &#8216;undef&#8217; } @ary),<br />
    &#8220;
&#8221;;</p>
<p> Perl will print </p>
<pre>
    6 . . .
    4 . . .
    3 . . .
    This is a test only a test.
    The array has 6 elements: 0, 1, 2, undef, undef, 5
</pre>
<p> The behavior of <code>local()</code> on non-existent members of composite types is subject to change in future. The behavior of <code>local()</code> on array elements specified using negative indexes is particularly surprising, and is very likely to change. </p>
<p> <i>Localized deletion of elements of composite types</i> </p>
<p> You can use the <tt>&quot;delete local $array[$idx]&quot;</tt> and <tt>&quot;delete local $hash{key}&quot;</tt> constructs to delete a composite type entry for the current block and restore it when it ends. They return the array/hash value before the localization, which means that they are respectively equivalent to </p>
<p>do {<br />
    my $val = $array[$idx];<br />
    local $array[$idx];<br />
    delete $array[$idx];<br />
    $val<br />
}</p>
<p> and </p>
<p>do {<br />
    my $val = $hash{key};<br />
    local $hash{key};<br />
    delete $hash{key};<br />
    $val<br />
}</p>
<p> except that for those the <tt>&quot;local&quot;</tt> is scoped to the <tt>&quot;do&quot;</tt> block. Slices are also accepted. </p>
<p>my % hash = (a = &gt; [ 7, 8, 9 ],<br />
             b = &gt; 1, )<br />
{<br />
    my $a = delete local $hash{a};<br />
#$a is[7, 8, 9]<br />
#% hash is(b =&gt; 1)<br />
    {<br />
        my @nums = delete local @$a[0, 2]<br />
#@nums is(7, 9)<br />
#$a is[undef, 8]<br />
            $a[0] = 999;<br />
#will be erased when the scope ends<br />
    }<br />
#$a is back to[7, 8, 9]<br />
}<br />
#% hash is back to its original state</p>
<h3>Lvalue subroutines</h3>
<p> It is possible to return a modifiable value from a subroutine. To do this, you have to declare the subroutine to return an lvalue. </p>
<p>my $val;<br />
sub canmod : lvalue<br />
{<br />
    $val;<br />
# or : return $val;<br />
}<br />
sub nomod<br />
{<br />
    $val;<br />
}<br />
canmod() = 5;<br />
#assigns to $val<br />
nomod() = 5;<br />
#ERROR</p>
<p> The scalar/list context for the subroutine and for the right-hand side of assignment is determined as if the subroutine call is replaced by a scalar. For example, consider: </p>
<pre>
    data(2,3) = get_data(3,4);
</pre>
<p> Both subroutines here are called in a scalar context, while in: </p>
<pre>
    (data(2,3)) = get_data(3,4);
</pre>
<p> and in: </p>
<pre>
    (<a href="//www.systutorials.com/docs/linux/man/2-data/">data</a>(2),<a href="//www.systutorials.com/docs/linux/man/3-data/">data</a>(3)) = get_data(3,4);
</pre>
<p> all the subroutines are called in a list context. </p>
<p> Lvalue subroutines are convenient, but you have to keep in mind that, when used with objects, they may violate encapsulation. A normal mutator can check the supplied argument before setting the attribute it is protecting, an lvalue subroutine cannot. If you require any special processing when storing and retrieving the values, consider using the <font SIZE="-1">CPAN</font> module Sentinel or something similar.</p>
<h3>Lexical Subroutines</h3>
<p> Beginning with Perl 5.18, you can declare a private subroutine with <tt>&quot;my&quot;</tt> or <tt>&quot;state&quot;</tt>. As with state variables, the <tt>&quot;state&quot;</tt> keyword is only available under <tt>&quot;use feature 'state'&quot;</tt> or <tt>&quot;use 5.010&quot;</tt> or higher. </p>
<p> Prior to Perl 5.26, lexical subroutines were deemed experimental and were available only under the <tt>&quot;use feature 'lexical_subs'&quot;</tt> pragma. They also produced a warning unless the &#8220;experimental::lexical_subs&#8221; warnings category was disabled. </p>
<p> These subroutines are only visible within the block in which they are declared, and only after that declaration: </p>
<p>#Include these two lines if your code is intended to run under Perl<br />
#versions earlier than 5.26.<br />
no warnings &#8220;experimental::lexical_subs&#8221;;<br />
use feature &#8216;lexical_subs&#8217;;<br />
foo();<br />
#calls the package / global subroutine<br />
                         state sub foo<br />
{<br />
    foo();<br />
#also calls the package subroutine<br />
}<br />
foo();<br />
#calls &#8220;state&#8221; sub<br />
    my $ref = \&amp; foo;<br />
#take a reference to &#8220;state&#8221; sub<br />
    my sub bar{&#8230; } bar();<br />
#calls &#8220;my&#8221; sub</p>
<p> You can&#8217;t (directly) write a recursive lexical subroutine: </p>
<p>#WRONG<br />
my sub baz<br />
{<br />
    baz();<br />
}</p>
<p> This example fails because <tt>&quot;baz()&quot;</tt> refers to the package/global subroutine <tt>&quot;baz&quot;</tt>, not the lexical subroutine currently being defined. </p>
<p> The solution is to use <tt>&quot;__SUB__&quot;</tt>: </p>
<p>my sub baz<br />
{<br />
    __SUB__-&gt;();<br />
#calls itself<br />
}</p>
<p> It is possible to predeclare a lexical subroutine. The <tt>&quot;sub foo {...}&quot;</tt> subroutine definition syntax respects any previous <tt>&quot;my sub;&quot;</tt> or <tt>&quot;state sub;&quot;</tt> declaration. Using this to define recursive subroutines is a bad idea, however: </p>
<p>my sub baz;<br />
#predeclaration sub baz<br />
{<br />
#define the &#8220;my&#8221; sub<br />
    baz();<br />
#WRONG : calls itself, but leaks memory<br />
}</p>
<p> Just like <tt>&quot;my $f; $f = sub { $f-&gt;() }&quot;</tt>, this example leaks memory. The name <tt>&quot;baz&quot;</tt> is a reference to the subroutine, and the subroutine uses the name <tt>&quot;baz&quot;</tt>; they keep each other alive (see &#8220;Circular References&#8221; in perlref). </p>
<p> <i></i>&quot;state sub&quot;<i> vs </i>&quot;my sub&quot;<i></i> </p>
<p> What is the difference between &#8220;state&#8221; subs and &#8220;my&#8221; subs? Each time that execution enters a block when &#8220;my&#8221; subs are declared, a new copy of each sub is created. &#8220;State&#8221; subroutines persist from one execution of the containing block to the next. </p>
<p> So, in general, &#8220;state&#8221; subroutines are faster. But &#8220;my&#8221; subs are necessary if you want to create closures: </p>
<p>sub whatever<br />
{<br />
    my $x = shift;<br />
    my sub inner{<br />
        &#8230; do something with $x&#8230;} inner();<br />
}</p>
<p> In this example, a new <tt>$x</tt> is created when <tt>&quot;whatever&quot;</tt> is called, and also a new <tt>&quot;inner&quot;</tt>, which can see the new <tt>$x</tt>. A &#8220;state&#8221; sub will only see the <tt>$x</tt> from the first call to <tt>&quot;whatever&quot;</tt>. </p>
<p> <i></i>&quot;our&quot;<i> subroutines</i> </p>
<p> Like <tt>&quot;our $variable&quot;</tt>, <tt>&quot;our sub&quot;</tt> creates a lexical alias to the package subroutine of the same name. </p>
<p> The two main uses for this are to switch back to using the package sub inside an inner scope: </p>
<p>sub foo{&#8230;} sub bar<br />
{<br />
    my sub foo{&#8230;}<br />
    {<br />
#need to use the outer foo here<br />
        our sub foo;<br />
        foo();<br />
    }<br />
}</p>
<p> and to make a subroutine visible to other packages in the same scope: </p>
<p>package MySneakyModule;<br />
our sub do_something{&#8230;} sub do_something_with_caller<br />
{<br />
    package DB;<br />
    () = caller 1;<br />
#sets @DB::args<br />
        do_something(@args);<br />
#uses MySneakyModule::do_something<br />
}</p>
<h3>Passing Symbol Table Entries (typeglobs)</h3>
<p> <font SIZE="-1"><code>WARNING</code></font>: The mechanism described in this section was originally the only way to simulate pass-by-reference in older versions of Perl. While it still works fine in modern versions, the new reference mechanism is generally easier to work with. See below. </p>
<p> Sometimes you don&#8217;t want to pass the value of an array to a subroutine but rather the name of it, so that the subroutine can modify the global copy of it rather than working with a local copy. In perl you can refer to all objects of a particular name by prefixing the name with a star: <tt>*foo</tt>. This is often known as a &#8220;typeglob&#8221;, because the star on the front can be thought of as a wildcard match for all the funny prefix characters on variables and subroutines and such. </p>
<p> When evaluated, the typeglob produces a scalar value that represents all the objects of that name, including any filehandle, format, or subroutine. When assigned to, it causes the name mentioned to refer to whatever <tt>&quot;*&quot;</tt> value was assigned to it. Example: </p>
<p>sub doubleary<br />
{<br />
    local(*someary) = @_;<br />
    foreach<br />
        $elem(@someary)<br />
        {<br />
            $elem *= 2;<br />
        }<br />
}<br />
doubleary(*foo);<br />
doubleary(*bar);</p>
<p> Scalars are already passed by reference, so you can modify scalar arguments without using this mechanism by referring explicitly to <tt>$_[0]</tt> etc. You can modify all the elements of an array by passing all the elements as scalars, but you have to use the <tt>&quot;*&quot;</tt> mechanism (or the equivalent reference mechanism) to <tt>&quot;push&quot;</tt>, <tt>&quot;pop&quot;</tt>, or change the size of an array. It will certainly be faster to pass the typeglob (or reference). </p>
<p> Even if you don&#8217;t want to modify an array, this mechanism is useful for passing multiple arrays in a single <font SIZE="-1">LIST,</font> because normally the <font SIZE="-1">LIST</font> mechanism will merge all the array values so that you can&#8217;t extract out the individual arrays. For more on typeglobs, see &#8220;Typeglobs and Filehandles&#8221; in perldata.</p>
<h3>When to Still Use <code>local()</code></h3>
<p> Despite the existence of <tt>&quot;my&quot;</tt>, there are still three places where the <tt>&quot;local&quot;</tt> operator still shines. In fact, in these three places, you <i>must</i> use <tt>&quot;local&quot;</tt> instead of <tt>&quot;my&quot;</tt>.</p>
<dl>
<dt>1.</p>
<dd> You need to give a global variable a temporary value, especially <tt>$_</tt>. </p>
<p> The global variables, like <tt>@ARGV</tt> or the punctuation variables, must be <tt>&quot;local&quot;</tt>ized with <tt>&quot;local()&quot;</tt>. This block reads in <i>/etc/motd</i>, and splits it up into chunks separated by lines of equal signs, which are placed in <tt>@Fields</tt>. </p>
<p>{<br />
    local @ARGV = (&#8220;/etc/motd&#8221;);<br />
    local $ / = undef;<br />
    local $_ = &lt;&gt;;<br />
    @Fields = split / ^\s *= +\s *$ / ;<br />
}</p>
<p> It particular, it&#8217;s important to <tt>&quot;local&quot;</tt>ize <tt>$_</tt> in any routine that assigns to it. Look out for implicit assignments in <tt>&quot;while&quot;</tt> conditionals.</p>
<dt>2.</p>
<dd> You need to create a local file or directory handle or a local function. </p>
<p> A function that needs a filehandle of its own must use <tt>&quot;local()&quot;</tt> on a complete typeglob. This can be used to create new symbol table entries: </p>
<p>sub ioqueue<br />
{<br />
    local(*READER, *WRITER);<br />
#not my !pipe(READER, WRITER) or die &#8220;pipe: $!&#8221;;<br />
    return (*READER, *WRITER);<br />
}<br />
($head, $tail) = ioqueue();</p>
<p> See the Symbol module for a way to create anonymous symbol table entries. </p>
<p> Because assignment of a reference to a typeglob creates an alias, this can be used to create what is effectively a local function, or at least, a local alias. </p>
<p>{<br />
    local *grow = \&amp; shrink;<br />
#only until this block exits<br />
    grow();<br />
#really calls shrink()<br />
        move();<br />
#if move() grow() s, it shrink() s too<br />
}<br />
grow();<br />
#get the real grow() again</p>
<p> See &#8220;Function Templates&#8221; in perlref for more about manipulating functions by name in this way.</p>
<dt>3.</p>
<dd> You want to temporarily change just one element of an array or hash. </p>
<p> You can <tt>&quot;local&quot;</tt>ize just one element of an aggregate. Usually this is done on dynamics: </p>
<p>{<br />
    local $SIG{INT} = &#8216;IGNORE&#8217;;<br />
    funct();<br />
#uninterruptible<br />
}<br />
#interruptibility automatically restored here</p>
<p> But it also works on lexically declared aggregates.</dl>
<h3>Pass by Reference</h3>
<p> If you want to pass more than one array or hash into a function&#8212;or return them from it&#8212;and have them maintain their integrity, then you&#8217;re going to have to use an explicit pass-by-reference. Before you do that, you need to understand references as detailed in perlref. This section may not make much sense to you otherwise. </p>
<p> Here are a few simple examples. First, let&#8217;s pass in several arrays to a function and have it <tt>&quot;pop&quot;</tt> all of then, returning a new list of all their former last elements: </p>
<p>@tailings = popmany( \@a, \@b, \@c, \@d);<br />
sub popmany<br />
{<br />
    my $aref;<br />
    my @retlist;<br />
    foreach<br />
        $aref(@_)<br />
        {<br />
            push @retlist, pop @$aref;<br />
        }<br />
    return @retlist;<br />
}</p>
<p> Here&#8217;s how you might write a function that returns a list of keys occurring in all the hashes passed to it: </p>
<p>@common = inter( \% foo, \% bar, \% joe);<br />
sub inter<br />
{<br />
    my($k, $href, % seen);<br />
#locals foreach $href(@_)<br />
    {<br />
        while ($k = each % $href) {<br />
            $seen<br />
            {<br />
                $k<br />
            }<br />
            ++;<br />
        }<br />
    }<br />
    return grep<br />
    {<br />
        $seen{$_} == @_<br />
    }<br />
    keys % seen;<br />
}</p>
<p> So far, we&#8217;re using just the normal list return mechanism. What happens if you want to pass or return a hash? Well, if you&#8217;re using only one of them, or you don&#8217;t mind them concatenating, then the normal calling convention is ok, although a little expensive. </p>
<p> Where people get into trouble is here: </p>
<p>(@a, @b) = func(@c, @d);<br />
or<br />
    (% a, % b) = func(% c, % d);</p>
<p> That syntax simply won&#8217;t work. It sets just <tt>@a</tt> or <tt>%a</tt> and clears the <tt>@b</tt> or <tt>%b</tt>. Plus the function didn&#8217;t get passed into two separate arrays or hashes: it got one long list in <tt>@_</tt>, as always. </p>
<p> If you can arrange for everyone to deal with this through references, it&#8217;s cleaner code, although not so nice to look at. Here&#8217;s a function that takes two array references as arguments, returning the two array elements in order of how many elements they have in them: </p>
<p>($aref, $bref) = func(\@c, \@d);<br />
print &#8220;@$aref has more than @$bref
&#8221;;<br />
sub func<br />
{<br />
    my($cref, $dref) = @_;<br />
    if (@$cref &gt; @$dref) {<br />
        return ($cref, $dref);<br />
    } else {<br />
        return ($dref, $cref);<br />
    }<br />
}</p>
<p> It turns out that you can actually do this also: </p>
<p>(*a, *b) = func(\@c, \@d);<br />
print &#8220;@a has more than @b
&#8221;;<br />
sub func<br />
{<br />
    local(*c, *d) = @_;<br />
    if (@c &gt; @d) {<br />
        return (\@c, \@d);<br />
    } else {<br />
        return (\@d, \@c);<br />
    }<br />
}</p>
<p> Here we&#8217;re using the typeglobs to do symbol table aliasing. It&#8217;s a tad subtle, though, and also won&#8217;t work if you&#8217;re using <tt>&quot;my&quot;</tt> variables, because only globals (even in disguise as <tt>&quot;local&quot;</tt>s) are in the symbol table. </p>
<p> If you&#8217;re passing around filehandles, you could usually just use the bare typeglob, like <tt>*STDOUT</tt>, but typeglobs references work, too. For example: </p>
<p>splutter(\*STDOUT);<br />
sub splutter<br />
{<br />
    my $fh = shift;<br />
    print $fh &#8220;her um well a hmmm
&#8221;;<br />
}<br />
$rec = get_rec(\* STDIN);<br />
sub get_rec<br />
{<br />
    my $fh = shift;<br />
    return scalar&lt;$fh&gt;;<br />
}</p>
<p> If you&#8217;re planning on generating new filehandles, you could do this. Notice to pass back just the bare *FH, not its reference. </p>
<p>sub openit<br />
{<br />
    my $path = shift;<br />
    local *FH;<br />
    return open(FH, $path) ? *FH : undef;<br />
}</p>
<h3>Prototypes</h3>
<p> Perl supports a very limited kind of compile-time argument checking using function prototyping. This can be declared in either the <font SIZE="-1">PROTO</font> section or with a prototype attribute. If you declare either of </p>
<pre>
    sub mypush (\@@)
    sub mypush :prototype(\@@)
</pre>
<p> then <tt>&quot;mypush()&quot;</tt> takes arguments exactly like <tt>&quot;push()&quot;</tt> does. </p>
<p> If subroutine signatures are enabled (see &#8220;Signatures&#8221;), then the shorter <font SIZE="-1">PROTO</font> syntax is unavailable, because it would clash with signatures. In that case, a prototype can only be declared in the form of an attribute. </p>
<p> The function declaration must be visible at compile time. The prototype affects only interpretation of new-style calls to the function, where new-style is defined as not using the <tt>&quot;&amp;&quot;</tt> character. In other words, if you call it like a built-in function, then it behaves like a built-in function. If you call it like an old-fashioned subroutine, then it behaves like an old-fashioned subroutine. It naturally falls out from this rule that prototypes have no influence on subroutine references like <tt>&quot;\&amp;foo&quot;</tt> or on indirect subroutine calls like <tt>&quot;&amp;{$subref}&quot;</tt> or <tt>&quot;$subref-&gt;()&quot;</tt>. </p>
<p> Method calls are not influenced by prototypes either, because the function to be called is indeterminate at compile time, since the exact code called depends on inheritance. </p>
<p> Because the intent of this feature is primarily to let you define subroutines that work like built-in functions, here are prototypes for some other functions that parse almost exactly like the corresponding built-in. </p>
<p>Declared as Called as sub mylink($$)<br />
mylink $old, $new<br />
                 sub<br />
                 myvec($$$)<br />
myvec $var, $offset, 1 sub myindex($$; $) myindex &amp;getstring, &#8220;substr&#8221; sub mysyswrite($$$; $) mysyswrite $buf, 0, length($buf) &#8211; $off, $off sub myreverse(@) myreverse $a, $b, $c sub myjoin($ @) myjoin &#8220;:&#8221;, $a, $b, $c sub mypop(\@) mypop @array sub mysplice(\@$$ @) mysplice @array, 0, 2, @pushme sub mykeys(\[% @]) mykeys % {$hashref} sub myopen(*; $) myopen HANDLE, $name sub mypipe(**) mypipe READHANDLE, WRITEHANDLE sub mygrep(&amp;@) mygrep{ / foo / } $a, $b, $c sub myrand(; $) myrand 42 sub mytime() mytime</p>
<p> Any backslashed prototype character represents an actual argument that must start with that character (optionally preceded by <tt>&quot;my&quot;</tt>, <tt>&quot;our&quot;</tt> or <tt>&quot;local&quot;</tt>), with the exception of <tt>&quot;$&quot;</tt>, which will accept any scalar lvalue expression, such as <tt>&quot;$foo = 7&quot;</tt> or <tt>&quot;my_function()-&gt;[0]&quot;</tt>. The value passed as part of <tt>@_</tt> will be a reference to the actual argument given in the subroutine call, obtained by applying <tt>&quot;\&quot;</tt> to that argument. </p>
<p> You can use the <tt>&quot;\[]&quot;</tt> backslash group notation to specify more than one allowed argument type. For example: </p>
<pre>
    sub myref (\[$@%&amp;*])
</pre>
<p> will allow calling <code>myref()</code> as </p>
<pre>
    myref $var
    myref @array
    myref %hash
    myref &amp;sub
    myref *glob
</pre>
<p> and the first argument of <code>myref()</code> will be a reference to a scalar, an array, a hash, a code, or a glob. </p>
<p> Unbackslashed prototype characters have special meanings. Any unbackslashed <tt>&quot;@&quot;</tt> or <tt>&quot;%&quot;</tt> eats all remaining arguments, and forces list context. An argument represented by <tt>&quot;$&quot;</tt> forces scalar context. An <tt>&quot;&amp;&quot;</tt> requires an anonymous subroutine, which, if passed as the first argument, does not require the <tt>&quot;sub&quot;</tt> keyword or a subsequent comma. </p>
<p> A <tt>&quot;*&quot;</tt> allows the subroutine to accept a bareword, constant, scalar expression, typeglob, or a reference to a typeglob in that slot. The value will be available to the subroutine either as a simple scalar, or (in the latter two cases) as a reference to the typeglob. If you wish to always convert such arguments to a typeglob reference, use <code>Symbol::qualify_to_ref()</code> as follows: </p>
<p>use Symbol &#8216;qualify_to_ref&#8217;;<br />
sub foo(*)<br />
{<br />
    my $fh = qualify_to_ref(shift, caller);<br />
    &#8230;<br />
}</p>
<p> The <tt>&quot;+&quot;</tt> prototype is a special alternative to <tt>&quot;$&quot;</tt> that will act like <tt>&quot;\[@%]&quot;</tt> when given a literal array or hash variable, but will otherwise force scalar context on the argument. This is useful for functions which should accept either a literal array or an array reference as the argument: </p>
<p>sub mypush(+@)<br />
{<br />
    my $aref = shift;<br />
    die &#8220;Not an array or arrayref&#8221; unless ref $aref eq &#8216;ARRAY&#8217;;<br />
    push @$aref, @_;<br />
}</p>
<p> When using the <tt>&quot;+&quot;</tt> prototype, your function must check that the argument is of an acceptable type. </p>
<p> A semicolon (<tt>&quot;;&quot;</tt>) separates mandatory arguments from optional arguments. It is redundant before <tt>&quot;@&quot;</tt> or <tt>&quot;%&quot;</tt>, which gobble up everything else. </p>
<p> As the last character of a prototype, or just before a semicolon, a <tt>&quot;@&quot;</tt> or a <tt>&quot;%&quot;</tt>, you can use <tt>&quot;_&quot;</tt> in place of <tt>&quot;$&quot;</tt>: if this argument is not provided, <tt>$_</tt> will be used instead. </p>
<p> Note how the last three examples in the table above are treated specially by the parser. <tt>&quot;mygrep()&quot;</tt> is parsed as a true list operator, <tt>&quot;myrand()&quot;</tt> is parsed as a true unary operator with unary precedence the same as <tt>&quot;rand()&quot;</tt>, and <tt>&quot;mytime()&quot;</tt> is truly without arguments, just like <tt>&quot;time()&quot;</tt>. That is, if you say </p>
<pre>
    mytime +2;
</pre>
<p> you&#8217;ll get <tt>&quot;mytime() + 2&quot;</tt>, not <tt><a href="/docs/linux/man/2-mytime/">mytime</a>(2)</tt>, which is how it would be parsed without a prototype. If you want to force a unary function to have the same precedence as a list operator, add <tt>&quot;;&quot;</tt> to the end of the prototype: </p>
<p>sub mygetprotobynumber($;);<br />
mygetprotobynumber $a &gt; $b;<br />
#parsed as mygetprotobynumber($a &gt; $b)</p>
<p> The interesting thing about <tt>&quot;&amp;&quot;</tt> is that you can generate new syntax with it, provided it&#8217;s in the initial position: </p>
<p>sub try(&amp;@)<br />
{<br />
    my($try, $catch) = @_;<br />
    eval{&amp;$try};<br />
    if ($ @) {<br />
        local $_ = $ @;<br />
        &amp;$catch;<br />
    }<br />
}<br />
sub catch (&amp;)<br />
{<br />
    $_[0]<br />
}<br />
try {<br />
    die &#8220;phooey&#8221;;<br />
} catch {<br />
    / phooey / and print &#8220;unphooey
&#8221;;<br />
};</p>
<p> That prints <tt>&quot;unphooey&quot;</tt>. (Yes, there are still unresolved issues having to do with visibility of <tt>@_</tt>. I&#8217;m ignoring that question for the moment. (But note that if we make <tt>@_</tt> lexically scoped, those anonymous subroutines can act like closures&#8230; (Gee, is this sounding a little Lispish? (Never mind.)))) </p>
<p> And here&#8217;s a reimplementation of the Perl <tt>&quot;grep&quot;</tt> operator: </p>
<p>sub mygrep(&amp;@)<br />
{<br />
    my $code = shift;<br />
    my @result;<br />
    foreach<br />
        $_(@_)<br />
        {<br />
            push(@result, $_) if &amp;$code;<br />
        }<br />
    @result;<br />
}</p>
<p> Some folks would prefer full alphanumeric prototypes. Alphanumerics have been intentionally left out of prototypes for the express purpose of someday in the future adding named, formal parameters. The current mechanism&#8217;s main goal is to let module writers provide better diagnostics for module users. Larry feels the notation quite understandable to Perl programmers, and that it will not intrude greatly upon the meat of the module, nor make it harder to read. The line noise is visually encapsulated into a small pill that&#8217;s easy to swallow. </p>
<p> If you try to use an alphanumeric sequence in a prototype you will generate an optional warning &#8211; &#8220;Illegal character in prototype&#8230;&#8221;. Unfortunately earlier versions of Perl allowed the prototype to be used as long as its prefix was a valid prototype. The warning may be upgraded to a fatal error in a future version of Perl once the majority of offending code is fixed. </p>
<p> It&#8217;s probably best to prototype new functions, not retrofit prototyping into older ones. That&#8217;s because you must be especially careful about silent impositions of differing list versus scalar contexts. For example, if you decide that a function should take just one parameter, like this: </p>
<p>sub func($)<br />
{<br />
    my $n = shift;<br />
    print &#8220;you gave me $n
&#8221;;<br />
}</p>
<p> and someone has been calling it with an array or expression returning a list: </p>
<p>func(@foo);<br />
func($text = ~ /\w + / g);</p>
<p> Then you&#8217;ve just supplied an automatic <tt>&quot;scalar&quot;</tt> in front of their argument, which can be more than a bit surprising. The old <tt>@foo</tt> which used to hold one thing doesn&#8217;t get passed in. Instead, <tt>&quot;func()&quot;</tt> now gets passed in a <tt>1</tt>; that is, the number of elements in <tt>@foo</tt>. And the <tt>&quot;m//g&quot;</tt> gets called in scalar context so instead of a list of words it returns a boolean result and advances <tt>&quot;pos($text)&quot;</tt>. Ouch! </p>
<p> If a sub has both a <font SIZE="-1">PROTO</font> and a <font SIZE="-1">BLOCK,</font> the prototype is not applied until after the <font SIZE="-1">BLOCK</font> is completely defined. This means that a recursive function with a prototype has to be predeclared for the prototype to take effect, like so: </p>
<p>sub foo($$);<br />
sub foo($$)<br />
{<br />
    foo 1, 2;<br />
}</p>
<p> This is all very powerful, of course, and should be used only in moderation to make the world a better place.</p>
<h3>Constant Functions</h3>
<p> Functions with a prototype of <tt>&quot;()&quot;</tt> are potential candidates for inlining. If the result after optimization and constant folding is either a constant or a lexically-scoped scalar which has no other references, then it will be used in place of function calls made without <tt>&quot;&amp;&quot;</tt>. Calls made using <tt>&quot;&amp;&quot;</tt> are never inlined. (See <i>constant.pm</i> for an easy way to declare most constants.) </p>
<p> The following functions would all be inlined: </p>
<p>sub pi(){3.14159} #Not exact, but close.sub PI(){4 * atan2 1, 1} #As good as it gets,<br />
#and it&#8217;s inlined, too!<br />
    sub ST_DEV(){0} sub ST_INO(){1} sub FLAG_FOO(){1 &lt;&lt; 8} sub FLAG_BAR(){1 &lt;&lt; 9} sub FLAG_MASK(){FLAG_FOO | FLAG_BAR} sub OPT_BAZ(){not(0x1B58 &amp; FLAG_MASK)} sub N(){int(OPT_BAZ) / 3} sub FOO_SET()<br />
{<br />
    1 if FLAG_MASK &amp;FLAG_FOO<br />
}<br />
sub FOO_SET2()<br />
{<br />
    if (FLAG_MASK &amp; FLAG_FOO) {<br />
        1<br />
    }<br />
}</p>
<p> (Be aware that the last example was not always inlined in Perl 5.20 and earlier, which did not behave consistently with subroutines containing inner scopes.) You can countermand inlining by using an explicit <tt>&quot;return&quot;</tt>: </p>
<p>sub baz_val()<br />
{<br />
    if (OPT_BAZ) {<br />
        return 23;<br />
    } else {<br />
        return 42;<br />
    }<br />
}<br />
sub bonk_val()<br />
{<br />
    return 12345<br />
}</p>
<p> As alluded to earlier you can also declare inlined subs dynamically at <font SIZE="-1">BEGIN</font> time if their body consists of a lexically-scoped scalar which has no other references. Only the first example here will be inlined: </p>
<p>BEGIN<br />
{<br />
    my $var = 1;<br />
    no strict &#8216;refs&#8217;;<br />
    *INLINED = sub(){$var};<br />
}<br />
BEGIN<br />
{<br />
    my $var = 1;<br />
    my $ref = \$var;<br />
    no strict &#8216;refs&#8217;;<br />
    *NOT_INLINED = sub(){$var};<br />
}</p>
<p> A not so obvious caveat with this (see [<font SIZE="-1">RT</font> #79908]) is that the variable will be immediately inlined, and will stop behaving like a normal lexical variable, e.g. this will print <tt>79907</tt>, not <tt>79908</tt>: </p>
<p>BEGIN<br />
{<br />
    my $x = 79907;<br />
    *RT_79908 = sub(){$x};<br />
    $x++;<br />
}<br />
print RT_79908();<br />
#prints 79907</p>
<p> As of Perl 5.22, this buggy behavior, while preserved for backward compatibility, is detected and emits a deprecation warning. If you want the subroutine to be inlined (with no warning), make sure the variable is not used in a context where it could be modified aside from where it is declared. </p>
<p>#Fine, no warning<br />
BEGIN<br />
{<br />
    my $x = 54321;<br />
    *INLINED = sub(){$x};<br />
}<br />
#Warns.Future Perl versions will stop inlining it.<br />
BEGIN<br />
{<br />
    my $x;<br />
    $x = 54321;<br />
    *ALSO_INLINED = sub(){$x};<br />
}</p>
<p> Perl 5.22 also introduces the experimental &#8220;const&#8221; attribute as an alternative. (Disable the &#8220;experimental::const_attr&#8221; warnings if you want to use it.) When applied to an anonymous subroutine, it forces the sub to be called when the <tt>&quot;sub&quot;</tt> expression is evaluated. The return value is captured and turned into a constant subroutine: </p>
<p>my $x = 54321;<br />
*INLINED = sub : const {$x};<br />
$x++;</p>
<p> The return value of <tt>&quot;INLINED&quot;</tt> in this example will always be 54321, regardless of later modifications to <tt>$x</tt>. You can also put any arbitrary code inside the sub, at it will be executed immediately and its return value captured the same way. </p>
<p> If you really want a subroutine with a <tt>&quot;()&quot;</tt> prototype that returns a lexical variable you can easily force it to not be inlined by adding an explicit <tt>&quot;return&quot;</tt>: </p>
<p>BEGIN<br />
{<br />
    my $x = 79907;<br />
    *RT_79908 = sub(){return $x};<br />
    $x++;<br />
}<br />
print RT_79908();<br />
#prints 79908</p>
<p> The easiest way to tell if a subroutine was inlined is by using B::Deparse. Consider this example of two subroutines returning <tt>1</tt>, one with a <tt>&quot;()&quot;</tt> prototype causing it to be inlined, and one without (with deparse output truncated for clarity): </p>
<p>$ perl &#8211; MO = Deparse &#8211; le &#8216;sub ONE { 1 } if (ONE) { print ONE if ONE }&#8217; sub ONE<br />
{<br />
    1;<br />
}<br />
if (ONE) {<br />
    print ONE() if ONE;<br />
}<br />
$ perl &#8211; MO = Deparse &#8211; le &#8216;sub ONE () { 1 } if (ONE) { print ONE if ONE }&#8217; sub ONE()<br />
{<br />
    1<br />
}<br />
do {<br />
    print 1<br />
};</p>
<p> If you redefine a subroutine that was eligible for inlining, you&#8217;ll get a warning by default. You can use this warning to tell whether or not a particular subroutine is considered inlinable, since it&#8217;s different than the warning for overriding non-inlined subroutines: </p>
<p>$ perl &#8211; e &#8216;sub one () {1} sub one () {2}&#8217; Constant subroutine one redefined at &#8211; e line 1. $ perl &#8211; we &#8216;sub one {1} sub one {2}&#8217; Subroutine one redefined at &#8211; e line 1.</p>
<p> The warning is considered severe enough not to be affected by the <code>-w</code> switch (or its absence) because previously compiled invocations of the function will still be using the old value of the function. If you need to be able to redefine the subroutine, you need to ensure that it isn&#8217;t inlined, either by dropping the <tt>&quot;()&quot;</tt> prototype (which changes calling semantics, so beware) or by thwarting the inlining mechanism in some other way, e.g. by adding an explicit <tt>&quot;return&quot;</tt>, as mentioned above: </p>
<pre>
    sub not_inlined () { return 23 }
</pre>
<h3>Overriding Built-in Functions</h3>
<p> Many built-in functions may be overridden, though this should be tried only occasionally and for good reason. Typically this might be done by a package attempting to emulate missing built-in functionality on a non-Unix system. </p>
<p> Overriding may be done only by importing the name from a module at compile time&#8212;ordinary predeclaration isn&#8217;t good enough. However, the <tt>&quot;use subs&quot;</tt> pragma lets you, in effect, predeclare subs via the import syntax, and these names may then override built-in ones: </p>
<p>use subs &#8216;chdir&#8217;, &#8216;chroot&#8217;, &#8216;chmod&#8217;, &#8216;chown&#8217;;<br />
chdir $somewhere;<br />
sub chdir<br />
{<br />
    &#8230;<br />
}</p>
<p> To unambiguously refer to the built-in form, precede the built-in name with the special package qualifier <tt>&quot;CORE::&quot;</tt>. For example, saying <tt>&quot;CORE::open()&quot;</tt> always refers to the built-in <tt>&quot;open()&quot;</tt>, even if the current package has imported some other subroutine called <tt>&quot;&amp;open()&quot;</tt> from elsewhere. Even though it looks like a regular function call, it isn&#8217;t: the <font SIZE="-1">CORE::</font> prefix in that case is part of Perl&#8217;s syntax, and works for any keyword, regardless of what is in the <font SIZE="-1">CORE</font> package. Taking a reference to it, that is, <tt>&quot;\&amp;CORE::open&quot;</tt>, only works for some keywords. See <font SIZE="-1">CORE</font>. </p>
<p> Library modules should not in general export built-in names like <tt>&quot;open&quot;</tt> or <tt>&quot;chdir&quot;</tt> as part of their default <tt>@EXPORT</tt> list, because these may sneak into someone else&#8217;s namespace and change the semantics unexpectedly. Instead, if the module adds that name to <tt>@EXPORT_OK</tt>, then it&#8217;s possible for a user to import the name explicitly, but not implicitly. That is, they could say </p>
<pre>
    use Module 'open';
</pre>
<p> and it would import the <tt>&quot;open&quot;</tt> override. But if they said </p>
<pre>
    use Module;
</pre>
<p> they would get the default imports without overrides. </p>
<p> The foregoing mechanism for overriding built-in is restricted, quite deliberately, to the package that requests the import. There is a second method that is sometimes applicable when you wish to override a built-in everywhere, without regard to namespace boundaries. This is achieved by importing a sub into the special namespace <tt>&quot;CORE::GLOBAL::&quot;</tt>. Here is an example that quite brazenly replaces the <tt>&quot;glob&quot;</tt> operator with something that understands regular expressions. </p>
<p>package REGlob;<br />
require Exporter;<br />
@ISA = &#8216;Exporter&#8217;;<br />
@EXPORT_OK = &#8216;glob&#8217;;<br />
sub import<br />
{<br />
    my $pkg = shift;<br />
    return unless @_;<br />
    my $sym = shift;<br />
        my $where = ($sym =~ s/^GLOBAL_// ? &#8216;CORE::GLOBAL&#8217; : caller(0));<br />
        $pkg-&gt;export($where, $sym, @_);<br />
}<br />
sub glob<br />
{<br />
    my $pat = shift;<br />
    my @got;<br />
    if (opendir my $d, &#8216;.&#8217;) {<br />
        @got = grep / $pat /, readdir $d;<br />
        closedir $d;<br />
    }<br />
    return @got;<br />
}<br />
1;</p>
<p> And here&#8217;s how it could be (ab)used: </p>
<p>#use REGlob &#8216;GLOBAL_glob&#8217;; #override glob() in ALL namespaces<br />
package Foo;<br />
use REGlob &#8216;glob&#8217;;<br />
#override glob() in Foo::only<br />
        print for &lt; ^[a &#8211; z_] +\.pm\$&gt;;<br />
#show all pragmatic modules</p>
<p> The initial comment shows a contrived, even dangerous example. By overriding <tt>&quot;glob&quot;</tt> globally, you would be forcing the new (and subversive) behavior for the <tt>&quot;glob&quot;</tt> operator for <i>every</i> namespace, without the complete cognizance or cooperation of the modules that own those namespaces. Naturally, this should be done with extreme caution&#8212;if it must be done at all. </p>
<p> The <tt>&quot;REGlob&quot;</tt> example above does not implement all the support needed to cleanly override perl&#8217;s <tt>&quot;glob&quot;</tt> operator. The built-in <tt>&quot;glob&quot;</tt> has different behaviors depending on whether it appears in a scalar or list context, but our <tt>&quot;REGlob&quot;</tt> doesn&#8217;t. Indeed, many perl built-in have such context sensitive behaviors, and these must be adequately supported by a properly written override. For a fully functional example of overriding <tt>&quot;glob&quot;</tt>, study the implementation of <tt>&quot;File::DosGlob&quot;</tt> in the standard library. </p>
<p> When you override a built-in, your replacement should be consistent (if possible) with the built-in native syntax. You can achieve this by using a suitable prototype. To get the prototype of an overridable built-in, use the <tt>&quot;prototype&quot;</tt> function with an argument of <tt>&quot;CORE::builtin_name&quot;</tt> (see &#8220;prototype&#8221; in perlfunc). </p>
<p> Note however that some built-ins can&#8217;t have their syntax expressed by a prototype (such as <tt>&quot;system&quot;</tt> or <tt>&quot;chomp&quot;</tt>). If you override them you won&#8217;t be able to fully mimic their original syntax. </p>
<p> The built-ins <tt>&quot;do&quot;</tt>, <tt>&quot;require&quot;</tt> and <tt>&quot;glob&quot;</tt> can also be overridden, but due to special magic, their original syntax is preserved, and you don&#8217;t have to define a prototype for their replacements. (You can&#8217;t override the <tt>&quot;do BLOCK&quot;</tt> syntax, though). </p>
<p> <tt>&quot;require&quot;</tt> has special additional dark magic: if you invoke your <tt>&quot;require&quot;</tt> replacement as <tt>&quot;require Foo::Bar&quot;</tt>, it will actually receive the argument <tt>&quot;Foo/Bar.pm&quot;</tt> in <tt>@_</tt>. See &#8220;require&#8221; in perlfunc. </p>
<p> And, as you&#8217;ll have noticed from the previous example, if you override <tt>&quot;glob&quot;</tt>, the <tt>&quot;&lt;*&gt;&quot;</tt> glob operator is overridden as well. </p>
<p> In a similar fashion, overriding the <tt>&quot;readline&quot;</tt> function also overrides the equivalent I/O operator <tt>&quot;&lt;FILEHANDLE&gt;&quot;</tt>. Also, overriding <tt>&quot;readpipe&quot;</tt> also overrides the operators <tt>&quot;``&quot;</tt> and <tt>&quot;qx//&quot;</tt>. </p>
<p> Finally, some built-ins (e.g. <tt>&quot;exists&quot;</tt> or <tt>&quot;grep&quot;</tt>) can&#8217;t be overridden.</p>
<h3>Autoloading</h3>
<p> If you call a subroutine that is undefined, you would ordinarily get an immediate, fatal error complaining that the subroutine doesn&#8217;t exist. (Likewise for subroutines being used as methods, when the method doesn&#8217;t exist in any base class of the class&#8217;s package.) However, if an <tt>&quot;AUTOLOAD&quot;</tt> subroutine is defined in the package or packages used to locate the original subroutine, then that <tt>&quot;AUTOLOAD&quot;</tt> subroutine is called with the arguments that would have been passed to the original subroutine. The fully qualified name of the original subroutine magically appears in the global <tt>$AUTOLOAD</tt> variable of the same package as the <tt>&quot;AUTOLOAD&quot;</tt> routine. The name is not passed as an ordinary argument because, er, well, just because, that&#8217;s why. (As an exception, a method call to a nonexistent <tt>&quot;import&quot;</tt> or <tt>&quot;unimport&quot;</tt> method is just skipped instead. Also, if the <font SIZE="-1">AUTOLOAD</font> subroutine is an <font SIZE="-1">XSUB,</font> there are other ways to retrieve the subroutine name. See &#8220;Autoloading with XSUBs&#8221; in perlguts for details.) </p>
<p> Many <tt>&quot;AUTOLOAD&quot;</tt> routines load in a definition for the requested subroutine using <code>eval()</code>, then execute that subroutine using a special form of <code>goto()</code> that erases the stack frame of the <tt>&quot;AUTOLOAD&quot;</tt> routine without a trace. (See the source to the standard module documented in AutoLoader, for example.) But an <tt>&quot;AUTOLOAD&quot;</tt> routine can also just emulate the routine and never define it. For example, let&#8217;s pretend that a function that wasn&#8217;t defined should just invoke <tt>&quot;system&quot;</tt> with those arguments. All you&#8217;d do is: </p>
<p>sub AUTOLOAD<br />
{<br />
    our $AUTOLOAD;<br />
#keep &#8216;use strict&#8217; happy<br />
        my $program = $AUTOLOAD;<br />
    $program = ~s /.*:: //;<br />
                       system($program, @_);<br />
}<br />
date();<br />
who();<br />
ls(&#8216;-l&#8217;);</p>
<p> In fact, if you predeclare functions you want to call that way, you don&#8217;t even need parentheses: </p>
<p>use subs qw(date who ls);<br />
date;<br />
who;<br />
ls &#8216;-l&#8217;;</p>
<p> A more complete example of this is the Shell module on <font SIZE="-1">CPAN,</font> which can treat undefined subroutine calls as calls to external programs. </p>
<p> Mechanisms are available to help modules writers split their modules into autoloadable files. See the standard AutoLoader module described in AutoLoader and in AutoSplit, the standard SelfLoader modules in SelfLoader, and the document on adding C functions to Perl code in perlxs.</p>
<h3>Subroutine Attributes</h3>
<p> A subroutine declaration or definition may have a list of attributes associated with it. If such an attribute list is present, it is broken up at space or colon boundaries and treated as though a <tt>&quot;use attributes&quot;</tt> had been seen. See attributes for details about what attributes are currently supported. Unlike the limitation with the obsolescent <tt>&quot;use attrs&quot;</tt>, the <tt>&quot;sub : ATTRLIST&quot;</tt> syntax works to associate the attributes with a pre-declaration, and not just with a subroutine definition. </p>
<p> The attributes must be valid as simple identifier names (without any punctuation other than the &#8216;_&#8217; character). They may have a parameter list appended, which is only checked for whether its parentheses (&#8216;(&#8216;,&#8217;)&#8217;) nest properly. </p>
<p> Examples of valid syntax (even though the attributes are unknown): </p>
<p>sub fnord(&amp;\%)<br />
    : switch (10, foo(7, 3))<br />
    : expensive;<br />
    sub plugh () : Ugly(&#8216;\(&#8220;) :Bad;<br />
    sub xyzzy : _5x5 {<br />
    &#8230; }</p>
<p> Examples of invalid syntax: </p>
<pre><code>
    sub fnord : switch(10,foo(); # ()-string not balanced
    sub snoid : Ugly('(');        # ()-string not balanced
    sub xyzzy : 5x5;              # "5x5" not a valid identifier
    sub plugh : Y2::north;        # "Y2::north" not a simple identifier
    sub snurt : foo + bar;        # "+" not a colon or space
</code></pre>
<p> The attribute list is passed as a list of constant strings to the code which associates them with the subroutine. In particular, the second example of valid syntax above currently looks like this in terms of how it&#8217;s parsed and invoked: </p>
<pre>
    use attributes __PACKAGE__, \&amp;plugh, q[Ugly('\(&quot;)], 'Bad';
</pre>
<p> For further details on attribute lists and their manipulation, see attributes and Attribute::Handlers.</p>
<h2>SEE ALSO</h2>
<p> See &#8220;Function Templates&#8221; in perlref for more about references and closures. See perlxs if you&#8217;d like to learn about calling C subroutines from Perl. See perlembed if you&#8217;d like to learn about calling Perl subroutines from C. See perlmod to learn about bundling up your functions in separate files. See perlmodlib to learn what library modules come standard on your system. See perlootut to learn how to make object method calls. </p>
<h2>Index</h2>
<dt><a href="#lbAS">SEE ALSO</a></p>
<dd></dl>

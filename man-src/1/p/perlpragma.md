---
title: "perlpragma(1)"
name: "perlpragma"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlpragma/"
---

<h2 class="name">NAME</h2>
 

 perlpragma - how to write a user pragma 

<h2>DESCRIPTION</h2>

 A pragma is a module which influences some aspect of the compile time or run time behaviour of Perl, such as <tt>&quot;strict&quot;</tt> or <tt>&quot;warnings&quot;</tt>. With Perl 5.10 you are no longer limited to the built in pragmata; you can now create user pragmata that modify the behaviour of user functions within a lexical scope.

<h2>A basic example</h2>

 For example, say you need to create a class implementing overloaded mathematical operators, and would like to provide your own pragma that functions much like <tt>&quot;use integer;&quot;</tt> You'd like this code 

 <pre><code>
use MyMaths;
my $l = MyMaths-&gt;new (1.2);
my $r = MyMaths-&gt;new (3.4);
print "A: ", $l + $r, "\n";
use myint;
print "B: ", $l + $r, "\n";
{
    no myint;
    print "C: ", $l + $r, "\n";
}
print "D: ", $l + $r, "\n";
no myint;
print "E: ", $l + $r, "\n";
</code></pre> 

 to give the output 

 <pre>
    A: 4.6
    B: 4
    C: 4.6
    D: 4
    E: 4.6
</pre> 

 <i>i.e.</i>, where <tt>&quot;use myint;&quot;</tt> is in effect, addition operations are forced to integer, whereas by default they are not, with the default behaviour being restored via <tt>&quot;no myint;&quot;</tt> 

 The minimal implementation of the package <tt>&quot;MyMaths&quot;</tt> would be something like this: 

 
package MyMaths;
use warnings;
use strict;
use myint();
use overload '+' = &gt; sub
{
    my($l, $r) = @_;
#Pass 1 to check up one call level from here
    if (myint::in_effect(1)) {
        int($$l) + int($$r);
    } else {
        $$l + $$r;
    }
};
sub new
{
    my($class, $value) = @_;
    bless \$value, $class;
}
1;
 

 Note how we load the user pragma <tt>&quot;myint&quot;</tt> with an empty list <tt>&quot;()&quot;</tt> to prevent its <tt>&quot;import&quot;</tt> being called. 

 The interaction with the Perl compilation happens inside package <tt>&quot;myint&quot;</tt>: 

 
package myint;
use strict;
use warnings;
sub import
{
    $ ^ H { "myint/in_effect" } = 1;
}
sub unimport
{
    $ ^ H { "myint/in_effect" } = 0;
}
sub in_effect
{
    my $level = shift // 0;
        my $hinthash = (caller($level))[10];
    return $hinthash-&gt;{"myint/in_effect"};
}
1;
 

 As pragmata are implemented as modules, like any other module, <tt>&quot;use myint;&quot;</tt> becomes 

 
BEGIN
{
    require myint;
    myint-&gt;import();
}
 

 and <tt>&quot;no myint;&quot;</tt> is 

 <pre><code>
BEGIN
{
    require myint;
    myint-&gt;unimport();
}
</code></pre> 

 Hence the <tt>&quot;import&quot;</tt> and <tt>&quot;unimport&quot;</tt> routines are called at <b>compile time</b> for the user's code. 

 User pragmata store their state by writing to the magical hash <tt>&quot;%^H&quot;</tt>, hence these two routines manipulate it. The state information in <tt>&quot;%^H&quot;</tt> is stored in the optree, and can be retrieved read-only at runtime with <tt>&quot;caller()&quot;</tt>, at index 10 of the list of returned results. In the example pragma, retrieval is encapsulated into the routine <tt>&quot;in_effect()&quot;</tt>, which takes as parameter the number of call frames to go up to find the value of the pragma in the user's script. This uses <tt>&quot;caller()&quot;</tt> to determine the value of <tt>$^H{&quot;myint/in_effect&quot;}</tt> when each line of the user's script was called, and therefore provide the correct semantics in the subroutine implementing the overloaded addition.

<h2>Key naming</h2>

 There is only a single <tt>&quot;%^H&quot;</tt>, but arbitrarily many modules that want to use its scoping semantics. To avoid stepping on each other's toes, they need to be sure to use different keys in the hash. It is therefore conventional for a module to use only keys that begin with the module's name (the name of its main package) and a ``/'' character. After this module-identifying prefix, the rest of the key is entirely up to the module: it may include any characters whatsoever. For example, a module <tt>&quot;Foo::Bar&quot;</tt> should use keys such as <tt>&quot;Foo::Bar/baz&quot;</tt> and <tt>&quot;Foo::Bar/$%/_!&quot;</tt>. Modules following this convention all play nicely with each other. 

 The Perl core uses a handful of keys in <tt>&quot;%^H&quot;</tt> which do not follow this convention, because they predate it. Keys that follow the convention won't conflict with the core's historical keys.

<h2>Implementation details</h2>

 The optree is shared between threads. This means there is a possibility that the optree will outlive the particular thread (and therefore the interpreter instance) that created it, so true Perl scalars cannot be stored in the optree. Instead a compact form is used, which can only store values that are integers (signed and unsigned), strings or <tt>&quot;undef&quot;</tt> - references and floating point values are stringified. If you need to store multiple values or complex structures, you should serialise them, for example with <tt>&quot;pack&quot;</tt>. The deletion of a hash key from <tt>&quot;%^H&quot;</tt> is recorded, and as ever can be distinguished from the existence of a key with value <tt>&quot;undef&quot;</tt> with <tt>&quot;exists&quot;</tt>. 

 <b>Don't</b> attempt to store references to data structures as integers which are retrieved via <tt>&quot;caller&quot;</tt> and converted back, as this will not be threadsafe. Accesses would be to the structure without locking (which is not safe for Perl's scalars), and either the structure has to leak, or it has to be freed when its creating thread terminates, which may be before the optree referencing it is deleted, if other threads outlive it. 

<h2>Index</h2>



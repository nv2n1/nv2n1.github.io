---
title: "pdlobjects(1)"
name: "pdlobjects"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdlobjects/"
---

PDL::Objects -- Object-Orientation, what is it and how to exploit it 

<h2>Description</h2>This still needs to be written properly. [Also, is there a good reason we don't recommend storing extra object data in the header hash?]
<h3>Inheritance</h3>There are basically two reasons for subclassing piddles. The first is simply that you want to be able to use your own routines like 

 <pre> $piddle-&gt;something()</pre>but don't want to mess up the <font SIZE="-1">PDL</font> namespace (a worthy goal, indeed!). The other is that you wish to provide special handling of some functions or more information about the data the piddle contains. In the first case, you can do with 

 <pre> package BAR;
 @ISA=qw/PDL/;
 sub foo {my($this) = @_; fiddle;}
 package main;
 $a = PDL::pdl(BAR,5);
 $a-&gt;foo();</pre>However, because a <font SIZE="-1">PDL</font> object is an opaque reference to a C struct, it is not possible to extend the <font SIZE="-1">PDL</font> class by e.g. extra data via subclassing. To circumvent this problem PerlDL has built-in support to extent the <font SIZE="-1">PDL</font> class via the <i>has-a</i> relation for blessed hashes. You can get the <i>HAS-A</i> behave like <i>IS-A</i> simply in that you assign the <tt>&quot;PDL&quot;</tt> object to the attribute named <font SIZE="-1">PDL</font> and redefine the method <i>initialize()</i>. 

 <pre> package FOO;
 @FOO::ISA = qw(PDL);
 sub initialize {
 my $class = shift;
 my $self = {
 creation_time =&gt; time(), # necessary extension :-)
 PDL =&gt; null, # used to store PDL object
 };
 bless $self, $class;
 }</pre>All <font SIZE="-1">PDL</font> constructors will call <i>initialize()</i> to make sure that your extensions are added by <i>all</i> <font SIZE="-1">PDL</font> constructors automatically. The <tt>&quot;PDL&quot;</tt> attribute is used by perlDL to store the <font SIZE="-1">PDL</font> object and all <font SIZE="-1">PDL</font> methods use this attribute automatically if they are called with a blessed hash reference instead of a <font SIZE="-1">PDL</font> object (a blessed scalar). 

 Do remember that if you subclass a class that is subclassed from a piddle, you need to call SUPER::initialize. 

 <font SIZE="-1">NEED STUFF ABOUT CODE</font> REFs!!
<h3>Examples</h3>You can find some simple examples of <font SIZE="-1">PDL</font> subclassing in the <font SIZE="-1">PDL</font> distribution test-case files. Look in <tt>&quot;t/subclass2.t&quot;</tt>, <tt>&quot;t/subclass3.t&quot;</tt>, etc.
<h3>Output Auto-Creation and Subclassed Objects</h3>For <font SIZE="-1">PDL</font> Functions where the output is created and returned, <font SIZE="-1">PDL</font> will either call the subclassed object's <tt>&quot;initialize&quot;</tt> or <tt>&quot;copy&quot;</tt> method to create the output object. (See PDL::Indexing for a discussion on Output Auto-Creation.) This behavior is summarized as follows:
<dl><dt>&bull;
<dd>For <i>Simple</i> functions, defined as having a signature of 

 <pre> func( a(), [o]b() )</pre><font SIZE="-1">PDL</font> will call <tt>$a</tt>-&gt;copy to create the output object. 

 In the spirit of the Perl philosophy of making <i>Easy Things Easy</i>, This behavior enables PDL-subclassed objects to be written without having to overload the many simple <font SIZE="-1">PDL</font> functions in this category. 

 The file t/subclass4.t in the <font SIZE="-1">PDL</font> Distribution tests for this behavior. See that file for an example.
<dt>&bull;
<dd>For other functions, <font SIZE="-1">PDL</font> will call <tt>$class</tt>-&gt;initialize to create the output object. Where <tt>$class</tt> is the class name of the first argument supplied to the function. 

 For these more complex cases, it is difficult to second-guess the subclassed object's designer to know if a <tt>&quot;copy&quot;</tt> or a <tt>&quot;initialize&quot;</tt> is appropriate. So for these cases, <tt>$class</tt>-&gt;initialize is called by default. If this is not appropriate for you, overload the function in your subclass and do whatever is appropriate is the overloaded function's code.</dl><h2>Author</h2>Copyright (C) Karl Glazebrook (kgb [at] aaoepp.aao.gov.au), Tuomas J. Lukka, (lukka [at] husc.harvard.edu) and Christian Soeller (c.soeller [at] auckland.ac.nz) 2000. Commercial reproduction of this documentation in a different format is forbidden.

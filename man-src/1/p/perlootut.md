---
title: "perlootut(1)"
name: "perlootut"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlootut/"
---

<h2 class="name">NAME</h2>
 

 perlootut - Object-Oriented Programming in Perl Tutorial 

<h2>DATE</h2>

 This document was created in February, 2011, and the last major revision was in February, 2013. 

 If you are reading this in the future then it's possible that the state of the art has changed. We recommend you start by reading the perlootut document in the latest stable release of Perl, rather than this version.

<h2>DESCRIPTION</h2>

 This document provides an introduction to object-oriented programming in Perl. It begins with a brief overview of the concepts behind object oriented design. Then it introduces several different <font SIZE="-1">OO</font> systems from <font SIZE="-1">CPAN</font> &lt;<a rel="nofollow" HREF="http://search.cpan.org">http://search.cpan.org</a>&gt; which build on top of what Perl provides. 

 By default, Perl's built-in <font SIZE="-1">OO</font> system is very minimal, leaving you to do most of the work. This minimalism made a lot of sense in 1994, but in the years since Perl 5.0 we've seen a number of common patterns emerge in Perl <font SIZE="-1">OO.</font> Fortunately, Perl's flexibility has allowed a rich ecosystem of Perl <font SIZE="-1">OO</font> systems to flourish. 

 If you want to know how Perl <font SIZE="-1">OO</font> works under the hood, the perlobj document explains the nitty gritty details. 

 This document assumes that you already understand the basics of Perl syntax, variable types, operators, and subroutine calls. If you don't understand these concepts yet, please read perlintro first. You should also read the perlsyn, perlop, and perlsub documents.

<h2>OBJECT-ORIENTED FUNDAMENTALS</h2>

 Most object systems share a number of common concepts. You've probably heard terms like ``class'', ``object, ''method``, and ''attribute&quot; before. Understanding the concepts will make it much easier to read and write object-oriented code. If you're already familiar with these terms, you should still skim this section, since it explains each concept in terms of Perl's <font SIZE="-1">OO</font> implementation. 

 Perl's <font SIZE="-1">OO</font> system is class-based. Class-based <font SIZE="-1">OO</font> is fairly common. It's used by Java, C<font SIZE="-2">++</font>, C#, Python, Ruby, and many other languages. There are other object orientation paradigms as well. JavaScript is the most popular language to use another paradigm. JavaScript's <font SIZE="-1">OO</font> system is prototype-based.

<h3>Object</h3>

 An <b>object</b> is a data structure that bundles together data and subroutines which operate on that data. An object's data is called <b>attributes</b>, and its subroutines are called <b>methods</b>. An object can be thought of as a noun (a person, a web service, a computer). 

 An object represents a single discrete thing. For example, an object might represent a file. The attributes for a file object might include its path, content, and last modification time. If we created an object to represent <i>/etc/hostname</i> on a machine named ``foo.example.com'', that object's path would be ``/etc/hostname'', its content would be ``foo\n'', and it's last modification time would be 1304974868 seconds since the beginning of the epoch. 

 The methods associated with a file might include <tt>&quot;rename()&quot;</tt> and <tt>&quot;write()&quot;</tt>. 

 In Perl most objects are hashes, but the <font SIZE="-1">OO</font> systems we recommend keep you from having to worry about this. In practice, it's best to consider an object's internal data structure opaque.

<h3>Class</h3>

 A <b>class</b> defines the behavior of a category of objects. A class is a name for a category (like ``File''), and a class also defines the behavior of objects in that category. 

 All objects belong to a specific class. For example, our <i>/etc/hostname</i> object belongs to the <tt>&quot;File&quot;</tt> class. When we want to create a specific object, we start with its class, and <b>construct</b> or <b>instantiate</b> an object. A specific object is often referred to as an <b>instance</b> of a class. 

 In Perl, any package can be a class. The difference between a package which is a class and one which isn't is based on how the package is used. Here's our ``class declaration'' for the <tt>&quot;File&quot;</tt> class: 

 <pre>
  package File;
</pre> 

 In Perl, there is no special keyword for constructing an object. However, most <font SIZE="-1">OO</font> modules on <font SIZE="-1">CPAN</font> use a method named <tt>&quot;new()&quot;</tt> to construct a new object: 

 <pre>
  my $hostname = File-&gt;new(
      path          =&gt; '/etc/hostname',
      content       =&gt; &quot;foo\n&quot;,
      last_mod_time =&gt; 1304974868,
  );
</pre> 

 (Don't worry about that <tt>&quot;-&gt;&quot;</tt> operator, it will be explained later.) 

 <i>Blessing</i> 

 As we said earlier, most Perl objects are hashes, but an object can be an instance of any Perl data type (scalar, array, etc.). Turning a plain data structure into an object is done by <b>blessing</b> that data structure using Perl's <tt>&quot;bless&quot;</tt> function. 

 While we strongly suggest you don't build your objects from scratch, you should know the term <b>bless</b>. A <b>blessed</b> data structure (aka ``a referent'') is an object. We sometimes say that an object has been ``blessed into a class''. 

 Once a referent has been blessed, the <tt>&quot;blessed&quot;</tt> function from the Scalar::Util core module can tell us its class name. This subroutine returns an object's class when passed an object, and false otherwise. 

 <pre><code>
use Scalar::Util 'blessed';
print blessed($hash);
#undef print blessed($hostname);
#File
</code></pre> 

 <i>Constructor</i> 

 A <b>constructor</b> creates a new object. In Perl, a class's constructor is just another method, unlike some other languages, which provide syntax for constructors. Most Perl classes use <tt>&quot;new&quot;</tt> as the name for their constructor: 

 
my $file = File-&gt;new (...);


<h3>Methods</h3>

 You already learned that a <b>method</b> is a subroutine that operates on an object. You can think of a method as the things that an object can <i>do</i>. If an object is a noun, then methods are its verbs (save, print, open). 

 In Perl, methods are simply subroutines that live in a class's package. Methods are always written to receive the object as their first argument: 

 
sub print_info
{
    my $self = shift;
    print "This file is at ", $self-&gt;path, "\n";
}
$file-&gt;print_info;
#The file is at / etc / hostname
 

 What makes a method special is <i>how it's called</i>. The arrow operator (<tt>&quot;-&gt;&quot;</tt>) tells Perl that we are calling a method. 

 When we make a method call, Perl arranges for the method's <b>invocant</b> to be passed as the first argument. <b>Invocant</b> is a fancy name for the thing on the left side of the arrow. The invocant can either be a class name or an object. We can also pass additional arguments to the method: 

 
sub print_info
{
    my $self = shift;
    my $prefix = shift // "This file is at ";
        print $prefix,
       ", ", $self-&gt;path, "\n";
}
$file-&gt;print_info("The file is located at ");
#The file is located at / etc / hostname


<h3>Attributes</h3>

 Each class can define its <b>attributes</b>. When we instantiate an object, we assign values to those attributes. For example, every <tt>&quot;File&quot;</tt> object has a path. Attributes are sometimes called <b>properties</b>. 

 Perl has no special syntax for attributes. Under the hood, attributes are often stored as keys in the object's underlying hash, but don't worry about this. 

 We recommend that you only access attributes via <b>accessor</b> methods. These are methods that can get or set the value of each attribute. We saw this earlier in the <tt>&quot;print_info()&quot;</tt> example, which calls <tt>&quot;$self-&gt;path&quot;</tt>. 

 You might also see the terms <b>getter</b> and <b>setter</b>. These are two types of accessors. A getter gets the attribute's value, while a setter sets it. Another term for a setter is <b>mutator</b> 

 Attributes are typically defined as read-only or read-write. Read-only attributes can only be set when the object is first created, while read-write attributes can be altered at any time. 

 The value of an attribute may itself be another object. For example, instead of returning its last mod time as a number, the <tt>&quot;File&quot;</tt> class could return a DateTime object representing that value. 

 It's possible to have a class that does not expose any publicly settable attributes. Not every class has attributes and methods.

<h3>Polymorphism</h3>

 <b>Polymorphism</b> is a fancy way of saying that objects from two different classes share an <font SIZE="-1">API.</font> For example, we could have <tt>&quot;File&quot;</tt> and <tt>&quot;WebPage&quot;</tt> classes which both have a <tt>&quot;print_content()&quot;</tt> method. This method might produce different output for each class, but they share a common interface. 

 While the two classes may differ in many ways, when it comes to the <tt>&quot;print_content()&quot;</tt> method, they are the same. This means that we can try to call the <tt>&quot;print_content()&quot;</tt> method on an object of either class, and <b>we don't have to know what class the object belongs to!</b> 

 Polymorphism is one of the key concepts of object-oriented design.

<h3>Inheritance</h3>

 <b>Inheritance</b> lets you create a specialized version of an existing class. Inheritance lets the new class reuse the methods and attributes of another class. 

 For example, we could create an <tt>&quot;File::MP3&quot;</tt> class which <b>inherits</b> from <tt>&quot;File&quot;</tt>. An <tt>&quot;File::MP3&quot;</tt> <b>is-a</b> <i>more specific</i> type of <tt>&quot;File&quot;</tt>. All mp3 files are files, but not all files are mp3 files. 

 We often refer to inheritance relationships as <b>parent-child</b> or <tt>&quot;superclass&quot;</tt>/<tt>&quot;subclass&quot;</tt> relationships. Sometimes we say that the child has an <b>is-a</b> relationship with its parent class. 

 <tt>&quot;File&quot;</tt> is a <b>superclass</b> of <tt>&quot;File::MP3&quot;</tt>, and <tt>&quot;File::MP3&quot;</tt> is a <b>subclass</b> of <tt>&quot;File&quot;</tt>. 

 <pre>
  package File::MP3;
  use parent 'File';
</pre> 

 The parent module is one of several ways that Perl lets you define inheritance relationships. 

 Perl allows multiple inheritance, which means that a class can inherit from multiple parents. While this is possible, we strongly recommend against it. Generally, you can use <b>roles</b> to do everything you can do with multiple inheritance, but in a cleaner way. 

 Note that there's nothing wrong with defining multiple subclasses of a given class. This is both common and safe. For example, we might define <tt>&quot;File::MP3::FixedBitrate&quot;</tt> and <tt>&quot;File::MP3::VariableBitrate&quot;</tt> classes to distinguish between different types of mp3 file. 

 <i>Overriding methods and method resolution</i> 

 Inheritance allows two classes to share code. By default, every method in the parent class is also available in the child. The child can explicitly <b>override</b> a parent's method to provide its own implementation. For example, if we have an <tt>&quot;File::MP3&quot;</tt> object, it has the <tt>&quot;print_info()&quot;</tt> method from <tt>&quot;File&quot;</tt>: 

 
my $cage = File::MP3-&gt;new (
    path = &gt; 'mp3s/My-Body-Is-a-Cage.mp3',
    content = &gt; $mp3_data,
    last_mod_time = &gt; 1304974868,
    title = &gt; 'My Body Is a Cage', );
$cage-&gt;print_info;
#The file is at mp3s / My - Body - Is - a - Cage.mp3
 

 If we wanted to include the mp3's title in the greeting, we could override the method: 

 
package File::MP3;
use parent 'File';
sub print_info
{
    my $self = shift;
    print "This file is at ", $self-&gt;path, "\n";
    print "Its title is ", $self-&gt;title, "\n";
}
$cage-&gt;print_info;
#The file is at mp3s / My - Body - Is - a - Cage.mp3
#Its title is My Body Is a Cage
 

 The process of determining what method should be used is called <b>method resolution</b>. What Perl does is look at the object's class first (<tt>&quot;File::MP3&quot;</tt> in this case). If that class defines the method, then that class's version of the method is called. If not, Perl looks at each parent class in turn. For <tt>&quot;File::MP3&quot;</tt>, its only parent is <tt>&quot;File&quot;</tt>. If <tt>&quot;File::MP3&quot;</tt> does not define the method, but <tt>&quot;File&quot;</tt> does, then Perl calls the method in <tt>&quot;File&quot;</tt>. 

 If <tt>&quot;File&quot;</tt> inherited from <tt>&quot;DataSource&quot;</tt>, which inherited from <tt>&quot;Thing&quot;</tt>, then Perl would keep looking ``up the chain'' if necessary. 

 It is possible to explicitly call a parent method from a child: 

 
package File::MP3;
use parent 'File';
sub print_info
{
    my $self = shift;
    $self-&gt;SUPER::print_info();
    print "Its title is ", $self-&gt;title, "\n";
}
 

 The <tt>&quot;SUPER::&quot;</tt> bit tells Perl to look for the <tt>&quot;print_info()&quot;</tt> in the <tt>&quot;File::MP3&quot;</tt> class's inheritance chain. When it finds the parent class that implements this method, the method is called. 

 We mentioned multiple inheritance earlier. The main problem with multiple inheritance is that it greatly complicates method resolution. See perlobj for more details.

<h3>Encapsulation</h3>

 <b>Encapsulation</b> is the idea that an object is opaque. When another developer uses your class, they don't need to know <i>how</i> it is implemented, they just need to know <i>what</i> it does. 

 Encapsulation is important for several reasons. First, it allows you to separate the public <font SIZE="-1">API</font> from the private implementation. This means you can change that implementation without breaking the <font SIZE="-1">API.</font> 

 Second, when classes are well encapsulated, they become easier to subclass. Ideally, a subclass uses the same APIs to access object data that its parent class uses. In reality, subclassing sometimes involves violating encapsulation, but a good <font SIZE="-1">API</font> can minimize the need to do this. 

 We mentioned earlier that most Perl objects are implemented as hashes under the hood. The principle of encapsulation tells us that we should not rely on this. Instead, we should use accessor methods to access the data in that hash. The object systems that we recommend below all automate the generation of accessor methods. If you use one of them, you should never have to access the object as a hash directly.

<h3>Composition</h3>

 In object-oriented code, we often find that one object references another object. This is called <b>composition</b>, or a <b>has-a</b> relationship. 

 Earlier, we mentioned that the <tt>&quot;File&quot;</tt> class's <tt>&quot;last_mod_time&quot;</tt> accessor could return a DateTime object. This is a perfect example of composition. We could go even further, and make the <tt>&quot;path&quot;</tt> and <tt>&quot;content&quot;</tt> accessors return objects as well. The <tt>&quot;File&quot;</tt> class would then be <b>composed</b> of several other objects.

<h3>Roles</h3>

 <b>Roles</b> are something that a class <i>does</i>, rather than something that it <i>is</i>. Roles are relatively new to Perl, but have become rather popular. Roles are <b>applied</b> to classes. Sometimes we say that classes <b>consume</b> roles. 

 Roles are an alternative to inheritance for providing polymorphism. Let's assume we have two classes, <tt>&quot;Radio&quot;</tt> and <tt>&quot;Computer&quot;</tt>. Both of these things have on/off switches. We want to model that in our class definitions. 

 We could have both classes inherit from a common parent, like <tt>&quot;Machine&quot;</tt>, but not all machines have on/off switches. We could create a parent class called <tt>&quot;HasOnOffSwitch&quot;</tt>, but that is very artificial. Radios and computers are not specializations of this parent. This parent is really a rather ridiculous creation. 

 This is where roles come in. It makes a lot of sense to create a <tt>&quot;HasOnOffSwitch&quot;</tt> role and apply it to both classes. This role would define a known <font SIZE="-1">API</font> like providing <tt>&quot;turn_on()&quot;</tt> and <tt>&quot;turn_off()&quot;</tt> methods. 

 Perl does not have any built-in way to express roles. In the past, people just bit the bullet and used multiple inheritance. Nowadays, there are several good choices on <font SIZE="-1">CPAN</font> for using roles.

<h3>When to Use <font SIZE="-1">OO</font></h3>

 Object Orientation is not the best solution to every problem. In <i>Perl Best Practices</i> (copyright 2004, Published by O'Reilly Media, Inc.), Damian Conway provides a list of criteria to use when deciding if <font SIZE="-1">OO</font> is the right fit for your problem:
<dl>
<dt>&bull;
<dd> The system being designed is large, or is likely to become large.
<dt>&bull;
<dd> The data can be aggregated into obvious structures, especially if there's a large amount of data in each aggregate.
<dt>&bull;
<dd> The various types of data aggregate form a natural hierarchy that facilitates the use of inheritance and polymorphism.
<dt>&bull;
<dd> You have a piece of data on which many different operations are applied.
<dt>&bull;
<dd> You need to perform the same general operations on related types of data, but with slight variations depending on the specific type of data the operations are applied to.
<dt>&bull;
<dd> It's likely you'll have to add new data types later.
<dt>&bull;
<dd> The typical interactions between pieces of data are best represented by operators.
<dt>&bull;
<dd> The implementation of individual components of the system is likely to change over time.
<dt>&bull;
<dd> The system design is already object-oriented.
<dt>&bull;
<dd> Large numbers of other programmers will be using your code modules.</dl>

<h2>PERL OO SYSTEMS</h2>

 As we mentioned before, Perl's built-in <font SIZE="-1">OO</font> system is very minimal, but also quite flexible. Over the years, many people have developed systems which build on top of Perl's built-in system to provide more features and convenience. 

 We strongly recommend that you use one of these systems. Even the most minimal of them eliminates a lot of repetitive boilerplate. There's really no good reason to write your classes from scratch in Perl. 

 If you are interested in the guts underlying these systems, check out perlobj.

<h3>Moose</h3>

 Moose bills itself as a ``postmodern object system for Perl 5''. Don't be scared, the ``postmodern'' label is a callback to Larry's description of Perl as ``the first postmodern computer language''. 

 <tt>&quot;Moose&quot;</tt> provides a complete, modern <font SIZE="-1">OO</font> system. Its biggest influence is the Common Lisp Object System, but it also borrows ideas from Smalltalk and several other languages. <tt>&quot;Moose&quot;</tt> was created by Stevan Little, and draws heavily from his work on the Perl 6 <font SIZE="-1">OO</font> design. 

 Here is our <tt>&quot;File&quot;</tt> class using <tt>&quot;Moose&quot;</tt>: 

 
package File;
use Moose;
has path = &gt; (is = &gt; 'ro');
has content = &gt; (is = &gt; 'ro');
has last_mod_time = &gt; (is = &gt; 'ro');
sub print_info
{
    my $self = shift;
    print "This file is at ", $self-&gt;path, "\n";
}
 

 <tt>&quot;Moose&quot;</tt> provides a number of features:
<dl>
<dt>&bull;
<dd> Declarative sugar 

 <tt>&quot;Moose&quot;</tt> provides a layer of declarative ``sugar'' for defining classes. That sugar is just a set of exported functions that make declaring how your class works simpler and more palatable. This lets you describe <i>what</i> your class is, rather than having to tell Perl <i>how</i> to implement your class. 

 The <tt>&quot;has()&quot;</tt> subroutine declares an attribute, and <tt>&quot;Moose&quot;</tt> automatically creates accessors for these attributes. It also takes care of creating a <tt>&quot;new()&quot;</tt> method for you. This constructor knows about the attributes you declared, so you can set them when creating a new <tt>&quot;File&quot;</tt>.
<dt>&bull;
<dd> Roles built-in 

 <tt>&quot;Moose&quot;</tt> lets you define roles the same way you define classes: 

 
package HasOnOffSwitch;
use Moose::Role;
has is_on = &gt; (is = &gt; 'rw',
               isa = &gt; 'Bool', );
sub turn_on
{
    my $self = shift;
    $self-&gt;is_on(1);
}
sub turn_off
{
    my $self = shift;
    $self-&gt;is_on(0);
}

<dt>&bull;
<dd> A miniature type system 

 In the example above, you can see that we passed <tt>&quot;isa =&gt; 'Bool'&quot;</tt> to <tt>&quot;has()&quot;</tt> when creating our <tt>&quot;is_on&quot;</tt> attribute. This tells <tt>&quot;Moose&quot;</tt> that this attribute must be a boolean value. If we try to set it to an invalid value, our code will throw an error.
<dt>&bull;
<dd> Full introspection and manipulation 

 Perl's built-in introspection features are fairly minimal. <tt>&quot;Moose&quot;</tt> builds on top of them and creates a full introspection layer for your classes. This lets you ask questions like ``what methods does the File class implement?'' It also lets you modify your classes programmatically.
<dt>&bull;
<dd> Self-hosted and extensible 

 <tt>&quot;Moose&quot;</tt> describes itself using its own introspection <font SIZE="-1">API.</font> Besides being a cool trick, this means that you can extend <tt>&quot;Moose&quot;</tt> using <tt>&quot;Moose&quot;</tt> itself.
<dt>&bull;
<dd> Rich ecosystem 

 There is a rich ecosystem of <tt>&quot;Moose&quot;</tt> extensions on <font SIZE="-1">CPAN</font> under the MooseX &lt;<a rel="nofollow" HREF="http://search.cpan.org/search?query=MooseX">http://search.cpan.org/search?query=MooseX</a>&amp;mode=dist&gt; namespace. In addition, many modules on <font SIZE="-1">CPAN</font> already use <tt>&quot;Moose&quot;</tt>, providing you with lots of examples to learn from.
<dt>&bull;
<dd> Many more features 

 <tt>&quot;Moose&quot;</tt> is a very powerful tool, and we can't cover all of its features here. We encourage you to learn more by reading the <tt>&quot;Moose&quot;</tt> documentation, starting with Moose::Manual &lt;<a rel="nofollow" HREF="http://search.cpan.org/perldoc?Moose::Manual">http://search.cpan.org/perldoc?Moose::Manual</a>&gt;.</dl>
 

 Of course, <tt>&quot;Moose&quot;</tt> isn't perfect. 

 <tt>&quot;Moose&quot;</tt> can make your code slower to load. <tt>&quot;Moose&quot;</tt> itself is not small, and it does a <i>lot</i> of code generation when you define your class. This code generation means that your runtime code is as fast as it can be, but you pay for this when your modules are first loaded. 

 This load time hit can be a problem when startup speed is important, such as with a command-line script or a ``plain vanilla'' <font SIZE="-1">CGI</font> script that must be loaded each time it is executed. 

 Before you panic, know that many people do use <tt>&quot;Moose&quot;</tt> for command-line tools and other startup-sensitive code. We encourage you to try <tt>&quot;Moose&quot;</tt> out first before worrying about startup speed. 

 <tt>&quot;Moose&quot;</tt> also has several dependencies on other modules. Most of these are small stand-alone modules, a number of which have been spun off from <tt>&quot;Moose&quot;</tt>. <tt>&quot;Moose&quot;</tt> itself, and some of its dependencies, require a compiler. If you need to install your software on a system without a compiler, or if having <i>any</i> dependencies is a problem, then <tt>&quot;Moose&quot;</tt> may not be right for you. 

 <i>Moo</i> 

 If you try <tt>&quot;Moose&quot;</tt> and find that one of these issues is preventing you from using <tt>&quot;Moose&quot;</tt>, we encourage you to consider Moo next. <tt>&quot;Moo&quot;</tt> implements a subset of <tt>&quot;Moose&quot;</tt>'s functionality in a simpler package. For most features that it does implement, the end-user <font SIZE="-1">API</font> is <i>identical</i> to <tt>&quot;Moose&quot;</tt>, meaning you can switch from <tt>&quot;Moo&quot;</tt> to <tt>&quot;Moose&quot;</tt> quite easily. 

 <tt>&quot;Moo&quot;</tt> does not implement most of <tt>&quot;Moose&quot;</tt>'s introspection <font SIZE="-1">API,</font> so it's often faster when loading your modules. Additionally, none of its dependencies require <font SIZE="-1">XS,</font> so it can be installed on machines without a compiler. 

 One of <tt>&quot;Moo&quot;</tt>'s most compelling features is its interoperability with <tt>&quot;Moose&quot;</tt>. When someone tries to use <tt>&quot;Moose&quot;</tt>'s introspection <font SIZE="-1">API</font> on a <tt>&quot;Moo&quot;</tt> class or role, it is transparently inflated into a <tt>&quot;Moose&quot;</tt> class or role. This makes it easier to incorporate <tt>&quot;Moo&quot;</tt>-using code into a <tt>&quot;Moose&quot;</tt> code base and vice versa. 

 For example, a <tt>&quot;Moose&quot;</tt> class can subclass a <tt>&quot;Moo&quot;</tt> class using <tt>&quot;extends&quot;</tt> or consume a <tt>&quot;Moo&quot;</tt> role using <tt>&quot;with&quot;</tt>. 

 The <tt>&quot;Moose&quot;</tt> authors hope that one day <tt>&quot;Moo&quot;</tt> can be made obsolete by improving <tt>&quot;Moose&quot;</tt> enough, but for now it provides a worthwhile alternative to <tt>&quot;Moose&quot;</tt>.

<h3>Class::Accessor</h3>

 Class::Accessor is the polar opposite of <tt>&quot;Moose&quot;</tt>. It provides very few features, nor is it self-hosting. 

 It is, however, very simple, pure Perl, and it has no non-core dependencies. It also provides a ``Moose-like'' <font SIZE="-1">API</font> on demand for the features it supports. 

 Even though it doesn't do much, it is still preferable to writing your own classes from scratch. 

 Here's our <tt>&quot;File&quot;</tt> class with <tt>&quot;Class::Accessor&quot;</tt>: 

 
package File;
use Class::Accessor 'antlers';
has path = &gt; (is = &gt; 'ro');
has content = &gt; (is = &gt; 'ro');
has last_mod_time = &gt; (is = &gt; 'ro');
sub print_info
{
    my $self = shift;
    print "This file is at ", $self-&gt;path, "\n";
}
 

 The <tt>&quot;antlers&quot;</tt> import flag tells <tt>&quot;Class::Accessor&quot;</tt> that you want to define your attributes using <tt>&quot;Moose&quot;</tt>-like syntax. The only parameter that you can pass to <tt>&quot;has&quot;</tt> is <tt>&quot;is&quot;</tt>. We recommend that you use this Moose-like syntax if you choose <tt>&quot;Class::Accessor&quot;</tt> since it means you will have a smoother upgrade path if you later decide to move to <tt>&quot;Moose&quot;</tt>. 

 Like <tt>&quot;Moose&quot;</tt>, <tt>&quot;Class::Accessor&quot;</tt> generates accessor methods and a constructor for your class.

<h3>Class::Tiny</h3>

 Finally, we have Class::Tiny. This module truly lives up to its name. It has an incredibly minimal <font SIZE="-1">API</font> and absolutely no dependencies on any recent Perl. Still, we think it's a lot easier to use than writing your own <font SIZE="-1">OO</font> code from scratch. 

 Here's our <tt>&quot;File&quot;</tt> class once more: 

 <pre><code>
package File;
use Class::Tiny qw(path content last_mod_time);
sub print_info
{
    my $self = shift;
    print "This file is at ", $self-&gt;path, "\n";
}
</code></pre> 

 That's it! 

 With <tt>&quot;Class::Tiny&quot;</tt>, all accessors are read-write. It generates a constructor for you, as well as the accessors you define. 

 You can also use Class::Tiny::Antlers for <tt>&quot;Moose&quot;</tt>-like syntax.

<h3>Role::Tiny</h3>

 As we mentioned before, roles provide an alternative to inheritance, but Perl does not have any built-in role support. If you choose to use Moose, it comes with a full-fledged role implementation. However, if you use one of our other recommended <font SIZE="-1">OO</font> modules, you can still use roles with Role::Tiny 

 <tt>&quot;Role::Tiny&quot;</tt> provides some of the same features as Moose's role system, but in a much smaller package. Most notably, it doesn't support any sort of attribute declaration, so you have to do that by hand. Still, it's useful, and works well with <tt>&quot;Class::Accessor&quot;</tt> and <tt>&quot;Class::Tiny&quot;</tt>

<h3><font SIZE="-1">OO</font> System Summary</h3>

 Here's a brief recap of the options we covered:
<dl>
<dt>&bull;
<dd> Moose 

 <tt>&quot;Moose&quot;</tt> is the maximal option. It has a lot of features, a big ecosystem, and a thriving user base. We also covered Moo briefly. <tt>&quot;Moo&quot;</tt> is <tt>&quot;Moose&quot;</tt> lite, and a reasonable alternative when Moose doesn't work for your application.
<dt>&bull;
<dd> Class::Accessor 

 <tt>&quot;Class::Accessor&quot;</tt> does a lot less than <tt>&quot;Moose&quot;</tt>, and is a nice alternative if you find <tt>&quot;Moose&quot;</tt> overwhelming. It's been around a long time and is well battle-tested. It also has a minimal <tt>&quot;Moose&quot;</tt> compatibility mode which makes moving from <tt>&quot;Class::Accessor&quot;</tt> to <tt>&quot;Moose&quot;</tt> easy.
<dt>&bull;
<dd> Class::Tiny 

 <tt>&quot;Class::Tiny&quot;</tt> is the absolute minimal option. It has no dependencies, and almost no syntax to learn. It's a good option for a super minimal environment and for throwing something together quickly without having to worry about details.
<dt>&bull;
<dd> Role::Tiny 

 Use <tt>&quot;Role::Tiny&quot;</tt> with <tt>&quot;Class::Accessor&quot;</tt> or <tt>&quot;Class::Tiny&quot;</tt> if you find yourself considering multiple inheritance. If you go with <tt>&quot;Moose&quot;</tt>, it comes with its own role implementation.</dl>

<h3>Other <font SIZE="-1">OO</font> Systems</h3>

 There are literally dozens of other OO-related modules on <font SIZE="-1">CPAN</font> besides those covered here, and you're likely to run across one or more of them if you work with other people's code. 

 In addition, plenty of code in the wild does all of its <font SIZE="-1">OO</font> ``by hand'', using just the Perl built-in <font SIZE="-1">OO</font> features. If you need to maintain such code, you should read perlobj to understand exactly how Perl's built-in <font SIZE="-1">OO</font> works.

<h2>CONCLUSION</h2>

 As we said before, Perl's minimal <font SIZE="-1">OO</font> system has led to a profusion of <font SIZE="-1">OO</font> systems on <font SIZE="-1">CPAN.</font> While you can still drop down to the bare metal and write your classes by hand, there's really no reason to do that with modern Perl. 

 For small systems, Class::Tiny and Class::Accessor both provide minimal object systems that take care of basic boilerplate for you. 

 For bigger projects, Moose provides a rich set of features that will let you focus on implementing your business logic. Moo provides a nice alternative to Moose when you want a lot of features but need faster compile time or to avoid <font SIZE="-1">XS.</font> 

 We encourage you to play with and evaluate Moose, Moo, Class::Accessor, and Class::Tiny to see which <font SIZE="-1">OO</font> system is right for you. 

<h2>Index</h2>



<dt><a HREF="#lbAP">PERL OO SYSTEMS</a>
<dd>


<dt><a HREF="#lbAW">CONCLUSION</a>
<dd></dl>

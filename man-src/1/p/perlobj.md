---
title: "perlobj(1)"
name: "perlobj"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlobj/"
---

<h2 class="name">NAME</h2>
 

 perlobj - Perl object reference 

<h2>DESCRIPTION</h2>

 This document provides a reference for Perl's object orientation features. If you're looking for an introduction to object-oriented programming in Perl, please see perlootut. 

 In order to understand Perl objects, you first need to understand references in Perl. See perlreftut for details. 

 This document describes all of Perl's object-oriented (<font SIZE="-1">OO</font>) features from the ground up. If you're just looking to write some object-oriented code of your own, you are probably better served by using one of the object systems from <font SIZE="-1">CPAN</font> described in perlootut. 

 If you're looking to write your own object system, or you need to maintain code which implements objects from scratch then this document will help you understand exactly how Perl does object orientation. 

 There are a few basic principles which define object oriented Perl:
<dl>
<dt>1.
<dd> An object is simply a data structure that knows to which class it belongs.
<dt>2.
<dd> A class is simply a package. A class provides methods that expect to operate on objects.
<dt>3.
<dd> A method is simply a subroutine that expects a reference to an object (or a package name, for class methods) as the first argument.</dl>
 

 Let's look at each of these principles in depth.

<h3>An Object is Simply a Data Structure</h3>

 Unlike many other languages which support object orientation, Perl does not provide any special syntax for constructing an object. Objects are merely Perl data structures (hashes, arrays, scalars, filehandles, etc.) that have been explicitly associated with a particular class. 

 That explicit association is created by the built-in <tt>&quot;bless&quot;</tt> function, which is typically used within the <i>constructor</i> subroutine of the class. 

 Here is a simple constructor: 

 <pre><code>
package File;
sub new
{
    my $class = shift;
    return bless{}, $class;
}
</code></pre> 

 The name <tt>&quot;new&quot;</tt> isn't special. We could name our constructor something else: 

 
package File;
sub load
{
    my $class = shift;
    return bless{}, $class;
}
 

 The modern convention for <font SIZE="-1">OO</font> modules is to always use <tt>&quot;new&quot;</tt> as the name for the constructor, but there is no requirement to do so. Any subroutine that blesses a data structure into a class is a valid constructor in Perl. 

 In the previous examples, the <tt>&quot;{}&quot;</tt> code creates a reference to an empty anonymous hash. The <tt>&quot;bless&quot;</tt> function then takes that reference and associates the hash with the class in <tt>$class</tt>. In the simplest case, the <tt>$class</tt> variable will end up containing the string ``File''. 

 We can also use a variable to store a reference to the data structure that is being blessed as our object: 

 
sub new
{
    my $class = shift;
    my $self = {};
    bless $self, $class;
    return $self;
}
 

 Once we've blessed the hash referred to by <tt>$self</tt> we can start calling methods on it. This is useful if you want to put object initialization in its own separate method: 

 
sub new
{
    my $class = shift;
    my $self = {};
    bless $self, $class;
    $self-&gt;_initialize();
    return $self;
}
 

 Since the object is also a hash, you can treat it as one, using it to store data associated with the object. Typically, code inside the class can treat the hash as an accessible data structure, while code outside the class should always treat the object as opaque. This is called <b>encapsulation</b>. Encapsulation means that the user of an object does not have to know how it is implemented. The user simply calls documented methods on the object. 

 Note, however, that (unlike most other <font SIZE="-1">OO</font> languages) Perl does not ensure or enforce encapsulation in any way. If you want objects to actually <i>be</i> opaque you need to arrange for that yourself. This can be done in a variety of ways, including using ``Inside-Out objects'' or modules from <font SIZE="-1">CPAN.</font> 

 <i>Objects Are Blessed; Variables Are Not</i> 

 When we bless something, we are not blessing the variable which contains a reference to that thing, nor are we blessing the reference that the variable stores; we are blessing the thing that the variable refers to (sometimes known as the <i>referent</i>). This is best demonstrated with this code: 

 
use Scalar::Util 'blessed';
my $foo = {};
my $bar = $foo;
bless $foo, 'Class';
print blessed($bar) // 'not blessed';    # prints "Class"
    $bar = "some other value";
print blessed($bar) // 'not blessed';    # prints "not blessed"
 

 When we call <tt>&quot;bless&quot;</tt> on a variable, we are actually blessing the underlying data structure that the variable refers to. We are not blessing the reference itself, nor the variable that contains that reference. That's why the second call to <tt>&quot;blessed( $bar )&quot;</tt> returns false. At that point <tt>$bar</tt> is no longer storing a reference to an object. 

 You will sometimes see older books or documentation mention ``blessing a reference'' or describe an object as a ``blessed reference'', but this is incorrect. It isn't the reference that is blessed as an object; it's the thing the reference refers to (i.e. the referent).

<h3>A Class is Simply a Package</h3>

 Perl does not provide any special syntax for class definitions. A package is simply a namespace containing variables and subroutines. The only difference is that in a class, the subroutines may expect a reference to an object or the name of a class as the first argument. This is purely a matter of convention, so a class may contain both methods and subroutines which <i>don't</i> operate on an object or class. 

 Each package contains a special array called <tt>@ISA</tt>. The <tt>@ISA</tt> array contains a list of that class's parent classes, if any. This array is examined when Perl does method resolution, which we will cover later. 

 Calling methods from a package means it must be loaded, of course, so you will often want to load a module and add it to <tt>@ISA</tt> at the same time. You can do so in a single step using the parent pragma. (In older code you may encounter the base pragma, which is nowadays discouraged except when you have to work with the equally discouraged fields pragma.) 

 However the parent classes are set, the package's <tt>@ISA</tt> variable will contain a list of those parents. This is simply a list of scalars, each of which is a string that corresponds to a package name. 

 All classes inherit from the <font SIZE="-1">UNIVERSAL</font> class implicitly. The <font SIZE="-1">UNIVERSAL</font> class is implemented by the Perl core, and provides several default methods, such as <tt>&quot;isa()&quot;</tt>, <tt>&quot;can()&quot;</tt>, and <tt>&quot;VERSION()&quot;</tt>. The <tt>&quot;UNIVERSAL&quot;</tt> class will <i>never</i> appear in a package's <tt>@ISA</tt> variable. 

 Perl <i>only</i> provides method inheritance as a built-in feature. Attribute inheritance is left up the class to implement. See the ``Writing Accessors'' section for details.

<h3>A Method is Simply a Subroutine</h3>

 Perl does not provide any special syntax for defining a method. A method is simply a regular subroutine, and is declared with <tt>&quot;sub&quot;</tt>. What makes a method special is that it expects to receive either an object or a class name as its first argument. 

 Perl <i>does</i> provide special syntax for method invocation, the <tt>&quot;-&gt;&quot;</tt> operator. We will cover this in more detail later. 

 Most methods you write will expect to operate on objects: 

 
sub save
{
    my $self = shift;
    open my $fh, '&gt;', $self-&gt;path() or die $ !;
    print{$fh} $self-&gt;data() or die $ !;
    close $fh or die $ !;
}


<h3>Method Invocation</h3>

 Calling a method on an object is written as <tt>&quot;$object-&gt;method&quot;</tt>. 

 The left hand side of the method invocation (or arrow) operator is the object (or class name), and the right hand side is the method name. 

 
my $pod = File-&gt;new ('perlobj.pod', $data);
$pod-&gt;save();
 

 The <tt>&quot;-&gt;&quot;</tt> syntax is also used when dereferencing a reference. It looks like the same operator, but these are two different operations. 

 When you call a method, the thing on the left side of the arrow is passed as the first argument to the method. That means when we call <tt>&quot;Critter-&gt;new()&quot;</tt>, the <tt>&quot;new()&quot;</tt> method receives the string <tt>&quot;Critter&quot;</tt> as its first argument. When we call <tt>&quot;$fred-&gt;speak()&quot;</tt>, the <tt>$fred</tt> variable is passed as the first argument to <tt>&quot;speak()&quot;</tt>. 

 Just as with any Perl subroutine, all of the arguments passed in <tt>@_</tt> are aliases to the original argument. This includes the object itself. If you assign directly to <tt>$_[0]</tt> you will change the contents of the variable that holds the reference to the object. We recommend that you don't do this unless you know exactly what you're doing. 

 Perl knows what package the method is in by looking at the left side of the arrow. If the left hand side is a package name, it looks for the method in that package. If the left hand side is an object, then Perl looks for the method in the package that the object has been blessed into. 

 If the left hand side is neither a package name nor an object, then the method call will cause an error, but see the section on ``Method Call Variations'' for more nuances.

<h3>Inheritance</h3>

 We already talked about the special <tt>@ISA</tt> array and the parent pragma. 

 When a class inherits from another class, any methods defined in the parent class are available to the child class. If you attempt to call a method on an object that isn't defined in its own class, Perl will also look for that method in any parent classes it may have. 

 
package File::MP3;
use parent 'File';
#sets @File::MP3::ISA = ('File');
my $mp3 = File::MP3-&gt;new ('Andvari.mp3', $data);
$mp3-&gt;save();
 

 Since we didn't define a <tt>&quot;save()&quot;</tt> method in the <tt>&quot;File::MP3&quot;</tt> class, Perl will look at the <tt>&quot;File::MP3&quot;</tt> class's parent classes to find the <tt>&quot;save()&quot;</tt> method. If Perl cannot find a <tt>&quot;save()&quot;</tt> method anywhere in the inheritance hierarchy, it will die. 

 In this case, it finds a <tt>&quot;save()&quot;</tt> method in the <tt>&quot;File&quot;</tt> class. Note that the object passed to <tt>&quot;save()&quot;</tt> in this case is still a <tt>&quot;File::MP3&quot;</tt> object, even though the method is found in the <tt>&quot;File&quot;</tt> class. 

 We can override a parent's method in a child class. When we do so, we can still call the parent class's method with the <tt>&quot;SUPER&quot;</tt> pseudo-class. 

 
sub save
{
    my $self = shift;
    say 'Prepare to rock';
    $self-&gt;SUPER::save();
}
 

 The <tt>&quot;SUPER&quot;</tt> modifier can <i>only</i> be used for method calls. You can't use it for regular subroutine calls or class methods: 

 
SUPER::save($thing);
#FAIL : looks for save() sub in package SUPER
    SUPER-&gt;save($thing);
#FAIL : looks for save() method in class
#SUPER
    $thing-&gt;SUPER::save();
#Okay : looks for save() method in parent
#classes
 

 <i>How </i><font SIZE="-1"><i>SUPER</i></font><i> is Resolved</i> 

 The <tt>&quot;SUPER&quot;</tt> pseudo-class is resolved from the package where the call is made. It is <i>not</i> resolved based on the object's class. This is important, because it lets methods at different levels within a deep inheritance hierarchy each correctly call their respective parent methods. 

 
package A;
sub new
{
    return bless{}, shift;
}
sub speak
{
    my $self = shift;
    say 'A';
}
package B;
use parent - norequire, 'A';
sub speak
{
    my $self = shift;
    $self-&gt;SUPER::speak();
    say 'B';
}
package C;
use parent - norequire, 'B';
sub speak
{
    my $self = shift;
    $self-&gt;SUPER::speak();
    say 'C';
}
my $c = C-&gt;new ();
$c-&gt;speak();
 

 In this example, we will get the following output: 

 <pre>
  A
  B
  C
</pre> 

 This demonstrates how <tt>&quot;SUPER&quot;</tt> is resolved. Even though the object is blessed into the <tt>&quot;C&quot;</tt> class, the <tt>&quot;speak()&quot;</tt> method in the <tt>&quot;B&quot;</tt> class can still call <tt>&quot;SUPER::speak()&quot;</tt> and expect it to correctly look in the parent class of <tt>&quot;B&quot;</tt> (i.e the class the method call is in), not in the parent class of <tt>&quot;C&quot;</tt> (i.e. the class the object belongs to). 

 There are rare cases where this package-based resolution can be a problem. If you copy a subroutine from one package to another, <tt>&quot;SUPER&quot;</tt> resolution will be done based on the original package. 

 <i>Multiple Inheritance</i> 

 Multiple inheritance often indicates a design problem, but Perl always gives you enough rope to hang yourself with if you ask for it. 

 To declare multiple parents, you simply need to pass multiple class names to <tt>&quot;use parent&quot;</tt>: 

 <pre>
  package MultiChild;
  use parent 'Parent1', 'Parent2';
</pre> 

 <i>Method Resolution Order</i> 

 Method resolution order only matters in the case of multiple inheritance. In the case of single inheritance, Perl simply looks up the inheritance chain to find a method: 

 <pre>
  Grandparent
    |
  Parent
    |
  Child
</pre> 

 If we call a method on a <tt>&quot;Child&quot;</tt> object and that method is not defined in the <tt>&quot;Child&quot;</tt> class, Perl will look for that method in the <tt>&quot;Parent&quot;</tt> class and then, if necessary, in the <tt>&quot;Grandparent&quot;</tt> class. 

 If Perl cannot find the method in any of these classes, it will die with an error message. 

 When a class has multiple parents, the method lookup order becomes more complicated. 

 By default, Perl does a depth-first left-to-right search for a method. That means it starts with the first parent in the <tt>@ISA</tt> array, and then searches all of its parents, grandparents, etc. If it fails to find the method, it then goes to the next parent in the original class's <tt>@ISA</tt> array and searches from there. 

 <pre>
            SharedGreatGrandParent
            /                    \
  PaternalGrandparent       MaternalGrandparent
            \                    /
             Father        Mother
                   \      /
                    Child
</pre> 

 So given the diagram above, Perl will search <tt>&quot;Child&quot;</tt>, <tt>&quot;Father&quot;</tt>, <tt>&quot;PaternalGrandparent&quot;</tt>, <tt>&quot;SharedGreatGrandParent&quot;</tt>, <tt>&quot;Mother&quot;</tt>, and finally <tt>&quot;MaternalGrandparent&quot;</tt>. This may be a problem because now we're looking in <tt>&quot;SharedGreatGrandParent&quot;</tt> <i>before</i> we've checked all its derived classes (i.e. before we tried <tt>&quot;Mother&quot;</tt> and <tt>&quot;MaternalGrandparent&quot;</tt>). 

 It is possible to ask for a different method resolution order with the mro pragma. 

 <pre>
  package Child;
  use mro 'c3';
  use parent 'Father', 'Mother';
</pre> 

 This pragma lets you switch to the ``C3'' resolution order. In simple terms, ``C3'' order ensures that shared parent classes are never searched before child classes, so Perl will now search: <tt>&quot;Child&quot;</tt>, <tt>&quot;Father&quot;</tt>, <tt>&quot;PaternalGrandparent&quot;</tt>, <tt>&quot;Mother&quot;</tt> <tt>&quot;MaternalGrandparent&quot;</tt>, and finally <tt>&quot;SharedGreatGrandParent&quot;</tt>. Note however that this is not ``breadth-first'' searching: All the <tt>&quot;Father&quot;</tt> ancestors (except the common ancestor) are searched before any of the <tt>&quot;Mother&quot;</tt> ancestors are considered. 

 The C3 order also lets you call methods in sibling classes with the <tt>&quot;next&quot;</tt> pseudo-class. See the mro documentation for more details on this feature. 

 <i>Method Resolution Caching</i> 

 When Perl searches for a method, it caches the lookup so that future calls to the method do not need to search for it again. Changing a class's parent class or adding subroutines to a class will invalidate the cache for that class. 

 The mro pragma provides some functions for manipulating the method cache directly.

<h3>Writing Constructors</h3>

 As we mentioned earlier, Perl provides no special constructor syntax. This means that a class must implement its own constructor. A constructor is simply a class method that returns a reference to a new object. 

 The constructor can also accept additional parameters that define the object. Let's write a real constructor for the <tt>&quot;File&quot;</tt> class we used earlier: 

 
package File;
sub new
{
    my $class = shift;
    my($path, $data) = @_;
    my $self = bless{
           path = &gt; $path,
           data = &gt; $data,
       },
       $class;
    return $self;
}
 

 As you can see, we've stored the path and file data in the object itself. Remember, under the hood, this object is still just a hash. Later, we'll write accessors to manipulate this data. 

 For our <tt>&quot;File::MP3&quot;</tt> class, we can check to make sure that the path we're given ends with ``.mp3'': 

 
package File::MP3;
sub new
{
    my $class = shift;
    my($path, $data) = @_;
    die "You cannot create a File::MP3 without an mp3 extension\n" unless $path = ~ /\.mp3\z / ;
    return $class-&gt;SUPER::new (@_);
}
 

 This constructor lets its parent class do the actual object construction.

<h3>Attributes</h3>

 An attribute is a piece of data belonging to a particular object. Unlike most object-oriented languages, Perl provides no special syntax or support for declaring and manipulating attributes. 

 Attributes are often stored in the object itself. For example, if the object is an anonymous hash, we can store the attribute values in the hash using the attribute name as the key. 

 While it's possible to refer directly to these hash keys outside of the class, it's considered a best practice to wrap all access to the attribute with accessor methods. 

 This has several advantages. Accessors make it easier to change the implementation of an object later while still preserving the original <font SIZE="-1">API.</font> 

 An accessor lets you add additional code around attribute access. For example, you could apply a default to an attribute that wasn't set in the constructor, or you could validate that a new value for the attribute is acceptable. 

 Finally, using accessors makes inheritance much simpler. Subclasses can use the accessors rather than having to know how a parent class is implemented internally. 

 <i>Writing Accessors</i> 

 As with constructors, Perl provides no special accessor declaration syntax, so classes must provide explicitly written accessor methods. There are two common types of accessors, read-only and read-write. 

 A simple read-only accessor simply gets the value of a single attribute: 

 
sub path
{
    my $self = shift;
    return $self-&gt;{path};
}
 

 A read-write accessor will allow the caller to set the value as well as get it: 

 
sub path
{
    my $self = shift;
    if (@_) {
        $self-&gt;{path} = shift;
    }
    return $self-&gt;{path};
}


<h3>An Aside About Smarter and Safer Code</h3>

 Our constructor and accessors are not very smart. They don't check that a <tt>$path</tt> is defined, nor do they check that a <tt>$path</tt> is a valid filesystem path. 

 Doing these checks by hand can quickly become tedious. Writing a bunch of accessors by hand is also incredibly tedious. There are a lot of modules on <font SIZE="-1">CPAN</font> that can help you write safer and more concise code, including the modules we recommend in perlootut.

<h3>Method Call Variations</h3>

 Perl supports several other ways to call methods besides the <tt>&quot;$object-&gt;method()&quot;</tt> usage we've seen so far. 

 <i>Method Names with a Fully Qualified Name</i> 

 Perl allows you to call methods using their fully qualified name (the package and method name): 

 
my $mp3 = File::MP3-&gt;new ('Regin.mp3', $data);
$mp3-&gt;File::save();
 

 When you call a fully qualified method name like <tt>&quot;File::save&quot;</tt>, the method resolution search for the <tt>&quot;save&quot;</tt> method starts in the <tt>&quot;File&quot;</tt> class, skipping any <tt>&quot;save&quot;</tt> method the <tt>&quot;File::MP3&quot;</tt> class may have defined. It still searches the <tt>&quot;File&quot;</tt> class's parents if necessary. 

 While this feature is most commonly used to explicitly call methods inherited from an ancestor class, there is no technical restriction that enforces this: 

 
my $obj = Tree-&gt;new ();
$obj-&gt;Dog::bark();
 

 This calls the <tt>&quot;bark&quot;</tt> method from class <tt>&quot;Dog&quot;</tt> on an object of class <tt>&quot;Tree&quot;</tt>, even if the two classes are completely unrelated. Use this with great care. 

 The <tt>&quot;SUPER&quot;</tt> pseudo-class that was described earlier is <i>not</i> the same as calling a method with a fully-qualified name. See the earlier ``Inheritance'' section for details. 

 <i>Method Names as Strings</i> 

 Perl lets you use a scalar variable containing a string as a method name: 

 
my $file = File-&gt;new ($path, $data);
my $method = 'save';
$file-&gt;$method();
 

 This works exactly like calling <tt>&quot;$file-&gt;save()&quot;</tt>. This can be very useful for writing dynamic code. For example, it allows you to pass a method name to be called as a parameter to another method. 

 <i>Class Names as Strings</i> 

 Perl also lets you use a scalar containing a string as a class name: 

 
my $class = 'File';
my $file = $class-&gt;new ($path, $data);
 

 Again, this allows for very dynamic code. 

 <i>Subroutine References as Methods</i> 

 You can also use a subroutine reference as a method: 

 
my $sub = sub
{
    my $self = shift;
    $self-&gt;save();
};
$file-&gt;$sub();
 

 This is exactly equivalent to writing <tt>&quot;$sub-&gt;($file)&quot;</tt>. You may see this idiom in the wild combined with a call to <tt>&quot;can&quot;</tt>: 

 
if (my $meth = $object-&gt;can('foo')) {
    $object-&gt;$meth();
}
 

 <i>Dereferencing Method Call</i> 

 Perl also lets you use a dereferenced scalar reference in a method call. That's a mouthful, so let's look at some code: 

 
$file-&gt;${ \'save'};
$file-&gt;${returns_scalar_ref()};
$file-&gt;${ \(returns_scalar())};
$file-&gt;${returns_ref_to_sub_ref()};
 

 This works if the dereference produces a string <i>or</i> a subroutine reference. 

 <i>Method Calls on Filehandles</i> 

 Under the hood, Perl filehandles are instances of the <tt>&quot;IO::Handle&quot;</tt> or <tt>&quot;IO::File&quot;</tt> class. Once you have an open filehandle, you can call methods on it. Additionally, you can call methods on the <tt>&quot;STDIN&quot;</tt>, <tt>&quot;STDOUT&quot;</tt>, and <tt>&quot;STDERR&quot;</tt> filehandles. 

 
open my $fh, '&gt;', 'path/to/file';
$fh-&gt;autoflush();
$fh-&gt;print('content');
STDOUT-&gt;autoflush();


<h3>Invoking Class Methods</h3>

 Because Perl allows you to use barewords for package names and subroutine names, it sometimes interprets a bareword's meaning incorrectly. For example, the construct <tt>&quot;Class-&gt;new()&quot;</tt> can be interpreted as either <tt>&quot;'Class'-&gt;new()&quot;</tt> or <tt>&quot;Class()-&gt;new()&quot;</tt>. In English, that second interpretation reads as ``call a subroutine named <b>Class()</b>, then call <b>new()</b> as a method on the return value of <b>Class()</b>''. If there is a subroutine named <tt>&quot;Class()&quot;</tt> in the current namespace, Perl will always interpret <tt>&quot;Class-&gt;new()&quot;</tt> as the second alternative: a call to <tt>&quot;new()&quot;</tt> on the object returned by a call to <tt>&quot;Class()&quot;</tt> 

 You can force Perl to use the first interpretation (i.e. as a method call on the class named ``Class'') in two ways. First, you can append a <tt>&quot;::&quot;</tt> to the class name: 

 <pre>
    Class::-&gt;new()
</pre> 

 Perl will always interpret this as a method call. 

 Alternatively, you can quote the class name: 

 <pre>
    'Class'-&gt;new()
</pre> 

 Of course, if the class name is in a scalar Perl will do the right thing as well: 

 
my $class = 'Class';
$class-&gt;new ();
 

 <i>Indirect Object Syntax</i> 

 <b>Outside of the file handle case, use of this syntax is discouraged as it can confuse the Perl interpreter. See below for more details.</b> 

 Perl supports another method invocation syntax called ``indirect object'' notation. This syntax is called ``indirect'' because the method comes before the object it is being invoked on. 

 This syntax can be used with any class or object method: 

 <pre>
    my $file = new File $path, $data;
    save $file;
</pre> 

 We recommend that you avoid this syntax, for several reasons. 

 First, it can be confusing to read. In the above example, it's not clear if <tt>&quot;save&quot;</tt> is a method provided by the <tt>&quot;File&quot;</tt> class or simply a subroutine that expects a file object as its first argument. 

 When used with class methods, the problem is even worse. Because Perl allows subroutine names to be written as barewords, Perl has to guess whether the bareword after the method is a class name or subroutine name. In other words, Perl can resolve the syntax as either <tt>&quot;File-&gt;new( $path, $data )&quot;</tt> <b>or</b> <tt>&quot;new( File( $path, $data ) )&quot;</tt>. 

 To parse this code, Perl uses a heuristic based on what package names it has seen, what subroutines exist in the current package, what barewords it has previously seen, and other input. Needless to say, heuristics can produce very surprising results! 

 Older documentation (and some <font SIZE="-1">CPAN</font> modules) encouraged this syntax, particularly for constructors, so you may still find it in the wild. However, we encourage you to avoid using it in new code. 

 You can force Perl to interpret the bareword as a class name by appending ``::'' to it, like we saw earlier: 

 <pre>
  my $file = new File:: $path, $data;
</pre>

<h3>bless, blessed, and ref</h3>

 As we saw earlier, an object is simply a data structure that has been blessed into a class via the <tt>&quot;bless&quot;</tt> function. The <tt>&quot;bless&quot;</tt> function can take either one or two arguments: 

 
my $object = bless{}, $class;
my $object = bless{};
 

 In the first form, the anonymous hash is being blessed into the class in <tt>$class</tt>. In the second form, the anonymous hash is blessed into the current package. 

 The second form is strongly discouraged, because it breaks the ability of a subclass to reuse the parent's constructor, but you may still run across it in existing code. 

 If you want to know whether a particular scalar refers to an object, you can use the <tt>&quot;blessed&quot;</tt> function exported by Scalar::Util, which is shipped with the Perl core. 

 
use Scalar::Util 'blessed';
if (defined blessed($thing)) {
    ...
}
 

 If <tt>$thing</tt> refers to an object, then this function returns the name of the package the object has been blessed into. If <tt>$thing</tt> doesn't contain a reference to a blessed object, the <tt>&quot;blessed&quot;</tt> function returns <tt>&quot;undef&quot;</tt>. 

 Note that <tt>&quot;blessed($thing)&quot;</tt> will also return false if <tt>$thing</tt> has been blessed into a class named ``0''. This is a possible, but quite pathological. Don't create a class named ``0'' unless you know what you're doing. 

 Similarly, Perl's built-in <tt>&quot;ref&quot;</tt> function treats a reference to a blessed object specially. If you call <tt>&quot;ref($thing)&quot;</tt> and <tt>$thing</tt> holds a reference to an object, it will return the name of the class that the object has been blessed into. 

 If you simply want to check that a variable contains an object reference, we recommend that you use <tt>&quot;defined blessed($object)&quot;</tt>, since <tt>&quot;ref&quot;</tt> returns true values for all references, not just objects.

<h3>The <font SIZE="-1">UNIVERSAL</font> Class</h3>

 All classes automatically inherit from the <font SIZE="-1">UNIVERSAL</font> class, which is built-in to the Perl core. This class provides a number of methods, all of which can be called on either a class or an object. You can also choose to override some of these methods in your class. If you do so, we recommend that you follow the built-in semantics described below.
<dl>
<dt>isa($class)
<dd> The <tt>&quot;isa&quot;</tt> method returns <i>true</i> if the object is a member of the class in <tt>$class</tt>, or a member of a subclass of <tt>$class</tt>. 

 If you override this method, it should never throw an exception.
<dt><font SIZE="-1">DOES</font>($role)
<dd> The <tt>&quot;DOES&quot;</tt> method returns <i>true</i> if its object claims to perform the role <tt>$role</tt>. By default, this is equivalent to <tt>&quot;isa&quot;</tt>. This method is provided for use by object system extensions that implement roles, like <tt>&quot;Moose&quot;</tt> and <tt>&quot;Role::Tiny&quot;</tt>. 

 You can also override <tt>&quot;DOES&quot;</tt> directly in your own classes. If you override this method, it should never throw an exception.
<dt>can($method)
<dd> The <tt>&quot;can&quot;</tt> method checks to see if the class or object it was called on has a method named <tt>$method</tt>. This checks for the method in the class and all of its parents. If the method exists, then a reference to the subroutine is returned. If it does not then <tt>&quot;undef&quot;</tt> is returned. 

 If your class responds to method calls via <tt>&quot;AUTOLOAD&quot;</tt>, you may want to overload <tt>&quot;can&quot;</tt> to return a subroutine reference for methods which your <tt>&quot;AUTOLOAD&quot;</tt> method handles. 

 If you override this method, it should never throw an exception.
<dt><font SIZE="-1">VERSION</font>($need)
<dd> The <tt>&quot;VERSION&quot;</tt> method returns the version number of the class (package). 

 If the <tt>$need</tt> argument is given then it will check that the current version (as defined by the <tt>$VERSION</tt> variable in the package) is greater than or equal to <tt>$need</tt>; it will die if this is not the case. This method is called automatically by the <tt>&quot;VERSION&quot;</tt> form of <tt>&quot;use&quot;</tt>. 

 
use Package 1.2 qw(some imported subs);
#implies:
Package-&gt;VERSION(1.2);
 

 We recommend that you use this method to access another package's version, rather than looking directly at <tt>$Package::VERSION</tt>. The package you are looking at could have overridden the <tt>&quot;VERSION&quot;</tt> method. 

 We also recommend using this method to check whether a module has a sufficient version. The internal implementation uses the version module to make sure that different types of version numbers are compared correctly.</dl>

<h3><font SIZE="-1">AUTOLOAD</font></h3>

 If you call a method that doesn't exist in a class, Perl will throw an error. However, if that class or any of its parent classes defines an <tt>&quot;AUTOLOAD&quot;</tt> method, that <tt>&quot;AUTOLOAD&quot;</tt> method is called instead. 

 <tt>&quot;AUTOLOAD&quot;</tt> is called as a regular method, and the caller will not know the difference. Whatever value your <tt>&quot;AUTOLOAD&quot;</tt> method returns is returned to the caller. 

 The fully qualified method name that was called is available in the <tt>$AUTOLOAD</tt> package global for your class. Since this is a global, if you want to refer to do it without a package name prefix under <tt>&quot;strict 'vars'&quot;</tt>, you need to declare it. 

 
#XXX - this is a terrible way to implement accessors, but it makes
#for a simple example.
our $AUTOLOAD;
sub AUTOLOAD
{
    my $self = shift;
#Remove qualifier from original method name...
    my $called = $AUTOLOAD = ~s /.*:: // r;
#Is there an attribute of that name ?
                                     die "No such attribute: $called" unless exists $self-&gt;{$called};
#If so, return it...
    return $self-&gt;{$called};
}
sub DESTROY
{
}
#see below
 

 Without the <tt>&quot;our $AUTOLOAD&quot;</tt> declaration, this code will not compile under the strict pragma. 

 As the comment says, this is not a good way to implement accessors. It's slow and too clever by far. However, you may see this as a way to provide accessors in older Perl code. See perlootut for recommendations on <font SIZE="-1">OO</font> coding in Perl. 

 If your class does have an <tt>&quot;AUTOLOAD&quot;</tt> method, we strongly recommend that you override <tt>&quot;can&quot;</tt> in your class as well. Your overridden <tt>&quot;can&quot;</tt> method should return a subroutine reference for any method that your <tt>&quot;AUTOLOAD&quot;</tt> responds to.

<h3>Destructors</h3>

 When the last reference to an object goes away, the object is destroyed. If you only have one reference to an object stored in a lexical scalar, the object is destroyed when that scalar goes out of scope. If you store the object in a package global, that object may not go out of scope until the program exits. 

 If you want to do something when the object is destroyed, you can define a <tt>&quot;DESTROY&quot;</tt> method in your class. This method will always be called by Perl at the appropriate time, unless the method is empty. 

 This is called just like any other method, with the object as the first argument. It does not receive any additional arguments. However, the <tt>$_[0]</tt> variable will be read-only in the destructor, so you cannot assign a value to it. 

 If your <tt>&quot;DESTROY&quot;</tt> method throws an exception, this will not cause any control transfer beyond exiting the method. The exception will be reported to <tt>&quot;STDERR&quot;</tt> as a warning, marked ``(in cleanup)'', and Perl will continue with whatever it was doing before. 

 Because <tt>&quot;DESTROY&quot;</tt> methods can be called at any time, you should localize any global status variables that might be set by anything you do in your <tt>&quot;DESTROY&quot;</tt> method. If you are in doubt about a particular status variable, it doesn't hurt to localize it. There are five global status variables, and the safest way is to localize all five of them: 

 
sub DESTROY
{
      local($., $@, $!, $^E, $?);
      my $self = shift;
      ...;
}
 

 If you define an <tt>&quot;AUTOLOAD&quot;</tt> in your class, then Perl will call your <tt>&quot;AUTOLOAD&quot;</tt> to handle the <tt>&quot;DESTROY&quot;</tt> method. You can prevent this by defining an empty <tt>&quot;DESTROY&quot;</tt>, like we did in the autoloading example. You can also check the value of <tt>$AUTOLOAD</tt> and return without doing anything when called to handle <tt>&quot;DESTROY&quot;</tt>. 

 <i>Global Destruction</i> 

 The order in which objects are destroyed during the global destruction before the program exits is unpredictable. This means that any objects contained by your object may already have been destroyed. You should check that a contained object is defined before calling a method on it: 

 
sub DESTROY
{
    my $self = shift;
    $self-&gt;
    {
        handle
        } -&gt; close() if $self-&gt;{handle};
}
 

 You can use the <tt>&quot;${^GLOBAL_PHASE}&quot;</tt> variable to detect if you are currently in the global destruction phase: 

 
sub DESTROY
{
    my $self = shift;
    return if ${^GLOBAL_PHASE} eq 'DESTRUCT';
    $self-&gt;
    {
        handle
        } -&gt; close();
}
 

 Note that this variable was added in Perl 5.14.0. If you want to detect the global destruction phase on older versions of Perl, you can use the <tt>&quot;Devel::GlobalDestruction&quot;</tt> module on <font SIZE="-1">CPAN.</font> 

 If your <tt>&quot;DESTROY&quot;</tt> method issues a warning during global destruction, the Perl interpreter will append the string `` during global destruction'' to the warning. 

 During global destruction, Perl will always garbage collect objects before unblessed references. See ``<font SIZE="-1">PERL_DESTRUCT_LEVEL''</font> in perlhacktips for more information about global destruction.

<h3>Non-Hash Objects</h3>

 All the examples so far have shown objects based on a blessed hash. However, it's possible to bless any type of data structure or referent, including scalars, globs, and subroutines. You may see this sort of thing when looking at code in the wild. 

 Here's an example of a module as a blessed scalar: 

 
package Time;
use strict;
use warnings;
sub new
{
    my $class = shift;
    my $time = time;
    return bless \$time, $class;
}
sub epoch
{
    my $self = shift;
    return ${$self};
}
my $time = Time-&gt;new ();
print $time-&gt;epoch();


<h3>Inside-Out objects</h3>

 In the past, the Perl community experimented with a technique called ``inside-out objects''. An inside-out object stores its data outside of the object's reference, indexed on a unique property of the object, such as its memory address, rather than in the object itself. This has the advantage of enforcing the encapsulation of object attributes, since their data is not stored in the object itself. 

 This technique was popular for a while (and was recommended in Damian Conway's <i>Perl Best Practices</i>), but never achieved universal adoption. The Object::InsideOut module on <font SIZE="-1">CPAN</font> provides a comprehensive implementation of this technique, and you may see it or other inside-out modules in the wild. 

 Here is a simple example of the technique, using the Hash::Util::FieldHash core module. This module was added to the core to support inside-out object implementations. 

 <pre><code>
package Time;
use strict;
use warnings;
use Hash::Util::FieldHash 'fieldhash';
fieldhash my % time_for;
sub new
{
    my $class = shift;
    my $self = bless \(my $object), $class;
    $time_for{$self} = time;
    return $self;
}
sub epoch
{
    my $self = shift;
    return $time_for{$self};
}
my $time = Time-&gt;new;
print $time-&gt;epoch;
</code></pre>

<h3>Pseudo-hashes</h3>

 The pseudo-hash feature was an experimental feature introduced in earlier versions of Perl and removed in 5.10.0. A pseudo-hash is an array reference which can be accessed using named keys like a hash. You may run in to some code in the wild which uses it. See the fields pragma for more information.

<h2>SEE ALSO</h2>

 A kinder, gentler tutorial on object-oriented programming in Perl can be found in perlootut. You should also check out perlmodlib for some style guides on constructing both modules and classes. 

<h2>Index</h2>



<dt><a HREF="#lbAU">SEE ALSO</a>
<dd></dl>

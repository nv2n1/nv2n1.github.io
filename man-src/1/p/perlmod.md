---
title: "perlmod(1)"
name: "perlmod"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlmod/"
---

<h2 class="name">NAME</h2>
 

 perlmod - Perl modules (packages and symbol tables) 

<h2>DESCRIPTION</h2>

<h3>Is this the document you were after?</h3>

 There are other documents which might contain the information that you're looking for:
<dl>
<dt>This doc
<dd> Perl's packages, namespaces, and some info on classes.
<dt>perlnewmod
<dd> Tutorial on making a new module.
<dt>perlmodstyle
<dd> Best practices for making a new module.</dl>

<h3>Packages</h3>

 Unlike Perl 4, in which all the variables were dynamic and shared one global name space, causing maintainability problems, Perl 5 provides two mechanisms for protecting code from having its variables stomped on by other code: lexically scoped variables created with <tt>&quot;my&quot;</tt> or <tt>&quot;state&quot;</tt> and namespaced global variables, which are exposed via the <tt>&quot;vars&quot;</tt> pragma, or the <tt>&quot;our&quot;</tt> keyword. Any global variable is considered to be part of a namespace and can be accessed via a ``fully qualified form''. Conversely, any lexically scoped variable is considered to be part of that lexical-scope, and does not have a ``fully qualified form''. 

 In perl namespaces are called ``packages'' and the <tt>&quot;package&quot;</tt> declaration tells the compiler which namespace to prefix to <tt>&quot;our&quot;</tt> variables and unqualified dynamic names. This both protects against accidental stomping and provides an interface for deliberately clobbering global dynamic variables declared and used in other scopes or packages, when that is what you want to do. 

 The scope of the <tt>&quot;package&quot;</tt> declaration is from the declaration itself through the end of the enclosing block, <tt>&quot;eval&quot;</tt>, or file, whichever comes first (the same scope as the <b>my()</b>, <b>our()</b>, <b>state()</b>, and <b>local()</b> operators, and also the effect of the experimental ``reference aliasing,'' which may change), or until the next <tt>&quot;package&quot;</tt> declaration. Unqualified dynamic identifiers will be in this namespace, except for those few identifiers that, if unqualified, default to the main package instead of the current one as described below. A <tt>&quot;package&quot;</tt> statement affects only dynamic global symbols, including subroutine names, and variables you've used <b>local()</b> on, but <i>not</i> lexical variables created with <b>my()</b>, <b>our()</b> or <b>state()</b>. 

 Typically, a <tt>&quot;package&quot;</tt> statement is the first declaration in a file included in a program by one of the <tt>&quot;do&quot;</tt>, <tt>&quot;require&quot;</tt>, or <tt>&quot;use&quot;</tt> operators. You can switch into a package in more than one place: <tt>&quot;package&quot;</tt> has no effect beyond specifying which symbol table the compiler will use for dynamic symbols for the rest of that block or until the next <tt>&quot;package&quot;</tt> statement. You can refer to variables and filehandles in other packages by prefixing the identifier with the package name and a double colon: <tt>$Package::Variable</tt>. If the package name is null, the <tt>&quot;main&quot;</tt> package is assumed. That is, <tt>$::sail</tt> is equivalent to <tt>$main::sail</tt>. 

 The old package delimiter was a single quote, but double colon is now the preferred delimiter, in part because it's more readable to humans, and in part because it's more readable to <b>emacs</b> macros. It also makes C<font SIZE="-2">++</font> programmers feel like they know what's going on---as opposed to using the single quote as separator, which was there to make Ada programmers feel like they knew what was going on. Because the old-fashioned syntax is still supported for backwards compatibility, if you try to use a string like <tt>&quot;This is $owner's house&quot;</tt>, you'll be accessing <tt>$owner::s</tt>; that is, the <tt>$s</tt> variable in package <tt>&quot;owner&quot;</tt>, which is probably not what you meant. Use braces to disambiguate, as in <tt>&quot;This is ${owner}'s house&quot;</tt>. 

 Packages may themselves contain package separators, as in <tt>$OUTER::INNER::var</tt>. This implies nothing about the order of name lookups, however. There are no relative packages: all symbols are either local to the current package, or must be fully qualified from the outer package name down. For instance, there is nowhere within package <tt>&quot;OUTER&quot;</tt> that <tt>$INNER::var</tt> refers to <tt>$OUTER::INNER::var</tt>. <tt>&quot;INNER&quot;</tt> refers to a totally separate global package. The custom of treating package names as a hierarchy is very strong, but the language in no way enforces it. 

 Only identifiers starting with letters (or underscore) are stored in a package's symbol table. All other symbols are kept in package <tt>&quot;main&quot;</tt>, including all punctuation variables, like <tt>$_</tt>. In addition, when unqualified, the identifiers <font SIZE="-1">STDIN, STDOUT, STDERR, ARGV, ARGVOUT, ENV, INC,</font> and <font SIZE="-1">SIG</font> are forced to be in package <tt>&quot;main&quot;</tt>, even when used for other purposes than their built-in ones. If you have a package called <tt>&quot;m&quot;</tt>, <tt>&quot;s&quot;</tt>, or <tt>&quot;y&quot;</tt>, then you can't use the qualified form of an identifier because it would be instead interpreted as a pattern match, a substitution, or a transliteration. 

 Variables beginning with underscore used to be forced into package main, but we decided it was more useful for package writers to be able to use leading underscore to indicate private variables and method names. However, variables and functions named with a single <tt>&quot;_&quot;</tt>, such as <tt>$_</tt> and <tt>&quot;sub _&quot;</tt>, are still forced into the package <tt>&quot;main&quot;</tt>. See also ``The Syntax of Variable Names'' in perlvar. 

 <tt>&quot;eval&quot;</tt>ed strings are compiled in the package in which the <b>eval()</b> was compiled. (Assignments to <tt>$SIG{}</tt>, however, assume the signal handler specified is in the <tt>&quot;main&quot;</tt> package. Qualify the signal handler name if you wish to have a signal handler in a package.) For an example, examine <i>perldb.pl</i> in the Perl library. It initially switches to the <tt>&quot;DB&quot;</tt> package so that the debugger doesn't interfere with variables in the program you are trying to debug. At various points, however, it temporarily switches back to the <tt>&quot;main&quot;</tt> package to evaluate various expressions in the context of the <tt>&quot;main&quot;</tt> package (or wherever you came from). See perldebug. 

 The special symbol <tt>&quot;__PACKAGE__&quot;</tt> contains the current package, but cannot (easily) be used to construct variable names. After <tt>&quot;my($foo)&quot;</tt> has hidden package variable <tt>$foo</tt>, it can still be accessed, without knowing what package you are in, as <tt>&quot;${__PACKAGE__.'::foo'}&quot;</tt>. 

 See perlsub for other scoping issues related to <b>my()</b> and <b>local()</b>, and perlref regarding closures.

<h3>Symbol Tables</h3>

 The symbol table for a package happens to be stored in the hash of that name with two colons appended. The main symbol table's name is thus <tt>%main::</tt>, or <tt>%::</tt> for short. Likewise the symbol table for the nested package mentioned earlier is named <tt>%OUTER::INNER::</tt>. 

 The value in each entry of the hash is what you are referring to when you use the <tt>*name</tt> typeglob notation. 

 <pre>
    local *main::foo    = *main::bar;
</pre> 

 You can use this to print out all the variables in a package, for instance. The standard but antiquated <i>dumpvar.pl</i> library and the <font SIZE="-1">CPAN</font> module Devel::Symdump make use of this. 

 The results of creating new symbol table entries directly or modifying any entries that are not already typeglobs are undefined and subject to change between releases of perl. 

 Assignment to a typeglob performs an aliasing operation, i.e., 

 <pre>
    *dick = *richard;
</pre> 

 causes variables, subroutines, formats, and file and directory handles accessible via the identifier <tt>&quot;richard&quot;</tt> also to be accessible via the identifier <tt>&quot;dick&quot;</tt>. If you want to alias only a particular variable or subroutine, assign a reference instead: 

 <pre>
    *dick = \$richard;
</pre> 

 Which makes <tt>$richard</tt> and <tt>$dick</tt> the same variable, but leaves <tt>@richard</tt> and <tt>@dick</tt> as separate arrays. Tricky, eh? 

 There is one subtle difference between the following statements: 

 <pre>
    *foo = *bar;
    *foo = \$bar;
</pre> 

 <tt>&quot;*foo = *bar&quot;</tt> makes the typeglobs themselves synonymous while <tt>&quot;*foo = \$bar&quot;</tt> makes the <font SIZE="-1">SCALAR</font> portions of two distinct typeglobs refer to the same scalar value. This means that the following code: 

 <pre><code>
$bar = 1;
*foo = \$bar;
#Make $foo an alias for $bar
{
    local $bar = 2;
#Restrict changes to block
        print $foo;
#Prints '1' !
}
</code></pre> 

 Would print '1', because <tt>$foo</tt> holds a reference to the <i>original</i> <tt>$bar</tt>. The one that was stuffed away by <tt>&quot;local()&quot;</tt> and which will be restored when the block ends. Because variables are accessed through the typeglob, you can use <tt>&quot;*foo = *bar&quot;</tt> to create an alias which can be localized. (But be aware that this means you can't have a separate <tt>@foo</tt> and <tt>@bar</tt>, etc.) 

 What makes all of this important is that the Exporter module uses glob aliasing as the import/export mechanism. Whether or not you can properly localize a variable that has been exported from a module depends on how it was exported: 

 
@EXPORT = qw($FOO);
#Usual form, can't be localized
             @EXPORT = qw(*FOO);
#Can be localized
 

 You can work around the first case by using the fully qualified name (<tt>$Package::FOO</tt>) where you need a local value, or by overriding it by saying <tt>&quot;*FOO = *Package::FOO&quot;</tt> in your script. 

 The <tt>&quot;*x = \$y&quot;</tt> mechanism may be used to pass and return cheap references into or from subroutines if you don't want to copy the whole thing. It only works when assigning to dynamic variables, not lexicals. 

 
% some_hash = ();
#can't be my()
    *some_hash = fn( \% another_hash);
sub fn
{
    local *hashsym = shift;
#now use % hashsym normally, and you
#will affect the caller's %another_hash
    my % nhash = ();
#do what you want return \% nhash;
}
 

 On return, the reference will overwrite the hash slot in the symbol table specified by the *some_hash typeglob. This is a somewhat tricky way of passing around references cheaply when you don't want to have to remember to dereference variables explicitly. 

 Another use of symbol tables is for making ``constant'' scalars. 

 <pre>
    *PI = \3.14159265358979;
</pre> 

 Now you cannot alter <tt>$PI</tt>, which is probably a good thing all in all. This isn't the same as a constant subroutine, which is subject to optimization at compile-time. A constant subroutine is one prototyped to take no arguments and to return a constant expression. See perlsub for details on these. The <tt>&quot;use constant&quot;</tt> pragma is a convenient shorthand for these. 

 You can say <tt>*foo{PACKAGE}</tt> and <tt>*foo{NAME}</tt> to find out what name and package the *foo symbol table entry comes from. This may be useful in a subroutine that gets passed typeglobs as arguments: 

 
sub identify_typeglob
{
    my $glob = shift;
    print 'You gave me ', *{$glob} {PACKAGE},
        '::', *{$glob} {NAME}, "\n";
}
identify_typeglob *foo;
identify_typeglob *bar::baz;
 

 This prints 

 <pre>
    You gave me main::foo
    You gave me bar::baz
</pre> 

 The <tt>*foo{THING}</tt> notation can also be used to obtain references to the individual elements of *foo. See perlref. 

 Subroutine definitions (and declarations, for that matter) need not necessarily be situated in the package whose symbol table they occupy. You can define a subroutine outside its package by explicitly qualifying the name of the subroutine: 

 <pre>
    package main;
    sub Some_package::foo { ... }   # &amp;foo defined in Some_package
</pre> 

 This is just a shorthand for a typeglob assignment at compile time: 

 
BEGIN
{
    *Some_package::foo = sub
    {
        ...
    }
}
 

 and is <i>not</i> the same as writing: 

 
{
    package Some_package;
    sub foo
    {
        ...
    }
}
 

 In the first two versions, the body of the subroutine is lexically in the main package, <i>not</i> in Some_package. So something like this: 

 
package main;
$Some_package::name = "fred";
$main::name = "barney";
sub Some_package::foo
{
    print "in ", __PACKAGE__, ": \$name is '$name'\n";
}
Some_package::foo();
 

 prints: 

 <pre>
    in main: $name is 'barney'
</pre> 

 rather than: 

 <pre>
    in Some_package: $name is 'fred'
</pre> 

 This also has implications for the use of the <font SIZE="-1">SUPER::</font> qualifier (see perlobj).

<h3><font SIZE="-1">BEGIN, UNITCHECK, CHECK, INIT</font> and <font SIZE="-1">END</font></h3>

 Five specially named code blocks are executed at the beginning and at the end of a running Perl program. These are the <tt>&quot;BEGIN&quot;</tt>, <tt>&quot;UNITCHECK&quot;</tt>, <tt>&quot;CHECK&quot;</tt>, <tt>&quot;INIT&quot;</tt>, and <tt>&quot;END&quot;</tt> blocks. 

 These code blocks can be prefixed with <tt>&quot;sub&quot;</tt> to give the appearance of a subroutine (although this is not considered good style). One should note that these code blocks don't really exist as named subroutines (despite their appearance). The thing that gives this away is the fact that you can have <b>more than one</b> of these code blocks in a program, and they will get <b>all</b> executed at the appropriate moment. So you can't execute any of these code blocks by name. 

 A <tt>&quot;BEGIN&quot;</tt> code block is executed as soon as possible, that is, the moment it is completely defined, even before the rest of the containing file (or string) is parsed. You may have multiple <tt>&quot;BEGIN&quot;</tt> blocks within a file (or eval'ed string); they will execute in order of definition. Because a <tt>&quot;BEGIN&quot;</tt> code block executes immediately, it can pull in definitions of subroutines and such from other files in time to be visible to the rest of the compile and run time. Once a <tt>&quot;BEGIN&quot;</tt> has run, it is immediately undefined and any code it used is returned to Perl's memory pool. 

 An <tt>&quot;END&quot;</tt> code block is executed as late as possible, that is, after perl has finished running the program and just before the interpreter is being exited, even if it is exiting as a result of a <b>die()</b> function. (But not if it's morphing into another program via <tt>&quot;exec&quot;</tt>, or being blown out of the water by a signal---you have to trap that yourself (if you can).) You may have multiple <tt>&quot;END&quot;</tt> blocks within a file---they will execute in reverse order of definition; that is: last in, first out (<font SIZE="-1">LIFO</font>). <tt>&quot;END&quot;</tt> blocks are not executed when you run perl with the <tt>&quot;-c&quot;</tt> switch, or if compilation fails. 

 Note that <tt>&quot;END&quot;</tt> code blocks are <b>not</b> executed at the end of a string <tt>&quot;eval()&quot;</tt>: if any <tt>&quot;END&quot;</tt> code blocks are created in a string <tt>&quot;eval()&quot;</tt>, they will be executed just as any other <tt>&quot;END&quot;</tt> code block of that package in <font SIZE="-1">LIFO</font> order just before the interpreter is being exited. 

 Inside an <tt>&quot;END&quot;</tt> code block, <tt>$?</tt> contains the value that the program is going to pass to <tt>&quot;exit()&quot;</tt>. You can modify <tt>$?</tt> to change the exit value of the program. Beware of changing <tt>$?</tt> by accident (e.g. by running something via <tt>&quot;system&quot;</tt>). 

 Inside of a <tt>&quot;END&quot;</tt> block, the value of <tt>&quot;${^GLOBAL_PHASE}&quot;</tt> will be <tt>&quot;END&quot;</tt>. 

 <tt>&quot;UNITCHECK&quot;</tt>, <tt>&quot;CHECK&quot;</tt> and <tt>&quot;INIT&quot;</tt> code blocks are useful to catch the transition between the compilation phase and the execution phase of the main program. 

 <tt>&quot;UNITCHECK&quot;</tt> blocks are run just after the unit which defined them has been compiled. The main program file and each module it loads are compilation units, as are string <tt>&quot;eval&quot;</tt>s, run-time code compiled using the <tt>&quot;(?{ })&quot;</tt> construct in a regex, calls to <tt>&quot;do FILE&quot;</tt>, <tt>&quot;require FILE&quot;</tt>, and code after the <tt>&quot;-e&quot;</tt> switch on the command line. 

 <tt>&quot;BEGIN&quot;</tt> and <tt>&quot;UNITCHECK&quot;</tt> blocks are not directly related to the phase of the interpreter. They can be created and executed during any phase. 

 <tt>&quot;CHECK&quot;</tt> code blocks are run just after the <b>initial</b> Perl compile phase ends and before the run time begins, in <font SIZE="-1">LIFO</font> order. <tt>&quot;CHECK&quot;</tt> code blocks are used in the Perl compiler suite to save the compiled state of the program. 

 Inside of a <tt>&quot;CHECK&quot;</tt> block, the value of <tt>&quot;${^GLOBAL_PHASE}&quot;</tt> will be <tt>&quot;CHECK&quot;</tt>. 

 <tt>&quot;INIT&quot;</tt> blocks are run just before the Perl runtime begins execution, in ``first in, first out'' (<font SIZE="-1">FIFO</font>) order. 

 Inside of an <tt>&quot;INIT&quot;</tt> block, the value of <tt>&quot;${^GLOBAL_PHASE}&quot;</tt> will be <tt>&quot;INIT&quot;</tt>. 

 The <tt>&quot;CHECK&quot;</tt> and <tt>&quot;INIT&quot;</tt> blocks in code compiled by <tt>&quot;require&quot;</tt>, string <tt>&quot;do&quot;</tt>, or string <tt>&quot;eval&quot;</tt> will not be executed if they occur after the end of the main compilation phase; that can be a problem in mod_perl and other persistent environments which use those functions to load code at runtime. 

 When you use the <b>-n</b> and <b>-p</b> switches to Perl, <tt>&quot;BEGIN&quot;</tt> and <tt>&quot;END&quot;</tt> work just as they do in <b>awk</b>, as a degenerate case. Both <tt>&quot;BEGIN&quot;</tt> and <tt>&quot;CHECK&quot;</tt> blocks are run when you use the <b>-c</b> switch for a compile-only syntax check, although your main code is not. 

 The <b>begincheck</b> program makes it all clear, eventually: 

 
#!/ usr / bin / perl
#begincheck
print "10. Ordinary code runs at runtime.\n";
END{print "16.   So this is the end of the tale.\n"} INIT{print " 7. INIT blocks run FIFO just before runtime.\n"} UNITCHECK{
    print " 4.   And therefore before any CHECK blocks.\n"} CHECK{print " 6.   So this is the sixth line.\n"} print "11.   It runs in order, of course.\n";
BEGIN{print " 1. BEGIN blocks run FIFO during compilation.\n"} END{print "15.   Read perlmod for the rest of the story.\n"} CHECK{print " 5. CHECK blocks run LIFO after all compilation.\n"} INIT{print " 8.   Run this again, using Perl's -c switch.\n"} print "12.   This is anti-obfuscated code.\n";
END{print "14. END blocks run LIFO at quitting time.\n"} BEGIN{print " 2.   So this line comes out second.\n"} UNITCHECK{
    print " 3. UNITCHECK blocks run LIFO after each file is compiled.\n"} INIT{print " 9.   You'll see the difference right away.\n"} print "13.   It only _looks_ like it should be confusing.\n";
__END__


<h3>Perl Classes</h3>

 There is no special class syntax in Perl, but a package may act as a class if it provides subroutines to act as methods. Such a package may also derive some of its methods from another class (package) by listing the other package name(s) in its global <tt>@ISA</tt> array (which must be a package global, not a lexical). 

 For more on this, see perlootut and perlobj.

<h3>Perl Modules</h3>

 A module is just a set of related functions in a library file, i.e., a Perl package with the same name as the file. It is specifically designed to be reusable by other modules or programs. It may do this by providing a mechanism for exporting some of its symbols into the symbol table of any package using it, or it may function as a class definition and make its semantics available implicitly through method calls on the class and its objects, without explicitly exporting anything. Or it can do a little of both. 

 For example, to start a traditional, non-OO module called Some::Module, create a file called <i>Some/Module.pm</i> and start with this template: 

 
package Some::Module;
#assumes Some / Module.pm
                    use strict;
use warnings;
#Get the import method from Exporter to export functions and
#variables
use Exporter 5.57 'import';
#set the version for version checking
our $VERSION = '1.00';
#Functions and variables which are exported by default
our @EXPORT = qw(func1 func2);
#Functions and variables which can be optionally exported
our @EXPORT_OK = qw($Var1 % Hashit func3);
#exported package globals go here
our $Var1 = '';
our % Hashit = ();
#non - exported package globals go here
#(they are still accessible as $Some::Module::stuff)
our @more = ();
our $stuff = '';
#file - private lexicals go here, before any functions which use them
my $priv_var = '';
my % secret_hash = ();
#here's a file-private function as a closure,
#callable as $priv_func-&gt;();
my $priv_func = sub{
    ...};
#make all your functions, whether exported or not ;
#remember to put something interesting in the{} stubs
sub func1{...} sub func2{...}
#this one isn't always exported, but could be called directly
#as Some::Module::func3()
sub func3{...} END
{
    ...
}
#module clean - up code here(global destructor) 1;
#don't forget to return a true value from the file
 

 Then go on to declare and use your variables in functions without any qualifications. See Exporter and the perlmodlib for details on mechanics and style issues in module creation. 

 Perl modules are included into your program by saying 

 <pre>
    use Module;
</pre> 

 or 

 <pre>
    use Module LIST;
</pre> 

 This is exactly equivalent to 

 
BEGIN
{
    require 'Module.pm';
    'Module'-&gt;import;
}
 

 or 

 
BEGIN
{
    require 'Module.pm';
    'Module'-&gt;import(LIST);
}
 

 As a special case 

 <pre>
    use Module ();
</pre> 

 is exactly equivalent to 

 <pre>
    BEGIN { require 'Module.pm'; }
</pre> 

 All Perl module files have the extension <i>.pm</i>. The <tt>&quot;use&quot;</tt> operator assumes this so you don't have to spell out &quot;<i>Module.pm</i>&quot; in quotes. This also helps to differentiate new modules from old <i>.pl</i> and <i>.ph</i> files. Module names are also capitalized unless they're functioning as pragmas; pragmas are in effect compiler directives, and are sometimes called ``pragmatic modules'' (or even ``pragmata'' if you're a classicist). 

 The two statements: 

 <pre>
    require SomeModule;
    require &quot;SomeModule.pm&quot;;
</pre> 

 differ from each other in two ways. In the first case, any double colons in the module name, such as <tt>&quot;Some::Module&quot;</tt>, are translated into your system's directory separator, usually ``/''. The second case does not, and would have to be specified literally. The other difference is that seeing the first <tt>&quot;require&quot;</tt> clues in the compiler that uses of indirect object notation involving ``SomeModule'', as in <tt>&quot;$ob = purge SomeModule&quot;</tt>, are method calls, not function calls. (Yes, this really can make a difference.) 

 Because the <tt>&quot;use&quot;</tt> statement implies a <tt>&quot;BEGIN&quot;</tt> block, the importing of semantics happens as soon as the <tt>&quot;use&quot;</tt> statement is compiled, before the rest of the file is compiled. This is how it is able to function as a pragma mechanism, and also how modules are able to declare subroutines that are then visible as list or unary operators for the rest of the current file. This will not work if you use <tt>&quot;require&quot;</tt> instead of <tt>&quot;use&quot;</tt>. With <tt>&quot;require&quot;</tt> you can get into this problem: 

 <pre><code>
require Cwd;
#make Cwd::accessible
    $here = Cwd::getcwd();
use Cwd;
#import names from Cwd::
    $here = getcwd();
require Cwd;
#make Cwd::accessible
    $here = getcwd();
#oops !no main::getcwd()
</code></pre> 

 In general, <tt>&quot;use Module ()&quot;</tt> is recommended over <tt>&quot;require Module&quot;</tt>, because it determines module availability at compile time, not in the middle of your program's execution. An exception would be if two modules each tried to <tt>&quot;use&quot;</tt> each other, and each also called a function from that other module. In that case, it's easy to use <tt>&quot;require&quot;</tt> instead. 

 Perl packages may be nested inside other package names, so we can have package names containing <tt>&quot;::&quot;</tt>. But if we used that package name directly as a filename it would make for unwieldy or impossible filenames on some systems. Therefore, if a module's name is, say, <tt>&quot;Text::Soundex&quot;</tt>, then its definition is actually found in the library file <i>Text/Soundex.pm</i>. 

 Perl modules always have a <i>.pm</i> file, but there may also be dynamically linked executables (often ending in <i>.so</i>) or autoloaded subroutine definitions (often ending in <i>.al</i>) associated with the module. If so, these will be entirely transparent to the user of the module. It is the responsibility of the <i>.pm</i> file to load (or arrange to autoload) any additional functionality. For example, although the <font SIZE="-1">POSIX</font> module happens to do both dynamic loading and autoloading, the user can say just <tt>&quot;use POSIX&quot;</tt> to get it all.

<h3>Making your module threadsafe</h3>

 Perl supports a type of threads called interpreter threads (ithreads). These threads can be used explicitly and implicitly. 

 Ithreads work by cloning the data tree so that no data is shared between different threads. These threads can be used by using the <tt>&quot;threads&quot;</tt> module or by doing <b>fork()</b> on win32 (fake <b>fork()</b> support). When a thread is cloned all Perl data is cloned, however non-Perl data cannot be cloned automatically. Perl after 5.8.0 has support for the <tt>&quot;CLONE&quot;</tt> special subroutine. In <tt>&quot;CLONE&quot;</tt> you can do whatever you need to do, like for example handle the cloning of non-Perl data, if necessary. <tt>&quot;CLONE&quot;</tt> will be called once as a class method for every package that has it defined (or inherits it). It will be called in the context of the new thread, so all modifications are made in the new area. Currently <font SIZE="-1">CLONE</font> is called with no parameters other than the invocant package name, but code should not assume that this will remain unchanged, as it is likely that in future extra parameters will be passed in to give more information about the state of cloning. 

 If you want to <font SIZE="-1">CLONE</font> all objects you will need to keep track of them per package. This is simply done using a hash and <b>Scalar::Util::weaken()</b>. 

 Perl after 5.8.7 has support for the <tt>&quot;CLONE_SKIP&quot;</tt> special subroutine. Like <tt>&quot;CLONE&quot;</tt>, <tt>&quot;CLONE_SKIP&quot;</tt> is called once per package; however, it is called just before cloning starts, and in the context of the parent thread. If it returns a true value, then no objects of that class will be cloned; or rather, they will be copied as unblessed, undef values. For example: if in the parent there are two references to a single blessed hash, then in the child there will be two references to a single undefined scalar value instead. This provides a simple mechanism for making a module threadsafe; just add <tt>&quot;sub CLONE_SKIP { 1 }&quot;</tt> at the top of the class, and <tt>&quot;DESTROY()&quot;</tt> will now only be called once per object. Of course, if the child thread needs to make use of the objects, then a more sophisticated approach is needed. 

 Like <tt>&quot;CLONE&quot;</tt>, <tt>&quot;CLONE_SKIP&quot;</tt> is currently called with no parameters other than the invocant package name, although that may change. Similarly, to allow for future expansion, the return value should be a single <tt>0</tt> or <tt>1</tt> value.

<h2>SEE ALSO</h2>

 See perlmodlib for general style issues related to building Perl modules and classes, as well as descriptions of the standard library and <font SIZE="-1">CPAN,</font> Exporter for how Perl's standard import/export mechanism works, perlootut and perlobj for in-depth information on creating classes, perlobj for a hard-core reference document on objects, perlsub for an explanation of functions and scoping, and perlxstut and perlguts for more information on writing extension modules. 

<h2>Index</h2>



<dt><a HREF="#lbAK">SEE ALSO</a>
<dd></dl>

---
title: "perldgux(1)"
name: "perldgux"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perldgux/"
---

<h2 class="name">NAME</h2>
 

 perldgux - Perl under DG/UX. 

<h2>SYNOPSIS</h2>

 One can read this document in the following formats: 

 <pre>
        man perldgux
        view perl perldgux
        explorer perldgux.html
        info perldgux
</pre> 

 to list some (not all may be available simultaneously), or it may be read <i>as is</i>: as <i></i><font SIZE="-1"><i>README</i></font><i>.dgux</i>.

<h2>DESCRIPTION</h2>

 Perl 5.7/8.x for <font SIZE="-1">DG/UX</font> ix86 R4.20MU0x

<h2>BUILDING PERL ON DG/UX</h2>

<h3>Non-threaded Perl on <font SIZE="-1">DG/UX</font></h3>

 Just run ./Configure script from the top directory. Then give ``make'' to compile.

<h3>Threaded Perl on <font SIZE="-1">DG/UX</font></h3>

 If you are using as compiler <font SIZE="-1">GCC-2</font>.95.x rev(<font SIZE="-1">DG/UX</font>) an easy solution for configuring perl in your <font SIZE="-1">DG/UX</font> machine is to run the command: 

 ./Configure -Dusethreads -Duseithreads -Dusedevel -des 

 This will automatically accept all the defaults and in particular /usr/local/ as installation directory. Note that <font SIZE="-1">GCC-2</font>.95.x rev(<font SIZE="-1">DG/UX</font>) knows the switch -pthread which allows it to link correctly <font SIZE="-1">DG/UX</font>'s -lthread library. 

 If you want to change the installation directory or have a standard <font SIZE="-1">DG/UX</font> with C compiler <font SIZE="-1">GCC-2</font>.7.2.x then you have no choice than to do an interactive build by issuing the command: 

 ./Configure -Dusethreads -Duseithreads 

 In particular with <font SIZE="-1">GCC-2</font>.7.2.x accept all the defaults and *watch* out for the message: 

 <pre>
    Any additional ld flags (NOT including libraries)? [ -pthread]
</pre> 

 Instead of -pthread put here -lthread. <font SIZE="-1">CGCC-2</font>.7.2.x that comes with the <font SIZE="-1">DG/UX</font> <font SIZE="-1">OS</font> does <font SIZE="-1">NOT</font> know the -pthread switch. So your build will fail if you choose the defaults. After configuration is done correctly give ``make'' to compile.

<h3>Testing Perl on <font SIZE="-1">DG/UX</font></h3>

 Issuing a ``make test'' will run all the tests. If the test lib/ftmp-security gives you as a result something like 

 <pre>
    lib/ftmp-security....File::Temp::_gettemp:
    Parent directory (/tmp/) is not safe (sticky bit not set
    when world writable?) at lib/ftmp-security.t line 100
</pre> 

 don't panic and just set the sticky bit in your /tmp directory by doing the following as root: 

 cd / chmod +t /tmp (=set the sticky bit to /tmp). 

 Then rerun the tests. This time all must be <font SIZE="-1">OK</font>.

<h3>Installing the built perl on <font SIZE="-1">DG/UX</font></h3>

 Run the command ``make install''

<h2>AUTHOR</h2>

 Takis Psarogiannakopoulos University of Cambridge Centre for Mathematical Sciences Department of Pure Mathematics Wilberforce road Cambridge <font SIZE="-1">CB3</font> 0WB , <font SIZE="-1">UK</font> email &lt;takis [at] XFree86.Org&gt;

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/1-perl/">perl</a></i>(1). 

<h2>Index</h2>



<dt><a HREF="#lbAJ">AUTHOR</a>
<dd>
<dt><a HREF="#lbAK">SEE ALSO</a>
<dd></dl>

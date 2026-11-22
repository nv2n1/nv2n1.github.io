---

title: "perldgux(1)"
name: "perldgux"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perldgux/"
---

perldgux - Perl under DG/UX. 

<h2>SYNOPSIS</h2>

 One can read this document in the following formats: 

 <pre>
        man perldgux
        view perl perldgux
        explorer perldgux.html
        info perldgux
</pre> 

 to list some (not all may be available simultaneously), or it may be read <i>as is</i>: as <i></i><i>README</i><i>.dgux</i>.

<h2>DESCRIPTION</h2>

 Perl 5.7/8.x for DG/UX ix86 R4.20MU0x

<h2>BUILDING PERL ON DG/UX</h2>

<h3>Non-threaded Perl on DG/UX</h3>

 Just run ./Configure script from the top directory. Then give ``make'' to compile.

<h3>Threaded Perl on DG/UX</h3>

 If you are using as compiler GCC-2.95.x rev(DG/UX) an easy solution for configuring perl in your DG/UX machine is to run the command: 

 ./Configure -Dusethreads -Duseithreads -Dusedevel -des 

 This will automatically accept all the defaults and in particular /usr/local/ as installation directory. Note that GCC-2.95.x rev(DG/UX) knows the switch -pthread which allows it to link correctly DG/UX's -lthread library. 

 If you want to change the installation directory or have a standard DG/UX with C compiler GCC-2.7.2.x then you have no choice than to do an interactive build by issuing the command: 

 ./Configure -Dusethreads -Duseithreads 

 In particular with GCC-2.7.2.x accept all the defaults and *watch* out for the message: 

 <pre>
    Any additional ld flags (NOT including libraries)? [ -pthread]
</pre> 

 Instead of -pthread put here -lthread. CGCC-2.7.2.x that comes with the DG/UX OS does NOT know the -pthread switch. So your build will fail if you choose the defaults. After configuration is done correctly give ``make'' to compile.

<h3>Testing Perl on DG/UX</h3>

 Issuing a ``make test'' will run all the tests. If the test lib/ftmp-security gives you as a result something like 

 <pre>
    lib/ftmp-security....File::Temp::_gettemp:
    Parent directory (/tmp/) is not safe (sticky bit not set
    when world writable?) at lib/ftmp-security.t line 100
</pre> 

 don't panic and just set the sticky bit in your /tmp directory by doing the following as root: 

 cd / chmod +t /tmp (=set the sticky bit to /tmp). 

 Then rerun the tests. This time all must be OK.

<h3>Installing the built perl on DG/UX</h3>

 Run the command ``make install''

<h2>AUTHOR</h2>

 Takis Psarogiannakopoulos University of Cambridge Centre for Mathematical Sciences Department of Pure Mathematics Wilberforce road Cambridge CB3 0WB , UK email &lt;takis [at] XFree86.Org&gt;

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/1-perl/">perl</a></i>(1). 



<dt><a HREF="#lbAJ">AUTHOR</a>
</dt><dd>
</dd><dt><a HREF="#lbAK">SEE ALSO</a>
</dt><dd></dd></dl>

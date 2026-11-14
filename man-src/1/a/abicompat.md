---
title: "abicompat(1)"
name: "abicompat"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abicompat/"
description: "abicompat – check ABI compatibility"
---

<h2>NAME</h2>
<p> abicompat &#8211; check ABI compatibility </p>
<p> abicompat checks that an application that links against a given shared library is still ABI compatible with a subsequent version of that library. If the new version of the library introduces an ABI incompatibility, then abicompat hints the user at what exactly that incompatibility is.</p>
<h2>INVOCATION</h2>
<pre><code>
abicompat[options][&lt;application&gt;&lt;shared - library - first - version&gt;&lt;shared - library - second - version&gt;]
</code></pre>
<h2>OPTIONS</h2>
<dl>
<dt>&bull;</p>
<dd> <code>&#8211;help</code> </p>
<p> Display a short help about the command and exit.</p>
<dt>&bull;</p>
<dd> <i>&#8211;version | -v</i> </p>
<p> Display the version of the program and exit.</p>
<dt>&bull;</p>
<dd> <code>&#8211;list-undefined-symbols | -u</code> </p>
<p> Display the list of undefined symbols of the application and exit.</p>
<dt>&bull;</p>
<dd> <code>&#8211;show-base-names | -b</code> </p>
<p> In the resulting report emitted by the tool, this option makes the application and libraries be referred to by their base names only; not by a full absolute name. This can be useful for use in scripts that wants to compare names of the application and libraries independently of what their directory names are.</p>
<dt>&bull;</p>
<dd> <code>&#8211;app-debug-info-dir | &#8211;appd</code> &lt;path-to-app-debug-info-directory&gt; </p>
<p> Set the path to the directory under which the debug information of the application is supposed to be laid out. This is useful for application binaries for which the debug info is in a separate set of files.</p>
<dt>&bull;</p>
<dd> <code>&#8211;lib-debug-info-dir1 | &#8211;libd1</code> &lt;path-to-lib1-debug-info&gt; </p>
<p> Set the path to the directory under which the debug information of the first version of the shared library is supposed to be laid out. This is useful for shared library binaries for which the debug info is in a separate set of files.</p>
<dt>&bull;</p>
<dd> <code>&#8211;lib-debug-info-dir2 | &#8211;libd2</code> &lt;path-to-lib1-debug-info&gt; </p>
<p> Set the path to the directory under which the debug information of the second version of the shared library is supposed to be laid out. This is useful for shared library binaries for which the debug info is in a separate set of files.</p>
<dt>&bull;</p>
<dd> <code>&#8211;suppressions | &#8211;suppr</code> &lt;<i>path-to-suppressions</i>&gt; </p>
<p> Use a <i>suppression specification</i> file located at <i>path-to-suppressions</i>. Note that this option can appear multiple times on the command line; all the suppression specification files are then taken into account.</p>
<dt>&bull;</p>
<dd> <code>&#8211;no-show-locs</code> Do not show information about where in the <i>second shared library</i> the respective type was changed.</p>
<dt>&bull;</p>
<dd> <code>&#8211;weak-mode</code> </p>
<p> This triggers the weak mode of <code>abicompat</code>. In this mode, only one version of the library is required. That is, abicompat is invoked like this: </p>
<pre>
abicompat --weak-mode &lt;the-application&gt; &lt;the-library&gt;
</pre>
<p> Note that the <code>&#8211;weak-mode</code> option can even be omitted if only one version of the library is given, along with the application; in that case, <code>abicompat</code> automatically switches to operate in weak mode: </p>
<pre>
abicompat &lt;the-application&gt; &lt;the-library&gt;
</pre>
<p> In this weak mode, the types of functions and variables exported by the library and consumed by the application (as in, the symbols of the these functions and variables are undefined in the application and are defined and exported by the library) are compared to the version of these types as expected by the application. And if these two versions of types are different, <code>abicompat</code> tells the user what the differences are. </p>
<p> In other words, in this mode, <code>abicompat</code> checks that the types of the functions and variables exported by the library mean the same thing as what the application expects, as far as the ABI is concerned. </p>
<p> Note that in this mode, <i>abicompat</i> doesn&#8217;t detect exported functions or variables (symbols) that are expected by the application but that are removed from the library. That is why it is called <code>weak</code> mode.</dl>
<h2>RETURN VALUES</h2>
<p> The exit code of the <code>abicompat</code> command is either 0 if the ABI of the binaries being compared are equal, or non-zero if they differ or if the tool encountered an error. </p>
<p> In the later case, the exit code is a 8-bits-wide bit field in which each bit has a specific meaning. </p>
<p> The first bit, of value 1, named <code>ABIDIFF_ERROR</code> means there was an error. </p>
<p> The second bit, of value 2, named <code>ABIDIFF_USAGE_ERROR</code> means there was an error in the way the user invoked the tool. It might be set, for instance, if the user invoked the tool with an unknown command line switch, with a wrong number or argument, etc. If this bit is set, then the <code>ABIDIFF_ERROR</code> bit must be set as well. </p>
<p> The third bit, of value 4, named <code>ABIDIFF_ABI_CHANGE</code> means the ABI of the binaries being compared are different. </p>
<p> The fourth bit, of value 8, named <code>ABIDIFF_ABI_INCOMPATIBLE_CHANGE</code> means the ABI of the binaries compared are different in an incompatible way. If this bit is set, then the <code>ABIDIFF_ABI_CHANGE</code> bit must be set as well. If the <code>ABIDIFF_ABI_CHANGE</code> is set and the <code>ABIDIFF_INCOMPATIBLE_CHANGE</code> is <i>NOT</i> set, then it means that the ABIs being compared might or might not be compatible. In that case, a human being needs to review the ABI changes to decide if they are compatible or not. </p>
<p> The remaining bits are not used for the moment.</p>
<h2>USAGE EXAMPLES</h2>
<dl>
<dt>&bull;</p>
<dd> Detecting a possible ABI incompatibility in a new shared library version: </p>
<p>$ cat &#8211; n test0.h 1 struct foo 2<br />
{<br />
    3 int m0;<br />
    4 5 foo() 6 : m0() 7<br />
    {<br />
    }<br />
    8<br />
};<br />
9 10 foo *<br />
    11 first_func();<br />
12 13 void 14 second_func(foo &amp;);<br />
15 16 void 17 third_func();<br />
$<br />
        $ cat &#8211;<br />
    n test &#8211; app.cc 1 // Compile with:<br />
             2        //  g++ -g -Wall -o test-app -L. -ltest-0 test-app.cc<br />
             3 4 #include &#8220;test0.h&#8221; 5 6 int 7 main() 8<br />
{<br />
    9 foo *f = first_func();<br />
    10 second_func(*f);<br />
    11 return 0;<br />
    12<br />
}<br />
$<br />
        $ cat &#8211;<br />
    n test0.cc 1 // Compile this with:<br />
        2        //  g++ -g -Wall -shared -o libtest-0.so test0.cc<br />
        3 4 #include &#8220;test0.h&#8221; 5 6 foo *<br />
        7 first_func() 8<br />
{<br />
    9 foo *f = new foo();<br />
    10 return f;<br />
    11<br />
}<br />
12 13 void 14 second_func(foo &amp;) 15<br />
{<br />
    16<br />
}<br />
17 18 void 19 third_func() 20 {<br />
    21} $<br />
    $ cat<br />
    &#8211; n test1.h<br />
      1 struct foo<br />
      2<br />
{<br />
    3 int m0;<br />
    4 char m1; /* &lt;&#8211; a new member got added here! */<br />
    5 6 foo() 7 : m0(),<br />
                  8 m1() 9<br />
    {<br />
    }<br />
    10<br />
};<br />
11 12 foo *<br />
    13 first_func();<br />
14 15 void 16 second_func(foo &amp;);<br />
17 18 void 19 third_func();<br />
$<br />
        $ cat &#8211;<br />
    n test1.cc 1 // Compile this with:<br />
        2        //  g++ -g -Wall -shared -o libtest-1.so test1.cc<br />
        3 4 #include &#8220;test1.h&#8221; 5 6 foo *<br />
        7 first_func() 8<br />
{<br />
    9 foo *f = new foo();<br />
    10 return f;<br />
    11<br />
}<br />
12 13 void 14 second_func(foo &amp;) 15<br />
{<br />
    16<br />
}<br />
17 18 /* Let&#8217;s comment out the definition of third_func()<br />
  19     void<br />
  20     third_func()<br />
  21     {<br />
  22     }<br />
  23  */<br />
    $</p>
<dt>&bull;</p>
<dd> Compile the first and second versions of the libraries: <code>libtest-0.so</code> and <code>libtest-1.so</code>: </p>
<pre>
$ g++ -g -Wall -shared -o libtest-0.so test0.cc
$ g++ -g -Wall -shared -o libtest-1.so test1.cc
</pre>
<dt>&bull;</p>
<dd> Compile the application and link it against the first version of the library, creating the <code>test-app</code> binary: </p>
<pre>
$ g++ -g -Wall -o test-app -L. -ltest-0.so test-app.cc
</pre>
<dt>&bull;</p>
<dd> Now, use <code>abicompat</code> to see if libtest-1.so is ABI compatible with app, with respect to the ABI of libtest-0.so: </p>
<p>$ abicompat test &#8211; app libtest &#8211; 0.so libtest &#8211; 1.so ELF file &#8216;test-app&#8217; might not be ABI compatible with &#8216;libtest-1.so&#8217; due to differences with &#8216;libtest-0.so&#8217; below : Functions changes summary : 0 Removed, 2 Changed, 0 Added functions Variables changes summary : 0 Removed, 0 Changed, 0 Added variable 2 functions with some indirect sub &#8211; type change : [C] &#8216;function foo* first_func()&#8217; has some indirect sub &#8211; type changes : return type changed : in pointed to type &#8216;struct foo&#8217; : size changed from 32 to 64 bits 1 data member insertion : &#8216;char foo::m1&#8217;, at offset 32(in bits)[C] &#8216;function void second_func(foo&amp;)&#8217; has some indirect sub &#8211; type changes : parameter 0 of type &#8216;foo&amp;&#8217; has sub &#8211; type changes : referenced type &#8216;struct foo&#8217; changed, as reported earlier $</p>
<dt>&bull;</p>
<dd> Now use the weak mode of abicompat, that is, providing just the application and the new version of the library: </p>
<pre><code>
$ abicompat-- weak - mode test - app libtest - 1.so functions defined in library 'libtest-1.so' have sub - types that are different from what application 'test-app' expects : function foo *first_func()
    : return type changed : in pointed to type 'struct foo' : size changed from 32 to 64 bits 1 data member insertion : 'char foo::m1',
    at offset 32(in bits)
        $
</code></pre>
</dl>
<h2>AUTHOR</h2>
<p> Dodji Seketeli</p>
<h2>COPYRIGHT</h2>
<p> 2014-2016, Red Hat, Inc. </p>
<h2>Index</h2>

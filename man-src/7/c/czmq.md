---
title: "czmq(7)"
name: "czmq"
section: "7"
letter: "c"
url: "/docs/linux/man/7-czmq/"
description: "czmq – high-level C binding for ZeroMQ"
---

<p>czmq &#8211; high-level C binding for ZeroMQ</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;czmq.h&gt;

cc ['flags'] 'files' -lzmq -lczmq ['libraries']</code></pre>
<h2>Description</h2>
<h3>Classes</h3>
<p>These classes provide the main socket and message API: </p>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-zsock/">zsock</a></code>(3) &#8211; working with ZeroMQ sockets (high-level)</dl>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-zstr/">zstr</a></code>(3) &#8211; sending and receiving strings</dl>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-zmsg/">zmsg</a></code>(3) &#8211; working with multipart messages</dl>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-zframe/">zframe</a></code>(3) &#8211; working with single message frames</dl>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-zactor/">zactor</a></code>(3) &#8211; Actor class (socket + thread)</dl>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-zloop/">zloop</a></code>(3) &#8211; event-driven reactor</dl>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-zpoller/">zpoller</a></code>(3) &#8211; trivial socket poller class</dl>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-zproxy/">zproxy</a></code>(3) &#8211; proxy actor (like zmq_proxy_steerable)</dl>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-zmonitor/">zmonitor</a></code>(3) &#8211; monitor events on ZeroMQ sockets</dl>
<p> These classes support authentication and encryption: </p>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-zauth/">zauth</a></code>(3) &#8211; authentication actor for ZeroMQ servers</dl>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-zcert/">zcert</a></code>(3) &#8211; work with CURVE security certificates</dl>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-zcertstore/">zcertstore</a></code>(3) &#8211; work with CURVE security certificate stores</dl>
<p> These classes provide generic containers: </p>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-zhash/">zhash</a></code>(3) &#8211; simple generic hash container</dl>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-zhashx/">zhashx</a></code>(3) &#8211; extended generic hash container</dl>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-zlist/">zlist</a></code>(3) &#8211; simple generic list container</dl>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-zlistx/">zlistx</a></code>(3) &#8211; extended generic list container</dl>
<p> These classes wrap-up non-portable functionality: </p>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-zbeacon/">zbeacon</a></code>(3) &#8211; LAN discovery and presence</dl>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-zclock/">zclock</a></code>(3) &#8211; millisecond clocks and delays</dl>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-zdir/">zdir</a></code>(3) &#8211; work with file-system directories</dl>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-zdir_patch/">zdir_patch</a></code>(3) &#8211; work with directory differences</dl>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-zfile/">zfile</a></code>(3) &#8211; work with file-system files</dl>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-zsys/">zsys</a></code>(3) &#8211; system-level methods</dl>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-zuuid/">zuuid</a></code>(3) &#8211; UUID support class</dl>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-ziflist/">ziflist</a></code>(3) &#8211; list available network interfaces</dl>
<p> And these utility classes add value: </p>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-zchunk/">zchunk</a></code>(3) &#8211; work with memory chunks</dl>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-zconfig/">zconfig</a></code>(3) &#8211; work with textual config files</dl>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-zrex/">zrex</a></code>(3) &#8211; work with regular expressions</dl>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-zgossip/">zgossip</a></code>(3) &#8211; decentralized configuration management</dl>
<p> These classes are deprecated: </p>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-zctx/">zctx</a></code>(3) &#8211; working with ZeroMQ contexts</dl>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-zsocket/">zsocket</a></code>(3) &#8211; working with ZeroMQ sockets (low-level)</dl>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-zsockopt/">zsockopt</a></code>(3) &#8211; get/set ZeroMQ socket options</dl>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-zthread/">zthread</a></code>(3) &#8211; working with system threads</dl>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-zauth_v2/">zauth_v2</a></code>(3) &#8211; authentication for ZeroMQ servers</dl>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-zbeacon_v2/">zbeacon_v2</a></code>(3) &#8211; LAN discovery and presence</dl>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-zmonitor_v2/">zmonitor_v2</a></code>(3) &#8211; socket event monitor</dl>
<dl>
<dd>&bull; </p>
<p> <code><a href="/docs/linux/man/3-zproxy_v2/">zproxy_v2</a></code>(3) &#8211; zmq_proxy wrapper</dl>
<h3>Scope and Goals</h3>
<p>CZMQ has these goals: </p>
<dl>
<dd>&bull; To wrap the &Oslash;MQ core API in semantics that are natural and lead to shorter, more readable applications.</dl>
<dl>
<dd>&bull; To hide the differences between versions of &Oslash;MQ.</dl>
<dl>
<dd>&bull; To provide a space for development of more sophisticated API semantics.</dl>
<h3>Ownership and License</h3>
<p>CZMQ is maintained by the ZeroMQ community at github.com/zeromq. Its other authors and contributors are listed in the AUTHORS file. </p>
<p> The contributors are listed in AUTHORS. This project uses the MPL v2 license, see LICENSE.</p>
<h3>Contributing</h3>
<p>To submit an issue use the issue tracker at m[blue]<code><a rel="nofollow" href="http://github.com/zeromq/czmq/issues">http://github.com/zeromq/czmq/issues</a></code>m[]. All discussion happens on the zeromq-dev list or #zeromq IRC channel at irc.freenode.net. </p>
<p> The proper way to submit patches is to clone this repository, make your changes, and use git to create a patch or a pull request. See m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[]. All contributors are listed in AUTHORS. </p>
<p> All classes are maintained by a single person, who is the responsible editor for that class and who is named in the header as such. This is usually the originator of the class. When several people collaborate on a class, one single person is always the lead maintainer and the one to blame when it breaks. </p>
<p> The general rule is, if you contribute code to CZMQ you must be willing to maintain it as long as there are users of it. Code with no active maintainer will in general be deprecated and/or removed.</p>
<h2>Using Czmq</h2>
<h3>Building and Installing</h3>
<p>CZMQ uses autotools for packaging. To build from git (all example commands are for Linux): </p>
<dl>
<dd>
<pre> git clone <a href="git://github.com/zeromq/czmq.git">git://github.com/zeromq/czmq.git</a>
 cd czmq
 sh autogen.sh
 ./configure
 make all
 sudo make install
 sudo ldconfig</pre>
</dl>
<p> You will need the pkg-config, libtool, and autoreconf packages. Set the LD_LIBRARY_PATH to /usr/local/libs unless you install elsewhere. </p>
<p> After building, you can run the CZMQ selftests: </p>
<dl>
<dd>
<pre> cd src
 ./czmq_selftest</pre>
</dl>
<h3>Linking with an Application</h3>
<p>Include czmq.h in your application and link with CZMQ. Here is a typical gcc link command: </p>
<dl>
<dd>
<pre> gcc -lczmq -lzmq myapp.c -o myapp</pre>
</dl>
<p> You should read czmq.h. This file includes zmq.h and the system header files that typical &Oslash;MQ applications will need. The provided <i>c</i> shell script lets you write simple portable build scripts: </p>
<dl>
<dd>
<pre> c -lczmq -lzmq -l myapp</pre>
</dl>
<h3>The Class Model</h3>
<p>CZMQ consists of classes, each class consisting of a .h and a .c. Classes may depend on other classes. </p>
<p> czmq.h includes all classes header files, all the time. For the user, CZMQ forms one single package. All classes start by including czmq.h. All applications that use CZMQ start by including czmq.h. czmq.h also defines a limited number of small, useful macros and typedefs that have proven useful for writing clearer C code. </p>
<p> All classes (with some exceptions) are based on a flat C class system and follow these rules (where <i>zclass</i> is the class name): </p>
<dl>
<dd>&bull; Class typedef: zclass_t</dl>
<dl>
<dd>&bull; Constructor: zclass_new</dl>
<dl>
<dd>&bull; Destructor: zclass_destroy</dl>
<dl>
<dd>&bull; Property methods: zclass_property_set, zclass_property</dl>
<dl>
<dd>&bull; Class structures are private (defined in the .c source but not the .h)</dl>
<dl>
<dd>&bull; Properties are accessed only via methods named as described above.</dl>
<dl>
<dd>&bull; In the class source code the object is always called self.</dl>
<dl>
<dd>&bull; The constructor may take arbitrary arguments, and returns NULL on failure, or a new object.</dl>
<dl>
<dd>&bull; The destructor takes a pointer to an object reference and nullifies it.</dl>
<p> Return values for methods are: </p>
<dl>
<dd>&bull; For methods that return an object reference, either the reference, or NULL on failure.</dl>
<dl>
<dd>&bull; For methods that signal success/failure, a return value of 0 means sucess, -1 failure.</dl>
<p> Private/static functions in a class are named s_functionname and are not exported via the header file. </p>
<p> All classes (with some exceptions) have a test method called zclass_test.</p>
<h2>Design Ideology</h2>
<h3>The Problem with C</h3>
<p>C has the significant advantage of being a small language that, if we take a little care with formatting and naming, can be easily interchanged between developers. Every C developer will use much the same 90% of the language. Larger languages like C++ provide powerful abstractions like STL containers but at the cost of interchange. </p>
<p> The huge problem with C is that any realistic application needs packages of functionality to bring the language up to the levels we expect for the 21st century. Much can be done by using external libraries but every additional library is a dependency that makes the resulting applications harder to build and port. While C itself is a highly portable language (and can be made more so by careful use of the preprocessor), most C libraries consider themselves part of the operating system, and as such do not attempt to be portable. </p>
<p> The answer to this, as we learned from building enterprise-level C applications at iMatix from 1995-2005, is to create our own fully portable, high-quality libraries of pre-packaged functionality, in C. Doing this right solves both the requirements of richness of the language, and of portability of the final applications.</p>
<h3>A Simple Class Model</h3>
<p>C has no standard API style. It is one thing to write a useful component, but something else to provide an API that is consistent and obvious across many components. We learned from building OpenAMQ (m[blue]<code><a rel="nofollow" href="http://www.openamq.org">http://www.openamq.org</a></code>m[]), a messaging client and server of 0.5M LoC, that a consistent model for extending C makes life for the application developer much easier. </p>
<p> The general model is that of a class (the source package) that provides objects (in fact C structures). The application creates objects and then works with them. When done, the application destroys the object. In C, we tend to use the same name for the object as the class, when we can, and it looks like this (to take a fictitious CZMQ class): </p>
<dl>
<dd>
<pre> zregexp_t *regexp = zregexp_new (regexp_string);
 if (!regexp)
 printf (&quot;E: invalid regular expression: %s
&quot;, regexp_string);
 else
 if (zregexp_match (regexp, input_buffer))
 printf (&quot;I: successful match for %s
&quot;, input buffer);
 zregexp_destroy (&amp;amp;regexp);</pre>
</dl>
<p> As far as the C program is concerned, the object is a reference to a structure (not a void pointer). We pass the object reference to all methods, since this is still C. We could do weird stuff like put method addresses into the structure so that we can emulate a C++ syntax but it&#8217;s not worthwhile. The goal is not to emulate an OO system, it&#8217;s simply to gain consistency. The constructor returns an object reference, or NULL if it fails. The destructor nullifies the class pointer, and is idempotent. </p>
<p> What we aim at here is the simplest possible consistent syntax. </p>
<p> No model is fully consistent, and classes can define their own rules if it helps make a better result. For example: </p>
<dl>
<dd>&bull; Some classes may not be opaque. For example, we have cases of generated serialization classes that encode and decode structures to/from binary buffers. It feels clumsy to have to use methods to access the properties of these classes.</dl>
<dl>
<dd>&bull; While every class has a new method that is the formal constructor, some methods may also act as constructors. For example, a &quot;dup&quot; method might take one object and return a second object.</dl>
<dl>
<dd>&bull; While every class has a destroy method that is the formal destructor, some methods may also act as destructors. For example, a method that sends an object may also destroy the object (so that ownership of any buffers can passed to background threads). Such methods take the same &quot;pointer to a reference&quot; argument as the destroy method.</dl>
<h3>Naming Style</h3>
<p>CZMQ aims for short, consistent names, following the theory that names we use most often should be shortest. Classes get one-word names, unless they are part of a family of classes in which case they may be two words, the first being the family name. Methods, similarly, get one-word names and we aim for consistency across classes (so a method that does something semantically similar in two classes will get the same name in both). So the canonical name for any method is: </p>
<dl>
<dd>
<pre> zclassname_methodname</pre>
</dl>
<p> And the reader can easily parse this without needing special syntax to separate the class name from the method name.</p>
<h3>Containers</h3>
<p>After a long experiment with containers, we&#8217;ve decided that we need exactly two containers: </p>
<dl>
<dd>&bull; A singly-linked list.</dl>
<dl>
<dd>&bull; A hash table using text keys.</dl>
<p> These are zlist and zhash, respectively. Both store void pointers, with no attempt to manage the details of contained objects. You can use these containers to create lists of lists, hashes of lists, hashes of hashes, etc. </p>
<p> We assume that at some point we&#8217;ll need to switch to a doubly-linked list.</p>
<h3>Portability</h3>
<p>Creating a portable C application can be rewarding in terms of maintaining a single code base across many platforms, and keeping (expensive) system-specific knowledge separate from application developers. In most projects (like &Oslash;MQ core), there is no portability layer and application code does conditional compilation for all mixes of platforms. This leads to quite messy code. </p>
<p> czmq acts as a portability layer, similar to but thinner than libraries like the [Apache Portable Runtime](m[blue]<code><a rel="nofollow" href="http://apr.apache.org">http://apr.apache.org</a></code>m[]) (APR). </p>
<p> These are the places a C application is subject to arbitrary system differences: </p>
<dl>
<dd>&bull; Different compilers may offer slightly different variants of the C language, often lacking specific types or using neat non-portable names. Windows is a big culprit here. We solve this by <i>patching</i> the language in czmq_prelude.h, e.g. defining int64_t on Windows.</dl>
<dl>
<dd>&bull; System header files are inconsistent, i.e. you need to include different files depending on the OS type and version. We solve this by pulling in all necessary header files in czmq_prelude.h. This is a proven brute-force approach that increases recompilation times but eliminates a major source of pain.</dl>
<dl>
<dd>&bull; System libraries are inconsistent, i.e. you need to link with different libraries depending on the OS type and version. We solve this with an external compilation tool, <i>C</i>, which detects the OS type and version (at runtime) and builds the necessary link commands.</dl>
<dl>
<dd>&bull; System functions are inconsistent, i.e. you need to call different functions depending, again, on OS type and version. We solve this by building small abstract classes that handle specific areas of functionality, and doing conditional compilation in these.</dl>
<p> An example of the last: </p>
<dl>
<dd>
<pre> #if (defined (__UNIX__))
 pid = GetCurrentProcessId();
 #elif (defined (__WINDOWS__))
 pid = getpid ();
 #else
 pid = 0;
 #endif</pre>
</dl>
<p> CZMQ uses the GNU autotools system, so non-portable code can use the macros this defines. It can also use macros defined by the czmq_prelude.h header file.</p>
<h3>Technical Aspects</h3>
<dl>
<dd>&bull; </p>
<p> <code>Thread safety</code>: the use of opaque structures is thread safe, though &Oslash;MQ applications should not share state between threads in any case.</dl>
<dl>
<dd>&bull; </p>
<p> <code>Name spaces</code>: we prefix class names with z, which ensures that all exported functions are globally safe.</dl>
<dl>
<dd>&bull; </p>
<p> <code>Library versioning</code>: we don&#8217;t make any attempt to version the library at this stage. Classes are in our experience highly stable once they are built and tested, the only changes typically being added methods.</dl>
<dl>
<dd>&bull; </p>
<p> <code>Performance</code>: for critical path processing, you may want to avoid creating and destroying classes. However on modern Linux systems the heap allocator is very fast. Individual classes can choose whether or not to nullify their data on allocation.</dl>
<dl>
<dd>&bull; </p>
<p> <code>Self-testing</code>: every class has a selftest method that runs through the methods of the class. In theory, calling all selftest functions of all classes does a full unit test of the library. The czmq_selftest application does this.</dl>
<dl>
<dd>&bull; </p>
<p> <code>Memory management</code>: CZMQ classes do not use any special memory management techiques to detect leaks. We&#8217;ve done this in the past but it makes the code relatively complex. Instead, we do memory leak testing using tools like valgrind.</dl>
<h2>Under The Hood</h2>
<h3>Adding a New Class</h3>
<p>If you define a new CZMQ class myclass you need to: </p>
<dl>
<dd>&bull; Write the zmyclass.c and zmyclass.h source files, in src and include respectively.</dl>
<dl>
<dd>&bull; Add`#include &lt;zmyclass.h&gt;` to include/czmq.h.</dl>
<dl>
<dd>&bull; Add the myclass header and test call to src/czmq_selftest.c.</dl>
<dl>
<dd>&bull; Add a reference documentation to <i>doc/zmyclass.txt</i>.</dl>
<dl>
<dd>&bull; Add myclass to &#8216;src/Makefile.am` and doc/Makefile.am.</dl>
<p> The bin/newclass.sh shell script will automate these steps for you.</p>
<h3>Coding Style</h3>
<p>In general the zctx class defines the style for the whole library. The overriding rules for coding style are consistency, clarity, and ease of maintenance. We use the C99 standard for syntax including principally: </p>
<dl>
<dd>&bull; The // comment style.</dl>
<dl>
<dd>&bull; Variables definitions placed in or before the code that uses them.</dl>
<p> So while ANSI C code might say: </p>
<dl>
<dd>
<pre> zblob_t *file_buffer; /* Buffer for our file */
 ... (100 lines of code)
 file_buffer = zblob_new ();
 ...</pre>
</dl>
<p> The style in CZMQ would be: </p>
<dl>
<dd>
<pre> zblob_t *file_buffer = zblob_new ();</pre>
</dl>
<h3>Assertions</h3>
<p>We use assertions heavily to catch bad argument values. The CZMQ classes do not attempt to validate arguments and report errors; bad arguments are treated as fatal application programming errors. </p>
<p> We also use assertions heavily on calls to system functions that are never supposed to fail, where failure is to be treated as a fatal non-recoverable error (e.g. running out of memory). </p>
<p> Assertion code should always take this form: </p>
<dl>
<dd>
<pre> int rc = some_function (arguments);
 assert (rc == 0);</pre>
</dl>
<p> Rather than the side-effect form: </p>
<dl>
<dd>
<pre> assert (some_function (arguments) == 0);</pre>
</dl>
<p> Since assertions may be removed by an optimizing compiler.</p>
<h3>Documentation</h3>
<p>Man pages are generated from the class header and source files via the doc/mkman tool, and similar functionality in the gitdown tool (m[blue]<code><a rel="nofollow" href="http://github.com/imatix/gitdown">http://github.com/imatix/gitdown</a></code>m[]). The header file for a class must wrap its interface as follows (example is from include/zclock.h): </p>
<dl>
<dd>
<pre> // @interface
 // Sleep for a number of milliseconds
 void
 zclock_sleep (int msecs);
 // Return current system clock as milliseconds
 int64_t
 zclock_time (void);
 // Self test of this class
 int
 zclock_test (Bool verbose);
 // @end</pre>
</dl>
<p> The source file for a class must provide documentation as follows: </p>
<dl>
<dd>
<pre> /*
 @header
 ...short explanation of class...
 @discuss
 ...longer discussion of how it works...
 @end
 */</pre>
</dl>
<p> The source file for a class then provides the self test example as follows: </p>
<dl>
<dd>
<pre> // @selftest
 int64_t start = zclock_time ();
 zclock_sleep (10);
 assert ((zclock_time () - start) &gt;= 10);
 // @end</pre>
</dl>
<p> The template for man pages is in doc/mkman.</p>
<h3>Development</h3>
<p>CZMQ is developed through a test-driven process that guarantees no memory violations or leaks in the code: </p>
<dl>
<dd>&bull; Modify a class or method.</dl>
<dl>
<dd>&bull; Update the test method for that class.</dl>
<dl>
<dd>&bull; Run the <i>selftest</i> script, which uses the Valgrind memcheck tool.</dl>
<dl>
<dd>&bull; Repeat until perfect.</dl>
<h3>Porting CZMQ</h3>
<p>When you try CZMQ on an OS that it&#8217;s not been used on (ever, or for a while), you will hit code that does not compile. In some cases the patches are trivial, in other cases (usually when porting to Windows), the work needed to build equivalent functionality may be quite heavy. In any case, the benefit is that once ported, the functionality is available to all applications. </p>
<p> Before attempting to patch code for portability, please read the czmq_prelude.h header file. There are several typical types of changes you may need to make to get functionality working on a specific operating system: </p>
<dl>
<dd>&bull; Defining typedefs which are missing on that specific compiler: do this in czmq_prelude.h.</dl>
<dl>
<dd>&bull; Defining macros that rename exotic library functions to more conventional names: do this in czmq_prelude.h.</dl>
<dl>
<dd>&bull; Reimplementing specific methods to use a non-standard API: this is typically needed on Windows. Do this in the relevant class, using #ifdefs to properly differentiate code for different platforms.</dl>
<p> The canonical <i>standard operating system</i> for all CZMQ code is Linux, gcc, POSIX.</p>
<h2>Authors</h2>
<p>The czmq manual was written by the authors in the AUTHORS file.</p>
<h2>Resources</h2>
<p>Main web site: m[blue]m[] </p>
<p> Report bugs to the email &lt;m[blue]<code>zeromq-dev [at] lists.zeromq.org</code>m[]<font SIZE="-2">[1]</font>&gt;</p>
<h2>Copyright</h2>
<p>Copyright (c) 1991-2012 iMatix Corporation &#8212; <a rel="nofollow" href="http://www.imatix.com">http://www.imatix.com</a> Copyright other contributors as noted in the AUTHORS file. This file is part of CZMQ, the high-level C binding for 0MQ: <a href="http://czmq.zeromq.org">http://czmq.zeromq.org</a> This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at <a href="http://mozilla.org/MPL/2.0/.">http://mozilla.org/MPL/2.0/.</a> LICENSE included with the czmq distribution.</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>zeromq-dev [at] lists.zeromq.org</p>
<dl>
<dd>mailto:zeromq-dev [at] lists.zeromq.org</dl>

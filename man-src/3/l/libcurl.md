---
title: "libcurl(3)"
name: "libcurl"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libcurl/"
description: "libcurl – client-side URL transfers"
---

<h2>NAME</h2>
<p> libcurl &#8211; client-side URL transfers</p>
<h2>DESCRIPTION</h2>
<p> This is a short overview on how to use libcurl in your C programs. There are specific man pages for each function mentioned in here. There are also the <i><a href="/docs/linux/man/3-libcurl-easy/">libcurl-easy</a>(3)</i> man page, the <i><a href="/docs/linux/man/3-libcurl-multi/">libcurl-multi</a>(3)</i> man page, the <i><a href="/docs/linux/man/3-libcurl-share/">libcurl-share</a>(3)</i> man page and the <i><a href="/docs/linux/man/3-libcurl-tutorial/">libcurl-tutorial</a>(3)</i> man page for in-depth understanding on how to program with libcurl. </p>
<p> There are more than thirty custom bindings available that bring libcurl access to your favourite language. Look elsewhere for documentation on those. </p>
<p> libcurl has a global constant environment that you must set up and maintain while using libcurl. This essentially means you call <i><a href="/docs/linux/man/3-curl_global_init/">curl_global_init</a>(3)</i> at the start of your program and <i><a href="/docs/linux/man/3-curl_global_cleanup/">curl_global_cleanup</a>(3)</i> at the end. See GLOBAL CONSTANTS below for details. </p>
<p> To transfer files, you always set up an &quot;easy handle&quot; using <i><a href="/docs/linux/man/3-curl_easy_init/">curl_easy_init</a>(3)</i>, but when you want the file(s) transferred you have the option of using the &quot;easy&quot; interface, or the &quot;multi&quot; interface. </p>
<p> The easy interface is a synchronous interface with which you call <i><a href="/docs/linux/man/3-curl_easy_perform/">curl_easy_perform</a>(3)</i> and let it perform the transfer. When it is completed, the function returns and you can continue. More details are found in the <i><a href="/docs/linux/man/3-libcurl-easy/">libcurl-easy</a>(3)</i> man page. </p>
<p> The multi interface on the other hand is an asynchronous interface, that you call and that performs only a little piece of the transfer on each invoke. It is perfect if you want to do things while the transfer is in progress, or similar. The multi interface allows you to select() on libcurl action, and even to easily download multiple files simultaneously using a single thread. See further details in the <i><a href="/docs/linux/man/3-libcurl-multi/">libcurl-multi</a>(3)</i> man page. </p>
<p> You can have multiple easy handles share certain data, even if they are used in different threads. This magic is setup using the share interface, as described in the <i><a href="/docs/linux/man/3-libcurl-share/">libcurl-share</a>(3)</i> man page. </p>
<p> There is also a series of other helpful functions to use, including these:</p>
<dl>
<dt>
<dd>
<dl>
<dt>curl_version_info()</p>
<dd> gets detailed libcurl (and other used libraries) version info</p>
<dt>curl_getdate()</p>
<dd> converts a date string to time_t</p>
<dt>curl_easy_getinfo()</p>
<dd> get information about a performed transfer</p>
<dt>curl_formadd()</p>
<dd> helps building an HTTP form POST</p>
<dt>curl_formfree()</p>
<dd> free a list built with <i><a href="/docs/linux/man/3-curl_formadd/">curl_formadd</a>(3)</i></p>
<dt>curl_slist_append()</p>
<dd> builds a linked list</p>
<dt>curl_slist_free_all()</p>
<dd> frees a whole curl_slist</dl>
</dl>
<h2>LINKING WITH LIBCURL</h2>
<p> On unix-like machines, there&#8217;s a tool named curl-config that gets installed with the rest of the curl stuff when &#8216;make install&#8217; is performed. </p>
<p> curl-config is added to make it easier for applications to link with libcurl and developers to learn about libcurl and how to use it. </p>
<p> Run &#8216;curl-config &#8211;libs&#8217; to get the (additional) linker options you need to link with the particular version of libcurl you&#8217;ve installed. See the <i><a href="/docs/linux/man/1-curl-config/">curl-config</a>(1)</i> man page for further details. </p>
<p> Unix-like operating system that ship libcurl as part of their distributions often don&#8217;t provide the curl-config tool, but simply install the library and headers in the common path for this purpose. </p>
<h2>LIBCURL SYMBOL NAMES</h2>
<p> All public functions in the libcurl interface are prefixed with &#8216;curl_&#8217; (with a lowercase c). You can find other functions in the library source code, but other prefixes indicate that the functions are private and may change without further notice in the next release. </p>
<p> Only use documented functions and functionality!</p>
<h2>PORTABILITY</h2>
<p> libcurl works <code>exactly</code> the same, on any of the platforms it compiles and builds on.</p>
<h2>THREADS</h2>
<p> Never ever call curl-functions simultaneously using the same handle from several threads. libcurl is thread-safe and can be used in any number of threads, but you must use separate curl handles if you want to use libcurl in more than one thread simultaneously. </p>
<p> The global environment functions are not thread-safe. See GLOBAL CONSTANTS below for details. </p>
<h2>PERSISTENT CONNECTIONS</h2>
<p> Persistent connections means that libcurl can re-use the same connection for several transfers, if the conditions are right. </p>
<p> libcurl will <code>always</code> attempt to use persistent connections. Whenever you use <i><a href="/docs/linux/man/3-curl_easy_perform/">curl_easy_perform</a>(3)</i> or <i><a href="/docs/linux/man/3-curl_multi_perform/">curl_multi_perform</a>(3)</i>, libcurl will attempt to use an existing connection to do the transfer, and if none exists it&#8217;ll open a new one that will be subject for re-use on a possible following call to <i><a href="/docs/linux/man/3-curl_easy_perform/">curl_easy_perform</a>(3)</i> or <i><a href="/docs/linux/man/3-curl_multi_perform/">curl_multi_perform</a>(3)</i>. </p>
<p> To allow libcurl to take full advantage of persistent connections, you should do as many of your file transfers as possible using the same curl handle. When you call <i><a href="/docs/linux/man/3-curl_easy_cleanup/">curl_easy_cleanup</a>(3)</i>, all the possibly open connections held by libcurl will be closed and forgotten. </p>
<p> Note that the options set with <i><a href="/docs/linux/man/3-curl_easy_setopt/">curl_easy_setopt</a>(3)</i> will be used on every repeated <i><a href="/docs/linux/man/3-curl_easy_perform/">curl_easy_perform</a>(3)</i> call. </p>
<h2>GLOBAL CONSTANTS</h2>
<p> There are a variety of constants that libcurl uses, mainly through its internal use of other libraries, which are too complicated for the library loader to set up. Therefore, a program must call a library function after the program is loaded and running to finish setting up the library code. For example, when libcurl is built for SSL capability via the GNU TLS library, there is an elaborate tree inside that library that describes the SSL protocol. </p>
<p> <i>curl_global_init()</i> is the function that you must call. This may allocate resources (e.g. the memory for the GNU TLS tree mentioned above), so the companion function <i>curl_global_cleanup()</i> releases them. </p>
<p> The basic rule for constructing a program that uses libcurl is this: Call <i>curl_global_init()</i>, with a <i>CURL_GLOBAL_ALL</i> argument, immediately after the program starts, while it is still only one thread and before it uses libcurl at all. Call <i>curl_global_cleanup()</i> immediately before the program exits, when the program is again only one thread and after its last use of libcurl. </p>
<p> You can call both of these multiple times, as long as all calls meet these requirements and the number of calls to each is the same. </p>
<p> It isn&#8217;t actually required that the functions be called at the beginning and end of the program &#8212; that&#8217;s just usually the easiest way to do it. It <i>is</i> required that the functions be called when no other thread in the program is running. </p>
<p> These global constant functions are <i>not thread safe</i>, so you must not call them when any other thread in the program is running. It isn&#8217;t good enough that no other thread is using libcurl at the time, because these functions internally call similar functions of other libraries, and those functions are similarly thread-unsafe. You can&#8217;t generally know what these libraries are, or whether other threads are using them. </p>
<p> The global constant situation merits special consideration when the code you are writing to use libcurl is not the main program, but rather a modular piece of a program, e.g. another library. As a module, your code doesn&#8217;t know about other parts of the program &#8212; it doesn&#8217;t know whether they use libcurl or not. And its code doesn&#8217;t necessarily run at the start and end of the whole program. </p>
<p> A module like this must have global constant functions of its own, just like <i>curl_global_init()</i> and <i>curl_global_cleanup()</i>. The module thus has control at the beginning and end of the program and has a place to call the libcurl functions. Note that if multiple modules in the program use libcurl, they all will separately call the libcurl functions, and that&#8217;s OK because only the first <i>curl_global_init()</i> and the last <i>curl_global_cleanup()</i> in a program change anything. (libcurl uses a reference count in static memory). </p>
<p> In a C++ module, it is common to deal with the global constant situation by defining a special class that represents the global constant environment of the module. A program always has exactly one object of the class, in static storage. That way, the program automatically calls the constructor of the object as the program starts up and the destructor as it terminates. As the author of this libcurl-using module, you can make the constructor call <i>curl_global_init()</i> and the destructor call <i>curl_global_cleanup()</i> and satisfy libcurl&#8217;s requirements without your user having to think about it. </p>
<p> <i>curl_global_init()</i> has an argument that tells what particular parts of the global constant environment to set up. In order to successfully use any value except <i>CURL_GLOBAL_ALL</i> (which says to set up the whole thing), you must have specific knowledge of internal workings of libcurl and all other parts of the program of which it is part. </p>
<p> A special part of the global constant environment is the identity of the memory allocator. <i>curl_global_init()</i> selects the system default memory allocator, but you can use <i>curl_global_init_mem()</i> to supply one of your own. However, there is no way to use <i>curl_global_init_mem()</i> in a modular program &#8212; all modules in the program that might use libcurl would have to agree on one allocator. </p>
<p> There is a failsafe in libcurl that makes it usable in simple situations without you having to worry about the global constant environment at all: <i>curl_easy_init()</i> sets up the environment itself if it hasn&#8217;t been done yet. The resources it acquires to do so get released by the operating system automatically when the program exits. </p>
<p> This failsafe feature exists mainly for backward compatibility because there was a time when the global functions didn&#8217;t exist. Because it is sufficient only in the simplest of programs, it is not recommended for any program to rely on it. </p>
<h2>Index</h2>

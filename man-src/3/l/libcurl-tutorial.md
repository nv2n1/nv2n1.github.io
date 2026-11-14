---
title: "libcurl-tutorial(3)"
name: "libcurl-tutorial"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libcurl-tutorial/"
description: "libcurl-tutorial – libcurl programming tutorial"
---

<h2>NAME</h2>
<p> libcurl-tutorial &#8211; libcurl programming tutorial</p>
<h2>Objective</h2>
<p> This document attempts to describe the general principles and some basic approaches to consider when programming with libcurl. The text will focus mainly on the C interface but might apply fairly well on other interfaces as well as they usually follow the C one pretty closely. </p>
<p> This document will refer to &#8216;the user&#8217; as the person writing the source code that uses libcurl. That would probably be you or someone in your position. What will be generally referred to as &#8216;the program&#8217; will be the collected source code that you write that is using libcurl for transfers. The program is outside libcurl and libcurl is outside of the program. </p>
<p> To get more details on all options and functions described herein, please refer to their respective man pages. </p>
<h2>Building</h2>
<p> There are many different ways to build C programs. This chapter will assume a UNIX-style build process. If you use a different build system, you can still read this to get general information that may apply to your environment as well.</p>
<dl>
<dt>Compiling the Program</p>
<dd> Your compiler needs to know where the libcurl headers are located. Therefore you must set your compiler&#8217;s include path to point to the directory where you installed them. The &#8216;curl-config'[3] tool can be used to get this information: </p>
<p> $ curl-config &#8211;cflags </p>
<dt>Linking the Program with libcurl</p>
<dd> When having compiled the program, you need to link your object files to create a single executable. For that to succeed, you need to link with libcurl and possibly also with other libraries that libcurl itself depends on. Like the OpenSSL libraries, but even some standard OS libraries may be needed on the command line. To figure out which flags to use, once again the &#8216;curl-config&#8217; tool comes to the rescue: </p>
<p> $ curl-config &#8211;libs </p>
<dt>SSL or Not</p>
<dd> libcurl can be built and customized in many ways. One of the things that varies from different libraries and builds is the support for SSL-based transfers, like HTTPS and FTPS. If a supported SSL library was detected properly at build-time, libcurl will be built with SSL support. To figure out if an installed libcurl has been built with SSL support enabled, use &#8216;curl-config&#8217; like this: </p>
<p> $ curl-config &#8211;feature </p>
<p> And if SSL is supported, the keyword &#8216;SSL&#8217; will be written to stdout, possibly together with a few other features that could be either on or off on for different libcurls. </p>
<p> See also the &quot;Features libcurl Provides&quot; further down.</p>
<dt>autoconf macro</p>
<dd> When you write your configure script to detect libcurl and setup variables accordingly, we offer a prewritten macro that probably does everything you need in this area. See docs/libcurl/libcurl.m4 file &#8211; it includes docs on how to use it. </p>
</dl>
<h2>Portable Code in a Portable World</h2>
<p> The people behind libcurl have put a considerable effort to make libcurl work on a large amount of different operating systems and environments. </p>
<p> You program libcurl the same way on all platforms that libcurl runs on. There are only very few minor considerations that differ. If you just make sure to write your code portable enough, you may very well create yourself a very portable program. libcurl shouldn&#8217;t stop you from that. </p>
<h2>Global Preparation</h2>
<p> The program must initialize some of the libcurl functionality globally. That means it should be done exactly once, no matter how many times you intend to use the library. Once for your program&#8217;s entire life time. This is done using </p>
<p>&nbsp;<wbr>curl_global_init() </p>
<p> and it takes one parameter which is a bit pattern that tells libcurl what to initialize. Using <i>CURL_GLOBAL_ALL</i> will make it initialize all known internal sub modules, and might be a good default option. The current two bits that are specified are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>CURL_GLOBAL_WIN32</p>
<dd> which only does anything on Windows machines. When used on a Windows machine, it&#8217;ll make libcurl initialize the win32 socket stuff. Without having that initialized properly, your program cannot use sockets properly. You should only do this once for each application, so if your program already does this or of another library in use does it, you should not tell libcurl to do this as well.</p>
<dt>CURL_GLOBAL_SSL</p>
<dd> which only does anything on libcurls compiled and built SSL-enabled. On these systems, this will make libcurl initialize the SSL library properly for this application. This only needs to be done once for each application so if your program or another library already does this, this bit should not be needed.</dl>
</dl>
<p> libcurl has a default protection mechanism that detects if <i><a href="/docs/linux/man/3-curl_global_init/">curl_global_init</a>(3)</i> hasn&#8217;t been called by the time <i><a href="/docs/linux/man/3-curl_easy_perform/">curl_easy_perform</a>(3)</i> is called and if that is the case, libcurl runs the function itself with a guessed bit pattern. Please note that depending solely on this is not considered nice nor very good. </p>
<p> When the program no longer uses libcurl, it should call <i><a href="/docs/linux/man/3-curl_global_cleanup/">curl_global_cleanup</a>(3)</i>, which is the opposite of the init call. It will then do the reversed operations to cleanup the resources the <i><a href="/docs/linux/man/3-curl_global_init/">curl_global_init</a>(3)</i> call initialized. </p>
<p> Repeated calls to <i><a href="/docs/linux/man/3-curl_global_init/">curl_global_init</a>(3)</i> and <i><a href="/docs/linux/man/3-curl_global_cleanup/">curl_global_cleanup</a>(3)</i> should be avoided. They should only be called once each. </p>
<h2>Features libcurl Provides</h2>
<p> It is considered best-practice to determine libcurl features at run-time rather than at build-time (if possible of course). By calling <i><a href="/docs/linux/man/3-curl_version_info/">curl_version_info</a>(3)</i> and checking out the details of the returned struct, your program can figure out exactly what the currently running libcurl supports. </p>
<h2>Handle the Easy libcurl</h2>
<p> libcurl first introduced the so called easy interface. All operations in the easy interface are prefixed with &#8216;curl_easy&#8217;. </p>
<p> Recent libcurl versions also offer the multi interface. More about that interface, what it is targeted for and how to use it is detailed in a separate chapter further down. You still need to understand the easy interface first, so please continue reading for better understanding. </p>
<p> To use the easy interface, you must first create yourself an easy handle. You need one handle for each easy session you want to perform. Basically, you should use one handle for every thread you plan to use for transferring. You must never share the same handle in multiple threads. </p>
<p> Get an easy handle with </p>
<p>&nbsp;<wbr>easyhandle&nbsp;<wbr>=&nbsp;<wbr>curl_easy_init(); </p>
<p> It returns an easy handle. Using that you proceed to the next step: setting up your preferred actions. A handle is just a logic entity for the upcoming transfer or series of transfers. </p>
<p> You set properties and options for this handle using <i><a href="/docs/linux/man/3-curl_easy_setopt/">curl_easy_setopt</a>(3)</i>. They control how the subsequent transfer or transfers will be made. Options remain set in the handle until set again to something different. Alas, multiple requests using the same handle will use the same options. </p>
<p> Many of the options you set in libcurl are &quot;strings&quot;, pointers to data terminated with a zero byte. When you set strings with <i><a href="/docs/linux/man/3-curl_easy_setopt/">curl_easy_setopt</a>(3)</i>, libcurl makes its own copy so that they don&#8217;t need to be kept around in your application after being set[4]. </p>
<p> One of the most basic properties to set in the handle is the URL. You set your preferred URL to transfer with CURLOPT_URL in a manner similar to: </p>
<pre>
 curl_easy_setopt(handle, CURLOPT_URL, &quot;<a rel="nofollow" href="http://domain.com/">http://domain.com/</a>&quot;);
</pre>
<p> Let&#8217;s assume for a while that you want to receive data as the URL identifies a remote resource you want to get here. Since you write a sort of application that needs this transfer, I assume that you would like to get the data passed to you directly instead of simply getting it passed to stdout. So, you write your own function that matches this prototype: </p>
<p>&nbsp;<wbr>size_t write_data(void&nbsp;<wbr>*buffer, size_t size, size_t nmemb, void&nbsp;<wbr>*userp); </p>
<p> You tell libcurl to pass all data to this function by issuing a function similar to this: </p>
<p>&nbsp;<wbr>curl_easy_setopt(easyhandle, CURLOPT_WRITEFUNCTION, write_data); </p>
<p> You can control what data your callback function gets in the fourth argument by setting another property: </p>
<p>&nbsp;<wbr>curl_easy_setopt(easyhandle, CURLOPT_WRITEDATA,&nbsp;<wbr>&amp;internal_struct); </p>
<p> Using that property, you can easily pass local data between your application and the function that gets invoked by libcurl. libcurl itself won&#8217;t touch the data you pass with <i>CURLOPT_WRITEDATA</i>. </p>
<p> libcurl offers its own default internal callback that will take care of the data if you don&#8217;t set the callback with <i>CURLOPT_WRITEFUNCTION</i>. It will then simply output the received data to stdout. You can have the default callback write the data to a different file handle by passing a &#8216;FILE *&#8217; to a file opened for writing with the <i>CURLOPT_WRITEDATA</i> option. </p>
<p> Now, we need to take a step back and have a deep breath. Here&#8217;s one of those rare platform-dependent nitpicks. Did you spot it? On some platforms[2], libcurl won&#8217;t be able to operate on files opened by the program. Thus, if you use the default callback and pass in an open file with <i>CURLOPT_WRITEDATA</i>, it will crash. You should therefore avoid this to make your program run fine virtually everywhere. </p>
<p> (<i>CURLOPT_WRITEDATA</i> was formerly known as <i>CURLOPT_FILE</i>. Both names still work and do the same thing). </p>
<p> If you&#8217;re using libcurl as a win32 DLL, you MUST use the <i>CURLOPT_WRITEFUNCTION</i> if you set <i>CURLOPT_WRITEDATA</i> &#8211; or you will experience crashes. </p>
<p> There are of course many more options you can set, and we&#8217;ll get back to a few of them later. Let&#8217;s instead continue to the actual transfer: </p>
<p>&nbsp;<wbr>success&nbsp;<wbr>=&nbsp;<wbr>curl_easy_perform(easyhandle); </p>
<p> <i><a href="/docs/linux/man/3-curl_easy_perform/">curl_easy_perform</a>(3)</i> will connect to the remote site, do the necessary commands and receive the transfer. Whenever it receives data, it calls the callback function we previously set. The function may get one byte at a time, or it may get many kilobytes at once. libcurl delivers as much as possible as often as possible. Your callback function should return the number of bytes it &quot;took care of&quot;. If that is not the exact same amount of bytes that was passed to it, libcurl will abort the operation and return with an error code. </p>
<p> When the transfer is complete, the function returns a return code that informs you if it succeeded in its mission or not. If a return code isn&#8217;t enough for you, you can use the CURLOPT_ERRORBUFFER to point libcurl to a buffer of yours where it&#8217;ll store a human readable error message as well. </p>
<p> If you then want to transfer another file, the handle is ready to be used again. Mind you, it is even preferred that you re-use an existing handle if you intend to make another transfer. libcurl will then attempt to re-use the previous connection. </p>
<p> For some protocols, downloading a file can involve a complicated process of logging in, setting the transfer mode, changing the current directory and finally transferring the file data. libcurl takes care of all that complication for you. Given simply the URL to a file, libcurl will take care of all the details needed to get the file moved from one machine to another. </p>
<h2>Multi-threading Issues</h2>
<p> The first basic rule is that you must <code>never</code> simultaneously share a libcurl handle (be it easy or multi or whatever) between multiple threads. Only use one handle in one thread at any time. You can pass the handles around among threads, but you must never use a single handle from more than one thread at any given time. </p>
<p> libcurl is completely thread safe, except for two issues: signals and SSL/TLS handlers. Signals are used for timing out name resolves (during DNS lookup) &#8211; when built without c-ares support and not on Windows. </p>
<p> If you are accessing HTTPS or FTPS URLs in a multi-threaded manner, you are then of course using the underlying SSL library multi-threaded and those libs might have their own requirements on this issue. Basically, you need to provide one or two functions to allow it to function properly. For all details, see this: </p>
<p> OpenSSL </p>
<p>&nbsp;<wbr><a rel="nofollow" href="http://www.openssl.org/docs/crypto/threads.html#DESCRIPTION">http://www.openssl.org/docs/crypto/threads.html#DESCRIPTION</a> </p>
<p> GnuTLS </p>
<p>&nbsp;<wbr><a rel="nofollow" href="http://www.gnu.org/software/gnutls/manual/html_node/Multi_002dthreaded-applications.html">http://www.gnu.org/software/gnutls/manual/html_node/Multi_002dthreaded-applications.html</a> </p>
<p> NSS </p>
<p>&nbsp;<wbr>is claimed to be thread-safe already without anything required. </p>
<p> PolarSSL </p>
<p>&nbsp;<wbr>Required actions unknown. </p>
<p> yassl </p>
<p>&nbsp;<wbr>Required actions unknown. </p>
<p> axTLS </p>
<p>&nbsp;<wbr>Required actions unknown. </p>
<p> When using multiple threads you should set the CURLOPT_NOSIGNAL option to 1 for all handles. Everything will or might work fine except that timeouts are not honored during the DNS lookup &#8211; which you can work around by building libcurl with c-ares support. c-ares is a library that provides asynchronous name resolves. On some platforms, libcurl simply will not function properly multi-threaded unless this option is set. </p>
<p> Also, note that CURLOPT_DNS_USE_GLOBAL_CACHE is not thread-safe. </p>
<h2>When It Doesn&#8217;t Work</h2>
<p> There will always be times when the transfer fails for some reason. You might have set the wrong libcurl option or misunderstood what the libcurl option actually does, or the remote server might return non-standard replies that confuse the library which then confuses your program. </p>
<p> There&#8217;s one golden rule when these things occur: set the CURLOPT_VERBOSE option to 1. It&#8217;ll cause the library to spew out the entire protocol details it sends, some internal info and some received protocol data as well (especially when using FTP). If you&#8217;re using HTTP, adding the headers in the received output to study is also a clever way to get a better understanding why the server behaves the way it does. Include headers in the normal body output with CURLOPT_HEADER set 1. </p>
<p> Of course, there are bugs left. We need to know about them to be able to fix them, so we&#8217;re quite dependent on your bug reports! When you do report suspected bugs in libcurl, please include as many details as you possibly can: a protocol dump that CURLOPT_VERBOSE produces, library version, as much as possible of your code that uses libcurl, operating system name and version, compiler name and version etc. </p>
<p> If CURLOPT_VERBOSE is not enough, you increase the level of debug data your application receive by using the CURLOPT_DEBUGFUNCTION. </p>
<p> Getting some in-depth knowledge about the protocols involved is never wrong, and if you&#8217;re trying to do funny things, you might very well understand libcurl and how to use it better if you study the appropriate RFC documents at least briefly. </p>
<h2>Upload Data to a Remote Site</h2>
<p> libcurl tries to keep a protocol independent approach to most transfers, thus uploading to a remote FTP site is very similar to uploading data to a HTTP server with a PUT request. </p>
<p> Of course, first you either create an easy handle or you re-use one existing one. Then you set the URL to operate on just like before. This is the remote URL, that we now will upload. </p>
<p> Since we write an application, we most likely want libcurl to get the upload data by asking us for it. To make it do that, we set the read callback and the custom pointer libcurl will pass to our read callback. The read callback should have a prototype similar to: </p>
<p>&nbsp;<wbr>size_t function(char&nbsp;<wbr>*bufptr, size_t size, size_t nitems, void&nbsp;<wbr>*userp); </p>
<p> Where bufptr is the pointer to a buffer we fill in with data to upload and size*nitems is the size of the buffer and therefore also the maximum amount of data we can return to libcurl in this call. The &#8216;userp&#8217; pointer is the custom pointer we set to point to a struct of ours to pass private data between the application and the callback. </p>
<p>&nbsp;<wbr>curl_easy_setopt(easyhandle, CURLOPT_READFUNCTION, read_function); </p>
<p>&nbsp;<wbr>curl_easy_setopt(easyhandle, CURLOPT_READDATA,&nbsp;<wbr>&amp;filedata); </p>
<p> Tell libcurl that we want to upload: </p>
<p>&nbsp;<wbr>curl_easy_setopt(easyhandle, CURLOPT_UPLOAD, 1L); </p>
<p> A few protocols won&#8217;t behave properly when uploads are done without any prior knowledge of the expected file size. So, set the upload file size using the CURLOPT_INFILESIZE_LARGE for all known file sizes like this[1]: </p>
<pre>
 /* in this example, file_size must be an curl_off_t variable */
 curl_easy_setopt(easyhandle, CURLOPT_INFILESIZE_LARGE, file_size);
</pre>
<p> When you call <i><a href="/docs/linux/man/3-curl_easy_perform/">curl_easy_perform</a>(3)</i> this time, it&#8217;ll perform all the necessary operations and when it has invoked the upload it&#8217;ll call your supplied callback to get the data to upload. The program should return as much data as possible in every invoke, as that is likely to make the upload perform as fast as possible. The callback should return the number of bytes it wrote in the buffer. Returning 0 will signal the end of the upload. </p>
<h2>Passwords</h2>
<p> Many protocols use or even require that user name and password are provided to be able to download or upload the data of your choice. libcurl offers several ways to specify them. </p>
<p> Most protocols support that you specify the name and password in the URL itself. libcurl will detect this and use them accordingly. This is written like this: </p>
<p>&nbsp;<wbr>protocol://user:password [at] example.com/path/ </p>
<p> If you need any odd letters in your user name or password, you should enter them URL encoded, as %XX where XX is a two-digit hexadecimal number. </p>
<p> libcurl also provides options to set various passwords. The user name and password as shown embedded in the URL can instead get set with the CURLOPT_USERPWD option. The argument passed to libcurl should be a char * to a string in the format &quot;user:password&quot;. In a manner like this: </p>
<p>&nbsp;<wbr>curl_easy_setopt(easyhandle, CURLOPT_USERPWD,&nbsp;<wbr>&quot;myname:thesecret&quot;); </p>
<p> Another case where name and password might be needed at times, is for those users who need to authenticate themselves to a proxy they use. libcurl offers another option for this, the CURLOPT_PROXYUSERPWD. It is used quite similar to the CURLOPT_USERPWD option like this: </p>
<p>&nbsp;<wbr>curl_easy_setopt(easyhandle, CURLOPT_PROXYUSERPWD,&nbsp;<wbr>&quot;myname:thesecret&quot;); </p>
<p> There&#8217;s a long time UNIX &quot;standard&quot; way of storing ftp user names and passwords, namely in the $HOME/.netrc file. The file should be made private so that only the user may read it (see also the &quot;Security Considerations&quot; chapter), as it might contain the password in plain text. libcurl has the ability to use this file to figure out what set of user name and password to use for a particular host. As an extension to the normal functionality, libcurl also supports this file for non-FTP protocols such as HTTP. To make curl use this file, use the CURLOPT_NETRC option: </p>
<p>&nbsp;<wbr>curl_easy_setopt(easyhandle, CURLOPT_NETRC, 1L); </p>
<p> And a very basic example of how such a .netrc file may look like: </p>
<pre>
 machine myhost.mydomain.com
 login userlogin
 password secretword
</pre>
<p> All these examples have been cases where the password has been optional, or at least you could leave it out and have libcurl attempt to do its job without it. There are times when the password isn&#8217;t optional, like when you&#8217;re using an SSL private key for secure transfers. </p>
<p> To pass the known private key password to libcurl: </p>
<p>&nbsp;<wbr>curl_easy_setopt(easyhandle, CURLOPT_KEYPASSWD,&nbsp;<wbr>&quot;keypassword&quot;); </p>
<h2>HTTP Authentication</h2>
<p> The previous chapter showed how to set user name and password for getting URLs that require authentication. When using the HTTP protocol, there are many different ways a client can provide those credentials to the server and you can control which way libcurl will (attempt to) use them. The default HTTP authentication method is called &#8216;Basic&#8217;, which is sending the name and password in clear-text in the HTTP request, base64-encoded. This is insecure. </p>
<p> At the time of this writing, libcurl can be built to use: Basic, Digest, NTLM, Negotiate, GSS-Negotiate and SPNEGO. You can tell libcurl which one to use with CURLOPT_HTTPAUTH as in: </p>
<p>&nbsp;<wbr>curl_easy_setopt(easyhandle, CURLOPT_HTTPAUTH, CURLAUTH_DIGEST); </p>
<p> And when you send authentication to a proxy, you can also set authentication type the same way but instead with CURLOPT_PROXYAUTH: </p>
<p>&nbsp;<wbr>curl_easy_setopt(easyhandle, CURLOPT_PROXYAUTH, CURLAUTH_NTLM); </p>
<p> Both these options allow you to set multiple types (by ORing them together), to make libcurl pick the most secure one out of the types the server/proxy claims to support. This method does however add a round-trip since libcurl must first ask the server what it supports: </p>
<p>&nbsp;<wbr>curl_easy_setopt(easyhandle, CURLOPT_HTTPAUTH,<br />
&nbsp;<wbr>CURLAUTH_DIGEST|CURLAUTH_BASIC); </p>
<p> For convenience, you can use the &#8216;CURLAUTH_ANY&#8217; define (instead of a list with specific types) which allows libcurl to use whatever method it wants. </p>
<p> When asking for multiple types, libcurl will pick the available one it considers &quot;best&quot; in its own internal order of preference. </p>
<h2>HTTP POSTing</h2>
<p> We get many questions regarding how to issue HTTP POSTs with libcurl the proper way. This chapter will thus include examples using both different versions of HTTP POST that libcurl supports. </p>
<p> The first version is the simple POST, the most common version, that most HTML pages using the &lt;form&gt; tag uses. We provide a pointer to the data and tell libcurl to post it all to the remote site: </p>
<pre><code>
char *data = "name=daniel&amp;project=curl";
curl_easy_setopt(easyhandle, CURLOPT_POSTFIELDS, data);
curl_easy_setopt(easyhandle, CURLOPT_URL, "http://posthere.com/");
curl_easy_perform(easyhandle); /* post away! */
</code></pre>
<p> Simple enough, huh? Since you set the POST options with the CURLOPT_POSTFIELDS, this automatically switches the handle to use POST in the upcoming request. </p>
<p> Ok, so what if you want to post binary data that also requires you to set the Content-Type: header of the post? Well, binary posts prevent libcurl from being able to do strlen() on the data to figure out the size, so therefore we must tell libcurl the size of the post data. Setting headers in libcurl requests are done in a generic way, by building a list of our own headers and then passing that list to libcurl. </p>
<p>struct curl_slist *headers = NULL;<br />
headers = curl_slist_append(headers, &#8220;Content-Type: text/xml&#8221;);<br />
/* post binary data */<br />
curl_easy_setopt(easyhandle, CURLOPT_POSTFIELDS, binaryptr);<br />
/* set the size of the postfields data */<br />
curl_easy_setopt(easyhandle, CURLOPT_POSTFIELDSIZE, 23L);<br />
/* pass our list of custom made headers */<br />
curl_easy_setopt(easyhandle, CURLOPT_HTTPHEADER, headers);<br />
curl_easy_perform(easyhandle); /* post away! */<br />
curl_slist_free_all(headers);  /* free the header list */</p>
<p> While the simple examples above cover the majority of all cases where HTTP POST operations are required, they don&#8217;t do multi-part formposts. Multi-part formposts were introduced as a better way to post (possibly large) binary data and were first documented in the RFC1867 (updated in RFC2388). They&#8217;re called multi-part because they&#8217;re built by a chain of parts, each part being a single unit of data. Each part has its own name and contents. You can in fact create and post a multi-part formpost with the regular libcurl POST support described above, but that would require that you build a formpost yourself and provide to libcurl. To make that easier, libcurl provides <i><a href="/docs/linux/man/3-curl_formadd/">curl_formadd</a>(3)</i>. Using this function, you add parts to the form. When you&#8217;re done adding parts, you post the whole form. </p>
<p> The following example sets two simple text parts with plain textual contents, and then a file with binary contents and uploads the whole thing. </p>
<p>struct curl_httppost *post = NULL;<br />
struct curl_httppost *last = NULL;<br />
curl_formadd(&amp;post, &amp;last,<br />
             CURLFORM_COPYNAME, &#8220;name&#8221;,<br />
             CURLFORM_COPYCONTENTS, &#8220;daniel&#8221;, CURLFORM_END);<br />
curl_formadd(&amp;post, &amp;last,<br />
             CURLFORM_COPYNAME, &#8220;project&#8221;,<br />
             CURLFORM_COPYCONTENTS, &#8220;curl&#8221;, CURLFORM_END);<br />
curl_formadd(&amp;post, &amp;last,<br />
             CURLFORM_COPYNAME, &#8220;logotype-image&#8221;,<br />
             CURLFORM_FILECONTENT, &#8220;curl.png&#8221;, CURLFORM_END);<br />
/* Set the form info */<br />
curl_easy_setopt(easyhandle, CURLOPT_HTTPPOST, post);<br />
curl_easy_perform(easyhandle); /* post away! */<br />
/* free the post data again */<br />
curl_formfree(post);</p>
<p> Multipart formposts are chains of parts using MIME-style separators and headers. It means that each one of these separate parts get a few headers set that describe the individual content-type, size etc. To enable your application to handicraft this formpost even more, libcurl allows you to supply your own set of custom headers to such an individual form part. You can of course supply headers to as many parts as you like, but this little example will show how you set headers to one specific part when you add that to the post handle: </p>
<p>struct curl_slist *headers = NULL;<br />
headers = curl_slist_append(headers, &#8220;Content-Type: text/xml&#8221;);<br />
curl_formadd(&amp;post, &amp;last,<br />
             CURLFORM_COPYNAME, &#8220;logotype-image&#8221;,<br />
             CURLFORM_FILECONTENT, &#8220;curl.xml&#8221;,<br />
             CURLFORM_CONTENTHEADER, headers,<br />
             CURLFORM_END);<br />
curl_easy_perform(easyhandle); /* post away! */<br />
curl_formfree(post);           /* free post */<br />
curl_slist_free_all(headers);  /* free custom header list */</p>
<p> Since all options on an easyhandle are &quot;sticky&quot;, they remain the same until changed even if you do call <i><a href="/docs/linux/man/3-curl_easy_perform/">curl_easy_perform</a>(3)</i>, you may need to tell curl to go back to a plain GET request if you intend to do one as your next request. You force an easyhandle to go back to GET by using the CURLOPT_HTTPGET option: </p>
<p>&nbsp;<wbr>curl_easy_setopt(easyhandle, CURLOPT_HTTPGET, 1L); </p>
<p> Just setting CURLOPT_POSTFIELDS to &quot;&quot; or NULL will *not* stop libcurl from doing a POST. It will just make it POST without any data to send! </p>
<h2>Showing Progress</h2>
<p> For historical and traditional reasons, libcurl has a built-in progress meter that can be switched on and then makes it present a progress meter in your terminal. </p>
<p> Switch on the progress meter by, oddly enough, setting CURLOPT_NOPROGRESS to zero. This option is set to 1 by default. </p>
<p> For most applications however, the built-in progress meter is useless and what instead is interesting is the ability to specify a progress callback. The function pointer you pass to libcurl will then be called on irregular intervals with information about the current transfer. </p>
<p> Set the progress callback by using CURLOPT_PROGRESSFUNCTION. And pass a pointer to a function that matches this prototype: </p>
<p>int progress_callback(void *clientp,<br />
                      double dltotal,<br />
                      double dlnow,<br />
                      double ultotal,<br />
                      double ulnow);</p>
<p> If any of the input arguments is unknown, a 0 will be passed. The first argument, the &#8216;clientp&#8217; is the pointer you pass to libcurl with CURLOPT_PROGRESSDATA. libcurl won&#8217;t touch it. </p>
<h2>libcurl with C++</h2>
<p> There&#8217;s basically only one thing to keep in mind when using C++ instead of C when interfacing libcurl: </p>
<p> The callbacks CANNOT be non-static class member functions </p>
<p> Example C++ code: </p>
<p>class AClass<br />
{<br />
    static size_t write_data(void *ptr, size_t size, size_t nmemb,<br />
                             void *ourpointer)<br />
    {<br />
        /* do what you want with the data */<br />
    }<br />
}</p>
<h2>Proxies</h2>
<p> What &quot;proxy&quot; means according to Merriam-Webster: &quot;a person authorized to act for another&quot; but also &quot;the agency, function, or office of a deputy who acts as a substitute for another&quot;. </p>
<p> Proxies are exceedingly common these days. Companies often only offer Internet access to employees through their proxies. Network clients or user-agents ask the proxy for documents, the proxy does the actual request and then it returns them. </p>
<p> libcurl supports SOCKS and HTTP proxies. When a given URL is wanted, libcurl will ask the proxy for it instead of trying to connect to the actual host identified in the URL. </p>
<p> If you&#8217;re using a SOCKS proxy, you may find that libcurl doesn&#8217;t quite support all operations through it. </p>
<p> For HTTP proxies: the fact that the proxy is a HTTP proxy puts certain restrictions on what can actually happen. A requested URL that might not be a HTTP URL will be still be passed to the HTTP proxy to deliver back to libcurl. This happens transparently, and an application may not need to know. I say &quot;may&quot;, because at times it is very important to understand that all operations over a HTTP proxy use the HTTP protocol. For example, you can&#8217;t invoke your own custom FTP commands or even proper FTP directory listings. </p>
<dl>
<dt>Proxy Options</p>
<dd>
<p> To tell libcurl to use a proxy at a given port number: </p>
<p>&nbsp;<wbr>curl_easy_setopt(easyhandle, CURLOPT_PROXY,&nbsp;<wbr>&quot;proxy-host.com:8080&quot;); </p>
<p> Some proxies require user authentication before allowing a request, and you pass that information similar to this: </p>
<p>&nbsp;<wbr>curl_easy_setopt(easyhandle, CURLOPT_PROXYUSERPWD,&nbsp;<wbr>&quot;user:password&quot;); </p>
<p> If you want to, you can specify the host name only in the CURLOPT_PROXY option, and set the port number separately with CURLOPT_PROXYPORT. </p>
<p> Tell libcurl what kind of proxy it is with CURLOPT_PROXYTYPE (if not, it will default to assume a HTTP proxy): </p>
<p>&nbsp;<wbr>curl_easy_setopt(easyhandle, CURLOPT_PROXYTYPE, CURLPROXY_SOCKS4); </p>
<dt>Environment Variables</p>
<dd>
<p> libcurl automatically checks and uses a set of environment variables to know what proxies to use for certain protocols. The names of the variables are following an ancient de facto standard and are built up as &quot;[protocol]_proxy&quot; (note the lower casing). Which makes the variable &#8216;http_proxy&#8217; checked for a name of a proxy to use when the input URL is HTTP. Following the same rule, the variable named &#8216;ftp_proxy&#8217; is checked for FTP URLs. Again, the proxies are always HTTP proxies, the different names of the variables simply allows different HTTP proxies to be used. </p>
<p> The proxy environment variable contents should be in the format &quot;[protocol://][user:password@]machine[:port]&quot;. Where the protocol:// part is simply ignored if present (so <a rel="nofollow" href="http://proxy">http://proxy</a> and <a href="bluerk://proxy">bluerk://proxy</a> will do the same) and the optional port number specifies on which port the proxy operates on the host. If not specified, the internal default port number will be used and that is most likely *not* the one you would like it to be. </p>
<p> There are two special environment variables. &#8216;all_proxy&#8217; is what sets proxy for any URL in case the protocol specific variable wasn&#8217;t set, and &#8216;no_proxy&#8217; defines a list of hosts that should not use a proxy even though a variable may say so. If &#8216;no_proxy&#8217; is a plain asterisk (&quot;*&quot;) it matches all hosts. </p>
<p> To explicitly disable libcurl&#8217;s checking for and using the proxy environment variables, set the proxy name to &quot;&quot; &#8211; an empty string &#8211; with CURLOPT_PROXY.</p>
<dt>SSL and Proxies</p>
<dd>
<p> SSL is for secure point-to-point connections. This involves strong encryption and similar things, which effectively makes it impossible for a proxy to operate as a &quot;man in between&quot; which the proxy&#8217;s task is, as previously discussed. Instead, the only way to have SSL work over a HTTP proxy is to ask the proxy to tunnel trough everything without being able to check or fiddle with the traffic. </p>
<p> Opening an SSL connection over a HTTP proxy is therefor a matter of asking the proxy for a straight connection to the target host on a specified port. This is made with the HTTP request CONNECT. (&quot;please mr proxy, connect me to that remote host&quot;). </p>
<p> Because of the nature of this operation, where the proxy has no idea what kind of data that is passed in and out through this tunnel, this breaks some of the very few advantages that come from using a proxy, such as caching. Many organizations prevent this kind of tunneling to other destination port numbers than 443 (which is the default HTTPS port number). </p>
<dt>Tunneling Through Proxy</p>
<dd> As explained above, tunneling is required for SSL to work and often even restricted to the operation intended for SSL; HTTPS. </p>
<p> This is however not the only time proxy-tunneling might offer benefits to you or your application. </p>
<p> As tunneling opens a direct connection from your application to the remote machine, it suddenly also re-introduces the ability to do non-HTTP operations over a HTTP proxy. You can in fact use things such as FTP upload or FTP custom commands this way. </p>
<p> Again, this is often prevented by the administrators of proxies and is rarely allowed. </p>
<p> Tell libcurl to use proxy tunneling like this: </p>
<p>&nbsp;<wbr>curl_easy_setopt(easyhandle, CURLOPT_HTTPPROXYTUNNEL, 1L); </p>
<p> In fact, there might even be times when you want to do plain HTTP operations using a tunnel like this, as it then enables you to operate on the remote server instead of asking the proxy to do so. libcurl will not stand in the way for such innovative actions either! </p>
<dt>Proxy Auto-Config</p>
<dd>
<p> Netscape first came up with this. It is basically a web page (usually using a .pac extension) with a Javascript that when executed by the browser with the requested URL as input, returns information to the browser on how to connect to the URL. The returned information might be &quot;DIRECT&quot; (which means no proxy should be used), &quot;PROXY host:port&quot; (to tell the browser where the proxy for this particular URL is) or &quot;SOCKS host:port&quot; (to direct the browser to a SOCKS proxy). </p>
<p> libcurl has no means to interpret or evaluate Javascript and thus it doesn&#8217;t support this. If you get yourself in a position where you face this nasty invention, the following advice have been mentioned and used in the past: </p>
<p> &#8211; Depending on the Javascript complexity, write up a script that translates it to another language and execute that. </p>
<p> &#8211; Read the Javascript code and rewrite the same logic in another language. </p>
<p> &#8211; Implement a Javascript interpreter; people have successfully used the Mozilla Javascript engine in the past. </p>
<p> &#8211; Ask your admins to stop this, for a static proxy setup or similar. </p>
</dl>
<h2>Persistence Is The Way to Happiness</h2>
<p> Re-cycling the same easy handle several times when doing multiple requests is the way to go. </p>
<p> After each single <i><a href="/docs/linux/man/3-curl_easy_perform/">curl_easy_perform</a>(3)</i> operation, libcurl will keep the connection alive and open. A subsequent request using the same easy handle to the same host might just be able to use the already open connection! This reduces network impact a lot. </p>
<p> Even if the connection is dropped, all connections involving SSL to the same host again, will benefit from libcurl&#8217;s session ID cache that drastically reduces re-connection time. </p>
<p> FTP connections that are kept alive save a lot of time, as the command- response round-trips are skipped, and also you don&#8217;t risk getting blocked without permission to login again like on many FTP servers only allowing N persons to be logged in at the same time. </p>
<p> libcurl caches DNS name resolving results, to make lookups of a previously looked up name a lot faster. </p>
<p> Other interesting details that improve performance for subsequent requests may also be added in the future. </p>
<p> Each easy handle will attempt to keep the last few connections alive for a while in case they are to be used again. You can set the size of this &quot;cache&quot; with the CURLOPT_MAXCONNECTS option. Default is 5. There is very seldom any point in changing this value, and if you think of changing this it is often just a matter of thinking again. </p>
<p> To force your upcoming request to not use an already existing connection (it will even close one first if there happens to be one alive to the same host you&#8217;re about to operate on), you can do that by setting CURLOPT_FRESH_CONNECT to 1. In a similar spirit, you can also forbid the upcoming request to be &quot;lying&quot; around and possibly get re-used after the request by setting CURLOPT_FORBID_REUSE to 1. </p>
<h2>HTTP Headers Used by libcurl</h2>
<p> When you use libcurl to do HTTP requests, it&#8217;ll pass along a series of headers automatically. It might be good for you to know and understand these. You can replace or remove them by using the CURLOPT_HTTPHEADER option. </p>
<dl>
<dt>Host</p>
<dd> This header is required by HTTP 1.1 and even many 1.0 servers and should be the name of the server we want to talk to. This includes the port number if anything but default. </p>
<dt>Accept</p>
<dd> &quot;*/*&quot;. </p>
<dt>Expect</p>
<dd> When doing POST requests, libcurl sets this header to &quot;100-continue&quot; to ask the server for an &quot;OK&quot; message before it proceeds with sending the data part of the post. If the POSTed data amount is deemed &quot;small&quot;, libcurl will not use this header. </p>
</dl>
<h2>Customizing Operations</h2>
<p> There is an ongoing development today where more and more protocols are built upon HTTP for transport. This has obvious benefits as HTTP is a tested and reliable protocol that is widely deployed and has excellent proxy-support. </p>
<p> When you use one of these protocols, and even when doing other kinds of programming you may need to change the traditional HTTP (or FTP or&#8230;) manners. You may need to change words, headers or various data. </p>
<p> libcurl is your friend here too. </p>
<dl>
<dt>CUSTOMREQUEST</p>
<dd> If just changing the actual HTTP request keyword is what you want, like when GET, HEAD or POST is not good enough for you, CURLOPT_CUSTOMREQUEST is there for you. It is very simple to use: </p>
<p>&nbsp;<wbr>curl_easy_setopt(easyhandle, CURLOPT_CUSTOMREQUEST,&nbsp;<wbr>&quot;MYOWNREQUEST&quot;); </p>
<p> When using the custom request, you change the request keyword of the actual request you are performing. Thus, by default you make a GET request but you can also make a POST operation (as described before) and then replace the POST keyword if you want to. You&#8217;re the boss. </p>
<dt>Modify Headers</p>
<dd> HTTP-like protocols pass a series of headers to the server when doing the request, and you&#8217;re free to pass any amount of extra headers that you think fit. Adding headers is this easy: </p>
<p>struct curl_slist *headers = NULL; /* init to NULL is important */<br />
headers = curl_slist_append(headers, &#8220;Hey-server-hey: how are you?&#8221;);<br />
headers = curl_slist_append(headers, &#8220;X-silly-content: yes&#8221;);<br />
/* pass our list of custom made headers */<br />
curl_easy_setopt(easyhandle, CURLOPT_HTTPHEADER, headers);<br />
curl_easy_perform(easyhandle); /* transfer http */<br />
curl_slist_free_all(headers);  /* free the header list */</p>
<p> &#8230; and if you think some of the internally generated headers, such as Accept: or Host: don&#8217;t contain the data you want them to contain, you can replace them by simply setting them too: </p>
<p>headers = curl_slist_append(headers, &#8220;Accept: Agent-007&#8221;);<br />
headers = curl_slist_append(headers, &#8220;Host: munged.host.line&#8221;);</p>
<dt>Delete Headers</p>
<dd> If you replace an existing header with one with no contents, you will prevent the header from being sent. For instance, if you want to completely prevent the &quot;Accept:&quot; header from being sent, you can disable it with code similar to this: </p>
<p>&nbsp;<wbr>headers&nbsp;<wbr>=&nbsp;<wbr>curl_slist_append(headers,&nbsp;<wbr>&quot;Accept:&quot;); </p>
<p> Both replacing and canceling internal headers should be done with careful consideration and you should be aware that you may violate the HTTP protocol when doing so. </p>
<dt>Enforcing chunked transfer-encoding</p>
<dd>
<p> By making sure a request uses the custom header &quot;Transfer-Encoding: chunked&quot; when doing a non-GET HTTP operation, libcurl will switch over to &quot;chunked&quot; upload, even though the size of the data to upload might be known. By default, libcurl usually switches over to chunked upload automatically if the upload data size is unknown. </p>
<dt>HTTP Version</p>
<dd>
<p> All HTTP requests includes the version number to tell the server which version we support. libcurl speaks HTTP 1.1 by default. Some very old servers don&#8217;t like getting 1.1-requests and when dealing with stubborn old things like that, you can tell libcurl to use 1.0 instead by doing something like this: </p>
<p>&nbsp;<wbr>curl_easy_setopt(easyhandle, CURLOPT_HTTP_VERSION, CURL_HTTP_VERSION_1_0); </p>
<dt>FTP Custom Commands</p>
<dd>
<p> Not all protocols are HTTP-like, and thus the above may not help you when you want to make, for example, your FTP transfers to behave differently. </p>
<p> Sending custom commands to a FTP server means that you need to send the commands exactly as the FTP server expects them (RFC959 is a good guide here), and you can only use commands that work on the control-connection alone. All kinds of commands that require data interchange and thus need a data-connection must be left to libcurl&#8217;s own judgement. Also be aware that libcurl will do its very best to change directory to the target directory before doing any transfer, so if you change directory (with CWD or similar) you might confuse libcurl and then it might not attempt to transfer the file in the correct remote directory. </p>
<p> A little example that deletes a given file before an operation: </p>
<pre><code>
headers = curl_slist_append(headers, "DELE file-to-remove");
/* pass the list of custom commands to the handle */
curl_easy_setopt(easyhandle, CURLOPT_QUOTE, headers);
curl_easy_perform(easyhandle); /* transfer ftp data! */
curl_slist_free_all(headers);  /* free the header list */
</code></pre>
<p> If you would instead want this operation (or chain of operations) to happen _after_ the data transfer took place the option to <i><a href="/docs/linux/man/3-curl_easy_setopt/">curl_easy_setopt</a>(3)</i> would instead be called CURLOPT_POSTQUOTE and used the exact same way. </p>
<p> The custom FTP command will be issued to the server in the same order they are added to the list, and if a command gets an error code returned back from the server, no more commands will be issued and libcurl will bail out with an error code (CURLE_QUOTE_ERROR). Note that if you use CURLOPT_QUOTE to send commands before a transfer, no transfer will actually take place when a quote command has failed. </p>
<p> If you set the CURLOPT_HEADER to 1, you will tell libcurl to get information about the target file and output &quot;headers&quot; about it. The headers will be in &quot;HTTP-style&quot;, looking like they do in HTTP. </p>
<p> The option to enable headers or to run custom FTP commands may be useful to combine with CURLOPT_NOBODY. If this option is set, no actual file content transfer will be performed. </p>
<dt>FTP Custom CUSTOMREQUEST</p>
<dd> If you do want to list the contents of a FTP directory using your own defined FTP command, CURLOPT_CUSTOMREQUEST will do just that. &quot;NLST&quot; is the default one for listing directories but you&#8217;re free to pass in your idea of a good alternative. </p>
</dl>
<h2>Cookies Without Chocolate Chips</h2>
<p> In the HTTP sense, a cookie is a name with an associated value. A server sends the name and value to the client, and expects it to get sent back on every subsequent request to the server that matches the particular conditions set. The conditions include that the domain name and path match and that the cookie hasn&#8217;t become too old. </p>
<p> In real-world cases, servers send new cookies to replace existing ones to update them. Server use cookies to &quot;track&quot; users and to keep &quot;sessions&quot;. </p>
<p> Cookies are sent from server to clients with the header Set-Cookie: and they&#8217;re sent from clients to servers with the Cookie: header. </p>
<p> To just send whatever cookie you want to a server, you can use CURLOPT_COOKIE to set a cookie string like this: </p>
<p>&nbsp;<wbr>curl_easy_setopt(easyhandle, CURLOPT_COOKIE,&nbsp;<wbr>&quot;name1=var1;&nbsp;<wbr>name2=var2;&quot;); </p>
<p> In many cases, that is not enough. You might want to dynamically save whatever cookies the remote server passes to you, and make sure those cookies are then used accordingly on later requests. </p>
<p> One way to do this, is to save all headers you receive in a plain file and when you make a request, you tell libcurl to read the previous headers to figure out which cookies to use. Set the header file to read cookies from with CURLOPT_COOKIEFILE. </p>
<p> The CURLOPT_COOKIEFILE option also automatically enables the cookie parser in libcurl. Until the cookie parser is enabled, libcurl will not parse or understand incoming cookies and they will just be ignored. However, when the parser is enabled the cookies will be understood and the cookies will be kept in memory and used properly in subsequent requests when the same handle is used. Many times this is enough, and you may not have to save the cookies to disk at all. Note that the file you specify to CURLOPT_COOKIEFILE doesn&#8217;t have to exist to enable the parser, so a common way to just enable the parser and not read any cookies is to use the name of a file you know doesn&#8217;t exist. </p>
<p> If you would rather use existing cookies that you&#8217;ve previously received with your Netscape or Mozilla browsers, you can make libcurl use that cookie file as input. The CURLOPT_COOKIEFILE is used for that too, as libcurl will automatically find out what kind of file it is and act accordingly. </p>
<p> Perhaps the most advanced cookie operation libcurl offers, is saving the entire internal cookie state back into a Netscape/Mozilla formatted cookie file. We call that the cookie-jar. When you set a file name with CURLOPT_COOKIEJAR, that file name will be created and all received cookies will be stored in it when <i><a href="/docs/linux/man/3-curl_easy_cleanup/">curl_easy_cleanup</a>(3)</i> is called. This enables cookies to get passed on properly between multiple handles without any information getting lost. </p>
<h2>FTP Peculiarities We Need</h2>
<p> FTP transfers use a second TCP/IP connection for the data transfer. This is usually a fact you can forget and ignore but at times this fact will come back to haunt you. libcurl offers several different ways to customize how the second connection is being made. </p>
<p> libcurl can either connect to the server a second time or tell the server to connect back to it. The first option is the default and it is also what works best for all the people behind firewalls, NATs or IP-masquerading setups. libcurl then tells the server to open up a new port and wait for a second connection. This is by default attempted with EPSV first, and if that doesn&#8217;t work it tries PASV instead. (EPSV is an extension to the original FTP spec and does not exist nor work on all FTP servers.) </p>
<p> You can prevent libcurl from first trying the EPSV command by setting CURLOPT_FTP_USE_EPSV to zero. </p>
<p> In some cases, you will prefer to have the server connect back to you for the second connection. This might be when the server is perhaps behind a firewall or something and only allows connections on a single port. libcurl then informs the remote server which IP address and port number to connect to. This is made with the CURLOPT_FTPPORT option. If you set it to &quot;-&quot;, libcurl will use your system&#8217;s &quot;default IP address&quot;. If you want to use a particular IP, you can set the full IP address, a host name to resolve to an IP address or even a local network interface name that libcurl will get the IP address from. </p>
<p> When doing the &quot;PORT&quot; approach, libcurl will attempt to use the EPRT and the LPRT before trying PORT, as they work with more protocols. You can disable this behavior by setting CURLOPT_FTP_USE_EPRT to zero. </p>
<h2>Headers Equal Fun</h2>
<p> Some protocols provide &quot;headers&quot;, meta-data separated from the normal data. These headers are by default not included in the normal data stream, but you can make them appear in the data stream by setting CURLOPT_HEADER to 1. </p>
<p> What might be even more useful, is libcurl&#8217;s ability to separate the headers from the data and thus make the callbacks differ. You can for example set a different pointer to pass to the ordinary write callback by setting CURLOPT_WRITEHEADER. </p>
<p> Or, you can set an entirely separate function to receive the headers, by using CURLOPT_HEADERFUNCTION. </p>
<p> The headers are passed to the callback function one by one, and you can depend on that fact. It makes it easier for you to add custom header parsers etc. </p>
<p> &quot;Headers&quot; for FTP transfers equal all the FTP server responses. They aren&#8217;t actually true headers, but in this case we pretend they are! ;-) </p>
<h2>Post Transfer Information</h2>
<p>&nbsp;<wbr>[&nbsp;<wbr>curl_easy_getinfo&nbsp;<wbr>] </p>
<h2>Security Considerations</h2>
<p> The libcurl project takes security seriously. The library is written with caution and precautions are taken to mitigate many kinds of risks encountered while operating with potentially malicious servers on the Internet. It is a powerful library, however, which allows application writers to make trade offs between ease of writing and exposure to potential risky operations. If used the right way, you can use libcurl to transfer data pretty safely. </p>
<p> Many applications are used in closed networks where users and servers can be trusted, but many others are used on arbitrary servers and are fed input from potentially untrusted users. Following is a discussion about some risks in the ways in which applications commonly use libcurl and potential mitigations of those risks. It is by no means comprehensive, but shows classes of attacks that robust applications should consider. The Common Weakness Enumeration project at <a rel="nofollow" href="http://cwe.mitre.org/">http://cwe.mitre.org/</a> is a good reference for many of these and similar types of weaknesses of which application writers should be aware. </p>
<dl>
<dt>Command Lines</p>
<dd> If you use a command line tool (such as curl) that uses libcurl, and you give options to the tool on the command line those options can very likely get read by other users of your system when they use &#8216;ps&#8217; or other tools to list currently running processes. </p>
<p> To avoid this problem, never feed sensitive things to programs using command line options. Write them to a protected file and use the -K option to avoid this. </p>
<dt>.netrc</p>
<dd> .netrc is a pretty handy file/feature that allows you to login quickly and automatically to frequently visited sites. The file contains passwords in clear text and is a real security risk. In some cases, your .netrc is also stored in a home directory that is NFS mounted or used on another network based file system, so the clear text password will fly through your network every time anyone reads that file! </p>
<p> To avoid this problem, don&#8217;t use .netrc files and never store passwords in plain text anywhere. </p>
<dt>Clear Text Passwords</p>
<dd> Many of the protocols libcurl supports send name and password unencrypted as clear text (HTTP Basic authentication, FTP, TELNET etc). It is very easy for anyone on your network or a network nearby yours to just fire up a network analyzer tool and eavesdrop on your passwords. Don&#8217;t let the fact that HTTP Basic uses base64 encoded passwords fool you. They may not look readable at a first glance, but they very easily &quot;deciphered&quot; by anyone within seconds. </p>
<p> To avoid this problem, use HTTP authentication methods or other protocols that don&#8217;t let snoopers see your password: HTTP with Digest, NTLM or GSS authentication, HTTPS, FTPS, SCP, SFTP and FTP-Kerberos are a few examples. </p>
<dt>Redirects</p>
<dd> The CURLOPT_FOLLOWLOCATION option automatically follows HTTP redirects sent by a remote server. These redirects can refer to any kind of URL, not just HTTP. A redirect to a file: URL would cause the libcurl to read (or write) arbitrary files from the local filesystem. If the application returns the data back to the user (as would happen in some kinds of CGI scripts), an attacker could leverage this to read otherwise forbidden data (e.g. file://localhost/etc/passwd). </p>
<p> If authentication credentials are stored in the ~/.netrc file, or Kerberos is in use, any other URL type (not just file:) that requires authentication is also at risk. A redirect such as <a href="ftp://some-internal-server/private-file">ftp://some-internal-server/private-file</a> would then return data even when the server is password protected. </p>
<p> In the same way, if an unencrypted SSH private key has been configured for the user running the libcurl application, SCP: or SFTP: URLs could access password or private-key protected resources, e.g. <a href="sftp://user@some-internal-server/etc/passwd">sftp://user@some-internal-server/etc/passwd</a> </p>
<p> The CURLOPT_REDIR_PROTOCOLS and CURLOPT_NETRC options can be used to mitigate against this kind of attack. </p>
<p> A redirect can also specify a location available only on the machine running libcurl, including servers hidden behind a firewall from the attacker. e.g. <a rel="nofollow" href="http://127.0.0.1/">http://127.0.0.1/</a> or <a href="http://intranet/delete-stuff.cgi?delete=all">http://intranet/delete-stuff.cgi?delete=all</a> or <a href="tftp://bootp-server/pc-config-data">tftp://bootp-server/pc-config-data</a> </p>
<p> Apps can mitigate against this by disabling CURLOPT_FOLLOWLOCATION and handling redirects itself, sanitizing URLs as necessary. Alternately, an app could leave CURLOPT_FOLLOWLOCATION enabled but set CURLOPT_REDIR_PROTOCOLS and install a CURLOPT_OPENSOCKETFUNCTION callback function in which addresses are sanitized before use. </p>
<dt>Private Resources</p>
<dd> A user who can control the DNS server of a domain being passed in within a URL can change the address of the host to a local, private address which the libcurl application will then use. e.g. The innocuous URL <a rel="nofollow" href="http://fuzzybunnies.example.com/">http://fuzzybunnies.example.com/</a> could actually resolve to the IP address of a server behind a firewall, such as 127.0.0.1 or 10.1.2.3 Apps can mitigate against this by setting a CURLOPT_OPENSOCKETFUNCTION and checking the address before a connection. </p>
<p> All the malicious scenarios regarding redirected URLs apply just as well to non-redirected URLs, if the user is allowed to specify an arbitrary URL that could point to a private resource. For example, a web app providing a translation service might happily translate file://localhost/etc/passwd and display the result. Apps can mitigate against this with the CURLOPT_PROTOCOLS option as well as by similar mitigation techniques for redirections. </p>
<p> A malicious FTP server could in response to the PASV command return an IP address and port number for a server local to the app running libcurl but behind a firewall. Apps can mitigate against this by using the CURLOPT_FTP_SKIP_PASV_IP option or CURLOPT_FTPPORT. </p>
<dt>Uploads</p>
<dd> When uploading, a redirect can cause a local (or remote) file to be overwritten. Apps must not allow any unsanitized URL to be passed in for uploads. Also, CURLOPT_FOLLOWLOCATION should not be used on uploads. Instead, the app should handle redirects itself, sanitizing each URL first. </p>
<dt>Authentication</p>
<dd> Use of CURLOPT_UNRESTRICTED_AUTH could cause authentication information to be sent to an unknown second server. Apps can mitigate against this by disabling CURLOPT_FOLLOWLOCATION and handling redirects itself, sanitizing where necessary. </p>
<p> Use of the CURLAUTH_ANY option to CURLOPT_HTTPAUTH could result in user name and password being sent in clear text to an HTTP server. Instead, use CURLAUTH_ANYSAFE which ensures that the password is encrypted over the network, or else fail the request. </p>
<p> Use of the CURLUSESSL_TRY option to CURLOPT_USE_SSL could result in user name and password being sent in clear text to an FTP server. Instead, use CURLUSESSL_CONTROL to ensure that an encrypted connection is used or else fail the request. </p>
<dt>Cookies</p>
<dd> If cookies are enabled and cached, then a user could craft a URL which performs some malicious action to a site whose authentication is already stored in a cookie. e.g. <a rel="nofollow" href="http://mail.example.com/delete-stuff.cgi?delete=all">http://mail.example.com/delete-stuff.cgi?delete=all</a> Apps can mitigate against this by disabling cookies or clearing them between requests. </p>
<dt>Dangerous URLs</p>
<dd> SCP URLs can contain raw commands within the scp: URL, which is a side effect of how the SCP protocol is designed. e.g. <a href="scp://user:pass@host/a;date">scp://user:pass@host/a;date</a> &gt;/tmp/test; Apps must not allow unsanitized SCP: URLs to be passed in for downloads. </p>
<dt>Denial of Service</p>
<dd> A malicious server could cause libcurl to effectively hang by sending a trickle of data through, or even no data at all but just keeping the TCP connection open. This could result in a denial-of-service attack. The CURLOPT_TIMEOUT and/or CURLOPT_LOW_SPEED_LIMIT options can be used to mitigate against this. </p>
<p> A malicious server could cause libcurl to effectively hang by starting to send data, then severing the connection without cleanly closing the TCP connection. The app could install a CURLOPT_SOCKOPTFUNCTION callback function and set the TCP SO_KEEPALIVE option to mitigate against this. Setting one of the timeout options would also work against this attack. </p>
<p> A malicious server could cause libcurl to download an infinite amount of data, potentially causing all of memory or disk to be filled. Setting the CURLOPT_MAXFILESIZE_LARGE option is not sufficient to guard against this. Instead, the app should monitor the amount of data received within the write or progress callback and abort once the limit is reached. </p>
<p> A malicious HTTP server could cause an infinite redirection loop, causing a denial-of-service. This can be mitigated by using the CURLOPT_MAXREDIRS option. </p>
<dt>Arbitrary Headers</p>
<dd> User-supplied data must be sanitized when used in options like CURLOPT_USERAGENT, CURLOPT_HTTPHEADER, CURLOPT_POSTFIELDS and others that are used to generate structured data. Characters like embedded carriage returns or ampersands could allow the user to create additional headers or fields that could cause malicious transactions. </p>
<dt>Server-supplied Names</p>
<dd> A server can supply data which the application may, in some cases, use as a file name. The curl command-line tool does this with &#8211;remote-header-name, using the Content-disposition: header to generate a file name. An application could also use CURLINFO_EFFECTIVE_URL to generate a file name from a server-supplied redirect URL. Special care must be taken to sanitize such names to avoid the possibility of a malicious server supplying one like &quot;/etc/passwd&quot;, &quot;utoexec.bat&quot; or even &quot;.bashrc&quot;. </p>
<dt>Server Certificates</p>
<dd> A secure application should never use the CURLOPT_SSL_VERIFYPEER option to disable certificate validation. There are numerous attacks that are enabled by apps that fail to properly validate server TLS/SSL certificates, thus enabling a malicious server to spoof a legitimate one. HTTPS without validated certificates is potentially as insecure as a plain HTTP connection. </p>
<dt>Showing What You Do</p>
<dd> On a related issue, be aware that even in situations like when you have problems with libcurl and ask someone for help, everything you reveal in order to get best possible help might also impose certain security related risks. Host names, user names, paths, operating system specifics, etc (not to mention passwords of course) may in fact be used by intruders to gain additional information of a potential target. </p>
<p> To avoid this problem, you must of course use your common sense. Often, you can just edit out the sensitive data or just search/replace your true information with faked data. </p>
</dl>
<h2>Multiple Transfers Using the multi Interface</h2>
<p> The easy interface as described in detail in this document is a synchronous interface that transfers one file at a time and doesn&#8217;t return until it is done. </p>
<p> The multi interface, on the other hand, allows your program to transfer multiple files in both directions at the same time, without forcing you to use multiple threads. The name might make it seem that the multi interface is for multi-threaded programs, but the truth is almost the reverse. The multi interface can allow a single-threaded application to perform the same kinds of multiple, simultaneous transfers that multi-threaded programs can perform. It allows many of the benefits of multi-threaded transfers without the complexity of managing and synchronizing many threads. </p>
<p> To use this interface, you are better off if you first understand the basics of how to use the easy interface. The multi interface is simply a way to make multiple transfers at the same time by adding up multiple easy handles into a &quot;multi stack&quot;. </p>
<p> You create the easy handles you want and you set all the options just like you have been told above, and then you create a multi handle with <i><a href="/docs/linux/man/3-curl_multi_init/">curl_multi_init</a>(3)</i> and add all those easy handles to that multi handle with <i><a href="/docs/linux/man/3-curl_multi_add_handle/">curl_multi_add_handle</a>(3)</i>. </p>
<p> When you&#8217;ve added the handles you have for the moment (you can still add new ones at any time), you start the transfers by calling <i><a href="/docs/linux/man/3-curl_multi_perform/">curl_multi_perform</a>(3)</i>. </p>
<p> <i><a href="/docs/linux/man/3-curl_multi_perform/">curl_multi_perform</a>(3)</i> is asynchronous. It will only execute as little as possible and then return back control to your program. It is designed to never block. </p>
<p> The best usage of this interface is when you do a select() on all possible file descriptors or sockets to know when to call libcurl again. This also makes it easy for you to wait and respond to actions on your own application&#8217;s sockets/handles. You figure out what to select() for by using <i><a href="/docs/linux/man/3-curl_multi_fdset/">curl_multi_fdset</a>(3)</i>, that fills in a set of fd_set variables for you with the particular file descriptors libcurl uses for the moment. </p>
<p> When you then call select(), it&#8217;ll return when one of the file handles signal action and you then call <i><a href="/docs/linux/man/3-curl_multi_perform/">curl_multi_perform</a>(3)</i> to allow libcurl to do what it wants to do. Take note that libcurl does also feature some time-out code so we advise you to never use very long timeouts on select() before you call <i><a href="/docs/linux/man/3-curl_multi_perform/">curl_multi_perform</a>(3)</i>, which thus should be called unconditionally every now and then even if none of its file descriptors have signaled ready. Another precaution you should use: always call <i><a href="/docs/linux/man/3-curl_multi_fdset/">curl_multi_fdset</a>(3)</i> immediately before the select() call since the current set of file descriptors may change when calling a curl function. </p>
<p> If you want to stop the transfer of one of the easy handles in the stack, you can use <i><a href="/docs/linux/man/3-curl_multi_remove_handle/">curl_multi_remove_handle</a>(3)</i> to remove individual easy handles. Remember that easy handles should be <i><a href="/docs/linux/man/3-curl_easy_cleanup/">curl_easy_cleanup</a>(3)</i>ed. </p>
<p> When a transfer within the multi stack has finished, the counter of running transfers (as filled in by <i><a href="/docs/linux/man/3-curl_multi_perform/">curl_multi_perform</a>(3)</i>) will decrease. When the number reaches zero, all transfers are done. </p>
<p> <i><a href="/docs/linux/man/3-curl_multi_info_read/">curl_multi_info_read</a>(3)</i> can be used to get information about completed transfers. It then returns the CURLcode for each easy transfer, to allow you to figure out success on each individual transfer. </p>
<h2>SSL, Certificates and Other Tricks</h2>
<p>&nbsp;<wbr>[&nbsp;<wbr>seeding, passwords, keys, certificates, ENGINE, ca certs&nbsp;<wbr>] </p>
<h2>Sharing Data Between Easy Handles</h2>
<p> You can share some data between easy handles when the easy interface is used, and some data is share automatically when you use the multi interface. </p>
<p> When you add easy handles to a multi handle, these easy handles will automatically share a lot of the data that otherwise would be kept on a per-easy handle basis when the easy interface is used. </p>
<p> The DNS cache is shared between handles within a multi handle, making subsequent name resolvings faster and the connection pool that is kept to better allow persistent connections and connection re-use is shared. If you&#8217;re using the easy interface, you can still share these between specific easy handles by using the share interface, see <i><a href="/docs/linux/man/3-libcurl-share/">libcurl-share</a>(3)</i>. </p>
<p> Some things are never shared automatically, not within multi handles, like for example cookies so the only way to share that is with the share interface.</p>
<h2>Footnotes</h2>
<dl>
<dt>[1]</p>
<dd> libcurl 7.10.3 and later have the ability to switch over to chunked Transfer-Encoding in cases where HTTP uploads are done with data of an unknown size.</p>
<dt>[2]</p>
<dd> This happens on Windows machines when libcurl is built and used as a DLL. However, you can still do this on Windows if you link with a static library.</p>
<dt>[3]</p>
<dd> The curl-config tool is generated at build-time (on UNIX-like systems) and should be installed with the &#8216;make install&#8217; or similar instruction that installs the library, header files, man pages etc.</p>
<dt>[4]</p>
<dd> This behavior was different in versions before 7.17.0, where strings had to remain valid past the end of the <i><a href="/docs/linux/man/3-curl_easy_setopt/">curl_easy_setopt</a>(3)</i> call. </p>
</dl>
<h2>Index</h2>

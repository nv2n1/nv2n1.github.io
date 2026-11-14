---
title: "libcurl-multi(3)"
name: "libcurl-multi"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libcurl-multi/"
description: "libcurl-multi – how to use the multi interface"
---

<h2>NAME</h2>
<p> libcurl-multi &#8211; how to use the multi interface</p>
<h2>DESCRIPTION</h2>
<p> This is an overview on how to use the libcurl multi interface in your C programs. There are specific man pages for each function mentioned in here. There&#8217;s also the <i><a href="/docs/linux/man/3-libcurl-tutorial/">libcurl-tutorial</a>(3)</i> man page for a complete tutorial to programming with libcurl and the <i><a href="/docs/linux/man/3-libcurl-easy/">libcurl-easy</a>(3)</i> man page for an overview of the libcurl easy interface. </p>
<p> All functions in the multi interface are prefixed with curl_multi.</p>
<h2>OBJECTIVES</h2>
<p> The multi interface offers several abilities that the easy interface doesn&#8217;t. They are mainly: </p>
<p> 1. Enable a &quot;pull&quot; interface. The application that uses libcurl decides where and when to ask libcurl to get/send data. </p>
<p> 2. Enable multiple simultaneous transfers in the same thread without making it complicated for the application. </p>
<p> 3. Enable the application to wait for action on its own file descriptors and curl&#8217;s file descriptors simultaneous easily.</p>
<h2>ONE MULTI HANDLE MANY EASY HANDLES</h2>
<p> To use the multi interface, you must first create a &#8216;multi handle&#8217; with <i><a href="/docs/linux/man/3-curl_multi_init/">curl_multi_init</a>(3)</i>. This handle is then used as input to all further curl_multi_* functions. </p>
<p> Each single transfer is built up with an easy handle. You must create them, and setup the appropriate options for each easy handle, as outlined in the <i><a href="/docs/linux/man/3-libcurl/">libcurl</a>(3)</i> man page, using <i><a href="/docs/linux/man/3-curl_easy_setopt/">curl_easy_setopt</a>(3)</i>. </p>
<p> When the easy handle is setup for a transfer, then instead of using <i><a href="/docs/linux/man/3-curl_easy_perform/">curl_easy_perform</a>(3)</i> (as when using the easy interface for transfers), you should instead add the easy handle to the multi handle using <i><a href="/docs/linux/man/3-curl_multi_add_handle/">curl_multi_add_handle</a>(3)</i>. The multi handle is sometimes referred to as a &#8216;multi stack&#8217; because of the fact that it may hold a large amount of easy handles. </p>
<p> Should you change your mind, the easy handle is again removed from the multi stack using <i><a href="/docs/linux/man/3-curl_multi_remove_handle/">curl_multi_remove_handle</a>(3)</i>. Once removed from the multi handle, you can again use other easy interface functions like <i><a href="/docs/linux/man/3-curl_easy_perform/">curl_easy_perform</a>(3)</i> on the handle or whatever you think is necessary. </p>
<p> Adding the easy handle to the multi handle does not start the transfer. Remember that one of the main ideas with this interface is to let your application drive. You drive the transfers by invoking <i><a href="/docs/linux/man/3-curl_multi_perform/">curl_multi_perform</a>(3)</i>. libcurl will then transfer data if there is anything available to transfer. It&#8217;ll use the callbacks and everything else you have setup in the individual easy handles. It&#8217;ll transfer data on all current transfers in the multi stack that are ready to transfer anything. It may be all, it may be none. </p>
<p> Your application can acquire knowledge from libcurl when it would like to get invoked to transfer data, so that you don&#8217;t have to busy-loop and call that <i><a href="/docs/linux/man/3-curl_multi_perform/">curl_multi_perform</a>(3)</i> like crazy. <i><a href="/docs/linux/man/3-curl_multi_fdset/">curl_multi_fdset</a>(3)</i> offers an interface using which you can extract fd_sets from libcurl to use in select() or poll() calls in order to get to know when the transfers in the multi stack might need attention. This also makes it very easy for your program to wait for input on your own private file descriptors at the same time or perhaps timeout every now and then, should you want that. </p>
<p> <i><a href="/docs/linux/man/3-curl_multi_perform/">curl_multi_perform</a>(3)</i> stores the number of still running transfers in one of its input arguments, and by reading that you can figure out when all the transfers in the multi handles are done. &#8216;done&#8217; does not mean successful. One or more of the transfers may have failed. Tracking when this number changes, you know when one or more transfers are done. </p>
<p> To get information about completed transfers, to figure out success or not and similar, <i><a href="/docs/linux/man/3-curl_multi_info_read/">curl_multi_info_read</a>(3)</i> should be called. It can return a message about a current or previous transfer. Repeated invokes of the function get more messages until the message queue is empty. The information you receive there includes an easy handle pointer which you may use to identify which easy handle the information regards. </p>
<p> When a single transfer is completed, the easy handle is still left added to the multi stack. You need to first remove the easy handle with <i><a href="/docs/linux/man/3-curl_multi_remove_handle/">curl_multi_remove_handle</a>(3)</i> and then close it with <i><a href="/docs/linux/man/3-curl_easy_cleanup/">curl_easy_cleanup</a>(3)</i>, or possibly set new options to it and add it again with <i><a href="/docs/linux/man/3-curl_multi_add_handle/">curl_multi_add_handle</a>(3)</i> to start another transfer. </p>
<p> When all transfers in the multi stack are done, cleanup the multi handle with <i><a href="/docs/linux/man/3-curl_multi_cleanup/">curl_multi_cleanup</a>(3)</i>. Be careful and please note that you <code>MUST</code> invoke separate <i><a href="/docs/linux/man/3-curl_easy_cleanup/">curl_easy_cleanup</a>(3)</i> calls on every single easy handle to clean them up properly. </p>
<p> If you want to re-use an easy handle that was added to the multi handle for transfer, you must first remove it from the multi stack and then re-add it again (possibly after having altered some options at your own choice).</p>
<h2>MULTI_SOCKET</h2>
<p> <i><a href="/docs/linux/man/3-curl_multi_socket_action/">curl_multi_socket_action</a>(3)</i> function offers a way for applications to not only avoid being forced to use select(), but it also offers a much more high-performance API that will make a significant difference for applications using large numbers of simultaneous connections. </p>
<p> <i><a href="/docs/linux/man/3-curl_multi_socket_action/">curl_multi_socket_action</a>(3)</i> is then used instead of <i><a href="/docs/linux/man/3-curl_multi_perform/">curl_multi_perform</a>(3)</i>. </p>
<p> When using this API, you add easy handles to the multi handle just as with the normal multi interface. Then you also set two callbacks with the CURLMOPT_SOCKETFUNCTION and CURLMOPT_TIMERFUNCTION options to <i><a href="/docs/linux/man/3-curl_multi_setopt/">curl_multi_setopt</a>(3)</i>. </p>
<p> The API is then designed to inform your application about which sockets libcurl is currently using and for what activities (read and/or write) on those sockets your application is expected to wait for. </p>
<p> Your application must then make sure to receive all sockets informed about in the CURLMOPT_SOCKETFUNCTION callback and make sure it reacts on the given activity on them. When a socket has the given activity, you call <i><a href="/docs/linux/man/3-curl_multi_socket_action/">curl_multi_socket_action</a>(3)</i> specifying which socket and action there are. </p>
<p> The CURLMOPT_TIMERFUNCTION callback is called to set a timeout. When that timeout expires, your application should call the <i><a href="/docs/linux/man/3-curl_multi_socket_action/">curl_multi_socket_action</a>(3)</i> function saying it was due to a timeout.</p>
<h2>BLOCKING</h2>
<p> A few areas in the code are still using blocking code, even when used from the multi interface. While we certainly want and intend for these to get fixed in the future, you should be aware of the following current restrictions: </p>
<pre>
 - Name resolves unless the c-ares or threaded-resolver backends are used
 - NSS SSL connections
 - HTTP proxy CONNECT operations
 - SOCKS proxy handshakes
 - file:// transfers
 - TELNET transfers
</pre>
<h2>Index</h2>

---
title: "curlopt_nosignal(3)"
name: "curlopt_nosignal"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_nosignal/"
---

CURLOPT_NOSIGNAL - skip all signal handling
<h2>Synopsis</h2>#include &lt;curl/curl.h&gt; 

 CURLcode curl_easy_setopt(CURL *handle, CURLOPT_NOSIGNAL, long onoff);
<h2>Description</h2>If <i>onoff</i> is 1, libcurl will not use any functions that install signal handlers or any functions that cause signals to be sent to the process. This option is here to allow multi-threaded unix applications to still set/use all timeout options etc, without risking getting signals. 

 If this option is set and libcurl has been built with the standard name resolver, timeouts will not occur while the name resolve takes place. Consider building libcurl with the c-ares or threaded resolver backends to enable asynchronous DNS lookups, to enable timeouts for name resolves without the use of signals. 

 Setting <i><a HREF="/docs/linux/man/3-curlopt_nosignal/">CURLOPT_NOSIGNAL</a>(3)</i> to 1 makes libcurl NOT ask the system to ignore SIGPIPE signals, which otherwise are sent by the system when trying to send data to a socket which is closed in the other end. libcurl makes an effort to never cause such SIGPIPEs to trigger, but some operating systems have no way to avoid them and even on those that have there are some corner cases when they may still happen, contrary to our desire. In addition, using <i>CURLAUTH_NTLM_WB</i> authentication could cause a SIGCHLD signal to be raised.
<h2>Default</h2>0
<h2>Availability</h2>Added in 7.10
<h2>Return Value</h2>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.

---
title: "curl_share_setopt(3)"
name: "curl_share_setopt"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_share_setopt/"
description: "curl_share_setopt – Set options for a shared object"
---

<h2>NAME</h2>
<p> curl_share_setopt &#8211; Set options for a shared object</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;curl/curl.h&gt;</code> </p>
<p> CURLSHcode curl_share_setopt(CURLSH *share, CURLSHoption option, parameter);</p>
<h2>DESCRIPTION</h2>
<p> Set the <i>option</i> to <i>parameter</i> for the given <i>share</i>.</p>
<h2>OPTIONS</h2>
<dl>
<dt>CURLSHOPT_LOCKFUNC</p>
<dd> The <i>parameter</i> must be a pointer to a function matching the following prototype: </p>
<p> void lock_function(CURL *handle, curl_lock_data data, curl_lock_access access, void *userptr); </p>
<p> <i>data</i> defines what data libcurl wants to lock, and you must make sure that only one lock is given at any time for each kind of data. </p>
<p> <i>access</i> defines what access type libcurl wants, shared or single. </p>
<p> <i>userptr</i> is the pointer you set with <i>CURLSHOPT_USERDATA</i>.</p>
<dt>CURLSHOPT_UNLOCKFUNC</p>
<dd> The <i>parameter</i> must be a pointer to a function matching the following prototype: </p>
<p> void unlock_function(CURL *handle, curl_lock_data data, void *userptr); </p>
<p> <i>data</i> defines what data libcurl wants to unlock, and you must make sure that only one lock is given at any time for each kind of data. </p>
<p> <i>userptr</i> is the pointer you set with <i>CURLSHOPT_USERDATA</i>.</p>
<dt>CURLSHOPT_SHARE</p>
<dd> The <i>parameter</i> specifies a type of data that should be shared. This may be set to one of the values described below.</p>
<dl>
<dt>
<dd>
<dl>
<dt>CURL_LOCK_DATA_COOKIE</p>
<dd> Cookie data will be shared across the easy handles using this shared object.</p>
<dt>CURL_LOCK_DATA_DNS</p>
<dd> Cached DNS hosts will be shared across the easy handles using this shared object. Note that when you use the multi interface, all easy handles added to the same multi handle will share DNS cache by default without this having to be used!</p>
<dt>CURL_LOCK_DATA_SSL_SESSION</p>
<dd> SSL session IDs will be shared across the easy handles using this shared object. This will reduce the time spent in the SSL handshake when reconnecting to the same server. Note SSL session IDs are reused within the same easy handle by default.</dl>
</dl>
<dt>CURLSHOPT_UNSHARE</p>
<dd> This option does the opposite of <i>CURLSHOPT_SHARE</i>. It specifies that the specified <i>parameter</i> will no longer be shared. Valid values are the same as those for <i>CURLSHOPT_SHARE</i>.</p>
<dt>CURLSHOPT_USERDATA</p>
<dd> The <i>parameter</i> allows you to specify a pointer to data that will be passed to the lock_function and unlock_function each time it is called.</dl>
<h2>RETURN VALUE</h2>
<p> CURLSHE_OK (zero) means that the option was set properly, non-zero means an error occurred as <i>&lt;curl/curl.h&gt;</i> defines. See the <i>libcurl-errors.3</i> man page for the full list with descriptions.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-curl_share_cleanup/">curl_share_cleanup</a></code>(3), <code><a href="/docs/linux/man/3-curl_share_init/">curl_share_init</a></code>(3) </p>
<h2>Index</h2>

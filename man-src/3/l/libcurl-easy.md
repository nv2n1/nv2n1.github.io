---
title: "libcurl-easy(3)"
name: "libcurl-easy"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libcurl-easy/"
---

<h2>NAME</h2>

 libcurl-easy - easy interface overview

<h2>DESCRIPTION</h2>

 When using libcurl's &quot;easy&quot; interface you init your session and get a handle (often referred to as an &quot;easy handle&quot;), which you use as input to the easy interface functions you use. Use <i><a HREF="/docs/linux/man/3-curl_easy_init/">curl_easy_init</a>(3)</i> to get the handle. 

 You continue by setting all the options you want in the upcoming transfer, the most important among them is the URL itself (you can't transfer anything without a specified URL as you may have figured out yourself). You might want to set some callbacks as well that will be called from the library when data is available etc. <i><a HREF="/docs/linux/man/3-curl_easy_setopt/">curl_easy_setopt</a>(3)</i> is used for all this. 

 When all is setup, you tell libcurl to perform the transfer using <i><a HREF="/docs/linux/man/3-curl_easy_perform/">curl_easy_perform</a>(3)</i>. It will then do the entire operation and won't return until it is done (successfully or not). 

 After the transfer has been made, you can set new options and make another transfer, or if you're done, cleanup the session by calling <i><a HREF="/docs/linux/man/3-curl_easy_cleanup/">curl_easy_cleanup</a>(3)</i>. If you want persistent connections, you don't cleanup immediately, but instead run ahead and perform other transfers using the same easy handle. 

 

<h2>Index</h2>



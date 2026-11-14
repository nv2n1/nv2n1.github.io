---
title: "ares_save_options(3)"
name: "ares_save_options"
section: "3"
letter: "a"
url: "/docs/linux/man/3-ares_save_options/"
description: "ares_save_options – Save configuration values obtained from initialized ares_channel"
---

<h2>NAME</h2>
<p> ares_save_options &#8211; Save configuration values obtained from initialized ares_channel</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ares.h&gt;
int ares_save_options(ares_channel channel, struct ares_options *options, int *optmask)
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-ares_save_options/">ares_save_options</a>(3)</code> function saves the channel data identified by <i>channel</i>, into the options struct identified by <i>options</i>, and saves the mask of options which are set to the integer pointer (passed by reference) identified by <i>optmask</i>. </p>
<p> The resultant options and optmask are then able to be passed directly to ares_init_options. When the options are no longer needed, ares_destroy_options should be called to free any associated memory.</p>
<h2>RETURN VALUES</h2>
<p> <code><a href="/docs/linux/man/3-ares_save_options/">ares_save_options</a>(3)</code> can return any of the following values:</p>
<dl>
<dt><code>ARES_SUCCESS</code></p>
<dd> The channel data was successfuly stored</p>
<dt><code>ARES_ENOMEM</code></p>
<dd> The memory was exhausted</p>
<dt><code>ARES_ENODATA</code></p>
<dd> The channel data identified by <i>channel</i> were invalid.</dl>
<h2>NOTE</h2>
<p> Since c-ares 1.6.0 the ares_options struct has been &quot;locked&quot; meaning that it won&#8217;t be extended to cover new functions. This function will remain functioning, but it can only return config data that can be represented in this config struct, which may no longer be the complete set of config options. <code><a href="/docs/linux/man/3-ares_dup/">ares_dup</a>(3)</code> will not have that restriction. </p>
<p> The ares_options struct can not handle potential IPv6 name servers the ares_channel might be configured to use. The <code><a href="/docs/linux/man/3-ares_save_options/">ares_save_options</a>(3)</code> function will only return IPv4 servers, if any. In order to retrieve all name servers an ares_channel might be using, the <code><a href="/docs/linux/man/3-ares_get_servers/">ares_get_servers</a>(3)</code> function must be used instead.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ares_destroy_options/">ares_destroy_options</a></code>(3), <code><a href="/docs/linux/man/3-ares_init_options/">ares_init_options</a></code>(3), <code><a href="/docs/linux/man/3-ares_get_servers/">ares_get_servers</a></code>(3), <code><a href="/docs/linux/man/3-ares_dup/">ares_dup</a></code>(3)</p>
<h2>AVAILABILITY</h2>
<p> <a href="/docs/linux/man/3-ares_save_options/">ares_save_options</a>(3) was added in c-ares 1.4.0</p>
<h2>AUTHOR</h2>
<p> Brad House<br />
 Copyright 1998 by the Massachusetts Institute of Technology. </p>
<h2>Index</h2>

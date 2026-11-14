---
title: "tcmodinfo(1)"
name: "tcmodinfo"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tcmodinfo/"
description: "tcmodinfo – Get and Set information in transcode modules"
---

<h2>NAME</h2>
<p> tcmodinfo &#8211; Get and Set information in transcode modules</p>
<h2>SYNOPSIS</h2>
<p> <code>tcmodinfo</code> [ <code>-i</code> <i>name</i> ] [ <code>-m</code> <i>path</i> ] [ <code>-t</code> <i>type</i> ] [ <code>-M</code> <i>param</i> ] [ <code>-C</code> <i>param</i> ] [ <code>-s</code> <i>socket</i> ] [ <code>-p</code> ] [ <code>-d</code> <i>verbosity</i> ] [ <code>-v</code> ]</p>
<h2>COPYRIGHT</h2>
<p> <code>tcmodinfo</code> is Copyright (C) by Tilmann Bitterberg/Transcode Team</p>
<h2>DESCRIPTION</h2>
<p> <code>tcmodinfo</code> loads a supplied <a href="/docs/linux/man/1-transcode/">transcode</a>(1) module and prints its parameters, or inquiry about default settings. It can also connect to transcode through a socket to do runtime configuration of transcode and its filters. Anyway, this last feature may be moved to some other helper program in future releases.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i</code> <i>name</i></p>
<dd> Specify the name of the module. <i>Name</i> is specified without the prefix <code>(i.e., filter_)_</code> and without the suffix <code>.so</code> So if you want information about filter_smooth.so, just supply <code>smooth</code></p>
<dt><code>-m</code> <i>path</i></p>
<dd> Look in <i>Path</i> instead of the compiled-in module path for a module.</p>
<dt><code>-t</code> <i>type</i></p>
<dd> Specify the <i>Type</i> of module to load. Default is filter modules. In current (1.1.0) release, tcmodinfo support &#8216;filter&#8217;, &#8216;encode&#8217; and &#8216;multiplex&#8217; module types. More types will be added in future releases, to cover all the transcode module range.</p>
<dt><code>-M</code> <i>parameter</i></p>
<dd> Print out the default setting of given parameter of a given (use -i/-t options too) module. If parameter isn&#8217;t known, nothing will be print out.<br />
 Caution: -M can&#8217;t be used together with -C</p>
<dt><code>-C</code> <i>configuration string</i></p>
<dd> Request to configure the module using given configuration string. Meaning of configuration string is of course module dependent, but format is always<br />
 param1:key1=val1:param2:param3:key2=val2<br />
 This option is used for debug purposes, you usually shouldn&#8217;t need it.<br />
 Caution: -C can&#8217;t be used together with -M</p>
<dt><code>-s</code> <i>socket</i></p>
<dd> Connect to socket <i>socket</i>. You can use this socket to do runtime configuration of transcode. For all the boring details about the socket protocol have a look at /docs/filter-socket.txt. transcode has to be started with the <code>&#8211;socket</code> option to open the socket.</p>
<dt><code>-d</code> <i>verbosity</i></p>
<dd> Specify the verbosiness level to use, like transcode does. Default value is 1 (TC_INFO verbosiness).</p>
<dt><code>-p</code></p>
<dd> Print the compiled-in module path and exit.</p>
<dt><code>-v</code></p>
<dd> Print version information and exit.</dl>
<h2>EXAMPLES</h2>
<p> The command </p>
<p> <code>tcmodinfo -i smooth</code> </p>
<p> prints information about the smooth filter. </p>
<p> <code>tcmodinfo -i levels -t filter</code> </p>
<p> same as above for levels filter (-t filter it&#8217;s the default) </p>
<p> <code>tcmodinfo -i raw -t multiplex</code> </p>
<p> same as above for raw multiplexor </p>
<p> <code>tcmodinfo -i xvid -t encode</code> </p>
<p> same as above for XviD encoder </p>
<p> <code>transcode &#8211;socket /tmp/tc-socket &amp;</code><br />
 <code>echo help | tcmodinfo -s /tmp/tc-socket</code> </p>
<p> prints the socket help text and exits. </p>
<p> <code>tcmodinfo -s /tmp/tc-socket</code> </p>
<p> Will drop you into an interactive &quot;shell&quot; where you can talk to the socket.</p>
<h2>AUTHORS</h2>
<p> <code>tcmodinfo</code> was written by Tilmann Bitterberg<br />
 &lt;transcode [at] tibit.org&gt; with contributions from many others. See AUTHORS for details.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-avimerge/">avimerge</a></code>(1), <code><a href="/docs/linux/man/1-avisplit/">avisplit</a></code>(1), <code><a href="/docs/linux/man/1-tccat/">tccat</a></code>(1), <code><a href="/docs/linux/man/1-tcdecode/">tcdecode</a></code>(1), <code><a href="/docs/linux/man/1-tcdemux/">tcdemux</a></code>(1), <code><a href="/docs/linux/man/1-tcextract/">tcextract</a></code>(1), <code><a href="/docs/linux/man/1-tcprobe/">tcprobe</a></code>(1), <code><a href="/docs/linux/man/1-tcscan/">tcscan</a></code>(1), <code><a href="/docs/linux/man/1-transcode/">transcode</a></code>(1) </p>
<h2>Index</h2>

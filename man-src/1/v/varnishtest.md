---
title: "varnishtest(1)"
name: "varnishtest"
section: "1"
letter: "v"
url: "/docs/linux/man/1-varnishtest/"
description: "varnishtest – Test program for Varnish"
---

<h2>NAME</h2>
<p> varnishtest &#8211; Test program for Varnish</p>
<h2>SYNOPSIS</h2>
<p> varnishtest [-iklLqv] [-n iter] [-D name=val] [-j jobs] [-t duration] file [file &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> The varnishtest program is a script driven program used to test the Varnish Cache. </p>
<p> The varnishtest program, when started and given one or more script files, can create a number of threads representing backends, some threads representing clients, and a varnishd process. This is then used to simulate a transaction to provoke a specific behavior. </p>
<p> The following options are available: </p>
<p> -D name=val Define macro for use in scripts</p>
<dl>
<dt><code>-i</code></p>
<dd> Find varnishd in build tree</p>
<dt><code>-j</code><i>&nbsp;<wbr>jobs</i></p>
<dd> Run this many tests in parallel</p>
<dt><code>-k</code></p>
<dd> Continue on test failure</p>
<dt><code>-l</code></p>
<dd> Leave temporary vtc.* if test fails</p>
<dt><code>-L</code></p>
<dd> Always leave temporary vtc.*</p>
<dt><code>-n</code><i>&nbsp;<wbr>iterations</i></p>
<dd> Run tests this many times</p>
<dt><code>-q</code></p>
<dd> Quiet mode: report only failures</p>
<dt><code>-t</code><i>&nbsp;<wbr>duration</i></p>
<dd> Time tests out after this long</p>
<dt><code>-v</code></p>
<dd> Verbose mode: always report test log</p>
<dt><code>-h</code></p>
<dd> Show help </p>
<p> file File to use as a script </p>
<p> Macro definitions that can be overridden. </p>
<p> varnishd Path to varnishd to use [varnishd] </p>
<p> If <i>TMPDIR</i> is set in the environment, varnishtest creates temporary <i>vtc.*</i> directories for each test in <i>$TMPDIR</i>, otherwise in <i>/tmp</i>.</dl>
<h2>SCRIPTS</h2>
<p> The script language used for Varnishtest is not a strictly defined language. The best reference for writing scripts is the varnishtest program itself. In the Varnish source code repository, under <i>bin/varnishtest/tests/</i>, all the regression tests for Varnish are kept. </p>
<p> An example: </p>
<pre><code>
varnishtest "#1029" server s1{
    rxreq
        expect req.url == "/bar" txresp - gzipbody{[bar]} rxreq expect req.url ==
    "/foo" txresp - body{&lt;h1&gt; FOO &lt; esi : include src = "/bar" / &gt; BARF&lt;/ h1&gt;}} -
    start
        varnish v1 -
    vcl + backend{sub vcl_backend_response{set beresp.do_esi = true;
if (bereq.url == "/foo") {
    set beresp.ttl = 0s;
} else {
    set beresp.ttl = 10m;
}
}
}
- start
        client c1{
            txreq - url "/bar" - hdr "Accept-Encoding: gzip" rxresp gunzip expect resp.bodylen == 5 txreq - url "/foo" - hdr "Accept-Encoding: gzip" rxresp expect resp.bodylen == 21} -
    run
</code></pre>
<p> When run, the above script will simulate a server (s1) that expects two different requests. It will start a Varnish server (v1) and add the backend definition to the VCL specified (-vcl+backend). Finally it starts the c1-client, which is a single client sending two requests.</p>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</p>
<dd> varnishtest source code repository with tests</p>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/1-varnishhist/">varnishhist</a>(1)</p>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/1-varnishlog/">varnishlog</a>(1)</p>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/1-varnishncsa/">varnishncsa</a>(1)</p>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/1-varnishstat/">varnishstat</a>(1)</p>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/1-varnishtop/">varnishtop</a>(1)</p>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/7-vcl/">vcl</a>(7)</dl>
<h2>HISTORY</h2>
<p> The varnishtest program was developed by Poul-Henning Kamp &lt;<i>phk [at] phk.freebsd.dk</i>&gt; in cooperation with Varnish Software AS. This manual page was originally written by Stig Sandbeck Mathisen &lt;<i>ssm [at] linpro.no</i>&gt; and updated by Kristian Lyngstøl &lt;<i>kristian [at] varnish-cache.org</i>&gt;.</p>
<h2>COPYRIGHT</h2>
<p> This document is licensed under the same licence as Varnish itself. See LICENCE for details.</p>
<dl>
<dt>&bull;</p>
<dd> Copyright (c) 2007-2014 Varnish Software AS </p>
</dl>
<h2>Index</h2>

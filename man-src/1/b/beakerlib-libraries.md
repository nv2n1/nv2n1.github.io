---
title: "beakerlib-libraries(1)"
name: "beakerlib-libraries"
section: "1"
letter: "b"
url: "/docs/linux/man/1-beakerlib-libraries/"
description: "BeakerLib – libraries – mechanism for loading shared test code from libraries"
---

<h2 class="name">NAME</h2>
<p> BeakerLib &#8211; libraries &#8211; mechanism for loading shared test code from libraries </p>
<h2>DESCRIPTION</h2>
<p> This file contains functions for bringing external code into the test namespace.</p>
<h2>FUNCTIONS</h2>
<p> <i>rlImport</i> </p>
<p> Imports code provided by one or more libraries into the test namespace. The library search mechanism is based on Beaker test hierarchy system, i.e.: </p>
<p> /component/type/test-name/test-file </p>
<p> When test-file calls rlImport with &#8216;foo/bar&#8217; parameter, the directory path is traversed upwards, and a check for presence of the test /foo/Library/bar/ will be performed. This means this function needs to be called from the test hierarchy, not e.g. the /tmp directory. </p>
<p> Once library is found, it is sourced and a verifier function is called. The verifier function is cunstructed by composing the library prefix and LibraryLoaded. Library prefix can be defined in the library itself. If the verifier passes the library is ready to use. Also variable <code>&lt;</code><font SIZE="-1"><code>PREFIX</code></font><code>&gt;LibraryDir</code> is created and it points to the library folder. </p>
<p> Usage: </p>
<pre>
    rlImport --all
    rlImport LIBRARY [LIBRARY2...]
</pre>
<dl>
<dt>&#8211;all</p>
<dd> Read Makefile in current/original directory, pick library requirements up and import them all.</p>
<dt><font SIZE="-1">LIBRARY</font></p>
<dd> Must have &#8216;component/library&#8217; format. Identifies the library to import.</dl>
<p> Returns 0 if the import of all libraries was successful. Returns non-zero if one or more library failed to import.</p>
<h2>AUTHORS</h2>
<dl>
<dt>&bull;</p>
<dd> Petr Muller &lt;muller [at] redhat.com&gt;</p>
<dt>&bull;</p>
<dd> Dalibor Pospisil &lt;dapospis [at] redhat.com&gt; </p>
</dl>
<h2>Index</h2>

---
title: "libssh2_version(3)"
name: "libssh2_version"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_version/"
---

<h2>NAME</h2>

 libssh2_version - return the libssh2 version number

<h2>SYNOPSIS</h2>

 #include &lt;libssh2.h&gt; 

 const char * libssh2_version(int required_version);

<h2>DESCRIPTION</h2>

 If <i>required_version</i> is lower than or equal to the version number of the libssh2 in use, the version number of libssh2 is returned as a pointer to a zero terminated string. 

 The <i>required_version</i> should be the version number as constructed by the LIBSSH2_VERSION_NUM define in the libssh2.h public header file, which is a 24 bit number in the 0xMMmmpp format. MM for major, mm for minor and pp for patch number.

<h2>RETURN VALUE</h2>

 The version number of libssh2 is returned as a pointer to a zero terminated string or NULL if the <i>required_version</i> isn't fulfilled.

<h2>EXAMPLE</h2>

 To make sure you run with the correct libssh2 version: 

 <pre><code>
if (!libssh2_version(LIBSSH2_VERSION_NUM)) {
    fprintf(stderr, "Runtime libssh2 version too old!");
    exit(1);
}
</code></pre> 

 Unconditionally get the version number: 

 printf(&quot;libssh2 version: %s&quot;, libssh2_version(0) );

<h2>AVAILABILITY</h2>

 This function was added in libssh2 1.1, in previous versions there way no way to extract this info in run-time. 

<h2>Index</h2>



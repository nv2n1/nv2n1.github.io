---
title: "abrt-action-analyze-ccpp-local(1)"
name: "abrt-action-analyze-ccpp-local"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abrt-action-analyze-ccpp-local/"
---

<h2 class="name">NAME</h2>
 

 abrt-action-analyze-ccpp-local - Generates backtrace and search for duplicates 

<h2>SYNOPSIS</h2>

 

 abrt-action-analyze-ccpp-local [--without-di][--without-bz][--without-bodhi]

<h2>DESCRIPTION</h2>

 

 This tool downloads debuginfo and generates a backtrace for coredump in the problem directory, also checks for existing duplicates in bugzilla and possible updates related to the detected crash

<h3>Integration with ABRT events</h3>

 

 <i>abrt-action-analyze-ccpp-local</i> is used in the analyze step when processing C/C++ crashes 

<dl>
<dt>
<dd> <pre>
EVENT=analyze_LocalGDB analyzer=CCpp
    abrt-action-analyze-ccpp-local
</pre></dl>

<h2>OPTIONS</h2>

 

 --without-di
<dl>
<dt>
<dd> Don't install debuginfo packages</dl>
 

 --without-bz
<dl>
<dt>
<dd> Don't search bugzilla for existing duplicates</dl>
 

 --without-bodhi
<dl>
<dt>
<dd> Don't search bodhi for existing updates</dl>

<h2>AUTHORS</h2>

 

<dl>
<dt>
<dd> &bull; ABRT team</dl>
 

<h2>Index</h2>



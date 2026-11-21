---

title: "abrt-action-analyze-ccpp-local(1)"
name: "abrt-action-analyze-ccpp-local"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abrt-action-analyze-ccpp-local/"
---

abrt-action-analyze-ccpp-local - Generates backtrace and search for duplicates 

abrt-action-analyze-ccpp-local [--without-di][--without-bz][--without-bodhi]

This tool downloads debuginfo and generates a backtrace for coredump in the problem directory, also checks for existing duplicates in bugzilla and possible updates related to the detected crash

<h3>Integration with ABRT events</h3>

 

 <i>abrt-action-analyze-ccpp-local</i> is used in the analyze step when processing C/C++ crashes 

<dl>
<dt>
</dt><dd> <pre>
EVENT=analyze_LocalGDB analyzer=CCpp
    abrt-action-analyze-ccpp-local
</pre></dd></dl>

<h2>OPTIONS</h2>

 

 --without-di
<dl>
<dt>
</dt><dd> Don't install debuginfo packages</dd></dl>
 

 --without-bz
<dl>
<dt>
</dt><dd> Don't search bugzilla for existing duplicates</dd></dl>
 

 --without-bodhi
<dl>
<dt>
</dt><dd> Don't search bodhi for existing updates</dd></dl>

<h2>AUTHORS</h2>

 

<dl>
<dt>
</dt><dd> &bull; ABRT team</dd></dl>

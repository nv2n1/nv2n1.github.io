---
title: "ffi(3)"
name: "ffi"
section: "3"
letter: "f"
url: "/docs/linux/man/3-ffi/"
description: "FFI – Foreign Function Interface"
---

<h2 class="name">NAME</h2>
<p> <code>FFI</code> &#8211; Foreign Function Interface </p>
<h2>LIBRARY</h2>
<p> libffi, -lffi</p>
<h2>SYNOPSIS</h2>
<p> In ffi.h Ft ffi_status Fo ffi_prep_cif Fa ffi_cif *cif Fa ffi_abi abi Fa unsigned int nargs Fa ffi_type *rtype Fa ffi_type **atypes Fc Ft void Fo ffi_prep_cif_var Fa ffi_cif *cif Fa ffi_abi abi Fa unsigned int nfixedargs Fa unsigned int ntotalargs Fa ffi_type *rtype Fa ffi_type **atypes Fc Ft void Fo ffi_call Fa ffi_cif *cif Fa void (*fn)(void) Fa void *rvalue Fa void **avalue Fc</p>
<h2>DESCRIPTION</h2>
<p> The foreign function interface provides a mechanism by which a function can generate a call to another function at runtime without requiring knowledge of the called function&#8217;s interface at compile time.</p>
<h2>SEE ALSO</h2>
<p> ffi_prep_cif3, ffi_prep_cif_var3, ffi_call3 </p>
<h2>Index</h2>

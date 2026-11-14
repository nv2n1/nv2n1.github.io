---
title: "ffi_prep_cif_var(3)"
name: "ffi_prep_cif_var"
section: "3"
letter: "f"
url: "/docs/linux/man/3-ffi_prep_cif_var/"
description: "ffi_prep_cif_var – Prepare a ffi_cif structure for use with ffi_call for variadic functions."
---

<h2 class="name">NAME</h2>
<p> <code>ffi_prep_cif_var</code> &#8211; Prepare a <code>ffi_cif</code> structure for use with <code>ffi_call</code> for variadic functions. </p>
<h2>SYNOPSIS</h2>
<p> In ffi.h Ft ffi_status Fo ffi_prep_cif_var Fa ffi_cif *cif Fa ffi_abi abi Fa unsigned int nfixedargs Fa unsigned int ntotalargs Fa ffi_type *rtype Fa ffi_type **atypes Fc</p>
<h2>DESCRIPTION</h2>
<p> The <code>ffi_prep_cif_var</code> function prepares a <code>ffi_cif</code> structure for use with <code>ffi_call</code> for variadic functions. Fa abi specifies a set of calling conventions to use. Fa atypes is an array of Fa ntotalargs pointers to <code>ffi_type</code> structs that describe the data type, size and alignment of each argument. Fa rtype points to an <code>ffi_type</code> that describes the data type, size and alignment of the return value. Fa nfixedargs must contain the number of fixed (non-variadic) arguments. Note that to call a non-variadic function <code>ffi_prep_cif</code> must be used.</p>
<h2>RETURN VALUES</h2>
<p> Upon successful completion, <code>ffi_prep_cif_var</code> returns <code>FFI_OK</code> It will return <code>FFI_BAD_TYPEDEF</code> if Fa cif is <code>NULL</code> or Fa atypes or Fa rtype is malformed. If Fa abi does not refer to a valid ABI, <code>FFI_BAD_ABI</code> will be returned. Available ABIs are defined in <code>&lt;ffitarget.h&gt;</code></p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-ffi/">ffi</a>(3), ffi_call3, ffi_prep_cif3 </p>
<h2>Index</h2>

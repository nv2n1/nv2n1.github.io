---
title: "hx509_oid_sprint(3)"
name: "hx509_oid_sprint"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hx509_oid_sprint/"
description: "hx509 printing functions –"
---

<h2 class="name">NAME</h2>
<p> hx509 printing functions &#8211; </p>
<h3>Functions</h3>
<p> void <code>hx509_bitstring_print</code> (const heim_bit_string *, hx509_vprint_func, void *) </p>
<p> int <code>hx509_cert_keyusage_print</code> (hx509_context, hx509_cert, char **) </p>
<p> void <code>hx509_oid_print</code> (const heim_oid *, hx509_vprint_func, void *) </p>
<p> int <code>hx509_oid_sprint</code> (const heim_oid *, char **) </p>
<p> void <code>hx509_print_stdout</code> (void *, const char *, va_list) </p>
<p> int <code>hx509_validate_cert</code> (hx509_context, hx509_validate_ctx, hx509_cert) </p>
<p> void <code>hx509_validate_ctx_add_flags</code> (hx509_validate_ctx, int) </p>
<p> void <code>hx509_validate_ctx_free</code> (hx509_validate_ctx) </p>
<p> int <code>hx509_validate_ctx_init</code> (hx509_context, hx509_validate_ctx *) </p>
<p> void <code>hx509_validate_ctx_set_print</code> (hx509_validate_ctx, hx509_vprint_func, void *) </p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>void hx509_bitstring_print (const heim_bit_string *b, hx509_vprint_funcfunc, void *ctx)</h3>
<p> Print a bitstring using a hx509_vprint_func function. To print to stdout use <code>hx509_print_stdout()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>b</i> bit string to print.<br />
 <i>func</i> hx509_vprint_func to print with.<br />
 <i>ctx</i> context variable to hx509_vprint_func function.</dl>
<h3>int hx509_cert_keyusage_print (hx509_contextcontext, hx509_certc, char **s)</h3>
<p> Print certificate usage for a certificate to a string. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>c</i> a certificate print the keyusage for.<br />
 <i>s</i> the return string with the keysage printed in to, free with <code>hx509_xfree()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>void hx509_oid_print (const heim_oid *oid, hx509_vprint_funcfunc, void *ctx)</h3>
<p> Print a oid using a hx509_vprint_func function. To print to stdout use <code>hx509_print_stdout()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>oid</i> oid to print<br />
 <i>func</i> hx509_vprint_func to print with.<br />
 <i>ctx</i> context variable to hx509_vprint_func function.</dl>
<h3>int hx509_oid_sprint (const heim_oid *oid, char **str)</h3>
<p> Print a oid to a string. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>oid</i> oid to print<br />
 <i>str</i> allocated string, free with <code>hx509_xfree()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>void hx509_print_stdout (void *ctx, const char *fmt, va_listva)</h3>
<p> Helper function to print on stdout for:</p>
<dl>
<dt>&bull;</p>
<dd> <code>hx509_oid_print()</code>,</p>
<dt>&bull;</p>
<dd> <code>hx509_bitstring_print()</code>,</p>
<dt>&bull;</p>
<dd> <code>hx509_validate_ctx_set_print()</code>.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ctx</i> the context to the print function. If the ctx is NULL, stdout is used.<br />
 <i>fmt</i> the printing format.<br />
 <i>va</i> the argumet list.</dl>
<h3>int hx509_validate_cert (hx509_contextcontext, hx509_validate_ctxctx, hx509_certcert)</h3>
<p> Validate/Print the status of the certificate. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>ctx</i> A hx509 validation context.<br />
 <i>cert</i> the cerificate to validate/print.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>void hx509_validate_ctx_add_flags (hx509_validate_ctxctx, intflags)</h3>
<p> Add flags to control the behaivor of the <code>hx509_validate_cert()</code> function. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ctx</i> A hx509 validation context.<br />
 <i>flags</i> flags to add to the validation context.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>void hx509_validate_ctx_free (hx509_validate_ctxctx)</h3>
<p> Free an hx509 validate context. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ctx</i> the hx509 validate context to free.</dl>
<h3>int hx509_validate_ctx_init (hx509_contextcontext, hx509_validate_ctx *ctx)</h3>
<p> Allocate a hx509 validation/printing context. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>ctx</i> a new allocated hx509 validation context, free with <code>hx509_validate_ctx_free()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>void hx509_validate_ctx_set_print (hx509_validate_ctxctx, hx509_vprint_funcfunc, void *c)</h3>
<p> Set the printing functions for the validation context. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ctx</i> a hx509 valication context.<br />
 <i>func</i> the printing function to usea.<br />
 <i>c</i> the context variable to the printing function.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Heimdalx509library from the source code. </p>
<h2>Index</h2>

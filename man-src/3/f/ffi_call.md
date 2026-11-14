---
title: "ffi_call(3)"
name: "ffi_call"
section: "3"
letter: "f"
url: "/docs/linux/man/3-ffi_call/"
description: "ffi_call – Invoke a foreign function."
---

<h2 class="name">NAME</h2>
<p> <code>ffi_call</code> &#8211; Invoke a foreign function. </p>
<h2>SYNOPSIS</h2>
<p> In ffi.h Ft void Fo ffi_call Fa ffi_cif *cif Fa void (*fn)(void) Fa void *rvalue Fa void **avalue Fc</p>
<h2>DESCRIPTION</h2>
<p> The <code>ffi_call</code> function provides a simple mechanism for invoking a function without requiring knowledge of the function&#8217;s interface at compile time. Fa fn is called with the values retrieved from the pointers in the Fa avalue array. The return value from Fa fn is placed in storage pointed to by Fa rvalue . Fa cif contains information describing the data types, sizes and alignments of the arguments to and return value from Fa fn , and must be initialized with <code>ffi_prep_cif</code> before it is used with <code>ffi_call</code> </p>
<p> Fa rvalue must point to storage that is sizeof(ffi_arg) or larger for non-floating point types. For smaller-sized return value types, the <code>ffi_arg</code> or <code>ffi_sarg</code> integral type must be used to hold the return value.</p>
<h2>EXAMPLES</h2>
<pre><code>
#include &lt;ffi.h&gt;
#include &lt;stdio.h&gt;
unsigned char
foo(unsigned int, float);
int main(int argc, const char **argv)
{
    ffi_cif cif;
    ffi_type *arg_types[2];
    void *arg_values[2];
    ffi_status status;
    // Because the return value from foo() is smaller than sizeof(long), it
    // must be passed as ffi_arg or ffi_sarg.
    ffi_arg result;
    // Specify the data type of each argument. Available types are defined
    // in &lt;ffi/ffi.h&gt;.
    arg_types[0] = &amp;ffi_type_uint;
    arg_types[1] = &amp;ffi_type_float;
    // Prepare the ffi_cif structure.
    if ((status = ffi_prep_cif(&amp;cif, FFI_DEFAULT_ABI,
                               2, &amp;ffi_type_uint8, arg_types)) != FFI_OK) {
        // Handle the ffi_status error.
    }
    // Specify the values of each argument.
    unsigned int arg1 = 42;
    float arg2 = 5.1;
    arg_values[0] = &amp;arg1;
    arg_values[1] = &amp;arg2;
    // Invoke the function.
    ffi_call(&amp;cif, FFI_FN(foo), &amp;result, arg_values);
    // The ffi_arg 'result' now contains the unsigned char returned from foo(),
    // which can be accessed by a typecast.
    printf("result is %hhu", (unsigned char)result);
    return 0;
}
// The target function.
unsigned char
foo(unsigned int x, float y)
{
    unsigned char result = x - y;
    return result;
}
</code></pre>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-ffi/">ffi</a>(3), ffi_prep_cif3 </p>
<h2>Index</h2>

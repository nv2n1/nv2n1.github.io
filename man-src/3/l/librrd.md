---
title: "librrd(3)"
name: "librrd"
section: "3"
letter: "l"
url: "/docs/linux/man/3-librrd/"
description: "librrd – RRD library functions"
---

<h2 class="name">NAME</h2>
<p> librrd &#8211; RRD library functions </p>
<h2>DESCRIPTION</h2>
<p> <code>librrd</code> contains most of the functionality in <code>RRDTool</code>. The command line utilities and language bindings are often just wrappers around the code contained in <code>librrd</code>. </p>
<p> This manual page documents the <code>librrd</code> <font SIZE="-1">API</font>. </p>
<p> <font SIZE="-1"><code>NOTE:</code></font> This document is a work in progress, and should be considered incomplete as long as this warning persists. For more information about the <code>librrd</code> functions, always consult the source code.</p>
<h2>CORE FUNCTIONS</h2>
<dl>
<dt><code>rrd_dump_cb_r(char *filename, int opt_header, rrd_output_callback_t cb, void *user)</code></p>
<dd> In some situations it is necessary to get the output of <tt>&quot;rrd_dump&quot;</tt> without writing it to a file or the standard output. In such cases an application can ask <code>rrd_dump_cb_r</code> to call an user-defined function each time there is output to be stored somewhere. This can be used, to e.g. directly feed an <font SIZE="-1">XML</font> parser with the dumped output or transfer the resulting string in memory. </p>
<p> The arguments for <code>rrd_dump_cb_r</code> are the same as for <code>rrd_dump_opt_r</code> except that the output filename parameter is replaced by the user-defined callback function and an additional parameter for the callback function that is passed untouched, i.e. to store information about the callback state needed for the user-defined callback to function properly. </p>
<p> Recent versions of <code>rrd_dump_opt_r</code> internally use this callback mechanism to write their output to the file provided by the user. </p>
<pre><code>
size_t rrd_dump_opt_cb_fileout(
    const void *data,
    size_t len,
    void *user)
{
    return fwrite(data, 1, len, (FILE *)user);
}
</code></pre>
<p> The associated call for <code>rrd_dump_cb_r</code> looks like </p>
<pre>
    res = rrd_dump_cb_r(filename, opt_header,
        rrd_dump_opt_cb_fileout, (void *)out_file);
</pre>
<p> where the last parameter specifies the file handle <code>rrd_dump_opt_cb_fileout</code> should write to. There&#8217;s no specific condition for the callback to detect when it is called for the first time, nor for the last time. If you require this for initialization and cleanup you should do those tasks before and after calling <code>rrd_dump_cr_r</code> respectively.</dl>
<h2>UTILITY FUNCTIONS</h2>
<dl>
<dt>rrd_random()</p>
<dd> Generates random numbers just like <i>random()</i>. This further ensures that the random number generator is seeded exactly once per process.</p>
<dt><code>rrd_add_ptr(void ***dest, size_t *dest_size, void *src)</code></p>
<dd> Dynamically resize the array pointed to by <tt>&quot;dest&quot;</tt>. <tt>&quot;dest_size&quot;</tt> is a pointer to the current size of <tt>&quot;dest&quot;</tt>. Upon successful <i>realloc()</i>, the <tt>&quot;dest_size&quot;</tt> is incremented by 1 and the <tt>&quot;src&quot;</tt> pointer is stored at the end of the new <tt>&quot;dest&quot;</tt>. Returns 1 on success, 0 on failure. </p>
<p>type **arr = NULL;<br />
type *elem = &#8220;whatever&#8221;;<br />
size_t arr_size = 0;<br />
if (!rrd_add_ptr(&amp;arr, &amp;arr_size, elem))<br />
    handle_failure();</p>
<dt><code>rrd_add_strdup(char ***dest, size_t *dest_size, char *src)</code></p>
<dd> Like <tt>&quot;rrd_add_ptr&quot;</tt>, except adds a <tt>&quot;strdup&quot;</tt> of the source string. </p>
<p>char **arr = NULL;<br />
size_t arr_size = NULL;<br />
char *str = &#8220;example text&#8221;;<br />
if (!rrd_add_strdup(&amp;arr, &amp;arr_size, str))<br />
    handle_failure();</p>
<dt><code>rrd_free_ptrs(void ***src, size_t *cnt)</code></p>
<dd> Free an array of pointers allocated by <tt>&quot;rrd_add_ptr&quot;</tt> or <tt>&quot;rrd_add_strdup&quot;</tt>. Also frees the array pointer itself. On return, the source pointer will be <font SIZE="-1">NULL</font> and the count will be zero. </p>
<pre><code>
/* created as above */
rrd_free_ptrs(&amp;arr, &amp;arr_size);
/* here, arr == NULL &amp;&amp; arr_size == 0 */
</code></pre>
<dt><code>rrd_mkdir_p(const char *pathname, mode_t mode)</code></p>
<dd> Create the directory named <tt>&quot;pathname&quot;</tt> including all of its parent directories (similar to <tt>&quot;mkdir -p&quot;</tt> on the command line &#8211; see <i><a href="/docs/linux/man/1-mkdir/">mkdir</a></i>(1) for more information). The argument <tt>&quot;mode&quot;</tt> specifies the permissions to use. It is modified by the process&#8217;s <tt>&quot;umask&quot;</tt>. See <i><a href="/docs/linux/man/2-mkdir/">mkdir</a></i>(2) for more details. </p>
<p> The function returns 0 on success, a negative value else. In case of an error, <tt>&quot;errno&quot;</tt> is set accordingly. Aside from the errors documented in <i><a href="/docs/linux/man/2-mkdir/">mkdir</a></i>(2), the function may fail with the following errors:</p>
<dl>
<dt>
<dd>
<dl>
<dt><font SIZE="-1"><code>EINVAL</code></font></p>
<dd> <tt>&quot;pathname&quot;</tt> is <tt>&quot;NULL&quot;</tt> or the empty string.</p>
<dt><font SIZE="-1"><code>ENOMEM</code></font></p>
<dd> Insufficient memory was available.</p>
<dt><code>any error returned by </code><a href="/docs/linux/man/2-stat/">stat</a><code>(2)</code></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd>
<p> In contrast to <i><a href="/docs/linux/man/2-mkdir/">mkdir</a></i>(2), the function does <code>not</code> fail if <tt>&quot;pathname&quot;</tt> already exists and is a directory.</dl>
</dl>
<h2>AUTHOR</h2>
<p> <font SIZE="-1">RRD</font> Contributors &lt;rrd-developers [at] lists.oetiker.ch&gt; </p>
<h2>Index</h2>

---
title: "intptr_t(3)"
name: "intptr_t"
section: "3"
letter: "i"
url: "/docs/linux/man/3-intptr_t/"
description: "system_data_types – overview of system data types"
---

<h2 class="name">NAME</h2>
<p> system_data_types &#8211; overview of system data types </p>
<h2>DESCRIPTION</h2>
<dl>
<dt><i>aiocb</i></p>
<dd>
<dl>
<dt>
<dd> <i>Include</i>: <i>&lt;aio.h&gt;</i>. </p>
<p> struct aiocb {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;aio_fildes;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;File descriptor&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;off_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;aio_offset;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;File offset&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;volatile void&nbsp;<wbr>&nbsp;*aio_buf;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Location of buffer&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;aio_nbytes;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Length of transfer&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;aio_reqprio;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Request priority offset&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct sigevent aio_sigevent;&nbsp;<wbr>&nbsp;/*&nbsp;Signal number and value&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;aio_lio_opcode;/*&nbsp;Operation to be performed&nbsp;*/ }; </p>
<p> For further information about this structure, see <code><a href="/docs/linux/man/7-aio/">aio</a></code>(7). </p>
<p> <i>Conforming to</i>: POSIX.1-2001 and later. </p>
<p> <i>See also</i>: <code><a href="/docs/linux/man/3-aio_cancel/">aio_cancel</a></code>(3), <code><a href="/docs/linux/man/3-aio_error/">aio_error</a></code>(3), <code><a href="/docs/linux/man/3-aio_fsync/">aio_fsync</a></code>(3), <code><a href="/docs/linux/man/3-aio_read/">aio_read</a></code>(3), <code><a href="/docs/linux/man/3-aio_return/">aio_return</a></code>(3), <code><a href="/docs/linux/man/3-aio_suspend/">aio_suspend</a></code>(3), <code><a href="/docs/linux/man/3-aio_write/">aio_write</a></code>(3), <code><a href="/docs/linux/man/3-lio_listio/">lio_listio</a></code>(3)</dl>
<dt><i>clock_t</i></p>
<dd>
<dl>
<dt>
<dd> <i>Include</i>: <i>&lt;time.h&gt;</i> or <i>&lt;sys/types.h&gt;</i>. Alternatively, <i>&lt;sys/time.h&gt;</i>. </p>
<p> Used for system time in clock ticks or <code>CLOCKS_PER_SEC</code> (defined in <i>&lt;time.h&gt;</i>). According to POSIX, it shall be an integer type or a real-floating type. </p>
<p> <i>Conforming to</i>: C99 and later; POSIX.1-2001 and later. </p>
<p> <i>See also</i>: <code><a href="/docs/linux/man/2-times/">times</a></code>(2), <code><a href="/docs/linux/man/3-clock/">clock</a></code>(3)</dl>
<dt><i>clockid_t</i></p>
<dd>
<dl>
<dt>
<dd> <i>Include</i>: <i>&lt;sys/types.h&gt;</i>. Alternatively, <i>&lt;time.h&gt;</i>. </p>
<p> Used for clock ID type in the clock and timer functions. According to POSIX, it shall be defined as an arithmetic type. </p>
<p> <i>Conforming to</i>: POSIX.1-2001 and later. </p>
<p> <i>See also</i>: <code><a href="/docs/linux/man/2-clock_adjtime/">clock_adjtime</a></code>(2), <code><a href="/docs/linux/man/2-clock_getres/">clock_getres</a></code>(2), <code><a href="/docs/linux/man/2-clock_nanosleep/">clock_nanosleep</a></code>(2), <code><a href="/docs/linux/man/2-timer_create/">timer_create</a></code>(2), <code><a href="/docs/linux/man/3-clock_getcpuclockid/">clock_getcpuclockid</a></code>(3)</dl>
<dt><i>dev_t</i></p>
<dd>
<dl>
<dt>
<dd> <i>Include</i>: <i>&lt;sys/types.h&gt;</i>. Alternatively, <i>&lt;sys/stat.h&gt;</i>. </p>
<p> Used for device IDs. According to POSIX, it shall be an integer type. For further details of this type, see <code><a href="/docs/linux/man/3-makedev/">makedev</a></code>(3). </p>
<p> <i>Conforming to</i>: POSIX.1-2001 and later. </p>
<p> <i>See also</i>: <code><a href="/docs/linux/man/2-mknod/">mknod</a></code>(2), <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2)</dl>
<dt><i>div_t</i></p>
<dd>
<dl>
<dt>
<dd> <i>Include</i>: <i>&lt;stdlib.h&gt;</i>. </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int quot;&nbsp;/*&nbsp;Quotient&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int rem;&nbsp;<wbr>&nbsp;/*&nbsp;Remainder&nbsp;*/ } div_t; </p>
<p> It is the type of the value returned by the <code><a href="/docs/linux/man/3-div/">div</a></code>(3) function. </p>
<p> <i>Conforming to</i>: C99 and later; POSIX.1-2001 and later. </p>
<p> <i>See also</i>: <code><a href="/docs/linux/man/3-div/">div</a></code>(3)</dl>
<dt><i>double_t</i></p>
<dd>
<dl>
<dt>
<dd> <i>Include</i>: <i>&lt;math.h&gt;</i>. </p>
<p> The implementation&#8217;s most efficient floating type at least as wide as <i>double</i>. Its type depends on the value of the macro <code>FLT_EVAL_METHOD</code> (defined in <i>&lt;float.h&gt;</i>):</p>
<dl>
<dt>0</p>
<dd> <i>double_t</i> is <i>double</i>.</p>
<dt>1</p>
<dd> <i>double_t</i> is <i>double</i>.</p>
<dt>2</p>
<dd> <i>double_t</i> is <i>long double</i>.</dl>
<p> For other values of <code>FLT_EVAL_METHOD</code>, the type of <i>double_t</i> is implementation-defined. </p>
<p> <i>Conforming to</i>: C99 and later; POSIX.1-2001 and later. </p>
<p> <i>See also</i>: the <i>float_t</i> type in this page.</dl>
<dt><i>fd_set</i></p>
<dd>
<dl>
<dt>
<dd> <i>Include</i>: <i>&lt;sys/select.h&gt;</i>. Alternatively, <i>&lt;sys/time.h&gt;</i>. </p>
<p> A structure type that can represent a set of file descriptors. According to POSIX, the maximum number of file descriptors in an <i>fd_set</i> structure is the value of the macro <code>FD_SETSIZE</code>. </p>
<p> <i>Conforming to</i>: POSIX.1-2001 and later. </p>
<p> <i>See also</i>: <code><a href="/docs/linux/man/2-select/">select</a></code>(2)</dl>
<dt><i>fenv_t</i></p>
<dd>
<dl>
<dt>
<dd> <i>Include</i>: <i>&lt;fenv.h&gt;</i>. </p>
<p> This type represents the entire floating-point environment, including control modes and status flags; for further details, see <code><a href="/docs/linux/man/3-fenv/">fenv</a></code>(3). </p>
<p> <i>Conforming to</i>: C99 and later; POSIX.1-2001 and later. </p>
<p> <i>See also</i>: <code><a href="/docs/linux/man/3-fenv/">fenv</a></code>(3)</dl>
<dt><i>fexcept_t</i></p>
<dd>
<dl>
<dt>
<dd> <i>Include</i>: <i>&lt;fenv.h&gt;</i>. </p>
<p> This type represents the floating-point status flags collectively; for further details see <code><a href="/docs/linux/man/3-fenv/">fenv</a></code>(3). </p>
<p> <i>Conforming to</i>: C99 and later; POSIX.1-2001 and later. </p>
<p> <i>See also</i>: <code><a href="/docs/linux/man/3-fenv/">fenv</a></code>(3)</dl>
<dt><i>FILE</i></p>
<dd>
<dl>
<dt>
<dd> <i>Include</i>: <i>&lt;stdio.h&gt;</i>. Alternatively, <i>&lt;wchar.h&gt;</i>. </p>
<p> An object type used for streams. </p>
<p> <i>Conforming to</i>: C99 and later; POSIX.1-2001 and later. </p>
<p> <i>See also</i>: <code><a href="/docs/linux/man/3-fclose/">fclose</a></code>(3), <code><a href="/docs/linux/man/3-flockfile/">flockfile</a></code>(3), <code><a href="/docs/linux/man/3-fopen/">fopen</a></code>(3), <code><a href="/docs/linux/man/3-fprintf/">fprintf</a></code>(3), <code><a href="/docs/linux/man/3-fread/">fread</a></code>(3), <code><a href="/docs/linux/man/3-fscanf/">fscanf</a></code>(3), <code><a href="/docs/linux/man/3-stdin/">stdin</a></code>(3), <code><a href="/docs/linux/man/3-stdio/">stdio</a></code>(3)</dl>
<dt><i>float_t</i></p>
<dd>
<dl>
<dt>
<dd> <i>Include</i>: <i>&lt;math.h&gt;</i>. </p>
<p> The implementation&#8217;s most efficient floating type at least as wide as <i>float</i>. Its type depends on the value of the macro <code>FLT_EVAL_METHOD</code> (defined in <i>&lt;float.h&gt;</i>):</p>
<dl>
<dt>0</p>
<dd> <i>float_t</i> is <i>float</i>.</p>
<dt>1</p>
<dd> <i>float_t</i> is <i>double</i>.</p>
<dt>2</p>
<dd> <i>float_t</i> is <i>long double</i>.</dl>
<p> For other values of <code>FLT_EVAL_METHOD</code>, the type of <i>float_t</i> is implementation-defined. </p>
<p> <i>Conforming to</i>: C99 and later; POSIX.1-2001 and later. </p>
<p> <i>See also</i>: the <i>double_t</i> type in this page.</dl>
<dt><i>gid_t</i></p>
<dd>
<dl>
<dt>
<dd> <i>Include</i>: <i>&lt;sys/types.h&gt;</i>. Alternatively, <i>&lt;grp.h&gt;</i>, <i>&lt;pwd.h&gt;</i>, <i>&lt;signal.h&gt;</i>, <i>&lt;stropts.h&gt;</i>, <i>&lt;sys/ipc.h&gt;</i>, <i>&lt;sys/stat.h&gt;</i>, or <i>&lt;unistd.h&gt;</i>. </p>
<p> A type used to hold group IDs. According to POSIX, this shall be an integer type. </p>
<p> <i>Conforming to</i>: POSIX.1-2001 and later. </p>
<p> <i>See also</i>: <code><a href="/docs/linux/man/2-chown/">chown</a></code>(2), <code><a href="/docs/linux/man/2-getgid/">getgid</a></code>(2), <code><a href="/docs/linux/man/2-getegid/">getegid</a></code>(2), <code><a href="/docs/linux/man/2-getgroups/">getgroups</a></code>(2), <code><a href="/docs/linux/man/2-getresgid/">getresgid</a></code>(2), <code><a href="/docs/linux/man/2-getgrnam/">getgrnam</a></code>(2), <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7)</dl>
<dt><i>id_t</i></p>
<dd>
<dl>
<dt>
<dd> <i>Include</i>: <i>&lt;sys/types.h&gt;</i>. Alternatively, <i>&lt;sys/resource.h&gt;</i>. </p>
<p> A type used to hold a general identifier. According to POSIX, this shall be an integer type that can be used to contain a <i>pid_t</i>, <i>uid_t</i>, or <i>gid_t</i>. </p>
<p> <i>Conforming to</i>: POSIX.1-2001 and later. </p>
<p> <i>See also</i>: <code><a href="/docs/linux/man/2-getpriority/">getpriority</a></code>(2), <code><a href="/docs/linux/man/2-waitid/">waitid</a></code>(2)</dl>
<dt><i>imaxdiv_t</i></p>
<dd>
<dl>
<dt>
<dd> <i>Include</i>: <i>&lt;inttypes.h&gt;</i>. </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;intmax_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;quot;&nbsp;/*&nbsp;Quotient&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;intmax_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;rem;&nbsp;<wbr>&nbsp;/*&nbsp;Remainder&nbsp;*/ } imaxdiv_t; </p>
<p> It is the type of the value returned by the <code><a href="/docs/linux/man/3-imaxdiv/">imaxdiv</a></code>(3) function. </p>
<p> <i>Conforming to</i>: C99 and later; POSIX.1-2001 and later. </p>
<p> <i>See also</i>: <code><a href="/docs/linux/man/3-imaxdiv/">imaxdiv</a></code>(3)</dl>
<dt><i>intmax_t</i></p>
<dd>
<dl>
<dt>
<dd> <i>Include</i>: <i>&lt;stdint.h&gt;</i>. Alternatively, <i>&lt;inttypes.h&gt;</i>. </p>
<p> A signed integer type capable of representing any value of any signed integer type supported by the implementation. According to the C language standard, it shall be capable of storing values in the range [<code>INTMAX_MIN</code>, <code>INTMAX_MAX</code>]. </p>
<p> The macro <code>INTMAX_C</code>() expands its argument to an integer constant of type <i>intmax_t</i>. </p>
<p> The length modifier for <i>intmax_t</i> for the <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3) and the <code><a href="/docs/linux/man/3-scanf/">scanf</a></code>(3) families of functions is <code>j</code>; resulting commonly in <code>%jd</code> or <code>%ji</code> for printing <i>intmax_t</i> values. </p>
<p> <i>Conforming to</i>: C99 and later; POSIX.1-2001 and later. </p>
<p> <i>Bugs</i>: <i>intmax_t</i> is not large enough to represent values of type <i>__int128</i> in implementations where <i>__int128</i> is defined and <i>long long</i> is less than 128 bits wide. </p>
<p> <i>See also</i>: the <i>uintmax_t</i> type in this page.</dl>
<dt><i>int</i>N<i>_t</i></p>
<dd>
<dl>
<dt>
<dd> <i>Include</i>: <i>&lt;stdint.h&gt;</i>. Alternatively, <i>&lt;inttypes.h&gt;</i>. </p>
<p> <i>int8_t</i>, <i>int16_t</i>, <i>int32_t</i>, <i>int64_t</i> </p>
<p> A signed integer type of a fixed width of exactly N bits, N being the value specified in its type name. According to the C language standard, they shall be capable of storing values in the range [<code>INT</code>N<code>_MIN</code>, <code>INT</code>N<code>_MAX</code>], substituting N by the appropriate number. </p>
<p> According to POSIX, <i>int8_t</i>, <i>int16_t</i>, and <i>int32_t</i> are required; <i>int64_t</i> is only required in implementations that provide integer types with width 64; and all other types of this form are optional. </p>
<p> The length modifiers for the <i>int</i>N<i>_t</i> types for the <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3) family of functions are expanded by macros of the forms <code>PRId</code>N and <code>PRIi</code>N (defined in <i>&lt;inttypes.h&gt;</i>); resulting for example in <code>%PRId64</code> or <code>%PRIi64</code> for printing <i>int64_t</i> values. The length modifiers for the <i>int</i>N<i>_t</i> types for the <code><a href="/docs/linux/man/3-scanf/">scanf</a></code>(3) family of functions are expanded by macros of the forms <code>SCNd</code>N and <code>SCNi</code>N, (defined in <i>&lt;inttypes.h&gt;</i>); resulting for example in <code>%SCNd8</code> or <code>%SCNi8</code> for scanning <i>int8_t</i> values. </p>
<p> <i>Conforming to</i>: C99 and later; POSIX.1-2001 and later. </p>
<p> <i>See also</i>: the <i>intmax_t</i>, <i>uint</i>N<i>_t</i>, and <i>uintmax_t</i> types in this page.</dl>
<dt><i>intptr_t</i></p>
<dd>
<dl>
<dt>
<dd> <i>Include</i>: <i>&lt;stdint.h&gt;</i>. Alternatively, <i>&lt;inttypes.h&gt;</i>. </p>
<p> A signed integer type such that any valid (<i>void *</i>) value can be converted to this type and back. According to the C language standard, it shall be capable of storing values in the range [<code>INTPTR_MIN</code>, <code>INTPTR_MAX</code>]. </p>
<p> The length modifier for <i>intptr_t</i> for the <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3) family of functions is expanded by the macros <code>PRIdPTR</code> and <code>PRIiPTR</code> (defined in <i>&lt;inttypes.h&gt;</i>); resulting commonly in <code>%PRIdPTR</code> or <code>%PRIiPTR</code> for printing <i>intptr_t</i> values. The length modifier for <i>intptr_t</i> for the <code><a href="/docs/linux/man/3-scanf/">scanf</a></code>(3) family of functions is expanded by the macros <code>SCNdPTR</code> and <code>SCNiPTR,</code> (defined in <i>&lt;inttypes.h&gt;</i>); resulting commonly in <code>%SCNdPTR</code> or <code>%SCNiPTR</code> for scanning <i>intptr_t</i> values. </p>
<p> <i>Conforming to</i>: C99 and later; POSIX.1-2001 and later. </p>
<p> <i>See also</i>: the <i>uintptr_t</i> and <i>void *</i> types in this page.</dl>
<dt><i>lconv</i></p>
<dd>
<dl>
<dt>
<dd> <i>Include</i>: <i>&lt;locale.h&gt;</i>. </p>
<p> struct lconv { /* Values in the &quot;C&quot; locale: */<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;*decimal_point;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;&quot;.&quot;&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;*thousands_sep;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;&quot;&quot;&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;*grouping;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;&quot;&quot;&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;*mon_decimal_point;&nbsp;<wbr>&nbsp;/*&nbsp;&quot;&quot;&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;*mon_thousands_sep;&nbsp;<wbr>&nbsp;/*&nbsp;&quot;&quot;&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;*mon_grouping;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;&quot;&quot;&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;*positive_sign;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;&quot;&quot;&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;*negative_sign;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;&quot;&quot;&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;*currency_symbol;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;&quot;&quot;&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;frac_digits;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;CHAR_MAX&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;p_cs_precedes;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;CHAR_MAX&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;n_cs_precedes;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;CHAR_MAX&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;p_sep_by_space;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;CHAR_MAX&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;n_sep_by_space;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;CHAR_MAX&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;p_sign_posn;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;CHAR_MAX&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;n_sign_posn;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;CHAR_MAX&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;*int_curr_symbol;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;&quot;&quot;&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int_frac_digits;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;CHAR_MAX&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int_p_cs_precedes;&nbsp;<wbr>&nbsp;/*&nbsp;CHAR_MAX&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int_n_cs_precedes;&nbsp;<wbr>&nbsp;/*&nbsp;CHAR_MAX&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int_p_sep_by_space;&nbsp;/*&nbsp;CHAR_MAX&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int_n_sep_by_space;&nbsp;/*&nbsp;CHAR_MAX&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int_p_sign_posn;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;CHAR_MAX&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int_n_sign_posn;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;CHAR_MAX&nbsp;*/ }; </p>
<p> Contains members related to the formatting of numeric values. In the &quot;C&quot; locale, its members have the values shown in the comments above. </p>
<p> <i>Conforming to</i>: C11 and later; POSIX.1-2001 and later. </p>
<p> <i>See also</i>: <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3), <code><a href="/docs/linux/man/3-localeconv/">localeconv</a></code>(3), <code><a href="/docs/linux/man/5-charsets/">charsets</a></code>(5), <code><a href="/docs/linux/man/7-locale/">locale</a></code>(7)</dl>
<dt><i>ldiv_t</i></p>
<dd>
<dl>
<dt>
<dd> <i>Include</i>: <i>&lt;stdlib.h&gt;</i>. </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;quot;&nbsp;/*&nbsp;Quotient&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;rem;&nbsp;<wbr>&nbsp;/*&nbsp;Remainder&nbsp;*/ } ldiv_t; </p>
<p> It is the type of the value returned by the <code><a href="/docs/linux/man/3-ldiv/">ldiv</a></code>(3) function. </p>
<p> <i>Conforming to</i>: C99 and later; POSIX.1-2001 and later. </p>
<p> <i>See also</i>: <code><a href="/docs/linux/man/3-ldiv/">ldiv</a></code>(3)</dl>
<dt><i>lldiv_t</i></p>
<dd>
<dl>
<dt>
<dd> <i>Include</i>: <i>&lt;stdlib.h&gt;</i>. </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long long&nbsp;<wbr>&nbsp;<wbr>&nbsp;quot;&nbsp;/*&nbsp;Quotient&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long long&nbsp;<wbr>&nbsp;<wbr>&nbsp;rem;&nbsp;<wbr>&nbsp;/*&nbsp;Remainder&nbsp;*/ } lldiv_t; </p>
<p> It is the type of the value returned by the <code><a href="/docs/linux/man/3-lldiv/">lldiv</a></code>(3) function. </p>
<p> <i>Conforming to</i>: C99 and later; POSIX.1-2001 and later. </p>
<p> <i>See also</i>: <code><a href="/docs/linux/man/3-lldiv/">lldiv</a></code>(3)</dl>
<dt><i>off_t</i></p>
<dd>
<dl>
<dt>
<dd> <i>Include</i>: <i>&lt;sys/types.h&gt;</i>. Alternatively, <i>&lt;aio.h&gt;</i>, <i>&lt;fcntl.h&gt;</i>, <i>&lt;stdio.h&gt;</i>, <i>&lt;sys/mman.h&gt;</i>, <i>&lt;sys/stat.h.h&gt;</i>, or <i>&lt;unistd.h&gt;</i>. </p>
<p> Used for file sizes. According to POSIX, this shall be a signed integer type. </p>
<p> <i>Versions</i>: <i>&lt;aio.h&gt;</i> and <i>&lt;stdio.h&gt;</i> define <i>off_t</i> since POSIX.1-2008. </p>
<p> <i>Conforming to</i>: POSIX.1-2001 and later. </p>
<p> <i>Notes</i>: On some architectures, the width of this type can be controlled with the feature test macro <code>_FILE_OFFSET_BITS</code>. </p>
<p> <i>See also</i>: <code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2), <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/2-posix_fadvise/">posix_fadvise</a></code>(2), <code><a href="/docs/linux/man/2-pread/">pread</a></code>(2), <code><a href="/docs/linux/man/2-truncate/">truncate</a></code>(2), <code><a href="/docs/linux/man/3-fseeko/">fseeko</a></code>(3), <code><a href="/docs/linux/man/3-lockf/">lockf</a></code>(3), <code><a href="/docs/linux/man/3-posix_fallocate/">posix_fallocate</a></code>(3), <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)</dl>
<dt><i>pid_t</i></p>
<dd>
<dl>
<dt>
<dd> <i>Include</i>: <i>&lt;sys/types.h&gt;</i>. Alternatively, <i>&lt;fcntl.h&gt;</i>, <i>&lt;sched.h&gt;</i>, <i>&lt;signal.h&gt;</i>, <i>&lt;spawn.h&gt;</i>, <i>&lt;sys/msg.h&gt;</i>, <i>&lt;sys/sem.h&gt;</i>, <i>&lt;sys/shm.h&gt;</i>, <i>&lt;sys/wait.h&gt;</i>, <i>&lt;termios.h&gt;</i>, <i>&lt;time.h&gt;</i>, <i>&lt;unistd.h&gt;</i>, or <i>&lt;utmpx.h&gt;</i>. </p>
<p> This type is used for storing process IDs, process group IDs, and session IDs. According to POSIX, it shall be a signed integer type, and the implementation shall support one or more programming environments where the width of <i>pid_t</i> is no greater than the width of the type <i>long</i>. </p>
<p> <i>Conforming to</i>: POSIX.1-2001 and later. </p>
<p> <i>See also</i>: <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), <code><a href="/docs/linux/man/2-getpid/">getpid</a></code>(2), <code><a href="/docs/linux/man/2-getppid/">getppid</a></code>(2), <code><a href="/docs/linux/man/2-getsid/">getsid</a></code>(2), <code><a href="/docs/linux/man/2-gettid/">gettid</a></code>(2), <code><a href="/docs/linux/man/2-getpgid/">getpgid</a></code>(2), <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2), <code><a href="/docs/linux/man/2-pidfd_open/">pidfd_open</a></code>(2), <code><a href="/docs/linux/man/2-sched_setscheduler/">sched_setscheduler</a></code>(2), <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2), <code><a href="/docs/linux/man/3-sigqueue/">sigqueue</a></code>(3), <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7),</dl>
<dt><i>ptrdiff_t</i></p>
<dd>
<dl>
<dt>
<dd> <i>Include</i>: <i>&lt;stddef.h&gt;</i>. </p>
<p> Used for a count of elements, and array indices. It is the result of subtracting two pointers. According to the C language standard, it shall be a signed integer type capable of storing values in the range [<code>PTRDIFF_MIN</code>, <code>PTRDIFF_MAX</code>]. </p>
<p> The length modifier for <i>ptrdiff_t</i> for the <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3) and the <code><a href="/docs/linux/man/3-scanf/">scanf</a></code>(3) families of functions is <code>t</code>; resulting commonly in <code>%td</code> or <code>%ti</code> for printing <i>ptrdiff_t</i> values. </p>
<p> <i>Conforming to</i>: C99 and later; POSIX.1-2001 and later. </p>
<p> <i>See also</i>: the <i>size_t</i> and <i>ssize_t</i> types in this page.</dl>
<dt><i>regex_t</i></p>
<dd>
<dl>
<dt>
<dd> <i>Include</i>: <i>&lt;regex.h&gt;</i>. </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t&nbsp;<wbr>&nbsp;re_nsub;&nbsp;/*&nbsp;Number of parenthesized subexpressions.&nbsp;*/ } regex_t; </p>
<p> This is a structure type used in regular expression matching. It holds a compiled regular expression, compiled with <code><a href="/docs/linux/man/3-regcomp/">regcomp</a></code>(3). </p>
<p> <i>Conforming to</i>: POSIX.1-2001 and later. </p>
<p> <i>See also</i>: <code><a href="/docs/linux/man/3-regex/">regex</a></code>(3)</dl>
<dt><i>regmatch_t</i></p>
<dd>
<dl>
<dt>
<dd> <i>Include</i>: <i>&lt;regex.h&gt;</i>. </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;regoff_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;rm_so;&nbsp;/*&nbsp;Byte offset from start of string<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;to start of substring&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;regoff_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;rm_eo;&nbsp;/*&nbsp;Byte offset from start of string of<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the first character after the end of<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;substring&nbsp;*/ } regmatch_t; </p>
<p> This is a structure type used in regular expression matching. </p>
<p> <i>Conforming to</i>: POSIX.1-2001 and later. </p>
<p> <i>See also</i>: <code><a href="/docs/linux/man/3-regexec/">regexec</a></code>(3)</dl>
<dt><i>regoff_t</i></p>
<dd>
<dl>
<dt>
<dd> <i>Include</i>: <i>&lt;regex.h&gt;</i>. </p>
<p> According to POSIX, it shall be a signed integer type capable of storing the largest value that can be stored in either a <i>ptrdiff_t</i> type or a <i>ssize_t</i> type. </p>
<p> <i>Versions</i>: Prior to POSIX.1-2008, the type was capable of storing the largest value that can be stored in either an <i>off_t</i> type or a <i>ssize_t</i> type. </p>
<p> <i>Conforming to</i>: POSIX.1-2001 and later. </p>
<p> <i>See also</i>: the <i>regmatch_t</i> structure and the <i>ptrdiff_t</i> and <i>ssize_t</i> types in this page.</dl>
<dt><i>sigevent</i></p>
<dd>
<dl>
<dt>
<dd> <i>Include</i>: <i>&lt;signal.h&gt;</i>. Alternatively, <i>&lt;aio.h&gt;</i>, <i>&lt;mqueue.h&gt;</i>, or <i>&lt;time.h&gt;</i>. </p>
<p> struct sigevent {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sigev_notify;&nbsp;/*&nbsp;Notification type&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sigev_signo;&nbsp;<wbr>&nbsp;/*&nbsp;Signal number&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;union sigval&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sigev_value;&nbsp;<wbr>&nbsp;/*&nbsp;Signal value&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(*sigev_notify_function)(union sigval);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Notification function&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pthread_attr_t&nbsp;*sigev_notify_attributes;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Notification attributes&nbsp;*/ }; </p>
<p> For further details about this type, see <code><a href="/docs/linux/man/7-sigevent/">sigevent</a></code>(7). </p>
<p> <i>Versions</i>: <i>&lt;aio.h&gt;</i> and <i>&lt;time.h&gt;</i> define <i>sigevent</i> since POSIX.1-2008. </p>
<p> <i>Conforming to</i>: POSIX.1-2001 and later. </p>
<p> <i>See also</i>: <code><a href="/docs/linux/man/2-timer_create/">timer_create</a></code>(2), <code><a href="/docs/linux/man/3-getaddrinfo_a/">getaddrinfo_a</a></code>(3), <code><a href="/docs/linux/man/3-lio_listio/">lio_listio</a></code>(3), <code><a href="/docs/linux/man/3-mq_notify/">mq_notify</a></code>(3) </p>
<p> See also the <i>aiocb</i> structure in this page.</dl>
<dt><i>siginfo_t</i></p>
<dd>
<dl>
<dt>
<dd> <i>Include</i>: <i>&lt;signal.h&gt;</i>. Alternatively, <i>&lt;sys/wait.h&gt;</i>. </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;si_signo;&nbsp;<wbr>&nbsp;/*&nbsp;Signal number&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;si_code;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Signal code&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pid_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;si_pid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Sending process ID&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uid_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;si_uid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Real user ID of sending process&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*si_addr;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Address of faulting instruction&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;si_status;&nbsp;/*&nbsp;Exit value or signal&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;union sigval si_value;&nbsp;<wbr>&nbsp;/*&nbsp;Signal value&nbsp;*/ } siginfo_t; </p>
<p> Information associated with a signal. For further details on this structure (including additional, Linux-specific fields), see <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2). </p>
<p> <i>Conforming to</i>: POSIX.1-2001 and later. </p>
<p> <i>See also</i>: <code><a href="/docs/linux/man/2-pidfd_send_signal/">pidfd_send_signal</a></code>(2), <code><a href="/docs/linux/man/2-rt_sigqueueinfo/">rt_sigqueueinfo</a></code>(2), <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/2-sigwaitinfo/">sigwaitinfo</a></code>(2), <code><a href="/docs/linux/man/3-psiginfo/">psiginfo</a></code>(3)</dl>
<dt><i>sigset_t</i></p>
<dd>
<dl>
<dt>
<dd> <i>Include</i>: <i>&lt;signal.h&gt;</i>. Alternatively, <i>&lt;spawn.h&gt;</i>, or <i>&lt;sys/select.h&gt;</i>. </p>
<p> This is a type that represents a set of signals. According to POSIX, this shall be an integer or structure type. </p>
<p> <i>Conforming to</i>: POSIX.1-2001 and later. </p>
<p> <i>See also</i>: <code><a href="/docs/linux/man/2-epoll_pwait/">epoll_pwait</a></code>(2), <code><a href="/docs/linux/man/2-ppoll/">ppoll</a></code>(2), <code><a href="/docs/linux/man/2-pselect/">pselect</a></code>(2), <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/2-signalfd/">signalfd</a></code>(2), <code><a href="/docs/linux/man/2-sigpending/">sigpending</a></code>(2), <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2), <code><a href="/docs/linux/man/2-sigsuspend/">sigsuspend</a></code>(2), <code><a href="/docs/linux/man/2-sigwaitinfo/">sigwaitinfo</a></code>(2), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)</dl>
<dt><i>sigval</i></p>
<dd>
<dl>
<dt>
<dd> <i>Include</i>: <i>&lt;signal.h&gt;</i>. </p>
<p> union sigval {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sigval_int;&nbsp;/*&nbsp;Integer value&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;<wbr>&nbsp;<wbr>&nbsp;*sigval_ptr;&nbsp;/*&nbsp;Pointer value&nbsp;*/ }; </p>
<p> Data passed with a signal. </p>
<p> <i>Conforming to</i>: POSIX.1-2001 and later. </p>
<p> <i>See also</i>: <code><a href="/docs/linux/man/3-pthread_sigqueue/">pthread_sigqueue</a></code>(3), <code><a href="/docs/linux/man/3-sigqueue/">sigqueue</a></code>(3), <code><a href="/docs/linux/man/7-sigevent/">sigevent</a></code>(7) </p>
<p> See also the <i>sigevent</i> structure and the <i>siginfo_t</i> type in this page.</dl>
<dt><i>size_t</i></p>
<dd>
<dl>
<dt>
<dd> <i>Include</i>: <i>&lt;stddef.h&gt;</i> or <i>&lt;sys/types.h&gt;</i>. Alternatively, <i>&lt;aio.h&gt;</i>, <i>&lt;glob.h&gt;</i>, <i>&lt;grp.h&gt;</i>, <i>&lt;iconv.h&gt;</i>, <i>&lt;monetary.h&gt;</i>, <i>&lt;mqueue.h&gt;</i>, <i>&lt;ndbm.h&gt;</i>, <i>&lt;pwd.h&gt;</i>, <i>&lt;regex.h&gt;</i>, <i>&lt;search.h&gt;</i>, <i>&lt;signal.h&gt;</i>, <i>&lt;stdio.h&gt;</i>, <i>&lt;stdlib.h&gt;</i>, <i>&lt;string.h&gt;</i>, <i>&lt;strings.h&gt;</i>, <i>&lt;sys/mman.h&gt;</i>, <i>&lt;sys/msg.h&gt;</i>, <i>&lt;sys/sem.h&gt;</i>, <i>&lt;sys/shm.h&gt;</i>, <i>&lt;sys/socket.h&gt;</i>, <i>&lt;sys/uio.h&gt;</i>, <i>&lt;time.h&gt;</i>, <i>&lt;unistd.h&gt;</i>, <i>&lt;wchar.h&gt;</i>, or <i>&lt;wordexp.h&gt;</i>. </p>
<p> Used for a count of bytes. It is the result of the <i>sizeof</i> operator. According to the C language standard, it shall be an unsigned integer type capable of storing values in the range [0, <code>SIZE_MAX</code>]. According to POSIX, the implementation shall support one or more programming environments where the width of <i>size_t</i> is no greater than the width of the type <i>long</i>. </p>
<p> The length modifier for <i>size_t</i> for the <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3) and the <code><a href="/docs/linux/man/3-scanf/">scanf</a></code>(3) families of functions is <code>z</code>; resulting commonly in <code>%zu</code> or <code>%zx</code> for printing <i>size_t</i> values. </p>
<p> <i>Versions</i>: <i>&lt;aio.h&gt;</i>, <i>&lt;glob.h&gt;</i>, <i>&lt;grp.h&gt;</i>, <i>&lt;iconv.h&gt;</i>, <i>&lt;mqueue.h&gt;</i>, <i>&lt;pwd.h&gt;</i>, <i>&lt;signal.h&gt;</i>, and <i>&lt;sys/socket.h&gt;</i> define <i>size_t</i> since POSIX.1-2008. </p>
<p> <i>Conforming to</i>: C99 and later; POSIX.1-2001 and later. </p>
<p> <i>See also</i>: <code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/2-write/">write</a></code>(2), <code><a href="/docs/linux/man/3-fread/">fread</a></code>(3), <code><a href="/docs/linux/man/3-fwrite/">fwrite</a></code>(3), <code><a href="/docs/linux/man/3-memcmp/">memcmp</a></code>(3), <code><a href="/docs/linux/man/3-memcpy/">memcpy</a></code>(3), <code><a href="/docs/linux/man/3-memset/">memset</a></code>(3), <code><a href="/docs/linux/man/3-offsetof/">offsetof</a></code>(3) </p>
<p> See also the <i>ptrdiff_t</i> and <i>ssize_t</i> types in this page.</dl>
<dt><i>ssize_t</i></p>
<dd>
<dl>
<dt>
<dd> <i>Include</i>: <i>&lt;sys/types.h&gt;</i>. Alternatively, <i>&lt;aio.h&gt;</i>, <i>&lt;monetary.h&gt;</i>, <i>&lt;mqueue.h&gt;</i>, <i>&lt;stdio.h&gt;</i>, <i>&lt;sys/msg.h&gt;</i>, <i>&lt;sys/socket.h&gt;</i>, <i>&lt;sys/uio.h&gt;</i>, or <i>&lt;unistd.h&gt;</i>. </p>
<p> Used for a count of bytes or an error indication. According to POSIX, it shall be a signed integer type capable of storing values at least in the range [-1, <code>SSIZE_MAX</code>], and the implementation shall support one or more programming environments where the width of <i>ssize_t</i> is no greater than the width of the type <i>long</i>. </p>
<p> Glibc and most other implementations provide a length modifier for <i>ssize_t</i> for the <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3) and the <code><a href="/docs/linux/man/3-scanf/">scanf</a></code>(3) families of functions, which is <code>z</code>; resulting commonly in <code>%zd</code> or <code>%zi</code> for printing <i>ssize_t</i> values. Although <code>z</code> works for <i>ssize_t</i> on most implementations, portable POSIX programs should avoid using it&#8212;for example, by converting the value to <i>intmax_t</i> and using its length modifier (<code>j</code>). </p>
<p> <i>Conforming to</i>: POSIX.1-2001 and later. </p>
<p> <i>See also</i>: <code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/2-readlink/">readlink</a></code>(2), <code><a href="/docs/linux/man/2-readv/">readv</a></code>(2), <code><a href="/docs/linux/man/2-recv/">recv</a></code>(2), <code><a href="/docs/linux/man/2-send/">send</a></code>(2), <code><a href="/docs/linux/man/2-write/">write</a></code>(2) </p>
<p> See also the <i>ptrdiff_t</i> and <i>size_t</i> types in this page.</dl>
<dt><i>suseconds_t</i></p>
<dd>
<dl>
<dt>
<dd> <i>Include</i>: <i>&lt;sys/types.h&gt;</i>. Alternatively, <i>&lt;sys/select.h&gt;</i>, or <i>&lt;sys/time.h&gt;</i>. </p>
<p> Used for time in microseconds. According to POSIX, it shall be a signed integer type capable of storing values at least in the range [-1, 1000000], and the implementation shall support one or more programming environments where the width of <i>suseconds_t</i> is no greater than the width of the type <i>long</i>. </p>
<p> <i>Conforming to</i>: POSIX.1-2001 and later. </p>
<p> <i>See also</i>: the <i>timeval</i> structure in this page.</dl>
<dt><i>time_t</i></p>
<dd>
<dl>
<dt>
<dd> <i>Include</i>: <i>&lt;time.h&gt;</i> or <i>&lt;sys/types.h&gt;</i>. Alternatively, <i>&lt;sched.h&gt;</i>, <i>&lt;sys/msg.h&gt;</i>, <i>&lt;sys/select.h&gt;</i>, <i>&lt;sys/sem.h&gt;</i>, <i>&lt;sys/shm.h&gt;</i>, <i>&lt;sys/stat.h&gt;</i>, <i>&lt;sys/time.h&gt;</i>, or <i>&lt;utime.h&gt;</i>. </p>
<p> Used for time in seconds. According to POSIX, it shall be an integer type. </p>
<p> <i>Versions</i>: <i>&lt;sched.h&gt;</i> defines <i>time_t</i> since POSIX.1-2008. </p>
<p> <i>Conforming to</i>: C99 and later; POSIX.1-2001 and later. </p>
<p> <i>See also</i>: <code><a href="/docs/linux/man/2-stime/">stime</a></code>(2), <code><a href="/docs/linux/man/2-time/">time</a></code>(2), <code><a href="/docs/linux/man/3-ctime/">ctime</a></code>(3), <code><a href="/docs/linux/man/3-difftime/">difftime</a></code>(3)</dl>
<dt><i>timer_t</i></p>
<dd>
<dl>
<dt>
<dd> <i>Include</i>: <i>&lt;sys/types.h&gt;</i>. Alternatively, <i>&lt;time.h&gt;</i>. </p>
<p> Used for timer ID returned by <code><a href="/docs/linux/man/2-timer_create/">timer_create</a></code>(2). According to POSIX, there are no defined comparison or assignment operators for this type. </p>
<p> <i>Conforming to</i>: POSIX.1-2001 and later. </p>
<p> <i>See also</i>: <code><a href="/docs/linux/man/2-timer_create/">timer_create</a></code>(2), <code><a href="/docs/linux/man/2-timer_delete/">timer_delete</a></code>(2), <code><a href="/docs/linux/man/2-timer_getoverrun/">timer_getoverrun</a></code>(2), <code><a href="/docs/linux/man/2-timer_settime/">timer_settime</a></code>(2)</dl>
<dt><i>timespec</i></p>
<dd>
<dl>
<dt>
<dd> <i>Include</i>: <i>&lt;time.h&gt;</i>. Alternatively, <i>&lt;aio.h&gt;</i>, <i>&lt;mqueue.h&gt;</i>, <i>&lt;sched.h&gt;</i>, <i>&lt;signal.h&gt;</i>, <i>&lt;sys/select.h&gt;</i>, or <i>&lt;sys/stat.h&gt;</i>. </p>
<p> struct timespec {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_t&nbsp;<wbr>&nbsp;tv_sec;&nbsp;<wbr>&nbsp;/*&nbsp;Seconds&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tv_nsec;&nbsp;/*&nbsp;Nanoseconds&nbsp;*/ }; </p>
<p> Describes times in seconds and nanoseconds. </p>
<p> <i>Conforming to</i>: C11 and later; POSIX.1-2001 and later. </p>
<p> <i>See also</i>: <code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2), <code><a href="/docs/linux/man/2-clock_nanosleep/">clock_nanosleep</a></code>(2), <code><a href="/docs/linux/man/2-nanosleep/">nanosleep</a></code>(2), <code><a href="/docs/linux/man/2-timerfd_gettime/">timerfd_gettime</a></code>(2), <code><a href="/docs/linux/man/2-timer_gettime/">timer_gettime</a></code>(2)</dl>
<dt><i>timeval</i></p>
<dd>
<dl>
<dt>
<dd> <i>Include</i>: <i>&lt;sys/time.h&gt;</i>. Alternatively, <i>&lt;sys/resource.h&gt;</i>, <i>&lt;sys/select.h&gt;</i>, or <i>&lt;utmpx.h&gt;</i>. </p>
<p> struct timeval {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tv_sec;&nbsp;<wbr>&nbsp;/*&nbsp;Seconds&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;suseconds_t tv_usec;&nbsp;/*&nbsp;Microseconds&nbsp;*/ }; </p>
<p> Describes times in seconds and microseconds. </p>
<p> <i>Conforming to</i>: POSIX.1-2001 and later. </p>
<p> <i>See also</i>: <code><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a></code>(2), <code><a href="/docs/linux/man/2-select/">select</a></code>(2), <code><a href="/docs/linux/man/2-utimes/">utimes</a></code>(2), <code><a href="/docs/linux/man/3-adjtime/">adjtime</a></code>(3), <code><a href="/docs/linux/man/3-futimes/">futimes</a></code>(3), <code><a href="/docs/linux/man/3-timeradd/">timeradd</a></code>(3)</dl>
<dt><i>uid_t</i></p>
<dd>
<dl>
<dt>
<dd> <i>Include</i>: <i>&lt;sys/types.h&gt;</i>. Alternatively, <i>&lt;pwd.h&gt;</i>, <i>&lt;signal.h&gt;</i>, <i>&lt;stropts.h&gt;</i>, <i>&lt;sys/ipc.h&gt;</i>, <i>&lt;sys/stat.h&gt;</i>, or <i>&lt;unistd.h&gt;</i>. </p>
<p> A type used to hold user IDs. According to POSIX, this shall be an integer type. </p>
<p> <i>Conforming to</i>: POSIX.1-2001 and later. </p>
<p> <i>See also</i>: <code><a href="/docs/linux/man/2-chown/">chown</a></code>(2), <code><a href="/docs/linux/man/2-getuid/">getuid</a></code>(2), <code><a href="/docs/linux/man/2-geteuid/">geteuid</a></code>(2), <code><a href="/docs/linux/man/2-getresuid/">getresuid</a></code>(2), <code><a href="/docs/linux/man/2-getpwnam/">getpwnam</a></code>(2), <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7)</dl>
<dt><i>uintmax_t</i></p>
<dd>
<dl>
<dt>
<dd> <i>Include</i>: <i>&lt;stdint.h&gt;</i>. Alternatively, <i>&lt;inttypes.h&gt;</i>. </p>
<p> An unsigned integer type capable of representing any value of any unsigned integer type supported by the implementation. According to the C language standard, it shall be capable of storing values in the range [0, <code>UINTMAX_MAX</code>]. </p>
<p> The macro <code>UINTMAX_C</code>() expands its argument to an integer constant of type <i>uintmax_t</i>. </p>
<p> The length modifier for <i>uintmax_t</i> for the <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3) and the <code><a href="/docs/linux/man/3-scanf/">scanf</a></code>(3) families of functions is <code>j</code>; resulting commonly in <code>%ju</code> or <code>%jx</code> for printing <i>uintmax_t</i> values. </p>
<p> <i>Conforming to</i>: C99 and later; POSIX.1-2001 and later. </p>
<p> <i>Bugs</i>: <i>uintmax_t</i> is not large enough to represent values of type <i>unsigned __int128</i> in implementations where <i>unsigned __int128</i> is defined and <i>unsigned long long</i> is less than 128 bits wide. </p>
<p> <i>See also</i>: the <i>intmax_t</i> type in this page.</dl>
<dt><i>uint</i>N<i>_t</i></p>
<dd>
<dl>
<dt>
<dd> <i>Include</i>: <i>&lt;stdint.h&gt;</i>. Alternatively, <i>&lt;inttypes.h&gt;</i>. </p>
<p> <i>uint8_t</i>, <i>uint16_t</i>, <i>uint32_t</i>, <i>uint64_t</i> </p>
<p> An unsigned integer type of a fixed width of exactly N bits, N being the value specified in its type name. According to the C language standard, they shall be capable of storing values in the range [0, <code>UINT</code>N<code>_MAX</code>], substituting N by the appropriate number. </p>
<p> According to POSIX, <i>uint8_t</i>, <i>uint16_t</i>, and <i>uint32_t</i> are required; <i>uint64_t</i> is only required in implementations that provide integer types with width 64; and all other types of this form are optional. </p>
<p> The length modifiers for the <i>uint</i>N<i>_t</i> types for the <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3) family of functions are expanded by macros of the forms <code>PRIu</code>N, <code>PRIo</code>N, <code>PRIx</code>N, and <code>PRIX</code>N (defined in <i>&lt;inttypes.h&gt;</i>); resulting for example in <code>%PRIu32</code> or <code>%PRIx32</code> for printing <i>uint32_t</i> values. The length modifiers for the <i>uint</i>N<i>_t</i> types for the <code><a href="/docs/linux/man/3-scanf/">scanf</a></code>(3) family of functions are expanded by macros of the forms <code>SCNu</code>N, <code>SCNo</code>N, <code>SCNx</code>N, and <code>SCNX</code>N (defined in <i>&lt;inttypes.h&gt;</i>); resulting for example in <code>%SCNu16</code> or <code>%SCNx16</code> for scanning <i>uint16_t</i> values. </p>
<p> <i>Conforming to</i>: C99 and later; POSIX.1-2001 and later. </p>
<p> <i>See also</i>: the <i>intmax_t</i>, <i>int</i>N<i>_t</i>, and <i>uintmax_t</i> types in this page.</dl>
<dt><i>uintptr_t</i></p>
<dd>
<dl>
<dt>
<dd> <i>Include</i>: <i>&lt;stdint.h&gt;</i>. Alternatively, <i>&lt;inttypes.h&gt;</i>. </p>
<p> An unsigned integer type such that any valid (<i>void *</i>) value can be converted to this type and back. According to the C language standard, it shall be capable of storing values in the range [0, <code>UINTPTR_MAX</code>]. </p>
<p> The length modifier for <i>uintptr_t</i> for the <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3) family of functions is expanded by the macros <code>PRIuPTR</code>, <code>PRIoPTR</code>, <code>PRIxPTR</code>, and <code>PRIXPTR</code> (defined in <i>&lt;inttypes.h&gt;</i>); resulting commonly in <code>%PRIuPTR</code> or <code>%PRIxPTR</code> for printing <i>uintptr_t</i> values. The length modifier for <i>uintptr_t</i> for the <code><a href="/docs/linux/man/3-scanf/">scanf</a></code>(3) family of functions is expanded by the macros <code>SCNuPTR,</code> <code>SCNoPTR,</code> <code>SCNxPTR</code>, and <code>SCNXPTR</code> (defined in <i>&lt;inttypes.h&gt;</i>); resulting commonly in <code>%SCNuPTR</code> or <code>%SCNxPTR</code> for scanning <i>uintptr_t</i> values. </p>
<p> <i>Conforming to</i>: C99 and later; POSIX.1-2001 and later. </p>
<p> <i>See also</i>: the <i>intptr_t</i> and <i>void *</i> types in this page.</dl>
<dt><i>va_list</i></p>
<dd>
<dl>
<dt>
<dd> <i>Include</i>: <i>&lt;stdarg&gt;</i>. Alternatively, <i>&lt;stdio.h&gt;</i>, or <i>&lt;wchar.h&gt;</i>. </p>
<p> Used by functions with a varying number of arguments of varying types. The function must declare an object of type <i>va_list</i> which is used by the macros <code><a href="/docs/linux/man/3-va_start/">va_start</a></code>(3), <code><a href="/docs/linux/man/3-va_arg/">va_arg</a></code>(3), <code><a href="/docs/linux/man/3-va_copy/">va_copy</a></code>(3), and <code><a href="/docs/linux/man/3-va_end/">va_end</a></code>(3) to traverse the list of arguments. </p>
<p> <i>Conforming to</i>: C99 and later; POSIX.1-2001 and later. </p>
<p> <i>See also</i>: <code><a href="/docs/linux/man/3-va_start/">va_start</a></code>(3), <code><a href="/docs/linux/man/3-va_arg/">va_arg</a></code>(3), <code><a href="/docs/linux/man/3-va_copy/">va_copy</a></code>(3), <code><a href="/docs/linux/man/3-va_end/">va_end</a></code>(3)</dl>
<dt><i>void *</i></p>
<dd>
<dl>
<dt>
<dd> According to the C language standard, a pointer to any object type may be converted to a pointer to <i>void</i> and back. POSIX further requires that any pointer, including pointers to functions, may be converted to a pointer to <i>void</i> and back. </p>
<p> Conversions from and to any other pointer type are done implicitly, not requiring casts at all. Note that this feature prevents any kind of type checking: the programmer should be careful not to convert a <i>void *</i> value to a type incompatible to that of the underlying data, because that would result in undefined behavior. </p>
<p> This type is useful in function parameters and return value to allow passing values of any type. The function will typically use some mechanism to know the real type of the data being passed via a pointer to <i>void</i>. </p>
<p> A value of this type can&#8217;t be dereferenced, as it would give a value of type <i>void</i>, which is not possible. Likewise, pointer arithmetic is not possible with this type. However, in GNU C, pointer arithmetic is allowed as an extension to the standard; this is done by treating the size of a <i>void</i> or of a function as 1. A consequence of this is that <i>sizeof</i> is also allowed on <i>void</i> and on function types, and returns 1. </p>
<p> The conversion specifier for <i>void *</i> for the <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3) and the <code><a href="/docs/linux/man/3-scanf/">scanf</a></code>(3) families of functions is <code>p</code>. </p>
<p> <i>Versions</i>: The POSIX requirement about compatibility between <i>void *</i> and function pointers was added in POSIX.1-2008 Technical Corrigendum 1 (2013). </p>
<p> <i>Conforming to</i>: C99 and later; POSIX.1-2001 and later. </p>
<p> <i>See also</i>: <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), <code><a href="/docs/linux/man/3-memcmp/">memcmp</a></code>(3), <code><a href="/docs/linux/man/3-memcpy/">memcpy</a></code>(3), <code><a href="/docs/linux/man/3-memset/">memset</a></code>(3) </p>
<p> See also the <i>intptr_t</i> and <i>uintptr_t</i> types in this page.</dl>
</dl>
<h2>NOTES</h2>
<p> The structures described in this manual page shall contain, at least, the members shown in their definition, in no particular order. </p>
<p> Most of the integer types described in this page don&#8217;t have a corresponding length modifier for the <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3) and the <code><a href="/docs/linux/man/3-scanf/">scanf</a></code>(3) families of functions. To print a value of an integer type that doesn&#8217;t have a length modifier, it should be converted to <i>intmax_t</i> or <i>uintmax_t</i> by an explicit cast. To scan into a variable of an integer type that doesn&#8217;t have a length modifier, an intermediate temporary variable of type <i>intmax_t</i> or <i>uintmax_t</i> should be used. When copying from the temporary variable to the destination variable, the value could overflow. If the type has upper and lower limits, the user should check that the value is within those limits, before actually copying the value. The example below shows how these conversions should be done.</p>
<h3>Conventions used in this page</h3>
<p> In &quot;Conforming to&quot; we only concern ourselves with C99 and later and POSIX.1-2001 and later. Some types may be specified in earlier versions of one of these standards, but in the interests of simplicity we omit details from earlier standards. </p>
<p> In &quot;Include&quot;, we first note the &quot;primary&quot; header(s) that define the type according to either the C or POSIX.1 standards. Under &quot;Alternatively&quot;, we note additional headers that the standards specify shall define the type.</p>
<h2>EXAMPLES</h2>
<p> The program shown below scans from a string and prints a value stored in a variable of an integer type that doesn&#8217;t have a length modifier. The appropriate conversions from and to <i>intmax_t</i>, and the appropriate range checks, are used as explained in the notes section above. </p>
<p> #include &lt;stdint.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;sys/types.h&gt; </p>
<p> int main (void) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;static const char&nbsp;*const str&nbsp;=&nbsp;&quot;500000 us in half a second&quot;;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;suseconds_t us;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;intmax_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tmp; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Scan the number from the string into the temporary variable&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sscanf(str,&nbsp;&quot;%jd&quot;,&nbsp;&amp;tmp); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Check that the value is within the valid range of suseconds_t&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(tmp&nbsp;&lt;&nbsp;-1 || tmp&nbsp;&gt;&nbsp;1000000)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Scanned value outside valid range!
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Copy the value to the suseconds_t variable&nbsp;&#8216;us&#8217;&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;us&nbsp;=&nbsp;tmp; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Even though suseconds_t can hold the value -1, this isn&#8217;t<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a sensible number of microseconds&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(us&nbsp;&lt;&nbsp;0)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Scanned value shouldn&#8217;t be negative!
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Print the value&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;There are&nbsp;%jd microseconds in half a second.
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(intmax_t)&nbsp;us); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7), <code><a href="/docs/linux/man/7-standards/">standards</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>

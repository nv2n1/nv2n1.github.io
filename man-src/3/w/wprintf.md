---
title: "wprintf(3)"
name: "wprintf"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wprintf/"
description: "wprintf, fwprintf, swprintf, vwprintf, vfwprintf, vswprintf – formatted wide-character output conversion"
---

<p>wprintf, fwprintf, swprintf, vwprintf, vfwprintf, vswprintf &#8211; formatted wide-character output conversion</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stdio.h&gt;
#include &lt;wchar.h&gt;

int wprintf(const wchar_t *format, ...);
int fwprintf(FILE *stream, const wchar_t *format, ...);
int swprintf(wchar_t *wcs, size_t maxlen,
             const wchar_t *format, ...);

int vwprintf(const wchar_t *format, va_list args);
int vfwprintf(FILE *stream, const wchar_t *format, va_list args);
int vswprintf(wchar_t *wcs, size_t maxlen,
              const wchar_t *format, va_list args);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): All functions shown above:</p>
<dl>
<dd>_XOPEN_SOURCE&nbsp;&gt;=&nbsp;500 || _ISOC99_SOURCE ||<br />
 _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L</dl>
<h2>Description</h2>
<p>The <code>wprintf</code>() family of functions is the wide-character equivalent of the <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3) family of functions. It performs formatted output of wide characters. </p>
<p> The <code>wprintf</code>() and <code>vwprintf</code>() functions perform wide-character output to <i>stdout</i>. <i>stdout</i> must not be byte oriented; see <code><a href="/docs/linux/man/3-fwide/">fwide</a></code>(3) for more information. </p>
<p> The <code>fwprintf</code>() and <code>vfwprintf</code>() functions perform wide-character output to <i>stream</i>. <i>stream</i> must not be byte oriented; see <code><a href="/docs/linux/man/3-fwide/">fwide</a></code>(3) for more information. </p>
<p> The <code>swprintf</code>() and <code>vswprintf</code>() functions perform wide-character output to an array of wide characters. The programmer must ensure that there is room for at least <i>maxlen</i> wide characters at <i>wcs</i>. </p>
<p> These functions are like the <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3), <code><a href="/docs/linux/man/3-vprintf/">vprintf</a></code>(3), <code><a href="/docs/linux/man/3-fprintf/">fprintf</a></code>(3), <code><a href="/docs/linux/man/3-vfprintf/">vfprintf</a></code>(3), <code><a href="/docs/linux/man/3-sprintf/">sprintf</a></code>(3), <code><a href="/docs/linux/man/3-vsprintf/">vsprintf</a></code>(3) functions except for the following differences:</p>
<dl>
<dt><code>&bull;</code></p>
<dd>The <i>format</i> string is a wide-character string.</p>
<dt><code>&bull;</code></p>
<dd>The output consists of wide characters, not bytes.</p>
<dt><code>&bull;</code></p>
<dd><code>swprintf</code>() and <code>vswprintf</code>() take a <i>maxlen</i> argument, <code><a href="/docs/linux/man/3-sprintf/">sprintf</a></code>(3) and <code><a href="/docs/linux/man/3-vsprintf/">vsprintf</a></code>(3) do not. (<code><a href="/docs/linux/man/3-snprintf/">snprintf</a></code>(3) and <code><a href="/docs/linux/man/3-vsnprintf/">vsnprintf</a></code>(3) take a <i>maxlen</i> argument, but these functions do not return -1 upon buffer overflow on Linux.)</dl>
<p> The treatment of the conversion characters <code>c</code> and <code>s</code> is different:</p>
<dl>
<dt><code>c</code></p>
<dd>If no <code>l</code> modifier is present, the <i>int</i> argument is converted to a wide character by a call to the <code><a href="/docs/linux/man/3-btowc/">btowc</a></code>(3) function, and the resulting wide character is written. If an <code>l</code> modifier is present, the <i>wint_t</i> (wide character) argument is written.</p>
<dt><code>s</code></p>
<dd>If no <code>l</code> modifier is present: the <i>const char&nbsp;*</i> argument is expected to be a pointer to an array of character type (pointer to a string) containing a multibyte character sequence beginning in the initial shift state. Characters from the array are converted to wide characters (each by a call to the <code><a href="/docs/linux/man/3-mbrtowc/">mbrtowc</a></code>(3) function with a conversion state starting in the initial state before the first byte). The resulting wide characters are written up to (but not including) the terminating null wide character (L&#8217;

---
title: "unicode_wb_end(3)"
name: "unicode_wb_end"
section: "3"
letter: "u"
url: "/docs/linux/man/3-unicode_wb_end/"
description: "unicode_wb_init, unicode_wb_next, unicode_wb_next_cnt, unicode_wb_end, unicode_wbscan_init, unicode_wbscan_next, unicode_wbscan_end – calculate word breaks"
---

<p>unicode_wb_init, unicode_wb_next, unicode_wb_next_cnt, unicode_wb_end, unicode_wbscan_init, unicode_wbscan_next, unicode_wbscan_end &#8211; calculate word breaks</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;courier-unicode.h&gt;

unicode_wb_info_t unicode_wb_init(int (*cb_func)(int, void *), void *cb_arg);

int unicode_wb_next(unicode_wb_info_t wb, unicode_char c);

int unicode_wb_next_cnt(unicode_wb_info_t wb, const unicode_char *cptr, size_t cnt);

int unicode_wb_end(unicode_wb_info_t wb);

unicode_wbscan_info_t unicode_wbscan_init(void);

int unicode_wbscan_next(unicode_wbscan_info_t wbs, unicode_char c);

size_t unicode_wbscan_end(unicode_wbscan_info_t wbs);</code></pre>
<h2>Description</h2>
<dd>These functions implement the unicode word breaking algorithm. Invoke <code>unicode_wb_init</code>() to initialize the word breaking algorithm. The first parameter is a callback function. The second parameter is an opaque pointer. The callback function gets invoked with two parameters. The second parameter is the opaque pointer that was given to <code>unicode_wb_init</code>(); and the opaque pointer is not subject to any further interpretation by these functions. </p>
<p> <code>unicode_wb_init</code>() returns an opaque handle. Repeated invocations of <code>unicode_wb_next</code>(), passing the handle, and one unicode character defines a sequence of unicode characters over which the word breaking algorithm calculation takes place. <code>unicode_wb_next_cnt</code>() is a shortcut for invoking <code>unicode_wb_next</code>() repeatedly over an array cptr containing cnt unicode characters. </p>
<p> <code>unicode_wb_end</code>() denotes the end of the unicode character sequence. After the call to <code>unicode_wb_end</code>() the word breaking unicode_wb_info_t handle is no longer valid. </p>
<p> Between the call to <code>unicode_wb_init</code>() and <code>unicode_wb_end</code>(), the callback function gets invoked exactly once for each unicode character given to <code>unicode_wb_next</code>() or <code>unicode_wb_next_cnt</code>(). Usually each call to <code>unicode_wb_next</code>() results in the callback function getting invoked immediately, but it does not have to be. It&#8217;s possible that a call to <code>unicode_wb_next</code>() returns without invoking the callback function, and some subsequent call to <code>unicode_wb_next</code>() (or <code>unicode_wb_end</code>()) invokes the callback function more than once, to catch things up. The contract is that before <code>unicode_wb_end</code>() returns, the callback function gets invoked the exact number of times as the number of characters in the unicode sequence defined by the intervening calls to <code>unicode_wb_next</code>() and <code>unicode_wb_next_cnt</code>(), unless an error occurs. </p>
<p> Each call to the callback function reports the calculated wordbreaking status of the corresponding character in the unicode character sequence. If the parameter to the callback function is non zero, a word break is permitted <i>before</i> the corresponding character. A zero value indicates that a word break is prohibited <i>before</i> the corresponding character. </p>
<p> The callback function should return 0. A non-zero value indicates to the word breaking algorithm that an error has occured. <code>unicode_wb_next</code>() and <code>unicode_wb_next_cnt</code>() return zero either if they never invoked the callback function, or if each call to the callback function returned zero. A non zero return from the callback function results in <code>unicode_wb_next</code>() and <code>unicode_wb_next_cnt</code>() immediately returning the same value. </p>
<p> <code>unicode_wb_end</code>() must be invoked to destroy the word breaking handle even if <code>unicode_wb_next</code>() and <code>unicode_wb_next_cnt</code>() returned an error indication. It&#8217;s also possible that, under normal circumstances, <code>unicode_wb_end</code>() invokes the callback function one or more times. The return value from <code>unicode_wb_end</code>() has the same meaning as from <code>unicode_wb_next</code>() and <code>unicode_wb_next_cnt</code>(); however in all cases after <code>unicode_wb_end</code>() returns the line breaking handle is no longer valid.</p>
<h3>Word scan</h3>
<p><code>unicode_wbscan_init</code>(), <code>unicode_wbscan_next</code>() and <code>unicode_wbscan_end</code> scan for the next word boundary in a unicode character sequence. <code>unicode_wbscan_init</code>() obtains a handle, then <code>unicode_wbscan_next</code>() gets repeatedly invoked to define the unicode character sequence. <code>unicode_wbscan_end</code>() deallocates the handle and returns the number of leading characters in the unicode character sequence up to the first word break. </p>
<p> A non-0 return value from <code>unicode_wbscan_next</code>() indicates that the word boundary is already known, and any further calls to <code>unicode_wbscan_next</code>() will be ignored. <code>unicode_wbscan_end</code>() must still be called, to obtain the unicode character count.</p>
<h2>See Also</h2>
<p>m[blue]<code>TR-29</code>m[]<font SIZE="-2">[1]</font>, <code><a href="/docs/linux/man/7-courier-unicode/">courier-unicode</a></code>(7), <code><a href="/docs/linux/man/3-unicode--wordbreak/">unicode::wordbreak</a></code>(3), <code><a href="/docs/linux/man/3-unicode_convert_tocase/">unicode_convert_tocase</a></code>(3), <code><a href="/docs/linux/man/3-unicode_line_break/">unicode_line_break</a></code>(3), <code><a href="/docs/linux/man/3-unicode_grapheme_break/">unicode_grapheme_break</a></code>(3).</p>
<h2>Author</h2>
<p><code>Sam Varshavchik</code></p>
<dl>
<dd>Author</dl>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>TR-29</p>
<dl>
<dd><a rel="nofollow" href="http://www.unicode.org/reports/tr29/tr29-27.html">http://www.unicode.org/reports/tr29/tr29-27.html</a></dl>

---
title: "unicode_lb_init(3)"
name: "unicode_lb_init"
section: "3"
letter: "u"
url: "/docs/linux/man/3-unicode_lb_init/"
description: "unicode_lb_init, unicode_lb_set_opts, unicode_lb_next, unicode_lb_next_cnt, unicode_lb_end, unicode_lbc_init, unicode_lbc_set_opts, unicode_lbc_next, unicode_lbc_next_cnt, unicode_lbc_end – calcula..."
---

<p>unicode_lb_init, unicode_lb_set_opts, unicode_lb_next, unicode_lb_next_cnt, unicode_lb_end, unicode_lbc_init, unicode_lbc_set_opts, unicode_lbc_next, unicode_lbc_next_cnt, unicode_lbc_end &#8211; calculate mandatory or allowed line breaks</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;courier-unicode.h&gt;

unicode_lb_info_t unicode_lb_init(int (*cb_func)(int, void *), void *cb_arg);

void unicode_lb_set_opts(unicode_lb_info_t lb, int opts);

int unicode_lb_next(unicode_lb_info_t lb, unicode_char c);

int unicode_lb_next_cnt(unicode_lb_info_t lb, const unicode_char *cptr, size_t cnt);

int unicode_lb_end(unicode_lb_info_t lb);

unicode_lbc_info_t unicode_lbc_init(int (*cb_func)(int, unicode_char, void *), void *cb_arg);

void unicode_lbc_set_opts(unicode_lbc_info_t lb, int opts);

int unicode_lbc_next(unicode_lb_info_t lb, unicode_char c);

int unicode_lbc_next_cnt(unicode_lb_info_t lb, const unicode_char *cptr, size_t cnt);

int unicode_lbc_end(unicode_lb_info_t lb);</code></pre>
<h2>Description</h2>
<dd>These functions implement the unicode line breaking algorithm. Invoke <code>unicode_lb_init</code>() to initialize the line breaking algorithm. The first parameter is a callback function. The second parameter is an opaque pointer. The callback function gets invoked with two parameters. The first parameter is one of three values: UNICODE_LB_MANDATORY, UNICODE_LB_NONE, or UNICODE_LB_ALLOWED, as described below. The second parameter is the opaque pointer that was passed to <code>unicode_lb_init</code>(); the opaque pointer is not subject to any further interpretation by these functions. </p>
<p> <code>unicode_lb_init</code>() returns an opaque handle. Repeated invocations of <code>unicode_lb_next</code>(), passing the handle and one unicode character at a time, defines a sequence of unicode characters over which the line breaking algorithm calculation takes place. <code>unicode_lb_next_cnt</code>() is a shortcut for invoking <code>unicode_lb_next</code>() repeatedly over an array cptr containing cnt unicode characters. </p>
<p> <code>unicode_lb_end</code>() denotes the end of the unicode character sequence. After the call to <code>unicode_lb_end</code>() the line breaking unicode_lb_info_t handle is no longer valid. </p>
<p> Between the call to <code>unicode_lb_init</code>() and <code>unicode_lb_end</code>(), the callback function gets invoked exactly once for each unicode character given to <code>unicode_lb_next</code>() or <code>unicode_lb_next_cnt</code>(). Usually each call to <code>unicode_lb_next</code>() results in the callback function getting invoked immediately, but it does not have to be. It&#8217;s possible that a call to <code>unicode_lb_next</code>() returns without invoking the callback function, and some subsequent call to <code>unicode_lb_next</code>() (or <code>unicode_lb_end</code>()) invokes the callback function more than once, to catch up. The contract is that before <code>unicode_lb_end</code>() returns, the callback function gets invoked the exact number of times as the number of characters in the unicode sequence defined by the intervening calls to <code>unicode_lb_next</code>() and <code>unicode_lb_next_cnt</code>(), unless an error occurs. </p>
<p> Each call to the callback function reports the calculated line breaking status of the corresponding character in the unicode character sequence: </p>
<p> UNICODE_LB_MANDATORY</p>
<dl>
<dd>A line break is MANDATORY <i>before</i> the corresponding character.</dl>
<p> UNICODE_LB_NONE</p>
<dl>
<dd>A line break is PROHIBITED <i>before</i> the corresponding character.</dl>
<p> UNICODE_LB_ALLOWED</p>
<dl>
<dd>A line break is OPTIONAL <i>before</i> the corresponding character.</dl>
<p> The callback function should return 0. A non-zero value indicates to the line breaking algorithm that an error has occured. <code>unicode_lb_next</code>() and <code>unicode_lb_next_cnt</code>() return zero either if they never invoked the callback function, or if each call to the callback function returned zero. A non zero return from the callback function results in <code>unicode_lb_next</code>() and <code>unicode_lb_next_cnt</code>() immediately returning the same value. </p>
<p> <code>unicode_lb_end</code>() must be invoked to destroy the line breaking handle even if <code>unicode_lb_next</code>() and <code>unicode_lb_next_cnt</code>() returned an error indication. It&#8217;s also possible that, under normal circumstances, <code>unicode_lb_end</code>() invokes the callback function one or more times. The return value from <code>unicode_lb_end</code>() has the same meaning as from <code>unicode_lb_next</code>() and <code>unicode_lb_next_cnt</code>(); however in all cases after <code>unicode_lb_end</code>() returns the line breaking handle is no longer valid.</p>
<h3>Alternative callback function</h3>
<p><code>unicode_lbc_init</code>(), <code>unicode_lbc_next</code>(), <code>unicode_lbc_next_cnt</code>(), <code>unicode_lbc_end</code>() are alternative functions that implement the same algorithm. The only difference is that the callback function receives an extra parameter, the unicode character value to which the line breaking status applies to, passed through from the input unicode character sequence.</p>
<h3>Options</h3>
<p><code>unicode_lb_set_opts</code>() and <code>unicode_lbc_set_opts</code>() enable non-default options for the line breaking algorithm. These functions must be called immediately after <code>unicode_lb_init</code>() or <code>unicode_lbc_init</code>(), and before any other function. <i>opts</i> is a bitmask that can contain the following values: </p>
<p> UNICODE_LB_OPT_PRBREAK</p>
<dl>
<dd>Enables a modified LB24 rule. This prevents plus signs, as in &#8220;C++&#8221; from breaking. This flag adds the following rules to the LB24 rule: </p>
<dl>
<dd>
<pre> PR x PR
 AL x PR
 ID x PR</pre>
</dl>
</dl>
<p> UNICODE_LB_OPT_SYBREAK</p>
<dl>
<dd>Tailored breaking rules for the &#8220;/&#8221; character. This prevents breaking after the &#8220;/&#8221; character (think URLs); including an exception to the &#8220;x SY&#8221; rule in LB13. This flag adds the following rules to the LB24 rule: </p>
<dl>
<dd>
<pre> SY x EX
 SY x AL
 SY x ID
 SP &#247; SY, which takes precedence over &quot;x SY&quot;.</pre>
</dl>
</dl>
<p> UNICODE_LB_OPT_DASHWJ</p>
<dl>
<dd>This flag reclassifies U+2013 and U+2014 as class WJ, prohibiting breaks before and after the m-dash and the n-dash unicode characters.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-courier-unicode/">courier-unicode</a></code>(7), <code><a href="/docs/linux/man/3-unicode--linebreak/">unicode::linebreak</a></code>(3), m[blue]<code>TR-14</code>m[]<font SIZE="-2">[1]</font></p>
<h2>Author</h2>
<p><code>Sam Varshavchik</code></p>
<dl>
<dd>Author</dl>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>TR-14</p>
<dl>
<dd><a rel="nofollow" href="http://www.unicode.org/reports/tr14/tr14-35.html">http://www.unicode.org/reports/tr14/tr14-35.html</a></dl>

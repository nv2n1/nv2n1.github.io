---
title: "zrex(3)"
name: "zrex"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zrex/"
description: "zrex – work with regular expressions"
---

<p>zrex &#8211; work with regular expressions</p>
<h2>Synopsis</h2>
<pre>// Constructor. Optionally, sets an expression against which we can match
// text and capture hits. If there is an error in the expression, reports
// zrex_valid() as false and provides the error in zrex_strerror(). If you
// set a pattern, you can call zrex_matches() to test it against text.
CZMQ_EXPORT zrex_t *
 zrex_new (const char *expression);
// Destructor
CZMQ_EXPORT void
 zrex_destroy (zrex_t **self_p);
// Return true if the expression was valid and compiled without errors.
CZMQ_EXPORT bool
 zrex_valid (zrex_t *self);
// Return the error message generated during compilation of the expression.
CZMQ_EXPORT const char *
 zrex_strerror (zrex_t *self);
// Returns true if the text matches the previously compiled expression.
// Use this method to compare one expression against many strings.
CZMQ_EXPORT bool
 zrex_matches (zrex_t *self, const char *text);
// Returns true if the text matches the supplied expression. Use this
// method to compare one string against several expressions.
CZMQ_EXPORT bool
 zrex_eq (zrex_t *self, const char *text, const char *expression);
// Returns number of hits from last zrex_matches or zrex_eq. If the text
// matched, returns 1 plus the number of capture groups. If the text did
// not match, returns zero. To retrieve individual capture groups, call
// zrex_hit ().
CZMQ_EXPORT int
 zrex_hits (zrex_t *self);
// Returns the Nth capture group from the last expression match, where
// N is 0 to the value returned by zrex_hits(). Capture group 0 is the
// whole matching string. Sequence 1 is the first capture group, if any,
// and so on.
CZMQ_EXPORT const char *
 zrex_hit (zrex_t *self, uint index);
// Fetches hits into string variables provided by caller; this makes for
// nicer code than accessing hits by index. Caller should not modify nor
// free the returned values. Returns number of strings returned. This
// method starts at hit 1, i.e. first capture group, as hit 0 is always
// the original matched string.
CZMQ_EXPORT int
 zrex_fetch (zrex_t *self, const char **string_p, ...);
// Self test of this class
CZMQ_EXPORT void
 zrex_test (bool verbose);</pre>
<h2>Description</h2>
<p>Wraps a very simple regular expression library (SLRE) as a CZMQ class. Supports this syntax: </p>
<dl>
<dd>
<pre>^ Match beginning of a buffer
$ Match end of a buffer
() Grouping and substring capturing
[...] Match any character from set
[^...] Match any character but ones from set
. Match any character
\s Match whitespace
\S Match non-whitespace
\d Match decimal digit
\D Match non decimal digit
 Match alphabetic character
\A Match non-alphabetic character
\w Match alphanumeric character
\W Match non-alphanumeric character
 Match carriage return

 Match newline
+ Match one or more times (greedy)
+? Match one or more times (non-greedy)
* Match zero or more times (greedy)
*? Match zero or more times (non-greedy)
? Match zero or once
� Match byte with hex value 0xDD
\meta Match one of the meta character: ^$().[*+?\</pre>
</dl>
<p> Please add @discuss section in ../src/zrex.c.</p>
<h2>Example</h2>
<p><code>From zrex_test method</code>. </p>
<pre><code>//  This shows the pattern of matching many lines to a single pattern
zrex_t *rex = zrex_new(&quot;\d+-\d+-\d+&quot;);
assert(rex);
assert(zrex_valid(rex));
bool matches = zrex_matches(rex, &quot;123-456-789&quot;);
assert(matches);
assert(zrex_hits(rex) == 1);
assert(streq(zrex_hit(rex, 0), &quot;123-456-789&quot;));
assert(zrex_hit(rex, 1) == NULL);
zrex_destroy(&amp;rex);

//  Here we pick out hits using capture groups
rex = zrex_new(&quot;(\d+)-(\d+)-(\d+)&quot;);
assert(rex);
assert(zrex_valid(rex));
matches = zrex_matches(rex, &quot;123-456-ABC&quot;);
assert(!matches);
matches = zrex_matches(rex, &quot;123-456-789&quot;);
assert(matches);
assert(zrex_hits(rex) == 4);
assert(streq(zrex_hit(rex, 0), &quot;123-456-789&quot;));
assert(streq(zrex_hit(rex, 1), &quot;123&quot;));
assert(streq(zrex_hit(rex, 2), &quot;456&quot;));
assert(streq(zrex_hit(rex, 3), &quot;789&quot;));
zrex_destroy(&amp;rex);

//  This shows the pattern of matching one line against many
//  patterns and then handling the case when it hits
rex = zrex_new(NULL); //  No initial pattern
assert(rex);
char *input = &quot;Mechanism: CURVE&quot;;
matches = zrex_eq(rex, input, &quot;Version: (.+)&quot;);
assert(!matches);
assert(zrex_hits(rex) == 0);
matches = zrex_eq(rex, input, &quot;Mechanism: (.+)&quot;);
assert(matches);
assert(zrex_hits(rex) == 2);
const char *mechanism;
zrex_fetch(rex, &amp;mechanism, NULL);
assert(streq(zrex_hit(rex, 1), &quot;CURVE&quot;));
assert(streq(mechanism, &quot;CURVE&quot;));
zrex_destroy(&amp;rex);
</code></pre>
<h2>Authors</h2>
<p>The czmq manual was written by the authors in the AUTHORS file.</p>
<h2>Resources</h2>
<p>Main web site: m[blue]m[] </p>
<p> Report bugs to the email &lt;m[blue]<code>zeromq-dev [at] lists.zeromq.org</code>m[]<font SIZE="-2">[1]</font>&gt;</p>
<h2>Copyright</h2>
<p>Copyright (c) 1991-2012 iMatix Corporation &#8212; <a rel="nofollow" href="http://www.imatix.com">http://www.imatix.com</a> Copyright other contributors as noted in the AUTHORS file. This file is part of CZMQ, the high-level C binding for 0MQ: <a href="http://czmq.zeromq.org">http://czmq.zeromq.org</a> This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at <a href="http://mozilla.org/MPL/2.0/.">http://mozilla.org/MPL/2.0/.</a> LICENSE included with the czmq distribution.</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>zeromq-dev [at] lists.zeromq.org</p>
<dl>
<dd>mailto:zeromq-dev [at] lists.zeromq.org</dl>

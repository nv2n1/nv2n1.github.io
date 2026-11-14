---
title: "pam_succeed_if(8)"
name: "pam_succeed_if"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_succeed_if/"
description: "pam_succeed_if – test account characteristics"
---

<p>pam_succeed_if &#8211; test account characteristics</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_succeed_if.so</code> [<i>flag</i>&#8230;] [<i>condition</i>&#8230;]</dl>
<h2>Description</h2>
<dd>pam_succeed_if.so is designed to succeed or fail authentication based on characteristics of the account belonging to the user being authenticated or values of other PAM items. One use is to select whether to load other modules based on this test. </p>
<p> The module should be given one or more conditions as module arguments, and authentication will succeed only if all of the conditions are met.</p>
<h2>Options</h2>
<p>The following <i>flag</i>s are supported: </p>
<p> <code>debug</code></p>
<dl>
<dd>Turns on debugging messages sent to syslog.</dl>
<p> <code>use_uid</code></p>
<dl>
<dd>Evaluate conditions using the account of the user whose UID the application is running under instead of the user being authenticated.</dl>
<p> <code>quiet</code></p>
<dl>
<dd>Don&#8217;t log failure or success to the system log.</dl>
<p> <code>quiet_fail</code></p>
<dl>
<dd>Don&#8217;t log failure to the system log.</dl>
<p> <code>quiet_success</code></p>
<dl>
<dd>Don&#8217;t log success to the system log.</dl>
<p> <code>audit</code></p>
<dl>
<dd>Log unknown users to the system log.</dl>
<p> <i>Condition</i>s are three words: a field, a test, and a value to test for. </p>
<p> Available fields are <i>user</i>, <i>uid</i>, <i>gid</i>, <i>shell</i>, <i>home</i>, <i>ruser</i>, <i>rhost</i>, <i>tty</i> and <i>service</i>: </p>
<p> <code>field &lt; number</code></p>
<dl>
<dd>Field has a value numerically less than number.</dl>
<p> <code>field &lt;= number</code></p>
<dl>
<dd>Field has a value numerically less than or equal to number.</dl>
<p> <code>field eq number</code></p>
<dl>
<dd>Field has a value numerically equal to number.</dl>
<p> <code>field &gt;= number</code></p>
<dl>
<dd>Field has a value numerically greater than or equal to number.</dl>
<p> <code>field &gt; number</code></p>
<dl>
<dd>Field has a value numerically greater than number.</dl>
<p> <code>field ne number</code></p>
<dl>
<dd>Field has a value numerically different from number.</dl>
<p> <code>field = string</code></p>
<dl>
<dd>Field exactly matches the given string.</dl>
<p> <code>field != string</code></p>
<dl>
<dd>Field does not match the given string.</dl>
<p> <code>field =~ glob</code></p>
<dl>
<dd>Field matches the given glob.</dl>
<p> <code>field !~ glob</code></p>
<dl>
<dd>Field does not match the given glob.</dl>
<p> <code>field in item:item:&#8230;</code></p>
<dl>
<dd>Field is contained in the list of items separated by colons.</dl>
<p> <code>field notin item:item:&#8230;</code></p>
<dl>
<dd>Field is not contained in the list of items separated by colons.</dl>
<p> <code>user ingroup group[:group:&#8230;.]</code></p>
<dl>
<dd>User is in given group(s).</dl>
<p> <code>user notingroup group[:group:&#8230;.]</code></p>
<dl>
<dd>User is not in given group(s).</dl>
<p> <code>user innetgr netgroup</code></p>
<dl>
<dd>(user,host) is in given netgroup.</dl>
<p> <code>user notinnetgr group</code></p>
<dl>
<dd>(user,host) is not in given netgroup.</dl>
<h2>Module Types Provided</h2>
<p>All module types (<code>account</code>, <code>auth</code>, <code>password</code> and <code>session</code>) are provided.</p>
<h2>Return Values</h2>
<p>PAM_SUCCESS</p>
<dl>
<dd>The condition was true.</dl>
<p> PAM_AUTH_ERR</p>
<dl>
<dd>The condition was false.</dl>
<p> PAM_SERVICE_ERR</p>
<dl>
<dd>A service error occurred or the arguments can&#8217;t be parsed correctly.</dl>
<h2>Examples</h2>
<p>To emulate the behaviour of <i>pam_wheel</i>, except there is no fallback to group 0 being only approximated by checking also the root group membership: </p>
<dl>
<dd>
<pre>auth required pam_succeed_if.so quiet user ingroup wheel:root</pre>
</dl>
<p> Given that the type matches, only loads the othermodule rule if the UID is over 500. Adjust the number after default to skip several rules. </p>
<dl>
<dd>
<pre>type [default=1 success=ignore] pam_succeed_if.so quiet uid &gt; 500
type required othermodule.so arguments...</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-glob/">glob</a></code>(7), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7)</p>
<h2>Author</h2>
<p>Nalin Dahyabhai &lt;nalin [at] redhat.com&gt;</p>

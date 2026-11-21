---

title: "pam_issue(8)"
name: "pam_issue"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_issue/"
description: "pam_issue – PAM module to add issue file to user prompt"
---

<p>pam_issue &#8211; PAM module to add issue file to user prompt </p>
<dl>
<dt><code>pam_issue.so</code> [noesc] [issue=<i>issue-file-name</i>] </dt>
</dl>
<dd> <p> pam_issue is a PAM module to prepend an issue file to the username prompt. It also by default parses escape codes in the issue file similar to some common getty&#8217;s (using \x format). </p>
<p>Recognized escapes: </p>
<p> <code>\d</code> </p>
 </dd>
<dl>
<dd> <p> current day </p>
 </dd></dl>
<p> <code>\l</code> </p>
<dl>
<dd> <p> name of this tty </p>
 </dd></dl>
<p> <code>\m</code> </p>
<dl>
<dd> <p> machine architecture (uname -m) </p>
 </dd></dl>
<p> <code>\n</code> </p>
<dl>
<dd> <p> machine&#8217;s network node hostname (uname -n) </p>
 </dd></dl>
<p> <code>\o</code> </p>
<dl>
<dd> <p> domain name of this system </p>
 </dd></dl>
<p> <code>\r</code> </p>
<dl>
<dd> <p> release number of operating system (uname -r) </p>
 </dd></dl>
<p> <code>\t</code> </p>
<dl>
<dd> <p> current time </p>
 </dd></dl>
<p> <code>\s</code> </p>
<dl>
<dd> <p> operating system name (uname -s) </p>
 </dd></dl>
<p> <code>\u</code> </p>
<dl>
<dd> <p> number of users currently logged in </p>
 </dd></dl>
<p> <code>\U</code> </p>
<dl>
<dd> <p> same as \u except it is suffixed with &quot;user&quot; or &quot;users&quot; (eg. &quot;1 user&quot; or &quot;10 users&quot;) </p>
 </dd></dl>
<p> <code>\v</code> </p>
<dl>
<dd> <p> operating system version and build date (uname -v) </p>
 </dd></dl>
<h2>OPTIONS</h2>
<p> <code>noesc</code> </p>
<dl>
<dd> <p> Turns off escape code parsing. </p>
 </dd></dl>
<p> <code>issue=</code><i>issue-file-name</i> </p>
<dl>
<dd> <p> The file to output if not using the default. </p>
 </dd></dl>
<h2>MODULE TYPES PROVIDED</h2>
<p>Only the <code>auth</code> module type is provided.  </p>
<h2>RETURN VALUES</h2>
<p>PAM_BUF_ERR </p>
<dl>
<dd> <p> Memory buffer error. </p>
 </dd></dl>
<p>PAM_IGNORE </p>
<dl>
<dd> <p> The prompt was already changed. </p>
 </dd></dl>
<p>PAM_SERVICE_ERR </p>
<dl>
<dd> <p> A service module error occurred. </p>
 </dd></dl>
<p>PAM_SUCCESS </p>
<dl>
<dd> <p> The new prompt was set successfully. </p>
 </dd></dl>
<h2>EXAMPLES</h2>
<p>Add the following line to /etc/pam.d/login to set the user specific issue at login: </p>
<dl>
<dd> <pre><code>        auth optional pam_issue.so issue=/etc/issue
</code></pre>
 </dd></dl>
<h2>SEE ALSO</h2>
<p> <code>pam.conf</code>(5), <code>pam.d</code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7)  </p>
<h2>AUTHOR</h2>
<p>pam_issue was written by Ben Collins &lt;bcollins [at] debian.org&gt;. </p>

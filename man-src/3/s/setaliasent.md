---
title: "setaliasent(3)"
name: "setaliasent"
section: "3"
letter: "s"
url: "/docs/linux/man/3-setaliasent/"
description: "setaliasent, endaliasent, getaliasent, getaliasent_r, getaliasbyname, getaliasbyname_r – read an alias entry"
---

<p>setaliasent, endaliasent, getaliasent, getaliasent_r, getaliasbyname, getaliasbyname_r &#8211; read an alias entry</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;aliases.h&gt;
void setaliasent(void);
void endaliasent(void);
struct aliasent *getaliasent(void);
int getaliasent_r(struct aliasent *result,

                  char *buffer, size_t buflen, struct aliasent **res);
struct aliasent *getaliasbyname(const char *name);
int getaliasbyname_r(const char *name, struct aliasent *result,

                     char *buffer, size_t buflen, struct aliasent **res);</code></pre>
<h2>Description</h2>
<p>One of the databases available with the Name Service Switch (NSS) is the aliases database, that contains mail aliases. (To find out which databases are supported, try <i>getent &#8211;help</i>.) Six functions are provided to access the aliases database. The <code>getaliasent</code>() function returns a pointer to a structure containing the group information from the aliases database. The first time it is called it returns the first entry; thereafter, it returns successive entries. The <code>setaliasent</code>() function rewinds the file pointer to the beginning of the aliases database. The <code>endaliasent</code>() function closes the aliases database. <code>getaliasent_r</code>() is the reentrant version of the previous function. The requested structure is stored via the first argument but the programmer needs to fill the other arguments also. Not providing enough space causes the function to fail. The function <code>getaliasbyname</code>() takes the name argument and searches the aliases database. The entry is returned as a pointer to a <i>struct aliasent</i>. <code>getaliasbyname_r</code>() is the reentrant version of the previous function. The requested structure is stored via the second argument but the programmer needs to fill the other arguments also. Not providing enough space causes the function to fail. The <i>struct aliasent</i> is defined in <i>&lt;aliases.h&gt;</i>: struct aliasent {<br />
    char *alias_name; /* alias name */<br />
    size_t alias_members_len;<br />
    char **alias_members; /* alias name list */<br />
    int alias_local;<br />
};</p>
<h2>Return Value</h2>
<p>The functions <code>getaliasent_r</code>() and <code>getaliasbyname_r</code>() return a nonzero value on error.</p>
<h2>Files</h2>
<p>The default alias database is the file <i>/etc/aliases</i>. This can be changed in the <i>/etc/nsswitch.conf</i> file.</p>
<h2>Attributes</h2>
<p>For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>setaliasent</code>(), <code>endaliasent</code>(), <code>getaliasent_r</code>(), <code>getaliasbyname_r</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>getaliasent</code>(), <code>getaliasbyname</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>These routines are glibc-specific. The NeXT system has similar routines: #include &lt;aliasdb.h&gt;<br />
void alias_setent(void);<br />
void alias_endent(void);<br />
alias_ent *alias_getent(void);<br />
alias_ent *alias_getbyname(char *name);</p>
<h2>Examples</h2>
<p>The following example compiles with <i>gcc example.c -o example</i>. It will dump all names in the alias database. </p>
<pre><code>#include &lt;aliases.h&gt;
#include &lt;errno.h&gt;
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
int main(void)
{
    struct aliasent *al;
    setaliasent();
    for (;;) {
        al = getaliasent();
        if (al == NULL)
            break;
        printf(&quot;Name: %s
&quot;, al-&gt;alias_name);
    }
    if (errno) {
        perror(&quot;reading alias&quot;);
        exit(EXIT_FAILURE);
    }
    endaliasent();
    exit(EXIT_SUCCESS);
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-getgrent/">getgrent</a></code>(3), <code><a href="/docs/linux/man/3-getpwent/">getpwent</a></code>(3), <code><a href="/docs/linux/man/3-getspent/">getspent</a></code>(3), <code><a href="/docs/linux/man/5-aliases/">aliases</a></code>(5)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>

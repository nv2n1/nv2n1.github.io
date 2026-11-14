---
title: "makedefs(1)"
name: "makedefs"
section: "1"
letter: "m"
url: "/docs/linux/man/1-makedefs/"
description: "makedefs – Postfix makefile configuration utility"
---

<h2 class="name">NAME</h2>
<p> makedefs &#8211; Postfix makefile configuration utility </p>
<h2>SYNOPSIS</h2>
<pre>
<code>make makefiles </code><i>name=value...</i>
</pre>
<h2>DESCRIPTION</h2>
<p> The <code>makedefs</code> command identifies the compilation environment, and emits macro definitions on the standard output stream that can be prepended to template Makefiles. These macros implement an internal interface and are subject to change without notice.</p>
<h2>NAME=VALUE OVERRIDES</h2>
<p> Default settings can be overruled by specifying them as environment variables (or as name=value pairs on the &quot;make&quot; command line). Use quotes if variables contain whitespace or shell meta characters. </p>
<p> The command &quot;<code>make makefiles name=value&#8230;</code>&quot; will replace the string <code>MAIL_VERSION</code> at the end of a value with the Postfix version (<i>major.minor.patchlevel</i> for a stable release, <i>major.minor-date</i> for a development release). Do not try to specify something like <code>$mail_version</code>: that produces inconsistent results with different implementations of the <a href="/docs/linux/man/1-make/">make</a>(1) command.</p>
<dl>
<dt><code>AUXLIBS=</code><i>object_library&#8230;</i></p>
<dd> Specifies one or more non-default object libraries. Postfix 3.0 and later specify some of their database library dependencies with AUXLIBS_CDB, AUXLIBS_LDAP, AUXLIBS_LMDB, AUXLIBS_MYSQL, AUXLIBS_PCRE, AUXLIBS_PGSQL, AUXLIBS_SDBM, and AUXLIBS_SQLITE, respectively.</p>
<dt><code>CC=</code><i>compiler_command</i></p>
<dd> Specifies a non-default compiler. On many systems, the default is <code>gcc</code>.</p>
<dt><code>CCARGS=</code><i>compiler_arguments</i></p>
<dd> Specifies non-default compiler arguments, for example, a non-default <i>include</i> directory. The following directives are special:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-DNO_DB</code></p>
<dd> Do not build with Berkeley DB support.</p>
<dt><code>-DNO_DEVPOLL</code></p>
<dd> Do not build with Solaris /dev/poll support. By default, /dev/poll support is compiled in on platforms that are known to support it.</p>
<dt><code>-DNO_DNSSEC</code></p>
<dd> Do not build with DNSSEC support, even if the resolver library appears to support it.</p>
<dt><code>-DNO_EPOLL</code></p>
<dd> Do not build with Linux EPOLL support. By default, EPOLL support is compiled in on platforms that are known to support it.</p>
<dt><code>-DNO_EAI</code></p>
<dd> Do not build with EAI (SMTPUTF8) support. By default, EAI support is compiled in when the &quot;pkg-config&quot; command is found, or the deprecated &quot;icu-config&quot; command.</p>
<dt><code>-DNO_INLINE</code></p>
<dd> Do not require support for C99 &quot;inline&quot; functions. Instead, implement argument typechecks for non-(printf/scanf)-like functions with ternary operators and unreachable code.</p>
<dt><code>-DNO_IPV6</code></p>
<dd> Do not build with IPv6 support. By default, IPv6 support is compiled in on platforms that are known to have IPv6 support. </p>
<p> Note: this directive is for debugging and testing only. It is not guaranteed to work on all platforms. If you don&#8217;t want IPv6 support, set &quot;inet_protocols = ipv4&quot; in main.cf.</p>
<dt><code>-DNO_IP_CYRUS_SASL_AUTH</code></p>
<dd> Don&#8217;t pass remote SMTP client and Postfix SMTP server IP address and port information to the Cyrus SASL library. This is compatible with Postfix &lt; 3.2.</p>
<dt><code>-DNO_KQUEUE</code></p>
<dd> Do not build with FreeBSD/NetBSD/OpenBSD/MacOSX KQUEUE support. By default, KQUEUE support is compiled in on platforms that are known to support it.</p>
<dt><code>-DNO_NIS</code></p>
<dd> Do not build with NIS or NISPLUS support. Support for NIS is unavailable on some recent Linux distributions.</p>
<dt><code>-DNO_NISPLUS</code></p>
<dd> Do not build with NISPLUS support. Support for NISPLUS is unavailable on some recent Solaris distributions.</p>
<dt><code>-DNO_PCRE</code></p>
<dd> Do not build with PCRE support. By default, PCRE support is compiled in when the <code>pcre-config</code> utility is installed.</p>
<dt><code>-DNO_POSIX_GETPW_R</code></p>
<dd> Disable support for POSIX getpwnam_r/getpwuid_r.</p>
<dt><code>-DNO_SIGSETJMP</code></p>
<dd> Use setjmp()/longjmp() instead of sigsetjmp()/siglongjmp(). By default, Postfix uses sigsetjmp()/siglongjmp() when they appear to work.</p>
<dt><code>-DNO_SNPRINTF</code></p>
<dd> Use sprintf() instead of snprintf(). By default, Postfix uses snprintf() except on ancient systems.</dl>
</dl>
<dt><code>DEBUG=</code><i>debug_level</i></p>
<dd> Specifies a non-default debugging level. The default is <code>-g</code>. Specify <code>DEBUG=</code> to turn off debugging.</p>
<dt><code>OPT=</code><i>optimization_level</i></p>
<dd> Specifies a non-default optimization level. The default is <code>-O</code>. Specify <code>OPT=</code> to turn off optimization.</p>
<dt><code>POSTFIX_INSTALL_OPTS=</code><i>-option&#8230;</i></p>
<dd> Specifies options for the postfix-install command, separated by whitespace. Currently, the only supported option is <code>-keep-build-mtime</code>.</p>
<dt><code>SHLIB_CFLAGS=</code><i>flags</i></p>
<dd> Override the compiler flags (typically, &quot;-fPIC&quot;) for Postfix dynamically-linked libraries and database plugins. </p>
<p> This feature was introduced with Postfix 3.0.</p>
<dt><code>SHLIB_RPATH=</code><i>rpath</i></p>
<dd> Override the runpath (typically, &quot;&#8217;-Wl,-rpath,${SHLIB_DIR}&#8217;&quot;) for Postfix dynamically-linked libraries. </p>
<p> This feature was introduced with Postfix 3.0.</p>
<dt><code>SHLIB_SUFFIX=</code><i>suffix</i></p>
<dd> Override the filename suffix (typically, &quot;.so&quot;) for Postfix dynamically-linked libraries and database plugins. </p>
<p> This feature was introduced with Postfix 3.0.</p>
<dt><code>shared=yes</code></p>
<dd>
<dt><code>shared=no</code></p>
<dd> Enable (disable) Postfix builds with dynamically-linked libraries typically named $shlib_directory/libpostfix-*.so.*. </p>
<p> This feature was introduced with Postfix 3.0.</p>
<dt><code>dynamicmaps=yes</code></p>
<dd>
<dt><code>dynamicmaps=no</code></p>
<dd> Enable (disable) Postfix builds with the configuration file $meta_directory/dynamicmaps.cf and dynamically-loadable database plugins typically named postfix-*.so.*. The setting &quot;dynamicmaps=yes&quot; implicitly enables Postfix dynamically-linked libraries. </p>
<p> This feature was introduced with Postfix 3.0.</p>
<dt><code>pie=yes</code></p>
<dd>
<dt><code>pie=no</code></p>
<dd> Enable (disable) Postfix builds with position-independent executables, on platforms where this is supported. </p>
<p> This feature was introduced with Postfix 3.0.</p>
<dt><i>installation_parameter</i><code>=</code><i>value</i>&#8230;</p>
<dd> Override the compiled-in default value of the specified installation parameter(s). The following parameters are supported in this context: </p>
<p> command_directory config_directory daemon_directory data_directory default_database_type html_directory mail_spool_directory mailq_path manpage_directory meta_directory newaliases_path queue_directory readme_directory sendmail_path shlib_directory openssl_path </p>
<p> See the <a href="/docs/linux/man/5-postconf/">postconf</a>(5) manpage for a description of these parameters. </p>
<p> This feature was introduced with Postfix 3.0.</p>
<dt><code>WARN=</code><i>warning_flags</i></p>
<dd> Specifies non-default gcc compiler warning options for use when &quot;make&quot; is invoked in a source subdirectory only.</dl>
<h2>LICENSE</h2>
<p> The Secure Mailer license must be distributed with this software.</p>
<h2>AUTHOR(S)</h2>
<pre>
Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA
Wietse Venema
Google, Inc.
111 8th Avenue
New York, NY 10011, USA
</pre>
<h2>Index</h2>

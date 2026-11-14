---
title: "initdb(1)"
name: "initdb"
section: "1"
letter: "i"
url: "/docs/linux/man/1-initdb/"
description: "initdb – create a new PostgreSQL database cluster"
---

<h2 class="name">NAME</h2>
<p> initdb &#8211; create a new PostgreSQL database cluster </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>initdb</code> [<i>option</i>&#8230;] [<code>&#8211;pgdata</code> | <code>-D</code>]<i> directory</i></dl>
<h2>DESCRIPTION</h2>
<p> <code>initdb</code></p>
<dd>creates a new PostgreSQL database cluster. A database cluster is a collection of databases that are managed by a single server instance. </p>
<p> Creating a database cluster consists of creating the directories in which the database data will live, generating the shared catalog tables (tables that belong to the whole cluster rather than to any particular database), and creating the template1 and postgres databases. When you later create a new database, everything in the template1 database is copied. (Therefore, anything installed in template1 is automatically copied into each database created later.) The postgres database is a default database meant for use by users, utilities and third party applications. </p>
<p> Although <code>initdb</code> will attempt to create the specified data directory, it might not have permission if the parent directory of the desired data directory is root-owned. To initialize in such a setup, create an empty data directory as root, then use <code>chown</code> to assign ownership of that directory to the database user account, then <code>su</code> to become the database user to run <code>initdb</code>. </p>
<p> <code>initdb</code> must be run as the user that will own the server process, because the server needs to have access to the files and directories that <code>initdb</code> creates. Since the server cannot be run as root, you must not run <code>initdb</code> as root either. (It will in fact refuse to do so.) </p>
<p> <code>initdb</code> initializes the database cluster&#8217;s default locale and character set encoding. The character set encoding, collation order (LC_COLLATE) and character set classes (LC_CTYPE, e.g. upper, lower, digit) can be set separately for a database when it is created. <code>initdb</code> determines those settings for the template1 database, which will serve as the default for all other databases. </p>
<p> To alter the default collation order or character set classes, use the <code>&#8211;lc-collate</code> and <code>&#8211;lc-ctype</code> options. Collation orders other than C or POSIX also have a performance penalty. For these reasons it is important to choose the right locale when running <code>initdb</code>. </p>
<p> The remaining locale categories can be changed later when the server is started. You can also use <code>&#8211;locale</code> to set the default for all locale categories, including collation order and character set classes. All server locale values (lc_*) can be displayed via <code>SHOW ALL</code>. More details can be found in Section 22.1, &#8220;Locale Support&#8221;, in the documentation. </p>
<p> To alter the default encoding, use the <code>&#8211;encoding</code>. More details can be found in Section 22.3, &#8220;Character Set Support&#8221;, in the documentation.</p>
<h2>OPTIONS</h2>
<p> <code>-A </code><i>authmethod</i>, <code>&#8211;auth=</code><i>authmethod</i></p>
<dl>
<dt>
<dd> This option specifies the authentication method for local users used in pg_hba.conf (host and local lines). Do not use trust unless you trust all local users on your system. trust is the default for ease of installation.</dl>
<p> <code>&#8211;auth-host=</code><i>authmethod</i></p>
<dl>
<dt>
<dd> This option specifies the authentication method for local users via TCP/IP connections used in pg_hba.conf (host lines).</dl>
<p> <code>&#8211;auth-local=</code><i>authmethod</i></p>
<dl>
<dt>
<dd> This option specifies the authentication method for local users via Unix-domain socket connections used in pg_hba.conf (local lines).</dl>
<p> <code>-D </code><i>directory</i>, <code>&#8211;pgdata=</code><i>directory</i></p>
<dl>
<dt>
<dd> This option specifies the directory where the database cluster should be stored. This is the only information required by <code>initdb</code>, but you can avoid writing it by setting the <code>PGDATA</code> environment variable, which can be convenient since the database server (<code>postgres</code>) can find the database directory later by the same variable.</dl>
<p> <code>-E </code><i>encoding</i>, <code>&#8211;encoding=</code><i>encoding</i></p>
<dl>
<dt>
<dd> Selects the encoding of the template database. This will also be the default encoding of any database you create later, unless you override it there. The default is derived from the locale, or SQL_ASCII if that does not work. The character sets supported by the PostgreSQL server are described in Section 22.3.1, &#8220;Supported Character Sets&#8221;, in the documentation.</dl>
<p> <code>&#8211;locale=</code><i>locale</i></p>
<dl>
<dt>
<dd> Sets the default locale for the database cluster. If this option is not specified, the locale is inherited from the environment that <code>initdb</code> runs in. Locale support is described in Section 22.1, &#8220;Locale Support&#8221;, in the documentation.</dl>
<p> <code>&#8211;lc-collate=</code><i>locale</i>, <code>&#8211;lc-ctype=</code><i>locale</i>, <code>&#8211;lc-messages=</code><i>locale</i>, <code>&#8211;lc-monetary=</code><i>locale</i>, <code>&#8211;lc-numeric=</code><i>locale</i>, <code>&#8211;lc-time=</code><i>locale</i></p>
<dl>
<dt>
<dd> Like <code>&#8211;locale</code>, but only sets the locale in the specified category.</dl>
<p> <code>&#8211;no-locale</code></p>
<dl>
<dt>
<dd> Equivalent to <code>&#8211;locale=C</code>.</dl>
<p> <code>&#8211;pwfile=</code><i>filename</i></p>
<dl>
<dt>
<dd> Makes <code>initdb</code> read the database superuser&#8217;s password from a file. The first line of the file is taken as the password.</dl>
<p> <code>-T </code><i>CFG</i>, <code>&#8211;text-search-config=</code><i>CFG</i></p>
<dl>
<dt>
<dd> Sets the default text search configuration. See default_text_search_config for further information.</dl>
<p> <code>-U </code><i>username</i>, <code>&#8211;username=</code><i>username</i></p>
<dl>
<dt>
<dd> Selects the user name of the database superuser. This defaults to the name of the effective user running <code>initdb</code>. It is really not important what the superuser&#8217;s name is, but one might choose to keep the customary name postgres, even if the operating system user&#8217;s name is different.</dl>
<p> <code>-W</code>, <code>&#8211;pwprompt</code></p>
<dl>
<dt>
<dd> Makes <code>initdb</code> prompt for a password to give the database superuser. If you don&#8217;t plan on using password authentication, this is not important. Otherwise you won&#8217;t be able to use password authentication until you have a password set up.</dl>
<p> <code>-X </code><i>directory</i>, <code>&#8211;xlogdir=</code><i>directory</i></p>
<dl>
<dt>
<dd> This option specifies the directory where the transaction log should be stored.</dl>
<p> Other, less commonly used, options are also available: </p>
<p> <code>-d</code>, <code>&#8211;debug</code></p>
<dl>
<dt>
<dd> Print debugging output from the bootstrap backend and a few other messages of lesser interest for the general public. The bootstrap backend is the program <code>initdb</code> uses to create the catalog tables. This option generates a tremendous amount of extremely boring output.</dl>
<p> <code>-L </code><i>directory</i></p>
<dl>
<dt>
<dd> Specifies where <code>initdb</code> should find its input files to initialize the database cluster. This is normally not necessary. You will be told if you need to specify their location explicitly.</dl>
<p> <code>-n</code>, <code>&#8211;noclean</code></p>
<dl>
<dt>
<dd> By default, when <code>initdb</code> determines that an error prevented it from completely creating the database cluster, it removes any files it might have created before discovering that it cannot finish the job. This option inhibits tidying-up and is thus useful for debugging.</dl>
<p> Other options: </p>
<p> <code>-s</code>, <code>&#8211;show</code></p>
<dl>
<dt>
<dd> Print the internal settings, then exit.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print the initdb version and exit.</dl>
<p> <code>-?</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help about initdb command line arguments, and exit.</dl>
<h2>ENVIRONMENT</h2>
<p> <code>PGDATA</code></p>
<dl>
<dt>
<dd> Specifies the directory where the database cluster is to be stored; can be overridden using the <code>-D</code> option.</dl>
<p> <code>TZ</code></p>
<dl>
<dt>
<dd> Specifies the time zone, using full time zone names, which the created database cluster should use.</dl>
<p> This utility, like most other PostgreSQL utilities, also uses the environment variables supported by libpq (see Section 31.14, &#8220;Environment Variables&#8221;, in the documentation).</p>
<h2>NOTES</h2>
<p> <code>initdb</code> can also be invoked via <code>pg_ctl initdb</code>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pg_ctl/">pg_ctl</a></code>(1), <code><a href="/docs/linux/man/1-postgres/">postgres</a></code>(1) </p>
<h2>Index</h2>

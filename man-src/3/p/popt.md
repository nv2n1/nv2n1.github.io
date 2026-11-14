---
title: "popt(3)"
name: "popt"
section: "3"
letter: "p"
url: "/docs/linux/man/3-popt/"
description: "popt – Parse command line options"
---

<p>popt &#8211; Parse command line options</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;popt.h&gt;

poptContext poptGetContext(const char *name, int argc,
                           const char **argv,
                           const struct poptOption *options,
                           int flags);

void poptFreeContext(poptContext con);

void poptResetContext(poptContext con);

int poptGetNextOpt(poptContext con);

const char *poptGetOptArg(poptContext con);

const char *poptGetArg(poptContext con);

const char *poptPeekArg(poptContext con);

const char **poptGetArgs(poptContext con);

const char *const poptStrerror(const int error);

const char *poptBadOption(poptContext con, int flags);

int poptReadDefaultConfig(poptContext con, int flags);

int poptReadConfigFile(poptContext con, char *fn);

int poptAddAlias(poptContext con, struct poptAlias alias,
                 int flags);

int poptParseArgvString(char *s, int *argcPtr,
                        const char ***argvPtr);

int poptDupArgv(int argc, const char **argv, int *argcPtr,
                const char ***argvPtr);

int poptStuffArgs(poptContext con, const char **argv);</code></pre>
<h2>Description</h2>
<p>The popt library exists essentially for parsing command-line options. It is found superior in many ways when compared to parsing the argv array by hand or using the getopt functions <code>getopt()</code> and <code>getopt_long()</code> [see <code><a href="/docs/linux/man/3-getopt/">getopt</a></code>(3)]. Some specific advantages of popt are: it does not utilize global variables, thus enabling multiple passes in parsing <i>argv</i> ; it can parse an arbitrary array of <i>argv</i>-style elements, allowing parsing of command-line-strings from any source; it provides a standard method of option aliasing (to be discussed at length below.); it can exec external option filters; and, finally, it can automatically generate help and usage messages for the application. </p>
<p> Like <code>getopt_long()</code>, the popt library supports short and long style options. Recall that a <code>short option</code> consists of a &#8211; character followed by a single alphanumeric character. A <code>long option</code>, common in GNU utilities, consists of two &#8211; characters followed by a string made up of letters, numbers and hyphens. Long options are optionally allowed to begin with a single -, primarily to allow command-line compatibility between popt applications and X toolkit applications. Either type of option may be followed by an argument. A space separates a short option from its arguments; either a space or an = separates a long option from an argument. </p>
<p> The popt library is highly portable and should work on any POSIX platform. The latest version is distributed with rpm and is always available from: <a href="ftp://ftp.rpm.org/pub/rpm/dist.">ftp://ftp.rpm.org/pub/rpm/dist.</a> </p>
<p> It may be redistributed under the X consortium license, see the file COPYING in the popt source distribution for details.</p>
<h2>Basic Popt Usage</h2>
<h3>1. The Option Table</h3>
<p>Applications provide popt with information on their command-line options by means of an &quot;option table,&quot; i.e., an array of <code>struct poptOption </code> structures: </p>
<p> #include &lt;popt.h&gt; </p>
<pre>struct poptOption {
 const char * longName; /* may be NULL */
 char shortName; /* may be '

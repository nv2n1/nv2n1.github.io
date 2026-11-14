---
title: "getarg(3)"
name: "getarg"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getarg/"
description: "getarg arg_printusage – collect command line options"
---

<h2 class="name">NAME</h2>
<p> <code>getarg</code> <code>arg_printusage</code> &#8211; collect command line options </p>
<h2>SYNOPSIS</h2>
<p> In getarg.h Ft int Fn getarg struct getargs *args size_t num_args int argc char **argv int *optind Ft void Fn arg_printusage struct getargs *args size_t num_args const char *progname const char *extra_string</p>
<h2>DESCRIPTION</h2>
<p> Fn getarg collects any command line options given to a program in an easily used way. Fn arg_printusage pretty-prints the available options, with a short help text. </p>
<p> Fa args is the option specification to use, and it&#8217;s an array of Fa struct getargs elements. Fa num_args is the size of Fa args (in elements). Fa argc and Fa argv are the argument count and argument vector to extract option from. Fa optind is a pointer to an integer where the index to the last processed argument is stored, it must be initialised to the first index (minus one) to process (normally 0) before the first call. </p>
<p> Fa arg_printusage take the same Fa args and Fa num_args as getarg; Fa progname is the name of the program (to be used in the help text), and Fa extra_string is a string to print after the actual options to indicate more arguments. The usefulness of this function is realised only be people who has used programs that has help strings that doesn&#8217;t match what the code does. </p>
<p> The Fa getargs struct has the following elements. </p>
<pre><code>
struct getargs {
    const char *long_name;
    char short_name;
    enum { arg_integer,
           arg_string,
           arg_flag,
           arg_negative_flag,
           arg_strings,
           arg_double,
           arg_collect
    } type;
    void *value;
    const char *help;
    const char *arg_help;
};
</code></pre>
<p> Fa long_name is the long name of the option, it can be <code>NULL</code> if you don&#8217;t want a long name. Fa short_name is the characted to use as short option, it can be zero. If the option has a value the Fa value field gets filled in with that value interpreted as specified by the Fa type field. Fa help is a longer help string for the option as a whole, if it&#8217;s <code>NULL</code> the help text for the option is omitted (but it&#8217;s still displayed in the synopsis). Fa arg_help is a description of the argument, if <code>NULL</code> a default value will be used, depending on the type of the option: </p>
<dl>
<dt><code>arg_integer</code></p>
<dd> the argument is a signed integer, and Fa value should point to an Fa int .</p>
<dt><code>Fa </code>arg_string</p>
<dd> the argument is a string, and Fa value should point to a Fa char* .</p>
<dt><code>Fa </code>arg_flag</p>
<dd> the argument is a flag, and Fa value should point to a Fa int . It gets filled in with either zero or one, depending on how the option is given, the normal case being one. Note that if the option isn&#8217;t given, the value isn&#8217;t altered, so it should be initialised to some useful default.</p>
<dt><code>Fa </code>arg_negative_flag</p>
<dd> this is the same as Fa arg_flag but it reverses the meaning of the flag (a given short option clears the flag), and the synopsis of a long option is negated.</p>
<dt><code>Fa </code>arg_strings</p>
<dd> the argument can be given multiple times, and the values are collected in an array; Fa value should be a pointer to a Fa struct getarg_strings structure, which holds a length and a string pointer.</p>
<dt><code>Fa </code>arg_double</p>
<dd> argument is a double precision floating point value, and Fa value should point to a Fa double .</p>
<dt><code>Fa </code>arg_collect</p>
<dd> allows more fine-grained control of the option parsing process. Fa value should be a pointer to a Fa getarg_collect_info structure:<br />
typedef int (*getarg_collect_func)(int short_opt,<br />
                                   int argc,<br />
                                   char **argv,<br />
                                   int *optind,<br />
                                   int *optarg,<br />
                                   void *data);<br />
typedef struct getarg_collect_info {<br />
    getarg_collect_func func;<br />
    void *data;<br />
} getarg_collect_info;</p>
<p> With the Fa func member set to a function to call, and Fa data to some application specific data. The parameters to the collect function are:</p>
<dl>
<dt><code>Fa </code>short_flag</p>
<dd> non-zero if this call is via a short option flag, zero otherwise</p>
<dt><code>Fa </code>argc , argv</p>
<dd> the whole argument list</p>
<dt><code>Fa </code>optind</p>
<dd> pointer to the index in argv where the flag is</p>
<dt><code>Fa </code>optarg</p>
<dd> pointer to the index in argv[*optind] where the flag name starts</p>
<dt><code>Fa </code>data</p>
<dd> application specific data</dl>
<p> You can modify Fa *optind , and Fa *optarg , but to do this correct you (more or less) have to know about the inner workings of getarg. </p>
<p> You can skip parts of arguments by increasing Fa *optarg (you could implement the &#8211;<code>z </code><i>3</i> set of flags from <code>gzip</code> with this), or whole argument strings by increasing Fa *optind (let&#8217;s say you want a flag &#8211;<code>c </code><i>x y z</i> to specify a coordinate); if you also have to set Fa *optarg to a sane value. </p>
<p> The collect function should return one of <code>ARG_ERR_NO_MATCH , ARG_ERR_BAD_ARG , ARG_ERR_NO_ARG, ENOMEM</code> on error, zero otherwise. </p>
<p> For your convenience there is a function, Fn getarg_optarg , that returns the traditional argument string, and you pass it all arguments, sans data, that where given to the collection function. </p>
<p> Don&#8217;t use this more this unless you absolutely have to.</dl>
<p> Option parsing is similar to what getopt uses. Short options without arguments can be compressed ( &#8211;<code>xyz</code> is the same as &#8211;<code>x y z )</code> and short options with arguments take these as either the rest of the argv-string or as the next option ( &#8211;<code>o </code><i>foo</i> or &#8211;<code>o </code><i>foo</i> </p>
<p> Long option names are prefixed with &#8212; (double dash), and the value with a = (equal), &#8211;<code>-foo= </code><i>bar</i> Long option flags can either be specified as they are ( &#8211;<code>-help</code> or with an (boolean parsable) option ( &#8211;<code>-help= </code><i>yes</i> &#8211;<code>-help= </code><i>true</i> or similar), or they can also be negated ( &#8211;<code>-no-help</code> is the same as &#8211;<code>-help= no</code> and if you&#8217;re really confused you can do it multiple times ( &#8211;<code>-no-no-help= </code><i>false</i> or even &#8211;<code>-no-no-help= </code><i>maybe</i></p>
<h2>EXAMPLE</h2>
<p>#include &lt;getarg.h&gt;<br />
#include &lt;stdio.h&gt;<br />
#include &lt;string.h&gt;<br />
char *source = &#8220;Ouagadougou&#8221;;<br />
char *destination;<br />
int weight;<br />
int include_catalog = 1;<br />
int help_flag;<br />
struct getargs args[] = {<br />
    {&#8220;source&#8221;, &#8216;s&#8217;, arg_string, &amp;source,<br />
     &#8220;source of shippment&#8221;, &#8220;city&#8221;},<br />
    {&#8220;destination&#8221;, &#8216;d&#8217;, arg_string, &amp;destination,<br />
     &#8220;destination of shippment&#8221;, &#8220;city&#8221;},<br />
    {&#8220;weight&#8221;, &#8216;w&#8217;, arg_integer, &amp;weight,<br />
     &#8220;weight of shippment&#8221;, &#8220;tons&#8221;},<br />
    {&#8220;catalog&#8221;, &#8216;c&#8217;, arg_negative_flag, &amp;include_catalog,<br />
     &#8220;include product catalog&#8221;},<br />
    {&#8220;help&#8221;, &#8216;h&#8217;, arg_flag, &amp;help_flag}};<br />
int num_args = sizeof(args) / sizeof(args[0]); /* number of elements in args */<br />
const char *progname = &#8220;ship++&#8221;;<br />
int main(int argc, char **argv)<br />
{<br />
    int optind = 0;<br />
    if (getarg(args, num_args, argc, argv, &amp;optind)) {<br />
        arg_printusage(args, num_args, progname, &#8220;stuff&#8230;&#8221;);<br />
        exit(1);<br />
    }<br />
    if (help_flag) {<br />
        arg_printusage(args, num_args, progname, &#8220;stuff&#8230;&#8221;);<br />
        exit(0);<br />
    }<br />
    if (destination == NULL) {<br />
        fprintf(stderr, &#8220;%s: must specify destination
&#8221;, progname);<br />
        exit(1);<br />
    }<br />
    if (strcmp(source, destination) == 0) {<br />
        fprintf(stderr, &#8220;%s: destination must be different from source
&#8221;);<br />
        exit(1);<br />
    }<br />
    /* include more stuff here &#8230; */<br />
    exit(2);<br />
}</p>
<p> The output help output from this program looks like this: </p>
<pre><code>
$ ship++ --help
        Usage : ship++ [--source = city][-s city][--destination = city][-d city]
                                        [--weight = tons][-w tons][--no - catalog][-c][--help][-h] stuff... -
                s city,
    --source = city source of shippment - d city, --destination = city destination of shippment - w tons, --weight = tons weight of shippment - c, --no - catalog include product catalog
</code></pre>
<h2>BUGS</h2>
<p> It should be more flexible, so it would be possible to use other more complicated option syntaxes, such as what <a href="/docs/linux/man/1-ps/">ps</a>(1), and <a href="/docs/linux/man/1-tar/">tar</a>(1), uses, or the AFS model where you can skip the flag names as long as the options come in the correct order. </p>
<p> Options with multiple arguments should be handled better. </p>
<p> Should be integreated with SL. </p>
<p> It&#8217;s very confusing that the struct you pass in is called getargS.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-getopt/">getopt</a>(3) </p>
<h2>Index</h2>

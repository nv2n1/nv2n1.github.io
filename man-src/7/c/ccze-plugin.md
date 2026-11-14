---
title: "ccze-plugin(7)"
name: "ccze-plugin"
section: "7"
letter: "c"
url: "/docs/linux/man/7-ccze-plugin/"
description: "ccze – A robust log colorizer, plugin infrastructure"
---

<p>ccze &#8211; A robust log colorizer, plugin infrastructure</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ccze.h&gt;</code></pre>
<p> <code>/* Plugin support */</code><br />
 <code>typedef void (*</code><i>ccze_plugin_startup_t</i><code>) (void);</code><br />
 <code>typedef void (*</code><i>ccze_plugin_shutdown_t</i><code>) (void);</code><br />
 <code>typedef int (*</code><i>ccze_plugin_handle_t</i><code>) (const char *</code><i>str</i><code>,</code> <code>size_t </code><i>length</i><code>, char **</code><i>rest</i><code>);</code> <code>CCZE_DEFINE_PLUGIN (</code><i>name</i><code>, </code><i>type</i><code>, </code><i>desc</i><code>);</code><br />
 <code>CCZE_DEFINE_PLUGINS (</code><i>plugins</i><code>&#8230;);</code><br />
 <code>/* Display */</code><br />
 <code>void ccze_addstr (ccze_color_t </code><i>col</i><code>, const char *</code><i>str</i><code>);</code><br />
 <code>void ccze_newline (void);</code><br />
 <code>void ccze_space (void);</code><br />
 <code>void ccze_wordcolor_process_one (char *</code><i>word</i><code>, int </code><i>slookup</i><code>);</code><br />
 <code>/* Helpers */</code><br />
 <code>ccze_color_t ccze_http_action (const char *</code><i>method</i><code>);</code><br />
 <code>void ccze_print_date (const char *</code><i>date</i><code>);</code> <code>/* Command line */</code><br />
 <code>char **ccze_plugin_argv_get (const char *</code><i>name</i><code>);</code><br />
 <code>const char *ccze_plugin_name_get (void);</code></p>
<h2>Description</h2>
<p>This manual page attempts to outline the internals of CCZE plugins: how they work, how they are implemented, and how to add new ones. </p>
<p> There are four required entry points in a plugin: a <i>startup</i>, a <i>shutdown</i> and a <i>handler</i> routine (more on these later), and an informational structure. </p>
<p> The <i>startup</i> function must be of type <code>ccze_plugin_startup_t</code>. This is called right after the module is loaded. Its purpose is to initialise all kinds of module-specific global variables, such as the regular expressions. </p>
<p> The <i>shutdown</i> function is its counterpart: this is used to deallocate any memory reserved by the <i>startup</i> code. </p>
<p> The core part of a plugin is the <i>handler</i>, of type <code>ccze_plugin_handle_t</code>. This does the actual coloring. The string to process is passed in the <i>str</i> argument, its length in <i>length</i>. The third argument, <i>rest</i> is a pointer to a string. Unlike the first two, this argument is used only for output. </p>
<p> When a handler processed a string, it must return a non-zero value, in case it could not process it, the handler must return with zero. If the string could be processed only partially, the part which was deemed unknown by the handler must be passed back in the <i>rest</i> variable. </p>
<p> The fourth part, although the smallest part, is the most important. Without this, the module is useless, it cannot be loaded. This part tells CCZE what the <i>startup</i>, <i>shutdown</i> and <i>handler</i> functions are called. </p>
<p> To encourage good style, the little details of this structure will not be disclosed in this manual page. Instead, the helper macro, <i>CCZE_DEFINE_PLUGIN</i> will be explained. </p>
<p> <i>CCZE_DEFINE_PLUGIN</i> is the macro to use if one wants to make the plugin loadable. Its first argument is an unquoted string: the name of the plugin. The second part is the type of the plugin, it can be <i>FULL</i>, <i>PARTIAL</i> or <i>ANY</i>. The last argument is a short description of the plugin. </p>
<p> It is assumed that the three functions mentioned earlier are called <i>ccze_</i><code>name</code><i>_setup</i>, <i>ccze_</i><code>name</code><i>_shutdown</i> and <i>ccze_</i><code>name</code><i>_handle</i>, respectively. </p>
<p> A <i>FULL</i> plugin is one that accepts raw input, untouched by any other plugin before, and processes it. On the other hand, a <i>PARTIAL</i> plugin relies on previous ones preprocessing the input. For example, <i>syslog</i> is a full plugin, on which <i>ulogd</i>, a partial plugin relies. The <i>syslog</i> plugin processes the raw input from the logfile, adds colour to most of it, save the actual message sent by a process, that is left to subsequent plugins, like <i>ulogd</i>. An <i>ANY</i> plugin is one can act as both other types. </p>
<p> With <i>CCZE_DEFINE_PLUGINS</i> one can place more than one plugin into one shared object. </p>
<p> There are two other helper functions, <i>ccze_plugin_argv_get</i> and <i>ccze_plugin_name_get</i>. One can pass arguments to CCZE plugins, and these is the function to retrieve them. While <i>ccze_plugin_name_get</i> returns the name of the current plugin, <i>ccze_plugin_argv_get</i> returns a NULL-terminated array, with each entry containing an argument.</p>
<h2>Display Methods</h2>
<p>The so-called <i>display methods</i> are the <code>only</code> supported interface to emit something to the display. These handle both the normal, ncurses-based, and the HTML output. This is a kind of abstraction so plugins will not have to worry about the differences between the output formats. </p>
<p> The most important one is <i>ccze_addstr</i>, which takes a color (see <i>ccze.h</i> for a list of supported color tags) and a string, and displays it appropriately. The <i>ccze_space</i> and <i>ccze_newline</i> functions emit a space and a newline, respectively. </p>
<p> Our last function, <i>ccze_wordcolor_process_one</i> passes <code>word</code> to the word colourising engine. If the second argument, <code>slookup</code> is non-zero, the engine will perform service lookups (like <i>getent</i> and friends).</p>
<h2>Helper Methods</h2>
<p>We only have two helper methods: <i>ccze_print_date</i>, which simply prints out the date in the appropriate colour, and <i>ccze_http_action</i>, which given a HTTP <code>method</code>, returns the associated colour, in a format suitable for <i>ccze_addstr</i>.</p>
<h2>Example</h2>
<pre><code>#include &lt;ccze.h&gt;
#include &lt;stddef.h&gt;
#include &lt;string.h&gt;

static char **ccze_foo_argv;

static int
ccze_foo_handle(const char *str, size_t length, char **rest)
{
    int i = 1;

    if (strstr(str, &quot;foo&quot;)) {
        ccze_addstr(CCZE_COLOR_GOODWORD, str);
        return 1;
    }

    while (ccze_foo_argv[i]) {
        if (strstr(str, ccze_foo_argv[i])) {
            ccze_addstr(CCZE_COLOR_GOODWORD, str);
            return 1;
        }
        i++;
    }
    return 0;
}

static void
ccze_foo_startup(void)
{
    ccze_foo_argv = ccze_plugin_argv_get(ccze_plugin_name_get());
}

static void
ccze_foo_shutdown(void)
{
}

CCZE_DEFINE_PLUGIN(foo, PARTIAL, &quot;Partial FOO coloriser.&quot;);</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ccze/">ccze</a></code>(1)</p>
<h2>Author</h2>
<p>ccze was written by Gergely Nagy &lt;algernon [at] bonehunter.rulez.org&gt;, based on colorize by Istvan Karaszi &lt;colorize [at] spam.raszi.hu&gt;.</p>

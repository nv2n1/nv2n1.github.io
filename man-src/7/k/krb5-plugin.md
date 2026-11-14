---
title: "krb5-plugin(7)"
name: "krb5-plugin"
section: "7"
letter: "k"
url: "/docs/linux/man/7-krb5-plugin/"
description: "krb5-plugin – plugin interface for Heimdal"
---

<p><code>krb5-plugin</code> &#8211; plugin interface for Heimdal</p>
<h2>Synopsis</h2>
<p>In krb5.h In krb5/an2ln_plugin.h In krb5/ccache_plugin.h In krb5/db_plugin.h In krb5/kuserok_plugin.h In krb5/locate_plugin.h In krb5/send_to_kdc_plugin.h</p>
<h2>Description</h2>
<p>Heimdal has a plugin interface. Plugins may be statically linked into Heimdal and registered via the krb5_plugin_register3 function, or they may be dynamically loaded from shared objects present in the Heimdal plugins directories. </p>
<p> Plugins consist of a C struct whose struct name is given in the associated header file, such as, for example, <i>krb5plugin_kuserok_ftable</i> and a pointer to which is either registered via krb5_plugin_register3 or found in a shared object via a symbol lookup for the symbol name defined in the associated header file (e.g., &quot;kuserok&quot; for the plugin for krb5_kuserok3 ). </p>
<p> The plugin structs for all plugin types always begin with the same three common fields: </p>
<ol>
<li> <i>minor_version</i> , an int. Plugin minor versions are defined in each plugin type&#8217;s associated header file.
<li> <i>init</i> , a pointer to a function with two arguments, a krb5_context and a void **, returning a krb5_error_code. This function will be called to initialize a plugin-specific context in the form of a void * that will be output through the init function&#8217;s second argument.
<li> <i>fini</i> , a pointer to a function of one argument, a void *, consisting of the plugin&#8217;s context to be destroyed, and returning void. </ol>
<p> Each plugin type must add zero or more fields to this struct following the above three. Plugins are typically invoked in no particular order until one succeeds or fails, or all return a special return value such as KRB5_PLUGIN_NO_HANDLE to indicate that the plugin was not applicable. Most plugin types obtain deterministic plugin behavior in spite of the non-deterministic invokation order by, for example, invoking all plugins for each &quot;rule&quot; and passing the rule to each plugin with the expectation that just one plugin will match any given rule. </p>
<p> There is a database plugin system intended for many of the uses of databases in Heimdal. The plugin is expected to call heim_db_register3 from its <i>init</i> entry point to register a DB type. The DB plugin&#8217;s <i>fini</i> function must do nothing, and the plugin must not provide any other entry points. </p>
<p> The krb5_kuserok plugin adds a single field to its struct: a pointer to a function that implements kuserok functionality with the following form: </p>
<blockquote>
<pre>static krb5_error_code
kuserok(void *plug_ctx, krb5_context context, const char *rule,
 unsigned int flags, const char *k5login_dir,
 const char *luser, krb5_const_principal principal,
 krb5_boolean *result)</pre>
</blockquote>
<p> The <i>luser</i> , <i>principal</i> and <i>result</i> arguments are self-explanatory (see krb5_kuserok3 ). The <i>plug_ctx</i> argument is the context output by the plugin&#8217;s init function. The <i>rule</i> argument is a kuserok rule from the krb5.conf file; each plugin is invoked once for each rule until all plugins fail or one succeeds. The <i>k5login_dir</i> argument provides an alternative k5login file location, if not NULL. The <i>flags</i> argument indicates whether the plugin may call krb5_aname_to_localname3 (KUSEROK_ANAME_TO_LNAME_OK), and whether k5login databases are expected to be authoritative (KUSEROK_K5LOGIN_IS_AUTHORITATIVE). </p>
<p> The plugin for krb5_aname_to_localname3 is named &quot;an2ln&quot; and has a single extra field for the plugin struct: </p>
<blockquote>
<pre>typedef krb5_error_code (*set_result_f)(void *, const char *);
static krb5_error_code
an2ln(void *plug_ctx, krb5_context context, const char *rule,
 krb5_const_principal aname, set_result_f set_res_f, void *set_res_ctx)</pre>
</blockquote>
<p> The arguments for the <i>an2ln</i> plugin are similar to those of the kuserok plugin, but the result, being a string, is set by calling the <i>set_res_f</i> function argument with the <i>set_res_ctx</i> and result string as arguments. The <i>set_res_f</i> function will make a copy of the string.</p>
<h2>Files</h2>
<dl>
<dt><code>libdir/plugin/krb5/* </code></p>
<dd>Shared objects containing plugins for Heimdal.</dl>
<h2>Examples</h2>
<p>An example an2ln plugin that maps principals to a constant &quot;nouser&quot; follows: </p>
<pre><code>#include &lt;krb5/an2ln_plugin.h&gt;

static krb5_error_code
nouser_plug_init(krb5_context context, void **ctx)
{
    *ctx = NULL;
    return 0;
}

static void nouser_plug_fini(void *ctx)
{
}

static krb5_error_code
nouser_plug_an2ln(void *plug_ctx, krb5_context context,
                  const char *rule,
                  krb5_const_principal aname,
                  set_result_f set_res_f, void *set_res_ctx)
{
    krb5_error_code ret;

    if (strcmp(rule, &quot;NOUSER&quot;) != 0)
        return KRB5_PLUGIN_NO_HANDLE;

    ret = set_res_f(set_res_ctx, &quot;nouser&quot;);

    return ret;
}

krb5plugin_an2ln_ftable an2ln = {
    KRB5_PLUGIN_AN2LN_VERSION_0,
    nouser_plug_init,
    nouser_plug_fini,
    nouser_plug_an2ln,
};</code></pre>
<p> An example kuserok plugin that rejects all requests follows. (Note that there exists a built-in plugin with this functionality; see krb5_kuserok3 ). </p>
<pre><code>#include &lt;krb5/kuserok_plugin.h&gt;

static krb5_error_code
reject_plug_init(krb5_context context, void **ctx)
{
    *ctx = NULL;
    return 0;
}

static void reject_plug_fini(void *ctx)
{
}

static krb5_error_code
reject_plug_kuserok(void *plug_ctx, krb5_context context, const char *rule,
                    unsigned int flags, const char *k5login_dir,
                    const char *luser, krb5_const_principal principal,
                    krb5_boolean *result)
{
    if (strcmp(rule, &quot;REJECT&quot;) != 0)
        return KRB5_PLUGIN_NO_HANDLE;

    *result = FALSE;
    return 0;
}

krb5plugin_kuserok_ftable kuserok = {
    KRB5_PLUGIN_KUSEROK_VERSION_0,
    reject_plug_init,
    reject_plug_fini,
    reject_plug_kuserok,
};</code></pre>
<h2>See Also</h2>
<p>krb5_plugin_register3 krb5_kuserok3 krb5_aname_to_localname3 </p>

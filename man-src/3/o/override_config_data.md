---

title: "override_config_data(3)"
name: "override_config_data"
section: "3"
letter: "o"
url: "/docs/linux/man/3-override_config_data/"
description: "override_config_data – Specifies a block of data containing config overrides. Allegro game programming library."
---

<p> override_config_data - Specifies a block of data containing config overrides. Allegro game programming library.  </p>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void override_config_data(const char *data, int length);</code>  </p>
<p> Version of override_config_file() which uses a block of data that has already been read into memory. The length of the block has to be specified in bytes. Example: </p>
<pre><code>   /* Force German as system language, Spanish keyboard map. */
   const char *override_data = &quot;[system]\n&quot;
      &quot;language=DE\n&quot;
      &quot;keyboard=ES&quot;;
   override_config_data(override_data, ustrsize(override_data));
</code></pre>
<p>Note that this function and override_config_file() are mutually exclusive, i.e. calling one will cancel the effects of the other. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-override_config_file/">override_config_file</a></code>(3), <code><a href="/docs/linux/man/3-set_config_data/">set_config_data</a></code>(3) </p>

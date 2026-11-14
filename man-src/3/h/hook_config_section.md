---
title: "hook_config_section(3)"
name: "hook_config_section"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hook_config_section/"
description: "hook_config_section – Hooks a configuration file section with custom handlers. Allegro game programming library."
---

<h2>NAME</h2>
<p> hook_config_section &#8211; Hooks a configuration file section with custom handlers. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void hook_config_section(const char *section,</code> <code>int (*intgetter)(const char *name, int def),</code> <code>const char *(*stringgetter)(const char *name, const char *def),</code> <code>void (*stringsetter)(const char *name, const char *value));</code></p>
<h2>DESCRIPTION</h2>
<p> Takes control of the specified config file section, so that your hook functions will be used to manipulate it instead of the normal disk file access. If both the getter and setter functions are NULL, a currently present hook will be unhooked. Hooked functions have the highest priority. If a section is hooked, the hook will always be called, so you can also hook a &#8216;#&#8217; section: even override_config_file() cannot override a hooked section. Example: </p>
<pre><code>
int decode_encrypted_int(const char *name, int def)
{
    ...
}

const char *decode_encrypted_string(const char *name, const char *def)
{
    ...
}

void encode_plaintext_string(const char *name, const char *value)
{
    ...
}

int main(int argc, char *argv[])
{
    ...
        /* Make it harder for users to tinker with the high scores. */
        hook_config_section("high_scores", decode_encrypted_int,
                            decode_encrypted_string, encode_plaintext_string);
    ...
}
END_OF_MAIN()
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-config_is_hooked/">config_is_hooked</a></code>(3) </p>
<h2>Index</h2>

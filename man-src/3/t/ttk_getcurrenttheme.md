---
title: "ttk_getcurrenttheme(3)"
name: "ttk_getcurrenttheme"
section: "3"
letter: "t"
url: "/docs/linux/man/3-ttk_getcurrenttheme/"
---

Ttk_CreateTheme, Ttk_GetTheme, Ttk_GetDefaultTheme, Ttk_GetCurrentTheme - create and use Tk themes. 

<h2>Synopsis</h2><pre>Ttk_Theme Ttk_CreateTheme(<i>interp</i>, <i>name</i>, <i>parentTheme</i>);
Ttk_Theme Ttk_GetTheme(<i>interp</i>, <i>name</i>);
Ttk_Theme Ttk_GetDefaultTheme(<i>interp</i>);
Ttk_Theme Ttk_GetCurrentTheme(<i>interp</i>);</pre><h2>Arguments</h2><dl COMPACT><dd>Tcl_Interp * <i>interp</i> (in) The Tcl interpreter in which to register/query available themes.
<dd>Ttk_Theme <i>parentTheme</i> (in) Fallback or parent theme from which the new theme will inherit elements and layouts.
<dd>const char * <i>name</i> (in) The name of the theme. 
</dl><h2>Description</h2><h2>See Also</h2>Ttk_RegisterLayout, Ttk_BuildLayout

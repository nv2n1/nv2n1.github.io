---

title: "nisserver-plugin-defs(1)"
name: "nisserver-plugin-defs"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nisserver-plugin-defs/"
---

nisserver-plugin-defs - print default settings for the NIS server plugin

<h2>SYNOPSIS</h2>

 nisserver-plugin-defs [-d <i>domain</i> ] [-m <i>map</i> ] [-s <i>suffix</i> ] 

<h2>DESCRIPTION</h2>

 The <i>nisserver-plugin-defs</i> command produces example configuration entries containing the default settings which the NIS server plugin will use for all maps for which it has built-in defaults, or if a particular map name is specified, for one map. 

<h2>ARGUMENTS</h2>

<dl>
<dt>-d DOMAIN
</dt><dd> By default, <i>nisserver-plugin-defs</i> uses a placeholder for the NIS domain name when it prints example configuration entries. This option allows a particular domain name to be specified.
</dd><dt>-m MAP
</dt><dd> By default, <i>nisserver-plugin-defs</i> prints example configuration entries for all of the maps for which it has built-in defaults. This option can be used to examine the defaults associated with a particular map name.
</dd><dt>-s SUFFIX
</dt><dd> By default, <i>nisserver-plugin-defs</i> uses a placeholder for the base DN under which it expects to find entries which are relevant for the map. This option allows a particular search base to be specified. 
</dd></dl>

<h2>BUGS</h2>

 Probably, but let's hope not. If you find any, please file them in the bug database at <a rel="nofollow" HREF="http://slapi-nis.fedorahosted.org/.">http://slapi-nis.fedorahosted.org/.</a> 

<h2>AUTHOR</h2>

 Nalin Dahyabhai &lt;nalin [at] redhat.com&gt;
